# API для Yatube

REST API для социальной сети Yatube. Позволяет работать с публикациями и комментариями.

## Возможности:

Аутентифицированный пользователь авторизован на создание, изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

## Как запустить проект:

Требования: `Python 3.9+`  
Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:exsull/api-yatube.git
```
```bash
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

Windows

```bash
source venv/Scripts/activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
cd yatube_api
```
```bash
python manage.py migrate
```

Запустить сервер:

```bash
python manage.py runserver
```

## Получение токена

```http
POST /api/v1/api-token-auth/
```

Тело запроса:

```json
{
    "username": "username",
    "password": "password"
}
```

Ответ:

```json
{
    "token": "0123456789abcdef..."
}
```

## Примеры запросов

### Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
```http
POST .../api/v1/posts/
```
```json
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```
Пример ответа:
```json
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```
### Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14.
```http
POST .../api/v1/posts/14/comments/
```
```json
{
    "text": "тест тест",
}
```
Пример ответа:
```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```
### Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.
```http
GET .../api/v1/groups/2/
```
Пример ответа:
```json
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```

### Получить список публикаций

```http
GET .../api/v1/posts/
```

Пример ответа:

```json
[
    {
        "id": 1,
        "text": "Первая публикация",
        "author": "admin"
    }
]
```

### Создать публикацию

```http
POST .../api/v1/posts/
Authorization: Token <ваш_токен>
```

Тело запроса:

```json
{
    "text": "Новая публикация"
}
```

## Автор

GitHub: [**exsull**](https://github.com/exsull)