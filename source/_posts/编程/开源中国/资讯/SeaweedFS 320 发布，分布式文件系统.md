
---
title: 'SeaweedFS 3.2.0 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1145'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1145'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">目前 </span>SeaweedFS 发布 3.2.0 版本，除了许多小修复外，<span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>还有两个主要改进：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>FUSE 支架越来越稳定。截断操作的过期修复使 SQLite 能够安全运行。</li> 
 <li><code>filer.sync</code>可以并行同步多个文件更改。（在修复之前，所有更改只能在目标文件管理器集群中一一应用）。</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更改日志：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">FUSE Mount</span> 
  <ul> 
   <li>修复 truncate 操作导致新文件较小时数据写入失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F2609" target="_blank">#2609 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F3384" target="_blank">#3384</a></li> 
   <li>修复硬链接的链接计数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F3386" target="_blank">#3386</a></li> 
   <li><code>df</code>当使用量接近限制时调整统计报告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F3407" target="_blank">#3407</a></li> 
   <li>修复检测随机读取模式的错误逻辑</li> 
  </ul> </li> 
 <li><code>filer.sync</code> 
  <ul> 
   <li>并行化从 1 到 128 个复制 goroutine 的同步。</li> 
   <li>修复主动-主动模式下的同步逻辑 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F3328" target="_blank">#3328</a></li> 
   <li>排除路径为空时修复</li> 
  </ul> </li> 
 <li>文件管理器 
  <ul> 
   <li>Filer 更喜欢同一数据中心中的卷服务器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fpull%2F3405" target="_blank">#3405</a></li> 
   <li>添加下载限速支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fpull%2F3408" target="_blank">#3408</a></li> 
  </ul> </li> 
 <li>Helm 图表 
  <ul> 
   <li>添加对 initContainers 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fpull%2F3399" target="_blank">#3399</a></li> 
   <li>其他监控改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fpull%2F3406" target="_blank">#3406</a></li> 
  </ul> </li> 
 <li>文件管理器商店 
  <ul> 
   <li>允许 postgresql 使用标准环境变量进行连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fpull%2F3413" target="_blank">#3413</a></li> 
  </ul> </li> 
 <li>Shell  
  <ul> 
   <li><code>filer.meta.load</code>添加安静模式，以减少详细输出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Fissues%2F3414" target="_blank">#3414</a></li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseaweedfs%2Fseaweedfs%2Freleases%2Ftag%2F3.20" target="_blank">https://github.com/seaweedfs/seaweedfs/releases/tag/3.20</a></p>
                                        </div>
                                      
</div>
            