from pydantic import BaseModel, ConfigDict

from app.models.enums import LanguageEnum, MessageStatusEnum, ToneEnum, TranslationStatusEnum


class MessageCreateRequest(BaseModel):
    content: str
    original_language: LanguageEnum
    target_language: LanguageEnum
    tone: ToneEnum


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    content: str
    translated_content: str | None
    status: MessageStatusEnum
    translation_status: TranslationStatusEnum
