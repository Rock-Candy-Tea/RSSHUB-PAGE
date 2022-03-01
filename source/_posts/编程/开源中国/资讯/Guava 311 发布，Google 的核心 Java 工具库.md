
---
title: 'Guava 31.1 发布，Google 的核心 Java 工具库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7719'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7719'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Guava 是 Google 的一套核心 Java 库，包括新的集合类型（如 multimap 和 multiset）、图库，以及用于并发、I/O、散列、缓存、基元、字符串等实用工具。它被广泛用于 Google 内部的 Java 项目，同时也被许多其他公司广泛使用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，Guava 31.1 已发布，该版本带来以下变更：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Base</code>：弃用<span> </span><code>lazyStackTrace</code><span style="color:#24292f"><span> </span>和<span> </span></span><code>lazyStackTraceIsLazy</code><span> </span>两个<span> </span><span style="color:#24292f"><code>Throwables</code></span><span> </span>方法。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F6ebd7d864830dbf615a767702bf5b0261f1a9722" target="_blank">6ebd7d8</a><span> </span>)</li> 
 <li><code>collect</code>：添加了一个新方法<code>ImmutableMap.Builder.buildKeepingLast()</code>，该方法保留任何给定键的最后一个值，而不是在键出现多次时抛出异常。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F68500b2c09fa6985eab2e41577e2992685b57f2b" target="_blank">68500b2</a><span> </span>)</li> 
 <li><code>hash</code>: 补充<span> </span><code>Hashing.fingerprint2011()</code>。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F13f703c25f43bda8935b28e7b481de48d6b9bc1b" target="_blank">13f703c</a><span> </span>)</li> 
 <li>更改<span> </span><code>ByteStreams.nullOutputStream()</code><span> </span>以遵循<span> </span><code>OutputStream.write</code><span> </span>的约定，如果字节范围超出范围则抛出异常</li> 
 <li><code>net</code>：添加<span> </span><code>@CheckReturnValue</code><span> </span>到包中。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2Fa0e2577de61a0d7e8a3dd075be66a31c93ea0446" target="_blank">a0e2577</a><span> </span>)</li> 
 <li><code>net</code>：为<span> </span><code>Access-Control-Allow-Private-Network</code><span> </span>添加了<span> </span><code>HttpHeaders</code><span> </span>常量。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F6dabbdf9c9154a0c4cda276779ca7c9a14cfa720" target="_blank">6dabbdf</a><span> </span>)</li> 
 <li><span style="color:#24292f"><code>util.concurrent</code>：</span>为<span> </span><code>AtomicDouble</code><span> </span>和<span> </span><code>AtomicDoubleArray</code><span> </span>添加了累积/更新（<span style="color:#24292f">accumulate/update</span>）方法。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fcommit%2F2d875d327ad74cbde5a6f18fbf85724bfbb5c47a" target="_blank">2d875d3</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Freleases%2Ftag%2Fv31.1" target="_blank">https://github.com/google/guava/releases/tag/v31.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            