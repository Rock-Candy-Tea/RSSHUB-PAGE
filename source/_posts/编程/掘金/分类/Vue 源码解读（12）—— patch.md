
---
title: 'Vue 源码解读（12）—— patch'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9929'
author: 掘金
comments: false
date: Wed, 19 May 2021 15:20:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=9929'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>前面我们说到，当组件更新时，实例化渲染 watcher 时传递的 <code>updateComponent</code> 方法会被执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> updateComponent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 执行 vm._render() 函数，得到 虚拟 VNode，并将 VNode 传递给 vm._update 方法，接下来就该到 patch 阶段了</span>
  vm._update(vm._render(), hydrating)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先会先执行 vm._render() 函数，得到组件的 VNode，并将 VNode 传递给 vm._update 方法，接下来就该进入到 patch 阶段了。今天我们就来深入理解组件更新时 patch 的执行过程。</p>
<h1 data-id="heading-1">历史</h1>
<p>1.x 版本的 Vue 没有 VNode 和 diff 算法，那个版本的 Vue 的核心只有响应式原理：<code>Object.defineProperty</code>、<code>Dep</code>、<code>Watcher</code>。</p>
<ul>
<li>
<p><code>Object.defineProperty</code>: 负责数据的拦截。getter 时进行依赖收集，setter 时让 dep 通知 watcher 去更新</p>
</li>
<li>
<p><code>Dep</code>：Vue data 选项返回的对象，对象的 key 和 dep 一一对应</p>
</li>
<li>
<p><code>Watcher</code>：key 和 watcher 时一对多的关系，组件模版中每使用一次 key 就会生成一个 watcher</p>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
    <span class="hljs-comment"><!-- 模版中每引用一次响应式数据，就会生成一个 watcher --></span>
    <span class="hljs-comment"><!-- watcher 1 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"msg1"</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- watcher 2 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"msg2"</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 和 dep 一一对应，和 watcher 一 对 多</span>
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Hello Vue 1.0'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当数据更新时，dep 通知 watcher 去直接更新 DOM，因为这个版本的 watcher 和 DOM 时一一对应关系，watcher 可以非常明确的知道这个 key 在组件模版中的位置，因此可以做到定向更新，所以它的更新效率是非常高的。</p>
<p>虽然更新效率高，但随之也产生了严重的问题，无法完成一个企业级应用，理由很简单：当你的页面足够复杂时，会包含很多的组件，在这种架构下就意味这一个页面会产生大量的 watcher，这非常耗资源。</p>
<p>这时就在 Vue 2.0 中通过引入 VNode 和 diff 算法去解决 1.x 中的问题。将 watcher 的粒度放大，变成一个组件一个 watcher（就是我们说的渲染 watcher），这时候你页面再大，watcher 也很少，这就解决了复杂页面 watcher 太多导致性能下降的问题。</p>
<p>当响应式数据更新时，dep 通知 watcher 去更新，这时候问题就来了，Vue 1.x 中 watcher 和 key 一一对应，可以明确知道去更新什么地方，但是 Vue 2.0 中 watcher 对应的是一整个组件，更新的数据在组件的的什么位置，watcher 并不知道。这时候就需要 VNode 出来解决问题。</p>
<p>通过引入 VNode，当组件中数据更新时，会为组件生成一个新的 VNode，通过比对新老两个 VNode，找出不一样的地方，然后执行 DOM 操作更新发生变化的节点，这个过程就是大家熟知的 diff。</p>
<p>以上就是 Vue 2.0 为什么会引入 VNode 和 diff 算法的历史原因了，也是 Vue 1.x 到 2.x 的一个发展历程。</p>
<h1 data-id="heading-2">目标</h1>
<ul>
<li>深入理解 Vue 的 patch 阶段，理解其 diff 算法的原理。</li>
</ul>
<h1 data-id="heading-3">源码解读</h1>
<h2 data-id="heading-4">入口</h2>
<blockquote>
<p>/src/core/instance/lifecycle.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> updateComponent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 执行 vm._render() 函数，得到 VNode，并将 VNode 传递给 _update 方法，接下来就该到 patch 阶段了</span>
  vm._update(vm._render(), hydrating)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">vm._update</h2>
<blockquote>
<p>/src/core/instance/lifecycle.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 页面首次渲染和后续更新的入口位置，也是 patch 的入口位置 
 */</span>
Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
  <span class="hljs-comment">// 页面的挂载点，真实的元素</span>
  <span class="hljs-keyword">const</span> prevEl = vm.$el
  <span class="hljs-comment">// 老 VNode</span>
  <span class="hljs-keyword">const</span> prevVnode = vm._vnode
  <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(vm)
  <span class="hljs-comment">// 新 VNode</span>
  vm._vnode = vnode
  <span class="hljs-comment">// Vue.prototype.__patch__ is injected in entry points</span>
  <span class="hljs-comment">// based on the rendering backend used.</span>
  <span class="hljs-keyword">if</span> (!prevVnode) &#123;
    <span class="hljs-comment">// 老 VNode 不存在，表示首次渲染，即初始化页面时走这里</span>
    vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 响应式数据更新时，即更新页面时走这里</span>
    vm.$el = vm.__patch__(prevVnode, vnode)
  &#125;
  restoreActiveInstance()
  <span class="hljs-comment">// update __vue__ reference</span>
  <span class="hljs-keyword">if</span> (prevEl) &#123;
    prevEl.__vue__ = <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (vm.$el) &#123;
    vm.$el.__vue__ = vm
  &#125;
  <span class="hljs-comment">// if parent is an HOC, update its $el as well</span>
  <span class="hljs-keyword">if</span> (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) &#123;
    vm.$parent.$el = vm.$el
  &#125;
  <span class="hljs-comment">// updated hook is called by the scheduler to ensure that children are</span>
  <span class="hljs-comment">// updated in a parent's updated hook.</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">vm.__patch__</h2>
<blockquote>
<p>/src/platforms/web/runtime/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">/ 在 Vue 原型链上安装 web 平台的 patch 函数
Vue.prototype.__patch__ = inBrowser ? patch : noop
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">patch</h2>
<blockquote>
<p>/src/platforms/web/runtime/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// patch 工厂函数，为其传入平台特有的一些操作，然后返回一个 patch 函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> patch: <span class="hljs-built_in">Function</span> = createPatchFunction(&#123; nodeOps, modules &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">nodeOps</h3>
<blockquote>
<p>src/platforms/web/runtime/node-ops.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * web 平台的 DOM 操作 API
 */</span>

<span class="hljs-comment">/**
 * 创建标签名为 tagName 的元素节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span> (<span class="hljs-params">tagName: string, vnode: VNode</span>): <span class="hljs-title">Element</span> </span>&#123;
  <span class="hljs-comment">// 创建元素节点</span>
  <span class="hljs-keyword">const</span> elm = <span class="hljs-built_in">document</span>.createElement(tagName)
  <span class="hljs-keyword">if</span> (tagName !== <span class="hljs-string">'select'</span>) &#123;
    <span class="hljs-keyword">return</span> elm
  &#125;
  <span class="hljs-comment">// false or null will remove the attribute but undefined will not</span>
  <span class="hljs-comment">// 如果是 select 元素，则为它设置 multiple 属性</span>
  <span class="hljs-keyword">if</span> (vnode.data && vnode.data.attrs && vnode.data.attrs.multiple !== <span class="hljs-literal">undefined</span>) &#123;
    elm.setAttribute(<span class="hljs-string">'multiple'</span>, <span class="hljs-string">'multiple'</span>)
  &#125;
  <span class="hljs-keyword">return</span> elm
&#125;

<span class="hljs-comment">// 创建带命名空间的元素节点</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElementNS</span> (<span class="hljs-params">namespace: string, tagName: string</span>): <span class="hljs-title">Element</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElementNS(namespaceMap[namespace], tagName)
&#125;

<span class="hljs-comment">// 创建文本节点</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span> (<span class="hljs-params">text: string</span>): <span class="hljs-title">Text</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createTextNode(text)
&#125;

<span class="hljs-comment">// 创建注释节点</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComment</span> (<span class="hljs-params">text: string</span>): <span class="hljs-title">Comment</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createComment(text)
&#125;

<span class="hljs-comment">// 在指定节点前插入节点</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertBefore</span> (<span class="hljs-params">parentNode: Node, newNode: Node, referenceNode: Node</span>) </span>&#123;
  parentNode.insertBefore(newNode, referenceNode)
&#125;

<span class="hljs-comment">/**
 * 移除指定子节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeChild</span> (<span class="hljs-params">node: Node, child: Node</span>) </span>&#123;
  node.removeChild(child)
&#125;

<span class="hljs-comment">/**
 * 添加子节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">appendChild</span> (<span class="hljs-params">node: Node, child: Node</span>) </span>&#123;
  node.appendChild(child)
&#125;

<span class="hljs-comment">/**
 * 返回指定节点的父节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parentNode</span> (<span class="hljs-params">node: Node</span>): ?<span class="hljs-title">Node</span> </span>&#123;
  <span class="hljs-keyword">return</span> node.parentNode
&#125;

<span class="hljs-comment">/**
 * 返回指定节点的下一个兄弟节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextSibling</span> (<span class="hljs-params">node: Node</span>): ?<span class="hljs-title">Node</span> </span>&#123;
  <span class="hljs-keyword">return</span> node.nextSibling
&#125;

<span class="hljs-comment">/**
 * 返回指定节点的标签名 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tagName</span> (<span class="hljs-params">node: Element</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> node.tagName
&#125;

<span class="hljs-comment">/**
 * 为指定节点设置文本 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setTextContent</span> (<span class="hljs-params">node: Node, text: string</span>) </span>&#123;
  node.textContent = text
&#125;

<span class="hljs-comment">/**
 * 为节点设置指定的 scopeId 属性，属性值为 ''
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setStyleScope</span> (<span class="hljs-params">node: Element, scopeId: string</span>) </span>&#123;
  node.setAttribute(scopeId, <span class="hljs-string">''</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">modules</h3>
<blockquote>
<p>/src/platforms/web/runtime/modules 和 /src/core/vdom/modules</p>
</blockquote>
<p>平台特有的一些操作，比如：attr、class、style、event 等，还有核心的 directive 和 ref，它们会向外暴露一些特有的方法，比如：create、activate、update、remove、destroy，这些方法在 patch 阶段时会被调用，从而做相应的操作，比如 创建 attr、指令等。这部分内容太多了，这里就不一一列举了，在阅读 patch 的过程中如有需要可回头深入阅读，比如操作节点的属性的时候，就去读 attr 相关的代码。</p>
<h2 data-id="heading-10">createPatchFunction</h2>
<p><strong>提示</strong>：由于该函数的代码量较大， 所以调整了一下代码结构，方便阅读和理解</p>
<blockquote>
<p>/src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> hooks = [<span class="hljs-string">'create'</span>, <span class="hljs-string">'activate'</span>, <span class="hljs-string">'update'</span>, <span class="hljs-string">'remove'</span>, <span class="hljs-string">'destroy'</span>]

<span class="hljs-comment">/**
 * 工厂函数，注入平台特有的一些功能操作，并定义一些方法，然后返回 patch 函数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPatchFunction</span> (<span class="hljs-params">backend</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i, j
  <span class="hljs-keyword">const</span> cbs = &#123;&#125;

  <span class="hljs-comment">/**
   * modules: &#123; ref, directives, 平台特有的一些操纵，比如 attr、class、style 等 &#125;
   * nodeOps: &#123; 对元素的增删改查 API &#125;
   */</span>
  <span class="hljs-keyword">const</span> &#123; modules, nodeOps &#125; = backend

  <span class="hljs-comment">/**
   * hooks = ['create', 'activate', 'update', 'remove', 'destroy']
   * 遍历这些钩子，然后从 modules 的各个模块中找到相应的方法，比如：directives 中的 create、update、destroy 方法
   * 让这些方法放到 cb[hook] = [hook 方法] 中，比如: cb.create = [fn1, fn2, ...]
   * 然后在合适的时间调用相应的钩子方法完成对应的操作
   */</span>
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < hooks.length; ++i) &#123;
    <span class="hljs-comment">// 比如 cbs.create = []</span>
    cbs[hooks[i]] = []
    <span class="hljs-keyword">for</span> (j = <span class="hljs-number">0</span>; j < modules.length; ++j) &#123;
      <span class="hljs-keyword">if</span> (isDef(modules[j][hooks[i]])) &#123;
        <span class="hljs-comment">// 遍历各个 modules，找出各个 module 中的 create 方法，然后添加到 cbs.create 数组中</span>
        cbs[hooks[i]].push(modules[j][hooks[i]])
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">/**
   * vm.__patch__
   *   1、新节点不存在，老节点存在，调用 destroy，销毁老节点
   *   2、如果 oldVnode 是真实元素，则表示首次渲染，创建新节点，并插入 body，然后移除老节点
   *   3、如果 oldVnode 不是真实元素，则表示更新阶段，执行 patchVnode
   */</span>
  <span class="hljs-keyword">return</span> patch
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">patch</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * vm.__patch__
 *   1、新节点不存在，老节点存在，调用 destroy，销毁老节点
 *   2、如果 oldVnode 是真实元素，则表示首次渲染，创建新节点，并插入 body，然后移除老节点
 *   3、如果 oldVnode 不是真实元素，则表示更新阶段，执行 patchVnode
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
  <span class="hljs-comment">// 如果新节点不存在，老节点存在，则调用 destroy，销毁老节点</span>
  <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;
    <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> isInitialPatch = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> insertedVnodeQueue = []

  <span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
    <span class="hljs-comment">// 新的 VNode 存在，老的 VNode 不存在，这种情况会在一个组件初次渲染的时候出现，比如：</span>
    <span class="hljs-comment">// <div id="app"><comp></comp></div></span>
    <span class="hljs-comment">// 这里的 comp 组件初次渲染时就会走这儿</span>
    <span class="hljs-comment">// empty mount (likely as component), create new root element</span>
    isInitialPatch = <span class="hljs-literal">true</span>
    createElm(vnode, insertedVnodeQueue)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 判断 oldVnode 是否为真实元素</span>
    <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)
    <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
      <span class="hljs-comment">// 不是真实元素，但是老节点和新节点是同一个节点，则是更新阶段，执行 patch 更新节点</span>
      patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 是真实元素，则表示初次渲染</span>
      <span class="hljs-keyword">if</span> (isRealElement) &#123;
        <span class="hljs-comment">// 挂载到真实元素以及处理服务端渲染的情况</span>
        <span class="hljs-comment">// mounting to a real element</span>
        <span class="hljs-comment">// check if this is server-rendered content and if we can perform</span>
        <span class="hljs-comment">// a successful hydration.</span>
        <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;
          oldVnode.removeAttribute(SSR_ATTR)
          hydrating = <span class="hljs-literal">true</span>
        &#125;
        <span class="hljs-keyword">if</span> (isTrue(hydrating)) &#123;
          <span class="hljs-keyword">if</span> (hydrate(oldVnode, vnode, insertedVnodeQueue)) &#123;
            invokeInsertHook(vnode, insertedVnodeQueue, <span class="hljs-literal">true</span>)
            <span class="hljs-keyword">return</span> oldVnode
          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
            warn(
              <span class="hljs-string">'The client-side rendered virtual DOM tree is not matching '</span> +
              <span class="hljs-string">'server-rendered content. This is likely caused by incorrect '</span> +
              <span class="hljs-string">'HTML markup, for example nesting block-level elements inside '</span> +
              <span class="hljs-string">'<p>, or missing <tbody>. Bailing hydration and performing '</span> +
              <span class="hljs-string">'full client-side render.'</span>
            )
          &#125;
        &#125;
        <span class="hljs-comment">// 走到这儿说明不是服务端渲染，或者 hydration 失败，则根据 oldVnode 创建一个 vnode 节点</span>
        <span class="hljs-comment">// either not server-rendered, or hydration failed.</span>
        <span class="hljs-comment">// create an empty node and replace it</span>
        oldVnode = emptyNodeAt(oldVnode)
      &#125;

      <span class="hljs-comment">// 拿到老节点的真实元素</span>
      <span class="hljs-keyword">const</span> oldElm = oldVnode.elm
      <span class="hljs-comment">// 获取老节点的父元素，即 body</span>
      <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)

      <span class="hljs-comment">// 基于新 vnode 创建整棵 DOM 树并插入到 body 元素下</span>
      createElm(
        vnode,
        insertedVnodeQueue,
        <span class="hljs-comment">// extremely rare edge case: do not insert if old element is in a</span>
        <span class="hljs-comment">// leaving transition. Only happens when combining transition +</span>
        <span class="hljs-comment">// keep-alive + HOCs. (#4590)</span>
        oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
        nodeOps.nextSibling(oldElm)
      )

      <span class="hljs-comment">// 递归更新父占位符节点元素</span>
      <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
        <span class="hljs-keyword">let</span> ancestor = vnode.parent
        <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
        <span class="hljs-keyword">while</span> (ancestor) &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
            cbs.destroy[i](ancestor)
          &#125;
          ancestor.elm = vnode.elm
          <span class="hljs-keyword">if</span> (patchable) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
              cbs.create[i](emptyNode, ancestor)
            &#125;
            <span class="hljs-comment">// #6513</span>
            <span class="hljs-comment">// invoke insert hooks that may have been merged by create hooks.</span>
            <span class="hljs-comment">// e.g. for directives that uses the "inserted" hook.</span>
            <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
            <span class="hljs-keyword">if</span> (insert.merged) &#123;
              <span class="hljs-comment">// start at index 1 to avoid re-invoking component mounted hook</span>
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < insert.fns.length; i++) &#123;
                insert.fns[i]()
              &#125;
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            registerRef(ancestor)
          &#125;
          ancestor = ancestor.parent
        &#125;
      &#125;

      <span class="hljs-comment">// 移除老节点</span>
      <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
        removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.tag)) &#123;
        invokeDestroyHook(oldVnode)
      &#125;
    &#125;
  &#125;

  invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
  <span class="hljs-keyword">return</span> vnode.elm
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">invokeDestroyHook</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 销毁节点：
 *   执行组件的 destroy 钩子，即执行 $destroy 方法 
 *   执行组件各个模块(style、class、directive 等）的 destroy 方法
 *   如果 vnode 还存在子节点，则递归调用 invokeDestroyHook
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeDestroyHook</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i, j
  <span class="hljs-keyword">const</span> data = vnode.data
  <span class="hljs-keyword">if</span> (isDef(data)) &#123;
    <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.destroy)) i(vnode)
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) cbs.destroy[i](vnode)
  &#125;
  <span class="hljs-keyword">if</span> (isDef(i = vnode.children)) &#123;
    <span class="hljs-keyword">for</span> (j = <span class="hljs-number">0</span>; j < vnode.children.length; ++j) &#123;
      invokeDestroyHook(vnode.children[j])
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">sameVnode</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 判读两个节点是否相同 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="hljs-comment">// key 必须相同，需要注意的是 undefined === undefined => true</span>
    a.key === b.key && (
      (
        <span class="hljs-comment">// 标签相同</span>
        a.tag === b.tag &&
        <span class="hljs-comment">// 都是注释节点</span>
        a.isComment === b.isComment &&
        <span class="hljs-comment">// 都有 data 属性</span>
        isDef(a.data) === isDef(b.data) &&
        <span class="hljs-comment">// input 标签的情况</span>
        sameInputType(a, b)
      ) || (
        <span class="hljs-comment">// 异步占位符节点</span>
        isTrue(a.isAsyncPlaceholder) &&
        a.asyncFactory === b.asyncFactory &&
        isUndef(b.asyncFactory.error)
      )
    )
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">emptyNodeAt</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 为元素(elm)创建一个空的 vnode
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span>(<span class="hljs-params">elm</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> VNode(nodeOps.tagName(elm).toLowerCase(), &#123;&#125;, [], <span class="hljs-literal">undefined</span>, elm)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">createElm</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 基于 vnode 创建整棵 DOM 树，并插入到父节点上
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">
  vnode,
  insertedVnodeQueue,
  parentElm,
  refElm,
  nested,
  ownerArray,
  index
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
    <span class="hljs-comment">// This vnode was used in a previous render!</span>
    <span class="hljs-comment">// now it's used as a new node, overwriting its elm would cause</span>
    <span class="hljs-comment">// potential patch errors down the road when it's used as an insertion</span>
    <span class="hljs-comment">// reference node. Instead, we clone the node on-demand before creating</span>
    <span class="hljs-comment">// associated DOM element for it.</span>
    vnode = ownerArray[index] = cloneVNode(vnode)
  &#125;

  vnode.isRootInsert = !nested <span class="hljs-comment">// for transition enter check</span>
  <span class="hljs-comment">/**
   * 重点
   * 1、如果 vnode 是一个组件，则执行 init 钩子，创建组件实例并挂载，
   *   然后为组件执行各个模块的 create 钩子
   *   如果组件被 keep-alive 包裹，则激活组件
   * 2、如果是一个普通元素，则什么也不错
   */</span>
  <span class="hljs-keyword">if</span> (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 获取 data 对象</span>
  <span class="hljs-keyword">const</span> data = vnode.data
  <span class="hljs-comment">// 所有的孩子节点</span>
  <span class="hljs-keyword">const</span> children = vnode.children
  <span class="hljs-keyword">const</span> tag = vnode.tag
  <span class="hljs-keyword">if</span> (isDef(tag)) &#123;
    <span class="hljs-comment">// 未知标签</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-keyword">if</span> (data && data.pre) &#123;
        creatingElmInVPre++
      &#125;
      <span class="hljs-keyword">if</span> (isUnknownElement(vnode, creatingElmInVPre)) &#123;
        warn(
          <span class="hljs-string">'Unknown custom element: <'</span> + tag + <span class="hljs-string">'> - did you '</span> +
          <span class="hljs-string">'register the component correctly? For recursive components, '</span> +
          <span class="hljs-string">'make sure to provide the "name" option.'</span>,
          vnode.context
        )
      &#125;
    &#125;

    <span class="hljs-comment">// 创建新节点</span>
    vnode.elm = vnode.ns
      ? nodeOps.createElementNS(vnode.ns, tag)
      : nodeOps.createElement(tag, vnode)
    setScope(vnode)

    <span class="hljs-comment">// 递归创建所有子节点（普通元素、组件）</span>
    createChildren(vnode, children, insertedVnodeQueue)
    <span class="hljs-keyword">if</span> (isDef(data)) &#123;
      invokeCreateHooks(vnode, insertedVnodeQueue)
    &#125;
    <span class="hljs-comment">// 将节点插入父节点</span>
    insert(parentElm, vnode.elm, refElm)

    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && data && data.pre) &#123;
      creatingElmInVPre--
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isTrue(vnode.isComment)) &#123;
    <span class="hljs-comment">// 注释节点，创建注释节点并插入父节点</span>
    vnode.elm = nodeOps.createComment(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 文本节点，创建文本节点并插入父节点</span>
    vnode.elm = nodeOps.createTextNode(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">createComponent</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 如果 vnode 是一个组件，则执行 init 钩子，创建组件实例，并挂载
 * 然后为组件执行各个模块的 create 方法
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 组件新的 vnode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>insertedVnodeQueue 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>parentElm oldVnode 的父节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>refElm oldVnode 的下一个兄弟节点
 * <span class="hljs-doctag">@returns </span>如果组件被 keep-alive 包裹，则返回 true，否则为 undefined
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vnode, insertedVnodeQueue, parentElm, refElm</span>) </span>&#123;
  <span class="hljs-comment">// 获取 vnode.data 对象</span>
  <span class="hljs-keyword">let</span> i = vnode.data
  <span class="hljs-keyword">if</span> (isDef(i)) &#123;
    <span class="hljs-comment">// 验证组件实例是否已经存在 && 被 keep-alive 包裹</span>
    <span class="hljs-keyword">const</span> isReactivated = isDef(vnode.componentInstance) && i.keepAlive
    <span class="hljs-comment">// 执行 vnode.data.init 钩子函数，该函数在讲 render helper 时讲过</span>
    <span class="hljs-comment">// 如果是被 keep-alive 包裹的组件：则再执行 prepatch 钩子，用 vnode 上的各个属性更新 oldVnode 上的相关属性</span>
    <span class="hljs-comment">// 如果是组件没有被 keep-alive 包裹或者首次渲染，则初始化组件，并进入挂载阶段</span>
    <span class="hljs-keyword">if</span> (isDef(i = i.hook) && isDef(i = i.init)) &#123;
      i(vnode, <span class="hljs-literal">false</span> <span class="hljs-comment">/* hydrating */</span>)
    &#125;
    <span class="hljs-comment">// after calling the init hook, if the vnode is a child component</span>
    <span class="hljs-comment">// it should've created a child instance and mounted it. the child</span>
    <span class="hljs-comment">// component also has set the placeholder vnode's elm.</span>
    <span class="hljs-comment">// in that case we can just return the element and be done.</span>
    <span class="hljs-keyword">if</span> (isDef(vnode.componentInstance)) &#123;
      <span class="hljs-comment">// 如果 vnode 是一个子组件，则调用 init 钩子之后会创建一个组件实例，并挂载</span>
      <span class="hljs-comment">// 这时候就可以给组件执行各个模块的的 create 钩子了</span>
      initComponent(vnode, insertedVnodeQueue)
      <span class="hljs-comment">// 将组件的 DOM 节点插入到父节点内</span>
      insert(parentElm, vnode.elm, refElm)
      <span class="hljs-keyword">if</span> (isTrue(isReactivated)) &#123;
        <span class="hljs-comment">// 组件被 keep-alive 包裹的情况，激活组件</span>
        reactivateComponent(vnode, insertedVnodeQueue, parentElm, refElm)
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">insert</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 向父节点插入节点 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insert</span>(<span class="hljs-params">parent, elm, ref</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isDef(parent)) &#123;
    <span class="hljs-keyword">if</span> (isDef(ref)) &#123;
      <span class="hljs-keyword">if</span> (nodeOps.parentNode(ref) === parent) &#123;
        nodeOps.insertBefore(parent, elm, ref)
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      nodeOps.appendChild(parent, elm)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">removeVnodes</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 移除指定索引范围（startIdx —— endIdx）内的节点 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeVnodes</span>(<span class="hljs-params">vnodes, startIdx, endIdx</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (; startIdx <= endIdx; ++startIdx) &#123;
    <span class="hljs-keyword">const</span> ch = vnodes[startIdx]
    <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-keyword">if</span> (isDef(ch.tag)) &#123;
        removeAndInvokeRemoveHook(ch)
        invokeDestroyHook(ch)
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// Text node</span>
        removeNode(ch.elm)
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">patchVnode</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 更新节点
 *   全量的属性更新
 *   如果新老节点都有孩子，则递归执行 diff
 *   如果新节点有孩子，老节点没孩子，则新增新节点的这些孩子节点
 *   如果老节点有孩子，新节点没孩子，则删除老节点的这些孩子
 *   更新文本节点
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">
  oldVnode,
  vnode,
  insertedVnodeQueue,
  ownerArray,
  index,
  removeOnly
</span>) </span>&#123;
  <span class="hljs-comment">// 老节点和新节点相同，直接返回</span>
  <span class="hljs-keyword">if</span> (oldVnode === vnode) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
    <span class="hljs-comment">// clone reused vnode</span>
    vnode = ownerArray[index] = cloneVNode(vnode)
  &#125;

  <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm

  <span class="hljs-comment">// 异步占位符节点</span>
  <span class="hljs-keyword">if</span> (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
    <span class="hljs-keyword">if</span> (isDef(vnode.asyncFactory.resolved)) &#123;
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.isAsyncPlaceholder = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 跳过静态节点的更新</span>
  <span class="hljs-comment">// reuse element for static trees.</span>
  <span class="hljs-comment">// note we only do this if the vnode is cloned -</span>
  <span class="hljs-comment">// if the new node is not cloned it means the render functions have been</span>
  <span class="hljs-comment">// reset by the hot-reload-api and we need to do a proper re-render.</span>
  <span class="hljs-keyword">if</span> (isTrue(vnode.isStatic) &&
    isTrue(oldVnode.isStatic) &&
    vnode.key === oldVnode.key &&
    (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
  ) &#123;
    <span class="hljs-comment">// 新旧节点都是静态的而且两个节点的 key 一样，并且新节点被 clone 了 或者 新节点有 v-once指令，则重用这部分节点</span>
    vnode.componentInstance = oldVnode.componentInstance
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 执行组件的 prepatch 钩子</span>
  <span class="hljs-keyword">let</span> i
  <span class="hljs-keyword">const</span> data = vnode.data
  <span class="hljs-keyword">if</span> (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) &#123;
    i(oldVnode, vnode)
  &#125;

  <span class="hljs-comment">// 老节点的孩子</span>
  <span class="hljs-keyword">const</span> oldCh = oldVnode.children
  <span class="hljs-comment">// 新节点的孩子</span>
  <span class="hljs-keyword">const</span> ch = vnode.children
  <span class="hljs-comment">// 全量更新新节点的属性，Vue 3.0 在这里做了很多的优化</span>
  <span class="hljs-keyword">if</span> (isDef(data) && isPatchable(vnode)) &#123;
    <span class="hljs-comment">// 执行新节点所有的属性更新</span>
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
    <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
  &#125;
  <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
    <span class="hljs-comment">// 新节点不是文本节点</span>
    <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
      <span class="hljs-comment">// 如果新老节点都有孩子，则递归执行 diff 过程</span>
      <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-comment">// 老孩子不存在，新孩子存在，则创建这些新孩子节点</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        checkDuplicateKeys(ch)
      &#125;
      <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
      addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
      <span class="hljs-comment">// 老孩子存在，新孩子不存在，则移除这些老孩子节点</span>
      removeVnodes(oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
      <span class="hljs-comment">// 老节点是文本节点，则将文本内容置空</span>
      nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
    <span class="hljs-comment">// 新节点是文本节点，则更新文本节点</span>
    nodeOps.setTextContent(elm, vnode.text)
  &#125;
  <span class="hljs-keyword">if</span> (isDef(data)) &#123;
    <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">updateChildren</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * diff 过程:
 *   diff 优化：做了四种假设，假设新老节点开头结尾有相同节点的情况，一旦命中假设，就避免了一次循环，以提高执行效率
 *             如果不幸没有命中假设，则执行遍历，从老节点中找到新开始节点
 *             找到相同节点，则执行 patchVnode，然后将老节点移动到正确的位置
 *   如果老节点先于新节点遍历结束，则剩余的新节点执行新增节点操作
 *   如果新节点先于老节点遍历结束，则剩余的老节点执行删除操作，移除这些老节点
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh, insertedVnodeQueue, removeOnly</span>) </span>&#123;
  <span class="hljs-comment">// 老节点的开始索引</span>
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 新节点的开始索引</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 老节点的结束索引</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
  <span class="hljs-comment">// 第一个老节点</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]
  <span class="hljs-comment">// 最后一个老节点</span>
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]
  <span class="hljs-comment">// 新节点的结束索引</span>
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>
  <span class="hljs-comment">// 第一个新节点</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]
  <span class="hljs-comment">// 最后一个新节点</span>
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]
  <span class="hljs-keyword">let</span> oldKeyToIdx, idxInOld, vnodeToMove, refElm

  <span class="hljs-comment">// removeOnly是一个特殊的标志，仅由 <transition-group> 使用，以确保被移除的元素在离开转换期间保持在正确的相对位置</span>
  <span class="hljs-keyword">const</span> canMove = !removeOnly

  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    <span class="hljs-comment">// 检查新节点的 key 是否重复</span>
    checkDuplicateKeys(newCh)
  &#125;

  <span class="hljs-comment">// 遍历新老两组节点，只要有一组遍历完（开始索引超过结束索引）则跳出循环</span>
  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-keyword">if</span> (isUndef(oldStartVnode)) &#123;
      <span class="hljs-comment">// 如果节点被移动，在当前索引上可能不存在，检测这种情况，如果节点不存在则调整索引</span>
      oldStartVnode = oldCh[++oldStartIdx] <span class="hljs-comment">// Vnode has been moved left</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isUndef(oldEndVnode)) &#123;
      oldEndVnode = oldCh[--oldEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
      <span class="hljs-comment">// 老开始节点和新开始节点是同一个节点，执行 patch</span>
      patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      <span class="hljs-comment">// patch 结束后老开始和新开始的索引分别加 1</span>
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
      <span class="hljs-comment">// 老结束和新结束是同一个节点，执行 patch</span>
      patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      <span class="hljs-comment">// patch 结束后老结束和新结束的索引分别减 1</span>
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; <span class="hljs-comment">// Vnode moved right</span>
      <span class="hljs-comment">// 老开始和新结束是同一个节点，执行 patch</span>
      patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      <span class="hljs-comment">// 处理被 transtion-group 包裹的组件时使用</span>
      canMove && nodeOps.insertBefore(parentElm, oldStartVnode.elm, nodeOps.nextSibling(oldEndVnode.elm))
      <span class="hljs-comment">// patch 结束后老开始索引加 1，新结束索引减 1</span>
      oldStartVnode = oldCh[++oldStartIdx]
      newEndVnode = newCh[--newEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left</span>
      <span class="hljs-comment">// 老结束和新开始是同一个节点，执行 patch</span>
      patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      canMove && nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
      <span class="hljs-comment">// patch 结束后，老结束的索引减 1，新开始的索引加 1</span>
      oldEndVnode = oldCh[--oldEndIdx]
      newStartVnode = newCh[++newStartIdx]
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果上面的四种假设都不成立，则通过遍历找到新开始节点在老节点中的位置索引</span>

      <span class="hljs-comment">// 找到老节点中每个节点 key 和 索引之间的关系映射 => oldKeyToIdx = &#123; key1: idx1, ... &#125;</span>
      <span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
      <span class="hljs-comment">// 在映射中找到新开始节点在老节点中的位置索引</span>
      idxInOld = isDef(newStartVnode.key)
        ? oldKeyToIdx[newStartVnode.key]
        : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
      <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element</span>
        <span class="hljs-comment">// 在老节点中没找到新开始节点，则说明是新创建的元素，执行创建</span>
        createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 在老节点中找到新开始节点了</span>
        vnodeToMove = oldCh[idxInOld]
        <span class="hljs-keyword">if</span> (sameVnode(vnodeToMove, newStartVnode)) &#123;
          <span class="hljs-comment">// 如果这两个节点是同一个，则执行 patch</span>
          patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
          <span class="hljs-comment">// patch 结束后将该老节点置为 undefined</span>
          oldCh[idxInOld] = <span class="hljs-literal">undefined</span>
          canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 最后这种情况是，找到节点了，但是发现两个节点不是同一个节点，则视为新元素，执行创建</span>
          createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
        &#125;
      &#125;
      <span class="hljs-comment">// 老节点向后移动一个</span>
      newStartVnode = newCh[++newStartIdx]
    &#125;
  &#125;
  <span class="hljs-comment">// 走到这里，说明老姐节点或者新节点被遍历完了</span>
  <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
    <span class="hljs-comment">// 说明老节点被遍历完了，新节点有剩余，则说明这部分剩余的节点是新增的节点，然后添加这些节点</span>
    refElm = isUndef(newCh[newEndIdx + <span class="hljs-number">1</span>]) ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
    addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
    <span class="hljs-comment">// 说明新节点被遍历完了，老节点有剩余，说明这部分的节点被删掉了，则移除这些节点</span>
    removeVnodes(oldCh, oldStartIdx, oldEndIdx)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">checkDuplicateKeys</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 检查一组元素的 key 是否重复 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkDuplicateKeys</span>(<span class="hljs-params">children</span>) </span>&#123;
  <span class="hljs-keyword">const</span> seenKeys = &#123;&#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < children.length; i++) &#123;
    <span class="hljs-keyword">const</span> vnode = children[i]
    <span class="hljs-keyword">const</span> key = vnode.key
    <span class="hljs-keyword">if</span> (isDef(key)) &#123;
      <span class="hljs-keyword">if</span> (seenKeys[key]) &#123;
        warn(
          <span class="hljs-string">`Duplicate keys detected: '<span class="hljs-subst">$&#123;key&#125;</span>'. This may cause an update error.`</span>,
          vnode.context
        )
      &#125; <span class="hljs-keyword">else</span> &#123;
        seenKeys[key] = <span class="hljs-literal">true</span>
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">addVnodes</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 在指定索引范围（startIdx —— endIdx）内添加节点
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addVnodes</span>(<span class="hljs-params">parentElm, refElm, vnodes, startIdx, endIdx, insertedVnodeQueue</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (; startIdx <= endIdx; ++startIdx) &#123;
    createElm(vnodes[startIdx], insertedVnodeQueue, parentElm, refElm, <span class="hljs-literal">false</span>, vnodes, startIdx)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">createKeyToOldIdx</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 得到指定范围（beginIdx —— endIdx）内节点的 key 和 索引之间的关系映射 => &#123; key1: idx1, ... &#125;
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">children, beginIdx, endIdx</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i, key
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  <span class="hljs-keyword">for</span> (i = beginIdx; i <= endIdx; ++i) &#123;
    key = children[i].key
    <span class="hljs-keyword">if</span> (isDef(key)) map[key] = i
  &#125;
  <span class="hljs-keyword">return</span> map
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">findIdxInOld</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
  * 找到新节点（vnode）在老节点（oldCh）中的位置索引 
  */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findIdxInOld</span>(<span class="hljs-params">node, oldCh, start, end</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start; i < end; i++) &#123;
    <span class="hljs-keyword">const</span> c = oldCh[i]
    <span class="hljs-keyword">if</span> (isDef(c) && sameVnode(node, c)) <span class="hljs-keyword">return</span> i
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">invokeCreateHooks</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 调用 各个模块的 create 方法，比如创建属性的、创建样式的、指令的等等 ，然后执行组件的 mounted 生命周期方法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeCreateHooks</span>(<span class="hljs-params">vnode, insertedVnodeQueue</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
    cbs.create[i](emptyNode, vnode)
  &#125;
  <span class="hljs-comment">// 组件钩子</span>
  i = vnode.data.hook <span class="hljs-comment">// Reuse variable</span>
  <span class="hljs-keyword">if</span> (isDef(i)) &#123;
    <span class="hljs-comment">// 组件好像没有 create 钩子</span>
    <span class="hljs-keyword">if</span> (isDef(i.create)) i.create(emptyNode, vnode)
    <span class="hljs-comment">// 调用组件的 insert 钩子，执行组件的 mounted 生命周期方法</span>
    <span class="hljs-keyword">if</span> (isDef(i.insert)) insertedVnodeQueue.push(vnode)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">createChildren</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 创建所有子节点，并将子节点插入父节点，形成一棵 DOM 树
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildren</span>(<span class="hljs-params">vnode, children, insertedVnodeQueue</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(children)) &#123;
    <span class="hljs-comment">// children 是数组，表示是一组节点</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">// 检测这组节点的 key 是否重复</span>
      checkDuplicateKeys(children)
    &#125;
    <span class="hljs-comment">// 遍历这组节点，依次创建这些节点然后插入父节点，形成一棵 DOM 树</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
      createElm(children[i], insertedVnodeQueue, vnode.elm, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>, children, i)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isPrimitive(vnode.text)) &#123;
    <span class="hljs-comment">// 说明是文本节点，创建文本节点，并插入父节点</span>
    nodeOps.appendChild(vnode.elm, nodeOps.createTextNode(<span class="hljs-built_in">String</span>(vnode.text)))
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-27">总结</h1>
<ul>
<li>
<p><strong>面试官 问</strong>：你能说一说 Vue 的 patch 算法吗？</p>
<p><strong>答</strong>：</p>
<p>Vue 的 patch 算法有三个作用：负责首次渲染和后续更新或者销毁组件</p>
<ul>
<li>
<p>如果老的 VNode 是真实元素，则表示首次渲染，创建整棵 DOM 树，并插入 body，然后移除老的模版节点</p>
</li>
<li>
<p>如果老的 VNode 不是真实元素，并且新的 VNode 也存在，则表示更新阶段，执行 patchVnode</p>
<ul>
<li>
<p>首先是全量更新所有的属性</p>
</li>
<li>
<p>如果新老 VNode 都有孩子，则递归执行 updateChildren，进行 diff 过程</p>
<blockquote>
<p>针对前端操作 DOM 节点的特点进行如下优化：</p>
</blockquote>
<ul>
<li>
<p>同层比较（降低时间复杂度）深度优先（递归）</p>
</li>
<li>
<p>而且前端很少有完全打乱节点顺序的情况，所以做了四种假设，假设新老 VNode 的开头结尾存在相同节点，一旦命中假设，就避免了一次循环，降低了 diff 的时间复杂度，提高执行效率。如果不幸没有命中假设，则执行遍历，从老的 VNode 中找到新的 VNode 的开始节点</p>
</li>
<li>
<p>找到相同节点，则执行 patchVnode，然后将老节点移动到正确的位置</p>
</li>
<li>
<p>如果老的 VNode 先于新的 VNode 遍历结束，则剩余的新的 VNode 执行新增节点操作</p>
</li>
<li>
<p>如果新的 VNode 先于老的 VNode 遍历结束，则剩余的老的 VNode 执行删除操纵，移除这些老节点</p>
</li>
</ul>
</li>
<li>
<p>如果新的 VNode 有孩子，老的 VNode 没孩子，则新增这些新孩子节点</p>
</li>
<li>
<p>如果老的 VNode 有孩子，新的 VNode 没孩子，则删除这些老孩子节点</p>
</li>
<li>
<p>剩下一种就是更新文本节点</p>
</li>
</ul>
</li>
<li>
<p>如果新的 VNode 不存在，老的 VNode 存在，则调用 destroy，销毁老节点</p>
</li>
</ul>
</li>
</ul>
<hr>
<p>好了，到这里，Vue 源码解读系列就结束了，如果你认认真真的读完整个系列的文章，相信你对 Vue 源码已经相当熟悉了，不论是从宏观层面理解，还是某些细节方面的详解，应该都没问题。即使有些细节现在不清楚，但是当遇到问题时，你也能一眼看出来该去源码的什么位置去找答案。</p>
<p>到这里你可以试着在自己的脑海中复述一下 Vue 的整个执行流程。过程很重要，但 <strong>总结</strong> 才是最后的升华时刻。如果在哪个环节卡住了，可再回去读相应的部分就可以了。</p>
<p>还记得系列的第一篇文章中提到的目标吗？相信阅读几遍下来，你一定可以在自己的简历中写到：<strong>精通 Vue 框架的源码原理</strong>。</p>
<p>接下来会开始 Vue 的手写系列。</p>
<h1 data-id="heading-28">配套视频</h1>
<p><a href="https://www.bilibili.com/video/BV1rQ4y1o7WF?share_source=copy_web" target="_blank" rel="nofollow noopener noreferrer">Vue 源码解读（12）—— patch</a></p>
<h1 data-id="heading-29">求关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-30">链接</h1>
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
<p><a href="https://juejin.cn/post/6963048982079602696" target="_blank">Vue 源码解读（11）—— render helper</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6964141635856760868" target="_blank">Vue 源码解读（12）—— patch</a></p>
</li>
</ul>
<h1 data-id="heading-31">学习交流群</h1>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank">链接</a></p></div>  
</div>
            