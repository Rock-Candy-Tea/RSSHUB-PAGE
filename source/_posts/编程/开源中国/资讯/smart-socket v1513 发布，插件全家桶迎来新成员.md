
---
title: 'smart-socket v1.5.13 发布，插件全家桶迎来新成员'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-df0fe24bb7e0abe28569190b10199e3f9d4.png'
author: 开源中国
comments: false
date: Mon, 25 Oct 2021 09:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-df0fe24bb7e0abe28569190b10199e3f9d4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img height="651" src="https://oscimg.oschina.net/oscnet/up-df0fe24bb7e0abe28569190b10199e3f9d4.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">smart-socket v1.5.13 版本除了一些细节优化，最大的亮点莫过于插件全家桶迎来了一位重磅级新成员：RateLimiterPlugin（流控插件）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">流控，在很多场景下是一项刚性需求。目前市面上所见的绝大多数流控方案都是 QPS 维度的，即限制单位时间内的请求/响应<strong>次数</strong>。而 smart-socket 本次发布的流控插件却比较与众不同，我们提供的是针对字节码的流量控制能力，实现了网络上下行流量的限速。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">产生出研发流控插件的想法缘于一次线上故障，当时某个业务的网络 IO 流量剧增，消耗了过多资源以致其他请求出现严重超时。由此使我意识到基于 QPS 限流策略的局限性，不仅仅是高并发会冲击系统的稳定性，<strong>低并发高流量</strong>也是个不容忽视的存在。尤其在分布式环境下，单节点的故障会引发一系列连锁反应。而要防止个别网络通道无节制的消耗 IO 资源，则需要将流量限速在安全范围内。</p> 
<p><img height="582" src="https://oscimg.oschina.net/oscnet/up-3f523782b776440e396eac2cc6bc88051c3.png" width="786" referrerpolicy="no-referrer"></p> 
<p>流控功能的实现原理是通过代理技术拦截了 Java 通信对象 AsynchronousSocketChannel 的 read/write 方法，识别出超负荷的 IO 任务并延迟至一下个窗口期执行（<em><span>具体实现参见仓库源码</span></em>）。</p> 
<p>启用该插件延续着 smart-socket 插件一贯的开箱即用的风格，只需在构造方法中指定 read 和 write 的流控值（单位：byte），输入 0 表示不限流。</p> 
<blockquote> 
 <p><code><span>processor.addPlugin(<span style="color:#ca7d37">new</span> RateLimiterPlugin<>(<span style="color:#0e9ce5">1024</span> * <span style="color:#0e9ce5">1024</span>, <span style="color:#0e9ce5">1024</span> * <span style="color:#0e9ce5">1024</span>))</span></code></p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">运行效果如下图：（<span style="color:#888888">10个客户端发送消息，每隔5秒钟打印一次</span>）</p> 
<p><img height="575" src="https://oscimg.oschina.net/oscnet/up-f84f71ee1136be62c465e068212272789dd.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:justify"><em><span style="color:#000000"><em><span style="color:#000000">完整示例代码 RateLimiterDemo 可从 smart-socket 仓库中获取。</span></em></span></em></p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff6827">更新内容</span></strong></h1> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">优化 WriteBuffer#write 算法。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">调整底层IO调度线程名。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">移除底层默认的 tcoNoDelay 设定。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增流控插件：<span style="color:#000000">RateLimiterPlugin。</span></p> </li> 
</ol> 
<ol start="3" style="margin-left:0; margin-right:0"> 
</ol> 
<h1 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff6827">maven坐标</span></strong></h1> 
<pre><code class="language-xml"><dependency>
    <groupId>org.smartboot.socketgroupId>
    <artifactId>aio-coreartifactId>
    <version>1.5.13version>
dependency></code></pre> 
<ul style="list-style-type:none; margin-left:0; margin-right:0"> 
</ul> 
<h1 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff6827">最后</span></strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">开源不易，若觉得该项目还不错，请为它点个 Star 。仓库地址：<a href="https://gitee.com/smartboot/smart-socket">https://gitee.com/smartboot/smart-socket</a></p>
                                        </div>
                                      
</div>
            