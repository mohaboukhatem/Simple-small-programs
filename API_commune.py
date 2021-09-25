
import requests,json
api = requests.get("https://api.yalidine.com/v1/")

ap = json.loads(api.text)
print(ap)

