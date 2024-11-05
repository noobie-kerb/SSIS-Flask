from config import secretKey, databaseHost, databaseName, databasePassword, databaseUser, BOOTSTRAP_SERVE_LOCAL, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET 
from flask import Flask 
from flask_bootstrap import Bootstrap 
from flask_wtf.csrf import CSRFProtect
from mysql.connector import connect, Error
import cloudinary
from cloudinary.uploader import upload
import cloudinary.api

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
    cloudinary.config(
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_API_KEY,
        api_secret = CLOUDINARY_API_SECRET
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