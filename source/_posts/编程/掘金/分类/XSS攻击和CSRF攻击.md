
---
title: 'XSS攻击和CSRF攻击'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8268'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 23:28:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=8268'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一. 什么是 XSS攻击</h2>
<p>Cross-Site Scripting（<code>跨站脚本攻击</code>）简称 XSS，是一种代码注入攻击。攻击者通过在目标网站上注入恶意脚本，使之在用户的浏览器上运行。利用这些恶意脚本，攻击者可获取用户的敏感信息如 Cookie、SessionID 等，进而危害数据安全。</p>
<h3 data-id="heading-1">XSS 常见的注入方法：</h3>
<ul>
<li>在 HTML 中内嵌的文本中，恶意内容以 script 标签形成注入。</li>
<li>在内联的 JavaScript 中，拼接的数据突破了原本的限制（字符串，变量，方法名等）。</li>
<li>在标签属性中，恶意内容包含引号，从而突破属性值的限制，注入其他属性或者标签。</li>
<li>在标签的 href、src 等属性中，包含 javascript:(伪协议)等可执行代码。</li>
<li>在 onload、onerror、onclick 等事件中，注入不受控制代码。</li>
<li>在 style 属性和标签中，包含类似 background-image:url("javascript:..."); 的代码（新版本浏览器已经可以防范）。</li>
<li>在 style 属性和标签中，包含类似 expression(...)的 CSS 表达式代码（新版本浏览器已经可以防范）。</li>
</ul>
<h3 data-id="heading-2">XSS 攻击的分类</h3>
<p>根据攻击的来源，XSS 攻击可分为存储型、反射型和 DOM 型三种。</p>
<ol>
<li>存储型：即攻击被存储在服务端，常见的是在评论区插入攻击脚本，如果脚本被储存到服务端，那么所有看见对应评论的用户都会受到攻击。</li>
<li>反射型：攻击者将脚本混在URL里，服务端接收到URL将恶意代码当做参数取出并拼接在HTML里返回，浏览器解析此HTML后即执行恶意代码</li>
<li>DOM型：将攻击脚本写在URL中，诱导用户点击该URL，如果URL被解析，那么攻击脚本就会被运行。和前两者的差别主要在于DOM型攻击不经过服务端</li>
</ol>
<p><strong>反射型 XSS 跟存储型 XSS 的区别是：存储型 XSS 的恶意代码存在数据库里，反射型 XSS 的恶意代码存在 URL 里。</strong></p>
<p><strong>DOM 型 XSS 跟前两种 XSS 的区别：DOM 型 XSS 攻击中，取出和执行恶意代码由浏览器端完成，属于前端 JavaScript 自身的安全漏洞，而其他两种 XSS 都属于服务端的安全漏洞。</strong></p>
<h3 data-id="heading-3">XSS常用防范方法</h3>
<ul>
<li>httpOnly: 在 cookie 中设置 HttpOnly 属性后，js脚本将无法读取到 cookie 信息。</li>
<li>输入过滤: 一般是用于对于输入格式的检查，例如：邮箱，电话号码，用户名，密码……等，按照规定的格式输入。不仅仅是前端负责，后端也要做相同的过滤检查。因为攻击者完全可以绕过正常的输入流程，直接利用相关接口向服务器发送设置。</li>
<li>转义 HTML: 如果拼接 HTML 是必要的，就需要对于引号，尖括号，斜杠进行转义,但这还不是很完善.想对 HTML 模板各处插入点进行充分的转义,就需要采用合适的转义库.(可以看下这个库,还是中文的)</li>
</ul>
<pre><code class="copyable">function escape(str) &#123;
  str = str.replace(/&/g, '&amp;')
  str = str.replace(/</g, '&lt;')
  str = str.replace(/>/g, '&gt;')
  str = str.replace(/"/g, '&quto;')
  str = str.replace(/'/g, '&#39;')
  str = str.replace(/`/g, '&#96;')
  str = str.replace(/\//g, '&#x2F;')
  return str
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>白名单: 对于显示富文本来说，不能通过上面的办法来转义所有字符，因为这样会把需要的格式也过滤掉。这种情况通常采用白名单过滤的办法，当然也可以通过黑名单过滤，但是考虑到需要过滤的标签和标签属性实在太多，更加推荐使用白名单的方式。</li>
</ul>
<h2 data-id="heading-4">二. 什么是 CSRF</h2>
<p><code>跨站请求伪造</code>（英语：Cross-site request forgery），也被称为 one-click attack 或者 session riding，通常缩写为 CSRF 或者 XSRF， 是一种挟制用户在当前已登录的 Web 应用程序上执行非本意的操作的攻击方法。如:攻击者诱导受害者进入第三方网站，在第三方网站中，向被攻击网站发送跨站请求。利用受害者在被攻击网站已经获取的注册凭证，绕过后台的用户验证，达到冒充用户对被攻击的网站执行某项操作的目的。</p>
<h3 data-id="heading-5">CSRF防御方法</h3>
<ul>
<li>验证码：强制用户必须与应用进行交互，才能完成最终请求。此种方式能很好的遏制 csrf，但是用户体验比较差。</li>
<li>Referer check：请求来源限制，此种方法成本最低，但是并不能保证 100% 有效，因为服务器并不是什么时候都能取到 Referer，而且低版本的浏览器存在伪造 Referer 的风险。</li>
<li>token：token 验证的 CSRF 防御机制是公认最合适的方案。若网站同时存在 XSS 漏洞的时候，这个方法也是空谈。</li>
</ul>
<h3 data-id="heading-6">CSRF与 XSS 区别</h3>
<ul>
<li>通常来说 CSRF 是由 XSS 实现的，CSRF 时常也被称为 XSRF（CSRF 实现的方式还可以是直接通过命令行发起请求等）。</li>
<li>本质上讲，XSS 是代码注入问题，CSRF 是 HTTP 问题。 XSS 是内容没有过滤导致浏览器将攻击者的输入当代码执行。</li>
<li>CSRF 则是因为浏览器在发送 HTTP 请求时候自动带上 cookie，而一般网站的 session 都存在 cookie里面(Token验证可以避免)。</li>
</ul>
<h2 data-id="heading-7">三、点击劫持 Clickjacking</h2>
<p>Clickjacking： <code>点击劫持</code>，是指利用透明的按钮或连接做成陷阱，覆盖在 Web 页面之上。然后诱使用户在不知情的情况下，点击那个连接访问内容的一种攻击手段。这种行为又称为界面伪装(UI Redressing) 。</p>
<h3 data-id="heading-8">点击劫持的两种方式：</h3>
<ul>
<li>攻击者使用一个透明 iframe，覆盖在一个网页上，然后诱使用户在该页面上进行操作，此时用户将在不知情的情况下点击透明的 iframe 页面；</li>
<li>攻击者使用一张图片覆盖在网页，遮挡网页原有的位置含义。</li>
</ul>
<h3 data-id="heading-9">点击劫持的防御方法</h3>
<ul>
<li><strong>X-FRAME-OPTIONS</strong></li>
</ul>
<p>X-FRAME-OPTIONS HTTP 响应头是用来给浏览器指示允许一个页面可否在,  或者  中展现的标记。网站可以使用此功能，来确保自己网站内容没有被嵌到别人的网站中去，也从而避免点击劫持的攻击。
</p><p>X-FRAME-OPTIONS HTTP有三个值：</p>
<ul>
<li>DENY：表示页面不允许在 frame 中展示，即便是在相同域名的页面中嵌套也不允许。</li>
<li>SAMEORIGIN：表示该页面可以在相同域名页面的 frame 中展示。</li>
<li>ALLOW-FROM url：表示该页面可以在指定来源的 frame 中展示。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            