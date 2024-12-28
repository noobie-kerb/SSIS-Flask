from os import getenv

secretKey = getenv("secretKey")
databaseName = getenv("databaseName")
databaseUser = getenv("databaseUser")
databasePassword = getenv("databasePassword")
databaseHost = getenv("databaseHost")
BOOTSTRAP_SERVE_LOCAL = getenv("BOOTSTRAP_SERVE_LOCAL")
CLOUDINARY_CLOUD_NAME = getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = getenv("CLOUDINARY_API_SECRET")