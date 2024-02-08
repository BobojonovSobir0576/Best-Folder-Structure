## Django Rest Framework: to make best folder structure...
> Install your packages

## Technologies Used
- [Django]()
- [Django Rest Framework](https://www.django-rest-framework.org/)


## Project Structure
This document outlines the structure of the Django project. It provides an overview of the main directories and files, explaining their purpose within the application.

## Overview
Below is the structure of the project:
- `manage.py`: A command-line utility that lets you interact with this Django project.
- `my_project/`: The main project directory.
  - `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
  - `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
  - `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.
  - `urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
  - `settings/`: Directory containing settings configurations for the project.
    - `__init__.py`: Makes Python treat the directories as containing packages.
    - `base.py`: Base settings applicable to all environments.
    - `development.py`: Settings specific to the development environment.
    - `production.py`: Settings specific to the production environment.
- `my_app/`: A Django app within the project.
  - `migrations/`: Directory storing database migrations for the app.
  - `__init__.py`, `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py`, `urls.py`: Standard Django app files for models, views, administration, and more.

## Running

> Windows cmd
 ```sh
set DJANGO_SETTINGS_MODULE=config.settings.development
python manage.py makemigrate and migrate and runserver
```

> Linux, MacOs or Ubuntu cmd
 ```sh
export DJANGO_SETTINGS_MODULE=config.settings.development
python manage.py makemigrate and migrate and runserver
```

## Additional Notes
> apps directory create and to push all app files into apps.
> command:
 ```sh
windows: move app_name apps\
linux: mv app_name apps\
```