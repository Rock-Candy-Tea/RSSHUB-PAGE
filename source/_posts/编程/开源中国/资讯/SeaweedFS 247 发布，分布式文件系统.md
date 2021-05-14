
---
title: 'SeaweedFS 2.47 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2282'
author: 开源中国
comments: false
date: Fri, 14 May 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2282'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.47 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>Volume 
  <ul> 
   <li>提前 volume assignment <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2049" target="_blank">＃2049</a></li> 
   <li>添加 retry 以 assign volumes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2056" target="_blank">＃2056</a></li> 
  </ul> </li> 
 <li>FUSE Mount 
  <ul> 
   <li>上传前写入本地临时文件</li> 
  </ul> </li> 
 <li>Filer 
  <ul> 
   <li>删除特定标签<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2041" target="_blank">＃2041</a></li> 
   <li>修复错误的日志错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2051" target="_blank">＃2051</a></li> 
  </ul> </li> 
 <li>Shell 
  <ul> 
   <li>可选的并行复制 ec shards<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2048" target="_blank">＃2048</a></li> 
  </ul> </li> 
 <li>S3 
  <ul> 
   <li>如果 bucket 不存在，则返回 404 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2039" target="_blank">＃2039</a></li> 
  </ul> </li> 
 <li>Java Client 
  <ul> 
   <li>添加 exists() function</li> 
   <li>使 SeaweedInputStream 抛出 FileNotFoundException</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.47" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.47</a></p>
                                        </div>
                                      
</div>
            