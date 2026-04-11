from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.auth import UserResponse


router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/search", response_model=list[UserResponse])
async def search_users(
    q: str = Query(None, min_length=1, description="Search query for email or full name"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[UserResponse]:
    """Search for users by email or full name.
    
    Args:
        q: Search query (searches in email and full_name)
        db: Database session
        current_user: Currently authenticated user
    
    Returns:
        List of matching users (excluding the current user)
    """
    query = select(User).where(User.id != current_user.id)
    
    if q:
        # Search in email or full_name (case-insensitive)
        query = query.where(
            (User.email.ilike(f"%{q}%")) | (User.full_name.ilike(f"%{q}%"))
        )
    
    result = await db.execute(query)
    users = result.scalars().all()
    return users
