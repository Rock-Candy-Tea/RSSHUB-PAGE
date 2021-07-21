
---
title: '《HTTP 权威指南》笔记之Web的基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b48f6ff8f24618a283baa41838759d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 20:19:33 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b48f6ff8f24618a283baa41838759d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">HTTP 概述</h1>
<p>HTTP —— 因特网的多媒体信使，服务于客户端与服务器之间。</p>
<h2 data-id="heading-1">资源</h2>
<h3 data-id="heading-2">媒体类型</h3>
<p>Web 服务器会为所有 HTTP 对象数据附加一个 MIME 类型。当 Web 浏览器从服务器中取回一个对象时，会去查看相关的 MIME 类型，看看它是否知道 应该如何处理这个对象。</p>
<p>MIME 类型是一种文本标记，表示一种主要的对象类型和一个特定的子类型，中间 由一条斜杠来分隔。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b48f6ff8f24618a283baa41838759d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">URI</h3>
<p>服务器资源名被称为<code>统一资源标识符</code>（Uniform Resource Identifier，URI），URI 有两种形式，分别称为 <code>URL</code> 和 <code>URN</code>。</p>
<ul>
<li>URL：统一资源定位符（URL），描述一台特定服务器上某资源的特定位置。</li>
<li>URN：统一资源名（URN），作为特定内容的唯一名称使用 的，与目前的资源所在地无关。</li>
</ul>
<p>现在，几乎所有的 URI 都是 URL。</p>
<h2 data-id="heading-4">事务</h2>
<p>一个 HTTP 事务由一条（从客户端发往服务器的）请求命令和一个（从服务器 发回客户端的）响应结果组成。</p>
<h3 data-id="heading-5">HTTP 方法</h3>
<p>HTTP 支持几种不同的请求命令，这些命令被称为 HTTP 方法（HTTP method）。常见的有：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5959f1cbf04e49d4b300128da86a4320~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">状态码</h3>
<p>每条 HTTP 响应报文返回时都会携带一个状态码。常见的有：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc27fa7cbe64a559b7bfe7168ca3ea8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">报文</h2>
<p>HTTP 报文是由一行一行的简单字符串组成的。</p>
<ul>
<li>
<p>请求报文：从 Web 客户端发往 Web 服务器的 HTTP 报文称为请求报文（request message）。</p>
</li>
<li>
<p>响应报文：从服务器发往客户端的报文称为响应报文（response message），</p>
</li>
</ul>
<h2 data-id="heading-8">连接</h2>
<p>了解 HTTP 报文是如何通过传输控制协议 （Transmission Control Protocol，TCP）连接从一个地方搬移到另一个地方去的。</p>
<h3 data-id="heading-9">TCP/IP</h3>
<p>HTTP 是个应用层协议。HTTP 无需操心网络通信的具体细节；它把联网的细节都 交给了通用、可靠的因特网传输协议 TCP/IP。</p>
<p>TCP 提供了：</p>
<ul>
<li>无差错的数据传输；</li>
<li>按序传输（数据总是会按照发送的顺序到达）；</li>
<li>未分段的数据流（可以在任意时刻以任意尺寸将数据发送出去）。</li>
</ul>
<p>用网络术语来说，HTTP 协议位于 TCP 的上层。HTTP 使用 TCP 来传输其报文数 据。与之类似，TCP 则位于 IP 的上层</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/412ac288046e479ab53493703e595657~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">协议版本</h2>
<ul>
<li>HTTP/0.9</li>
</ul>
<p>HTTP/0.9 定义的初衷是为了获取 简单的 HTML 对象，它很快就被 HTTP/1.0 取代了。</p>
<ul>
<li>HTTP/1.0</li>
</ul>
<p>1.0 是第一个得到广泛使用的 HTTP 版本。添加了版本号、各种 HTTP 首部、一些额外的方法，以及对多媒体对象的处理。</p>
<ul>
<li>HTTP/1.0+</li>
</ul>
<p>非正式（非官方扩展）的 HTTP 扩展版本通常 称为 HTTP/1.0+。</p>
<ul>
<li>HTTP/1.1</li>
</ul>
<p>HTTP/1.1 重点关注的是校正 HTTP 设计中的结构性缺陷，明确语义，引入重要 的性能优化措施，并删除一些不好的特性。是当前 使用的 HTTP 版本。</p>
<ul>
<li>HTTP-NG（又名 HTTP/2.0）</li>
</ul>
<p>HTTP-NG 是 HTTP/1.1 后继结构的原型建议，它重点关注的是性能的大幅优化， 以及更强大的服务逻辑远程执行框架。</p>
<h2 data-id="heading-11">Web 的结构组件</h2>
<p>除了（Web 浏览器和 Web 服务器）这两个 Web 应用程序参与交互外，在因特网上，还有一些其他比较重要的应用程序。如下所示。</p>
<ul>
<li><strong>代理</strong>：位于客户端和服务器之间的 HTTP 中间实体。</li>
<li><strong>缓存</strong>：HTTP 的仓库，使常用页面的副本可以保存在离客户端更近的地方。</li>
<li><strong>网关</strong>：连接其他应用程序的特殊 Web 服务器。</li>
<li><strong>隧道</strong>：对 HTTP 通信报文进行盲转发的特殊代理。</li>
<li><strong>Agent</strong>：代理发起自动 HTTP 请求的半智能 Web 客户端，如：Web 浏览器，网络爬虫。</li>
</ul>
<h1 data-id="heading-12">URL与资源</h1>
<h2 data-id="heading-13">URL 语法</h2>
<p>大多数 URL 方案的 URL 语法都建立在这个由 9 部分构成的通用格式上：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">scheme</span>></span>://<span class="hljs-tag"><<span class="hljs-name">user</span>></span>:<span class="hljs-tag"><<span class="hljs-name">password</span>></span>@<span class="hljs-tag"><<span class="hljs-name">host</span>></span>:<span class="hljs-tag"><<span class="hljs-name">port</span>></span>/<span class="hljs-tag"><<span class="hljs-name">path</span>></span>;<span class="hljs-tag"><<span class="hljs-name">params</span>></span>?<span class="hljs-tag"><<span class="hljs-name">query</span>></span>#<span class="hljs-tag"><<span class="hljs-name">frag</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中最重要的是：方案（scheme）、 主机（host）和路径（path）。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566e90d2717f41dbaaf3dc9592f5df02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">常见的方案 scheme 描述</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/541b6e93bb594bcd83f94ffeddd66637~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-15">HTTP 报文</h1>
<h2 data-id="heading-16">报文流</h2>
<ul>
<li>报文流入源端服务器，工作完成之后，会流回用户的 Agent 代理中</li>
<li>不管是请求报文还是响应报文，所有报文都会向 下游（downstream）流动</li>
</ul>
<h2 data-id="heading-17">报文的组成三部分</h2>
<ul>
<li>对报文进行描述的起始行（start line）</li>
<li>包含属性的首部（header）块</li>
<li>包含数据的主体（body）部分</li>
</ul>
<h3 data-id="heading-18">报文的语法</h3>
<p>请求报文：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">method</span>></span> <span class="hljs-tag"><<span class="hljs-name">request-URL</span>></span> <span class="hljs-tag"><<span class="hljs-name">version</span>></span> // 起始行
<span class="hljs-tag"><<span class="hljs-name">headers</span>></span> // 首部
<span class="hljs-tag"><<span class="hljs-name">entity-body</span>></span> // 主体
<span class="copy-code-btn">复制代码</span></code></pre>
<p>响应报文：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">version</span>></span> <span class="hljs-tag"><<span class="hljs-name">status-code</span>></span> <span class="hljs-tag"><<span class="hljs-name">reason-phrase</span>></span> // 起始行 
<span class="hljs-tag"><<span class="hljs-name">headers</span>></span> // 首部
<span class="hljs-tag"><<span class="hljs-name">entity-body</span>></span> // 主体
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：请求报文和响应报文，只有<code>起始行</code>的语法有所不同</p>
<ul>
<li>请求：<请求方法><请求URL><HTTP版本></li>
<li>响应：<HTTP版本><状态码><原因短句></li>
</ul>
<p>假想的请求和响应报文
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f081f62354e43ceb35ad7eb56168724~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">方法</h2>
<h3 data-id="heading-20">GET</h3>
<p>GET 是最常用的方法。通常用于请求服务器发送某个资源。</p>
<h3 data-id="heading-21">HEAD</h3>
<p>HEAD 方法与 GET 方法的行为很类似，但服务器在响应中只返回首部。不会返回实体的主体部分。
使用 HEAD，可以：</p>
<ul>
<li>在不获取资源的情况下了解资源的情况（比如，判断其类型）；</li>
<li>通过查看响应中的状态码，看看某个对象是否存在；</li>
<li>通过查看首部，测试资源是否被修改了。</li>
</ul>
<h3 data-id="heading-22">PUT</h3>
<p>与 GET 从服务器读取文档相反，PUT 方法会向服务器写入文档。</p>
<h3 data-id="heading-23">POST</h3>
<p>POST 方法起初是用来向服务器输入数据的。实际上，通常会用它来支持 HTML 的表单。</p>
<h3 data-id="heading-24">TRACE</h3>
<p>客户端发起一个请求时，这个请求可能要穿过防火墙、代理、网关或其他一些应用程序。每个中间节点都可能会修改原始的 HTTP 请求。TRACE 方法允许客户端在最终将请求发送给服务器时，看看它变成了什么样子。</p>
<p>TRACE 请求会在目的服务器端发起一个“环回”诊断。行程最后一站的服务器会弹回一条 TRACE 响应，并在响应主体中携带它收到的原始请求报文。这样客户端就可以查看在所有中间 HTTP 应用程序组成的请求 / 响应链上，原始报文是否被毁坏或修改过。</p>
<h3 data-id="heading-25">OPTIONS</h3>
<p>OPTIONS 方法请求 Web 服务器告知其支持的各种功能。可以询问服务器通常支持 哪些方法，或者对某些特殊资源支持哪些方法。（有些服务器可能只支持对一些特殊 类型的对象使用特定的操作）</p>
<h3 data-id="heading-26">DELETE</h3>
<p>DELETE 方法所做的事情就是请服务器删除请求 URL 所指定的资源。 但是，客户端应用程序无法保证删除操作一定会被执行。因为 HTTP 规范允许服务 器在不通知客户端的情况下撤销请求。</p>
<h2 data-id="heading-27">状态码</h2>
<h3 data-id="heading-28">100～199——信息性状态码</h3>
<p>HTTP/1.1 向协议中引入了信息性状态码。这些状态码相对较新，关于其复杂性和感 知价值存在一些争论，而受到限制。</p>
<h3 data-id="heading-29">200～299——成功状态码</h3>
<p>客户端发起请求时，这些请求通常都是成功的。服务器有一组用来表示成功的状态 码，分别对应于不同类型的请求。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86fdf9ce0b4c4dbd9e55caacdb13a940~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30">300～399——重定向状态码</h3>
<p>重定向状态码要么告知客户端使用替代位置来访问他们所感兴趣的资源，要么就提供一个替代的响应而不是资源的内容。如果资源已被移动，可发送一个重定向状态码和一个可选的 Location 首部来告知客户端资源已被移走，以及现在可以在哪里找到它。这样，浏览器就可以在不打扰使用者的情况下，透明地转入新的位置了。</p>
<p>如：304 (Not Modified) 服务器告知客户端可以直接从本地缓存读取资源</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeb5ab57a30d42c696ef6cc4538f998c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a28b0bddbb34392893fe14b53510283~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>你可能已经注意到 302、303 和 307 状态码之间存在一些交叉。这些状 态码的用法有着细微的差别，大部分差别都源于 HTTP/1.0 和 HTTP/1.1 应用程序对 这些状态码处理方式的不同。</p>
</blockquote>
<h3 data-id="heading-31">400～499——客户端错误状态码</h3>
<p>有时客户端会发送一些服务器无法处理的东西，比如格式错误的请求报文，或者最常见的是，请求一个不存在的 URL。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adbdcf5fadd842b58a953e9a4876238b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a270905232b64f44809bcda6ac5986b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-32">500～599——服务器错误状态码</h3>
<p>有时客户端发送了一条有效请求，服务器自身却出错了。这可能是客户端碰上了服 务器的缺陷，或者服务器上的子元素，比如某个网关资源，出了错。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c71b5831563749119f001c27ef9983a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d4dff8321094ad3ad94ec9bf15e9043~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-33">首部</h2>
<p>首部和方法配合工作，共同决定了客户端和服务器能做什么事情。可以将首部分为五个主要的类型：</p>
<h3 data-id="heading-34">通用首部</h3>
<p>是客户端和服务器都可以使用的通用首部。</p>
<ul>
<li>通用的信息性首部</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da9b1642aec240b8b063502431ac225c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通用的缓存首部</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/824e84570c6a4a14b570e411203e3044~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：从技术角度来看，Pragma 是一种请求首部。从未被指定用于响应首部。由于经常被错误地用于响应首部，很多客户端和代理都会将 Pragma 解释为响应首部，但其确切语义并未得到很好地定义。任何情况下 Cache-Control 的使用都优于 Pragma。</p>
</blockquote>
<h3 data-id="heading-35">请求首部</h3>
<p>就是请求报文特有的。</p>
<ul>
<li>请求的信息性首部</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6861d2e557346709d3b3c126ccf10cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>请求的 Accept 首部</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b66b43109b204f5d8db78fc019042919~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>条件请求首部</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94ff0651f0434e38b4abb36e61c30e1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安全请求首部</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42d460e94a534f7eaeb27a49048fd91d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>代理请求首部</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c9740b262f449e69ab88b62f60b2d28~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-36">响应首部</h3>
<p>响应报文有自己的首部集，以便为客户端提供信息</p>
<ul>
<li>响应的信息性首部</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb9be73f2d8d4146a623e30c54fe5a34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>协商响应首部</li>
</ul>
<p>HTTP/1.1 可以为服务器和客户端提供对资源进行协商的能力。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1bedf1b82194e118902af954145c873~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安全响应首部</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eeee1d290444ab88fd279dafc269dac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-37">实体首部</h3>
<p>实体首部提供了有关实体及其内容的大量信息，从有关对象类型的信息，到能够对资源使用的各种有效的请求方法。</p>
<ul>
<li>实体的信息性首部</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960a077072f84bcf9114fe702dc26340~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>内容实体首部</li>
</ul>
<p>内容首部提供了与实体内容有关的特定信息，说明了其类型、尺寸以及处理它所需 的其他有用信息。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/273b77eaa92147f098e7a86c474b7712~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>实体缓存首部</li>
</ul>
<p>通用的缓存首部说明了如何或什么时候进行缓存。实体的缓存首部提供了与被缓存实体有关的信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38c85a4544fc4feba0c2a7b402d48400~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-38">扩展首部</h3>
<p>扩展首部是非标准的首部，由应用程序开发者创建，但还未添加到已批准的 HTTP 规范中去。</p></div>  
</div>
            