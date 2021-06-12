import requests
from json import loads

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

def get_user_id(uid):
    url = f'https://api.vk.com/method/users.get?user_ids={uid}&fields=bdate&v=5.71&access_token={ACCESS_TOKEN}'
    res= requests.get(url).json()
    return res['response'][0]['id']

def get_friends_id(user_id):
    url = f'https://api.vk.com/method/friends.get?user_id={user_id}&fields=bdate&v=5.71&access_token={ACCESS_TOKEN}'
    res= requests.get(url).json()
    return res['response']['items']
    
def get_friends_bdate_list(friends):
    friends_bdate_list = []
    for friend in friends:
        if 'bdate' in friend and len(friend['bdate'].split('.')) == 3:
            friends_bdate_list.append(friend['bdate'][-4:])
    return friends_bdate_list

def calc_age(uid):
    user_id = get_user_id(uid)
    friends = get_friends_id(user_id)
    friends_bdate_list = get_friends_bdate_list(friends)
    years_dict = {}
    ages = list()
    for year in friends_bdate_list:
        if 2021 - int(year) in years_dict.keys():
            years_dict[2021 - int(year)] += 1 
        else:
            years_dict[2021 - int(year)] = 1
    for k, v in years_dict.items():
        ages.append((k, v))
    ages.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    return ages

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
