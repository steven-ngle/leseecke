from sqlmodel import Field, SQLModel
from enum import Enum
from datetime import datetime, timezone


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
    user_id: int = Field(foreign_key="user.id", index=True)
    
def get_utc_now():
    return datetime.now(timezone.utc)

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str | None=None
    page: int
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)
    book_id: int = Field(foreign_key="book.id", index=True)

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str