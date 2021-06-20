
---
title: 'HanLP 1.8.2 发布，常规维护与修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4976'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4976'
---

<div>   
<div class="content">
                                                                    
                                                        <p>HanLP 1.8.2 现已发布。HanLP 是由一系列模型与算法组成的 Java 工具包，目标是普及自然语言处理在生产环境中的应用。HanLP 具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。 在提供丰富功能的同时，HanLP 内部模块坚持低耦合、模型坚持惰性加载、服务坚持静态提供、词典坚持明文发布，使用非常方便，同时自带一些语料处理工具，帮助用户训练自己的模型。</p> 
<p>新版本具体更新内容如下：</p> 
<ul> 
 <li>调整公式，维特比分词准确率从94.49提升至94.69 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.hankcs.com%2Ft%2Ftopic%2F136%2F61%3Fu%3Dhankcs" target="_blank">https://bbs.hankcs.com/t/topic/136/61?u=hankcs</a></li> 
 <li>改进 HMM 采样函数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.hankcs.com%2Ft%2Ftopic%2F136%2F64%3Fu%3Dhankcs" target="_blank">https://bbs.hankcs.com/t/topic/136/64?u=hankcs</a></li> 
 <li>支持禁用自动刷新词典缓存（CustomDictionaryAutoRefreshCache=false）fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fissues%2F1655" target="_blank">#1655</a></li> 
 <li>修复CoreDictionary的reload方法</li> 
 <li>修订bigram模型</li> 
 <li>修订简繁映射表</li> 
 <li>lve4的声母修正为ve fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fissues%2F1644" target="_blank">#1644</a></li> 
 <li>修复 CustomDictionary.reload() fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Fissues%2F1635" target="_blank">#1635</a></li> 
 <li>数据包兼容<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffile.hankcs.com%2Fhanlp%2Fdata-for-1.7.5.zip" target="_blank">data-for-1.7.5.zip</a><code> md5=1d9e1be4378b2dbc635858d9c3517aaa</code></li> 
 <li>Portable版同步升级到v1.8.1</li> 
</ul> 
<pre>        <dependency>
            <groupId>com.hankcs</groupId>
            <artifactId>hanlp</artifactId>
            <version>portable-1.8.1</version>
        </dependency></pre> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhankcs%2FHanLP%2Freleases%2Ftag%2Fv1.8.2" target="_blank">https://github.com/hankcs/HanLP/releases/tag/v1.8.2</a></p>
                                        </div>
                                      
</div>
            