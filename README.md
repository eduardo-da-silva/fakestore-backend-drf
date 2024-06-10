# Backend FakeStore API - Django with Django Rest Framework (DRF)

This is a simple Django project that uses Django Rest Framework to create a REST API for a fake store. The API provides endpoints for products, categories, and orders.

Also, the project is integrated with the Passage.ID to handle user authentication.

To use the Passage.ID, you must create an account on the platform and create an application to get the APP_ID and API_KEY. You can do this by accessing the following link: [https://passage.id/](https://passage.id/). Create an account, create an application, select the complete authentication flow, then the embedded login experience, and get the APP_ID and API_KEY.

IMPORTANT: I've created such an application for educational purposes only, providing a backend to be used with frontend projects in my classes. I'm using such a backend to teach my students how to create a PWA frontend project using Vue to consume this API, perform user authentication, and so on. The class notes are in Portuguese, but you can access them by clicking [here](https://eduardo-da-silva.github.io/aula-desenvolvimento-mobile).

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
