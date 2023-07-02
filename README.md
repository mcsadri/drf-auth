# drf-api-permissions-postgres

- Lab: Class 32 - Permissions & Postgresql
- Author: Manuch Sadri

## Overview

An CF401py introduction to using Permissions and Postgresql Database using Django REST Framework and Docker.

## Feature Tasks and Requirements

### General

- [ ] Update the project from Class 21, `drf-api`, to complete the following functionality tasks:
  - [ ] Restrict access to portions of your APIs data.
  - [ ] Switch over to using `postgres` from `sqlite`.
- [ ] Customize your project to use different application features/models than what was used in demos.

### Django REST Framework

- [ ] Make your site a DRF powered API as you did in previous lab.
- [ ] Adjust project’s permissions so that only authenticated user’s have access to API.
- [ ] Add a custom permission so that only appropriate users can update or delete it.
  - [ ] Exactly what this means will depend on your application, so if you have any questions about “appropriate users” means reach out to TA/Instructor.
- [ ] Add ability to switch user’s directly from browsable API.

### Features - Docker

- **NOTE**: Refer to demo for built out `Dockerfile` and `docker-compose.yml` examples.
- [ ] create `Dockerfile` based off `python:3.10-slim`
- [ ] create `docker-compose.yml` to run Django app as a `web` service.
- [ ] enter `docker compose up --build` to start your site.
- [ ] add `postgres` as a service
  - Note: It is not required to include a volume so that data can persist when container is shut down.
- [ ] Go to browsable api and confirm site properly restricts users based on their permissions.

## Stretch Goals

- [ ] Try different permission levels, including custom ones.
- [ ] Figure out how to directly access postgres running inside container. Hint: it will take research.
- [ ] Add a `volume` to persist data when container is shut down.

## Implementation Notes

- [ ] You should NOT be running Postgres directly on host machine.
  - [ ] This means that operations like `createsuperuser` and `migrate` will need to happen inside the container.
  - [ ] For example…
    - [ ] docker compose run web python manage.py migrate
    - or:
    - [ ] docker compose run web bash

## UAT

- [ ] Modify provided unit tests in demo to work for your project.
