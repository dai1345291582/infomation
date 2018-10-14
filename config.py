import logging
import redis
from datetime import timedelta


class Config(object):
    # 密钥
    SECRET_KEY = 'falnaflsnvlnddiengdnflasdmlkadmofelfc'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask_session配置
    # 指定session保存到redis中
    SESSION_TYPE = 'redis'
    # 让cookie中的session_id被加密签名处理
    SESSION_USE_SIGNER = True
    # 使用redis的实例
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置session的有效期
    PERMANENT_SESSION_LIFETIME = timedelta(days=2)


class DevelopementConfig(Config):
    """开发模式下的配置"""
    # 测试
    DEBUG = True

    # 日志级别
    LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产模式下的配置"""
    LEVEL = logging.ERROR


config = {
    'developement': DevelopementConfig,
    'production': ProductionConfig
}
