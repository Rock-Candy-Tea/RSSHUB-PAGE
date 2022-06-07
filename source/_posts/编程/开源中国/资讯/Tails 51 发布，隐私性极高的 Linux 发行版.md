
---
title: 'Tails 5.1 发布，隐私性极高的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33e8ae4d6a9a53103688e73c0ca8c1b9953.png'
author: 开源中国
comments: false
date: Tue, 07 Jun 2022 07:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33e8ae4d6a9a53103688e73c0ca8c1b9953.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Tails 5.1 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftails.boum.org%2Fnews%2Fversion_5.1%2F" target="_blank">发布</a>，此版本修复了此前<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftails.boum.org%2Fsecurity%2Fprototype_pollution%2Findex.en.html" target="_blank">宣布</a>的 Firefox 和 Tor 浏览器的 JavaScript 引擎安全漏洞 ，并带来了一些功能更新。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更改和更新</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h1> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Tor 连接助手</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Tails 5.1 包括对 Tor 连接助手的许多改进：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li> <p><span>如果选择自动连接到 Tor ，Tor 连接助手会自动修复计算机时钟。</span></p> </li> 
 <li> <p>顶部导航中显示的时间，使用在 Tor Connection 助手中修复时钟时选择的时区。</p> </li> 
 <li>Tor 连接助手的最后一个屏幕会清楚地表明是否使用 Tor 桥接器进行连接。</li> 
</ul> 
<h2><img alt height="147" src="https://oscimg.oschina.net/oscnet/up-33e8ae4d6a9a53103688e73c0ca8c1b9953.png" width="400" referrerpolicy="no-referrer"></h2> 
<h2>不安全的浏览器和强制门户</h2> 
<ul> 
 <li>尚未连接到 Tor 网络时，为不安全的浏览器编写了一个新主页。</li> 
</ul> 
<p><img height="258" src="https://oscimg.oschina.net/oscnet/up-1698b6ca8aedd99de953d65b169512ea5bc.png" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>当欢迎屏幕中未启用<em>不安全浏览器</em>时，Tails 现在会在重新启动之前要求确认。</li> 
</ul> 
<p><img alt height="156" src="https://oscimg.oschina.net/oscnet/up-910f1b86c4e790e99f7d115b1aa3bd318ea.png" width="300" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>软件</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li> <p><span><em>将 tor </em>更新到 0.4.7.7。</span></p> </li> 
 <li> <p><span><em>将 Tor 浏览器 </em>更新到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.torproject.org%2Fnew-release-tor-browser-11014%2F" target="_blank">11.0.14</a>。</span></p> </li> 
 <li> <p><span><em>将 Thunderbird </em>更新到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.thunderbird.net%2Fen-US%2Fthunderbird%2F91.9.0%2Freleasenotes%2F" target="_blank">91.9</a>。</span></p> </li> 
 <li> <p><span><em>将 Linux </em>内核更新到 5.10.113。</span></p> </li> 
</ul> 
<h1>已修复的问题</h1> 
<ul> 
 <li> <p>从选项回滚时删除自动选择<strong>配置网桥选项，以隐藏正在连接到 Tor。</strong>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18546" target="_blank">#18546</a> )</p> </li> 
 <li> <p><span>在必须配置网桥的两个屏幕上给出相同的说明。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18596" target="_blank">#18596</a> )</span></p> </li> 
 <li> <p><span>帮助重命名默认的<em>KeePassXC</em>数据库以在将来自动打开它。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18966" target="_blank">#18966</a> )</span></p> </li> 
 <li> <p><span><em>修复使用文件</em>浏览器中的<em>OnionShare</em>共享文件。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18990" target="_blank">#18990</a> )</span></p> </li> 
 <li> <p><span>在活动概览中禁用搜索提供程序：文件、计算器和终端。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fissues%2F18952" target="_blank">#18952</a>）</span></p> </li> 
</ul> 
<p> </p> 
<p>有关更多详细信息，请阅读<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.tails.boum.org%2Ftails%2Ftails%2F-%2Fblob%2Fmaster%2Fdebian%2Fchangelog" target="_blank">变更日志</a>。</p> 
<p> </p> 
<h2>关于 Tails</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Tails（"The Amnesic Incognito Live System" 的缩写）是一个十分注重 “隐私性” 和 “隐匿性” 的 Linux 发行版，它衍生自 Debian，设计之初就是帮助用户匿名使用互联网，并最大限度保护个人隐私。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为达到此目标，Tails 使用了 Tor 网络，使得网络流量很难被追踪。Tails 还预装了一些应用，包括网页浏览器、IRC 客户端、邮件客户端、即时消息通信工具，它们都以安全为理念进行了预配置，并对网络流量进行了匿名性处理。因此通过 Tails 我们可以不留下任何痕迹 “隐身” 地使用互联网。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="392" src="https://static.oschina.net/uploads/space/2020/0408/074646_R9PC_3820517.png" width="700" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            