# education_modules

для запуска сервера необходимо клонировать репозиторий следующей командой:
- git clone https://github.com/serebas/education_modules.git <имя_каталога>\<название_проекта>

далее перейти в каталог:
- cd <имя_каталога>

создать виртуальное окружение:
- python -m venv venv
и активировать его:
- venv\Scripts\activate.bat

установить все зависимости:
- pip install -r requirements.txt

выполнить миграцию бд:
- cd <название_проекта>
- python manage.py migrate

т.к. все ключи хранятся в переменной окружения, файл которой не попадает в репозиторий, для работоспособностив всех тестов
в настройках небходимо подставить SECRET_KEY = 'django-insecure-=b7wysrqd37@3(!0a2)dh#esj%-@t77pl2xis&5y#l+x6bnkat'

запуск всех тестов будет доступно по команде: - pytest
