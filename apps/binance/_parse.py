from .models import Market, AllTickerParseExample


# Constants
BINANCE_MARKET = 'binance'


def parse_all_tickers():

    # Get a marker object with existing json data
    all_tickers = Market.objects.get(market=BINANCE_MARKET).all_tickers

    if len(all_tickers) > 0:

        print('{0} count of ticker pairs to be parsed'.format(len(all_tickers)))

        # Iterate through all pairs
        for ticker in all_tickers:

            # Add each ticker data into the AllTickerParseExample table
            obj, created = AllTickerParseExample.objects.update_or_create(
                symbol=ticker['symbol'],
                defaults={
                    'price': ticker['price']
                }
            )
    else:
        print('Something went wrong for {0} market'.format(BINANCE_MARKET))


def run():

    print('1. Parse data process started')
    parse_all_tickers()
    print('2. Parse data process completed')
