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
        "icon": "/icons/career-check.png",
        "desc": "Тесты на определение профессии: находим подходящую сферу и карьерные рекомендации по результатам.",
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
        "name": "taroT",
        "icon": "/icons/tarot.png",
        "desc": "Расклады Таро с толкованием карт под твой вопрос — любовь, карьера, решения.",
        "username": "botyardtarotbot",
    },
    {
        "slug": "cart",
        "name": "Семейный список покупок",
        "icon": "/icons/cart.png",
        "desc": "Общий список покупок для группы/семьи.",
        "username": "botyardcartbot",
    },
    {
        "slug": "relay",
        "name": "Кривой телефон",
        "icon": "/icons/relay.png",
        "desc": "Групповая рисовалка-эстафета в стиле скетчбука.",
        "username": "botyardrelaybot",
    },
    {
        "slug": "baza",
        "name": "Baza без воды",
        "icon": "/icons/baza.png",
        "desc": "Энциклопедия по Claude Code / Claude.ai / API.",
        "username": "bazadry_bot",
    },
    {
        "slug": "habits",
        "name": "Трекер привычек",
        "icon": "/icons/habits.png",
        "desc": "Ежедневные привычки, стрики и heatmap выполнения.",
        "username": "botyardhabitsbot",
    },
    {
        "slug": "subs",
        "name": "Трекер подписок",
        "icon": "/icons/subs.png",
        "desc": "Учёт подписок и напоминания перед списанием.",
        "username": "botyardsubsbot",
    },
    {
        "slug": "trader",
        "name": "Бумажный трейдер",
        "icon": "/icons/trader.png",
        "desc": "Симулятор биржевой торговли без риска на реальные деньги.",
        "username": "botyardtraderbot",
    },
]
