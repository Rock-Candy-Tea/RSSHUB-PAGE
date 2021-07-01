
---
title: '源码浅析-Vue3中的13个全局Api'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9368'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 17:37:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=9368'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文章共5314字，预计阅读时间5-15分钟。</p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>不知不觉<a href="https://github.com/vuejs/vue-next/blob/004bd18cf75526bd79f68ccea8102aa94a8a28e2/package.json" target="_blank" rel="nofollow noopener noreferrer">Vue-next</a>的版本已经来到了3.1.2，最近对照着源码学习Vue3的全局Api，边学习边整理了下来，希望可以和大家一起进步。</p>
<p>我们以官方定义、用法、源码浅析三个维度来一起看看它们。</p>
<p>下文是关于Vue3全局Api的内容，大家如果有更好的理解和想法，可以在评论区留言，每条我都会回复~</p>
<h1 data-id="heading-1">全局API</h1>
<p>全局API是直接在<code>Vue</code>上挂载方法，在<code>Vue</code>中，全局API一共有13个。分别是：</p>
<ul>
<li><strong>createapp</strong>  返回一个提供应用上下文的应用实例；</li>
<li><strong>h</strong> 返回一个”虚拟节点；</li>
<li><strong>definecomponent</strong> 返回options的对象，在TS下，会给予组件正确的参数类型推断；</li>
<li><strong>defineasynccomponent</strong> 创建一个只有在需要时才会加载的异步组件；</li>
<li><strong>resolvecomponent</strong> 按传入的组件名称解析 component；</li>
<li><strong>resolvedynamiccomponent</strong> 返回已解析的Component或新建的VNode；</li>
<li><strong>resolvedirective</strong> 通过其名称解析一个 directive;</li>
<li><strong>withdirectives</strong> 返回一个包含应用指令的 VNode;</li>
<li><strong>createrenderer</strong> 跨平台自定义渲染;</li>
<li><strong>nexttick</strong> 是将回调函数延迟在下一次dom更新数据后调用;</li>
<li><strong>mergeprops</strong> 将包含 VNode prop 的多个对象合并为一个单独的对象;</li>
<li><strong>usecssmodule</strong> 访问 CSS 模块;</li>
<li><strong>version</strong> 查看已安装的 Vue 的版本号;</li>
</ul>
<h2 data-id="heading-2">createApp</h2>
<p>官方定义：返回一个提供应用上下文的应用实例。应用实例挂载的整个组件树共享同一个上下文。</p>
<p>顾名思义，CreateApp 作为 vue 的启动函数，返回一个应用实例，每个 Vue 应用程序都首先使用以下函数创建一个新的<strong>应用程序实例</strong>，应用程序实例公开的大多数方法都返回相同的实例，可以链式调用。例如：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.createApp(&#123;&#125;).component(<span class="hljs-string">'SearchInput'</span>, SearchInputComponent)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">用法</h3>
<ul>
<li>
<p><strong>第一个参数</strong>: 接收一个根组件选项</p>
</li>
<li>
<p><strong>第二个参数</strong>: 将根 prop 传递给应用程序</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用法示例</span>
<span class="hljs-keyword">import</span> &#123; createApp, h, nextTick &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> app = createApp(&#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      ...
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;...&#125;,
  <span class="hljs-attr">computed</span>: &#123;...&#125;
  ...
&#125;,
    &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'Evan'</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>createApp()</strong>： <a href="https://github.com/vuejs/vue-next/blob/master/packages/runtime-dom/src/index.ts#L56" target="_blank" rel="nofollow noopener noreferrer">56行 - 102行内容 <sup>[1]</sup></a></li>
<li><strong>ensureRenderer()</strong>：<a href="https://github.com/vuejs/vue-next/blob/ef5c41523f98dbb9c26700fa3b987a2fae26b4e1/packages/runtime-dom/src/index.ts#L35" target="_blank" rel="nofollow noopener noreferrer">35 行- 37行内容 <sup>[2]</sup></a></li>
<li><strong>createRenderer（）</strong>：<a href="https://github.com/vuejs/vue-next/blob/ef5c41523f98dbb9c26700fa3b987a2fae26b4e1/packages/runtime-core/src/renderer.ts#L419" target="_blank" rel="nofollow noopener noreferrer">419 行- 424行内容 <sup>[3]</sup></a></li>
<li><strong>baseCreateRenderer()</strong>：<a href="https://github.com/vuejs/vue-next/blob/ef5c41523f98dbb9c26700fa3b987a2fae26b4e1/packages/runtime-core/src/renderer.ts#L448" target="_blank" rel="nofollow noopener noreferrer">448 行- 2418行 <sup>[4]</sup></a></li>
<li><strong>app._component：</strong><a href="https://github.com/vuejs/vue-next/blob/2b52d5d7c53f7843f4a1e85fd7f1720dc2847ebc/packages/runtime-core/src/apiCreateApp.ts#L174" target="_blank" rel="nofollow noopener noreferrer">174行<sup>[5]</sup></a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码位置上方[1]</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createApp = (<span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
    <span class="hljs-comment">// 使用ensureRenderer().createApp() 来创建 app 对象</span>
    <span class="hljs-comment">// 源码位置上方[2]</span>
    <span class="hljs-comment">// -> ensureRenderer方法调用了来自runtime-core的createRenderer</span>
    <span class="hljs-comment">// 源码位置上方[3]</span>
    <span class="hljs-comment">// -> createRenderer(HostNode, HostElement),两个通用参数HostNode(主机环境中的节点)和HostElement(宿主环境中的元素)，对应于宿主环境。</span>
    <span class="hljs-comment">// -> reateRenderer(使用（可选的）选项创建一个 Renderer 实例。),该方法返回了 baseCreateRenderer</span>
    <span class="hljs-comment">// 源码位置上方[4]</span>
    <span class="hljs-comment">// -> baseCreateRenderer方法最终返回 render hydrate createApp三个函数，生成的 render 传给 createAppAPI ，hydrate 为可选参数，ssr 的场景下会用到；</span>
  <span class="hljs-keyword">const</span> app = ensureRenderer().createApp(...args)

  <span class="hljs-keyword">if</span> (__DEV__) &#123;
     <span class="hljs-comment">// DEV环境下，用于组件名称验证是否是原生标签或者svg属性标签</span>
    injectNativeTagCheck(app)
     <span class="hljs-comment">// DEV环境下，检查CompilerOptions如果有已弃用的属性，显示警告</span>
    injectCompilerOptionsCheck(app)
  &#125;

  <span class="hljs-keyword">const</span> &#123; mount &#125; = app
  <span class="hljs-comment">// 从创建的app对象中解构获取mount，改写mount方法后 返回app实例</span>
  app.mount = (containerOrSelector: Element | ShadowRoot | string): <span class="hljs-function"><span class="hljs-params">any</span> =></span> &#123;
    <span class="hljs-comment">// container 是真实的 DOM 元素,normalizeContainer方法使用document.querySelector处理传入的<containerOrSelector>参数，如果在DEV环境下元素不存在 或者 元素为影子DOM并且mode状态为closed，则返回相应的警告 </span>
    <span class="hljs-keyword">const</span> container = normalizeContainer(containerOrSelector)
    <span class="hljs-comment">// 如果不是真实的DOM元素则 return</span>
    <span class="hljs-keyword">if</span> (!container) <span class="hljs-keyword">return</span>

     <span class="hljs-comment">// 这里的app._component 其实就是全局API的createApp的第一个参数，源码位置在上方[5]</span>
    <span class="hljs-keyword">const</span> component = app._component
    <span class="hljs-comment">// component不是函数 并且 没有不包含render、template</span>
    <span class="hljs-keyword">if</span> (!isFunction(component) && !component.render && !component.template) &#123;
      <span class="hljs-comment">// 不安全的情况</span>
      <span class="hljs-comment">// 原因:可能在dom模板中执行JS表达式。</span>
      <span class="hljs-comment">// 用户必须确保内dom模板是可信的。如果它是</span>
      <span class="hljs-comment">// 模板不应该包含任何用户数据。</span>
        
       <span class="hljs-comment">//  使用 DOM的innerHTML作为component.template 内容</span>
      component.template = container.innerHTML
      <span class="hljs-comment">// 2.挂载前检查，获得元素属性的集合遍历如果name不是v-cloak状态 并且属性名称包含v-、:、@ ，会给出vue文档链接提示</span>
      <span class="hljs-keyword">if</span> (__COMPAT__ && __DEV__) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < container.attributes.length; i++) &#123;
          <span class="hljs-keyword">const</span> attr = container.attributes[i]
          <span class="hljs-keyword">if</span> (attr.name !== <span class="hljs-string">'v-cloak'</span> && <span class="hljs-regexp">/^(v-|:|@)/</span>.test(attr.name)) &#123;
            compatUtils.warnDeprecation(
              DeprecationTypes.GLOBAL_MOUNT_CONTAINER,
              <span class="hljs-literal">null</span>
            )
            <span class="hljs-keyword">break</span>
          &#125;
        &#125;
      &#125;
    &#125;

    <span class="hljs-comment">// 挂载前清除内容</span>
    container.innerHTML = <span class="hljs-string">''</span>
    <span class="hljs-comment">// 真正的挂载 （元素， 是否复用[此处个人理解，仅供参考]，是否为SVG元素）</span>
    <span class="hljs-keyword">const</span> proxy = mount(container, <span class="hljs-literal">false</span>, container <span class="hljs-keyword">instanceof</span> SVGElement)
    <span class="hljs-keyword">if</span> (container <span class="hljs-keyword">instanceof</span> Element) &#123;
      <span class="hljs-comment">// 删除元素上的 v-cloak 指令</span>
      container.removeAttribute(<span class="hljs-string">'v-cloak'</span>)
      <span class="hljs-comment">// 设置data-v-app属性</span>
      container.setAttribute(<span class="hljs-string">'data-v-app'</span>, <span class="hljs-string">''</span>)
    &#125;
    <span class="hljs-keyword">return</span> proxy
  &#125;

  <span class="hljs-keyword">return</span> app
&#125;) <span class="hljs-keyword">as</span> CreateAppFunction<Element>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">h</h2>
<p>官方定义：返回一个”虚拟节点“，通常缩写为 <strong>VNode</strong>：一个普通对象，其中包含向 Vue 描述它应在页面上渲染哪种节点的信息，包括所有子节点的描述。它的目的是用于手动编写的渲染函数；</p>
<blockquote>
<p>h是什么意思？根据祖师爷的回复，h 的含义如下：</p>
<p>It comes from the term "hyperscript", which is commonly used in many virtual-dom implementations. "Hyperscript" itself stands for "script that generates HTML structures" because HTML is the acronym for "hyper-text markup language".</p>
<p>它来自术语“hyperscript”，该术语常用于许多虚拟 dom 实现。“Hyperscript”本身代表“生成 HTML 结构的脚本”，因为 HTML 是“超文本标记语言”的首字母缩写词。</p>
<p>回复出处：<a href="https://github.com/vuejs/babel-plugin-transform-vue-jsx/issues/6" target="_blank" rel="nofollow noopener noreferrer">github.com/vuejs/babel…</a></p>
</blockquote>
<p>其实h()函数和createVNode()函数都是创建dom节点，他们的作用是一样的，但是在VUE3中createVNode()函数的功能比h()函数要多且做了性能优化，渲染节点的速度也更快。</p>
<h3 data-id="heading-6">用法</h3>
<ul>
<li>
<p><strong>第一个参数：</strong> HTML 标签名、组件、异步组件或函数式组件。使用返回 null 的函数将渲染一个注释。此参数是必需的。</p>
</li>
<li>
<p><strong>第二个参数：</strong> 一个对象，与我们将在模板中使用的 attribute、prop、class 和、style和事件相对应。可选。</p>
</li>
<li>
<p><strong>第三个参数：</strong> 子代 VNode，使用 <code>h()</code> 生成，或者使用字符串来获取“文本 VNode”，或带有插槽的对象。可选。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用法示例</span>
h(<span class="hljs-string">'div'</span>, &#123;&#125;, [
  <span class="hljs-string">'Some text comes first.'</span>,
  h(<span class="hljs-string">'h1'</span>, <span class="hljs-string">'A headline'</span>),
  h(MyComponent, &#123;
    <span class="hljs-attr">someProp</span>: <span class="hljs-string">'foobar'</span>
  &#125;)
])
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-7">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>h：</strong><a href="https://github.com/vuejs/vue-next/blob/870f2a7ba35245fd8c008d2ff666ea130a7e4704/packages/runtime-core/src/h.ts#L174" target="_blank" rel="nofollow noopener noreferrer">174行 - 196行 <sup>[6]</sup></a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码位置见上方[6]</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">type: any, propsOrChildren?: any, children?: any</span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">arguments</span>.length
  <span class="hljs-comment">// 如果参数是两个</span>
  <span class="hljs-keyword">if</span> (l === <span class="hljs-number">2</span>) &#123;
      <span class="hljs-comment">// 判断是否是对象，并且不为数组</span>
    <span class="hljs-keyword">if</span> (isObject(propsOrChildren) && !isArray(propsOrChildren)) &#123;
      <span class="hljs-comment">// 所有VNode对象都有一个 __v_isVNode 属性，isVNode 方法也是根据这个属性来判断是否为VNode对象。</span>
      <span class="hljs-keyword">if</span> (isVNode(propsOrChildren)) &#123;
        <span class="hljs-keyword">return</span> createVNode(type, <span class="hljs-literal">null</span>, [propsOrChildren])
      &#125;
      <span class="hljs-comment">// 只包含属性不含有子元素  </span>
      <span class="hljs-keyword">return</span> createVNode(type, propsOrChildren)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 忽略props属性 </span>
      <span class="hljs-keyword">return</span> createVNode(type, <span class="hljs-literal">null</span>, propsOrChildren)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">if</span> (l > <span class="hljs-number">3</span>) &#123;
      <span class="hljs-comment">// Array.prototype.slice.call(arguments, 2),这句话的意思就是说把调用方法的参数截取出来,可以理解成是让arguments转换成一个数组对象，让arguments具有slice()方法</span>
      children = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">2</span>)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (l === <span class="hljs-number">3</span> && isVNode(children)) &#123;
      <span class="hljs-comment">// 如果参数长度等于3，并且第三个参数为VNode对象</span>
      children = [children]
    &#125;
    <span class="hljs-comment">// h 函数内部的主要处理逻辑就是根据参数个数和参数类型，执行相应处理操作，但最终都是通过调用 createVNode 函数来创建 VNode 对象</span>
    <span class="hljs-keyword">return</span> createVNode(type, propsOrChildren, children)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">defineComponent</h2>
<p>官方定义：<code>defineComponent</code> 只返回传递给它的对象。但是，就类型而言，返回的值有一个合成类型的构造函数，用于手动渲染函数、TSX 和 IDE 工具支持</p>
<blockquote>
<p>definComponent主要是用来帮助Vue在TS下正确推断出setup()组件的参数类型</p>
<p>引入 defineComponent() 以正确推断 setup() 组件的参数类型；</p>
<p>defineComponent 可以正确适配无 props、数组 props 等形式；</p>
</blockquote>
<h3 data-id="heading-9">用法</h3>
<ul>
<li>
<p>**参数：**具有组件选项的对象或者是一个 <code>setup</code> 函数，函数名称将作为组件名称来使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 之前写Ts + vue，需要声明相关的数据类型。如下</span>
<span class="hljs-comment">// 声明props和return的数据类型</span>
interface Data &#123;
  [key: string]: unknown
&#125;
<span class="hljs-comment">// 使用的时候入参要加上声明，return也要加上声明</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup(props: Data): Data &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// 非常的繁琐，使用defineComponent 之后，就可以省略这些类型定义，defineComponent 可以接受显式的自定义props接口或从属性验证对象中自动推断；</span>

<span class="hljs-comment">// 用法示例1：</span>
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> MyComponent = defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.count++
    &#125;
  &#125;
&#125;)

<span class="hljs-comment">// 用法示例2：</span>
<span class="hljs-comment">// 不只适用于 setup，只要是 Vue 本身的 API ，defineComponent 都可以自动帮你推导。</span>
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  setup (props, context) &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-10">源码浅析</h3>
<p>GitHub地址：<a href="https://github.com/vuejs/vue-next/blob/870f2a7ba35245fd8c008d2ff666ea130a7e4704/packages/runtime-core/src/apiDefineComponent.ts" target="_blank" rel="nofollow noopener noreferrer">源码文件位置</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
...
...
<span class="hljs-comment">//  实际上这个 api 只是直接 return 传进来的 options,export default defineComponent(&#123;&#125;) 是有点等价于export default &#123;&#125;,目前看来这样做的最大作用只是限制 type, setup 必须是函数，props 必须是 undefined 或者 对象。</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComponent</span>(<span class="hljs-params">options: unknown</span>) </span>&#123;
  <span class="hljs-keyword">return</span> isFunction(options) ? &#123; <span class="hljs-attr">setup</span>: options, <span class="hljs-attr">name</span>: options.name &#125; : options
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">defineAsyncComponent</h2>
<p>官方定义：创建一个只有在需要时才会加载的异步组件。</p>
<h3 data-id="heading-12">用法</h3>
<p>参数：接受一个返回 <code>Promise</code> 的工厂函数。Promise 的 <code>resolve</code> 回调应该在服务端返回组件定义后被调用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在 Vue 2.x 中，声明一个异步组件只需这样</span>
<span class="hljs-keyword">const</span> asyncModal = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./Modal.vue'</span>)
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">const</span> asyncModal = &#123;
  <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./Modal.vue'</span>),
  <span class="hljs-attr">delay</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">error</span>: ErrorComponent,
  <span class="hljs-attr">loading</span>: LoadingComponent
&#125;


<span class="hljs-comment">// 现在，在 Vue 3 中，由于函数式组件被定义为纯函数，因此异步组件的定义需要通过将其包裹在新的 defineAsyncComponent 助手方法中来显式地定义：</span>
<span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> ErrorComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ErrorComponent.vue'</span>
<span class="hljs-keyword">import</span> LoadingComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/LoadingComponent.vue'</span>

<span class="hljs-comment">// 不带选项的异步组件</span>
<span class="hljs-keyword">const</span> asyncModal = defineAsyncComponent(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./Modal.vue'</span>))

<span class="hljs-comment">// 带选项的异步组件，对 2.x 所做的另一个更改是，component 选项现在被重命名为loader，以便准确地传达不能直接提供组件定义的信息。注意： defineAsyncComponent不能使用在Vue Router上！</span>
<span class="hljs-keyword">const</span> asyncModalWithOptions = defineAsyncComponent(&#123;
  <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./Modal.vue'</span>),
  <span class="hljs-attr">delay</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">errorComponent</span>: ErrorComponent,
  <span class="hljs-attr">loadingComponent</span>: LoadingComponent
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">源码浅析</h3>
<p>GitHub地址： <a href="https://github.com/vuejs/vue-next/blob/bd3cc4d2c79454736908433b607b1e1323bea67a/packages/runtime-core/src/apiAsyncComponent.ts#L41" target="_blank" rel="nofollow noopener noreferrer">41行- 196行</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码位置见上方</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineAsyncComponent</span><
  <span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Component</span> = </span>&#123; <span class="hljs-keyword">new</span> (): ComponentPublicInstance &#125;
>(source: AsyncComponentLoader<T> | AsyncComponentOptions<T>): T &#123;
      
  <span class="hljs-keyword">if</span> (isFunction(source)) &#123;
    source = &#123; <span class="hljs-attr">loader</span>: source &#125;
  &#125;
 <span class="hljs-comment">// 异步组件的参数</span>
  <span class="hljs-keyword">const</span> &#123;
    loader,
    loadingComponent,
    errorComponent,
    delay = <span class="hljs-number">200</span>,
    timeout, <span class="hljs-comment">// undefined = never times out</span>
    suspensible = <span class="hljs-literal">true</span>,
    <span class="hljs-attr">onError</span>: userOnError
  &#125; = source

  <span class="hljs-keyword">let</span> pendingRequest: <span class="hljs-built_in">Promise</span><ConcreteComponent> | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">let</span> resolvedComp: ConcreteComponent | <span class="hljs-literal">undefined</span>

  <span class="hljs-keyword">let</span> retries = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 重新尝试load得到组件内容</span>
  <span class="hljs-keyword">const</span> retry = <span class="hljs-function">() =></span> &#123;
    retries++
    pendingRequest = <span class="hljs-literal">null</span>
    <span class="hljs-keyword">return</span> load()
  &#125;

  <span class="hljs-keyword">const</span> load = (): <span class="hljs-built_in">Promise</span><ConcreteComponent> => &#123;
    <span class="hljs-keyword">let</span> thisRequest: <span class="hljs-built_in">Promise</span><ConcreteComponent>
    <span class="hljs-keyword">return</span> (
      <span class="hljs-comment">// 如果pendingRequest 存在就return，否则实行loader()</span>
      pendingRequest ||
      (thisRequest = pendingRequest = loader()
       <span class="hljs-comment">// 失败场景处理</span>
        .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          err = err <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Error</span> ? err : <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">String</span>(err))
          <span class="hljs-keyword">if</span> (userOnError) &#123;
            <span class="hljs-comment">// 对应文档中的 失败捕获回调函数 用户使用</span>
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
              <span class="hljs-keyword">const</span> userRetry = <span class="hljs-function">() =></span> resolve(retry())
              <span class="hljs-keyword">const</span> userFail = <span class="hljs-function">() =></span> reject(err)
              userOnError(err, userRetry, userFail, retries + <span class="hljs-number">1</span>)
            &#125;)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">throw</span> err
          &#125;
        &#125;)
        .then(<span class="hljs-function">(<span class="hljs-params">comp: any</span>) =></span> &#123;
          <span class="hljs-comment">// 个人理解：在thisRequest = pendingRequest = loader()，loader()最开始属于等待状态，赋值给pendingRequest、在thisRequest此刻他们是相等的等待状态，当进入then的时候pendingRequest已经发生了改变，所以返回pendingRequest</span>
          <span class="hljs-keyword">if</span> (thisRequest !== pendingRequest && pendingRequest) &#123;
            <span class="hljs-keyword">return</span> pendingRequest
          &#125;
          <span class="hljs-comment">// 如果在DEV环境则警告</span>
          <span class="hljs-keyword">if</span> (__DEV__ && !comp) &#123;
            warn(
              <span class="hljs-string">`Async component loader resolved to undefined. `</span> +
                <span class="hljs-string">`If you are using retry(), make sure to return its return value.`</span>
            )
          &#125;
          <span class="hljs-comment">// interop module default</span>
          <span class="hljs-keyword">if</span> (
            comp &&
            (comp.__esModule || comp[<span class="hljs-built_in">Symbol</span>.toStringTag] === <span class="hljs-string">'Module'</span>)
          ) &#123;
            comp = comp.default
          &#125;
          <span class="hljs-comment">// 如果在DEV环境则警告</span>
          <span class="hljs-keyword">if</span> (__DEV__ && comp && !isObject(comp) && !isFunction(comp)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Invalid async component load result: <span class="hljs-subst">$&#123;comp&#125;</span>`</span>)
          &#125;
          resolvedComp = comp
          <span class="hljs-keyword">return</span> comp
        &#125;))
    )
  &#125;

  <span class="hljs-keyword">return</span> defineComponent(&#123;
    <span class="hljs-attr">__asyncLoader</span>: load,
    <span class="hljs-comment">// 异步组件统一名字</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'AsyncComponentWrapper'</span>,
    <span class="hljs-comment">// 组件有setup方法的走setup逻辑</span>
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> instance = currentInstance!

      <span class="hljs-comment">// already resolved</span>
      <span class="hljs-keyword">if</span> (resolvedComp) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> createInnerComp(resolvedComp!, instance)
      &#125;

      <span class="hljs-keyword">const</span> onError = <span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">Error</span></span>) =></span> &#123;
        pendingRequest = <span class="hljs-literal">null</span>
        handleError(
          err,
          instance,
          ErrorCodes.ASYNC_COMPONENT_LOADER,
          !errorComponent <span class="hljs-comment">/* do not throw in dev if user provided error component */</span>
        )
      &#125;

      <span class="hljs-comment">// suspense-controlled or SSR.</span>
      <span class="hljs-comment">// 对应文档中如果父组件是一个 suspense 那么只返回promise结果 其余的控制交给 suspense 处理即可</span>
      <span class="hljs-keyword">if</span> (
        (__FEATURE_SUSPENSE__ && suspensible && instance.suspense) ||
        (__NODE_JS__ && isInSSRComponentSetup)
      ) &#123;
        <span class="hljs-keyword">return</span> load()
          .then(<span class="hljs-function"><span class="hljs-params">comp</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> createInnerComp(comp, instance)
          &#125;)
          .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            onError(err)
            <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span>
              errorComponent
                ? createVNode(errorComponent <span class="hljs-keyword">as</span> ConcreteComponent, &#123;
                    <span class="hljs-attr">error</span>: err
                  &#125;)
                : <span class="hljs-literal">null</span>
          &#125;)
      &#125;

      <span class="hljs-keyword">const</span> loaded = ref(<span class="hljs-literal">false</span>)
      <span class="hljs-keyword">const</span> error = ref()
      <span class="hljs-keyword">const</span> delayed = ref(!!delay)

      <span class="hljs-keyword">if</span> (delay) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          delayed.value = <span class="hljs-literal">false</span>
        &#125;, delay)
      &#125;

      <span class="hljs-keyword">if</span> (timeout != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (!loaded.value && !error.value) &#123;
            <span class="hljs-keyword">const</span> err = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
              <span class="hljs-string">`Async component timed out after <span class="hljs-subst">$&#123;timeout&#125;</span>ms.`</span>
            )
            onError(err)
            error.value = err
          &#125;
        &#125;, timeout)
      &#125;

      load()
        .then(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// promise成功返回后触发trigger导致组件更新 重新渲染组件 只不过此时我们已经得到组件内容</span>
          loaded.value = <span class="hljs-literal">true</span>
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          onError(err)
          error.value = err
        &#125;)

      <span class="hljs-comment">// 返回的函数会被当做组件实例的 render 函数</span>
      <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// render初始执行触发 loaded的依赖收集 </span>
        <span class="hljs-keyword">if</span> (loaded.value && resolvedComp) &#123;
          <span class="hljs-keyword">return</span> createInnerComp(resolvedComp, instance)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (error.value && errorComponent) &#123;
          <span class="hljs-keyword">return</span> createVNode(errorComponent <span class="hljs-keyword">as</span> ConcreteComponent, &#123;
            <span class="hljs-attr">error</span>: error.value
          &#125;)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (loadingComponent && !delayed.value) &#123;
          <span class="hljs-keyword">return</span> createVNode(loadingComponent <span class="hljs-keyword">as</span> ConcreteComponent)
        &#125;
      &#125;
    &#125;
  &#125;) <span class="hljs-keyword">as</span> any
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">resolveComponent</h2>
<p>官方定义：如果在当前应用实例中可用，则允许按名称解析 <code>component</code>，返回一个 <code>Component</code>。如果没有找到，则返回接收的参数 <code>name</code>。</p>
<h3 data-id="heading-15">用法</h3>
<p>参数：已加载的组件的名称</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> app = createApp(&#123;&#125;)
app.component(<span class="hljs-string">'MyComponent'</span>, &#123;
  <span class="hljs-comment">/* ... */</span>
&#125;)

<span class="hljs-keyword">import</span> &#123; resolveComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> MyComponent = resolveComponent(<span class="hljs-string">'MyComponent'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>resolveComponent()：</strong><a href="https://github.com/vuejs/vue-next/blob/51d2be20386d4dc59006d31a1cc96676871027ce/packages/runtime-core/src/helpers/resolveAssets.ts#L22" target="_blank" rel="nofollow noopener noreferrer">21行- 27行<sup> [7]</sup></a></li>
<li><strong>resolveAsset()：</strong><a href="https://github.com/vuejs/vue-next/blob/51d2be20386d4dc59006d31a1cc96676871027ce/packages/runtime-core/src/helpers/resolveAssets.ts#L22" target="_blank" rel="nofollow noopener noreferrer">62行- 123行<sup> [8]</sup></a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 接收一个name参数，主要还是在resolveAsset方法中做了处理，源码位置见上方[7]</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveComponent</span>(<span class="hljs-params">
  name: string,
  maybeSelfReference?: boolean
</span>): <span class="hljs-title">ConcreteComponent</span> | <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> resolveAsset(COMPONENTS, name, <span class="hljs-literal">true</span>, maybeSelfReference) || name
&#125;

<span class="hljs-comment">// resolveAsset源码在上方地址[8]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveAsset</span>(<span class="hljs-params">
  type: AssetTypes,
  name: string,
  warnMissing = <span class="hljs-literal">true</span>,
  maybeSelfReference = <span class="hljs-literal">false</span>
</span>) </span>&#123;
  <span class="hljs-comment">// 寻找当前渲染实例，不存在则为当前实例</span>
  <span class="hljs-keyword">const</span> instance = currentRenderingInstance || currentInstance
  <span class="hljs-keyword">if</span> (instance) &#123;
    <span class="hljs-keyword">const</span> Component = instance.type

    <span class="hljs-comment">// 自我名称具有最高的优先级</span>
    <span class="hljs-keyword">if</span> (type === COMPONENTS) &#123;
      <span class="hljs-comment">// getComponentName 首先判断传入的Component参数是不是函数，如果是函数优先使用.displayName属性，其次使用.name</span>
      <span class="hljs-keyword">const</span> selfName = getComponentName(Component)
      <span class="hljs-keyword">if</span> (
        <span class="hljs-comment">// camelize 使用replace方法，正则/-(\w)/gname，匹配后toUpperCase() 转换成大写</span>
        <span class="hljs-comment">// capitalize函数：str.charAt(0).toUpperCase() + str.slice(1) 首字母大写 + 处理后的字符</span>
        selfName &&
        (selfName === name ||
          selfName === camelize(name) ||
          selfName === capitalize(camelize(name)))
      ) &#123;
        <span class="hljs-keyword">return</span> Component
      &#125;
    &#125;

    <span class="hljs-keyword">const</span> res =
      <span class="hljs-comment">// 注册</span>
      <span class="hljs-comment">// 首先检查实例[type]，它被解析为选项API</span>
      resolve(instance[type] || (Component <span class="hljs-keyword">as</span> ComponentOptions)[type], name) ||
      <span class="hljs-comment">// 全局注册</span>
      resolve(instance.appContext[type], name)

    <span class="hljs-keyword">if</span> (!res && maybeSelfReference) &#123;
      <span class="hljs-keyword">return</span> Component
    &#125;

    <span class="hljs-keyword">if</span> (__DEV__ && warnMissing && !res) &#123;
      warn(<span class="hljs-string">`Failed to resolve <span class="hljs-subst">$&#123;type.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>)&#125;</span>: <span class="hljs-subst">$&#123;name&#125;</span>`</span>)
    &#125;

    <span class="hljs-keyword">return</span> res
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__DEV__) &#123;
    <span class="hljs-comment">// 如果实例不存在，并且在DEV环境警告：can only be used in render() or setup()</span>
    warn(
      <span class="hljs-string">`resolve<span class="hljs-subst">$&#123;capitalize(type.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>))&#125;</span> `</span> +
        <span class="hljs-string">`can only be used in render() or setup().`</span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">resolveDynamicComponent</h2>
<p>官方定义： 返回已解析的 <code>Component</code> 或新创建的 <code>VNode</code>，其中组件名称作为节点标签。如果找不到 <code>Component</code>，将发出警告。</p>
<h3 data-id="heading-18">用法</h3>
<p>参数：接受一个参数：<code>component</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; resolveDynamicComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
render () &#123;
  <span class="hljs-keyword">const</span> MyComponent = resolveDynamicComponent(<span class="hljs-string">'MyComponent'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>resolveDirective()</strong>： <a href="https://github.com/vuejs/vue-next/blob/4e3f82f6835472650741896e19fbdc116d86d1eb/packages/runtime-core/src/helpers/resolveAssets.ts#L43" target="_blank" rel="nofollow noopener noreferrer">43行 - 48行内容 <sup>[9]</sup></a></li>
<li><strong>resolveAsset()：</strong><a href="https://github.com/vuejs/vue-next/blob/51d2be20386d4dc59006d31a1cc96676871027ce/packages/runtime-core/src/helpers/resolveAssets.ts#L22" target="_blank" rel="nofollow noopener noreferrer">62行- 123行</a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码位置位于上方[9]位置处</span>
<span class="hljs-comment">// 根据该函数的名称，我们可以知道它用于解析动态组件,在 resolveDynamicComponent 函数内部，若 component 参数是字符串类型，则会调用前面介绍的 resolveAsset 方法来解析组件,</span>
<span class="hljs-comment">// 如果 resolveAsset 函数获取不到对应的组件，则会返回当前 component 参数的值。比如 resolveDynamicComponent('div') 将返回 'div' 字符串</span>
<span class="hljs-comment">// 源码见上方[1]地址</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveDynamicComponent</span>(<span class="hljs-params">component: unknown</span>): <span class="hljs-title">VNodeTypes</span> </span>&#123;
  <span class="hljs-keyword">if</span> (isString(component)) &#123;
    <span class="hljs-keyword">return</span> resolveAsset(COMPONENTS, component, <span class="hljs-literal">false</span>) || component
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 无效类型将引发警告,如果 component 参数非字符串类型，则会返回 component || NULL_DYNAMIC_COMPONENT 这行语句的执行结果，其中 NULL_DYNAMIC_COMPONENT 的值是一个 Symbol 对象。</span>
    <span class="hljs-keyword">return</span> (component || NULL_DYNAMIC_COMPONENT) <span class="hljs-keyword">as</span> any
  &#125;
&#125;

<span class="hljs-comment">//  resolveAsset函数解析见上方[8]位置处</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">resolveDirective</h2>
<p>如果在当前应用实例中可用，则允许通过其名称解析一个 <code>directive</code>。返回一个 <code>Directive</code>。如果没有找到，则返回 <code>undefined</code>。</p>
<h3 data-id="heading-21">用法</h3>
<ul>
<li>第一个参数：已加载的指令的名称。</li>
</ul>
<h3 data-id="heading-22">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>resolveDirective()</strong>： <a href="https://github.com/vuejs/vue-next/blob/4e3f82f6835472650741896e19fbdc116d86d1eb/packages/runtime-core/src/helpers/resolveAssets.ts#L43" target="_blank" rel="nofollow noopener noreferrer">43行 - 48行内容 <sup>[10]</sup></a></li>
<li><strong>resolveAsset()：</strong><a href="https://github.com/vuejs/vue-next/blob/51d2be20386d4dc59006d31a1cc96676871027ce/packages/runtime-core/src/helpers/resolveAssets.ts#L62" target="_blank" rel="nofollow noopener noreferrer">62行- 123行 </a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 源码位置见上方[10]位置处
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveDirective</span>(<span class="hljs-params">name: string</span>): <span class="hljs-title">Directive</span> | <span class="hljs-title">undefined</span> </span>&#123;
  <span class="hljs-comment">// 然后调用前面介绍的 resolveAsset 方法来解析组件,resolveAsset函数解析见上方[8]位置处</span>
  <span class="hljs-keyword">return</span> resolveAsset(DIRECTIVES, name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">withDirectives</h2>
<p>官方定义：允许将指令应用于 <strong>VNode</strong>。返回一个包含应用指令的 VNode。</p>
<h3 data-id="heading-24">用法</h3>
<ul>
<li>
<p>第一个参数：一个虚拟节点，通常使用 <code>h()</code> 创建</p>
</li>
<li>
<p>第二个参数：一个指令数组，每个指令本身都是一个数组，最多可以定义 4 个索引。</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; withDirectives, resolveDirective &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> foo = resolveDirective(<span class="hljs-string">'foo'</span>)
<span class="hljs-keyword">const</span> bar = resolveDirective(<span class="hljs-string">'bar'</span>)

<span class="hljs-keyword">return</span> withDirectives(h(<span class="hljs-string">'div'</span>), [
  [foo, <span class="hljs-built_in">this</span>.x],
  [bar, <span class="hljs-built_in">this</span>.y]
])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>resolveDirective()</strong>： <a href="https://github.com/vuejs/vue-next/blob/ff50e8d78c033252c4ce7ffddb8069b3ddae5936/packages/runtime-core/src/directives.ts#L85" target="_blank" rel="nofollow noopener noreferrer">85行 - 114内容 <sup>[11]</sup></a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码链接在上方[11]位置处</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">withDirectives</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">VNode</span>>(<span class="hljs-params">
  vnode: T,
  directives: DirectiveArguments
</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-comment">// 获取当前实例</span>
  <span class="hljs-keyword">const</span> internalInstance = currentRenderingInstance
  <span class="hljs-keyword">if</span> (internalInstance === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 如果在 render 函数外面使用 withDirectives() 则会抛出异常：</span>
    __DEV__ && warn(<span class="hljs-string">`withDirectives can only be used inside render functions.`</span>)
    <span class="hljs-keyword">return</span> vnode
  &#125;
  <span class="hljs-keyword">const</span> instance = internalInstance.proxy
  <span class="hljs-comment">// 在 vnode 上绑定 dirs 属性，并且遍历传入的 directives 数组</span>
  <span class="hljs-keyword">const</span> bindings: DirectiveBinding[] = vnode.dirs || (vnode.dirs = [])
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < directives.length; i++) &#123;
    <span class="hljs-keyword">let</span> [dir, value, arg, modifiers = EMPTY_OBJ] = directives[i]
    <span class="hljs-keyword">if</span> (isFunction(dir)) &#123;
      dir = &#123;
        <span class="hljs-attr">mounted</span>: dir,
        <span class="hljs-attr">updated</span>: dir
      &#125; <span class="hljs-keyword">as</span> ObjectDirective
    &#125;
    bindings.push(&#123;
      dir,
      instance,
      value,
      <span class="hljs-attr">oldValue</span>: <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>,
      arg,
      modifiers
    &#125;)
  &#125;
  <span class="hljs-keyword">return</span> vnode
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">createRenderer</h2>
<p>官方定义：createRenderer 函数接受两个泛型参数： <code>HostNode</code> 和 <code>HostElement</code>，对应于宿主环境中的 Node 和 Element 类型。</p>
<h3 data-id="heading-27">用法</h3>
<ul>
<li>第一个参数：HostNode宿主环境中的节点。</li>
<li>第二个参数：Element宿主环境中的元素。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 对于 runtime-dom，HostNode 将是 DOM Node 接口，HostElement 将是 DOM Element 接口。</span>
<span class="hljs-comment">// 自定义渲染器可以传入特定于平台的类型，如下所示：</span>

<span class="hljs-comment">// createRenderer(HostNode, HostElement),两个通用参数HostNode(主机环境中的节点)和HostElement(宿主环境中的元素)，对应于宿主环境。</span>
<span class="hljs-comment">// reateRenderer(使用（可选的）选项创建一个 Renderer 实例。),该方法返回了 baseCreateRenderer</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRenderer</span><
  <span class="hljs-title">HostNode</span> = <span class="hljs-title">RendererNode</span>,
  <span class="hljs-title">HostElement</span> = <span class="hljs-title">RendererElement</span>
>(<span class="hljs-params">options: RendererOptions<HostNode, HostElement></span>) </span>&#123;
  <span class="hljs-keyword">return</span> baseCreateRenderer<HostNode, HostElement>(options)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">源码解析</h3>
<ul>
<li><strong>createRenderer（）</strong>：<a href="https://github.com/vuejs/vue-next/blob/ef5c41523f98dbb9c26700fa3b987a2fae26b4e1/packages/runtime-core/src/renderer.ts#L419" target="_blank" rel="nofollow noopener noreferrer">419 行- 424行内容 <sup>[3]</sup></a></li>
<li><strong>baseCreateRenderer()</strong>：<a href="https://github.com/vuejs/vue-next/blob/b0203a30929e4e7f59e035574e43d72ed3b9d7fd/packages/runtime-core/src/renderer.ts#L448" target="_blank" rel="nofollow noopener noreferrer">448 行- 2418行 <sup>[4]</sup></a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRenderer</span><
  <span class="hljs-title">HostNode</span> = <span class="hljs-title">RendererNode</span>,
  <span class="hljs-title">HostElement</span> = <span class="hljs-title">RendererElement</span>
>(<span class="hljs-params">options: RendererOptions<HostNode, HostElement></span>) </span>&#123;
  <span class="hljs-keyword">return</span> baseCreateRenderer<HostNode, HostElement>(options)
&#125;

<span class="hljs-comment">// baseCreateRenderer这个放2000行的左右的代码量，这里就完整不贴过来了，里面是渲染的核心代码，从平台特性 options 取出相关 API，实现了 patch、处理节点、处理组件、更新组件、安装组件实例等等方法，最终返回了一个renderer对象。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?: <span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-comment">// compile-time feature flags check</span>
  <span class="hljs-keyword">if</span> (__ESM_BUNDLER__ && !__TEST__) &#123;
    initFeatureFlags()
  &#125;

  <span class="hljs-keyword">if</span> (__DEV__ || __FEATURE_PROD_DEVTOOLS__) &#123;
    <span class="hljs-keyword">const</span> target = getGlobalThis()
    target.__VUE__ = <span class="hljs-literal">true</span>
    setDevtoolsHook(target.__VUE_DEVTOOLS_GLOBAL_HOOK__)
  &#125;

  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">insert</span>: hostInsert,
    <span class="hljs-attr">remove</span>: hostRemove,
    <span class="hljs-attr">patchProp</span>: hostPatchProp,
    <span class="hljs-attr">forcePatchProp</span>: hostForcePatchProp,
    <span class="hljs-attr">createElement</span>: hostCreateElement,
    <span class="hljs-attr">createText</span>: hostCreateText,
    <span class="hljs-attr">createComment</span>: hostCreateComment,
    <span class="hljs-attr">setText</span>: hostSetText,
    <span class="hljs-attr">setElementText</span>: hostSetElementText,
    <span class="hljs-attr">parentNode</span>: hostParentNode,
    <span class="hljs-attr">nextSibling</span>: hostNextSibling,
    <span class="hljs-attr">setScopeId</span>: hostSetScopeId = NOOP,
    <span class="hljs-attr">cloneNode</span>: hostCloneNode,
    <span class="hljs-attr">insertStaticContent</span>: hostInsertStaticContent
  &#125; = options
...
...
    ...
  <span class="hljs-comment">// 返回 render hydrate createApp三个函数，生成的 render 传给 createAppAPI ，hydrate 为可选参数，ssr 的场景下会用到；</span>
  <span class="hljs-keyword">return</span> &#123;
    render,
    hydrate,
    <span class="hljs-attr">createApp</span>: createAppAPI(render, hydrate)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">nextTick</h2>
<p>官方定义：将回调推迟到下一个 DOM 更新周期之后执行。在更改了一些数据以等待 DOM 更新后立即使用它。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp, nextTick &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> app = createApp(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> message = ref(<span class="hljs-string">'Hello!'</span>)
    <span class="hljs-keyword">const</span> changeMessage = <span class="hljs-keyword">async</span> newMessage => &#123;
      message.value = newMessage
      <span class="hljs-keyword">await</span> nextTick()
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Now DOM is updated'</span>)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>nextTick()</strong>： <a href="https://github.com/vuejs/vue-next/blob/03a7a73148a9e210a7889c7a2ecf925338735c70/packages/runtime-core/src/scheduler.ts#L42" target="_blank" rel="nofollow noopener noreferrer">42行 - 48行内容</a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码位置在上方</span>

<span class="hljs-comment">// 这里直接创建一个异步任务，但是改变dom属性也是异步策略，怎么保证dom加载完成</span>
<span class="hljs-comment">// Vue2.x是 会判断浏览器是否支持promise属性 -> 是否支持MutationObserver -> 是否支持setImmediate  -> 都不支持使用setTimeout，Vue3不再支持IE11，所以nextTick直接使用Promise</span>

<span class="hljs-comment">// Vue 异步执行 DOM 更新。只要观察到数据变化，Vue 将开启一个队列，并缓冲在同一事件循环中发生的所有数据改变。如果同一个 watcher 被多次触发，只会被推入到队列中一次。这种在缓冲时去除重复数据对于避免不必要的计算和 DOM 操作上非常重要。然后，在下一个的事件循环“tick”中，Vue 刷新队列并执行实际 (已去重的) 工作。</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextTick</span>(<span class="hljs-params">
  <span class="hljs-built_in">this</span>: ComponentPublicInstance | <span class="hljs-keyword">void</span>,
  fn?: () => <span class="hljs-keyword">void</span>
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">void</span>> </span>&#123;
  <span class="hljs-keyword">const</span> p = currentFlushPromise || resolvedPromise
  <span class="hljs-keyword">return</span> fn ? p.then(<span class="hljs-built_in">this</span> ? fn.bind(<span class="hljs-built_in">this</span>) : fn) : p
&#125;

<span class="hljs-comment">// 你设置vm.someData = 'new value'，该组件不会立即重新渲染。当刷新队列时，组件会在事件循环队列清空时的下一个“tick”更新。如果你想在 DOM 状态更新后做点什 ，可以在数据变化之后立即使用Vue.nextTick(callback) 。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">mergeProps</h2>
<p>官方定义： 将包含 VNode prop 的多个对象合并为一个单独的对象。其返回的是一个新创建的对象，而作为参数传递的对象则不会被修改。</p>
<h3 data-id="heading-32">用法</h3>
<p>参数： 可以传递不限数量的对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; h, mergeProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> props = mergeProps(&#123;
      <span class="hljs-comment">// 该 class 将与 $attrs 中的其他 class 合并。</span>
      <span class="hljs-attr">class</span>: <span class="hljs-string">'active'</span>
    &#125;, <span class="hljs-built_in">this</span>.$attrs)
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, props)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">源码浅析</h3>
<p>GitHub地址：</p>
<ul>
<li><strong>mergeProps()</strong>： <a href="https://github.com/vuejs/vue-next/blob/32e21333dd1197a978cf42802729b2133bda5a0b/packages/runtime-core/src/vnode.ts#L687" target="_blank" rel="nofollow noopener noreferrer">687行 - 712行 </a></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeProps</span>(<span class="hljs-params">...args: (Data & VNodeProps)[]</span>) </span>&#123;
  <span class="hljs-comment">// extend就是Object.assign方法， ret合并第一个参数为对象</span>
  <span class="hljs-keyword">const</span> ret = extend(&#123;&#125;, args[<span class="hljs-number">0</span>])
  <span class="hljs-comment">// 遍历args参数</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < args.length; i++) &#123;
    <span class="hljs-keyword">const</span> toMerge = args[i]
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> toMerge) &#123;
      <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'class'</span>) &#123;
        <span class="hljs-comment">// 合并class</span>
        <span class="hljs-keyword">if</span> (ret.class !== toMerge.class) &#123;
          ret.class = normalizeClass([ret.class, toMerge.class])
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'style'</span>) &#123;
        <span class="hljs-comment">// 合并style</span>
        ret.style = normalizeStyle([ret.style, toMerge.style])
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isOn(key)) &#123;、
      <span class="hljs-comment">// 判断是不是以 on开头的</span>
        <span class="hljs-keyword">const</span> existing = ret[key]
        <span class="hljs-keyword">const</span> incoming = toMerge[key]
        <span class="hljs-keyword">if</span> (existing !== incoming) &#123;
          <span class="hljs-comment">// 如果第一个参数中不存在,则合并，否则新增</span>
          ret[key] = existing
            ? [].concat(existing <span class="hljs-keyword">as</span> any, incoming <span class="hljs-keyword">as</span> any)
            : incoming
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key !== <span class="hljs-string">''</span>) &#123;
        <span class="hljs-comment">// key不为空则添加属性</span>
        ret[key] = toMerge[key]
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> ret
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">useCssModule</h2>
<p>官方定义：允许在 <a href="https://v3.cn.vuejs.org/api/composition-api.html#setup" target="_blank" rel="nofollow noopener noreferrer"><code>setup</code></a> 的<a href="https://v3.cn.vuejs.org/guide/single-file-component.html" target="_blank" rel="nofollow noopener noreferrer">单文件组件</a>函数中访问 CSS 模块。</p>
<h3 data-id="heading-35">用法</h3>
<ul>
<li>参数：CSS 模块的名称。默认为 <code>'$style'</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// useCssModule 只能在 render 或 setup 函数中使用。</span>
<span class="hljs-comment">// 这里的name不止可以填写$style,</span>
<span class="hljs-comment">/*
*<style module="aaa"
* ...
*</style>
*/</span>
<span class="hljs-comment">// 这样就可以使用 const style = useCssModule(‘aaa'),来获取相应内容</span>

<script>
<span class="hljs-keyword">import</span> &#123; h, useCssModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> style = useCssModule()
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> h(<span class="hljs-string">'div'</span>, &#123;
      <span class="hljs-attr">class</span>: style.success
    &#125;, <span class="hljs-string">'Task complete!'</span>)
  &#125;
&#125;
</script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">module</span>></span><span class="css">
<span class="hljs-selector-class">.success</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#090</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="hljs-comment">// 在 <style> 上添加 module 后， $style的计算属性就会被自动注入组件。</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">module</span>></span><span class="css">
<span class="hljs-selector-class">.six</span>
 <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-class">.one</span>
 <span class="hljs-attribute">font-size</span>:<span class="hljs-number">62px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="hljs-comment">// 添加model后可以直接使用$style绑定属性</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"$style.red"</span>></span>
   hello red!
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">源码解析</h3>
<p>GitHub地址：</p>
<p><strong>useCssModule()</strong>： <a href="https://github.com/vuejs/vue-next/blob/870f2a7ba35245fd8c008d2ff666ea130a7e4704/packages/runtime-dom/src/helpers/useCssModule.ts" target="_blank" rel="nofollow noopener noreferrer">1行 - 30行 </a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; warn, getCurrentInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/runtime-core'</span>
<span class="hljs-keyword">import</span> &#123; EMPTY_OBJ &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/shared'</span>

<span class="hljs-comment">// 取出 this.$style </span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCssModule</span>(<span class="hljs-params">name = <span class="hljs-string">'$style'</span></span>): <span class="hljs-title">Record</span><<span class="hljs-title">string</span>, <span class="hljs-title">string</span>> </span>&#123;
  <span class="hljs-comment">/* 如果是istanbul覆盖率测试则跳出 */</span>
  <span class="hljs-keyword">if</span> (!__GLOBAL__) &#123;
    <span class="hljs-comment">// 获取当前实例</span>
    <span class="hljs-keyword">const</span> instance = getCurrentInstance()!
    <span class="hljs-keyword">if</span> (!instance) &#123;
      <span class="hljs-comment">// useCssModule 只能在 render 或 setup 函数中使用。</span>
      __DEV__ && warn(<span class="hljs-string">`useCssModule must be called inside setup()`</span>)
      <span class="hljs-comment">// EMPTY_OBJ是使用Object.freeze()冻结对象</span>
      <span class="hljs-keyword">return</span> EMPTY_OBJ
    &#125;
    <span class="hljs-keyword">const</span> modules = instance.type.__cssModules
    <span class="hljs-comment">// 如果不存在css模块，警告</span>
    <span class="hljs-keyword">if</span> (!modules) &#123;
      __DEV__ && warn(<span class="hljs-string">`Current instance does not have CSS modules injected.`</span>)
      <span class="hljs-keyword">return</span> EMPTY_OBJ
    &#125;
    <span class="hljs-keyword">const</span> mod = modules[name]
    <span class="hljs-comment">// 如果不存在未找到name的css模块，警告</span>
    <span class="hljs-keyword">if</span> (!mod) &#123;
      __DEV__ &&
        warn(<span class="hljs-string">`Current instance does not have CSS module named "<span class="hljs-subst">$&#123;name&#125;</span>".`</span>)
      <span class="hljs-keyword">return</span> EMPTY_OBJ
    &#125;
    <span class="hljs-keyword">return</span> mod <span class="hljs-keyword">as</span> Record<string, string>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      warn(<span class="hljs-string">`useCssModule() is not supported in the global build.`</span>)
    &#125;
    <span class="hljs-keyword">return</span> EMPTY_OBJ
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">version</h2>
<p>官方定义： 以字符串形式提供已安装的 Vue 的版本号。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue-next/packages/vue/package.json 中的version 为3.1.2，使用.split('.')[0]，得出3</span>
<span class="hljs-keyword">const</span> version = <span class="hljs-built_in">Number</span>(Vue.version.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>])
<span class="hljs-keyword">if</span> (version === <span class="hljs-number">3</span>) &#123;
  <span class="hljs-comment">// Vue 3</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (version === <span class="hljs-number">2</span>) &#123;
  <span class="hljs-comment">// Vue 2</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 不支持的 Vue 的版本</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-38">参考资料</h1>
<p><a href="https://github.com/vuejs/vue-next/" target="_blank" rel="nofollow noopener noreferrer">Vue-next-GitHub</a></p>
<p><a href="https://cn.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">Vue3官方文档</a></p>
<p><a href="https://github.com/shengxinjing/vue3-book" target="_blank" rel="nofollow noopener noreferrer">Vue3源码分析</a></p>
<p><a href="https://00feng00.github.io/2021/03/03/vue3VNode/" target="_blank" rel="nofollow noopener noreferrer">vue3 VNode</a></p>
<h1 data-id="heading-39">结尾</h1>
<p>好了，以上就是本篇全部文章内容啦。</p>
<p>如果遇到问题或者有其他意见可以在下方评论区贴出！</p>
<p>码字不易。如果觉得本篇文章对你有帮助的话，希望你可以留言点赞支持一下，非常感谢~</p></div>  
</div>
            