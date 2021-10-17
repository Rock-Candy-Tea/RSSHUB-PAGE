
---
title: 'Devuan 4.0 发布，不依赖 systemd 的 Debian 分支'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2020/0604/020937_LRRX_2720166.png'
author: 开源中国
comments: false
date: Sun, 17 Oct 2021 00:00:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2020/0604/020937_LRRX_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Devuan 4.0 稳定版已正式发布，代号 "Chimaera"。</p> 
<p>主要变化：</p> 
<ul> 
 <li>基于 Debian Bullseye (11.1)，使用的内核版本为 Linux Kernel 5.10</li> 
 <li>可选的 init 系统包括：sysvinit, runit 和 OpenRC</li> 
 <li>改进桌面支持：在不依赖 systemd 的前提下，Debian 中几乎所有可用的桌面环境现在都是 Devuan 的一部分</li> 
 <li>新的引导、显示管理器和桌面主题</li> 
 <li>增强的可访问性：需要通过 GUI 或控制台的安装工作现在可以通过软件或硬件语音合成来进行，或使用可刷新的盲文显示器来完成，而且 Devuan Chimaera 有能力在没有 PulseAudio 的情况下安装桌面环境，允许在控制台和 GUI 会话中同时进行语音合成</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Devuan 是使用 SysV init 软件代替 Debian systemd 包的 Debian 分支。依赖于初始化系统 systemd 的服务已经被提供等效功能的其他软件所替代。因为选择初始化系统 systemd 引发的争议，一群不满的开发者创建了不使用 systemd 的 Debian 分支 Devuan（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.dyne.org%2Flurker%2Fmessage%2F20141127.212941.f55acc3a.en.html" target="_blank">点击这里查看最初的公告</a>）。systemd 最受争议的地方是违背了 Unix 哲学，被认为太过于复杂，而 Devuan 提供了多种初始化系统供用户选择，其中包括 SysV init、sinit、openrc、runit、s6 和 shepherd。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2020/0604/020937_LRRX_2720166.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Devuan 采用 Xfce 作为默认桌面环境。</p>
                                        </div>
                                      
</div>
            