from flask import *

def updateFoolMealCSV():
    data = "meal_id,food_id,amount"

def updateMealCSV():
    data = "user_id,name"

def updateUsersCSV():
    data = "name,phone,height,weight,gender,age,password"

def updateFoodCSV():
    data = "name,calories,protein,fat,carbs"

app = Flask(__name__)