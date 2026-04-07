from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.conversation import Conversation, ConversationParticipant
from app.models.user import User
from app.schemas.conversation import ConversationCreateRequest, ConversationResponse


router = APIRouter(prefix="/api/conversations", tags=["conversations"])


@router.post("/", response_model=ConversationResponse)
async def create_conversation(
    payload: ConversationCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ConversationResponse:
    conversation = Conversation(is_group=payload.is_group, name=payload.name)
    db.add(conversation)
    await db.flush()

    db.add(ConversationParticipant(conversation_id=conversation.id, user_id=current_user.id))
    await db.commit()
    await db.refresh(conversation)
    return ConversationResponse.model_validate(conversation)


@router.get("/", response_model=list[ConversationResponse])
async def list_my_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[ConversationResponse]:
    query = (
        select(Conversation)
        .join(ConversationParticipant, ConversationParticipant.conversation_id == Conversation.id)
        .where(ConversationParticipant.user_id == current_user.id)
    )
    result = await db.execute(query)
    conversations = result.scalars().all()
    return [ConversationResponse.model_validate(item) for item in conversations]
