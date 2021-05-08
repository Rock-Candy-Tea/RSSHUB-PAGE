
---
title: 'Vue使用uuid-npm快速生成uuid，适用于多种场景'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d59105eada646aaa95f0ad4319cdd1c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 18:56:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d59105eada646aaa95f0ad4319cdd1c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">首先，什么是 UUID ？</h5>
<p>UUID 是 通用唯一识别码（Universally Unique Identifier）的缩写，是一种软件建构的标准，亦为开放软件基金会组织在分布式计算环境领域的一部分。其目的，是让分布式系统中的所有元素，都能有唯一的辨识信息，而不需要通过中央控制端来做辨识信息的指定。
RFC 4122第3节提供UUID字符串表示形式的定义。UUID 是由一组32位数的16进制数字所构成，是故 UUID 理论上的总数为1632=2128，约等于3.4 x 10123。
也就是说若每纳秒产生1百万个 UUID，要花100亿年才会将所有 UUID 用完
格式：
UUID 的十六个八位字节被表示为 32个十六进制数字，以连字号分隔的五组来显示，形式为 8-4-4-4-12，总共有 36个字符（即三十二个英数字母和四个连字号）。例如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">123e4567</span>-e89b-12d3-a456-<span class="hljs-number">426655440000</span>
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数字 M 的四位表示 UUID 版本，当前规范有5个版本，M可选值为1, 2, 3, 4, 5 ；
数字 N 的一至四个最高有效位表示 UUID 变体( variant )，有固定的两位10xx因此只可能取值8, 9, a, b；
UUID版本通过 M 表示，当前规范有5个版本，可选值为1, 2, 3, 4, 5。这5个版本使用不同算法，利用不同的信息来产生 UUID，各版本有各自优势，适用于不同情景。具体使用的信息</p>
<h5 data-id="heading-1">UUID - npm</h5>
<p>Vue 、React 等可以直接通过 npm 安装并使用 uuid。
用于创建RFC4122 UUID。
完整 -支持RFC4122版本1、3、4和5 UUID。
1、安装：npm install uuid
Vue使用uuid-npm快速生成uuid，适用于多种场景
2020-08-19阅读 2K0
最近项目中需要记录访客的 UUID 以实现用户存留、日活、月活等用户画像。
首先，什么是 UUID ？
UUID 是 通用唯一识别码（Universally Unique Identifier）的缩写，是一种软件建构的标准，亦为开放软件基金会组织在分布式计算环境领域的一部分。其目的，是让分布式系统中的所有元素，都能有唯一的辨识信息，而不需要通过中央控制端来做辨识信息的指定。</p>
<p>RFC 4122第3节提供UUID字符串表示形式的定义。UUID 是由一组32位数的16进制数字所构成，是故 UUID 理论上的总数为1632=2128，约等于3.4 x 10123。
也就是说若每纳秒产生1百万个 UUID，要花100亿年才会将所有 UUID 用完</p>
<p>格式：
UUID 的十六个八位字节被表示为 32个十六进制数字，以连字号分隔的五组来显示，形式为 8-4-4-4-12，总共有 36个字符（即三十二个英数字母和四个连字号）。例如：</p>
<p>123e4567-e89b-12d3-a456-426655440000
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx</p>
<p>数字 M 的四位表示 UUID 版本，当前规范有5个版本，M可选值为1, 2, 3, 4, 5 ；</p>
<p>数字 N 的一至四个最高有效位表示 UUID 变体( variant )，有固定的两位10xx因此只可能取值8, 9, a, b；</p>
<p>UUID版本通过 M 表示，当前规范有5个版本，可选值为1, 2, 3, 4, 5。这5个版本使用不同算法，利用不同的信息来产生 UUID，各版本有各自优势，适用于不同情景。具体使用的信息</p>
<p>UUID - npm
Vue 、React 等可以直接通过 npm 安装并使用 uuid。</p>
<p>用于创建RFC4122 UUID。</p>
<p>完整 -支持RFC4122版本1、3、4和5 UUID。</p>
<p>1、安装：
<code>npm install uuid</code></p>
<p>2、生成一个 UUID ：</p>
<p><code>import &#123; v4 as uuidv4 &#125; from 'uuid'; </code></p>
<p><code>uuidv4(); // ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'</code></p>
<p><code>拿到uuid  let uuid = uuidv4() </code></p>
<p>3、使用 CommonJS 语法：</p>
<p><code>const &#123; v4: uuidv4 &#125; = require('uuid');</code></p>
<p><code>uuidv4(); // ⇨ '1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed'</code></p>
<p>API摘要 具体的API，可以去 npm 的详情页面查看。:<a href="https://www.npmjs.com/package/uuid#api" target="_blank" rel="nofollow noopener noreferrer">www.npmjs.com/package/uui…</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d59105eada646aaa95f0ad4319cdd1c~tplv-k3u1fbpfcp-watermark.image" alt="BPSM)GF~[SGNRPP]M68YP3M.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>应用场景：
我们可以根据需求，来满足不用的应用场景，比如：</p>
<p>页面刷新即生成一个新的 UUID ：</p>
<p><code>uuid.v4() //直接加在页面的任意位置</code></p>
<h6 data-id="heading-2">打开页面/标签，即生成一个 UUID ，页面刷新 UUID 不会变。</h6>
<h6 data-id="heading-3">打开页面，如果没有 UUID 则生成一个存入 sessionStorage ，如果有则直接读取 sessionStorage 中保存的 UUID 。</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> uuid = sessionStorage.getItem(<span class="hljs-string">'uuid'</span>);
<span class="hljs-keyword">if</span> (!uuid) &#123;
  sessionStorage.setItem(<span class="hljs-string">'uuid'</span>,uuidv4());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-4">UUID 长期保存，清缓存后自动生成：</h6>
<h6 data-id="heading-5">这样我们可以将 uuid 存入 localStorage 中，可以长期保存：</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> uuid = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'uuid'</span>);
<span class="hljs-keyword">if</span> (!uuid) &#123;
  <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'uuid'</span>,uuidv4());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">增加登录验证，未登陆状态再生成 UUID：</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (getToken())&#123;<span class="hljs-comment">//判断是否有 token</span>
  sessionStorage.removeItem(<span class="hljs-string">'uuid'</span>); <span class="hljs-comment">//如果有，清除 sessionStorage 中的 uuid</span>
&#125; <span class="hljs-keyword">else</span> &#123;<span class="hljs-comment">//未登录状态生成 uuid</span>
  <span class="hljs-keyword">let</span> uuid = sessionStorage.getItem(<span class="hljs-string">'uuid'</span>);
  <span class="hljs-keyword">if</span> (!uuid) &#123;
    sessionStorage.setItem(<span class="hljs-string">'uuid'</span>,uuidv4());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">当然，也可以根据时间、设备信息、MD5和加盐（Salt）等方式生成更加精确的 UUID，大家可以根据自己的需求灵活运用。</h6></div>  
</div>
            