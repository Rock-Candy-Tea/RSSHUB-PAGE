
---
title: '【安全测试工程师】超实用的Web渗透测试学习路线～'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fca3866a8524efea8eefdadba3fb802~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:48:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fca3866a8524efea8eefdadba3fb802~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：云牧青</p>
<p>来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.hs.net%2Fthread%2F1186" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.hs.net/thread/1186" ref="nofollow noopener noreferrer">恒生LIGHT云社区</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>本文整理的学习路线，清晰明了，重点分明，能快速上手实践，相信想学的同学们都能轻松学完。都是干货啦，先收藏⭐再看吧。本文偏基础能让萌新们快速摸到***测试的门道，少走弯路，也能让正在学习的小伙伴们查漏补缺，也欢迎大佬们在评论区指正错误~</p>
<hr>
<p>先上脑图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fca3866a8524efea8eefdadba3fb802~tplv-k3u1fbpfcp-zoom-1.image" alt="QQ截图20210723160512.png" title="2299" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实安全测试需要的知识面是非常广的，但跟着教程有重点地学习还是能很快理清思路上手测试的，后续可以自己深入研究，吃透这些领域的知识。</p>
<p>首先我们要了解什么是***测试。</p>
<p>我们知道业务功能、逻辑的测试有黑盒测试和白盒测试，前者把程序看作一个不能打开的黑盒子，在完全不考虑程序内部结构和内部特性的情况下，在程序接口进行测试，主要测试程序前台展示的功能。后者通过检查软件内部的逻辑结构，对软件中的逻辑路径进行覆盖测试，主要用于检测软件编码过程中的错误。</p>
<p>在软件安全测试方面，<em><strong>测试类似于黑盒测试，通过模拟</strong></em>的进攻非法，来测试软件是否存在安全漏洞。此外代码审计类似于白盒测试，用于检查源代码中的安全缺陷。因为保证软件的安全质量需要贯穿软件的整个研发周期，进入安全行业后，大家会发现还有很多其他机制的，但这都不在本篇讨论范围，大家只需知道，***测试只是最后的安全质量验收阶段。</p>
<p>软件根据运行使用场景分为很多种，PC桌面端软件、手机APP软件以及浏览器使用的Web软件等。本文讨论的就是Web软件的***测试。</p>
<p>本文分为基础知识、工具使用、基本漏洞和实践四部分，可以依照这个顺序学习，也可以灵活食用。推荐掌握基础知识后，上手一下测试工具，然后学一个漏洞，立马实践一下。</p>
<p>最后说一下本文的熟练度：掌握>深入了解>了解。赶紧往下学起来吧！</p>
<h2 data-id="heading-1">一、基础知识</h2>
<p>要进行Web***测试所需的知识，有重点划分，有些了解一点就行。后续可以深入，当然深入起来每个都可以是一个本科课程。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b8dda22346346e88df038b9b1559932~tplv-k3u1fbpfcp-zoom-1.image" alt="808020A7E0ABA060CA24558C45AE22F85C76DB.jpg" title="2059" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1.1 信息安全（了解）</h3>
<p>学习信息安全是为了培养安全意识，做***测试心中当然要有个标准，知道什么是安全的什么是不安全的，一些漏洞的评判标准并不是固定的，出现复杂情况就需要我们自己判断。</p>
<p>这个课程比较小众，可以去慕课网看看，一般看《信息安全概论》即可</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.icourse163.org%2Fsearch.htm%3Fsearch%3D%25E4%25BF%25A1%25E6%2581%25AF%25E5%25AE%2589%25E5%2585%25A8%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.icourse163.org/search.htm?search=%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8#/" ref="nofollow noopener noreferrer">www.icourse163.org/search.htm?…</a></p>
<p>这个课程可以在学习计划中排到较低的优先级，都是入门的，可以算视野拓展了，实际作用不大。可以了解信息安全的几个要素、***进攻流程、访问控制模型、信息安全的其他模型和行业标准。</p>
<h4 data-id="heading-3">1.2 密码学（深入了解）</h4>
<p>这个其实也是信息安全中的内容，但是内容较多有时可能会单独拿出来。</p>
<p>密码学有助于我们理解ssl、https、web应用中的密码加密传输环节。</p>
<p>要掌握的内容有：</p>
<p>哈希算法的定义，哈希算法的暴力破解、字典破解和彩虹表。</p>
<p>对称加密和非对称加密</p>
<p>具体算法我们不要求掌握，单要熟记理解各种加密的加密过程、优缺点、应用场景等。</p>
<p>除了去找系统的课程，我给大家推荐一个科普视频，有助于快速了解。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1P7411375j" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1P7411375j" ref="nofollow noopener noreferrer">信息传输中的安全隐患</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1q7411E7oa" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1q7411E7oa" ref="nofollow noopener noreferrer">对称加密/非对称加密/混合加密</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1C7411L7UZ" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1C7411L7UZ" ref="nofollow noopener noreferrer">哈希函数/消息认证码/重放进攻</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1KE41177kK" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1KE41177kK" ref="nofollow noopener noreferrer">数字签名/防事后否认/中间人进攻</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1xE411N7SP" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1xE411N7SP" ref="nofollow noopener noreferrer">数字证书/证书链与CA/HTTPS</a></p>
<h3 data-id="heading-4">1.3 计算机网络</h3>
<p>计算机网络在web***测试中无疑是最重要的基础，我们抓包、扫描主机开放的其他服务端口等，都是在计网基础之上的。后续小伙伴们想深入学习推荐《计算机网络自顶向下方法》，此书像剥洋葱一样讲解了我们目前使用的网络是如何一层一层封装的，其中除了面试常问的tcp握手等较常见的问题，还有阻塞机制等。</p>
<h4 data-id="heading-5">1.3.1 分层模型（了解）</h4>
<p>了解tcp/ip五层模型，OSI七层模型。了解哪一层有哪些常用协议，要知道这些协议并不是随意地在理论上分层分类，而是有实际的封装关系的。</p>
<h4 data-id="heading-6">1.3.2 IP、TCP协议（掌握）</h4>
<p>深入理解ip局域网和公网、tcp套接字、路由器NAT转发等。日后熟练了要能知道局域网IP段、熟悉一些常见的服务端口。</p>
<p>主要是搞懂一些IPv4的机制，为我们日常处理某些问题提供理论支撑。如测试给的环境我们肯定都能访问，但是如果觉得存在某个漏洞，想通过控制服务器回访我们自己的电脑来证明存在漏洞，这时如果服务器在公网，而你在某个局域网则会访问失败。</p>
<p>推荐视频：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1DD4y127r4" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1DD4y127r4" ref="nofollow noopener noreferrer">【硬件科普】IP地址是什么东西？IPV6和IPV4有什么区别？公网IP和私有IP又是什么？</a></p>
<p>顺便把DNS也了解一下，后续使用dnslog有用。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Rp4y1a7xQ" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1Rp4y1a7xQ" ref="nofollow noopener noreferrer">【硬件科普】能上QQ但是打不开网页？详解DNS服务，DNS解析，DNS劫持和污染</a></p>
<h4 data-id="heading-7">1.3.3 HTTP协议（掌握）</h4>
<p>了解HTTP报文格式、掌握一些常见头属性的作用、了解一些常见的状态码、掌握各种HTTP方法（GET、POST、OPTION、TRACE、PUT、DELETE等）及其参数格式和编码。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F70949908" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/70949908" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/70949908</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fan-wen%2Fp%2F11180076.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/an-wen/p/11180076.html" ref="nofollow noopener noreferrer">www.cnblogs.com/an-wen/p/11…</a></p>
<h4 data-id="heading-8">1.3.4 SSL、HTTPS（深入了解）</h4>
<p>我们在发现一些敏感信息明文传输时，会要求使用前端加密或https协议来修复。我们需要了解为什么认定https是安全的。到后面我们开始实践后，还可以返回来思考，为什么我们需要在浏览器导入工具的证书？为什么服务器用了https我们仍可以抓包看到明文？</p>
<p>弄清ssl和https的关系，简单地说https=http+ssl，但是ssl技术也可用于加密其他通信。还要ssl在网络分层模型中在第几层，弄清https中数据封装的顺序，http、tcp、ssl的先后。</p>
<p>资料：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1w4411m7GL" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1w4411m7GL" ref="nofollow noopener noreferrer">【硬核】HTTPS原理全解析</a></p>
<h3 data-id="heading-9">1.4 Web前端（深入了解）</h3>
<p>主要是学会一些html和JavaScript，才能测XSS漏洞，css样式我们很少不涉及。</p>
<p>html即超文本标记语言，只需了解它有标签和属性，浏览器会渲染他们使文本呈现一些简单的样式。具体有哪些标签不用去记。</p>
<p>JavaScript是网页的脚本语言，控制着网页的行为，属于动态编程语言，灵活强大。跨站脚本进攻中的脚本指的就是 JavaScript。我们学习JavaScript并不是拿去写前端的，只是用于测试网页是否存在漏洞，侧重点在于搞懂有哪些方式能够触发js代码，也就是花式触发js代码，我们一般用函数alert来证明js被触发。</p>
<p>常见的几点：script标签、所有标签中的事件、部分标签中的src属性和href属性data属性。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.javascript.info%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.javascript.info/" ref="nofollow noopener noreferrer">现代 JavaScript 教程</a></p>
<h3 data-id="heading-10">1.5 浏览器机制（掌握）</h3>
<p>掌握浏览器同源策略、web身份认证</p>
<p>同源策略和cookie共同支撑起了web的身份认证基础。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FSecurity%2FSame-origin_policy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy" ref="nofollow noopener noreferrer">浏览器的同源策略</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F52091630" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/52091630" ref="nofollow noopener noreferrer">一文带你看懂cookie，面试前端不用愁</a></p>
<h3 data-id="heading-11">1.6 SQL</h3>
<p>要求学会基本语法即可。主流的数据库有MySQL和Oracle，二者语法有些差别。</p>
<p>推荐先学MySQL，看书即可，推荐《MySQL必知必会》，很薄很小的一本书，很快就能啃完。</p>
<p>至于Oracle，补习一下字符串拼接、对应的sleep函数等，就可以应付sql注入了。</p>
<h3 data-id="heading-12">1.7 linux shell</h3>
<p>若是碰到命令执行的点，学习一下一句话反弹shell，以及反引号的命令替换，即输出字符串时，把字符串中反引号的部分替换为其执行的结果。当然，最好先用nmap扫描一下确认是Linux机器。</p>
<p>想要上手Linux命令行or运维等，推荐教程：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV187411y7hF" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV187411y7hF" ref="nofollow noopener noreferrer">【狂神说Java】Linux最通俗易懂的教程阿里云真实环境学习</a></p>
<h3 data-id="heading-13">1.8 行业术语</h3>
<p>白帽子：一般指正面的***</p>
<p>Payload：有效的进攻代码</p>
<p>Poc：可以说是漏洞验证程序，运行这个程序就可以检测是否存在漏洞。一些验证起来繁琐、步骤多的漏洞，可以写Poc来提高效率。</p>
<p>CVE：英文全称是 “Common Vulnerabilities & Exposures” 通用漏洞披露。CVE就好像是一个字典表，为广泛认同的信息安全漏洞或者已经暴露出来的弱点给出一个公共的名称。</p>
<p>反序列化：可以理解为序列化是指将一个数据结构输出为字符串的过程，反序列化是根据字符串生成数据结构的过程，在Java后端中字符串是json格式，数据结构就指类。</p>
<p>其他一些属于可能字面意思就能理解，如弱口令、弱密码、短信轰炸......</p>
<h2 data-id="heading-14">二、工具使用</h2>
<h3 data-id="heading-15">2.1 BurpSuite</h3>
<p>这个是我们***测试的利器，除了强大的抓包、重放功能，还有暴力破解、支持插件等。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ft0data.gitbooks.io%2Fburpsuite%2Fcontent%2Fchapter1.html" target="_blank" rel="nofollow noopener noreferrer" title="https://t0data.gitbooks.io/burpsuite/content/chapter1.html" ref="nofollow noopener noreferrer">burpsuite实战指南</a></p>
<p>重点是Proxy模块以及证书安装，配置好就能开始抓包了；Repeater模块是重放，很简单；Intruder模块是暴力破解，有时候可能需要字典，但是测试过程中证明暴力破解一般不需要真的去找个几千几万甚至几十万的字典...</p>
<p>笔者只说一个技巧，就是如何排除浏览器自身的包、心跳报文等垃圾信息的干扰。</p>
<ol>
<li>Proxy的Option中勾选最下面的Don't send items to Proxy history or live tasks, if out of scope</li>
<li>Target的Scope中Include in scope中添加一个any，Exclude from scope中添加你的黑名单url，支持正则，也可以在Proxy中选中报文右键Remove from scope添加</li>
<li>保存规则，每次启动时自动加载</li>
</ol>
<h3 data-id="heading-16">2.2 netcat</h3>
<p>安全测试中的瑞士军～刀，使用一般是 <code>nc -lvvp</code></p>
<p>用于接收反弹过来的shell，或是接收http请求。</p>
<h3 data-id="heading-17">2.3 dnslog</h3>
<p>在[1.2.2 IP、TCP协议（掌握）](### 1.2.2 IP、TCP协议（掌握）)中我们提到，有些情况我们需要一个公网机器来接收被测服务器的请求，如果是简单的http请求等，我们可以使用<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.dnslog.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.dnslog.cn/" ref="nofollow noopener noreferrer">dnslog</a></p>
<p>如果是文件包含，远程调用，那只能使用公网主机了。</p>
<h3 data-id="heading-18">2.4 sqlmap</h3>
<p>新人可以试试，自动检测sql注入的工具。</p>
<p>一般我们都把burp的报文保存到txt里，这样就直接有cookie了，然后在要注入的点打上星号*，sqlmap运行 <code>python sqlmap.py -r %filepath%</code> 即可，其它参数：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Finsane-Mr-Li%2Fp%2F10150165.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/insane-Mr-Li/p/10150165.html" ref="nofollow noopener noreferrer">www.cnblogs.com/insane-Mr-L…</a></p>
<p>一般会追加一些参数来指定成功注入后，干一些什么事，如执行系统命令、列出数据库名等。</p>
<h3 data-id="heading-19">2.5 Nmap</h3>
<p>主要用于扫描主机开放的不安全的服务，以及判断操作系统类型（当然这个参考就行，不一定准）</p>
<p>安装带图形界面的，扫描时配置选all TCP ports</p>
<h2 data-id="heading-20">三、基本漏洞</h2>
<p>学习和快速上手业务方面的安全问题，我推荐书籍《Web***指业务安全实战指南》，这本书比之前推荐的必知必会要厚，但其实字数不多，也很好理解，看一遍不会花太多时间，但是能让读者快速入门实践。</p>
<p>再进一步学习推荐《白帽子讲Web安全》</p>
<p>其实大大小小地漏洞很多，甚至每个CVE都能算一个漏洞，但是哪些要覆盖测试，根据自己的情况而定，自己可以列一个测试清单。一些漏洞的测试技巧甚至步骤都是固定的，这里罗列一下，大家自行整理。</p>
<ul>
<li>
<p>认证模块、用户系统</p>
<ul>
<li>信息泄露</li>
<li>暴力破解</li>
<li>认证绕过</li>
<li>登录处注入</li>
</ul>
</li>
<li>
<p>配置安全     用户系统</p>
<ul>
<li>cookie未设置HttpOnly</li>
<li>开启了不安全的HTTP方法</li>
<li>Host头进攻</li>
<li>URL跳转</li>
</ul>
</li>
<li>
<p>Session测试</p>
</li>
<li>
<p>用户权限管理</p>
<ul>
<li>未授权</li>
<li>越权访问</li>
</ul>
</li>
<li>
<p>信息泄露</p>
</li>
<li>
<p>文件上下载</p>
</li>
<li>
<p>CSRF & ***F</p>
</li>
<li>
<p>XXE外部实体注入</p>
<ul>
<li>报文注入</li>
<li>导入文件注入</li>
</ul>
</li>
<li>
<p>SQL注入</p>
</li>
<li>
<p>XSS脚本注入</p>
</li>
<li>
<p>服务端命令注入</p>
</li>
<li>
<p>逻辑漏洞</p>
</li>
</ul>
<p>最后再推荐一个项目 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwiki.owasp.org%2Fimages%2Fd%2Fdc%2FOWASP_Top_10_2017_%25E4%25B8%25AD%25E6%2596%2587%25E7%2589%2588v1.3.pdf" target="_blank" rel="nofollow noopener noreferrer" title="https://wiki.owasp.org/images/d/dc/OWASP_Top_10_2017_%E4%B8%AD%E6%96%87%E7%89%88v1.3.pdf" ref="nofollow noopener noreferrer">owasp top10</a> ，开放式Web应用程序安全项目（OWASP，Open Web Application Security Project）是一个非营利性组织，它提供有关计算机和互联网应用程序的公正、实际、有成本效益的信息。其top10项目列出了Web前10的漏洞，有兴趣的可以研究研究。</p>
<h2 data-id="heading-21">四、实践</h2>
<p>学了知识当然要实践检验一番才能加深理解和记忆，但是没有网站测怎么办呢？测公网上运营的网站是不可取的哦。</p>
<p>用于练习的网站我们称之为靶机或靶场，推荐dvwa，一个用php写的web服务，我们下载phpstudy就能搭建</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_42263820%2Farticle%2Fdetails%2F106749458" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_42263820/article/details/106749458" ref="nofollow noopener noreferrer">DVWA+Phpstudy靶场平台搭建</a></p>
<p>搭建好就能自己练习了，可以自己先过一遍。没思路的话可以看教程。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freebuf.com%2Fauthor%2Flonehand" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freebuf.com/author/lonehand" ref="nofollow noopener noreferrer">lonehand</a>曾写了一系列很好的教程，但是最近都被freebuf下架了，可以看看这里的搬运：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Flinuxsec%2Fcategory%2F912871.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/linuxsec/category/912871.html" ref="nofollow noopener noreferrer">www.cnblogs.com/linuxsec/ca…</a></p></div>  
</div>
            