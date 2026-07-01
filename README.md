# Binance Futures Trading Bot

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY / SELL Support
- CLI Arguments
- Logging
- Input Validation
- Error Handling

## Installation

```bash
pip install -r requirements.txt
```

## Create .env

```
API_KEY=Your_API_Key
API_SECRET=Your_API_Secret
```

## Run MARKET

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run LIMIT

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```
## Assumptions

- Uses Binance USDT-M Futures Testnet.
- API credentials are stored in a `.env` file.
- LIMIT orders use `GTC` (Good Till Cancelled).
- Quantity and price should follow Binance symbol rules.