from flask import Flask, request
from models import PostModel, engine
from schemas import PostSchema
from sqlalchemy import select
from sqlalchemy.orm import Session

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def posts():
    if request.method == "GET":
        with Session(engine) as session:
            query = select(PostModel)
            rows = session.scalars(query).all()
            return [row.serialize() for row in rows]
    if request.method == "POST":
        payload = PostSchema(**request.get_json())
        row = PostModel(id=payload.id, body=payload.body)
        with Session(engine) as session:
            session.add(row)
            session.commit()
        return payload.model_dump()


@app.route("/<id>/", methods=["GET", "DELETE"])
def post(id):
    if request.method == "GET":
        with Session(engine) as session:
            row = session.scalar(select(PostModel).where(PostModel.id == id))
            return row.serialize()
    if request.method == "DELETE":
        with Session(engine) as session:
            try:
                row = session.scalar(select(PostModel).where(PostModel.id == id))
                session.delete(row)
                session.commit()
                return "200"
            except:
                return "Object with provided id does not exist"


if __name__ == "__main__":
    app.run(debug=True)
