from pydantic import BaseModel, ConfigDict


class ConversationCreateRequest(BaseModel):
    is_group: bool = False
    name: str | None = None


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    is_group: bool
    name: str | None
