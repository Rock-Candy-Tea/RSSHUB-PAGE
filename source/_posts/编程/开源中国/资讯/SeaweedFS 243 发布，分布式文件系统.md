
---
title: 'SeaweedFS 2.43 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9147'
author: 开源中国
comments: false
date: Tue, 04 May 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9147'
---

<div>   
<div class="content">
                                                                                            <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.43 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>FUSE Mount 
  <ul> 
   <li>修复多个装载之间数据不一致的回归问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2038" target="_blank">＃2038</a></li> 
   <li>处理随机读取更有效地利用内存<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2037" target="_blank">＃2037</a></li> 
  </ul> </li> 
 <li>S3 
  <ul> 
   <li>授权使用 bucket wild cards<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2030" target="_blank">＃2030</a></li> 
  </ul> </li> 
 <li>Minor 
  <ul> 
   <li>Volume server：<code>-minFreeSpace</code>option 支持特定的可用空间大小<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2025" target="_blank">＃2025</a></li> 
   <li>不要在 brotlii archives<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2031" target="_blank">＃2031</a> 和 rar 文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2032" target="_blank">＃2032</a> 上进行压缩</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.43" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.43</a></p>
                                        </div>
                                      
</div>
            