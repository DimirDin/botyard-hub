import { useEffect } from "react";

export function Toast({ message, error, onDone }) {
  useEffect(() => {
    if (!message) return;
    const t = setTimeout(onDone, 2400);
    return () => clearTimeout(t);
  }, [message, onDone]);

  if (!message) return null;
  return <div className={`toast ${error ? "toast--error" : ""}`}>{message}</div>;
}
