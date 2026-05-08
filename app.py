from flask import *

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)@app.route("/users")


