import json
import requests
import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

from dotenv import load_dotenv

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


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi! I'm here to help you with all your currency conversion needs.\nYou can find out how to use me by sending a /help command")


def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands:
	/exchangerate - Get the exchange rate between two currencies
	/convertcurrency - Convert one currency to another
	/jokes - To help you crack a smile just in case you're feeling blue :)""")


# def exchange_rate(update: Update, context: CallbackContext):
#     update.message.reply_text('What currency do you want to convert from?')
#     # convert_to = logger.info("%s", update.message.text)
#     update.message.reply_text('What currency do you want to convert to?')
#     # convert_from = logger.info("%s", update.message.text)

#     api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={convert_from}_{convert_to}'
#     response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
#     res = response.json()
#     rate = res['exchange_rate']
#     answer = f'Currently the exchange rate of {convert_to} to {convert_from} is {rate}'
#     if response.status_code == requests.codes.ok:
#         update.message.reply_text(answer)
#     else:
#         update.message.reply_text('Error:', response.status_code, response.text)
    

#def calculate_exchange_rate():
    


def jokes(update: Update, context: CallbackContext):
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
    res = response.json()
    joke = res[0]['joke']
    if response.status_code == requests.codes.ok:
        update.message.reply_text(joke)
    else:
        update.message.reply_text('Error:', response.status_code, response.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(f"Sorry {update.message.text} is not a valid command so I don't know what to do")


def main():
    updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    # updater.dispatcher.add_handler(CommandHandler('exchangerate', exchange_rate))
    updater.dispatcher.add_handler(CommandHandler('jokes', jokes))
    # updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
    # updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
