
---
title: '【小程序】Google Sheets _ 管理你的加密貨幣錢包餘額'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/7a7bcca9-c236-463b-9226-0c4f3b8dd717.png'
author: Matters
comments: false
date: Sat, 29 Jan 2022 00:08:28 GMT
thumbnail: 'https://assets.matters.news/embed/7a7bcca9-c236-463b-9226-0c4f3b8dd717.png'
---

<div>   
<p>半吊子業餘程序猿又來老王賣瓜了！！！</p><p>上次用Python抓LikeCoin錢包餘額的文章看留言感覺還是有點難度，使用率感覺應該是很低很低……所以這禮拜決定改用Google Sheet！！！</p><p>雖然後臺還是有代碼，但是這回不用你複製貼上，直接用我提供的範本就行，你需要做的只有：另存範本、加入你的錢包地址、還有按照下面提供的步驟設定自動跑時間就好。希望這篇文章不會是另一篇“<strong>好像很厲害，但是我看不懂</strong>”的技術文。</p><h2>🛑 <strong>警告：因爲帶脚本的谷歌Sheets會存在你的谷歌雲端硬盤，所以如果決定使用，還請各位最好能存在沒有個人資料的谷歌賬號，<u>不然就只能自行確認程序碼，或者相信大叔的人品了</u>。</strong></h2><p>程序碼會貼在文後，以供參考。</p><h2>🟨 <strong>作品介紹</strong></h2><p>這是一個用Google Sheets做的錢包餘額總匯，可以幫你監視你不同錢包裏的三項餘額（可用、委托、委托收益等），還會按照更新時最新的匯率，提供相對應的美金金額以供參考，當前版本只限已上架Osmosis的幣幣。</p><p>第一次使用需要用電腦設定自動跑脚本的時間段，之後便可隨意在手機或電腦上查看。</p><p>作品點擊<a href="https://docs.google.com/spreadsheets/d/1EKO1DuCVkUEDjcYoWg1GgmcMW871TOaUPN4UwevNoZk/edit?usp=sharing" rel="noopener noreferrer" target="_blank">這裏</a>開啓。</p><h2>🟨 <strong>適用人群</strong></h2><ul><li>手機版Kepler錢包沒有支持你所持有的幣（如LikeCoin）</li><li>委托了好幾種幣，想要經常確認有多少收益可以再拿來委托</li><li>持有錢包數量 > 1</li></ul><p>備注：如果你有好幾種幣，但是只有一個Kepler錢包，也可以考慮用<a href="https://ping.pub/" rel="noopener noreferrer" target="_blank">Ping Wallet</a>管理，詳情請看Daisy的<a href="https://matters.news/@daisy/%E4%B8%80%E5%80%8B-ping-pub-%E7%9B%A1%E6%83%85%E7%AE%A1%E7%90%86-like-huahua-osmo-atom-bafyreih6272qbamc2245kwkzhylpsb4asdevdfheg6jup2wovartyt5fcu" rel="noopener noreferrer" target="_blank">文章</a>。</p><figure class="image"><img src="https://assets.matters.news/embed/7a7bcca9-c236-463b-9226-0c4f3b8dd717.png" data-asset-id="7a7bcca9-c236-463b-9226-0c4f3b8dd717" referrerpolicy="no-referrer"><figcaption><span>綠色欄位是小程序會提供的資料</span></figcaption></figure><hr><hr><h2>🟨 <strong>使用説明：第一次設定</strong></h2><p>❶ 點擊<a href="https://docs.google.com/spreadsheets/d/1EKO1DuCVkUEDjcYoWg1GgmcMW871TOaUPN4UwevNoZk/edit?usp=sharing" rel="noopener noreferrer" target="_blank">這裏</a>打開文件，點擊“<strong>檔案</strong>” >> “<strong>建立副本</strong>”，開啓複製選項<strong>。</strong></p><figure class="image"><img src="https://assets.matters.news/embed/8724aa22-0fa1-4fa4-ae0f-291d750c93d1.png" data-asset-id="8724aa22-0fa1-4fa4-ae0f-291d750c93d1" referrerpolicy="no-referrer"><figcaption><span>打開複製選項</span></figcaption></figure><hr><hr><p>❷ 把文件名稱換成自己喜歡的名字，然後選擇文件夾再點擊“確認”。如果嫌麻煩直接點“確定”也是可以。</p><figure class="image"><img src="https://assets.matters.news/embed/2d2141e9-6cf9-4364-8345-78c34b1654ff.png" data-asset-id="2d2141e9-6cf9-4364-8345-78c34b1654ff" referrerpolicy="no-referrer"><figcaption><span>把範本存到自己的谷歌硬盤，不然無法修改</span></figcaption></figure><hr><hr><p>❸ 開始更新複製的檔案。第一行有三種顔色，請參考下圖説明。需要用戶輸入的只有藍色欄位，畢竟我可不知道你的錢包地址、錢包名和要看的貨幣（笑）。</p><p>一行肯定不夠用，要新增只要複製第二行貼到第三行再重複第三步即可。</p><figure class="image"><img src="https://assets.matters.news/embed/8bdc5c9e-b757-4ec9-984f-f919701085b8.png" data-asset-id="8bdc5c9e-b757-4ec9-984f-f919701085b8" referrerpolicy="no-referrer"><figcaption><span>除了藍色欄位，其他請不要更動，以免小程序失靈</span></figcaption></figure><figure class="image"><img src="https://assets.matters.news/embed/5f81dc6f-5f61-4a5c-8c70-d7e4c54593ce.png" data-asset-id="5f81dc6f-5f61-4a5c-8c70-d7e4c54593ce" referrerpolicy="no-referrer"><figcaption><span>欄位分類説明</span></figcaption></figure><hr><hr><p>❹ 資料更新完畢就讓我們來手動啓動脚本測試看看吧。點擊“API”工作簿，點擊“手動刷新”按鈕。</p><p>這步是爲了確認巨集可以正常運行。</p><figure class="image"><img src="https://assets.matters.news/embed/5c3caf42-b555-44d3-be33-8b7442a5ac3d.png" data-asset-id="5c3caf42-b555-44d3-be33-8b7442a5ac3d" referrerpolicy="no-referrer"><figcaption><span>點擊手動刷新測試巨集是否可以正常運行</span></figcaption></figure><hr><hr><p>❺ 第一次跑需要授權該脚本，點擊“繼續”，以後就不用授權了。</p><figure class="image"><img src="https://assets.matters.news/embed/384a5b5e-9151-41f1-b8de-623a5185412d.png" data-asset-id="384a5b5e-9151-41f1-b8de-623a5185412d" referrerpolicy="no-referrer"><figcaption><span>授權許可</span></figcaption></figure><hr><hr><p>❻ 還會有如下圖般的警告！所以<strong>再次申明，爲了安全起見，大家用的時候最好用沒有個人資料的谷歌賬號（這樣你就完全不用擔心本人的程式碼暗藏會偷你個人資料的機關）</strong>。如果決定使用就先點擊“高級”再點擊“轉至Get_Info（不安全）”。這個也是只有第一次會出現，後面就不需要再確認了。<strong>話説如果有人知道怎麽讓谷歌驗證，歡迎留言告知。</strong></p><figure class="image"><img src="https://assets.matters.news/embed/b4420020-5554-4fd7-8181-865de4704091.png" data-asset-id="b4420020-5554-4fd7-8181-865de4704091" referrerpolicy="no-referrer"><figcaption><span>自己寫的巨集被這樣懷疑還真是心情很複雜</span></figcaption></figure><hr><hr><p>❼ 確認後，就會看到開始跑和跑完的提示。</p><figure class="image"><img src="https://assets.matters.news/embed/f08eb10c-34d0-4db9-b53d-7bf6a89c8674.png" data-asset-id="f08eb10c-34d0-4db9-b53d-7bf6a89c8674" referrerpolicy="no-referrer"><figcaption><span>巨集運行過程和完成的提示</span></figcaption></figure><hr><hr><p>❽ 倒回去工作頁“錢包結餘”看，資料已經更新完畢。巨集更新的時候也會記錄時間，所以一看就知道是什麽時候更新的。這一欄在設定好自動跑後會特別重要，因爲一看就知道它有沒有乖乖工作。</p><figure class="image"><img src="https://assets.matters.news/embed/3f993dcb-cce0-4135-8c47-74ff171c909b.png" data-asset-id="3f993dcb-cce0-4135-8c47-74ff171c909b" referrerpolicy="no-referrer"><figcaption><span>巨集更新的時候也會記錄時間，所以一看就知道是什麽時候更新的</span></figcaption></figure><hr><hr><h2>🟨 <strong>使用説明：定時自動更新</strong></h2><p>講了這麽多麻煩的設定，終於要到最棒的地方了！按鈕跑巨集要等它跑完，但是設定讓它定時自動跑，你打開看就不用等了。</p><p>❶ <strong>點擊“擴充功能” >> “Apps Script”</strong></p><figure class="image"><img src="https://assets.matters.news/embed/08796514-6895-415c-8bcc-54cafc6988d3.png" data-asset-id="08796514-6895-415c-8bcc-54cafc6988d3" referrerpolicy="no-referrer"><figcaption><span>開啓Apps Script可以看到程序碼和設定自動跑的條件</span></figcaption></figure><hr><hr><p>❷ 在彈出的視窗點擊鬧鐘圖形的“<strong>觸發條件</strong>”。</p><figure class="image"><img src="https://assets.matters.news/embed/0f043142-8bef-477d-a4f0-dbb6f5c96814.png" data-asset-id="0f043142-8bef-477d-a4f0-dbb6f5c96814" referrerpolicy="no-referrer"><figcaption><span>鬧鐘圖形 = 觸發條件設定</span></figcaption></figure><hr><hr><p>❸ 點擊“<strong>新增觸發條件</strong>”，開始設定觸發條件。</p><figure class="image"><img src="https://assets.matters.news/embed/951e87e9-c63d-46c7-81f3-bf394c61385c.png" data-asset-id="951e87e9-c63d-46c7-81f3-bf394c61385c" referrerpolicy="no-referrer"><figcaption><span>點擊“新增觸發條件”，開始設定觸發條件</span></figcaption></figure><hr><hr><p>❹ 按照下圖設定一天更新4次，如果想要跑更多次可以在選項”<strong>選取時間型觸發條件類型</strong>”和“<strong>選取小時間隔</strong>”修改。最快可以一分鐘跑一次。</p><p>設定完別忘記點擊”<strong>儲存</strong>“。</p><figure class="image"><img src="https://assets.matters.news/embed/224400fb-6b19-4cf7-a350-59b827b933a8.png" data-asset-id="224400fb-6b19-4cf7-a350-59b827b933a8" referrerpolicy="no-referrer"><figcaption><span>觸發條件設定，設定完別忘記點擊”儲存“</span></figcaption></figure><hr><hr><p>❺ 看到如下圖般多了一行觸發條件就是完成了。</p><figure class="image"><img src="https://assets.matters.news/embed/95b829ab-6524-4c7e-8356-3927be039934.png" data-asset-id="95b829ab-6524-4c7e-8356-3927be039934" referrerpolicy="no-referrer"><figcaption><span>觸發條件設定完成</span></figcaption></figure><hr><hr><h2>🟨 <strong>補充説明</strong></h2><p>雖然號稱可以查看所有COSMOS鏈上有的幣，但是要先加上相對應的API。工作頁“<strong>API</strong>”目前只記錄了下面這些幣，其他幣可以去<a href="https://ping.pub/" rel="noopener noreferrer" target="_blank">Ping Wallet</a>找相對應的API加上，如果嫌麻煩也可以支持本文5港幣，並留言想要加的API（一次最多5種，因爲我怕你叫我全部加到完……）。</p><figure class="image"><img src="https://assets.matters.news/embed/6441add3-0d33-4389-8a65-1d342a412841.png" data-asset-id="6441add3-0d33-4389-8a65-1d342a412841" referrerpolicy="no-referrer"><figcaption><span>現在範本只支持這些幣，因爲大叔只添加了這幾個幣的API……</span></figcaption></figure><hr><hr><h2>🟨 <strong>你也許錯過的文章</strong></h2><p>簡單來説就是為舊文打廣告？</p><p><strong>小工具</strong></p><ul><li><a href="https://matters.news/@baoshin/q-python%E7%B3%BB%E5%88%97-%E6%89%8B%E6%A9%9F%E6%9F%A5%E7%9C%8Blike-coin%E9%8C%A2%E5%8C%85%E9%A4%98%E9%A1%8D-bafyreibho7gzah4hufgbgbai6qnz4vbcdzxc525xyhlcmepw7q7clnkedu" rel="noopener noreferrer" target="_blank">QPython系列：手機查看LikeCoin錢包餘額</a></li><li><a href="https://matters.news/@baoshin/%E5%B0%8F%E7%A8%8B%E5%BA%8F-%E6%AA%A2%E9%96%B2%E4%BD%A0%E8%A8%82%E9%96%B2%E7%9A%84%E5%9C%8D%E7%88%90%E6%9C%80%E6%96%B0%E5%8B%95%E6%85%8B-bafyreielvqf7iso62iavbkzibycd6frozvlq4l36o3zm6pfx4qlyptxafa" rel="noopener noreferrer" target="_blank">【小程序】檢閲你訂閲的圍爐最新動態</a></li><li><a href="https://matters.news/@baoshin/%E8%BE%A6%E6%B4%BB%E5%8B%95%E7%9A%84%E5%A5%BD%E5%A4%A5%E4%BC%B4-%E6%8C%87%E5%AE%9A%E6%A8%99%E7%B0%BD%E6%96%87%E7%AB%A0%E5%88%97%E8%A1%A8%E7%94%9F%E6%88%90%E5%99%A8-bafyreicljv2gft6eamxrex7yxcjhaskbav3zeiye6dmlb6372l7rjjkuby" rel="noopener noreferrer" target="_blank">辦活動的好夥伴，指定標簽文章列表生成器</a></li><li><a href="https://matters.news/@baoshin/%E4%BD%BF%E7%94%A8%E5%BF%83%E5%BE%97-%E6%AF%94matters%E8%8D%89%E7%A8%BF%E6%9B%B4%E5%AE%B9%E6%98%93%E7%94%A8-%E5%8F%88%E4%B8%8D%E6%9C%83%E8%A2%AB%E5%90%83%E6%8E%89%E7%9A%84%E8%B0%B7%E6%AD%8C%E6%96%87%E4%BB%B6%E6%80%8E%E9%BA%BD%E7%94%A8-bafyreian2kis75lvvvczu627it35bsdxvzsray42xihyh57mltmyoqafrq" rel="noopener noreferrer" target="_blank">【使用心得】比Matters草稿更容易用，又不會被吃掉的谷歌文件怎麽用？</a></li></ul><p><strong>Excel VBA</strong></p><ul><li><a href="https://matters.news/@baoshin/%E6%80%8E%E9%BA%BD%E7%94%A8excel-vba%E5%AF%A6%E7%8F%BE-%E8%A4%87%E8%A3%BD%E8%B2%BC%E4%B8%8A-%E4%B8%8A-%E9%91%AB%E5%A4%A7%E5%8F%94excel-vba%E7%AC%AC%E4%B8%80%E6%9C%9F-bafyreifjhrlgrioovvqwuw34fz7g2mpa2yrxetekc2tnggwzryidih7hla" rel="noopener noreferrer" target="_blank">怎麽用Excel VBA實現”複製貼上“（上），鑫大叔Excel VBA第一期</a></li><li><a href="https://matters.news/@baoshin/%E6%80%8E%E9%BA%BD%E7%94%A8excel-vba%E5%AF%A6%E7%8F%BE-%E8%A4%87%E8%A3%BD%E8%B2%BC%E4%B8%8A-%E4%B8%8B-%E9%91%AB%E5%A4%A7%E5%8F%94excel-vba%E7%AC%AC%E4%BA%8C%E6%9C%9F-bafyreigcdb7cjvwnrprrejasflv4trhwnllumna5amqstbwv2y33rlg7py" rel="noopener noreferrer" target="_blank">怎麽用Excel VBA實現”複製貼上“（下），鑫大叔Excel VBA第二期</a></li></ul><p><strong>Excel小技巧</strong></p><ul><li><a href="https://matters.news/@baoshin/%E5%9C%A8excel%E6%8A%8A%E6%99%82%E9%96%93%E8%BD%89%E6%8F%9B%E6%88%90%E5%80%BC%E7%8F%AD%E6%97%A5-bafyreicy2l5673j7uvxtcdhhrsbhjmrwqwry7uyjyn4jzxb3q7yrwrjljy" rel="noopener noreferrer" target="_blank">在Excel把時間轉換成值班日</a></li><li><a href="https://matters.news/@baoshin/%E9%91%AB%E5%A4%A7%E5%8F%94excel%E5%B0%8F%E6%8A%80%E5%B7%A7-vlookup%E7%9A%84%E6%A2%9D%E4%BB%B6%E5%A4%9A%E6%96%BC%E4%B8%80%E5%80%8B%E6%80%8E%E9%BA%BD%E8%BE%A6-bafyreifug3spycfpmu6iaojthxzlqsqrjaxmot4puao6wrniu6xa4gd3q4" rel="noopener noreferrer" target="_blank">鑫大叔Excel小技巧 | Vlookup的條件多於一個怎麽辦？</a></li><li><a href="https://matters.news/@baoshin/%E6%99%9A%E4%B8%8A%E5%8D%81%E4%B8%80%E9%BB%9E%E6%94%B6%E5%88%B0%E9%97%9C%E6%96%BCexcel%E7%9A%84%E6%B1%82%E6%95%91%E9%9B%BB%E8%A9%B1-bafyreigy53sudsg2aleh23xwudenggp676nh5ao33odnzwcqap6dfon7f4" rel="noopener noreferrer" target="_blank">晚上十一點收到關於Excel的求救電話</a></li></ul><h2>🟨 <strong>程式碼</strong></h2><p><strong>巨集.gs</strong></p><pre class="ql-syntax" spellcheck="false">function AutoRunInfo() &#123;
  var ss = SpreadsheetApp.getActiveSpreadsheet();  
  var sht00 = ss.getSheetByName("錢包結餘");

  tR0 = sht00.getLastRow()
  //SpreadsheetApp.getUi().alert('Confirmation received.');

  UnitCol = 8

  for (var sR0 = 2; sR0 <= tR0; sR0++) &#123;
    aToken = sht00.getRange(sR0,1).getValue().toLowerCase();
    if (sht00.getRange(sR0,1).getValue() !="")&#123;
      //質押
      aURL = sht00.getRange(sR0,UnitCol+1).getValue();      
      try&#123;
        aValue = GetTokenAvailable(aURL,aToken)/sht00.getRange(sR0,UnitCol+0).getValue();      
      &#125; catch (e) &#123;
        aValue = "Error"
      &#125;      
      sht00.getRange(sR0,3).setValue(aValue);

      //委托
      sURL = sht00.getRange(sR0,UnitCol+3).getValue();      
      try&#123;
        sValue = GetTokenStake(sURL)/sht00.getRange(sR0,UnitCol+0).getValue();      
      &#125; catch (e) &#123;
        sValue = "Error"
      &#125;      
      sht00.getRange(sR0,5).setValue(sValue);

      //獎勵，沒有委托 = 沒有獎勵，所以要先確認是不是有委托
      if(sValue != 0)&#123;
        rURL = sht00.getRange(sR0,UnitCol+2).getValue();
        try&#123;
          rValue = GetTokenReward(rURL)/sht00.getRange(sR0,UnitCol+0).getValue();      
        &#125; catch (e) &#123;
          rValue = "Error"
        &#125;
      &#125; else &#123;
        rValue = 0
      &#125;
      sht00.getRange(sR0,4).setValue(rValue); 

      totalQty = 0
      if (aValue != "Error")&#123;
        totalQty = totalQty + aValue;
      &#125;

      if (rValue != "Error")&#123;
        totalQty = totalQty + rValue;
      &#125;

      if (sValue != "Error")&#123;
        totalQty = totalQty + sValue;
      &#125;

      try&#123;
        //totalValue = GetPrice("https://api-osmosis.imperator.co/tokens/v1/"+aToken,"price");  
        totalValue = totalQty * GetPrice("https://api-osmosis.imperator.co/tokens/v1/"+aToken,"price");  
      &#125; catch (e) &#123;
        totalValue = "Error"
      &#125;      
      sht00.getRange(sR0,6).setValue(totalValue); 

      sht00.getRange(sR0,UnitCol+4).setValue(new Date()); 
    &#125;
  &#125;
&#125;;
</pre><hr><hr><p><strong>API.gs</strong></p><pre class="ql-syntax" spellcheck="false">function GetPrice(Url,itemKey) &#123;
  var res = UrlFetchApp.fetch(Url);
  var content = res.getContentText();
  var jsonObject = JSON.parse(content);
  return jsonObject[0][itemKey];
&#125;

function GetTokenAvailable(Url,token) &#123;
  var res = UrlFetchApp.fetch(Url);
  var content = res.getContentText();
  var jsonObject = JSON.parse(content);

  var xyz = Number(jsonObject["pagination"]["total"])
  var amt = 0.0

  if (xyz == 0 ) &#123;
    return 0;
  &#125; else if (xyz == 1) &#123;
    return Number(jsonObject["balances"][0]["amount"]);
  &#125; else &#123;
    for (var i = 0; i < xyz; i++) &#123;
      denom = String((jsonObject["balances"][i]["denom"]));
      if (denom.includes(token) == true)&#123;
        amt+= Number(jsonObject["balances"][i]["amount"]);        
      &#125;
    &#125;
    return amt;
  &#125; 
&#125;

function GetTokenStake(Url) &#123;
  try &#123;
    var res = UrlFetchApp.fetch(Url);
  &#125; catch (e) &#123;
    return 0;
  &#125;
  var content = res.getContentText();
  var jsonObject = JSON.parse(content);

  var xyz = Number(jsonObject["pagination"]["total"])
  var amt = 0.0

  if (xyz == 0 ) &#123;
    return 0;
  &#125; else &#123;
    for (var i = 0; i < xyz; i++) &#123;
      amt+= Number(jsonObject["delegation_responses"][i]["delegation"]["shares"]);
    &#125;
  &#125;
  return amt;
&#125;

function GetTokenReward(Url) &#123;
  var res = UrlFetchApp.fetch(Url);
  var content = res.getContentText();
  var jsonObject = JSON.parse(content);
  return Number(jsonObject["total"][0]['amount']);  
&#125;
</pre><hr><hr><p><br></p>  
</div>
            