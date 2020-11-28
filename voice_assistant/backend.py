from requests_toolbelt import MultipartEncoder
import requests
import json
import ast
import subprocess
import sys
import sqlite3
sys.path.append("db")
import answer_storage2
from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin

"""
Бекенд, связывающий 2 микросервиса (ASR, STT), с JS фронтендом.
Приложение использует два метода:
    - listen активируется при нажатии на микрофон: распознавание речи.
    - read активируется при отправки динамик: синтез речи.
"""

app = Flask(__name__)
cors = CORS(app)

def chunked_reader(f, chunksize=2 ** 20):  # 1Mb chunks
    while True:
        chunk = f.read(chunksize)
        if not chunk:
            return
        yield chunk


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/listen', methods=['POST'])
@cross_origin(supports_credentials=True)
def listen():
    # Записываем полученный с фронтенда бинарник в wav файл
    to_recognize = request.files['file'].read()
    with open("./asr_service/question.wav", "wb") as f:
        f.write(to_recognize)

    # Отправляем wav файл на ASR сервис
    q = requests.get("http://0.0.0.0:5000/recognize_wav")
    # DEBUG:
    print(q.text)

    dict1 = [{"text": q.text}]
    m = MultipartEncoder(fields={ 'messages': json.dumps(dict1))
    return (m.to_string(), {'Content-Type': m.content_type})


@app.route('/read', methods=['POST'])
def read():
    text = request.form["text"]

    # Отправляем текст на сервис синтеза речи (STT)
    s = requests.get('http://0.0.0.0:5555/say?text={}'.format(text))

    m = MultipartEncoder(fields={ 'files': ("sound.wav", s.content, 'audio/wav') })
    return ({'Content-Type': m.content_type})

if __name__ == "__main__":
    app.run(host='localhost', port=8083, debug=True)
