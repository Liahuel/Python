import requests
from bs4 import BeautifulSoup

# URL objetivo
url = "https://news.ycombinator.com/"

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar los títulos de las noticias
    titles = soup.select('.titleline > a')

    # Imprimir los títulos
    print("Títulos de noticias:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.text}")
else:
    print("Error al acceder a la página:", response.status_code)