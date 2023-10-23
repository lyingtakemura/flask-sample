from flask import Flask, request

app = Flask(__name__)

db = {"posts": []}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return db["posts"]
    if request.method == "POST":
        db["posts"].append(request.get_json())
        return db["posts"]


if __name__ == "__main__":
    app.run(debug=True)
