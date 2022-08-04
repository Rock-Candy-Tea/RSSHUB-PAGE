
---
title: 'feilong 3.2.0 发布，让 Java 开发更简便的工具库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7474'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 10:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7474'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">feilong 3.2.0 发布了，让Java开发更简便的工具库</p> 
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
     <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>3.2.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="color:#24292f; text-align:start">Gradle 依赖配置:</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">com</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">github</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ifeilong</span>:<span>feilong</span>:<span style="color:var(--color-prettylights-syntax-constant)">3.2</span><span style="color:var(--color-prettylights-syntax-constant)">.0</span></pre> 
</div> 
<p style="color:#24292f; text-align:start">本次升级共有<span> </span><code>10</code><span> </span>处变更, 具体参见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fmilestone%2F15%3Fclosed%3D1" target="_blank">3.2.0 milestone</a></p> 
<h2 style="text-align:start">🍑<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-core%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">feilong-core</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F60" target="_blank">#60</a><span> </span>✨<span> </span>Validator 添加一个 类似于 StringUtils.isAnyBlank(CharSequence...) 的方法 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">enhancement</a>]</p> 
<h2 style="text-align:start">🔒<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-security%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">feilong-security</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F382" target="_blank">#382</a><span> </span>修改 com.feilong.security.oneway.Sm3Util 注释 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Ajavadoc%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">javadoc</a>]</p> 
<h2 style="text-align:start">🍼<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-servlet%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">feilong-servlet</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F153" target="_blank">#153</a><span> </span>com.feilong.servlet.ServletContextUtil.EXCLUDE_KEYS 做成配置文件</p> 
<h2 style="text-align:start">⬆️<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253A%25E4%25BE%259D%25E8%25B5%2596%25E5%258D%2587%25E7%25BA%25A7%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">依赖升级</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F384" target="_blank">#384</a><span> </span>maven-assembly-plugin 升级到 3.4.2<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F398" target="_blank">#398</a><span> </span>maven-install-plugin 升级到 3.0.1<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F399" target="_blank">#399</a><span> </span>maven-resources-plugin 升级到 3.3.0<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F383" target="_blank">#383</a><span> </span>升级 bcprov-jdk15on>1.70<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F381" target="_blank">#381</a><span> </span>升级 jsoup 1.15.2</p> 
<h2 style="text-align:start">➖<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253A%25E4%25BE%259D%25E8%25B5%2596%25E8%25B0%2583%25E6%2595%25B4%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">依赖调整</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F205" target="_blank">#205</a><span> </span>用 log4j2 替代 log4j</p> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253A%25E5%2585%25B6%25E4%25BB%2596%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">其他</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F380" target="_blank">#380</a><span> </span>🔥<span> </span>删除 maven-antrun-plugin 依赖管理 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253A%25E5%2588%25A0%25E9%2599%25A4%2Bmilestone%253A3.2.0%2Bis%253Aclosed" target="_blank">删除</a>]</p> 
<p> </p>
                                        </div>
                                      
</div>
            