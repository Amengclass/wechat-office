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


# 从微信 API 获取访问令牌的函数
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


# 获取天气信息
def get_weather(city_id, location):
    """
       获取天气信息。
       Args:
           city_id (str): 城市 ID，用于调用高德天气 API
           location (str): 城市名称，用于调用和风天气 API

       Returns:
           dict: 包含天气信息的字典对象，包括链接、日期、城市、温度、天气状况、风向、日出和日落时间。
       """
    # 高德
    url1 = r'https://restapi.amap.com/v3/weather/weatherInfo?city={0}&key={1}'.format(
        city_id, config['weather']['gd_key'])
    response1 = requests.get(url1)  # 发送请求获取天气信息
    data1 = response1.json()
    print(data1)

    # 获取城市id
    url_id = r'https://geoapi.qweather.com/v2/city/lookup?location={0}&key={1}'.format(
        location, config['weather']['hf_key'])
    response_id = requests.get(url_id)
    data_id = response_id.json()
    hf_cityid = data_id['location'][0]['id']

    url2 = r'https://devapi.qweather.com/v7/weather/3d?location={0}&key={1}'.format(
        hf_cityid, config['weather']['hf_key'])
    response2 = requests.get(url2)
    data2 = response2.json()
    print(data2)

    # 城市
    city = data1['lives'][0]['city']
    #
    # 温度
    temp = {}
    temp['today'] = data2['daily'][0]['tempMin'] + u'°C' + '~' + data2['daily'][0]['tempMax'] + u'°C'
    temp['now'] = data1['lives'][0]['temperature'] + u'°C'
    #
    # 天气状况
    weather = data1['lives'][0]['weather']

    # 风向
    win = data1['lives'][0]['winddirection'] + u'风 ' + data1['lives'][0]['windpower'] + u'级'

    # 日期
    date = data2['daily'][0]['fxDate']

    sum_time = {}
    # 日出和日落时间
    sum_time["sunrise"] = data2['daily'][0]['sunrise']
    sum_time["sunset"] = data2['daily'][0]['sunset']

    return {'link': data2['fxLink'], 'date': date, 'city': city, 'temp': temp, 'wea': weather, 'win': win,
            "sun_time": sum_time}


# 彩虹屁
def get_rainbow():
    """
        获取彩虹屁。
        Returns:
            str: 彩虹屁文本。
    """
    url = 'https://v1.hitokoto.cn/'
    response = requests.get(url)
    data = response.json()
    print(data["hitokoto"])
    return data["hitokoto"]


# 发送消息
def send_message(touser, token, info, rainbow_text):
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
        "url": info['link'],
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": info['date'],
                "color": "#000"
            },
            "city": {
                "value": info['city'],
                "color": "#000"
            },
            "weather_now": {
                "value": info['wea'],
                "color": "#000"
            },
            "temprature_now": {
                "value": info['temp']['now'],
                "color": "#000"
            },
            "temprature_today": {
                "value": info['temp']['today'],
                "color": "#000"
            },
            "win": {
                "value": info['win'],
                "color": "#000"
            },
            "rainbow": {
                "value": rainbow_text,
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
    info = get_weather(city_id="450323",location="灵川") # 把这里的city_id改为自己城市id，location改为自己城市名字
    rainbow_text = get_rainbow()

    # 要推送的用户
    touser = config["template"]["touser"]
    # send_message(touser, token, info, rainbow_text)
    # 循环推送
    for i in touser:
        if i == "oObnS6kT9reaXqGWZAYE393QK0EI":
            info = get_weather(city_id="440400", location="珠海")
        send_message(i, token, info, rainbow_text)
