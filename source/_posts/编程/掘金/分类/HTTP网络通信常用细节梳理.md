
---
title: 'HTTP网络通信常用细节梳理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9037'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 00:17:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=9037'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">HTTP1.1长链接</h4>
<p>HTTP协议的初始版本中，每进行一次HTTP通信就要断开一次TCP链接，也就是短连接。</p>
<p>以早期的通信情况来说，因为都是些容量很小的文本传输，所以即使这样也没有多大问题，但是随着HTTP的大量普及，文旦中包含大量富文本的情况多了起来。每次的请求都会造成无谓的TCP链接建立和断开，增加通信录的开销。</p>
<p>为了解决这个问题，有些浏览器在请求时，用了一个非标准的Connection字段。这个字段要求服务器不要关闭TCP链接，以便其他请求复用，服务器同样回应这个字段。</p>
<pre><code class="hljs language-s copyable" lang="s">Connection: keep-alive
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个可以复用的TCP链接就建立了，直到客户端或服务器主动关闭链接，但是这并非标准字段，不同实现的行为可能不一致，还可能造成混乱。</p>
<ul>
<li>长链接</li>
</ul>
<p>HTTP1.1版本在1997年1月发布，最大的变化就是引入了持久链接，即TCP链接默认不关闭，可以被多个请求复用，不需要再声明Connection: keep-alive。</p>
<p>持久连接减少了TCP链接的重复建立和断开所造成的的额外开销，减轻了服务器端的负载。减少开销的时间让HTTP请求和响应能够更早的结束，这样Web页面的速度也就响应变快了。</p>
<p>客户端和服务器发现对方一段时间没有活动，就可以主动关闭链接，不过规范的做法是客户端在最后一个请求时发送Connection: close，明确要求服务器关闭链接。目前对于同一个域名，大多数浏览器允许同时建立6个持久链接。</p>
<ul>
<li>管道机制</li>
</ul>
<p>同一个TCP链接里面客户端可以同时发送多个请求，这样就进一步改变了HTTP协议的效率。</p>
<p>从前发送请求后需等待及接收响应，才能发送下一个请求，管道化技术出现后不用等待响应即可直接发送下一个请求，这样就能够做到同时并行发送多个请求，而不需要一个接一个的等待响应了。</p>
<p>管道化技术比持久化链接还要快，请求数越多时间差越明显。</p>
<p>一个TCP链接可以传送多个回应，势必就要有一种机制，区分数据包是属于哪一个回应的，这就是Content-length字段的作用，声明本次回应的数据长度。</p>
<pre><code class="hljs language-s copyable" lang="s">Content-Length: 3000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码告诉浏览器，本次回应的长度是3000个字节，后面的字节就属于下一个回应了。在1.0版本中，Content-Length字段不是必须的，因为浏览器发现服务器关闭了TCP链接，就表明收到的数据包已经完成了。</p>
<ul>
<li>分块传输</li>
</ul>
<p>使用Content-Length字段的前提条件是，服务器发送回应之前，必须知道回应的数据长度。对于一些耗时的动态操作来说，意味着，服务器要等到所有操作完成，才能发送数据，显然这样的效率不高，更好的方法是产生一块数据就发送一块，采用流模式取代缓存模式。</p>
<p>因此1，1规定可以不使用content-length字段，而是用分块传输编码，只要请求或响应头信息有Transfer-Encoding字段，就表明响应将又数量未定的数据块组成。</p>
<pre><code class="hljs language-s copyable" lang="s">Transfer-Encoding: chunked
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个非空数据块之前会有一个16进制的数值，表示这个块的的长度，最后是一个大小为0的块，表示本次回应的数据发送完了。</p>
<pre><code class="hljs language-s copyable" lang="s">HTTP/1.1 200 OK
...
25
This is the data in the first chunk
...
2
...
4
...
0
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然HTTP1.1允许复用TCP链接，但是同一个TCP链接里面，所有的数据通信是按次序进行的，服务器只有处理完一个回应才会进行下一个回应。如果前面的请求慢，后面就会有需要请求排队，称为对头阻塞。为了避免这种问题，可以减少请求数或者同事多开持续请求。这就出现了很多的优化技巧，比如说。合并脚本和样式表，将图片嵌入css代码，域名分片等等。其实如果HTTP协议设计的更好一些，这些额外的工作都是可以避免的。</p>
<h4 data-id="heading-1">HTTP2协议</h4>
<p>为了解决响应阻塞问题2015年推出了HTTP2。</p>
<p>HTTP2主要用于解决HTTP1.1效率不高的问题，他不叫HTTP2.0是因为不打算发布子版本了，下一个版本直接就叫HTTP3。</p>
<ul>
<li>二进制协议</li>
</ul>
<p>HTTP1.1头信息肯定是文本，数据体可以是文本也可以是二进制，HTTP2则是一个彻底的二进制协议，头信息和数据体都是二进制，并且统称为帧，头信息帧和数据帧。</p>
<p>二进制协议的一个好处是可以定义额外的帧，HTTP2定了一近十种帧，为将来的高级应用打好基础，如果使用文本实现这种功能，解析数据将会变得非常麻烦，二进制解析则方便很多。</p>
<ul>
<li>多工</li>
</ul>
<p>HTTP2复用TCP链接，在一个链接里，客户端和浏览器都可以同时发送多个请求或回应，而且不用按照顺序一一对应，这样就避免了堵塞。</p>
<p>在一个TCP链接里面，服务器同时收到了A请求和B请求，先回应了A请求结果发现处理过程非常耗时，先发送A请求已经处理好的部分，再回应B请求，完成后再发送A请求剩余的部分。这种双向的，实时通信就叫做多工。</p>
<p>效果地址: https:http2.akamai.com/demo</p>
<ul>
<li>数据流</li>
</ul>
<p>因为HTTP2的数据包是不按顺序发送的，同一个链接里面连续的数据包，可能属于不同的回应，因此必须要对数据包做标记，指出他属于哪个回应。</p>
<p>HTTP2将每个请求或回应的所有数据包，称为一个数据流，每个数据流都有一个独一无二的编号，数据包发送的时候，都必须标记数据流ID，用来区分它属于哪个数据流，另外还规定，客户端发出的数据流，ID一律为奇数，服务器发布的，ID为偶数。</p>
<p>数据流发送到一半的时候，客户端和服务器都可以发送信号取消这个数据流。1.1版本取消数据的唯一方法就是关闭TCP链接，HTTP2可以取消某一次请求，同时保证TCP链接还开着，可以被其他请求使用。</p>
<p>客户端还可以指定数据流的优先级，优先级越高，服务器就会越早回应。</p>
<ul>
<li>压缩头信息</li>
</ul>
<p>HTTP协议不带有状态，每次请求都必须附上所有信息，所以请求的很多字段都是重复的，比如Cookie和User Agent，一模一样的内容每次请求都必须附带，这会浪费很多带宽也影响速度。</p>
<p>HTTP2对这一点做了优化，引入了头信息压缩机制，一方面头信息使用gzip或compress压缩后再发送，另一方面，客户端和服务器同时维护一张头信息表，所有字段都会存入这个表，生成一个索引号，以后就不发送这个字段只发送索引号这样就提高速度了。</p>
<ul>
<li>服务器推送</li>
</ul>
<p>HTTP2允许服务器未经过请求主动向客户端发送资源，这就叫服务器推送。</p>
<p>常见场景是客户端请求一个网页，这个网页包含很多静态资源，正常情况下，客户端必须收到网页后解析HTML编码，发现有静态资源再发出静态资源请求，其实服务器可以预期到客户端请求网页后很可能会再请求静态资源，所有就主动把这些静态资源随着网页一起发给客户端了。</p>
<p>这个功能还是建议考虑自身的需要，会增加一部分成本开销。</p>
<h4 data-id="heading-2">压缩传输数据资源</h4>
<p>通过压缩传输数据资源提升性能体验。默认HTTP进行数据传输数据是没有进行压缩的，原始数据多大传输的数据就多大。</p>
<p>我们都知道文件压缩之后数据体积减少是很客观的。</p>
<ul>
<li>响应数据压缩</li>
</ul>
<p>HTTP响应数据一般会根据数据的类型进行压缩方案的处理，比如文本最常用的方案就是Gzip的压缩方案，目前大部分的网站都采用这种压缩方式。</p>
<ol>
<li>gzip</li>
</ol>
<p>浏览器再请求服务器的时候会在请求头中通过Accept-Encoding字段标识可以接收gzip压缩方案，服务器在收到请求后可以获取到这种压缩方案，将资源压缩后返回给浏览器，并且在响应头中加入Content-Encoding字段，值为gzip。</p>
<p>如果客户端不添加Accept-Encoding头，服务器返回了Content-Encoding，客户端如果支持的话也会正常解析。Accept-Encoding基本是浏览器自动添加的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> zlib = <span class="hljs-built_in">require</span>(<span class="hljs-string">'zlib'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> rs = fs.cerateReadStream(<span class="hljs-string">'jquery.js'</span>);
<span class="hljs-keyword">const</span> ws = fs.cerateWriteStream(<span class="hljs-string">'jquery.js.gz'</span>);
<span class="hljs-keyword">const</span> gz = zlib.createGzip();
rs.pipe(gz).pipe(ws);
ws.on(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'失败'</span>);
&#125;)
ws.on(<span class="hljs-string">'finish'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'完成'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常工作中gzip一般可以在nginx服务器中开启，不需要自己编写。还是比较简单的。</p>
<p>gzip一般是针对文本文件，比如js，css，对于图片来说一般是在开发阶段压缩。</p>
<ul>
<li>请求数据压缩</li>
</ul>
<p>HTTP2以前请求头是不可以压缩的，HTTP2引入了头信息压缩机制，一方面头信息使用gzip或express压缩后再发送，另一方面，客户端和服务器同时维护一张头信息表，通过索引字段来传输，减少厅信息数据体积。</p>
<p>实际工作中会存在请求正文非常大的场景，比如发表长篇博客，上报用于调试网络数据等等，这些数据如果能在本地压缩后再提交就可以节省网络流量，减少传输时间。</p>
<p>DFLATE是一种使用Lempel-Ziv压缩算法的哈夫曼编码压缩格式。</p>
<p>ZLIB是一种使用DEFLATE的压缩格式。</p>
<p>GZIP是一种使用DEFLATE的压缩格式。</p>
<p>Content-Encoding中的deflate实际上是ZLIB。</p>
<p>前端发送的时候可以进行压缩：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rawBody = <span class="hljs-string">'content=test'</span>;
<span class="hljs-keyword">const</span> rawLen = rawBody.length;

<span class="hljs-keyword">const</span> bufBody = <span class="hljs-keyword">new</span> Unit8Array(rawLen);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < rawLen; i++) &#123;
    bufBody[i] = rawBody.charCodeAt(i);
&#125;

<span class="hljs-keyword">const</span> format = <span class="hljs-string">'gzip'</span>;

<span class="hljs-keyword">let</span> buf;

<span class="hljs-keyword">switch</span> (format) &#123;
    <span class="hljs-keyword">case</span> gzip<span class="hljs-string">': buf = window.pako.gzip(bufBody); break;
&#125;

const xhr = new XMLHttpRequest();
xhr.open('</span>POST<span class="hljs-string">', '</span>/service/<span class="hljs-string">');

xhr.setRequestHeader('</span>Content-Encoding<span class="hljs-string">', format);
xhr.setRequestHeader('</span>Content-type<span class="hljs-string">', '</span>application/x-www-form-urlencoded<span class="hljs-string">')

xhr.send(buf);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>服务器端进行解压</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> zlib = <span class="hljs-built_in">require</span>(<span class="hljs-string">'zlib'</span>);

http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> zlibStream;
    <span class="hljs-keyword">const</span> encoding = req.headers[<span class="hljs-string">'content-encoding'</span>]

    <span class="hljs-keyword">switch</span> (encoding) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'gzip'</span> : zlibStream = zlib.createGunzip(); <span class="hljs-keyword">break</span>;
    &#125;

    res.writeHead(<span class="hljs-number">200</span>, &#123; <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'text/plain'</span> &#125;);
    req.pipe(zlibStream).pipe(res);
&#125;).listen(<span class="hljs-number">3000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种压缩一半也只适用于文本，如果数据量太大压缩过程也是比较耗时的。</p></div>  
</div>
            