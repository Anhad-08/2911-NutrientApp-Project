from db import db
from models import User
from app import app
import csv


def GetUser():
    with open("./data/users.csv", "r") as f:
        data = csv.DictReader(f)
        for each in data:
            obj = User(
                name=each["name"],
                password=each["password"]
            )
            db.session.add(obj)
    db.session.commit()


def LoadData():
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        GetUser()
        # OPTIONAL: create a test user
        test = User(name="anhad", password="123")
        db.session.add(test)
        db.session.commit()

if __name__ == "__main__":
    LoadData()
    app.run(debug=True, port=8888)
