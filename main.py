import requests

APP_ID: str = 'af3c9ccd'
APP_KEY: str = 'e416cbba2d1a1f6e1d02b2a513120f8e'
URL_END_P: str = 'https://trackapi.nutritionix.com/v2/natural/exercise'
header: dict = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,

}

mesaj: str = input('Tell me which exercises you did: ')
body_endpoint: dict = {
    'query': mesaj,
    'gender': 'male',
    'weight_kg': '112',
    'height_cm': '182',
    'age': '38'
}

raspuns_exercitiu = requests.post(url=URL_END_P,
                                  headers=header, json=body_endpoint)
raspuns_exercitiu.raise_for_status()
print(raspuns_exercitiu.json())
