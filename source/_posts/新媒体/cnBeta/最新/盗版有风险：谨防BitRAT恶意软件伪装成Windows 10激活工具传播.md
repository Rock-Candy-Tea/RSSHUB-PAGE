
---
title: '盗版有风险：谨防BitRAT恶意软件伪装成Windows 10激活工具传播'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0322/41fc3180b7a6df7.jpg'
author: cnBeta
comments: false
date: Tue, 22 Mar 2022 09:21:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0322/41fc3180b7a6df7.jpg'
---

<div>   
<strong>近段时间，一轮新的 BitRAT 恶意软件活动正在加速传播。手段是利用非官方的微软许可证激活器，来激活盗版 Windows 操作系统。</strong>Bleeping Computer 指出，BitRAT 是一款功能强大的远程访问木马。在网络犯罪论坛和暗网市场上，它正以 20 美元的买断价，向网络犯罪分子们兜售。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0322/41fc3180b7a6df7.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">叫卖帖（图 via <a href="https://www.bleepingcomputer.com/news/security/bitrat-malware-now-spreading-as-a-windows-10-license-activator/" target="_self">Bleeping Computer</a>）</p><p>在买来恶意软件后，每位攻击者都会在 BitRAT 基础上进行打包分发，包括但不限于网络钓鱼、水坑、木马等。</p><p>AhnLab 安全研究人员最近发现，威胁参与者正在将 BitRAT 伪装成 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 专业版的激活工具，并在网盘上分享传播。</p><p>据悉，Webhards 是一项在韩国相当流行的在线存储服务，其通过社交媒体平台 / Discord 发布的直接下载链接，而吸引了大量的访问者。</p><p>但是对于粗心的网络用户来说，还是很容易被各类威胁参与者所利用的。</p><p><img src="https://static.cnbetacdn.com/article/2022/0322/bb2fbb7839bde5b.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">伪装成激活工具的恶意软件下载器</p><p>按照正规流程，用户需要通过合法渠道向<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>购买许可证以激活 Windows 10 操作系统。不过也有一些迂回方法，比如利用 Windows 7 → Windows 10 的免费升级政策。</p><p>胆子更大的一些盗版用户，会冒险搜索网络上散布的非官方激活工具，但其中混入了许多恶意软件 —— 比如上图所示的“W10DigitalActiviation.exe”。</p><p>其带有一个简洁的图形化用户界面（GUI），配上对小白“相对友好”的一键激活按键。然而点击之后，它并不会在主机系统上激活 Windows 许可证。</p><p>代码分析发现，威胁参与者会利用硬编码，从命令与控制服务器上下载名为“Software_Reporter_Tool.exe”的恶意软件（本质上是 BitRAT 恶意软件）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0322/6a3c5781503e551.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0322/6a3c5781503e551.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">恶意代码分析（实际会下载 BitRAT 恶意软件）</p><p>恶意文件的会被安装到 %TEMP% 路径，并添加到 Startup 文件夹中。为了避免被系统自带的安全软件给清除，它甚至还会将自身纳入 Windows Defender 的排除项。</p><p>在榨干了所谓“激活工具”的利用价值后，“W10DigitalActiviation.exe”会被卸磨杀驴（从系统中删除），从而只在受害者计算机上留下被夺舍的 BitRAT 恶意软件。</p><blockquote><p>对于网络犯罪分子们来说，BitRAT 的功能可谓是‘便宜又大碗’，能够从主机上窃取大量有价值的信息、执行 DDoS 攻击、绕过用户权限控制（UAC）等。</p><p>此外它还能够当做键盘记录器、监测剪贴板、访问网络摄像头、录音、窃取 Web 浏览器的凭证，甚至利用受害设备的计算资源来挖掘 XMRig 加密货币。</p><p>以及通过 SOCKS4 和 SOCKS5（UDP）通路，提供对受害者 Windows 系统的访问、隐藏虚拟网络计算（hVNC）、还有基于反向代理的远程控制。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0322/31ef2528f03c483.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0322/31ef2528f03c483.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">BitRAT 恶意软件的 C&C 控制面板</p><p>从这些功能来看，<a href="https://asec.ahnlab.com/en/32781/" target="_self">ASEC</a> 分析师认为它与 TinyNuke（及其衍生的 AveMaria / Warzone）代码有很强的相似性。</p><p>综上所述，即使抛开法律与道德因素，使用盗版软件的安全风险、仍无异于一场赌博。</p><p>用于激活非法软件副本 / 破坏知识产权保护的系统工具越多，最终感染上恶意软件的可能性就越大。即使暂时负担不起 Windows 许可证，也可考虑其它期待选项。</p><p>更重要的是，大家还是要养成良好的习惯 —— 不要轻易使用来路不明的许可证激活器、或其它由未知供应商制作并发布的未签名可执行文件。</p>   
</div>
            