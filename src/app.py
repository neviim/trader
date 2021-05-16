from flask import Flask, jsonify
from datetime import datetime
from decouple import config

import redis
import time
import json
import sys

###
# Altentica no banco redis.
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

### Get vela
#
def getVela(id):
    time.sleep(2)
    return {
        "id": id,
        "name": "EURUSD",
        "dta_inicial": str(datetime.now())
    }

###
# Get catecoria
def getCategorias():
    time.sleep(2)
    return [
        {"id": 1, "pares": "EURUSD"},
        {"id": 2, "pares": "JAPUSD"},
        {"id": 3, "pares": "BTCUSD"}
    ]


###
# Server flask
app = Flask(__name__)

rc = redis_connect()

@app.route('/', methods=['GET'])
def index():

    if rc.get('dt') == None:
        rc.set('dt', str(datetime.now()), ex=3)
    return rc.get('dt')

@app.route('/delete-key', methods=['GET'])
def deletekey():
    rc.delete('dt')
    return 'Ok'

@app.route('/velas/<id>', methods=['GET'])
def getVelaById(id):
    key = "vela:" + id
    if rc.get(key) == None:
        vela = getVela(id)
        rc.set(key, json.dumps(vela), ex=3)
    return jsonify(json.loads(rc.get(key)))

@app.route('/categorias', methods=['GET'])
def getAllCategorias():
    key = "categorias"
    if rc.get(key) == None:
        categorias = getCategorias()
        rc.set(key, json.dumps(categorias), ex=3)
    return jsonify(json.loads(rc.get(key)))