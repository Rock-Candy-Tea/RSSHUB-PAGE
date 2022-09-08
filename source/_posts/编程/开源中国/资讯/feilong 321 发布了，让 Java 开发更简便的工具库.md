
---
title: 'feilong 3.2.1 发布了，让 Java 开发更简便的工具库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=328'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 11:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=328'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">feilong 3.2.1 发布了，让Java开发更简便的工具库</p> 
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
     <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>3.2.1</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="color:#24292f; text-align:start">Gradle 依赖配置:</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">com</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">github</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ifeilong</span>:<span>feilong</span>:<span style="color:var(--color-prettylights-syntax-constant)">3.2</span><span style="color:var(--color-prettylights-syntax-constant)">.1</span></pre> 
</div> 
<p style="color:#24292f; text-align:start">本次升级共有<span> </span><code>9</code><span> </span>处变更, 具体参见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fmilestone%2F16%3Fclosed%3D1" target="_blank">3.2.1 milestone</a></p> 
<h2 style="text-align:start">🍑<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-core%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">feilong-core</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F406" target="_blank">#406</a><span> </span>✨<span> </span>Dateutil todate 新增模式的pattern 简化写法, 默认方法使用 yyyy-MM-dd 模式 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">enhancement</a>]</p> 
<p style="color:#24292f; text-align:start">即 你可以使用下面的写法</p> 
<div style="text-align:start"> 
 <pre><span>DateUtil</span>.<span style="color:var(--color-prettylights-syntax-entity)">toDate</span>(<span style="color:var(--color-prettylights-syntax-string)">"2022-09-08"</span>)</pre> 
</div> 
<p style="color:#24292f; text-align:start">代替以前必须传<span> </span><code>yyyy-MM-dd</code></p> 
<div style="text-align:start"> 
 <pre><span>DateUtil</span>.<span style="color:var(--color-prettylights-syntax-entity)">toDate</span>(<span style="color:var(--color-prettylights-syntax-string)">"2022-09-08"</span>,<span style="color:var(--color-prettylights-syntax-string)">"yyyy-MM-dd"</span>)</pre> 
</div> 
<div style="text-align:start"> 
 <pre><span>DateUtil</span>.<span style="color:var(--color-prettylights-syntax-entity)">toDate</span>(<span style="color:var(--color-prettylights-syntax-string)">"2022-09-08"</span>,<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">DatePattern</span>.<span style="color:var(--color-prettylights-syntax-constant)">COMMON_DATE</span>)</pre> 
</div> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F403" target="_blank">#403</a><span> </span>✨<span> </span>uriutil encode decode 增加默认utf-8的方法 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">enhancement</a>]<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F387" target="_blank">#387</a><span> </span>✨<span> </span>封装个方法来简化下面设置url 的代码 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">enhancement</a>]</p> 
<p style="color:#24292f; text-align:start">新建<span> </span><code>com.feilong.core.net.URLUtil.ifNoHttpOrHttpsProtocolPrependPre(String, String)</code></p> 
<p style="color:#24292f; text-align:start">如以下10行代码, 作用是判断LogoPic 是不是空, 如果不是, 判断是不是以<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--2sst8k%2F" target="_blank">http://开头</a>, 不是以这个开头会拼接前缀</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">if</span> (<span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>() != <span style="color:var(--color-prettylights-syntax-constant)">null</span> && !<span style="color:var(--color-prettylights-syntax-string)">""</span>.<span style="color:var(--color-prettylights-syntax-entity)">equals</span>(<span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>())) &#123;
            <span style="color:var(--color-prettylights-syntax-comment)">// 微信登录头像地址是绝对路径</span>
            <span style="color:var(--color-prettylights-syntax-comment)">// 喜马拉雅登录头像地址是相对路径</span>
            <span style="color:var(--color-prettylights-syntax-keyword)">if</span> (<span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>().<span style="color:var(--color-prettylights-syntax-entity)">startsWith</span>(<span style="color:var(--color-prettylights-syntax-string)">"http://"</span>)) &#123;
                <span>result</span>.<span style="color:var(--color-prettylights-syntax-entity)">setUserLogoPic</span>(<span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>());
            &#125; <span style="color:var(--color-prettylights-syntax-keyword)">else</span> &#123;
                <span>result</span>.<span style="color:var(--color-prettylights-syntax-entity)">setUserLogoPic</span>(<span>coverPerfix</span> + <span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>());
            &#125;
        &#125;</pre> 
</div> 
<p style="color:#24292f; text-align:start">可以使用以下1行代码代替</p> 
<div style="text-align:start"> 
 <pre><span>result</span>.<span style="color:var(--color-prettylights-syntax-entity)">setUserLogoPic</span>(<span style="color:var(--color-prettylights-syntax-constant)">URLUtil</span>.<span style="color:var(--color-prettylights-syntax-entity)">ifNoHttpOrHttpsProtocolPrependPre</span>(<span>userInfo</span>.<span style="color:var(--color-prettylights-syntax-entity)">getLogoPic</span>(), <span>coverPerfix</span>));</pre> 
</div> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F402" target="_blank">#402</a><span> </span>✨<span> </span>让 CollectionsUtil.addIgnoreNullOrEmpty(Collection, T) 支持动态数组 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Aenhancement%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">enhancement</a>]</p> 
<h2 style="text-align:start">🍷<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253Afeilong-net%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">feilong-net</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F405" target="_blank">#405</a><span> </span>http log jsonformat 转成tostring [[help wanted](https://github.com/ifeilong/feilong/issues?q=is%3Aissue+label%3Ahelp wanted+milestone%3A3.2.1+is%3Aclosed)]</p> 
<h2 style="text-align:start">⬆️<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%3Fq%3Dis%253Aissue%2Blabel%253A%25E4%25BE%259D%25E8%25B5%2596%25E5%258D%2587%25E7%25BA%25A7%2Bmilestone%253A3.2.1%2Bis%253Aclosed" target="_blank">依赖升级</a></h2> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F409" target="_blank">#409</a><span> </span>jsoup 升级到 1.15.3<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F408" target="_blank">#408</a><span> </span>logback 升级到1.4.0<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F410" target="_blank">#410</a><span> </span>maven-javadoc-plugin 升级到 3.4.1<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fifeilong%2Ffeilong%2Fissues%2F412" target="_blank">#412</a><span> </span>maven-project-info-reports-plugin 升级到3.4.1</p>
                                        </div>
                                      
</div>
            