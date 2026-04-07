# Import models to register them with Base.metadata
from app.models.base import Base
from app.models.user import User
from app.models.conversation import Conversation, ConversationParticipant
from app.models.message import Message

__all__ = ["Base", "User", "Conversation", "ConversationParticipant", "Message"]
