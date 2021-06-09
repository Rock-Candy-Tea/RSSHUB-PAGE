
---
title: '虚拟 DOM 与 Diff 算法的实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f14362268964bcca515b18805be22a6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:32:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f14362268964bcca515b18805be22a6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>Vue 源码中虚拟 DOM 与 Diff 算法的实现借鉴了 <code>snabbdom</code> 这个库，<code>snabbdom</code> 是一个虚拟 DOM 库，它专注于简单，模块化，强大的功能和性能。要彻底明白虚拟 DOM 与 Diff 算法就得分析 <code>snabbdom</code> 这个库到底做了什么？</p>
<h2 data-id="heading-1">获取源代码</h2>
<p>可以通过<code>npm i snabbdom -D</code> 来下载 <code>snabbdom</code> 库，这样我们既能看到 <code>src</code> 下用 Typescript 编写的源码，也能看到编译好的 JavaScript 代码。下面贴的源码是 <code>2.1.0</code> 版本，现在已经更新到 <code>3.0.3</code> 版本了。建议将下方出现的源码复制到下载的 <code>snabbdom</code> 库中相应位置，这样看源码比较清晰。那我们就开始分析源码吧。</p>
<h2 data-id="heading-2">源码分析</h2>
<h3 data-id="heading-3">JavaScript 对象模拟真实 DOM 树</h3>
<p>通过调用 <code>snabbdom</code> 库中的 <code>h</code>函数就可以对真实 DOM 节点进行抽象。我们先来看看一个完整的虚拟 DOM 节点（vnode）是什么样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">sel</span>: <span class="hljs-string">"div"</span>, <span class="hljs-comment">// 当前vnode的选择器</span>
  <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 当前vnode对应真实的DOM节点</span>
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 当前vnode的唯一标识</span>
  <span class="hljs-attr">data</span>: &#123;&#125;, <span class="hljs-comment">// 当前vnode的属性，样式等</span>
  <span class="hljs-attr">children</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 当前vnode的子元素</span>
  <span class="hljs-attr">text</span>: <span class="hljs-string">'文本内容'</span> <span class="hljs-comment">// 当前vnode的文本节点内容</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，<code>h</code>函数的作用就是用 JavaScript 对象模拟真实的 DOM 树，对真实 DOM 树进行抽象。调用 <code>h</code>函数就能得到由 vnode 组成的虚拟 DOM 树。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f14362268964bcca515b18805be22a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
调用 <code>h</code>函数有多种形式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> ① h(<span class="hljs-string">'div'</span>)
 ② h(<span class="hljs-string">'div'</span>, <span class="hljs-string">'text'</span>)
 ③ h(<span class="hljs-string">'div'</span>, h(<span class="hljs-string">'p'</span>))
 ④ h(<span class="hljs-string">'div'</span>, [])
 ⑤ h(<span class="hljs-string">'div'</span>, &#123;&#125;)
 ⑥ h(<span class="hljs-string">'div'</span>, &#123;&#125;, <span class="hljs-string">'text'</span>)
 ⑦ h(<span class="hljs-string">'div'</span>, &#123;&#125;, h(<span class="hljs-string">'span'</span>))
 ⑧ h(<span class="hljs-string">'div'</span>, &#123;&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使得 <code>h</code>函数的第二和第三个参数比较灵活，要判断的情况也比较多，下面把这部分的核心源码分析贴一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// h函数：根据传入的参数推测出h函数的调用形式以及每个vnode对应属性的属性值</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: string</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: string, data: VNodeData | <span class="hljs-literal">null</span></span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: string, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: string, data: VNodeData | <span class="hljs-literal">null</span>, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: any, b?: any, c?: any</span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-title">var</span> <span class="hljs-title">data</span>: <span class="hljs-title">VNodeData</span> = </span>&#123;&#125;</span>;
  <span class="hljs-title">var</span> <span class="hljs-title">children</span>: <span class="hljs-title">any</span></span>;
  <span class="hljs-title">var</span> <span class="hljs-title">text</span>: <span class="hljs-title">any</span></span>;
  <span class="hljs-keyword">var</span> i: number
  <span class="hljs-comment">// c有值，情况有：⑥ ⑦ ⑧</span>
  <span class="hljs-keyword">if</span> (c !== <span class="hljs-literal">undefined</span>) &#123; 
    <span class="hljs-comment">// c有值的情况下b有值，情况有：⑥ ⑦ ⑧</span>
    <span class="hljs-keyword">if</span> (b !== <span class="hljs-literal">null</span>) &#123; 
      <span class="hljs-comment">// 将b赋值给data </span>
      data = b  
    &#125;
    <span class="hljs-comment">// c的数据类型是数组，情况有：⑧</span>
    <span class="hljs-keyword">if</span> (is.array(c)) &#123; 
      children = c 
    <span class="hljs-comment">// 判断c是文本节点，情况有：⑥</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(c)) &#123; 
      text = c 
    <span class="hljs-comment">// 情况有：⑦，⑦这条语句会先执行h('span')代码，直接调用vnode函数，调用后会返回&#123;sel: 'span'&#125;，</span>
    <span class="hljs-comment">// 这时c有值并且c并且含有sel属性</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (c && c.sel) &#123;
      <span class="hljs-comment">// 注：这里的c不是h('span')，而是h('span')的返回值，是个&#123; sel: 'span' &#125;这样的对象，</span>
      <span class="hljs-comment">// 最后组装成数组赋值给children</span>
      children = [c]
    &#125;
  <span class="hljs-comment">// c没有值，b有值，情况有：② ③ ④ ⑤</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b !== <span class="hljs-literal">undefined</span> && b !== <span class="hljs-literal">null</span>) &#123; 
    <span class="hljs-comment">// b的数据类型是数组，情况有：④</span>
    <span class="hljs-keyword">if</span> (is.array(b)) &#123; 
      children = b 
    <span class="hljs-comment">// 判断b是文本节点，情况有：②</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(b)) &#123; 
      text = b 
    <span class="hljs-comment">// 情况有：③，③这条语句会先执行h('p')代码，直接调用vnode函数，调用后会返回&#123;sel: 'p'&#125;，</span>
    <span class="hljs-comment">// 这时b有值并且b并且含有sel属性</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b && b.sel) &#123;
      <span class="hljs-comment">// 注：这里的b不是h('p')，而是h('p')的返回值，是个&#123; sel: 'p' &#125;这样的对象，</span>
      <span class="hljs-comment">// 最后组装成数组赋值给children</span>
      children = [b] 
    <span class="hljs-comment">// 情况有：⑤，将b赋值给data</span>
    &#125; <span class="hljs-keyword">else</span> &#123; data = b &#125; 
  &#125;
  <span class="hljs-comment">// children有值，遍历children</span>
  <span class="hljs-keyword">if</span> (children !== <span class="hljs-literal">undefined</span>) &#123; 
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
      <span class="hljs-comment">// 判断children中的每一项的数据类型是否是string/number，调用vnode函数</span>
      <span class="hljs-keyword">if</span> (is.primitive(children[i])) &#123;
          children[i] = vnode(<span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, children[i], <span class="hljs-literal">undefined</span>)
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">/**
   * 调用vnode后返回形如
   * &#123;
   *    sel: 'div',
   *    data: &#123; style: '#000' &#125;,
   *    children: undefined,
   *    text: 'text',
   *    elm: undefined, 
   *    key: undefined
   * &#125;
   * 这样的JavaScript对象
  */</span>
  <span class="hljs-keyword">return</span> vnode(sel, data, children, text, <span class="hljs-literal">undefined</span>);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vnode函数：根据传入的参数组装vnode结构</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span>(<span class="hljs-params">sel: string | <span class="hljs-literal">undefined</span>,
  data: any | <span class="hljs-literal">undefined</span>,
  children: <span class="hljs-built_in">Array</span><VNode | string> | <span class="hljs-literal">undefined</span>,
  text: string | <span class="hljs-literal">undefined</span>,
  elm: Element | Text | <span class="hljs-literal">undefined</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-comment">// 判断data是否有值，有值就将data.key赋值给key，无值就将undefined赋值给key</span>
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key 
  <span class="hljs-comment">// 将传入vnode函数的参数组装成一个对象返回</span>
  <span class="hljs-keyword">return</span> &#123; sel, data, children, text, elm, key &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">diff 算法--入口函数</h3>
<p>通过 <code>h</code>函数得到新旧虚拟节点 DOM 对象后就可以进行差异比较了。在实际使用过程中，我们是直接调用 <code>snabbdom</code> 的 <code>patch</code> 函数，然后传入两个参数，通过 <code>patch</code> 函数内部处理就可以得到新旧虚拟节点 DOM 对象的差异，并将差异部分更新到真正的 DOM 树上。</p>
<p>首先，<code>patch</code> 函数会去判断 <code>oldVnode</code> 是否是真实DOM节点，如果是则需要先转换为虚拟DOM节点 <code>oldVnode = emptyNodeAt(oldVnode)</code> ；然后去比较新旧 vnode 是否是同一个节点 <code>sameVnode(oldVnode, vnode)</code>，如果是同一节点则精确比较新旧 vnode <code>patchVnode(oldVnode, vnode, insertedVnodeQueue)</code> ，如果不是则直接创建新 vnode 对应的真实 DOM 节点 <code>createElm(vnode, insertedVnodeQueue)</code>，在 createElm 函数中创建新 vnode 的真实 DOM 节点以及它对应的子节点，并把子节点插入到相应位置。如果 oldVnode.elm 有父节点则把新 vnode 对应的真实 DOM 节点作为子节点插入到相应位置，并且删除旧节点。下面贴一下 <code>patch</code> 函数的源码解析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;
    <span class="hljs-keyword">let</span> i: number, <span class="hljs-attr">elm</span>: Node, <span class="hljs-attr">parent</span>: Node
    <span class="hljs-keyword">const</span> insertedVnodeQueue: VNodeQueue = []
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.pre.length; ++i) cbs.pre[i]()

    <span class="hljs-comment">// isVnode(oldVnode)判断oldVnode.sel是否存在，不存在表示oldVnode是真实的DOM节点</span>
    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
      <span class="hljs-comment">// oldVnode可能是真实的DOM节点，也可能是旧的虚拟DOM节点，</span>
      <span class="hljs-comment">// 如果是真实的DOM节点要调用vnode函数组装成虚拟DOM节点</span>
      oldVnode = emptyNodeAt(oldVnode)
    &#125;

    <span class="hljs-comment">// 判断出是同一个虚拟DOM节点</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123; 
      <span class="hljs-comment">// 精确比较两个虚拟DOM节点</span>
      patchVnode(oldVnode, vnode, insertedVnodeQueue) 
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// oldVnode.elm是虚拟DOM节点对应的真实DOM节点</span>
      elm = oldVnode.elm! 
      <span class="hljs-comment">// api.parentNode(elm)获取elm的父节点elm.parentNode</span>
      parent = api.parentNode(elm) <span class="hljs-keyword">as</span> Node 

      <span class="hljs-comment">// 创建vnode下真实DOM节点并更新到相应位置</span>
      createElm(vnode, insertedVnodeQueue) 

      <span class="hljs-comment">// elm的父节点存在</span>
      <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123; 
        <span class="hljs-comment">// api.nextSibling(elm)-->elm.nextSibling 返回紧跟在elm之后的节点</span>
        <span class="hljs-comment">// api.insertBefore(parent, B, C)-->-->parent.insertBefore(B, C)，将B节点插入到C节点之前</span>
        api.insertBefore(parent, vnode.elm!, api.nextSibling(elm))
        removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>) <span class="hljs-comment">// 删除旧的DOM节点</span>
      &#125;
    &#125;

    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < insertedVnodeQueue.length; ++i) &#123;
      insertedVnodeQueue[i].data!.hook!.insert!(insertedVnodeQueue[i])
    &#125;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.post.length; ++i) cbs.post[i]()
    <span class="hljs-keyword">return</span> vnode
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>patch</code> 函数中用到了 <code>emptyNodeAt</code> 函数，这个函数主要是处理 <code>patch</code> 函数第一个参数为真实DOM节点的情况。下面贴一下这个函数的源码解析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span>(<span class="hljs-params">elm: Element</span>) </span>&#123;
    <span class="hljs-comment">// 判断传入的DOM节点elm有没有id属性，因为虚拟DOM节点的sel属性是选择器，例如：div#wrap</span>
    <span class="hljs-keyword">const</span> id = elm.id ? <span class="hljs-string">'#'</span> + elm.id : <span class="hljs-string">''</span> 
    <span class="hljs-comment">// 判断传入的ODM节点elm有没有class属性，因为虚拟DOM节点的sel属性是选择器，例如：div.wrap</span>
    <span class="hljs-keyword">const</span> c = elm.className ? <span class="hljs-string">'.'</span> + elm.className.split(<span class="hljs-string">' '</span>).join(<span class="hljs-string">'.'</span>) : <span class="hljs-string">''</span> 
    <span class="hljs-comment">// 调用vnode函数将传入的DOM节点组装成虚拟DOM节点</span>
    <span class="hljs-keyword">return</span> vnode(api.tagName(elm).toLowerCase() + id + c, &#123;&#125;, [], <span class="hljs-literal">undefined</span>, elm) 
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>patch</code> 函数中用到了 <code>sameVnode</code> 函数，这个函数主要用来比较两个虚拟DOM节点是否是同一个虚拟节点。下面贴一下这个函数的源码分析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1: VNode, vnode2: VNode</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-comment">// 判断vnode1和vnode2是否是同一个虚拟DOM节点</span>
  <span class="hljs-keyword">return</span> vnode1.key === vnode2.key && vnode1.sel === vnode2.sel 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">diff 算法--新旧 vnode 不是同一个节点的情况</h3>
<p>根据 <code>sameVnode</code> 函数返回的结果，新旧 vnode 不是同一个虚拟节点。首先获取到 oldVnode 对应真实 DOM 节点的父节点 <code>parent</code> ，然后调用 <code>createElm</code> 函数去创建 vnode 对应的真实 DOM 节点以及它的子节点和标签属性等等。判断是否有 <code>parent</code>， 如果有则将 vnode.elm 对应的DOM节点作为子节点插入到 <code>parent</code> 节点下的相应位置。部分源码分析在<code>patch</code>函数中，下面贴一下 <code>createElm</code> 函数的源码分析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode: VNode, insertedVnodeQueue: VNodeQueue</span>): <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-keyword">let</span> i: any
    <span class="hljs-keyword">let</span> data = vnode.data
    <span class="hljs-keyword">if</span> (data !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-keyword">const</span> init = data.hook?.init
      <span class="hljs-keyword">if</span> (isDef(init)) &#123;
        init(vnode)
        data = vnode.data
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> children = vnode.children
    <span class="hljs-keyword">const</span> sel = vnode.sel
    <span class="hljs-comment">// 判断sel值中是否包含!</span>
    <span class="hljs-keyword">if</span> (sel === <span class="hljs-string">'!'</span>) &#123;
      <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
        vnode.text = <span class="hljs-string">''</span>
      &#125;
      <span class="hljs-comment">// --> document.createComment(vnode.text!)创建注释节点</span>
      vnode.elm = api.createComment(vnode.text!)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sel !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// 解析sel选择器</span>
      <span class="hljs-comment">// 查找sel属性值中#的索引，没找到返回-1</span>
      <span class="hljs-keyword">const</span> hashIdx = sel.indexOf(<span class="hljs-string">'#'</span>)
      <span class="hljs-comment">// hashIdx作为起始位置查找sel属性值中.的索引，如果hashIdx < 0 那么从位置0开始查找</span>
      <span class="hljs-keyword">const</span> dotIdx = sel.indexOf(<span class="hljs-string">'.'</span>, hashIdx)
      <span class="hljs-keyword">const</span> hash = hashIdx > <span class="hljs-number">0</span> ? hashIdx : sel.length
      <span class="hljs-keyword">const</span> dot = dotIdx > <span class="hljs-number">0</span> ? dotIdx : sel.length
      <span class="hljs-comment">// 若id选择器或class选择器存在，则从0位开始截取到最小索引值的位置结束，截取出的就是标签名称</span>
      <span class="hljs-comment">// 都不存在直接取sel值</span>
      <span class="hljs-keyword">const</span> tag = hashIdx !== -<span class="hljs-number">1</span> || dotIdx !== -<span class="hljs-number">1</span> ? sel.slice(<span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.min(hash, dot)) : sel
      <span class="hljs-comment">// 根据tag名创建DOM元素</span>
      <span class="hljs-keyword">const</span> elm = vnode.elm = isDef(data) && isDef(i = data.ns)
        ? api.createElementNS(i, tag)
        : api.createElement(tag)
      <span class="hljs-comment">// 设置id属性</span>
      <span class="hljs-keyword">if</span> (hash < dot) elm.setAttribute(<span class="hljs-string">'id'</span>, sel.slice(hash + <span class="hljs-number">1</span>, dot))
      <span class="hljs-comment">// 设置calss属性</span>
      <span class="hljs-keyword">if</span> (dotIdx > <span class="hljs-number">0</span>) elm.setAttribute(<span class="hljs-string">'class'</span>, sel.slice(dot + <span class="hljs-number">1</span>).replace(<span class="hljs-regexp">/\./g</span>, <span class="hljs-string">' '</span>))
      <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) cbs.create[i](emptyNode, vnode)
      <span class="hljs-comment">// 判断children是否是数组，是数组则遍历children</span>
      <span class="hljs-keyword">if</span> (is.array(children)) &#123;
        <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
          <span class="hljs-keyword">const</span> ch = children[i]
          <span class="hljs-keyword">if</span> (ch != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// createElm(ch as VNode, insertedVnodeQueue)递归创建子节点</span>
            <span class="hljs-comment">// api.appendChild(A, B)-->A.appendChild(B)将B节点插入到指定父节点A的子节点列表的末尾</span>
            api.appendChild(elm, createElm(ch <span class="hljs-keyword">as</span> VNode, insertedVnodeQueue))
          &#125;
        &#125;
        <span class="hljs-comment">// 判断vnode.text有没有值</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(vnode.text)) &#123;
        <span class="hljs-comment">// api.createTextNode(vnode.text)根据vnode.text创建文本节点</span>
        <span class="hljs-comment">// api.appendChild(elm, B)-->A.appendChild(B)将文本节点B添加到父节点elm子节点列表的末尾处</span>
        api.appendChild(elm, api.createTextNode(vnode.text))
      &#125;
      <span class="hljs-keyword">const</span> hook = vnode.data!.hook
      <span class="hljs-keyword">if</span> (isDef(hook)) &#123;
        hook.create?.(emptyNode, vnode)
        <span class="hljs-keyword">if</span> (hook.insert) &#123;
          insertedVnodeQueue.push(vnode)
        &#125;
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// sel不存在直接创建文本节点</span>
      vnode.elm = api.createTextNode(vnode.text!)
    &#125;
    <span class="hljs-keyword">return</span> vnode.elm
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">diff 算法--新旧 vnode 是同一个节点的情况</h3>
<p>上面分析了新旧 vnode 不是同一个虚拟节点，那么是同一个虚拟节点又该怎么去处理？首先，调用 <code>patchVnode</code> 函数 <code>patchVnode(oldVnode, vnode, insertedVnodeQueue)</code>，这个函数会对新旧 vnode 进行精确比较：</p>
<p>① 如果新旧虚拟 DOM 对象全等 <code>oldVnode === vnode</code> ，那么不做任何操作，直接返回；</p>
<p>② 然后判断 vnode 是否有文本节点 <code>isUndef(vnode.text)</code> ，如果没有文本节点则判断 oldVnode 与 vnode 有没有子节点 <code>isDef(oldCh) && isDef(ch)</code>，如果都有子节点且不相等则调用 <code>updateChildren</code> 函数去更新子节点；</p>
<p>③ 如果只有 vnode 有子节点而 oldVnode 有文本节点或没有内容，将 oldVnode 的文本节点置空或不做处理，调用 <code>addVnodes</code> 函数将 vnode 的子节点创建出对应的真实DOM并循环插入到父节点下；</p>
<p>④ 如果只有 oldVnode 有子节点而 vnode 没有内容，则直接删除 oldVnode 下的子节点；</p>
<p>⑤ 如果只有 oldVnode 有文本节点而 vnode 没有内容，则将 oldVnode 对应的真实 DOM 节点的文本置空;</p>
<p>⑥ 如果 vnode 有文本节点，oldVnode 有子节点就将对应真实 DOM 节点的子节点删除，没有就不处理，然后将 vnode 的文本节点作为子节点插入到对应真实 DOM 节点下。</p>
<p>部分源码分析在<code>patch</code>函数中，下面贴一下 <code>patchVnode</code> 函数的源码分析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode: VNode, vnode: VNode, insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">const</span> hook = vnode.data?.hook
    hook?.prepatch?.(oldVnode, vnode)
    <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm!
    <span class="hljs-keyword">const</span> oldCh = oldVnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-keyword">const</span> ch = vnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-comment">// oldVnode与vnode完全相等并没有需要更新的内容则直接返回，不做处理</span>
    <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span> 
    <span class="hljs-keyword">if</span> (vnode.data !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
      vnode.data.hook?.update?.(oldVnode, vnode)
    &#125;
    <span class="hljs-comment">// vnode.text为undefined表示vnode虚拟节点没有文本内容</span>
    <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123; 
      <span class="hljs-comment">// oldCh与ch都不为undefined表示oldVnode与vnode都有虚拟子节点children</span>
      <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123; 
        <span class="hljs-comment">// oldCh !== ch 利用算法去更新子节点</span>
        <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123; 
        <span class="hljs-comment">// 将oldVnode的文本节点设置为''</span>
        <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) api.setTextContent(elm, <span class="hljs-string">''</span>) 
        <span class="hljs-comment">// 调用addVnodes方法将vnode的虚拟子节点循环插入到elm节点的子列表下</span>
        addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
      <span class="hljs-comment">// oldCh不为undefined表示oldVnode有虚拟子节点children</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123; 
        <span class="hljs-comment">// vnode没有children则直接删除oldVnode的children</span>
        removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>) 
      <span class="hljs-comment">// oldVnode.text有值而vnode.text没有值</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123; 
        <span class="hljs-comment">// 将oldVnode的文本节点设置为''</span>
        api.setTextContent(elm, <span class="hljs-string">''</span>) 
      &#125;
    <span class="hljs-comment">// oldVnode与vnode文本节点内容不同</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123; 
      <span class="hljs-comment">// isDef(oldCh)-->oldCh !== undefined 表明oldVnode虚拟节点下有虚拟子节点</span>
      <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123; 
        removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
      &#125;
      <span class="hljs-comment">// oldCh虚拟节点下没有虚拟子节点则直接更新文本内容</span>
      api.setTextContent(elm, vnode.text!)
    &#125;
    hook?.postpatch?.(oldVnode, vnode)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">diff 算法--新旧 vnode 子节点的更新策略</h3>
<p>当新旧 vnode 都有子节点时，<code>diff</code> 算法定义了四个指针来处理子节点，四个指针分别是：<code>oldStartVnode(旧前vnode)</code>/<code>newStartVnode(新前vnode)</code>/<code>oldEndVnode(旧后vnode)</code>/<code>newEndVnode(新后vnode)</code> 。进入循环体内后，新旧 vnode 的子节点两两比较，这里提供了一套比较规则，如下图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d2ac881b91e4af2b96526cd8cbd7461~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果上面四个规则都不满足，将 oldVnode 的子节点从旧的前索引 <code>oldStartIdx</code> 到旧的后索引 <code>oldEndIdx</code> 做一个 key 与对应位置序号的映射 <code>oldKeyToIdx</code> ，通过新 vnode 的 key 去找 <code>oldKeyToIdx</code> 中是否有对应的索引值，若没有，表明 <code>oldVnode</code> 没有对应的旧节点，是一个新增的节点，进行插入操作；若有，表明 <code>oldVnode</code> 有对应的旧节点，不是一个新增节点，进行移动操作。当新旧 vnode 中其中一个的所有子节点处理完毕，而另一个还未处理完，那么就要用其他的处理方案。具体的看下面的源码分析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 旧vnode的子节点的前索引oldStartIdx到后索引oldEndIdx的key与对应位置序号的映射关系</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">children: VNode[], beginIdx: number, endIdx: number</span>): <span class="hljs-title">KeyToIndexMap</span> </span>&#123;
  <span class="hljs-keyword">const</span> map: KeyToIndexMap = &#123;&#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = beginIdx; i <= endIdx; ++i) &#123;
    <span class="hljs-keyword">const</span> key = children[i]?.key
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-literal">undefined</span>) &#123;
      map[key] = i
    &#125;
  &#125;
  <span class="hljs-comment">/**
   * 例如：map = &#123; A: 1, B: 2 &#125;
  */</span>
  <span class="hljs-keyword">return</span> map
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm: Node,
    oldCh: VNode[],
    newCh: VNode[],
    insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 旧的前索引</span>
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 新的前索引</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 旧的后索引</span>
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 新的后索引</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 旧的前vnode</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 新的前vnode</span>
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx] <span class="hljs-comment">// 旧的后vnode</span>
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx] <span class="hljs-comment">// 新的后vnode</span>
    <span class="hljs-keyword">let</span> oldKeyToIdx: KeyToIndexMap | <span class="hljs-literal">undefined</span>
    <span class="hljs-keyword">let</span> idxInOld: number
    <span class="hljs-keyword">let</span> elmToMove: VNode
    <span class="hljs-keyword">let</span> before: any

    <span class="hljs-comment">// 当旧的前索引 <= 旧的后索引 && 新的前索引 <= 新的后索引时执行循环语句</span>
    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-comment">// 为什么oldStartVnode == null? </span>
      <span class="hljs-comment">// 因为虚拟节点进行移动操作后要将原来的虚拟节点置为undefined了</span>
      <span class="hljs-comment">// oldCh[idxInOld] = undefined as any</span>
      <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// oldStartVnode为null就过滤掉当前节点，取oldCh[++oldStartIdx]节点(旧的前索引的下一个索引的节点)</span>
        oldStartVnode = oldCh[++oldStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// oldEndVnode为null就过滤掉当前节点，取oldCh[--oldEndIdx]节点(旧的后索引的上一个索引的节点)</span>
        oldEndVnode = oldCh[--oldEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// newStartVnode为null就过滤掉当前节点，取newCh[++newStartIdx]节点(新的前索引的下一个索引的节点)</span>
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// newEndVnode为null就过滤掉当前节点，取newCh[--newEndIdx]节点(新的后索引的上一个索引的节点)</span>
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
        <span class="hljs-comment">/**
        * ① 旧的前vnode（oldStartVnode） 与 新的前vnode（newStartVnode） 比较是否是同一个虚拟节点
        * 旧的虚拟子节点                       新的虚拟子节点
        * h('li', &#123; key: 'A' &#125;, 'A')      h('li', &#123; key: 'A' &#125;, 'A')
        * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'B' &#125;, 'B')
       */</span>
        <span class="hljs-comment">// 如果判断是同一个虚拟节点则调用patchVnode函数</span>
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue)
        <span class="hljs-comment">// oldCh[++oldStartIdx]取旧的前索引节点的下一个虚拟节点（例子中key为B的节点），赋值给oldStartVnode</span>
        oldStartVnode = oldCh[++oldStartIdx]
        <span class="hljs-comment">// oldCh[++oldStartIdx]取新的前索引节点的下一个虚拟节点（例子中key为B的节点），赋值给newStartVnode</span>
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
        <span class="hljs-comment">/**
         * 如果旧的前vnode（例子中key为B的虚拟节点） 与 新的前vnode（例子中key为B的虚拟节点） 
         * 不是同一个虚拟节点则进行方案②比较
         * ② 旧的后vnode（oldEndVnode） 与 新的后vnode（newEndVnode） 比较是否是同一个虚拟节点
         * 旧的虚拟子节点                   新的虚拟子节点
         * h('li', &#123; key: 'C' &#125;, 'C')      h('li', &#123; key: 'A' &#125;, 'A')
         * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'B' &#125;, 'B')
        */</span>
        <span class="hljs-comment">// 如果判断是同一个虚拟节点则调用patchVnode函数</span>
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue)
        <span class="hljs-comment">// oldCh[--oldEndIdx]取旧的后索引节点的上一个虚拟节点（例子中key为C的虚拟节点），赋值给oldEndVnode</span>
        oldEndVnode = oldCh[--oldEndIdx]
        <span class="hljs-comment">// newCh[--newEndIdx]取新的后索引节点的上一个虚拟节点（例子中key为A的虚拟节点），赋值给newEndVnode</span>
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
        <span class="hljs-comment">/**
        * 如果旧的后vnode 与 新的后vnode 不是同一个虚拟节点则进行方案③比较
        * ③ 旧的前vnode（oldStartVnode） 与 新的后vnode（newEndVnode） 比较是否是同一个虚拟节点
        * 旧的虚拟子节点                   新的虚拟子节点
        * h('li', &#123; key: 'C' &#125;, 'C')      h('li', &#123; key: 'A' &#125;, 'A')
        * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'B' &#125;, 'B')
        *                                 h('li', &#123; key: 'C' &#125;, 'C')
       */</span>
        <span class="hljs-comment">// 如果判断是同一个虚拟节点则调用patchVnode函数</span>
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue)
        <span class="hljs-comment">// 将旧的前vnode（相当于例子中key为C的虚拟节点）插入到当前旧的后vnode的下一个兄弟节点的前面</span>
        <span class="hljs-comment">// 如果oldEndVnode是最末尾的虚拟节点，则node.nextSibling会返回null，</span>
        <span class="hljs-comment">// 则新的虚拟节点直接插入到最末尾，等同于appenChild</span>
        api.insertBefore(parentElm, oldStartVnode.elm!, api.nextSibling(oldEndVnode.elm!))
        <span class="hljs-comment">// oldCh[++oldStartIdx]取旧的前索引虚拟节点的下一个虚拟节点（例子中key为B的虚拟节点），赋值给oldStartVnode</span>
        oldStartVnode = oldCh[++oldStartIdx]
        <span class="hljs-comment">// newCh[--newEndIdx]取新的后索引虚拟节点的上一个虚拟节点（例子中key为B的虚拟节点），赋值给newEndVnode</span>
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left</span>
        <span class="hljs-comment">/**
        * 如果旧的前vnode 与 新的后vnode 不是同一个虚拟节点则进行方案④比较
        * ④ 旧的后vnode（oldEndVnode） 与 新的前vnode（newStartVnode） 比较是否是同一个虚拟节点
        * 旧的虚拟子节点                   新的虚拟子节点
        * h('li', &#123; key: 'C' &#125;, 'C')      h('li', &#123; key: 'B' &#125;, 'B')
        * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'A' &#125;, 'A')
        *                                 h('li', &#123; key: 'C' &#125;, 'C')
       */</span>
        <span class="hljs-comment">// 如果判断是同一个虚拟节点则调用patchVnode函数</span>
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue)
        <span class="hljs-comment">// 将旧的后vnode（例子中key为B）插入到当前旧的前vnode（例子中key为C）的前面</span>
        api.insertBefore(parentElm, oldEndVnode.elm!, oldStartVnode.elm!)
        <span class="hljs-comment">// oldCh[--oldEndIdx]取旧的后索引节点的上一个虚拟节点（例子中key为C的虚拟节点），赋值给oldEndVnode</span>
        oldEndVnode = oldCh[--oldEndIdx]
        <span class="hljs-comment">// newCh[++newStartIdx]取新的前索引节点的下一个虚拟节点（例子中key为A的虚拟节点），赋值给newStartVnode</span>
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不满足以上四种情况</span>
        <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
          <span class="hljs-comment">// oldKeyToIdx保存旧的children中各个节点的key与对应位置序号的映射关系</span>
          oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
        &#125;
        <span class="hljs-comment">// 从oldKeyToIdx中获取当前newStartVnode节点key对应的序号</span>
        idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> string]
        <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// isUndef(idxInOld) --> idxInOld === undefined</span>
          <span class="hljs-comment">/**
           * idxInOld = undefined 要插入节点
           * 旧的虚拟子节点中没有idxInOld对应的节点，而新的虚拟子节点中有，
           * 所以newStartVnode是需要插入的虚拟节点
           * 旧的虚拟子节点                   新的虚拟子节点
           * h('li', &#123; key: 'A' &#125;, 'A')      h('li', &#123; key: 'C' &#125;, 'C') 
           * h('li', &#123; key: 'B' &#125;, 'B')
          */</span>
          <span class="hljs-comment">// 根据newStartVnode（例子中key为C的虚拟节点）创建真实DOM节点createElm()，</span>
          <span class="hljs-comment">// 将创建的DOM节点插入到oldStartVnode.elm（例子中key为A的节点）的前面</span>
          api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">/**
           * idxInOld != undefined 要移动节点
           * 旧的虚拟子节点中有idxInOld对应的节点，所以oldCh[idxInOld]是需要移动的虚拟节点
           * 旧的虚拟子节点                   新的虚拟子节点
           * h('li', &#123; key: 'A' &#125;, 'A')      h('div', &#123; key: 'B' &#125;, 'B')
           * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'D' &#125;, 'D')                                                      
          */</span>
          elmToMove = oldCh[idxInOld] <span class="hljs-comment">// elmToMove保存要移动的虚拟节点</span>
          <span class="hljs-comment">// 判断elmToMove与newStartVnode在key相同的情况下sel属性是否相同</span>
          <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
            <span class="hljs-comment">// sel属性不相同表明不是同一个虚拟节点，</span>
            <span class="hljs-comment">// 根据newStartVnode虚拟节点创建真实DOM节点并插入到oldStartVnode.elm（旧的key为A的节点）之前</span>
            api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// key与sel相同表示是同一个虚拟节点，调用patchVnode函数</span>
            patchVnode(elmToMove, newStartVnode, insertedVnodeQueue)
            <span class="hljs-comment">// 处理完被移动的虚拟节点oldCh[idxInOld]要设置为undefined，方便下次循环处理时过滤掉已经处理的节点</span>
            oldCh[idxInOld] = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> any
            <span class="hljs-comment">// 将elmToMove.elm（例子中旧的key为B的节点）插入到oldStartVnode.elm（例子中key为A的节点）的前面</span>
            api.insertBefore(parentElm, elmToMove.elm!, oldStartVnode.elm!)
          &#125;
        &#125;
        <span class="hljs-comment">// 取newCh[++newStartIdx]虚拟节点（例子中key为D的虚拟节点）赋值给newStartVnode</span>
        newStartVnode = newCh[++newStartIdx]
      &#125;
    &#125;
    <span class="hljs-comment">/**
     * 循环结束后旧的前索引 <= 旧的后索引 || 新的前索引 <= 新的后索引，
     * 表示还有部分虚拟节点（例子中key为C的虚拟节点）没处理
     * 旧的虚拟子节点                   新的虚拟子节点
     * 情况一：
     * h('li', &#123; key: 'A' &#125;, 'A')      h('li', &#123; key: 'A' &#125;, 'A')
     * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'B' &#125;, 'B')
     * h('li', &#123; key: 'D' &#125;, 'D')      h('li', &#123; key: 'C' &#125;, 'C')
     *                                 h('li', &#123; key: 'D' &#125;, 'D')
     * 情况二：
     * h('li', &#123; key: 'A' &#125;, 'A')      h('li', &#123; key: 'A' &#125;, 'A')
     * h('li', &#123; key: 'B' &#125;, 'B')      h('li', &#123; key: 'B' &#125;, 'B')
     * h('li', &#123; key: 'C' &#125;, 'C')
    */</span>
    <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
      <span class="hljs-comment">// 处理例子中情况一</span>
      <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        <span class="hljs-comment">// 待插入的节点以before节点为参照，newCh[newEndIdx]是例子中新的子节点中key为C的虚拟节点，</span>
        <span class="hljs-comment">// 所以before = newCh[newEndIdx + 1]是key为D的虚拟节点</span>
        before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
        <span class="hljs-comment">// 例子中现在newStartIdx，newEndIdx都为2</span>
        addVnodes(parentElm, before, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 处理例子中情况二，删除旧的前索引到旧的后索引中间的节点（例子中删除旧的key为C的虚拟节点）</span>
        removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            