
---
title: '浏览器安全之网络安全（HTTPS）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f06069fb32b4746be5044ec3cdbea2a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:51:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f06069fb32b4746be5044ec3cdbea2a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 4 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">为什么要使用 HTTPS 协议</h1>
<p>在将 HTTP 数据提交给 TCP 层之后，数据会经过用户电脑、WiFi 路由器、运营商和目标服务器，在这中间的每个环节中，数据都有可能被窃取或篡改。比如用户电脑被黑客安装了恶意软件，那么恶意软件就能抓取和篡改所发出的 HTTP 请求的内容。或者用户一不小心连接上了 WiFi 钓鱼路由器，那么数据也都能被黑客抓取或篡改。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f06069fb32b4746be5044ec3cdbea2a~tplv-k3u1fbpfcp-watermark.image" alt="中间人" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">什么是 HTTPS 协议</h1>
<p>实际上就是在 HTTP 协议栈中引入安全层，所有经过安全层的数据都会被加密或者解密
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c53376d4dd340a39c2b367e43a0255f~tplv-k3u1fbpfcp-watermark.image" alt="HTTP VS HTTPS" loading="lazy" referrerpolicy="no-referrer">
安全层有两个主要的职责：</p>
<ol>
<li>对发起 HTTP 请求的数据进行加密操作。</li>
<li>对接收到 HTTP 的内容进行解密操作。</li>
</ol>
<p>下面一步步实现一个从简单到复杂的 HTTPS 协议</p>
<h1 data-id="heading-2">第一版：使用对称加密</h1>
<p>对称加密是指加密和解密都使用的是相同的密钥。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bb5ff1edb6d4638bc827864bb137523~tplv-k3u1fbpfcp-watermark.image" alt="使用对称加密" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>浏览器端弄个随机数(<code>client-random</code>),并发送它所支持的加密套件列表(指浏览器能支持多少种加密方法列表)。</li>
<li>服务器从发过来的加密套件列表里选择一个，并也整个随机数(<code>service_random</code>),并返回给浏览器</li>
<li>浏览器跟服务器分别返回确认信息。</li>
</ol>
<p>按加密套件算法，将 <code>client-random</code> 和 <code>service-random</code> 混合起来生成一个密钥 <code>master secret</code>，然后基于这个密钥进行数据的加密传输。</p>
<p><strong>缺点：</strong>
由于 <code>client-random</code> 与 <code>service-random</code> 都是明文传输，所以会被截获。
黑客拿到协商的加密套件和双方的随机数，生成密钥。</p>
<h1 data-id="heading-3">第二版：使用非对称加密</h1>
<p>非对称加密算法有 A、B 两把密钥，如果你用 A 密钥来加密，那么只能使用 B 密钥来解密；反过来，如果你要 B 密钥来加密，那么只能用 A 密钥来解密。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aca128061f834380823660f8d0f1312a~tplv-k3u1fbpfcp-watermark.image" alt="非对称加密" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>浏览器发送它所支持的加密套件列表。</li>
<li>服务器会生成个公钥跟私钥，公钥是给浏览器加密使用的，所以将公钥跟选择的加密套件返回</li>
<li>浏览器跟服务器分别返回确认信息。</li>
</ol>
<p>这样浏览器向服务端发送数据时，就可以采用公钥来加密数据，由于公钥的数据只有对应的私钥才能解密，即便黑客截取了数据和公钥，也是无法解密的。
<strong>缺点：</strong></p>
<ol>
<li>非对称加密的效率太低</li>
<li>无法保证服务器发送给浏览器的数据安全，因为服务端是采用私钥加密的，而黑客是可以拦截到公钥，这样服务端返回的数据就得不到保障。</li>
</ol>
<h1 data-id="heading-4">第三版：对称加密和非对称加密搭配使用</h1>
<p>在传输数据阶段依然使用对称加密，但是对称加密的密钥我们采用非对称加密来传输。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3705189be7444a8aa711d72bc02c498c~tplv-k3u1fbpfcp-watermark.image" alt="混合加密实现 HTTPS" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>浏览器端弄个随机数(<code>client-random</code>),并发送它所支持的加密套件列表和非对称加密套件列表。</li>
<li>服务器会生成个公钥和私钥，并弄个随机数(<code>service-random</code>),返回该随机数、公钥、选择的加密套件、非对称加密套件</li>
<li>浏览器再生成个随机数 <code>pre-master</code> ，并采用公钥加密，进行浏览器确认</li>
<li>最后服务器拿出自己的私钥，解密出 <code>pre-master</code> 数据，并返回确认消息。</li>
</ol>
<p>这样浏览器跟服务器就有了一致 <code>client-random</code> ， <code>service-random</code>，<code>pre-master</code>，根据这些生成对称密钥，由于两端采用的是一套对称加密套件，所以生成的密钥是一致的。
<code>pre-master</code> 是经过公钥加密之后传输的，所以黑客无法获取到 <code>pre-master</code>，这样黑客就无法生成密钥，也就保证了黑客无法破解传输过程中的数据了。
<strong>缺点：</strong>
黑客通过 <code>DNS</code> 劫持将你所在官网的 IP 地址替换成了黑客的 IP 地址。
即无法证明服务器是可靠的。</p>
<h1 data-id="heading-5">第四版：添加数字证书</h1>
<p>需要服务器向浏览器提供证明“我就是我”：
使用权威机构颁发的证书，这个权威机构称为 CA（Certificate Authority），颁发的证书就称为数字证书（Digital Certificate)。
对于浏览器来说，数字证书作用：</p>
<ol>
<li>一个是通过数字证书向浏览器证明服务器的身份</li>
<li>另一个是数字证书里面包含了服务器公钥。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/796c3871a6df4132a0c297cfc85ba180~tplv-k3u1fbpfcp-watermark.image" alt="完整的 HTTPS 请求流程" loading="lazy" referrerpolicy="no-referrer">
<strong>两点改造：</strong></p>
<ol>
<li>服务器没有直接返回公钥给浏览器，而是返回了数字证书，而公钥包含在数字证书中；</li>
<li>在浏览器端多了一个证书验证的操作，验证了证书之后，才继续后续流程。</li>
</ol>
<h1 data-id="heading-6">HTTPS 的握手过程</h1>
<ol>
<li>首先是 <code>tcp</code> 的三次握手建立连接</li>
<li><code>client</code> 发送 <code>random1</code> +支持的加密算法集合（<code>clientHello</code>）</li>
<li><code>server</code> 收到信息，返回选择一个加密算法 + <code>random2</code>（<code>serverHello</code>）+ 证书+ 确认</li>
<li><code>clent</code> 验证证书有效性，并生成随机数 <code>pre-master</code> ，并通过服务器公钥加密 发送给 <code>server</code></li>
<li><code>server</code> 收到 <code>premaster</code> ，根据约定的加密算法对 <code>random1</code> + <code>random2</code> + <code>premaster</code>（解密）生成 <code>master-secret</code> ，然后发送预定成功</li>
<li><code>client</code> 收到生成同样的 <code>master-secert</code>，对称加密秘钥传输完毕</li>
</ol></div>  
</div>
            