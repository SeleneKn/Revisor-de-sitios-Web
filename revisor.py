import sys
from datetime import datetime, timezone
import requests

SITIOS = [
    "https://example1.com",
    "https://example2.com",
]

MAX_HORAS = 24


def verificar_wordpress(urls):
  fallos = []
  ahora = datetime.now(timezone.utc)

  for url in urls:
    url_base = url.rstrip("/")
    try:
      # 1. Verificar si responde la web principal
      resp = requests.get(url_base, timeout=10)
      if resp.status_code != 200:
        fallos.append((url, f"HTTP Error: {resp.status_code}"))
        continue

      # 2. Consultar la API de WordPress para la última nota
      api_url = f"{url_base}/wp-json/wp/v2/posts?per_page=1"
      api_resp = requests.get(api_url, timeout=10)
      if api_resp.status_code != 200:
        fallos.append((url, f"API Error: {api_resp.status_code}"))
        continue

      posts = api_resp.json()
      if not posts:
        fallos.append((url, "Sin publicaciones encontradas"))
        continue

      # 3. Validar la fecha de la última nota
      fecha_str = posts[0]["date_gmt"]
      fecha_post = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S").replace(
          tzinfo=timezone.utc
      )
      diferencia_horas = (ahora - fecha_post).total_seconds() / 3600

      if diferencia_horas > MAX_HORAS:
        fallos.append(
            (url, f"Última nota hace {diferencia_horas:.1f} horas (>24h)")
        )

    except Exception as e:
      fallos.append((url, f"Excepción: {str(e)}"))

  return fallos


if __name__ == "__main__":
  print("Verificando sitios WordPress...")
  sitios_fallidos = verificar_wordpress(SITIOS)

  if sitios_fallidos:
    print("\n[!] Sitios que fallaron:")
    for sitio, motivo in sitios_fallidos:
      print(f" - {sitio}: {motivo}")
    sys.exit(1)
  else:
    print("\n[✔] Todos los sitios responden y están actualizados.")
    sys.exit(0)