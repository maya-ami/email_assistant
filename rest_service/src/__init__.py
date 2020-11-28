from imbox import Imbox
import email, imaplib
from imap_tools import MailBox, AND
import requests
from typing import List
from pydantic import BaseModel, validator
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


def create_app():
    """Инициализация FastAPI сервиса.

    Returns:
        app: FastAPI application
    """

    app = FastAPI(title="Mail AI REST Service",
                  description="Сервис подключения к почтовому ящику",
                  version="0.0.1",
                  debug=True)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    return app

class Item(BaseModel):
    email: str = None
    password: str = None

app = create_app()


@app.post("/api")
async def check_mail(item: Item):
    """
    Подключается к почтовому ящику,
    отбирает непрочитанные письма и отправляет
    на NLP сервис определения темы текста.
    В зависимости от темы кладет письмо в нужную папку.
    При отсутствии тематической папки - создает её.
    """
    username = item.email
    password = item.password

    with MailBox('imap.gmail.com').login(username, password, initial_folder='Inbox') as mailbox:
        for msg in mailbox.fetch(AND(seen=False)):
            text = msg.text
            topic = requests.get("http://0.0.0.0:6666/api?text={}".format(text))
            if not mailbox.folder.exists(topic):
                mailbox.folder.create(topic)
            mailbox.move(msg.uid, topic)

    return "ok"
