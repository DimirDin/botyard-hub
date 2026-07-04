import time

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.config import settings
from app.registry import MODULES
from app.telegram_auth import validate_init_data

app = FastAPI(title="Botyard Hub — API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.domain],
    allow_methods=["*"],
    allow_headers=["*"],
)

TELEGRAM_SEND_MESSAGE = "https://api.telegram.org/bot{token}/sendMessage"

# In-memory throttle — не БД ради одного счётчика на процесс.
_last_feedback_at: dict[int, float] = {}
FEEDBACK_RATE_LIMIT_SEC = 15


class FeedbackIn(BaseModel):
    init_data: str
    message: str = Field(min_length=1, max_length=2000)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/modules")
async def list_modules():
    return MODULES


@app.post("/api/feedback")
async def send_feedback(payload: FeedbackIn):
    user = validate_init_data(payload.init_data)
    tg_id = user.get("tg_id")
    if not tg_id:
        raise HTTPException(401, "initData: no user")

    now = time.monotonic()
    last = _last_feedback_at.get(tg_id, 0)
    if now - last < FEEDBACK_RATE_LIMIT_SEC:
        raise HTTPException(429, "Слишком часто — попробуй через несколько секунд")
    _last_feedback_at[tg_id] = now

    who = f"@{user['username']}" if user.get("username") else (user.get("first_name") or "аноним")
    text = f"📨 Обратная связь из Пункта управления\nОт: {who} (id {tg_id})\n\n{payload.message}"

    async with httpx.AsyncClient(timeout=5.0) as client:
        resp = await client.post(
            TELEGRAM_SEND_MESSAGE.format(token=settings.bot_token),
            json={"chat_id": settings.owner_chat_id, "text": text},
        )
    if not resp.json().get("ok"):
        raise HTTPException(502, "Не удалось отправить сообщение")

    return {"sent": True}
