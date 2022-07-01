import datetime
from typing import List, Optional

from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    __tablename__ = "book"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    price: float
    isbn: str
    summary: str


class Reader(SQLModel, table=True):
    __tablename__ = "reader"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int


class BookReader(SQLModel, table=True):
    __tablename__ = "book_reader"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    book: int = Field(foreign_key="book.id")
    reader: int = Field(foreign_key="reader.id")
    date_read: Optional[datetime.datetime] = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    rating: int
    review: str
