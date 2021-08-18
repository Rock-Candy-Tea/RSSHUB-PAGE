
---
title: 'Ursnif木马变种正利用CAPTCHA验证来欺骗并窃取受害者信息'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0818/9523a7529c8efe0.jpg'
author: cnBeta
comments: false
date: Wed, 18 Aug 2021 04:01:08 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0818/9523a7529c8efe0.jpg'
---

<div>   
Bleeping Computer 报道称：<strong>Ursnif 网银木马的一个新变种（又称 Gozi），正在对粗心的受害者展开基于无害验证码的欺骗攻击，以窃取他们的敏感信息。</strong>MalwareHunterTeam 曝光了这款变种木马，可知当试图通过特定 URL 观看嵌入页面的 YouTube 视频时，它会引诱受害者下载一个所谓“console-play.exe”的恶意文件。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0818/9523a7529c8efe0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0818/9523a7529c8efe0.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">恶意网站截图</p><p>恶意网站会显示一个虚假的 reCAPTCHA 验证界面，以证明访客是真人而不是机器人。</p><p>同时由于这个“播放控制台”是一个可执行文件，浏览器会向用户发出潜在的恶意软件威胁警告。即便如此，毫无戒心的用户还是很容易上钩。</p><p><a href="https://static.cnbetacdn.com/article/2021/0818/ad998a5928b7daf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0818/ad998a5928b7daf.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">虚假的 reCAPTCHA 人机验证界面</p><p>如上图所示，该网站会要求用户依次按下 B、S、Tab、A、F、以及回车键。对于熟悉快捷键操作的熟练计算机用户来说，明显知道 BSAF 这几个字母其实都是幌子。</p><p>因为在当前界面下，一旦你按下了 Tab 和回车键，就有可能在不知不觉中将 Ursnif 木马程序给保留下来。此时网页视频也会继续播放，因此具有相当大的迷惑性。</p><p><a href="https://static.cnbetacdn.com/article/2021/0818/d0a2e8b59848227.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0818/d0a2e8b59848227.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">.NET Helper 文件夹中的内容</p><p>如果下载运行了 console-play.exe，就会在系统 AppData 下的 Roaming 路径，创建一个名为“Bouncy for .NET Helper”的文件夹。</p><p>为了混淆视听，恶意软件制作者还特意在“BouncyDotNet.exe”主程序之外，夹杂了大量的诱饵文件。</p><p><a href="https://static.cnbetacdn.com/article/2021/0818/df4c78da233da7a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0818/df4c78da233da7a.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">注册表详情</p><p>据悉，BouncyDotNet.exe 会创建有助于 Ursnif 网银木马传播的感染性动态链接库（DLL）文件，以进一步窃取与凭证相关的敏感信息。</p><p>但这其实并不是本年度的第一波 Ursnif 恶意软件攻击，因为 Avast 早在 3 月份就指出，这款网银木马已经导致意大利 100 多家银行躺枪。</p>   
</div>
            