import requests as re
response = re.get('https://www.cricbuzz.com/')
html = response.text
print(html)