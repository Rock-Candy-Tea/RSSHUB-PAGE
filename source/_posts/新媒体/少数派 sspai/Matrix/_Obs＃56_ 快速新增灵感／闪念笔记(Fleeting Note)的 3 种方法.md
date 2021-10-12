
---
title: '_Obs＃56_ 快速新增灵感／闪念笔记(Fleeting Note)的 3 种方法'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://picsum.photos/400/300?random=3705'
author: 少数派 sspai
comments: false
date: Sun, 10 Oct 2021 13:22:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=3705'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><p>我们偶尔会有灵光一闪、稍踪即逝的绝妙想法，这些突发奇想何时会出现无从循迹、无法臆测，灵感来无影去无踪，我们必须在最短的时间、用最快的方法将之记录起来，以下介绍使用Obsidian将灵感快速新增成为笔记的方法。</p><ul><li>第一种方法是立即建立一篇笔记。</li><li>第二个方法是直接新增到每日笔记，并将之变成待办事项。</li><li>第三个方法是使用AutoHotkey在外部直接输入文字再插入Obsidian对应位置。macOS的使用者请试试AppleScript或Alfred等方法来达成。</li></ul><p>主要使用到的插件如下：</p><ul><li>Templater</li><li>QuickAdd</li><li>Advanced Obsidian URI （URI: 统一资源标识符）</li></ul><blockquote><p>💡 建议</p><p>灵感/闪念笔记应该在一天或两天里清理掉（整理、合并到永久笔记或删除），以免又形成另一个资料垃圾场。</p></blockquote><h2>方法1. 建立灵感笔记</h2><p>使用QuickAdd新增一个Template的Choice，并设定一个快捷键。输入灵感文字後会产生同名的笔记。</p><h3>操作步骤</h3><ol><li>QuickAdd选项→新增Template: Fleeting note的Choice</li><li>指定【Template path】为「模板资料夹/templater-fleeting-note.md」</li><li>勾选【File Name Format】，【File Name】栏位输入「&#123;&#123;VALUE:灵光一闪&#125;&#125;」</li><li>【Create in folder】指定资料夹为「030-Inbox」</li></ol><p>▼ templater-fleeting-note.md</p><pre class="language-"><code>---
created: [ <% tp.date.now("YYYY-MM-DD HH:mm") %> ]
aliases: [ <% tp.file.title %> ]
tags: [ fleeting, todo ]
---
# <% tp.file.title %>

Modified:: <%+ tp.file.last_modified_date() %>

<% tp.file.title %>

<% await tp.system.clipboard() %></code></pre><p> </p><blockquote><p>⚠️ 缺点</p><p>生成了一个新档案，最後需要删除或搬移等档案操作</p></blockquote><h2>方法2. 输入内容後新增到每日笔记</h2><p>此方法适用有使用Obsidian每日笔记与任务管理的状况。在弹出视窗输入内容後直接插入每日笔记指定标题处。</p><h3>操作步骤</h3><ol><li>QuickAdd选项→新增Capture: Fleeting note的Choice</li><li>指定【File Name】栏位为「020-Daily/&#123;&#123;DATE:YYYY-MM-DD_ddd&#125;&#125;」</li><li>勾选【Task】以形成待办事项格式</li><li>勾选【Insert after】，指定要插入内容到那个段落<ol><li>输入标题文字</li><li>勾选【Insert at end of section】</li><li>变更【Create line if not found】为【Bottom】</li><li>勾选【Capture format】并输入脚本码(全形倒引号要改成半形)：</li></ol></li></ol><pre class="language-"><code>```js quickadd
let text = await this.quickAddApi.utility.getClipboard();
text = await this.quickAddApi.inputPrompt("✍添加灵感笔记", "输入内容", text);
text = text.replace("\n", "<br>");
return text;</code></pre><p> </p><blockquote><p>⚠️ 缺点</p><p>方法1与方法2者都必须在Obsidian里操作，但有可能灵感来时正好在使用别的应用程式。</p></blockquote><h2>方法3. 由外部应用直接新增</h2><p>不必在Obsidian里，直接执行AutoHotkey的弹出式视窗，输入内容後透过Advanced Obsidian URI将内容插入每日笔记的指定标题处。</p><pre class="language-null"><code>;; fleeting-note.ahk
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
&#125;</code></pre><h3>相关链接</h3><ul><li>temlater-fleeting-note.md: <a href="https://gist.github.com/emisjerry/8939f9aa8f4de9eab377b1461cb4f9bd">https://gist.github.com/emisjerry/8939f9aa8f4de9eab377b1461cb4f9bd</a></li><li>fleeting-note.ahk: <a href="https://gist.github.com/emisjerry/01ec842be695a5248db642206b96dee7">https://gist.github.com/emisjerry/01ec842be695a5248db642206b96dee7</a></li></ul><h3>教学视频</h3><p>Bilibili视频：<a href="https://www.bilibili.com/video/BV1Dq4y1d7YE/">https://www.bilibili.com/video/BV1Dq4y1d7YE/</a></p><iframe class="ss-videoIframe" src="https://www.youtube.com/embed/c69rpaaAyEM"> </iframe><p>＃＃</p></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-3019" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%5BObs%EF%BC%8356%5D%20%E5%BF%AB%E9%80%9F%E6%96%B0%E5%A2%9E%E7%81%B5%E6%84%9F%EF%BC%8F%E9%97%AA%E5%BF%B5%E7%AC%94%E8%AE%B0(Fleeting%20Note)%E7%9A%84%203%20%E7%A7%8D%E6%96%B9%E6%B3%95%E3%80%91%E6%88%91%E4%BB%AC%E5%81%B6%E5%B0%94%E4%BC%9A%E6%9C%89%E7%81%B5%E5%85%89%E4%B8%80%E9%97%AA%E3%80%81%E7%A8%8D%E8%B8%AA%E5%8D%B3%E9%80%9D%E7%9A%84%E7%BB%9D%E5%A6%99%E6%83%B3%E6%B3%95%EF%BC%8C%E8%BF%99%E4%BA%9B%E7%AA%81%E5%8F%91%E5%A5%87%E6%83%B3%E4%BD%95%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0%E6%97%A0%E4%BB%8E%E5%BE%AA%E8%BF%B9%E3%80%81%E6%97%A0%E6%B3%95%E8%87%86%E6%B5%8B%EF%BC%8C%E7%81%B5%E6%84%9F%E6%9D%A5%E6%97%A0%E5%BD%B1%E5%8E%BB%E6%97%A0%E8%B8%AA%EF%BC%8C%E6%88%91%E4%BB%AC%E5%BF%85%E9%A1%BB%E5%9C%A8**%E6%9C%80%E7%9F%AD%E7%9A%84%E6%97%B6%E9%97%B4**%E3%80%81%E7%94%A8**%E6%9C%80%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F10%2F10%2F6974e937119e77fad8b93ec5bce1631c.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-9776" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%5BObs%EF%BC%8356%5D%20%E5%BF%AB%E9%80%9F%E6%96%B0%E5%A2%9E%E7%81%B5%E6%84%9F%EF%BC%8F%E9%97%AA%E5%BF%B5%E7%AC%94%E8%AE%B0(Fleeting%20Note)%E7%9A%84%203%20%E7%A7%8D%E6%96%B9%E6%B3%95%E3%80%91%E6%88%91%E4%BB%AC%E5%81%B6%E5%B0%94%E4%BC%9A%E6%9C%89%E7%81%B5%E5%85%89%E4%B8%80%E9%97%AA%E3%80%81%E7%A8%8D%E8%B8%AA%E5%8D%B3%E9%80%9D%E7%9A%84%E7%BB%9D%E5%A6%99%E6%83%B3%E6%B3%95%EF%BC%8C%E8%BF%99%E4%BA%9B%E7%AA%81%E5%8F%91%E5%A5%87%E6%83%B3%E4%BD%95%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0%E6%97%A0%E4%BB%8E%E5%BE%AA%E8%BF%B9%E3%80%81%E6%97%A0%E6%B3%95%E8%87%86%E6%B5%8B%EF%BC%8C%E7%81%B5%E6%84%9F%E6%9D%A5%E6%97%A0%E5%BD%B1%E5%8E%BB%E6%97%A0%E8%B8%AA%EF%BC%8C%E6%88%91%E4%BB%AC%E5%BF%85%E9%A1%BB%E5%9C%A8**%E6%9C%80%E7%9F%AD%E7%9A%84%E6%97%B6%E9%97%B4**%E3%80%81%E7%94%A8**%E6%9C%80%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            