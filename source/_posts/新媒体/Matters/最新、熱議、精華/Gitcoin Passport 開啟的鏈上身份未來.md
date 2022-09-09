
---
title: 'Gitcoin Passport 開啟的鏈上身份未來'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/e75e31e9-7ea7-489e-98f5-7ea78179d4dd.jpeg'
author: Matters
comments: false
date: Fri, 09 Sep 2022 04:13:55 GMT
thumbnail: 'https://assets.matters.news/embed/e75e31e9-7ea7-489e-98f5-7ea78179d4dd.jpeg'
---

<div>   
<figure class="image"><img src="https://assets.matters.news/embed/e75e31e9-7ea7-489e-98f5-7ea78179d4dd.jpeg" data-asset-id="e75e31e9-7ea7-489e-98f5-7ea78179d4dd" referrerpolicy="no-referrer"><figcaption><span>source : https://www.forbes.com/sites/forbestechcouncil/2021/12/10/how-decentralized-identity-is-reshaping-privacy-for-digital-identities/?sh=694662d33226</span></figcaption></figure><p>今年五月以太坊創辦人 Vitalik 寫了 <a href="https://vitalik.ca/" rel="noopener noreferrer" target="_blank">Soulbound</a>，接著與 E. Glen Weyl 及 Puja Ohlhaver 共同發表了<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763" rel="noopener noreferrer" target="_blank">去中心化社會</a>的論文，整個產業對於去中心化身份及社會的想像便幾乎成形了。但雖然願景遠大也令人興奮，但相關的開發團隊並不是太多，也許是缺乏明確商業模式的激勵，或是缺乏對應用場景的想像。我想快速寫篇文章來補一下這個溝，畢竟重塑社會架構這麼有趣的願景不能只有我跟幾個朋友知道。</p><p>（如果需要一些背景知識，去中心化社會論文的<a href="https://medium.com/@noahonward/%E5%8E%BB%E4%B8%AD%E5%BF%83%E5%8C%96%E7%A4%BE%E6%9C%83-4bad67eb0c23" rel="noopener noreferrer" target="_blank">簡短中文版</a>在這。）</p><p>任何帳號或身份系統都是一種產品或服務，他們服務特定的社會架構與交流方式。我們可能早就習慣線下社會的身分證或護照，持有身份證明讓我們能上學、能工作、能開車、能去夜店、能出國，但同時我們也得繳稅、得當兵、得盡各種國民義務。如果大量人口可以很容易的擁有或製造多重身份的話，國家的治理很容易出問題。我們已經很習慣這個方式，所以不曾想像身份有什麼替代方案。</p><p>但網路上的身份並不是這樣，我們可以創造無限的 Gmail 帳號去接收垃圾信件，也可以開無限了 twitter 帳號去假造輿論，在 Web1 看資訊及 Web2 社交互動/網路購物的世界雖然有點不方便，但似乎還不至於到無法忍受的地步。但到了 Web3 就比較麻煩了，Web3 講求數位資源的分配（代幣/NFT），如果某個服務打算發代幣給所有參與互動的人們，那一定會有人開一千個錢包領取一千份獎勵，這種女巫攻擊（Sybil Attack）就造成了不公平，容易讓參與者停止參與，平台也活不下去。</p><h1>Gitcoin Passport</h1><figure class="image"><img src="https://assets.matters.news/embed/8a77d2bd-db86-4ce0-8077-ff1eed62d8b7.jpeg" data-asset-id="8a77d2bd-db86-4ce0-8077-ff1eed62d8b7" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>Gitcoin Passport 可能是 DID 最完整的早期範例，他們的痛點也很明確。</p><p>Gitcoin 是全世界最大的加密貨幣捐款平台，他們採用平方募資法去分配資金，如果不知道平方募資是什麼可以看一下<a href="https://blocktrend.substack.com/p/260" rel="noopener noreferrer" target="_blank">這篇文章</a>，因為概念不新就不多加解釋。簡單說平方募資是讓越多人捐款支持（而不是獲得捐款最多）的專案可以獲得更多的資金，那這時候問題就來了，如果某個專案的提出團隊，開了一千個錢包，每個錢包只為專案捐款一塊美金，那專案大概可以拿走大部分的資金池，這完全抵消了平方募資讓捐款更公平分擔的初衷，投資人大概也不願意繼續在平台上捐款。</p><p>Gitcoin 的痛點明確，在 Gitcoin 平台的第 14 輪募資裡，44,886 中有 16,073個帳戶被偵測可能是機器人帳戶。明顯的他們急需確認平台上的捐款者們不是機器人，而是真正做出了捐款選擇的個人（Proof of personhood），這時候 Gitcoin Passport 就派上了用場。</p><blockquote><em>Gitcoin passport is a decentralized identity record, where you can collect “stamps” that show you have access to certain accounts, Twitter, Facebook, Bright ID, Google, ENS, etc.</em></blockquote><figure class="image"><img src="https://assets.matters.news/embed/fedb4358-dee4-4fd3-806d-204cf319c3ba.png" data-asset-id="fedb4358-dee4-4fd3-806d-204cf319c3ba" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>這是我找到其中一個對 Gitcoin Passport 比較完整的解釋。</p><p>邏輯其實也挺簡單的，以以太坊的錢包地址為身份中心，去連結 Web2 或是 Web3 的帳號，可以連結並證明擁有的帳號越多，你是人類而非網路機器人的機會就越高。如果你連結了所有的帳號服務，那在平方募資計算時，平台可能會把你算成 1.5 個人，如果你完全沒有做 Passport 的連結，平台也不會完全排除你身為人的可能，但會把你計算成 0.5 個人，Gitcoin Passport 的權重大概在 50%~150% 中間遊走。當然一個 Google 或 Twitter 帳號只能與一個以太坊錢包做連結。</p><p>對於機器人來說，創造、連結跟擁有這麼多帳戶（尤其還計算使用頻率或時長的時候 ex. 2008 開啟的 twitter 帳號權重比 2022 的高許多）的達成成本大概太高。</p><p>如果捐款者希望自己的捐款影響力更大，更有意義，那他們就有動機去連結更多帳戶，連結的帳戶也有多種領域的選擇（其中也包括 BrightID 的親友認證與 Proof of Humanity 等），分散錢包作為機器人的風險。</p><p>Gitcoin Passport 作為一個身份系統，他的作用並不是將不做身份認證的使用者拒於門外，而是保持開放參與，但鼓勵有做身份認證的個人，作用是激勵，而非歧視。Gitcoin 在沒有大肆宣傳的情況下目前已經有 30% 的錢包使用 Passport，每個使用 Passport 的錢包平均都連結了至少一個帳號，在 Gitcoin 生態系裡快速印證了市場採用。</p><h1>Beyond Gitcoin</h1><p>有趣的是 Gitcoin Passport 的應用並不止於此，所有去中心化應用都可以接上 Gitcoin Passport SDK，並為自己的應用客製細節。幾個去中心化應用可以透過 Gitcoin Passport 做到的事</p><ul><li>dApps 可以驗證有經過 Gitcoin Passport 流程的以太坊錢包，並針對他們所連結的帳戶計算一個人類分數</li><li>dApps 接下來可以針對這個人類分數決定要開放什麼樣的服務或內容給這個錢包的擁有者</li></ul><p>Gitcoin 的部落格上也提到某些特定的應用</p><ul><li>想採用平方募資法的平台</li><li>HSBC 在 2012 年開了 50,000 個帳戶幫助毒梟集團匯出 2.1B 美金，在 KYC 對平台太過昂貴的情況下，Gitcoin Passport 是個好的替代方案</li><li>在 Ceramic Network 上的 Gitcoin Passport 讓使用者可以自行決定要透露多少資料給服務組織，在不提供個人資料細節下證明身份，在隱私上也可以起到保護作用</li><li>未來所有 DAO 的激勵機制必須要建立在公平基礎上，以避免女巫攻擊的發生。任何『激勵參與』的機制，大概都會需要去中心化身份的輔助</li></ul><p>這些範例創造許多新的可能，如果 Web3 分享擁有權及數位資產/資源的未來繼續散播到更多的線上線下組織，那去中心化身份的應用大概就無可避免。</p><h1>Beyond Proof of Personhood</h1><p>延伸一下去中心化身份的未來，Proof of personhood 的目的在於證明人類身份，能確實證明人類身份就解決了女巫攻擊的問題。但也許我們可以不用停在這，因為近期與公民組織頻繁互動，所以再以公民組織為例。</p><p>假設公民組織的文化鼓勵行動與貢獻，貢獻越多者可能會獲得更多的社交與其他資源。如果把上述的社群帳號連結想像成公民組織（如 g0v）內的各個專案，讓個人貢獻者的參與深度、廣度及品質可以被紀錄並計算成貢獻分數，便有了個清楚的路徑讓個人貢獻者取得更多社群的話語權與社交資源，激勵個人持續貢獻。當然這只是我的猜測與臆想，實際情況要與更多社群參與者聊了之後才會知道。</p><p>在公民組織的案例裡比較有趣的是系統希望證明的並不是像 Gitcoin Passport 一樣的『人類』身份，而是一個『貢獻者』身份，只要同一個專案貢獻不能被雙重認領，那就算貢獻者擁有兩個錢包/身份也無所謂，這更像是一種個人選擇。</p><p>最簡單也直接在話語權或是社交資源的展示方式是投票，社群決策總是會碰到意見不合的時候，專案內部的決策投票權重可以以單一貢獻身份對該專案貢獻分數作計算，提高投票權中，形成一套特殊的決策系統。</p><p>當然這一切都得建立在貢獻機制是公平的情況之下，這也許才是最難的。如果希望貢獻者持續貢獻，那也許只計算一定時間內的貢獻分數，以維持社群決策能力的相關性（也許總統重選的四年標竿是個好參考），四年後將決策能力替換成某種徽章也說不定。</p><p>Gitcoin Passport 可以印證『人類』身份，公民組織內可以建立『貢獻者』身份，產品團隊可以建立『工程師』身份，公民可以建立『台北參與者』身份，遊戲可以建立『玩家』身份，各種不同的情境都可以建立不同的去中心化身份，並將平台、協議、社會的資源做分配，端看在每個不同的小社會裡，我們激勵什麼樣的行為，也定義什麼叫做『公平』。</p><figure class="audio"><audio controls data-file-name preload="metadata"></audio><div class="player">
      <header>
        <div class="meta">
          <h4 class="title"></h4>

          <div class="time">
            <span class="current"></span>
            <span class="duration"></span>
          </div>
        </div>

        <span class="play"></span>
      </header>

      <footer>
        <div class="progress-bar">
          <span></span>
        </div>
      </footer>
    </div><figcaption><span></span></figcaption></figure><p><br></p><p><br></p>  
</div>
            