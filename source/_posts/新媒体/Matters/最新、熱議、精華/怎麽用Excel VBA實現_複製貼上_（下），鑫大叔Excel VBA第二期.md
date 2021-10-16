
---
title: '怎麽用Excel VBA實現_複製貼上_（下），鑫大叔Excel VBA第二期'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/66a8db70-f8c0-4310-8165-3eaf9167768e.png'
author: Matters
comments: false
date: Sat, 16 Oct 2021 04:59:32 GMT
thumbnail: 'https://assets.matters.news/embed/66a8db70-f8c0-4310-8165-3eaf9167768e.png'
---

<div>   
<h2>🔷<strong> 介紹 </strong>🔷</h2><p>沒看上一期的可能不清楚VBA是什麽，簡單來説是一種主要用於Microsoft Office的編程語言，適合沒學過編程的人用（因爲容易）。這裏主要討論Excel用的VBA。更多介紹請去看<a href="https://matters.news/@baoshin/%E6%80%8E%E9%BA%BD%E7%94%A8excel-vba%E5%AF%A6%E7%8F%BE-%E8%A4%87%E8%A3%BD%E8%B2%BC%E4%B8%8A-%E4%B8%8A-%E9%91%AB%E5%A4%A7%E5%8F%94excel-vba%E7%AC%AC%E4%B8%80%E6%9C%9F-bafyreifjhrlgrioovvqwuw34fz7g2mpa2yrxetekc2tnggwzryidih7hla" target="_blank">第一期</a>。</p><hr><hr><h2>🔷<strong> VBA循環結構 </strong>🔷</h2><p>循環結構就是用來重複執行同一段代碼，重複次數通過特定條件控制。</p><p>VBA主要有三種循環結構，分別爲For、While和Loop，每種又有幾種小變化，剛開始會一種就夠用了。這次範例用While ... Wend。</p><p>範例代碼如下：</p><pre class="ql-syntax">Sub Macro2()
    r = 0
    c = 2
    
    While r < 100
        r = r + 1
    
        Sheets("B").Cells(r, c) = r
        Sheets("C").Cells(r, c + 1) = Sheets("B").Cells(r, c)
    Wend
End Sub
</pre><hr><hr><h2>🔷<strong> VBA代碼解説（範例1）</strong>🔷</h2><p><strong>❇️ 變數</strong></p><pre class="ql-syntax">    r = 0
    c = 2
</pre><ul><li>這裏“r”和“c“是變數，我們這裏定義他們一個等於數字0，一個等於數字2</li><li><strong>變數（Variable）</strong>：程式在處理資料的時候常常會用到變數，主要用來暫存資料，變數代表的數據會經常變動，故名“變數”。</li><li><strong>變數命名規則：</strong>第一個字必須是英文字母或中文字，之後可以隨意使用中文、英文、數字、或底線符號（“_”），簡單來說就是，如果跑程式出錯，改就是了。</li></ul><p><strong>❇️ While ... Wend</strong></p><pre class="ql-syntax">    While r < 100
    Wend
</pre><ul><li>上面提到的While ... Wend用法之一，”r < 100“就是它的循環條件。用人話來説就是只要r小於100，這個宏就會一直重複的從While跑到Wend，當然也會執行在它們之間的代碼，直到你受不了强制關掉爲止。</li></ul><p><strong>❇️ 算數運算子中的加法</strong></p><pre class="ql-syntax">r = r + 1
</pre><ul><li>不知道你還記得小時候學的加減乘除嗎？啥，你忘記了？慢走不送！！！別打我，開個玩笑而已…… 我們前面定義r=0，所以r+1就是1，下一次再加1就是2。</li><li>好吧，那這行有啥用處呢？還記得上面提到的While ...... Wend嗎？只要r小於100就會一直循環，所以爲了不讓他循環天荒地老，我們每循環一次就給r加1，這樣循環99次r就會等於100，循環就會因爲不符合條件停止。</li><li><strong>算數運算子（Operator）</strong>都有哪些：加法（+）、減法（-）、乘法（*）、除法（/）、整數除法（\）、餘數（Mod）、次方（^）。後續會講解有用到的部分。</li></ul><p><strong>❇️ 工作表、存儲格的應用</strong></p><pre class="ql-syntax">        Sheets("B").Cells(r, c) = r
        Sheets("C").Cells(r, c + 1) = Sheets("B").Cells(r, c)
</pre><ul><li>這兩行是在上一期的的基礎上修改，差別只在於r和c。所以在開始While ... Wend之前，r是1，c是2。</li><li>因為這兩行是放在While ... Wend之間，所以變數r因為前一行的r=r+1一直改變，因此第1行“<strong>Sheets("B").Cells(r, c) = r</strong>”代表：工作表B的C列從第1行到99行，每行都會填上與行數相對應的數字。</li><li>第2行“<strong>Sheets("C").Cells(r, c + 1) = Sheets("B").Cells(r, c)</strong>”代表：工作表C會複製工作表B的內容，只不過工作表B在B列的內容會被複製到工作表C的C列。</li><li>可能有點混亂，但只要實際跑一遍就會理解了</li></ul><h2>🔷<strong> 本期範例下載 </strong>🔷</h2><p><a href="https://drive.google.com/file/d/1xaU6MYzP5MhIOTA-9otc_tSwJRI6w5No/view?usp=sharing" target="_blank">點我下載</a>，檔案打開後注意下是不是有下圖的警告，這是要使用者確認這個巨集是否可信，以免執行了有問題的巨集。點擊“<strong>啟用內容”</strong>就可以正常使用了。</p><figure class="image"><img src="https://assets.matters.news/embed/66a8db70-f8c0-4310-8165-3eaf9167768e.png" data-asset-id="66a8db70-f8c0-4310-8165-3eaf9167768e" referrerpolicy="no-referrer"><figcaption><span>初始Excel安全設定會自動關閉巨集，所以需要點擊“啟用內容”解鎖</span></figcaption></figure><hr><hr><h2>🔷<strong> 在功能區加入開發人員標籤 </strong>🔷</h2><p>這個標籤不是必須，但是有了方便很多。例如可以錄製巨集，也不用一定要用快捷鍵（alt + F11）開啟VB編輯器了。</p><p><strong>❇️ 整個開啟流程：</strong></p><ul><li><strong>檔案</strong> >> <strong>其他</strong>... >> <strong>選項</strong> >> <strong>自訂功能區</strong> >> 勾選 <strong>開發人員</strong></li></ul><p><strong>❇️ 第一步，</strong>看看你的Excel是不是已經有“<strong>開發人員</strong>”標籤了，有可以跳過這個小單元，沒有就點“<strong>檔案</strong>”。</p><figure class="image"><img src="https://assets.matters.news/embed/07fe8bf9-d18d-4507-8453-015069a4bfb2.png" data-asset-id="07fe8bf9-d18d-4507-8453-015069a4bfb2" referrerpolicy="no-referrer"><figcaption><span>看看你的Excel是不是已經有“開發人員”標籤了，沒有就點“檔案”</span></figcaption></figure><p><strong>❇️ 第二步，</strong>點擊“<strong>其他</strong>” >> “<strong>選項</strong>”，開啟Excel選項。</p><figure class="image"><img src="https://assets.matters.news/embed/9d82999b-5929-4256-b938-26b728f9528f.png" data-asset-id="9d82999b-5929-4256-b938-26b728f9528f" referrerpolicy="no-referrer"><figcaption><span>開啟Excel選項</span></figcaption></figure><p><strong>❇️ 第三步，</strong>點擊“<strong>自訂功能區</strong>”，勾選”<strong>開發人員</strong>“，再點“<strong>確定</strong>”，大功告成。</p><figure class="image"><img src="https://assets.matters.news/embed/b9e77dab-7489-4b91-88e7-9ff4871f8ad3.png" data-asset-id="b9e77dab-7489-4b91-88e7-9ff4871f8ad3" referrerpolicy="no-referrer"><figcaption><span>Excel選項</span></figcaption></figure><hr><hr><h2>🔷<strong> 開發人員標籤下有哪些常用的功能？</strong>🔷</h2><figure class="image"><img src="https://assets.matters.news/embed/db77248e-7768-4eaa-81d6-259d9bd0ec4c.png" data-asset-id="db77248e-7768-4eaa-81d6-259d9bd0ec4c" referrerpolicy="no-referrer"><figcaption><span>大叔認為比較常用的功能（開發人員標籤）</span></figcaption></figure><ul><li><strong>Visual Basic：</strong>開啟VB編輯器，和快速鍵（Alt + F11）一樣效果</li><li><strong>巨集：</strong>叫出巨集對話框，做進一步的設定，後續會繼續介紹這個功能。</li><li><strong>錄製巨集：</strong>編程好幫手，用它錄出來的程式碼不好用，卻是極好的範本，修改一下就能直接套用到你的巨集裡。個人覺得這個功能在學習VBA初期，除了讓你覺得好玩，用處不大，所以等後續才解說如何使用和如何修改錄製出來的程式碼。</li><li><strong>巨集安全性：</strong>上期提到每次打開帶有巨集的檔案都會有如下圖的警告，這是因為Excel初始安全設定，如果不想要每次都要多點一下“啟用內容”，就需要在這裡修改安全性。</li></ul><figure class="image"><img src="https://assets.matters.news/embed/4db687f7-e14c-48be-935a-37e880270364.png" data-asset-id="4db687f7-e14c-48be-935a-37e880270364" referrerpolicy="no-referrer"><figcaption><span>初始Excel安全設定會自動關閉巨集</span></figcaption></figure><hr><hr><h2>🔷 <strong>如何讓你不用每次開啟帶有巨集的Excel都要點“啟用內容” </strong>🔷</h2><p><strong>❇️ 第一步，</strong>在“<strong>開發人員</strong>”標籤下點擊“<strong>巨集安全性</strong>”叫出巨集設定對話框。</p><p><strong>❇️ 第二步，</strong>選擇“<strong>啟用所有巨集</strong>”，並點擊“<strong>確定</strong>”。</p><figure class="image"><img src="https://assets.matters.news/embed/76b4a6c7-b7a4-4034-af37-b4b2a0997594.png" data-asset-id="76b4a6c7-b7a4-4034-af37-b4b2a0997594" referrerpolicy="no-referrer"><figcaption><span>如何設定成默認自動啟動所有巨集</span></figcaption></figure><hr><hr><h2>🔷 下期預告 🔷</h2><ul><li>目前有人要求資料庫中提取數據，待我進一步了解需求再來準備~</li></ul><hr><hr><p><br></p><p><br></p><p><a href="https://matters.news/@baoshin/%E6%80%8E%E9%BA%BD%E7%94%A8excel-vba%E5%AF%A6%E7%8F%BE-%E8%A4%87%E8%A3%BD%E8%B2%BC%E4%B8%8A-%E4%B8%8B-%E9%91%AB%E5%A4%A7%E5%8F%94excel-vba%E7%AC%AC%E4%BA%8C%E6%9C%9F-bafyreigcdb7cjvwnrprrejasflv4trhwnllumna5amqstbwv2y33rlg7py#aaa" target="_blank">小測試，請無視我</a></p>  
</div>
            