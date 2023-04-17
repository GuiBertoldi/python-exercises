import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"
response = requests.get(url)

if response.status_code == 200:
    raw_html = response.text
    soup = BeautifulSoup(raw_html, "html.parser")
    titles = soup.find_all("h2")

    print("Títulos de artigos do New York Times:")
    for title in titles:
        print(title.get_text(strip=True))

else:
    print("Erro ao fazer requisição HTTP:", response.status_code)
