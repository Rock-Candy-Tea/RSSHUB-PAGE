
---
title: 'Vue 源码解读（10）—— 编译器 之 生成渲染函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7936'
author: 掘金
comments: false
date: Wed, 12 May 2021 15:53:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=7936'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>这篇文章是 Vue 编译器的最后一部分，前两部分分别是：<a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析</a>、<a href="https://juejin.cn/post/6960465810682806308" target="_blank">Vue 源码解读（9）—— 编译器 之 优化</a>。</p>
<p>从 HTML 模版字符串开始，解析所有标签以及标签上的各个属性，得到 AST 语法树，然后基于 AST 语法树进行静态标记，首先标记每个节点是否为静态静态，然后进一步标记出静态根节点。这样在后续的更新中就可以跳过这些静态根节点的更新，从而提高性能。</p>
<p>这最后一部分讲的是如何从 AST 生成渲染函数。</p>
<h1 data-id="heading-1">目标</h1>
<p>深入理解渲染函数的生成过程，理解编译器是如何将 AST 变成运行时的代码，也就是我们写的类 html 模版最终变成了什么？</p>
<h1 data-id="heading-2">源码解读</h1>
<h2 data-id="heading-3">入口</h2>
<blockquote>
<p>/src/compiler/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 在这之前做的所有的事情，只有一个目的，就是为了构建平台特有的编译选项（options），比如 web 平台
 * 
 * 1、将 html 模版解析成 ast
 * 2、对 ast 树进行静态标记
 * 3、将 ast 生成渲染函数
 *    静态渲染函数放到  code.staticRenderFns 数组中
 *    code.render 为动态渲染函数
 *    在将来渲染时执行渲染函数得到 vnode
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createCompiler = createCompilerCreator(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCompile</span> (<span class="hljs-params">
  template: string,
  options: CompilerOptions
</span>): <span class="hljs-title">CompiledResult</span> </span>&#123;
  <span class="hljs-comment">// 将模版解析为 AST，每个节点的 ast 对象上都设置了元素的所有信息，比如，标签信息、属性信息、插槽信息、父节点、子节点等。</span>
  <span class="hljs-comment">// 具体有那些属性，查看 options.start 和 options.end 这两个处理开始和结束标签的方法</span>
  <span class="hljs-keyword">const</span> ast = parse(template.trim(), options)
  <span class="hljs-comment">// 优化，遍历 AST，为每个节点做静态标记</span>
  <span class="hljs-comment">// 标记每个节点是否为静态节点，然后进一步标记出静态根节点</span>
  <span class="hljs-comment">// 这样在后续更新中就可以跳过这些静态节点了</span>
  <span class="hljs-comment">// 标记静态根，用于生成渲染函数阶段，生成静态根节点的渲染函数</span>
  <span class="hljs-keyword">if</span> (options.optimize !== <span class="hljs-literal">false</span>) &#123;
    optimize(ast, options)
  &#125;
  <span class="hljs-comment">// 代码生成，将 ast 转换成可执行的 render 函数的字符串形式</span>
  <span class="hljs-comment">// code = &#123;</span>
  <span class="hljs-comment">//   render: `with(this)&#123;return $&#123;_c(tag, data, children, normalizationType)&#125;&#125;`,</span>
  <span class="hljs-comment">//   staticRenderFns: [_c(tag, data, children, normalizationType), ...]</span>
  <span class="hljs-comment">// &#125;</span>
  <span class="hljs-keyword">const</span> code = generate(ast, options)
  <span class="hljs-keyword">return</span> &#123;
    ast,
    <span class="hljs-attr">render</span>: code.render,
    <span class="hljs-attr">staticRenderFns</span>: code.staticRenderFns
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">generate</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 从 AST 生成渲染函数
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;
 *   render: `with(this)&#123;return _c(tag, data, children)&#125;</span></span>`,
 *   staticRenderFns: state.staticRenderFns
 * &#125; 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generate</span>(<span class="hljs-params">
  ast: ASTElement | <span class="hljs-keyword">void</span>,
  options: CompilerOptions
</span>): <span class="hljs-title">CodegenResult</span> </span>&#123;
  <span class="hljs-comment">// 实例化 CodegenState 对象，生成代码的时候需要用到其中的一些东西</span>
  <span class="hljs-keyword">const</span> state = <span class="hljs-keyword">new</span> CodegenState(options)
  <span class="hljs-comment">// 生成字符串格式的代码，比如：'_c(tag, data, children, normalizationType)'</span>
  <span class="hljs-comment">// data 为节点上的属性组成 JSON 字符串，比如 '&#123; key: xx, ref: xx, ... &#125;'</span>
  <span class="hljs-comment">// children 为所有子节点的字符串格式的代码组成的字符串数组，格式：</span>
  <span class="hljs-comment">//     `['_c(tag, data, children)', ...],normalizationType`，</span>
  <span class="hljs-comment">//     最后的 normalization 是 _c 的第四个参数，</span>
  <span class="hljs-comment">//     表示节点的规范化类型，不是重点，不需要关注</span>
  <span class="hljs-comment">// 当然 code 并不一定就是 _c，也有可能是其它的，比如整个组件都是静态的，则结果就为 _m(0)</span>
  <span class="hljs-keyword">const</span> code = ast ? genElement(ast, state) : <span class="hljs-string">'_c("div")'</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">render</span>: <span class="hljs-string">`with(this)&#123;return <span class="hljs-subst">$&#123;code&#125;</span>&#125;`</span>,
    <span class="hljs-attr">staticRenderFns</span>: state.staticRenderFns
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">genElement</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<blockquote>
<p><strong>阅读建议</strong>：</p>
<p>先读最后的 else 模块生成 code 的语句部分，即处理自定义组件和原生标签的 else 分支，理解最终生成的数据格式是什么样的；然后再回头阅读 <code>genChildren</code> 和 <code>genData</code>，先读 <code>genChildren</code>，代码量少，彻底理解最终生成的数据结构，最后再从上到下去阅读其它的分支。</p>
<p>在阅读以下代码时，请把 <a href="https://juejin.cn/post/6961545472204865572">Vue 源码解读（8）—— 编译器 之 解析（下）</a> 最后得到的 AST 对象放旁边辅助阅读，因为生成渲染函数的过程就是在处理该对象上众多的属性的过程。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genElement</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">if</span> (el.parent) &#123;
    el.pre = el.pre || el.parent.pre
  &#125;

  <span class="hljs-keyword">if</span> (el.staticRoot && !el.staticProcessed) &#123;
    <span class="hljs-comment">/**
     * 处理静态根节点，生成节点的渲染函数
     *   1、将当前静态节点的渲染函数放到 staticRenderFns 数组中
     *   2、返回一个可执行函数 _m(idx, true or '') 
     */</span>
    <span class="hljs-keyword">return</span> genStatic(el, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.once && !el.onceProcessed) &#123;
    <span class="hljs-comment">/**
     * 处理带有 v-once 指令的节点，结果会有三种：
     *   1、当前节点存在 v-if 指令，得到一个三元表达式，condition ? render1 : render2
     *   2、当前节点是一个包含在 v-for 指令内部的静态节点，得到 `_o(_c(tag, data, children), number, key)`
     *   3、当前节点就是一个单纯的 v-once 节点，得到 `_m(idx, true of '')`
     */</span>
    <span class="hljs-keyword">return</span> genOnce(el, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.for && !el.forProcessed) &#123;
    <span class="hljs-comment">/**
     * 处理节点上的 v-for 指令  
     * 得到 `_l(exp, function(alias, iterator1, iterator2)&#123;return _c(tag, data, children)&#125;)`
     */</span>
    <span class="hljs-keyword">return</span> genFor(el, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.if && !el.ifProcessed) &#123;
    <span class="hljs-comment">/**
     * 处理带有 v-if 指令的节点，最终得到一个三元表达式：condition ? render1 : render2
     */</span>
    <span class="hljs-keyword">return</span> genIf(el, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.tag === <span class="hljs-string">'template'</span> && !el.slotTarget && !state.pre) &#123;
    <span class="hljs-comment">/**
     * 当前节点不是 template 标签也不是插槽和带有 v-pre 指令的节点时走这里
     * 生成所有子节点的渲染函数，返回一个数组，格式如：
     * [_c(tag, data, children, normalizationType), ...] 
     */</span>
    <span class="hljs-keyword">return</span> genChildren(el, state) || <span class="hljs-string">'void 0'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.tag === <span class="hljs-string">'slot'</span>) &#123;
    <span class="hljs-comment">/**
     * 生成插槽的渲染函数，得到
     * _t(slotName, children, attrs, bind)
     */</span>
    <span class="hljs-keyword">return</span> genSlot(el, state)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// component or element</span>
    <span class="hljs-comment">// 处理动态组件和普通元素（自定义组件、原生标签）</span>
    <span class="hljs-keyword">let</span> code
    <span class="hljs-keyword">if</span> (el.component) &#123;
      <span class="hljs-comment">/**
       * 处理动态组件，生成动态组件的渲染函数
       * 得到 `_c(compName, data, children)`
       */</span>
      code = genComponent(el.component, el, state)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 自定义组件和原生标签走这里</span>
      <span class="hljs-keyword">let</span> data
      <span class="hljs-keyword">if</span> (!el.plain || (el.pre && state.maybeComponent(el))) &#123;
        <span class="hljs-comment">// 非普通元素或者带有 v-pre 指令的组件走这里，处理节点的所有属性，返回一个 JSON 字符串，</span>
        <span class="hljs-comment">// 比如 '&#123; key: xx, ref: xx, ... &#125;'</span>
        data = genData(el, state)
      &#125;

      <span class="hljs-comment">// 处理子节点，得到所有子节点字符串格式的代码组成的数组，格式：</span>
      <span class="hljs-comment">// `['_c(tag, data, children)', ...],normalizationType`，</span>
      <span class="hljs-comment">// 最后的 normalization 表示节点的规范化类型，不是重点，不需要关注</span>
      <span class="hljs-keyword">const</span> children = el.inlineTemplate ? <span class="hljs-literal">null</span> : genChildren(el, state, <span class="hljs-literal">true</span>)
      <span class="hljs-comment">// 得到最终的字符串格式的代码，格式：</span>
      <span class="hljs-comment">// '_c(tag, data, children, normalizationType)'</span>
      code = <span class="hljs-string">`_c('<span class="hljs-subst">$&#123;el.tag&#125;</span>'<span class="hljs-subst">$&#123;data ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;data&#125;</span>`</span> : <span class="hljs-string">''</span> <span class="hljs-regexp">//</span> data
        &#125;</span><span class="hljs-subst">$&#123;children ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;children&#125;</span>`</span> : <span class="hljs-string">''</span> <span class="hljs-regexp">//</span> children
        &#125;</span>)`</span>
    &#125;
    <span class="hljs-comment">// 如果提供了 transformCode 方法， </span>
    <span class="hljs-comment">// 则最终的 code 会经过各个模块（module）的该方法处理，</span>
    <span class="hljs-comment">// 不过框架没提供这个方法，不过即使处理了，最终的格式也是 _c(tag, data, children)</span>
    <span class="hljs-comment">// module transforms</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < state.transforms.length; i++) &#123;
      code = state.transforms[i](el, code)
    &#125;
    <span class="hljs-keyword">return</span> code
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">genChildren</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成所有子节点的渲染函数，返回一个数组，格式如：
 * [_c(tag, data, children, normalizationType), ...] 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genChildren</span>(<span class="hljs-params">
  el: ASTElement,
  state: CodegenState,
  checkSkip?: boolean,
  altGenElement?: <span class="hljs-built_in">Function</span>,
  altGenNode?: <span class="hljs-built_in">Function</span>
</span>): <span class="hljs-title">string</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// 所有子节点</span>
  <span class="hljs-keyword">const</span> children = el.children
  <span class="hljs-keyword">if</span> (children.length) &#123;
    <span class="hljs-comment">// 第一个子节点</span>
    <span class="hljs-keyword">const</span> el: any = children[<span class="hljs-number">0</span>]
    <span class="hljs-comment">// optimize single v-for</span>
    <span class="hljs-keyword">if</span> (children.length === <span class="hljs-number">1</span> &&
      el.for &&
      el.tag !== <span class="hljs-string">'template'</span> &&
      el.tag !== <span class="hljs-string">'slot'</span>
    ) &#123;
      <span class="hljs-comment">// 优化，只有一个子节点 && 子节点的上有 v-for 指令 && 子节点的标签不为 template 或者 slot</span>
      <span class="hljs-comment">// 优化的方式是直接调用 genElement 生成该节点的渲染函数，不需要走下面的循环然后调用 genCode 最后得到渲染函数</span>
      <span class="hljs-keyword">const</span> normalizationType = checkSkip
        ? state.maybeComponent(el) ? <span class="hljs-string">`,1`</span> : <span class="hljs-string">`,0`</span>
        : <span class="hljs-string">``</span>
      <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;(altGenElement || genElement)(el, state)&#125;</span><span class="hljs-subst">$&#123;normalizationType&#125;</span>`</span>
    &#125;
    <span class="hljs-comment">// 获取节点规范化类型，返回一个 number 0、1、2，不是重点， 不重要</span>
    <span class="hljs-keyword">const</span> normalizationType = checkSkip
      ? getNormalizationType(children, state.maybeComponent)
      : <span class="hljs-number">0</span>
    <span class="hljs-comment">// 函数，生成代码的一个函数</span>
    <span class="hljs-keyword">const</span> gen = altGenNode || genNode
    <span class="hljs-comment">// 返回一个数组，数组的每个元素都是一个子节点的渲染函数，</span>
    <span class="hljs-comment">// 格式：['_c(tag, data, children, normalizationType)', ...]</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`[<span class="hljs-subst">$&#123;children.map(c => gen(c, state)).join(<span class="hljs-string">','</span>)&#125;</span>]<span class="hljs-subst">$&#123;normalizationType ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;normalizationType&#125;</span>`</span> : <span class="hljs-string">''</span>
      &#125;</span>`</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">genNode</h3>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genNode</span>(<span class="hljs-params">node: ASTNode, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">if</span> (node.type === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> genElement(node, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (node.type === <span class="hljs-number">3</span> && node.isComment) &#123;
    <span class="hljs-keyword">return</span> genComment(node)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> genText(node)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">genText</h3>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genText</span>(<span class="hljs-params">text: ASTText | ASTExpression</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_v(<span class="hljs-subst">$&#123;text.type === <span class="hljs-number">2</span>
    ? text.expression <span class="hljs-regexp">//</span> no need <span class="hljs-keyword">for</span> () because already wrapped <span class="hljs-keyword">in</span> _s()
    : transformSpecialNewlines(<span class="hljs-built_in">JSON</span>.stringify(text.text))
    &#125;</span>)`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">genComment</h3>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genComment</span>(<span class="hljs-params">comment: ASTText</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_e(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(comment.text)&#125;</span>)`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">genData</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理节点上的众多属性，最后生成这些属性组成的 JSON 字符串，比如 data = &#123; key: xx, ref: xx, ... &#125; 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genData</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 节点的属性组成的 JSON 字符串</span>
  <span class="hljs-keyword">let</span> data = <span class="hljs-string">'&#123;'</span>

  <span class="hljs-comment">// 首先先处理指令，因为指令可能在生成其它属性之前改变这些属性</span>
  <span class="hljs-comment">// 执行指令编译方法，比如 web 平台的 v-text、v-html、v-model，然后在 el 对象上添加相应的属性，</span>
  <span class="hljs-comment">// 比如 v-text： el.textContent = _s(value, dir)</span>
  <span class="hljs-comment">//     v-html：el.innerHTML = _s(value, dir)</span>
  <span class="hljs-comment">// 当指令在运行时还有任务时，比如 v-model，则返回 directives: [&#123; name, rawName, value, arg, modifiers &#125;, ...&#125;] </span>
  <span class="hljs-comment">// directives first.</span>
  <span class="hljs-comment">// directives may mutate the el's other properties before they are generated.</span>
  <span class="hljs-keyword">const</span> dirs = genDirectives(el, state)
  <span class="hljs-keyword">if</span> (dirs) data += dirs + <span class="hljs-string">','</span>

  <span class="hljs-comment">// key，data = &#123; key: xx &#125;</span>
  <span class="hljs-keyword">if</span> (el.key) &#123;
    data += <span class="hljs-string">`key:<span class="hljs-subst">$&#123;el.key&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// ref，data = &#123; ref: xx &#125;</span>
  <span class="hljs-keyword">if</span> (el.ref) &#123;
    data += <span class="hljs-string">`ref:<span class="hljs-subst">$&#123;el.ref&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// 带有 ref 属性的节点在带有 v-for 指令的节点的内部， data = &#123; refInFor: true &#125;</span>
  <span class="hljs-keyword">if</span> (el.refInFor) &#123;
    data += <span class="hljs-string">`refInFor:true,`</span>
  &#125;
  <span class="hljs-comment">// pre，v-pre 指令，data = &#123; pre: true &#125;</span>
  <span class="hljs-keyword">if</span> (el.pre) &#123;
    data += <span class="hljs-string">`pre:true,`</span>
  &#125;
  <span class="hljs-comment">// 动态组件，data = &#123; tag: 'component' &#125;</span>
  <span class="hljs-comment">// record original tag name for components using "is" attribute</span>
  <span class="hljs-keyword">if</span> (el.component) &#123;
    data += <span class="hljs-string">`tag:"<span class="hljs-subst">$&#123;el.tag&#125;</span>",`</span>
  &#125;
  <span class="hljs-comment">// 为节点执行模块(class、style)的 genData 方法，</span>
  <span class="hljs-comment">// 得到 data = &#123; staticClass: xx, class: xx, staticStyle: xx, style: xx &#125;</span>
  <span class="hljs-comment">// module data generation functions</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < state.dataGenFns.length; i++) &#123;
    data += state.dataGenFns[i](el)
  &#125;
  <span class="hljs-comment">// 其它属性，得到 data = &#123; attrs: 静态属性字符串 &#125; 或者 </span>
  <span class="hljs-comment">// data = &#123; attrs: '_d(静态属性字符串, 动态属性字符串)' &#125;</span>
  <span class="hljs-comment">// attributes</span>
  <span class="hljs-keyword">if</span> (el.attrs) &#123;
    data += <span class="hljs-string">`attrs:<span class="hljs-subst">$&#123;genProps(el.attrs)&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// DOM props，结果同 el.attrs</span>
  <span class="hljs-keyword">if</span> (el.props) &#123;
    data += <span class="hljs-string">`domProps:<span class="hljs-subst">$&#123;genProps(el.props)&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// 自定义事件，data = &#123; `on$&#123;eventName&#125;:handleCode` &#125; 或者 &#123; `on_d($&#123;eventName&#125;:handleCode`, `$&#123;eventName&#125;,handleCode`) &#125;</span>
  <span class="hljs-comment">// event handlers</span>
  <span class="hljs-keyword">if</span> (el.events) &#123;
    data += <span class="hljs-string">`<span class="hljs-subst">$&#123;genHandlers(el.events, <span class="hljs-literal">false</span>)&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// 带 .native 修饰符的事件，</span>
  <span class="hljs-comment">// data = &#123; `nativeOn$&#123;eventName&#125;:handleCode` &#125; 或者 &#123; `nativeOn_d($&#123;eventName&#125;:handleCode`, `$&#123;eventName&#125;,handleCode`) &#125;</span>
  <span class="hljs-keyword">if</span> (el.nativeEvents) &#123;
    data += <span class="hljs-string">`<span class="hljs-subst">$&#123;genHandlers(el.nativeEvents, <span class="hljs-literal">true</span>)&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// 非作用域插槽，得到 data = &#123; slot: slotName &#125;</span>
  <span class="hljs-comment">// slot target</span>
  <span class="hljs-comment">// only for non-scoped slots</span>
  <span class="hljs-keyword">if</span> (el.slotTarget && !el.slotScope) &#123;
    data += <span class="hljs-string">`slot:<span class="hljs-subst">$&#123;el.slotTarget&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// scoped slots，作用域插槽，data = &#123; scopedSlots: '_u(xxx)' &#125;</span>
  <span class="hljs-keyword">if</span> (el.scopedSlots) &#123;
    data += <span class="hljs-string">`<span class="hljs-subst">$&#123;genScopedSlots(el, el.scopedSlots, state)&#125;</span>,`</span>
  &#125;
  <span class="hljs-comment">// 处理 v-model 属性，得到</span>
  <span class="hljs-comment">// data = &#123; model: &#123; value, callback, expression &#125; &#125;</span>
  <span class="hljs-comment">// component v-model</span>
  <span class="hljs-keyword">if</span> (el.model) &#123;
    data += <span class="hljs-string">`model:&#123;value:<span class="hljs-subst">$&#123;el.model.value
      &#125;</span>,callback:<span class="hljs-subst">$&#123;el.model.callback
      &#125;</span>,expression:<span class="hljs-subst">$&#123;el.model.expression
      &#125;</span>&#125;,`</span>
  &#125;
  <span class="hljs-comment">// inline-template，处理内联模版，得到</span>
  <span class="hljs-comment">// data = &#123; inlineTemplate: &#123; render: function() &#123; render 函数 &#125;, staticRenderFns: [ function() &#123;&#125;, ... ] &#125; &#125;</span>
  <span class="hljs-keyword">if</span> (el.inlineTemplate) &#123;
    <span class="hljs-keyword">const</span> inlineTemplate = genInlineTemplate(el, state)
    <span class="hljs-keyword">if</span> (inlineTemplate) &#123;
      data += <span class="hljs-string">`<span class="hljs-subst">$&#123;inlineTemplate&#125;</span>,`</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 删掉 JSON 字符串最后的 逗号，然后加上闭合括号 &#125;</span>
  data = data.replace(<span class="hljs-regexp">/,$/</span>, <span class="hljs-string">''</span>) + <span class="hljs-string">'&#125;'</span>
  <span class="hljs-comment">// v-bind dynamic argument wrap</span>
  <span class="hljs-comment">// v-bind with dynamic arguments must be applied using the same v-bind object</span>
  <span class="hljs-comment">// merge helper so that class/style/mustUseProp attrs are handled correctly.</span>
  <span class="hljs-keyword">if</span> (el.dynamicAttrs) &#123;
    <span class="hljs-comment">// 存在动态属性，data = `_b(data, tag, 静态属性字符串或者_d(静态属性字符串, 动态属性字符串))`</span>
    data = <span class="hljs-string">`_b(<span class="hljs-subst">$&#123;data&#125;</span>,"<span class="hljs-subst">$&#123;el.tag&#125;</span>",<span class="hljs-subst">$&#123;genProps(el.dynamicAttrs)&#125;</span>)`</span>
  &#125;
  <span class="hljs-comment">// v-bind data wrap</span>
  <span class="hljs-keyword">if</span> (el.wrapData) &#123;
    data = el.wrapData(data)
  &#125;
  <span class="hljs-comment">// v-on data wrap</span>
  <span class="hljs-keyword">if</span> (el.wrapListeners) &#123;
    data = el.wrapListeners(data)
  &#125;
  <span class="hljs-keyword">return</span> data
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">genDirectives</h3>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<blockquote>
<p><strong>阅读建议</strong>：这部分内容也可以放到其它方法后面去读，比如你想深究 v-model 的实现原理</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 运行指令的编译方法，如果指令存在运行时任务，则返回 directives: [&#123; name, rawName, value, arg, modifiers &#125;, ...&#125;] 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genDirectives</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// 获取指令数组</span>
  <span class="hljs-keyword">const</span> dirs = el.directives
  <span class="hljs-comment">// 没有指令则直接结束</span>
  <span class="hljs-keyword">if</span> (!dirs) <span class="hljs-keyword">return</span>
  <span class="hljs-comment">// 指令的处理结果</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-string">'directives:['</span>
  <span class="hljs-comment">// 标记，用于标记指令是否需要在运行时完成的任务，比如 v-model 的 input 事件</span>
  <span class="hljs-keyword">let</span> hasRuntime = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> i, l, dir, needRuntime
  <span class="hljs-comment">// 遍历指令数组</span>
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>, l = dirs.length; i < l; i++) &#123;
    dir = dirs[i]
    needRuntime = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// 获取节点当前指令的处理方法，比如 web 平台的 v-html、v-text、v-model</span>
    <span class="hljs-keyword">const</span> gen: DirectiveFunction = state.directives[dir.name]
    <span class="hljs-keyword">if</span> (gen) &#123;
      <span class="hljs-comment">// 执行指令的编译方法，如果指令还需要运行时完成一部分任务，则返回 true，比如 v-model</span>
      <span class="hljs-comment">// compile-time directive that manipulates AST.</span>
      <span class="hljs-comment">// returns true if it also needs a runtime counterpart.</span>
      needRuntime = !!gen(el, dir, state.warn)
    &#125;
    <span class="hljs-keyword">if</span> (needRuntime) &#123;
      <span class="hljs-comment">// 表示该指令在运行时还有任务</span>
      hasRuntime = <span class="hljs-literal">true</span>
      <span class="hljs-comment">// res = directives:[&#123; name, rawName, value, arg, modifiers &#125;, ...]</span>
      res += <span class="hljs-string">`&#123;name:"<span class="hljs-subst">$&#123;dir.name&#125;</span>",rawName:"<span class="hljs-subst">$&#123;dir.rawName&#125;</span>"<span class="hljs-subst">$&#123;dir.value ? <span class="hljs-string">`,value:(<span class="hljs-subst">$&#123;dir.value&#125;</span>),expression:<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(dir.value)&#125;</span>`</span> : <span class="hljs-string">''</span>
        &#125;</span><span class="hljs-subst">$&#123;dir.arg ? <span class="hljs-string">`,arg:<span class="hljs-subst">$&#123;dir.isDynamicArg ? dir.arg : <span class="hljs-string">`"<span class="hljs-subst">$&#123;dir.arg&#125;</span>"`</span>&#125;</span>`</span> : <span class="hljs-string">''</span>
        &#125;</span><span class="hljs-subst">$&#123;dir.modifiers ? <span class="hljs-string">`,modifiers:<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(dir.modifiers)&#125;</span>`</span> : <span class="hljs-string">''</span>
        &#125;</span>&#125;,`</span>
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (hasRuntime) &#123;
    <span class="hljs-comment">// 也就是说，只有指令存在运行时任务时，才会返回 res</span>
    <span class="hljs-keyword">return</span> res.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>) + <span class="hljs-string">']'</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">genProps</h3>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 遍历属性数组 props，得到所有属性组成的字符串
 * 如果不存在动态属性，则返回：
 *   'attrName,attrVal,...'
 * 如果存在动态属性，则返回：
 *   '_d(静态属性字符串, 动态属性字符串)' 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genProps</span>(<span class="hljs-params">props: <span class="hljs-built_in">Array</span><ASTAttr></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 静态属性</span>
  <span class="hljs-keyword">let</span> staticProps = <span class="hljs-string">``</span>
  <span class="hljs-comment">// 动态属性</span>
  <span class="hljs-keyword">let</span> dynamicProps = <span class="hljs-string">``</span>
  <span class="hljs-comment">// 遍历属性数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < props.length; i++) &#123;
    <span class="hljs-comment">// 属性</span>
    <span class="hljs-keyword">const</span> prop = props[i]
    <span class="hljs-comment">// 属性值</span>
    <span class="hljs-keyword">const</span> value = __WEEX__
      ? generateValue(prop.value)
      : transformSpecialNewlines(prop.value)
    <span class="hljs-keyword">if</span> (prop.dynamic) &#123;
      <span class="hljs-comment">// 动态属性，`dAttrName,dAttrVal,...`</span>
      dynamicProps += <span class="hljs-string">`<span class="hljs-subst">$&#123;prop.name&#125;</span>,<span class="hljs-subst">$&#123;value&#125;</span>,`</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 静态属性，'attrName,attrVal,...'</span>
      staticProps += <span class="hljs-string">`"<span class="hljs-subst">$&#123;prop.name&#125;</span>":<span class="hljs-subst">$&#123;value&#125;</span>,`</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 去掉静态属性最后的逗号</span>
  staticProps = <span class="hljs-string">`&#123;<span class="hljs-subst">$&#123;staticProps.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>)&#125;</span>&#125;`</span>
  <span class="hljs-keyword">if</span> (dynamicProps) &#123;
    <span class="hljs-comment">// 如果存在动态属性则返回：</span>
    <span class="hljs-comment">// _d(静态属性字符串，动态属性字符串)</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`_d(<span class="hljs-subst">$&#123;staticProps&#125;</span>,[<span class="hljs-subst">$&#123;dynamicProps.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>)&#125;</span>])`</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 说明属性数组中不存在动态属性，直接返回静态属性字符串</span>
    <span class="hljs-keyword">return</span> staticProps
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">genHandlers</h3>
<blockquote>
<p>/src/compiler/codegen/events.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成自定义事件的代码
 * 动态：'nativeOn|on_d(staticHandlers, [dynamicHandlers])'
 * 静态：`nativeOn|on$&#123;staticHandlers&#125;`
 */</span>
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genHandlers</span> (<span class="hljs-params">
  events: ASTElementHandlers,
  isNative: boolean
</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 原生：nativeOn，否则为 on</span>
  <span class="hljs-keyword">const</span> prefix = isNative ? <span class="hljs-string">'nativeOn:'</span> : <span class="hljs-string">'on:'</span>
  <span class="hljs-comment">// 静态</span>
  <span class="hljs-keyword">let</span> staticHandlers = <span class="hljs-string">``</span>
  <span class="hljs-comment">// 动态</span>
  <span class="hljs-keyword">let</span> dynamicHandlers = <span class="hljs-string">``</span>
  <span class="hljs-comment">// 遍历 events 数组</span>
  <span class="hljs-comment">// events = [&#123; name: &#123; value: 回调函数名, ... &#125; &#125;]</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> name <span class="hljs-keyword">in</span> events) &#123;
    <span class="hljs-comment">// 获取指定事件的回调函数名，即 this.methodName 或者 [this.methodName1, ...]</span>
    <span class="hljs-keyword">const</span> handlerCode = genHandler(events[name])
    <span class="hljs-keyword">if</span> (events[name] && events[name].dynamic) &#123;
      <span class="hljs-comment">// 动态，dynamicHandles = `eventName,handleCode,...,`</span>
      dynamicHandlers += <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>,<span class="hljs-subst">$&#123;handlerCode&#125;</span>,`</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 静态，staticHandles = `"eventName":handleCode,`</span>
      staticHandlers += <span class="hljs-string">`"<span class="hljs-subst">$&#123;name&#125;</span>":<span class="hljs-subst">$&#123;handlerCode&#125;</span>,`</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 去掉末尾的逗号</span>
  staticHandlers = <span class="hljs-string">`&#123;<span class="hljs-subst">$&#123;staticHandlers.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>)&#125;</span>&#125;`</span>
  <span class="hljs-keyword">if</span> (dynamicHandlers) &#123;
    <span class="hljs-comment">// 动态，on_d(statickHandles, [dynamicHandlers])</span>
    <span class="hljs-keyword">return</span> prefix + <span class="hljs-string">`_d(<span class="hljs-subst">$&#123;staticHandlers&#125;</span>,[<span class="hljs-subst">$&#123;dynamicHandlers.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>)&#125;</span>])`</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 静态，`on$&#123;staticHandlers&#125;`</span>
    <span class="hljs-keyword">return</span> prefix + staticHandlers
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">genStatic</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成静态节点的渲染函数
 *   1、将当前静态节点的渲染函数放到 staticRenderFns 数组中
 *   2、返回一个可执行函数 _m(idx, true or '') 
 */</span>
<span class="hljs-comment">// hoist static sub-trees out</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genStatic</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 标记当前静态节点已经被处理过了</span>
  el.staticProcessed = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// Some elements (templates) need to behave differently inside of a v-pre</span>
  <span class="hljs-comment">// node.  All pre nodes are static roots, so we can use this as a location to</span>
  <span class="hljs-comment">// wrap a state change and reset it upon exiting the pre node.</span>
  <span class="hljs-keyword">const</span> originalPreState = state.pre
  <span class="hljs-keyword">if</span> (el.pre) &#123;
    state.pre = el.pre
  &#125;
  <span class="hljs-comment">// 将静态根节点的渲染函数 push 到 staticRenderFns 数组中，比如：</span>
  <span class="hljs-comment">// [`with(this)&#123;return _c(tag, data, children)&#125;`]</span>
  state.staticRenderFns.push(<span class="hljs-string">`with(this)&#123;return <span class="hljs-subst">$&#123;genElement(el, state)&#125;</span>&#125;`</span>)
  state.pre = originalPreState
  <span class="hljs-comment">// 返回一个可执行函数：_m(idx, true or '')</span>
  <span class="hljs-comment">// idx = 当前静态节点的渲染函数在 staticRenderFns 数组中下标</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_m(<span class="hljs-subst">$&#123;state.staticRenderFns.length - <span class="hljs-number">1</span>
    &#125;</span><span class="hljs-subst">$&#123;el.staticInFor ? <span class="hljs-string">',true'</span> : <span class="hljs-string">''</span>
    &#125;</span>)`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">genOnce</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理带有 v-once 指令的节点，结果会有三种：
 *   1、当前节点存在 v-if 指令，得到一个三元表达式，condition ? render1 : render2
 *   2、当前节点是一个包含在 v-for 指令内部的静态节点，得到 `_o(_c(tag, data, children), number, key)`
 *   3、当前节点就是一个单纯的 v-once 节点，得到 `_m(idx, true of '')`
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genOnce</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 标记当前节点的 v-once 指令已经被处理过了</span>
  el.onceProcessed = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">if</span> (el.if && !el.ifProcessed) &#123;
    <span class="hljs-comment">// 如果含有 v-if 指令 && if 指令没有被处理过，则走这里</span>
    <span class="hljs-comment">// 处理带有 v-if 指令的节点，最终得到一个三元表达式，condition ? render1 : render2 </span>
    <span class="hljs-keyword">return</span> genIf(el, state)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el.staticInFor) &#123;
    <span class="hljs-comment">// 说明当前节点是被包裹在还有 v-for 指令节点内部的静态节点</span>
    <span class="hljs-comment">// 获取 v-for 指令的 key</span>
    <span class="hljs-keyword">let</span> key = <span class="hljs-string">''</span>
    <span class="hljs-keyword">let</span> parent = el.parent
    <span class="hljs-keyword">while</span> (parent) &#123;
      <span class="hljs-keyword">if</span> (parent.for) &#123;
        key = parent.key
        <span class="hljs-keyword">break</span>
      &#125;
      parent = parent.parent
    &#125;
    <span class="hljs-comment">// key 不存在则给出提示，v-once 节点只能用于带有 key 的 v-for 节点内部</span>
    <span class="hljs-keyword">if</span> (!key) &#123;
      process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && state.warn(
        <span class="hljs-string">`v-once can only be used inside v-for that is keyed. `</span>,
        el.rawAttrsMap[<span class="hljs-string">'v-once'</span>]
      )
      <span class="hljs-keyword">return</span> genElement(el, state)
    &#125;
    <span class="hljs-comment">// 生成 `_o(_c(tag, data, children), number, key)`</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`_o(<span class="hljs-subst">$&#123;genElement(el, state)&#125;</span>,<span class="hljs-subst">$&#123;state.onceId++&#125;</span>,<span class="hljs-subst">$&#123;key&#125;</span>)`</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 上面几种情况都不符合，说明就是一个简单的静态节点，和处理静态根节点时的操作一样,</span>
    <span class="hljs-comment">// 得到 _m(idx, true or '')</span>
    <span class="hljs-keyword">return</span> genStatic(el, state)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">genFor</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理节点上的 v-for 指令  
 * 得到 `_l(exp, function(alias, iterator1, iterator2)&#123;return _c(tag, data, children)&#125;)`
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genFor</span>(<span class="hljs-params">
  el: any,
  state: CodegenState,
  altGen?: <span class="hljs-built_in">Function</span>,
  altHelper?: string
</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// v-for 的迭代器，比如 一个数组</span>
  <span class="hljs-keyword">const</span> exp = el.for
  <span class="hljs-comment">// 迭代时的别名</span>
  <span class="hljs-keyword">const</span> alias = el.alias
  <span class="hljs-comment">// iterator 为 v-for = "(item ,idx) in obj" 时会有，比如 iterator1 = idx</span>
  <span class="hljs-keyword">const</span> iterator1 = el.iterator1 ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;el.iterator1&#125;</span>`</span> : <span class="hljs-string">''</span>
  <span class="hljs-keyword">const</span> iterator2 = el.iterator2 ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;el.iterator2&#125;</span>`</span> : <span class="hljs-string">''</span>

  <span class="hljs-comment">// 提示，v-for 指令在组件上时必须使用 key</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
    state.maybeComponent(el) &&
    el.tag !== <span class="hljs-string">'slot'</span> &&
    el.tag !== <span class="hljs-string">'template'</span> &&
    !el.key
  ) &#123;
    state.warn(
      <span class="hljs-string">`<<span class="hljs-subst">$&#123;el.tag&#125;</span> v-for="<span class="hljs-subst">$&#123;alias&#125;</span> in <span class="hljs-subst">$&#123;exp&#125;</span>">: component lists rendered with `</span> +
      <span class="hljs-string">`v-for should have explicit keys. `</span> +
      <span class="hljs-string">`See https://vuejs.org/guide/list.html#key for more info.`</span>,
      el.rawAttrsMap[<span class="hljs-string">'v-for'</span>],
      <span class="hljs-literal">true</span> <span class="hljs-comment">/* tip */</span>
    )
  &#125;

  <span class="hljs-comment">// 标记当前节点上的 v-for 指令已经被处理过了</span>
  el.forProcessed = <span class="hljs-literal">true</span> <span class="hljs-comment">// avoid r</span>
  <span class="hljs-comment">// 得到 `_l(exp, function(alias, iterator1, iterator2)&#123;return _c(tag, data, children)&#125;)`</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;altHelper || <span class="hljs-string">'_l'</span>&#125;</span>((<span class="hljs-subst">$&#123;exp&#125;</span>),`</span> +
    <span class="hljs-string">`function(<span class="hljs-subst">$&#123;alias&#125;</span><span class="hljs-subst">$&#123;iterator1&#125;</span><span class="hljs-subst">$&#123;iterator2&#125;</span>)&#123;`</span> +
    <span class="hljs-string">`return <span class="hljs-subst">$&#123;(altGen || genElement)(el, state)&#125;</span>`</span> +
    <span class="hljs-string">'&#125;)'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">genIf</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理带有 v-if 指令的节点，最终得到一个三元表达式，condition ? render1 : render2 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genIf</span>(<span class="hljs-params">
  el: any,
  state: CodegenState,
  altGen?: <span class="hljs-built_in">Function</span>,
  altEmpty?: string
</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 标记当前节点的 v-if 指令已经被处理过了，避免无效的递归</span>
  el.ifProcessed = <span class="hljs-literal">true</span> <span class="hljs-comment">// avoid recursion</span>
  <span class="hljs-comment">// 得到三元表达式，condition ? render1 : render2</span>
  <span class="hljs-keyword">return</span> genIfConditions(el.ifConditions.slice(), state, altGen, altEmpty)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genIfConditions</span>(<span class="hljs-params">
  conditions: ASTIfConditions,
  state: CodegenState,
  altGen?: <span class="hljs-built_in">Function</span>,
  altEmpty?: string
</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 长度若为空，则直接返回一个空节点渲染函数</span>
  <span class="hljs-keyword">if</span> (!conditions.length) &#123;
    <span class="hljs-keyword">return</span> altEmpty || <span class="hljs-string">'_e()'</span>
  &#125;

  <span class="hljs-comment">// 从 conditions 数组中拿出第一个条件对象 &#123; exp, block &#125;</span>
  <span class="hljs-keyword">const</span> condition = conditions.shift()
  <span class="hljs-comment">// 返回结果是一个三元表达式字符串，condition ? 渲染函数1 : 渲染函数2</span>
  <span class="hljs-keyword">if</span> (condition.exp) &#123;
    <span class="hljs-comment">// 如果 condition.exp 条件成立，则得到一个三元表达式，</span>
    <span class="hljs-comment">// 如果条件不成立，则通过递归的方式找 conditions 数组中下一个元素，</span>
    <span class="hljs-comment">// 直到找到条件成立的元素，然后返回一个三元表达式</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`(<span class="hljs-subst">$&#123;condition.exp&#125;</span>)?<span class="hljs-subst">$&#123;genTernaryExp(condition.block)
      &#125;</span>:<span class="hljs-subst">$&#123;genIfConditions(conditions, state, altGen, altEmpty)
      &#125;</span>`</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;genTernaryExp(condition.block)&#125;</span>`</span>
  &#125;

  <span class="hljs-comment">// v-if with v-once should generate code like (a)?_m(0):_m(1)</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genTernaryExp</span>(<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-keyword">return</span> altGen
      ? altGen(el, state)
      : el.once
        ? genOnce(el, state)
        : genElement(el, state)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">genSlot</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成插槽的渲染函数，得到
 * _t(slotName, children, attrs, bind)
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genSlot</span>(<span class="hljs-params">el: ASTElement, state: CodegenState</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 插槽名称</span>
  <span class="hljs-keyword">const</span> slotName = el.slotName || <span class="hljs-string">'"default"'</span>
  <span class="hljs-comment">// 生成所有的子节点</span>
  <span class="hljs-keyword">const</span> children = genChildren(el, state)
  <span class="hljs-comment">// 结果字符串，_t(slotName, children, attrs, bind)</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-string">`_t(<span class="hljs-subst">$&#123;slotName&#125;</span><span class="hljs-subst">$&#123;children ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;children&#125;</span>`</span> : <span class="hljs-string">''</span>&#125;</span>`</span>
  <span class="hljs-keyword">const</span> attrs = el.attrs || el.dynamicAttrs
    ? genProps((el.attrs || []).concat(el.dynamicAttrs || []).map(<span class="hljs-function"><span class="hljs-params">attr</span> =></span> (&#123;
      <span class="hljs-comment">// slot props are camelized</span>
      <span class="hljs-attr">name</span>: camelize(attr.name),
      <span class="hljs-attr">value</span>: attr.value,
      <span class="hljs-attr">dynamic</span>: attr.dynamic
    &#125;)))
    : <span class="hljs-literal">null</span>
  <span class="hljs-keyword">const</span> bind = el.attrsMap[<span class="hljs-string">'v-bind'</span>]
  <span class="hljs-keyword">if</span> ((attrs || bind) && !children) &#123;
    res += <span class="hljs-string">`,null`</span>
  &#125;
  <span class="hljs-keyword">if</span> (attrs) &#123;
    res += <span class="hljs-string">`,<span class="hljs-subst">$&#123;attrs&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">if</span> (bind) &#123;
    res += <span class="hljs-string">`<span class="hljs-subst">$&#123;attrs ? <span class="hljs-string">''</span> : <span class="hljs-string">',null'</span>&#125;</span>,<span class="hljs-subst">$&#123;bind&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">return</span> res + <span class="hljs-string">')'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">genComponent</h2>
<blockquote>
<p>/src/compiler/codegen/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// componentName is el.component, take it as argument to shun flow's pessimistic refinement</span>
<span class="hljs-comment">/**
 * 生成动态组件的渲染函数
 * 返回 `_c(compName, data, children)`
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genComponent</span>(<span class="hljs-params">
  componentName: string,
  el: ASTElement,
  state: CodegenState
</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-comment">// 所有的子节点</span>
  <span class="hljs-keyword">const</span> children = el.inlineTemplate ? <span class="hljs-literal">null</span> : genChildren(el, state, <span class="hljs-literal">true</span>)
  <span class="hljs-comment">// 返回 `_c(compName, data, children)`</span>
  <span class="hljs-comment">// compName 是 is 属性的值</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_c(<span class="hljs-subst">$&#123;componentName&#125;</span>,<span class="hljs-subst">$&#123;genData(el, state)&#125;</span><span class="hljs-subst">$&#123;children ? <span class="hljs-string">`,<span class="hljs-subst">$&#123;children&#125;</span>`</span> : <span class="hljs-string">''</span>
    &#125;</span>)`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">总结</h1>
<ul>
<li>
<p><strong>面试官 问</strong>：简单说一下 Vue 的编译器都做了什么？</p>
<p><strong>答</strong>：</p>
<p>Vue 的编译器做了三件事情：</p>
<ul>
<li>
<p>将组件的 html 模版解析成 AST 对象</p>
</li>
<li>
<p>优化，遍历 AST，为每个节点做静态标记，标记其是否为静态节点，然后进一步标记出静态根节点，这样在后续更新的过程中就可以跳过这些静态节点了；标记静态根用于生成渲染函数阶段，生成静态根节点的渲染函数</p>
</li>
<li>
<p>从 AST 生成运行渲染函数，即大家说的 render，其实还有一个，就是 staticRenderFns 数组，里面存放了所有的静态节点的渲染函数</p>
</li>
</ul>
</li>
</ul>
<hr>
<ul>
<li>
<p><strong>面试官</strong>：详细说一下渲染函数的生成过程</p>
<p><strong>答</strong>：</p>
<p>大家一说到渲染函数，基本上说的就是 render 函数，其实编译器生成的渲染有两类：</p>
<ul>
<li>
<p>第一类就是一个 render 函数，负责生成动态节点的 vnode</p>
</li>
<li>
<p>第二类是放在一个叫 staticRenderFns 数组中的静态渲染函数，这些函数负责生成静态节点的 vnode</p>
</li>
</ul>
<p>渲染函数生成的过程，其实就是在遍历 AST 节点，通过递归的方式，处理每个节点，最后生成形如：<code>_c(tag, attr, children, normalizationType)</code> 的结果。tag 是标签名，attr 是属性对象，children 是子节点组成的数组，其中每个元素的格式都是 <code>_c(tag, attr, children, normalizationTYpe)</code> 的形式，normalization 表示节点的规范化类型，是一个数字 0、1、2，不重要。</p>
<p>在处理 AST 节点过程中需要大家重点关注也是面试中常见的问题有：</p>
<ul>
<li>
<p>静态节点是怎么处理的</p>
<p>静态节点的处理分为两步：</p>
<ul>
<li>
<p>将生成静态节点 vnode 函数放到 staticRenderFns 数组中</p>
</li>
<li>
<p>返回一个 _m(idx) 的可执行函数，意思是执行 staticRenderFns 数组中下标为 idx 的函数，生成静态节点的 vnode</p>
</li>
</ul>
</li>
<li>
<p>v-once、v-if、v-for、组件 等都是怎么处理的</p>
<ul>
<li>
<p>单纯的 v-once 节点处理方式和静态节点一致</p>
</li>
<li>
<p>v-if 节点的处理结果是一个三元表达式</p>
</li>
<li>
<p>v-for 节点的处理结果是可执行的 _l 函数，该函数负责生成 v-for 节点的 vnode</p>
</li>
<li>
<p>组件的处理结果和普通元素一样，得到的是形如 <code>_c(compName)</code> 的可执行代码，生成组件的 vnode</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr>
<p>到这里，Vue 编译器 的源码解读就结束了。相信大家在阅读的过程中不免会产生云里雾里的感觉。这个没什么，编译器这块儿确实是比较复杂，可以说是整个框架最难理解也是代码量最大的一部分了。一定要静下心来多读几遍，遇到无法理解的地方，一定要勤动手，通过示例代码加断点调试的方式帮助自己理解。</p>
<p>当你读完几遍以后，这时候情况可能就会好一些，但是有些地方可能还会有些晕，这没事，正常。毕竟这是一个框架的编译器，要处理的东西太多太多了，你只需要理解其核心思想（模版解析、静态标记、代码生成）就可以了。后面会有 <strong>手写 Vue 系列</strong>，编译器这部分会有一个简版的实现，帮助加深对这部分知识的理解。</p>
<p>编译器读完以后，会发现有个不明白的地方：编译器最后生成的代码都是经过 <code>with</code> 包裹的，比如:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>&#123;&#123; item &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过编译后生成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">with</span> (<span class="hljs-built_in">this</span>) &#123;
  <span class="hljs-keyword">return</span> _c(
    <span class="hljs-string">'div'</span>,
    &#123;
      <span class="hljs-attr">attrs</span>:
      &#123;
        <span class="hljs-string">"id"</span>: <span class="hljs-string">"app"</span>
      &#125;
    &#125;,
    _l(
      (arr),
      <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item</span>) </span>&#123;
        <span class="hljs-keyword">return</span> _c(
          <span class="hljs-string">'div'</span>,
          &#123;
            <span class="hljs-attr">key</span>: item
          &#125;,
          [_v(_s(item))]
        )
      &#125;
    ),
    <span class="hljs-number">0</span>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>都知道，<code>with</code> 语句可以扩展作用域链，所以生成的代码中的 <code>_c、_l、_v、_s</code> 都是 this 上一些方法，也就是说在运行时执行这些方法可以生成各个节点的 vnode。</p>
<p>所以联系前面的知识，响应式数据更新的整个执行过程就是：</p>
<ul>
<li>
<p>响应式拦截到数据的更新</p>
</li>
<li>
<p>dep 通知 watcher 进行异步更新</p>
</li>
<li>
<p>watcher 更新时执行组件更新函数 updateComponent</p>
</li>
<li>
<p>首先执行 vm._render 生成组件的 vnode，这时就会执行编译器生成的函数</p>
</li>
<li>
<p><strong>问题</strong>：</p>
<ul>
<li>
<p>渲染函数中的 <code>_c、_l、、_v、_s</code> 等方法是什么？</p>
</li>
<li>
<p>它们是如何生成 vnode 的？</p>
</li>
</ul>
</li>
</ul>
<p>下一篇文章 <strong>Vue 源码解读（11）—— render helper</strong> 将会带来这部分知识的详细解读，也是面试经常被问题的：比如：<code>v-for</code> 的原理是什么？</p>
<h1 data-id="heading-21">配套视频</h1>
<p><a href="https://www.bilibili.com/video/BV1zf4y1a7BQ?share_source=copy_web" target="_blank" rel="nofollow noopener noreferrer">Vue 源码解读（10）—— 编译器 之 生成渲染函数</a></p>
<h1 data-id="heading-22">求关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-23">链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/post/6949370458793836580" target="_blank">Vue 源码解读（1）—— 前言</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6950084496515399717" target="_blank">Vue 源码解读（2）—— Vue 初始化过程</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6950826293923414047" target="_blank">Vue 源码解读（3）—— 响应式原理</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6951568091893465102" target="_blank">Vue 源码解读（4）—— 异步更新</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952643167715852319" target="_blank">Vue 源码解读（5）—— 全局 API</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6953503236254859294" target="_blank">Vue 源码解读（6）—— 实例方法</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6954923081462710309" target="_blank">Vue 源码解读（7）—— Hook Event</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6960465810682806308" target="_blank">Vue 源码解读（9）—— 编译器 之 优化</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6961545472204865572" target="_blank">Vue 源码解读（10）—— 编译器 之 生成渲染函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6961545472204865572">Vue 源码解读（11）—— render helper</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6961545472204865572">Vue 源码解读（12）—— patch</a></p>
</li>
</ul>
<h1 data-id="heading-24">学习交流群</h1>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank">链接</a></p></div>  
</div>
            