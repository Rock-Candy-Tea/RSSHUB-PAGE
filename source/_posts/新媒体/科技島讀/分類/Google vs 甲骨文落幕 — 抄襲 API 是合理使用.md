
---
title: 'Google vs. 甲骨文落幕 — 抄襲 API 是合理使用'
categories: 
 - 新媒体
 - 科技島讀
 - 分類
headimg: 'https://daodu.tech/wp-content/uploads/2021/04/image-compressed.jpg'
author: 科技島讀
comments: false
date: Wed, 07 Apr 2021 22:20:09 GMT
thumbnail: 'https://daodu.tech/wp-content/uploads/2021/04/image-compressed.jpg'
---

<div>   
<p style="text-align: left;"><span style="color: #999999;">閱讀時間 12 分鐘</span></p>
<h2>Android 選擇抄襲</h2>
<p>2005 年，地球仍是 Nokia、黑莓機等「半智慧手機」橫行的時代。智慧型手機山雨欲來，但尚未呱呱落地 — 要等到 2 年後 iPhone 才會問世。許多公司正緊鑼密鼓地秘密開發智慧行動裝置。</p>
<p>其中一家公司是 Google。Google 併購了新創 Android。Android 團隊決定以 Java 語言為核心，建造新一代的手機作業系統。當時 Java 主要用於電腦與伺服器。而團隊負責人 Andy Rubin 指出 Java 已有眾多的開發者與詳盡的文件，是發展智慧型手機系統的最好起點。</p>
<p>問題是 Google 需取得 Java 的擁有者昇陽（Sun Microsystems）的授權。然而雙方始終無法談成。最終 <a href="https://daodu.tech/07-01-2015-google-%e6%9c%80%e9%ab%98%e6%b3%95%e9%99%a2%e4%b8%8a%e8%a8%b4%e5%a4%b1%e6%95%97%ef%bc%8coracle-%e5%88%86-android-%e4%b8%80%e6%9d%af%e7%be%b9%e5%86%8d%e9%80%b2%e4%b8%80%e6%ad%a5" data-wpel-link="internal">Andy Rubin 在一封內部信中留下兩個選項</a>：</p>
<blockquote><p>. . . . 如果昇陽不想跟我們合作，我們有兩個選項：（1）放棄並改用微軟的 CLR VM 與 C# 語言，或（2）<b>硬做 </b>Java 然後捍衛我們的決定，一路上豎立許多敵人。</p></blockquote>
<p>Google 選擇（2）硬做。Google 希望吸引 Java 工程師轉來為 Android 開發，於是採用了一個巧妙的作法：它沒有照抄 Java 的所有程式碼，而是只抄襲了 Java 的應用程式介面（Application Programming Interface, API）。</p>
<p><a href="https://daodu.tech/07-01-2015-google-%e6%9c%80%e9%ab%98%e6%b3%95%e9%99%a2%e4%b8%8a%e8%a8%b4%e5%a4%b1%e6%95%97%ef%bc%8coracle-%e5%88%86-android-%e4%b8%80%e6%9d%af%e7%be%b9%e5%86%8d%e9%80%b2%e4%b8%80%e6%ad%a5" data-wpel-link="internal">我曾舉例解釋什麼是 API</a>：</p>
<blockquote><p>想像有一個圖書館，專門蒐集各種工具書。圖書館裡有 37 個書架。每一個書架上放同領域的書。例如個人理財書架上放了很多個人理財的書。廚藝書架上放很多廚藝的工具書。</p></blockquote>
<blockquote><p>每一本工具書裡有不同章節。例如廚藝書架上其中一本是《快速牛肉料理大全》。書的其中一章是「蔥爆牛肉」。</p></blockquote>
<blockquote><p>每一章裡還分兩部分，「材料準備」與「實際製作」。例如「蔥爆牛肉」這一章，會先有一個材料準備：「綠蔥至家樂福買。牛肉需澳洲牛，可以在 Costco 買。另外準備醬油。」實際操作的部份，則描述做菜流程：「蔥爆香，再下牛肉跟調味料」。</p></blockquote>
<blockquote><p>Google 的巧妙之處，便是在蓋 Android 圖書館時，照抄了 Java 圖書館的 37 個書架名，以及這 37 個書架內，共 7,000 行的「材料準備」。Google 沒有抄實際操作的章節。</p></blockquote>
<p>注意 Google 重新寫了「實際製作」的部分的程式碼 — 因為要配合手機的特性 — 這部分稱之為執行碼（implementing code）。但 Google 照抄了 Java 共 37 大項，11,500 行的「材料準備」部分，稱之為屬性宣告碼（declaring code）。Google 也照抄了「書架」、「章節」的名稱以及其組織方式（如<a href="https://daodu.tech/07-01-2015-google-%e6%9c%80%e9%ab%98%e6%b3%95%e9%99%a2%e4%b8%8a%e8%a8%b4%e5%a4%b1%e6%95%97%ef%bc%8coracle-%e5%88%86-android-%e4%b8%80%e6%9d%af%e7%be%b9%e5%86%8d%e9%80%b2%e4%b8%80%e6%ad%a5" data-wpel-link="internal">下圖</a>）。</p>
<p>抄的好處是當 Java 的工程師轉過來時，就不用重新學習 API 架構；只要使用已知的指令呼叫方式（method call）就能上手。<br>
<img class="aligncenter size-full wp-image-9897" src="https://daodu.tech/wp-content/uploads/2021/04/image-compressed.jpg" alt width="567" height="485" srcset="https://daodu.tech/wp-content/uploads/2021/04/image-compressed.jpg 567w, https://daodu.tech/wp-content/uploads/2021/04/image-compressed-300x257.jpg 300w, https://daodu.tech/wp-content/uploads/2021/04/image-compressed-440x376.jpg 440w" sizes="(max-width: 567px) 100vw, 567px" referrerpolicy="no-referrer">Google 的策略成功了。Android 免費、開源，迅速席捲市場，成為市佔率最高的手機作業系統。Google 也賺到滿滿的錢。相對的，昇陽卻日落西山，於 2010 年被甲骨文（Oracle）併購。</p>
<p>甲骨文於 2010 年控告 Google 侵犯其著作權。此案纏訟 10 年，不僅影響數百億美金的手機市場，也牽動軟體業的運行方式，被稱為「十年來最重要的著作權案」。</p>
<p>終於，本週美國最高法院做出了蓋棺論定：Google 勝訴。根據 <a href="https://www.techbang.com/posts/85705-google-and-oracles-10-year-copyright-case-was-reversed-and-the" data-wpel-link="external" target="_blank" rel="external noopener noreferrer">T 客邦</a>報導：</p>
<blockquote><p>美國最高法院週一裁定，Alphabet 公司旗下的 Google 公司使用甲骨文公司的軟體程式碼所構建在全球大多數智慧手機上執行的 Android 系統，並未違反聯邦 [著作權] 法。這是 Google 的一大勝利</p></blockquote>
<blockquote><p>法官們以 6 票贊成、2 票反對的結果推翻了下級法院的裁決。先前法院判定 Google 將甲骨文的軟體程式碼包含在 Android 系統中是不合理使用，違法美國 [著作權] 法，需賠償 88 億美元。</p></blockquote>
<blockquote><p>大法官 Stephen Breyer 表示，允許甲骨文在其程式碼上執行 [著作權]，將使其成為「限制新程式未來創造力的枷鎖」，從而損害公眾利益。</p></blockquote>
<p>以下我將討論 Google 為何勝訴，以及此一判決對軟體業的影響。</p>
<h2>著作權是手段</h2>
<p>為何 Google 擺明是抄襲，而且是為了挖角別家的開發者，卻可以勝訴？</p>
<p>首先要理解著作權是一種手段，不是結果本身。著作權的存在是為了鼓勵創作，特別是鼓勵創作那些易於複製的東西，例如電影、書、音樂等。如果沒有著作權保護，作品可以任意複製，作者無法從作品中獲利，那就沒有人要創作了。因此才會有著作權 — 著作權的目的是激發科學與藝術（science and art）。</p>
<p>也因此著作權的保護不是絕對的。著作權本質上是為了一個人（著作權人）的利益，限制整個社會的行為。所以（美國）國會也設下許多限制，限縮著作權的涵蓋範圍。例如若一個領域就算沒有著作權保護，仍然蓬勃發展，那麼著作權就不需要過度的伸張。</p>
<p>而<a href="https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf" data-wpel-link="external" target="_blank" rel="external noopener noreferrer">美國最高法院本次判決</a>的核心，就是認為允許 Google 抄襲 Java 的 API 反而有助於創造更活絡的軟體環境。</p>
<p>不過這是跳到結論。我們先倒回去，討論個別的論點。Google 在上訴中提出了兩個主要辯護論點。</p>
<p>第一，Google 主張 API <b>不受著作權保護</b>。Google 主張 API 這種分類方式，是一種概念、一種數學方程式，或是一種操作方法（method of operation），不該受著作權保護。就像物理課本裡的地心引力公式，或是字典的索引不應該受著作權保護一樣。</p>
<p>相反的，甲骨文則主張設計 API 是需要高度創造力。設計一套直覺、易記的 API 並不簡單，跟寫出《哈利波特》一樣需要創意。而且 API 有許多種設計方式 — 微軟與蘋果後來都開發出自己的 API — 因此甲骨文所選的設計當然應該享有著作權的保護。</p>
<p>這其實是本案最重要的爭執點，也是軟體業最關心的部分。很可惜最高法院迴避了此一問題，只說「為了方便討論，我們<b>假設 </b>API 具有著作權保護」，並直接跳到下一個論點。</p>
<h2>合理使用</h2>
<p>第二，Google 主張其是<b>合理使用 </b>Java 的 API。</p>
<p>合理使用（fair use）是可以侵犯別人著作權的例外狀況。如前述，著作權的保護不是絕對，會受到其他權利的限制。例如美國憲法第一修正案保證言論自由，因此雖然電視新聞享有著作權；但如果我想要抨擊、嘲諷電視新聞，就可以取用其中一小段，拿來製作抨擊內容的材料。這是一種合理使用。</p>
<p>常見的合理使用包括評論、嘲諷、教學、研究、逆向工程等。根據美國著作權法，法院必須根據 4 個要點來評估是否為合理使用：</p>
<ol>
<li>使用的目的和性質；</li>
<li>著作權作品的性質；</li>
<li>相對整個有著作權作品相比所使用的內容和數量；以及</li>
<li>這種使用對有著作權作品的潛在市場或價值所產生的影響。</li>
</ol>
<p>更白話文就是：</p>
<ol>
<li>為什麼抄；</li>
<li>被抄的是什麼樣的東西；</li>
<li>抄了多大比例；以及</li>
<li>抄了害對方損失多少。</li>
</ol>
<p><a href="https://daodu.tech/07-01-2015-google-%e6%9c%80%e9%ab%98%e6%b3%95%e9%99%a2%e4%b8%8a%e8%a8%b4%e5%a4%b1%e6%95%97%ef%bc%8coracle-%e5%88%86-android-%e4%b8%80%e6%9d%af%e7%be%b9%e5%86%8d%e9%80%b2%e4%b8%80%e6%ad%a5" data-wpel-link="internal">我曾以 DJ 說明一種合理使用</a>：</p>
<blockquote><p>. . . . 某夜店 DJ 擷取（sample）了 Taylor Swift 情歌的片段，放在舞曲組曲中。這時雖然他用到了 Taylor Swift 的情歌，但是是有限的使用，並且有轉換其意義（transformative），不會讓人誤解 DJ 是原唱，也不會傷害到 Taylor Swift 的情歌市場。那麼基於鼓勵創作的公益性，這樣的侵權沒有關係。</p></blockquote>
<p>在本案中，多數法官認為 4 個考量要點都對 Google 有利。</p>
<p>法官首先考慮第 2 要點。他認為被抄的 API 與一般的程式碼不同，其並不直接執行任務，只是開發者與程式碼之間的介面（interface），且主要價值源自於開發者對於 API 的熟悉度，因此抄襲更可能是合理使用。</p>
<p>在第 1 要點上，法官認為 Google 的抄襲也是一種轉化（transformative）使用 — 從電腦轉移到手機。因此不會替代原本的使用情境。</p>
<p>在第 3 要點上，法官認為 Google 抄襲的 API 僅佔總程式碼的 0.4%。而且 Google 不是為了 API 的「創意或美麗」而抄襲，而是為了讓開發者能更快上手，不算實質性的（substantively）抄襲。這有點類似我製作一個同樣使用 QWERTY 介面的鍵盤，不是因為這樣的排列特別美麗或好用，而是因為大家都習慣了。</p>
<p>在第 4 要點上，法官認為 Android 並不是 Java 的競爭者，沒有傷害 Java 的市場。也沒有證據證明如果 Android 沒有抄襲，甲骨文就能成功地進軍手機市場。事實上法官認為 Android 帶動更多人熟悉 Java 語法，反而擴大了 Java 的市場。</p>
<p>基於以上四點，多數法官認為 Google 抄襲 Java 的 API 屬於合理使用。允許其合理使用有助於加快軟體發展，且沒有傷害到甲骨文的原有市場，因此判決 Google 勝訴。</p>
<h2>軟體業安心</h2>
<p>判決一出，軟體社群大多一片好評，紛紛驚呼：「心頭大石終於落地了。」因為使用既有的 API，再重新寫執行碼在業界實已是常態。如果甲骨文勝訴，整個軟體業都要重新調整。</p>
<p>然而發表不同意見書的 Clarence Thomas 大法官則指出，多數法官的判決迴避了核心的問題 — API 是否可以享有著作權保護 — 而且違背商場現實。他認為 Android 當然傷害了 Java 在手機市場的機會。Thomas 指出 Java 原本是手機領域最普及的程式語言。原本亞馬遜、三星都與甲骨文簽有 Java 的授權協議；但因為 Google 沒付錢、Android 又是開源的，導致亞馬遜把授權金砍到原本的 2.5%，三星的授權金則從 4 千萬美金掉到 1 百萬美金。</p>
<p>Thomas 也不認為 Google 的使用方式有什麼「轉化」— 兩者 API 的功能根本一模一樣，從電腦到手機也不算真正的跨市場。他進一步質疑，如果誰都能抄襲，那麼未來誰還願意投資開發直覺、好記的 API 呢？</p>
<p>從產業的角度來看，我同意多數大法官的意見。「挪用」API 已是常態，現在只是確認為合法使用。目前看來新 API 前仆後繼地出現，並沒有缺乏投資的狀況。如果判決反過來，變成每次寫新的軟體平台都要重學 API 或是付授權金，的確會動盪整個產業。</p>
<p>未來軟體之間的 API 會更接近，更容易相容（interoperable），也更容易開發。不過我不確定長期是否真的對整個軟體社群有利，還是對大企業更有利。未來大公司看到有潛力的開源碼專案或是新創的程式碼，也可以照抄 API，吸走客戶，靠規模擊敗新創。這對 <a href="https://daodu.tech/10-29-2020-stripe-acquire-paystack-more-chaos-more-valuable" data-wpel-link="internal">Stripe</a> 與 <a href="https://daodu.tech/01-16-2020-visa-acquire-plaid-for-5-3-billion-dollars-high-risk-high-reward" data-wpel-link="internal">Plaid</a> 等「API 企業」都是新的挑戰。</p>
<p>我可以確定的是，最高法院用了 62 頁判決，其中超過 10 頁解釋何謂軟體平台、API 與程式碼，證明了軟體已成為社會的骨幹，亟需更多權利義務的定義。只是軟體可以輕鬆的決定哪一個指令能呼叫哪一個任務，法院卻得花 10 年才能釐清人際之間的利益衝突。</p>
                
                
  
</div>
            