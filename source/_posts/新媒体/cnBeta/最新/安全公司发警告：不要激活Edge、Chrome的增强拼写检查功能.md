
---
title: '安全公司发警告：不要激活Edge、Chrome的增强拼写检查功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/09/f3d40014c3cd2dc.png'
author: cnBeta
comments: false
date: Mon, 19 Sep 2022 06:12:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/09/f3d40014c3cd2dc.png'
---

<div>   
如果你正在使用Edge和Chrome的增强拼写检查功能，那么现在是时候放弃它们了，因为一份新报告显示，该功能实际上可以将你的表格数据发送到拥有上述浏览器的科技巨头那里。<br>
<p style="text-align: left;">据名为otto-js的JavaScript安全公司披露称，当Chrome的增强拼写检查功能和Edge的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>编辑器拼写和语法检查器(Microsoft Editor Spelling & Grammar Checker)浏览器插件被用户手动激活时就会发生这种情况。尽管如此，值得注意的是，这两种浏览器都有自己的基本拼写检查器默认启用，但它们不会构成安全风险，因为它们的行为与增强功能不同。</p><p style="text-align: left;">当激活后，这些功能可以向微软和Google发送数据。传送的信息取决于你在特定网站上填写的表格，这意味着你分享的信息越多填写的表格字段越多，在激活增强拼写检查功能时可能会向这些公司发送的数据越多。如你正在访问的网站可能要求你提供个人身份信息(PII)像你的全名、家庭住址、电子邮件地址、社会安全号、护照号码、驾驶执照号码、信用卡号码、出生日期等。更糟糕的是，你的密码也可能被传送到微软和Google，根据otto-js研究小组的说法，称这个过程为“拼写劫持”。</p><p style="text-align: left;">“如果启用‘显示密码’，那么该功能甚至会将你的密码发送到他们的第三方服务器上，”otto JavaScript Security的联合创始人兼首席技术官Josh Summitt在测试该公司的脚本行为检测时分享了这一发现，“在研究不同浏览器的数据泄漏时，我们发现了一个功能组合，一旦启用将不必要地将敏感数据暴露给第三方如Google和微软。令人担忧的是，这些功能很容易启用，而且大多数用户会启用这些功能而没有真正意识到在后台发生了什么。”</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/09/f3d40014c3cd2dc.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/09/f3d40014c3cd2dc.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">只要使用的是Edge和Chrome并且有它们的增强拼写检查功能，拼写劫持就可能发生在所有网站上。为了证明这一点，otto-js分享了当他们使用员工凭证（特别是密码）登录公司的阿里巴巴云账户时是如何发生的，这些凭证后来被发送到了Google。此外，otto-js还分享了一个视频演示以展示拼写劫持如何暴露公司的云基础设施--包括服务器、数据库、公司电子邮件账户和密码管理器。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=384458617&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: left;">“该视频使用工作场所的一个常见场景来显示启用浏览器增强的拼写检查功能是一件多么容易的事情以及员工如何在不知不觉中暴露公司的情况，”otto-js补充道，“大多数CISO在得知他们公司的管理证书在不知情的情况下被明文共享给第三方，甚至是他们普遍信任的第三方时会感到非常震惊。”</p><p style="text-align: left;">这家JavaScript安全公司还进一步强调了可能受到该问题影响的公司和服务的名称。它包括阿里巴巴--云服务、<a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 365和Google云--Secret Manager。AWS - Secrets Manager和LastPass一开始虽然也被列入名单，但otto-js表示，这两家公司已经完全缓解了这个问题。</p><p style="text-align: left;">除了保持Chrome的增强拼写检查功能和Edge的微软编辑器拼写和语法检查器浏览器插件不被触动和停用之外，otto-js称公司还可以通过增加“spellcheck=false”来防止拼写劫持问题。</p><p style="text-align: left;">Otto-js建议道：“公司可以减轻分享客户PII的风险--通过在所有输入字段中添加'spellcheck=false'，尽管这可能给用户带来问题。或者你可以只把它添加到有敏感数据的表单字段。公司也可以删除‘显示密码’的功能。这不会防止拼写劫持，但它能防止用户密码被发送。公司还可以使用像otto-js这样的客户端安全软件来监控和控制第三方脚本。”</p><p style="text-align: left;">这家安全公司表示，目前还不知道传输给微软和Google的数据是否被储存，也不知道它们是如何被管理的。微软仍没有对此发表任何评论，但Google发言人告诉BleepingComputer--“Google不会将其附加到任何用户身份上，只是在服务器上临时处理。”</p>   
</div>
            