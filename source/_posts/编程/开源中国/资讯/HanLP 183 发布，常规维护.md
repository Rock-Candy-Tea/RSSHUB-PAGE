
---
title: 'HanLP 1.8.3 发布，常规维护'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=782'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=782'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">HanLP 1.8.3 现已发布。HanLP 是由一系列模型与算法组成的 Java 工具包，目标是普及自然语言处理在生产环境中的应用。HanLP 具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。 在提供丰富功能的同时，HanLP 内部模块坚持低耦合、模型坚持惰性加载、服务坚持静态提供、词典坚持明文发布，使用非常方便，同时自带一些语料处理工具，帮助用户训练自己的模型。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本具体更新内容如下：</p> 
<ul> 
 <li>修复动态自定义词典与CustomDictionaryForcing的搭配问题 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fissues%2F1712" target="_blank">#1712</a></li> 
 <li>调整<code>莎=sha1,suo1</code><span> </span>fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fissues%2F1670" target="_blank">#1670</a></li> 
 <li>根据总词频动态决定未登录词的默认词频</li> 
 <li>DoubleArrayTrie里的LongestSearcher的next支持null作为值 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftiandiweizun" target="_blank">@tiandiweizun</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fpull%2F1674" target="_blank">#1674</a></li> 
 <li>Update DoubleArrayTrie.java的注释 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTITC" target="_blank">@TITC</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fpull%2F1699" target="_blank">#1699</a></li> 
 <li>数据包兼容<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffile.hankcs.com%2Fhanlp%2Fdata-for-1.7.5.zip" target="_blank">data-for-1.7.5.zip</a><code><span> </span>md5=1d9e1be4378b2dbc635858d9c3517aaa</code></li> 
 <li>Portable版同步升级到v1.8.3</li> 
</ul> 
<div> 
 <pre>        <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
            <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.hankcs</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
            <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>hanlp</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
            <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>portable-1.8.3</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
        </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="color:#24292f; text-align:start"><strong>Full Changelog</strong>:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fcompare%2Fv1.8.2...v1.8.3" target="_blank">v1.8.2...v1.8.3</a></p> 
<p style="color:#24292f; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Freleases%2Ftag%2Fv1.8.3" target="_blank">https://github.com/hankcs/HanLP/releases/tag/v1.8.3</a></p>
                                        </div>
                                      
</div>
            