from sqlmodel import Field, SQLModel, Relationship
from typing import List
from enum import Enum
from datetime import datetime, timezone

class UserCreate(SQLModel):
    username: str
    email: str
    password: str

class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    books: List["Book"] = Relationship(back_populates="user")

class BookStatus(str, Enum):
    READ = "read"
    READING = "reading"
    WANT_TO_READ = "want to read"

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    author: str
    cover: str
    status: BookStatus = Field(default=BookStatus.WANT_TO_READ)
    pages: int | None=None
    rating: int | None = Field(default=None, ge=1, le=5)
    user_id: int | None = Field(default=None, foreign_key="user.id", index=True)
    user: User | None = Relationship(back_populates="books")
    notes: List["Note"] = Relationship(back_populates="book")

def get_utc_now():
    return datetime.now(timezone.utc)

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str | None=None
    page: int
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)
    book_id: int = Field(foreign_key="book.id", index=True)
    book: Book | None = Relationship(back_populates="notes")