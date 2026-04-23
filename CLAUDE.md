# CLAUDE.md This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SharkBux (SharkBox) is a Telegram Mini App "tap-to-earn" crypto game. Users tap a shark to earn tokens, trade them for TON cryptocurrency, and evolve their shark through 4 levels. The UI is in Arabic (RTL). The frontend is deployed on Vercel; the bot runs on Render free tier.

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot (also starts the HTTP server)
python bot.py
```

The bot requires a `TOKEN` env var (or replace the hardcoded value in `bot.py`). The HTTP server binds to `PORT` env var (default 8080) — required by Render free tier.

## Architecture

**Two-file project** with no build system, no tests, no linting config:

- **`bot.py`** — Single-file Python backend. Runs an aiogram 3.x Telegram bot (long polling) and an aiohttp HTTP server concurrently via `asyncio.gather()`. The HTTP server has one route (`/`) that returns a health string — its only purpose is satisfying Render's port-binding requirement. The `/start` command sends an inline keyboard button that opens the Web App.

- **`index.html`** — Self-contained SPA frontend. No frameworks or build step. All CSS, HTML, and JS in one file. State lives entirely in `localStorage` (key: `shark_elite_data`) — there is no backend database or API for game state. Uses the Telegram Web Apps SDK for haptic feedback and dialogs.

## Key Patterns

- **Page routing**: 5 pages (TAP, TRADE, EVO, TASKS, WALLET) managed by toggling `.active` CSS class on `.page` divs via `navTo()`.
- **Game state**: `{ bal, ton, nrg, lv }` persisted to localStorage on every change. Energy regenerates +2 every 2 seconds via `setInterval`.
- **Evolution system**: 4 beast levels defined in `BEASTS` array. Each level has power multiplier, max energy, and TON cost to unlock.
- **Trading chart**: Candlestick chart rendered with random data, refreshes every 3 seconds. Price drifts randomly around 0.000100. Not real market data.
- **Deployment split**: Frontend on Vercel (`sharkbux-project.vercel.app`), bot on Render. `WEB_APP_URL` in `bot.py` must point to the Vercel deployment.

## Important Notes

- The bot token in `bot.py` is hardcoded and should be moved to an environment variable.
- All game state is client-side and trivially modifiable — no server-side validation exists.
- External image URLs (ibb.co) for beast sprites are embedded directly in the JS `BEASTS` array.
