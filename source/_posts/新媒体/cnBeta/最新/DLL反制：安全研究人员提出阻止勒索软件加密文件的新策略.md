
---
title: 'DLL反制：安全研究人员提出阻止勒索软件加密文件的新策略'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0505/af71d8ca9357d44.jpg'
author: cnBeta
comments: false
date: Thu, 05 May 2022 05:51:58 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0505/af71d8ca9357d44.jpg'
---

<div>   
尽管恶意软件开发者擅长利用各种软硬件漏洞来达成目的，但他们散播的成品也并非毫无破绽。<strong>比如近日，安全研究人员 John Page（又名 hyp3rlinx）就介绍了一招反制勒索软件的新套路。</strong>由个人网站和 Twitter 账号上发布的内容可知，John Page 专精于找到恶意软件本身的漏洞，并于近日分享了阻止勒索软件加密受害者文件的方法。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0505/af71d8ca9357d44.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0505/af71d8ca9357d44.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">视频截图（来自：malvuln / YouTube）</p><p>据悉，许多勒索软件都会被 DLL 劫持所影响。通常攻击者会利用这种动态链接库来诱骗程序加载，以运行他们预期中的恶意代码。</p><p>但转念一想，你也大可合理利用该技术来“反劫持”并阻止某些类型的勒索软件。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=346115086&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">Ransom WannaCry - Code Execution Vulnerability（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzQ2MTE1MDg2LnNodG1s.html" target="_self">via</a>）</p><p>John Page 在网站上分享了针对 REvil、Wannacry、Conti 等最新版恶意软件的漏洞和自定义 DLL 的详情。</p><p>可知要顺利解套，DLL 需在攻击者可能放置恶意软件的潜在目录中守株待兔。</p><p><img src="https://static.cnbetacdn.com/article/2022/0505/c6e61448db970b4.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Malvuln <a href="https://www.malvuln.com/" target="_self">网站</a>）</p><p>John Page 还建议采用分层策略，比如将之放在包含重要数据的网络共享上。</p><p>由于动态链接库不会在勒索软件访问它们之前被调用，因而此举可无视绕过反病毒软件防护的勒索软件活动。</p><p><a href="https://static.cnbetacdn.com/article/2022/0505/72d83f23477dd77.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0505/72d83f23477dd77.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>遗憾的是，DLL 反劫持套路只适用于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 操作系统，而无法轻松照搬到 Mac、Linux 或 Android 平台上。</p><p>此外它只能尝试避免被勒索软件加密文件，而不能阻止被攻击者访问系统和泄露数据。</p>   
</div>
            