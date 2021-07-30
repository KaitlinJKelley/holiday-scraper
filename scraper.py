from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

url = "https://nationaldaycalendar.com/february/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = urllib.request.Request(url=url, headers=headers)

page = urlopen(req)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

soup = soup.find(id="et-boc")

print(soup.get_text())

