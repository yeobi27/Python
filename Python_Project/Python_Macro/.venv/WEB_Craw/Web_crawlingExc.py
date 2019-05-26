import requests
r.encoding = 'utf-8'
r = requests.get('https://wikidocs.net')
# html = r.text

print(r.status_code)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.ok)

# print(html)