from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return {"message" : "this is test for flask implementation"}

if __name__ == "__main__":
    app.run(debug=True)