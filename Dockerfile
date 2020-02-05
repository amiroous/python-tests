FROM python:3.7.2-alpine3.9

RUN apk update
RUN apk add g++ bash
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install pytest
RUN pip install selenium
RUN pip install Appium-Python-Client

WORKDIR /app

COPY functional /app/functional

WORKDIR /app/functional

RUN pipenv install

#CMD ["sh", "-c", "python", "-m" , "pytest", "-m", "health_test"]
