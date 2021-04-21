
---
title: 'CSRF攻防基础讲解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17070bb9aeeb432fb892468b4e5df5b9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 19:29:37 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17070bb9aeeb432fb892468b4e5df5b9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">CSRF攻击</h1>
<ul>
<li>Cross-site request forgery</li>
<li>跨站请求伪造</li>
</ul>
<h2 data-id="heading-1">场景模拟</h2>
<p>在用户登录某个网站后，看到某篇文章高兴之余，挥手打字，突然有人发来一个链接，登录者打开链接后什么都没有操作或者只是好奇的点击了某个按钮，在原登录网站评论页多出了一条自己的评论记录？？？what happened?<br>
如果您或者您的朋友发生了这样的事情，那么请第一时间邮件反馈给网站维护者，您大概率可能是被攻击了，而这种攻击就是CSRF,下面逐步介绍其攻击原理和防范措施。</p>
<h2 data-id="heading-2">攻击原理</h2>
<ol>
<li>用户登录A网站</li>
<li>A网站登录成功后返回用户身份信息</li>
<li>B网站获取A网站的用户登录身份信息向A网站发起请求，并且携带了A网站的用户身份信息</li>
</ol>
<p><img alt="CSRF攻击原理.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17070bb9aeeb432fb892468b4e5df5b9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">攻击危害</h2>
<ul>
<li>
<p>利用用户登录态</p>
</li>
<li>
<p>用户不知情</p>
</li>
<li>
<p>完成业务请求</p>
</li>
<li>
<p>...</p>
</li>
<li>
<p>盗取用户资金（转账、消费）</p>
</li>
<li>
<p>冒充用户发帖背锅</p>
</li>
<li>
<p>个人隐私泄露</p>
</li>
</ul>
<h1 data-id="heading-4">CSRF 攻击防御</h1>
<h2 data-id="heading-5">禁止第三方网站带Cookies</h2>
<h3 data-id="heading-6">sameSite</h3>
<p><code>samesite</code>是HTTP响应头<code>Set-Cookie</code>的属性之一。它允许您声明该Cookie是否仅限于第一方或者同一站点的访问。<br>
<code>SameSite</code>接受下面三个值:</p>
<ul>
<li>Lax</li>
</ul>
<p>Cookies允许与当前网页的URL与请求目标一致时发送，并且与第三方网站发起的GET请求也会发送。浏览器默认值。</p>
<pre><code class="hljs language-shell copyable" lang="shell">Set-Cookie: userId=123; SameSite=Lax;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Strict</li>
</ul>
<p>Cookies只会在当前网页的URL与请求目标一致时发送，不会与第三方网站发起的请求一起发送。</p>
<pre><code class="hljs language-shell copyable" lang="shell">Set-Cookie:userId=123;SameSite=Strict
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>None</li>
</ul>
<p>Cookie将在所有上下文中发送，即允许跨域发送。<br>
使用<code>None</code>时，必须同时设置<code>Secure</code>属性（Cookie只能通过HTTPS协议发送），否则无效。</p>
<p>以下的设置无效：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Set-Cookie: userId=123; SameSite=None
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面的设置有效：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Set-Cookie: userId=123; SameSite=None;Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多用法可以参考<a href="http://www.ruanyifeng.com/blog/2019/09/cookie-samesite.html" target="_blank" rel="nofollow noopener noreferrer">阮一峰老师SameSite属性介绍</a>、<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite" target="_blank" rel="nofollow noopener noreferrer">MDN-SameSite</a>,到此读者可能会疑惑
sameSite难道可以解决所有的CSRF攻击吗？<br>
答案：当然不是，sameSite受浏览器兼容性的影响，并不能解决防御所有攻击。兼容性列表在MDN的链接中。<br>
再按照攻击原理所理解，CSRF的攻击是不经过目标网站的前端的，那么我们是不是可以在此处“动手脚”尼？</p>
<h2 data-id="heading-7">在前端页面加入验证信息</h2>
<h3 data-id="heading-8">验证码</h3>
<hr>
<p>处理思路：后端生成验证码保存并传递给前端；在前端提交表单数据中加入验证码并提交，在后端校验验证码存在和正确与否；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//验证码生成</span>
<span class="hljs-keyword">var</span> captcha = &#123;&#125;;
<span class="hljs-keyword">var</span> cache = &#123;&#125;;
captcha.captcha = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ctx, next</span>) </span>&#123;
    <span class="hljs-keyword">var</span> ccpa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'ccap'</span>);<span class="hljs-comment">//验证码生成模块</span>
    <span class="hljs-keyword">var</span> capt = ccpa();
    <span class="hljs-keyword">var</span> data = capt.get();
    captcha.setCache(ctx.cookies.get(<span class="hljs-string">'userId'</span>), data[<span class="hljs-number">0</span>]);
    ctx.body = data[<span class="hljs-number">1</span>]
&#125;
captcha.setCache = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">uid, data</span>) </span>&#123;
    cache[uid] = data;
&#125;
captcha.validCache = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">uid, data</span>) </span>&#123;
    <span class="hljs-keyword">return</span> cache[uid] === data;
&#125;
<span class="hljs-built_in">module</span>.exports = captcha;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//验证码校验</span>
...
<span class="hljs-keyword">const</span> data = ctx.request.body;
<span class="hljs-keyword">if</span>(!data.captcha)&#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'验证码错误'</span>)
&#125;
<span class="hljs-keyword">var</span> captcha = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../tools/captcha'</span>)
<span class="hljs-keyword">var</span> resultCaptche = captcha.validCache(ctx.cookies.get(<span class="hljs-string">'userId'</span>),data.captche);
<span class="hljs-keyword">if</span>(!resultCaptche)&#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'验证码错误'</span>)
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加入图形验证码对防御攻击可以起到很好的作用，但是每个表单都需要输入图形验证码且还要保证每次输入的验证码都正确。这对于用户来说是非常痛苦的一件事，由此可见这种方式在实际的使用中并不受用，那么有没有其他的更好的方案尼？</p>
<h3 data-id="heading-9">token验证</h3>
<hr>
<p>token其实是一段随机的字符串，它的作用是让攻击者发起请求时没有办法获取这个字符串，也就是必须要经过我们的页面，经过目标网站的前端。</p>
<ul>
<li>在 HTTP 请求中以參数的形式添加一个随机产生的 token，并在服务器端验证这个 token，假设请求中没有token 或者 token 内容不对，拒绝该请求。</li>
<li>在HTTP请求头中，通过axios的配置参数，给所有的fetch请求全部加上Token这个HTTP请求头属性，并把Token值也放入请求头中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//fetch.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getToken</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'Token'</span>) ||<span class="hljs-string">''</span>;
&#125;
<span class="hljs-keyword">const</span> fetch = axios.create(&#123;
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">60000</span> 
&#125;);
fetch.interceptors.request.use(
    <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
        config.headers[<span class="hljs-string">'X-Token'</span>] = getToken(); 
        <span class="hljs-keyword">return</span> config;
    &#125;,
    <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        closeLoding();
        <span class="hljs-built_in">Promise</span>.reject(error);
    &#125;
);
...
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> fetch;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">关于Token</h3>
<ol>
<li>Token可以保存在localStorage中</li>
<li>Token加密且签名</li>
<li>Token生成与过期机制</li>
<li>将 JSON Web Tokens 应用到 OAuth 2</li>
</ol>
<h2 data-id="heading-11">Referer</h2>
<ul>
<li>验证referer</li>
<li>禁止第三方网站的请求</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 校验代码</span>
<span class="hljs-keyword">const</span> referer = ctx.request.headers.referer;
<span class="hljs-comment">// 简易防御</span>
<span class="hljs-keyword">if</span>(referer.indexOf(<span class="hljs-string">'localhost'</span>)=== -<span class="hljs-number">1</span>)&#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'非法请求'</span>)
&#125;
上面的防御对这个地址是无效的：http:xx.xx.xx?name=<span class="hljs-string">"张三"</span>&uid=<span class="hljs-string">'112'</span>&localhost==<span class="hljs-string">'哈哈哈'</span>
<span class="hljs-comment">// 正则表达式防御</span>
<span class="hljs-keyword">if</span>(!<span class="hljs-regexp">/^https?:\/\/localhost/</span>.test(referer))&#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'非法请求'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这里还要考虑没有referer的情况哈</p>
<h1 data-id="heading-12">结语</h1>
<p>安全作为系统的壁垒，重要程度不用多说。<br>
CSRF攻击更是安全防御的重中之中。<br>
本文记录的是笔者在开发过程中遇到的问题及处理的思路。可供有类似问题的读者参考。<br>
其他安全方面的文章笔者会持续更新,欢迎各位读者提出意见和建议。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            