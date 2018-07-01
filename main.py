from linebot.models import (
    TextSendMessage, ImageSendMessage,
)

def create_message(input):

    if input == "test":
        message = TextSendMessage(text = 'test')
    if input == "hack":
        # 1. 固定メッセージを返す
        message = TextSendMessage(text = 'Hack Time!')

    return message
