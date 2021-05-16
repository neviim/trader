from decouple import config

import redis
import sys
import json
import time

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

rc = redis_connect()

###
# Adicionar dados para cache
rc.set('binance_data', json.dumps({'EURUSD': 19876, 'Valor': 5000}))

###
# Semelhante a forma de cima
rc.mset({'EURUSD': 5000, 'JAPUSD': 7000})
# print(rc.get('EURUSD'))
# print(rc.get('JAPUSD'))

###
# Grava cache de 1s, apos isso o apaga
rc.psetex('EURUSD', 1000, 'Put')
print(rc.get('EURUSD'))

time.sleep(2)

print(rc.get('EURUSD'))