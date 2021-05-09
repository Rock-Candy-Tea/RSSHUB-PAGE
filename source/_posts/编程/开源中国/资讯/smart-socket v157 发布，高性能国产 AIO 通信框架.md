
---
title: 'smart-socket v1.5.7 发布，高性能国产 AIO 通信框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fdfa7f3f0daddc72e5fff198806e0fad2c6.png'
author: 开源中国
comments: false
date: Sun, 09 May 2021 08:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fdfa7f3f0daddc72e5fff198806e0fad2c6.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:justify">smart-socket 是一个 AIO 通信框架，可以快速、轻松地开发 Client/Server 网络应用程序。它大大简化了网络编程难度和复杂度，可广泛应用与各类TCP/UDP的通信场景。</p> 
<ol> 
</ol> 
<p style="text-align:justify">smart-socket 是从许多协议（Http、WebSocket、MQTT、二进制私有协议）的实践中积累了大量宝贵经验，从而凝练成了一款极简、易用、高性能的通信框架。</p> 
<p style="text-align:left"><strong>极简</strong></p> 
<ul> 
 <li>支持各种传输类型、协议，且仅围绕着两大核心接口（MessageProcessor、Protocol）编程开发。</li> 
 <li>灵活且可扩展的状态机设计，可以清晰地分离关注点。</li> 
 <li>核心包代码 1478 行，编译后的 jar 包仅 41 KB（如果对此无明显感触，可以比较其他同类项目）。</li> 
</ul> 
<p style="text-align:left"><strong>易用</strong></p> 
<ul> 
 <li>文档丰富的 Javadoc 、用户指南和示例。</li> 
 <li>没有额外的依赖，只要求JDK 8及以上版本。</li> 
 <li>高度可定制化的插件。已内置一些非常实用且开箱即用的插件：<span style="background-color:#ffffff; color:#40485b">SSL/TLS通信、心跳、断链重连、服务指标统计、黑名单、内存池监测</span>。</li> 
</ul> 
<p style="text-align:left"><strong>高性能</strong></p> 
<ul> 
 <li>更好的吞吐量，更低的延迟</li> 
 <li>更少的资源消耗</li> 
 <li>最尽肯能减少不必要的内存拷贝</li> 
</ul> 
<h4 style="text-align:justify">更新内容</h4> 
<ol> 
 <li>优化：移除共享内存页，简化内存池设计。</li> 
 <li>优化：AioQuickClient 新增方法 getSession，便于获取连接会话对象。</li> 
 <li>优化：重构 ConcurrentReadCompletionHandler 守护线程逻辑。</li> 
 <li>优化：移除 IOUtil#close 方法中的判空校验。</li> 
 <li>优化：重构 WriteBuffer，采用读写分离锁，提升 IO 效率。</li> 
 <li>新特性：新增解码器，FixedLengthBytesProtocol、ByteArrayProtocol、StringProtocol。</li> 
 <li>其他：新增 netty 示例，用于比对 smart-socket 和 netty 的通信能力。</li> 
</ol> 
<h4 style="text-align:left">性能表现</h4> 
<p><img height="1390" src="https://oscimg.oschina.net/oscnet/up-fdfa7f3f0daddc72e5fff198806e0fad2c6.png" width="2394" referrerpolicy="no-referrer"></p> 
<p><img height="1274" src="https://oscimg.oschina.net/oscnet/up-d8af49d7e7eea3fd6ad4433115563fabcc0.png" width="2364" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">Maven</h4> 
<pre style="text-align:left"><code><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>org.smartboot.socket<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>aio-core<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>1.5.7<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></code></pre>
                                        </div>
                                      
</div>
            