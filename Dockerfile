FROM python:3.11.11-alpine3.21
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "task_manager/manage.py", "runserver"]


