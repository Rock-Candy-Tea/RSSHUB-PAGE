
---
title: '浅析从URL输入到页面展现到底发生什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8fd5dda8c7345ac8d1a44314dc452e4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 20:18:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8fd5dda8c7345ac8d1a44314dc452e4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>由于上次面试，没有准备这题，就很尴尬的浅层次回答，使得面试更加的焦灼起来。</p>
<p>所以我先借这次的机会，认真的看看和理解这道题。</p>
<p>我看了很多的文章，得出一些心得，URL的输入到浏览器解析大概经历了以下几个过程。</p>
<blockquote>
<p>URL解析</p>
<p>DNS查询</p>
<p>TCP/IP连接</p>
<p>HTTP请求</p>
<p>响应请求</p>
<p>页面渲染</p>
<p>TCP断开链接</p>
</blockquote>
<h1 data-id="heading-0">URL解析</h1>
<p>首先我们要了解的预备知识</p>
<p>URL是统一资源定位符，用来表示是某个资源的地址</p>
<p><strong>URL的组成</strong></p>
<p>URL 主要由 <code>协议</code>、<code>主机</code>、<code>端口</code>、<code>路径</code>、<code>查询参数</code>、<code>锚点</code>6部分组成！</p>
<pre><code class="copyable">http://www.example.com:80/path/index.html?key1=value1&key2=value2#SomewhereInTheDocument
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>http</code> 是协议。它表明了浏览器必须使用何种协议，常用的协议是http，https。</li>
<li><code>www.example.com</code> 是域名，也可以是IP地址。</li>
<li><code>:80</code> 是端口。 同一个域名下面可能同时包含多个网站，它们之间通过端口（port）区分。http协议默认端口是：80端口，如果不写默认就是:80端口，https为443。</li>
<li><code>/path/index.html</code> 是网络服务器上资源的路径网络资源在服务器中的指定路径,例如上边的例子就是指向网站的<code>/path</code>子目录下面的网页文件<code>index.html</code>。</li>
<li><code>?key1=value1&key2=value2</code> 是提供给网络服务器的额外信息。如果要向服务器传入参数，在这部分输入。</li>
<li><code>#SomewhereInTheDocument</code> 是资源本身的另一部分的锚点.浏览器加载页面以后，会自动滚动到锚点所在的位置。锚点名称通过网页元素的<code>id</code>属性命名。</li>
</ul>
<h2 data-id="heading-1">如何解析</h2>
<p>在地址栏输入URL后，浏览器会对UR解析，抽取出域名字段，例如我们输入<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.com" target="_blank" title="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.com">www.baidu.com</a>。就会解析出<code>www.baidu.com</code>这个域名。</p>
<p>然后接下来就是DNS解析</p>
<h1 data-id="heading-2">DNS解析</h1>
<p>可以这样理解域名解析。将域名解析为IP地址，浏览器会发送一个UDP的包给DNS域名解析服务器。</p>
<p>DNS查询的工作方式：</p>
<p>客户端和浏览器，本地DNS之间的查询方式是<strong>递归查询</strong>；</p>
<p>本地DNS服务器与根域及其子域之间的查询方式是<strong>迭代查询</strong>；</p>
<p>我们先看一张图，看下整个解析过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8fd5dda8c7345ac8d1a44314dc452e4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708094216621" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">递归查询</h2>
<p>我们的浏览器、操作系统、路由器都会缓存一些URL对应的IP地址，统称为DNS高速缓存。这是为了加快DNS解析速度，使得不必每次都到根域名服务器中去查询。</p>
<p>递归查询的步骤有</p>
<p>第一步：浏览器缓存查询，现在浏览的缓存中查找是否有对应的域名的IP，如果有该解析过程将会结束，如果没有静茹下一步。</p>
<p>第二步：系统缓存查询，操作系统会检查自己本地的hosts文件。如果有，就先调用这个IP地址，完成域名解析。如果没有的话，就会进入第三步</p>
<p>第三步：路由器缓存查询，路由器有自己的DNS缓存，如果在路由器的缓存中没有找到对应的IP，就会进入下一步。</p>
<p>第四步：DNS服务器查询，这里就是迭代查询</p>
<h2 data-id="heading-4">迭代查询</h2>
<p>整个递归查找过程如下：</p>
<p>在根域名服务器<code>.</code>中查找，但是他不会直接的说出IP，而是带领进入顶级域名，就会进入<code>.com .net .cn</code>等顶级域名服务器中查询，他也不会直接返回ip，而是返回权威域名，然后进入权威域名服务器，例如 <code>163.com baidu.com</code>等。在权威域名中返回对应的IP。</p>
<p>拿到IP后传给本地的DNS，然后返回给电脑，同时也会进行缓存，以便下次快速进入，最后来和目标服务器建立连接。</p>
<p><strong>注意</strong>：迭代是不会自己去查询ip，而是查找相关的服务器IP地址返回给客户端，客户端会不断的向这些服务器进行查询，直到查询到了位置。</p>
<p>经过一番的查询就会得到IP开始建立链接：</p>
<h1 data-id="heading-5">TCP/IP连接</h1>
<p>预备知识</p>
<blockquote>
<p>SYN 同步位  SYN=1 表示进行一个链接请求</p>
<p>ACK 确认位  ACK=1 确认有效  ACK=0 确认无效</p>
<p>ack 确认号 对方发送的 序号+1</p>
<p>seq 序号 随机的</p>
<p>FIN 终止   FIN= 1数据已经发送完毕，并且要求释放。</p>
</blockquote>
<p>简单小对话，基础了解<strong>三次握手</strong></p>
<p>C：我要给你发信息了</p>
<p>S：好的，我准备好了，你发吧</p>
<p>C：好的，收到</p>
<p>在DNS解析后得到IP，这时就该建立链接，建立链接就会经历三次握手</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5db82c05ef0b46639938b85431ce7f92~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708102805517" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第一次握手：建立连接时，客户端发送syn包（syn=j）到服务器，并进入SYN_SENT状态，等待服务器确认；SYN：同步序列编号（Synchronize Sequence Numbers）。</li>
<li>第二次握手：服务器收到syn包，必须确认客户的SYN（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包，此时服务器进入SYN_RECV状态；</li>
<li>第三次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=k+1），此包发送完毕，客户端和服务器进入ESTABLISHED（TCP连接成功）状态，完成三次握手。</li>
</ul>
<p><strong>握手过程中传送的包里不包含数据，三次握手完毕后，客户端与服务器才正式开始传送数据。</strong></p>
<p><strong>TCP 三次握手结束后，开始发送 HTTP 请求报文</strong>。</p>
<h1 data-id="heading-6">HTTP请求</h1>
<p>发送HTTP请求的过程就是构建HTTP请求报文并通过TCP协议中发送到服务器指定端口 请求报文由<strong>请求行</strong>，<strong>请求头</strong>，<strong>请求体</strong>组成。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f60aecb5bcdc43e4839253f6a03dcb56~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708113332627" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">请求行</h2>
<p><strong>包含请求方法、URL、协议版本</strong></p>
<ul>
<li>请求方法包含 8 种：GET、POST、PUT、DELETE、PATCH、HEAD、OPTIONS、TRACE。</li>
<li>URL 即请求地址，由 <协议>：//<主机>：<端口>/<路径>?<参数> 组成</li>
<li>协议版本即 http 版本号</li>
</ul>
<h2 data-id="heading-8">请求头</h2>
<p>请求头部通知服务器有关于客户端请求的信息。它包含许多有关的客户端环境和请求正文的有用信息。其中比如：<strong>Host，表示主机名，虚拟主机；Connection,HTTP/1.1 增加的，使用 keepalive，即持久连接，一个连接可以发多个请求；User-Agent，请求发出者，兼容性以及定制化需求。</strong></p>
<h2 data-id="heading-9">请求体</h2>
<p>可以承载多个请求参数的数据，包含回车符、换行符和请求数据，并不是所有请求都具有请求数据。上面图片，承载着 name、password、realName 三个请求参数。</p>
<h1 data-id="heading-10">响应请求</h1>
<p>每台服务器上都会安装处理请求的应用——web server。常见的 web server 产品有 apache、nginx、IIS 或 Lighttpd 等。web server 担任管控的角色，对于不同用户发送的请求，会结合配置文件，把不同请求委托给服务器上处理相应请求的程序进行处理（例如 CGI 脚本，JSP 脚本，servlets，ASP 脚本，服务器端 JavaScript，或者一些其它的服务器端技术等），然后返回后台程序处理产生的结果作为响应。</p>
<p>HTTP的响应报文也由三部分组成（响应行+响应头+响应体）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/146d67dfeb2c41daae0f6053988d3ad2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708113504160" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>从服务器请求的HTML,CSS,JS文件就放在响应体里面。</strong></p>
<p><strong>状态码</strong>，它以“清晰明确”的语言告诉客户端本次请求的处理结果。</p>
<blockquote>
<p>1xx：指示信息–表示请求已接收，继续处理。</p>
<p>2xx：成功–表示请求已被成功接收、理解、接受。</p>
<p>3xx：重定向–要完成请求必须进行更进一步的操作。</p>
<p>4xx：客户端错误–请求有语法错误或请求无法实现。</p>
<p>5xx：服务器端错误–服务器未能实现合法的请求。</p>
</blockquote>
<h1 data-id="heading-11">页面渲染</h1>
<p>在这时就已经拿到了相关数据。</p>
<p>接下就是对获取的内容解析和渲染，这部分就是浏览器需要工作的事。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45e752cb101442168fc62b3827f47adb~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708114320200" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器解析渲染页面分为一下五个步骤：</p>
<h3 data-id="heading-12">1.根据 HTML 解析 DOM 树</h3>
<ul>
<li>根据 HTML 的内容，将标签按照结构解析成为 DOM 树，DOM 树解析的过程是一个深度优先遍历。即先构建当前节点的所有子节点，再构建下一个兄弟节点。</li>
<li>在读取 HTML 文档，构建 DOM 树的过程中，若遇到 script 标签，则 DOM 树的构建会暂停，直至脚本执行完毕。</li>
</ul>
<h3 data-id="heading-13">2.根据 CSS 解析生成 CSS 规则树（CSSOM）</h3>
<ul>
<li>解析 CSS 规则树时 js 执行将暂停，直至 CSS 规则树就绪。</li>
<li>浏览器在 CSS 规则树生成之前不会进行渲染。</li>
</ul>
<h3 data-id="heading-14">3.结合 DOM 树和 CSS 规则树，生成渲染树</h3>
<ul>
<li>DOM 树和 CSS 规则树全部准备好了以后，浏览器才会开始构建渲染树。</li>
<li>精简 CSS 并可以加快 CSS 规则树的构建，从而加快页面相应速度。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98822b8f8d6a4dd49a0b91054f1ea77e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708120555201" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">4.根据渲染树计算每一个节点的信息（布局）</h3>
<ul>
<li>布局：通过渲染树中渲染对象的信息，计算出每一个渲染对象的位置和尺寸</li>
<li>回流：在布局完成后，发现了某个部分发生了变化影响了布局，那就需要倒回去重新渲染。</li>
</ul>
<h3 data-id="heading-16">5.根据计算好的信息绘制页面</h3>
<ul>
<li>绘制阶段，系统会遍历呈现树，并调用呈现器的“paint”方法，将呈现器的内容显示在屏幕上。</li>
<li>重绘：某个元素的背景颜色，文字颜色等，不影响元素周围或内部布局的属性，将只会引起浏览器的重绘。</li>
<li>回流：某个元素的尺寸发生了变化，则需重新计算渲染树，重新渲染。</li>
</ul>
<h2 data-id="heading-17">需要知道的知识</h2>
<h3 data-id="heading-18">回流</h3>
<p>当<code>Render Tree</code>中部分或全部元素的尺寸、结构、或某些属性发生改变时，浏览器重新渲染部分或全部文档的过程称为回流。</p>
<p>会导致回流的操作：</p>
<ul>
<li>页面首次渲染</li>
<li>浏览器窗口大小发生改变</li>
<li>元素尺寸或位置发生改变</li>
<li>元素内容变化（文字数量或图片大小等等）</li>
<li>元素字体大小变化</li>
<li>添加或者删除<strong>可见</strong>的<code>DOM</code>元素</li>
<li>激活<code>CSS</code>伪类（例如：<code>:hover</code>）</li>
<li>查询某些属性或调用某些方法</li>
</ul>
<p>一些常用且会导致回流的属性和方法：</p>
<ul>
<li><code>clientWidth</code>、<code>clientHeight</code>、<code>clientTop</code>、<code>clientLeft</code></li>
<li><code>offsetWidth</code>、<code>offsetHeight</code>、<code>offsetTop</code>、<code>offsetLeft</code></li>
<li><code>scrollWidth</code>、<code>scrollHeight</code>、<code>scrollTop</code>、<code>scrollLeft</code></li>
<li><code>scrollIntoView()</code>、<code>scrollIntoViewIfNeeded()</code></li>
<li><code>getComputedStyle()</code></li>
<li><code>getBoundingClientRect()</code></li>
<li><code>scrollTo()</code></li>
</ul>
<h3 data-id="heading-19">重绘</h3>
<p>当页面中元素样式的改变并不影响它在文档流中的位置时（例如：<code>color、background-color、visibility</code>等），浏览器会将新样式赋予给元素并重新绘制它，这个过程称为重绘。</p>
<h1 data-id="heading-20">TCP断开链接</h1>
<p><strong>当数据传送完毕，需要断开 tcp 连接，此时发起 tcp 四次挥手</strong>。</p>
<p>简单小对话，基础了解<strong>四次挥手</strong></p>
<p>C：我的信息发完了。</p>
<p>S：好的，我听到了，那我就不再接收你的信息了。</p>
<p>S：我也不需要再给你发信息了(全双工通讯)</p>
<p>C：好的，已经关闭了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0445c9bd4aa64f1d8748467f9d783023~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210708103449129" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>1）客户端进程发出连接释放报文，并且停止发送数据。释放数据报文首部，FIN=1，其序列号为seq=u（等于前面已经传送过来的数据的最后一个字节的序号加1），此时，客户端进入FIN-WAIT-1（终止等待1）状态。 TCP规定，FIN报文段即使不携带数据，也要消耗一个序号。</p>
</li>
<li>
<p>2）服务器收到连接释放报文，发出确认报文，ACK=1，ack=u+1，并且带上自己的序列号seq=v，此时，服务端就进入了CLOSE-WAIT（关闭等待）状态。TCP服务器通知高层的应用进程，客户端向服务器的方向就释放了，这时候处于半关闭状态，即客户端已经没有数据要发送了，但是服务器若发送数据，客户端依然要接受。这个状态还要持续一段时间，也就是整个CLOSE-WAIT状态持续的时间。</p>
</li>
<li>
<p>3）客户端收到服务器的确认请求后，此时，客户端就进入FIN-WAIT-2（终止等待2）状态，等待服务器发送连接释放报文（在这之前还需要接受服务器发送的最后的数据）。</p>
</li>
<li>
<p>4）服务器将最后的数据发送完毕后，就向客户端发送连接释放报文，FIN=1，ack=u+1，由于在半关闭状态，服务器很可能又发送了一些数据，假定此时的序列号为seq=w，此时，服务器就进入了LAST-ACK（最后确认）状态，等待客户端的确认。</p>
</li>
<li>
<p>5）客户端收到服务器的连接释放报文后，必须发出确认，ACK=1，ack=w+1，而自己的序列号是seq=u+1，此时，客户端就进入了TIME-WAIT（时间等待）状态。注意此时TCP连接还没有释放，必须经过2*MSL（最长报文段寿命）的时间后，当客户端撤销相应的TCB后，才进入CLOSED状态。</p>
</li>
<li>
<p>6）服务器只要收到了客户端发出的确认，立即进入CLOSED状态。同样，撤销TCB后，就结束了这次的TCP连接。可以看到，服务器结束TCP连接的时间要比客户端早一些。</p>
</li>
</ul>
<h4 data-id="heading-21">参考文章</h4>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fljianshu%2FBlog%2Fissues%2F24" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ljianshu/Blog/issues/24" ref="nofollow noopener noreferrer">从URL输入到页面展现到底发生什么？</a>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F159428230" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/159428230" ref="nofollow noopener noreferrer">TCP连接三次握手、关闭四次挥手[常见问题汇总]</a>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F69731366" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/69731366" ref="nofollow noopener noreferrer">TCP三次握手四次挥手深刻总结</a>      <a href="https://juejin.cn/post/6935232082482298911#heading-13" target="_blank" title="https://juejin.cn/post/6935232082482298911#heading-13">从输入URL开始建立前端知识体系</a>     <a href="https://juejin.cn/post/6844903569087266823" target="_blank" title="https://juejin.cn/post/6844903569087266823">浏览器的回流与重绘 (Reflow & Repaint)</a></p></div>  
</div>
            