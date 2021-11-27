
---
title: 'GhostBSD 21.11.24 发布，注重安全与稳定性的 FreeBSD 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4466'
author: 开源中国
comments: false
date: Sat, 27 Nov 2021 08:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4466'
---

<div>   
<div class="content">
                                                                                            <p>GhostBSD 是一个基于 FreeBSD 的类 Unix 操作系统，它的目标是易于安装和易于使用，并十分注重安全、隐私、稳定、可用性和开放。在 GhostBSD 18.10 之前，该项目是基于 FreeBSD 的。2018年，宣布未来版本的操作系统将基于 TrueOS。2020年，随着 TrueOS 的停产，GhostBSD 转回了 FreeBSD。</p> 
<p>GhostBSD 21.11.24 更新内容包括：</p> 
<h3>特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-src%2Fissues%2F106" target="_blank">ghostbsd/ghostbsd-src#106</a> 在软件包仓库中添加了版本文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-src%2Fissues%2F107" target="_blank">ghostbsd/ghostbsd-src#107</a> 在软件包仓库的版本文件中添加了带有 ghostbsd-build 的 /etc/version</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-src%2Fissues%2F108" target="_blank">ghostbsd/ghostbsd-src#108</a> 在更新管理器中添加了更新 /etc/version 的功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-src%2Fissues%2F109" target="_blank">ghostbsd/ghostbsd-src#109</a> 创建 ghostbsd-version</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-build%2Fcommit%2F1f7ce4fbdb9bafdc869e792acfbf3e3a41f53896" target="_blank">ghostbsd/ghostbsd-build/commit/1f7ce4f</a> 在 set_ghostbsd_version 下移动了版本，并从 repo 中设置 GhostBSD ISO 版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fghostbsd-src%2Fissues%2F95" target="_blank">ghostbsd/ghostbsd-src#95</a> 将更新完成窗口中的 "立即重启 "按钮移到右边的第一个位置。</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostbsd%2Fgbi%2Fpull%2F61" target="_blank">ghostbsd/gbi#61</a> 修正了用空磁盘创建的方案</li> 
</ul> 
<h3>最低系统要求</h3> 
<ul> 
 <li>64 位处理器</li> 
 <li>4GB 以上的内存</li> 
 <li>15GB 的可用硬盘空间</li> 
</ul> 
<p>注意：GhostBSD 不能成功地安装在内存小于 4G 的系统中，因为一旦 GhostBSD 被启动，它就会从内存中运行，而不是从 USB 闪存或 DVD 中。</p> 
<h3><strong>下载</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ghostbsd.org%2Fdownload" target="_blank">https://www.ghostbsd.org/download</a></p> 
<h3>将 iso 写到 U 盘上：</h3> 
<p>在 BSD 上</p> 
<pre><code>dd if=GhostBSD-21.11.24.iso of=/dev/da0 bs=4m
</code></pre> 
<p>在 Linux 上</p> 
<pre><code>dd if=GhostBSD-21.11.24.iso of=/dev/sdc bs=4M
</code></pre> 
<p>在 Mac 上</p> 
<pre><code>dd if=GhostBSD-21.10.16.iso of=/dev/disk2 bs=10240
</code></pre> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fghostbsd.org%2Fghostbsd_21.11.24_iso_is_now_available" target="_blank">https://ghostbsd.org/ghostbsd_21.11.24_iso_is_now_available</a></p>
                                        </div>
                                      
</div>
            