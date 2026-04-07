from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.enums import LanguageEnum, ToneEnum


class SignupRequest(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    preferred_language: LanguageEnum = LanguageEnum.FR
    preferred_tone: ToneEnum = ToneEnum.STANDARD


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    full_name: str
    preferred_language: LanguageEnum
    preferred_tone: ToneEnum
    is_active: bool
    is_online: bool
