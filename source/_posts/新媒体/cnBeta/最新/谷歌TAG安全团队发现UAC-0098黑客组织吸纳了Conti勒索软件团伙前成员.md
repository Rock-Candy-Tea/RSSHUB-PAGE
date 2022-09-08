
---
title: '谷歌TAG安全团队发现UAC-0098黑客组织吸纳了Conti勒索软件团伙前成员'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0908/5a07933354634e5.png'
author: cnBeta
comments: false
date: Thu, 08 Sep 2022 06:53:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0908/5a07933354634e5.png'
---

<div>   
<strong>谷歌威胁分析小组（TAG）在周三的一篇文章中提到 —— 某个吸纳了前 Conti 勒索软件团伙的网络犯罪组织，正针对乌克兰政府和欧洲非政府组织发起攻击。</strong>明面上，俄乌冲突已经持续了半年多。但在幕后，包括黑客攻击和电子战在内的网络活动，也一直在暗中展开较量。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0908/5a07933354634e5.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">文件分享网站上的 UAC-0098 有效载荷（图自：Google <a href="https://blog.google/threat-analysis-group/initial-access-broker-repurposing-techniques-in-targeted-attacks-against-ukraine/" target="_self">TAG</a>）</p><p>最新消息是，TAG 的 Pierre-Marc Bureau 指出 —— 追求利润的网络犯罪组织，也在该领域变得愈加活跃。</p><blockquote><p>2022 年 4-8 月，TAG 一直在追踪涉乌网络行动。有线索表明它们与得到俄方支持的攻击者密切相关。</p><p>其中之一，已被乌克兰国家计算机紧急响应小组（CERT）指定为 UAC-0098 。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0908/80a8e882b6c9eed.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">托管的被盗线索</p><p>与此同时，TAG 又将之与肆虐全球的 Conti 勒索软件团伙联系了起来 —— 今年 5 月，该组织曾攻击瘫痪了哥斯达黎加的政府机构。</p><blockquote><p>基于多项分析评估指标，TAG 认定 UAC-0098 的部分团伙、也是 Conti 网络犯罪组织的前成员，理由是他们将类似的技术运用到了针对乌克兰的目标上。</p></blockquote><p>此前该组织有使用名为 IcedID 的网银木马来开展勒索软件攻击。但 Google 安全研究人员称，其现又转向了“既有政治动机、也受利益趋势”的攻击活动。</p><p><img src="https://static.cnbetacdn.com/article/2022/0908/e02a1f1e11bd55b.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">钓鱼邮件示例（翻译自乌克兰语）</p><p>TAG 分析，该组织成员正利用其专业知识来充当初始访问代理 —— 黑客先是破坏了计算机系统，然后将访问权限出售给对特定目标感兴趣的其它攻击参与者。</p><p>在最近的一轮活动中，UAC-0098 向乌克兰酒店业的一些组织发去了网络钓鱼电子邮件，并且假借了网警的身份。</p><p>在另一个案例中，该组织还通过一家被黑的印度酒店的邮件地址，向意大利的一个人道主义非政府组织发起了钓鱼攻击。</p><p>其它活动还涉嫌冒充星链互联网卫星服务的代表，以引诱受害者安装所谓的必要联网软件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0908/9ffdeae41dd74ce.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">PowerShell 脚本示例</p><p>最后，这家与 Conti 有染的黑客组织，还曾于 5 月下旬的首次公开后不久，就利用了 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 操作系统中的 Follina 漏洞。</p><p>不过 TAG 表示，在本次和其它攻击活动中，他们尚不清楚 UAC-0098 在初始攻击得逞后还采取了哪些行动。</p><p>当然，此类黑客攻击也并不总是能笑到最后。比如在俄乌冲突爆发初期，高调宣布挺俄的该组织，就被某匿名个人泄露了它们内部一年多的聊天记录。</p>   
</div>
            