
---
title: 'web安全 - xss和csrf'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1896'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 18:05:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=1896'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">XSS（Cross-Site Scripting） 跨站脚本攻击</h3>
<p><code>跨站脚本攻击(Cross-Site Scripting, XSS)</code>是指通过<code>存在安全漏洞的Web网站注册用户的浏览器</code>内运行的<code>非法的HTML标签</code>或<code>JavaScript</code>进行的一种攻击。<code>动态创建的HTML部分</code>有可能隐藏着安全漏洞。就这样，攻击者编写脚本设下陷阱，用户在自己的浏览器上运行时，一不小心就会受到被动攻击。</p>
<h3 data-id="heading-1">XSS类型</h3>
<h4 data-id="heading-2">1. 非持久型 XSS（反射型 XSS）</h4>
<p>反射型 XSS 只是简单地把用户输入的数据 “反射” 给浏览器，这种攻击方式往往需要攻击者诱使用户点击一个<code>恶意链接</code>，或者提交一个<code>表单</code>，或者进入一个恶意网站时，注入脚本进入被攻击者的网站。当用户点击恶意链接时，页面跳转到攻击者预先准备的页面，会发现<code>在攻击者的页面执行了 js 脚本</code>。攻击者可以注入任意的恶意脚本进行攻击，可能注入<code>恶作剧脚本</code>，或者注入<code>能获取用户隐私数据(如cookie)的脚本</code>，这取决于攻击者的目的。</p>
<p><strong>防御策略：</strong></p>
<ul>
<li>Web 页面渲染的所有内容或者<code>渲染的数据</code>都必须来自于服务端。</li>
<li>尽量不要从 URL，document.referrer，document.forms 等这种 DOM API 中获取数据直接渲染。</li>
<li>尽量不要使用 <code>eval</code>, new Function()，document.write()，document.writeln()，window.setInterval()，window.setTimeout()，innerHTML，document.createElement() 等可执行字符串的方法。</li>
<li>过滤不必要的HTML标签，例如：<code>iframe</code> alt script和特殊字符。过滤一些事件onclick onfocus。</li>
</ul>
<h4 data-id="heading-3">2. 持久型 XSS（存储型 XSS）</h4>
<p>存储型 XSS 会把用户输入的数据 “存储” 在服务器端，当浏览器请求数据时，脚本从服务器上传回并执行。这种 XSS 攻击具有很强的稳定性。</p>
<p>比较常见的一个场景是攻击者在社区或论坛上写下一篇包含恶意 JavaScript 代码的文章或评论，文章或评论发表后，所有访问该文章或评论的用户，都会在他们的浏览器中执行这段恶意的 JavaScript 代码。</p>
<p><strong>防御策略：</strong></p>
<ul>
<li>
<p><code>CSP</code>：浏览器内置了防范 XSS 的措施 CSP， 本质上就是建立白名单，开发者明确告诉浏览器哪些外部资源可以加载和执行。我们只需要配置规则，如何拦截是由浏览器自己实现的。我们可以通过这种方式来尽量减少 XSS 攻击。</p>
</li>
<li>
<p><code>HttpOnly</code> （最有效的防御手段）</p>
<p>禁止通过document.cookie的方式获取cookies。严格来说，HttpOnly 并非阻止 XSS 攻击，而是能阻止 XSS 攻击后的 Cookie 劫持攻击。</p>
</li>
<li>
<p><code>输入检查</code></p>
<p>不要相信用户的任何输入。 对于用户的任何输入要进行检查、过滤和转义。建立可信任的字符和 HTML 标签白名单，对于不在白名单之列的字符或者标签进行过滤或编码。</p>
</li>
<li>
<p><code>输出检查</code></p>
<p>用户的输入会存在问题，服务端的输出也会存在问题。一般来说，除富文本的输出外，在变量输出到 HTML 页面时，可以使用编码或转义的方式来防御 XSS 攻击。</p>
</li>
</ul>
<h4 data-id="heading-4">3. 基于DOM</h4>
<p>基于 DOM 的 XSS 攻击是指通过恶意脚本修改页面的 DOM 结构，是纯粹发生在客户端的攻击。</p>
<h4 data-id="heading-5">CSRF</h4>
<p><code>CSRF</code>（Cross Site Request Forgery，<code>跨站请求伪造</code>），是一种<code>劫持受信任用户</code>向服务器发送非预期请求的攻击方式。</p>
<p>通常情况下，CSRF 攻击是攻击者借助受害者的 <code>Cookie</code>骗取服务器的信任，可以在受害者毫不知情的情况下以受害者名义伪造请求发送给受攻击服务器，从而在并未授权的情况下执行在权限保护之下的操作。</p>
<p><strong>防御策略：</strong></p>
<p>对 CSRF 攻击的防范措施主要有如下几种方式。</p>
<ul>
<li>
<p>验证码</p>
<p>验证码被认为是对抗 CSRF 攻击最简洁而有效的防御方法。</p>
<p>从上述示例中可以看出，CSRF 攻击往往是在用户不知情的情况下构造了网络请求。而验证码会强制用户必须与应用进行交互，才能完成最终请求。因为通常情况下，验证码能够很好地遏制 CSRF 攻击。</p>
<p>但验证码并不是万能的，因为出于用户考虑，不能给网站所有的操作都加上验证码。因此，验证码只能作为防御 CSRF 的一种辅助手段，而不能作为最主要的解决方案。</p>
</li>
<li>
<p>Referer Check</p>
<p>根据 HTTP 协议，在 HTTP 头中有一个字段叫 Referer，它记录了该 HTTP 请求的来源地址。通过 Referer Check，可以检查请求是否来自合法的"源"。</p>
</li>
<li>
<p>添加 token 验证</p>
<p>CSRF 攻击之所以能够成功，是因为攻击者可以完全伪造用户的请求，该请求中所有的用户验证信息都是存在于 Cookie 中，因此攻击者可以在不知道这些验证信息的情况下直接利用用户自己的 Cookie 来通过安全验证。要抵御 CSRF，关键在于在请求中放入攻击者所不能伪造的信息，并且该信息不存在于 Cookie 之中。可以在 HTTP 请求中以参数的形式加入一个随机产生的 token，并在服务器端建立一个拦截器来验证这个 token，如果请求中没有 token 或者 token 内容不正确，则认为可能是 CSRF 攻击而拒绝该请求。</p>
</li>
</ul>
<h3 data-id="heading-6">参考文章</h3>
<p><a href="https://juejin.cn/post/6951571103953190925" target="_blank">一、web安全（xss/csrf）简单攻击原理和防御方案（理论篇）</a></p>
<p><a href="https://juejin.cn/post/6953059119561441287" target="_blank">二、web安全（xss/csrf）简单攻击原理和防御方案（实战篇）</a></p>
<p><a href="https://github.com/dwqs/blog/issues/68" target="_blank" rel="nofollow noopener noreferrer">浅说 XSS 和 CSRF</a></p></div>  
</div>
            