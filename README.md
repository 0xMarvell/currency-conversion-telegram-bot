# CURRENCY CONVERSION TELEGRAM BOT
A script for running a Telegram bot that can:
 - Convert money amounts from one currency to another.
 - Fetch the latest exchange rates between available currencies.
 - Tell a random joke to users 😄.

It performs these tasks by fetching data from [API Ninja's](https://api-ninjas.com/) free APIs:
 -  [The exchange rate API.](https://api-ninjas.com/api/exchangerate)
 - [The convert currency API.](https://api-ninjas.com/api/convertcurrency)
 - [The jokes API.](https://api-ninjas.com/api/jokes)

You can test out the bot using the link provided in the repo description above.

## Before you can run this project (locally)
 - Make sure to have [python 3.10](https://www.python.org/downloads/) installed on your local mahcine.
 - Create an [API Ninja account](https://www.spotify.com/signup/). You'll need the API key from your account dashboard for this to work.
 - Open a [Telegram account](https://telegram.org/) (if you don't already have one).
 - Create your Telegram bot. You can do this using this [guide.](https://core.telegram.org/bots#6-botfather). You will also need to take note of the telegram link provided after creating your bot.

### Using your app API key and Telegram token as environment variables
After creating your API Ninja account and your Telegram bot, you'll need to:
 - Navigate to your account dahsboard and take note of your API key.
 - Take note of the API token provided for you after creating your Telegram bot.

They're both vital credentials and should be added to this script as environment variables. Learn how to set environment variables for python projects using this [guide](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1).

 - Note that your environment variables should be named `TELEGRAM_TOKEN` and `API_NINJA_TOKEN` respectively.

## Run project
 - Clone project.
    ```bash
    git clone https://github.com/Marvellous-Chimaraoke/currency-conversion-telegram-bot.git
    ```
 - Open project folder in text editor (VSCode, Atom, etc).
 - Create virtual environment using the terminal.
    ```bash
    python3.10 -m venv env
    ```
 - Activate virtual environment (MacOS/Linux/Git Bash).
   ```bash
   source env/bin/activate
   ```
 - Activate virtual environment (Windows).
   ```powershell
   env/bin/activate.ps1 (powershell)
   env/bin/activate.bat (command prompt)
   ```
 - Install all required packages.
   ```bash
   pip install -r requirements.txt
   ```
 - In `bot.py` file, uncomment line 170 and comment out lines 172 - 177 then save file.
    ```python
      # Start the Bot (locally)
      # Uncomment the line of code below
      # updater.start_polling() 
      
      # Start the bot (Hosting on Heroku)
      # Comment out the lines of code below
      updater.start_webhook(
          listen="0.0.0.0",
          port=int(PORT),
          url_path=TELEGRAM_TOKEN,
          webhook_url='https://mrcurrency.herokuapp.com/' + TELEGRAM_TOKEN
          )
    ```
 - Run python script. It will act as a local server for your Telegram bot.
   ```bash
   python bot.py
   ```

A message will pop up in your terminal to confirm that your bot is up and running. All you have to do is access your telegram bot using the link provided to you when you created the bot.
