from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from db import SQLModel, _create_demo_data, engine, get_engine

from models import Book, BookReader, Reader

SQLModel.metadata.create_all(get_engine())

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


async def get_session():
    with Session(get_engine()) as session:
        yield session


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books")
async def get_books(session: Session = Depends(get_session)):
    try:
        stmt = select(Book)
        books = session.exec(stmt).fetchall()
        if books:
            return books
        else:
            raise HTTPException(detail="Not Found", status_code=404)
    except HTTPException as httpe:
        raise httpe
    except Exception as e:
        print(f"Failed to get books {e}")


@app.get("/readers")
async def get_readers(session: Session = Depends(get_session)):
    try:
        stmt = select(Reader)
        readers = session.exec(stmt).fetchall()
        if readers:
            return readers
        else:
            raise HTTPException(detail="Not Found", status_code=404)
    except HTTPException as httpe:
        raise httpe
    except Exception as e:
        print(f"Failed to get readers {e}")


@app.get("/readers/{reader_id}/books")
async def get_reader_books(reader_id: int, session: Session = Depends(get_session)):
    try:
        stmt = select(BookReader).where(BookReader.reader == reader_id)
        reader_books = session.exec(stmt).fetchall()
        if reader_books:
            return reader_books
        else:
            raise HTTPException(detail="Not Found", status_code=404)
    except HTTPException as httpe:
        raise httpe
    except Exception as e:
        print(f"Failed to get reader books {e}")


@app.get("/readbooks")
async def get_readbooks(session: Session = Depends(get_session)):
    try:
        stmt = select(BookReader)
        readbooks = session.exec(stmt).fetchall()
        if readbooks:
            return readbooks
        else:
            raise HTTPException(detail="Not Found", status_code=404)
    except HTTPException as httpe:
        raise httpe
    except Exception as e:
        print(f"Failed to get readbooks {e}")


if __name__ == "__main__":
    _create_demo_data()
