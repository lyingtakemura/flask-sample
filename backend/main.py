from flask import Flask, request
from schemas import PostSchema

app = Flask(__name__)

db = {"posts": []}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return [PostSchema(**obj).model_dump() for obj in db["posts"]]
    if request.method == "POST":
        obj = PostSchema(**request.get_json()).model_dump()
        db["posts"].append(obj)
        return obj


if __name__ == "__main__":
    app.run(debug=True)
