# how-to-get-market-cap-from-CoinGecko-without-API

A lightweight Python script that fetches cryptocurrency market capitalization data from CoinGecko’s public API. Designed for easy integration, full debugging, and open-source contributions.

## Features

* Retrieve a full list of coins from CoinGecko
* Look up a coin’s ID by its symbol
* Fetch USD market capitalization for any supported symbol
* Detailed logging at HTTP, library, and application levels
* Async-friendly entrypoint for seamless workflow integration

## Prerequisites

* Python 3.8 or newer
* Internet access

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/how-to-get-market-cap-from-CoinGecko-without-API.git
   cd how-to-get-market-cap-from-CoinGecko-without-API
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

> **requirements.txt** should include:
>
> ```text
> requests>=2.25.0
> telethon>=1.24.0   # optional: for Telegram integration
> ```

## Usage

1. **Import and call the async function**

   ```python
   import asyncio
   from marketcap_retriever import marketcap_retrieve_operations

   async def main():
       # Use format "<symbol>_anytag", e.g. "btc_demo"
       await marketcap_retrieve_operations("eth_demo")

   asyncio.run(main())
   ```

2. **Output**

   * Script logs the USD market cap for the given symbol.
   * Example log:

     ```
     INFO:__main__:Market cap of ETH from CoinGecko: 183456789012.34 USD
     ```

## Configuration

* **Logging Levels**

  * Default: `DEBUG` for full visibility.
  * Adjust in `logging.basicConfig(level=logging.DEBUG)`.

* **Rate Limits**

  * CoinGecko public API allows up to 50 calls/minute.
  * Implement caching or delays for high-frequency calls.

## Function Reference

| Function                                      | Description                                                   |
| --------------------------------------------- | ------------------------------------------------------------- |
| `get_coingecko_coin_list()`                   | Fetches full coin list (ID, symbol, name) from CoinGecko.     |
| `get_market_cap_from_coingecko(symbol, list)` | Finds coin ID by symbol and retrieves its USD market cap.     |
| `marketcap_retrieve_operations(ticker)`       | Async entrypoint: splits ticker, retrieves list, fetches cap. |

## Logging

* Uses Python’s `logging` module at `DEBUG` level.
* HTTP debug via `http.client.debuglevel = 1`.
* Third-party libs (`requests`, `urllib3`, `telethon`) set to `DEBUG`.

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add my feature"`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

Please follow PEP 8 and include tests for new functionality.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
