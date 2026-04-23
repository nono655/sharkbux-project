# AGENTS.md

## Quick Start

```bash
cp .env.example .env          # fill in TOKEN, PORT, WEB_APP_URL
pip install -r requirements.txt
python bot.py                 # starts bot + HTTP health server
```

No build step, no tests, no linter, no type checker.

## Architecture

- **`bot.py`** — Slim entrypoint. Wires Dispatcher + aiohttp server, calls `asyncio.gather()`.
- **`bot/config.py`** — Loads `TOKEN`, `PORT`, `WEB_APP_URL` from `.env` via python-dotenv. Exits if TOKEN missing.
- **`bot/i18n.py`** — Bilingual string dict (AR/EN). Language detected from `message.from_user.language_code`. Users can override with `/lang`.
- **`bot/handlers.py`** — All aiogram handlers: `/start`, `/help`, `/lang`.
- **`bot/server.py`** — aiohttp health server for Render port-binding requirement.
- **`index.html`** — Self-contained SPA frontend. No frameworks or build step. All game state in `localStorage` (key: `shark_elite_data`). Arabic RTL.

## Bot Commands

| Command | Purpose |
|---------|---------|
| `/start` | Welcome + Web App button (AR or EN based on user language) |
| `/help` | Game instructions (bilingual) |
| `/lang ar` or `/lang en` | Override language preference |

## Gotchas

- **TOKEN is no longer hardcoded.** Must be set in `.env` or env var. `bot/config.py` exits if missing.
- **`PORT` env var required on Render.** Default 8080. Render fails without it.
- **`WEB_APP_URL` must point to the Vercel deployment.** Set in `.env`.
- **No server-side game state.** All balances/energy/levels live in browser localStorage. Trivially forgeable.
- **Frontend is Arabic RTL.** `lang="ar"`, Tajawal/Rajdhani fonts.
- **Beast sprite URLs are external** (ibb.co). No local fallback.
- **Trading chart is fake.** Random noise around 0.000100.

## File Map

| File | Purpose |
|------|---------|
| `bot.py` | Entrypoint: starts bot + health server |
| `bot/config.py` | Env var loading + validation |
| `bot/i18n.py` | Bilingual strings + language detection |
| `bot/handlers.py` | Aiogram command handlers |
| `bot/server.py` | Render health server |
| `index.html` | Full SPA: game UI, chart, localStorage |
| `requirements.txt` | `aiogram`, `aiohttp`, `python-dotenv` |
| `.env.example` | Template for required env vars |
| `CLAUDE.md` | Legacy architecture notes |

## Conventions

- Page routing toggles `.active` on `.page` divs via `navTo()`.
- Game state shape: `{ bal, ton, nrg, lv }`. Saved on every mutation.
- Energy regeneration: `setInterval` +2 every 2s.
- Evolution levels in JS `BEASTS` array (4 entries).
- Bot language preference stored in-memory (`bot/i18n.py:_lang_prefs`). Resets on restart.
