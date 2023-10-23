from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    body: str
