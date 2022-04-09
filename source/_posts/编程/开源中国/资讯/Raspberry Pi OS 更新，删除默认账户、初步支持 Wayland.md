
---
title: 'Raspberry Pi OS 更新，删除默认账户、初步支持 Wayland'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0409/071901_Ulud_4937141.png'
author: 开源中国
comments: false
date: Sat, 09 Apr 2022 07:19:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0409/071901_Ulud_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>树莓派基金会近日为 Raspberry Pi OS 带来了更新，具体更新内容如下：</p> 
<h3>安全</h3> 
<p>多年来，Raspberry Pi 操作系统的安全性在逐渐加强；这不是为了应对特定的威胁，而是作为一种普遍的预防措施。</p> 
<p>到目前为止，所有 Raspberry Pi OS 的安装都有一个叫做 "pi" 的默认用户。虽然在黑客入侵你的系统时，仅仅知道一个用户名并没有什么帮助，但这仍然有可能遭到黑客的暴力破解。为了应对这一情况，在这个最新的版本中，默认的 "pi" 用户将被删除，用户需要在第一次启动 Raspberry Pi OS 时创建一个用户账号。</p> 
<h3>新的向导</h3> 
<p>Raspberry Pi 的设置向导会在第一次启动时运行，用户可以通过它来进行初步设置，如：连接到无线局域网、安装软件更新，以及提示你修改默认 “pi” 账户的密码。但这个设置向导此前是可选的，用户可以点击 "取消" 按钮，跳过这些设置。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0409/071901_Ulud_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>由于取消了默认的 “pi” 用户账户，从新版本开始，用户必须在进入桌面之前先创建一个账户，设置向导将无法再跳过。除此之外，新版本中设置向导不再像以前那样作为一个应用程序在桌面本身运行，而是在第一次启动时在一个专门的环境中运行。设置向导本身与以前相比基本没有什么变化。</p> 
<p>如果用户使用的是没有向导的 Raspberry Pi OS Lite，也同样需要创建一个新的用户帐户。只不过在启动系统时，系统会在命令行中通过文本提示用户创建帐户。</p> 
<h3>Raspberry Pi Imager</h3> 
<p>Raspberry Pi Imager 工具允许用户使用用户帐户预配置镜像，当像这样创建的系统首次启动时，将以在 Imager 中创建的用户身份登录。</p> 
<p><img alt height="464" src="https://static.oschina.net/uploads/space/2022/0409/071911_nZth_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>现有用户</h3> 
<p>现有用户在更新至新系统后，首先需确保是以 "pi" 用户的身份进行了登录，然后打开一个终端窗口并输入：</p> 
<p><code>sudo rename-user</code></p> 
<p>在短暂的停顿后，终端会提示你进行重启，然后 Raspberry Pi 会重启到一个精简版的启动向导，该向导页面只允许用户改变用户名和密码。</p> 
<p><img alt height="524" src="https://static.oschina.net/uploads/space/2022/0409/071921_AZlP_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>一旦输入了新的用户名和密码，Raspberry Pi 会重启并进入桌面，你现有的用户（和你的主目录）会被重新命名，除此之外没有其他变化。</p> 
<h3>蓝牙外设</h3> 
<p>新版本中，解决了一个长期存在的蓝牙外设问题。此前如果用户想在 Raspberry Pi 上使用蓝牙键盘或鼠标，用户总是先需要使用 USB 来进行最初的蓝牙配对。</p> 
<p>在新系统中中，这一要求已被删除。用户只需将需要使用的蓝牙键盘或鼠标调整至配对模式，Raspberry Pi 就会自动扫描周围可配对的蓝牙鼠标和键盘。</p> 
<p>这个新特性既适用于内置了蓝牙适配器的 Raspberry Pi 3 和 4，也适用于使用 USB 蓝牙适配器的早期型号。</p> 
<h3>Wayland</h3> 
<p>Wayland 是 X Window System 的拟议替代品，Wayland 相比 X Window System 有多项优势，特别是安全和性能，但它仍然是相当新的技术，目前仍在开发中。</p> 
<p>在新版本中，Raspberry Pi OS 使在 Wayland 之上运行桌面成为可能，但目前仅作为一项实验性功能，供有兴趣的用户尝试。</p> 
<h3>其他</h3> 
<ul> 
 <li>Linux 5.15 LTS</li> 
 <li>Chromium 98.0.4758.10</li> 
 <li>OpenJDK 17</li> 
 <li>……</li> 
</ul> 
<h3>下载</h3> 
<p>链接如下：（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.raspberrypi.com%2Fsoftware%2F" target="_blank">https://www.raspberrypi.com/software/</a>）</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.raspberrypi.com%2Fnews%2Fraspberry-pi-bullseye-update-april-2022%2F" target="_blank">https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/</a></p>
                                        </div>
                                      
</div>
            