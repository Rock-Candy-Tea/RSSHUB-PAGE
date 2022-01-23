
---
title: 'QPython系列：手機查看LikeCoin錢包餘額'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/03e228a2-8d31-493a-98af-0bf17b8e9d61.png'
author: Matters
comments: false
date: Sat, 22 Jan 2022 17:51:07 GMT
thumbnail: 'https://assets.matters.news/embed/03e228a2-8d31-493a-98af-0bf17b8e9d61.png'
---

<div>   
<p>看到這個標題你是不是想問，看LikeCoin錢包餘額不是打開LikerLand看就行？</p><p>如果你只有一個LikerLand賬號確實是打開App看就好，但對不止一個Matters賬號的人要看錢包餘額就得登出再登入。用Kelper錢包的就更慘，不開電腦根本沒法看。</p><h2><strong>⏺ 適用人群</strong></h2><p>❇️ 持有多於一個Liker Land賬號</p><p>❇️ 想在手機看Kepler錢包的LikeCoin餘額</p><p>❇️ 安卓手機用戶（沒法子，大叔目前用的不是iPhone）</p><h2><strong>⏺ 作品介紹</strong></h2><p>因爲大叔手太癢，弄了好幾個LikeCoin錢包分散放，然後久了就搞不清楚那個錢包有多少錢，又有哪些獎勵該去領出來了？剛好看到<a class="mention" href="https://matters.news/@ttt50966" target="_blank" data-display-name="Kuàn-ka" data-user-name="ttt50966" data-id="VXNlcjoxMTM4NA">﻿<span>@Kuàn-ka</span>﻿</a> 最近發佈的<a href="https://www.google.com/url?q=https://matters.news/@ttt50966/like-coin-%25E9%25A4%2598%25E9%25A1%258D%25E6%259F%25A5%25E8%25A9%25A2-scriptable-widget-i-os-bafyreicvkb7ia7vyk6xk574l7yebut6q36dkckm7j3uer4tgsdjgelwowe&sa=D&source=editors&ust=1642875495499973&usg=AOvVaw3eFabkfI6FfaHlhkrDLGFZ" rel="noopener noreferrer" target="_blank">文章</a>有直接在文中附上源碼，就決定拿來修改使用。</p><p>第一次使用需要在谷歌商店下載QPython和做一些設定，完成後只要開App跑脚本就可以獲得以下結果。</p><hr><figure class="image"><img src="https://assets.matters.news/embed/03e228a2-8d31-493a-98af-0bf17b8e9d61.png" data-asset-id="03e228a2-8d31-493a-98af-0bf17b8e9d61" referrerpolicy="no-referrer"><figcaption><span>效果圖是我兩個沒怎麽在用的錢包餘額</span></figcaption></figure><hr><hr><h2><strong>⏺ 安裝説明</strong></h2><p><strong>所需工具和資料有：</strong></p><p>❇️ QPython（谷歌商店可<a href="https://www.google.com/url?q=https://play.google.com/store/apps/details?id%3Dorg.qpython.qpy3%26hl%3Dzh%26gl%3DUS&sa=D&source=editors&ust=1642875495501260&usg=AOvVaw0NF_hpmcPNBLEseJlhuF7z" rel="noopener noreferrer" target="_blank">免費下載</a>）</p><p>❇️ 你的LikeCoin錢包地址（後面會説明）</p><p>❇️ 大叔寫的程序碼（因爲太長，放到文章最後面，或者點<a href="https://colab.research.google.com/drive/1gEu92Ld0lZ7uWOU-i1Aa9Kvr5Xwe4al8?usp=sharing" rel="noopener noreferrer" target="_blank">這裏</a>打開）</p><p><strong>添加所需的Python庫：</strong></p><ol><li>點開App，如果App和你要權限點Ok就是了。看到菜單點“QPYPI”。</li><li>先點“Pip console”安裝一個需要用到的庫。</li><li>輸入“pip3 install requests”，參考圖片。</li><li>按下回車鍵，發出上一步輸入的指令。</li><li>等到箭頭（-->）再次出現就完成了。</li></ol><figure class="image"><img src="https://assets.matters.news/embed/be97a5a7-4008-4660-8244-b2940a3226f6.png" data-asset-id="be97a5a7-4008-4660-8244-b2940a3226f6" referrerpolicy="no-referrer"><figcaption><span>如何添加所需的Python庫</span></figcaption></figure><hr><hr><p><strong>建立脚本：</strong></p><ol><li>點開編輯器，複製貼上程式碼。</li><li>點擊儲存鍵，選擇“scrpts3”存放脚本。</li><li>輸入方便你識別的脚本名，結尾必須是“.py”，點擊打勾鍵存儲脚本。</li></ol><figure class="image"><img src="https://assets.matters.news/embed/252c30e7-5c06-41c1-82b0-42d0bcc0d03f.png" data-asset-id="252c30e7-5c06-41c1-82b0-42d0bcc0d03f" referrerpolicy="no-referrer"><figcaption><span>如何建立脚本</span></figcaption></figure><hr><hr><p><strong>運行脚本：</strong></p><ol><li>點擊程序。</li><li>點擊要運行的脚本。</li><li>點擊“Run”。</li><li>等脚本跑完，所需時間會被錢包數量和網路速度影響，如圖中兩個錢包也就幾秒鐘的事情。</li></ol><figure class="image"><img src="https://assets.matters.news/embed/9829cfc5-9719-4fe5-be55-8ef622f8551e.png" data-asset-id="9829cfc5-9719-4fe5-be55-8ef622f8551e" referrerpolicy="no-referrer"><figcaption><span>如何跑脚本</span></figcaption></figure><hr><hr><p><strong>錢包地址怎麽找：</strong></p><p>下圖最左邊的是Kepler錢包的地址找法，其他三張圖是LikerLand的。</p><ol><li>點擊“我的錢包”。</li><li>點擊“收款”。</li><li>點擊“複製”即可複製錢包地址。</li></ol><figure class="image"><img src="https://assets.matters.news/embed/7d7d73c5-df41-4930-90d5-3503836fcd77.png" data-asset-id="7d7d73c5-df41-4930-90d5-3503836fcd77" referrerpolicy="no-referrer"><figcaption><span>Kepler和LikerLand錢包地址在哪裏</span></figcaption></figure><hr><hr><h2><strong>⏺ 下期預告</strong></h2><p>除了看LikeCoin錢包，還在做一鍵看完各種貨幣錢包的脚本，還有一鍵看完幣價的脚本。想看的話請多多拍手，不然我誤會沒人要看可能就自己用而不會發文了~</p><h2><strong>⏺ 程式碼</strong></h2><p>最多可以輸入10個錢包地址，只要將下面程式碼中的“<strong>你的錢包地址1</strong>”換成你自己的錢包地址即可，其他錢包依序輸入<strong>wallet[1]</strong>、<strong>wallet[2]</strong>、<strong>wallet[3]</strong>後面的引號之間即可。</p><p>程式碼也可以在<a href="https://colab.research.google.com/drive/1gEu92Ld0lZ7uWOU-i1Aa9Kvr5Xwe4al8?usp=sharing" rel="noopener noreferrer" target="_blank">這裏</a>找到。</p><pre class="ql-syntax" spellcheck="false">import requests
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
from datetime import datetime

wallet=['','','','','','','','','','']
wallet[0]='你的錢包地址1'
wallet[1]=''
wallet[2]=''
wallet[3]=''
wallet[4]=''
wallet[5]=''
wallet[6]=''
wallet[7]=''
wallet[8]=''
wallet[9]=''

def GetLikeWalletInfo(address):
    for x in range(3):
        if (x == 0):
            url = "https://mainnet-node.like.co/cosmos/bank/v1beta1/balances/" + address
            res = requests.get(url)
            data = res.json()
            
            rAmt = 0
            sChecker = str(data)
            if sChecker[:7] !="&#123;'code'":
                DD1 = data['balances']
                for DD2 in DD1:        
                    aAmt = DD2['amount']                    
                    aAmt = float(aAmt) /pow(10,9)
                    
        elif (x == 1):
            url = "https://mainnet-node.like.co/cosmos/distribution/v1beta1/delegators/" + address +"/rewards"
            res = requests.get(url)
            data = res.json()
            
            rAmt = 0
            sChecker = str(data)
            if sChecker[:7] !="&#123;'code'":
                DD1 = data['rewards']
                for DD2 in DD1:
                    DD3 = DD2['reward']            
                    for DD4 in DD3:                        
                        rAmt = rAmt + float(DD4['amount'])
                        
                rAmt = float(rAmt) /pow(10,9)
                
        elif (x == 2):
            url = "https://mainnet-node.like.co/cosmos/staking/v1beta1/delegations/" + address
            res = requests.get(url)
            data = res.json()
            
            sAmt = 0
            sChecker = str(data)
            if sChecker[:7] !="&#123;'code'":
                DD1 = data['delegation_responses']
                
                for DD2 in DD1:   
                    #print(DD2['balance']['amount'])
                    sAmt = sAmt + float(DD2['balance']['amount'])
                    
                sAmt = float(sAmt) /pow(10,9)

    print(f"&#123;address[-4:] :>4&#125;&#123;int(aAmt) :>7&#125;&#123;int(rAmt) :>7&#125;&#123;int(sAmt) :>7&#125;")

dt = datetime.today().isoformat()[:19].replace("T", " ")
print('')
print('你的LikeCoin錢包餘額查詢中……')
print ("開始時間:",dt)
print('-'*30)
print(f"&#123;'錢包':<4&#125;&#123;'餘額':^7&#125;&#123;'獎勵':<7&#125;&#123;'委托':<7&#125;")

for x in range(len(wallet)):
    if wallet[x] != '':      
        GetLikeWalletInfo(wallet[x])

print('-'*30)
dt = datetime.today().isoformat()[:19].replace("T", " ")
print ("更新完成:",dt)
print('')
</pre>  
</div>
            