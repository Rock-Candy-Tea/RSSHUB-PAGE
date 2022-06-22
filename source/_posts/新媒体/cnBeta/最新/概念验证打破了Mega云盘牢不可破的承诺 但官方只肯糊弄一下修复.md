
---
title: '概念验证打破了Mega云盘牢不可破的承诺 但官方只肯糊弄一下修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0622/562e90a892cefaa.png'
author: cnBeta
comments: false
date: Wed, 22 Jun 2022 11:31:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0622/562e90a892cefaa.png'
---

<div>   
在“无法解密用户存储数据”的承诺下，由传奇人物 Kim Dotcom 在十年前推出的 Mega 云存储服务，已经吸引了 2.5 亿注册用户。同时平台上托管的文件数量达到了 1200 亿，并占用了超过 1000 PB 的存储空间。<strong>在官网上，Mega 更是直接搬出了与 Dropbox 和 Google Drive 等竞品的对比 —— 尤其强调自家服务采用了端到端的加密措施。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0622/562e90a892cefaa.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0622/562e90a892cefaa.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://arstechnica.com/information-technology/2022/06/mega-says-it-cant-decrypt-your-files-new-poc-exploit-shows-otherwise/" target="_self">ARS Technica</a>）</p><p>尴尬的是，周二公布的一项<a href="https://mega-awry.io/" target="_self">研究表明</a>，Mega 掌管的基础设施实体，其实并不能充分保障用户存储数据的安全。</p><p>作者指出，Mega 采用的文件加密机制充满了低级的密码学缺陷，使得别有用心的人可以在用户登录足够多的次数后、轻松执行完整的密钥恢复攻击。</p><p>得逞后，攻击者便可破译用户存储的文件、甚至将其它恶意文件上传到用户的存储库 —— 即便表面上看起来与此前真实上传的数据没有区别。</p><blockquote><p>研究人员写道 —— 我们已证明 Mega 的系统无法保护其用户免受恶意服务器的侵害，并提出了五种不同的 攻击手段，它们都会对用户文件的机密性造成极大的破坏。</p><p>我们构建了所有攻击的概念验证，并展示了实际可利用性。此外用户数据的完整性也陷入了风险，攻击者可随意植入其指定的恶意软件，且可绕过客户端的所有真实性检查。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0622/57f513abd5c9b14.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0622/57f513abd5c9b14.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>即使三月私下收到了研究人员的报告，Mega 周二开始推送的一项更新，依然只能算是一个让攻击执行变得更加困难的临时解决方案。</p><p>研究人员警告称，该补丁并未解决密钥重用、缺乏完整性检查、以及之前发现的其它系统性问题。他们在一封电子邮件中写道：</p><blockquote><p>这意味着，如果其它攻击的先决条件以某种不同的方式得到满足，这些漏洞仍可被利用。</p><p>正因如此，即使系统不再受到此前提出的确切攻击链的影响，我们对该补丁还是并不认可。</p></blockquote><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=358912928&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">RSA Key Recovery Attack（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzU4OTEyOTI4LnNodG1s.html" target="_self">via</a>）</p><p>问题在于 Mega 的安全层次结构缺乏确保密钥完整性的任何手段，导致服务器不会拒绝一个无效的密钥、而是继续与一个无效的密钥进行交互，这使得平台很容易遭受密钥恢复攻击。</p><p>如果使用暴力手段，攻击者可在 1023 次客户端登录后恢复 RSA 私钥。但若使用二分法 + 格密码分析，攻击所需的尝试次数就可减少到 512 次 —— 正如 mega-awry.io 的概念验证所示。</p><p>遗憾的是，Mega 董事长 Stephen Hall 否认其失掉了十年前向用户作出的承诺。理由是该漏洞只能在处于活动状态的用户登录超过 512 次时才会让恶意行为者得逞，但这种情况是相当罕见的。</p><p>至于后续 Mega 是否会参考研究人员给出的中长期修复方案，仍有待时间去检验。</p>   
</div>
            