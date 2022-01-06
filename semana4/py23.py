import requests

r = requests.get('https://xkcd.com/353/')

print(r)
print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(r.content)

print('status code',r.status_code)
print('headers',r.headers)
print('url',r.url)
print('text',r.text)

print()
print()

payload = {'username':'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()

print(r_dict['form'])
