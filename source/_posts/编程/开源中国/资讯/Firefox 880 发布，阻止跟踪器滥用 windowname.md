
---
title: 'Firefox 88.0 发布，阻止跟踪器滥用 window.name'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b74a4d1272069ebf359ab4c6c19e4fbf413.png'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 07:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b74a4d1272069ebf359ab4c6c19e4fbf413.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Firefox 88.0 版本现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.mozilla.org%2Fsecurity%2F2021%2F04%2F19%2Ffirefox-88-combats-window-name-privacy-abuses%2F" target="_blank">发布</a>，该版本引入了一项新的保护措施，以进一步防止 Web 上的隐私泄露。在 Firefox 施加的新限制下，跟踪器将不再能够滥用 window.name 属性来跨网站跟踪用户。</p> 
<p>具体更新内容如下：</p> 
<p><strong>New</strong></p> 
<ul> 
 <li>PDF 表格现在支持在 PDF 文件中嵌入 JavaScript。一些 PDF 表格使用 JavaScript 进行验证和其他交互功能。</li> 
 <li>Print 更新：Margin units 现在已 localized。</li> 
 <li>现在 Linux 上支持使用触摸板进行平滑的捏合缩放。</li> 
 <li>为了防止跨网站的隐私泄露，Firefox 现在将 window.name 数据隔离到创建该数据的网站。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.mozilla.org%2Fsecurity%2F2021%2F04%2F19%2Ffirefox-88-combats-window-name-privacy-abuses%2F" target="_blank">了解更多</a></li> 
</ul> 
<p><strong>Fixed</strong></p> 
<ul> 
 <li>Screen readers 不再错误地阅读网站在视觉上隐藏的内容，如谷歌帮助面板中的文章。</li> 
 <li>各种<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fsecurity%2Fadvisories%2Fmfsa2021-16%2F" target="_blank">安全修复程序</a>。</li> 
</ul> 
<p><strong>Changed</strong></p> 
<ul> 
 <li>如果用户在过去 50 秒内已经在同一网站的同一标签页中授予同一设备的访问权限，那么 Firefox 将不会提示用户访问麦克风或摄像头。此举减少了用户被提示授予设备访问权限的次数。</li> 
 <li>从 url 栏的页面操作菜单中删除了"Take a Screenshot"功能。要截屏，可右击打开上下文菜单。也可以通过自定义菜单直接在工具栏上添加截图快捷方式。打开 Firefox 菜单，选择“自定义...”。</li> 
 <li>FTP 支持已被禁用，并计划在即将发布的版本中完全移除。解决这一安全风险，降低了攻击的可能性，同时也取消了对非加密协议的支持。</li> 
</ul> 
<p><strong>Enterprise</strong></p> 
<ul> 
 <li>在最新版本的 Firefox 中，已经实现了各种错误修复和新策略。详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.mozilla.org%2Fkb%2Ffirefox-enterprise-88-release-notes" target="_blank">Firefox for Enterprise 88 发行说明</a>。</li> 
</ul> 
<p><strong>Developer</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fdocs%2FMozilla%2FFirefox%2FReleases%2F88" target="_blank">Developer Information</a></li> 
 <li>在网络面板中引入了一个新的切换按钮，用于在 JSON 格式化的 HTTP 响应和原始数据之间进行切换（如 received over the wire）。</li> 
</ul> 
<p><img alt height="196" src="https://oscimg.oschina.net/oscnet/up-b74a4d1272069ebf359ab4c6c19e4fbf413.png" width="500" referrerpolicy="no-referrer"></p> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fen-US%2Ffirefox%2F88.0%2Freleasenotes%2F" target="_blank">https://www.mozilla.org/en-US/firefox/88.0/releasenotes/</a></p>
                                        </div>
                                      
</div>
            