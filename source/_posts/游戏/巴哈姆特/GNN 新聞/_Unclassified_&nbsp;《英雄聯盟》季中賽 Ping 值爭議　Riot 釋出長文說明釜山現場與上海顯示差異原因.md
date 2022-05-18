
---
title: '_Unclassified_&nbsp;《英雄聯盟》季中賽 Ping 值爭議　Riot 釋出長文說明釜山現場與上海顯示差異原因'
categories: 
 - 游戏
 - 巴哈姆特
 - GNN 新聞
headimg: 'https://p2.bahamut.com.tw/B/2KU/74/fd22e7916e81d1ce55f230588e1gc5u5.JPG?v=1652796565838'
author: 巴哈姆特
comments: false
date: 2022-05-18 02:49:35
thumbnail: 'https://p2.bahamut.com.tw/B/2KU/74/fd22e7916e81d1ce55f230588e1gc5u5.JPG?v=1652796565838'
---

<div>   
<ul class="platform-tag"><li class="platform-olg"><a href="https://acg.gamer.com.tw/news.php?p=olg" target="_blank">PC 線上</a></li></ul>
<!-- 新聞內容 -->
<div>
<div>
<div>
　　《<a class="acglink" href="https://acg.gamer.com.tw/search.php?encode=utf8&kw=%E8%8B%B1%E9%9B%84%E8%81%AF%E7%9B%9F" target="_blank">英雄聯盟</a>》2022 季中邀請賽由於 Ping 值問題不斷引發玩家爭議、甚至讓玩家質疑比賽公平性，<a href="https://lolesports.com/article/riot-games-tech-blog-artificial-latency-for-remote-competitors/blt44154a33b5d5a616" target="_blank">Riot 今日釋出「遠程比賽時的人工延遲使用」技術說明</a>文章，解釋為什麼同樣的 Ping 值在上海與釜山參賽選手的螢幕上顯示會不一樣。</div>
<div>
 </div>
<div>
　　《<a class="acglink" href="https://acg.gamer.com.tw/search.php?encode=utf8&kw=%E8%8B%B1%E9%9B%84%E8%81%AF%E7%9B%9F" target="_blank">英雄聯盟</a>》2022 季中邀請賽由於配合 RNG 線上參賽，特別採用 35ms Ping 值，希望藉由讓現場隊伍與線上參賽的隊伍以同樣網路狀況的名義來進行比賽，但由於不少現場參賽選手在比賽前幾天都覺得延遲超過官方宣稱的 35ms，經 Riot 仔細分析後發現，的確前三日比賽日誌紀錄檔（Log）中呈現的延遲與在釜山比賽現場的體驗存在著差異，因而官方決定比賽第四天、更改現場網路環境配置，且因為 RNG 參與的比賽中出現未曾預料的對陣雙方延遲有不同的情況，Riot 宣布前三日 RNG 的對戰必須重賽，而這項重賽要求已經讓不少中國玩家感到相當不滿。</div>
<div>
 </div>
<div>
　　在小組賽最後一天比賽中，選手 Zeus 在 T1 與 SGB 比賽時直播帶到他個人畫面，眼尖的玩家發現顯示 Ping 值不是 35ms，而是 22 ms，使得賽後許多中國玩家到官方 Twitter 質疑是否這不公平，甚至還要求重賽。</div>
<div>
 </div>
<div>
<ul class="bh-grids-img">
<li class="bh-grids-img-box" style="width: 99.74%;">
<figcaption style="padding-bottom: 66.80%"><img alt="image" name="gnnPIC" class="lazyload" data-sizes="auto" src="https://p2.bahamut.com.tw/B/2KU/74/fd22e7916e81d1ce55f230588e1gc5u5.JPG?v=1652796565838" data-srcset="https://p2.bahamut.com.tw/B/2KU/74/fd22e7916e81d1ce55f230588e1gc5u5.JPG?w=1000 1x,https://p2.bahamut.com.tw/B/2KU/74/fd22e7916e81d1ce55f230588e1gc5u5.JPG 2x" style="max-width: unset;" title="T1（照片來源：Riot Games）" referrerpolicy="no-referrer"></figcaption>
<figure class="pic-desc">
T1（照片來源：Riot Games）</figure>
</li>
</ul>
</div>
<div>
　　面對玩家對 Ping 值的質疑，Riot 今日發表長文從技術角度層面來解釋他們此次處理 Ping 值的情況，內容解釋了釜山與上海間相隔大概 850 公里，從 RNG 戰隊基地到季中邀請賽的伺服器自然延遲約為 35 ms，而十支戰隊在釜山比賽場館自然延遲約 15ms，他們希望讓所有參賽隊伍在平等競技條件下競賽，因而決定導入人工延遲的方法、設定如 35ms 的目標值，讓大家保持同樣的網路環境。</div>
<div>
 </div>
<div>
　　Riot 針對小組賽頭三日釜山與上海網路延遲不同的問題解釋，他們使用延遲服務工具來讓所有參賽選手的 Ping 值都調整到 35ms 範圍，但這工具出現錯誤、讓釜山比賽現場的選手在比賽時會產生額外的延遲，使得其實際延遲高於場館電腦螢幕顯示 35ms。因此，在釜山現場隊伍與 RNG 連線對戰時，位於中國的選手是在 35ms Ping 值區間進行比賽，但在釜山的選手 Ping 值則更高，其根本原因是一個代碼漏洞錯誤計算了延遲，導致該數值在 Log 也是錯誤的，因此他們才決定 RNG 三場重賽，並修改配置來解決這個漏洞。</div>
<div>
 </div>
<div>
　　但 Riot 指出，5 月 13 日修改配置後，雖然實際 Ping 值已經修正、確保與上海對等，但位於釜山的選手螢幕顯示數值是錯誤的，導致直播播放選手螢幕畫面時，會呈現較低的 Ping 值，他們團隊未能即時將這個誤差與大家溝通，讓觀眾誤認為位於釜山的選手是以低於他們實際數值的 Ping 值進行比賽。</div>
<div>
 </div>
<div>
　　Riot 解釋，主要是由於當初解決延遲服務漏洞的方法是增加到配置中的補償偏移值，這種作法對於螢幕顯示數值會有副作用，導致在上海的選手螢幕顯示的 Ping 值是正確的、釜山的選手顯示數值會比實際低 13 ms，主要是因為上海使用延遲工具時、因為他們的 Ping 值本來就是 35ms 左右，因此工具不會加上補償，而釜山螢幕數字顯示不正確的原因，是因為引擎導入了延遲配置偏移量，讓實際延遲能夠達到 35ms ，但這將會使 Log 與 Ping 值顯示偏移約 13ms 的效應。</div>
<div>
 </div>
<div>
<ul class="bh-grids-img">
<li class="bh-grids-img-box" style="width: 99.87%;">
<figcaption style="padding-bottom: 49.94%"><img alt="image" name="gnnPIC" class="lazyload" data-sizes="auto" src="https://p2.bahamut.com.tw/B/2KU/72/77447430c9e8f86478ec87dd1e1gc5s5.PNG?v=1652796385849" data-srcset="https://p2.bahamut.com.tw/B/2KU/72/77447430c9e8f86478ec87dd1e1gc5s5.PNG?w=1000 1x,https://p2.bahamut.com.tw/B/2KU/72/77447430c9e8f86478ec87dd1e1gc5s5.PNG 2x" style="max-width: unset;" title="Zeus 的畫面顯示為 22ms，但實際上現場 Ping 值為 35 ms（照片來源：Riot Games）" referrerpolicy="no-referrer"></figcaption>
<figure class="pic-desc">
Zeus 的畫面顯示為 22ms，但實際上現場 Ping 值為 35 ms（照片來源：Riot Games）</figure>
</li>
</ul>
</div>
<div>
　　Riot 強調，技術團隊一直是以為職業選手創造同等競賽環境作為最高優先，也希望盡一切努力堅持競賽公平性，並為全世界粉絲創造更好的觀賽體驗。在這次事件中，他們未能及時發現漏洞影響了比賽，他們對 Ping 值顯示錯誤問題的溝通也不夠及時透明，再次對此造成的問題和困擾致以深深的歉意。</div>
<div>
 </div>
<div>
　　Riot 強調，他們正在進行額外的測試和驗證，以確保後面的對抗賽和淘汰賽階段順利。他們還要感謝隊伍和選手在此期間表現出的堅韌態度，儘管有諸多障礙，戰隊與隊伍仍為他們解決這些問題提供寶貴意見。雖然他們不敢斷言以後永遠不會再出現任何可能影響比賽的問題，但他們承諾一定從這次事件中吸取教訓，更即時地與隊伍和粉絲進行溝通，並持續地為良好的比賽環境做出自我監督和自我改進。</div>
</div>
<div>
 </div>
<p> </p>
<div class="article_gamercard lazyload" data-fanspage-id="125" data-from="web_gnn"></div>
<p style="font-size: 12px; padding: 10px 0;"></p>
</div>
<!-- 新聞內容結束 -->
  
</div>
            