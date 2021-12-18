
---
title: 'Node.js v17.3.0 发布，更新 OpenSSL 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3924'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3924'
---

<div>   
<div class="content">
                                                                                            <p>Node.js 是一个跨平台的 JavaScript 运行时环境，使用高效、轻量级的事件驱动、非阻塞 I/O 模型。目前更新了 v17.3.0 版本，主要内容是将 OpenSSL 升级到 3.0.1 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41177" target="_blank">#41177</a>）。</p> 
<p>OpenSSL-3.0.1 包含针对 CVE-2021-4044 的修复：无效处理 libssl 中的 X509_verify_cert() 内部错误（中等）。这是 OpenSSL 中的一个漏洞，可以通过 Node.js 加以利用。更多信息可以<a href="http://https : //www.openssl.org/news/secadv/20211214.txt">在这里阅读</a>。</p> 
<p>另外一些显著变化：</p> 
<p><strong>库 lib</strong></p> 
<ul> 
 <li>使 AbortSignal 可克隆/可转移（James M Snell）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41050" target="_blank">#41050</a></li> 
</ul> 
<p><strong style="color:#333333">开发 deps</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333"><span> </span>npm 升级到 8.3.0 版本 <span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41127" target="_blank">#41127</a></li> 
</ul> 
<p><strong style="color:#333333">文档 doc</strong></p> 
<ul> 
 <li>将 <span style="background-color:#ffffff; color:#333333">@bnb 添加为贡献者 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41100" target="_blank">#41100</a></li> 
</ul> 
<p><strong>进程</strong> <strong style="color:#333333">process</strong></p> 
<ul> 
 <li>添加 <span style="background-color:#f0f0f0; color:#333333">getActiveResourcesInfo()</span>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40813" target="_blank">#40813</a></li> 
</ul> 
<p><strong>计时器</strong> <strong style="color:#333333">timers</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#2e3033">添加实验性的调度器 API </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40909" target="_blank">#40909</a></li> 
</ul> 
<p>除上述显著更新外，此版本还有大量其他更新内容，完整更改列表可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv17.3.0%2F" target="_blank">查看更新公告原文</a>。</p>
                                        </div>
                                      
</div>
            