
---
title: 'Finnix 124 发布，供系统管理员使用的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=195'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=195'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Finnix 是一个免费、独立、可启动的 Linux 发行版，供系统管理员使用，基于 Debian。Finnix 包括为系统管理员提供的最新技术，数百个为系统管理员准备的软件包等。最重要的是，Finnix 足够小，可以快速下载并写入 USB 驱动器或刻录到 CD 上。Finnix 不是为普通的桌面用户准备的，它不包括任何桌面或生产力工具。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">跟上一个版本更新相隔 6 个月，Finnix 124 正式发布，这次发布也是为了庆祝 Finnix 首次公开发布 22 周年。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Finnix 124 主要的更新内容包括：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>wifi-connect</code><span> </span>辅助工具在没有任何命令行选项的情况下调用，现在会显示附近的接入点</li> 
 <li><code>ip=</code><span> </span>内核命令行网络配置现在除了前缀长度外还支持 netmasks</li> 
 <li>增加了一个纯 Python<span> </span><code>strings</code><span> </span>的实现</li> 
 <li>除了 amd64、i386、arm64、armhf、ppc64el、s390x 之外，还增加了对 RISC-V (riscv64) 的非官方构建支持</li> 
 <li>用更传统的 multi-user.target 替换了运行中的 systemd finnix.target</li> 
 <li>增加了新的软件包： 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Finxi" target="_blank">inxi</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffinnix%2Ffinnix%2Fissues%2F23" target="_blank">finnix/finnix#23</a>)</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Frmlint" target="_blank">rmlint</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffinnix%2Ffinnix%2Fissues%2F24" target="_blank">finnix/finnix#24</a>)</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Fnwipe" target="_blank">nwipe</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffinnix%2Ffinnix%2Fissues%2F25" target="_blank">finnix/finnix#25</a>)</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Frename" target="_blank">rename</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffinnix%2Ffinnix%2Fissues%2F26" target="_blank">finnix/finnix#26</a>)</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Fgdu" target="_blank">gdu</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffinnix%2Ffinnix%2Fissues%2F27" target="_blank">finnix/finnix#27</a>)</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Fpwgen" target="_blank">pwgen</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Fsntp" target="_blank">sntp</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Flz4" target="_blank">lz4</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Flzip" target="_blank">lzip</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Flzop" target="_blank">lzop</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Ftesting%2Fzstd" target="_blank">zstd</a></li> 
  </ul> </li> 
 <li>移除的软件包： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>pppoeconf (有问题)</li> 
   <li>crda (过时)</li> 
  </ul> </li> 
 <li>上游的 Debian 软件包更新</li> 
 <li>其他修复和改进</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.finnix.org%2F" target="_blank">https://blog.finnix.org/</a></p>
                                        </div>
                                      
</div>
            