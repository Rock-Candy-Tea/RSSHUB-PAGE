
---
title: '手写 Vue2 系列 之 初始渲染'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/317fac56603347f99bf7295351c27476~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 16:04:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/317fac56603347f99bf7295351c27476~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇文章 <a href="https://juejin.cn/post/6980129607353630756" target="_blank">手写 Vue2 系列 之 编译器</a> 中完成了从模版字符串到 render 函数的工作。当我们得到 render 函数之后，接下来就该进入到真正的挂载阶段了：</p>
<p>挂载 -> 实例化渲染 Watcher -> 执行 updateComponent 方法 -> 执行 render 函数生成 VNode -> 执行 patch 进行首次渲染 -> 递归遍历 VNode 创建各个节点并处理节点上的普通属性和指令 -> 如果节点是自定义组件则创建组件实例 -> 进行组件的初始化、挂载 -> 最终所有 VNode 变成真实的 DOM 节点并替换掉页面上的模版内容 -> 完成初始渲染</p>
<h1 data-id="heading-1">目标</h1>
<p>所以，本篇文章目标就是实现上面描述的整个过成，完成初始渲染。整个过程中涉及如下知识点：</p>
<ul>
<li>
<p>render helper</p>
</li>
<li>
<p>VNode</p>
</li>
<li>
<p>patch 初始渲染</p>
</li>
<li>
<p>指令(v-model、v-bind、v-on)的处理</p>
</li>
<li>
<p>实例化子组件</p>
</li>
<li>
<p>插槽的处理</p>
</li>
</ul>
<h1 data-id="heading-2">实现</h1>
<p>接下来就正式进入代码实现过程，一步步实现上述所有内容，完成页面的初始渲染。</p>
<h2 data-id="heading-3">mount</h2>
<blockquote>
<p>/src/compiler/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 编译器
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!vm.$options.render) &#123; <span class="hljs-comment">// 没有提供 render 选项，则编译生成 render 函数</span>
    <span class="hljs-comment">// ...</span>
  &#125;
  mountComponent(vm)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">mountComponent</h2>
<blockquote>
<p>/src/compiler/mountComponent.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm Vue 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-comment">// 更新组件的的函数</span>
  <span class="hljs-keyword">const</span> updateComponent = <span class="hljs-function">() =></span> &#123;
    vm._update(vm._render())
  &#125;

  <span class="hljs-comment">// 实例化一个渲染 Watcher，当响应式数据更新时，这个更新函数会被执行</span>
  <span class="hljs-keyword">new</span> Watcher(updateComponent)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">vm._render</h2>
<blockquote>
<p>/src/compiler/mountComponent.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 负责执行 vm.$options.render 函数
 */</span>
Vue.prototype._render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 给 render 函数绑定 this 上下文为 Vue 实例</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$options.render.apply(<span class="hljs-built_in">this</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">render helper</h3>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 在 Vue 实例上安装运行时的渲染帮助函数，比如 _c、_v，这些函数会生成 Vnode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VueContructor&#125;</span> </span>target Vue 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderHelper</span>(<span class="hljs-params">target</span>) </span>&#123;
  target._c = createElement
  target._v = createTextNode
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">createElement</h3>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 根据标签信息创建 Vnode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>tag 标签名 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Map&#125;</span> </span>attr 标签的属性 Map 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array<Render>&#125;</span> </span>children 所有的子节点的渲染函数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">tag, attr, children</span>) </span>&#123;
  <span class="hljs-keyword">return</span> VNode(tag, attr, children, <span class="hljs-built_in">this</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">createTextNode</h3>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 生成文本节点的 VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>textAst 文本节点的 AST 对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">textAst</span>) </span>&#123;
  <span class="hljs-keyword">return</span> VNode(<span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-built_in">this</span>, textAst)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">VNode</h3>
<blockquote>
<p>/src/compiler/vnode.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>tag 标签名
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attr 属性 Map 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>children 子节点组成的 VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>text 文本节点的 ast 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>context Vue 实例
 * <span class="hljs-doctag">@returns <span class="hljs-variable">VNode</span></span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">VNode</span>(<span class="hljs-params">tag, attr, children, context, text = <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 标签</span>
    tag,
    <span class="hljs-comment">// 属性 Map 对象</span>
    attr,
    <span class="hljs-comment">// 父节点</span>
    <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 子节点组成的 Vnode 数组</span>
    children,
    <span class="hljs-comment">// 文本节点的 Ast 对象</span>
    text,
    <span class="hljs-comment">// Vnode 的真实节点</span>
    <span class="hljs-attr">elm</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// Vue 实例</span>
    context
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">vm._update</h2>
<blockquote>
<p>/src/compiler/mountComponent.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// 老的 VNode</span>
  <span class="hljs-keyword">const</span> prevVNode = <span class="hljs-built_in">this</span>._vnode
  <span class="hljs-comment">// 新的 VNode</span>
  <span class="hljs-built_in">this</span>._vnode = vnode
  <span class="hljs-keyword">if</span> (!prevVNode) &#123;
    <span class="hljs-comment">// 老的 VNode 不存在，则说明时首次渲染根组件</span>
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">this</span>.__patch__(<span class="hljs-built_in">this</span>.$el, vnode)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 后续更新组件或者首次渲染子组件，都会走这里</span>
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">this</span>.__patch__(prevVNode, vnode)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">安装 __patch__、render helper</h2>
<blockquote>
<p>/src/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 初始化配置对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options 
 */</span>
Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  initData(<span class="hljs-built_in">this</span>)
  <span class="hljs-comment">// 安装运行时的渲染工具函数</span>
  renderHelper(<span class="hljs-built_in">this</span>)
  <span class="hljs-comment">// 在实例上安装 patch 函数</span>
  <span class="hljs-built_in">this</span>.__patch__ = patch
  <span class="hljs-comment">// 如果存在 el 配置项，则调用 $mount 方法编译模版</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.el) &#123;
    <span class="hljs-built_in">this</span>.$mount()
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">patch</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 初始渲染和后续更新的入口
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VNode&#125;</span> </span>oldVnode 老的 VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VNode&#125;</span> </span>vnode 新的 VNode
 * <span class="hljs-doctag">@returns </span>VNode 的真实 DOM 节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (oldVnode && !vnode) &#123;
    <span class="hljs-comment">// 老节点存在，新节点不存在，则销毁组件</span>
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">if</span> (!oldVnode) &#123; <span class="hljs-comment">// oldVnode 不存在，说明是子组件首次渲染</span>
    createElm(vnode)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">if</span> (oldVnode.nodeType) &#123; <span class="hljs-comment">// 真实节点，则表示首次渲染根组件</span>
      <span class="hljs-comment">// 父节点，即 body</span>
      <span class="hljs-keyword">const</span> parent = oldVnode.parentNode
      <span class="hljs-comment">// 参考节点，即老的 vnode 的下一个节点 —— script，新节点要插在 script 的前面</span>
      <span class="hljs-keyword">const</span> referNode = oldVnode.nextSibling
      <span class="hljs-comment">// 创建元素</span>
      createElm(vnode, parent, referNode)
      <span class="hljs-comment">// 移除老的 vnode</span>
      parent.removeChild(oldVnode)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'update'</span>)
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> vnode.elm
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">createElm</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 创建元素
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>parent VNode 的父节点，真实节点
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode, parent, referNode</span>) </span>&#123;
  <span class="hljs-comment">// 记录节点的父节点</span>
  vnode.parent = parent
  <span class="hljs-comment">// 创建自定义组件，如果是非组件，则会继续后面的流程</span>
  <span class="hljs-keyword">if</span> (createComponent(vnode)) <span class="hljs-keyword">return</span>

  <span class="hljs-keyword">const</span> &#123; attr, children, text &#125; = vnode
  <span class="hljs-keyword">if</span> (text) &#123; <span class="hljs-comment">// 文本节点</span>
    <span class="hljs-comment">// 创建文本节点，并插入到父节点内</span>
    vnode.elm = createTextNode(vnode)
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 元素节点</span>
    <span class="hljs-comment">// 创建元素，在 vnode 上记录对应的 dom 节点</span>
    vnode.elm = <span class="hljs-built_in">document</span>.createElement(vnode.tag)
    <span class="hljs-comment">// 给元素设置属性</span>
    setAttribute(attr, vnode)
    <span class="hljs-comment">// 递归创建子节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = children.length; i < len; i++) &#123;
      createElm(children[i], vnode.elm)
    &#125;
  &#125;
  <span class="hljs-comment">// 如果存在 parent，则将创建的节点插入到父节点内</span>
  <span class="hljs-keyword">if</span> (parent) &#123;
    <span class="hljs-keyword">const</span> elm = vnode.elm
    <span class="hljs-keyword">if</span> (referNode) &#123;
      parent.insertBefore(elm, referNode)
    &#125; <span class="hljs-keyword">else</span> &#123;
      parent.appendChild(elm)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">createTextNode</h3>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 创建文本节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>textVNode 文本节点的 VNode
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">textVNode</span>) </span>&#123;
  <span class="hljs-keyword">let</span> &#123; text &#125; = textVNode, textNode = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">if</span> (text.expression) &#123;
    <span class="hljs-comment">// 存在表达式，这个表达式的值是一个响应式数据</span>
    <span class="hljs-keyword">const</span> value = textVNode.context[text.expression]
    textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> ? <span class="hljs-built_in">JSON</span>.stringify(value) : <span class="hljs-built_in">String</span>(value))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 纯文本</span>
    textNode = <span class="hljs-built_in">document</span>.createTextNode(text.text)
  &#125;
  <span class="hljs-keyword">return</span> textNode
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">setAttribute</h3>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 给节点设置属性
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attr 属性 Map 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">vnode</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setAttribute</span>(<span class="hljs-params">attr, vnode</span>) </span>&#123;
  <span class="hljs-comment">// 遍历属性，如果是普通属性，直接设置，如果是指令，则特殊处理</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> name <span class="hljs-keyword">in</span> attr) &#123;
    <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'vModel'</span>) &#123;
      <span class="hljs-comment">// v-model 指令</span>
      <span class="hljs-keyword">const</span> &#123; tag, value &#125; = attr.vModel
      setVModel(tag, value, vnode)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'vBind'</span>) &#123;
      <span class="hljs-comment">// v-bind 指令</span>
      setVBind(vnode)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'vOn'</span>) &#123;
      <span class="hljs-comment">// v-on 指令</span>
      setVOn(vnode)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 普通属性</span>
      vnode.elm.setAttribute(name, attr[name])
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">setVModel</h4>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * v-model 的原理
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>tag 节点的标签名
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 属性值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>node 节点
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setVModel</span>(<span class="hljs-params">tag, value, vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">context</span>: vm, elm &#125; = vnode
  <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'select'</span>) &#123;
    <span class="hljs-comment">// 下拉框，<select></select></span>
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 利用 promise 延迟设置，直接设置不行，</span>
      <span class="hljs-comment">// 因为这会儿 option 元素还没创建</span>
      elm.value = vm[value]
    &#125;)
    elm.addEventListener(<span class="hljs-string">'change'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      vm[value] = elm.value
    &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'input'</span> && vnode.elm.type === <span class="hljs-string">'text'</span>) &#123;
    <span class="hljs-comment">// 文本框，<input type="text" /></span>
    elm.value = vm[value]
    elm.addEventListener(<span class="hljs-string">'input'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      vm[value] = elm.value
    &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'input'</span> && vnode.elm.type === <span class="hljs-string">'checkbox'</span>) &#123;
    <span class="hljs-comment">// 选择框，<input type="checkbox" /></span>
    elm.checked = vm[value]
    elm.addEventListener(<span class="hljs-string">'change'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      vm[value] = elm.checked
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">setVBind</h4>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * v-bind 原理
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">vnode</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setVBind</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">attr</span>: &#123; vBind &#125;, elm, <span class="hljs-attr">context</span>: vm &#125; = vnode
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> attrName <span class="hljs-keyword">in</span> vBind) &#123;
    elm.setAttribute(attrName, vm[vBind[attrName]])
    elm.removeAttribute(<span class="hljs-string">`v-bind:<span class="hljs-subst">$&#123;attrName&#125;</span>`</span>)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">setVOn</h4>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * v-on 原理
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setVOn</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">attr</span>: &#123; vOn &#125;, elm, <span class="hljs-attr">context</span>: vm &#125; = vnode
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> eventName <span class="hljs-keyword">in</span> vOn) &#123;
    elm.addEventListener(eventName, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
      vm.$options.methods[vOn[eventName]].apply(vm, args)
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">createComponent</h3>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 创建自定义组件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">vnode</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (vnode.tag && !isReserveTag(vnode.tag)) &#123; <span class="hljs-comment">// 非保留节点，则说明是组件</span>
    <span class="hljs-comment">// 获取组件配置信息</span>
    <span class="hljs-keyword">const</span> &#123; tag, <span class="hljs-attr">context</span>: &#123; <span class="hljs-attr">$options</span>: &#123; components &#125; &#125; &#125; = vnode
    <span class="hljs-keyword">const</span> compOptions = components[tag]
    <span class="hljs-keyword">const</span> compIns = <span class="hljs-keyword">new</span> Vue(compOptions)
    <span class="hljs-comment">// 将父组件的 VNode 放到子组件的实例上</span>
    compIns._parentVnode = vnode
    <span class="hljs-comment">// 挂载子组件</span>
    compIns.$mount()
    <span class="hljs-comment">// 记录子组件 vnode 的父节点信息</span>
    compIns._vnode.parent = vnode.parent
    <span class="hljs-comment">// 将子组件添加到父节点内</span>
    vnode.parent.appendChild(compIns._vnode.elm)
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">isReserveTag</h2>
<blockquote>
<p>/src/utils.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 是否为平台保留节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isReserveTag</span>(<span class="hljs-params">tagName</span>) </span>&#123;
  <span class="hljs-keyword">const</span> reserveTag = [<span class="hljs-string">'div'</span>, <span class="hljs-string">'h3'</span>, <span class="hljs-string">'span'</span>, <span class="hljs-string">'input'</span>, <span class="hljs-string">'select'</span>, <span class="hljs-string">'option'</span>, <span class="hljs-string">'p'</span>, <span class="hljs-string">'button'</span>, <span class="hljs-string">'template'</span>]
  <span class="hljs-keyword">return</span> reserveTag.includes(tagName)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">插槽原理</h2>
<p>以下示例是插槽的常用方式。插槽的原理其实很简单，只是实现起来稍微有些麻烦罢了。</p>
<ul>
<li>
<p>解析</p>
<p>如果组件标签有子节点，在解析的时候将这些子节点，解析成一个特定的数据结构，该结构中包含了插槽的全部信息，然后将该数据结构放到父节点的属性上，其实就是找个地方存放这些信息，然后在 renderSlot 中使用时取出来。当然这个解析过程是发生在父组件的解析过程中的。</p>
</li>
<li>
<p>生成渲染函数</p>
<p>在生成子组件的渲染函数阶段，如果碰到 slot 标签，则返回一个 <code>_t</code> 的渲染函数，函数接收两个参数：属性的 JSON 字符串形式，slot 标签的所有子节点的渲染函数组成的 children 数组。</p>
</li>
<li>
<p>render helper</p>
<p>在执行子组件的渲染函数时，如果执行到 <code>vm._t</code>，就会调用 <code>renderSlot</code> 方法，该方法会返回插槽的 VNode，然后进入子组件的 patch 阶段，将这些 VNode 变成真实的 DOM 并渲染到页面上。</p>
</li>
</ul>
<p>以上就是插槽的原理，然后接下来实现的时候，在某些地方可能会稍微有点绕，多多少少是因为整体架构存在一些问题，所以里面会有一些修补性质的代码，这些代码你可以理解为为了实现插槽功能，而写的一点业务代码。你只需要把住插槽的本质即可。</p>
<h3 data-id="heading-22">示例</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- comp --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"slot1"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>插槽默认内容<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"slot2"</span> <span class="hljs-attr">v-bind:test</span>=<span class="hljs-string">"xx"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>插槽默认内容<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">comp</span>></span><span class="hljs-tag"></<span class="hljs-name">comp</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">comp</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:slot2</span>=<span class="hljs-string">"xx"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>作用域插槽，通过插槽从父组件给子组件传递内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">comp</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">parse</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processElement</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>

    <span class="hljs-comment">// 处理插槽内容</span>
    processSlotContent(curEle)

    <span class="hljs-comment">// 节点处理完以后让其和父节点产生关系</span>
    <span class="hljs-keyword">if</span> (stackLen) &#123;
      stack[stackLen - <span class="hljs-number">1</span>].children.push(curEle)
      curEle.parent = stack[stackLen - <span class="hljs-number">1</span>]
      <span class="hljs-comment">// 如果节点存在 slotName，则说明该节点是组件传递给插槽的内容</span>
      <span class="hljs-comment">// 将插槽信息放到组件节点的 rawAttr.scopedSlots 对象上</span>
      <span class="hljs-comment">// 而这些信息在生成组件插槽的 VNode 时（renderSlot）会用到</span>
      <span class="hljs-keyword">if</span> (curEle.slotName) &#123;
        <span class="hljs-keyword">const</span> &#123; parent, slotName, scopeSlot, children &#125; = curEle
        <span class="hljs-comment">// 这里关于 children 的操作，只是单纯为了避开 JSON.stringify 的循环引用问题</span>
        <span class="hljs-comment">// 因为生成渲染函数时需要对 attr 执行 JSON.stringify 方法</span>
        <span class="hljs-keyword">const</span> slotInfo = &#123;
          slotName, scopeSlot, <span class="hljs-attr">children</span>: children.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            <span class="hljs-keyword">delete</span> item.parent
            <span class="hljs-keyword">return</span> item
          &#125;)
        &#125;
        <span class="hljs-keyword">if</span> (parent.rawAttr.scopedSlots) &#123;
          parent.rawAttr.scopedSlots[curEle.slotName] = slotInfo
        &#125; <span class="hljs-keyword">else</span> &#123;
          parent.rawAttr.scopedSlots = &#123; [curEle.slotName]: slotInfo &#125;
        &#125;
      &#125;
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">processSlotContent</h3>
<blockquote>
<p>/src/compiler/parse.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理插槽
 * <scope-slot>
 *   <template v-slot:default="scopeSlot">
 *     <div>&#123;&#123; scopeSlot &#125;&#125;</div>
 *   </template>
 * </scope-slot>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123; AST &#125;</span> </span>el 节点的 AST 对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processSlotContent</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-comment">// 注意，具有 v-slot:xx 属性的 template 只能是组件的根元素，这里不做判断</span>
  <span class="hljs-keyword">if</span> (el.tag === <span class="hljs-string">'template'</span>) &#123; <span class="hljs-comment">// 获取插槽信息</span>
    <span class="hljs-comment">// 属性 map 对象</span>
    <span class="hljs-keyword">const</span> attrMap = el.rawAttr
    <span class="hljs-comment">// 遍历属性 map 对象，找出其中的 v-slot 指令信息</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> attrMap) &#123;
      <span class="hljs-keyword">if</span> (key.match(<span class="hljs-regexp">/v-slot:(.*)/</span>)) &#123; <span class="hljs-comment">// 说明 template 标签上 v-slot 指令</span>
        <span class="hljs-comment">// 获取指令后的插槽名称和值，比如: v-slot:default=xx</span>
        <span class="hljs-comment">// default</span>
        <span class="hljs-keyword">const</span> slotName = el.slotName = <span class="hljs-built_in">RegExp</span>.$1
        <span class="hljs-comment">// xx</span>
        el.scopeSlot = attrMap[<span class="hljs-string">`v-slot:<span class="hljs-subst">$&#123;slotName&#125;</span>`</span>]
        <span class="hljs-comment">// 直接 return，因为该标签上只可能有一个 v-slot 指令</span>
        <span class="hljs-keyword">return</span>
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">generate</h3>
<blockquote>
<p>/src/compiler/generate.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 解析 ast 生成 渲染函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>ast 语法树 
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;string&#125;</span> </span>渲染函数的字符串形式
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genElement</span>(<span class="hljs-params">ast</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 处理子节点，得到一个所有子节点渲染函数组成的数组</span>
  <span class="hljs-keyword">const</span> children = genChildren(ast)

  <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'slot'</span>) &#123;
    <span class="hljs-comment">// 生成插槽的处理函数</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`_t(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(attrs)&#125;</span>, [<span class="hljs-subst">$&#123;children&#125;</span>])`</span>
  &#125;

  <span class="hljs-comment">// 生成 VNode 的可执行方法</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`_c('<span class="hljs-subst">$&#123;tag&#125;</span>', <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(attrs)&#125;</span>, [<span class="hljs-subst">$&#123;children&#125;</span>])`</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">renderHelper</h4>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 在 Vue 实例上安装运行时的渲染帮助函数，比如 _c、_v，这些函数会生成 Vnode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VueContructor&#125;</span> </span>target Vue 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderHelper</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  target._t = renderSlot
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">renderSlot</h4>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 插槽的原理其实很简单，难点在于实现
 * 其原理就是生成 VNode，难点在于生成 VNode 之前的各种解析，也就是数据准备阶段
 * 生成插槽的的 VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attrs 插槽的属性
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>children 插槽所有子节点的 ast 组成的数组
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderSlot</span>(<span class="hljs-params">attrs, children</span>) </span>&#123;
  <span class="hljs-comment">// 父组件 VNode 的 attr 信息</span>
  <span class="hljs-keyword">const</span> parentAttr = <span class="hljs-built_in">this</span>._parentVnode.attr
  <span class="hljs-keyword">let</span> vnode = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">if</span> (parentAttr.scopedSlots) &#123; <span class="hljs-comment">// 说明给当前组件的插槽传递了内容</span>
    <span class="hljs-comment">// 获取插槽信息</span>
    <span class="hljs-keyword">const</span> slotName = attrs.name
    <span class="hljs-keyword">const</span> slotInfo = parentAttr.scopedSlots[slotName]
    <span class="hljs-comment">// 这里的逻辑稍微有点绕，建议打开调试，查看一下数据结构，理清对应的思路</span>
    <span class="hljs-comment">// 这里比较绕的逻辑完全是为了实现插槽这个功能，和插槽本身的原理没关系</span>
    <span class="hljs-built_in">this</span>[slotInfo.scopeSlot] = <span class="hljs-built_in">this</span>[<span class="hljs-built_in">Object</span>.keys(attrs.vBind)[<span class="hljs-number">0</span>]]
    vnode = genVNode(slotInfo.children, <span class="hljs-built_in">this</span>)
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 插槽默认内容</span>
    <span class="hljs-comment">// 将 children 变成 vnode 数组</span>
    vnode = genVNode(children, <span class="hljs-built_in">this</span>)
  &#125;

  <span class="hljs-comment">// 如果 children 长度为 1，则说明插槽只有一个子节点</span>
  <span class="hljs-keyword">if</span> (children.length === <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> vnode[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">return</span> createElement.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">'div'</span>, &#123;&#125;, vnode)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">genVNode</h4>
<blockquote>
<p>/src/compiler/renderHelper.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将一批 ast 节点(数组)转换成 vnode 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array<Ast>&#125;</span> </span>childs 节点数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 组件实例
 * <span class="hljs-doctag">@returns </span>vnode 数组
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genVNode</span>(<span class="hljs-params">childs, vm</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode = []
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = childs.length; i < len; i++) &#123;
    <span class="hljs-keyword">const</span> &#123; tag, attr, children, text &#125; = childs[i]
    <span class="hljs-keyword">if</span> (text) &#123; <span class="hljs-comment">// 文本节点</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> text === <span class="hljs-string">'string'</span>) &#123; <span class="hljs-comment">// text 为字符串</span>
        <span class="hljs-comment">// 构造文本节点的 AST 对象</span>
        <span class="hljs-keyword">const</span> textAst = &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-number">3</span>,
          text,
        &#125;
        <span class="hljs-keyword">if</span> (text.match(<span class="hljs-regexp">/&#123;&#123;(.*)&#125;&#125;/</span>)) &#123;
          <span class="hljs-comment">// 说明是表达式</span>
          textAst.expression = <span class="hljs-built_in">RegExp</span>.$1.trim()
        &#125;
        vnode.push(createTextNode.call(vm, textAst))
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// text 为文本节点的 ast 对象</span>
        vnode.push(createTextNode.call(vm, text))
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 元素节点</span>
      vnode.push(createElement.call(vm, tag, attr, genVNode(children, vm)))
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> vnode
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-29">结果</h1>
<p>好了，到这里，模版的初始渲染就已经完成了，如果你能看到如下效果图，则说明一切正常。因为整个过程涉及的内容还是比较多的，如果觉得某些地方不太清楚，建议再看看，仔细梳理下整个流程。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/317fac56603347f99bf7295351c27476~tplv-k3u1fbpfcp-watermark.image" alt="Jun-18-2021 07-35-17.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，原始标签、自定义组件、插槽都已经完整的渲染到了页面上，完成了初始渲染之后，接下来就该去实现后续的更新过程了，也就是下一篇 <a href="https://juejin.cn/post/6981224810386833422">手写 Vue2 系列 之 patch —— diff</a>。</p>
<h1 data-id="heading-30">关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-31">链接</h1>
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
            