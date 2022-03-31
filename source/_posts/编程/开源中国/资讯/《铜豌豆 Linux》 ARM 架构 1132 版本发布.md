
---
title: '《铜豌豆 Linux》 ARM 架构 11.3.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7372'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 17:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7372'
---

<div>   
<div class="content">
                                                                    
                                                        <p>《铜豌豆 Linux》 ARM 架构 11.3.2 版本发布</p> 
<h3>2022-03-31</h3> 
<p>《铜豌豆 Linux》 ARM 架构版本，在经过历时三个多月的开发后，第一次公开对外发布。</p> 
<p>支持 arm v8 64 位 CPU，包括飞腾、鲲鹏、苹果 M1 等。</p> 
<p>《铜豌豆 Linux》 ARM 架构此次发布的 11.3.2 版本，是基于 Debian 11.3 制作。<br> 是目前国内第一个基于最新的 Debian 11 制作的中文 Linux 发行版。<br> 2022-03-26, Debian 官方发布 11.3 版本： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2FNews%2F2022%2F20220326" target="_blank"> https://www.debian.org/News/2022/20220326</a></p> 
<h3>主要软件包版本</h3> 
<ul> 
 <li>内核: 5.10.106-1 (2022-03-17)</li> 
 <li>还支持飞腾内核：linux-image-4.19.237-atzlinux-ft8</li> 
 <li>glibc： 2.33-5</li> 
 <li>Xfce 桌面环境 4.16</li> 
 <li>Mate 桌面环境 1.24.0+4</li> 
 <li>KDE 桌面环境 5.20.5</li> 
 <li>Gnome 桌面环境 3.38+3</li> 
 <li>小企鹅输入法 fcitx 4.2.9.8-3</li> 
 <li>liblunar-calendar-gtk3-module 农历 3.0.1-2</li> 
 <li>可以在 Xfce、MATE、Gnome 等桌面环境的默认日历程序中，直接显示农历和中国节假日信息</li> 
 <li>wps 11.1.0.10920</li> 
 <li>微信</li> 
 <li>请在铜豌豆软件源安装，目前有 2.0 和 2.1 两个版本，功能各有所长。这两个版本，可以同时安装。</li> 
 <li>钉钉 1.3.0.20214</li> 
 <li>chromium 99.0.4844.84-1</li> 
 <li>火狐浏览器 91.7.0esr-1~deb11u1</li> 
 <li>雷鸟邮件客户端 thunderbird 91.7.0-2~deb11u1</li> 
 <li>星际译王 stardict-gtk 3.0.7+git20211225+dfsg-1~bpo11+1</li> 
 <li>opengnb 1.2.8.5-1</li> 
 <li>方便快捷搭建 VPN 网络，内网穿透，国人自己开发，特别适合国内网络环境，速度极快。</li> 
</ul> 
<h3>安全更新</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2Fsecurity%2F" target="_blank">Debian 官方软件包安全更新</a> 同步到 2022-03-30 日。</li> 
</ul> 
<h3>铜豌豆 ARM 架构软件源</h3> 
<p>与 ARM 架构操作系统，同步推出 ARM 架构铜豌豆软件源：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fallpackages-arm64.htm" target="_blank">https://www.atzlinux.com/allpackages-arm64.htm </a></p> 
<p>目前 ARM 架构的中文 Linux 应用软件还比较少，后续逐步丰富。 大家也可以从软件厂商网站，或者其它 Linux 发行版上下载 deb 软件包安装。</p> 
<h3>飞腾 4.19.x 内核</h3> 
<p>飞腾机器部分机型，在 《铜豌豆 Linux》默认的 5.10.x 内核下，部分设备没有驱动。 大家可以使用打过飞腾补丁的内核来解决驱动问题。</p> 
<ul> 
 <li>该内核是将飞腾公司提供的针对 4.19.x 内核的第 8 版补丁，在官方内核 4.19 LTS 最新版的 4.19.237（2022-03-28 发布）上应用， 制作内核的 deb 包：linux-image-4.19.237-atzlinux-ft8</li> 
 <li>iso 安装</li> 
 <li>文件路径为： <em>pool/main/l/linux-4.19.237-atzlinux-ft8/linux-image-4.19.237-atzlinux-ft8_4.19.237-atzlinux-ft8-1_arm64.deb</em> <p>登录系统后，重新拔插下 U 盘，让 U 盘自动挂载，在命令行进入挂载目录，用 root 账号安装该内核软件包：<br> dpkg -i linux-image-4.19.237-atzlinux-ft8_4.19.237-atzlinux-ft8-1_arm64.deb</p> </li> 
 <li>对于安装完成后，网络可以正常使用的情况</li> 
 <li>可以直接用铜豌豆商店，或者 apt 命令安装该内核。 <p>apt install linux-image-4.19.237-atzlinux-ft8</p> </li> 
</ul> 
<h3>下载</h3> 
<p>安装文件大小约 3 G，下载地址如下：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapt.atzlinux.com%2Fatzlinux-cd%2F11.3.2%2Farm64%2Fiso-dvd%2Fatzlinux-11.3.2-arm64-DVD-1.iso" target="_blank">https://apt.atzlinux.com/atzlinux-cd/11.3.2/arm64/iso-dvd/atzlinux-11.3.2-arm64-DVD-1.iso </a></p> 
<hr> 
<ul> 
 <li>系统默认创建两个用户，一个是具有最高系统权限的管理员用户 root ；一个是名字为 wo 的普通用户。</li> 
 <li>root 用户可以直接登录系统， <em><span style="color:#ff0000"><span><strong>初始密码</strong></span></span></em>为：</li> 
 <li><em>debian-cn;168</em><br> 中间为英文的连接符，英文的分号</li> 
 <li>普通用户名为： <strong>wo</strong> ，<strong>初始密码</strong>为：</li> 
 <li><em>debian168;</em><br> 最后一个字符是英文的分号 
  <hr></li> 
</ul> 
<p>下载的安装文件名为：<em>atzlinux-11.3.2-arm64-DVD-1.iso</em><br> 下载完成后，可进行完整性验证，支持校验和、公钥签名验证。 验证所需<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fatzlinux-cd%2F11.3.2%2Farm64%2Fiso-dvd%2F" target="_blank">相关文件请访问这里</a>获取。</p> 
<p>该 iso 安装文件，支持目前国内市场上常用的 ARM v8 指令集 64 位 CPU，如飞腾、鲲鹏等。</p> 
<h3>无缝升级</h3> 
<p>请用 root 用户运行下列命令，一键更新所有软件包到最新版本：<br> <br> <em>apt update<br> apt upgrade </em></p> 
<h3>iso 文件信息：</h3> 
<ul> 
 <li>iso 文件软件包完整列表：</li> 
 <li><a href="https://gitee.com/atzlinux/debian-cn/blob/arm/isodvd/11.3/atzlinux-11.3.2-arm64-DVD-1.list" target="_blank">https://gitee.com/atzlinux/debian-cn/blob/arm/isodvd/11.3/atzlinux-11.3.2-arm64-DVD-1.list </a></li> 
</ul> 
<h4>已知问题</h4> 
<ul> 
 <li>安装阶段</li> 
 <li>USB 2.0 3.0 插口</li> 
 <li>目前机器多同时具备 USB 2.0 和 USB 3.0 两种 USB 接口。U 盘接口也分USB 2.0 和 USB 3.0 两种类型。 U 盘接口为 USB 2.0 的，请插入机器 USB 2.0 插口安装； U 盘接口为 USB 3.0 的，请插入机器 USB 3.0 插口安装， 插错接口有可能导致安装程序无法启动，无法出现安装界面等问题。</li> 
 <li>部分 USB 外接无线网卡在安装过程中，无法自动识别</li> 
 <li>当出现无法找到网卡提示时，可以尝试将该外接无法网卡从 USB 接口中拔出，再重新插入下。 如仍无法识别，请先继续使用无网络方式完成安装，部分网卡类型，可以在机器完成安装后识别。</li> 
 <li>飞腾机器部分网卡无法自动获取 IP 地址</li> 
 <li>部分飞腾机型网卡，在安装时能够识别，但无法通过 DHCP 自动获取 IP 地址。 请先继续使用无网络方式完成安装，该类网卡可以在机器完成安装后使用网络。</li> 
 <li>硬盘分区选择全盘安装自动分区时，提示 EFI 分区错误</li> 
 <li>请忽略该错误，继续完成安装即可。</li> 
 <li>部分飞腾机型，存在 EFI 不兼容，导致安装最后失败，无法完成的情况。</li> 
 <li>部分飞腾机器安装完成后，第一次启动时，在 EFI 机器引导启动界面报错</li> 
 <li>需要按界面提示的手工按键（如 ESC 键等），进入 EFI 菜单，选择硬盘 EFI 条目进入系统。 <p>该问题，只会在第一次启动时出现，后续会自动进入系统。 已经告知机器硬件厂家确认，反馈需要进行 EFI 版本升级，不是铜豌豆 Linux 操作系统本身问题。</p> </li> 
 <li>个别飞腾机器老版本 EFI bug</li> 
 <li>旧版本 EFI 有 bug ，会在安装时，导致 EFI 损坏。请在安装前联系硬件厂家，获取最新版的 EFI。</li> 
</ul> 
<h4>其它事项</h4> 
<p>root 账号登录系统出现：</p> 
<ol> 
 <li>点击象棋、围棋程序，会报错</li> 
 <li>默认声音图标显示为静音</li> 
 <li>无法打开声音，不能够播放声音</li> 
 <li>无法打开 chromium 浏览器</li> 
</ol> 
<p>以上为正常现象。这是由于 Debian 的安全机制，不建议 root 用户直接使用日常应用程序。请用普通账号登录系统使用相关功能。</p> 
<h3>问题反馈</h3> 
<p>欢迎大家反馈问题，请前往《铜豌豆 Linux》项目码云组织，反馈问题：</p> 
<p><a href="https://gitee.com/atzlinux/debian-cn/issues/I50BYT" target="_blank">https://gitee.com/atzlinux/debian-cn/issues/I50BYT</a></p> 
<p>积极反馈问题，也是在参与开源项目，向开源项目做贡献。</p> 
<h3>《铜豌豆 Linux 11 版本》维护期</h3> 
<p>该版本维护期至 2026 年 8 月。</p> 
<p>在 Debian 11 版于 2021 年 8 月正式发布后，Debian 官方将维护三年至 2024 年 8 月 ，随后 Debian 的 LTS 团队将再继续维护两年。 LTS 维护相关情况，请参阅： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FLTS" target="_blank"> https://wiki.debian.org/LTS</a></p> 
<p><strong>铜豌豆 Linux 11 版本系列，将跟随 Debian 官方和 Debian LTS 的版本继续进行维护和更新发布。</strong></p> 
<h4>感谢</h4> 
<ul> 
 <li>首先要感谢 《铜豌豆 Linux》社区的各位热心网友的热情 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.atzlinux.com%2Fjuanzeng.htm%23arm" target="_blank"> 捐赠众筹</a></li> 
 <li>要是没有大家的鼓励和支持，《铜豌豆 Linux》项目便不会开发 ARM 架构版本。</li> 
 <li>其次要感谢北京予先、广州汉为公司提供测试机器，并积极配合解决各类问题</li> 
 <li>感谢龙蜥社区，帮忙联系飞腾，提供飞腾 4.19 内核补丁</li> 
 <li>《铜豌豆 Linux》社区和龙蜥 Linux 社区，在此事情上，进行了非常有意义的合作。</li> 
</ul>
                                        </div>
                                      
</div>
            