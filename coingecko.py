import os
import logging
import http.client
import re
import time
from decimal import Decimal as D
from datetime import datetime
from decimal import ROUND_DOWN  # Import rounding mode
import asyncio

# ----- Enable Full Debugging -----
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Increase debugging for third-party libraries
logging.getLogger("telethon").setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.DEBUG)
http.client.HTTPConnection.debuglevel = 1
# ---------------------------------


# Function to get the full list of coins from CoinGecko
def get_coingecko_coin_list():
    logger.debug("Fetching coin list from CoinGecko")
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url)
        logger.debug(f"CoinGecko coin list response status: {response.status_code}")
        if response.status_code == 200:
            coin_list = response.json()
            logger.debug(f"CoinGecko coin list retrieved, count: {len(coin_list)}")
            return coin_list
        else:
            logger.error(f"Error fetching CoinGecko coin list: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error fetching CoinGecko coin list: {e}")
        return None

# Function to get market cap from CoinGecko
def get_market_cap_from_coingecko(symbol, coin_list):
    logger.debug(f"Fetching market cap from CoinGecko for symbol: {symbol}")
    try:
        coin_id = next((coin['id'] for coin in coin_list if coin['symbol'].lower() == symbol.lower()), None)
        if not coin_id:
            logger.error(f"CoinGecko ID for {symbol} not found.")
            return None

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        response = requests.get(url)
        logger.debug(f"CoinGecko market cap response status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            market_cap = D(data['market_data']['market_cap']['usd'])
            logger.debug(f"Market cap from CoinGecko for {symbol}: {market_cap}")
            return market_cap
        else:
            logger.error(f"Error fetching market cap from CoinGecko: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error fetching market cap from CoinGecko for {symbol}: {e}")
        return None

# Function to perform "market cap show" operations
async def marketcap_retrieve_operations(ticker):
    logger.debug(f"Entering marketcap_retrieve_operations with ticker: {ticker}")
    base_currency = ticker.split("_")[0]
    logger.debug(f"Base currency extracted: {base_currency}")

    # Get market cap from CoinGecko
    coin_list = get_coingecko_coin_list()
    if coin_list:
        market_cap_gecko = get_market_cap_from_coingecko(base_currency, coin_list)
        if market_cap_gecko is not None:
            logger.info(f"Market cap of {base_currency} from CoinGecko: {market_cap_gecko} USD")
        else:
            logger.error(f"Failed to retrieve market cap from CoinGecko for {base_currency}")
    else:
        logger.error("CoinGecko coin list could not be retrieved.")



