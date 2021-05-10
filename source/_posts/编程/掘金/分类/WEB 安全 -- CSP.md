
---
title: 'WEB 安全 -- CSP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4308a97a2ba4aa6a2c96db9908a6e62~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 18:32:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4308a97a2ba4aa6a2c96db9908a6e62~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前段时间在做项目页面性能统计时，需要在 html 中嵌入一段 js 脚本，原本以为只要加个 script 标签，写上对应的 js 即可，当我写好代码准备调试时，控制台抛出了个异常...</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4308a97a2ba4aa6a2c96db9908a6e62~tplv-k3u1fbpfcp-watermark.image" alt="CSP[0].png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原来我们项目使用 CSP 来做了一层安全保护，所以并不能直接插入没有“安全标识“的内嵌脚本，那应该怎么插入这段脚本呢？以及 CSP 到底是什么？它是如何保护我们网页的？在一番查阅研究后，找到了答案...</p>
<h3 data-id="heading-0">什么是 CSP（Content Security Policy）</h3>
<p>CSP 直译为「内容安全策略」，它是由 w3c 提出来用于保证 web 站点内容安全的一种机制，定义中的「内容」不仅仅指的是 js 脚本内容，还包含了像网站中的图片、多媒体、样式等资源内容。网站维护者用它去定义一些内容来源的规则，然后通过某种方式将这些规则告诉浏览器，浏览器根据这些规则来判定哪些来源的内容是安全的，可以使用的。</p>
<h3 data-id="heading-1">CSP 作用及原理</h3>
<p>如果把 CSP 比作是一张宴会邀请名单，那么网站维护者就是制作这份名单的人，浏览器就是宴会的管理人员，管理人员根据名单来判别谁能进入宴会，其他不明来源的人（非法内容、脚本）则会被拒绝进入,这样我们就能很好的维护整个宴会的秩序。CSP 一个最显著的作用就是防止网站遭受 XSS 攻击，我们用 CSP 来设定安全的 web 内容域，阻止非法脚本的执行，从本质上消除了 XSS 攻击的可能。举一个最简单的 XSS 攻击，用户通过表单提交一段恶意的 js 脚本，web 站点的后端程序并未对非法字符进行过滤，当其他用户访问该站点时，就会遭殃，倘若使用了 CSP ，这段脚本由于并非来自网站管理者指定的有效域，所以将不被执行。 CSP 除了可以设定内容有效域之外，还可以指定哪种协议是可以被使用的，比如你可以指定所有 web 内容必须通过 https 来加载，这样就可以一定程度上减少网站遭受<a href="https://blog.csdn.net/tangCprogranm/article/details/84558652" target="_blank" rel="nofollow noopener noreferrer">数据包嗅探攻击</a>。</p>
<h3 data-id="heading-2">如何开启 CSP</h3>
<p>在你网站中使用 CSP 其实很简单，有两种开启方式：</p>
<ol>
<li>通过 <code><meta></code> 标签来开启 CSP 的配置;</li>
</ol>
<p><code><meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*;"></code><br>
2. 通过返回 Content-Security-Policy 这个 HTTP Header 即可，这个 Header 对应的值就是我们 web 内容来源的规则;</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0193a7e5f99f42f2a9fbb45151f545f3~tplv-k3u1fbpfcp-watermark.image" alt="CSP[1].jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">如何编写“规则”</h3>
<p>这些规则定义了 web 内容的来源是否合法，它是由一系列 CSP 的指令组合而成，组合格式如同上文的 meta 标签所示，每个指令用 <code>;</code> 进行分隔。比如上面示例中用到的<code>img-src https://*;</code> ,它指定了我们网页中的图片来源地址必须是用 https 协议的。下面列举一些较为常用的指令：</p>
<ul>
<li><strong>script-src</strong> 这个指令规定了网站中可执行脚本的来源，同时也控制了 <a href="https://developer.mozilla.org/zh-CN/docs/Web/XSLT" target="_blank" rel="nofollow noopener noreferrer">XSLT</a> 的来源。</li>
<li><strong>style-src</strong> 定义了样式文件的来源。</li>
<li><strong>img-src</strong> 规定了网站中的图片的来源。</li>
<li><strong>media-src</strong> 规定了富媒体（音视频、<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebVTT_API" target="_blank" rel="nofollow noopener noreferrer">视频文本轨格式</a>）资源的来源。</li>
<li><strong>child-src</strong> 规定了像 worker 、frame 这种嵌入可使用的链接。</li>
<li><strong>font-src</strong> 规定了字体的来源，如果在网页中使用了第三方字体可以使用这个指令。</li>
<li><strong>form-action</strong> 规定了网页中的 <code>form</code> 元素 <code>action</code> 的可提交地址。</li>
<li><strong>connect-src</strong> 规定了脚本中发起连接的地址，像 XMLHttpRequest 的 send 方法、WebSocket连接地址、EventSource 等。</li>
<li><strong>frame-src</strong> 这个指令规定了 frame 的可使用链接。在 CSP level 2 中废弃了，文档中叫我们用 child-src 来代替这个指令，但在 level 3 中恢复使用。</li>
<li><strong>object-src</strong> 规定了一些插件的来源，像 Flash 等。</li>
<li><strong>report-uri</strong> 这个指令是指定一个 CSP 上报地址，当浏览器检测到有不通过指令时，将通过这个指定地址进行上报。值得注意的是，这个指令不能在 meta 元素中使用，并且在 CSP level3 中这个指令会被废弃，用 report-to 来代替，为了保证这个指令有效，官方推荐 report-uri & report-to 同时使用。</li>
<li><strong>worker-src</strong> 这个指令是 CSP level3 中加的，规定了 Worker、SharedWorker、serviceWorker 中可用的地址。</li>
<li><strong>base-uri</strong> 规定了页面 <code>base</code> 标签中的链接。</li>
<li><strong>frame-ancestors</strong> 规定了当前的页面可以被哪些来源所嵌入。作用于 <code><frame>, <iframe>, <embed>, <applet></code>。该指令不能通过 <code><meta></code>指定且只对非 HTML 文档类型的资源生效。</li>
</ul>
<p>对于上面这些指令，w3c 也给他们设定了一些预设值，来完成一些基础场景的指令配置：</p>
<ul>
<li>self 这个值代表指令的来源只匹配当前域，不包括子域。比如 example.com 可以，api.example.com 则会匹配失败。</li>
<li>none 指令为这个值的时候，则不匹配任何东西。例如:</li>
</ul>
<p><code>Content-Security-Policy: script-src https://cdn.example.com/scripts/; object-src 'none'</code><br>
这个例子则表示网页中没有插件可以执行。</p>
<ul>
<li>unsafe-inline 该值表示允许内嵌的脚本、样式。直接用这个感觉很粗糙，下面会提到更为安全的内嵌脚本、样式定义方法。</li>
<li>unsafe-eval 代表相应指令的源允许通过字符串动态创建的脚本执行，像 eval、setTimeout 等。</li>
</ul>
<p>对于内联的脚本或者样式，即用 <code>script</code> 标签或者 <code>style</code> 标签内嵌到 HTML 的内容，CSP 也给了限制规则，就是在对应的 script 、style 标签上加一个 nonce 属性，并赋一个加密串，然后在页面的响应头 <code>Content-Security-Policy</code> 中加上这个加密串即可。确保每次请求页面时，加密串是不一样的，不然会让网站攻击者有可乘之机，下面是一个内嵌脚本的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 内嵌到 HTML 的脚本</span>
<script nonce=<span class="hljs-string">'e1f5e9ea-4765-4bf3-bd0a-5c6ab622d375'</span>>
  ...
</script>

<span class="hljs-comment">// 相应头</span>
Content-Security-Policy: script-src <span class="hljs-string">'self'</span> <span class="hljs-string">'nonce-e1f5e9ea-4765-4bf3-bd0a-5c6ab622d375'</span> hm.baidu.com zz.bdstatic.com www.googletagmanager.com;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值的注意的是 <strong>nonce 和 上面提到的预设值需要用 <code>''</code> 单引号包裹起来才能生效。</strong>  一个 nonce 值可以用到多个内联脚本、样式中。</p>
<h3 data-id="heading-4">一个 🌰 分析</h3>
<pre><code class="copyable">Content-Security-Policy: img-src *; connect-src * wss: blob:; frame-src 'self'*.zhihu.com weixin:; 
script-src 'self' *.zhihu.com 'nonce-e1f5e9ea-4765-4bf3-bd0a-5c6ab622d375'; style-src 'self' 'unsafe-inline'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中规定了：</p>
<ol>
<li>图片可以是任意来源的；</li>
<li>网站中发起连接的地址可以是 wss 或则 blob 协议的；</li>
<li>内嵌的 iframe 内容必须是来自站点的同一个源，或者是 <code>*.zhihu.com</code>、<code>weixin：</code> 域名协议下；</li>
<li>脚本内容必须自站点的同一个源，或者 <code>*.zhihu.com</code>域下，或者是 nonce 属性为 <code>e1f5e9ea-4765-4bf3-bd0a-5c6ab622d375</code> 的内嵌脚本；</li>
<li>样式内容必须自站点的同一个源，而且支持在 HTML 中通过 style 标签引入内嵌样式内容；</li>
</ol>
<h3 data-id="heading-5">总结</h3>
<p>以上就是 CSP 的基本使用，CSP 还有错误上报等一些辅助功能，这里就不一一介绍了。w3c 提出这个机制，目的是为了更好的保护我们的网站，个人认为在中大型项目中很有必要引入 CSP，引入成本不高，但它能在网站安全上给你极大信心。当然对于 Web 安全来说是没有绝对安全的，只有降低其遭受攻击的风险。</p>
<h4 data-id="heading-6">参考</h4>
<p><a href="https://www.w3.org/TR/CSP3/" target="_blank" rel="nofollow noopener noreferrer">Content Security Policy Level 3</a><br>
<a href="https://www.w3.org/TR/CSP2/" target="_blank" rel="nofollow noopener noreferrer">Content Security Policy Level 2</a><br>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP" target="_blank" rel="nofollow noopener noreferrer">内容安全策略( CSP )</a></p>
<p>原文：<a href="https://zhuanlan.zhihu.com/p/142987601" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/142987601</a></p></div>  
</div>
            