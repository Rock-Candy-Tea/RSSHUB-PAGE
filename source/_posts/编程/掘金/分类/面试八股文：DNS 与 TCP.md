
---
title: '面试八股文：DNS 与 TCP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f18747fc9e496f937c7a7f10e83c0a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 02:22:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f18747fc9e496f937c7a7f10e83c0a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">一图概览</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f18747fc9e496f937c7a7f10e83c0a~tplv-k3u1fbpfcp-watermark.image" alt="2021-6-8-18-20-56.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">DNS & hosts</h1>
<p>DNS，全称：<strong>D</strong>omain <strong>N</strong>ame <strong>S</strong>ystem，中文：域名系统</p>
<blockquote>
<p>域名系统本身的原理是比较复杂的，但域名系统的功能很简单，就是<strong>输入一个域名，输出一个 IP</strong>，这里我们只对 DNS 做简单讨论</p>
</blockquote>
<p>举例说明：</p>
<ol>
<li>
<p>在浏览器输入 baidu.com 这个地址</p>
</li>
<li>
<p>浏览器需要知道你访问的这个地址对应的 IP 是多少，于是浏览器就会去问操作系统</p>
</li>
<li>
<p>如果操作系统也不知道，就会去问电信、移动、联通这样的<strong>网络运行商</strong>（以下简称 ISP）</p>
</li>
<li>
<p>当你付费之后，网络运营商就会告诉你 baidu.com 这个地址对应的 IP 是多少（假设这里 baidu.com 对应的 IP 是 1.2.3.4），然后将 IP 返回给你</p>
</li>
<li>
<p>浏览器获取到 baidu.com 对应的 IP 之后，就会与 1.2.3.4 这个 IP <strong>建立 TCP 连接</strong></p>
</li>
</ol>
<p>细化过程：</p>
<ol>
<li>
<p>在浏览器输入 baidu.com 这个地址的时候，浏览器首先会去检查自身是否有缓存，如果发现之前访问过 baidu.com ，那么浏览器就会直接将上一次的 IP 进行返回</p>
</li>
<li>
<p>如果浏览器没有缓存，就回去询问操作系统，然后操作系统首先也是会检查自身是否有缓存，如果没有就会去询问 ISP（网络运行商）</p>
</li>
<li>
<p>平时我们修改 hosts 这个文件，其实就是在手动给操作系统设置缓存，比如我们在 hosts 中写入<code>baidu.com 2.3.4.5</code>，以后每次访问 baidu.com 这个地址的时候就不会再去询问 ISP 了，直接会通过 hosts 中的设置去访问 2.3.4.5 这个 IP</p>
</li>
</ol>
<h1 data-id="heading-2">TCP 三次握手</h1>
<p>TCP 全称：<strong>T</strong>ransmission <strong>C</strong>ontrol <strong>P</strong>rotocol，即<strong>传输控制协议</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064307e5837449af9973d6aef43df743~tplv-k3u1fbpfcp-watermark.image" alt="无标题-2021-02-22-1714.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设 A 是浏览器，B 是服务器</p>
<ol>
<li>
<p>A 首先会向 B 发送一个叫做<code>SYN(x)</code>（假设这里 x = 100）的信息</p>
<blockquote>
<p>SYN 是 synchronize(同步) 的缩写，同步不是指「同步异步」中的同步，而是「同步信息」中的同步；这里的 x 一般是一个数字编号，且 x 和 y 一般都是从 0 开始的，这里我们对 x 和 y 的意义不做讨论，有兴趣的请自行研究</p>
</blockquote>
</li>
<li>
<p>B 收到 A 发来的同步信息后，就会返回<code>ACK(x+1)</code>（101） <code>SYN(y)</code>（这里假设 y = 200）</p>
<blockquote>
<p>ACK 是 acknowledge(知道) 的缩写</p>
</blockquote>
</li>
<li>
<p>然后 A 会回复消息 <code>ACK(y+1)</code>（201）给 B</p>
</li>
</ol>
<p>从以上过程中能够确保以下几件事：</p>
<ul>
<li>A 可以向 B 发送信息</li>
<li>B 能收到 A 发送的信息</li>
<li>B 也可以向 A 发送信息</li>
<li>A 也能收到 B 发送的信息</li>
</ul>
<p><strong>三次握手成功后</strong>就开始建立 TCP 连接了，建立连接后就可以开始<strong>传输内容</strong>了（一般是 HTTP 内容，也可以是其他内容，且传输的过程也可以是双向的，并非一定是单向的），HTTP 内容传输结束后，就会「关闭」</p>
<h1 data-id="heading-3">TCP 四次挥手</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68d5b5ff4fc849feb5ba6a975c482f3c~tplv-k3u1fbpfcp-watermark.image" alt="无标题-2021-02-22-17142.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>上述内容传输完成后，A 会发送一个<code>FIN(x)</code></p>
<blockquote>
<p>注意：不一定是 A 先发送 FIN，也可以是 B 先发送</p>
</blockquote>
</li>
<li>
<p>B 先回复<code>ACK(x+1)</code></p>
<blockquote>
<p>注意：关闭时的 x 和 y 一般都不是 0</p>
</blockquote>
</li>
<li>
<p>然后再回复<code>FIN(y)</code></p>
<blockquote>
<p>步骤 2 和步骤 3 中间可能会夹杂着其他内容</p>
</blockquote>
</li>
<li>
<p>A 回复<code>ACK(y+1)</code></p>
</li>
</ol>
<p>最后，A 和 B 各自关闭自己的 TCP 连接</p>
<h1 data-id="heading-4">一些 Q & A</h1>
<h2 data-id="heading-5">为什么需要关闭 TCP 连接？</h2>
<p>因为一直保持连接会浪费内存和 CPU</p>
<h2 data-id="heading-6">TCP 和 UDP 的区别是什么？</h2>
<blockquote>
<p>八股文，面试必背</p>
</blockquote>
<ul>
<li>TCP 面向连接有状态，UDP 无状态</li>
<li>TCP 可靠（不丢失不重复），UDP 不可靠</li>
<li>TCP 传输效率较低，UDP 较高</li>
</ul>
<h2 data-id="heading-7">为什么 TCP 的三次握手不能精简为两次？</h2>
<p>为了确保客户端（A端）能接收到服务端（B端）的数据（只有两次的话，无法判断 A 是否能接收到 B 的数据）</p>
<h2 data-id="heading-8">为什么 TCP 的四次挥手不能将中间两步合并成一步？</h2>
<p>因为两步中间（指发送<code>ACK(x+1)</code>和<code>FIN(y)</code>之间）往往会有其他数据需要发送，需要等其他数据发送完成之后，再发送<code>FIN(y)</code></p></div>  
</div>
            