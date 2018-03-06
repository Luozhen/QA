#!usr/bin/env python
# coding:utf-8

import json
import requests
from wxpy import *

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "你的api key"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]

bot = Bot(cache_path=True)
found_mp = bot.search('CherishLzh')[0]

@bot.register(found_mp)
def forward_message(msg):
    return auto_reply(msg.text)

embed()
Bot.join()