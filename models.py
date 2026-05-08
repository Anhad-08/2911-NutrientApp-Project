from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False, unique=True)
    password = mapped_column(String(200), nullable=False)




# from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, DateTime 
# from sqlalchemy.orm import mapped_column, relationship
# from db import db
# from sqlalchemy.sql import functions as func
# from flask_login import UserMixin

# class User(db.Model, UserMixin):
#     id = mapped_column(Integer, primary_key=True) 
#     name = mapped_column(String(200), nullable=False, unique=True) 
#     phone = mapped_column(String(20), nullable=False)
#     height = mapped_column(Float, nullable=False) 
#     weight = mapped_column(Float, nullable=False)
#     gender = mapped_column(String(20), nullable=False)
#     age = mapped_column(Integer, nullable=False)
#     tdee = mapped_column(Float, nullable=True, default=2000)
#     password = mapped_column(String(200), nullable=False)
#     # meals = relationship("Meal")

#     def getTotalMacros(self):
#         fat = 0
#         protein = 0
#         carbs = 0
#         calories = 0
#         for each in self.meals:
#             macros = each.getMacros()
#             fat += macros["fat"]
#             protein += macros["protein"]
#             carbs += macros["carbs"]
#             calories += macros["calories"]
#         return {"fat": fat, "protein": protein, "carbs": carbs, "calories": calories}



# # if user input about 2 eggs, that quantity will automatically be converted to 2*50g