from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.api import api_router
from app.core.database import engine
from app.models import Base


app = FastAPI(title="MultiChat API")

# CORS ouvert pour faciliter la connexion du frontend Vite/Vercel.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/api/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "Backend FastAPI is running"}


app.include_router(api_router)

# Required by Vercel serverless runtime.
handler = Mangum(app)
