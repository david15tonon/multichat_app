from pydantic import BaseModel

from app.models.enums import LanguageEnum, ToneEnum


class TranslateRequest(BaseModel):
    text: str
    target_language: LanguageEnum
    tone: ToneEnum


class TranslateResponse(BaseModel):
    translated_text: str
