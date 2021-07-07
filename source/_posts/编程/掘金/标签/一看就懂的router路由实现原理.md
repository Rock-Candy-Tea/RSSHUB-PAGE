
---
title: '一看就懂的router路由实现原理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6996'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 02:33:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=6996'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、什么是前端路由</h2>
<hr>
<ul>
<li>路由这个概念最先是后端出现的。在以前用模板引擎开发页面时，经常会看到这样</li>
</ul>
<pre><code class="copyable">        http://www.xxx.com/login

        http://www.xxx.com/register

        http://www.xxx.com/home
        
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>大致流程可以看成这样：</li>
</ul>
<ol>
<li>
<p>浏览器发出请求</p>
</li>
<li>
<p>服务器监听到80端口（或443）有请求过来，并解析url路径</p>
</li>
<li>
<p>根据服务器的路由配置，返回相应信息（可以是 html 字串，也可以是 json 数据，图片等）</p>
<ol start="4">
<li>浏览器根据数据包的 Content-Type 来决定如何解析数据</li>
</ol>
</li>
</ol>
<ul>
<li>后端路由简单来说路由就是用来跟后端服务器进行交互的一种方式，通过不同的路径，来请求不同的资源，请求不同的页面是路由的其中一种功能。而前端路由则是在 Web 前端单页应用 SPA(Single Page Application)中，路由描述的是 URL 与 UI 之间的映射关系，这种映射是单向的，即 URL 变化引起 UI 更新（无需刷新页面）。</li>
</ul>
<h2 data-id="heading-1">二、前端路由模式</h2>
<ul>
<li>前端路由有两种模式：分别为 <strong>hash模式</strong> 和 <strong>history模式</strong>。</li>
</ul>
<h3 data-id="heading-2">1. hash 模式</h3>
<p>随着 ajax 的流行，异步数据请求交互运行在不刷新浏览器的情况下进行。而异步交互体验的更高级版本就是 SPA —— 单页应用。单页应用不仅仅是在页面交互是无刷新的，连页面跳转都是无刷新的，为了实现单页应用，所以就有了前端路由。</p>
<p>类似于服务端路由，前端路由实现起来其实也很简单，就是匹配不同的 url 路径，进行解析，然后动态的渲染出区域 html 内容。但是这样存在一个问题，就是 url 每次变化的时候，都会造成页面的刷新。那解决问题的思路便是在改变 url 的情况下，保证页面的不刷新。在 2014 年之前，大家是通过 hash 来实现路由，url hash 就是类似于：</p>
<pre><code class="copyable">        http://www.xxx.com/#/login

        http://www.xxx.com/#/home
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种 <strong>#</strong>。后面 hash 值的变化，并不会导致浏览器向服务器发出请求，浏览器不发出请求，也就不会刷新页面。另外每次 hash 值的变化，还会触发 <strong>hashchange</strong> 这个事件，通过这个事件我们就可以知道 hash 值发生了哪些变化。然后我们便可以监听<strong>hashchange</strong>来实现更新页面部分内容的操作：</p>
<h3 data-id="heading-3">2. history 模式</h3>
<p>14年后，因为HTML5标准发布。多了两个 API，<strong>pushState</strong> 和 <strong>replaceState</strong>，通过这两个 API 可以改变 url 地址且不会发送请求。同时还有<strong>popstate</strong> 事件。通过这些就能用另一种方式来实现前端路由了，但原理都是跟 hash 实现相同的。用了 HTML5 的实现，单页路由的 url 就不会多出一个#，变得更加美观。但因为没有 # 号，所以当用户刷新页面之类的操作时，浏览器还是会给服务器发送请求。为了避免出现这种情况，所以这个实现需要服务器的支持，需要把所有路由都重定向到根页面。</p>
<h3 data-id="heading-4">三、如何实现前端路由？</h3>
<ul>
<li>
<p>要实现前端路由，需要解决<strong>两个核心</strong>：</p>
<ol>
<li>
<p>如何改变 URL 却不引起页面刷新？</p>
</li>
<li>
<p>如何检测 URL 变化了？</p>
</li>
</ol>
</li>
</ul>
<p>下面分别使用 <strong>hash</strong> 和 <strong>history</strong> 两种实现方式回答上面的两个核心问题。</p>
<h4 data-id="heading-5">1. hash 实现</h4>
<p>hash 是 URL 中 hash (#) 及后面的那部分，常用作锚点在页面内进行导航，改变 URL 中的 hash 部分不会引起页面刷新通过 hashchange 事件监听 URL 的变化。</p>
<ul>
<li>
<p>改变 URL 的方式只有这几种：</p>
<ol>
<li>
<p>通过浏览器前进后退改变 URL</p>
</li>
<li>
<p>通过 a 标签改变 URL</p>
</li>
<li>
<p>通过window.location改变URL</p>
</li>
</ol>
</li>
</ul>
<h4 data-id="heading-6">2. history 实现</h4>
<p>history 提供了 <strong>pushState</strong> 和 <strong>replaceState</strong> 两个方法，这两个方法改变 URL 的 path 部分不会引起页面刷新。</p>
<ul>
<li>
<p>history 提供类似 <strong>hashchange</strong> 事件的 <strong>popstate</strong> 事件，但 <strong>popstate</strong> 事件有些不同：</p>
<ol>
<li>
<p>通过浏览器前进后退改变 URL 时会触发 <strong>popstate</strong> 事件</p>
</li>
<li>
<p>通过<strong>pushState</strong>/<strong>replaceState</strong>或 a 标签改变 URL 不会触发 <strong>popstate</strong> 事件。</p>
</li>
<li>
<p>好在我们可以拦截 <strong>pushState</strong>/<strong>replaceState</strong>的调用和 a 标签的点击事件来检测 URL 变化</p>
</li>
<li>
<p>通过js 调用 <strong>history</strong> 的 <strong>back</strong>，<strong>go</strong>，**forward **方法课触发该事件</p>
</li>
</ol>
</li>
</ul>
<p>所以监听 URL 变化可以实现，只是没有 <strong>hashchange</strong> 那么方便。</p>
<h2 data-id="heading-7">四、原生js实现前端路由示例</h2>
<h3 data-id="heading-8">1. hash实现</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-comment"><!-- 定义路由 --></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/home"</span>></span>home<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/about"</span>></span>about<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

        <span class="hljs-comment"><!-- 渲染路由对应的 UI --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"routeView"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> routerView = routeView
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">let</span> hash = location.hash;
        routerView.innerHTML = hash
    &#125;)
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'DOMContentLoaded'</span>, <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">if</span>(!location.hash)&#123;<span class="hljs-comment">//如果不存在hash值，那么重定向到#/</span>
            location.hash=<span class="hljs-string">"/"</span>
        &#125;<span class="hljs-keyword">else</span>&#123;<span class="hljs-comment">//如果存在hash值，那就渲染对应UI</span>
            <span class="hljs-keyword">let</span> hash = location.hash;
            routerView.innerHTML = hash
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解释下上面代码，其实很简单：</li>
</ul>
<ol>
<li>
<p>我们通过a标签的href属性来改变URL的hash值（当然，你触发浏览器的前进后退按钮也可以，或者在控制台输入window.location赋值来改变hash）</p>
</li>
<li>
<p>我们监听hashchange事件。一旦事件触发，就改变routerView的内容，若是在vue中，这改变的应当是router-view这个组件的内容</p>
</li>
<li>
<p>为何又监听了load事件？这时应为页面第一次加载完不会触发 hashchange，因而用load事件来监听hash值，再将视图渲染成对应的内容</p>
</li>
</ol>
<h3 data-id="heading-9">2. history 实现</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'/home'</span>></span>home<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'/about'</span>></span>about<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"routeView"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> routerView = routeView
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'DOMContentLoaded'</span>, onLoad)
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function">()=></span>&#123;
        routerView.innerHTML = location.pathname
    &#125;)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onLoad</span> (<span class="hljs-params"></span>) </span>&#123;
        routerView.innerHTML = location.pathname
        <span class="hljs-keyword">var</span> linkList = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'a[href]'</span>)
        linkList.forEach(<span class="hljs-function"><span class="hljs-params">el</span> =></span> el.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
            e.preventDefault()
            history.pushState(<span class="hljs-literal">null</span>, <span class="hljs-string">''</span>, el.getAttribute(<span class="hljs-string">'href'</span>))
            routerView.innerHTML = location.pathname
        &#125;))
    &#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释下上面代码：</p>
<ol>
<li>
<p>我们通过a标签的href属性来改变URL的path值（当然，你触发浏览器的前进后退按钮也可以，或者在控制台输入history.go,back,forward赋值来触发popState事件）。这里需要注意的就是，当改变path值时，默认会触发页面的跳转，所以需要拦截 a 标签点击事件默认行为， 点击时使用 pushState 修改 URL并更新手动 UI，从而实现点击链接更新 URL 和 UI 的效果。</p>
</li>
<li>
<p>我们监听popState事件。一旦事件触发，就改变routerView的内容。load事件则是一样的</p>
</li>
</ol>
<ul>
<li>
<p>有个问题：hash模式，也可以用history.go,back,forward来触发hashchange事件吗？</p>
<p>A：也是可以的。因为不管什么模式，浏览器为保存记录都会有一个栈。</p>
</li>
</ul>
<p>哈哈，到这里就差不多，为了搞清楚它的原理也参考了很多文档，东拼西凑的尽量以容易理解的方式把它整理了一下。希望对你们有所帮助，当然，如果本文有什么不妥的地方也欢迎指出。</p></div>  
</div>
            