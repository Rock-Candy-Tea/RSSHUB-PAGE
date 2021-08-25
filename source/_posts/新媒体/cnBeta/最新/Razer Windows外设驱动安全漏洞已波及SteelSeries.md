
---
title: 'Razer Windows外设驱动安全漏洞已波及SteelSeries'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0825/d2c424263fcbca9.jpg'
author: cnBeta
comments: false
date: Wed, 25 Aug 2021 09:07:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0825/d2c424263fcbca9.jpg'
---

<div>   
几天前，安全研究人员 jonhat 曝光了存在于 Razer Synapse 软件中的一个零日漏洞，或被攻击者用于在本机获得 SYSTEM 级别的管理员账户权限。极端情况下，攻击者只需购买一只几十元的 Razer 鼠标即可得逞。<strong>不出所料的是，该漏洞同样影响到了包括赛睿（SteelSeries）在内的其它 PC 外设制造商。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0825/d2c424263fcbca9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0825/d2c424263fcbca9.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">视频截图（via @zux0x3a）</p><p>利用 LPE 漏洞，攻击者可通过在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 / 11 PC 上插入键鼠等外设时，等待系统自动下载安装实用工具软件时，轻松达成本地账号提权的目的。</p><p>尽管达成目的仍需物理接触到一台 Windows PC，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://razer.jd.com/" target="_blank">雷蛇</a>（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://razer.jd.com/" target="_blank">RAZER</a>）、赛睿（SteelSeries）这两家外设大厂遭遇的驱动程序软件 LPE 漏洞，还是对行业敲响了警钟。</p><p><img src="https://static.cnbetacdn.com/article/2021/0825/c141ebf9a1dac74.png" alt="1.png" referrerpolicy="no-referrer"></p><p>问题在于 Windows 10 / 11 操作系统会在外设驱动安装阶段，默认使用 SYSTEM 级别的高权限账户。</p><p>而后被攻击者在继承管理员权限的情况下，利用相同的系统访问权限打开命令提示符（CMD）或 PowerShell 实例。</p><p>换言之，这使得攻击者能够对目标计算机执行包括安装恶意软件在内的几乎任何操作。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=282759631&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">Just another priv_escalation with SteelSeries - zux0x3a（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjgyNzU5NjMxLnNodG1s.html" target="_self">via</a>）</p><p>0xsp 的 Lawrence Amer 指出，Razer 和 SteelSeries 软件安装程序也存在同样的漏洞。</p><p>尽管驱动安装耗时不尽相同，但攻击者仍可通过一系列骚操作而得逞。</p><p>首先在浏览器中查看许可协议、尝试保存网页、然后从出现的对话框中右键启动 PowerShell 。</p><p><img src="https://static.cnbetacdn.com/article/2021/0825/38605070183fce8.png" alt="2.png" referrerpolicy="no-referrer"></p><p>此外另一位网名叫 @an0n_r0 的安全研究人员发现，攻击者甚至可以伪造 SteelSeries 产品，而无需插入任何实际的外设，以达成同样的目的。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=282759478&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">Proof of Concept video for SteelSeries LPE - an0n_r0（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjgyNzU5NDc4LnNodG1s.html" target="_self">via</a>）</p><p>演示期间，其通过 Android 模拟脚本触发了这一驱动安装过程。不过虽然该脚本同样可将<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>伪装成 Razer 外设，但 Bleeping Computer 表示该过程无需用户交互，因而并未触发 Razer 的漏洞。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1169677.htm" target="_blank">Razer Synapse零日漏洞曝光：插上鼠标即可获得SYSTEM账户权限</a></p></div>   
</div>
            