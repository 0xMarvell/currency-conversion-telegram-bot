import os
import requests
from dotenv import load_dotenv
from dbhelper import DBHelper

db = DBHelper()
db.setup()
load_dotenv()

convert_to = 'NGN'
convert_from = 'GBP'

api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={convert_from}_{convert_to}'
response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
res = response.json()
rate = res['exchange_rate']
answer = f'Currently the exchange rate of {convert_to} to {convert_from} is {rate}'
if response.status_code == requests.codes.ok:
    print(answer)
    db.add_currency_choice(rate)
    print(db.get_choices())
    # db.delete_currency_choice(rate)
    # print(db.get_choices())
else:
    print('Error:', response.status_code, response.text)