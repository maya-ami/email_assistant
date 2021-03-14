## Email classification service
On the client-side, emails are sorted into folders based on their topics.

**NB**: A sentiment analysis model is used for a prototype. Swap with a relevant model in production.

## Usage
```
uvicorn --host HOST --port PORT src:app
```

## Docs
API documentation is at http://HOST:PORT/redoc

![](doc.PNG)
