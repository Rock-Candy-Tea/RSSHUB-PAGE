
---
title: '总结向：HTTP 协议'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78480ea6476b4aa492f841f99a2fe143~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 07:03:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78480ea6476b4aa492f841f99a2fe143~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>这是我参与更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>如果❤️我的文章有帮助，欢迎点赞、关注。这是对我继续技术创作最大的鼓励。[更多系列文章在我博客] <a href="https://coderdao.github.io/" target="_blank" rel="nofollow noopener noreferrer">coderdao.github.io/</a></p>
</blockquote>
<h1 data-id="heading-0">总结向：HTTP 协议</h1>
<p>如果想要入行互联网技术岗，那么 <code>HTTP</code> 几乎是天天要打交道的东西，但我发现大部分人对 HTTP 只是浅尝辄止，对更多的细节及原理就了解不深了，在面试的时候感觉非常吃力。</p>
<p>这篇文章就是为了帮助大家树立完整的 HTTP 知识体系，并达到一定的深度，从容地应对各种开发、面试问题。</p>
<h1 data-id="heading-1">GET/POST 区别？</h1>
<ul>
<li>从 <code>缓存</code> 的角度，GET 请求会被浏览器主动缓存下来，留下历史记录，而 POST 默认不会。</li>
<li>从 <code>编码</code> 的角度，GET 只能进行 URL 编码，只能接收 ASCII 字符，而 POST 没有限制。</li>
<li>从 <code>参数</code> 的角度，GET 一般放在 URL 中，因此不安全，POST 放在请求体中，更适合传输敏感信息。</li>
<li>从 <code>幂等性</code> 的角度，<code>GET</code>是 <code>幂等</code> 的，而<code>POST</code>不是。(<code>幂等</code>使用同样的条件，一次请求和重复请求对同一系统的资源影响是一致)</li>
<li>从 <code>TCP</code> 的角度，GET 请求会把请求报文一次性发出去，而 POST 会分为两个 TCP 数据包，首先发 header 部分，如果服务器响应 100(continue)， 然后发 body 部分。(<strong>火狐</strong>浏览器除外，它的 POST 请求只发一个 TCP 包)</li>
</ul>
<p>除 GET、POST 意外，<code>http/1.1</code> 规定了以下请求方法:</p>
<ul>
<li>GET: 通常用来获取资源</li>
<li>HEAD: 获取资源的元信息</li>
<li>POST: 提交数据，即上传数据</li>
<li>PUT: 修改数据</li>
<li>DELETE: 删除资源(几乎用不到)</li>
<li>CONNECT: 建立连接隧道，用于代理服务器</li>
<li>OPTIONS: 列出可对资源实行的请求方法，用来跨域请求</li>
<li>TRACE: 追踪请求-响应的传输路径</li>
</ul>
<h1 data-id="heading-2">HTTP 1.0、1.1、2.0 区别</h1>
<h2 data-id="heading-3">HTTP 1.0：</h2>
<p>总结：</p>
<ul>
<li>无连接</li>
<li>无状态</li>
</ul>
<p>最早在1996年在网页中使用，内容简单。
浏览器的每次请求都需要与服务器建立一个TCP连接，服务器处理完成后立即断开TCP连接（无连接），服务器不跟踪每个客户端也不记录过去的请求（无状态）。</p>
<h2 data-id="heading-4">HTTP 1.1：</h2>
<p>总结：</p>
<ul>
<li>默认持久连接</li>
<li>请求管道化</li>
<li>增加缓存处理（新的字段如cache-control）</li>
<li>增加Host字段、支持断点传输等（把文件分成几部分）</li>
</ul>
<p>1999年广泛被应用，HTTP/1.0中默认使用Connection: close。在HTTP/1.1中已经 默认使用Connection: keep-alive（长连接），避免了连接建立和释放的开销。
但服务器须按照客户端请求顺序依次响应结果 ，以保证客户端区分出每次请求的响应内容。通过Content-Length字段来判断当前请求数据是否已经全部接收。不允许同时多个并行响应。</p>
<h2 data-id="heading-5">HTTP 2.0：</h2>
<p>总结：</p>
<ul>
<li>二进制分帧并行传输</li>
<li>多路复用</li>
<li>头部压缩</li>
<li>服务器推送</li>
</ul>
<p>HTTP/2引入二进制数据帧和流的概念，其中帧对数据进行顺序标识，如下所示，</p>
<ul>
<li>流（stream）—— 已建立连接上的双向字节流</li>
<li>消息 —— 与逻辑消息对应的完整的一系列数据帧</li>
<li>帧 —— HTTP2.0通信的最小单位，每个帧包含帧头部，至少也会标识出当前帧所属的流（stream id）。</li>
</ul>
<p>每个请求是一个数据<code>流</code>，数据流以<code>消息</code>的方式发送，而消息又分为多个<code>帧</code>，帧头部记录着<code>stream id</code>用来标识所属的数据流，不同属的帧可以在连接中随机混杂在一起。接收方可以根据stream id将帧再归属到各自不同的请求当中去。</p>
<h3 data-id="heading-6">多路复用：</h3>
<p>1、所有的HTTP2.0通信都在一个TCP连接上完成，这个连接可以承载任意数量的双向数据流。</p>
<p>2、每个数据流以消息的形式发送，而消息由一或多个帧组成。这些帧可以乱序发送，然后再根据每个帧头部的流标识符（stream id）重新组装。</p>
<p>举个例子，每个请求是一个数据流，数据流以消息的方式发送，而消息又分为多个帧，帧头部记录着stream id用来标识所属的数据流，不同属的帧可以在连接中随机混杂在一起。接收方可以根据stream id将帧再归属到各自不同的请求当中去。</p>
<p>3、另外，多路复用（连接共享）可能会导致关键请求被阻塞。HTTP2.0里每个数据流都可以设置优先级和依赖，优先级高的数据流会被服务器优先处理和返回给客户端，数据流还可以依赖其他的子数据流。</p>
<p>4、可见，HTTP2.0实现了真正的并行传输，它能够在一个TCP上进行任意数量HTTP请求。而这个强大的功能则是基于“二进制分帧”的特性。</p>
<h3 data-id="heading-7">头部压缩</h3>
<p>在HTTP1.x中，头部元数据都是以纯文本的形式发送的，通常会给每个请求增加500~800字节的负荷。</p>
<p>HTTP2.0使用encoder来减少需要传输的header大小，通讯双方各自cache一份header fields表，既避免了重复header的传输，又减小了需要传输的大小。高效的压缩算法可以很大的压缩header，减少发送包的数量从而降低延迟。</p>
<h3 data-id="heading-8">服务器推送：</h3>
<p>服务器除了对最初请求的响应外，服务器还可以额外的向客户端推送资源，而无需客户端明确的请求。</p>
<h1 data-id="heading-9">HTTP 和 HTTPS 的区别</h1>
<h2 data-id="heading-10">HTTPS 简介</h2>
<p>HTTPS 实际为了解决 <code>HTTP为明文发送内容，不利于敏感数据</code>, 而在 HTTP 基础上加入了SSL协议，SSL依靠证书来验证服务器的身份，并为浏览器和服务器之间的通信加密。</p>
<p>HTTPS协议的主要作用可以分为两种：</p>
<ul>
<li>一种提供<code>信息安全通道</code>，保证数据安全传输；</li>
<li>一种确认网站<code>真实性</code>。</li>
</ul>
<h2 data-id="heading-11">区别</h2>
<ul>
<li>https相对于http加入了ssl层，需要到ca申请证书（收费的），</li>
<li>https相对于http身份认证（认知用户、服务器），数据加密。防止数据被窃取、改变。</li>
<li>现行架构下最安全但是耗时多，缓存不是很好，</li>
<li>https使用 443 端口；http使用 80 端口。注意兼容http和https</li>
</ul>
<h2 data-id="heading-12">HTTPS 传输过程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78480ea6476b4aa492f841f99a2fe143~tplv-k3u1fbpfcp-zoom-1.image" alt="图片描述" loading="lazy" referrerpolicy="no-referrer">
前置条件：
服务端 生成 TSL/SSL 公钥、私钥。把公钥给 CA 签发带有公钥的证书。</p>
<ol>
<li>Client发起一个HTTPS请求，根据RFC2818的规定，Client知道需要连接Server的443（默认）端口。</li>
<li>Server有事先配置好的密钥对（公钥、私钥），这里把公钥证书（public key certificate）返回给客户端。</li>
<li>Client验证公钥证书：比如是否在有效期内，证书的用途是不是匹配Client请求的站点，是不是在CRL吊销列表里面，它的上一级证书是否有效，这是一个递归的过程，直到验证到根证书（操作系统内置的Root证书或者Client内置的Root证书）。如果验证通过则继续，不通过则显示警告信息。</li>
<li>Client使用伪随机数生成器生成加密所使用的会话密钥，然后用证书的公钥加密这个会话密钥，发给Server。</li>
<li>Server使用自己的私钥（private key）解密这个消息，得到会话密钥。至此，Client和Server双方都持有了相同的会话密钥。</li>
<li>Server使用会话密钥加密“明文内容A”，发送给Client。</li>
<li>Client使用会话密钥解密响应的密文，得到“明文内容A”。</li>
<li>Client再次发起HTTPS的请求，使用会话密钥加密请求的“明文内容B”，然后Server使用会话密钥解密密文，得到“明文内容B”。</li>
</ol>
<h1 data-id="heading-13">输入 URL 到页面渲染的过程</h1>
<p>总体分 6 步：</p>
<ul>
<li>输入网址</li>
<li>DNS域名解析</li>
<li>建立TCP连接</li>
<li>发送HTTP请求，服务器处理请求，返回响应结果</li>
<li>关闭TCP连接</li>
<li>浏览器渲染</li>
</ul>
<p>细致问每一步具体做了什么？又有以下答案：</p>
<h2 data-id="heading-14">DNS域名解析</h2>
<p>本质：把域名 <code>juejin.cn</code> 转换成具体 <code>IP地址</code></p>
<p>应用场景：当爬虫请求数据为空时，可以 <code>ping</code> 一下请求域名。是否能成功。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ec1d64a3a49447cbfc156197be1f249~tplv-k3u1fbpfcp-zoom-1.image" alt="图片描述" loading="lazy" referrerpolicy="no-referrer">
<code>www.baidu.com</code> 是成功例子；<code>www.juejin.cn</code> 可能是 <code>禁止ping</code>/ 绑hosts / 网站挂了 等几种情况。这个可以结合 <code>curl</code> / <code>浏览器访问</code>... 等更多方法结合判断</p>
<p>DNS的解析过程，是在<code>浏览器</code>、<code>本地DNS</code> 之间 <code>递归查询</code>；找不到就继续在 <code>本地DNS</code> 与 <code>根域服务器</code>、<code>顶级域名服务器</code>、<code>权威域名服务器</code>之间 <code>迭代查询</code>；</p>
<h2 data-id="heading-15">发送HTTP请求，服务器处理请求，返回响应结果</h2>
<p>TCP连接建立后，浏览器就可以利用HTTP／HTTPS协议向服务器发送请求了。
服务器接受到请求，就解析请求头，如果头部有缓存相关信息如if-none-match与if-modified-since，则验证缓存是否有效返回状态码为304，</p>
<p>如果是301/302表示服务器已更换域名需要重定向，这时网络进程会从响应头的Location字段里面读取重定向的地址，然后再发起新的HTTP或者HTTPS请求，跳回第4步。
如果是200，就检查Content-Type字段，值为text/html说明是HTML文档，是application/octet-stream说明是文件下载；</p></div>  
</div>
            