Для запуска на локальной машине используйте следующие команды:
pip install --upgrade pip
pip install -r requirements.txt
cd task_manager
python manage.py runserver
Для тестирования:
python manage.py test
К сожалению, развернуть докер контейнер не удалось (не видит порт подключения), хотя оба контейнера разворачиваются без ошибок
