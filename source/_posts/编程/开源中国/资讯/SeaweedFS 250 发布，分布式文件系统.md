
---
title: 'SeaweedFS 2.50 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6166'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6166'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</p> 
<p>目前，SeaweedFS 2.50 已发布，该版本更新内容如下：</p> 
<ul> 
 <li>Fuse Mount 
  <ul> 
   <li>添加 fuse 子命令以将 weed 与 mount 一起使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2085" target="_blank">#2085 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2099" target="_blank">#2099</a></li> 
  </ul> </li> 
 <li>Filer Store  
  <ul> 
   <li>支持 sqlite 作为 filer meta store</li> 
  </ul> </li> 
 <li>Filer.bacup 
  <ul> 
   <li>备份到本地目录，可选择增量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2084" target="_blank">#2084</a></li> 
   <li>从 Windows 上的路径转义冒号 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2084" target="_blank">#2084</a></li> 
  </ul> </li> 
 <li>S3 
  <ul> 
   <li>对象写缓存控制和过期 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2079" target="_blank">#2079</a></li> 
   <li>使用 If-Match 获取对象：bogus ETag <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2080" target="_blank">#2080</a></li> 
   <li>修复在 put-object 过程中保存元数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2092" target="_blank">#2092</a></li> 
  </ul> </li> 
 <li>Minor 
  <ul> 
   <li>如果错误太多，则重新创建 grpc 连接<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F2098" target="_blank">#2098</a></li> 
   <li><code>weed server</code> 修复自由空间参数</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F2.50" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/2.50</a> </p>
                                        </div>
                                      
</div>
            