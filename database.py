import os
from flask import Flask, session, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from form import NameForm
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SECRET_KEY"] = "okstringlskdksaj"
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    def __repr__(self):
        return '<Role %r>' %self.name
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' %self.username
    
@app.route('/', methods=['GET', 'POST'])  
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('form.html', form=form, name=session.get('name'), known=session.get('known', False))

if __name__ == '__main__':
    app.run(debug=True)
    