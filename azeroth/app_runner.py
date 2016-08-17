from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from azeroth.config import config

mysql_db = SQLAlchemy()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=config.TEST)