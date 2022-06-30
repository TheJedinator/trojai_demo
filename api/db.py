import os
from fastapi import HTTPException
from sqlmodel import SQLModel, create_engine
from models import Book, Reader, BookReader
from sqlmodel import Session, select

engine = None


def get_engine():
    global engine
    postgres_db = os.environ.get("POSTGRES_DB", "postgresql://user:example@localhost:5432/trojai")
    try:
        if engine is None:

            engine = create_engine(postgres_db, pool_size=30, max_overflow=10, pool_timeout=10)
            return engine
        else:
            return engine
    except Exception as e:
        print(f"Failed to get engine {e}")
        if engine:
            engine.dispose()
        raise HTTPException(detail="Internal Server Error - Database Down", status_code=500)


def _create_demo_data():
    session = Session(engine)
    stmt = select(Book)
    books = session.exec(stmt).fetchall()
    if not books:
        book_1 = Book(title="The Lord of the Rings", price=19.99, isbn="978-0-395-19395-8", summary="A great book")
        book_2 = Book(title="The Hobbit", price=8.99, isbn="978-0-395-19395-8", summary="A great book")
        book_3 = Book(title="The Catcher in the Rye", price=8.99, isbn="978-0-395-19395-8", summary="A great book")
        book_4 = Book(title="The Grapes of Wrath", price=8.99, isbn="978-0-395-19395-8", summary="A great book")
        book_5 = Book(title="The Great Gatsby", price=8.99, isbn="978-0-395-19395-8", summary="A great book")

        reader_1 = Reader(name="John Doe", age=42)
        reader_2 = Reader(name="Jane Doe", age=43)
        reader_3 = Reader(name="Jack Doe", age=44)
        reader_4 = Reader(name="Jill Doe", age=45)
        reader_5 = Reader(name="Jana Doe", age=46)

        session.add_all(
            [
                book_1,
                book_2,
                book_3,
                book_4,
                book_5,
                reader_1,
                reader_2,
                reader_3,
                reader_4,
                reader_5,
            ]
        )
        session.commit()
        session.refresh(book_1)
        session.refresh(book_2)
        session.refresh(book_3)
        session.refresh(book_4)
        session.refresh(book_5)
        session.refresh(reader_1)
        session.refresh(reader_2)
        session.refresh(reader_3)
        session.refresh(reader_4)
        session.refresh(reader_5)

        book_reader_1 = BookReader(book=book_1.id, reader=reader_1.id, rating=2, review="This is not the worst book")  # type: ignore
        book_reader_2 = BookReader(book=book_2.id, reader=reader_2.id, rating=5, review="This is a great book")  # type: ignore
        book_reader_3 = BookReader(book=book_3.id, reader=reader_3.id, rating=4, review="This is a satisfactory book")  # type: ignore
        book_reader_4 = BookReader(book=book_4.id, reader=reader_4.id, rating=3, review="This is a meh book")  # type: ignore
        book_reader_5 = BookReader(book=book_5.id, reader=reader_5.id, rating=1, review="This is a crappy book")  # type: ignore
        session.add_all([book_reader_1, book_reader_2, book_reader_3, book_reader_4, book_reader_5])
        session.commit()
        session.close()
