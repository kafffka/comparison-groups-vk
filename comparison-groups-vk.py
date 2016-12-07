import vk, config

'''
Если больше 1к групп
Ввод данных в консоли
Вывод ошибки, если группы закрыты
'''


a = vk.api(method="groups.get", user_id=1962220, v="5.8", access_token=config.access_token)['items']
b = vk.api(method="groups.get", user_id=112327604, v="5.8", access_token=config.access_token)['items']
common = vk.api(method="groups.getById", group_ids=str(set(a).intersection(b))[1:-1], v="5.8")
names = [i['name'] for i in common]
print(names)
