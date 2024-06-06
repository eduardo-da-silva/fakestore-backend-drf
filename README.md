# Backend FakeStore API - Django with Django Rest Framework (DRF)

This is a simple Django project that uses Django Rest Framework to create a REST API for a fake store. The API provides endpoints for products, categories, and orders.

Also, the project is integrated with the Passage.ID to handle user authentication.

## How to use

After cloning the repository, you must to create a .env file in the root directory of the project with the following content:

```
MODE=DEVELOPMENT        #  possible values are: DEVELOPMENT, PRODUCTION, MIGRATE
SECRET_KEY=SOME_SECRET_KEY_HERE
DEBUG=True              #  possible values are: True, False
PASSAGE_APP_ID=THE_APP_ID_PROVIDED_BY_PASSAGE
PASSAGE_API_KEY=THE_API_KEY_PROVIDED_BY_PASSAGE
```

## Using Docker

You can also run the project using Docker. To do this, you must have Docker and Docker Compose installed on your machine. After that, you can create a docker-compose.yml file in the root directory of the project with the following content:

```yaml
name: fakestore-backend-drf
services:
  app:
    image: eduardosilvasc/fakestore-backend-drf:latest
    environment:
      - MODE=DEVELOPMENT #  possible values are: DEVELOPMENT, PRODUCTION, MIGRATE
      - SECRET_KEY=SOME_SECRET_KEY_HERE
      - DEBUG=True #  possible values are: True, False
      - PASSAGE_APP_ID=THE_APP_ID_PROVIDED_BY_PASSAGE
      - PASSAGE_API_KEY=THE_API_KEY_PROVIDED_BY_PASSAGE
    ports:
      - 8000:8000
```

Então, bastar rodar o comando `docker-compose up` para subir o container.
