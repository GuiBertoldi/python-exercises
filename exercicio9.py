import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com")
content = response.content

soup = BeautifulSoup(content, "html.parser")

with open("resultados.txt", "w") as arquivo:
    arquivo.write("Resultados:\n")
    arquivo.write(f"Título: {titulo}\n")
    arquivo.write(f"Descrição: {descricao}\n")
    arquivo.write(f"Link: {link}\n")