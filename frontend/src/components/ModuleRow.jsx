import { openBot, hapticImpact } from "../lib/telegram";

export function ModuleRow({ mod }) {
  return (
    <div
      className="module-row"
      onClick={() => {
        hapticImpact("light");
        openBot(mod.username);
      }}
    >
      <div className="module-row__socket">{mod.emoji}</div>
      <div className="module-row__body">
        <div className="module-row__name">{mod.name}</div>
        <div className="module-row__desc">{mod.desc}</div>
      </div>
      <div className="module-row__status">
        <span className="module-row__led" />
        <span className="module-row__arrow">→</span>
      </div>
    </div>
  );
}
