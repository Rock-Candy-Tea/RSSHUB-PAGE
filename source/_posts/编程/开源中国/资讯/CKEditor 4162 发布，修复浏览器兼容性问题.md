
---
title: 'CKEditor 4.16.2 发布，修复浏览器兼容性问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cd1418095dfba3258b464b27634546aa13c.png'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 06:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cd1418095dfba3258b464b27634546aa13c.png'
---

<div>   
<div class="content">
                                                                                            <p>CKEditor 4.16.2 维护版本已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-4.16.2-with-browser-improvements-and-security-fixes%2F" target="_blank">发布</a>。此版本是一个维护版本，更新内容包括修复安全问题、修复浏览器兼容性问题、升级与 React 的集成，以及修复其他重要问题。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cd1418095dfba3258b464b27634546aa13c.png" referrerpolicy="no-referrer"></p> 
<p><strong>修复安全问题</strong></p> 
<p>修复了剪贴板插件中的安全漏洞 (CVE-2021-32809)，该漏洞会引起出现滥用粘贴功能（使用格式错误的 HTML ）的情况，进而导致将任意的 HTML 注入编辑器。</p> 
<p>此外，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fdocs%2Fckeditor4%2Flatest%2Fguide%2Fdev_widgets.html" target="_blank">Widget</a> 插件中发现的另一个漏洞 (CVE-2021-32808) 容易导致出现执行 JavaScript 代码的情况，以及 Fake Objects 插件由于容易注入格式错误的 Fake Objects HTML (CVE-2021-37695)，这也可能会导致执行 JavaScript 代码。</p> 
<p><strong>修复浏览器兼容性问题</strong></p> 
<p>此版本针对多款浏览器引入了多项错误修正和增强功能，确保跨平台兼容性，以提供最便捷的使用体验。</p> 
<ul> 
 <li>修复在 Chrome 中显示空格键无效的问题。在删除两个连续空格的其中一个后，剩下的一个会直接以字符的形式 (&nbsp;) 显示，而非一个空格。最新的版本修复了这个问题，现在可以按预期运行。</li> 
 <li>为所有支持的 Internet Explorer 版本引入了 CSS 选择器转义机制 (CSS.escape() polyfill)。此功能解决了表格元素（如 td、tr 或 th）的 id 以点开头会导致编辑器中出现 javascript 运行时错误的问题。另一个已解决的问题是，在 id 包含逗号的编辑器中无法拖放图像。新引入的机制完全符合最近的官方 HTML 规范。</li> 
 <li>针对 Firefox 的错误修复。</li> 
</ul> 
<p><strong>升级与 React 的集成</strong></p> 
<p>与 React 的集成升级到了 2.0.0 版本，增加了对 React v17.x 的支持、对 React hooks 的支持，以及对 TypeScript 和类型的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-4-react-integration-2.0.0-with-react-17-support%2F" target="_blank">详情点此查看</a>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-14c9d43b23ad1508c411a58e7cbc18b8d41.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-4.16.2-with-browser-improvements-and-security-fixes%2F" target="_blank">更多内容查看发布公告</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fckeditor-4%2Fdownload%2F" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            