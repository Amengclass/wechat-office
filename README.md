<div align="center">

# 💌 WeChat Office

> 用 Python 写的微信公众号模板消息推送工具 —— 每天定时给 TA 推送天气、每日一言和星座运势。

**中文** | [English](README_EN.md)

[![Stars](https://img.shields.io/github/stars/Amengclass/wechat-office?style=social)](https://github.com/Amengclass/wechat-office/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Amengclass/wechat-office?color=blue)](https://github.com/Amengclass/wechat-office/commits/master)
[![Built with](https://img.shields.io/badge/built%20with-Python-3776AB.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Amengclass/wechat-office/pulls)

</div>

## ✨ 特性

- **天气推送** — 通过高德 + 和风双天气 API 获取实时天气，以模板消息形式发送到公众号
- **每日一言** — 集成免费 hitokoto API，每天推送一句彩虹屁 / 名言
- **可定制模板** — 模板内容完全由你定义，支持 emoji，随你发挥
- **灵活配置** — 所有参数集中在 `config.json`，改配置即可换城市、换模板、换推送对象
- **免费自动推送** — 提供 PythonAnywhere 免费托管教程，每天定时自动推送
- **多用户支持** — `touser` 支持数组，一条脚本推送给多个人

## 🖼️ 效果预览

| `test.py`（测试推送） | `tianqi.py`（天气推送） |
| :---: | :---: |
| <img src="./img/5.jpg" width="70%"> | <img src="./img/6.jpg" width="70%"> |

## 🚀 快速开始

1. **克隆仓库**并进入目录：

   ```bash
   git clone https://github.com/Amengclass/wechat-office.git
   cd wechat-office
   ```

2. **安装依赖**（本仓库仅依赖 `requests`）：

   ```bash
   pip install requests
   ```

3. **配置参数**：编辑 `config.json`，填入微信公众号测试号的 AppID、AppSecret、模板 ID，以及天气 API Key（获取方式见[详细教程](#-详细教程)）

4. **运行推送**：

   ```bash
   python tianqi.py
   ```

   推送成功会输出红色 `推送成功` 提示。默认推送城市为**北京**，在 `tianqi.py` 中把 `location="北京"` 改成你自己的城市即可。

## ⚙️ 配置说明

所有配置都在 `config.json` 中：

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

| 字段 | 说明 |
| --- | --- |
| `wechat.AppID` | 微信测试号 AppID（[测试号申请入口](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)） |
| `wechat.AppSecret` | 微信测试号 AppSecret |
| `wechat.access_token` | 运行后自动写入，无需手动填写 |
| `weather.gd_key` | 高德天气 API Key（[申请入口](https://console.amap.com/dev/index)） |
| `weather.hf_key` | 和风天气 API Key（[申请入口](https://id.qweather.com/)） |
| `template.touser` | 接收推送的用户 openid（数组，可填多个） |
| `template.template_id` | 微信后台新建的模板 ID |

> ⚠️ 注意：上方 JSON 是**合法可解析**的版本。请勿在 JSON 中写 `#` 注释，否则程序会解析失败。

## 📖 详细教程

### 1️⃣ 获取微信测试号 AppID / AppSecret

访问 [微信公众平台测试号](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login) 并扫码登录，在页面上获取 `appID` 和 `appsecret`：

![微信测试号后台](https://user-images.githubusercontent.com/110412182/186095663-3146adbf-a6e3-4e55-8add-41079d77b870.png)

把它们填入 `config.json` 的对应位置：

<img src="./img/0.png" alt="修改config.json" width="80%">

### 2️⃣ 新建模板 & 运行 test.py（测试用）

在微信后台「新增测试模板」，模板内容按下面字段新建（`test.py` 使用）：

```text
测试1：{{date.DATA}}
测试2：{{city.DATA}}
测试3：{{weather_now.DATA}}
测试4：{{temprature_now.DATA}}
测试5：{{temprature_today.DATA}}
测试6：{{win.DATA}}
测试7：{{rainbow.DATA}}
```

<img src="./img/1.png" alt="新建测试模板" width="60%">

添加成功后，将模板 ID 复制下来：

<img src="./img/2.png" alt="模板ID" width="60%">

把模板 ID 填进 `config.json`：

<img src="./img/3.png" alt="填写模板ID" width="60%">

扫码关注测试号后，后台会显示用户的微信号信息，把用户 openid 填到 `touser` 里：

<img src="./img/4.png" alt="获取用户openid" width="60%">

确认配置无误后运行：

```bash
python test.py
```

收到推送即配置正确，效果预览见上方表格。

### 3️⃣ 天气推送 tianqi.py

新建天气模板并替换模板 ID，模板内容如下（可自由发挥加 emoji ʕ•ᴥ•ʔ）：

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

天气数据来自高德和风两个免费 API，需要分别申请 Key，申请方式见下一步。运行：

```bash
python tianqi.py
```

效果预览见上方表格。

### 4️⃣ 申请天气 API Key

#### 高德天气

注册登录 [高德开放平台](https://console.amap.com/dev/index)：

<img src="./img/7.png" alt="高德注册登录" width="40%">

创建 Key（选择 Web 服务类型即可）：

<img src="./img/8.png" alt="高德创建Key" width="60%">

把 Key 复制下来，填进 `config.json` 的 `gd_key`：

<img src="./img/10.png" alt="填写高德Key" width="80%">

#### 和风天气

注册登录 [和风天气控制台](https://id.qweather.com/)：

<img src="./img/11.png" alt="和风注册登录" width="80%">

添加 Key：

<img src="./img/12.png" alt="和风添加Key" width="60%">

<img src="./img/13.png" alt="和风Key详情" width="60%">

把 Key 复制下来填进 `config.json` 的 `hf_key`：

<img src="./img/14.png" alt="填写和风Key" width="60%">

<img src="./img/15.png" alt="两个Key都填好" width="67%">

两个 Key 都填好后，运行 `python tianqi.py` 即可收到天气推送。

### 5️⃣ 免费服务器托管：每天自动推送

用免费的 [PythonAnywhere](https://www.pythonanywhere.com/) 托管，实现每天定时自动推送：

<img src="./img/16.png" alt="PythonAnywhere官网" width="80%">

**① 注册账号**

点击注册：

<img src="./img/18.png" alt="PythonAnywhere注册" width="67%">

注册成功后的界面（看不懂英文可在页面切换为中文）：

<img src="./img/19.png" alt="注册成功界面" width="67%">

**② 新建文件夹**

选择右上角 `Files`，新建文件夹（名字随意，示例叫 `wechat`）：

<img src="./img/20.png" alt="Files入口" width="60%">

<img src="./img/21.png" alt="新建文件夹" width="67%">

**③ 上传文件**

把 `config.json` 和 `tianqi.py` 上传到该文件夹：

<img src="./img/22.png" alt="上传文件" width="67%">

<img src="./img/23.png" alt="上传文件2" width="80%">

**④ 试运行**

双击 `tianqi.py` 试运行，确保配置正确：

<img src="./img/25.png" alt="试运行" width="80%">

确认无误后，回到主页选择 `Tasks`：

<img src="./img/26.png" alt="Tasks入口" width="80%">

**⑤ 添加定时任务**

<img src="./img/27.png" alt="添加定时任务" width="80%">

- **时间**：PythonAnywhere 使用 UTC 时间，与北京时间差 8 小时。想中午 12 点推送就填 `4:00`（12 − 8 = 4）
- **命令**：`cd /home/你的用户名/wechat && python tianqi.py`
- **描述**：随意填写任务描述

查看你的文件夹路径：打开存放脚本的文件夹，复制左上角路径即可。如果文件夹名也叫 `wechat`，只需把路径中的用户名换成你的账号名：

<img src="./img/28.png" alt="查看文件夹路径" width="67%">

配置完成后，每天到点就会自动运行推送了（下图是配置好早上 7 点任务的示例）：

<img src="./img/29.png" alt="定时任务配置完成" width="80%">

## ❓ FAQ

<details>
<summary>运行后收不到推送，怎么办？</summary>

按顺序检查：

1. `touser` 必须是**扫码关注测试号后**显示的用户 openid，不是微信号；
2. `template_id` 是否与后台新建的模板完全一致；
3. 天气 Key（`gd_key` / `hf_key`）是否申请成功且类型正确；
4. 首次运行需联网获取 `access_token`，查看终端是否输出 `推送成功`（红色）。
</details>

<details>
<summary>高德 / 和风天气 API 收费吗？</summary>

个人开发者均可免费申请，本教程用的就是免费额度，足够日常使用。
</details>

<details>
<summary>PythonAnywhere 上定时任务的时间为什么不对？</summary>

平台使用 UTC 时间，配置时间 = 北京时间 − 8 小时。例如北京时间 12:00 推送，就填 `4:00`。
</details>

<details>
<summary>怎么同时推送给多个人？</summary>

`touser` 填多个 openid，并在 `tianqi.py` 末尾取消注释 for 循环即可：

```python
for i in touser:
    send_message(i, token, info, rainbow_text)
```
</details>

## 📁 项目结构

```text
wechat-office/
├── config.json   # 配置文件（AppID / 天气Key / 模板ID）
├── tianqi.py     # 天气推送主程序（高德 + 和风双API）
├── test.py       # 测试程序（不依赖天气API，验证模板消息通）
└── img/          # README 教程截图
```

> 依赖仅 `requests`，直接 `pip install requests` 即可（无需 requirements.txt）。

## 🤝 贡献

欢迎提交 [Issues](https://github.com/Amengclass/wechat-office/issues) 反馈问题，也欢迎 [Pull Requests](https://github.com/Amengclass/wechat-office/pulls) 贡献代码。

## 📄 License

本项目尚未添加 License。如计划开源使用，建议补充（例如 MIT）。
