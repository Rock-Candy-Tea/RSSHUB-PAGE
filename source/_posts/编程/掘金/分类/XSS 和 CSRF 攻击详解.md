
---
title: 'XSS 和 CSRF 攻击详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9150820b8af465594cb32a445450044~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 19:04:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9150820b8af465594cb32a445450044~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 Web 安全领域中，XSS 和 CSRF 是最常见的攻击方式。</p>
<p>简单的理解：</p>
<ul>
<li>
<p><strong>XSS攻击：</strong> 跨站脚本攻击。</p>
<p><code>攻击者脚本</code> 嵌入 <code>被攻击网站</code>，获取用户cookie等隐私信息。</p>
</li>
<li>
<p><strong>CSRF攻击：</strong> 跨站请求伪造。</p>
<p><code>已登录用户</code> 访问 <code>攻击者网站</code>，攻击网站向被攻击网站发起恶意请求（利用浏览器会自动携带cookie）。</p>
</li>
</ul>
<h1 data-id="heading-0">XSS</h1>
<p>XSS，即 Cross Site Script，中译是跨站脚本攻击。</p>
<blockquote>
<p>其原本缩写是 CSS，但为了和层叠样式表(Cascading Style Sheet)有所区分，因而在安全领域叫做 XSS。</p>
</blockquote>
<p>XSS 攻击是指攻击者在网站上注入恶意的客户端代码，通过恶意脚本对客户端网页进行篡改，从而在用户浏览网页时，对用户浏览器进行控制或者获取用户隐私数据的一种攻击方式。</p>
<p>攻击者对客户端网页注入的恶意脚本一般包括 JavaScript，有时也会包含 HTML 和 Flash。有很多种方式进行 XSS 攻击，但它们的共同点为：将一些隐私数据像 cookie、session 发送给攻击者，将受害者重定向到一个由攻击者控制的网站，在受害者的机器上进行一些恶意操作。</p>
<p>XSS攻击可以分为3类：<a href="https://juejin.cn/post/6945277278347591688#%E5%AD%98%E5%82%A8%E5%9E%8B">存储型</a>（持久型）、<a href="https://juejin.cn/post/6945277278347591688#%E5%8F%8D%E5%B0%84%E5%9E%8B">反射型</a>（非持久型）、<a href="https://juejin.cn/post/6945277278347591688#%E5%9F%BA%E4%BA%8EDOM">基于DOM</a>。</p>
<span id="user-content-存储型">
<h2 data-id="heading-1">存储型</h2>
<p>存储型 XSS 会把用户输入的数据 "存储" 在服务器端，当浏览器请求数据时，脚本从服务器上传回并执行。这种 XSS 攻击具有很强的稳定性。</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9150820b8af465594cb32a445450044~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>通过上图，我们可以看出存储型 XSS 攻击大致需要经过如下步骤：</p>
<ul>
<li>首先黑客利用站点漏洞将一段恶意 JavaScript 代码提交到网站的数据库中；</li>
<li>然后用户向网站请求包含了恶意 JavaScript 脚本的页面；</li>
<li>当用户浏览该页面的时候，恶意脚本就会将用户的 Cookie 信息等数据上传到服务器。</li>
</ul>
<p>下面我们来看个例子，2015 年喜马拉雅就被曝出了存储型 XSS 漏洞。起因是在用户设置专辑名称时，服务器对关键字过滤不严格，比如可以将专辑名称设置为一段 JavaScript，如下图所示：</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448349874197408f9e7a11ab5122fc9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>当黑客将专辑名称设置为一段 JavaScript 代码并提交时，喜马拉雅的服务器会保存该段 JavaScript 代码到数据库中。然后当用户打开黑客设置的专辑时，这段代码就会在用户的页面里执行（如下图），这样就可以获取用户的 Cookie 等数据信息。</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00eff47b5b9e4d589cd7d897d016bd84~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>当用户打开黑客设置的专辑页面时，服务器也会将这段恶意 JavaScript 代码返回给用户，因此这段恶意脚本就在用户的页面中执行了。</p>
<p>恶意脚本可以通过 XMLHttpRequest 或者 Fetch 将用户的 Cookie 数据上传到黑客的服务器，如下图所示：</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86ab956e2ed44dce994f4ff830daa45f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>黑客拿到了用户 Cookie 信息之后，就可以利用 Cookie 信息在其他机器上登录该用户的账号（如下图），并利用用户账号进行一些恶意操作。</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74676b80bdb6440793611603d314ed54~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>以上就是存储型 XSS 攻击的一个典型案例，这是乌云网在 2015 年曝出来的，虽然乌云网由于某些原因被关停了，但是你依然可以通过<a href="https://shuimugan.com/bug/view?bug_no=138479" target="_blank" rel="nofollow noopener noreferrer">这个站点</a>来查看乌云网的一些备份信息。</p>
<span id="user-content-反射型">
<h2 data-id="heading-2">反射型</h2>
<p>反射型 XSS 只是简单地把用户输入的数据 “反射” 给浏览器，这种攻击方式往往需要攻击者诱使用户点击一个恶意链接，或者提交一个表单，或者进入一个恶意网站时，注入脚本进入被攻击者的网站。</p>
<p>下面我们结合一个简单的 Node 服务程序来看看什么是反射型 XSS。首先我们使用 Node 来搭建一个简单的页面环境，搭建好的服务代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">var</span> router = express.Router();
 
 
<span class="hljs-comment">/* GET home page. */</span>
router.get(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
  res.render(<span class="hljs-string">'index'</span>, &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'Express'</span>,<span class="hljs-attr">xss</span>:req.query.xss &#125;);
&#125;);
 
 
<span class="hljs-built_in">module</span>.exports = router;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span><%= title %><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">'stylesheet'</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'/stylesheets/style.css'</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span><%= title %><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Welcome to <%= title %><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <%- xss %>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这两段代码，第一段是路由，第二段是视图，作用是将 URL 中 xss 参数的内容显示在页面。我们可以在本地演示下，比如打开<code>http://localhost:3000/?xss=123</code>这个链接，这样在页面中展示就是“123”了（如下图），是正常的，没有问题的。</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c81b886a5c547d99fa1d96c84fc4971~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>但当打开<code>http://localhost:3000/?xss=alert('你被xss攻击了')</code>这段 URL 时，其结果如下图所示：</p>
<p><img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f0b5b7a399f423590fe0913895a6e32~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过这个操作，我们会发现用户将一段含有恶意代码的请求提交给 Web 服务器，Web 服务器接收到请求时，又将恶意代码反射给了浏览器端，这就是反射型 XSS 攻击。在现实生活中，黑客经常会通过 QQ 群或者邮件等渠道诱导用户去点击这些恶意链接，所以对于一些链接我们一定要慎之又慎。</p>
<p>另外需要注意的是，<strong>Web 服务器不会存储反射型 XSS 攻击的恶意脚本，这是和存储型 XSS 攻击不同的地方</strong>。</p>
<span id="user-content-基于DOM">
<h2 data-id="heading-3">基于 DOM 的 XSS 攻击</h2>
<p>基于 DOM 的 XSS 攻击是不牵涉到页面 Web 服务器的。具体来讲，黑客通过各种手段将恶意脚本注入用户的页面中，比如通过网络劫持在页面传输过程中修改 HTML 页面的内容，这种劫持类型很多，有通过 WiFi 路由器劫持的，有通过本地恶意软件来劫持的，它们的共同点是在 Web 资源传输过程或者在用户使用页面的过程中修改 Web 页面的数据。</p>
<h1 data-id="heading-4">CSRF</h1>
<p>CSRF英文全称是Cross-site request forgery，所以又称为“跨站请求伪造”，是指黑客引诱用户打开黑客的网站,在黑客的网站中，利用用户的登录状态发起的跨站请求。简单来讲，<strong>CSRF攻击就是黑客利用了用户的登录状态，并通过第三方的站点来做一些坏事。</strong></p>
<p>通常当用户打开了黑客的页面后,黑客有三种方式去实施CSRF攻击。</p>
<p>下面我们以极客时间官网为例子,来分析这三种攻击方式都是怎么实施的。这里假设极客时间具有转账功能,可以通过POST或Get来实现转账,转账接口如下所示:</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 同时支持 POST 和 Get</span>
<span class="hljs-comment"># 接口</span>
https://time.geekbang.org/sendcoin
<span class="hljs-comment">#参数</span>
<span class="hljs-comment">## 目标用户</span>
user
<span class="hljs-comment">## 目标金额</span>
number
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了上面的转账接口,我们就可以来模拟CSRF攻击了。</p>
<h2 data-id="heading-5">1. 自动发起Get请求</h2>
<p>黑客最容易实施的攻击方式是自动发起 Get 请求,具体攻击方式你可以参考下面这段代码:</p>
<pre><code class="hljs language-html copyable" lang="html"><! DOCTYPE html> 
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>黑客的站点: CSRF攻击演示<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://time.geekbang.org/sendcoin?user=hacker&number=100"</span>></span> 
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是黑客页面的 HTML 代码，在这段代码中，黑客将转账的请求接口隐藏在 img 标签内，欺骗浏览器这是一张图片资源。当该页面被加载时，浏览器会自动发起 img 的资源请求，如果服务器没有对该请求做判断的话，那么服务器就会认为该请求是一个转账请求，于是用户账户上的100极客币就被转移到黑客的账户上去了。</p>
<h2 data-id="heading-6">2. 自动发起POST请求</h2>
<p>除了自动发送 Get 请求之外，有些服务器的接口是使用 POST 方法的，所以黑客还需要在他的站点上伪造 POST 请求，当用户打开黑客的站点时，是自动提交 POST 请求，具体的方式你可以参考下面示例代码:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>黑客的站点: CSRF攻击演示<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">id</span>= <span class="hljs-string">'hacker-form'</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"https://time.geekbang.org/sendcoin"</span> <span class="hljs-attr">method</span>=<span class="hljs-string">POST</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"hidden"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"userll"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"hacker"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"hidden"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"numberll"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"100"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> <span class="hljs-built_in">document</span>.getElementById (<span class="hljs-string">'hacker-form'</span>).submit(); </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span> 
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这段代码中,我们可以看到黑客在他的页面中构建了一个隐藏的表单，该表单的内容就是极客时间的转账接口。当用户打开该站点之后,这个表单会被自动执行提交；当表单被提交之后，服务器就会执行转账操作。因此使用构建自动提交表单这种方式，就可以自动实现跨站点POST数据提交。</p>
<h2 data-id="heading-7">3. 引诱用户点击链接</h2>
<p>除了自动发起 Get 和 Post 请求之外，还有一种方式是诱惑用户点击黑客站点上的链接，这种方式通常出现在论坛或者恶意邮件上。黑客会采用很多方式去诱惑用户点击链接,示例代码如下所示:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">width</span>=<span class="hljs-string">150</span> <span class="hljs-attr">src</span>=<span class="hljs-string">http://images.xuejuzi.cn/1612/1-161230185104_1.jpg</span>></span> <span class="hljs-tag"></<span class="hljs-name">img</span>></span> 
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://time.geekbang.org/sendcoin?user=hacker&number=100"</span> <span class="hljs-attr">taget</span>=<span class="hljs-string">"_bla点击下载美女照片"</span>
  </<span class="hljs-attr">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段黑客站点代码，页面上放了一张美女图片，下面放了图片下载地址，而这个下载地址实际上是黑客用来转账的接口，一旦用户点击了这个链接，那么他的极客币就被转到黑客账户上了。</p>
<p>以上三种就是黑客经常采用的攻击方式。如果当用户登录了极客时间,以上三种CSRF攻击方式中的任何一种发生时，那么服务器都会将一定金额的极客币发送到黑客账户。</p>
<p>到这里，相信你已经知道什么是CSRF攻击了。<strong>和xss不同的是，CSRF攻击不需要将恶意代码注入用户的页面，仅仅是利用服务器的漏洞和用户的登录状态来实施攻击。</strong></p>
<h1 data-id="heading-8">攻击防御</h1>
<h2 data-id="heading-9">XSS防御</h2>
<p>我们知道存储型 XSS 攻击和反射型 XSS 攻击都是需要经过 Web 服务器来处理的，因此可以认为这两种类型的漏洞是服务端的安全漏洞。而基于 DOM 的 XSS 攻击全部都是在浏览器端完成的，因此基于 DOM 的 XSS 攻击是属于前端的安全漏洞。</p>
<p>但无论是何种类型的 XSS 攻击，它们都有一个共同点，那就是首先往浏览器中注入恶意脚本，然后再通过恶意脚本将用户信息发送至黑客部署的恶意服务器上。</p>
<p>所以要阻止 XSS 攻击，我们可以通过阻止恶意 JavaScript 脚本的注入和恶意消息的发送来实现。</p>
<p>接下来我们就来看看一些常用的阻止 XSS 攻击的策略。</p>
<h3 data-id="heading-10">1. 服务器对输入脚本进行过滤或转码</h3>
<p>不管是反射型还是存储型 XSS 攻击，我们都可以在服务器端将一些关键的字符进行转码，比如最典型的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">code:<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">alert(<span class="hljs-string">'你被 xss 攻击了'</span>)</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码过滤后，只留下了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">code:
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，当用户再次请求该页面时，由于``标签的内容都被过滤了，所以这段脚本在客户端是不可能被执行的。</p>
<p>除了过滤之外，服务器还可以对这些内容进行转码，还是上面那段代码，经过转码之后，效果如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">code:&lt;script&gt;alert(&#<span class="hljs-number">39</span>; 你被 xss 攻击了 &#<span class="hljs-number">39</span>;)&lt;/script&gt;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过转码之后的内容，如``标签被转换为<code><script></code>，因此即使这段脚本返回给页面，页面也不会执行这段脚本。</p>
<h3 data-id="heading-11">2. 充分利用 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP" target="_blank" rel="nofollow noopener noreferrer">CSP</a></h3>
<p>虽然在服务器端执行过滤或者转码可以阻止 XSS 攻击的发生，但完全依靠服务器端依然是不够的，我们还需要把 CSP 等策略充分地利用起来，以降低 XSS 攻击带来的风险和后果。</p>
<p>实施严格的 CSP 可以有效地防范 XSS 攻击，具体来讲 CSP 有如下几个功能：</p>
<ul>
<li>限制加载其他域下的资源文件，这样即使黑客插入了一个 JavaScript 文件，这个 JavaScript 文件也是无法被加载的；</li>
<li>禁止向第三方域提交数据，这样用户数据也不会外泄；</li>
<li>禁止执行内联脚本和未授权的脚本；</li>
<li>还提供了上报机制，这样可以帮助我们尽快发现有哪些 XSS 攻击，以便尽快修复问题。</li>
</ul>
<p>因此，利用好 CSP 能够有效降低 XSS 攻击的概率。</p>
<h3 data-id="heading-12">3. 使用 HttpOnly 属性</h3>
<p>由于很多 XSS 攻击都是来盗用 Cookie 的，因此还可以通过使用 HttpOnly 属性来保护我们 Cookie 的安全。</p>
<p>通常服务器可以将某些 Cookie 设置为 HttpOnly 标志，HttpOnly 是服务器通过 HTTP 响应头来设置的，下面是打开 Google 时，HTTP 响应头中的一段：</p>
<pre><code class="hljs language-json copyable" lang="json">set-cookie: NID=<span class="hljs-number">189</span>=M8q2FtWbsR8RlcldPVt7qkrqR38LmFY9jUxkKo34Bi6Qu_ocNOat7nkYZUTzolHjFnwBw0izgsATSI7TZyiiiaV94qGh-BzEYsNVa7TZmjAYTxYTOM9L_<span class="hljs-number">-0</span>CN9ipL6cXi8l6-z41asXtm2uEwcOC5oh9djkffOMhWqQrlnCtOI; expires=Sat, <span class="hljs-number">18</span>-Apr<span class="hljs-number">-2020</span> <span class="hljs-number">06</span>:<span class="hljs-number">52</span>:<span class="hljs-number">22</span> GMT; path=/; domain=.google.com; HttpOnly
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，set-cookie 属性值最后使用了 HttpOnly 来标记该 Cookie。顾名思义，使用 HttpOnly 标记的 Cookie 只能使用在 HTTP 请求过程中，所以无法通过 JavaScript 来读取这段 Cookie。我们还可以通过 Chrome 开发者工具来查看哪些 Cookie 被标记了 HttpOnly，如下图：</p>
<p><img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adc3679ce90e4a96a4ae484ac16acbca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，NID 这个 Cookie 的 HttpOlny 属性是被勾选上的，所以 NID 的内容是无法通过 document.cookie 是来读取的。</p>
<p>由于 JavaScript 无法读取设置了 HttpOnly 的 Cookie 数据，所以即使页面被注入了恶意 JavaScript 脚本，也是无法获取到设置了 HttpOnly 的数据。因此一些比较重要的数据我们建议设置 HttpOnly 标志。</p>
<h2 data-id="heading-13">CSRF防御</h2>
<p>下面是我总结的发起 CSRF 攻击的三个必要条件:</p>
<ul>
<li>
<p>第一个，目标站点一定要有CSRF漏洞；</p>
</li>
<li>
<p>第二个，用户要登录过目标站点，并且在浏览器上保持有该站点的登录状态；</p>
</li>
<li>
<p>第三个，需要用户打开一个第三方站点,可以是黑客的站点，也可以是一些论坛。</p>
</li>
</ul>
<p>满足以上三个条件之后，黑客就可以对用户进行 CSRF 攻击了。这里还需要额外注意一点，与 XSS 攻击不同，CSRF 攻击不会往页面注入恶意脚本，因此黑客是无法通过 CSRF 攻击来获取用户页面数据的；其最关键的一点是要能找到服务器的漏洞，所以说对于 CSRF 攻击我们主要的防护手段是提升服务器的安全性。</p>
<p>要让服务器避免遭受到 CSRF 攻击,通常有以下几种途径。</p>
<h3 data-id="heading-14">1. 充分利用好Cookie的SameSite属性</h3>
<p>通过上面的介绍，相信你已经知道了黑客会利用用户的登录状态来发起 CSRF 攻击，而 Cookie 正是浏览器和服务器之间维护登录状态的一个关键数据，因此要阻止 CSRF 攻击，我们首先就要考虑在 Cookie 上来做文章</p>
<p>通常 CSRF 攻击都是从第三方站点发起的，要防止 CSRF 攻击，我们最好能实现从第三方站点发送请求时禁止 Cookie 的发送，因此在浏览器通过不同来源发送 HTTP 请求时，有如下区别：</p>
<ul>
<li>
<p>如果是从第三方站点发起的请求，那么需要浏览器禁止发送某些关键 Cookie 数据到服务器；</p>
</li>
<li>
<p>如果是同一个站点发起的请求，那么就需要保证 Cookie 数据正常发送。</p>
</li>
</ul>
<p>而我们要聊的 Cookie 中的 SameSite 属性正是为了解决这个问题的，通过使用 SameSite 可以有效地降低 CSRF 攻击的风险。</p>
<p>那 SameSite 是怎么防止 CSRF 攻击的呢?</p>
<p><strong>在 HTTP 响应头中，通过 set-cookie 字段设置 Cookie 时，可以带上 SameSite 选项，如下：</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash">Set-Cookie: widget_session=abc123; SameSite=None; Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SameSite 选项通常有 Strict、Lax 和 None 三个值。</p>
<ul>
<li>
<p>Strict 最为严格。如果 SameSite 的值是 Strict，那么浏览器会完全禁止第三方 Cookie。</p>
<p>简言之，如果你从极客时间的页面中访问 InfoQ 的资源，而 InfoQ 的某些 Cookie 设置 SameSite = Strict 的话，那么这些 Cookie 是不会被发送到 InfoQ 的服务器上的。只有你从 InfoQ 的站点去请求 InfoQ 的资源时，才会带上这些 Cookie。</p>
</li>
<li>
<p>Lax 相对宽松一点。在跨站点的情况下，从第三方站点的链接打开和从第三方站点提交 GET 方式的表单这两种方式都会携带 Cookie。但如果在第三方站点中使用 Post 方法,或者通过 img，iframe 等标签加载的 URL，这些场景都不会携带 Cookie。</p>
</li>
<li>
<p>而如果使用 None 的话，在任何情况下都会发送 Cookie 数据。</p>
</li>
</ul>
<blockquote>
<p>注意！若设置为 None 必须同时设置<code>Secure</code>属性（Cookie 只能通过 HTTPS 协议发送），否则无效。</p>
</blockquote>
<p><img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1ce209f06974758b933cb44f11d0fb6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于防范 CSRF 攻击，我们可以针对实际情况将一些关键的 Cookie 设置为 Strict 或者 Lax 模式，这样在跨站点请求时，这些关键的 Cookie 就不会被发送到服务器，从而使得黑客的 CSRF 攻击失效。</p>
<h3 data-id="heading-15">2. 验证请求的来源站点</h3>
<p>接着我们再来了解另外一种防止 CSRF 攻击的策略，那就是在服务器端验证请求来源的站点。</p>
<p>由于 CSRF 攻击大多来自于第三方站点，因此服务器可以禁止来自第三方站点的请求。那么该怎么判断请求是否来自第三方站点呢？</p>
<p>这就需要介绍 HTTP 请求头中的 Referer 和 Origin 属性了。</p>
<p><strong>Referer 是 HTTP 请求头中的一个字段，记录了该HTTP请求的来源地址。</strong> 比如我从极客时间的官网打开了 InfoQ 的站点，那么请求头中的 Referer 值是极客时间的 URL，如下图:</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cf1b07372f94505886985e372ccbfe2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>虽然可以通过 Referer 告诉服务器 HTTP 请求的来源，但是有一些场景是不适合将来源 URL 暴露给服务器的，因此浏览器提供给开发者一个选项，可以不用上传 Referer 值，具体可参考 <strong>Referrer Policy</strong>。</p>
<p>但在服务器端验证请求头中的 Referer 并不是太可靠，因此标准委员会又制定了 Origin 属性，在一些重要的场合，比如通过 XMLHttpRequest、Fecth 发起跨站请求或者通过 Post 方法发送请求时，都会带上Origin属性，如下图:</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a7c99d51aee4e1ea8a1c10e32f989a6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>从上图可以看出，Origin 属性只包含了域名信息，并没有包含具体的 URL 路径，这是 Origin 和 Referer 的一个主要区别。在这里需要补充一点,，Origin 的值之所以不包含详细路径信息，是有些站点因为安全考虑，不想把源站点的详细路径暴露给服务器。</p>
<p>因此，服务器的策略是优先判断 Origin，如果请求头中没有包含 Origin 属性，再根据实际情况判断是否使用Referer值。</p>
<h3 data-id="heading-16">3. CSRF Token</h3>
<p>除了使用以上两种方式来防止 CSRF 攻击之外，还可以采用 CSRF Token 来验证，这个流程比较好理解，大致分为两步。</p>
<p>第一步，在浏览器向服务器发起请求时，服务器生成一个 CSRF Token，CSRF Token 其实就是服务器生成的字符串，然后将该字符串植入到返回的页面中。你可以参考下面示例代码:</p>
<pre><code class="hljs language-html copyable" lang="html"><! DOCTYPE html>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"https://time.geekbang.org/sendcoin"</span> <span class="hljs-attr">method</span>=<span class="hljs-string">"POST"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"hidden"</span>" <span class="hljs-attr">name</span>=<span class="hljs-string">lcsrf-token</span>"" <span class="hljs-attr">value</span>=<span class="hljs-string">"nc98P987bcpncYhoadjoiydc9ajDl <input type="</span><span class="hljs-attr">text</span>"<span class="hljs-attr">l</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"userll>
      <input type="</span><span class="hljs-attr">text</span>" <span class="hljs-attr">name</span>=<span class="hljs-string">"number"</span><span class="hljs-attr">l</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步，在浏览器端如果要发起转账的请求，那么需要带上页面中的 CSRF Token，然后服务器会验证该 Token 是否合法。如果是从第三方站点发出的请求，那么将无法获取到 CSRF Token 的值，所以即使发出了请求，服务器也会因为 CSRF Token 不正确而拒绝请求。</p>
<h1 data-id="heading-17">参考</h1>
<ol>
<li>极客时间-浏览器的工作原理与实践33/34</li>
<li><a href="https://github.com/dwqs/blog/issues/68" target="_blank" rel="nofollow noopener noreferrer">浅说 XSS 和 CSRF</a></li>
<li><a href="https://juejin.im/post/5bad9140e51d450e935c6d64" target="_blank" rel="nofollow noopener noreferrer">前端安全系列（一）：如何防止XSS攻击？</a></li>
<li><a href="https://segmentfault.com/a/1190000007059639" target="_blank" rel="nofollow noopener noreferrer">用大白话谈谈XSS与CSRF</a></li>
<li><a href="https://blog.csdn.net/stpeace/article/details/53512283" target="_blank" rel="nofollow noopener noreferrer">CSRF攻击与防御</a></li>
</ol></span></span></span></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            