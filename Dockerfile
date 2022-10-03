FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend-media

COPY . /backend-media

WORKDIR /backend-media

EXPOSE 8002

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
