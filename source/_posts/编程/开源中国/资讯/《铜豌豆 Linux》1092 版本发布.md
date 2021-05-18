
---
title: '《铜豌豆 Linux》10.9.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=390'
author: 开源中国
comments: false
date: Tue, 18 May 2021 10:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=390'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2FNews%2F2021%2F20210517.htm" target="_blank">https://www.atzlinux.com/News/2021/20210517.htm</a></p> 
<h1>《铜豌豆 Linux》10.9.2 版本发布</h1> 
<h3>2021-05-17</h3> 
<p>此次发布主要为优化 ISO 安装速度，更新升级软件包、调整软件包。</p> 
<h3>软件包更新</h3> 
<p>Debian 官方软件包，更新至 Debian 官方仓库 buster-proposed-updates 2021-05-17 日。</p> 
<h3>安全更新</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2Fsecurity%2F" target="_blank">Debian 官方软件包安全更新</a> 同步到 2021-05-17 日。</li> 
</ul> 
<h3>iso 文件调整及优化</h3> 
<ul> 
 <li>优化安装速度约三分之一</li> 
 <li>在虚拟机、慢速磁盘、移动 U 盘上的效果明显</li> 
 <li>新增 支持 免 U 盘安装铜豌豆系统</li> 
 <li>可以在已经安装的 Linux 系统的机器上，使用硬盘安装的方式来安装铜豌豆系统，不需要再制作安装 U 盘，具体方法请参阅：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fskills-tech.htm%23hd-install" target="_blank">https://www.atzlinux.com/skills-tech.htm#hd-install</a></li> 
 <li>新增支持 <strong>铜豌豆随手带</strong> 功能</li> 
 <li>可以将铜豌豆系统安装到 U 盘、移动硬盘，制作形成一个 live 系统，随身携带，将 U 盘可以插入任一其它电脑启动铜豌豆系统。<br> 具体方法请参阅：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fskills-tech.htm%23hd-live" target="_blank">https://www.atzlinux.com/skills-tech.htm#hd-live</a></li> 
 <li>将 5.10.x 系列最新版本内核软件包集成到 iso 文件</li> 
 <li>路径为： <em>pool/main/l/linux/linux-image-5.10.0-0.bpo.5-rt-amd64_5.10.24-1~bpo10+1_amd64.deb</em> <p>对部分比较新的硬件，在安装过程及系统安装完成后均无法驱动的情况，可以在操作系统安装完成后，再安装这个新版内核并重启机器。</p> <p>登录系统后，重新拔插下 U 盘，让 U 盘自动挂载，在命令行进入挂载目录，用 root 账号安装该内核软件包：<br> dpkg -i linux-image-5.10.0-0.bpo.5-rt-amd64_5.10.24-1~bpo10+1_amd64.deb</p> </li> 
</ul> 
<h3>主要软件包调整：</h3> 
<ul> 
 <li>铜豌豆补丁包</li> 
 <li>1.1.50 版， /etc/atzlinux_version 文件, 版本号设置为 10.9.2；<br> 修复三合一版本中，登录界面右上角有无法使用的 gnome 桌面选项问题。</li> 
 <li>iw 无线网卡命令软件包 升级到 Debian 官方上游最新的 5.9-3 版本</li> 
 <li>新增自制 netscripts-atzlinux 软件包</li> 
 <li>封装简化网络相关命令输入，快速获取基本网络信息。</li> 
</ul> 
<h3>各版本软件包增加：</h3> 
<ul> 
 <li>纯文字版</li> 
 <li>apt-forktracer， 列出系统上安装的非 Debian 官方软件包列表<br> arping，以太网 MAC ping 检测<br> bc， 命令行计算器<br> firmware-atheros， 高通网卡固件<br> linux-cpupower，CPU 频率、空闲等信息查看<br> netscripts-atzlinux，铜豌豆网络小脚本<br> sysstat，系统性能状态查看<br> tlp-rdw，无线类设备网络、节能优化</li> 
 <li>xfce 精简版</li> 
 <li>无</li> 
 <li>xfce 完整版</li> 
 <li>bc<br> firmware-atheros<br> firmware-sof-signed Intel SOF 音频固件<br> linux-cpupower<br> netscripts-atzlinux<br> smartmontools， 硬盘信息状态监控<br> sysstat<br> tlp-rdw<br> wireless-regdb，无线网卡各国规则库</li> 
 <li>三合一版</li> 
 <li>bc<br> firmware-atheros<br> firmware-sof-signed<br> linux-cpupower<br> netscripts-atzlinux<br> smartmontools<br> sysstat<br> tlp-rdw<br> wireless-regdb</li> 
 <li>KDE 版</li> 
 <li>bc<br> firmware-atheros<br> firmware-sof-signed<br> linux-cpupower<br> netscripts-atzlinux<br> smartmontools<br> sysstat<br> tlp-rdw<br> wireless-regdb</li> 
</ul> 
<h3>软件包删除：</h3> 
<ul> 
 <li>xfce 精简版</li> 
 <li>无</li> 
 <li>xfce 完整版</li> 
 <li>无</li> 
 <li>三合一版</li> 
 <li>libpq5, 在该版本中，不需要使用。</li> 
 <li>KDE 版</li> 
 <li>无</li> 
</ul> 
<h3>下载</h3> 
<p>安装文件大小约 3.1 G，下载地址如下：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.tuna.tsinghua.edu.cn%2Fosdn%2Fstorage%2Fg%2Fa%2Fat%2Fatzlinux%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fiso-dvd%2Fatzlinux-10.9.2-amd64-DVD-1.iso" target="_blank">https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/a/at/atzlinux/atzlinux-cd/10.9.2/amd64/iso-dvd/atzlinux-10.9.2-amd64-DVD-1.iso</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.bfsu.edu.cn%2Fosdn%2Fstorage%2Fg%2Fa%2Fat%2Fatzlinux%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fiso-dvd%2Fatzlinux-10.9.2-amd64-DVD-1.iso" target="_blank">https://mirrors.bfsu.edu.cn/osdn/storage/g/a/at/atzlinux/atzlinux-cd/10.9.2/amd64/iso-dvd/atzlinux-10.9.2-amd64-DVD-1.iso</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.xtom.com.hk%2Fosdn%2Fstorage%2Fg%2Fa%2Fat%2Fatzlinux%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fiso-dvd%2Fatzlinux-10.9.2-amd64-DVD-1.iso" target="_blank">https://mirrors.xtom.com.hk/osdn/storage/g/a/at/atzlinux/atzlinux-cd/10.9.2/amd64/iso-dvd/atzlinux-10.9.2-amd64-DVD-1.iso</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flx.atzlinux.com%3A24359%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fiso-dvd%2Fatzlinux-10.9.2-amd64-DVD-1.iso" target="_blank">https://lx.atzlinux.com:24359/atzlinux-cd/10.9.2/amd64/iso-dvd/atzlinux-10.9.2-amd64-DVD-1.iso</a></p> 
<hr> 
<ul> 
 <li>清华大学开源软件镜像站下载</li> 
 <li>北京外国语大学开源软件镜像站下载</li> 
 <li>xtom 香港 开源软件镜像站下载</li> 
 <li>北方联通下载</li> 
 <li>系统默认创建两个用户，一个是具有最高系统权限的管理员用户 root ；一个是名字为 wo 的普通用户。</li> 
 <li>root 用户可以直接登录系统， <em><span style="color:#ff0000"><strong>初始密码</strong></span></em>为：</li> 
 <li><em>debian-cn;168</em><br> 中间为英文的连接符，英文的分号</li> 
 <li>普通用户名为： <strong>wo</strong> ，<strong>初始密码</strong>为：</li> 
 <li><em>debian168;</em><br> 最后一个字符是英文的分号 
  <hr></li> 
</ul> 
<p>下载的安装文件名为：<em>atzlinux-10.9.2-amd64-DVD-1.iso</em><br> 下载完成后，可进行完整性验证，支持校验和、公钥签名验证。 验证所需<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fiso-dvd%2F" target="_blank">相关文件请访问这里</a>获取。</p> 
<p>该 iso 安装文件，支持目前国内市场上常用的 Intel/amd 64 位 CPU。</p> 
<h3>无缝升级</h3> 
<p>铜豌豆软件源已经同步更新此次升级的软件包，之前用 iso 安装系统的用户，无需重装。</p> 
<p>请用 root 用户运行下列命令，一键更新所有软件包到最新版本：<br> <br> <em>apt update<br> apt upgrade </em></p> 
<h3>iso 文件信息：</h3> 
<ul> 
 <li>jidgo 文件：</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fatzlinux-cd%2F10.9.2%2Famd64%2Fjigdo-dvd%2F" target="_blank">https://www.atzlinux.com/atzlinux-cd/10.9.2/amd64/jigdo-dvd/</a> <p><strong>指引：</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fskills.htm%23jigdo" target="_blank"> 使用 jigdo 下载制作铜豌豆 iso 镜像文件 </a></p> </li> 
 <li>iso 文件软件包完整列表：</li> 
 <li><a href="https://gitee.com/atzlinux/debian-cn/blob/apt-install/isodvd/10.9/atzlinux-10.9.2-amd64-DVD-1.list" target="_blank">https://gitee.com/atzlinux/debian-cn/blob/apt-install/isodvd/10.9/atzlinux-10.9.2-amd64-DVD-1.list</a></li> 
</ul> 
<h4>已知问题</h4> 
<ul> 
 <li>钉钉</li> 
 <li>文件传输对话框界面显示乱码，有需要此功能的用户可以到铜豌豆软件源安装 dingtalk-electron 软件包。 该软件包和系统原有钉钉可以同时共存。</li> 
 <li>雷鸟邮件客户端</li> 
 <li>GPG 无法导入带中文书名号 uid 的密钥。 https://gitee.com/atzlinux/debian-cn/issues/I230IA</li> 
</ul> 
<h4>其它事项</h4> 
<p>root 账号登录系统</p> 
<ol> 
 <li>点击象棋、围棋程序，会报错</li> 
 <li>默认声音图标显示为静音</li> 
 <li>无法打开声音，不能够播放声音</li> 
</ol> 
<p>以上为正常现象。这是由于 Debian 的安全机制，不建议 root 用户直接使用日常应用程序。请用普通账号登录系统使用相关功能。</p>
                                        </div>
                                      
</div>
            