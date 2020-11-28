## Команда НеИИ

Общая архитектура решения:

![](system.PNG)


Подробнее о каждом из компонентов:

1. **Почтовый клиент.**
  ![](client.png)
2. **Mail Rest Service.**
  - Подключается к почтовому ящику по протоколу IMAP.:heavy_check_mark:
  - Отправляет непрочитанные в NLP и NLG сервисы и получает ответ.:heavy_check_mark:
  - Создает тематические папки. Раскладывает письма по папкам в соответствии с темой.:heavy_check_mark:
3. **NLP сервис.**
  - Определение темы письма. На клиенте письма раскидываются по папкам в зависимости от темы.
  - Реферирование текста. На клиенте вместо неинформативных преамбул типа "Добрый день, коллеги..." отображается суть письма в 1-2 фразах. Позволяет видеть суть без "проваливания" в каждую цепочку.
  - Определение важности. На клиенте письма, определенный как важные, отмечаются значком :fire:
4. **NLG сервис.**
  - Генерация возможного ответа. На клиенте выводится в диалоговом окне цепочки в качестве подсказки серым шрифтом. Отправка только по нажатию пользователя.
  ![](generate_reply.PNG)
5. **Голосовой помощник.**

  ГП состоит из следующих компонентов:
  - asr_service - Сервис распознавания речи для голосового управления: набор ответа, голосовой поиск. [Подробнее](https://github.com/maya-ami/neii_hackathon2020/tree/master/voice_assistant/asr_service) :heavy_check_mark:

  - nlu_service - Сервис выделения интентов пользователя. **В РАЗРАБОТКЕ**

  - tts_service - Сервис синтеза речи для . [Подробнее](https://github.com/maya-ami/neii_hackathon2020/tree/master/voice_assistant/tts_service) :heavy_check_mark:
