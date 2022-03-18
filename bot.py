import requests
import os

from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters
)

from dotenv import load_dotenv
from time import sleep

load_dotenv()

API_NINJA_TOKEN = os.getenv('API_NINJA_TOKEN')

def start(update, context):
	update.message.reply_text(
		"Hi! I'm here to help you with all your currency conversion needs.\nYou can find out how to use me by sending a /help command")


def help(update, context):
	update.message.reply_text("""Available Commands:
	/exchangerate - Get the exchange rate between two currencies
	/convertcurrency - Convert one currency to another
	/jokes - To help you crack a smile just in case you're feeling blue :)\n/done - To say goodbye """)


def exchange_rate(update, context):
    update.message.reply_text("""To do this, I'm going to need some information from you.
    What currency do you want to convert from and what currency do you want to convert to?
    Please type in your choices in a 'currency1 to curreny2' format
    E.G 'USD to GBP'""")


def get_exchange_rate(update, context):
    choices = str(update.message.text).split()

    if len(choices) > 3 or len(choices) < 3:
        update.message.reply_text(
            """Seems you didn't type in your choices in the specified format. Use the command /help to retry the operation."""
        )
    else:
        convert_to = choices[-1]
        convert_from = choices[0]

        api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={convert_from}_{convert_to}'
        response = requests.get(api_url, headers={'X-Api-Key': API_NINJA_TOKEN})
        res = response.json()
        rate = res['exchange_rate']
        answer = f'Currently the exchange rate of {convert_to} to {convert_from} is {rate}.\nIn other words, one {convert_from} is equal to {rate} {convert_to}'
        if response.status_code == requests.codes.ok:
            update.message.reply_text(answer)
        else:
            update.message.reply_text('Error:', response.status_code, response.text)


def convert_currency(update, context):
    update.message.reply_text("""To do this, I'm going to need some information from you.
    What currency do you want to convert from and what currency do you want to convert to?
    Please type in your choices in a 'currency1 to curreny2' format
    E.G '50000 USD to GBP'""")


def get_converted_currency(update, context):
    choice = str(update.message.text).split()

    if len(choice) > 4 or len(choice) < 4:
        update.message.reply_text(
            """Seems you didn't type in your choices in the specified format. Use the command /help to retry the operation."""
        )
    else:
        want = choice[-1]
        have = choice[1]
        amount = choice[0]
        api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={want}&have={have}&amount={amount}'
        response = requests.get(api_url, headers={'X-Api-Key': API_NINJA_TOKEN})
        res = response.json()
        new_amount = res['new_amount']
        old_amount = res['old_amount']
        old_currency = res['old_currency']
        new_currency = res['new_currency']
        answer = f'Currently, {old_amount} {old_currency} is equvalent to {new_amount} {new_currency} '
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


def done(update, context):
    update.message.reply_text(
        """Thanks for coming around, I hope to see you again sometime😄. And remeber, to spend some time with me again, you just have to type in /start😉"""
    )


def main():
    updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('exchangerate', exchange_rate))
    dp.add_handler(CommandHandler('convertcurrency', convert_currency))
    dp.add_handler(CommandHandler('jokes', jokes))
    dp.add_handler(CommandHandler('done', done))

    dp.add_handler(MessageHandler(Filters.text, get_exchange_rate))
    dp.add_handler(MessageHandler(Filters.text, get_converted_currency))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    print('Activating bot server...')
    sleep(2.00)
    print('Your bot is up and running :)')
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
