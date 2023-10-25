from schemas import PostSchema
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PostModel(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String())

    def serialize(self):
        keys = self.__table__.columns.keys()
        result = {}
        for key in keys:
            result[key] = getattr(self, key)
        return PostSchema(**result).model_dump()


engine = create_engine("sqlite:///sqlite.db", echo=True)
Base.metadata.create_all(engine)
