import requests

def api(method, **kwargs):
    values = {'v': '5.8'}
    values.update(kwargs)
    url  = u'https://api.vk.com/method/{}'.format(method)
    res = requests.get(url, values)
    data = res.json()
    if 'error' in data:
        print(data['error']['error_msg'])
        return None
    return data[u'response']
