import uuid

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import LanguageEnum, ToneEnum


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    preferred_language: Mapped[LanguageEnum] = mapped_column(Enum(LanguageEnum), default=LanguageEnum.FR, nullable=False)
    preferred_tone: Mapped[ToneEnum] = mapped_column(Enum(ToneEnum), default=ToneEnum.STANDARD, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_online: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    conversation_links = relationship("ConversationParticipant", back_populates="user", cascade="all, delete-orphan")
    messages = relationship("Message", back_populates="sender")
