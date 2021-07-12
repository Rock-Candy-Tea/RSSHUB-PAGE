
---
title: '手写 Vue2 系列 之 computed'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54cc32e739d4bffbb683a42a979cfa7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 16:18:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54cc32e739d4bffbb683a42a979cfa7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇文章 <a href="https://juejin.cn/post/6982341667483303950" target="_blank" title="https://juejin.cn/post/6982341667483303950">手写 Vue2 系列 之 patch —— diff</a> 实现了 DOM diff 过程，完成页面响应式数据的更新。</p>
<h1 data-id="heading-1">目标</h1>
<p>本篇的目标是实现 computed 计算属性，完成模版中计算属性的展示。涉及的知识点：</p>
<ul>
<li>
<p>计算属性的本质</p>
</li>
<li>
<p>计算属性的缓存原理</p>
</li>
</ul>
<h1 data-id="heading-2">实现</h1>
<p>接下来就开始实现 computed 计算属性，。</p>
<h2 data-id="heading-3">_init</h2>
<blockquote>
<p>/src/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 初始化配置对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options 
 */</span>
Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 初始化 options.data</span>
  <span class="hljs-comment">// 代理 data 对象上的各个属性到 Vue 实例</span>
  <span class="hljs-comment">// 给 data 对象上的各个属性设置响应式能力</span>
  initData(<span class="hljs-built_in">this</span>)
  <span class="hljs-comment">// 初始化 computed 选项，并将计算属性代理到 Vue 实例上</span>
  <span class="hljs-comment">// 结合 watcher 实现缓存</span>
  initComputed(<span class="hljs-built_in">this</span>)
  <span class="hljs-comment">// 安装运行时的渲染工具函数</span>
  renderHelper(<span class="hljs-built_in">this</span>)
  <span class="hljs-comment">// ...</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">initComputed</h2>
<blockquote>
<p>/src/initComputed.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 初始化 computed 配置项
 * 为每一项实例化一个 Watcher，并将其 computed 属性代理到 Vue 实例上
 * 结合 watcher.dirty 和 watcher.evalute 实现 computed 缓存
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm Vue 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initComputed</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-comment">// 获取 computed 配置项</span>
  <span class="hljs-keyword">const</span> computed = vm.$options.computed
  <span class="hljs-comment">// 记录 watcher</span>
  <span class="hljs-keyword">const</span> watcher = vm._watcher = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-comment">// 遍历 computed 对象</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> computed) &#123;
    <span class="hljs-comment">// 实例化 Watcher，回调函数默认懒执行</span>
    watcher[key] = <span class="hljs-keyword">new</span> Watcher(computed[key], &#123; <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span> &#125;, vm)
    <span class="hljs-comment">// 将 computed 的属性 key 代理到 Vue 实例上</span>
    defineComputed(vm, key)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">defineComputed</h2>
<blockquote>
<p>/src/initComputed.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将计算属性代理到 Vue 实例上
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm Vue 实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key computed 的计算属性
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComputed</span>(<span class="hljs-params">vm, key</span>) </span>&#123;
  <span class="hljs-comment">// 属性描述符</span>
  <span class="hljs-keyword">const</span> descriptor = &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> watcher = vm._watcher[key]
      <span class="hljs-keyword">if</span> (watcher.dirty) &#123; <span class="hljs-comment">// 说明当前 computed 回调函数在本次渲染周期内没有被执行过</span>
        <span class="hljs-comment">// 执行 evalute，通知 watcher 执行 computed 回调函数，得到回调函数返回值</span>
        watcher.evalute()
      &#125;
      <span class="hljs-keyword">return</span> watcher.value
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'no setter'</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 将计算属性代理到 Vue 实例上</span>
  <span class="hljs-built_in">Object</span>.defineProperty(vm, key, descriptor)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Watcher</h2>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>cb 回调函数，负责更新 DOM 的回调函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options watcher 的配置项
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Watcher</span>(<span class="hljs-params">cb, options = &#123;&#125;, vm = <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-comment">// 备份 cb 函数</span>
  <span class="hljs-built_in">this</span>._cb = cb
  <span class="hljs-comment">// 回调函数执行后的值</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-comment">// computed 计算属性实现缓存的原理，标记当前回调函数在本次渲染周期内是否已经被执行过</span>
  <span class="hljs-built_in">this</span>.dirty = !!options.lazy
  <span class="hljs-comment">// Vue 实例</span>
  <span class="hljs-built_in">this</span>.vm = vm
  <span class="hljs-comment">// 非懒执行时，直接执行 cb 函数，cb 函数中会发生 vm.xx 的属性读取，从而进行依赖收集</span>
  !options.lazy && <span class="hljs-built_in">this</span>.get()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">watcher.get</h3>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 负责执行 Watcher 的 cb 函数
 * 执行时进行依赖收集
 */</span>
Watcher.prototype.get = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  pushTarget(<span class="hljs-built_in">this</span>)
  <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>._cb.apply(<span class="hljs-built_in">this</span>.vm)
  popTarget()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">watcher.update</h3>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 响应式数据更新时，dep 通知 watcher 执行 update 方法，
 * 让 update 方法执行 this._cb 函数更新 DOM
 */</span>
Watcher.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 通过 Promise，将 this._cb 的执行放到 this.dirty = true 的后面</span>
  <span class="hljs-comment">// 否则，在点击按钮时，computed 属性的第一次计算会无法执行，</span>
  <span class="hljs-comment">// 因为 this._cb 执行的时候，会更新组件，获取计算属性的值的时候 this.dirty 依然是</span>
  <span class="hljs-comment">// 上一次的 false，导致无法得到最新的的计算属性的值</span>
  <span class="hljs-comment">// 不过这个在有了异步更新队列之后就不需要了，当然，毕竟异步更新对象的本质也是 Promise</span>
  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>._cb()
  &#125;)
  <span class="hljs-comment">// 执行完 _cb 函数，DOM 更新完毕，进入下一个渲染周期，所以将 dirty 置为 false</span>
  <span class="hljs-comment">// 当再次获取 计算属性 时就可以重新执行 evalute 方法获取最新的值了</span>
  <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">watcher.evalute</h3>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">Watcher.prototype.evalute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 执行 get，触发计算函数 (cb) 的执行</span>
  <span class="hljs-built_in">this</span>.get()
  <span class="hljs-comment">// 将 dirty 置为 false，实现一次刷新周期内 computed 实现缓存</span>
  <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">pushTarget</h2>
<blockquote>
<p>/src/dep.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 存储所有的 Dep.target</span>
<span class="hljs-comment">// 为什么会有多个 Dep.target?</span>
<span class="hljs-comment">// 组件会产生一个渲染 Watcher，在渲染的过程中如果处理到用户 Watcher，</span>
<span class="hljs-comment">// 比如 computed 计算属性，这时候会执行 evalute -> get</span>
<span class="hljs-comment">// 假如直接赋值 Dep.target，那 Dep.target 的上一个值 —— 渲染 Watcher 就会丢失</span>
<span class="hljs-comment">// 造成在 computed 计算属性之后渲染的响应式数据无法完成依赖收集</span>
<span class="hljs-keyword">const</span> targetStack = []

<span class="hljs-comment">/**
 * 备份本次传递进来的 Watcher，并将其赋值给 Dep.target
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target Watcher 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushTarget</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-comment">// 备份传递进来的 Watcher</span>
  targetStack.push(target)
  Dep.target = target
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">popTarget</h2>
<blockquote>
<p>/src/dep.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将 Dep.target 重置为上一个 Watcher 或者 null
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">popTarget</span>(<span class="hljs-params"></span>) </span>&#123;
  targetStack.pop()
  Dep.target = targetStack[targetStack.length - <span class="hljs-number">1</span>]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">结果</h1>
<p>好了，到这里，Vue computed 属性实现就完成了，如果你能看到如下效果图，则说明一切正常。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54cc32e739d4bffbb683a42a979cfa7~tplv-k3u1fbpfcp-watermark.image" alt="Jun-20-2021 10-50-02.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，页面中的计算属性已经正常显示，而且也可以做到响应式更新，且具有缓存的能力（通过控制台查看 computed 输出）。</p>
<p>到这里，手写 Vue 系列就剩最后一部分内容了 —— <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">手写 Vue 系列 之 异步更新队列</a>。</p></div>  
</div>
            