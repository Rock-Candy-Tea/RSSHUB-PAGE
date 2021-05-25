
---
title: 'SeaweedFS 2.49 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8990'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8990'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.49 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>FUSE Mount 
  <ul> 
   <li>支持多个文件管理器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2015" target="_blank">#2015</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1531" target="_blank">#1531</a></li> 
  </ul> </li> 
 <li>Filer 
  <ul> 
   <li>如果出现传输错误，接收 grpc 连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2070" target="_blank">#2070</a></li> 
   <li>在 master 暂时失去连接的情况下进行等待</li> 
   <li>从 peer filer 中启动 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F1861" target="_blank">#1861</a></li> 
  </ul> </li> 
 <li>Master 
  <ul> 
   <li>避免当节点与父节点断开连接时可能出现的 nil <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2073" target="_blank">#2073</a></li> 
  </ul> </li> 
 <li>S3 
  <ul> 
   <li>如果请求被签名但没有设置认证，则增加错误。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2075" target="_blank">#2075</a></li> 
   <li>废除 filer.options.buckets_fsync，使用特定路径的配置代替</li> 
  </ul> </li> 
 <li>Java Client 1.6.6 
  <ul> 
   <li>修复复制设置未传递给文件管理器的问题 </li> 
   <li>assign 失败时引发异常</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.49" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.49</a></p>
                                        </div>
                                      
</div>
            