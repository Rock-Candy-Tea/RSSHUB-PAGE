
---
title: '微软警告NOBELIUM攻击技术愈加泛滥 谨防HTML代码夹带恶意软件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1116/08f0904f766d070.png'
author: cnBeta
comments: false
date: Tue, 16 Nov 2021 12:28:00 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1116/08f0904f766d070.png'
---

<div>   
早在 5 月，微软就认定有俄罗斯背景的 NOBELIUM 黑客组织要对持续数月的 SolarWinds 网络攻击事件负责，并同企业、政府和执法机构达成了合作，以遏制此类网络攻击的负面影响。<strong>早些时候，微软更进一步地剖析了 NOBELIUM 使用的一套更加复杂的恶意软件传送方法。可知其用于造成破坏，并获得“HTML Smuggling”系统的访问权。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1116/08f0904f766d070.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1116/08f0904f766d070.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">HTML Smuggling 技术概览（图自：Microsoft <a href="https://www.microsoft.com/security/blog/2021/11/11/html-smuggling-surges-highly-evasive-loader-technique-increasingly-used-in-banking-malware-targeted-attacks/" target="_self">Security</a>）</p><p>微软表示，HTML Smuggling 是一种利用合法 HTML5 和 JavaScript 功能、以高度规避安全系统检测的恶意软件传送技术。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/89c0a55878e931c.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">钓鱼邮件示例</p><p>近年来，这项技术已被越来越多地用于部署网银恶意软件、远程访问木马（RAT）、以及其它有针对性的钓鱼邮件活动。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/1ce8c36a222bd2c.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Mekotio 活动中曝光的威胁行为</p><p>其实早在今年 5 月，这项技术就已经在 NOBELIUM 发起的钓鱼邮件活动中被观察到，最近的案例包括网银木马 Mekotio、AsyncRAT / NJRAT 和 Trickbot（控制肉鸡并传播勒索软件负载和其它威胁）。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/b1acd205c4c51c4.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">HTML Smuggling 网页代码示例</p><p>顾名思义，HTML Smuggling 允许攻击者在特制的 HTML 附件或网页中“夹带私货”。当目标用户在浏览器中打开时，这些恶意编码脚本就会在不知不觉中被解码，进而在受害者的设备上组装出有效负载。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/503d3d80d69bc8f.png" alt="5.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">被 JavaScript 加花的 ZIP 文件</p><p>换言之，攻击者没有直接通过网络来传递可执行文件，而是绕过了防火墙、再在暗地里重新构建恶意软件。举个例子，攻击者会在电子邮件消息中附上 HTML Smuggling（或重定向）页面链接，然后提示自动下载序列。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/0dde8d61782f2bc.png" alt="6.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">钓鱼页面</p><p>为帮助用户辨别愈演愈烈的 HTML Smuggling 攻击，微软在文中给出了一些演示实例，告诫银行与个人采取必要的防御措施，同时不忘推销一下自家的 Microsoft 365 安全解决方案。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/b3f065b7a150c32.png" alt="7.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">在浏览器中构造的、带有密码保护下载器的 JavaScript 实例</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1116/efbf0ef4395318a.png" alt="9.png" referrerpolicy="no-referrer"></p><p>据悉，Microsoft 使用多层方法来抵御网络威胁，通过与一系列其它终端防御措施协同合作，以阻止在攻击链的更高层执行并减轻来自更复杂攻击的后果。</p><p><img src="https://static.cnbetacdn.com/article/2021/1116/004f8ca1a881f17.png" alt="8.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Trickbot 钓鱼活动的 HTML Smuggling 攻击示例</p><p>最后，微软强烈建议广大客户养成良好的习惯，抽空了解各类恶意软件感染案例，同时将非必要的本地 / 管理员权限调到最低。</p>   
</div>
            