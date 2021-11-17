
---
title: 'Windows SubSystem for Linux 0.50.2 发布，添加新 logo'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0b0d0f10560762d094fd896910c37c30992.png'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0b0d0f10560762d094fd896910c37c30992.png'
---

<div>   
<div class="content">
                                                                                            <p>Windows 的 Linux 子系统 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fp%2Fapp%2F9p9tqf7mrm4r%23activetab%3Dpivot%3Aoverviewtab" target="_blank">WSL</a>) 发布了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FWSL%2Freleases%2Ftag%2F0.50.2" target="_blank"> 0.50.2 版本</a>，此版本的显著变化之一是增加了新 logo。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0b0d0f10560762d094fd896910c37c30992.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#424242">除此之外还更新了内核版本，以及其他改进和修复。</span></p> 
<ul> 
 <li style="text-align:left"><span style="color:#000000">在硬件支持的情况下启用硬件性能计数器[GH 4678]<br> 增加</span><span style="background-color:#ffffff; color:#24292f"><span> </span></span><code>USERPROFILE%\.wslconfig</code><span style="color:#000000">选项来选择退出。</span></li> 
 <li><span style="color:#000000">修复打印包含插入内容的系统错误信息时的问题</span></li> 
 <li><span style="color:#000000">更新 user tile，使其在用户的主目录而不是 C:\WINDOWS\System32 中启动</span></li> 
 <li><span style="color:#000000">恢复 /etc/wsl.conf boot.command 进程的默认信号处置，防止僵尸进程 [GH 7575]</span></li> 
 <li><span style="color:#000000">对 Windows 安装文件改用静态 CRT</span></li> 
 <li><span style="color:#000000">使用存储 API 通过</span><span style="background-color:#ffffff; color:#24292f"><span> </span></span><code>wsl.exe --install</code><span style="color:#000000">下载发行版</span></li> 
 <li><span style="color:#000000">在</span><span style="background-color:#ffffff; color:#24292f"><span> </span></span><code>wsl.exe --install</code><span style="color:#000000">中添加</span><code>--no-launch</code><span style="color:#000000">选项</span></li> 
 <li><span style="color:#000000">对本地化字符串的多项更新</span></li> 
 <li><span style="color:#000000">改用更新的 tar 来导入/导出WSL2发行版</span></li> 
 <li><span style="color:#000000">更新到官方的 22000 sdk</span></li> 
 <li><span style="color:#000000">剥离用于发布构建的 Linux 符号</span></li> 
 <li><span style="color:#000000">更新 Linux 内核到 5.10.74.3</span> 
  <ul> 
   <li><span style="color:#000000">更新到上游稳定内核版本 5.10.74</span></li> 
   <li><span style="color:#000000">启用 BPF 类型格式（CONFIG_DEBUG_INFO_BTF），供eBPF工具使用 [GH 7437]</span></li> 
   <li><span style="color:#000000">将 Dxgkrnl 版本改为 2110</span> 
    <ul> 
     <li><span style="color:#000000">实现了 D3DKMTShareObjectWithHost</span></li> 
     <li><span style="color:#000000">修正了结果的 QueryStatistics VM 总线对齐问题</span></li> 
     <li><span style="color:#000000">实现了 D3DKMTCreateSyncFile</span></li> 
     <li><span style="color:#000000">解决上游提交的反馈问题</span></li> 
     <li><span style="color:#000000">将 d3dkmthk 移至 include/uapi/misc</span></li> 
     <li><span style="color:#000000">用 __u32 替换了 u32，用 __u64 替换了 u64</span></li> 
     <li><span style="color:#000000">在枚举器值前面添加了"_"，以支持包括 WDK 和 Linux 头文件</span></li> 
     <li><span style="color:#000000">删除了用户模式可见结构中的漏洞，以便与 32 位应用程序兼容</span></li> 
     <li><span style="color:#000000">在用户模式可见结构中用定义的 u64 取代了用户模式应用的指针</span></li> 
     <li><span style="color:#000000">修复 GCC 版本超过 8.1 时的构建失败 [GH 7558]</span></li> 
    </ul> </li> 
  </ul> </li> 
 <li style="text-align:left"><span style="color:#000000">为 Dxgkrnl 的使用启用缓冲区共享和同步文件框架（CONFIG_DMA_SHARED_BUFFER, CONFIG_SYNC_FILE）</span></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FWSL%2Freleases%2Ftag%2F0.50.2" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            