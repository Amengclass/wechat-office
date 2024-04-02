# -*- coding: utf-8 -*-
# @Author: xhf
# @Date:   2024.4.1

import requests
import json


# 从config.json中读取配置信息
def read_config():
    """
       读取配置文件并返回配置内容。

       Returns:
           dict: 包含配置信息的字典对象，如果文件不存在或解析失败，则返回空字典。
       """
    with open('config.json', 'r') as file:
        return json.load(file)

config = read_config()

def get_token(AppID, AppSecret):
    """
        获取微信 access_token。

        Args:
            AppID (str): 微信应用的 AppID。
            AppSecret (str): 微信应用的 AppSecret。

        Returns:
            str: 获取到的 access_token。
        """
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(AppID,
                                                                                                             AppSecret)

    r = requests.get(url)
    data = json.loads(r.text)
    return data["access_token"]

# 发送消息
def send_message(touser, token, info=None, rainbow_text=None):
    """
        发送消息。
        Args:
            touser (str): 接收消息的用户 openid。
            token (str): 微信 access_token。
            info (dict): 包含天气信息的字典。
            rainbow_text (str): 彩虹屁文本。
    """
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'.format(token)
    data = {
        "touser": touser,
        "template_id": config["template"]["template_id"],
        # "url": info['link'],
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": "你好",
                "color": "#000"
            },
            "city": {
                "value": "没问题",
                "color": "#000"
            },
            "weather_now": {
                "value": "我的测试",
                "color": "#000"
            },
            "temprature_now": {
                "value": "太多了吧",
                "color": "#000"
            },
            "temprature_today": {
                "value": "啦啦啦啦",
                "color": "#000"
            },
            "win": {
                "value": "sdfsf",
                "color": "#000"
            },
            "rainbow": {
                "value": "sfsdf",
                "color": "#000"
            }
        }
    }
    response = requests.post(url=url, data=json.dumps(data))
    if response.json()['errmsg'] == 'ok':
        print('\033[91m' + '推送成功' + '\033[0m')  # 输出红色文字
    else:
        print('\033[91m' + '推送失败' + '\033[0m')  # 输出红色文字


if __name__ == '__main__':
    token = get_token(config["wechat"]["AppID"], config["wechat"]["AppSecret"])
    # 要推送的用户
    touser = config["template"]["touser"]
    send_message(touser, token)
