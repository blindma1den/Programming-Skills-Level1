import os
from flask import Flask
from dotenv import load_dotenv

from _code.blueprints.manchester_united import manchester_united
from _code.blueprints.dani_travel import dani_travel
from _code.blueprints.valencia_hospital import valencia_hospital

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# blueprints
app.register_blueprint(manchester_united)
app.register_blueprint(dani_travel)
app.register_blueprint(valencia_hospital)


@app.route('/')
def hello():
    return '@dlimon2 | Dev Level 1'


if __name__ == '__main__':
    app.run()