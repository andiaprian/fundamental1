import requests

print("Hello World")

# kalau ada error pakai seperti di bawah ini
try:
    r = requests.get('https://googlse.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada error', e)