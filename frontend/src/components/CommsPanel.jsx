import { useState } from "react";
import { api } from "../lib/api";
import { hapticSuccess, hapticError } from "../lib/telegram";

export function CommsPanel({ onResult }) {
  const [text, setText] = useState("");
  const [sending, setSending] = useState(false);

  const handleSend = async () => {
    if (!text.trim() || sending) return;
    setSending(true);
    try {
      await api.sendFeedback(text.trim());
      hapticSuccess();
      onResult({ message: "✓ Сообщение передано" });
      setText("");
    } catch (e) {
      hapticError();
      onResult({ message: e.message || "не удалось передать", error: true });
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="comms-panel">
      <div className="comms-panel__label">📡 канал прямой связи с разработчиком</div>
      <textarea
        className="comms-textarea"
        placeholder="_ опиши баг, идею или просто напиши привет..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button className="comms-send" onClick={handleSend} disabled={sending || !text.trim()}>
        {sending ? "передаю..." : "передать сообщение"}
      </button>
      <div className="comms-hint">Приходит напрямую в Telegram владельцу платформы.</div>
    </div>
  );
}
