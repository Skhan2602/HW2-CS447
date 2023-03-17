import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "appdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
class user(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    id = db.Column(db.string(4),unique=True)
    points = db.Column(db.string(3))

    def __repr__(self):
        return "<name: {}>".format(self.name)

@app.route('/', methods=["GET", "POST"])
def home():
    name = None
    if request.form:
        try:
            name = name(name=request.form.get("name"))
            db.session.add(name)
            db.session.commit()
        except Exception as e:
            print("Failed to add name")
            print(e)
    user = user.query.all()
    return render_template("user.html", user=user)

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    user = user.query.filter_by(name=name).first()
    db.session.delete(user)
    db.session.commit()