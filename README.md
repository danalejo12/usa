# usa
Ciudades de estados unidos

Sitio web hecho con Django que muestra ciudades de Estados Unidos con su foto,
fecha de fundación, población y lugares turísticos.

## Requisitos

- Python 3.12 o superior
- PostgreSQL

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/danalejo12/usa.git
cd usa

# 2. Crear y activar el entorno virtual
python -m venv env
env\Scripts\activate        # Windows
# source env/bin/activate   # Linux / macOS

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables: copiar .env.example a .env y poner tus datos
copy .env.example .env      # Windows
# cp .env.example .env      # Linux / macOS
```

Crea en PostgreSQL una base de datos llamada `usa` (o el nombre que pongas en `DB_NAME`).

```bash
# 5. Crear las tablas
python manage.py migrate

# 6. Cargar las 12 ciudades de ejemplo
python manage.py loaddata ciudades

# 7. Crear un usuario administrador
python manage.py createsuperuser

# 8. Iniciar el servidor
python manage.py runserver
```

Abre http://127.0.0.1:8000/ para ver el sitio y http://127.0.0.1:8000/admin/ para administrar las ciudades.

## Créditos de las fotos

Las fotos de las ciudades provienen de [Wikimedia Commons](https://commons.wikimedia.org/)
y se usan bajo sus respectivas licencias libres.
