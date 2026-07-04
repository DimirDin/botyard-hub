# botyard-hub — Claude Code Instructions

Telegram Mini App «Пункт управления» — хаб-бот платформы botyard.site: переходы во
все действующие боты платформы + канал обратной связи напрямую владельцу. Общая
инфраструктура платформы — `MASTER_CONTEXT.md` (хранится вне репозитория, у владельца).

## Архитектура (не менять без явного запроса)
- Backend: FastAPI, порт 3016. **Без БД** — реестр модулей статичный
  (`backend/app/registry.py`), фидбэк уходит напрямую владельцу через Bot API
  `sendMessage`, ничего не сохраняется.
- Bot: aiogram 3, роль минимальная — `/start` открывает Mini App, `setChatMenuButton`.
- Frontend: React 18 + Vite, Telegram Mini App SDK, дизайн «Пункт управления»
  (control deck: тёмная панель, LED-индикаторы, рокер-переключатели табов) —
  эксклюзивный стиль для этого бота, не переносить в другие боты платформы.

## Build & Test
```bash
# backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload --port 3016

# bot
cd bot && pip install aiogram==3.*
python main.py

# frontend
cd frontend && npm install && npm run dev
```

## Code Style
- Python 3.12+, type hints, async для сетевых вызовов
- Не заводить БД/Redis ради этого бота — реестр модулей меняется вручную раз в
  несколько недель, фидбэк не требует персистентности (уходит в личку владельцу)

## Definition of done
1. Работает локально (`docker compose up`)
2. Реестр модулей (`registry.py`) содержит только реально задеплоенные боты платформы
3. `/api/feedback` реально доставляет сообщение в Telegram (проверено вручную)
