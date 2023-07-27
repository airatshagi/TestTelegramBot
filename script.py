import json
import requests
from os import getenv
from dotenv import load_dotenv
from fake_useragent import UserAgent
from time import sleep

load_dotenv()
sites_list = json.loads(getenv("sites_list"))
time_interval_minutes = int(getenv("time_interval_minutes")) * 60

telegram_token = getenv("telegram_token")
telegram_chat_id = getenv("telegram_chat_id")

useragent_fake_user = UserAgent()
sites_headers = {
    "User-Agent": useragent_fake_user.chrome
}


def test_sites():
    while True:
        for site_value in sites_list.values():
            url_answer = requests.head(site_value.rstrip(), headers=sites_headers, timeout=5)
            answer_code = url_answer.status_code

            if answer_code != 200:
                text_message = f"site: {site_value} ; status code: {answer_code}"
                url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&text={text_message}"
                requests.get(url)

            sleep(1)

        sleep(time_interval_minutes)


test_sites()
