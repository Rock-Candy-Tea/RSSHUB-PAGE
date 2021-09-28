
---
title: 'Guava 31 发布，Google 的核心 Java 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2944'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2944'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Guava 是 Google 的一套核心 Java 库，包括新的集合类型（如 multimap 和 multiset）、图库，以及用于并发、I/O、散列、缓存、基元、字符串等的实用工具。它被广泛用于 Google 内部的 Java 项目，同时也被许多其他公司广泛使用。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">更新日志</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>对 Guava 的空值进行了更彻底的注释</li> 
 <li><code>base</code>：修改了<span> </span><code>Functions.forSupplier</code><span> </span>和<span> </span><code>Predicates.instanceOf</code>，以接受一个额外的类型参数来指定返回<span> </span><code>Function</code>/<span> </span><code>Predicate</code><span> </span>的输入类型。</li> 
 <li><code>collect</code>：增加了<span> </span><code>ImmutableMap.ofEntries</code>，与<span> </span><code>Map.ofEntries</code><span> </span>类似，但适用于<span> </span><code>ImmutableMap</code></li> 
 <li><code>collect</code>：增加了<span> </span><code>ImmutableMap.of</code>、<span> </span><code>ImmutableBiMap.of</code><span> </span>和<span> </span><code>ImmutableSortedMap.of</code><span> </span>的重载，最多可容纳10个条目。</li> 
 <li><code>collect</code>：将<span> </span><code>ImmutableMap.Builder.build()</code><span> </span>重命名为<span> </span><code>buildOrThrow()</code>。现有的<span> </span><code>build()</code><span> </span>方法将继续存在，但可能会被废弃。</li> 
 <li><code>collect</code>：从<span> </span><code>Interner</code><span> </span>和<span> </span><code>Interners</code><span> </span>中删除了<span> </span><code>@Beta</code>。</li> 
 <li><code>collect</code>：为<span> </span><code>Streams.stream(Optional)</code><span> </span>添加了<span> </span><code>@InlineMe</code>。</li> 
 <li><code>hash</code><span> </span>：从<span> </span><code>HashFunction</code><span> </span>中删除了<span> </span><code>@Beta</code>。</li> 
 <li><code>hash</code>：废弃了有问题的<span> </span><code>murmur3_32</code>，并引入<span> </span><code>murmur3_32_fixed</code></li> 
 <li><code>io</code>：改变了<span> </span><code>CharStreams.asWriter(appendable).write(string[, ...])</code><span> </span>以拒绝一个空<span> </span><code>string</code>。</li> 
 <li><code>io</code>: 修正了<span> </span><code>FileBackedOutputStream</code><span> </span>清理中的一个错误。</li> 
 <li><code>net</code>：改变了<span> </span><code>HostAndPort.fromString</code>，以拒绝用非 ASCII 数字拼成的端口号。</li> 
 <li><code>net</code>: 为<span> </span><code>X-Device-Ip</code>、<span> </span><code>X-Device-Referer</code>、<span> </span><code>X-Device-Accept-Language</code>、<span> </span><code>X-Device-Requested-With</code>、<code>Sec-CH-Prefers-Color-Scheme</code>、<span> </span><code>Sec-CH-UA-Bitness</code><span> </span>和<span> </span><code>Keep-Alive</code><span> </span>增加了<span> </span><code>HttpHeaders</code><span> </span>常量。</li> 
 <li><code>primitives</code>：修正了<span> </span><code>UnsignedLong.doubleValue()</code><span> </span>中的一个舍入错误。</li> 
 <li><code>reflect</code>：改变了<span> </span><code>Invokable</code><span> </span>的类型层次结构，<span> </span><code>Invokable</code><span> </span>不再继承<span> </span><code>AccessibleObject</code><span> </span>或<span> </span><code>GenericDeclaration</code><span> </span>。</li> 
 <li><code>testlib</code>：增强了<span> </span><code>NullPointerTester</code>，允许<span> </span><code><T extends @Nullable Object></code><span> </span>类型的参数<span> </span><code>null</code>。</li> 
 <li><code>testlib</code>：修正了影响自定义集合测试套件的派生测试的错误。<span> </span><code>setUp</code><span> </span>和<span> </span><code>tearDown</code><span> </span>方法现在被复制到派生测试套件。</li> 
 <li><code>util.concurrent</code>: 增加了<span> </span><code>ServiceManager.startupDurations()</code>。</li> 
 <li><code>util.concurrent</code>：删除了<span> </span><code>Futures.catching</code><span> </span>和<span> </span><code>catchingAsync</code><span> </span>的 GWT-only 重载，这些重载允许调用者省略<span> </span><code>Executor</code>。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Freleases%2Ftag%2Fv31.0" target="_blank">https://github.com/google/guava/releases/tag/v31.0</a></p>
                                        </div>
                                      
</div>
            