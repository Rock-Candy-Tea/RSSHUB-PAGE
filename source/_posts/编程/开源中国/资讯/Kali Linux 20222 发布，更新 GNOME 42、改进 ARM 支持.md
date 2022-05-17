
---
title: 'Kali Linux 2022.2 发布，更新 GNOME 42、改进 ARM 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0517/073206_pnhR_4937141.jpg'
author: 开源中国
comments: false
date: Tue, 17 May 2022 07:34:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0517/073206_pnhR_4937141.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Kali Linux 2022.2 正式发布，该版本也是 Kali Linux 今年的第二个版本，上一个版本为今年 2 月发布的 Kali Linux 2022.1。</p> 
<p><img alt height="366" src="https://static.oschina.net/uploads/space/2022/0517/073206_pnhR_4937141.jpg" width="700" referrerpolicy="no-referrer"></p> 
<h3>GNOME 42</h3> 
<p>Kali Linux 2022.2 带来了 GNOME 的最新版本 GNOME 42，在之前 40 和 41 版本的基础上，该版本更加完善。</p> 
<p>GNOME 主题现在包括一个更现代的外观，去掉了弹出式菜单中的箭头，使用了更多的圆角。此外，还升级和调整了 dash-to-stock 扩展，使其与新的外观整合地更好，并修复了一些错误。</p> 
<p>下面是升级后的 Kali 主题的预览。</p> 
<p><strong>Kali-Dark</strong>:</p> 
<p><img alt height="406" src="https://static.oschina.net/uploads/space/2022/0517/073216_YeoO_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>Kali-Light</strong>:</p> 
<p><img alt height="406" src="https://static.oschina.net/uploads/space/2022/0517/073226_bSL2_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>GNOME 42 的内置屏幕截图工具</h3> 
<p>在 GNOME 42 中，有一项比其他所有功能都更亮眼的新功能：屏幕截图和屏幕录制工具。 就用户体验而言，这是一个巨大的进步。同时，屏幕截图被保存到 <code>~/Pictures/Screenshots/</code>文件夹并复制到剪贴板，因此用户无需查找它们。</p> 
<p><img alt height="406" src="https://static.oschina.net/uploads/space/2022/0517/073236_5hDZ_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>KDE Plasma 5.24</h3> 
<p>这个新的 Plasma 版本专注于改进设计，并改善环境的整体感觉和可用性。</p> 
<p><img alt height="438" src="https://static.oschina.net/uploads/space/2022/0517/073246_Ii2h_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>其他桌面增强功能</h3> 
<p>调整 Xfce</p> 
<ul> 
 <li>当点击注销对话框时，禁用嘈杂的主板蜂鸣声</li> 
 <li>配置 <strong>mousepad</strong>（文本编辑器），以在文件末尾添加缺少的换行符（POSIX 标准）</li> 
 <li>设置多显示器设置的默认壁纸</li> 
 <li>修正鼠标指针的大小，以防止在大型显示器中自动缩放</li> 
 <li>为 ARM 设备提供新的简化面板布局。 
  <ul> 
   <li>此修改还删除了 CPU 图形小部件，不仅因为它需要水平空间，还因为它在低规格 ARM 设备中的性能受到影响。</li> 
  </ul> </li> 
</ul> 
<p><img alt height="465" src="https://static.oschina.net/uploads/space/2022/0517/073259_55xD_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>应用程序图标</h3> 
<p>距离上次 kali 菜单的更新已经有一段时间了。这次对 nmap、fff 和 edb-debugger 的图标进行了改进和更新，并为 evil-winrm 和 bloodhound 增加了新图标。</p> 
<p>另一个改进是，包含用户界面的程序现在将尊重 Kali 提供的自定义图标。以前，App drawer 里的图标显示的是正确的图像，但一旦你启动它，硬编码的程序图标就会被优先考虑，通常会使用较低质量和像素的图像。如今这一变化只影响 KDE 和 GNOME 桌面，在 Xfce 上不起作用。</p> 
<p>之前:</p> 
<p><img alt height="83" src="https://static.oschina.net/uploads/space/2022/0517/073313_MzlQ_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>之后:</p> 
<p><img alt height="77" src="https://static.oschina.net/uploads/space/2022/0517/073322_XXoX_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>自动复制缺失的配置</h3> 
<p>一般来说，Kali 中的配置文件是存储在 <code>$HOME</code> 目录，但有些程序不支持。作为一种解决方法，一些配置文件需要在创建时被复制到用户的主目录。</p> 
<p>这种方法有两个问题。</p> 
<ul> 
 <li>首先，如果用户在他们的文件夹中删除了一个重要的文件，系统可能会产生异常</li> 
 <li>另外，用户只会在它被创建的时候收到可用的配置文件。因此，如果操作系统更新或程序增加了一个新的文件（或修改了现有的文件），用户将不会收到它，除非他们手动复制它。</li> 
</ul> 
<p>有了这个变化，系统将自动复制在你的主文件夹中发现的中的任何文件，而不替换已经存在的文件。</p> 
<h3>支持 VirtualBox 共享文件夹</h3> 
<p>如果你正在使用 VirtualBox，当一个用户账户被创建时，它现在会自动被添加到 <code>vboxsf</code> 组中。这意味着如果你想使用共享文件夹，现在就少了一个步骤。</p> 
<h3>对 Terminal 的调整</h3> 
<ul> 
 <li>对 Zsh 语法高亮颜色做了小改动，以提高可读性。</li> 
 <li>python3-pip 和 python3-virtualenv 现在被默认包含在 Kali 安装中。</li> 
 <li>为 John The Ripper 增加了 shell 自动补全功能。</li> 
 <li>所有 ...2john 工具 (zip2john、7z2john、pdf2john 等) 现在可以直接输入它们的名字来调用，不需要先 <code>cd /usr/share/john/</code>。</li> 
 <li>资源包（wordlists、windows-resources、powersploit等）现在显示出更清晰的输出，用颜色区分文件或目录的类型。</li> 
</ul> 
<p><img alt height="296" src="https://static.oschina.net/uploads/space/2022/0517/073335_8GQw_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Kali Unkaputtbar</h3> 
<p>在 Kali Linux 中引入了对 BTRFS 快照的官方支持，并称它为 Kali Unkaputtbar。</p> 
<p>功能介绍</p> 
<ul> 
 <li>启动快照</li> 
 <li>差异快照</li> 
 <li>浏览快照</li> 
 <li>额外的自动快照</li> 
</ul> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0517/073343_1JN2_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Win-KeX 3.1</h3> 
<p>此更新消除了阻止 GUI 程序以 root 身份运行的限制。现在你可以用 sudo 启动任何 GUI 程序，比如说</p> 
<pre><code>sudo wireshark
</code></pre> 
<p><img alt height="463" src="https://static.oschina.net/uploads/space/2022/0517/073355_hrGj_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Kali 的新工具</h3> 
<ul> 
 <li>BruteShark - 网络取证分析工具(NFAT)</li> 
 <li>Evil-WinRM - WinRM shell</li> 
 <li>Hakrawler - 网络爬虫工具</li> 
 <li>Httpx - 多用途的 HTTP 工具箱</li> 
 <li>LAPSDumper - 转储 LAPS 密码</li> 
 <li>PEDump - 转储 Win32 可执行文件</li> 
 <li>Sparrow-wifi - Linux 下的图形化 Wi-Fi 分析器</li> 
 <li>……</li> 
</ul> 
<h3>Kali ARM 更新</h3> 
<p>Raspberry Pi：</p> 
<ul> 
 <li>将内核提升到 5.10.103</li> 
 <li>修复了蓝牙</li> 
 <li>Wi-Fi 固件现在默认使用 7.45.206 而不是 7.45.154，并应用了 nexmon 补丁</li> 
 <li>Raspberry Pi Zero 2 W 现在被 nexmon 支持了</li> 
 <li>对 <code>wpa_supplicant.conf</code> 处理的改进</li> 
 <li>内核内置了对 NVME 的支持</li> 
</ul> 
<p>Pinebook Pro：</p> 
<ul> 
 <li>使用 Kali 内核和 u-boot</li> 
</ul> 
<p>USB Armory MKII：</p> 
<ul> 
 <li>内核升级到 5.15</li> 
</ul> 
<p>构建脚本的改进：</p> 
<ul> 
 <li><code>command-not-found</code> 和 <code>kali-tweaks</code> 被包含在最小构建中</li> 
 <li>基本目录现在在构建完成时被清理掉，而不是留下一个空目录</li> 
</ul> 
<h3>下载</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fget-kali%2F" target="_blank">链接</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2022-2-release%2F" target="_blank">https://www.kali.org/blog/kali-linux-2022-2-release/</a></p>
                                        </div>
                                      
</div>
            