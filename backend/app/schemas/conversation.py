from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ConversationCreateRequest(BaseModel):
    is_group: bool = False
    name: str | None = None
    participant_ids: list[UUID] | None = None


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Conversation ID")
    is_group: bool
    name: str | None
