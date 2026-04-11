import uuid
from datetime import datetime

from sqlalchemy import Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import LanguageEnum, MessageStatusEnum, ToneEnum, TranslationStatusEnum


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, index=True)
    sender_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)

    content: Mapped[str] = mapped_column(Text, nullable=False)
    original_language: Mapped[LanguageEnum] = mapped_column(Enum(LanguageEnum), nullable=False)
    translated_content: Mapped[str | None] = mapped_column(Text, nullable=True)
    target_language: Mapped[LanguageEnum | None] = mapped_column(Enum(LanguageEnum), nullable=True)
    tone: Mapped[ToneEnum] = mapped_column(Enum(ToneEnum), nullable=False)
    status: Mapped[MessageStatusEnum] = mapped_column(Enum(MessageStatusEnum), default=MessageStatusEnum.SENDING, nullable=False)
    translation_status: Mapped[TranslationStatusEnum] = mapped_column(Enum(TranslationStatusEnum), default=TranslationStatusEnum.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False, index=True)

    conversation = relationship("Conversation", back_populates="messages")
    sender = relationship("User", back_populates="messages")
