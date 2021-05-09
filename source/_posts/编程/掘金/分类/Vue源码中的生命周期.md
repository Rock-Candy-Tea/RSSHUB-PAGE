
---
title: 'Vue源码中的生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c8383d929de484ab6de8d775e9c9e05~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 21:34:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c8383d929de484ab6de8d775e9c9e05~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>😶基础知识又得重新补习一下了</p>
</blockquote>
<h3 data-id="heading-0">前情回顾</h3>
<p>理解vdom的前提下，component，element的创建实际上对vnode的实例化。而创建组件的时候会将生命周期混入进去，一起来看下这个生命周期</p>
<h3 data-id="heading-1">生命周期</h3>
<p>生命周期的变量定义在<code>shared</code>文件夹中的<code>constant.js</code>文件中。constant顾名思义，变量嘛。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 生命周期钩子数组</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LIFECYCLE_HOOKS = [
  <span class="hljs-string">'beforeCreate'</span>,
  <span class="hljs-string">'created'</span>,
  <span class="hljs-string">'beforeMount'</span>,
  <span class="hljs-string">'mounted'</span>,
  <span class="hljs-string">'beforeUpdate'</span>,
  <span class="hljs-string">'updated'</span>,
  <span class="hljs-string">'beforeDestroy'</span>,
  <span class="hljs-string">'destroyed'</span>,
  <span class="hljs-string">'activated'</span>,
  <span class="hljs-string">'deactivated'</span>,
  <span class="hljs-string">'errorCaptured'</span>,
  <span class="hljs-string">'serverPrefetch'</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同同时这个问价还定义了一个资源类型</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ASSET_TYPES = [
  <span class="hljs-string">'component'</span>,
  <span class="hljs-string">'directive'</span>,
  <span class="hljs-string">'filter'</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义好了生命周期名称以后，必然需要有个地方去解释执行这些命令。这个位置在<code>core文件夹</code>中的<code>instance</code>文件夹中的<code>lifeCycle.js</code>。</p>
<p>这个文件夹定义了以下几个方法:</p>
<ul>
<li><code>setActiveInstance</code>设置激活的实例,这里的实例指的是我们写的vue组件或页面。</li>
<li><code>initLifecycle</code> 初始化生命周期。</li>
<li><code>lifecycleMixin</code> 在Vue实例的原型上混入生命周期方法。</li>
<li><code>mountComponent</code> 挂载组件。</li>
<li><code>updateChildComponent</code> 更新子组件。</li>
<li><code>isInInactiveTree</code> 判断当前实例的激活状态。</li>
<li><code>activateChildComponent</code> 激活子组件。</li>
<li><code>deactivateChildComponent</code> 灭活子组件。</li>
<li><code>callHook</code> 调用钩子方法。</li>
</ul>
<h3 data-id="heading-2">方法细节</h3>
<ul>
<li><code>callHook</code>。callHook的代码如下：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHook</span> (<span class="hljs-params">vm: Component, hook: string</span>) </span>&#123;
  <span class="hljs-comment">// #7573 disable dep collection when invoking lifecycle hooks</span>
  pushTarget()
  <span class="hljs-keyword">const</span> handlers = vm.$options[hook]
  <span class="hljs-keyword">const</span> info = <span class="hljs-string">`<span class="hljs-subst">$&#123;hook&#125;</span> hook`</span>
  <span class="hljs-keyword">if</span> (handlers) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = handlers.length; i < j; i++) &#123;
      invokeWithErrorHandling(handlers[i], vm, <span class="hljs-literal">null</span>, vm, info)
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (vm._hasHookEvent) &#123;
    vm.$emit(<span class="hljs-string">'hook:'</span> + hook)
  &#125;
  popTarget()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不得不说，这个源码整的越来越复杂了。其意图是从<code>$options</code>中取出钩子方法，然后遍历执行对应的方法。</p>
<p>在之前的版本中没有<code>invokeWithErrorHandling</code>这个方法。遍历handlers时直接交给<code>vm</code>调用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHook</span> (<span class="hljs-params">vm: Component, hook: string</span>) </span>&#123;
  <span class="hljs-keyword">const</span> handlers = vm.$options[hook]
  <span class="hljs-keyword">if</span> (handlers) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = handlers.length; i < j; i++) &#123;
      <span class="hljs-keyword">try</span> &#123;
        handlers[i].call(vm)
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        handleError(e, vm, <span class="hljs-string">`<span class="hljs-subst">$&#123;hook&#125;</span> hook`</span>)
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (vm._hasHookEvent) &#123;
    vm.$emit(<span class="hljs-string">'hook:'</span> + hook)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而最新的代码时封装了一个<code>invokeWithErrorHandling</code>方法，执行的时候会包含错误处理。</p>
<p>这里有个地方我一直不太理解，就是这个<code>_hasHookEvent</code>。从上边的代码里看。如果<code>$optons</code>中的hook即<code>handlers</code>存在，则会调用对应的hook方法。或者如果<code>vm</code>实例的<code>_hasHookEvent</code>属性为<code>true</code>，也会调用<code>$emit</code>方法触发对应的hook方法。</p>
<p>然后我们看下event.js`。</p>
<blockquote>
<p>core/instance/event.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> hookRE = <span class="hljs-regexp">/^hook:/</span>
  Vue.prototype.$on = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event: string | <span class="hljs-built_in">Array</span><string>, fn: <span class="hljs-built_in">Function</span></span>): <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(event)) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = event.length; i < l; i++) &#123;
        <span class="hljs-built_in">this</span>.$on(event[i], fn)
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      (vm._events[event] || (vm._events[event] = [])).push(fn)
      <span class="hljs-comment">// optimize hook:event cost by using a boolean flag marked at registration</span>
      <span class="hljs-comment">// instead of a hash lookup</span>
      <span class="hljs-keyword">if</span> (hookRE.test(event)) &#123;
        vm._hasHookEvent = <span class="hljs-literal">true</span>
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> vm
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用<code>$on</code>方法监听事件时，如果事件名称以<code>hook:</code>为前缀，那么这个事件就会被当做<code>hoodkEvent</code>,在将事件的回调push到实例对象的<code>_event</code>属性时，实例的<code>_hasHookEvent</code>属性会被设置为<code>true</code>。当使用<code>$emit</code>触发<code>$emit('hoook:eventname')</code>时，对应的回调函数就会被触发。</p>
<p>使用的方式大致如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><LoginComponent @hook:created=<span class="hljs-string">"created"</span>></LoginComponent>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>initLifecycle</code>。初始化生命周期这个方法，其实只是在实例上申明了几个私有属性，用作申明周期的标识。其代码如下：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initLifecycle</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = vm.$options

  <span class="hljs-comment">// locate first non-abstract parent</span>
  <span class="hljs-keyword">let</span> parent = options.parent
  <span class="hljs-keyword">if</span> (parent && !options.abstract) &#123;
    <span class="hljs-keyword">while</span> (parent.$options.abstract && parent.$parent) &#123;
      parent = parent.$parent
    &#125;
    parent.$children.push(vm)
  &#125;

  vm.$parent = parent
  vm.$root = parent ? parent.$root : vm
 <span class="hljs-comment">// 设置初始化状态</span>
  vm.$children = []
  vm.$refs = &#123;&#125;

  vm._watcher = <span class="hljs-literal">null</span>
  vm._inactive = <span class="hljs-literal">null</span>
  vm._directInactive = <span class="hljs-literal">false</span>
  vm._isMounted = <span class="hljs-literal">false</span>
  vm._isDestroyed = <span class="hljs-literal">false</span>
  vm._isBeingDestroyed = <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>vm</code>设置了<code>$children</code>,<code>$ref</code>,<code>_watcher</code>,<code>_inactve</code>为空，<code>_directInactive</code>,<code>_isMounted</code>,<code>_isDestroyed</code>,<code>_isBeingDestroyed</code>为false。</p>
<ul>
<li><code>lifecycleMixin</code>生命周期混入方法。</li>
</ul>
<p>这个方法在vue的原型上添加了<code>_update</code>，<code>$forceupdate</code>,<code>$destroy</code>三个方法。</p>
<blockquote>
<p>Vue.prototype._update</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (vm._isMounted) &#123;
      callHook(vm, <span class="hljs-string">'beforeUpdate'</span>)
    &#125;
    <span class="hljs-keyword">const</span> prevEl = vm.$el
    <span class="hljs-keyword">const</span> prevVnode = vm._vnode
    <span class="hljs-keyword">const</span> prevActiveInstance = activeInstance
    activeInstance = vm
    vm._vnode = vnode
    <span class="hljs-comment">// Vue.prototype.__patch__ is injected in entry points</span>
    <span class="hljs-comment">// based on the rendering backend used.</span>
    <span class="hljs-keyword">if</span> (!prevVnode) &#123;
      <span class="hljs-comment">// initial render</span>
      vm.$el = vm.__patch__(
        vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>,
        vm.$options._parentElm,
        vm.$options._refElm
      )
      <span class="hljs-comment">// no need for the ref nodes after initial patch</span>
      <span class="hljs-comment">// this prevents keeping a detached DOM tree in memory (#5851)</span>
      vm.$options._parentElm = vm.$options._refElm = <span class="hljs-literal">null</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// updates</span>
      vm.$el = vm.__patch__(prevVnode, vnode)
    &#125;
    activeInstance = prevActiveInstance
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
<p><code>_update</code>方法会先判断实例是否已经挂载，如果实例已经挂载，则会先调用<code>beforeUpdate</code>钩子。</p>
<p>然后当前实例的<code>_vnode</code>及当前实例分别赋值给<code>prevNode</code>和<code>preActiveInstance</code>。如果没有<code>preVode</code>则说明是初次渲染，直接调用<code>__pattch__</code>方法进行处理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Vue.prototype.__patch__ is injected in entry points</span>
    <span class="hljs-comment">// based on the rendering backend used.</span>
    <span class="hljs-keyword">if</span> (!prevVnode) &#123;
      <span class="hljs-comment">// initial render 初次渲染</span>
      vm.$el = vm.__patch__(
        vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>,
        vm.$options._parentElm,
        vm.$options._refElm
      )
      <span class="hljs-comment">// no need for the ref nodes after initial patch</span>
      <span class="hljs-comment">// this prevents keeping a detached DOM tree in memory (#5851)</span>
      vm.$options._parentElm = vm.$options._refElm = <span class="hljs-literal">null</span>
    &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果存在preVnode则直接调用<code>__patch__</code>进行更新</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// updates</span>
  vm.$el = vm.__patch__(prevVnode, vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>$forceUpdate</code>方法。这个放个直接判断实例上是否存在<code>_watcher</code>属性，如果存在<code>_watcher</code>属性，则直接调用watcher的update方法。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.prototype.$forceUpdate = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (vm._watcher) &#123;
      vm._watcher.update()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>$destroy</code>方法。这个方法会判断实例的<code>_isBeingDestroyed</code>属性,然后执行<code>beforeDestroy</code>钩子函数。然后依次清除<code>watcher</code>,解绑事件(调用<code>$off</code>),设置<code>_isDestroyed</code>属性为true。设置<code>$vnode.parent</code>为null。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.prototype.$destroy = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (vm._isBeingDestroyed) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    callHook(vm, <span class="hljs-string">'beforeDestroy'</span>)
    vm._isBeingDestroyed = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// remove self from parent</span>
    <span class="hljs-keyword">const</span> parent = vm.$parent
    <span class="hljs-keyword">if</span> (parent && !parent._isBeingDestroyed && !vm.$options.abstract) &#123;
      remove(parent.$children, vm)
    &#125;
    <span class="hljs-comment">// teardown watchers</span>
    <span class="hljs-keyword">if</span> (vm._watcher) &#123;
      vm._watcher.teardown()
    &#125;
    <span class="hljs-keyword">let</span> i = vm._watchers.length
    <span class="hljs-keyword">while</span> (i--) &#123;
      vm._watchers[i].teardown()
    &#125;
    <span class="hljs-comment">// remove reference from data ob</span>
    <span class="hljs-comment">// frozen object may not have observer.</span>
    <span class="hljs-keyword">if</span> (vm._data.__ob__) &#123;
      vm._data.__ob__.vmCount--
    &#125;
    <span class="hljs-comment">// call the last hook...</span>
    vm._isDestroyed = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// invoke destroy hooks on current rendered tree</span>
    vm.__patch__(vm._vnode, <span class="hljs-literal">null</span>)
    <span class="hljs-comment">// fire destroyed hook</span>
    callHook(vm, <span class="hljs-string">'destroyed'</span>)
    <span class="hljs-comment">// turn off all instance listeners.</span>
    vm.$off()
    <span class="hljs-comment">// remove __vue__ reference</span>
    <span class="hljs-keyword">if</span> (vm.$el) &#123;
      vm.$el.__vue__ = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-comment">// release circular reference (#6759)</span>
    <span class="hljs-keyword">if</span> (vm.$vnode) &#123;
      vm.$vnode.parent = <span class="hljs-literal">null</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>mountComponent</code>挂载组件。这个方法会先判断<code>$options</code>中是否有render方法。如果render不存在，则创建一个空节点。然后调用<code>beforeMount</code>钩子方法。之后，调用实例的<code>_render</code>方法进行更新。最后在实例上设置新的<code>_watcher</code>,以上的步骤完成后，则调用<code>mounted</code>钩子函数。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span> (<span class="hljs-params">
  vm: Component,
  el: ?Element,
  hydrating?: boolean
</span>): <span class="hljs-title">Component</span> </span>&#123;
  vm.$el = el
  <span class="hljs-keyword">if</span> (!vm.$options.render) &#123;
    vm.$options.render = createEmptyVNode
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-keyword">if</span> ((vm.$options.template && vm.$options.template.charAt(<span class="hljs-number">0</span>) !== <span class="hljs-string">'#'</span>) ||
        vm.$options.el || el) &#123;
        warn(
          <span class="hljs-string">'You are using the runtime-only build of Vue where the template '</span> +
          <span class="hljs-string">'compiler is not available. Either pre-compile the templates into '</span> +
          <span class="hljs-string">'render functions, or use the compiler-included build.'</span>,
          vm
        )
      &#125; <span class="hljs-keyword">else</span> &#123;
        warn(
          <span class="hljs-string">'Failed to mount component: template or render function not defined.'</span>,
          vm
        )
      &#125;
    &#125;
  &#125;
  callHook(vm, <span class="hljs-string">'beforeMount'</span>)

  <span class="hljs-keyword">let</span> updateComponent
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
    updateComponent = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> name = vm._name
      <span class="hljs-keyword">const</span> id = vm._uid
      <span class="hljs-keyword">const</span> startTag = <span class="hljs-string">`vue-perf-start:<span class="hljs-subst">$&#123;id&#125;</span>`</span>
      <span class="hljs-keyword">const</span> endTag = <span class="hljs-string">`vue-perf-end:<span class="hljs-subst">$&#123;id&#125;</span>`</span>

      mark(startTag)
      <span class="hljs-keyword">const</span> vnode = vm._render()
      mark(endTag)
      measure(<span class="hljs-string">`vue <span class="hljs-subst">$&#123;name&#125;</span> render`</span>, startTag, endTag)

      mark(startTag)
      vm._update(vnode, hydrating)
      mark(endTag)
      measure(<span class="hljs-string">`vue <span class="hljs-subst">$&#123;name&#125;</span> patch`</span>, startTag, endTag)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    updateComponent = <span class="hljs-function">() =></span> &#123;
      vm._update(vm._render(), hydrating)
    &#125;
  &#125;

  vm._watcher = <span class="hljs-keyword">new</span> Watcher(vm, updateComponent, noop)
  hydrating = <span class="hljs-literal">false</span>

  <span class="hljs-comment">// manually mounted instance, call mounted on self</span>
  <span class="hljs-comment">// mounted is called for render-created child components in its inserted hook</span>
  <span class="hljs-keyword">if</span> (vm.$vnode == <span class="hljs-literal">null</span>) &#123;
    vm._isMounted = <span class="hljs-literal">true</span>
    callHook(vm, <span class="hljs-string">'mounted'</span>)
  &#125;
  <span class="hljs-keyword">return</span> vm
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">总结</h3>
<p><code>生命周期其实是一个组件从加载到销毁的过程</code>。如果组件初次加载，则会先创建一个空节点，然后调用<code>beforeMount</code>,之后就是使用实例的<code>_render</code>进行渲染，渲染后则调用<code>mounted</code>,设置实例的属性<code>isMounted</code>为true。组件更新的过程会先调用<code>beforeUpdate</code>钩子，之后使用<code>__patch__</code>进行更新操作。组件销毁时会先触发<code>beforeDestroy</code>钩子，然后设置对应的属性为false，对应的示例属性对象为null,最后调用<code>destroyed</code>钩子。</p>
<p>大致就是这么一个过程。</p>
<h3 data-id="heading-4">思考</h3>
<p>今天也看了些css相关的内容。明天顺带着提一下吧。</p>
<h3 data-id="heading-5">最后说两句</h3>
<ol>
<li>动一动您发财的小手，<strong><code>「点个赞吧」</code></strong></li>
<li>动一动您发财的小手，<strong><code>「点个在看」</code></strong></li>
<li>都看到这里了，不妨  <strong><code>「加个关注」</code></strong></li>
<li>不妨  <strong><code>「转发一下」</code></strong>，好东西要记得分享</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c8383d929de484ab6de8d775e9c9e05~tplv-k3u1fbpfcp-zoom-1.image" alt="javascript基础知识总结" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            