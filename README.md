## wecat公众号推送模板

​	最近在社交媒体上热传的情侣天气推送项目，使用 Python 编写了一个可定制化的模板消息发送功能。这个项目不仅能够发送天气信息，还通过整合免费 API 实现了发送更多有趣的内容，如每日星座运势、搞笑段子等。

## 主要功能

- **天气信息推送：** 通过调用天气 API 获取实时的天气情况，并以模板消息的形式发送给用户。
- **自定义内容：** 利用免费的 API 获取各种有趣的内容，例如每日星座运势、搞笑段子等，并与天气信息一起发送给用户。
- **灵活配置：** 用户可以根据自己的需求灵活配置模板消息的内容，包括天气、星座运势、段子等。



## 如何使用

1. **克隆仓库：** `git clone https://github.com/Amengclass/wechat-office.git`
2. **安装依赖：** 使用 `pip install -r requirements.txt` 安装所需的 Python 包。
3. **配置参数：** 在 `config.json` 文件中填写相关信息，如微信公众号的 AppID、AppSecret、模板ID 等。
4. **运行程序：** 执行 `python tianqi.py` 开始发送模板消息给用户。



## 贡献者

- [Amengclass (剑姬同学)](https://github.com/Amengclass)
- [其他贡献者](https://github.com/yourusername/douyin-couple-weather/contributors)

## 反馈与建议

如果您有任何问题、建议或者发现了 bug，请随时提出 [Issues](https://github.com/Amengclass/wechat-office/issues)，我们会尽快处理。感谢您的贡献！





## 使用详细教程

#### 首先访问 https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

登录后台得到appID 和 appsecret  分别填入`config.json文件`中
![image](https://user-images.githubusercontent.com/110412182/186095663-3146adbf-a6e3-4e55-8add-41079d77b870.png)

修改到这个部分

<img src="./img/0.png" alt="0" style="zoom: 80%;" />



### test.py 测试用的

可以收到通知，自定义内容


#### 1、新建的模板 (用于test.py)

```
测试1：{{date.DATA}}
测试2：{{city.DATA}} 
测试3：{{weather_now.DATA}} 
测试4：{{temprature_now.DATA}}
测试5：{{temprature_today.DATA}}
测试6：{{win.DATA}}
测试7：{{rainbow.DATA}}
```

<img src="./img/1.png" alt="1" style="zoom: 50%;" />

添加成功后如图：将模版ID复制下来

<img src="./img/2.png" alt="2" style="zoom:50%;" />

然后修改进到`config.json`里

<img src="./img/3.png" alt="3" style="zoom:50%;" />

写到这；扫二维码关注后可以看见多了用户的微信号信息，放到上边的`touser`里就好。
<img src="./img/4.png" alt="4" style="zoom:50%;" />

#### 2、运行

请确认`config.json`的以下部分被填写了

```json
 #这是微信注册号
  "wechat": { 
    "AppID": "",   #这里填微信测试号的appId
    "AppSecret": "" #这里填微信测试号的appsecret
  },
#这里是配置的模版部分
  "template": {
    "touser": "",   #这里填推送用户id
    "template_id": "", #这里填模板id
    "url": "" #这里填点击模板想要跳转到界面，例如www.baidu.com
  }
```



#### 3、效果

<img src="./img/5.jpg" alt="5" style="zoom:50%;" />





### tianqi.py  天气推送

效果图

<img src="./img/6.jpg" alt="6" style="zoom:50%;" />

别的功能大家酌情增加吧

同上，新建模板然后替换模板id   ʕ•ᴥ•ʔ

##### 模版

```python
🗓️今天是{{date.DATA}} o(〃'▽'〃)o
🏙️城市：{{city.DATA}} ヾ(≧▽≦*)o
🎈凤向：{{win.DATA}}╰(*°▽°*)╯
⛅️今日天气(❁´◡`❁)
	 描述:{{weather_text.DATA}}
     当前：{{weather_now.DATA}} 
     白天：{{weather_day.DATA}} 
     夜晚：{{weather_night.DATA}} 
🌡️温度：{{temprature_now.DATA}}
   范围：{{temprature_today.DATA}}

每日一言：🌈{{rainbow.DATA}}🌈
```



这里用到天气的api，所以需要申请相关的key配置一下

##### [高德天气(点击跳转)](https://console.amap.com/dev/index)

###### 注册登录

<img src="./img/7.png" alt="7" style="zoom: 33%;" />

###### 然后创建key即可

<img src="./img/8.png" alt="8" style="zoom: 50%;" />

把这个key复制下来，修改进`config.json`文件里

<img src="./img/10.png" alt="10" style="zoom: 80%;" />



##### [和风天气(点击跳转)](https://id.qweather.com/#/login?redirect=https%3A%2F%2Fconsole.qweather.com)

###### 注册登录

<img src="./img/11.png" alt="11" style="zoom:80%;" />

###### 然后添加key

<img src="./img/12.png" alt="12" style="zoom:50%;" />

<img src="./img/13.png" alt="13" style="zoom: 60%;" />

同样的把这个key复制下来替换进`config.json`中

<img src="./img/14.png" alt="14" style="zoom:50%;" />

<img src="./img/15.png" alt="15" style="zoom: 67%;" />

也就是`添加了两个key`

运行 tianqi.py 即可

```
python tianqi.py
```

### config.json修改说明

```json
{#这是微信注册号
    "wechat": {
        "AppID": "",
        "AppSecret": "",#这里填微信测试号的appId
        "access_token": ""#这里填微信测试号的appsecret
    },
    "weather": {
        "gd_key": "",#这里填高德天气key
        "hf_key": ""#这里填和风天气key
    },
    "template": {
        "touser": [
            "",
            ""
        ],#这里填推送用户id
        "template_id": ""#这里填模板id
    }
}
```



### 免费服务器托管自动运行：每天自动推送

#### 1、[点击打开pythonanywhere](https://www.pythonanywhere.com/)![16](./img/16.png)

#### 2、点击进行注册

<img src="./img/18.png" alt="18" style="zoom: 67%;" />

#### 3、注册成功后的界面

<img src="./img/19.png" alt="19" style="zoom:67%;" />

如果看不懂英文，就将页面转为中文即可

选择右上角的`Files`

<img src="./img/20.png" alt="20" style="zoom:50%;" />



#### 4、新建文件夹

​	我这里叫做	`wechat`(随便起什么名字都可以)，然后点击`New directory`

<img src="./img/21.png" alt="21" style="zoom: 67%;" />



#### 5、点击上传文件

选择`config.json`和`tianqi.py`文件进行上传

<img src="./img/22.png" alt="22" style="zoom: 67%;" /><img src="./img/23.png" alt="23" style="zoom:80%;" />

#### 6、试运行

​	双击`tianqi.py`文件，试运行，确保配置正确

![25](./img/25.png)

如果到这里都没有问题，说明配置都已经正确，接下来我们设定定时任务自动运行

返回到主页，选择`Tasks`

![26](./img/26.png)



#### 7、然后添加一个定时任务![27](./img/27.png)

- [ ] 首先时间：

​		与北京时间有8小时时差，自己算即可，如果你是想中午12点推送，那么12-8＝4，所以你就设定4:00 utc即可

- [ ] 其次是Command or path to script(eg./home/yourusername/yourscrip.py）

  ```python
  cd /home/xhf/wechat && python tianqi.py
  ```

其中`/home/xhf/wechat`是我之前上传到的文件夹路径，怎么看呢？

你只需要打开你存储py文件的那个文件夹，然后复制左上角即可，如果你的存储文件夹名称和我一样是`wechat`，那么你只需修改xhf为你的账户名称即可

<img src="./img/28.png" alt="28" style="zoom: 67%;" />

- [ ] 最后Optional description

 随便填写什么任务描述都可以



如图，就配置好了自动任务，我的在每天的早上7点，就会运行，推送消息了

![29](./img/29.png)

### 附录

#### test.py代码

```python
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
    token = get_stable_token(config["wechat"]["AppID"], config["wechat"]["AppSecret"])
    # 要推送的用户
    touser = config["template"]["touser"][0]
    send_message(touser, token)
```



#### tianqi.py代码

```python
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

```









