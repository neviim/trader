from binance import ThreadedWebsocketManager
from decouple import config

api_key = config('BINANCEKEY')
api_secret = config('BINANCECHAVESECRETA')

def main():

    symbol = 'BNBBTC'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

    # multiple sockets can be started
    twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['BNBBTC@miniTicker', 'BNBBTC@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)


if __name__ == "__main__":
   main()