FROM python:3.8

WORKDIR /code

COPY ./Pipfile /code/Pipfile
RUN pip install pipenv
RUN pipenv install

COPY ./src /code/app/src
WORKDIR /code/app/src/

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]