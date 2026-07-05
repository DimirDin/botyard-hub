"""
Реестр модулей (ботов) платформы botyard.site — см. §6 MASTER_CONTEXT.md.

Статика, не БД: намеренно, чтобы не поднимать Postgres ради шести строк,
которые меняются раз в несколько недель, когда выходит новый бот. Список
редактируется вручную при добавлении нового бота в проду.

Показываем только реально задеплоенные боты (статус «в проде» в реестре
платформы) — «дизайн утверждён» без рабочего инстанса сюда не идёт, иначе
кнопка ведёт в никуда.
"""

MODULES = [
    {
        "slug": "career-check",
        "name": "CareerCheck",
        "emoji": "💼",
        "desc": "Разбор резюме и карьерные рекомендации.",
        "username": "CareerCheck_Bot",
    },
    {
        "slug": "loan",
        "name": "Кредитный калькулятор",
        "emoji": "🏦",
        "desc": "Расчёт кредита и советы по досрочному погашению.",
        "username": "loanbotyardbot",
    },
    {
        "slug": "tarot",
        "name": "AI-таро",
        "emoji": "🔮",
        "desc": "Расклады Таро без внешнего API, офлайн-логика.",
        "username": "botyardtarotbot",
    },
    {
        "slug": "cart",
        "name": "Семейный список покупок",
        "emoji": "🛒",
        "desc": "Общий список покупок для группы/семьи.",
        "username": "botyardcartbot",
    },
    {
        "slug": "relay",
        "name": "Кривой телефон",
        "emoji": "🎨",
        "desc": "Групповая рисовалка-эстафета в стиле скетчбука.",
        "username": "botyardrelaybot",
    },
    {
        "slug": "baza",
        "name": "Baza без воды",
        "emoji": "📚",
        "desc": "Энциклопедия по Claude Code / Claude.ai / API.",
        "username": "bazadry_bot",
    },
    {
        "slug": "habits",
        "name": "Трекер привычек",
        "emoji": "✅",
        "desc": "Ежедневные привычки, стрики и heatmap выполнения.",
        "username": "botyardhabitsbot",
    },
    {
        "slug": "subs",
        "name": "Трекер подписок",
        "emoji": "💳",
        "desc": "Учёт подписок и напоминания перед списанием.",
        "username": "botyardsubsbot",
    },
    {
        "slug": "trader",
        "name": "Бумажный трейдер",
        "emoji": "📈",
        "desc": "Симулятор биржевой торговли без риска на реальные деньги.",
        "username": "botyardtraderbot",
    },
]
