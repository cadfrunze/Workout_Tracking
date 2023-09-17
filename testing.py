from datetime import datetime

astazi: str = datetime.now().strftime('Data: %d/%m/%Y | Ora: %H:%M')

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines('\n' + astazi)