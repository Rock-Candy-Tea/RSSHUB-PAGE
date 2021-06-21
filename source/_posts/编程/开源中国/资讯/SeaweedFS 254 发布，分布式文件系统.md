
---
title: 'SeaweedFS 2.54 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=674'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=674'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.50 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>FUSE mount 
  <ul> 
   <li>修复 2.53 中引入的一个 deletion bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2138" target="_blank">#2138</a>。这会导致文件块实际上没有被删除，这可以通过在<code>weed shell</code>中运行<code>volume.fix</code>来修复。</li> 
   <li>如果文件被删除，则跳过刷新。这使 WinFsp 能够通过 sshfs 在 Windows 上挂载 SeaweedFS <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2110" target="_blank">#2110</a></li> 
  </ul> </li> 
 <li>Master 
  <ul> 
   <li>当一个 collection 被删除时，修复 stats</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.54" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.54</a></p>
                                        </div>
                                      
</div>
            