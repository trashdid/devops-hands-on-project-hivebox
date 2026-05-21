FROM python:3.14.5-alpine3.23

ARG APP_VERSION=unknown
ENV APP_VERSION=${APP_VERSION}

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /app ./

CMD ["python", "main.py"]