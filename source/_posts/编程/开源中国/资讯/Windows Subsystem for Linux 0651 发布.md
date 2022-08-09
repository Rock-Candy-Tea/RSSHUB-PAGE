
---
title: 'Windows Subsystem for Linux 0.65.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0808/111107_O0JC_2720166.png'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 07:37:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0808/111107_O0JC_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>微软 <span style="background-color:#ffffff; color:#0f1419">Linux on Windows 团队主管<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fbenhillis%2Fstatus%2F1554619646812164096" target="_blank">宣布</a>，已面向所有 </span>Windows Insiders 用户推出了 Windows Subsystem for Linux 0.65.1。</p> 
<blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">WSL 即 Windows Subsystem for Linux，是 Windows 的 Linux 子系统，本质是在 Windows 上原生运行 Linux 二进制可执行文件（ELF 格式）的兼容层。它允许用户直接在 Windows 中运行 GNU/Linux 环境，而无需通过虚拟机 (VM)) 或配置双启动系统，支持 Windows 10 和 Windows 11。WSL 是一个非常方便的实用程序，尤其适用于跨平台开发和测试。微软会定期更新 WSL 的新特性和功能。</p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2022/0808/111107_O0JC_2720166.png" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li>改进 localhost relay 以获得更好的性能，并准确报告绑定失败的情况</li> 
 <li>使用<code>/dev/ptp0</code><span>来保持</span>访客时钟 (guest chock) 与主机同步</li> 
 <li>当无法获取发行版列表并连接到<span> </span><code>wsl.exe --list --online</code>时，改进了错误处理</li> 
 <li>将 Linux 内核版本升级到 5.15.57.1 
  <ul> 
   <li>修复自上一个 v5.10 WSL2 内核以来的 9p 文件系统回归错误</li> 
   <li>启用对高精度时间同步协议 (PTP) 时钟设备的支持</li> 
   <li>在 x86_64 构建中启用 Retbleed 缓解</li> 
   <li>启用 nftables 和流量控制</li> 
   <li>启用 VGEM 驱动</li> 
  </ul> </li> 
 <li>将 Microsoft.WSLg 升级到 1.0.41 
  <ul> 
   <li>WSLg: 添加默认 x11 铃声</li> 
   <li>WSLg: 更新 /etc/wsl.conf 以将默认用户设置为 wslg</li> 
   <li>WSLGd: 在 gdbserver 下添加启动 weston 的选项</li> 
   <li>WSLGd: 简化 weston 命令行构建</li> 
   <li>compositor: 添加 wslgd-notify</li> 
   <li>compositor: 停止捕获 SIGINT</li> 
   <li>compositor: load xwayland module last</li> 
   <li>rdp: 调整 MoveWindow/SnapArrange PDU 的边际幅度 (margin adjustment)</li> 
   <li>rdpaudio: 使用 pthread_cancel instead of pthread_kill</li> 
   <li>xwayland: give Xwayland its own session</li> 
   <li>xwayland: Don't track focus for override redirect windows</li> 
  </ul> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FWSL%2Freleases%2Ftag%2F0.65.1" target="_blank">下载地址 & Release Note</a></p>
                                        </div>
                                      
</div>
            