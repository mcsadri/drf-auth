# drf-api-permissions-postgres

- Lab: Class 32 - Permissions & Postgresql
- Author: Manuch Sadri

## Overview

An CF401py introduction to using Permissions and Postgresql Database using Django REST Framework and Docker.

## Feature Tasks and Requirements

### General

- [X] Update the project from Class 21, `drf-api`, to complete the following functionality tasks:
  - [X] Restrict access to portions of your APIs data.
  - [X] Switch over to using `postgres` from `sqlite`.
- [X] Customize your project to use different application features/models than what was used in demos.

### Django REST Framework

- [X] Make your site a DRF powered API as you did in previous lab.
- [X] Adjust project’s permissions so that only authenticated user’s have access to API.
- [X] Add a custom permission so that only appropriate users can update or delete it.
- [X] Add ability to switch user’s directly from browsable API.

### Features - Docker

- **NOTE**: Refer to demo for built out `Dockerfile` and `docker-compose.yml` examples.
- [X] create `Dockerfile` based off `python:3.10-slim`
- [X] create `docker-compose.yml` to run Django app as a `web` service.
- [X] enter `docker compose up --build` to start your site.
- [X] add `postgres` as a service
  - Note: It is not required to include a volume so that data can persist when container is shut down.
- [X] Go to browsable api and confirm site properly restricts users based on their permissions.

## Stretch Goals

- [ ] Try different permission levels, including custom ones.
- [ ] Figure out how to directly access postgres running inside container. Hint: it will take research.
- [ ] Add a `volume` to persist data when container is shut down.

## Implementation Notes

- [X] You should NOT be running Postgres directly on host machine.
  - [X] This means that operations like `createsuperuser` and `migrate` will need to happen inside the container.
  - For example…
    - [X] docker compose run web python manage.py migrate
    - or:
    - [ ] docker compose run web bash

## UAT

- [ ] Modify provided unit tests in demo to work for your project.
