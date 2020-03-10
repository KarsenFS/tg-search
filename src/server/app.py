import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, jsonify, Response
from flask_cors import CORS
# from telethon.sync import TelegramClient, events
# from telethon.tl.functions.contacts import GetContactsRequest
# from telethon.tl.types import UserStatusOffline

# configuration
DEBUG = True

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('../') / '.env' # Путь до .env файла со всеми токенами и ключами
load_dotenv(dotenv_path=env_path) # Загрузка .env файла

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

api_id = os.getenv("TEST_API_ID") # получение api_id из .env файла
api_hash = os.getenv("TEST_API_HASH")

# client = TelegramClient("my_name", api_id, api_hash)
# client.connect()

# sanity check route
@app.route('/auth', methods=['GET'])
def auth():
    return jsonify(api_id) #При запросе на http://127.0.0.1:5000/auth, вернет json с api_id (из файла .env)
    # return jsonify(client.get_me())


if __name__ == '__main__':
    app.run()