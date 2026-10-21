# Validador de Sitios WordPress 🕵️‍♂️🤖

Script en Python ligero y eficiente diseñado para monitorear el estado operativo y la frescura de contenido de una red de sitios WordPress.

## ¿Qué hace?
1. **Verifica disponibilidad HTTP:** Comprueba que la página principal de cada sitio responda con un código `200 OK`.
2. **Consulta la API REST:** Se conecta al endpoint de WordPress (`/wp-json/wp/v2/posts`) para evaluar la última publicación.
3. **Valida antigüedad:** Calcula si la última entrada se publicó hace menos de 24 horas.
4. **Reporta fallos:** Imprime en consola un listado detallado de los sitios que presentan problemas (caídos, errores de API o desactualizados) y finaliza con un código de salida `1` (útil para herramientas de CI/CD o monitoreo).

## Requisitos
* Python 3.x
* Librería `requests`

Instala las dependencias necesarias con:
```bash
pip install requests

```

## Uso

1. Configura la lista de URLs que deseas monitorear modificando la variable `SITIOS` en el script.
2. Ejecuta el script desde tu terminal:

```bash
python validador.py

```

```

```
