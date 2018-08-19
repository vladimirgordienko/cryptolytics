from binance.client import Client
from .models import Market


# Init instance to communicate with remote resource - Binance API
# This instance is created to use public API only (no user, password are provided)
# Python-binance docs: https://python-binance.readthedocs.io/en/latest/overview.html
cl = Client('', '', {"verify": True, "timeout": 30})

# Constants
BINANCE_MARKET = 'binance'


def get_data():

    # Binance market should exist in database (Market)
    # market = Market.objects.get(market=BINANCE_MARKET).filter(status=STATUS_ACTIVE)
    market = Market.objects.get(market=BINANCE_MARKET)

    if market:

        obj, created = Market.objects.update_or_create(
            pk=market.pk,
            defaults={
                'ping': cl.ping(),
                'server_time': cl.get_server_time(),
                'system_status': cl.get_system_status(),
                'exchange_info': cl.get_exchange_info(),
                'all_tickers': cl.get_all_tickers(),
                'orderbook_tickers': cl.get_orderbook_tickers()
            }
        )
    else:
        print('{0} market is not found in configuration or has inactive status'.format(BINANCE_MARKET))


def run():

    print('1. Update process started')
    get_data()
    print('2. Update process completed')
