from decouple import config

import redis
import sys
import json

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=config("HOST"),
            port=config("PORT"),
            password=config("PASSWORD"),
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError!")
        sys.exit(1)

###
# Adicionar dados ao restro
rc = redis_connect()

rc.set('binance_data', json.dumps({'EURUSD': 19876, 'Valor': 5000}))
