from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://nationaldaycalendar.com/january/"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

soup = soup.find(id="et-boc")

print(soup.get_text())

