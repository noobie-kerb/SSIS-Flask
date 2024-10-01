from app import initialize_app
from dotenv import load_dotenv

load_dotenv('.env')

app = initialize_app()

if __name__ == "__main__":
    app.run()