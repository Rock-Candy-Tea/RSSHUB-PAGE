
---
title: '浅析URL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f73f07be7c148898f9c8aa85e3991da~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 23:29:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f73f07be7c148898f9c8aa85e3991da~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 何为URL</h1>
<p>URL的全称为<strong>Uniform Resource Locator</strong>，中文译名一般为<strong>统一资源定位符</strong>。URL的概念与html、http等概念相伴而生，经常被（错误地）作为同义词相互替换用。</p>
<p>URL的作用是“<strong>给定的独特资源在Web上的地址</strong>”<sup>[2]</sup>。“理论上说，每个有效的URL都指向一个唯一的资源。这个资源可以是一个 HTML 页面，一个 CSS 文档，一幅图像，等等”。这是MDN的原文，此处将其引用。也就是说，<strong>资源</strong>可以指互联网上存在的一切，比如网页、图片等等，而URL的作用就是给每个资源分配一个<strong>地址</strong>编码。</p>
<p>URL由很多部分构成。下面以一个示例URL来说明：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">http:<span class="hljs-comment">//www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>scheme</code>：对应的部分是<code>http://</code>，即规定了该URL所使用的<strong>协议（protocol）</strong>。</li>
<li><code>authority</code>：对应的部分是<code>www.example.com：80</code>，即该网址的<strong>域名（domain）和端口（port）</strong>。域名和端口通过冒号分开，即在<code>authority</code>中，<code>www.example.com</code>是域名，<code>:80</code>是端口。由于互联网中网址默认端口为<code>80</code>（http）或<code>443</code>（https），所以端口一般略去不写。除了域名之外，也可以用ip地址代替域名。</li>
<li><code>Path to resource</code>：即资源路径。对应的部分是<code>path/to/myfile.html</code>。在Web的早期阶段，像这样的路径表示Web服务器上的物理文件位置。如今，它主要是由没有任何物理现实的Web服务器处理的抽象。</li>
<li><code>Parameters</code>：参数。对应的部分是<code>?key1=value1&key2=value2</code>，通常以问号开头。参数通常都是键值对形式，如这里的<code>key1=value1</code>，多个参数以<code>&</code>隔开。用处是传递给服务器，进行额外操作。</li>
<li><code>anchor</code>：锚点。对应的部分是<code>#SomewhereInTheDocument</code>，用于在文章的不同部分之间跳转。值得注意的是，＃后面的部分（也称为片段标识符）从来没有发送到请求的服务器。</li>
</ul>
<p>通过上面的解析，我们便可以很轻松地读懂浏览器那一长串好像乱码一样的地址了。</p>
<h1 data-id="heading-1">2. 何为DNS？</h1>
<p>DNS全称为Domain Name System，即“域名系统”。“是包含 TCP/IP 的一系列行业标准协议中，同时 DNS 客户端和 DNS 服务器为计算机和用户提供计算机名称到 IP 地址的映射名称解析服务”<sup>[3]</sup>。DNS最重要的功能是将域名映射为数字形式的IP地址。</p>
<p>关于DNS的工作原理等，可以阅读<a href="https://www.ibm.com/cloud/learn/dns" target="_blank" rel="nofollow noopener noreferrer">IBM所写的文章（英文）</a>。</p>
<h1 data-id="heading-2">3. nslookup怎么用？</h1>
<p>该命令可以用于提供诊断DNS结构的信息。后面直接输入域名即可。如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f73f07be7c148898f9c8aa85e3991da~tplv-k3u1fbpfcp-watermark.image" alt="对于北京大学官网使用nslookup" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">4. IP与ping详解</h1>
<p>IP地址是分配给连接到使用Internet协议的网络的每个设备的一串数字，有IPv4和IPv6两种形式的IP地址。在广泛使用IPv6之前，IP基本上等同于IPv4。IP地址的作用是提供的一种统一的地址格式，为互联网上的每一个网络和每一台主机分配一个逻辑地址，以此来屏蔽物理地址的差异。</p>
<p><code>ping</code>是一个命令行使用的命令，它的作用是用于检查本机与外网连接是否正常。如下图示例：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46b4c7ac0f1e4438928d7920b20dff8a~tplv-k3u1fbpfcp-watermark.image" alt="ping清华官网" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">5. 域名详解</h1>
<p>域名即网站的地址。域名被用于 URL 识别一个服务器属于哪个特定的网站。</p>
<p>以一个例子来说明域名的分类。例子来源于MDN：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be2b16405b4f4e10b7862a9095fff51c~tplv-k3u1fbpfcp-watermark.image" alt="域名例子" loading="lazy" referrerpolicy="no-referrer"></p>
<p>域名的阅读应遵循牌匾式阅读顺序：从右往左读。从右往左依次分为这么几个部分：</p>
<ul>
<li>TLD：即Top Level Domain，顶级域名，可以用于表示该网址的功能是什么，或者属于哪个国家或地区。例如，<code>.ac</code>代表学术机构，<code>.gov</code>代表政府组织，<code>.edu</code>代表高校或者教育单位。<code>.cn</code>代表中国，<code>.hk</code>代表香港等等。</li>
<li>label：在图片中分为<code>label1</code>和<code>label2</code>，紧随TLD出现。标签由1到63个大小写不敏感的字符组成，这些字符包含字母A-z，数字0-9，甚至 “-” 这个符号（当然，“-” 不应该出现在标签开头或者标签的结尾）。</li>
</ul>
<p>注意：<code>www</code>是历史遗留问题，用处不大。</p>
<h1 data-id="heading-5">References</h1>
<ul>
<li>[1] <a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL" target="_blank" rel="nofollow noopener noreferrer">What is a URL? (English)-MDN</a></li>
<li>[2] <a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL" target="_blank" rel="nofollow noopener noreferrer">什么是URL（中文）-MDN</a></li>
<li>[3] <a href="https://docs.microsoft.com/zh-cn/windows-server/networking/dns/dns-top" target="_blank" rel="nofollow noopener noreferrer">域名系统 (DNS)</a></li>
<li>[4] <a href="https://www.ibm.com/cloud/learn/dns" target="_blank" rel="nofollow noopener noreferrer">DNS - IBM</a></li>
<li>[5] <a href="https://aws.amazon.com/cn/route53/what-is-dns/" target="_blank" rel="nofollow noopener noreferrer">DNS - AWS</a></li>
<li>[6] <a href="https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup" target="_blank" rel="nofollow noopener noreferrer">nslookup - Microsoft</a></li>
<li>[7] <a href="https://developer.mozilla.org/zh-CN/docs/Glossary/IP_Address" target="_blank" rel="nofollow noopener noreferrer">IP-MDN</a></li>
<li>[8] <a href="https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping" target="_blank" rel="nofollow noopener noreferrer">ping命令详解</a></li>
<li>[9] <a href="https://developer.mozilla.org/zh-CN/docs/Glossary/Domain_name" target="_blank" rel="nofollow noopener noreferrer">域名-MDN</a></li>
<li>[10] <a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name" target="_blank" rel="nofollow noopener noreferrer">域名详解-MDN</a></li>
</ul></div>  
</div>
            