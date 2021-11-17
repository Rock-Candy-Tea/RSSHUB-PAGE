
---
title: 'Insights_ 基於 Matters 「上千万文本數據」的分析之一：情感篇'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/09ffb870-1585-40ce-8b54-c675eac71e2f/000003.png'
author: Matters
comments: false
date: Wed, 01 May 2019 01:02:31 GMT
thumbnail: 'https://assets.matters.news/embed/09ffb870-1585-40ce-8b54-c675eac71e2f/000003.png'
---

<div>   
<p>好吧，我承認標題是用來唬人的（本文末尾有解釋）。</p><p>在 Matters 偶爾要寫寫代碼，搬搬磚。前些天，正優化搜索引擎時產生了一個疑問：</p><blockquote><strong>每天要索引的這些文字，它們是否也會像人類一樣表達情緒呢？它們到底開不開心？它們所表達的情緒是正面的，還是負面的？</strong></blockquote><p>抱着這樣的獵奇心理，從網上找了幾個情感詞典來爲 Matters 每個標籤的文章的用詞打分。大概思路是遇到代表正面、積極情緒的詞就 +1 分；反之，負面、消極的就 -1 分。之後，我們將每篇文章的得分加總，再除以相關詞語的個數，就是這些文章的「情感得分」。</p><p>當然，因爲這個方法太過簡單，所以即便得分爲負值，也並不代表相應文章所體現的情緒就一定是消極的。但是，如果我們將所有文章放在一起來對比，就會知道，總體相對來說，哪些文章更「消極」，那些文章更「開心」。例如下圖，選取文章「情感得分」平均下來最低/最高的標籤各20 個，可以發現「大屠杀 耶德瓦...」的文章，總體上顯然比「TechMoon」下的文章更消極，其他標籤同理，紅色表示相對更消極，藍色則更積極：</p><figure class="image"><img src="https://assets.matters.news/embed/09ffb870-1585-40ce-8b54-c675eac71e2f/000003.png" data-asset-id="09ffb870-1585-40ce-8b54-c675eac71e2f" referrerpolicy="no-referrer"><figcaption><span>按標籤劃劃分的文章「情感得分」的箱線圖</span></figcaption></figure><p>上圖中，雖然可以看到標籤下各自文章的情感分布，但是並不能體現文章數量對「情感得分」的整體影響。</p><p>如果我們把文章數量也考慮進來，可以看下圖，"score" 是各標籤文章得分加總，"article_count" 是各標籤文章數量，"avg_score" 是 "score ÷ article_count"，這樣處理之後，Matters 文章們的「小情緒」也就一目瞭然了，具體怎樣，大家可以自行觀察（作者太懶，不想繼續寫了，哼！）：</p><figure class="image"><img src="https://assets.matters.news/embed/72eceb77-dc81-43c8-9bfb-d46e5a2f3b41/00000c.png" data-asset-id="72eceb77-dc81-43c8-9bfb-d46e5a2f3b41" referrerpolicy="no-referrer"><figcaption><span>標籤「情感得分」對比圖</span></figcaption></figure><hr><p><em>想得到文章的詞彙數據，就先要將文章切分成一個一個的詞語，每個詞要有對應的標識數據，記錄這個詞在哪篇文章的哪一句話里出現過。在寫這篇帖子時，經過詞彙切分，得到的數據總共有 10,664,507 行，也就是所謂的「上千万文本數據」。</em></p>  
</div>
            