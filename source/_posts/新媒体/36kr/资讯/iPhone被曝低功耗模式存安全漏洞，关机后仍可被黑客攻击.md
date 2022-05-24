
---
title: 'iPhone被曝低功耗模式存安全漏洞，关机后仍可被黑客攻击'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220524/v2_8db5ab1899664b6b8acfd35f07c285e9_img_000'
author: 36kr
comments: false
date: Tue, 24 May 2022 06:11:26 GMT
thumbnail: 'https://img.36krcdn.com/20220524/v2_8db5ab1899664b6b8acfd35f07c285e9_img_000'
---

<div>   
<p>近日，一项来自德国达姆施塔特工业大学的论文指出了苹果iOS15版本下LPM模式的安全风险。论文指出，苹果公司并没有为低功耗模式（LPM）下仍然运行的蓝牙芯片配备数字签名机制，也没有对运行固件进行加密。利用这个漏洞，恶意软件可以在手机关机时继续运行，并且更加隐蔽。</p> 
<p>当用户主动关机或者因为电量不足而关机，手机会进入LPM模式。不同于低电量模式，LPM模式允许关机状态下的近场通信（NFC）、超宽带（UWB）和蓝牙芯片在一种特殊模式下工作，可以持续24小时。</p> 
<p>基于这个模式，iPhone用户可以在关机后继续使用“查找”功能定位自己的设备，以及通过NFC使用苹果钱包和数字汽车钥匙等功能。</p> 
<p>作者在论文中展示了LPM模式下攻击关机iPhone的可能性。论文指出，LPM模式下的许多安全屏障都可以被破坏。例如，在使用Find My等功能时，用以保护固件不被篡改的补丁可以被修改，利用这些漏洞，攻击者可以控制用户的LPM权限，如禁用用户的查找定位功能，获取和影响一些隐私信息。</p> 
<p>“LPM功能的设计似乎主要由功能驱动，没有考虑预期应用程序之外的威胁。”作者称这是第一篇对iPhone无线芯片安全风险进行研究的论文，这项研究将发表在国际无线安全研究领域顶级学术会议ACM WiSec上。</p> 
<p>安全专家奇安盘古CEO韩争光对界面新闻记者分析，苹果手机在关机后蓝牙模块仍然能访<a class="project-link" data-id="1679802853905161" data-name="问安" data-logo="https://img.36krcdn.com/20220401/v2_f7b9874917e745ef891545ab1aa14fd7_img_000" data-refer-type="1" href="https://36kr.com/project/1679802853905161" target="_blank">问安</a>全处理器的一些数据，这显然是一个安全隐患，攻击者一旦掌握了对蓝牙固件的攻击能力，其造成的危害绝非影响查找等功能如此简单。</p> 
<p class="image-wrapper"><img data-img-size-val="700,243" src="https://img.36krcdn.com/20220524/v2_8db5ab1899664b6b8acfd35f07c285e9_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图源：论文</p> 
<p>韩争光称，论文中亦指出，该安全问题是在越狱手机上的研究成果，攻击依赖于修改蓝牙固件或者通过漏洞获取蓝牙模块的代码执行。但对于一款没有越狱的手机而言，修改蓝牙固件仍然是一件非常困难的事情，而且查找功能依赖蓝牙模块，一旦蓝牙模块完全断电会对功能造成非常大的影响，因此其危害程度并没有想象中那么大。</p> 
<p>由于LPM模式主要在硬件上实现，所以无法通过软件更新达到风险防护。作者称，苹果公司应该在iPhone上安装一个真正的硬件电源开关（完全断开电池），以供那些关心这个问题的人使用。</p> 
<p>截至发稿，苹果公司并未对该事件进行回应。</p> 
<p>本文来自“<a href="https://www.jiemian.com/article/7502835.html" rel="noopener noreferrer nofollow">界面新闻</a>”，记者：姜菁玲，36氪经授权发布。</p>  
</div>
            