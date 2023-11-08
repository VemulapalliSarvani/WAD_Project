import requests as re
response = re.get('https://www.nbcsports.com/')
html = response.text
print(html)