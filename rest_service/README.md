## Mail Rest Service.
- Connects to email via IMAP.:heavy_check_mark:
- Sends unread mails to NLP and NLG services and receives answers.:heavy_check_mark:
- Creates emails folders and sorts mails based on topics.:heavy_check_mark:

## Usage
```
uvicorn --host HOST --port PORT src:app
```

## Docs
API documentation is at http://HOST:PORT/redoc

![](doc.PNG)
