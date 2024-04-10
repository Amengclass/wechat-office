# -*- coding: utf-8 -*-
# @Author: xhf
# @Date:   2024.4.1

import requests
import json
import os

config_path = os.path.join(os.path.dirname(__file__), "config.json")

# 从config.json中读取配置信息
def read_config():
    """
       读取配置文件并返回配置内容。

       Returns:
           dict: 包含配置信息的字典对象，如果文件不存在或解析失败，则返回空字典。
       """
    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def updata_config():
    """
       将配置信息写入配置文件。

       Args:
           config_path (str): 配置文件路径。
       """
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

config = read_config()

# 从微信 API 获取访问令牌的函数
def get_stable_token(AppID=config["wechat"]["AppID"], AppSecret=config["wechat"]["AppSecret"]):
    """
            获取微信 access_token。

            Args:
                AppID (str): 微信应用的 AppID。
                AppSecret (str): 微信应用的 AppSecret。

            Returns:
                str: 获取到的 access_token。
            """
    url = "https://api.weixin.qq.com/cgi-bin/stable_token?"
    data = \
        {
            "grant_type": "client_credential",
            "appid": AppID,
            "secret": AppSecret
        }
    data = json.dumps(data)
    response = requests.post(url, data=data)

    res = response.json()
    print(res)
    # 更新配置文件
    access_token = res["access_token"]
    config["wechat"]["access_token"] = access_token

    updata_config()
    return access_token


# 获取天气信息
def get_weather(location):
    """
        获取指定位置的天气信息。

        参数:
            location (str): 指定的位置信息。

        返回:
            dict: 包含天气信息的字典，包括以下键值对：
                - 'link' (str): 天气信息的链接。
                - 'date' (str): 日期。
                - 'city' (str): 城市名称。
                - 'temp' (dict): 包含温度信息的字典，包括 'today' 和 'now' 两个键值对，分别表示今天的最低和最高温度以及当前温度。
                - 'wea' (dict): 包含天气状况信息的字典，包括 'now'、'day'、'night' 和 'text' 四个键值对，分别表示当前天气、白天天气、夜晚天气以及总体天气描述。
                - 'win' (str): 风向和风力信息。
                - 'sun_time' (dict): 包含日出和日落时间的字典，分别表示 'sunrise' 和 'sunset'。

        异常:
            - requests.exceptions.RequestException: 网络请求异常。
            - json.JSONDecodeError: JSON解析异常。
        """
    city_id_url1 = r'https://restapi.amap.com/v3/geocode/geo?address={0}&key={1}'.format(location,
                                                                                         config['weather']['gd_key'])
    response_id = requests.get(city_id_url1)
    data_id = response_id.json()
    gd_cityid = data_id['geocodes'][0]['adcode']

    # 高德
    url1 = r'https://restapi.amap.com/v3/weather/weatherInfo?city={0}&key={1}'.format(
        gd_cityid, config['weather']['gd_key'])
    response1 = requests.get(url1)  # 发送请求获取天气信息
    data1 = response1.json()
    print(data1)

    # 获取城市id
    city_id_url2 = r'https://geoapi.qweather.com/v2/city/lookup?location={0}&key={1}'.format(
        location, config['weather']['hf_key'])
    response_id = requests.get(city_id_url2)
    data_id = response_id.json()
    hf_cityid = data_id['location'][0]['id']

    url2 = r'https://devapi.qweather.com/v7/weather/3d?location={0}&key={1}'.format(
        hf_cityid, config['weather']['hf_key'])
    response2 = requests.get(url2)
    data2 = response2.json()
    print(data2)

    # url3 = r'https://devapi.qweather.com/v7/weather/24h?location={0}&key={1}'.format(
    #     hf_cityid, config['weather']['hf_key'])
    # response3 = requests.get(url3)
    # data3 = response3.json()
    # print(data3)
    # 城市
    city = data1['lives'][0]['city']
    # 温度
    temp = {}
    temp['today'] = data2['daily'][0]['tempMin'] + u'°C' + '~' + data2['daily'][0]['tempMax'] + u'°C'
    temp['now'] = data1['lives'][0]['temperature'] + u'°C'
    #
    # 天气状况
    weather = {}
    weather['now'] = data1['lives'][0]['weather']
    weather['day'] = data2['daily'][0]['textDay']
    weather['night'] = data2['daily'][0]['textNight']
    weather['text'] = u"今天白天有" + data2['daily'][0]['textDay'] + u"，" + u"夜晚有" + data2['daily'][0]['textNight']

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
            "weather_text":{
                "value": info['wea']['text'],
                "color": "#000"
            },
            "weather_now": {
                "value": info['wea']['now'],
                "color": "#000"
            },
            "weather_day": {
                "value": info['wea']['day'],
                "color": "#000"
            },
            "weather_night": {
                "value": info['wea']['night'],
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
    #获取token,获取后会更新到配置文件中
    get_stable_token(config["wechat"]["AppID"], config["wechat"]["AppSecret"])

    # 从配置中获取token
    token =  config["wechat"]["access_token"]
    info = get_weather(location="北京")  # 获取天气信息 # 把这里的location改为自己城市名字
    rainbow_text = get_rainbow()

    # 要推送的用户
    touser = config["template"]["touser"][0]
    send_message(touser, token, info, rainbow_text)

    # 推送给多个用户：用for循环即可
    # 循环推送
    # for i in touser:
    #     send_message(i, token, info, rainbow_text)
