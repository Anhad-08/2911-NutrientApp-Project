from flask import *

from sqlalchemy import select
from pathlib import Path
from db import db
from models import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


def updateFoolMealCSV():
    data = "meal_id,food_id,amount"
    for each in FoodMeal.query.all():
        data += f"\n{each.meal_id},{each.food_id},{each.amount}"
    with open("data/foodmeal.csv", "w") as f:
        f.write(data)

def updateMealCSV():
    data = "user_id,name"
    for each in Meal.query.all():
        data += f"\n{each.user_id},{each.name}"
    with open("data/meals.csv", "w") as f:
        f.write(data)
    updateFoolMealCSV()

def updateUsersCSV():
    data = "name,phone,height,weight,gender,age,tdee,password"
    for each in User.query.all():
        data += f"\n{each.name},{each.phone},{each.height},{each.weight},{each.gender},{each.age},{each.tdee},{each.password}"
    with open("data/users.csv", "w") as f:
        f.write(data)

def updateFoodCSV():
    data = "name,calories,protein,fat,carbs"
    for each in Food.query.all():
        data += f"\n{each.name},{each.calories},{each.protein},{each.fat},{each.carbs}"
    with open("data/food.csv", "w") as f:
        f.write(data)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretAgileCourse"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.instance_path = Path(".").resolve()

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addnew")
def add_new():
    return render_template("addnew.html")

@app.route("/users")
def users_list():
    statement = select(User).order_by(User.id)
    records = db.session.execute(statement)
    data = records.scalars().all()
    return render_template("users.html", users = data)

if __name__ == "__main__":
    app.run(debug=True)
