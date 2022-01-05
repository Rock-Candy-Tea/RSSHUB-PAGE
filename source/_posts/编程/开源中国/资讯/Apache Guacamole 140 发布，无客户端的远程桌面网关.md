
---
title: 'Apache Guacamole 1.4.0 发布，无客户端的远程桌面网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/072613_qFoN_4937141.png'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 07:26:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/072613_qFoN_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Guacamole 是一个无客户端的远程桌面网关。它支持标准协议，如 VNC、RDP 和 SSH。之所以称它为无客户端，因为它不需要插件或客户端软件。由于 HTML5 的存在，一旦 Guacamole 被安装在服务器上，你只需要一个网络浏览器就能访问你的桌面。</p> 
<p>1.4.0 版本的特点是支持连接平铺、在多个连接中广播键盘事件，以及使用加密和签名的 JSON 认证。对单点登录的支持得到了改进，增加了对 RDP 的多点触摸支持，并修复了对 RDP 音频输入支持的问题。</p> 
<p>1.4.0 版本与旧的 1.x 组件兼容。</p> 
<ul> 
 <li>为旧的 1.x 版本编写的扩展可以被 1.4.0 使用；</li> 
 <li>为较早的 1.x 版本所使用的 Guacamole 协议版本编写的组件可以与 1.4.0 版本的组件一起使用。</li> 
</ul> 
<h3>连接平铺和键盘广播</h3> 
<p>多个连接现在可以在同一个浏览器标签中同时显示，并自动排列成一个均匀的平铺布局。</p> 
<p><img alt height="361" src="https://static.oschina.net/uploads/space/2022/0105/072613_qFoN_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>当前聚焦的连接由一个蓝色边框表示，用户可以选择同时聚焦任何数量的这些平铺连接。如果有多个连接被聚焦，键盘交互会在每个连接中进行广播。</p> 
<h3>对 RDP 音频输入支持的主要修复</h3> 
<p>根据远程桌面中使用的应用程序，Guacamole 对 RDP 的音频输入支持存在与音频缓冲区行为和大小变化相关的质量问题。如果应用程序使用的音频后端不能调整偶尔爆破的音频数据包，远程桌面收到的任何音频数据包如果超过了剩余的缓冲区空间，就会被丢弃，导致可听到的“咔嚓声”比预期更快的播放。</p> 
<p>这一点现在已经得到修复。Guacamole 将自动节制其发送至远程桌面的数据量，以避免耗尽远程缓冲空间，确保远程桌面内的应用程序收到的音频与 Guacamole 通过浏览器收到的音频相同。</p> 
<h3>RDP 支持多点触摸事件</h3> 
<p>除了 Guacamole 对模拟触摸设备上的鼠标的既定支持外，在支持和启用的情况下，现在可以将多点触摸事件传递给远程桌面服务器。</p> 
<p>RDP 通过其 "RDPEI" 通道支持多点触摸。如果在 Guacamole RDP 连接上启用了触摸功能，与 Guacamole 显示器的触摸交互将直接影响远程桌面会话中支持触摸的应用程序，而不是被转化为鼠标事件。</p> 
<h3>支持辅助 SSO 供应商</h3> 
<p>Guacamole 对单点登录的支持历来都是全有或全无的，要么所有用户都使用 SSO 进行认证，要么根本没有。现在的情况不再是这样了。Guacamole 现在可以被配置为除了 SSO 之外还允许正常的用户名/密码认证，并且可以同时使用多个 SSO 供应商。</p> 
<p>SSO 认证扩展是否对所有用户自动生效，取决于该扩展是否有优先权，现在可以使用 <code>extension-priority</code> 属性来定义。</p> 
<h3>支持用加密、签名的 JSON 进行认证</h3> 
<p>“guacamole-auth-json" 认证扩展，以前是由 Glyptodon 维护的第三方项目，现在已经作为该项目自己的扩展被带入 Apache Guacamole。</p> 
<p>guacamole-auth-json 允许外部软件用一个加密和签名的 JSON 文档自动验证和授权用户。只要收到的 JSON 没有过期，并且用正确的密钥进行了加密和签名，它就被接受为充分的验证，即用户被授权访问该 JSON 描述的资源。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fguacamole.apache.org%2Freleases%2F1.4.0%2F" target="_blank">https://guacamole.apache.org/releases/1.4.0/</a></p>
                                        </div>
                                      
</div>
            