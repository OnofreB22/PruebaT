# Prueba Técnica - Desarrollo de API en Python

## Descripción
Esta es una API desarrollada en Django para gestionar una entidad llamada "Estaciones". La API permite crear estaciones, listar todas las estaciones y, dado el ID de una estación, encontrar y retornar la estación más cercana a su ubicación.

## Tecnologías utilizadas
- **Python**: Lenguaje principal del desarrollo.
- **Django**: Framework principal para el desarrollo de la API.
- **Django REST Framework**: Para simplificar la creación de los endpoints de la API.
- **PostgreSQL**: Base de datos utilizada, aunque puede configurarse con cualquier base de datos SQL.
- **PostGis**: Extension de PostgreSQL para convertir este motor de bases de datos en una base de datos espacial.
- **Docker**: Para contenerización y despliegue local del proyecto.
- **Drf-spectacular**: Herramienta para generar un esquema/documentacion de la API automaticamente.

## Características
La API expone tres endpoints:
1. **``POST`` /estaciones/**: Crear una nueva estación.
2. **``GET`` /estaciones/**: Listar todas las estaciones.
3. **``GET`` /estaciones/cercana/id/**: Dado el ID de una estación, retornar la estación más cercana a su ubicación.

## Requisitos previos
- Docker y Docker Compose instalados.
- Python 3.13+ si decides ejecutar localmente sin Docker.
- PostgreSQL (Si decides no utilizar Docker).

## Instalación y Configuración

### 1. Clonar el Repositorio
Clona el proyecto desde GitHub:
```bash
git clone https://github.com/OnofreB22/PruebaT.git
cd PruebaT
```

### 2. Ejecutar el proyecto
```bash
docker-compose up --build
```

### 3. Realizar migraciones de la base de datos (Opcional)
```bash
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
```

### 4. Ejecucion de las pruebas unitarias (Opcional)
```bash
docker-compose run --rm app sh -c "python manage.py test"
```
## Uso de la API

### Crear una nueva estacion
- **Endpoint**: ``POST`` localhost:8000/estaciones/
- **Body**:
```json
{
  "nombre": "Nombre de la Estación",
  "ubicacion": "POINT(longitud latitud)"
}
```

### Obtener un listado de todas las estaciones
- **Endpoint**: ``GET`` localhost:8000/estaciones/
- **Body**:
```json
[
    {
        "id": 1,
        "nombre": "Bogota",
        "ubicacion": "SRID=4326;POINT (-74.03616403078435 4.726529812472924)"
    },
    {
        "id": 2,
        "nombre": "Medellin",
        "ubicacion": "SRID=4326;POINT (-75.56959104387936 6.1922579572101855)"
    },
    {
        "id": 3,
        "nombre": "Envigado",
        "ubicacion": "SRID=4326;POINT (-75.58752264870299 6.170063820656889)"
    }
]
```

### Obtener la estacion mas cercana
- **Endpoint**: `GET` localhost:8000/estaciones/cercana/`<id>`/
- **Body**:
```json
{
    "id": 3,
    "nombre": "Envigado",
    "ubicacion": "SRID=4326;POINT (-75.58752264870299 6.170063820656889)"
}
```

### Obtener el esquema de la API generado por "drf-spectacular" `yml`
- **Endpoint**: `GET` localhost:8000/api/schema/

### Obtener el esquema de la API generado por "drf-spectacular" `SwaggerUI`
- **Endpoint**: `GET` localhost:8000/api/docs/