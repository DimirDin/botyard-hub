import { getInitData } from "./telegram";

async function request(path, options = {}) {
  const res = await fetch(`/api${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export const api = {
  modules: () => request("/modules"),
  sendFeedback: (message) =>
    request("/feedback", {
      method: "POST",
      body: JSON.stringify({ init_data: getInitData(), message }),
    }),
};
