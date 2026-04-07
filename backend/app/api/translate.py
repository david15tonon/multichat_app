from fastapi import APIRouter, HTTPException, status

from app.schemas.translate import TranslateRequest, TranslateResponse
from app.services.translator import translator_service


router = APIRouter(prefix="/api", tags=["translate"])


@router.post("/translate", response_model=TranslateResponse)
async def translate(payload: TranslateRequest) -> TranslateResponse:
    if not payload.text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text is required")

    translated = translator_service.translate(
        text=payload.text,
        target_language=payload.target_language.value,
        tone=payload.tone.value,
    )
    return TranslateResponse(translated_text=translated)
