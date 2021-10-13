
---
title: 'IPFire 2.27 Core 160 发布，即将移除 Python 2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3415'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 06:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3415'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">IPFire 是一个开源 Linux 发行版，主要用于路由器和防火墙；具有一个独立的防火墙系统，带有基于 Web 的管理控制台进行配置，它支持安装附加组件以添加更多服务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">IPFire 2.27 Core 160 正式发布，它带有大量的 bug 修复和软件包更新，并为删除 Python 2 做准备。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">提高网络吞吐量</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">IPFire 团队的目标是提高硬件的吞吐量、降低延迟，以实现更快的网络。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这次更新带来了第一个变化，它将使支持它的网络接口能够将属于同一数据流的数据包发送到同一个处理器核心。这允许利用更好的缓存局部性和防火墙引擎以及入侵防御系统从中受益，尤其是在连接数量较多及 CPU 缓存较小的硬件上。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此功能会在支持它的硬件上自动启用。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">准备移除 Python 2</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Python 2 已经在 2021 年 1 月 1 日达到了 EOL。在过去的几个月，IPFire 团队已经将代码转移到了 Python 3，并在这次更新中完成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">然而，Python 2 仍然存在于发行版中，供所有仍需移植自定义脚本的用户使用。在下一次 Core 更新中将正式移除 Python 2。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在防火墙引擎中，增加了对重定向服务的支持，并修复了长期存在的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugzilla.ipfire.org%2Fshow_bug.cgi%3Fid%3D12265" target="_blank">＃12265</a><span> </span>错误</li> 
 <li>修复了 IPsec VPN 脚本中的一些错误，这些错误使用户无法创建基于证书的连接</li> 
 <li>网络代理现在可以在没有 GREEN 网络的系统上使用</li> 
 <li>防火墙日志查看器现在显示 IP 协议名称而不是数字</li> 
 <li>所有的图表现在都是以 SVG 格式呈现的，这使得在浏览器中的任何缩放都更加顺畅</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.ipfire.org%2Fpost%2Fipfire-2-27-core-update-160-released" target="_blank">https://blog.ipfire.org/post/ipfire-2-27-core-update-160-release</a></p>
                                        </div>
                                      
</div>
            