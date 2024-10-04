from config import secretKey, databaseHost, databaseName, databasePassword, databaseUser, BOOTSTRAP_SERVE_LOCAL
from flask import Flask 
from flask_bootstrap import Bootstrap 
from flask_wtf.csrf import CSRFProtect
from mysql.connector import connect, Error

bootstrap = Bootstrap()
csrf=CSRFProtect()

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
    try:
        db = connect(
            host = databaseHost,
            user = databaseUser,
            password = databasePassword,
            database = databaseName
        )
        cursor = db.cursor()
        app.config['db'] = db
        app.config['cursor'] = cursor
    except Error as e:
        print(f"Error connection: {e}")
    bootstrap.init_app(app)
    csrf.init_app(app)

    from .controller import register_routes
    register_routes(app)
    return app