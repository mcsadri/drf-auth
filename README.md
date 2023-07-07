# drf-auth

- Lab: Class 33 - Authentication & Production Server
- Author: Manuch Sadri

## Overview

An CF401py introduction to using to Authentication & Production Servers using JSON Web Tokens and Gunicorn

## Feature Tasks and Requirements

### Django

- [X] Add JWT Authentication to your API.
  - [X] Install needed libraries in project configuration and/or site settings.
- [X] Keep any pre-existing authentication so DRF Browsable API still usable.
  - [X] Install needed libraries in project configuration and/or site settings.

### Docker

- [ ] Switch to using [Gunicorn](https://gunicorn.org/) instead of Django’s built in development server.
  - [ ] mind the number of workers to avoid sluggishness
- [ ] Warning You will run into styling issues when you switch over to Gunicorn.
  - [ ] On Django side you’ll need to properly handle static files using [Whitenoise](http://whitenoise.evans.io/en/stable/django.html)

### Storage Options

- [X] Your choice of SQLite or **PostgreSQL**
- [ ] Adjust `docker-compose.yml` so that data is persisted in a volume outside of container.
  - [ ] These steps are different depending on whether SQLite or PostgreSQL is being used.

## Stretch Goals

- [ ] Create a boilerplate `Dockerfile` and `docker-compose.yml` so you don’t need to start from scratch each time.
  - [ ] E.g. as a VS Code snippet, or a gist.
- [ ] Research deployment options for Docker/Postgres/Django and report findings to class
- [ ] Research separate PostgreSQL hosting
- [ ] Create/Find a `seed` project so that you can have a running start on next DRF project.

## Implementation Notes

- [ ] README should include steps to manually test using HTTP Client such as httpie, ThunderClient, etc.
  - [ ] List the routes (including HTTTP method and note whether token is required) for:
    - [ ] get tokens
    - [ ] refresh tokens
    - [ ] CRUD routes for resource

## UAT

- n/a
