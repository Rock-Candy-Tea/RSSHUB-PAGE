
---
title: 'Group-IB：0ktapus网络钓鱼攻击导致Twilio等130个组织的上万凭据被窃取'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0816/9ee5fd726853b9b.jpg'
author: cnBeta
comments: false
date: Mon, 29 Aug 2022 07:02:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0816/9ee5fd726853b9b.jpg'
---

<div>   
两周前，Twilio 和 Cloudflare 披露了一场精心策划的网络钓鱼攻击，导致两家公司员工的账户凭据被泄露。其中 Twilio 的两步验证（2FA）系统被攻破，导致攻击者能够访问其内部系统。<strong>现在，安全研究人员已找到这轮大规模网络钓鱼攻击的幕后黑手，可知 130 个组织近 10000 个账户凭据受到了被窃取。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0816/9ee5fd726853b9b.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>由 Twilio 和 Cloudflare 披露的细节可知，这轮网络钓鱼攻击有着相当于外科手术的精确度和执行计划。</p><p>首先，攻击者通过不明渠道获得了员工的私人电话号码（某些情况下还套路到了其家人的号码），然后通过发送短信来忽悠员工登录精心伪造的身份验证页面。</p><p><a href="https://static.cnbetacdn.com/article/2022/0829/7ac3f7f1b7630cc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0829/7ac3f7f1b7630cc.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">受害者遭遇的常规网络钓鱼套路（图自：<a href="https://www.group-ib.com/media/0ktapus-campaign/" target="_self">Group-IB</a>）</p><p>40 分钟内，76 名 Cloudflare 员工陆续收到了钓鱼短信 —— 其中包含一个在攻击实施 40 分钟前才注册的域名，以绕过该公司对假冒威胁站点的黑名单防护策略。</p><p>紧接着，网络钓鱼攻击者利用了代理站点来实时执行劫持，并截获了 Twilio 双因素（2FA）身份验证用的一次性验证码、并将之套用到了真实站点。</p><p><a href="https://static.cnbetacdn.com/article/2022/0829/dfd2999d1f8bd41.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0829/dfd2999d1f8bd41.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">区域波及范围</p><p>于是几乎在同一时间，攻击者利用其对 Twilio 网络的访问权限、窃取了 Signal Messenger 约 1900 名用户的电话号码。</p><p>由 Group-IB 周四发布的安全报告可知，Twilio 被卷入了一场被称作“<a href="https://sec.okta.com/scatterswine" target="_self">0Ktapus</a>”的更大规模的网络钓鱼攻击事件。过去六个月时间里，同样的套路导致 130 个组织的 9931 个凭据被泄露。</p><p><a href="https://static.cnbetacdn.com/article/2022/0829/60b9990a0ffb71b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0829/60b9990a0ffb71b.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">行业波及范围</p><p>分析发现，为了引诱受害者上钩，幕后攻击者利用了至少 169 个独特的互联网域名 —— 常见包含单点登录（SSO）、虚拟专用网、多因素认证（MFA）、帮助（HELP）等关键词。</p><p>为了充分利用既有的攻击手段，幕后黑客选择了通过此前未知的、但相同的网络钓鱼工具包来打造钓鱼网站，且规模和范围前所未有 —— 至少从 2022 年 3 月持续至今。</p><p><img src="https://static.cnbetacdn.com/article/2022/0829/ee6739865856583.jpg" alt="6.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">疑似昵称“X”的管理员信息</p><p>Group-IB 研究人员补充道，正如 Signal 披露的那样，一旦攻击者成功侵入了一个组织，它们就能够迅速转向、并发起后续的一系列供应链攻击。</p><p>虽然没有指出到底有哪些公司受到了影响，仅称其中至少有 114 家位于美国、或在美设有分支机构的企业 —— 其中 IT、软件开发和云服务公司成为了 0ktapus 钓鱼攻击的首要目标。</p><p><img src="https://static.cnbetacdn.com/article/2022/0829/9f448c0997f3a33.jpg" alt="7.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">安全研究人员推测攻击者位于北卡罗来纳州</p><p>周四的时候，<a href="https://sec.okta.com/scatterswine" target="_self">Okta</a> 也在一篇帖子中透露了其为受害者之一。可知钓鱼攻击者会引诱受害者至 Telegram 频道，以绕过基于一次性验证码的 2FA 验证防护。</p><p>当受害者在精心伪造的站点上输入用户名和密码时，机密信息会即刻传递给攻击者、并导致真实站点沦陷。</p><p>ArsTechnica <a href="https://arstechnica.com/information-technology/2022/08/phishers-who-hit-twilio-and-cloudflare-stole-10k-credentials-from-136-others/" target="_self">指出</a> —— 此类事件的不断上演，揭示了现代组织在面对手段并不高明的社会工程攻击时的脆弱性、及其对合作伙伴与客户能够造成的深远影响。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1304909.htm" target="_blank">Signal披露1900名客户电话号码因Twilio攻击事件而被泄露</a></p></div>   
</div>
            