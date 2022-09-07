
---
title: 'OpenWrt 22.03 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4974'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4974'
---

<div>   
<div class="content">
                                                                                            <p>OpenWrt 22.03 稳定版系列的第一个稳定版本现已发布。自之前的 OpenWrt 21.02 版本分支以来，该版本包含了超过 3800 次 commit，并且已经开发了大约一年的时间。OpenWrt Project 是一个针对嵌入式设备的 Linux 操作系统，它用于取代供应商提供的各种无线路由器和非网络设备固件。</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffirmware-selector.openwrt.org%2F%3Fversion%3D22.03.0" target="_blank">Download firmware image for your device (firmware selector)</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.openwrt.org%2Freleases%2F22.03.0%2Ftargets%2F" target="_blank">Download firmware images directly from OpenWrt download servers</a></p> </li> 
</ul> 
<h4>OpenWrt 22.03.0 的亮点</h4> 
<p><strong>基于 nftables 的 Firewall4 防火墙</strong></p> 
<p>Firewall4 现已替代<code>firewall3</code>成为 OpenWrt 镜像中的默认防火墙配置软件. Firewall4 使用了 nftables 而不是 iptables 来配置 Linux 的网络过滤器。</p> 
<p>Firewall4 的 UCI 配置界面与之前的防火墙配置界面一致。旧的防火墙配置会无缝迁移到 firewall4，并使用 nftables。但是，自定义 iptables 命令选项在 Firewall4 中会失效。</p> 
<p><code>iptables</code>不再默认在固件中安装。若有需要，你可以通过 opkg 或者<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Fguide-user%2Fadditional-software%2Fimagebuilder" target="_blank">ImageBuilder</a>来安装。<code>iptables-nft</code>,<code>arptables-nft</code>,<code>ebtables-nft</code>和<code>xtables-nft</code>可以在使用 nftables 的情况下，提供与之前的命令相同的接口。</p> 
<p><strong>新设备支持</strong></p> 
<p>相较于 OpenWrt 21.02，OpenWrt 22.03 又新增了约 180 款设备的支持。OpenWrt 22.03 现支持超过 1580 款设备。 OpenWrt 22.03 支持了超过 15 款使用联发科 MT7915 主控的 Wifi 6 (IEEE 802.11ax) 设备。</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Ftechref%2Ftargets%2Fqoriq" target="_blank">qoriq</a>: NXP QorIQ (PowerPC) 在 OpenWrt 22.03 已受支持</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Ftechref%2Ftargets%2Fbmips" target="_blank">bmips</a>: Boardcom MIPS BCM33xx, BCM63xx 和 BCM7xxx SoC 也已支持.</p> </li> 
</ul> 
<p><strong>更多设备迁移到 DSA</strong></p> 
<p>下列设备在 OpenWrt 22.03 中也从 swconfig 迁移到了 DSA：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Ftechref%2Ftargets%2Fbcm53xx" target="_blank">bcm53xx</a>: 所有设备</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Ftechref%2Ftargets%2Flantiq" target="_blank">lantiq</a>: 使用了 xrx200 / vr9 SoC 的设备</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fdocs%2Ftechref%2Ftargets%2Fsunxi" target="_blank">sunxi</a>: Bananapi Lamobo R1 (仅带有交换机的 sunxi 设备)</p> </li> 
</ul> 
<p><strong>LuCI 的黑暗模式</strong></p> 
<p>LuCI bootstrap 界面现已支持黑暗模式，其默认配置是跟随浏览器设定，此配置可以在 “系统” → “系统” → “语言与样式” 中修改。</p> 
<p><strong>解决了 2038 年问题</strong></p> 
<p>OpenWrt 22.03 使用的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmusl.libc.org%2Ftime64.html" target="_blank">musl 1.2.x</a>将 32 位系统上的<code>time_t</code>类型从 32 位改为了 64 位长，而 64 位系统的长度早已是 64 位。 当 Unix 时间戳存储于有符号32位整数上时，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FYear_2038_problem" target="_blank">它会于 2038 年 1 月 19 日溢出</a>。将这一类型改为 64 位后，溢出则会发生在 2000 亿年后。 这项改动修改了 musl libc 的 ABI 接口，因此需要重新编译所有链接到 musl libc 的用户程序。 对于 64 位系统，这项工作已于很多年前完成；ARC 上的 glibc 的<code>time_t</code>也早已是 64 位长度。</p> 
<p><strong>核心组件升级</strong></p> 
<p>在 22.03.0-rc6 中，以下核心组件均已升级:</p> 
<ul> 
 <li> <p>工具链升级:</p> 
  <ul> 
   <li> <p>musl libc 1.2.3</p> </li> 
   <li> <p>glibc 2.34</p> </li> 
   <li> <p>gcc 11.2.0</p> </li> 
   <li> <p>binutils 2.37</p> </li> 
  </ul> </li> 
 <li> <p>Linux 内核</p> 
  <ul> 
   <li>5.10.138: 所有设备</li> 
  </ul> </li> 
 <li> <p>网络:</p> 
  <ul> 
   <li> <p>hostapd 2.10, dnsmasq 2.86, dropbear 2022.82</p> </li> 
   <li> <p>Linux 内核 5.15.58 的 cfg80211/mac80211</p> </li> 
  </ul> </li> 
 <li> <p>系统用户程序:</p> 
  <ul> 
   <li>busybox 1.35.0</li> 
  </ul> </li> 
</ul> 
<p>除此之外，其他软件的升级可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Freleases%2F22.03%2Fchangelog-22.03.0" target="_blank">详细的更新日志</a>。</p> 
<h4><strong>升级到 22.03.0</strong></h4> 
<p>可以使用系统升级工具将你的设备从 21.02 升级到 22.03，在大部分情况下你的设置会被保留；也可以从之前的 22.03.0 预览版升级到正式版。</p> 
<p>不支持使用系统升级工具从 19.07 升级到 22.03。</p> 
<p>无法将传统的 swconfig 配置升级到 DSA 配置。在这种情况下，系统升级工具将会拒绝升级并报以下错误：<code>Image version mismatch. image 1.1 device 1.0 Please wipe config during upgrade (force required) or reinstall. Config cannot be migrated from swconfig to DSA Image check failed</code></p> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenwrt.org%2Fzh%2Freleases%2F22.03%2Fnotes-22.03.0" target="_blank">查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            