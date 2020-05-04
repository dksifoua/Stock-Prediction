from stock_price_stream import StockPriceStream

stocks = ['AAPL'] # , 'GOOGL', 'GS', 'MSFT', 'WMT'

stock_streams = [StockPriceStream(name=stock) for stock in stocks]
for stream in stock_streams:
    stream.start()
