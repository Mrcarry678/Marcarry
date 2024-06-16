import schedule
import time
import requests
from subprocess import call

# Telegram bot API token and chat ID
bot_token = 'your_bot_token_here'
chat_id = 'your_chat_id_here'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    requests.post(url, params=params)

def open_py_file():
    call(["python", "m.py"])
    send_telegram_message("Server On")

def server_on():
    send_telegram_message("Server On")

def server_off():
    send_telegram_message("Server Off")

def check_server_info():
    try:
        # Replace 'github_cloudspace_url' with the actual URL of your GitHub Cloudspace
        response = requests.get('github_cloudspace_url')
        if response.status_code == 200:
            send_telegram_message(f"Server Info: {response.json()}")
        else:
            send_telegram_message("Failed to fetch server info")
    except Exception as e:
        send_telegram_message(f"Error: {e}")

open_py_file()

schedule.every(86400).seconds.do(open_py_file)
schedule.every().day.at("00:00").do(server_on)
schedule.every().day.at("23:59").do(server_off)
schedule.every().hour.do(check_server_info)  # Check server info every hour

while True:
    schedule.run_pending()
    time.sleep(1)