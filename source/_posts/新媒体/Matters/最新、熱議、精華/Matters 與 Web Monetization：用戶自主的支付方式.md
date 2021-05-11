
---
title: 'Matters 與 Web Monetization：用戶自主的支付方式'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/8f608783-1cf3-450d-b201-6cf44f779177.gif'
author: Matters
comments: false
date: Fri, 07 May 2021 14:45:44 GMT
thumbnail: 'https://assets.matters.news/embed/8f608783-1cf3-450d-b201-6cf44f779177.gif'
---

<div>   
<p>對於互聯網支付， 這是個日新月異的年代。各國法幣管制步步緊收，而虛擬貨幣又種類繁多、良莠不齊。人們頻繁地兌換幣種，最後把價值託管在交易所，讓交易所變成了新的銀行。</p><p>有沒有一種辦法，讓支付者與收款者能夠使用各自中意的幣種，順利進行交易，同時還不需要依賴中心化的交易所呢？跨鏈協議（<a href="https://interledger.org/" target="_blank">Interledger Protocol</a>）便實現了這樣的功能。跨鏈協議網絡由獨立的<a href="https://interledger.org/rfcs/0001-interledger-architecture/#connectors" target="_blank">連接點</a>組成，形成了去中心的跨幣種市場，自動轉換交易兩端的不同幣種，聯通傳統的銀行系統和新型的區塊鏈賬本。</p><p>Web Monetization 網頁標準則將跨鏈協議接入了互聯網。一直以來，互聯網沒有通行的支付標準，用於指示付款需求的 402 HTTP 狀態碼也始終處於實驗中。某種程度上，Stripe 的崛起與比特幣的發明，都是在填補這個空缺；而基於跨鏈協議的 Web Monetization 解決了跨幣種的問題，成爲了另一個開始通行的標準，也正在 <a href="https://discourse.wicg.io/t/proposal-web-monetization-a-new-revenue-model-for-the-web/3785/10" target="_blank">W3C 提案</a>審理中。</p><p>所以 Matters 通過 Mozzilla、Creative Commons 和 Coil 聯合發起的 <a href="https://www.grantfortheweb.org/" target="_blank">Grant for the Web</a> 整合了 Web Monetization 標準，在Grant for the Web的支持下，讓用戶在 Matters 網站或者 IPFS 中都能夠輕鬆使用 Web Monetization，接受其他用戶的捐贈。</p><p>Web Monetization 在中文世界中使用還不廣泛，為了讓更多用戶能夠體驗，我們也拿出一筆錢，用以獎勵在文章中使用了 Web Monetization 的用戶。</p><h2>如何通過 Web Monetization 接受捐贈</h2><p>Web Monetization 的付款方與收款方均需要一個服務提供商。接收方的服務商會提供一個收款地址（<a href="https://paymentpointers.org/" target="_blank">payment pointer</a>），Matters 則會將這個地址嵌入用戶的文章中，用於接受捐贈。收到捐贈之後，用戶可以再根據需要從收款服務提供轉到其他帳戶。</p><p>目前比較流行的收款服務提供商有 <a href="https://gatehub.net/" target="_blank">GateHub</a> 和 <a href="https://uphold.com/" target="_blank">Uphold</a>，在用戶註冊免費帳戶後都會分配一個收款地址。比如對於 Uphold，你可以在面板最右側的轉帳區域點擊 From ，再在下拉列表中選擇 Interledger，最後複製收款地址。</p><figure class="image"><img src="https://assets.matters.news/embed/8f608783-1cf3-450d-b201-6cf44f779177.gif" data-asset-id="8f608783-1cf3-450d-b201-6cf44f779177" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>在 Matters <a href="https://matters.news/me/wallet" target="_blank">錢包頁面</a>中，點擊最後一個“跨鏈收款地址”，便會彈出一個彈窗。你只需要在這裡粘貼上一步複製的地址，點擊確認，就大功告成了！</p><figure class="image"><img src="https://assets.matters.news/embed/88dcbbad-78d6-44ae-8b80-659f0b0ce995.png" data-asset-id="88dcbbad-78d6-44ae-8b80-659f0b0ce995" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><h2>如何通過 Web Monetization 給出捐贈</h2><p>目前流行的支付服務提供商僅有 <a href="https://coil.com/" target="_blank">Coil</a>，在桌面端提供瀏覽器插件，在手機端提供客製化瀏覽器。不管是通過瀏覽器插件還是客製化手機瀏覽器，你都可以在上面登錄 Coil 帳號，然後正常瀏覽網頁。</p><p>配置了跨鏈收款地址後，用戶發佈的文章在 Matters 網站和 IPFS 都會內嵌收款地址。此時你的 Coil 插件或者瀏覽器會提醒你這篇文章已經接入 Web Monetization，你就可以直接捐贈給作者了。</p><h2>Matters 獎金計劃</h2><p>Web Monetization 的推廣尚在早期，使用的捐贈者也比較少。為此，我們準備了一筆2000美金的獎金，让配置了 Web Monetization 的用戶可以體驗這項尚在早期的功能，並且按照用戶文章的站內閱讀時長獲得獎金。</p><p><strong>5月20日</strong>之前，你只需在配置好Web Monetization 後，給在 Matters 發布的文章上打上 <a href="https://paper.dropbox.com/?q=%23WebMonetizationMatters" target="_blank">#WebMonetizationMatters</a> 這個標籤，你發布的文章就會加入我們這次的獎金計劃，一起分得這2000美金的獎金。獎金的最後分配結果，我們也會公布出來，期待大家的參與！</p>  
</div>
            