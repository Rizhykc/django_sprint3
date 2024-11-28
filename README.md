# Блогикум часть 2

## Это часть работы над проектом Блогикум:

- [Блогикум часть 1](https://github.com/Rizhykc/django_sprint1)
- Блогикум часть 2 ← _этот репозиторий_
- [Блогикум часть 3](https://github.com/Rizhykc/django_sprint4)


## Технологии:

- Python 3.9.13
- Django 3.2.25
- SQLite

## Установка (Windows):

1. Клонирование репозитория

```
git clone https://github.com/Rizhykc/django_sprint3.git
```

2. Переход в директорию django_sprint3

```
cd django_sprint3
```

3. Создание и активация виртуального окружения

```
python -m venv venv
source venv/Scripts/activate
```

4. Обновите pip

```
python -m pip install --upgrade pip
```

5. Установка зависимостей

```
pip install -r requirements.txt
```

6. Перейти в папку проекта blogicum и запустить его:

```
cd blogicum
./manage.py migrate
./manage.py loaddata db.json
./manage.py runserver
```

7. Перейти на локальный сервер:

```
http://127.0.0.1:8000/
```

8. Перейти в панель администратора:

```
http://127.0.0.1:8000/admin/
```
