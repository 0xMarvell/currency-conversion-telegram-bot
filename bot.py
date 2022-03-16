from dotenv import load_dotenv
import requests
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

from dotenv import load_dotenv

load_dotenv()

# api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want=EUR&have=NGN&amount=50000'
# response = requests.get(api_url, headers={'X-Api-Key': '6z3Qq8IuUoESg4EDBkx5TQ==wRKIwlp2ERcUIH7t'})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)

updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi! I'm here to help you with all your currency conversion needs :) \nYou can find out how to use me by sending a /help command")


# def help(update: Update, context: CallbackContext):
# 	update.message.reply_text("""Available Commands :-
# 	/youtube - To get the youtube URL
# 	/linkedin - To get the LinkedIn profile URL
# 	/gmail - To get gmail URL
# 	/geeks - To get the GeeksforGeeks URL""")


# def gmail_url(update: Update, context: CallbackContext):
# 	update.message.reply_text(
# 		"Your gmail link here (I am not\
# 		giving mine one for security reasons)")


# def youtube_url(update: Update, context: CallbackContext):
# 	update.message.reply_text("Youtube Link =>\
# 	https://www.youtube.com/")


# def linkedIn_url(update: Update, context: CallbackContext):
# 	update.message.reply_text(
# 		"LinkedIn URL => \
# 		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


# def geeks_url(update: Update, context: CallbackContext):
# 	update.message.reply_text(
# 		"GeeksforGeeks URL => https://www.geeksforgeeks.org/")


# def unknown(update: Update, context: CallbackContext):
# 	update.message.reply_text(
# 		"Sorry '%s' is not a valid command" % update.message.text)


# def unknown_text(update: Update, context: CallbackContext):
# 	update.message.reply_text(
# 		"Sorry I can't recognize you , you said '%s'" % update.message.text)


# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
# updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
# updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# updater.dispatcher.add_handler(MessageHandler(
# 	Filters.command, unknown)) # Filters out unknown commands

# # Filters out unknown messages.
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# updater.start_polling()
