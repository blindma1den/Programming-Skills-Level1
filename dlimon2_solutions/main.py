import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
# blueprints
from _code.blueprints.manchester_united import manchester_united


app.register_blueprint(manchester_united)

@app.route('/')
def hello():
    return '@dlimon2 | Dev Level 1'


if __name__ == '__main__':
    app.run()