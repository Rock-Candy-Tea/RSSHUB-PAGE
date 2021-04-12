
---
title: 'aio-enhance v1.0.4 发布，Java AIO 内核增强类库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202010/10095334_KIce.png'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 09:46:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202010/10095334_KIce.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">aio-enhance 是一款无侵入式的 <strong>Java AIO 内核增强类库</strong>（<em><strong>注意：这不是一款通信框架</strong></em>），解决原生 AIO 架构设计中存在的缺陷，提供更高效、更稳定的通信能力。</p> 
<p style="text-align:start">aio-enhance 采用了 NIO 技术实现了一套全新的异步 IO 模型，兼容完整的 Java AIO 接口。用户可自由选择 Java 原生提供的，或者 aio-enhance 增强的 AIO 实现，架构如下图。</p> 
<p style="text-align:start"><img alt src="https://static.oschina.net/uploads/img/202010/10095334_KIce.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">一、项目背景</h2> 
<p style="text-align:start"><strong>2.1 解决平台兼容性问题。</strong></p> 
<p style="text-align:start">Java 原生 AIO 在 Mac 操作系统下存在兼容性问题，进行性能压测会偶发性的系统崩溃。</p> 
<p style="text-align:start"><strong>2.2 修复官方 AIO 架构缺陷</strong></p> 
<p style="text-align:start">Java 原生 AIO 在底层架构设计上存在缺陷（参考：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopenjdk.java.net%2Fprojects%2Fnio%2Fresources%2FAsynchronousIo.html" target="_blank">Java AIO通信模型</a>）。多核 CPU 环境下处理高并发请求，会引发比较严重的锁竞争现象，以致无法充分发挥机器性能。</p> 
<p style="text-align:start">普通4核机器竞争压力不大，AIO 的运行表现实测优于NIO。但随着 CPU 核数的增加，AIO 的性能优势逐渐下降。</p> 
<p style="text-align:start"><strong>2.3 优化 AIO 线程模型</strong></p> 
<p style="text-align:start">Java AIO 相较于 NIO 多了一层异步线程模型，极大降低了开发人员的编程难度。但是通信过程中的 accept、connect、read、write 等事件都是复用同一组线程资源，容易造成读写回调进入<strong>死锁状态</strong>。 AIO通信框架在设计上需要特别关注这一点，但如果引入 aio-enhance 则无此顾虑。</p> 
<h2 style="text-align:start">二、适用场景</h2> 
<p style="text-align:start">如果您符合以下几个条件，aio-enhance 会是一个不错的选择。</p> 
<ul> 
 <li>任何基于 Java AIO 实现的通信框架，如：<a href="https://gitee.com/smartboot/smart-socket">smart-socket</a>；</li> 
 <li>对高并发实时性有严苛要求；</li> 
 <li>多核CPU环境（至少4核以上）</li> 
</ul> 
<h2 style="text-align:start">三、集成</h2> 
<p style="text-align:start"><strong>步骤一：依赖</strong></p> 
<p style="text-align:start">引入增强包：aio-enhance.jar。可以通过maven方式引入依赖，亦可直接下载 jar 包并导入classpath。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>org.smartboot.aio<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>aio-enhance<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>1.0.4<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></span></pre> 
 </div> 
</div> 
<p style="text-align:start"><strong>步骤二：启动</strong></p> 
<p style="text-align:start">可以通过硬编码的方式设置系统属性，如下：</p> 
<div style="text-align:start"> 
 <div> 
  <pre><strong><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">System</span></span></span></strong><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.</span></span></span><span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">setProperty</span></span></span></span>(<span style="color:#dd2200">"<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">java</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.nio</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.channels</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.spi</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.AsynchronousChannelProvider</span></span></span>"</span>, <span style="color:#dd2200">"<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">org</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.smartboot</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.aio</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.EnhanceAsynchronousChannelProvider</span></span></span>"</span>);</pre> 
 </div> 
</div> 
<p style="text-align:start">也可在 java 启动命令行中设置，如下：</p> 
<div style="text-align:start"> 
 <div> 
  <pre><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">java</span></span></span> <span style="color:#000080"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">-Djava</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">.nio.channels.spi.AsynchronousChannelProvider=org.smartboot.aio.EnhanceAsynchronousChann</span></span></span></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            