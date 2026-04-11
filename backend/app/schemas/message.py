from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.enums import LanguageEnum, MessageStatusEnum, ToneEnum, TranslationStatusEnum


class MessageCreateRequest(BaseModel):
    content: str
    original_language: LanguageEnum
    target_language: LanguageEnum
    tone: ToneEnum


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    sender_id: UUID | None
    content: str
    translated_content: str | None
    status: MessageStatusEnum
    translation_status: TranslationStatusEnum
    tone: ToneEnum
    original_language: LanguageEnum
    target_language: LanguageEnum | None
    created_at: datetime
