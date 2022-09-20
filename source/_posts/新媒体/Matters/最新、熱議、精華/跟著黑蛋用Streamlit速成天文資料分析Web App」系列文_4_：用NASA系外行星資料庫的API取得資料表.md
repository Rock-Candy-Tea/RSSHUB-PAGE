
---
title: '跟著黑蛋用Streamlit速成天文資料分析Web App」系列文_4_：用NASA系外行星資料庫的API取得資料表'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/790ef1eb-a672-4516-94b2-342dbec8638e.png'
author: Matters
comments: false
date: Mon, 19 Sep 2022 23:39:27 GMT
thumbnail: 'https://assets.matters.news/embed/790ef1eb-a672-4516-94b2-342dbec8638e.png'
---

<div>   
<p>會議中，PM貳婰舞跟黑蛋說：「客戶對於我們之前透過NASA系外行星資料庫網站手動匯出的CSV檔，表示有太多不必要的欄位，希望聚焦幾個欄位且名稱要以中文呈現，他要求的欄位有『行星名稱』、『所屬恆星名稱』、『與地球的距離』、『行星軌道週期』、『行星質量』、『行星半徑』、『發現年份』、『發現方法』。」</p><p>黑蛋回說：「看來需要先過濾處理資料表，我會再研究看看是否有相關API可以取得資料，這樣就能以Python程式自動化產出整理過後的報表，若未來資料庫有新增行星資料，也不用透過網站手動下載，排程定期產出CSV檔即可。」</p><p>結束視訊會議後，他憶起之前在NASA系外行星資料庫網站首頁左下方有看到新舊版API的說明頁面入口：</p><figure class="image"><img src="https://assets.matters.news/embed/790ef1eb-a672-4516-94b2-342dbec8638e.png" data-asset-id="790ef1eb-a672-4516-94b2-342dbec8638e" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>新版API是基於<a href="https://www.ivoa.net/documents/TAP/" rel="noopener noreferrer" target="_blank">Table Access Protocol(TAP)</a>標準，其<a href="https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html" rel="noopener noreferrer" target="_blank">說明頁面</a>除了描述API的使用方法，也說明各資料表欄位所代表的意義。這個API是使用<a href="https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html" rel="noopener noreferrer" target="_blank">Astronomical Data Query Language(ADQL)</a>語法來查詢資料表並過濾欄位，該語法是基於SQL。</p><p>應客戶需求，黑蛋在API網址中用ADQL的select…from語法，查詢能一行綜觀同個行星所有欄位值的資料表「Planetary Systems Composite Parameters」，並選取所需欄位。他還發現在API中加入format=csv參數，就能在Python script中用Pandas的read_csv()函式，直接將API回傳的資料表讀進DataFrame中，以便將欄位名稱改成中文。最後，他用以下Python script自動匯出客戶此次要求的CSV檔。</p><figure class="image"><img src="https://assets.matters.news/embed/d189f38f-92b2-41ca-8315-b2e3066bdd7c.png" data-asset-id="d189f38f-92b2-41ca-8315-b2e3066bdd7c" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><blockquote>此系列文由<a href="https://astrobackhacker.tw/" rel="noopener noreferrer" target="_blank">蘇羿豪</a>撰寫，以「<a href="https://creativecommons.org/licenses/by/4.0/deed.zh_TW" rel="noopener noreferrer" target="_blank">創用CC 姓名標示 4.0(CC BY 4.0)國際版授權條款</a>」釋出。</blockquote><p><br></p>  
</div>
            