
---
title: '_Obs＃56_ 快速新增灵感／闪念笔记(Fleeting Note)的 3 种方法'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://picsum.photos/400/300?random=6680'
author: 少数派 sspai
comments: false
date: Sun, 10 Oct 2021 13:22:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=6680'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><p>我們偶爾會有靈光一閃、稍蹤即逝的絕妙想法，這些突發奇想何時會出現無從循跡、無法臆測，靈感來無影去無蹤，我們必須在<strong>最短的時間</strong>、用<strong>最快的方法</strong>將之記錄起來，以下介紹使用Obsidian將靈感快速新增成為筆記的方法。</p><p>第一種方法是立即建立一篇筆記。<br>第二個方法是直接新增到每日筆記，並將之變成待辦事項。<br>第三個方法是使用AutoHotkey在外部直接輸入文字再插入Obsidian對應位置。macOS的使用者請試試AppleScript或Alfred等方法來達成。</p><p>主要使用到的外掛如下：</p><ul><li>Templater</li><li>QuickAdd</li><li>Advanced Obsidian URI （URI: 統一資源標識符）</li></ul><pre class="language-ad-comment"><code>title: 建議
icon: lightbulb
靈感/閃念筆記應該在一天或兩天裡清理掉（整理、合併到永久筆記或刪除），以免又形成另一個資料垃圾場。</code></pre><h2>方法1. 建立靈感筆記</h2><p>使用QuickAdd新增一個Template的Choice，並設定一個快捷鍵。輸入靈感文字後會產生同名的筆記。</p><h3>操作步驟</h3><ol><li>QuickAdd選項→新增Template: Fleeting note的Choice</li><li>指定【Template path】為「模板資料夾/templater-fleeting-note.md」</li><li>勾選【File Name Format】，【File Name】欄位輸入「&#123;&#123;VALUE:靈光一閃&#125;&#125;」</li><li>【Create in folder】指定資料夾為「030-Inbox」</li></ol><h3>templater-fleeting-note.md</h3><pre class="language-js:templater-fleeting-note.md"><code>---
created: [ <% tp.date.now("YYYY-MM-DD HH:mm") %> ]
aliases: [ <% tp.file.title %> ]
tags: [ fleeting, todo ]
---
# <% tp.file.title %>

Modified:: <%+ tp.file.last_modified_date() %>

<% tp.file.title %>

<% await tp.system.clipboard() %></code></pre><p> </p><pre class="language-ad-fail"><code>title: 缺點
生成了一個新檔案，最後需要刪除或搬移等檔案操作</code></pre><h2>方法2. 輸入內容後新增到每日筆記</h2><p>此方法適用有使用Obsidian每日筆記與任務管理的狀況。在彈出視窗輸入內容後直接插入每日筆記指定標題處。</p><h3>操作步驟</h3><ol><li>QuickAdd選項→新增Capture: Fleeting note的Choice</li><li>指定【File Name】欄位為「020-Daily/&#123;&#123;DATE:YYYY-MM-DD_ddd&#125;&#125;」</li><li>勾選【Task】以形成待辦事項格式</li><li>勾選【Insert after】，指定要插入內容到那個段落<ol><li>輸入標題文字</li><li>勾選【Insert at end of section】</li></ol></li><li>變更【Create line if not found】為【Bottom】</li><li>勾選【Capture format】並輸入腳本碼(全形倒引號要改成半形)：</li></ol><pre class="language-js:Capture：Fleeting-note"><code>‘‘‘js quickadd
let text = await this.quickAddApi.utility.getClipboard();
text = await this.quickAddApi.inputPrompt("✍添加靈感筆記", "輸入內容", text);
text = text.replace("\n", "<br>");
</code></pre><p>return text;<br>‘‘‘<br><% tp.file.cursor(1) %></p><pre class="language-"><code>
```ad-warning
title: 缺點
方法1與方法2者都必須在Obsidian裡操作，但有可能靈感來時正好在使用別的應用程式。</code></pre><h2>方法3. 由外部應用直接新增</h2><p>不必在Obsidian裡，直接執行AutoHotkey的彈出式視窗，輸入內容後透過Advanced Obsidian URI將內容插入每日筆記的指定標題處。</p><pre class="language-autohotkey:fleeting-note.ahk"><code>;; fleeting-note.ahk
;; Input any ideas into Obsidian's Daily note.
;; Hotkey: Alt+D
;; Author: emisjerry, http://jdev.tw/blog/
#SingleInstance Force

global valut := "MOC"
global note := "020-Daily/" . A_YYYY . "-" . A_MM . "-" . A_DD . "_" . A_DDD
global heading := "靈光一閃"

!d::
  text = %Clipboard%
  text := MultiLineInputBox("Your ideas: ", text, "Insert your ideas into Daily note")
  if (text != "") &#123;
    text := StrReplace(text, "`n", "<br>")
    text := StrReplace(text, "`r", "")
    text := encodeURI("- [ ] " . text)  ;; encodes and changes to a todo item
    text := StrReplace(text, "`n", "<br>")
    text := StrReplace(text, "`r", "")
    ;;msgbox text=%text%$
    Run obsidian://advanced-uri?vault=%valut%&filepath=%note%&heading=%heading%&data=%text%&mode=append
  &#125;

  return

MultiLineInputBox(Text:="", Default:="", Caption:="Multi Line Input Box")&#123;
  static
  ButtonOK:=ButtonCancel:= false
  if !MultiLineInputBoxGui&#123;
    Gui, MultiLineInputBox: Font, s14, Segoe UI
    Gui, MultiLineInputBox: add, Text, r1 w600  , % Text
    Gui, MultiLineInputBox: add, Edit, r10 w600 vMultiLineInputBox, % Default
    Gui, MultiLineInputBox: add, Button, w100 h50 x380 gMultiLineInputBoxOK , &OK
    Gui, MultiLineInputBox: add, Button, w100 h50 x+10 gMultiLineInputBoxCancel, &Cancel
    MultiLineInputBoxGui := true
  &#125;
  GuiControl,MultiLineInputBox:, MultiLineInputBox, % Default
  Gui, MultiLineInputBox: Show,, % Caption
  SendMessage, 0xB1, 0, -1, Edit1, A
  while !(ButtonOK||ButtonCancel)
    continue
  if ButtonCancel
    return
  Gui, MultiLineInputBox: Submit, NoHide
  Gui, MultiLineInputBox: Cancel
  return MultiLineInputBox
  ;----------------------
  MultiLineInputBoxOK:
  ButtonOK:= true
  return
  ;---------------------- 
  MultiLineInputBoxGuiEscape:
  MultiLineInputBoxCancel:
  ButtonCancel:= true
  Gui, MultiLineInputBox: Cancel
  return
&#125;

encodeURI(Uri, Enc = "UTF-8")
&#123;
  StrPutVar(Uri, Var, Enc)
  f := A_FormatInteger
  SetFormat, IntegerFast, H
  Loop
  &#123;
  Code := NumGet(Var, A_Index - 1, "UChar")
  If (!Code)
    Break
  If (Code >= 0x30 && Code <= 0x39 ; 0-9
    || Code >= 0x41 && Code <= 0x5A ; A-Z
    || Code >= 0x61 && Code <= 0x7A) ; a-z
    Res .= Chr(Code)
  Else
    Res .= "%" . SubStr(Code + 0x100, -1)
  &#125;
  SetFormat, IntegerFast, %f%
  Return, Res
&#125;

decodeURI(Uri, Enc = "UTF-8")
&#123;
  Pos := 1
  Loop
  &#123;
  Pos := RegExMatch(Uri, "i)(?:%[\da-f]&#123;2&#125;)+", Code, Pos++)
  If (Pos = 0)
    Break
  VarSetCapacity(Var, StrLen(Code) // 3, 0)
  StringTrimLeft, Code, Code, 1
  Loop, Parse, Code, `%
    NumPut("0x" . A_LoopField, Var, A_Index - 1, "UChar")
  StringReplace, Uri, Uri, `%%Code%, % StrGet(&Var, Enc), All
  &#125;
  Return, Uri
&#125;

StrPutVar(Str, ByRef Var, Enc = "")
&#123;
  Len := StrPut(Str, Enc) * (Enc = "UTF-16" || Enc = "CP1200" ? 2 : 1)
  VarSetCapacity(Var, Len, 0)
  Return, StrPut(Str, &Var, Enc)
&#125;</code></pre><h2>相關連結</h2><ul><li>temlater-fleeting-note.md: https://gist.github.com/emisjerry/8939f9aa8f4de9eab377b1461cb4f9bd</li><li>fleeting-note.ahk: https://gist.github.com/emisjerry/01ec842be695a5248db642206b96dee7</li></ul><h2>教學影片</h2><iframe class="ss-videoIframe" src="https://www.youtube.com/embed/c69rpaaAyEM"> </iframe><p>＃＃</p></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-7582" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%5BObs%EF%BC%8356%5D%20%E5%BF%AB%E9%80%9F%E6%96%B0%E5%A2%9E%E7%81%B5%E6%84%9F%EF%BC%8F%E9%97%AA%E5%BF%B5%E7%AC%94%E8%AE%B0(Fleeting%20Note)%E7%9A%84%203%20%E7%A7%8D%E6%96%B9%E6%B3%95%E3%80%91%E6%88%91%E4%BB%AC%E5%81%B6%E5%B0%94%E4%BC%9A%E6%9C%89%E7%81%B5%E5%85%89%E4%B8%80%E9%97%AA%E3%80%81%E7%A8%8D%E8%B8%AA%E5%8D%B3%E9%80%9D%E7%9A%84%E7%BB%9D%E5%A6%99%E6%83%B3%E6%B3%95%EF%BC%8C%E8%BF%99%E4%BA%9B%E7%AA%81%E5%8F%91%E5%A5%87%E6%83%B3%E4%BD%95%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0%E6%97%A0%E4%BB%8E%E5%BE%AA%E8%BF%B9%E3%80%81%E6%97%A0%E6%B3%95%E8%87%86%E6%B5%8B%EF%BC%8C%E7%81%B5%E6%84%9F%E6%9D%A5%E6%97%A0%E5%BD%B1%E5%8E%BB%E6%97%A0%E8%B8%AA%EF%BC%8C%E6%88%91%E4%BB%AC%E5%BF%85%E9%A1%BB%E5%9C%A8**%E6%9C%80%E7%9F%AD%E7%9A%84%E6%97%B6%E9%97%B4**%E3%80%81%E7%94%A8**%E6%9C%80%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F10%2F10%2F6974e937119e77fad8b93ec5bce1631c.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-8291" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%5BObs%EF%BC%8356%5D%20%E5%BF%AB%E9%80%9F%E6%96%B0%E5%A2%9E%E7%81%B5%E6%84%9F%EF%BC%8F%E9%97%AA%E5%BF%B5%E7%AC%94%E8%AE%B0(Fleeting%20Note)%E7%9A%84%203%20%E7%A7%8D%E6%96%B9%E6%B3%95%E3%80%91%E6%88%91%E4%BB%AC%E5%81%B6%E5%B0%94%E4%BC%9A%E6%9C%89%E7%81%B5%E5%85%89%E4%B8%80%E9%97%AA%E3%80%81%E7%A8%8D%E8%B8%AA%E5%8D%B3%E9%80%9D%E7%9A%84%E7%BB%9D%E5%A6%99%E6%83%B3%E6%B3%95%EF%BC%8C%E8%BF%99%E4%BA%9B%E7%AA%81%E5%8F%91%E5%A5%87%E6%83%B3%E4%BD%95%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0%E6%97%A0%E4%BB%8E%E5%BE%AA%E8%BF%B9%E3%80%81%E6%97%A0%E6%B3%95%E8%87%86%E6%B5%8B%EF%BC%8C%E7%81%B5%E6%84%9F%E6%9D%A5%E6%97%A0%E5%BD%B1%E5%8E%BB%E6%97%A0%E8%B8%AA%EF%BC%8C%E6%88%91%E4%BB%AC%E5%BF%85%E9%A1%BB%E5%9C%A8**%E6%9C%80%E7%9F%AD%E7%9A%84%E6%97%B6%E9%97%B4**%E3%80%81%E7%94%A8**%E6%9C%80%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            