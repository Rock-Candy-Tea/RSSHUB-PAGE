
---
title: '🙇‍♀️  深入跨域，理论和实践都不能少 🌱【回顾 Plan】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42bae9ca445941c98ae37377581636cc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 23:19:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42bae9ca445941c98ae37377581636cc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="图怪兽_9c1382e911db7d26c646ff70332bff80_52263.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42bae9ca445941c98ae37377581636cc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">前言</h1>
<p>从“跨域”这个词开始，去理清跨域这个知识点，途径同源策略，跨过document.domain，window.postMessage，JSONP，CORS等，先放若干个问题，希望看完文章的你可以答上来。</p>
<ol>
<li>能说说跨域吗？</li>
<li>能说说同源策略吗？</li>
<li>为什么要同源策略，它限制了什么？</li>
<li>你知道哪些跨域方案呢？</li>
<li>有关cookie的跨域怎么实现？</li>
<li>能具体说说JSONP吗？返回什么数据呢，前端怎么处理呢？知道什么原理吗？实现过吗？JSONP服务器端实现过吗？</li>
<li>postMessage 了解吗？怎么使用？需要注意什么？（安全方面）</li>
<li>代理了解过吗？用过哪些代理方案呢不？怎么在项目中用呢？</li>
<li>cors可以具体说一个简单请求和非简单请求吗？具体过程说一下？项目中怎么使用？</li>
</ol>
<p>文章可能有些地方写的不当和不全的地方，欢迎评论区给我建议，感谢~~ 🤞🤞🤞</p>
<p>也希望里面的知识点有哪里不清楚的，你可以自己可以花时间去整明白更好，加油呀😊</p>
<p>这次就不放导图啦，右边目录很清楚~~</p>
<h1 data-id="heading-1">1、讲一下跨域是什么？</h1>
<p>一个源加载的文档或者脚本和来自另一个源的文档和脚本等资源进行交互（也就是不满足同源策略的两个源之间进行一些交互），就是跨域。</p>
<p>所以你需要清楚的是同源策略是什么？它为什么出现？它又限制了什么？  往下看吧：</p>
<h1 data-id="heading-2">2、同源策略</h1>
<h2 data-id="heading-3">2.1、 同源策略是什么？</h2>
<p>所谓"同源"指的是"三个相同"。</p>
<ul>
<li>协议相同</li>
<li>域名相同</li>
<li>端口相同</li>
</ul>
<p>举个栗子:</p>
<p><code>http://www.jingda.com/dir/page.html</code>这个网址，协议是<code>http://</code>，域名是<code>www.jingda.com</code>，端口是80（默认端口可以省略）。来看看下面改编的哪些是同源哪些是不同源：</p>
<ul>
<li><code>http://www.jingda.com/dir2/other.html</code>：同源</li>
<li><code>http://jingda1.com/dir/other.html</code>：不同源（域名不同）</li>
<li><code>http://v2.www.jingda.com/dir/other.html</code>：不同源（域名不同）</li>
<li><code>http://www.jingda.com:81/dir/other.html</code>：不同源（端口不同）</li>
<li><code>https://www.jingda.com/dir/page.html</code>：不同源（协议不同）</li>
</ul>
<h2 data-id="heading-4">2.2、 为什么需要同源策略？</h2>
<p>同源政策的目的，是为了保证用户信息的安全，防止恶意的网站窃取数据。它能帮助阻隔恶意文档，减少可能被攻击的媒介。
假设小明同学在A银行的官网进行了登录，之后他又去浏览了其他网站，如果其他网站可以读取A银行官网的cookie，那么小明在A银行的登录信息和其他存款记录等都会被泄露，将是一件非常危险的情况。</p>
<p>而cookie的访问限制只是同源策略限制的一种情况，下面我们介绍一下其他的。</p>
<h2 data-id="heading-5">2.3、 同源策略带来了什么访问限制？</h2>
<ul>
<li>跨源数据存储访问：访问存储在浏览器中的数据，如 localStorage 和 IndexedDB，是以源进行分割；Cookies  使用不同的源定义方式。每个源都拥有自己单独的存储空间，一个源中的 JavaScript 脚本不能对属于其它源的数据进行读写操作。</li>
<li>跨源脚本API访问：JavaScript 的 API 中，如 iframe.contentWindow、 window.parent、window.open 和 window.opener 允许文档间直接相互引用。当两个文档的源不同时，这些引用方式将对 Window 和 Location对象的访问添加限制，</li>
<li>跨源网络访问：同源策略控制不同源之间的交互，例如在使用XMLHttpRequest 或 <img src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"> 标签时则会受到同源策略的约束。</li>
</ul>
<h1 data-id="heading-6">3、解决跨域的几种方法？</h1>
<p>将上面三种访问限制简化成下面的三种表达：</p>
<p>（1） Cookie、LocalStorage 和 IndexDB 无法读取。</p>
<p>（2） JavaScript 的 API 中的一些引用，无法获得。（详见上）</p>
<p>（3） AJAX  请求不能发送。（也就是无法使用XMLHttpRequest）</p>
<p>（因为在网上有关跨域的解决方案，可能是比较多，但这里我是根据上面三种限制依次介绍一下可能行得通的解决方案）</p>
<h2 data-id="heading-7">3.1、 cookie -- document.domain</h2>
<p>当我们尝试解决因同源策略下，无法访问cookie这种情况时，我们可以借助：</p>
<ul>
<li>1、<code>浏览器允许通过设置document.domain共享 Cookie。</code>来达成效果。但是，<code>两个网页一级域名相同，只是二级域名不同</code>才可以设置，那什么是一级域名，什么是二级域名呢？</li>
</ul>
<p>举个栗子：
A网页：<code>http://w1.jingda.com/a.html</code>
在这个网页地址中，<code>w1.jingda.com</code>这部分统称为域名，</p>
<ul>
<li>一级域名是由一个合法的字符串+域名后缀组成，所以，jingda.com这种形式的域名才是一级域名，jingda是域名主体，.com、.net也是域名后缀。</li>
<li>二级域名实际就是一级域名下面的主机名，顾名思义，<code>它是在一级域名前面加上一个字符串</code>，比如w1.jingda.com，</li>
</ul>
<p>解释完怎样的情况可以设置document.domain共享 Cookie，让我们看看一个如何操作：</p>
<p>假设有两个网页地址，我们可以看到，他们的一级域名是相同的，二级域名的不同的：</p>
<p>A网页：<code>http://w1.jingda.com/a.html</code></p>
<p>B网页：<code>http://w2.jingda.com/b.html</code></p>
<p>那么只要设置相同的document.domain，两个网页就可以共享Cookie。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.domain = <span class="hljs-string">'example.com'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>A网页通过脚本设置一个 Cookie。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.cookie = <span class="hljs-string">"test1=hello"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>B网页就可以读到这个 Cookie。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> allCookie = <span class="hljs-built_in">document</span>.cookie;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、服务器也可以在设置Cookie的时候，指定Cookie的所属域名为一级域名，比如.example.com。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Set</span>-Cookie: key=value; domain=.example.com; path=/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话，二级域名和三级域名不用做任何设置，都可以读取这个Cookie。</p>
<p>这里的话，补充一下设置cookie的时候，一些其他的设置来限定其可访问性：</p>
<ol>
<li>Domain 和 Path 标识定义了Cookie的作用域：即允许 Cookie 应该发送给哪些URL。</li>
<li>Secure：Secure属性是说如果一个cookie被设置了Secure=true，那么这个cookie只能用https协议发送给服务器，用http协议是不发送的。</li>
<li>HttpOnly ：使用 HttpOnly 属性可防止通过 JavaScript 访问 cookie 值</li>
<li>SameSite Cookie 允许服务器要求某个 cookie 在跨站请求时不会被发送，从而可以阻止跨站请求伪造攻击（CSRF）。</li>
</ol>
<p>你应该注意到，这里我们只是单单解决了在有一些限制条件下的<code>访问cookie</code>的限制。但是上面还提到的<code>LocalStorage 和 IndexDB</code>暂时还没有解决。(等下再说)</p>
<h2 data-id="heading-8">3.2、 API访问 --  window.postMessage</h2>
<p>postMessage是html5新增的一个解决跨域的一个方法，为了能让不同源中文档进行交流，可以使用 window.postMessage安全地实现跨源通信。（安全是指在正确的使用情况下），这</p>
<h3 data-id="heading-9">3.2.1、window.postMessage的使用场景？</h3>
<p>个我自己也是没有用过的。使用方法大家可以参考这篇<a href="https://blog.csdn.net/weixin_40650646/article/details/81777398?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control&dist_request_id=1328769.70653.16176908362791735&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control" target="_blank" rel="nofollow noopener noreferrer">window.postMessage用法</a>一个比较小的案例</p>
<p>因为是两个窗口页面之间的通信，因此我们这边假设我两个页面，A,B，目的是在B窗口中点击postMessage按钮，能够在A页面收到发来的消息。
A页面：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> op = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'b.html'</span>, <span class="hljs-string">'_blank'</span>); 
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">receiveMessage</span>(<span class="hljs-params">event</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'event'</span>, event);
    &#125;
    op.addEventListener(<span class="hljs-string">"message"</span>, receiveMessage, <span class="hljs-literal">false</span>); 
  &#125;
</script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">"test()"</span>></span>open<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>B页面：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">post</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">window</span>.postMessage(<span class="hljs-string">"hi there!"</span>, location.origin);
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">receiveMessage</span>(<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'event'</span>, event)
  &#125;
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"message"</span>, receiveMessage, <span class="hljs-literal">false</span>);
</script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">"post()"</span>></span>postMessage<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我就直接说一下大概的思路了：
首先看看B页面：</p>
<ol>
<li>在B页面有一个按钮，点击这个按钮会触发一个方法，post()</li>
<li>在post()方法中，window.postMessage("hi there!", location.origin)，发送到所有同源的窗口，注意，当前窗口也会收到</li>
<li>之后通过 window.addEventListener("message", receiveMessage, false)去监听，如果有数据，就执行receiveMessage(),把数据打印出来</li>
</ol>
<p>再来看A页面：</p>
<ol>
<li>在A页面也有一个按钮，当点击这个按钮时触发test()</li>
<li>打开新窗口，并建立窗口的引用变量op = window.open('B.html', '_blank');</li>
<li>op.addEventListener("message", receiveMessage, false); 监听新开窗口发来的消息,通过 receiveMessage() 把数据打印出来</li>
</ol>
<h3 data-id="heading-10">3.2.2、如何正确的使用，以保证安全性？</h3>
<ol>
<li>始终使用origin和source属性验证发件人的身份,没有验证origin和source属性会导致跨站点脚本攻击。</li>
<li>当使用postMessage将数据发送到其他窗口时，指定精确的目标origin，而不是*</li>
</ol>
<h2 data-id="heading-11">3.3、JSONP</h2>
<blockquote>
<p>JSONP(JSON with Padding)是JSON的一种“使用模式”，可用于解决主流浏览器的跨域数据访问的问题。</p>
</blockquote>
<h3 data-id="heading-12">3.3.1、JSONP的介绍</h3>
<p>JSONP 是通过在<code><script></srcipt></code>标签里，通过src，img，href 属性的跨域方式向一个不同源的网站地址发送http请求，并且使得json数据可以在javascript代码中能够使用。</p>
<p>它规避了javascript代码中的跨源网络访问，也就是无法使用XMLHttpRequest，fetch（fetch是基于原生的XMLHttpRequest对象来实现数据请求的）被同源机制管到了。</p>
<p>提前准备一个接口：<code>https://photo.sina.cn/aj/index?page=1&cate=recommend</code>
直接网页中打开，我们是可以看到有很多数据的，如下图：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a55a44ecdcc4ac7a22bda1fa7ef5f4e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>让我们尝试在本地请求一下这个地址，看看能不能拿到数据：这里我们使用的是fetch（fetch是基于原生的XMLHttpRequest对象来实现数据请求的）;</p>
<pre><code class="hljs language-js copyable" lang="js"><body>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        fetch(<span class="hljs-string">'https://photo.sina.cn/aj/index?page=1&cate=recommend'</span>)
            .then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
                <span class="hljs-built_in">console</span>.log(data);
                
            &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 live-server打开浏览器，在控制台可以看到报错了，因为这个是一个跨域的请求：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f79c55945e84098a028d76ef4417586~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来我们来看看JSONP如何解决这个问题：</p>
<h3 data-id="heading-13">3.3.2、jsonp 如何使用？原理是什么？返回数据格式？前端怎么处理？</h3>
<p>还是请求上面的这个网站地址，我们把代码改成下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><body>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callback</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(data);
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://photo.sina.cn/aj/index?page=1&cate=recommend&callback=callback"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>  
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看看页面控制台输出：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a93274fe8c6143e5b6ba22469bc09e36~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>data成功取到了。但是我们的数据到达之后是json数据，不能直接使用，script标签是一个加载资源的标签，它并不能直接运行这个代码。</p>
<p>事实上我们是在访问的时候，在请求的地址后面加上一个，<code>&callback=callback</code>，通知服务器，本地想进行一个跨资源访问（以JSOP的形式进行跨域）。等号后面的<code>callback</code>是一个你自己定义的函数，名字可自取，这个函数就是，通知我需要请求的地址，这边页面上我有一个函数，它会等待调用，用来执行你发过来的数据（也就是可以去执行把数据请求下来的操作）。</p>
<p>因此在数据到达之后，还包了一层函数 <code>callback(&#123;data&#125;)</code>，当数据通过script标签请求下来之后，再通过<code>callback</code>实现了一个调用本地资源的能力。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/742812ac2e5d436d862a4eb433055a36~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后再理一下这部分的内容：</p>
<ul>
<li>JSONP的原理</li>
</ul>
<p>script标签请求数据，在请求的地址后面加上一个，<code>&callback=callback</code>，请求的服务器就在json数据外面包一层callback函数，当这个带有数据的callback函数可以在script得到之后可以运行的函数：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846a35663a2e4c2aa0fa673875901e06~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>返回的数据格式</li>
</ul>
<p>JSON</p>
<ul>
<li>以及前端如何处理的</li>
</ul>
<p>JSON with padding --- <code>callback(&#123;data&#125;)</code></p>
<h3 data-id="heading-14">3.3.3、自己封装一个jsonp？</h3>
<ol>
<li>准备工作</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <script>
    <span class="hljs-keyword">let</span> jsonp = <span class="hljs-function">() =></span> &#123;

    &#125;
    jsonp(<span class="hljs-string">'https://photo.sina.cn/aj/index'</span>, &#123;
      <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">cate</span>: <span class="hljs-string">'recommend'</span>
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(response,<span class="hljs-string">'调用成功啦'</span>);
    &#125;)
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>具体实现流程</li>
</ol>
<ul>
<li>确定传递参数： url 、携带的参数 、callback;</li>
<li>处理url上的参数（？后面的）;</li>
<li>准备好url（携带callback函数）;</li>
<li>构建script标签;</li>
<li>把这个标签挂到window上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="hljs-comment">// 1、确定好参数</span>
    <span class="hljs-keyword">let</span> jsonp = <span class="hljs-function">(<span class="hljs-params">url,data = &#123;&#125;,callback = <span class="hljs-string">'callback'</span></span>) =></span> &#123;
    <span class="hljs-comment">// 2、处理好url里面的参数</span>
      <span class="hljs-keyword">let</span> dataStr = url.indexOf(<span class="hljs-string">'?'</span>) === -<span class="hljs-number">1</span> ? <span class="hljs-string">'?'</span>:<span class="hljs-string">'&'</span>
    <span class="hljs-comment">// 3、把参数和&拼接上去</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> data) &#123;
        dataStr += <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=<span class="hljs-subst">$&#123;data[key]&#125;</span>&`</span>;
      &#125;
    <span class="hljs-comment">// 4、把callback拼接上</span>
      dataStr += <span class="hljs-string">'callback='</span> + callback;
    <span class="hljs-comment">// 5、创建一个script标签</span>
      <span class="hljs-keyword">let</span> oScript = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
      oScript.src = url + dataStr;
      <span class="hljs-built_in">document</span>.body.appendChild(oScript);
     <span class="hljs-comment">// 6、把script标签挂载到window上去</span>

    <span class="hljs-comment">//方案一、</span>
      <span class="hljs-comment">// window[callback] = (data) => &#123;</span>
      <span class="hljs-comment">//   console.log(data);</span>
      <span class="hljs-comment">// &#125;</span>
    <span class="hljs-comment">// 方案二、</span>
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove,reject</span>) =></span> &#123;
        <span class="hljs-built_in">window</span>[callback] = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            reslove(data)
          &#125; <span class="hljs-keyword">catch</span>(e) &#123;
            reject(e)
          &#125; <span class="hljs-keyword">finally</span> &#123;
            oScript.parentNode.removeChild(oScript);
            <span class="hljs-comment">//删除这个script节点</span>
          &#125;
        &#125;
      &#125;)
    &#125;
    <span class="hljs-comment">//调用jsonp方法</span>
    jsonp(<span class="hljs-string">'https://photo.sina.cn/aj/index?a=1'</span>, &#123;
      <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">cate</span>: <span class="hljs-string">'recommend'</span>
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(response,<span class="hljs-string">'调用成功啦'</span>);
    &#125;)
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.3.4、实现一个jsonp服务器端？（node版本，express版本）</h3>
<h4 data-id="heading-16">node版本</h4>
<p>创建一个结构如下的服务器端文件夹，我们将在index.js中实现我们的JSONP：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97ce7dbe8f414f39b56957d2f3c50933~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
http.createServer(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>)</span>&#123;
<span class="hljs-comment">// req url  callback=?</span>
<span class="hljs-built_in">console</span>.log(req.url);
<span class="hljs-keyword">let</span> data = &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;;
res.writeHead(<span class="hljs-number">200</span>, &#123;<span class="hljs-string">'Content-type'</span> : <span class="hljs-string">'text/json'</span>&#125;)
  <span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/callback=([\w]+)/</span>
  <span class="hljs-keyword">if</span> (reg.test(req.url)) &#123;
    <span class="hljs-keyword">let</span> padding = <span class="hljs-built_in">RegExp</span>.$1
    res.end(<span class="hljs-string">`<span class="hljs-subst">$&#123;padding&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(data)&#125;</span>)`</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    res.end(<span class="hljs-built_in">JSON</span>.stringify(data));
  &#125;
<span class="hljs-comment">//  res.end('<p>Hello World</p>');</span>
 res.end(<span class="hljs-built_in">JSON</span>.stringify(data));
&#125;).listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">express 版本</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">var</span> cors = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cors'</span>);<span class="hljs-comment">//后端cors 中间件</span>
<span class="hljs-keyword">const</span> app = express();
app.use(cors());
app.get(<span class="hljs-string">'/product'</span>,<span class="hljs-function">(<span class="hljs-params">req,res</span>)=></span>&#123;
    res.json(&#123;
        <span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">b</span>:<span class="hljs-number">2</span>
    &#125;)
&#125;)
app.listen(<span class="hljs-number">8000</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'server is ok'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">3.4 cors</h2>
<h3 data-id="heading-19">3.4.1、介绍一下cors？</h3>
<blockquote>
<p>CORS是一个W3C标准，全称是"跨域资源共享"（Cross-origin resource sharing）。它允许浏览器向跨源服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制。</p>
</blockquote>
<h3 data-id="heading-20">3.4.2、简单请求和非简单请求？</h3>
<p>浏览器将CORS请求分成两类：简单请求（simple request）和非简单请求（not-so-simple request）。</p>
<p>除了简单请求其他的都是非简单请求，因此只要记住哪些是简单请求就可以啦：</p>
<h4 data-id="heading-21">简单请求：（需要同时满足下面两种条件）</h4>
<ol>
<li>请求方法是以下三种方法之一：</li>
</ol>
<ul>
<li>HEAD</li>
<li>GET</li>
<li>POST</li>
</ul>
<ol start="2">
<li>HTTP的头信息不超出以下几种字段：</li>
</ol>
<ul>
<li>Accept：设置接受的内容类型（请求头）</li>
<li>Accept-Language：设置接受的语言（请求头）</li>
<li>Content-Language：为封闭内容设置自然语言或者目标用户语言（响应头）</li>
<li>Content-Type：（设置请求体的MIME类型（适用POST和PUT请求））只限于三个值</li>
</ul>
<p><code>application/x-www-form-urlencoded</code>： </p>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）<p></p>
<p><code>multipart/form-data</code>：将表单的数据处理为一条消息，以标签为单元，用分隔符分开。既可以上传键值对，也可以上传文件。</p>
<p><code>text/plain</code>：text/plain ：纯文本格式</p>
<h3 data-id="heading-22">3.4.3、项目中怎么使用？</h3>
<ul>
<li>服务器端：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> app= express();
 
app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'server is OK'</span>);
  res.end(<span class="hljs-string">'jingjing'</span>)
&#125;);

<span class="hljs-comment">// app.use((req, res, next) => &#123;</span>
<span class="hljs-comment">// res.header("Access-Control-Allow-Origin",'http://localhost:5500');</span>
<span class="hljs-comment">// res.header("Access-Control-Allow-Credentials", true);</span>
<span class="hljs-comment">// res.header("Access-Control-Allow-Headers", 'Content-Type,Content-Length,Authorization, Accept,X-Requested-With');</span>
<span class="hljs-comment">// res.header("Access-Control-Allow-Methods", 'PUT,POST,GET,DELETE,OPTIONS,HEAD');</span>
<span class="hljs-comment">// req.method === 'OPTIONS' ? res.send('CURRENT SERVICES SUPPORT CROSS DOMAIN REQUESTS!') : next();</span>
<span class="hljs-comment">// &#125;);</span>

app.listen(<span class="hljs-number">8081</span>, <span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Server is running at http://localhost:8081'</span>)
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>前端请求：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"sendAjax()"</span>></span>sendAjax<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> sendAjax = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
        xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:5500'</span>, <span class="hljs-literal">true</span>);
        xhr.send();
        xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (xhr.readyState == <span class="hljs-number">4</span> && xhr.status == <span class="hljs-number">200</span>) &#123;
            <span class="hljs-built_in">console</span>.log(xhr.responseText);
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功了'</span>)
          &#125;
        &#125;;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  </body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跨域报错：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16820873f7364422b97389648ec1442c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>把中间注释的部分放开再执行：没有上面的报错了，也返回了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(xhr.responseText);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功了'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2900bb9d90d24fb298bbb09bef7f92e5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>分析一下：</p>
<ul>
<li>"Access-Control-Allow-Origin",<code>http://localhost:5500</code>：</li>
</ul>
<p>如果服务端仅允许来自 <code>http://localhost:5500</code>的访问，如果服务端返回的 Access-Control-Allow-Origin: * 表明，该资源可以被任意外域访问。</p>
<ul>
<li>"Access-Control-Allow-Credentials", true):</li>
</ul>
<p>Access-Control-Allow-Credentials 头指定了当浏览器的credentials设置为true时是否允许浏览器读取response的内容。</p>
<ul>
<li>"Access-Control-Allow-Headers", 'Content-Type,Content-Length,Authorization, Accept,X-Requested-With'):</li>
</ul>
<p>首部字段 Access-Control-Allow-Headers 表明服务器允许请求中携带字段 X-PINGOTHER 与 Content-Type。</p>
<ul>
<li>"Access-Control-Allow-Methods", 'PUT,POST,GET,DELETE,OPTIONS,HEAD':</li>
</ul>
<p>首部字段 Access-Control-Allow-Methods 表明服务器允许客户端使用 POST, GET 和 OPTIONS 等方法发起请求</p>
<ul>
<li>req.method === 'OPTIONS' ? res.send('CURRENT SERVICES SUPPORT CROSS DOMAIN REQUESTS!') : next():</li>
</ul>
<p>“需预检的请求”要求必须首先使用 OPTIONS   方法发起一个预检请求到服务器，以获知服务器是否允许该实际请求(除简单请求以外的，比如 POST方法就需要用到预检)</p>
<h2 data-id="heading-23">3.5、代理 （nginx）</h2>
<h3 data-id="heading-24">3.5.1 原理</h3>
<p>A网站向B网站请求1.js文件时，向B网站发送一个获取的请求，nginx根据配置文件接收这个请求，代替A网站向B网站来请求这个资源，nginx拿到这个资源后再返回给a网站，以此来解决了跨域问题。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28ca4c97c5b84cd6a4f7cdcdd242ca60~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">3.5.2 使用</h3>
<p>使用Nginx，有关下载和配置Nginx，我就不再这里说了，感兴趣的小伙伴可以参考一下这篇文章，里面配置相关的讲的比较清楚。<a href="https://blog.csdn.net/envon123/article/details/83270277" target="_blank" rel="nofollow noopener noreferrer">正确的Nginx跨域配置</a></p>
<p>（自己平时也没怎么用就是，唉，大多知识点也是一边写一边理）</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cbbbcabfb9447feb70a0d1e6436c9af~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是的但是，学习还是要学滴。回到最开始我们提到的一些问题，来看看你能回答多少 👇👇👇</p>
<h1 data-id="heading-26">总结</h1>
<p>最后再来一次拷问：</p>
<ol>
<li>能说说跨域吗？</li>
<li>能说说同源策略吗？</li>
<li>为什么要同源策略，它限制了什么？</li>
<li>你知道哪些跨域方案呢？</li>
<li>有关cookie的跨域怎么实现？</li>
<li>能具体说说JSONP吗？返回什么数据呢，前端怎么处理呢？知道什么原理吗？实现过吗？JSONP服务器端实现过吗？</li>
<li>postMessage 了解吗？怎么使用？需要注意什么？（安全方面）</li>
<li>代理了解过吗？用过哪些代理方案呢不？怎么在项目中用呢？</li>
<li>cors可以具体说一个简单请求和非简单请求吗？具体过程说一下？项目中怎么使用？</li>
</ol>
<p>🙈</p>
<p>好啦，有关跨域的就梳理到这里了</p>
<p>还好菜，继续加油吧</p>
<p>我是婧大，一个大三学崽，目前正在准备实习面试。</p>
<p>这段时间应该主要是理理一些知识点，欢迎一起学习。wx:lj18379991972 💕💕💕</p>
<p>你的点赞是给我最大的支持🤞</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0cb8b3f344c48778940762ffe92b8cd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>【参考文献】：</p>
<p><a href="http://www.ruanyifeng.com/blog/2016/04/cors.html" target="_blank" rel="nofollow noopener noreferrer">跨域资源共享 CORS 详解</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy" target="_blank" rel="nofollow noopener noreferrer">浏览器的同源策略</a></p>
<p><a href="https://blog.csdn.net/envon123/article/details/83270277" target="_blank" rel="nofollow noopener noreferrer">正确的Nginx跨域配置</a></p>
<p><a href="https://blog.csdn.net/weixin_40650646/article/details/81777398?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control&dist_request_id=1328769.70653.16176908362791735&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control" target="_blank" rel="nofollow noopener noreferrer">window.postMessage用法</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers" target="_blank" rel="nofollow noopener noreferrer">HTTP Headers</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            