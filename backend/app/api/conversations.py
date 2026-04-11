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
    import uuid as uuid_lib
    
    conversation = Conversation(is_group=payload.is_group, name=payload.name)
    db.add(conversation)
    await db.flush()

    # Add current user as participant
    db.add(ConversationParticipant(conversation_id=conversation.id, user_id=current_user.id))
    
    # Add other participants if provided
    if payload.participant_ids:
        for participant_id in payload.participant_ids:
            # Ensure participant_id is a UUID
            if isinstance(participant_id, str):
                participant_id = uuid_lib.UUID(participant_id)
            db.add(ConversationParticipant(conversation_id=conversation.id, user_id=participant_id))
    
    await db.commit()
    await db.refresh(conversation)
    return ConversationResponse.model_validate(conversation)


@router.get("/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ConversationResponse:
    """Get conversation details. Verify user is a participant."""
    import uuid
    try:
        conv_uuid = uuid.UUID(conversation_id)
    except ValueError:
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid conversation ID")
    
    # Check that user is a participant
    participant_result = await db.execute(
        select(ConversationParticipant).where(
            (ConversationParticipant.conversation_id == conv_uuid)
            & (ConversationParticipant.user_id == current_user.id)
        )
    )
    if not participant_result.scalar_one_or_none():
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a participant")
    
    conversation_result = await db.execute(select(Conversation).where(Conversation.id == conv_uuid))
    conversation = conversation_result.scalar_one_or_none()
    
    if not conversation:
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    
    return ConversationResponse.model_validate(conversation)



    query = (
        select(Conversation)
        .join(ConversationParticipant, ConversationParticipant.conversation_id == Conversation.id)
        .where(ConversationParticipant.user_id == current_user.id)
    )
    result = await db.execute(query)
    conversations = result.scalars().all()
    return [ConversationResponse.model_validate(item) for item in conversations]
