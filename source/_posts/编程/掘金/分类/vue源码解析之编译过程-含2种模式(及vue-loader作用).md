
---
title: 'vue源码解析之编译过程-含2种模式(及vue-loader作用)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d9b186ad414c1bbfd2d38c8f1f24b3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:36:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d9b186ad414c1bbfd2d38c8f1f24b3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue源码解析之编译过程-含2种模式(及vue-loader作用)</h1>
<p>自从上一次内部分享会分享了 <a href="https://juejin.cn/post/6850037279268798472" target="_blank" title="https://juejin.cn/post/6850037279268798472">vue的diff算法</a> 后，小伙伴们一致对vue的源码感兴趣，那就整吧</p>
<p>注：以下内容只讲了几个关键步骤，个人觉得，先把关键步骤了解明白，知道关键步骤的 输入和输出 后，自己也可以尝试手写实现</p>
<h2 data-id="heading-1">2种模式指的是</h2>
<ol>
<li><strong>.html文件模式</strong>。.html文件内使用vue，没有vue-loader
<ul>
<li>执行.html文件 是vue的最基本的执行，不用加入vue-loader。先了解这个过程，后续更好理解vue-loader做了什么</li>
</ul>
</li>
<li><strong>.vue文件模式</strong>。使用webpack工程，用vue-loader解析.vue 文件</li>
</ol>
<h2 data-id="heading-2">编译过程</h2>
<p>（2种模式，大部分过程是相同的，就获取 匿名渲染树函数 上有所不同）</p>
<ol>
<li>先初始化各种属性和方法</li>
<li>.html文件模式：
<ol>
<li>拿到#app对应的dom代码字符串template</li>
<li>编译template生成ast树 和 <strong>匿名渲染树函数</strong></li>
</ol>
</li>
<li>.vue文件模式：
<ol>
<li>vue-loader编译.vue文件，得到 <strong>匿名渲染树函数</strong></li>
</ol>
</li>
<li>执行 vm._update(vm._render(), hydrating); // （关键函数） 渲染/更新 函数
<ol>
<li>先执行vm._render()，通过 执行 <strong>匿名渲染树函数</strong>，得到 虚拟dom树vnode</li>
<li>在执行vm._update() ，层层递归 虚拟dom树vnode，得到真正的dom节点，然后update到真正的dom树上去，然后浏览器渲染出最新的dom树</li>
</ol>
</li>
</ol>
<h2 data-id="heading-3">.html文件模式的编译过程</h2>
<p>执行.html文件 是vue的最基本的执行，不用加入vue-loader。先了解这个过程，后续更好理解vue-loader做了什么</p>
<h3 data-id="heading-4">测试文件：<strong>.html文件</strong></h3>
<ul>
<li>CDN引入vue的未压缩版，在script标签内，直接使用vue
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  &#123;&#123;aa&#125;&#125; --- 1
  <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"qqq"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  &#123;&#123;C_aa&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
  <span class="hljs-keyword">debugger</span>
  <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">aa</span>: <span class="hljs-number">123</span>
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
      aa (nval, oval) &#123;
        <span class="hljs-built_in">console</span>.log(nval, oval)
      &#125;
    &#125;,
    <span class="hljs-attr">computed</span>: &#123;
      C_aa () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-keyword">async</span> qqq () &#123;
        <span class="hljs-built_in">this</span>.aa = <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">1</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>以下按源代码执行顺序，从上到下</strong></p>
<ol>
<li>
<p>先初始化各种属性和方法</p>
<pre><code class="hljs language-js copyable" lang="js">initLifecycle(vm); <span class="hljs-comment">// 初始化生命周期</span>
initEvents(vm); <span class="hljs-comment">// 初始化事件</span>
initRender(vm); <span class="hljs-comment">// 初始化，处理渲染模板的函数</span>
callHook(vm, <span class="hljs-string">'beforeCreate'</span>); <span class="hljs-comment">// 执行 beforeCreate</span>
initInjections(vm); <span class="hljs-comment">// 初始化inject before data/props</span>
initState(vm); <span class="hljs-comment">// 初始化 props,methods,data,computed,watch</span>
initProvide(vm); <span class="hljs-comment">// 初始化provide after data/props</span>
callHook(vm, <span class="hljs-string">'created'</span>); <span class="hljs-comment">// 执行created</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>拿到#app对应的dom代码字符串</p>
<p>template = getOuterHTML(el);</p>
<p>打印template就是：<code> "<div id="app"> &#123;&#123;aa&#125;&#125; --- 1 <div @click="qqq">click me</div> &#123;&#123;C_aa&#125;&#125; </div>" </code></p>
</li>
<li>
<p>编译template生成ast树 和 匿名渲染树函数</p>
<p>var compiled = compile(template, options);</p>
<ul>
<li>
<p>得到ast树（好处是 方便解析一些vue在标签内的一些特定语法，最终有助于生成匿名渲染函数）</p>
<pre><code class="hljs language-js copyable" lang="js">compiled: &#123;
    <span class="hljs-attr">ast</span>: 太大了 如图,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d9b186ad414c1bbfd2d38c8f1f24b3~tplv-k3u1fbpfcp-watermark.image" alt="ast.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>树结构，子元素都在children内</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b43e71af562d4ef08d27cdb683f07e1a~tplv-k3u1fbpfcp-watermark.image" alt="ast-children.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>得到 匿名渲染树函数</p>
<pre><code class="hljs language-js copyable" lang="js">compiled: &#123;
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_v(<span class="hljs-string">"\n  "</span>+_s(aa)+<span class="hljs-string">" --- 1\n  "</span>),_c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">on</span>:&#123;<span class="hljs-string">"click"</span>:qqq&#125;&#125;,[_v(<span class="hljs-string">"click me"</span>)]),_v(<span class="hljs-string">"\n  "</span>+_s(C_aa)+<span class="hljs-string">"\n"</span>)])&#125;   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 createFunction(compiled.render, fnGenErrors); 得到 <strong>匿名渲染树函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous</span>(<span class="hljs-params">
</span>) </span>&#123;
<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_v(<span class="hljs-string">"\n  "</span>+_s(aa)+<span class="hljs-string">" --- 1\n  "</span>),_c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">on</span>:&#123;<span class="hljs-string">"click"</span>:qqq&#125;&#125;,[_v(<span class="hljs-string">"click me"</span>)]),_v(<span class="hljs-string">"\n  "</span>+_s(C_aa)+<span class="hljs-string">"\n"</span>)])&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还会把这个 <strong>匿名渲染树函数</strong> 的结果缓存起来，key是上面的template，value是匿名渲染树函数</p>
</li>
</ul>
</li>
<li>
<p>callHook(vm, 'beforeMount'); // 执行beforeMount</p>
</li>
<li>
<p><strong>执行 vm._update(vm._render(), hydrating); // （关键函数） 渲染/更新 函数</strong></p>
<ol>
<li>先执行vm._render()，通过 执行 <strong>匿名渲染树函数</strong>，得到 虚拟dom树vnode
<ul>
<li><strong>虚拟dom树vnode是用js对象去表示dom树</strong></li>
<li><strong>操作js要比操作真实的dom性能高很多，特别是做 新旧vnode之间的 diff算法 的时候</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 执行 匿名渲染树函数，得到vnode 虚拟dom树</span>
vnode = render.call(vm._renderProxy, vm.$createElement); 
vnode结构如下图
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee47e322d59444db97cb876ee3ff514e~tplv-k3u1fbpfcp-watermark.image" alt="vnode.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>在执行vm._update() ，层层递归 虚拟dom树vnode，得到真正的dom节点，然后update到真正的dom树上去，然后浏览器渲染出最新的dom树
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!prevVnode) &#123; <span class="hljs-comment">// 第一次渲染</span>
  <span class="hljs-comment">/* 第一次渲染，里面通过递归，一层一层的 createElement 生成真正的dom，
     在appendChild到页面上，在removeChild #app的dom */</span>
  vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">/* updates 通过diff算法，一层一层的对比新旧vonde（时间复杂是n），
     高效的得到新旧vnode的差异，然后根据vnode生成真实的dom，并update到真实的dom树中 */</span>
  vm.$el = vm.__patch__(prevVnode, vnode); <span class="hljs-comment">// 旧vnode 和 新vnode  </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
diff算法的细节，可以看我另一篇：<a href="https://juejin.cn/post/6850037279268798472" target="_blank" title="https://juejin.cn/post/6850037279268798472">juejin.cn/post/685003…</a></li>
</ol>
</li>
<li>
<p>callHook(vm, 'mounted'); // 执行mounted，此时，真实的dom树已经好了，可以获取到dom元素了</p>
</li>
<li>
<p>调用结束</p>
</li>
</ol>
<h2 data-id="heading-5">.vue文件模式的编译过程</h2>
<h3 data-id="heading-6">测试文件：<strong>.vue文件</strong>（内容同上）</h3>
<ul>
<li>
<p>使用webpack工程，用vue-loader解析.vue 文件</p>
<p>app.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123;aa&#125;&#125; --- 1
    <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"qqq"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    &#123;&#123;C_aa&#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">aa</span>: <span class="hljs-number">123</span>
    &#125;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    aa (nval, oval) &#123;
      <span class="hljs-built_in">console</span>.log(nval, oval)
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    C_aa () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">100</span>
    &#125;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-keyword">async</span> qqq () &#123;
      <span class="hljs-built_in">this</span>.aa = <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-built_in">console</span>.log(App)
<span class="hljs-keyword">debugger</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> &#123;
    <span class="hljs-keyword">debugger</span>
    <span class="hljs-built_in">console</span>.log(h(App))
    <span class="hljs-keyword">return</span> h(App)
  &#125;
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>以下按源代码执行顺序，从上到下</strong></p>
<ol>
<li>
<p>先初始化各种属性和方法（同.html文件模式）</p>
</li>
<li>
<p>通过vue-loader编译.vue文件，得到 <strong>匿名渲染树函数</strong></p>
<ol>
<li>先看看vue-loader编译后的.vue文件 长什么样子：（上面main.js 第3行的打印）</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/046d858be0ee41b38275028763122e59~tplv-k3u1fbpfcp-watermark.image" alt="vue-loader.png" loading="lazy" referrerpolicy="no-referrer">
2. 点击 App.vue?6fd5:1 后，可以得到 如下 <strong>匿名渲染树函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> render = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> _vm = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">var</span> _h = _vm.$createElement
  <span class="hljs-keyword">var</span> _c = _vm._self._c || _h
  <span class="hljs-keyword">return</span> _c(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">attrs</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">"app"</span> &#125; &#125;, [
    _vm._v(<span class="hljs-string">" "</span> + _vm._s(_vm.aa) + <span class="hljs-string">" --- 1 "</span>),
    _c(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">on</span>: &#123; <span class="hljs-attr">click</span>: _vm.qqq &#125; &#125;, [_vm._v(<span class="hljs-string">"click me"</span>)]),
    _vm._v(<span class="hljs-string">" "</span> + _vm._s(_vm.C_aa) + <span class="hljs-string">" "</span>)
  ])
&#125;
<span class="hljs-keyword">var</span> staticRenderFns = []
render._withStripped = <span class="hljs-literal">true</span>

<span class="hljs-keyword">export</span> &#123; render, staticRenderFns &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>总结：vue-loader的作用：编译.vue文件，得到 <strong>匿名渲染树函数</strong></li>
</ol>
</li>
<li>
<p>往下的其他步骤 同.html文件模式一样</p>
</li>
</ol>
<h2 data-id="heading-7">下一篇</h2>
<p><a href="https://juejin.cn/post/6997672012231655437/" target="_blank" title="https://juejin.cn/post/6997672012231655437/">vue源码解析之调度原理(响应式原理)</a></p>
<hr>
<p>码字不易，点赞鼓励！</p></div>  
</div>
            