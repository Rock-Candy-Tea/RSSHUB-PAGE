
---
title: 'DNS 黑魔法传送门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf23f5f7d1942ceb03b7b3f196ab1ad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 18:08:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf23f5f7d1942ceb03b7b3f196ab1ad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">目录</h2>
<ol>
<li>前言</li>
<li>第一步：浏览器对 DNS 解析</li>
<li>第二步：本地 hosts文件 DNS解析</li>
<li>第三步：本地域名解析服务器 DNS 解析</li>
<li>第四步：根域名解析服务器 DNS 解析</li>
<li>第五步：gTLD服务器 DNS 解析</li>
<li>第六步：权威域名服务器 DNS 解析</li>
<li>第七步：返回缓存</li>
<li>DNS 解析原理</li>
<li>DNS 解析优化</li>
<li>DNS 劫持</li>
<li>DNS 劫持应对策略</li>
<li>结束语</li>
<li>题外话</li>
<li>参考</li>
</ol>
<h2 data-id="heading-1">前言</h2>
<p>在上一篇文章中，介绍<a href="https://juejin.cn/post/6954138529475592223" target="_blank">浏览器解析 URL 的黑魔法</a>，这篇文章来介绍一下 DNS 黑魔法。</p>
<h3 data-id="heading-2">概念</h3>
<p>DNS 的全称是 Domain Name System 或者 Domain Name Service，它主要的作用就是将人们所熟悉的网址 (域名) “翻译”成电脑可以理解的 IP 地址，这个过程叫做 DNS 域名解析。</p>
<h3 data-id="heading-3">为什么需要 DNS 解析</h3>
<p>网络通讯大部分是基于TCP/IP的，而TCP/IP是基于IP地址的，所以计算机在网络上进行通讯时只能识别如“192.168.0.0.1”之类的IP地址，而不能认识域名。而对于人类的心智模型来说，很难记住10个以上IP地址的网站，所以我们访问网站时，更多的是在浏览器地址栏中输入域名，就能看到所需要的页面，这是因为有一个叫“DNS服务器”的计算机自动把我们的域名“翻译”成了相应的IP地址，然后调出IP地址所对应的网页。</p>
<h3 data-id="heading-4">大厂经常问</h3>
<p>DNS 解析在面试中是一个常见的问题。经常会存在这样的题目「在浏览器输入一个 URL 之后发生了什么？」，这个问题扩展开来就囊括了 DNS 的解析过程。当然还有的面试官会把 DNS 的解析过程单独拿出来问。这篇文章就详细来讲讲 DNS 怎么解析的。</p>
<h2 data-id="heading-5">第一步：浏览器 DNS 解析</h2>
<h3 data-id="heading-6">检查浏览器缓存中是否缓存过该域名对应的IP地址</h3>
<p>用户通过浏览器浏览过某网站之后，浏览器就会自动缓存该网站域名对应的地址，当用户再次访问的时候，浏览器就会从缓存中查找该域名对应的IP地址，因为缓存不仅是有大小限制，而且还有时间限制（域名被缓存的时间通过属性来设置），所以存在域名对应的找不到的情况。</p>
<p>当浏览器从缓存中找到了该网站域名对应的地址，那么整个解析过程结束，如果没有找到，将进行下一步骤。对于的缓存时间问题，不宜设置太长的缓存时间，时间太长，如果域名对应的发生变化，那么用户将在一段时间内无法正常访问到网站，如果太短，那么又造成频繁解析域名。</p>
<h3 data-id="heading-7">浏览器缓存 DNS 时间</h3>
<p>浏览器为了提高响应的时间，会对 DNS 记录缓存，但是不同的浏览器缓存的时间不一样。</p>
<h4 data-id="heading-8">chrome</h4>
<p>chrome://net-internals/#dns 这里可以看各域名的DNS 缓存时间。Chrome对每个域名会默认缓存60s。但是有可能chrome://net-internals显示不出来dns缓存。只有一个清除缓存的按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf23f5f7d1942ceb03b7b3f196ab1ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当遇到这样的情况时，你可以按照如下的流程操作来查看 DNS 缓存，这个不能查看 DNS 缓存是因为 chrome://net-internals/ 的一些功能已经在Chrome 71之后被移除了。</p>
<ol>
<li>chrome://net-export 导出日志</li>
<li><a href="https://netlog-viewer.appspot.com/" target="_blank" rel="nofollow noopener noreferrer">netlog-viewer.appspot.com</a> 下导入日志查看</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e104e518e24439ea3eabe50c1081f96~tplv-k3u1fbpfcp-watermark.image" alt="DNS解析1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">Firefox</h4>
<p>Firefox有DNS缓存功能，默认缓存时间只有1分钟。</p>
<h4 data-id="heading-10">IE</h4>
<p>IE将DNS缓存30min。</p>
<h4 data-id="heading-11">Safari</h4>
<p>Safari DNS缓存时间约为10s</p>
<h3 data-id="heading-12">浏览器对 DNS 解析结果的处理</h3>
<p>如果一个域名的DNS解析结果会有多个的话，浏览器是如何处理的呢？Chrome浏览器会优先向第一个IP发起HTTP请求，如果不通，再向后面的IP发起HTTP请求。<a href="http://tool.chinaz.com/dns/" target="_blank" rel="nofollow noopener noreferrer">DNS 域名查询网址</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dde713bf737748ba84e6660f15736bed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">第二步：本地 hosts文件 DNS解析</h2>
<p>如果第一个步骤没有完成对域名的解析过程，那么浏览器会去系统缓存中查找系统是否缓存过这个域名对应的地址，也可以理解为系统自己也具备域名解析的基本能力。在系统中，可以通过设置文件来将域名手动的绑定到 某个 IP 上。如果使用过代理软件（如 fiddler ）的同学可能对这个比较清楚一点，在系统的 hosts 文件，可以用来设置域名和 IP 的对于关系。对于普通用户，并不推荐自己手动绑定域名和，对于开发者来说，通过绑定域名和，可以轻松切换环境，可以从测试环境切换到开发环境，方便开发和测试。</p>
<h3 data-id="heading-14">hosts文件</h3>
<p>hosts文件是一个用于储存计算机网络中各节点信息的计算机文件。这个文件负责将主机域名映射到相应的IP地址。hosts文件通常用于补充或取代网络中DNS的功能。和DNS不同的是，计算机的用户可以直接对hosts文件进行控制。hosts文件的作用非常大，可以自由解析域名。</p>
<h3 data-id="heading-15">hosts文件位置</h3>
<ul>
<li>Windows NT/2000/XP/Vista/win7（即微软NT系列操作系统）：默认位置为 %SystemRoot%\system32\drivers\etc\，但也可以改变。</li>
<li>典型的XP系统hosts文件位置：C:\windows\system32\drivers\etc</li>
<li>Windows 95/98/Me：%WinDir%\Linux及其他类Unix操作系统：/etc苹果系：</li>
<li>Mac OS 9及更早的系统：System Folder: Preferences或System folder（文件格式可能与Windows和Linux所对应的文件不同）</li>
<li>Mac OS X：/private/etc（使用BSD风格的hosts文件）</li>
<li>iPhone OS：/etc</li>
<li>iPad OS：/private/etcSymbian第1/2版手机：C:\system\data\hosts</li>
<li>Symbian第3版手机：C:\private\10000882\hosts，只能使用兼容AllFiles的文件浏览器访问，大部分都不行。</li>
</ul>
<p><strong>位置如果有问题请告知，谢谢！</strong></p>
<h3 data-id="heading-16">hosts文件的一些用途</h3>
<ul>
<li>将广告域名重定向到本地IP地址：127.0.0.1上来过滤广告。</li>
<li>hosts文件可用于拦截一些恶意网站的请求，从而防止访问欺诈网站或感染一些病毒或恶意软件。</li>
<li>使用hosts文件来强制将网站指定到正确的IP上。</li>
</ul>
<h2 data-id="heading-17">第三步：本地域名解析服务器 DNS 解析</h2>
<p>如果在本机上无法完成域名的解析，那么系统只能请求本地域名解析服务系统进行解析，本地域名系统一般都是本地区的域名服务器，比如你连接的校园网，那么域名解析系统就在你的校园机房里，如果你连接的是电信、移动或者联通的网络，那么本地域名解析服务器就在本地区，由各自的运营商来提供服务。对于本地服务器地址，系统使用命令就可以查看，在和系统下，直接使用命令来查看服务地址。一般都缓存了大部分的域名解析的结果，当然缓存时间也受域名失效时间控制，大部分的解析工作到这里就差不多已经结束了，负责了大部分的解析工作。</p>
<h2 data-id="heading-18">第四步：根域名解析服务器 DNS 解析</h2>
<p>本地域名解析器还没有完成解析的话，那么本地域名解析服务器将向根域名服务器发起解析请求。本地域名解析向根域名服务器发起解析请求，根域名服务器返回的是所查域的通用顶级域xxx地址。</p>
<h3 data-id="heading-19">根域名解析服务器</h3>
<p>由于早期的 DNS 查询结果是一个512字节的 UDP 数据包。这个包最多可以容纳13个服务器的地址，因此就规定全世界有13个根域名服务器，编号从a.root-servers.net一直到m.root-servers.net。
这13台根域名服务器由12个组织独立运营。其中，Verisign 公司管理两台根域名服务器：A 和 J。每家公司为了保证根域名服务器的可用性，会部署多个节点，比如单单 Verisign 一家公司就部署了104台根域名服务器（2016年1月数据）。
所以，根域名服务器其实不止13台。据统计，截止2016年1月，全世界共有 517 台根域名服务器。你可以在 <a href="http://root-servers.org/" target="_blank" rel="nofollow noopener noreferrer">root-servers.org</a> 这个网站查到所有根域名服务器的信息。</p>
<h2 data-id="heading-20">第五步：gTLD服务器 DNS 解析</h2>
<p>本地域名解析服务器向gTLD服务器发起请求。gLTD服务器查询并返回域名对应的Name Server域名服务器的地址，通常是你注册的域名服务器，例如你在某个域名服务器提供商申请的域名，那么这个域名解析任务就由这个域名服务提供商来完成。</p>
<h2 data-id="heading-21">第六步：权威域名服务器 DNS 解析</h2>
<p>权威域名服务器会查询存储的域名和ip的映射关系表，将 ip 连同一个 TTL 值返回给DNS 本地域名服务器。</p>
<h2 data-id="heading-22">第七步：返回，然后缓存</h2>
<p>本地域名服务器拿到 ip 和 TTL 会缓存起来。返回给浏览器。</p>
<h2 data-id="heading-23">DNS 解析原理</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7bc087c36bd49d68554c7db8e6848ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>本地DNS解析是递归过程。</li>
<li>其他服务器DNS解析是迭代过程。</li>
</ul>
<p>每一次DNS解析需要20~120ms ，第一次解析完成后，会把解析信息缓存到本地 下一次再次发送这个域名请求，直接从本地缓存中进行解析了
一个页面中域名很多那么需要解析的就很多服务器。减少域名解析（页面中尽可能少用不同的服务器），但是真实情况要做一个取舍： 为了节约服务器资源，大型网站一般都是服务器分布式 或者 服务器分离 WEB资源服务器 图片服务器 数据服务器 .....</p>
<h2 data-id="heading-24">DNS 解析优化</h2>
<p>DNS解析会有20ms~120ms的耗时，哪减少这个耗时是有必要的，通常是做饭是减少 DNS 的请求次数，尽可能不要请求太多的服务器解析。但是现在很多的公司为了做负载均衡或者服务器的分离独立部署，都是更可能多请求服务器。哪还有一种做法就是 DNS 预解析，DNS预解析其实就是减少域名解析成IP的时间。</p>
<pre><code class="hljs language-js copyable" lang="js"><link rel=<span class="hljs-string">"dns-prefetch"</span> href=<span class="hljs-string">"xxx"</span>></link>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><meta http-equiv=<span class="hljs-string">"x-dns-prefetch-control"</span> content=<span class="hljs-string">"on"</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">DNS 劫持</h2>
<h3 data-id="heading-26">概念</h3>
<p>DNS劫持即通过某种技术手段，篡改正确域名和IP地址的映射关系，使得域名映射到了错误的IP地址，因此可以认为DNS劫持是一种DNS重定向攻击。DNS劫持通常可被用作域名欺诈，如在用户访问网页时显示额外的信息来赚取收入等；也可被用作网络钓鱼，如显示用户访问的虚假网站版本并非法窃取用户的个人信息。</p>
<h3 data-id="heading-27">DNS 劫持大事记</h3>
<h4 data-id="heading-28">《AWS route53 BGP路由泄漏事件》</h4>
<p>事件发生在2018年4月24日。黑客针对四段分配给AWS，本应作为AWS route53 DNS服务器服务地址的IP空间(205.251.192.0/23, 205.251.194.0/23, 205.251.196.0/23, 205.251.198.0/23)发布了虚假的BGP路由，导致在BGP泄漏的两个小时期间，本应该AWS route53 DNS服务器的DNS查询都被重定向到了黑客的恶意DNS服务器。且黑客DNS劫持的目标十分明确，恶意DNS服务器只响应对<a href="http://myetherwallet.com/" target="_blank" rel="nofollow noopener noreferrer">myetherwallet.com</a> 的查询，其他域名的查询均返回SERVFAIL。一旦用户没有注意“网站不安全”的提示而访问<a href="http://myetherwallet.com/" target="_blank" rel="nofollow noopener noreferrer">myetherwallet.com</a> 登录自己的以太坊钱包，黑客就可以轻易获取用户的私钥进而窃取用户的数字货币资产。
据不完全统计，DNS劫持导致两个小时内有多个用户的以太坊钱包被转账清空，共计至少13000美元的资产被黑客盗取。</p>
<h4 data-id="heading-29">《巴西银行钓鱼事件》</h4>
<p>事件发生在2018年。黑客利用D-Link路由器的漏洞，入侵了至少500个家用路由器。黑客入侵后更改受害者路由器上的DNS配置，将受害者的DNS请求重定向到黑客自己搭建的恶意DNS服务器上。黑客入侵后更改受害者路由器上的DNS配置，将受害者的DNS请求重定向到黑客自己搭建的恶意DNS服务器上，最终诱导原本想访问正常银行网站的受害者访问到钓鱼网站，并恶意窃取受害者的银行账目密码信息。
黑客诱导原本想访问正常银行网站的受害者访问到钓鱼网站，并恶意窃取受害者的银行账目密码信息。</p>
<h3 data-id="heading-30">DNS 劫持分类</h3>
<h4 data-id="heading-31">本地DNS劫持</h4>
<ul>
<li>篡改本地的 hosts文件。黑客通过木马病毒或者恶意程序入侵PC，篡改DNS配置(hosts文件，DNS服务器地址，DNS缓存等)。</li>
<li>攻击路由器或者利用路由器的漏洞篡改 DNS 配置。</li>
</ul>
<h4 data-id="heading-32">DNS解析路径劫持</h4>
<ul>
<li>通过技术手段(中间盒子，软件等)将DNS流量重定向到其他DNS服务器。</li>
<li>利用分光等设备将DNS查询复制到网络设备，并先于正常应答返回DNS劫持的结果。</li>
<li>网络设备或者软件直接代替DNS服务器对DNS查询进行应答。</li>
</ul>
<h4 data-id="heading-33">篡改DNS权威记录</h4>
<ul>
<li>篡改DNS权威记录 我们这里指的黑客非法入侵DNS权威记录管理账号，直接修改DNS记录的行为。</li>
</ul>
<h2 data-id="heading-34">DNS 劫持应对策略</h2>
<p>DNS劫持在互联网中似乎已经变成了家常便饭，那么该如何应对各种层出不穷的DNS劫持呢？如果怀疑自己遇到了DNS劫持，首先要做的事情就是要确认问题。</p>
<h3 data-id="heading-35">如何确认DNS劫持</h3>
<p>阿里云的可以检测域名是否被劫持（注意我不是阿里云的拖，哈哈哈哈），<a href="https://zijian.aliyun.com/#/domainDetect" target="_blank" rel="nofollow noopener noreferrer">地址</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da5f5c6415f54b45a12c5208b34cbb73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-36">DNS劫持防范</h3>
<ul>
<li>安装杀毒软件，防御木马病毒和恶意软件；定期修改路由器管理账号密码和更新固件。</li>
<li>选择安全技术实力过硬的域名注册商，并且给自己的域名权威数据上锁，防止域名权威数据被篡改。</li>
<li>选择支持DNSSEC的域名解析服务商，并且给自己的域名实施DNSSEC。DNSSEC能够保证递归DNS服务器和权威DNS服务器之间的通信不被篡改。阿里云DNS作为一家专业的DNS解析服务厂商，一直在不断完善打磨产品功能，DNSSEC功能已经在开发中，不日就会上线发布。</li>
<li>在客户端和递归DNS服务器通信的最后一英里使用DNS加密技术，如DNS-over-TLS，DNS-over-HTTPS等。</li>
</ul>
<h2 data-id="heading-37">结束语</h2>
<p>如果文章中什么不对或者写的不好的地方，请大家多多指正，谢谢！码字不易，点个赞加个关注吧！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d86381325f4e47c3822153957e8ba753~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-38">题外话</h2>
<p>笔者在「深圳虾皮」，一家口碑还不错的东南亚电商公司，2021大量招人，机会多多！快来加入我们吧！</p>
<p>现在有想法，还是以后有想法的同学，都可以加我微信[stone---999]！内推你加入我们的大家庭！</p>
<h2 data-id="heading-39">参考</h2>
<ul>
<li><a href="https://www.zhihu.com/question/23042131/answer/66571369" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/23…</a></li>
<li><a href="https://cloud.tencent.com/developer/news/324975" target="_blank" rel="nofollow noopener noreferrer">cloud.tencent.com/developer/n…</a></li>
<li><a href="https://www.ruanyifeng.com/blog/2018/05/root-domain.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2018/0…</a></li>
<li><a href="https://www.ruanyifeng.com/blog/2016/06/dns.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2016/0…</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/86538629" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/86538629</a></li>
</ul></div>  
</div>
            