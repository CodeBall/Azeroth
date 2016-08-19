from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from azeroth.config import config

mysql_db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    mysql_db.init_app(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=config.TEST)