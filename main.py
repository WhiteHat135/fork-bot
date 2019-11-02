""" Import Module """
import json
import request
import urllib
""" Main vars """
token = '869011883:AAFkJ1IEfaqf9bD5RxGekz9L2Xf7z0JCECo'
url = f"https://api.telegram.org/bot{token}/"
group_id = "-1001461305516"
""" Download  """
def get_url(url):
    responce = request.get(url)
    content = responce.content
    return content
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js
def get_updates():
    content = url + "getUpdates"
    js = get_json_from_url(url)
    return js

    
""" def send_message(url, group_id, events)
    responce = request.get(url + "sendMessage?chat_id=-1001461305516&text={events}") """