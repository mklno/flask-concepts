from flask import Flask, render_template
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


@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("form.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)
