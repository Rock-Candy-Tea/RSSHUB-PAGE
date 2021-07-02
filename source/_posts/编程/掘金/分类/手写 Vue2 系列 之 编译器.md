
---
title: '手写 Vue2 系列 之 编译器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b37a56386143ea8d0b6cbe3d8d0f42~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 17:09:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b37a56386143ea8d0b6cbe3d8d0f42~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>接下来就要正式进入手写 Vue2 系列了。这里不会从零开始，会基于 <code>lyn-vue</code> 直接进行升级，所以如果你没有阅读过 <a href="https://juejin.cn/post/6977152988678733855" target="_blank">手写 Vue 系列 之 Vue1.x</a>，请先从这篇文章开始，按照顺序进行学习。</p>
<p>都知道，Vue1 存在的问题就是在大型应用中 Watcher 太多，如果不清楚其原理请查看 <a href="https://juejin.cn/post/6977152988678733855" target="_blank">手写 Vue 系列 之 Vue1.x</a>。</p>
<p>所以在 Vue2 中通过引入了 VNode 和 diff 算法来解决该问题。通过降低 Watcher 的粒度，一个组件对应一个 Watcher（渲染 Watcher），这样就不会出现大型页面 Watcher 太多导致性能下降的问题。</p>
<p>在 Vue1 中，Watcher 和 页面中的响应式数据一一对应，当响应式数据发生改变，Dep 通知 Watcher 完成对应的 DOM 更新。但是在 Vue2 中一个组件对应一个 Watcher，当响应式数据发生改变时，Watcher 并不知道这个响应式数据在组件中的什么位置，那又该如何完成更新呢？</p>
<p>阅读过之前的 <a href="https://juejin.cn/column/6960553066101735461" target="_blank">源码系列</a>，大家肯定都知道，Vue2 引入了 VNode 和 diff 算法，将组件 <strong>编译</strong> 成 VNode，每次响应式数据发生变化时，会生成新的 VNode，通过 diff 算法对比新旧 VNode，找出其中发生改变的地方，然后执行对应的 DOM 操作完成更新。</p>
<p>所以，到这里大家也能明白，Vue1 和 Vue2 在核心的数据响应式部分其实没什么变化，主要的变动在编译器部分。</p>
<h1 data-id="heading-1">目标</h1>
<p>完成 Vue2 编译器的一个简版实现，从字符串模版解析开始，到最终得到 <code>render</code> 函数。</p>
<h1 data-id="heading-2">编译器</h1>
<p>在手写 Vue1 时，编译器时通过 DOM API 来遍历模版的 DOM 结构来完成的，在 Vue2 中不再使用这种方式，而是和官方一样，直接编译组件的模版字符串，生成 AST，然后从 AST 生成渲染函数。</p>
<p>首先将 Vue1 的 compiler 目录备份，然后新建一个 compiler 目录，作为 Vue2 的编译器目录</p>
<pre><code class="hljs language-shell copyable" lang="shell">mv compiler compiler-vue1 && mkdir compiler
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">mount</h2>
<blockquote>
<p>/src/compiler/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 编译器
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!vm.$options.render) &#123; <span class="hljs-comment">// 没有提供 render 选项，则编译生成 render 函数</span>
    <span class="hljs-comment">// 获取模版</span>
    <span class="hljs-keyword">let</span> template = <span class="hljs-string">''</span>

    <span class="hljs-keyword">if</span> (vm.$options.template) &#123;
      <span class="hljs-comment">// 模版存在</span>
      template = vm.$options.template
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      <span class="hljs-comment">// 存在挂载点</span>
      template = <span class="hljs-built_in">document</span>.querySelector(vm.$options.el).outerHTML
      <span class="hljs-comment">// 在实例上记录挂载点，this._update 中会用到</span>
      vm.$el = <span class="hljs-built_in">document</span>.querySelector(vm.$options.el)
    &#125;

    <span class="hljs-comment">// 生成渲染函数</span>
    <span class="hljs-keyword">const</span> render = compileToFunction(template)
    <span class="hljs-comment">// 将渲染函数挂载到 $options 上</span>
    vm.$options.render = render
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">compileToFunction</h3>
<blockquote>
<p>/src/compiler/compileToFunction.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析模版字符串，得到 AST 语法树
 * 将 AST 语法树生成渲染函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123; String &#125;</span> </span>template 模版字符串
 * <span class="hljs-doctag">@returns </span>渲染函数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compileToFunction</span>(<span class="hljs-params">template</span>) </span>&#123;
  <span class="hljs-comment">// 解析模版，生成 ast</span>
  <span class="hljs-keyword">const</span> ast = parse(template)
  <span class="hljs-comment">// 将 ast 生成渲染函数</span>
  <span class="hljs-keyword">const</span> render = generate(ast)
  <span class="hljs-keyword">return</span> render
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">parse</h2>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析模版字符串，生成 AST 语法树
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>template 模版字符串
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;AST&#125;</span> </span>root ast 语法树
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parse</span>(<span class="hljs-params">template</span>) </span>&#123;
  <span class="hljs-comment">// 存放所有的未配对的开始标签的 AST 对象</span>
  <span class="hljs-keyword">const</span> stack = []
  <span class="hljs-comment">// 最终的 AST 语法树</span>
  <span class="hljs-keyword">let</span> root = <span class="hljs-literal">null</span>

  <span class="hljs-keyword">let</span> html = template
  <span class="hljs-keyword">while</span> (html.trim()) &#123;
    <span class="hljs-comment">// 过滤注释标签</span>
    <span class="hljs-keyword">if</span> (html.indexOf(<span class="hljs-string">'<!--'</span>) === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 说明开始位置是一个注释标签，忽略掉</span>
      html = html.slice(html.indexOf(<span class="hljs-string">'-->'</span>) + <span class="hljs-number">3</span>)
      <span class="hljs-keyword">continue</span>
    &#125;
    <span class="hljs-comment">// 匹配开始标签</span>
    <span class="hljs-keyword">const</span> startIdx = html.indexOf(<span class="hljs-string">'<'</span>)
    <span class="hljs-keyword">if</span> (startIdx === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">if</span> (html.indexOf(<span class="hljs-string">'</'</span>) === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 说明是闭合标签</span>
        parseEnd()
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 处理开始标签</span>
        parseStartTag()
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (startIdx > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 说明在开始标签之间有一段文本内容，在 html 中找到下一个标签的开始位置</span>
      <span class="hljs-keyword">const</span> nextStartIdx = html.indexOf(<span class="hljs-string">'<'</span>)
      <span class="hljs-comment">// 如果栈为空，则说明这段文本不属于任何一个元素，直接丢掉，不做处理</span>
      <span class="hljs-keyword">if</span> (stack.length) &#123;
        <span class="hljs-comment">// 走到这里说说明栈不为空，则处理这段文本，并将其放到栈顶元素的肚子里</span>
        processChars(html.slice(<span class="hljs-number">0</span>, nextStartIdx))
      &#125;
      html = html.slice(nextStartIdx)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 说明没有匹配到开始标签，整个 html 就是一段文本</span>
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> root
  
  <span class="hljs-comment">// parseStartTag 函数的声明</span>
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// processElement 函数的声明</span>
&#125;

<span class="hljs-comment">// processVModel 函数的声明</span>
<span class="hljs-comment">// ...</span>
<span class="hljs-comment">// processVOn 函数的声明</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">parseStartTag</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析开始标签
 * 比如： <div id="app">...</div>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseStartTag</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 先找到开始标签的结束位置 ></span>
  <span class="hljs-keyword">const</span> end = html.indexOf(<span class="hljs-string">'>'</span>)
  <span class="hljs-comment">// 解析开始标签里的内容 <内容>，标签名 + 属性，比如: div id="app"</span>
  <span class="hljs-keyword">const</span> content = html.slice(<span class="hljs-number">1</span>, end)
  <span class="hljs-comment">// 截断 html，将上面解析的内容从 html 字符串中删除</span>
  html = html.slice(end + <span class="hljs-number">1</span>)
  <span class="hljs-comment">// 找到 第一个空格位置</span>
  <span class="hljs-keyword">const</span> firstSpaceIdx = content.indexOf(<span class="hljs-string">' '</span>)
  <span class="hljs-comment">// 标签名和属性字符串</span>
  <span class="hljs-keyword">let</span> tagName = <span class="hljs-string">''</span>, attrsStr = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (firstSpaceIdx === -<span class="hljs-number">1</span>) &#123;
    <span class="hljs-comment">// 没有空格，则认为 content 就是标签名，比如 <h3></h3> 这种情况，content = h3</span>
    tagName = content
    <span class="hljs-comment">// 没有属性</span>
    attrsStr = <span class="hljs-string">''</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    tagName = content.slice(<span class="hljs-number">0</span>, firstSpaceIdx)
    <span class="hljs-comment">// content 的剩下的内容就都是属性了，比如 id="app" xx=xx</span>
    attrsStr = content.slice(firstSpaceIdx + <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-comment">// 得到属性数组，[id="app", xx=xx]</span>
  <span class="hljs-keyword">const</span> attrs = attrsStr ? attrsStr.split(<span class="hljs-string">' '</span>) : []
  <span class="hljs-comment">// 进一步解析属性数组，得到一个 Map 对象</span>
  <span class="hljs-keyword">const</span> attrMap = parseAttrs(attrs)
  <span class="hljs-comment">// 生成 AST 对象</span>
  <span class="hljs-keyword">const</span> elementAst = generateAST(tagName, attrMap)
  <span class="hljs-comment">// 如果根节点不存在，说明当前节点为整个模版的第一个节点</span>
  <span class="hljs-keyword">if</span> (!root) &#123;
    root = elementAst
  &#125;
  <span class="hljs-comment">// 将 ast 对象 push 到栈中，当遇到结束标签的时候就将栈顶的 ast 对象 pop 出来，它两就是一对儿</span>
  stack.push(elementAst)

  <span class="hljs-comment">// 自闭合标签，则直接调用 end 方法，进入闭合标签的处理截断，就不入栈了</span>
  <span class="hljs-keyword">if</span> (isUnaryTag(tagName)) &#123;
    processElement()
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">parseEnd</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理结束标签，比如: <div id="app">...</div>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseEnd</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 将结束标签从 html 字符串中截掉</span>
  html = html.slice(html.indexOf(<span class="hljs-string">'>'</span>) + <span class="hljs-number">1</span>)
  <span class="hljs-comment">// 处理栈顶元素</span>
  processElement()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">parseAttrs</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析属性数组，得到一个属性 和 值组成的 Map 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attrs 属性数组，[id="app", xx="xx"]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseAttrs</span>(<span class="hljs-params">attrs</span>) </span>&#123;
  <span class="hljs-keyword">const</span> attrMap = &#123;&#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = attrs.length; i < len; i++) &#123;
    <span class="hljs-keyword">const</span> attr = attrs[i]
    <span class="hljs-keyword">const</span> [attrName, attrValue] = attr.split(<span class="hljs-string">'='</span>)
    attrMap[attrName] = attrValue.replace(<span class="hljs-regexp">/"/g</span>, <span class="hljs-string">''</span>)
  &#125;
  <span class="hljs-keyword">return</span> attrMap
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">generateAST</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成 AST 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>tagName 标签名
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attrMap 标签组成的属性 map 对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateAST</span>(<span class="hljs-params">tagName, attrMap</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 元素节点</span>
    <span class="hljs-attr">type</span>: <span class="hljs-number">1</span>,
    <span class="hljs-comment">// 标签</span>
    <span class="hljs-attr">tag</span>: tagName,
    <span class="hljs-comment">// 原始属性 map 对象，后续还需要进一步处理</span>
    <span class="hljs-attr">rawAttr</span>: attrMap,
    <span class="hljs-comment">// 子节点</span>
    <span class="hljs-attr">children</span>: [],
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">processChars</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理文本
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>text 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processChars</span>(<span class="hljs-params">text</span>) </span>&#123;
  <span class="hljs-comment">// 去除空字符或者换行符的情况</span>
  <span class="hljs-keyword">if</span> (!text.trim()) <span class="hljs-keyword">return</span>

  <span class="hljs-comment">// 构造文本节点的 AST 对象</span>
  <span class="hljs-keyword">const</span> textAst = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-number">3</span>,
    text,
  &#125;
  <span class="hljs-keyword">if</span> (text.match(<span class="hljs-regexp">/&#123;&#123;(.*)&#125;&#125;/</span>)) &#123;
    <span class="hljs-comment">// 说明是表达式</span>
    textAst.expression = <span class="hljs-built_in">RegExp</span>.$1.trim()
  &#125;
  <span class="hljs-comment">// 将 ast 放到栈顶元素的肚子里</span>
  stack[stack.length - <span class="hljs-number">1</span>].children.push(textAst)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">processElement</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理元素的闭合标签时会调用该方法
 * 进一步处理元素上的各个属性，将处理结果放到 attr 属性上
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processElement</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 弹出栈顶元素，进一步处理该元素</span>
  <span class="hljs-keyword">const</span> curEle = stack.pop()
  <span class="hljs-keyword">const</span> stackLen = stack.length
  <span class="hljs-comment">// 进一步处理 AST 对象中的 rawAttr 对象 &#123; attrName: attrValue, ... &#125;</span>
  <span class="hljs-keyword">const</span> &#123; tag, rawAttr &#125; = curEle
  <span class="hljs-comment">// 处理结果都放到 attr 对象上，并删掉 rawAttr 对象中相应的属性</span>
  curEle.attr = &#123;&#125;
  <span class="hljs-comment">// 属性对象的 key 组成的数组</span>
  <span class="hljs-keyword">const</span> propertyArr = <span class="hljs-built_in">Object</span>.keys(rawAttr)

  <span class="hljs-keyword">if</span> (propertyArr.includes(<span class="hljs-string">'v-model'</span>)) &#123;
    <span class="hljs-comment">// 处理 v-model 指令</span>
    processVModel(curEle)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propertyArr.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.match(<span class="hljs-regexp">/^v-bind:(.*)/</span>))) &#123;
    <span class="hljs-comment">// 处理 v-bind 指令，比如 <span v-bind:test="xx" /></span>
    processVBind(curEle, <span class="hljs-built_in">RegExp</span>.$1, rawAttr[<span class="hljs-string">`v-bind:<span class="hljs-subst">$&#123;<span class="hljs-built_in">RegExp</span>.$<span class="hljs-number">1</span>&#125;</span>`</span>])
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propertyArr.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.match(<span class="hljs-regexp">/^v-on:(.*)/</span>))) &#123;
    <span class="hljs-comment">// 处理 v-on 指令，比如 <button v-on:click="add"> add </button></span>
    processVOn(curEle, <span class="hljs-built_in">RegExp</span>.$1, rawAttr[<span class="hljs-string">`v-on:<span class="hljs-subst">$&#123;<span class="hljs-built_in">RegExp</span>.$<span class="hljs-number">1</span>&#125;</span>`</span>])
  &#125;

  <span class="hljs-comment">// 节点处理完以后让其和父节点产生关系</span>
  <span class="hljs-keyword">if</span> (stackLen) &#123;
    stack[stackLen - <span class="hljs-number">1</span>].children.push(curEle)
    curEle.parent = stack[stackLen - <span class="hljs-number">1</span>]
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">processVModel</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 v-model 指令，将处理结果直接放到 curEle 对象身上
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>curEle 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processVModel</span>(<span class="hljs-params">curEle</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; tag, rawAttr, attr &#125; = curEle
  <span class="hljs-keyword">const</span> &#123; type, <span class="hljs-string">'v-model'</span>: vModelVal &#125; = rawAttr

  <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'input'</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/text/</span>.test(type)) &#123;
      <span class="hljs-comment">// <input type="text" v-model="inputVal" /></span>
      attr.vModel = &#123; tag, <span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>, <span class="hljs-attr">value</span>: vModelVal &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/checkbox/</span>.test(type)) &#123;
      <span class="hljs-comment">// <input type="checkbox" v-model="isChecked" /></span>
      attr.vModel = &#123; tag, <span class="hljs-attr">type</span>: <span class="hljs-string">'checkbox'</span>, <span class="hljs-attr">value</span>: vModelVal &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'textarea'</span>) &#123;
    <span class="hljs-comment">// <textarea v-model="test" /></span>
    attr.vModel = &#123; tag, <span class="hljs-attr">value</span>: vModelVal &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'select'</span>) &#123;
    <span class="hljs-comment">// <select v-model="selectedValue">...</select></span>
    attr.vModel = &#123; tag, <span class="hljs-attr">value</span>: vModelVal &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">processVBind</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 v-bind 指令
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>curEle 当前正在处理的 AST 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>bindKey v-bind:key 中的 key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>bindVal v-bind:key = val 中的 val
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processVBind</span>(<span class="hljs-params">curEle, bindKey, bindVal</span>) </span>&#123;
  curEle.attr.vBind = &#123; [bindKey]: bindVal &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">processVOn</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 v-on 指令
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>curEle 当前被处理的 AST 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vOnKey v-on:key 中的 key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vOnVal v-on:key="val" 中的 val
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processVOn</span>(<span class="hljs-params">curEle, vOnKey, vOnVal</span>) </span>&#123;
  curEle.attr.vOn = &#123; [vOnKey]: vOnVal &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">isUnaryTag</h3>
<blockquote>
<p>/src/utils.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 是否为自闭合标签，内置一些自闭合标签，为了处理简单
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isUnaryTag</span>(<span class="hljs-params">tagName</span>) </span>&#123;
  <span class="hljs-keyword">const</span> unaryTag = [<span class="hljs-string">'input'</span>]
  <span class="hljs-keyword">return</span> unaryTag.includes(tagName)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">generate</h2>
<blockquote>
<p>/src/compiler/generate.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 从 ast 生成渲染函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>ast ast 语法树
 * <span class="hljs-doctag">@returns </span>渲染函数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generate</span>(<span class="hljs-params">ast</span>) </span>&#123;
  <span class="hljs-comment">// 渲染函数字符串形式</span>
  <span class="hljs-keyword">const</span> renderStr = genElement(ast)
  <span class="hljs-comment">// 通过 new Function 将字符串形式的函数变成可执行函数，并用 with 为渲染函数扩展作用域链</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">`with(this) &#123; return <span class="hljs-subst">$&#123;renderStr&#125;</span> &#125;`</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">genElement</h3>
<blockquote>
<p>/src/compiler/generate.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析 ast 生成 渲染函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>ast 语法树 
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;string&#125;</span> </span>渲染函数的字符串形式
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genElement</span>(<span class="hljs-params">ast</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; tag, rawAttr, attr &#125; = ast

  <span class="hljs-comment">// 生成属性 Map 对象，静态属性 + 动态属性</span>
  <span class="hljs-keyword">const</span> attrs = &#123; ...rawAttr, ...attr &#125;

  <span class="hljs-comment">// 处理子节点，得到一个所有子节点渲染函数组成的数组</span>
  <span class="hljs-keyword">const</span> children = genChildren(ast)

  <span class="hljs-comment">// 生成 VNode 的可执行方法</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_c('<span class="hljs-subst">$&#123;tag&#125;</span>', <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(attrs)&#125;</span>, [<span class="hljs-subst">$&#123;children&#125;</span>])`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">genChildren</h3>
<blockquote>
<p>/src/compiler/generate.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 ast 节点的子节点，将子节点变成渲染函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>ast 节点的 ast 对象 
 * <span class="hljs-doctag">@returns </span>[childNodeRender1, ....]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genChildren</span>(<span class="hljs-params">ast</span>) </span>&#123;
  <span class="hljs-keyword">const</span> ret = [], &#123; children &#125; = ast
  <span class="hljs-comment">// 遍历所有的子节点</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = children.length; i < len; i++) &#123;
    <span class="hljs-keyword">const</span> child = children[i]
    <span class="hljs-keyword">if</span> (child.type === <span class="hljs-number">3</span>) &#123;
      <span class="hljs-comment">// 文本节点</span>
      ret.push(<span class="hljs-string">`_v(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(child)&#125;</span>)`</span>)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (child.type === <span class="hljs-number">1</span>) &#123;
      <span class="hljs-comment">// 元素节点</span>
      ret.push(genElement(child))
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> ret
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">结果</h1>
<p>在 <code>mount</code> 方法中加一句 <code>console.log(vm.$options.render)</code>，打开控制台，刷新页面，看到如下内容，说明编译器就完成了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b37a56386143ea8d0b6cbe3d8d0f42~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就会进入正式的挂载阶段，完成页面的初始渲染。</p>
<h1 data-id="heading-20">关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-21">链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/column/6960553066101735461" target="_blank">精通 Vue 技术栈的源码原理</a></p>
</li>
<li>
<p><a href="https://space.bilibili.com/359669053/channel/detail?cid=178493" target="_blank" rel="nofollow noopener noreferrer">配套视频</a></p>
</li>
<li>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank">学习交流群</a></p>
</li>
</ul></div>  
</div>
            