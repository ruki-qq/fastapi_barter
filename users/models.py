from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import BaseModel

class User(BaseModel):
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(128), index=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(128), index=True)
    last_name: Mapped[str] = mapped_column(String(128), index=True)
    password_hash: Mapped[str] = mapped_column(String(128))

