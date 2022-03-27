
---
title: 'CKEditor 4.18.0 发布，修复远程代码执行漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d59138229930e138161d82124a59ee8dae3.png'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 23:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d59138229930e138161d82124a59ee8dae3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CKEditor 4.18.0 已发布，更新内容包括修复针对浏览器的错误，以及完善安全补丁。</p> 
<p>CKEditor 4.18.0 为 HTML 处理核心模块和对话框插件提供了重要的安全修复。它还包括在最新版本的 Chrome 中对 Paste From Word 插件进行重要的错误修复。此外，新版本还弃用了生命周期已结束的 WebSpellChecker Dialog 插件。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d59138229930e138161d82124a59ee8dae3.png" referrerpolicy="no-referrer"></p> 
<p><strong>安全修复</strong></p> 
<p>CKEditor 4 HTML 处理核心模块中有潜在的安全漏洞，该漏洞允许注入格式错误的 HTML 以绕过内容清理，这可能导致执行 JavaScript 代码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fckeditor%2Fckeditor4%2Fsecurity%2Fadvisories%2FGHSA-4fc4-4p5g-6w89" target="_blank">(CVE-2022-24728)。</a>新版本针对该漏洞提供了修复补丁。</p> 
<p>此外，CKEditor 4 团队在标准安全审计期间发现了 CKEditor 4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fcke4%2Faddon%2Fdialog" target="_blank">对话框插件</a>中潜在的正则表达式拒绝服务漏洞。该漏洞导致攻击者滥用对话输入验证器正则表达式，这可能导致性能显着下降 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fckeditor%2Fckeditor4%2Fsecurity%2Fadvisories%2FGHSA-f6rf-9m92-x2hh" target="_blank">(CVE-2022-24729)</a>。当前版本已修复此漏洞。</p> 
<p>官方强烈建议升级至新版本，以避免任何潜在风险。</p> 
<p><strong>修复针对浏览器的错误</strong></p> 
<p>Chrome 98 引入了一个错误，该错误会导致“从 Word 粘贴”插件中的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D1302246" target="_blank">像素单位计算不正确</a>，从而导致某些功能（如表格边框）的大小无效。此版本通过更新可缓解问题的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fdocs%2Fckeditor4%2Flatest%2Fapi%2FCKEDITOR_tools.html%23method-convertToPx" target="_blank">convertToPx 方法来修复此问题。</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-4.18.0-browser-bugfix-and-security-patches%2F" target="_blank">更多内容查看发布公告</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fckeditor-4%2Fdownload%2F" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            