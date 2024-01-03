from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Post(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    body: str


postgres_url = "postgresql://postgres:postgres@localhost:5432/flask-sample"
engine = create_engine(postgres_url, echo=True)
SQLModel.metadata.create_all(engine)
