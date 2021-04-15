
---
title: 'X.Org Server 1.20.11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-22d9d69d73e5b3992e020c92afd55f4f559.png'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 07:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-22d9d69d73e5b3992e020c92afd55f4f559.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>X.Org Server 因被趋势科技再度发现存在安全问题，不得不发布了一个小版本更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fxorg%2F2021-April%2F060678.html" target="_blank">1.20.11</a> 进行修复。</p> 
<p><img height="360" src="https://oscimg.oschina.net/oscnet/up-22d9d69d73e5b3992e020c92afd55f4f559.png" width="785" referrerpolicy="no-referrer"></p> 
<p>趋势科技安全研究人员发现，X.Org Server 的 X Input 扩展输入验证存在缺陷，最终可能导致已被授权的客户端获得权限升级。据介绍，CVE-2021-3472 对 X Input 请求长度检查不充分，可能导致 X.Org Server 中的内存访问超出范围。如果 X.Org Server 以特权权限运行，那么可能会导致被授权的 X11 客户端获得权限提升。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.freedesktop.org%2Fxorg%2Fxserver%2F-%2Fcommit%2F7aaf54a1884f71dc363f0b884e57bcb67407a6cd" target="_blank">此补丁</a>修复了 XChangeFeedbackControl() 请求下溢问题，一同发布的还有其他累积的补丁。</p> 
<p>X.Org Server 1.20.11 主要由许多向后移植的 XQuartz 修复程序、依赖于 DRI2 的 KMS Meson 构建修复程序以及其他修复程序组成，详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fxorg%2F2021-April%2F060678.html" target="_blank">Changelog</a>。</p> 
<p>不过官方仍没透露关于下一个大版本 X.Org Server 1.21 的任何消息，或许真如外界所言，不会再发布。与此同时，XWayland 独立工作仍在继续，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fxorg%2F2021-April%2F060679.html" target="_blank">XWayland 21.1.1</a> 也在近日发布了此 X Input 的安全修复程序。</p>
                                        </div>
                                      
</div>
            