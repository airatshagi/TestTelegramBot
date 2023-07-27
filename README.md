Конфиг файл .env должен содержать параметры:
    * time_interval_minutes - интервал минут опроса сайтов
    * telegram_token - токен телеграм бота
    * telegram_chat_id - id беседы, куда отправлять сообщения
    * sites_list - json-строка, список опрашиваемых сайтов вида: {"site1":"https://www.site1.ru/", "site2":"https://www.site1.ru/catalog/page.html"}