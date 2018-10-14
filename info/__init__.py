from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config
import redis

# 数据库
db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    app = Flask(__name__)
    # 配置
    app.config.from_object(config[config_name])
    # 配置数据库 关联app
    db.init_app(app)
    # 配置reids
    redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # CSRFProtect保护app
    CSRFProtect(app)
    Session(app)

    return app
