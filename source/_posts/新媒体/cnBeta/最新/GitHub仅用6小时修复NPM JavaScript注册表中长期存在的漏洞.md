
---
title: 'GitHub仅用6小时修复NPM JavaScript注册表中长期存在的漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1118/b1e27db78c1dd3f.webp'
author: cnBeta
comments: false
date: Thu, 18 Nov 2021 02:47:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1118/b1e27db78c1dd3f.webp'
---

<div>   
<strong>GitHub 今天表示，<a href="https://github.blog/2021-11-15-githubs-commitment-to-npm-ecosystem-security/" target="_blank">团队已经修复了 NPM（Node Package Manager）JavaScript 注册表中一个长期存在的问题</a>，该问题将允许攻击者在没有适当授权的情况下更新任何软件包。</strong>首席安全官 Mike Hanley 昨天发布了这个问题，这个问题是由安全研究人员 Kajetan Grzybowski 和 Maciej Piechota 于 11 月 2 日报告的，<strong>并在6小时内修复。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1118/b1e27db78c1dd3f.webp" alt="zmny56bm.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这一令人印象深刻的速度与该漏洞存在的时间长短形成鲜明对比，据说比“我们有可用的遥测数据的时间框架要长，可以追溯到 2020 年 9 月”。</p><p style="text-align: left;">该漏洞是基于一个熟悉的不安全模式，即系统正确地验证了一个用户，但随后允许访问超出该用户的权限。在这种情况下，NPM 服务正确地验证了一个用户被授权更新一个包，但“对注册表数据进行底层更新的服务根据上传的包文件的内容来决定发布哪个包”。</p><p style="text-align: left;">NPM 是数百万开发者的重要资源；例如，最受欢迎的软件包之一是 lodash，这是一个 JavaScript 工具库，每天被下载约 700 万次。这样一个软件包的恶意版本的后果将是严重的，这就是为什么 Hanley 补充说，“我们可以非常自信地说，这个漏洞至少自2020年9月以来没有被恶意利用过”。</p>   
</div>
            