from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import BaseModel

if TYPE_CHECKING:
    from users.models import User


class Ad(BaseModel):
    title: Mapped[str] = mapped_column(String(128), index=True)
    description: Mapped[str] = mapped_column(String(256), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    user: Mapped["User"] = relationship(back_populates="users", lazy="selectin")
