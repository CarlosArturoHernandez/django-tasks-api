# Django-React Task Manager App

<img src="portada-GitHub.png" alt="Portada del GitHub"></img>

![Logo de Task Manager](https://skillicons.dev/icons?i=django,react,sqlite,tailwind)

## Descripción

Django-React Task Manager App es una aplicación para la gestión de tareas desarrollada con Django REST Framework y React. Proporciona una plataforma para organizar y gestionar tareas de forma básica.

## Tecnologías Utilizadas

- Django
- Django REST Framework
- React
- SQLite

## Requisitos Previos

- Python >= 3.6
- Django >= 3.0
- Node.js >= 12
- SQLite (incluido con Python)

## Instalación

1. Clona este repositorio: `git clone https://github.com/TuUsuario/django-task-manager.git`
2. Configura el entorno virtual (opcional pero recomendado): `python -m venv venv`
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias de Django: `pip install -r requirements.txt`
5. Migraciones de la base de datos: `python manage.py migrate`
6. Inicia el servidor Django: `python manage.py runserver`
7. En otra terminal, navega al directorio del cliente React: `cd client`
8. Instala las dependencias de Node.js: `npm install`
9. Inicia el servidor React: `npm start`
10. Visita `http://localhost:5173` en tu navegador para ver la aplicación.

## Funcionalidades Principales

- Creación, edición y eliminación de tareas.
- Interfaz de usuario responsive con React.
- Panel de administración para gestionar usuarios del backend.

## Estructura de Archivos

- `client/` - Código fuente del cliente React.
- `django_crud_api/` - Código fuente de la API Django.
- `tasks/` - Código de la aplicación de django
- `db.sqlite3` - Base de datos SQLite para desarrollo.

## Configuración de BD

- No se requiere configuración adicional para SQLite, ya que es parte del entorno de desarrollo de Python.
