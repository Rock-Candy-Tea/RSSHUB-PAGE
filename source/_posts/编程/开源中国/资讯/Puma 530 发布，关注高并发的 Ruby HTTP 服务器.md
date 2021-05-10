
---
title: 'Puma 5.3.0 发布，关注高并发的 Ruby HTTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4155'
author: 开源中国
comments: false
date: Mon, 10 May 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4155'
---

<div>   
<div class="content">
                                                                                            <p>Puma 是一个简单、快速、线程化并且关注高并发的 HTTP 1.1 服务器，适用于开发和生产中的 Ruby/Rack 应用。</p> 
<p>Puma 5.3.0 正式发布，该版本更新内容如下：</p> 
<p>特性：</p> 
<ul> 
 <li>增加对 Linux 抽象套接字的支持 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2564" target="_blank">#2564</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2526" target="_blank">#2526</a>])</li> 
 <li>增加对 worker 超时和启动的调试 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2559" target="_blank">#2559</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2528" target="_blank">#2528</a>])</li> 
 <li>运行 one-worker 集群时打印警告 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2565" target="_blank">#2565</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2534" target="_blank">#2534</a>])</li> 
 <li>pumactl 重启时不关闭 systemd 激活的套接字 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2563" target="_blank">#2563</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2504" target="_blank">#2504</a>])</li> 
</ul> 
<p>Bug 修复：</p> 
<ul> 
 <li>systemd - 修复事件触发 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2591" target="_blank">#2591</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2572" target="_blank">#2572</a>])</li> 
 <li>立即解除临时文件的链接 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2613" target="_blank">#2613</a>])</li> 
 <li>改进对 HTTP_HOST header 的解析 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2605" target="_blank">#2605</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2584" target="_blank">#2584</a>])</li> 
 <li>处理没有回溯的重大错误 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2607" target="_blank">#2607</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2552" target="_blank">#2552</a>])</li> 
 <li>修复过早退出请求的问题 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2606" target="_blank">#2606</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2574" target="_blank">#2574</a>])</li> 
 <li>处理 Ruby 2.6.6 中关于线程位置的 segfault ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2567" target="_blank">#2567</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2566" target="_blank">#2566</a>])</li> 
 <li>在正确的地方定义 UNPACK_TCP_STATE_FROM_TCP_INFO ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2588" target="_blank">#2588</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2556" target="_blank">#2556</a>])</li> 
 <li>request.rb - 修复不兼容的 ascii 编码的 chunked assembly ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2585" target="_blank">#2585</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2583" target="_blank">#2583</a>])</li> 
</ul> 
<p>性能：</p> 
<ul> 
 <li>只在设置了 remote_addr_header 的情况下重置 peerip ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2609" target="_blank">#2609</a>])</li> 
 <li>减少 puma_parser 结构的大小 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2590" target="_blank">#2590</a>])</li> 
</ul> 
<p>重构：</p> 
<ul> 
 <li>重构关闭时的资源消耗 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2600" target="_blank">#2600</a>])</li> 
 <li>对 wait_for_less_busy_worker 功能进行微优化 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2579" target="_blank">#2579</a>])</li> 
 <li>大量的测试修复</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Freleases%2Ftag%2Fv5.3.0" target="_blank">https://github.com/puma/puma/releases/tag/v5.3.0</a></p>
                                        </div>
                                      
</div>
            