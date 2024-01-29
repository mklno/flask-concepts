from flask import Flask, render_template, url_for, session, redirect, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[InputRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "okstringlskdksaj"


# normal view function
@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("form.html", form=form, name=name)


# view function with session
@app.route("/index", methods=["GET", "POST"])
def newIndex():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed the name!')
        session["name"] = form.name.data
        return redirect(url_for("newIndex"))
    return render_template("form.html", form=form, name=session.get("name"))


if __name__ == "__main__":
    app.run(debug=True)
