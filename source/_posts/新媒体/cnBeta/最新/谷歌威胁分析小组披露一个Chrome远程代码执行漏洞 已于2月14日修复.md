
---
title: '谷歌威胁分析小组披露一个Chrome远程代码执行漏洞 已于2月14日修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0325/7ee6751f22cefa3.png'
author: cnBeta
comments: false
date: Fri, 25 Mar 2022 05:05:30 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0325/7ee6751f22cefa3.png'
---

<div>   
<strong>谷歌威胁分析小组（TAG）近日指出：早在 2022 年 1 月 4 日，他们就留意到了针对 Chrome 浏览器的一个漏洞利用工具包。</strong>然后 2 月 10 日，其追踪发现两个疑似有朝鲜背景的团体也在利用相应的手段，向美国新闻、IT、加密货币和金融科技站点发起了攻击。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0325/7ee6751f22cefa3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0325/7ee6751f22cefa3.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">钓鱼网站示例（图 via Google <a href="https://blog.google/threat-analysis-group/countering-threats-north-korea/" target="_self">Blog</a>）</p><p>庆幸的是，这家科技巨头于 2 月 14 日成功修补了该漏洞。鉴于所有攻击者都利用相同的漏洞工具包，TAG 推测他们可能是从同一个上游供应商那里获取的。</p><p>期间，谷歌从新闻媒体从业者那里收到了一些报告，得知有攻击者假装是迪士尼、谷歌、甲骨文的招聘人员，向他们发去了钓鱼邮件。其中包含了指向虚假网站的链接，比如 ZipRecruiter 和 Indeed 等招聘门户网站的镜像。</p><p>与此同时，金融科技和加密货币公司也被伪装成合法企业的钓鱼链接所欺骗。任何点击链接的人，都会被隐藏于受感染的网站中的 iframe 代码给触发漏洞利用。</p><p><a href="https://static.cnbetacdn.com/article/2022/0325/2696c687d90ff71.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0325/2696c687d90ff71.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>至于这个漏洞利用工具包，起初仅提供一些针对目标系统开展指纹识别的严重混淆 JavaScript 代码。</p><blockquote><p>该脚本会收集所有可用的客户端信息，比如用户代理、分辨率等，然后将其发回给漏洞利用服务。</p><p>若满足一组未知的要求，客户端将被推送包含 Chrome 远程代码执行（RCE）漏洞利用的额外 JavaScript 代码。</p><p>得逞之后，该脚本还会请求下一阶段的沙箱逃逸（简称 SBX）代码，可惜 TAG 团队未能深入获取更多细节。</p></blockquote><p>此外攻击者利用了几套复杂的方法来隐藏他们的活动，包括仅在目标访问网站的预期访问时间段内启用 iframe、用于一次性点击的唯一 URL 链接实现、以及利用 AES 加密步骤和管道的原子性。</p><p>最后，尽管 Google 早在 2 月 14 日就修复了 Chrome 中的 REC 漏洞，但该公司还是希望通过披露这些细节，以敦促用户尽快接收浏览器的最新安全补丁、并在 Chrome 中启用增强安全浏览选项。</p>   
</div>
            