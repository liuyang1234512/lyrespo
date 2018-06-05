import os

# 设置上传文件存放的位置
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

# 指定静态资源文件路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(STATIC_DIR, 'uploads')

class Config():
    ENV = 'development'
    DEBUG = True

    #数据库的配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@127.0.0.1:3306/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #设置session相关的参数
    SECRET_KEY = '%^&*$#@&**'



