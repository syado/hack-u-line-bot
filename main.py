from linebot.models import (
    TextSendMessage, ImageSendMessage,
)
import requests

def create_message(input):

    if input == "test":
        message = TextSendMessage(text = 'test')
    if input == "hack":
        message = TextSendMessage(text = 'Hack Time!')
    if input.lower() in {"btc"}:
        bf = 'https://lightning.bitflyer.jp/v1/ticker?product_code='
        b_btc_jpy  = "{0:>10}".format(str(requests.get(bf + 'BTC_JPY').json()['ltp']))
        message = TextSendMessage(text = 'btc : ' + b_btc_jpy + ' JPY\n')

    return message
