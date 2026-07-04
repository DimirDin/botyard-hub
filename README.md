# botyard-hub — Пункт управления

Хаб-бот платформы [botyard.site](https://botyard.site): один Mini App с переходами во
все действующие боты платформы + канал обратной связи напрямую владельцу.

- Backend: FastAPI, без БД (реестр модулей — `backend/app/registry.py`, статика)
- Bot: aiogram 3, `/start` открывает Mini App
- Frontend: React 18 + Vite, дизайн «Пункт управления» (control deck)

См. `CLAUDE.md` для команд разработки и `deploy/README.md` для деплоя на VPS платформы.
