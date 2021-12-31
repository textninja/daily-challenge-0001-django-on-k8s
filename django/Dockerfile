FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN django-admin startproject dtc0001
WORKDIR /app/dtc0001
COPY urls.py /app/dtc0001/dtc0001/urls.py
COPY dtc0001themechange dtc0001themechange 
COPY settings.py /app/dtc0001/dtc0001/settings.py
CMD daphne -b 0.0.0.0 dtc0001.asgi:application
