# 🤖 Binance Futures Trading Bot (CLI + Testnet)

This is a command-line trading bot built for **Binance USDT-M Futures**. It allows you to place various types of orders — from basic market/limit to advanced strategies like Stop-Limit, OCO, TWAP, and Grid trading. It's modular, testnet-friendly (no real funds required), and logs everything it does.

---

##  What It Can Do

- Place **Market** and **Limit** orders via CLI
-  Use **Stop-Limit** to trigger limit orders when a price is hit
-  Set up **OCO** (One-Cancels-the-Other) with stop-loss and take-profit
-  Execute **TWAP** — break large orders into smaller ones over time
-  Run a **Grid Strategy** — auto buy low/sell high in a price range
-  All operations run on Binance’s **Futures Testnet**
-  Saves all logs (success, errors, executions) to `bot.log`

---

##  Folder Structure
your-github-repo/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── logger.py
│   ├── validate.py
│   └── advanced/
│       ├── stop_limit.py
│       ├── oco.py
│       ├── twap.py
│       └── grid_strategy.py
├── .env                   ← contains demo keys
├── bot.log
├── requirements.txt
├── README.md
├── report.pdf             ← add screenshots, explanation


---

## ⚙️ How to Set It Up

1. **Clone the repo and install dependencies**:

```bash
git clone https://github.com/yourusername/yourname-binance-bot.git
cd yourname-binance-bot
pip install -r requirements.txt


###Add your API keys in a .env file (testnet keys or dummy values):

BINANCE_API_KEY=your_testnet_key
BINANCE_SECRET_KEY=your_testnet_secret

###How to Use It (Examples)
# Market order
python src/market_orders.py BTCUSDT BUY 0.01

# Limit order
python src/limit_orders.py BTCUSDT SELL 0.01 29500

# Stop-Limit
python src/advanced/stop_limit.py BTCUSDT BUY 0.01 29100 29200

# OCO Order
python src/advanced/oco.py BTCUSDT SELL 0.01 29700 29300

# TWAP Strategy
python src/advanced/twap.py BTCUSDT BUY 0.05 --intervals 5 --delay 10

# Grid Strategy
python src/advanced/grid_strategy.py BTCUSDT BUY 0.01 28500 29500 5
