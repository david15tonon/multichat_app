import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.conversation import Conversation
from app.models.enums import MessageStatusEnum, TranslationStatusEnum
from app.models.message import Message
from app.models.user import User
from app.schemas.message import MessageCreateRequest
from app.schemas.message import MessageResponse
from app.services.translator import translator_service


router = APIRouter(prefix="/api/messages", tags=["messages"])


@router.post("/{conversation_id}", response_model=MessageResponse)
async def create_message(
    conversation_id: str,
    payload: MessageCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MessageResponse:
    try:
        conversation_uuid = uuid.UUID(conversation_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid conversation id") from exc

    conversation_result = await db.execute(select(Conversation).where(Conversation.id == conversation_uuid))
    conversation = conversation_result.scalar_one_or_none()
    if conversation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

    message = Message(
        conversation_id=conversation_uuid,
        sender_id=current_user.id,
        content=payload.content,
        original_language=payload.original_language,
        target_language=payload.target_language,
        tone=payload.tone,
        status=MessageStatusEnum.SENDING,
        translation_status=TranslationStatusEnum.PENDING,
    )
    db.add(message)

    try:
        translated = translator_service.translate(
            text=payload.content,
            target_language=payload.target_language.value,
            tone=payload.tone.value,
        )
        message.translated_content = translated
        message.status = MessageStatusEnum.SENT
        message.translation_status = TranslationStatusEnum.DONE
    except Exception:
        message.translation_status = TranslationStatusEnum.FAILED

    await db.commit()
    await db.refresh(message)
    return MessageResponse.model_validate(message)
