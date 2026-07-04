const tg = typeof window !== "undefined" ? window.Telegram?.WebApp : null;

export function getInitData() {
  return tg?.initData || "";
}

export function ready() {
  tg?.ready();
  tg?.expand();
}

export function openBot(username) {
  const url = `https://t.me/${username}`;
  if (tg?.openTelegramLink) {
    tg.openTelegramLink(url);
  } else {
    window.open(url, "_blank");
  }
}

export function hapticImpact(style = "light") {
  tg?.HapticFeedback?.impactOccurred(style);
}

export function hapticSuccess() {
  tg?.HapticFeedback?.notificationOccurred("success");
}

export function hapticError() {
  tg?.HapticFeedback?.notificationOccurred("error");
}
