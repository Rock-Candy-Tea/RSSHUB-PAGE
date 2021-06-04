
---
title: '快快樂樂學EXCEL'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/cf1a58b5-4eb8-4e2f-ace5-acf33c944b4d.png'
author: Matters
comments: false
date: Thu, 03 Jun 2021 13:34:45 GMT
thumbnail: 'https://assets.matters.news/embed/cf1a58b5-4eb8-4e2f-ace5-acf33c944b4d.png'
---

<div>   
<p>朋友們在工作上都需要使用EXCEL試算表。粗暴地把用家分成幾種：</p><ul><li>懂得用VBA的神經病</li><li>會用VLOOKUP和PIVOT的老屎忽（屁股）</li><li>懂跟不懂沒差別的小白</li></ul><p>這種分類其實沒意義。無論你屬於哪種，在商業社會文書環境裡，沒了下面的東西，你就是不會用EXCEL：</p><ul><li>你要有MICROSOFT EXCEL，最好是定期更新的版本</li><li>你要有互聯網連線，能使用GOOGLE SEARCH</li><li>你要有好的邏輯思維和拆解問題和需要的能力</li></ul><p>能寫VBA、能說一大堆專業用語當然好，但都不及上面三點重要。太厲害的檔案一般都有以下的問題：</p><ul><li>太複雜，傳到菜鳥手裡便被破壞掉</li><li>弄得太FOOL-PROOF的話，沒那麼容易被破壞，但卻犧牲掉靈活性</li><li>更新困難。若創作者離職，換到菜鳥手裡便成為垃圾；換到高手手裡又會成了眼中盯，也是難逃被完全更改的命運</li></ul><p>絕大部分的情況下，用家需要的不是高超的技術，而是解讀需求及尋求方案的能力。而這種能力，來源於思考、實踐，和經驗分享。</p><p>易大師這就來分享一下經驗。大家覺得有用的話，在下面留個言讓大師知道。</p><hr><p>列表，自然是EXCEL的基本。以下這種列表，用家都看習慣了。</p><figure class="image"><img src="https://assets.matters.news/embed/cf1a58b5-4eb8-4e2f-ace5-acf33c944b4d.png" data-asset-id="cf1a58b5-4eb8-4e2f-ace5-acf33c944b4d" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>但很多客戶都不喜歡列表，卻喜歡以下這種GRID的圖表。</p><figure class="image"><img src="https://assets.matters.news/embed/a947b21f-ba58-407d-ab97-83b8fac9311b.png" data-asset-id="a947b21f-ba58-407d-ab97-83b8fac9311b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>如果只是做一次，列表的內容又不怎麼改變，其實就是很簡單的COPY&PASTE。但當你經常要改動這個圖表，又或是有幾百、幾千個ENTRIES的話，就不太可能粘貼了。本大師就是要做一個這樣的圖表，將幾千個ENTRIES換成這樣有一百多個COLUMNS的表，每一個ROW的項目數也不一樣。</p><figure class="image"><img src="https://assets.matters.news/embed/a87aa865-d5b2-4f8f-a2f7-9e07ad9d0c0c.png" data-asset-id="a87aa865-d5b2-4f8f-a2f7-9e07ad9d0c0c" referrerpolicy="no-referrer"><figcaption><span>本大師昨夜的成品</span></figcaption></figure><p>手動COPY&PASTE自然不是一件容易的事，而且也不划算；別說本大師日理萬機，游手好閒的也情願把時間花在滑手機吧。</p><p>所以，動動腦筋，看看GOOGLE，就可以輕鬆做到了。</p><figure class="image"><img src="https://assets.matters.news/embed/0d089cde-a591-4a49-8e85-e04cd74be76b.gif" data-asset-id="0d089cde-a591-4a49-8e85-e04cd74be76b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>其實，要做到這樣的功能，只需要很簡單的公式。</p><pre class="ql-syntax">=TEXTJOIN(CHAR(10),TRUE,IF(($B$1:$B$16=C$18)*($C$1:$C$16=$A19),$A$1:$A$16,”"))
</pre><p>TEXTJOIN 是一個比較新的公式，需要使用2016或以上版本的EXCEL。</p><figure class="image"><img src="https://assets.matters.news/embed/432f2505-f7a6-4b46-987c-6ec4addaff17.png" data-asset-id="432f2505-f7a6-4b46-987c-6ec4addaff17" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>藍色的表格裡，團隊是COLUMN，等級是ROW，而每一個格子裡是附合該格子相對應團隊和等級的名字。每個名字顯示為分行。</p><p>上面的公式，是要以ARRAY FORMULA的方式寫進格子裡（在最左上的格子裡寫一次，CTRL-SHIFT-ENTER，再拉滿所有格子就可以了。</p><p>先來拆解我怎麼使用<a href="https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c" target="_blank">TEXTJOIN</a>的公式。</p><pre class="ql-syntax">TEXTJOIN(delimiter, ignore_empty, text1, [text2], …)
</pre><p>這個公式的目的就是把從不同的地方取得的文字加在一起作顯示。我的例子裡就是把列表中不同的稱號放在格子裡。</p><ul><li>Delimiter的部分是讓公式知道怎麼把不同的文字加在一起。我想要名字都分行顯示，所以我使用了char(10) 這個來加入一個LINE BREAK</li><li>ignore_empty的部分是一個TRUE或FALSE的選擇，是告訴公式是否略過空白。我選擇了是，所以是TRUE，略過空白稱號</li><li>text 1, text 2, text 3 …如此類推，就是要被加在一起的文字了。在這裡，我就不是直接把稱號寫進去，而是讓公式到列表裡去搜尋符合我設下條件的稱號</li></ul><p>在這第三個部分，我是寫另一條公式進去。</p><pre class="ql-syntax">IF(($B$1:$B$16=C$18)*($C$1:$C$16=$A19),$A$1:$A$16,””)
</pre><p>這個IF的公式，用家應該不會覺得陌生。</p><pre class="ql-syntax">=IF (logical_test, [value_if_true], [value_if_false])
</pre><p>它基本上就是去看第一個部分的logical_test是對還是錯；如果是對的話，就返回第二節(value if true)，錯的話就返回第三節 (value if false)。</p><pre class="ql-syntax">IF(($B$1:$B$16=C$18)*($C$1:$C$16=$A19),$A$1:$A$16,””)
</pre><p>先說說我的這條公式裡第二和第三節的部分。若前面的logical test 返回是對，就會返回A1到A16，就是稱號；若前面的logical test返回是錯，就什麼都不返回(“”)。</p><p>我的logical test是什麼呢？就是看列表裡的團隊COLUMN是否符合藍色表格裡的格子所在的COLUMN，和等級是否符合藍色表格裡的格子所在的ROW。由於我這條公式會用在不同的格子裡，相對應的column和 row 都會改變，所以在設定時就得加上$符號來顯示相對應的。</p><p>這個LOGICAL TEST其實有機會返回多過一個的ENTRY，例如一級聖人裡就不止一個名字了。所以，我們需要這個IF公式去作多次的選取，也就因此而用上array formula了。（這個我不多講，自己GOOGLE去吧！）</p><p>看，是不是很簡單？</p>  
</div>
            