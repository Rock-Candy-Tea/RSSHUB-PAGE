
---
title: 'Guava 30.1.1 发布，Google 的 Java 核心工具库'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Tue, 23 Mar 2021 07:41:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p>Guava 30.1.1 现已发布。Guava 是 Google 的一个开源项目，包含许多 Google 核心 Java 常用库，如：集合 [collections] 、缓存 [caching] 、原生类型支持 [primitives support] 、并发库 [concurrency libraries] 、通用注解 [common annotations] 、字符串处理 [string processing] 与 I/O 等。</p> 
<p>更新内容如下：</p> 
<ul> 
 <li>增强了 <a href="https://www.oschina.net/news/123566/guava-30-1-released">Guava 30.1</a> 在 Java 7 VM 下运行<code>guava-android</code>时的 warning log message 的侵占性。（Android VM 不受影响）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F00c25e9b1194e1792da848852d214639d9de59b7" target="_blank">00c25e9</a>）</li> 
 <li><code>cache</code>：修复了<code>asMap().compute(...)</code>与负载之间的兼容性。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F42bf4f4eb7d299d635838296e322ec7e1e77a440" target="_blank">42bf4f4</a>）</li> 
 <li><code>cache</code>：已添加<code>@CheckReturnValue</code>到某些 API。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2Fa5ef129ffc4e4d5a19f38660058ae79f42627136" target="_blank">a5ef129</a>）</li> 
 <li><code>collect</code>：在不可变类型的 mutator 方法中添加了<code>@DoNotCall</code>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F6ae9532d11b871ea9d8edd691cf7f64f35add6f0" target="_blank">6ae9532</a>）</li> 
 <li><code>hash</code>：已从<code>HashCode</code>中删除了<code>@Beta</code>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F2c9f161e10ed4f4568c67cbeb47f3f1f4b3d9c08" target="_blank">2c9f161</a>）</li> 
 <li><code>io</code>：已从<code>CountingOutputStream</code>中删除了<code>@Beta</code>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2Fd394bac847467039530f514f880ecca27263d0ff" target="_blank">d394bac</a>）</li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Freleases%2Ftag%2Fv30.1.1" target="_blank">https://github.com/google/guava/releases/tag/v30.1.1</a></p> 
<p><strong>Maven</strong></p> 
<pre><dependency>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>30.1.1-jre</version>
  <!-- or, for Android: -->
  <version>30.1.1-android</version>
</dependency></pre>
                                        </div>
                                      
</div>
            