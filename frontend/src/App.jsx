import { useEffect, useState } from "react";
import { ModuleRow } from "./components/ModuleRow";
import { CommsPanel } from "./components/CommsPanel";
import { Toast } from "./components/Toast";
import { api } from "./lib/api";
import { ready } from "./lib/telegram";

export default function App() {
  const [tab, setTab] = useState("modules");
  const [modules, setModules] = useState(null);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    ready();
    api.modules().then(setModules).catch(() => setModules([]));
  }, []);

  return (
    <>
      <header className="deck-header">
        <div className="deck-header__title">
          <span className="deck-header__dot" />
          botyard // control deck
        </div>
        <div className="deck-header__count">
          <span>{modules?.length ?? "…"}</span> модулей в сети
        </div>
      </header>

      <nav className="deck-tabs">
        <button
          className={`deck-tab ${tab === "modules" ? "deck-tab--active" : ""}`}
          onClick={() => setTab("modules")}
        >
          🎛 модули
        </button>
        <button
          className={`deck-tab ${tab === "comms" ? "deck-tab--active" : ""}`}
          onClick={() => setTab("comms")}
        >
          📡 связь
        </button>
      </nav>

      <div className="page">
        {tab === "modules" && (
          <>
            {!modules && <div className="state-empty">⠋ загрузка...</div>}
            {modules?.length === 0 && <div className="state-empty">модули не найдены</div>}
            {modules?.map((m) => (
              <ModuleRow key={m.slug} mod={m} />
            ))}
          </>
        )}

        {tab === "comms" && <CommsPanel onResult={setToast} />}
      </div>

      <Toast message={toast?.message} error={toast?.error} onDone={() => setToast(null)} />
    </>
  );
}
