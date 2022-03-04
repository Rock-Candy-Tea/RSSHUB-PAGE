
---
title: 'Arthas 发布 3.5.6 版本：应用排包瘦身不再烦恼'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://arthas.aliyun.com/doc/_images/arthas.png'
author: 开源中国
comments: false
date: Fri, 04 Mar 2022 11:10:00 GMT
thumbnail: 'https://arthas.aliyun.com/doc/_images/arthas.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://arthas.aliyun.com/doc/_images/arthas.png" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0"><code>Arthas</code>是Alibaba开源的Java诊断工具，深受开发者喜爱。</p> 
<ul style="list-style-type:disc"> 
 <li> <p>Github： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Farthas" target="_blank">https://github.com/alibaba/arthas</a></p> </li> 
 <li> <p>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farthas.aliyun.com%2Fdoc%2F" target="_blank">https://arthas.aliyun.com/doc/</a></p> </li> 
</ul> 
<p style="color:black; margin-left:0; margin-right:0">Arthas 最新发布了 3.5.6 版本：</p> 
<ol style="list-style-type:decimal"> 
 <li> <p>支持统计ClassLoader实际使用URL和未使用的URL</p> </li> 
 <li> <p>增加<code>memory</code>命令</p> </li> 
 <li> <p>恢复对 enum 类增强支持，过滤掉的类在日志中打印具体原因。</p> </li> 
</ol> 
<div> 
 <h2><strong style="color:#569cd6">classloader 命令支持统计实际使用URL和未使用的URL</strong></h2> 
</div> 
<p style="color:black; margin-left:0; margin-right:0">随着应用越来越复杂，依赖的jar包越来越多，我们想对应用做瘦身，但会有很多顾虑。因为不清楚哪些jar包是没被使用的😂。</p> 
<p style="color:black; margin-left:0; margin-right:0">因此，Arthas在<code>classloader</code>命令里增加URL使用统计功能，方便排除未使用jar包。</p> 
<p style="color:black; margin-left:0; margin-right:0">使用<code>--url-stat</code>参数，则会打印出所有ClassLoader的<code>Used URLs</code>和<code>Unused URLs</code>。</p> 
<pre><code>$ classloader --url-stat
 com.taobao.arthas.agent.ArthasClassloader@3c41660, hash:3c41660
 Used URLs:
 file:/Users/admin/.arthas/lib/3.5.6/arthas/arthas-core.jar
 Unused URLs:

 sun.misc.Launcher$AppClassLoader@75b84c92, hash:75b84c92
 Used URLs:
 file:/Users/admin/code/java/arthas/math-game/target/math-game.jar
 file:/Users/admin/.arthas/lib/3.5.6/arthas/arthas-agent.jar
 Unused URLs:

 sun.misc.Launcher$ExtClassLoader@7f31245a, hash:7f31245a
 Used URLs:
 file:/tmp/jdk1.8/Contents/Home/jre/lib/ext/sunec.jar
 file:/tmp/jdk1.8/Contents/Home/jre/lib/ext/sunjce_provider.jar
 file:/tmp/jdk1.8/Contents/Home/jre/lib/ext/localedata.jar
 Unused URLs:
 file:/tmp/jdk1.8/Contents/Home/jre/lib/ext/nashorn.jar
 file:/tmp/jdk1.8/Contents/Home/jre/lib/ext/cldrdata.jar
...
</code></pre> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">注意，基于JVM目前已加载的所有类统计，不代表Unused URLs可以从应用中删掉。因为可能将来需要从Unused URLs里加载类，或者需要加载resources。</p> 
</blockquote> 
<div> 
 <h2><strong style="color:#569cd6">memory命令</strong></h2> 
</div> 
<ul style="list-style-type:disc"> 
 <li> <p>https://arthas.aliyun.com/doc/memory.html</p> </li> 
</ul> 
<p style="color:black; margin-left:0; margin-right:0"><code>memory</code>命令可以查看JVM内存信息。 因为之前使用<code>dashboard</code>命令查看内存信息时，因为窗口有限，输出可能被截断，因此提供单独的<code>memory</code>命令。</p> 
<pre><code>$ memory
Memory                           used      total      max        usage
heap                             32M       256M       4096M      0.79%
g1_eden_space                    11M       68M        -1         16.18%
g1_old_gen                       17M       184M       4096M      0.43%
g1_survivor_space                4M        4M         -1         100.00%
nonheap                          35M       39M        -1         89.55%
codeheap_'non-nmethods'          1M        2M         5M         20.53%
metaspace                        26M       27M        -1         96.88%
codeheap_'profiled_nmethods'     4M        4M         117M       3.57%
compressed_class_space           2M        3M         1024M      0.29%
codeheap_'non-profiled_nmethods' 685K      2496K      120032K    0.57%
mapped                           0K        0K         -          0.00%
direct                           48M       48M        -          100.00%
</code></pre> 
<div> 
 <h2><strong style="color:#569cd6">恢复对 enum 类增强支持，过滤掉的类在日志中打印具体原因</strong></h2> 
</div> 
<p style="color:black; margin-left:0; margin-right:0">当我们尝试watch java package里的类时：</p> 
<pre><code>watch java.util.concurrent.TimeUnit convert
</code></pre> 
<p style="color:black; margin-left:0; margin-right:0">在<code>~/logs/arthas/arthas.log</code>里会打印具体原因：</p> 
<pre><code>2022-03-01 22:31:55 [arthas-command-execute] INFO  c.t.arthas.core.advisor.Enhancer 
-ignore class: java.util.concurrent.TimeUnit, 
reson: class loaded by Bootstrap Classloader, 
try to execute `options unsafe true`
</code></pre> 
<p style="color:black; margin-left:0; margin-right:0">如果按提示执行<code>options unsafe true</code>，则可以成功watch。</p> 
<div> 
 <h2><strong style="color:#569cd6">总结</strong></h2> 
</div> 
<ul style="list-style-type:disc"> 
 <li> <p>classloader wiki: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farthas.aliyun.com%2Fdoc%2Fclassloader.html" target="_blank">https://arthas.aliyun.com/doc/classloader.html</a></p> </li> 
 <li> <p>memory wiki: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farthas.aliyun.com%2Fdoc%2Fmemory.html" target="_blank">https://arthas.aliyun.com/doc/memory.html</a></p> </li> 
 <li> <p>Release 日志: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Farthas%2Freleases%2Ftag%2Farthas-all-3.5.6" target="_blank">https://github.com/alibaba/arthas/releases/tag/arthas-all-3.5.6</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            