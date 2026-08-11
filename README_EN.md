<div align="center">

# 💌 WeChat Office

> A WeChat Official Account template-message push tool written in Python — automatically sends weather, daily quotes and horoscope to your loved one every day.

[中文](README.md) | **English**

[![Stars](https://img.shields.io/github/stars/Amengclass/wechat-office?style=social)](https://github.com/Amengclass/wechat-office/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Amengclass/wechat-office?color=blue)](https://github.com/Amengclass/wechat-office/commits/master)
[![Built with](https://img.shields.io/badge/built%20with-Python-3776AB.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Amengclass/wechat-office/pulls)

</div>

## ✨ Features

- **Weather push** — Fetches real-time weather from two free APIs (AMap + QWeather) and sends it to your Official Account as a template message
- **Daily quote** — Integrates the free hitokoto API to push a quote / compliment every day
- **Customizable template** — Template content is fully defined by you, emoji supported, get creative
- **Flexible configuration** — All settings live in `config.json`; change city, template or recipient without touching the code
- **Free scheduled push** — Step-by-step PythonAnywhere hosting guide included, so it runs automatically every day
- **Multiple recipients** — `touser` accepts an array; push to many people with one script

## 🖼️ Preview

| `test.py` (test push) | `tianqi.py` (weather push) |
| :---: | :---: |
| <img src="./img/5.jpg" width="70%"> | <img src="./img/6.jpg" width="70%"> |

## 🚀 Quick Start

1. **Clone the repository** and enter the directory:

   ```bash
   git clone https://github.com/Amengclass/wechat-office.git
   cd wechat-office
   ```

2. **Install dependencies** (the only dependency is `requests`):

   ```bash
   pip install requests
   ```

3. **Configure**: edit `config.json` with the sandbox account's AppID, AppSecret, template ID and weather API keys (see the [detailed tutorial](#-detailed-tutorial) for how to get them)

4. **Run the push**:

   ```bash
   python tianqi.py
   ```

   A red `推送成功` (push succeeded) message means it worked. The default city is **Beijing** — change `location="北京"` in `tianqi.py` to your own city.

## ⚙️ Configuration

Everything lives in `config.json`:

```json
{
  "wechat": {
    "AppID": "",
    "AppSecret": "",
    "access_token": ""
  },
  "weather": {
    "gd_key": "",
    "hf_key": ""
  },
  "template": {
    "touser": [""],
    "template_id": ""
  }
}
```

| Field | Description |
| --- | --- |
| `wechat.AppID` | Sandbox account AppID ([apply here](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)) |
| `wechat.AppSecret` | Sandbox account AppSecret |
| `wechat.access_token` | Written automatically on first run — leave it empty |
| `weather.gd_key` | AMap weather API key ([apply here](https://console.amap.com/dev/index)) |
| `weather.hf_key` | QWeather weather API key ([apply here](https://id.qweather.com/)) |
| `template.touser` | Recipients' openids (array; multiple allowed) |
| `template.template_id` | Template ID created in the WeChat backend |

> ⚠️ Note: the JSON above is **valid and ready to use**. Do NOT put `#` comments inside JSON, or the script will fail to parse it.

## 📖 Detailed Tutorial

### 1️⃣ Get the sandbox AppID / AppSecret

Open the [WeChat sandbox test account](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login), scan the QR code to log in, and copy the `appID` and `appsecret` from the page:

![WeChat sandbox backend](https://user-images.githubusercontent.com/110412182/186095663-3146adbf-a6e3-4e55-8add-41079d77b870.png)

Fill them into `config.json`:

<img src="./img/0.png" alt="edit config.json" width="80%">

### 2️⃣ Create a template & run test.py

In the WeChat backend, add a test template with these fields (used by `test.py`):

```text
测试1：{{date.DATA}}
测试2：{{city.DATA}}
测试3：{{weather_now.DATA}}
测试4：{{temprature_now.DATA}}
测试5：{{temprature_today.DATA}}
测试6：{{win.DATA}}
测试7：{{rainbow.DATA}}
```

<img src="./img/1.png" alt="create test template" width="60%">

Once created, copy the template ID:

<img src="./img/2.png" alt="template ID" width="60%">

Paste it into `config.json`:

<img src="./img/3.png" alt="fill template ID" width="60%">

After following the account, the sandbox page shows each follower's openid — put yours into `touser`:

<img src="./img/4.png" alt="get user openid" width="60%">

Run it:

```bash
python test.py
```

If you receive the message, your configuration is correct (see the preview above).

### 3️⃣ Weather push with tianqi.py

Create another template and swap in its template ID. The template content is up to you (emoji welcome ʕ•ᴥ•ʔ):

```text
🗓️今天是{{date.DATA}} o(〃'▽'〃)o
🏙️城市：{{city.DATA}} ヾ(≧▽≦*)o
🎈风向：{{win.DATA}}╰(*°▽°*)╯
⛅️今日天气(❁´◡`❁)
	 描述:{{weather_text.DATA}}
     当前：{{weather_now.DATA}}
     白天：{{weather_day.DATA}}
     夜晚：{{weather_night.DATA}}
🌡️温度：{{temprature_now.DATA}}
   范围：{{temprature_today.DATA}}

每日一言：🌈{{rainbow.DATA}}🌈
```

Weather data comes from two free APIs — AMap and QWeather — each needs its own key (see step 4). Then run:

```bash
python tianqi.py
```

See the preview above for the result.

### 4️⃣ Apply for weather API keys

#### AMap (高德)

Register / log in to the [AMap Open Platform](https://console.amap.com/dev/index):

<img src="./img/7.png" alt="AMap register" width="40%">

Create a key (choose "Web service" type):

<img src="./img/8.png" alt="AMap create key" width="60%">

Copy the key into `gd_key` in `config.json`:

<img src="./img/10.png" alt="fill AMap key" width="80%">

#### QWeather (和风)

Register / log in to the [QWeather Console](https://id.qweather.com/):

<img src="./img/11.png" alt="QWeather register" width="80%">

Add a key:

<img src="./img/12.png" alt="QWeather add key" width="60%">

<img src="./img/13.png" alt="QWeather key detail" width="60%">

Copy the key into `hf_key` in `config.json`:

<img src="./img/14.png" alt="fill QWeather key" width="60%">

<img src="./img/15.png" alt="both keys filled" width="67%">

With both keys in place, run `python tianqi.py` and you'll start receiving weather pushes.

### 5️⃣ Free hosting: scheduled push every day

Use free [PythonAnywhere](https://www.pythonanywhere.com/) to run the script automatically on a schedule:

<img src="./img/16.png" alt="PythonAnywhere homepage" width="80%">

**① Sign up**

Click register:

<img src="./img/18.png" alt="PythonAnywhere sign up" width="67%">

The dashboard after signing up (you can switch the page to Chinese if needed):

<img src="./img/19.png" alt="PythonAnywhere dashboard" width="67%">

**② Create a folder**

Open `Files` from the top right, then create a new directory (any name works, e.g. `wechat`):

<img src="./img/20.png" alt="Files menu" width="60%">

<img src="./img/21.png" alt="create directory" width="67%">

**③ Upload files**

Upload `config.json` and `tianqi.py` into that folder:

<img src="./img/22.png" alt="upload files" width="67%">

<img src="./img/23.png" alt="upload files 2" width="80%">

**④ Test run**

Open `tianqi.py` and run it once to make sure everything is configured correctly:

<img src="./img/25.png" alt="test run" width="80%">

If it works, go back to the dashboard and open `Tasks`:

<img src="./img/26.png" alt="Tasks menu" width="80%">

**⑤ Add a scheduled task**

<img src="./img/27.png" alt="add scheduled task" width="80%">

- **Time**: PythonAnywhere uses UTC, which is 8 hours behind Beijing time. For a 12:00 noon push, enter `4:00` (12 − 8 = 4)
- **Command**: `cd /home/YOUR_USERNAME/wechat && python tianqi.py`
- **Description**: any description you like

To find your folder path: open the folder that holds the script and copy the path from the top left. If your folder is also named `wechat`, just replace the username in the path:

<img src="./img/28.png" alt="folder path" width="67%">

Once set, the script runs automatically every day at the scheduled time (example below: a daily 7:00 AM task):

<img src="./img/29.png" alt="scheduled task configured" width="80%">

## ❓ FAQ

<details>
<summary>I don't receive any push. What should I check?</summary>

Go through this list:

1. `touser` must be the openid shown in the sandbox **after following the account**, not your WeChat ID;
2. `template_id` must exactly match the template you created in the backend;
3. Both weather keys (`gd_key` / `hf_key`) must be valid and of the right type;
4. The first run needs network access to fetch `access_token` — check the terminal for the red `推送成功` (push succeeded) message.
</details>

<details>
<summary>Do the AMap / QWeather APIs cost money?</summary>

No — individual developers get free tiers, and this tutorial only uses the free quotas, which is enough for daily use.
</details>

<details>
<summary>Why is my PythonAnywhere scheduled task running at the wrong time?</summary>

The platform uses UTC. Configured time = Beijing time − 8 hours. For example, a 12:00 Beijing push should be scheduled as `4:00`.
</details>

<details>
<summary>How do I push to multiple people?</summary>

Put multiple openids in `touser` and uncomment the for loop at the end of `tianqi.py`:

```python
for i in touser:
    send_message(i, token, info, rainbow_text)
```
</details>

## 📁 Project Structure

```text
wechat-office/
├── config.json   # Configuration (AppID / weather keys / template ID)
├── tianqi.py     # Weather push main script (AMap + QWeather)
├── test.py       # Test script (no weather API needed, verifies template messaging)
└── img/          # README screenshots
```

> The only dependency is `requests` — `pip install requests` is enough (no requirements.txt needed).

## 🤝 Contributing

Feedback and bug reports are welcome via [Issues](https://github.com/Amengclass/wechat-office/issues), and code contributions via [Pull Requests](https://github.com/Amengclass/wechat-office/pulls).

## 📄 License

This project does not have a License yet. If you plan to open-source it for others to use, consider adding one (e.g. MIT).
