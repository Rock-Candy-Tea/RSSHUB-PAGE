
---
title: '『前端BUG』—— 本地代理导致会话cookie中的数据丢失'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd8d064cd084cbbb00d9e3dbabc8d34~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 08:02:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd8d064cd084cbbb00d9e3dbabc8d34~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h2 data-id="heading-0">问题</h2>
<p>在本地用代理请求服务端接口，解决跨域问题后，发生了一件极其诡异的事情，明明登录成功了，但是请求每个接口都返回未登录的报错信息。</p>
<h2 data-id="heading-1">原因</h2>
<p>该套系统是采用会话cookie进行登录用户的身份认证，故查看每个请求的Request Headers中的cookie的值，发现原本如下图中的红框区域的SESSION不见了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd8d064cd084cbbb00d9e3dbabc8d34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而明明登录接口的Response Headers中是存在set-cookie。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63e4eff2002d4fe48b0c14bf305e3e93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>set-cookie会是把其值中的SESSION存储到浏览器的cookie中，存储成功后，每次请求服务端时，都会去浏览器中的cookie中读取SESSION，然后通过Request Headers中的cookie传递到服务端，完成身份认证。</p>
<p>另外set-cookie的值是服务端设置的，我们来认真观察一下set-cookie的值</p>
<pre><code class="copyable">SESSION=NjE1MTNmZWI1N2ExNDYyZGE4MWE0YmZjNjgwMmFmZGY=; Path=/api/operation/; HttpOnly; SameSite=Lax
<span class="copy-code-btn">复制代码</span></code></pre>
<p>里面除<code>SESSION</code>，还有<code>Path</code>、<code>HttpOnly</code>、<code>SameSite</code>，而<code>Path</code>就是导致SESSION无法存储到客户端中的<strong>元凶</strong>，其中<code>Path</code>的值<code>/api/operation/</code>表示该cookie只有在用请求路径的前缀为<code>/api/operation/</code>才能使用。</p>
<p>回到代理配置中一看，</p>
<pre><code class="copyable">proxy: getProxy(&#123;
  '/dev': &#123; 
    target: 'https://xxx.xxx.com',
    pathRewrite: &#123; '^/dev': '/api' &#125;,
    secure: false,
    changeOrigin: true
  &#125;
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代理后，请求服务端的地址为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxxx.xxx.com%2Fdev%2Foperation%2Fxxx" target="_blank" rel="nofollow noopener noreferrer" title="https://xxx.xxx.com/dev/operation/xxx" ref="nofollow noopener noreferrer">xxx.xxx.com/dev/operati…</a> ，其路径为 dev/operation/xxx，自然与<code>/api/operation/</code>不匹配，导致该cookie无法使用，自然无法将<code>SESSION</code>保存到浏览器的cookie中。</p>
<h2 data-id="heading-2">解决</h2>
<p>找到原因了，问题很好解决，只要更改一下代理配置。</p>
<pre><code class="copyable">proxy: getProxy(&#123;
  '/api': &#123; 
    target: 'https://xxx.xxx.com',
    pathRewrite: &#123; '^/api': '/api' &#125;,
    secure: false,
    changeOrigin: true
  &#125;
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外不要忘记更改 axios 的配置中的<code>baseURL</code>，将其改为<code>/api/</code>。</p></div>  
</div>
            