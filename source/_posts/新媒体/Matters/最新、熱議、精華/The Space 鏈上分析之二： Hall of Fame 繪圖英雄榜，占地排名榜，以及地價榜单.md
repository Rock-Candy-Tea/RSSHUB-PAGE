
---
title: 'The Space 鏈上分析之二： Hall of Fame 繪圖英雄榜，占地排名榜，以及地價榜单'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/9122f58e-295e-4cc8-b173-863b191a824d.png'
author: Matters
comments: false
date: Sat, 18 Jun 2022 03:01:46 GMT
thumbnail: 'https://assets.matters.news/embed/9122f58e-295e-4cc8-b173-863b191a824d.png'
---

<div>   
<p>上周看到『<a href="https://matters.news/@daisy/293879-the-space" rel="noopener noreferrer" target="_blank">The Space | 瘋狂的一夜，一晚畫了一千像素</a>』就一直想知道，當前地圖上這樣瘋狂畫圖的人 除了 <a class="mention" href="https://matters.news/@daisy" target="_blank" data-display-name="Daisy" data-user-name="daisy" data-id="VXNlcjo2MDQ">﻿<span>@Daisy</span>﻿</a> 還有多少？</p><p>續上一篇 thespace."TheSpaceRegistry_evt_Color" events table 的使用，因為所有的繪圖事件 (events) 都一定會 emit 出一個 color event, 那麼查詢 evt_Color table 就能拿到所有人的繪圖過程，</p><pre class="ql-syntax" spellcheck="false">SELECT owner, COUNT(*) AS count_drawings,
 COUNT(DISTINCT "tokenId") AS count_pixels
FROM thespace."TheSpaceRegistry_evt_Color"
GROUP BY 1
ORDER BY count_drawings DESC
</pre><p>上一篇已提到 COUNT(*) 可以做整體統計，除此以外它還可以分類統計，就是 GROUP BY 語句， 在 SELECT 之后放上 想要分類的項，此处用 owner, 并且在 FROM ...table 之后加上 GROUP BY ... 那麼 SELECT 后面就可以用 COUNT 作 「對此 owner 分類的」計數，比如 COUNT(*) 統計了整個繪圖次數，還可以用 COUNT(DISTINCT "tokenId") 統計不重複的 tokenId 數，此處 tokenId 對應的是 一百萬個像素的編號，也通俗理解為地塊編號；點击「Run」查詢，可以看到截止現在有 203 個錢包曾有過畫過；還可以看到 count_drawings vs count_pixels 是有差别的，應該是有很多像素發生了争搶的情况，被人繪成别的，自己再搶回来，當然也可能是很多人對畫好的顏色并不滿意，再来繪一次别的顏色。</p><pre class="ql-syntax" spellcheck="false">SELECT owner, COUNT(*) AS count_drawings,
 COUNT(DISTINCT "tokenId") AS count_pixels,
 SUM(gas_used*gas_price)/1e18 AS gas_matic
FROM thespace."TheSpaceRegistry_evt_Color"
JOIN polygon.transactions ON hash=evt_tx_hash
GROUP BY 1
ORDER BY count_drawings DESC
</pre><p>除此之外，因為 event table 都有存了原始的 對應 鏈上交易的 evt_tx_hash 此處也可以 順便展示其用途，即 對 polygon.transactions 這樣的 raw table 進行 JOIN Query, 聯合查詢，聯合的 field 是 evt_tx_hash 對應 polygon.transactions 上的 hash 這樣 可以想像两張 table 按相同的 hash 對接在一起 方便用。這里的例子只用到 polygon.transactions 里面的 gas_used*gas_price 這就是實際用到的 matic gas fee, 在 GROUP BY 語句中 除了 COUNT 還有類似的 SUM(...) 顾名思義就是統計求和，看看他們分别在 TheSpace 費了多少 Gas,  因為 Gas 的使用單位是 Matic, 内部与 Ether 相同的有小數點后 18位，所以 除以 科學計數法 (1e18) 就是變为以 Matic 為單位了</p><p>查詢結果已加入 <a href="https://dune.com/bluebasketbooks/thespace-dashboard" rel="noopener noreferrer" target="_blank">https://dune.com/bluebasketbooks/thespace-dashboard</a> 這張 Dashboard</p><figure class="image"><img src="https://assets.matters.news/embed/9122f58e-295e-4cc8-b173-863b191a824d.png" data-asset-id="9122f58e-295e-4cc8-b173-863b191a824d" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>其中 Daisy 的帳號 \x2af159c310... 也僅排第二而已，那麼排名榜單第一的 \x64110f5b... 究竟是誰？</p><p>又或者，因為上面結果是 TheSpace上線十几天以来的總計，如果按單日計算呢，Daisy的一晚畫了一千像素會不會是第一？答案在這里有了， <a href="https://dune.com/queries/920536?d=7" rel="noopener noreferrer" target="_blank">https://dune.com/queries/920536?d=7</a> 提示：按ㄖ分類也只不過是增加一個 GROUP BY 的維度，在 PostgreSQL 的語法是 date_trunc('day', evt_block_time) ::date AS ... 轉換為日期，結果仍然是 \x64110f5b... 以單日 1,117 drawings 排名榜首～ ( 當然這里通用的是 UTC 國際日期，而你所實際住地的 單日 繪了很多有可能在 UTC 被分到前后两日去了，有兴趣者還可以查 PostgreSQL 的時區函式来轉換使用當地ㄖ期 )</p><p><br></p><h2>(二) 占地排名榜</h2><p>上面問題在前幾天已加上到 Dashboard, 被眼尖的讀者 ( <a class="mention" href="https://matters.news/@bornnaked" target="_blank" data-display-name="裸子" data-user-name="bornnaked" data-id="VXNlcjo3OTQyNw">﻿<span>@裸子</span>﻿</a> ) 已發現，與 Polygonscan 上去對照，怎麼會不一樣？確實有可能有差異，因為上一篇說了，Dune的數據可能有 up to 3 hours delay。但如果三小時已過， TheSpace 上當前的近三小時并未有 新的繪圖 events, 那么就肯定是有一邊數據并未更新到最新。</p><p>另外一個原因，則来自，可能統計的是事情的不同面向。</p><blockquote>與 Poygonscan 上的這個 Quantity(token) 數量對不起來，</blockquote><p>具體來說，繪圖事件 與 Planck (PLK) holders 并非同一概念。繪圖事件僅僅是繪圖，可能是自己涂自己的地，只是變換顏色未有所有權轉移；而 hold 一個 Planck (PLK) 則有可能只是單純的買地，并未變換顏色。</p><p>于是，在 Polygonscan 上再研究，如果只買地不重畫顏色，會有何種 events?答案在 thespace."TheSpaceRegistry_evt_Transfer" 里面找到了，這一張 events table 記录的就是單純 ownership 轉移，有 "from" "to" "tokenId" 這几項就够用了，當然，与其它 events table 類似的是 也有 evt_block_time/evt_hash/.. 等等，在有需要時可以用于 JOIN Query</p><pre class="ql-syntax" spellcheck="false">WITH last_owners AS (
  SELECT DISTINCT ON ("tokenId") *
  FROM thespace."TheSpaceRegistry_evt_Transfer"
  ORDER BY "tokenId", evt_block_number DESC, evt_index DESC
)

SELECT "to", COUNT(*),
  MAX(evt_block_time) AS latest,
  (ARRAY_AGG("tokenId" ORDER BY evt_block_time DESC))[1:5] AS last_5
FROM last_owners
GROUP BY 1
ORDER BY count DESC, latest DESC
</pre><p>這里同樣先說結好了，需要從 thespace."TheSpaceRegistry_evt_Transfer" 里面查到結果，但因為這張事件表 記录了所有 ownership 轉移的情况，而為了對每 Planck (PLK) 只查最后一任 owner (地主), 需要一次 DISTINCT ON ("tokenId") 查詢，其含義是對每個 Planck 交易情况，只需要知道最后一次易手纪录，在 ORDER BY "tokenId" 之后可以按時間查詢 Descending 排序的最后一次記录，里面可以使用 evt_block_time DESC 与 evt_block_number DESC 也几乎相同，但在其它類似 高頻交易中有 多個 tokenId 在相同 block_number 的情况，得到相同的 evt_block_time, 于是外加上  evt_index DESC 更多一層保障。</p><p>得到 \x2af159c310e... 以 2841 holdings 與 Polygonscan 結果完全對應！　197 個帳號持有 27,000+ 對應2萬7千多個已開發地塊，并且与前 面 203 accounts 并不一致的原因是有人曾畫過但后来其手上所有 地塊都被人買走了</p><figure class="image"><img src="https://assets.matters.news/embed/ffa69821-4841-4c61-8b6f-57cae5c32a37.png" data-asset-id="ffa69821-4841-4c61-8b6f-57cae5c32a37" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>這里，還同時使用了 MAX(evt_block_time) 得到 每 owner 的最后一次 入手時間，以及 (ARRAY_AGG(...))[1:5] 等等順便取得每人的最后 5 次入手的地塊 (Planck) 編號，更為方便對照。</p><p><br></p><h2>(三) 地價榜单</h2><p>地價榜單，也是最多人問及的。同樣的工作原理，也是在 Polygonscan 上去尋找，定價過程中會觸發什麼 events? 然后在 thespace.* 這些 decoded tables 中去寻找</p><p>答案在 thespace."TheSpaceRegistry_evt_Price" 找到</p><pre class="ql-syntax" spellcheck="false">WITH prices AS (
  SELECT DISTINCT ON ("tokenId") price/1e18 AS price_spaces, *
  FROM thespace."TheSpaceRegistry_evt_Price"
  ORDER BY "tokenId", evt_block_time DESC
)
SELECT *
FROM prices
-- WHERE price_spaces>=100
ORDER BY price_spaces DESC, evt_block_time DESC
</pre><p>同樣的原理，也使用 DISTINCT ON ("tokenId") 只关心查每 Planck 的最后一次定價，去重複，得到 臨時 prices table, 同時，因為 $Space幣同樣内部使用了小數點后 18位， 為了讀價方便，這里先計算 price/1e18 AS price_spaces 得到以 $Space為單位的數字</p><p>最后從 SELECT * FROM prices 讀出所有 columns, 想知道 定價榜单？就 按 定價  price_spaces 排降序就是了，得到 已開發過的 (minted) 所有 27,000+ 地塊的 價目表，</p><p>其中 "-- WHERE price_spaces>=100" 以 -- 開頭在 SQL 中是注釋掉，暫不運行的意思，你也可以試試 取消注釋，看看定價大于 100$Space 幣的地塊有多少？想知道定價最貴的地塊價錢是多少 ？ 答案是 1,0000,0000 $Space, 一個億的 $Space幣！</p><pre class="ql-syntax" spellcheck="false">price_spaces tokenId price owner
100000000 728415 1e+26 \x437b672246e4e2....
100000000 683092 1e+26 \x437b672246e4e2....
</pre><p>具體位置在哪儿，都来觀摩一下？ 根據 tokenId 728415 = (y-1)*1000+x 来反向計算，其定位在 (415,729), 在這兒～</p><p>　那個 紅色 「Default Risk」什麼意思？ 應該喊「清稅官」在哪里 ？這位已經 Due Tax 3千4百多萬了</p><figure class="image"><img src="https://assets.matters.news/embed/7ffa3d72-b7bc-405e-a6f9-9cf8f8460319.png" data-asset-id="7ffa3d72-b7bc-405e-a6f9-9cf8f8460319" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p><br class="smart"></p><p><br></p><p><br></p>  
</div>
            