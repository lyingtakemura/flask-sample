from flask import Flask, request
from sqlmodel import Session, select

from models import Post, engine

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def posts():
    if request.method == "GET":
        with Session(engine) as session:
            statement = select(Post)
            result = session.exec(statement).all()
            return [obj.model_dump() for obj in result]

    if request.method == "POST":
        obj = request.get_json()
        post = Post(body=obj.get("body"))
        with Session(engine) as session:
            session.add(post)
            session.commit()
            session.refresh(post)
            return post.model_dump()


@app.route("/<id>/", methods=["GET", "DELETE"])
def post(id):
    if request.method == "GET":
        with Session(engine) as session:
            try:
                statement = select(Post).where(Post.id == id)
                result = session.exec(statement).one()
                return result.model_dump()
            except:
                return {"response": "NOT_FOUND"}

    if request.method == "DELETE":
        with Session(engine) as session:
            try:
                statement = select(Post).where(Post.id == id)
                obj = session.exec(statement).one()
                session.delete(obj)
                session.commit()
                return {"response": "DELETED"}
            except:
                return {"response": "OBJECT NOT FOUND"}


if __name__ == "__main__":
    app.run(debug=True)
