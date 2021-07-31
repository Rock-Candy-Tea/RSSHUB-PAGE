
---
title: 'ISOMorph攻击可绕过浏览器防护并利用JS代码传递恶意文件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0731/5eb7292c7f9b98e.png'
author: cnBeta
comments: false
date: Sat, 31 Jul 2021 08:19:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0731/5eb7292c7f9b98e.png'
---

<div>   
Menlo Security 刚刚对 HTML Smuggling（又称 ISOMorph）攻击进行了评估，<strong>发现它可以绕过一些网络安全技术（比如过时的代理或沙箱功能），将恶意文件传输给用户。</strong>据说该恶意威胁利用了新颖的攻击手段，以将危险的有效负载直接注入受害者的网络浏览器。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0731/5eb7292c7f9b98e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0731/5eb7292c7f9b98e.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">技术分析</p><p><a href="https://www.menlosecurity.com/blog/isomorph-infection-in-depth-analysis-of-a-new-html-smuggling-campaign/" target="_self">Menlo Security</a> 指出：HTML Smuggling 是一套相当复杂的技术，其利用了 JavaScript 在 HTML 页面上创建恶意负载，而不是发送 HTPP 请求来获取 Web 服务器上的资源。</p><p>需要指出的是，这不该归咎于浏览器技术本身的漏洞或设计缺陷，因为 Web 开发者也经常通过该工具来优化文件的下载。</p><p><a href="https://static.cnbetacdn.com/article/2021/0731/566540c3d56f698.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0731/566540c3d56f698.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">执行流程</p><p>ISOMorph 攻击者使用 JavaScript 代码，直接在浏览器中创建有效负载。首先是创建一个元素“a”，接着在 blob 上设置 HREF，并且编写了点击以开始下载的操作。</p><p>一旦将有效负载下载到了终端设备上，用户必须手动打开，攻击者才会得逞（执行恶意软件）。</p><p><img src="https://static.cnbetacdn.com/article/2021/0731/ef1c8e2549fa08b.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">代码示例</p><p>为绕过各种网络安全检测机制，比如沙箱、旧代理、以及防火墙，攻击者还利用了浏览器无法阻止来自网络解决方案的有效载荷这一漏洞。</p><p>由于有效载荷直接内置于目标浏览器中，传统的安全解决方案几乎对它没辙。</p><p><img src="https://static.cnbetacdn.com/article/2021/0731/03be0d779cb979f.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;"><a href="https://www.virustotal.com/graph/embed/g0ed7d7222a764ea4a78fdbb325f09facfa674f79a6214451b1d97a3d9d453e6d" target="_self">VirusTotal</a> 追踪截图</p><p><a href="https://secureteam.co.uk/articles/information-assurance/what-is-html-smuggling/" target="_self">SecureTeam</a> 指出，尽管第一反应是禁用 JavaScript，但此举明显矫枉过正，因为许多合法 Web 应用程序和系统也在使用这项技术。</p><p>当然，防范 HTML 攻击并不难，SecureTeam 的建议是采用更智能的网络安全设计，包括由各种技术来构建的多层“深度防御”环境。</p><p>那样即使外界的恶意软件无法渗透网络边界，内网的其它防御测试也能够对相关感染进行检测和治理。</p>   
</div>
            