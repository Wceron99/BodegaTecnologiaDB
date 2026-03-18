# Sistema de Gestión de Empleados

Este proyecto es una aplicación web sencilla para registrar empleados, desarrollada con Flask y SQLite.

## Tecnologías utilizadas
- Python
- Flask
- HTML Templates (Jinja2)
- Base de datos SQLite
- Git
- GitHub

## Funcionalidades
- Registrar empleados
- Listar empleados
- Editar empleados
- Eliminar empleados
- Guardar información en una base de datos SQLite

## Estructura del proyecto
```
flask_empleados/
│
├── app.py
├── database.db
├── init_db.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── agregar.html
│   └── editar.html
│
└── static/
    └── style.css
```

## Instalación y ejecución
1. Instalar dependencias: `pip install -r requirements.txt`
2. Crear base de datos: `python init_db.py`
3. Ejecutar servidor: `python app.py`
4. Abrir en navegador: http://127.0.0.1:5000

## Control de versiones
Este proyecto utiliza Git para el control de versiones y está alojado en GitHub.