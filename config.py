from os import getenv

secretKey = getenv("secretKey")
databaseName = getenv("databaseName")
databaseUser = getenv("databaseUser")
databasePassword = getenv("databasePassword")
databaseHost = getenv("databaseHost")
BOOTSTRAP_SERVE_LOCAL = getenv("BOOTSTRAP_SERVE_LOCAL")