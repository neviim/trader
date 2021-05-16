from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return str(datetime.now())

