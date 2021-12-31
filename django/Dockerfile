FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN django-admin startproject dtc0001
WORKDIR /code/dtc0001
COPY settings.py /code/dtc0001/dtc0001/settings.py
RUN python manage.py startapp polls
CMD python manage.py runserver 0.0.0.0:8000
