from deeppavlov import build_model, configs

from pydantic import BaseModel, validator
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


def create_app():
    """Инициализация FastAPI сервиса.

    Returns:
        app: FastAPI application
    """

    app = FastAPI(title="Topic Classification Service",
                  description="Сервис классификации текста",
                  version="0.0.1",
                  debug=True)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    return app

app = create_app()
# initialize deeppavlov sentiment model once for demo use
sent_model = build_model(configs.classifiers.rusentiment_elmo_twitter_cnn, download=True)

@app.get("/api")
async def classify(item: str):
    """
    Определение темы письма. На клиенте письма раскидываются по папкам в зависимости от темы.
    """
    topic = sent_model([item])[0]
    return topic
