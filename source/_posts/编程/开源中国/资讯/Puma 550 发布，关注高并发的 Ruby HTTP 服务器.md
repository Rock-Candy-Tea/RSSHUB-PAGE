
---
title: 'Puma 5.5.0 发布，关注高并发的 Ruby HTTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1076'
author: 开源中国
comments: false
date: Sun, 26 Sep 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1076'
---

<div>   
<div class="content">
                                                                                            <p>Puma 是一个简单、快速、线程化并且关注高并发的 HTTP 1.1 服务器，适用于开发和生产中的 Ruby/Rack 应用。</p> 
<p>Puma 5.5.0 正式发布，该版本更新内容如下：</p> 
<ul> 
 <li>功能 
  <ul> 
   <li>通过 <code>[localhost]()</code> gem，为 localhost 自动提供 SSL 证书 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2610" target="_blank">#2610</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2257" target="_blank">#2257</a>])</li> 
   <li>增加对 PROXY 协议的支持（仅 v1）([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2654" target="_blank">#2654</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2651" target="_blank">#2651</a>])</li> 
   <li>为 <code>-no-config</code> 文件增加一个语义上的 CLI 选项 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2689" target="_blank">#2689</a>])</li> 
  </ul> </li> 
 <li>错误修正 
  <ul> 
   <li>更详细的异常处理 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2700" target="_blank">#2700</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2699" target="_blank">#2699</a>])</li> 
   <li>允许多个 after_worker_fork hooks ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2690" target="_blank">#2690</a>])</li> 
   <li>在 worker fork 上保留 BUNDLE_APP_CONFIG ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2688" target="_blank">#2688</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2687" target="_blank">#2687</a>])</li> 
  </ul> </li> 
 <li>性能 
  <ul> 
   <li>修复服务器端 SSL 连接关闭的性能问题 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2675" target="_blank">#2675</a>])</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Freleases%2Ftag%2Fv5.5.0" target="_blank">https://github.com/puma/puma/releases/tag/v5.5.0</a></p>
                                        </div>
                                      
</div>
            