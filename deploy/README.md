# Деплой botyard-hub на VPS платформы

Порт `3016` (следующий свободный после 3015, см. §6 MASTER_CONTEXT). Без своей БД —
не нужна ни Postgres, ни Redis.

## Первый деплой

```bash
ssh root@2.26.31.241
mkdir -p /srv/apps/botyard-hub && cd /srv/apps/botyard-hub
git clone https://github.com/DimirDin/botyard-hub.git .

# .env вручную (chmod 600), не в репозитории
cat > .env <<'EOF'
BOT_TOKEN=<токен от @BotFather>
OWNER_CHAT_ID=<личный chat_id владельца>
MINI_APP_URL=https://hub.botyard.site
DOMAIN=https://hub.botyard.site
EOF
chmod 600 .env

docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

# фронтенд собирается отдельно, Caddy раздаёт готовый dist с диска
docker run --rm -v $(pwd)/frontend:/app -w /app node:22-alpine sh -c 'npm ci && npm run build'
```

Добавить блок `deploy/Caddyfile.snippet` в `/etc/caddy/Caddyfile` на сервере (сделать
бэкап файла перед правкой), `caddy reload`. DNS: A-запись `hub` → `2.26.31.241` в Jino,
сверить через DoH-резолвер (не локальный `dig`, см. §7 MASTER_CONTEXT).

## Обновление после правок

```bash
ssh root@2.26.31.241
cd /srv/apps/botyard-hub && git pull

# если менялся backend/ или bot/
docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

# если менялся frontend/
docker run --rm -v $(pwd)/frontend:/app -w /app node:22-alpine sh -c 'npm ci && npm run build'
```

## Проверка

```bash
curl https://hub.botyard.site/health
curl -sI https://hub.botyard.site/ | head -1
```

## Добавление нового бота в хаб

Реальный бот в проде на платформе → добавить объект в `backend/app/registry.py`
(`slug`, `name`, `emoji`, `desc`, `username` — Telegram-юзернейм бота без `@`). Не
добавлять боты со статусом «дизайн утверждён»/«в разработке» без рабочего инстанса —
кнопка будет вести в никуда.
