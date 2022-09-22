
---
title: 'feilong 3.3.0 发布，让Java开发更简便的工具库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9785'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 15:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9785'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">feilong 3.3.0 发布了，让Java开发更简便的工具库</p> 
<ol> 
 <li>让你从大量重复的底层代码中脱身,提高开发效率;</li> 
 <li>让你的代码<code>更简炼</code>，<code>易写</code>、<code>易读</code>、<code>易于维护</code>;</li> 
</ol> 
<p style="color:#24292f; text-align:start">文档地址:<span> </span><a href="http://feilong-core.mydoc.io/">http://feilong-core.mydoc.io/</a></p> 
<p style="color:#24292f; text-align:start">maven 依赖配置:</p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
     <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.github.ifeilong</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
     <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>feilong</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
     <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>3.3.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="color:#24292f; text-align:start">Gradle 依赖配置:</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">com</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">github</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ifeilong</span>:<span>feilong</span>:<span style="color:var(--color-prettylights-syntax-constant)">3.3</span><span style="color:var(--color-prettylights-syntax-constant)">.0</span></pre> 
</div> 
<p style="color:#24292f; text-align:start">本次升级共有<span> </span><code>3</code><span> </span>处变更, 具体参见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fmilestone%2F19%3Fclosed%3D1" target="_blank">3.3.0 milestone</a></p> 
<h2 style="text-align:start">🍷<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-net%2Bmilestone%253A3.3.0%2Bis%253Aclosed" target="_blank">feilong-net</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F371" target="_blank">#371</a><span> </span>✨<span> </span>httpclient 支持retry功能 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.3.0%2Bis%253Aclosed" target="_blank">enhancement</a>]</p> 
<p style="color:#24292f; text-align:start">主要处理, httpclient默认<span> </span><code>java.net.SocketTimeoutException</code>,<span> </span><code>org.apache.http.conn.ConnectTimeoutException</code><span> </span>两个超时异常不重试的问题</p> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-net-bot%2Bmilestone%253A3.3.0%2Bis%253Aclosed" target="_blank">feilong-net-bot</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F417" target="_blank">#417</a><span> </span>新增钉钉机器人/企业微信机器人自动捕获异常 消息机器人报错比如超时等不影响大局 支持参数设置</p> 
<p style="color:#24292f; text-align:start">example:</p> 
<p style="color:#24292f; text-align:start"><code><feilong:dingtalkBot id="dingtalkBot" accessToken="********" secret="********" defaultTitle="aaa" isCatchException="true" /></code></p> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F365" target="_blank">#365</a><span> </span>钉钉机器人/企业微信机器人 支持异步</p> 
<p style="color:#24292f; text-align:start">example:</p> 
<p style="color:#24292f; text-align:start"><code><feilong:dingtalkBot id="dingtalkBot" accessToken="********" secret="********" defaultTitle="aaa" isAsync="true" /></code></p>
                                        </div>
                                      
</div>
            