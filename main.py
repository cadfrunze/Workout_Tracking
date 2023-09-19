import requests
import os
from datetime import datetime

APP_ID = os.environ.get('APP_ID')
APP_KEY_NUTRINIONIX = os.environ.get('APP_KEY_NUTRINIONIX')
URL_END_P = os.environ.get('URL_END_P')
APP_KEY_SHEETY = os.environ.get('APP_KEY_SHEETY')
AUTORIZATION_SHEETY = os.environ.get('AUTORIZATION_SHEETY')

header: dict = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY_NUTRINIONIX,

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

end_point: str = f'https://api.sheety.co/{APP_KEY_SHEETY}/testing/workouts'

header_sheety: dict = {
    'Content-Type': 'application/json',
    'Authorization': AUTORIZATION_SHEETY
}

cerere_post = requests.post(url=end_point, json=setari_foaie_sheet, headers=header_sheety)
cerere_post.raise_for_status()
