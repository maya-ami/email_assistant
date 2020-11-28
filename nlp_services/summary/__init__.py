from summa import summarizer

from pydantic import BaseModel, validator
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


def create_app():
    """Инициализация FastAPI сервиса.

    Returns:
        app: FastAPI application
    """

    app = FastAPI(title="Summary Service",
                  description="Сервис реферирования текста",
                  version="0.0.1",
                  debug=True)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    return app


app = create_app()

@app.post("/api")
async def summarize(item: str):
    """
    Позволяет получить выжимку текста в 2-3 предложениях. Результат отдается на клиент.
    Позволяет пользователю видеть суть письма без "проваливания" в каждую цепочку.
    """
    summary = summarizer.summarize(item, words=50, language='russian')
    return summary
