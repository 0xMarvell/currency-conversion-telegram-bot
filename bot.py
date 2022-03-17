import json
import requests
import os
import logging

from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters
)

from dotenv import load_dotenv
from dbhelper import DBHelper

load_dotenv()

# api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want=EUR&have=NGN&amount=50000'
# response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print('Error:', response.status_code, response.text)

# api_url = 'https://api.api-ninjas.com/v1/exchangerate?pair=USD_EUR'
# response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
# x = response.json()
# if response.status_code == requests.codes.ok:
#     print(x['exchange_rate'])
# else:
#     print('Error:', response.status_code, response.text)

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)


def start(update, context):
	update.message.reply_text(
		"Hi! I'm here to help you with all your currency conversion needs.\nYou can find out how to use me by sending a /help command")


def help(update, context):
	update.message.reply_text("""Available Commands:
	/exchangerate - Get the exchange rate between two currencies
	/convertcurrency - Convert one currency to another
	/jokes - To help you crack a smile just in case you're feeling blue :)""")


def currency_1(update, context):
    update.message.reply_text('What currency do you want to convert from?')
    user_input = update.message.text
    db.add_currency_choice(get_currency_1(user_input))
    

def get_currency_1(user_input):
    answer = str(user_input)  
    #update.message.reply_text(answer)
    return answer


def currency_2(update, context):
    update.message.reply_text('What currency do you want to convert to?')
    user_input = update.message.text
    db.add_currency_choice(get_currency_1(user_input))
    

def get_currency_2(user_input):
    answer = str(user_input)  
    #update.message.reply_text(answer)
    return answer


def exchange_rate(update, context):
    update.message.reply_text("""To do this, I'm going to need some information from you through these commands:
	/currency1 - What currency do you want to convert from?
	/currency2 - What currency do you want to convert to?
	/getrate - Time to get the exchange rate between your currencies!""")

# def get_rate()
#     convert_to = get_currency_2(user_input = update.message.text)
#     convert_from = get_currency_1(user_input = update.message.text)

#     api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={convert_from}_{convert_to}'
#     response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
#     res = response.json()
#     rate = res['exchange_rate']
#     answer = f'Currently the exchange rate of {convert_to} to {convert_from} is {rate}'
#     if response.status_code == requests.codes.ok:
#         update.message.reply_text(answer)
#     else:
#         update.message.reply_text('Error:', response.status_code, response.text)


def jokes(update, context):
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
    res = response.json()
    joke = res[0]['joke']
    if response.status_code == requests.codes.ok:
        update.message.reply_text(joke)
    else:
        update.message.reply_text('Error:', response.status_code, response.text)


def unknown(update, context):
	update.message.reply_text(f"I'm sorry but {update.message.text} is not a valid command so I don't know what to do 😕")


def main():
    db.setup()
    updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    # dp.add_handler(CommandHandler('exchangerate', exchange_rate))
    dp.add_handler(CommandHandler('jokes', jokes))
    # dp.add_handler(CommandHandler('bookinfo1', currency_1))
    # dp.add_handler(CommandHandler('bookinfo2', currency_2))

    # dp.add_handler(MessageHandler(Filters.text, get_currency_1))
    # dp.add_handler(MessageHandler(Filters.text, get_currency_2))
    dp.add_handler(MessageHandler(Filters.text, unknown))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    db = DBHelper()
