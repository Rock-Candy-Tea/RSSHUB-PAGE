
---
title: 'Tails 4.22 发布，隐私性极高的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2552'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2552'
---

<div>   
<div class="content">
                                                                                            <p>在 Tails 4.22 更新中，主要专注于解决 Tor Connection 中出现的问题，以使其更加强大和易于使用。</p> 
<h2>变化和更新</h2> 
<p>包括软件和硬件支持</p> 
<ul> 
 <li>将 Tor Browser 更新到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.torproject.org%2Fnew-release-tor-browser-1056" target="_blank">10.5.6</a></li> 
 <li>将 Thunderbird 更新到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.thunderbird.net%2Fen-US%2Fthunderbird%2F78.13.0%2Freleasenotes%2F" target="_blank">78.13</a></li> 
 <li>将 AMD 显卡固件更新到 20210818，这应该会改善对部分型号 AMD 显卡的支持</li> 
</ul> 
<p>Tor Connection</p> 
<ul> 
 <li>修改自定义网桥接口，只允许进入 1 个网桥 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18550" target="_blank">#18550</a>) </li> 
 <li>允许在持久性存储中保存一个自定义网桥 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F5461" target="_blank">#5461</a>)</li> 
 <li>允许在使用网桥连接到 Tor 失败时手动修复时钟，(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F15548" target="_blank">#15548</a>) 这有助于来自伦敦东部的人们使用 obfs4 桥接器连接到 Tor，并使连接到 Tor 在总体上更加稳定</li> 
 <li>将决定我们是否能连接到 Tor 的超时时间从 30 秒减少到 10 秒。将完全启动 Tor 的超时时间从 120 秒增加到 600 秒。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18501" target="_blank">#18501</a>)</li> 
 <li>允许从错误屏幕上再次尝试连接到 Tor (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18539" target="_blank">#18539</a>)</li> 
</ul> 
<p>其他</p> 
<ul> 
 <li>确保自动升级是从一个工作镜像中下载的 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F15755" target="_blank">#15755</a>)</li> 
 <li>在 Tails 中包含的离线文档中添加俄语</li> 
</ul> 
<h2>修正的问题</h2> 
<p>Tor Connection</p> 
<ul> 
 <li>修复了使用默认网桥连接到 Tor 的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18462" target="_blank">#18462</a>)</li> 
 <li>当 Wi-Fi 设置被保存在持久性存储中时，修复连接到 Tor 的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18532" target="_blank">#18532</a>)</li> 
 <li>当 Tor Connection 到达错误屏幕时，停止在后台尝试连接到 Tor (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18740" target="_blank">#18740</a>)</li> 
</ul> 
<p>已知的问题</p> 
<p>这个版本没有特定的问题</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.torproject.org%2Fnew-release-tails-422" target="_blank">https://blog.torproject.org/new-release-tails-422</a></p>
                                        </div>
                                      
</div>
            