"""HMAC-валидация Telegram WebApp initData — тот же алгоритм, что в botyard-baza/backend/app/gate.py."""
import hashlib
import hmac
import json
import time
from urllib.parse import parse_qsl

from fastapi import HTTPException

from app.config import settings


def validate_init_data(init_data: str) -> dict:
    parsed = dict(parse_qsl(init_data))
    received_hash = parsed.pop("hash", None)
    if not received_hash:
        raise HTTPException(401, "initData: missing hash")

    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed.items()))
    secret_key = hmac.new(b"WebAppData", settings.bot_token.encode(), hashlib.sha256).digest()
    computed_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    if not hmac.compare_digest(computed_hash, received_hash):
        raise HTTPException(401, "initData: invalid signature")

    auth_date = int(parsed.get("auth_date", 0))
    if time.time() - auth_date > 3600:
        raise HTTPException(401, "initData: expired (>1h)")

    user = json.loads(parsed["user"]) if "user" in parsed else {}
    return {"tg_id": user.get("id"), "username": user.get("username"), "first_name": user.get("first_name")}
