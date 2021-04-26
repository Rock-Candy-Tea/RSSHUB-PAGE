
---
title: 'SeaweedFS 2.41 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8179'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8179'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.41 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>FUSE mount 
  <ul> 
   <li>延迟新文件的创建，直到文件被关闭，除非文件被专门打开</li> 
  </ul> </li> 
 <li>Volume Server 
  <ul> 
   <li>Erasure Code: transient errors 可能会导致 thundering herd effect<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2012" target="_blank">＃2012</a></li> 
   <li>当 below minFreeSpacePercent 时，不要添加新的 volumes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2017" target="_blank">＃2017</a></li> 
  </ul> </li> 
 <li>Filer 
  <ul> 
   <li>删除文件夹时，Mysql/Postgres 数据库中可能有一些遗留条目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2006" target="_blank">＃2006</a></li> 
  </ul> </li> 
 <li>Minor 
  <ul> 
   <li>Filer 目录列表增加了<code>namePatternExclude</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2023" target="_blank">＃2023</a></li> 
   <li>Filer 目录列表可确保在检查名称模式时区分大小写</li> 
   <li><code>weed shell</code> lock 显示哪个服务器 holds the lock<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1983" target="_blank">＃1983</a></li> 
   <li><code>weed filer.copy</code>包含空文件夹<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2016" target="_blank">＃2016</a></li> 
   <li>volume server 正确报告错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2012" target="_blank">＃2012</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.41" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.41</a></p>
                                        </div>
                                      
</div>
            