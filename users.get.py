import requests

def is_verified_user(user_id, access_token):
    # Создаем параметры запроса
    params = {
        'user_ids': user_id,
        'fields': 'verified',
        'access_token': access_token,
        'v': '5.131'
    }
    
    # Отправляем запрос к API ВКонтакте для получения информации о пользователе
    response = requests.get('https://api.vk.com/method/users.get', params=params)
    response_json = response.json()
    
    # Проверяем, есть ли поле 'verified' в информации о пользователе
    if 'response' in response_json and response_json['response']:
        is_verified = response_json['response'][0].get('verified', 0)
        return is_verified
    
    return 0

def add_friends(user_id, friends, access_token):
    # Проходим по списку друзей пользователя
    for friend_id in friends:
        # Проверяем, является ли друг верифицированным
        if is_verified_user(friend_id, access_token):
            # Добавляем друга в список для добавления в друзья
            params = {
                'user_id': friend_id,
                'access_token': access_token,
                'v': '5.131'
            }
            response = requests.get('https://api.vk.com/method/friends.add', params=params)
            print(f"Друг {friend_id} добавлен в друзья")
        else:
            print(f"Друг {friend_id} не является верифицированным")

# Ваши данные
user_id = '807577722'  # ID вашего пользователя
access_token = 'Epfully'  # Ваш токен доступа

# Получаем список друзей пользователя
params = {
    'user_id': user_id,
    'access_token': access_token,
    'v': '5.131'
}
response = requests.get('https://api.vk.com/method/friends.get', params=params)
response_json = response.json()

# Проверяем, есть ли поле 'response' в ответе
if 'response' in response_json and response_json['response']:
    friends = response_json['response']['items']
    add_friends(user_id, friends, access_token)  # Добавляем друзей в список друзей
else:
    print("Ошибка при получении списка друзей")