import requests
url_0 = "http://192.168.0.201:8000/index.php"
url = "http://192.168.0.201:8000/login.php"
data = {"user": "admin", "pass": "admin"}

s = requests.session()
s.get(url_0)
r = s.post(url, data)
print r
url_inicia_wireless="http://192.168.0.201:8000/scripts/status_wireless.php?service=wireless&action=start"
s.get(url_inicia_wireless)
