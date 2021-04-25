
---
title: 'Vue 源码解读（7）—— Hook Event'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8406'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 18:53:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=8406'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><code>Hook Event</code>（钩子事件）相信很多 Vue 开发者都没有使用过，甚至没听过，毕竟 Vue 官方文档中也没有提及。</p>
<p>Vue 提供了一些生命周期钩子函数，供开发者在特定的逻辑点添加额外的处理逻辑，比如：在组件挂载阶段提供了 <code>beforeMount</code> 和 <code>mounted</code> 两个生命周期钩子，供开发者在组件挂载阶段执行额外的逻辑处理，比如为组件准备渲染所需的数据。</p>
<p>那这个 Hook Event —— 钩子事件，其中也有钩子的意思，和 Vue 的生命周期钩子函数有什么关系呢？它又有什么用呢？这就是这边文章要解答的问题。</p>
<h1 data-id="heading-1">目标</h1>
<ul>
<li>
<p>理解什么是 Hook Event ？明白其使用场景</p>
</li>
<li>
<p>深入理解 Hook Event 的实现原理</p>
</li>
</ul>
<h1 data-id="heading-2">什么是 Hook Event ？</h1>
<p>Hook Event 是 Vue 的自定义事件结合生命周期钩子实现的一种从组件外部为组件注入额外生命周期方法的功能。</p>
<h2 data-id="heading-3">使用场景</h2>
<p>假设现在有这么一个第三方的业务组件，逻辑很简单，就在 mounted 生命周期中调用接口获取数据，然后将数据渲染到页面上。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"JSON.stringify(item)"</span>></span>
        &#123;&#123; item &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">arr</span>: []
    &#125;
  &#125;,
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 调用接口获取组件渲染的数据</span>
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: &#123; data &#125; &#125; = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/api/getList'</span>)
    <span class="hljs-built_in">this</span>.arr.push(...data)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在使用的发现这个组件有些瑕疵，比如最简单的，接口等待时间可能比较长，我想在 mounted 生命周期开始执行的时候在控制台输出一个 <code>loading ...</code> 字符串，增强用户体验。</p>
<p>这个需求该怎么实现呢？</p>
<p>有两个办法：第一个比较麻烦，修改源码；而第二种方式则简单多了，就是我们今天介绍的 Hook Event，从组件外面为组件注入额外的生命周期方法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">comp</span> @<span class="hljs-attr">hook:mounted</span>=<span class="hljs-string">"hookMounted"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// 这就是上面的那个第三方业务组件</span>
<span class="hljs-keyword">import</span> Comp <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Comp.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    Comp
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">hookMounted</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'loading ...'</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候你再刷新页面就会发现业务组件在请求数据的时候，会在控制台输出一个 <code>loading ...</code> 字符串。</p>
<h2 data-id="heading-4">作用</h2>
<p>Hook Event 有什么作用？</p>
<p>通过 Hook Event 可以从组件外部为组件注入额外的生命周期方法。</p>
<h1 data-id="heading-5">实现原理</h1>
<p>知道了 Hook Event 的使用场景和作用，接下来就从源码去找它的实现原理，做到 “知其然，亦知其所以然”。</p>
<p>前面说过，Hook Event 是 Vue 的自定义事件结合生命周期钩子函数实现的一种功能，所以我们就去看生命周期相关的代码，比如：我们知道，Vue 的生命周期函数是通过一个叫 <code>callHook</code> 的方法来执行的</p>
<h2 data-id="heading-6">callHook</h2>
<blockquote>
<p>/src/core/instance/lifecycle.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * callHook(vm, 'mounted')
 * 执行实例指定的生命周期钩子函数
 * 如果实例设置有对应的 Hook Event，比如：<comp <span class="hljs-doctag">@hook</span>:mounted="method" />，执行完生命周期函数之后，触发该事件的执行
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 组件实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>hook 生命周期钩子函数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHook</span> (<span class="hljs-params">vm: Component, hook: string</span>) </span>&#123;
  <span class="hljs-comment">// 打开依赖收集</span>
  pushTarget()
  <span class="hljs-comment">// 从实例配置对象中获取指定钩子函数，比如 mounted</span>
  <span class="hljs-keyword">const</span> handlers = vm.$options[hook]
  <span class="hljs-comment">// mounted hook</span>
  <span class="hljs-keyword">const</span> info = <span class="hljs-string">`<span class="hljs-subst">$&#123;hook&#125;</span> hook`</span>
  <span class="hljs-keyword">if</span> (handlers) &#123;
    <span class="hljs-comment">// 通过 invokeWithErrorHandler 执行生命周期钩子</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = handlers.length; i < j; i++) &#123;
      invokeWithErrorHandling(handlers[i], vm, <span class="hljs-literal">null</span>, vm, info)
    &#125;
  &#125;
  <span class="hljs-comment">// Hook Event，如果设置了 Hook Event，比如 <comp @hook:mounted="method" />，则通过 $emit 触发该事件</span>
  <span class="hljs-comment">// vm._hasHookEvent 标识组件是否有 hook event，这是在 vm.$on 中处理组件自定义事件时设置的</span>
  <span class="hljs-keyword">if</span> (vm._hasHookEvent) &#123;
    <span class="hljs-comment">// vm.$emit('hook:mounted')</span>
    vm.$emit(<span class="hljs-string">'hook:'</span> + hook)
  &#125;
  <span class="hljs-comment">// 关闭依赖收集</span>
  popTarget()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">invokeWithErrorHandling</h3>
<blockquote>
<p>/src/core/util/error.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 通用函数，执行指定函数 handler
 * 传递进来的函数会被用 try catch 包裹，进行异常捕获处理
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeWithErrorHandling</span> (<span class="hljs-params">
  handler: <span class="hljs-built_in">Function</span>,
  context: any,
  args: <span class="hljs-literal">null</span> | any[],
  vm: any,
  info: string
</span>) </span>&#123;
  <span class="hljs-keyword">let</span> res
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 执行传递进来的函数 handler，并将执行结果返回</span>
    res = args ? handler.apply(context, args) : handler.call(context)
    <span class="hljs-keyword">if</span> (res && !res._isVue && isPromise(res) && !res._handled) &#123;
      res.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> handleError(e, vm, info + <span class="hljs-string">` (Promise/async)`</span>))
      <span class="hljs-comment">// issue #9511</span>
      <span class="hljs-comment">// avoid catch triggering multiple times when nested calls</span>
      res._handled = <span class="hljs-literal">true</span>
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    handleError(e, vm, info)
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">vm.$on</h2>
<blockquote>
<p>/src/core/instance/events.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 监听实例上的自定义事件，vm._event = &#123; eventName: [fn1, ...], ... &#125;
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>event 单个的事件名称或者有多个事件名组成的数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>fn 当 event 被触发时执行的回调函数
 * <span class="hljs-doctag">@returns </span>
 */</span>
Vue.prototype.$on = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event: string | <span class="hljs-built_in">Array</span><string>, fn: <span class="hljs-built_in">Function</span></span>): <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(event)) &#123;
    <span class="hljs-comment">// event 是有多个事件名组成的数组，则遍历这些事件，依次递归调用 $on</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = event.length; i < l; i++) &#123;
      vm.$on(event[i], fn)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 将注册的事件和回调以键值对的形式存储到 vm._event 对象中 vm._event = &#123; eventName: [fn1, ...] &#125;</span>
    (vm._events[event] || (vm._events[event] = [])).push(fn)
    <span class="hljs-comment">// hookEvent，提供从外部为组件实例注入声明周期方法的机会</span>
    <span class="hljs-comment">// 比如从组件外部为组件的 mounted 方法注入额外的逻辑</span>
    <span class="hljs-comment">// 该能力是结合 callhook 方法实现的</span>
    <span class="hljs-keyword">if</span> (hookRE.test(event)) &#123;
      vm._hasHookEvent = <span class="hljs-literal">true</span>
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> vm
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">总结</h1>
<ul>
<li>
<p><strong>面试官 问</strong>：什么是 Hook Event？</p>
<p><strong>答</strong>：</p>
<p>Hook Event 是 Vue 的自定义事件结合生命周期钩子实现的一种从组件外部为组件注入额外生命周期方法的功能。</p>
</li>
</ul>
<hr>
<ul>
<li>
<p><strong>面试官 问</strong>：Hook Event 是如果实现的？</p>
<p><strong>答</strong>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">comp</span> @<span class="hljs-attr">hook:lifecycleMethod</span>=<span class="hljs-string">"method"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>处理组件自定义事件的时候（vm.$on) 如果发现组件有 <code>hook:xx</code> 格式的事件（xx 为 Vue 的生命周期函数），则将 <code>vm._hasHookEvent</code> 置为 <code>true</code>，表示该组件有 Hook Event</p>
</li>
<li>
<p>在组件生命周期方法被触发的时候，内部会通过 <code>callHook</code> 方法来执行这些生命周期函数，在生命周期函数执行之后，如果发现 <code>vm._hasHookEvent</code> 为 true，则表示当前组件有 Hook Event，通过 <code>vm.$emit('hook:xx')</code> 触发 Hook Event 的执行</p>
</li>
</ul>
<p>这就是 Hook Event 的实现原理。</p>
</li>
</ul>
<h1 data-id="heading-10">配套视频</h1>
<p><a href="https://www.bilibili.com/video/BV1284y1F7Zs?share_source=copy_web" target="_blank" rel="nofollow noopener noreferrer">Vue 源码解读（7）—— Hook Event</a></p>
<h1 data-id="heading-11">求关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-12">链接</h1>
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
<p><a href="https://juejin.cn/post/6954923081462710309">Vue 源码解读（8）—— 编译器 之 解析</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6954923081462710309">Vue 源码解读（9）—— 编译器 之 优化</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6954923081462710309">Vue 源码解读（10）—— 编译器 之 生成渲染函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6954923081462710309">Vue 源码解读（11）—— render helper</a></p>
</li>
</ul></div>  
</div>
            