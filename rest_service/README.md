## Mail Rest Service.
- Подключается к почтовому ящику по протоколу IMAP.:heavy_check_mark:
- Отправляет непрочитанные в NLP и NLG сервисы.
- Получает от сервисов ответ и передает информацию на клиент.

![](doc.PNG)

## Запуск
```
uvicorn --host HOST --port PORT src:app
```
