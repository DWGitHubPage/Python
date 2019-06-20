# Python3.7.3
# Using http3


import http3

r = http3.get('https://news.ycombinator.com/')

print(r.url)
print(r)
print(r.status_code)
print(r.protocol)
print(r.headers['content-type'])
print(r.text)


params = {'key1': 'value1', 'key2': 'value2'}
s = http3.get('https://httpbin.org/', params=params)
s = http3.post('https://httpbin.org/post', data={'key': 'value'})

print(s.url)
print(s)
print(s.status_code)
print(s.protocol)
print(s.headers['content-type'])
print(s.text)


t = http3.get('http://github.com/', allow_redirects=False)

print(t.url)
print(t)
print(t.status_code)
print(t.protocol)


