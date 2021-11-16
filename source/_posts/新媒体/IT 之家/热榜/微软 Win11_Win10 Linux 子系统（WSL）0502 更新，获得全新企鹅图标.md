
---
title: '微软 Win11_Win10 Linux 子系统（WSL）0.50.2 更新，获得全新企鹅图标'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/0a560a12-5c2d-4f28-a1cb-d614baf0fdf8.png'
author: IT 之家
comments: false
date: Mon, 15 Nov 2021 23:31:34 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/0a560a12-5c2d-4f28-a1cb-d614baf0fdf8.png'
---

<div>   
<p data-vmark="7bd1"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 16 日消息，微软今日向 Github 和 Microsoft Store 的 Windows Linux 子系统（WSL）发布了 <span class="accentTextColor">0.50.2 版本更新</span>，带来了诸多改进。</p><p data-vmark="3d8b"><img src="https://img.ithome.com/newsuploadfiles/2021/11/0a560a12-5c2d-4f28-a1cb-d614baf0fdf8.png" w="709" h="219" title="微软 Win11/Win10 Linux 子系统（WSL）0.50.2 更新，获得全新企鹅图标" width="709" height="219" referrerpolicy="no-referrer"></p><p data-vmark="953d">0.50.2 版本最显而易见的改变就是<span class="accentTextColor">全新的 Tux 小企鹅图标</span>，除此之外，该版本使用了更新的内核，并进行了诸多修复。</p><h2 data-vmark="bc29">以下为完整日志：</h2><ul class=" list-paddingleft-2"><li><p data-vmark="523c"> Windows Subsystem for Linux 添加新图标</p></li><li><p data-vmark="53f8">如果硬件支持，则启用硬件性能计数器，已在 opt-out 中添加了一个 USERPROFILE%\.wslconfig 选项：</p></li></ul><pre>[wsl2]
hardwarePerformanceCounters=false</pre><ul class="ai-word-checked list-paddingleft-2"><li><p data-vmark="99b5">修复打印系统错误消息时包含插入内容的的问题。</p></li><li><p data-vmark="81a3">更新用户磁贴以在用户的主目录而不是 C:\WINDOWS\System32 中启动</p></li><li><p data-vmark="8911">恢复 /etc/wsl.conf boot.command 进程的默认信号处理以防止僵尸进程</p></li><li><p data-vmark="87ae">切换到对 Windows 二进制文件使用静态 CRT</p></li><li><p data-vmark="3e1b">wsl.exe --install 使用商店 API 下载分发</p></li><li><p data-vmark="f965">将 --no-launch 选项添加到 wsl.exe --install</p></li><li><p data-vmark="f925">许多本地化字符串的更新</p></li><li><p data-vmark="e052">切换到更新的 tar 以导入/导出 WSL2 发行版</p></li><li><p data-vmark="443d">更新到官方 22000 sdk</p></li><li><p data-vmark="0315">去除用于发布版本的 Linux symbols</p></li><li><p data-vmark="a5ea">升级 Linux kernel 内核到 5.10.74.3</p></li></ul><blockquote><p data-vmark="b99c">更新至上游稳定内核版本 5.10.74</p><p data-vmark="4c51">启用 BPF Type Format (CONFIG_DEBUG_INFO_BTF) 以供 eBPF 工具使用</p><p data-vmark="fb18">将 Dxgkrnl 版本更改为 2110</p><p data-vmark="b5ea">为 Dxgkrnl 使用启用缓冲区共享和同步文件框架（CONFIG_DMA_SHARED_BUFFER、CONFIG_SYNC_FILE）</p></blockquote><p data-vmark="8ff8">IT之家小伙伴可以在 <a href="https://github.com/microsoft/WSL/releases/tag/0.50.2" target="_blank">GitHub 页面</a>查看更新并安装 0.50.2 版本的 WSL。</p>
          
</div>
            