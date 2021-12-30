
---
title: '製作 Telegram 聊天機械人回答現時 LIKE 幣價格'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/b8576a03-74e2-4479-88b2-374a00c03979.png'
author: Matters
comments: false
date: Thu, 30 Dec 2021 11:39:18 GMT
thumbnail: 'https://assets.matters.news/embed/b8576a03-74e2-4479-88b2-374a00c03979.png'
---

<div>   
<p>之前介紹了<a href="https://matters.news/@makzan/python-%E8%88%87-json-api-%E6%87%89%E7%94%A8%E5%85%A5%E9%96%80-%E4%BD%BF%E7%94%A8-python-%E5%8F%96%E5%BE%97%E7%8F%BE%E6%99%82-like-coin-%E5%B9%A3%E5%83%B9-bafyreifupall2254neimmbaees6p36n4pf6fv7glaoiftimuy2f72cxybq" rel="noopener noreferrer" target="_blank">使用 Python 及 Coingecko API 取得 $LIKE 幣價</a>)及<a href="https://matters.news/@makzan/%E4%BD%BF%E7%94%A8-pyto-%E5%B0%87-like-%E5%B9%A3%E5%83%B9%E6%94%BE%E5%88%B0-i-os-%E4%B8%BB%E7%95%AB%E9%9D%A2-%E5%8F%8A%E4%BD%BF%E7%94%A8-siri-%E8%AA%9E%E9%9F%B3%E8%A7%B8%E7%99%BC-bafyreifdsj52ajz4ogdernzwe647xiee7ha4iql6x54atcvpaeycgdct64" rel="noopener noreferrer" target="_blank">放到 iOS 主畫面並以 Siri 語音觸發</a>的介紹文。</p><p>今期講解一下通過建立 Telegram 聊天機械人來實現查找指令功能。</p><p>Telegram 是類似 LINE, Whatsapp 的通訊軟件，也是其中最早支援聊天機械人服務的通訊軟件。我們可以通過建立 Telegram 聊天機械人，並向聊天機械人發出指令，以觸發預定義的函數。而這些函數處理完成後，發回信息予用戶。</p><figure class="image"><img src="https://assets.matters.news/embed/b8576a03-74e2-4479-88b2-374a00c03979.png" data-asset-id="b8576a03-74e2-4479-88b2-374a00c03979" referrerpolicy="no-referrer"><figcaption><span>觸發流程</span></figcaption></figure><ol><li>發出指令，例如 /LIKE, /price 等</li><li>機械人在線收到指令，觸發函數</li><li>函數處理完成，獲得必要數據，向用戶發出信息</li><li>用戶收到信息。</li></ol><p>成果截圖：</p><figure class="image"><img src="https://assets.matters.news/embed/082e3d9e-8e28-4925-9923-f999fc051d8a.jpeg" data-asset-id="082e3d9e-8e28-4925-9923-f999fc051d8a" referrerpolicy="no-referrer"><figcaption><span>測試機械人範例結果</span></figcaption></figure><p>測試機械人：可以使用 Telegram 連接此聊天機械人，並詢問 /LIKE 或 /price 等指令。</p><p><a href="https://t.me/like_price_bot" rel="noopener noreferrer" target="_blank">https://t.me/like_price_bot</a></p><hr><h2><strong>1️⃣ 建立 Telegram Bot 聊天機械人</strong></h2><p>想利用聊天機械人為自己進行查詢及執行任務，首先需要注冊一個專屬機械人。要登記，需於 Telegram 內使用 @BotFather 機械人。<a href="https://core.telegram.org/bots#6-botfather" rel="noopener noreferrer" target="_blank">BotFather</a> 是 Telegram 為開發者而設的聊天機械人管理服務。</p><p><a href="https://t.me/botfather" rel="noopener noreferrer" target="_blank">https://t.me/botfather</a></p><figure class="image"><img src="https://assets.matters.news/embed/972919fe-4efb-42e8-927d-0862f4ed2e97.jpeg" data-asset-id="972919fe-4efb-42e8-927d-0862f4ed2e97" referrerpolicy="no-referrer"><figcaption><span>使用 BotFather 創建新聊天機械人</span></figcaption></figure><p>與 BotFather 管理服務開始聊天後，可以發出 <code>/newbot</code> 指令，按指示填上機械人名稱，例如我使用 Like Price Bot，你可以按自己需求設定，例如 Jane's Helper 等。然後需要為這個機械人註冊一個用戶名稱，且必須以 _bot 結尾。例如我在這例子中使用 <code>like_price_bot</code>，又或者按你的需求自定義一個不重覆的名稱，例如 <code>jane_helper_bot</code> 等。</p><p>完成後，BotFather 會發出一個完成信息，內𥚃包括我們的 Python 程式所需要的 API TOKEN。範例如下：</p><pre class="ql-syntax" spellcheck="false">Done! Congratulations on your new bot. You will find it at t.me/thomas_helper_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
Use this token to access the HTTP API:
5021980959:AAEDaEh-7PayRc2VG8ov7bU0occHQAi08q4
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
</pre><p>當中 “Use this token to access the HTTP API:” 的下一行，以數字開頭及包括字母與數字的，就是這個聊天機械人的 API 令牌（Token），這類似存取資源的密鑰，有了他就可以控制這個聊天機械人，所以要妥善保管及不要外洩喔。</p><p>⚠️ API Token 需要妥善保管好</p><h2><strong>2️⃣ 安裝 Python Telegram Bot 套件</strong></h2><p>登記好機械人後， 接下來可以開始編程部份。</p><p>使用 Python 開發的話，暫時最方便的是 <a href="https://python-telegram-bot.org/" rel="noopener noreferrer" target="_blank">Python-Telegram-Bot</a>，可以通過 <code>pip install python-telegram-bot</code> 安裝。</p><p>注：視乎你的系統之 pip 安裝在哪𥚃，例如在 Mac 中，有可能需要使用 <code>pip3</code> 代替 <code>pip</code>，即 <code>pip3 intsall python-telegram-bot</code>。</p><p>運行結果：</p><figure class="image"><img src="https://assets.matters.news/embed/abf78514-9962-465f-87f6-e9bba6398a98.png" data-asset-id="abf78514-9962-465f-87f6-e9bba6398a98" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><h2><strong>3️⃣ 構建 Bot 代碼</strong></h2><p>安裝好後，便可以正式編寫 Python 代碼。</p><p>使用 <code>python-telegram-bot</code>，最基本的起步代碼如下：</p><pre class="ql-syntax" spellcheck="false"># (1) 匯入必要的 python-telegram-bot 程式庫from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

# (2) 填上從 BotFather 注冊機械人得來的 API 令牌
TOKEN = "YOUR_BOT_API_TOKEN_HERE"

# (3) 機械人的主要功能使 Updater，負責注冊指令回饋方法及連接 Telegram 服務
updater = Updater(token=TOKEN)

# (4) 定義不同的函數，第一個通常為 start 函數，將會由用戶發出 /start 指令觸發。
def start(update: Update, context: CallbackContext):
    # (5) 通過 context.bot.send_message 發回信息。
    # text 為發出的信息，當中若包括斜號開頭文字，如 /LIKE，則在 Telegram 中為可以直接按下的快捷鍵。
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot. You may check LIKE price with me: /LIKE")    

# (6) 注冊使用哪個指令字串來觸發上述函數 'start' 即使用 /start 觸發
updater.dispatcher.add_handler(CommandHandler('start', start))

# (7) 注冊好所有指令函數後，使用 start_polling 開始監聽來自用戶的機械人指令
updater.start_polling()
</pre><p>把上述代碼儲存，例如儲存為 <code>like_price_bot.py</code> 檔案。 此時，若運行代碼 <code>python like_price_bot.py</code>，並使用 Telegram 跳轉到機械人聊天畫面，機械人網址為 <a href="https://t.me/" rel="noopener noreferrer" target="_blank">https://t.me/</a> 加上機械人用戶名稱，例如上述例子是 <a href="https://t.me/like_price_bot" rel="noopener noreferrer" target="_blank">https://t.me/like_price_bot</a>。</p><p>在聊天畫面中，可以發出 /start 及得到返回文字。但除此之外，我們的機械人並未懂得做更多事情，以下，我們會添加幣價查詢指令函數。</p><h2><strong>4️⃣ 加入更多指令</strong></h2><p>上述的起始樣板代碼，連接好 Telegram 服務及設定了第一個指令回饋。我們可以照板煮碗，定義其他查詢用函數，例如 <code>like</code> 及 <code>price</code>。</p><p>首先我們定義一個 like 函數。當中使用我們之前教學文所取得 $LIKE 幣價的方法。通過 <code>requests</code> 向 <a href="https://www.coingecko.com/en/api" rel="noopener noreferrer" target="_blank">Coingecko API</a> 查詢，並將返回值以 Telegram 信息方式發回。</p><p>重溫一下 Coingecko API，取得幣價的網址為：</p><p><a href="https://api.coingecko.com/api/v3/simple/price?ids=likecoin&vs_currencies=usd" rel="noopener noreferrer" target="_blank">https://api.coingecko.com/api/v3/simple/price?ids=likecoin&vs_currencies=usd</a></p><p>返回值是 JSON 結構，包括查詢幣種及兌換法幣價值。</p><figure class="image"><img src="https://assets.matters.news/embed/cdb819b8-f45d-4e00-beed-e0f90b22071c.png" data-asset-id="cdb819b8-f45d-4e00-beed-e0f90b22071c" referrerpolicy="no-referrer"><figcaption><span>CoinGecko API 的返回值。</span></figcaption></figure><p>故查詢 API 代碼如下，API 的使用請情也可以參考《<a href="https://matters.news/@makzan/python-%E8%88%87-json-api-%E6%87%89%E7%94%A8%E5%85%A5%E9%96%80-%E4%BD%BF%E7%94%A8-python-%E5%8F%96%E5%BE%97%E7%8F%BE%E6%99%82-like-coin-%E5%B9%A3%E5%83%B9-bafyreifupall2254neimmbaees6p36n4pf6fv7glaoiftimuy2f72cxybq" rel="noopener noreferrer" target="_blank">Python 與 JSON API 應用入門：使用 Python 取得現時 LikeCoin 幣價</a>》一文。</p><pre class="ql-syntax" spellcheck="false">def like(update: Update, context: CallbackContext):
    import requests
    # 查詢 LikeCoin 幣價的 API 網址
    url = "https://api.coingecko.com/api/v3/simple/price?ids=likecoin&vs_currencies=usd"
    # 取得 API 返回值
    res = requests.get(url)
    # 將返回文字分析為 JSON 字典結構
    data = res.json()
    # 從結構中
    price = data["likecoin"]["usd"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"LIKE: &#123;price&#125;")
</pre><p>相應的，我們為剛剛定義的函數注冊 telegram 指令，例如 /like。這個指令是不分大小寫的，所以 /like 或 /LIKE 皆可以觸發。</p><pre class="ql-syntax" spellcheck="false">updater.dispatcher.add_handler(CommandHandler('like', like))
</pre><p>同埋，我們也可以製作搜尋其他不同幣價的指令，或定義一個同時包括幾個幣價的指令。並使用相類似的方法返回信息。</p><p>多幣值的 Coingecko API 查找網址為：</p><p><a href="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,terra-luna,osmosis,likecoin,crypto-com-chain&vs_currencies=usd" rel="noopener noreferrer" target="_blank">https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,terra-luna,osmosis,likecoin,crypto-com-chain&vs_currencies=usd</a></p><p>當中請自行替換需要查詢的幣種。而返回結構如下：</p><figure class="image"><img src="https://assets.matters.news/embed/157f4b62-600d-4ae1-afda-df8a48486ce8.png" data-asset-id="157f4b62-600d-4ae1-afda-df8a48486ce8" referrerpolicy="no-referrer"><figcaption><span>使用 Coingecko API 查詢多幣值</span></figcaption></figure><hr><h2><strong>5️⃣ 最終代碼</strong></h2><p>最終代碼如下，已加入 <code>/price</code> 指令，亦可以在以下網址取得源代碼，當中的 YOUR_BOT_API_TOKEN_HERE 請替換成你所創立的聊天機械人 API 令牌。你亦可以加入其他查詢指令函數來配合你的需要。</p><p><a href="https://gist.github.com/makzan/b90dd176504e4b076ef9f99e022a3570" rel="noopener noreferrer" target="_blank">https://gist.github.com/makzan/b90dd176504e4b076ef9f99e022a3570</a></p><p>源代碼：</p><pre class="ql-syntax" spellcheck="false">from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

TOKEN = "YOUR_BOT_API_TOKEN_HERE"

updater = Updater(token=TOKEN)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot. You may check LIKE price with me: /LIKE")

def like(update: Update, context: CallbackContext):
    import requests
    url = "https://api.coingecko.com/api/v3/simple/price?ids=likecoin&vs_currencies=usd"

    res = requests.get(url)
    data = res.json()
    price = data["likecoin"]["usd"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"LIKE: &#123;price&#125;")

def price(update: Update, context: CallbackContext):
    import requests
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,terra-luna,osmosis,likecoin,crypto-com-chain&vs_currencies=usd"

    res = requests.get(url)
    data = res.json()
    btc,eth,like,osmo,cro,luna = (
      data["bitcoin"]["usd"],
      data["ethereum"]["usd"],
      data["likecoin"]["usd"],
      data["osmosis"]["usd"],
      data["crypto-com-chain"]["usd"],
      data["terra-luna"]["usd"],
    )
    text = f"BTC: &#123;btc&#125;\nETH: &#123;eth&#125;\nLIKE: &#123;like&#125;\nOSMO: &#123;osmo&#125;\nCRO: &#123;cro&#125;\nLUNA: &#123;luna&#125;"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('like', like))
updater.dispatcher.add_handler(CommandHandler('price', price))

updater.start_polling()
</pre><p>Enjoy! 😉</p><p>— 麥誠 Makzan，2021-12-30。</p><hr><p>我是<a href="https://matters.news/@makzan/%E4%B8%83%E5%80%8B%E6%9C%88%E5%BE%8C%E7%9A%84%E6%96%B0%E4%BA%BA%E5%A0%B1%E5%88%B0%E8%87%AA%E6%88%91%E4%BB%8B%E7%B4%B9-%E4%BE%86%E5%88%B0%E9%A6%AC%E7%89%B9%E5%B8%82%E6%98%AF-2021-%E5%B9%B4%E6%9C%80%E5%A4%A7%E7%9A%84%E6%94%B6%E7%A9%AB-bafyreicqwsbpuf6a5lqgp2c44q44ge272mt4aoqfu5gytyylno6hhr563u" rel="noopener noreferrer" target="_blank">麥誠軒（Makzan)</a>，除了正職外，平常我要麼辦本地賽與辦世界賽，要麼任教編程與網站開發的在職培訓。現正轉型將面授培訓內容寫成電子書、網上教材等，至今撰寫了 7 本書， 2 個視頻教學課程。</p><p>如果我的文章有價值，請左下角 <strong>👍🏻按讚支持</strong>，或<a href="https://liker.land/thomasmak/civic" rel="noopener noreferrer" target="_blank">訂閱贊助</a>我持續創作及分享。</p><p><br></p><figure class="image"><img src="https://assets.matters.news/embed/327297f5-4fc4-4721-91b6-c860bc92803c.png" data-asset-id="327297f5-4fc4-4721-91b6-c860bc92803c" referrerpolicy="no-referrer"><figcaption><span>麥誠 Makzan</span></figcaption></figure><p><br></p>  
</div>
            