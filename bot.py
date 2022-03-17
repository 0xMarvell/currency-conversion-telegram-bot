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


def exchange_rate(update, context):
    update.message.reply_text("""To do this, I'm going to need some information from you.
    What do you want to conver from and what currency do you want to convert to?
    Please type in your choices in a 'currency1 to curreny2' format
    E.G 'USD to GBP'""")


def get_exchange_rate(update, context):
    choices = str(update.message.text).split()

    if len(choices) > 3 or len(choices) < 3:
        update.message.reply_text(
            "Seems you didnt type in your choices in the specified format.",
            "use the command /exchangerate to retry."
        )
    else:
        convert_to = choices[-1]
        convert_from = choices[0]

        api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={convert_from}_{convert_to}'
        response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_TOKEN')})
        res = response.json()
        rate = res['exchange_rate']
        answer = f'Currently the exchange rate of {convert_to} to {convert_from} is {rate}.\nIn other words, one {convert_from} is equal to {rate} {convert_to}'
        if response.status_code == requests.codes.ok:
            update.message.reply_text(answer)
        else:
            update.message.reply_text('Error:', response.status_code, response.text)


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


def done():
    # TODO: Complete /done command to allow user end interaction with bot
    pass


def main():
    updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('exchangerate', exchange_rate))
    dp.add_handler(CommandHandler('jokes', jokes))

    # dp.add_handler(MessageHandler(Filters.text, unknown))
    dp.add_handler(MessageHandler(Filters.text, get_exchange_rate))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
