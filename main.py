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
    elif input[:3] == "素数:":
        try:
            num_len = [2]
            num_len2 = [4]
            num_len3 = 1
            for num in range(3, 10000, 2):
                if  num > num_len2[num_len3-1]:
                    num_len3 = num_len3 + 1
                flag =  True
                for i in range(1,num_len3):
                    if num % num_len[i] == 0:
                        flag = False
                        break
                if flag:
                    num_len.append(num)
                    num_len2.append(num**2)
                if len(num_len) == int(input[3:]):
                    return message(str(num_len[input[3:]]))
        except:
            text = "例(素数:10)"

    else:
        ans = cal.cal(input)
        if ans != "err":
            text = "計算結果\n"+str(ans)+"\n正しくないかも？"
        else:
            text = "hello"
    
    return message(text)
