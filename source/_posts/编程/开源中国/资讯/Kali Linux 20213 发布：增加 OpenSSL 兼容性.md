
---
title: 'Kali Linux 2021.3 发布：增加 OpenSSL 兼容性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fb432aeb0f40726ec0559d8a67a929b7613.jpg'
author: 开源中国
comments: false
date: Wed, 15 Sep 2021 06:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fb432aeb0f40726ec0559d8a67a929b7613.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Kali Linux 2021.3 现已发布。以下是其主要更新内容：</p> 
 <p><img alt height="628" src="https://oscimg.oschina.net/oscnet/up-fb432aeb0f40726ec0559d8a67a929b7613.jpg" width="1200" referrerpolicy="no-referrer"></p> 
 <h4>OpenSSL：默认情况下具有广泛的兼容性</h4> 
 <p>从 Kali Linux 2021.3 开始，OpenSSL 具有更广泛的兼容性，以允许 Kali 与尽可能多的服务进行通信。这意味着默认情况下启用旧协议（例如 TLS 1.0 和 TLS 1.1）和旧密码。这样做是为了帮助提高 Kali 与一些过时的系统和服务器通信的能力。不过，用户可以过命令行工具 kali-tweaks 修改这个设置。</p> 
 <h4>Kali-Tools</h4> 
 <p>该网站进行了全面升级，提供了一个新的、更快的布局、内容和系统！后端现在处于半自动化状态，并且更多地处于开放状态，就像以前一样，允许任何人提供帮助和贡献。一旦该网站稳定下来，开发人员就会将它们打包起来，允许离线阅读。</p> 
 <p><img alt height="1010" src="https://oscimg.oschina.net/oscnet/up-65b4ccf4bec25a1f6411e167ad0a385452c.png" width="1435" referrerpolicy="no-referrer"></p> 
 <h4>虚拟化</h4> 
 <p>在虚拟化环境中运行 Live 映像的用户将获得更流畅的体验。主机和来宾之间的复制、粘贴和拖放等基本功能现在开箱即用，适合 VMware、VirtualBox、Hyper-V 和 QEMU+Spice 等所有用户。并且现在很容易为 Hyper-V 增强会话模式配置 Kali。如果用户使用此功能，请务必访问<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkali.org%2Fdocs%2Fvirtualization%2Finstall-hyper-v-guest-enhanced-session-mode%2F" target="_blank">注意事项</a>。</p> 
 <h4>Kali ARM 更新</h4> 
 <p>开发人员一直在对 Kali ARM 映像进行各种调整和修补，其中包括：</p> 
 <ul> 
  <li>Kali ARM 构建脚本已经过重新设计</li> 
  <li>所有图像最终都应该在第一次启动时调整文件系统的大小</li> 
  <li>现在重新生成默认的 snakeoil 证书，它修复了以前无法运行的几个工具</li> 
  <li>图像默认为 iptables-legacy 和 ip6tables-legacy 以支持 iptables</li> 
  <li>现在在所有图像上设置默认语言环境 en_US.UTF-8，用户也可以将其更改为喜欢的语言环境</li> 
  <li>默认情况下，ARM 映像上的 Kali 用户现在与基本映像位于所有相同的组中，并使用 zsh 作为默认 shell。用户可以使用预先安装的 kali-tweaks 工具更改默认 shell</li> 
  <li>Raspberry Pi 映像现在可以使用 /boot 分区上的 wpa_supplicant.conf 文件</li> 
  <li>Raspberry Pi 映像现在带有 kalipi-config，并且预装了 kalipi-tft-config</li> 
  <li>Pinebook Pro 的内核已更新至 5.14，用户现在可以在启动时在 LCD 屏幕上看到消息，而不是在 X 启动之前光标一直闪烁</li> 
 </ul> 
 <h4>桌面和主题更新</h4> 
 <p>桌面空间也有一些变化：</p> 
 <ul> 
  <li>改进了 Xfce 通知和注销对话框的 GTK3 主题</li> 
  <li>重新设计 GTK2 主题以更好地适应旧程序</li> 
  <li>改进了 GNOME 和 Xfce 的 Kali-Dark 和 Kali-Light 语法高亮主题</li> 
 </ul> 
 <p><img alt height="900" src="https://oscimg.oschina.net/oscnet/up-89d55eea4732ef23694650ecf4c2b71a86f.png" width="1600" referrerpolicy="no-referrer"></p> 
 <p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2021-3-release%2F" target="_blank">更新公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            