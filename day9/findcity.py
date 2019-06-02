# 1. 查询城市 ID
# 2. 退出

# 1. 河北省
# 2. 陕西
# 请输入省份

import json

def load_cities():
    with open('./day9/cities.json', 'r', encoding='utf-8', newline='') as f:
        cities_json = f.read()
        cities = json.loads(cities_json)
        cities_list = cities['result']
        return cities_list

def find_id_with_city():
    cities = load_cities()
    for j in ['province', 'city', 'district']:
        l = []
        for k in cities:
            if k[j] not in l:
                print(k[j], end='   ')
                l.append(k[j])
        print()
        name = input(f'请输入{j}:')
        l = []
        for i in cities:
            if i[j]==name:
                l.append(i)
        cities = l
    return l[0]['id']



id = find_id_with_city()
print(f'id为{id}')




