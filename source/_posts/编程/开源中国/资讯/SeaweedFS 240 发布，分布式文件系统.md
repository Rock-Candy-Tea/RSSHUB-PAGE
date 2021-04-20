
---
title: 'SeaweedFS 2.40 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4126'
author: 开源中国
comments: false
date: Tue, 20 Apr 2021 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4126'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.40 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>FUSE mount 
  <ul> 
   <li>内存使用效率更高</li> 
  </ul> </li> 
 <li>Bugs 
  <ul> 
   <li>volumeServer.evacuate 匀速运动<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1990" target="_blank">＃1990</a></li> 
   <li>volume.check.disk 跳过只读卷循环<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2002" target="_blank">＃2002</a></li> 
   <li>volume.tier.move：当目标卷服务器已经具有卷时，避免数据丢失<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2001" target="_blank">＃2001</a></li> 
   <li>避免循环使用音量分配替代请求<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fdiscussions%2F1996" target="_blank">＃1996</a></li> 
   <li><code>weed shell</code>返回终端正确<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1995" target="_blank">＃1995</a></li> 
   <li>filer pload 到一个没有"/"后缀的目录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1988" target="_blank">＃1988</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.40" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.40</a></p>
                                        </div>
                                      
</div>
            