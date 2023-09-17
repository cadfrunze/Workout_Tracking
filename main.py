import requests
from datetime import datetime

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
raspuns_final: dict = raspuns_exercitiu.json()['exercises'][0]


setari_foaie_sheet: dict = {
    'workout': {
        'date': datetime.now().strftime('%d/%m/%Y'),
        'time': datetime.now().strftime('%H:%M:%S'),
    }
}
for (keya, valoarea) in raspuns_final.items():
    if keya == 'duration_min':
        setari_foaie_sheet['workout']['duration'] = str(valoarea)
    elif keya == 'nf_calories':
        setari_foaie_sheet['workout']['calories'] = str(valoarea)
    elif keya == 'name':
        setari_foaie_sheet['workout']['exercise'] = str(valoarea).title()

print(setari_foaie_sheet)
end_point: str = 'https://api.sheety.co/84e3d01b8e36c55e4d7a081710112b16/testing/workouts'

header_sheety: dict = {
'Content-Type': 'application/json',
    'Authorization': 'Bearer testare'
}
# cerere_get = requests.get(url=end_point, headers=header_sheety)
# print(cerere_get.text)
cerere_post = requests.post(url=end_point, json=setari_foaie_sheet, headers=header_sheety)
cerere_post.raise_for_status()
print(cerere_post.text)