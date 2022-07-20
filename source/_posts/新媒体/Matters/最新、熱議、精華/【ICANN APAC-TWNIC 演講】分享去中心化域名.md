
---
title: '【ICANN APAC-TWNIC 演講】分享去中心化域名'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/dfb1619e-a19d-446b-9cd0-98657e7ee38e.png'
author: Matters
comments: false
date: Tue, 31 May 2022 06:24:51 GMT
thumbnail: 'https://assets.matters.news/embed/dfb1619e-a19d-446b-9cd0-98657e7ee38e.png'
---

<div>   
<p>感謝前NCC 主委詹婷怡的邀請，讓我能在 ICANN（DNS 與IP 分配機構）的<a href="https://forum.twnic.tw/2022/" rel="noopener noreferrer" target="_blank">2022論壇</a>介紹對於去中心化域名並表達自己的意見，身處於有唐鳳和Tempo 等大佬的講者群我實在感到非常興奮．真沒想到當初因為寫量子計算部落格的機緣，最後被邀請去講 Web3/Crypto 的主題，如此人生體驗實在是極為有趣． 希望大家能夠從文章/影片有所獲得，依照慣例，歡迎留言分享、轉發讚賞、甚至<a href="https://www.physics2045.blog/donation/" rel="noopener noreferrer" target="_blank">捐款</a>：）</p><h1><a href="https://www.youtube.com/watch?v=TR4vckk7Uh4" rel="noopener noreferrer" target="_blank">Youtube 地址(1:26:58)</a></h1><h2>簡報內容</h2><p><strong>廣告Orca 與Mango(P1-P2):</strong> 雖然本講的主題是去中心化域名，不過既然主辦單位允許打廣告，那我就還是認真推廣代言項目．Orca 是Solana 鏈上最多人使用、交易量最大的去中心化交易所，其設計哲學是給人使用（而非給機器使用），在UI/UX方面都非常流暢，最近由於支援Stepn 成為內建交易所的緣故，用戶指數成長，每日月活躍人數超過100K；Mango 則是Solana 鍵上最專業的一站式交易平台，支援現貨交易、借貸放貸、永續合約交易等等，可以說是鏈上FTX （有訂單簿、全倉保證金、和交易子帳號），從nasen.ai 可以看出這是Solana 鏈上計算量最大的Dex．</p><figure class="image"><img src="https://assets.matters.news/embed/dfb1619e-a19d-446b-9cd0-98657e7ee38e.png" data-asset-id="dfb1619e-a19d-446b-9cd0-98657e7ee38e" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><strong>為何要去中心化域名（P3）</strong>:對於域名系統，有個類似區塊鏈不可能三角的「域名不可能三角（zokko triangle）」，單一域名系統無法同時做到「安全、去中心化和人類可讀」．在Web2的世界中（例如ICANN），就是選擇了安全性與人類可讀（所以中心化）；在Web3/Crypto的世界中，透過非對稱的公私鑰和共識演算法，系統做到了去中心化和安全，但是也因此不具備人類可讀地址．所以最後的解決方案就是在L1（區塊鏈本體之外）加上一層域名的基礎建設（這部分就有治理和安全性的部分要注意，因為這個應用通常不是L1自身），讓賦予地址好讀好記的型態．</p><p><strong>ENS以太坊域名系統（P4-P5）</strong>:以太坊域名系統是建立在ETH上的去中心化域名系統（像是我的地址就是kowei.eth），不過他除了儲存地址用於轉賬和辨識方便外，也已經支援各種應用：首先是可以儲存其他鏈的地址（如BTC DOGE FTM，雖然用這個延伸功能的域名很少），也可以儲存社交媒體帳號、email地址，同時指向某個網站（傳統的DNS、去中心化的IPFS、永久儲存的AR都不是問題），五月初的時候ENS總註冊量已經超過了100萬個域名了（大家之前如果在Crypto Twitter 晃晃應該是能看到許多profile 有.ens ．</p><p><strong>ENS作為NFT（P6-P7）</strong>:ENS 在鏈上的型態就是NFT 的ERC721，所以可以在Opensea/Looksrare等NFT 平台作為資產交易，有時候也回成為熱點交易項目．同時既然是NFT 資產，就會有人做NFTFI，早在2020年Opensea 高層就曾經抵押NFT 申請貸款過，所以基礎建設的可組合性在Crypto 世界絕對不能小看．這邊值得提到的細節是ENS 設計上，同一個地址有不同權限「登記人」和「使用者」，我可以轉讓所有權改變登記人，但是在這段期間保留使用的權利，實在是很方便的設計．</p><p><strong>ENS的設計問題（P8）</strong>：零寬字符是眾所週知的挑戰（也就是kowei.eth 和「空白鍵」kowei.eth是兩個肉眼難以區分的域名），這讓域名蟑螂和詐騙集團完全可以透過創造大量零寬字符干擾正常使用者的使用體驗（買到假域名、或是轉錢轉錯地址…），這點目前看起來沒有釜底抽薪的解決方法，最多就是在種和的dapp或域名賣場加上零寬字符警示．</p><p><strong>$ENS治理代幣與DAO（P9-P11）</strong>: 如果有可以升級的合約和需要權衡取捨的選項，那就得DAO治理，ENS 這個公共財/基礎建設也包含在這個範疇中，而$ENS 代幣已經於去年十一月空投．第一個需要治理的就是項目金庫：即使扣掉$ENS 自家代幣不算，金庫中仍就有4000ETH 和10M 數量級的USDC（這些主要是註冊收入，之後會有長期的續約收入），各種花費都可以透過論壇討論和投票表決來支出（也可以表決要ENS基金會換人）；其次就是ENS DAO能設定ens 的域名費用（目前是三個字元每年要640USD最貴，如果是五個字元以上就一年5U而已）．不過，即使ENS DAO 已經掌握了.end 域名的智能合約跟權限，ENS根權限仍舊是掌握在之前七人多簽錢包手上 ，等待DAO 更成熟後就會轉移這個權利（主要是ENS 和DNS的整合還是有中心化團體溝通比較不容易出事和有效率）．</p><p><strong>Solana naming system(P12-P13)</strong>:由Bonfida 開發建立於Solana上的類似產品，有一些和ENS不同之處，主要是在於可以一次買斷永遠持有、並且價格和字元長度無關（好域名應該都被買走了）、支援中文等非英文域名 ，至於零寬字符仍是讓人頭痛的問題．現在也已經售出超過200K 個域名了．</p><p>原文連結<a href="https://www.physics2045.blog/2022/05/28/icann-apac-twnic-2022/" rel="noopener noreferrer" target="_blank">凝視奇點的物理學徒</a></p>  
</div>
            