## Text summarization service
Allows to obtain most important info in 2-3 sentences. The result is sent to the client-side where it can be shown on hovering over a mail. Thus, a user can get the gist without having to open a thread.

## Usage
```
uvicorn --host HOST --port PORT src:app
```

## Docs
API documentation is at http://HOST:PORT/redoc

![](doc.PNG)
