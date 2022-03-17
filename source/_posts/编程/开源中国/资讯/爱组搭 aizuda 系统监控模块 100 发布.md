
---
title: '爱组搭 aizuda 系统监控模块 1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5967'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 15:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5967'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">介绍</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">主要功能 操作系统 cpu 内存 jvm 系统 数据查询 等，该模块核心是集成oshi实现对服务器及应用的监控。</p> 
</blockquote> 
<p style="color:#004050; text-align:start">第三方组件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foshi%2Foshi" target="_blank">oshi</a> 是基于 JNA 的（本地）操作系统和硬件信息库。它不需要安装任何其他额外的本地库，旨在提供一种跨平台的实现来检索系统信息，例如操作系统版本、进程、内存和 CPU 使用率、磁盘和分区、设备、传感器等。</p> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F9xd041%2F%23%25E5%25AE%2589%25E8%25A3%2585" target="_blank">#</a>安装</h2> 
<ul> 
 <li>Maven</li> 
</ul> 
<div style="text-align:start"> 
 <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>dependency</span><span style="color:#999999">></span></span>
  <span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>groupId</span><span style="color:#999999">></span></span>com.aizuda<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>groupId</span><span style="color:#999999">></span></span>
  <span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>artifactId</span><span style="color:#999999">></span></span>aizuda-monitor<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>artifactId</span><span style="color:#999999">></span></span>
  <span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>version</span><span style="color:#999999">></span></span>1.0.0<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>version</span><span style="color:#999999">></span></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>dependency</span><span style="color:#999999">></span></span>
</code></pre> 
</div> 
<ul> 
 <li>Gradle</li> 
</ul> 
<div style="text-align:start"> 
 <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code>implementation 'com.aizuda:aizuda-monitor:1.0.0'
</code></pre> 
</div> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F9xd041%2F" target="_blank">#点击查看演示效果</a></h2>
                                        </div>
                                      
</div>
            