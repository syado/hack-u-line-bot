from linebot.models import (
    TextSendMessage, ImageSendMessage,
)
import requests
import cal

def message(text):
    return TextSendMessage(text)
    
def create_message(input):

    if input == "test":
        text = 'test'
    elif input == "hack":
        text = 'Hack Time!'
    elif input.lower() in {"btc","bitcoin","ビットコイン"}:
        bf = 'https://lightning.bitflyer.jp/v1/ticker?product_code='
        b_btc_jpy  = "{0:>10}".format(str(requests.get(bf + 'BTC_JPY').json()['ltp']))
        text = 'BitCoin : ' + b_btc_jpy + ' JPY'
    else:
        ans = cal(input)
        if ans != "err":
            text = "計算結果\n"+ans
        else:
            text = "hello"
    
    return message(text)
