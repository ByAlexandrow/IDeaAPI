### Описание проекта:

Yatube - социальная сеть, где пользователи могут делиться запоминающимися событиями своей жизни с другими. Есть возможность публиковать и редактировать посты и комментарии, подписаываться на определенного пользователя и следить за его публикациями.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

По этому запросу будет получен список всех комментариев к определенному посту
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Выполнив этот запрос, Вы получите информацию об определенном сообществе
```
http://127.0.0.1:8000/api/v1/groups/{id}/
```
По этому запросу Вы получите все посты
```
http://127.0.0.1:8000/api/v1/posts/
```

### Использованные технологии:

- [Django](https://www.djangoproject.com/) - фреймворк для веб-разработки на Python.

- [Django REST framework](https://www.django-rest-framework.org/) - библиотека для создания веб-API на основе Django.

- [SQLite3](https://www3.sqlite.org/) - система управления базами данных.

### Контакты:

[Gladia-Torr](https://github.com/Gladia-Torr) - будущий разработчик
