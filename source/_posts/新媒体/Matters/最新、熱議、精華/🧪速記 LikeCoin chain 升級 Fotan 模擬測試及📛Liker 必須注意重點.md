
---
title: '🧪速記 LikeCoin chain 升級 Fotan 模擬測試及📛Liker 必須注意重點'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/ad85608f-d0cf-484d-b0fe-600a000ad6d7.png'
author: Matters
comments: false
date: Thu, 29 Jul 2021 14:32:48 GMT
thumbnail: 'https://assets.matters.news/embed/ad85608f-d0cf-484d-b0fe-600a000ad6d7.png'
---

<div>   
<p>昨天晚上 LikeCoin 驗證人們在 Google Meet 一起測試 LikeCoin chain 升級至 Fotan 版本，我也去湊熱鬧看看發生甚麼事。</p><figure class="image"><img src="https://assets.matters.news/embed/ad85608f-d0cf-484d-b0fe-600a000ad6d7.png" data-asset-id="ad85608f-d0cf-484d-b0fe-600a000ad6d7" referrerpolicy="no-referrer"><figcaption><span>升級步驟講解（圖片偷自 LikeCoin Facebook）</span></figcaption></figure><h2>如果你不想知道測試過程，只想知道升級將會對身為 Liker 的你有甚麼影響，請看最後兩段。</h2><hr><p>早前驗證人 Liker Social 發起 LikeCoin chain 升級為 FoTan 議案 1 並獲得通過。而更早之前驗證人們一直在 Testnet 測試各項升級程序，為的就是在昨天進行模擬測試取得經驗，並為真正升級那天綵排一次流程。當然有一些驗證人本身經已技術超群，可能不需測試因為對他們影響並不大，到正式升級才實際操作都綽綽有餘。然而對於抽出晚上寶貴時間一同演練的驗證人肯定是負責任的表現，我要為他們鼓掌。</p><p>昨天下午在 LikeCoin Discord 公佈了升級的 Google Meet 會議地址後，晚上最高峰時有30多人在線。老實說我是文組人真的有點不明白他們在做甚麼，只知道驗證人們依照 <a href="https://docs.like.co/validator/fotan-upgrade-testnet/upgrade-step-by-step" target="_blank">LikeCoin 全書內指示</a>一步一步去做，然後互相確認大家是否同步至相同區塊高度 ( block height ) ，之後再執行一些步驟。可是在這時「Boom」（實際是無聲的），卡了一個大 bug。難道整晚綵排就此放棄？</p><p>主導升級測試的 Chung 就在眾目睽睽之下嘗試去 debug，不斷循不同角度去猜想為甚麼有錯誤。後來 William 在 GitHub 找到 Cosmos SDK，亦即是 LikeCoin 建基的區塊鏈技術平台曾經發生過類似問題。他們一起研究後，William 大致上認為大家要把經已做的砍掉重練（驚）。不過接著，神奇的事發生了，Chung 不知做了甚麼，突然就 fix 好了這個 bug，不需大家多做些甚麼，Testnet 升級順利完成！</p><figure class="image"><img src="https://assets.matters.news/embed/985ed50e-af83-459e-9822-436eca194f28.png" data-asset-id="985ed50e-af83-459e-9822-436eca194f28" referrerpolicy="no-referrer"><figcaption><span>升級順利完成（圖片偷自 LikeCoin Discord）</span></figcaption></figure><p>以上這些對不是技術人員的你和我可能沒有甚麼大感覺，但我想 Chung 本人（不是中本聰，爛 gag）在寫了那麼久的 Doc 在團隊內部測試了那麼多次，竟然在臨門一腳出事，還要對著那麼多不同國家經已很有實力的驗證人，仿如在武林高手面前出招，換轉是我可能就要直接 GG 了。正正因為驗證人都來自不同國家，大家的時區、生活習慣甚或是簡單如 keyboard layout 都完全不同。如果說對上一次 2019 年底由 ERC-20 升級 Cosmos 是技術上的考驗，升級到 FoTan 就是技術加上組織能力的考驗。要組合那麼多人於同一時間做同一件事，分分鐘雞同鴨講對各個指令認知不同，真的不是那麼輕鬆。依書直接輸入內容人人都會，但出現問題後知道怎樣去拆解就是硬實力了，Chung 最後如有神助的表現，簡直就是 MVP！不敢想像如果不是成功搞定這個 bug，要重新組合驗證人們再次進行測試會有怎樣的麻煩。而經歷過今次，對接下來正式升級大家應該更有信心，畢竟區塊鏈本身都是很新的東西，有很多問題不是平常會遇到，能有這麼有經驗的人去處理，大家絕對可以對這次升級投以信心一票。</p><figure class="embed-video"><div class="iframe-container"><iframe src="https://www.youtube.com/embed/RCt8zkwT_Z4?rel=0" frameborder="0" allowfullscreen="true" sandbox="allow-scripts allow-same-origin allow-popups"></iframe></div><figcaption><span>懂得技術的你也許會對這次綵排更為了解</span></figcaption></figure><h2>如果你只關心升級實際對你有甚麼影響，以下為不專業的 LikeCoin FoTan 升級注意重點，都是我邊看 Discord 邊學現妙現賣的，一切以 LikeCoin 公佈為準：</h2><ul><li>升級後錢包地址（即在 BigDipper 中看到 Cosmos 起始那串地址）和以往完全相同</li><li>現時在線的驗證人如果不升級到 Fotan，整個系統全面升級後就會被視為不在線而導致你委託的 LikeCoin 本金被扣減</li><li>這時候如果你取回委託，由於升級前系統會紀錄所有驗證人的委託狀態，LikeCoin 會正常地退回你的錢包，畢竟錢包地址都是一樣</li><li>每天讚賞公民的拍手會自動儲起（塞車）但不會失去，所以只會遲到不會不到。創作基金的發放則會避開/調整發放的時間。亦會再實際試一下會不會再增加些甚麼機制暫停/繼續</li><li>交易所方面，LikeCoin team 應該會和他們聯系好調整升級為 Fotan 版本的 LikeCoin chain。但如果你擔心的話，在預計升級的那一天就不要使用交易所也不要把 LikeCoin 留在交易所（其實這樣也為了保障你自己，升級不升級也不要把錢長期留在交易所吧）</li></ul><p>接下來 Chung 應該會與 Cosmos 那邊確認一下 bug 應該怎樣修，相信這個經驗對未來其他需要在 Cosmos SDK 升級的人都會帶來益處，然後他會更新 LikeCoin 全書內容。此外參與升級綵排的其中一位驗證人將提出第 2 議案確認升級日期，似乎將會是 8月18日 8pm UTC+8（大家一起發一發呀！），各位 Likers 敬請留意。</p>  
</div>
            