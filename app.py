from flask import *
from db import db
from models import *
from pathlib import Path
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import select

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretAgileCourse"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.instance_path = Path(".").resolve()

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addnew")
def add_new():
    return render_template("addnew.html")

@app.route("/users")
def users_list():
    return "Users list page coming soon"


@app.route("/food")
def food_list():
    return "Food list page coming soon"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginpost", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    statement = select(User).where(User.name == username, User.password == password)
    records = db.session.execute(statement)
    user = records.scalars().first()

    if not user:
        flash("Invalid username or password")
        return redirect(url_for("login"))
    login_user(user)
    return redirect(url_for("user_info", user_id=user.id))

@app.route("/user/<int:user_id>")
def user_info(user_id):
    user = db.session.get(User, user_id)
    return render_template("user_info.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)@app.route("/users")


