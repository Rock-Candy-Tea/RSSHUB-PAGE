
---
title: '浅析 URL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6288'
author: 掘金
comments: false
date: Mon, 03 May 2021 00:11:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=6288'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1. URL 包含哪几部分，每部分分别有什么作用？</strong></p>
<p>一个完整的URL=协议+域名或IP+端口号+路径+查询字符串+锚点。</p>
<p>举例：<a href="https://www.baidu.com/s?wd=hello&rsv_spt=1#5" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com/s?wd=hello&…</a></p>
<ul>
<li>“https:”为协议部分，它表明了浏览器必须使用何种协议，该URL表明网页使用的是HTTPS协议。</li>
<li>“<a href="http://www.baidu.xn--com-9o0a/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com”</a> 为域名部分，它表明正在请求哪个Web服务器，一个URL中，也可以使用IP地址。</li>
<li>此URL中未写明端口，因为HTTPS默认端口443。</li>
<li>“/s”是路径部分，表明网络服务器上资源的路径。</li>
<li>“?wd=hello&rsv_spt=1”为查询字符串，查询字符串中可以允许有多个参数，参数与参数之间用“&”作为分隔符。查询字符串是提供给网络服务器的额外参数。</li>
<li>“#5”是锚点，锚点表示资源中的一种“书签”，给浏览器显示位于该“加书签”位置的内容的方向。</li>
</ul>
<p><strong>2. DNS 的作用是什么，nslookup 命令怎么用？</strong></p>
<p>DNS (Domain Name System) 域名系统，是一个层次化、分散化的Internet连接资源命名系统。DNS维护着一个包含域名与对应资源例如IP地址的列表。</p>
<p>DNS最突出的功能是将易于记忆的域名(例如mozilla.org)翻译成为数字化的IP地址(例如151,106,5,172).这一从域名到IP地址的映射过程被成为DNS查询(DNS lookup),与之对应,DNS反向查询(rDNS)用来找到与IP地址对应的域名。</p>
<p><strong>nslookup命令</strong>用来查询DNS的记录，查看域名解析是否正常，在网络故障的时候用来诊断网络问题。其用法如下：</p>
<ul>
<li><strong>直接查询</strong>：<code>nslookup domain [dns-server]</code></li>
<li><strong>查询其他记录</strong>：<code>nslookup -qt=type domain [dns-server]</code></li>
</ul>
<p>其中，type可以是以下这些类型：</p>
<ol>
<li>A 地址记录</li>
<li>AAAA 地址记录</li>
<li>AFSDB Andrew文件系统数据库服务器记录</li>
<li>ATMA ATM地址记录</li>
<li>CNAME 别名记录</li>
<li>HINFO 硬件配置记录，包括CPU、操作系统信息</li>
<li>ISDN 域名对应的ISDN号码</li>
<li>MB 存放指定邮箱的服务器</li>
<li>MG 邮件组记录</li>
<li>MINFO 邮件组和邮箱的信息记录</li>
<li>MR 改名的邮箱记录</li>
<li>MX 邮件服务器记录</li>
<li>NS 名字服务器记录</li>
<li>PTR 反向记录</li>
<li>RP 负责人记录</li>
<li>RT 路由穿透记录</li>
<li>SRV TCP服务器信息记录</li>
<li>TXT 域名对应的文本信息</li>
<li>X25 域名对应的X.25地址记录</li>
</ol>
<ul>
<li><strong>查询更具体的信息</strong>：<code>nslookup –d [其他参数] domain [dns-server]</code></li>
</ul>
<p>只要在查询的时候，加上-d参数，即可查询域名的缓存。</p>
<p><strong>3. IP 的作用是什么，ping 命令怎么用？</strong></p>
<p>IP地址（英语：IP Address，全称Internet Protocol Address），又译为网际协议地址、互联网协议地址。当设备连接网络，设备将被分配一个IP地址，用作标识。通过IP地址，设备间可以互相通讯，如果没有IP地址，我们将无法知道哪个设备是发送方，无法知道哪个是接收方。IP地址有两个主要功能：<strong>标识设备或网络</strong> 和 <strong>寻址</strong>（英语：location addressing）。</p>
<p>ping 命令用于检测主机。</p>
<p>执行 ping 指令会使用 ICMP 传输协议，发出要求回应的信息，若远端主机的网络功能没有问题，就会回应该信息，因而得知该主机运作正常。</p>
<p><strong>语法：</strong>
<code>ping [-dfnqrRv][-c<完成次数>][-i<间隔秒数>][-I<网络界面>][-l<前置载入>][-p<范本样式>][-s<数据包大小>][-t<存活数值>][主机名称或IP地址]</code></p>
<p><strong>4. 域名是什么，分别有哪几类域名？</strong></p>
<p>网域名称（英语：Domain Name，简称：Domain），简称域名、网域，是由一串用点分隔的字符组成的互联网上某一台计算机或计算机组的名称，用于在数据传输时标识计算机的电子方位。<strong>域名可以说是一个IP地址的代称</strong>，目的是为了便于记忆后者。</p>
<p>域名主要分为三类：</p>
<ol>
<li>第一类是通用顶级域名（General top Level Domain，简称gTLD）</li>
<li>第二类是国家及地区代码顶级域名(country Code Top Level Domain，简称ccTLD)</li>
<li>第三类是2011年“新通用顶级域名”的计划实施以来新增的新通用顶级域名（New Generic Top-level Domain，简称NEW gTLD）</li>
</ol></div>  
</div>
            