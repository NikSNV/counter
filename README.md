# Нужно разработать микросервис для счетчиков статистики. Сервис должен уметь взаимодействовать с клиентом при помощи REST API. Также нужно реализовать валидацию входных данных.

##### _разработка Sladkov N.V._

### _Документация API_ (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )

## Описание ТЗ:

##### _Функционал:_
API методы:
Метод сохранения статистики
Метод показа статистики
Метод сброса статистики
Метод сохранения статистики.
Принимает на вход:

date - дата события
views - количество показов
clicks - количество кликов
cost - стоимость кликов (в рублях с точностью до копеек)
Поля views, clicks и cost - опциональные. Статистика агрегируется по дате.

Метод показа статистики
Принимает на вход:

from - дата начала периода (включительно)
to - дата окончания периода (включительно)
Отвечает статистикой, отсортированной по дате. В ответе должны быть поля:

date - дата события
views - количество показов
clicks - количество кликов
cost - стоимость кликов
cpc = cost/clicks (средняя стоимость клика)
cpm = cost/views * 1000 (средняя стоимость 1000 показов)
Метод сброса статистики
Удаляет всю сохраненную статистику.

Критерии приемки:
язык программирования: Python/Django
можно использовать любое хранилище(PostgreSQL, MySQl, Redis и т.д.) или обойтись без него (in-memory).
формат даты YYYY-MM-DD.
стоимость указывается в рублях с точностью до копеек.
в методе показа статистики можно выбрать сортировку по любому из полей ответа.
простая инструкция для запуска (в идеале — с возможностью запустить в docker).
Усложнения:
покрытие unit-тестами.
документация (достаточно структурированного описания методов, примеров их вызова в README.md).


## Окружение проекта:
  * python 3.9
  * Django 3.2.6
  * djangorestframework
  * drf-yasg

Склонируйте репозиторий с помощью git

    git clone https://github.com/NikSNV/counter.git
Перейти в папку:
```bash
cd counter
```
Создать и активировать виртуальное окружение Python.

## Используется база данных SQLLite3

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt

```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя по необходимости
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
```bash
Username (leave blank to use 'admin'): admin
Email address: test@test.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


### _Документация API_ (создал автодокументирование API на swagger доступно по адресу http://127.0.0.1:8000/swagger/ )


### Метод сохранения статистики:
* Request method: POST
* Example: 
```
curl  -H 'Content-Type: application/json' --data '{"date": "2021-02-02","views": 800, "clicks": 650, "cost": 70.0}' http://127.0.0.1:8000/api/counters/
```

### Метод показа статистики с фильтрацией по заданному диапазону дат:
* Request method: GET
* URL Example: http://127.0.0.1:8000/api/counters/2020-01-01/2021-10-15/


### Метод показа статистики с выбором фильтра по заданному диапазону дат:
* Request method: GET
* Доступные фильтры из DB для подстановки в URL:
    * date
    * views
    * clicks
    * cost

* URL Example: http://127.0.0.1:8000/api/counters/2020-01-01/2021-10-15/views/


### Метод сброса статистики:
* Request method: GET
* URL Example: http://127.0.0.1:8000/api/delete/


### Покрытие unit-тестами:
* Сделал проверку вьюх на вызов. Запустите в корне:
* Example: python manage.py test
