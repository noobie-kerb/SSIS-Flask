from flask import Flask 
from flask_bootstrap import Bootstrap 
from config import secretKey, databaseHost, databaseName, databasePassword, databaseUser, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL

mysql = MySQL()
bootstrap = Bootstrap()

def initialize_app():
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = secretKey,
        MYSQL_USER=  databaseUser,
        MYSQL_PASSWORD=databasePassword,
        MYSQL_DB=databaseName,
        MYSQL_HOST=databaseHost,
        BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .user import user_bp as user_blueprint
    app.register_blueprint(user_blueprint)

    return app