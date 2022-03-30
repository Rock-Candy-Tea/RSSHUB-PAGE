
---
title: '不少WordPress网站被注入恶意脚本 对乌克兰网站发起DDoS攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0330/6eb1102397dcc88.jpg'
author: cnBeta
comments: false
date: Tue, 29 Mar 2022 23:58:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0330/6eb1102397dcc88.jpg'
---

<div>   
<strong>不少 WordPress 网站正在遭受黑客们的攻击，通过注入的恶意脚本，利用访问者的浏览器对乌克兰网站进行分布式拒绝服务攻击。</strong>今天，MalwareHunterTeam 发现一个 WordPress 网站被入侵使用这个脚本，针对十个网站进行分布式拒绝服务（DDoS）攻击。<br>
 这些网站包括乌克兰政府机构、智囊团、乌克兰国际军团的招募网站、金融网站和其他亲乌克兰的网站。<p style="text-align: left;">目标网站的完整清单如下。</p><blockquote style="text-align: left;"><p style="text-align: left;">https://stop-russian-desinformation.near.page</p><p style="text-align: left;">https://gfsis.org/</p><p style="text-align: left;">http://93.79.82.132/</p><p style="text-align: left;">http://195.66.140.252/</p><p style="text-align: left;">https://kordon.io/</p><p style="text-align: left;">https://war.ukraine.ua/</p><p style="text-align: left;">https://www.fightforua.org/</p><p style="text-align: left;">https://bank.gov.ua/</p><p style="text-align: left;">https://liqpay.ua</p><p style="text-align: left;">https://edmo.eu</p></blockquote><p style="text-align: left;">当加载时，JavaScript 脚本将迫使访问者的浏览器对列出的每个网站执行 HTTP GET 请求，每次不超过 1000 个并发连接。DDoS攻击将在后台发生，而用户不知道它正在发生，只是他们的浏览器会变慢。这使得脚本能够在访问者不知道他们的浏览器已被用于攻击的情况下进行 DDoS 攻击。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0330/6eb1102397dcc88.jpg" alt="QQ截图20220330075800.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">对目标网站的每个请求都将利用一个随机查询字符串，这样请求就不会通过 Cloudflare 或 Akamai 等缓存服务提供，而是直接由被攻击的服务器接收。例如，DDoS 脚本将在网站服务器的访问日志中产生类似以下的请求。</p><blockquote style="text-align: left;"><p style="text-align: left;">"get /?17.650025158868488 http/1.1"</p><p style="text-align: left;">"get /?932.8529889504794 http/1.1"</p><p style="text-align: left;">"get /?71.59119445542395 http/1.1"</p></blockquote><p style="text-align: left;">BleepingComputer 只找到了几个感染了这种 DDoS 脚本的网站。然而，开发者 Andrii Savchenko 表示，有数百个 WordPress 网站被破坏，以进行这些攻击。Savchenko 在Twitter上说：“实际上大约有上百个这样的网站。都是通过WP漏洞。不幸的是，许多供应商/业主没有反应”。</p><p style="text-align: left;">在研究该脚本以寻找其他受感染的网站时，BleepingComputer 发现，亲乌克兰的网站 https://stop-russian-desinformation.near.page，也在使用同样的脚本，用于对俄罗斯网站进行攻击。在访问该网站时，用户的浏览器被用来对67个俄罗斯网站进行 DDoS 攻击。</p><p style="text-align: left;">虽然这个网站澄清它将利用访问者的浏览器对俄罗斯网站进行DDoS攻击，但被攻击的WordPress网站在网站所有者或其访问者不知情的情况下使用了这些脚本。</p>   
</div>
            