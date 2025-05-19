import requests

url = 'https://www.w3.org/Style/CSS/current-work'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()
html = response.text

with open('css_current-work.html', 'w', encoding='utf-8') as outfile:
   outfile.write(html)

