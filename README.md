## Курсовой проект Docker"

#### Проект модуля 8
***
#### Реализованы задачи:
* Для разных сервисов созданы отдельные контейнеры (django, postgresql, redis, celery).
* Всё оформлено в файле docker-compose и dockerfile.
* Проект готов на размещение на удаленном сервере: 
  * можно запустить по инструкции, приложенной в Readme-файл;
  * для запуска не требуется дополнительных настроек.

***
### Прежде чем начать использовать проект нужно:
* Установить на ПК пакет docker и docker-compose
* Создать файл `.env` для переменного окружения.

### `.env`
    ALLOWED_HOSTS=*
    LANGUAGE_CODE=ru-ru
    TIME_ZONE=Europe/Novosibirsk
    POSTGRES_DB=<DATABASES_NAME>
    POSTGRES_USER=<DATABASES_USER>
    POSTGRES_PASSWORD=<DATABASES_PASSWORD>
    DATABASES_HOST=db
    TG_API_KEY=<TG_API_KEY>
    CELERY=redis://redis:6379

***
### Запуск Docker проекта
    docker-compose build
    docker-compose up
***
