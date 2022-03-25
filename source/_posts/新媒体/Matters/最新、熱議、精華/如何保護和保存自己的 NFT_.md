
---
title: '如何保護和保存自己的 NFT_'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://picsum.photos/400/300?random=1502'
author: Matters
comments: false
date: Thu, 24 Mar 2022 10:50:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=1502'
---

<div>   
<h2>本文探討的方向(以 Ethereum NFT 為例)</h2><ol><li>究竟 NFT 被存放在哪裡?</li><li>冷/熱錢包的功用是什麼?</li><li>擁有者如何保護自己的 NFT 降低被盜風險?</li></ol><hr><h2>一. 究竟 NFT 被存放在哪裡?</h2><p>NFT 是 Non-Fungible Token 的縮寫，NFT 也是 token 的一種，Token 存放和備份在以太坊(Ethereum)上的節點(Node)中，並可在以太坊上流通。</p><p>以太坊節點一覽: <a href="https://etherscan.io/nodetracker" rel="noopener noreferrer" target="_blank">https://etherscan.io/nodetracker</a></p><p>NFT 經由鑄造 (mint) 將智能合約與作品資訊、Metadata 和檔案儲存位置寫入並存放在區塊鏈上，而這些檔案儲存位置則是透過 NFT 中的 URI (Uniform Resource Identifier) 來指向 NFT 作品儲存的位置，可以是去中心化儲存的星際檔案系統 (IPFS) 或是去中心化儲存協議 (例如: Arweave 和 Filecoin)，又或是中心化儲存服務 (例如: AWS) ，儲存的位置取決於 NFT 項目決定要將作品/圖像保存在哪，讓 NFT 呈現時可以呼叫出來展示。</p><p>但有一些 NFT 作品是直接存在於區塊鏈上，無須透過指定的位置儲存。那就是區塊鏈生成藝術 (Generative Art)，透過演算法和智能合約就能將 NFT 作品呈現出來，而不受儲存管道限制。</p><hr><h2>二. 冷/熱錢包的功用是什麼?</h2><p>經常會有人誤以為自己的 NFT 是儲存在自己的冷/熱錢包之中，但實際上並非如此。那錢包到底在 NFT 的世界扮演什麼樣的角色?或發揮什麼樣的功用?</p><blockquote>錢包是使用者跟區塊鏈互動的媒介/工具，透過地址 (Address) 來做辨識。其中錢包組成的主要元素有「私鑰」、「公鑰」和「地址」。</blockquote><p><strong>1. 地址 (address): </strong></p><blockquote>由公鑰透過雜湊函數轉換生成地址，可以想像成公開的「銀行存簿帳號」。</blockquote><p><strong>2. 公鑰 (public key): </strong></p><blockquote>私鑰透過演算法進行加密後所產生的一組亂數，可以想像成「銀行戶名」。</blockquote><p><strong>3. 私鑰 (private key): </strong></p><blockquote>由裝置隨機產生的亂數，可以想像成「密碼」。</blockquote><p>即是先有了「密碼」(私鑰)，再開設「銀行戶名」(公鑰)，最後得到「銀行存簿帳號」(地址)，但是使用者的區塊鏈資產則是存放在區塊鏈上而非錢包之中。</p><p>要與區塊鏈互動(交易/傳送/授權)時才會是錢包發揮功用的時機，每次互動都需要有私鑰(密碼)才會成功送出交易到區塊鏈上，然後依據送出的請求(交易/傳送/授權)更改區塊鏈狀態，接著才會對使用者存放在區塊鏈上的 NFT 做出相對應的動作。</p><p>也因為地址是公開的，所以每個人都可以看到有什麼鏈上資產被存放在區塊鏈上的這個地址中，同時也能清楚檢視這個地址過去在鏈上的交易紀錄。</p><p><strong>4. 助記詞 (Recovery Phrase):</strong></p><p>私鑰由64位十六進制(16的64次方種可能組成)的字串組成，但是非常難記住，所以透過演算法產生多個英文單字來做到更加容易記住，這就是助記詞!</p><p>所以助記詞也是私鑰的另一種呈現方式，獲得助記詞等同於獲得私鑰，所以千萬要妥善保管。</p><p><strong>5. 冷/熱錢包的差異在哪?</strong></p><ul><li>熱錢包指的是私鑰與網路有連接上的錢包都可以被歸類為熱錢包，熱錢包的好處就是在使用上比冷錢包方便，但也因為連網的關係暴露在各種風險中，導致熱錢包的安全性沒有冷錢包好。</li><li>冷錢包指的是私鑰不與網路連接或是僅有非常少部分時間與網路連接的錢包，冷錢包的好處就是有比較高的安全性，通常冷錢包都是實體/硬體錢包所以會需要另外花錢購買。</li></ul><pre class="ql-syntax" spellcheck="false">最大的差異就是在於方便性和安全性，但是安全性是最需要被優先考慮的!
</pre><hr><h2>三. 擁有者如何保護自己的 NFT 降低被盜風險?</h2><p>「公鑰」和「地址」都不是我們要保護的!除了錢包<strong><u>密碼</u></strong>要保護外~</p><p><strong><u>要保護的是私鑰和助記詞! 要保護的是私鑰和助記詞! 要保護的是私鑰和助記詞!</u></strong></p><p>因為「私鑰」可以:</p><ul><li>轉移/出售這個地址在區塊鏈中的 Token(無論是 ERC-20 加密貨幣或是 ERC-721 以及 ERC-1155 NFT)。</li><li>簽署 (Sign Messages)，證明使用者擁有該地址的私鑰，用來完成交易的送出確認。</li></ul><p>只要被有心人是取得私鑰，他們就可以非常快速的從使用者的地址中盜走(轉移/賣出)資產。</p><p>最後，建議 NFT 參與者都備妥一個或以上的冷錢包，在安全的方式下保護自己的私鑰和助記詞!</p><hr><p>希望本篇基礎介紹，能幫助到對於 NFT 參與者理解 NFT 存在哪?以及如何保護 NFT 資產，喜歡或有幫助的話，請幫忙拍手給予支持哦~ </p><p>筆者正在 Matters Discord Community NFT 討論區擔任管理者，歡迎一起來討論哦!<br class="smart"></p><p><strong>Matters Discord: </strong><a href="https://discord.com/invite/matterslab" rel="noopener noreferrer" target="_blank">https://discord.com/invite/matterslab</a><br class="smart"></p><ul><li>歡迎已加入 Matters Discord 的太空軍，有空到 【🌠︱nft-討論區】一起討論或分享 NFT 相關資訊。</li><li>歡迎還沒加入 Discord 的朋友，一起加入太空軍參與社群早期建立，也許會有意想不到的收穫與驚喜哦。<br class="smart"></li></ul>  
</div>
            