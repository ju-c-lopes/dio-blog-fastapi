from datetime import datetime

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False


class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published_at: datetime | None = None
    published: bool | None = None
