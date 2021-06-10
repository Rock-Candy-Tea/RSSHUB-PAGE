
---
title: '关于DNS的那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/278243771a894ed9a900d19e53c69a36~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 23:25:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/278243771a894ed9a900d19e53c69a36~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.DNS的定义以及它的作用</h2>
<p>维基百科中对于DNS的解释</p>
<blockquote>
<p><strong>域名系统</strong>（英语：<strong>D</strong>omain <strong>N</strong>ame <strong>S</strong>ystem，缩写：<strong>DNS</strong>）是互联网的一项服务。它作为将[域名]和[IP地址]相互映射的一个分布式数据库，能够使人更方便地访问互联网。DNS使用TCP和UDP端口53。当前，对于每一级域名长度的限制是63个字符，域名总长度则不能超过253个字符。</p>
</blockquote>
<p>DNS主要的作用就是将人们所熟悉的网址 (域名) “翻译”成电脑可以理解的 IP 地址，这个过程叫做 DNS 域名解析。 打个比方，我们登百度的地址的时候，都是敲<code>www.baidu.com</code>，进行登陆，难道你会去敲IP地址登百度？明显，域名容易记忆。</p>
<h2 data-id="heading-1">二.DNS服务器</h2>
<h3 data-id="heading-2">2.1  域名的级别</h3>
<ul>
<li>.代表根域名</li>
<li>.com这种是顶级域名，也叫一级域名</li>
<li>baidu.com这种叫二级域名，</li>
<li><a href="http://www.baidu.xn--com-t28dz2y4fo7wk99epejvk7b/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com这种叫三级域名</a></li>
<li>依次类推</li>
</ul>
<h3 data-id="heading-3">2.2 对应的DNS服务器种类</h3>
<p><strong>根域名服务器(ROOT DNS Server)</strong></p>
<p>根域名服务器就是存放顶级域名服务器地址的。存储260个顶级域名服务器的IP地址。对于Ipv4来说全球有13个根域名服务器，它储存了每个域(如.com .net .cn)的解析和域名服务器的地址信息。</p>
<p><strong>顶级域名服务器</strong></p>
<p>例如.com的域名服务器，存储的是一些一级域名的权威DNS服务器地址(如toutiao.com的DNS)。</p>
<p>顶级域名又称一级域名，顶级域名可以分为三类，即gTLD、ccTLD和New gTLD：</p>
<ul>
<li>gTLD：国际顶级域名(generic top-level domains，gTLD)，例如：.com/.net/.org等都属于gTLD;</li>
<li>ccTLD：国家和地区顶级域名(country code top-level domains，简称ccTLD)，例如：中国是.cn域名，日本是.jp域名;</li>
<li>New gTLD：新顶级域名(New gTLD)，例如：.xyz/.top/.red/.help等新顶级域名
顶级域名服务器就是根据上面三类保存域名IP对应数据的</li>
</ul>
<p><strong>本地域名服务器(Local DNS)</strong></p>
<p>一般是运营商的DNS，主要作用就是代理用户进行域名分析的。</p>
<h2 data-id="heading-4">三.DNS解析原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/278243771a894ed9a900d19e53c69a36~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.1 递归查询</h3>
<p>主机向本地域名服务器的查询一般都是采用递归查询。</p>
<p>所谓递归查询就是：如果主机所询问的本地域名服务器不知道被查询的域名的IP地址，那么本地域名服务器就以DNS客户的身份，向其它根域名服务器继续发出查询请求报文(即替主机继续查询)，而不是让主机自己进行下一步查询。</p>
<p>因此，递归查询返回的查询结果或者是所要查询的IP地址，或者是报错，表示无法查询到所需的IP地址。</p>
<h3 data-id="heading-6">3.2 迭代查询</h3>
<p>当根域名服务器收到本地域名服务器发出的迭代查询请求报文时，要么给出所要查询的IP地址，要么告诉本地服务器：“你下一步应当向哪一个域名服务器进行查询”。</p>
<p>然后让本地服务器进行后续的查询。根域名服务器通常是把自己知道的顶级域名服务器的IP地址告诉本地域名服务器，让本地域名服务器再向顶级域名服务器查询。</p>
<p>顶级域名服务器在收到本地域名服务器的查询请求后，要么给出所要查询的IP地址，要么告诉本地服务器下一步应当向哪一个权限域名服务器进行查询。</p>
<p>最后，知道了所要解析的IP地址或报错，然后把这个结果返回给发起查询的主机。</p>
<p><strong>递归</strong>：客户端只发一次请求，要求对方给出最终结果。</p>
<p><strong>迭代</strong>：客户端发出一次请求，对方如果没有授权回答，它就会返回一个能解答这个查询的其它名称服务器列表，客户端会再向返回的列表中发出请求，直到找到最终负责所查域名的名称服务器，从它得到最终结果。</p>
<p><strong>授权回答</strong>：向dns服务器查询一个域名，刚好这个域名是本服务器负责，返回的结果就是授权回答。</p>
<p><strong>从递归和迭代查询可以看出：</strong></p>
<p><strong>客户端-本地dns服务端：这部分属于递归查询。（定义）</strong></p>
<p><strong>本地dns服务端---外网：这部分属于迭代查询。</strong></p>
<p><strong>递归查询时，返回的结果只有两种:查询成功或查询失败.</strong></p>
<p><strong>迭代查询，又称作重指引,返回的是最佳的查询点或者主机地址.</strong></p>
<h3 data-id="heading-7">3.3 详细过程</h3>
<p><img src="https://s1.51cto.com/oss/202003/23/bec464420068e83aad20fd3476adeb16.jpeg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以在浏览器中输入www.toutiao.com为例。</p>
<p>①用户请求通过浏览器输入要访问网站的地址，例如：<a href="http://www.toutiao.com.xn--urlip-4n1hi9co92aosbqcyis61c63bpzlbsc66zzuvviww53b909aeqm395b.xn--,urlip,ip-vk6nqk1a28e73mnolfmuea7zf556ievjja218avrbh28az75aomwjn9g6wc4v2g2c0ewa7415avram5tep7c0a.xn--,2-dz4c33aw1yuwcu24au7am3ud8ci41dn1jz38c./" target="_blank" rel="nofollow noopener noreferrer">www.toutiao.com。浏览器会在自己的缓存中查找URL对应IP地址。如果之前访问过，保存了这个URL对应IP地址的缓存，那么就直接访问IP地址。如果没有缓存，进入到第2步。</a></p>
<p>②如果没有，就去问操作系统，操作系统也会去看自己的缓存，如果有，就直接返回。</p>
<p>③通过计算机本地的Host文件配置，可以设置URL和IP地址的映射关系。比如windows下是通过C:\windwos\system32\driver\etc\hosts文件来设置的，linux中则是/etc/named.confg文件。这里查找本地的Host文件，看是有IP地址的缓存。如果在文件中依旧没有找到映射关系，进入第四步。</p>
<p>④请求Local DNS Server，通过本地运营商获取URL和IP的映射关系。如果在校园网，DNS服务器就在学校，如果是小区网络，DNS服务器是运营商提供的。总之这个服务器在物理位置上离发起请求的计算机比较近。Local DNS Server缓存了大量的DNS解析结果。由于它的性能较好，物理上的距离又比较近，它通常会在很短的时间内返回指定域名的解析结果。80%的DNS解析需求在这一步就满足了。如果在这一步还是没有完成DNS解析，进入第五步。</p>
<p>⑤通过Root DNS Server进行解析，ROOT DNS Server会根据请求的URL 返回给Local DNS Server顶级域名服务器的地址。例如：查询的是”.com”的域名，就查询 gTL对应的域名服务器的地址。</p>
<p>⑥返回顶级域名服务器的地址以后，访问对应的顶级域名服务器(gTLD、ccTLD、New gTLD)，并且返回Name Server服务器地址。简单来说Name Server服务器记录某域名和负责解析该域的权威DNS。</p>
<p>⑦Name Server会把指定域名的A记录或者CNAME返回给Local DNS Server，并且设置一个TTL。</p>
<ul>
<li>A (Address) 记录是用来指定主机名(或域名)对应的IP地址记录。用户可以将该域名下的网站服务器指向到自己的web server上。同时也可以设置您域名的二级域名。</li>
<li>CNAME：别名记录。这种记录允许您将多个名字映射到另外一个域名。通常用于同时提供WWW和MAIL服务的计算机。例如，有一台计算机名为“host.mydomain.com”(A记录)。它同时提供WWW和MAIL服务，为了便于用户访问服务。服务商从方便维护的角度，一般也建议用户使用CNAME记录绑定域名的。如果主机使用了双线IP，显然使用CNAME也要方便一些。</li>
<li>TTL(Time To Live)：也就是设置这个DNS解析在Local DNS Server上面的过期时间。超过了这个过期时间，URL和IP的映射就会被删除，需要获取还要请求Name Server。</li>
</ul>
<p>⑧如果此时获取的是A记录，那么就可以直接访问网站的IP了。但是通常来说大型的网站都会返回CNAME，然后将其传给GTM Server。</p>
<p>GTM(Global Traffic Manager的简写)即全局流量管理，基于网宿智能DNS、分布式监控体系，实现实时故障切换及全球负载均衡，保障应用服务的持续高可用性。传给GTM的目的就是希望通过GTM的负载均衡机制，帮助用户找到最适合自己的服务器IP。</p>
<p>也就是离自己最近，性能最好，服务器状态最健康的。而且大多数的网站会做CDN缓存，此时就更需要使用GTM帮你找到网络节点中适合你的CDN缓存服务器。</p>
<p>⑨找到CDN缓存服务器以后，可以直接从服务器上面获取一些静态资源，例如：HTML、CSS、JS和图片。但是一些动态资源，例如商品信息，订单信息，需要通过第9步。</p>
<p>⑩对于没有缓存的动态资源需要从应用服务器获取，在应用服务器与互联网之间通常有一层负载均衡器负责反向代理。有它路由到应用服务器上。</p>
<p>注意:仔细看上面的过程，你可能发现了，没有提到DNS服务器怎么知道"根域名服务器"的IP地址。回答是"根域名服务器"的NS记录和IP地址一般是不会变化的，所以内置在DNS服务器里面。</p>
<h2 data-id="heading-8">四.总结</h2>
<p>DNS服务器是用来做URL与IP地址解析的，帮助用户找到要访问服务器的IP。从DNS服务器的结构来说大致分为三层：根域名服务器，顶级域名服务器，本地域名服务器。</p>
<p>申请域名的供应商会提供Name Server作为DNS解析。从用户访问一个网站出发，经过浏览器，本地Host文件、Local DNS Server、Root DNS Server、顶级域名服务器(gTLD、ccTLD、New gTLD)、Name Server、GTM、CDN、Application Server。</p></div>  
</div>
            