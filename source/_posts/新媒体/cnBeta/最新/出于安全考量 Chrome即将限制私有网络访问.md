
---
title: '出于安全考量 Chrome即将限制私有网络访问'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0113/79f3075daed2343.webp'
author: cnBeta
comments: false
date: Thu, 13 Jan 2022 08:49:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0113/79f3075daed2343.webp'
---

<div>   
<strong>出于安全方面的考量以及过去被恶意软件滥用的情况，Google 表示 Chrome 浏览器近期将阻止互联网网站和本地私人网络内的设备/服务器之间的查询和互动。</strong>这一变化将通过实施新的 W3C 规范来实现，该规范被称为私人网络访问（PNA），将在今年上半年推出。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0113/79f3075daed2343.webp" alt="ujd98xii.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">新的 PNA 规范在 Chrome 浏览器内增加了一个机制，通过该机制，互联网网站可以在建立连接前向本地网络内的系统征求许可。Google 表示：</p><p style="text-align: left;">Chrome 浏览器将在任何子资源的私人网络请求之前开始发送 CORS 预检请求，该请求要求目标服务器给予明确许可。</p><p style="text-align: left;">这个预检请求将携带一个新的头，即 Access-Control-Request-Private-Network: true，而对它的响应必须携带一个相应的头，即 Access-Control-Allow-Private-Network: true。</p><p style="text-align: left;">如果本地设备，如服务器或<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>未能响应，互联网网站将被阻止连接。新的 PNA 规范是近年来将被添加到 Chrome 浏览器中的最重要的安全功能之一。自 2010 年代初以来，网络犯罪团伙已经意识到，他们可以利用浏览器作为“代理”，转发连接到公司的内部网络。</p><p style="text-align: left;">例如，一个恶意网站可能包含试图访问192.168.0.1这样一个IP地址的代码，这是大多数路由器管理面板的典型地址，只能从本地网络访问。当用户访问这种恶意网站时，他们的浏览器可以在用户不知情的情况下向他们的路由器发出自动请求，发送恶意代码，绕过路由器的认证，修改路由器设置。</p><p style="text-align: left;">这种攻击此前确实发生过。这种互联网到本地网络的攻击的变种也可以针对其他本地系统，如内部服务器、域控制器、防火墙，甚至本地托管的应用程序（通过http://localhost 域或其他本地定义的域）。通过在Chrome浏览器内部引入PNA规范及其权限协商系统，Google希望防止这种自动攻击成为可能。</p><p style="text-align: left;">据Google称，PNA 的一个版本已经与 2021 年 11 月发布的 Chrome 96 一起上线，但全面支持将在今年分两个阶段推出，分别是 Chrome 98（3月初）和Chrome 101（5月底）的发布，详情如下。</p><p style="text-align: left;">在 Chrome 98 中。</p><p style="text-align: left;">● Chrome会在私有网络子资源请求之前发送预检请求。</p><p style="text-align: left;">● 预检失败只在DevTools中显示警告，不影响私人网络请求。</p><p style="text-align: left;">● Chrome收集兼容性数据，并向受影响最大的网站伸出援手。</p><p style="text-align: left;">● Google 预计这将与现有网站广泛兼容。</p><p style="text-align: left;">最早在Chrome 101 中全面部署</p><p style="text-align: left;">● 只有当兼容性数据表明该变化足够安全，并且我们在必要时直接进行了外联时，这才会开始。</p><p style="text-align: left;">● Chrome浏览器强制要求预检请求必须成功，否则会导致请求失败。</p><p style="text-align: left;">● 废弃试验也同时开始，以允许受此阶段影响的网站请求延长时间。该试验将持续至少6个月。</p>   
</div>
            