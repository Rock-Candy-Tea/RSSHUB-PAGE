
---
title: 'XWayland 22.1.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8156'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8156'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/news/182796/xwayland-22-1-released">XWayland 22.1 </a>已发布了一个多月，近日推出的补丁更新 22.1.1 修复了自发布以来的多个错误。</p> 
<p>主要包括：</p> 
<ul> 
 <li>在无根模式下运行时，默认情况下不映射复合覆盖窗口。这是因为客户端试图获取 COW 时，X Server 将会映射窗口并阻止所有指针事件。</li> 
 <li>由于某些 Vulkan 游戏/应用程序在窗口模式下运行仅以 58 FPS 运行，而实际上是以 60 FPS 来匹配 60Hz 的刷新率，这是因为不正确的计算处理导致 MSC 以 ~58Hz 的速度运行。因此该版本对 XWayland 现在的队列代码进行了修改。</li> 
 <li> <p>修复 use-after-free 错误</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.x.org%2Farchives%2Fxorg%2F2022-March%2F060943.html" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            