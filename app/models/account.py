from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .common.base import Base
from .profile import Profile

class Account(Base):
    __tablename__ = 'account'

    id = mapped_column(Integer, primary_key = True)

    name = mapped_column(String(100))
    email = mapped_column(String(70), unique = True)

    profile: Mapped["Profile"] = relationship()
