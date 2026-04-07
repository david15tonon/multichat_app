from fastapi import APIRouter

from app.api import auth, conversations, messages, translate


api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(conversations.router)
api_router.include_router(translate.router)
api_router.include_router(messages.router)
