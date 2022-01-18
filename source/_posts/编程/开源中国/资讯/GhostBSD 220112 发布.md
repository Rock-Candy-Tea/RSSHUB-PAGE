
---
title: 'GhostBSD 22.01.12 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0118/073916_1WZX_4937141.png'
author: 开源中国
comments: false
date: Tue, 18 Jan 2022 07:39:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0118/073916_1WZX_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>GhostBSD 是一个基于 FreeBSD 的类 Unix 操作系统，它的目标是易于安装和易于使用，并十分注重安全、隐私、稳定、可用性和开放。</p> 
<p>在 GhostBSD 18.10 之前，该项目是基于 FreeBSD 的。2018年，宣布未来版本的操作系统将基于 TrueOS。2020年，随着 TrueOS 的停产，GhostBSD 转回了 FreeBSD。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0118/073916_1WZX_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>这个版本包含修复、改进和软件更新：其中安装程序在 ZFS 安装的清理阶段挂起的问题得到了修复、OpenRC 和 dhcpcd 从基础代码中删除，此外，还增加了 HD 7000 系列和旧版 GPU 的自动化配置；添加了对 os-release 的支持，以便在 mate-system-monitor、python distros、pfetch 和 neofetch 等应用程序中显示 GhostBSD 名称和 GhostBSD 版本，并添加了一组新的壁纸，同时从默认选择中删除了 p7zip。</p> 
<p>其他更新内容如下：</p> 
<h3>Epic</h3> 
<ul> 
 <li>[Epic] 从基础代码中删除相关的 OpenRC 代码</li> 
 <li>[Task] 从 contrib 中删除 OpenRC</li> 
 <li>[Task] 从 libexec/rc 中删除 OpenRC 服务</li> 
 <li>[Task] 从 contrib 中删除 dhcpcd</li> 
 <li>[Task] 从 loader 中删除 rc_system</li> 
</ul> 
<h3>特性：</h3> 
<ul> 
 <li>[Feature]: 用 UPNP 选项构建 VLC 包</li> 
 <li>[Feature]: 自定义 /etc/os-release</li> 
 <li>[Feature] 在 uname 输出中加入 GhostBSD，以便 pfetch/neofetch 能显示正确的操作系统信息。</li> 
 <li>[Feature]: 用于自动配置图形硬件的 initgfx</li> 
</ul> 
<h3>Bug</h3> 
<ul> 
 <li>修复了错误信息中的拼写错误</li> 
 <li>在 ZFS 安装的清理阶段挂起的问题得到了修复</li> 
 <li>添加代码以查看是否存在 tree_iter2</li> 
 <li>修正了用空磁盘创建方案的问题</li> 
</ul> 
<h3>安全：</h3> 
<ul> 
 <li>[Bug]: 发现有漏洞的软件包 [PKGS-7381]</li> 
</ul> 
<h3>最低系统要求</h3> 
<ul> 
 <li>64 位处理器</li> 
 <li>4GB 以上的内存</li> 
 <li>15GB 的可用硬盘空间</li> 
</ul>
                                        </div>
                                      
</div>
            