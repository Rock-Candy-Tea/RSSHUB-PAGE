
---
title: '【源码学习】你知道data，props，methods初始化的顺序么？ (附思维导图)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0bf0a6f19f14e3ea920e780796bce66~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 02:53:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0bf0a6f19f14e3ea920e780796bce66~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h2 data-id="heading-0">声明</h2>
<p>🔊 本文是开始学习 <code>Vue</code> 源码的第三篇笔记，当前的版本是 <code>2.6.14</code>  。如果对你有一点点帮助，请点赞鼓励一下，如果有错误或者遗漏，请在评论区指出，非常感谢各位大佬。</p>
<p>🔊 代码基本上是逐行注释，由于本人的能力有限，很多基础知识也进行了注释和讲解。由于源码过长，文章不会贴出完整代码，所以基本上都是贴出部分伪代码然后进行分析，建议在阅读时对照源码，效果更佳。</p>
<p>🔊 从本篇文章开始，可能会出现暂时看不懂的地方，是因为还没有学习前置知识，不必惊慌，只需知道存在这样一个知识点，接着向下看，看完了前置知识，回过头来再看这里就一目了然了。</p>
<blockquote>
<p><strong>本文代码所在路径</strong>：<strong>\vue-dev\src\core\instance\state.js</strong></p>
</blockquote>
<h1 data-id="heading-1">前言</h1>
<p>先回顾一下上文，我们知道了 <code>Vue</code> 的初始化过程，在 <code>Vue.prototype._init</code> 中我们分成四个部分进行分析，其中第三部分做了一系列的初始化，本文继续学习其中的一个初始化过程，响应式原理的核心部分 <code>initState</code> 。也就是 <code>data</code>，<code>props</code>，<code>methods</code>，<code>watch</code>，<code>computed</code> 的初始化过程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0bf0a6f19f14e3ea920e780796bce66~tplv-k3u1fbpfcp-watermark.image" alt="Vue.prototype._init (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">initState</h1>
<h2 data-id="heading-3">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化数据 响应式原理的入口
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例Vm
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-comment">// 为当前组件创建了一个watchers属性，为数组类型  vm._watchers保存着当前vue组件实例的所有监听者（watcher）</span>
  vm._watchers = []
  <span class="hljs-comment">// 从实例上获取配置项</span>
  <span class="hljs-keyword">const</span> opts = vm.$options
  <span class="hljs-comment">//如果vm.$options上面定义了props 初始化props 对props配置做响应式处理  </span>
  <span class="hljs-comment">//代理props配置上的key到vue实例,支持this.propKey的方式访问</span>
  <span class="hljs-keyword">if</span> (opts.props) initProps(vm, opts.props)
  <span class="hljs-comment">//如果vm.$options上面定义了methods 初始化methods ,props的优先级 高于methods的优先级</span>
  <span class="hljs-comment">//代理methods配置上的key到vue实例,支持this.methodsKey的方式访问</span>
  <span class="hljs-keyword">if</span> (opts.methods) initMethods(vm, opts.methods)
  <span class="hljs-comment">//如果vm.$options上面定义了data ,初始化data, 代理data中的属性到vue实例,支持通过 this.dataKey 的方式访问定义的属性</span>
  <span class="hljs-keyword">if</span> (opts.data) &#123;
    initData(vm)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//这里是data为空时observe 函数观测一个空对象：&#123;&#125;</span>
    observe(vm._data = &#123;&#125;, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>)
  &#125;
  <span class="hljs-comment">//如果vm.$options上面定义了computed 初始化computed</span>
  <span class="hljs-comment">//computed 是通过watcher来实现的,对每个computedKey实例化一个watcher,默认懒执行.</span>
  <span class="hljs-comment">//将computedKey代理到vue实例上,支持通过this.computedKey的方式来访问computed.key</span>
  <span class="hljs-keyword">if</span> (opts.computed) initComputed(vm, opts.computed)
  <span class="hljs-comment">//如果vm.$options上面定义了watch 初始化watch</span>
  <span class="hljs-keyword">if</span> (opts.watch && opts.watch !== nativeWatch) &#123; 
    <span class="hljs-comment">// 判断组件有watch属性 并没有nativeWatch（ 兼容火狐）</span>
    initWatch(vm, opts.watch)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">代码解读</h2>
<p>⭐ 为当前组件创建了一个 <code>watchers</code> 属性，为数组类型  <code>vm._watchers</code> 保存着当前 <code>vue</code> 组件实例的所有监听者<code>（watcher）</code></p>
<p>⭐ 从代码中可以看出，初始化的顺序是 <code>props</code> -> <code>methods</code> -> <code>data</code> -> <code>computed</code> -> <code>watch</code></p>
<p>⭐ <strong>initProps</strong> 如果 <code>vm.$options</code> 上面定义了 <code>props</code> 初始化 <code>props</code> 对 <code>props</code> 配置做响应式处理，代理 <code>props</code> 配置上的 <code>key</code> 到 <code>vue</code> 实例，支持 <code>this.propKey</code> 的方式访问。</p>
<p>⭐ <strong>initMethods</strong> 如果 <code>vm.$options</code> 上面定义了 <code>methods</code> 初始化 <code>methods</code> , <code>props</code> 的优先级 高于 <code>methods</code> 的优先级，代理 <code>methods</code> 配置上的 <code>key</code> 到 <code>vue</code> 实例 , 支持 <code>this.methodsKey</code> 的方式访问。</p>
<p>⭐ <strong>initData</strong> 如果 <code>vm.$options</code> 上面定义了 <code>data</code> ,初始化 <code>data</code>, 代理 <code>data</code> 中的属性到 <code>vue</code> 实例，支持通过 <code>this.dataKey</code> 的方式访问定义的属性。<code>data</code> 为空时 <code>observe</code> 函数观测一个空对象。</p>
<p>⭐ <strong>initComputed</strong> 如果 <code>vm.$options</code> 上面定义了 <code>computed</code> 初始化 <code>computed</code>。<code>computed</code> <code>是通过watcher</code> 来实现的，对每个 <code>computedKey</code> 实例化一个 <code>watcher</code>，默认懒执行。将 <code>computedKey</code> 代理到 <code>vue</code> 实例上，支持通过 <code>this.computedKey</code> 的方式来访问 <code>computed.key</code> 。</p>
<p>⭐ <strong>initWatch</strong></p>
<h1 data-id="heading-5">proxy</h1>
<h2 data-id="heading-6">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 代理对象</span>
<span class="hljs-keyword">const</span> sharedPropertyDefinition = &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">get</span>: noop,
  <span class="hljs-attr">set</span>: noop
&#125;

<span class="hljs-comment">/**
 * 代理 通过sharedPropertyDefinition对象 给key添加一层getter和setter  将key代理到 vue 实例上
 * 当我们访问this.key的时候,实际上就会访问 vm._data.key / vm._props.key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target  实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>sourceKey  _data / _props
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key data / props 中的属性
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span> (<span class="hljs-params">target: <span class="hljs-built_in">Object</span>, sourceKey: string, key: string</span>) </span>&#123;
  sharedPropertyDefinition.get = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxyGetter</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[sourceKey][key]
  &#125;
  sharedPropertyDefinition.set = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxySetter</span> (<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-built_in">this</span>[sourceKey][key] = val
  &#125;
  <span class="hljs-comment">// 拦截对 this.key的访问</span>
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, sharedPropertyDefinition)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">代码解读</h2>
<p>⭐  通过 <code>sharedPropertyDefinition</code> 对象 给 <code>key</code> 添加一层 <code>getter</code> 和 <code>setter</code>  将 <code>key</code> 代理到 <code>vue</code> 实例上，当我们访问 <code>this.key</code> 的时候，实际上就会访问 <code>vm._data.key / vm._props.key</code>。</p>
<h1 data-id="heading-8">initProps</h1>
<h2 data-id="heading-9">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化props
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>propsOptions 配置对象上的props
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initProps</span> (<span class="hljs-params">vm: Component, propsOptions: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-comment">// 存放父组件传入子组件的props</span>
  <span class="hljs-keyword">const</span> propsData = vm.$options.propsData || &#123;&#125;
  <span class="hljs-comment">// 存放经过转换后的最终的props的对象, props 与 vm._props 保持同一个引用，初始值为 &#123;&#125;</span>
  <span class="hljs-keyword">const</span> props = vm._props = &#123;&#125;

  <span class="hljs-comment">// 缓存 props 的每个 key，性能优化, 一个存放props的key的数组，就算props的值是空的，key也会存在里面 ,keys 与 vm.$options._propKeys 保持同一个引用，初始值为 &#123;&#125;</span>
  <span class="hljs-keyword">const</span> keys = vm.$options._propKeys = []

  <span class="hljs-comment">// 判断是不是根元素</span>
  <span class="hljs-keyword">const</span> isRoot = !vm.$parent

  <span class="hljs-comment">//当组件不是根组件时，使用 toggleObserving(false) 取消对 Object Array 类型 Prop 深度观测，为什么这么做呢，因为 Object Array 在父组件中已经被深度观测过了。</span>
  <span class="hljs-keyword">if</span> (!isRoot) &#123;
    toggleObserving(<span class="hljs-literal">false</span>)
  &#125;
  
  <span class="hljs-comment">// 遍历props配置对象</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> propsOptions) &#123;
    <span class="hljs-comment">// 向缓存键值数组中添加键名</span>
    keys.push(key)
    <span class="hljs-comment">/**
     * 用validateProp校验是否为预期的类型值，然后返回相应 prop 值(或default值)
     * 如果有定义类型检查，布尔值没有默认值时会被赋予false，字符串默认undefined
     */</span>
    <span class="hljs-keyword">const</span> value = validateProp(key, propsOptions, propsData, vm)
    <span class="hljs-comment">//非生产环境</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">// 进行键名的转换，将驼峰式转换成连字符式的键名</span>
      <span class="hljs-keyword">const</span> hyphenatedKey = hyphenate(key)
      
      <span class="hljs-comment">// 校验prop是否为内置的属性, 内置属性：key,ref,slot,slot-scope,is</span>
      <span class="hljs-keyword">if</span> (isReservedAttribute(hyphenatedKey) ||
          config.isReservedAttr(hyphenatedKey)) &#123;
        warn(
          <span class="hljs-string">`"<span class="hljs-subst">$&#123;hyphenatedKey&#125;</span>" is a reserved attribute and cannot be used as component prop.`</span>,
          vm
        )
      &#125;
      <span class="hljs-comment">// 对属性建立观察，并在直接使用props属性时给予警告</span>
      defineReactive(props, key, value, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 子组件直接修改属性时 弹出警告</span>
        <span class="hljs-keyword">if</span> (!isRoot && !isUpdatingChildComponent) &#123;
          warn(
            <span class="hljs-string">`Avoid mutating a prop directly since the value will be `</span> +
            <span class="hljs-string">`overwritten whenever the parent component re-renders. `</span> +
            <span class="hljs-string">`Instead, use a data or computed property based on the prop's `</span> +
            <span class="hljs-string">`value. Prop being mutated: "<span class="hljs-subst">$&#123;key&#125;</span>"`</span>,
            vm
          )
        &#125;
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-comment">// 生产环境下直接对属性进行存取器包装，建立依赖观察, 为 props 的每个 key 设置数据响应式</span>
      defineReactive(props, key, value)
    &#125;

    <span class="hljs-comment">// 当实例上没有同名属性时，对属性进行代理操作,将对键名的引用指向vm._props对象中</span>
    <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> vm)) &#123;
      <span class="hljs-comment">// 代理 key 到 vm 对象上</span>
      proxy(vm, <span class="hljs-string">`_props`</span>, key)
    &#125;
  &#125;
   <span class="hljs-comment">// 开启观察状态标识, 重新打开观测开关，避免影响后续代码执行</span>
  toggleObserving(<span class="hljs-literal">true</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">代码解读</h2>
<p>⭐ <strong>初始化变量</strong> <code>propsData</code>  存放父组件传入子组件的 <code>props</code>。<code>const props = vm._props = &#123; &#125; </code> 存放经过转换后的最终的 <code>props</code> 的对象 , <code>props</code> 与 <code>vm._props</code> 保持同一个引用，初始值为 <code>&#123;&#125;</code>。
<code>const keys = vm.$options._propKeys = [] </code>， <code>keys</code> 与 <code>vm.$options._propKeys</code> 保持同一个引用，初始值为 <code>[]</code> 。<code>isRoot</code> 判断是不是根元素。</p>
<p>⭐ 当组件不是根组件时，使用 <code>toggleObserving(false)</code> 取消对<code> Object</code> <code>Array</code> 类型 <code>Prop</code> 深度观测。</p>
<p>⭐ 遍历 <code>props</code> 配置对象。缓存 <code>props</code> 的每个 <code>key</code> ，用以性能优化 。</p>
<p>⭐ 校验是否为预期的类型值，然后返回相应 <code>prop</code> 值(或 <code>default</code> 值)，如果有定义类型检查，布尔值没有默认值时会被赋予 <code>false</code>，字符串默认 <code>undefined</code>。</p>
<p>⭐ <code>defineReactive</code>，对属性建立观察。</p>
<p>⭐ 当实例上没有同名属性时，对属性进行代理操作 , 将对键名的引用指向 <code>vm._props</code> 对象中。</p>
<p>⭐ 开启观察状态标识,重新打开观测开关，避免影响后续代码执行<code> toggleObserving(true)</code>。</p>
<p>⭐ 本文对 <code>initProps</code>  掌握到这里即可，后面会详细分析 <code>defineReactive</code> 方法。</p>
<h1 data-id="heading-11">initMethods</h1>
<h2 data-id="heading-12">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化methods
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>methods 实例配置项上面的methods vm.$options.methods
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMethods</span> (<span class="hljs-params">vm: Component, methods: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-comment">// 获取实例配置上的props</span>
  <span class="hljs-keyword">const</span> props = vm.$options.props
  <span class="hljs-comment">// 做一些检查 然后赋值给Vue实例</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> methods) &#123;
    <span class="hljs-comment">// 判断环境 只在非生产环境下起作用</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">// 判断key是否是function类型</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> methods[key] !== <span class="hljs-string">'function'</span>) &#123;
        warn(
          <span class="hljs-string">`Method "<span class="hljs-subst">$&#123;key&#125;</span>" has type "<span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> methods[key]&#125;</span>" in the component definition. `</span> +
          <span class="hljs-string">`Did you reference the function correctly?`</span>,
          vm
        )
      &#125;
      <span class="hljs-comment">// 检测 methods 中的属性名是否与 props 冲突，由 initState 方法我们知道，props 是先与 methods 初始化的。</span>
      <span class="hljs-keyword">if</span> (props && hasOwn(props, key)) &#123;
        warn(
          <span class="hljs-string">`Method "<span class="hljs-subst">$&#123;key&#125;</span>" has already been defined as a prop.`</span>,
          vm
        )
      &#125;
      <span class="hljs-comment">// 检测 methods 是否使用了关键字保留字， 而且不允许以$ 或者 _ 开头。</span>
      <span class="hljs-keyword">if</span> ((key <span class="hljs-keyword">in</span> vm) && isReserved(key)) &#123;
        warn(
          <span class="hljs-string">`Method "<span class="hljs-subst">$&#123;key&#125;</span>" conflicts with an existing Vue instance method. `</span> +
          <span class="hljs-string">`Avoid defining component methods that start with _ or $.`</span>
        )
      &#125;
    &#125;
    <span class="hljs-comment">/**
     * 将 methods 中的所有方法赋值到 vue 实例上 ,支持通过 this.methodsKey 的方式访问定义的方法
     * 如果 key 不是一个函数 则赋值为空函数
     * 如果 key 是函数 则执行bind()函数
     */</span>
    vm[key] = <span class="hljs-keyword">typeof</span> methods[key] !== <span class="hljs-string">'function'</span> ? noop : bind(methods[key], vm)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">代码解读</h2>
<p>⭐ 判断属性是否是 <code>function</code> 类型，检测 <code>methods</code> 中的属性名是否与 <code>props</code> 冲突，由 <code>initState</code> 方法我们知道，<code>props</code> 是先于 <code>methods</code> 初始化的。检测 <code>methods</code> 是否使用了关键字保留字，而且不允许以 <code>$</code> 或者 <code>_</code> 开头。</p>
<p>⭐ 将 <code>methods</code> 中的所有方法赋值到 <code>vue</code> 实例上 , 支持通过 <code>this.methodsKey</code> 的方式访问定义的方法。</p>
<h1 data-id="heading-14">initData</h1>
<h2 data-id="heading-15">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化data
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-comment">//从vm.$options.data里面拿到data,就是我们在开发时候定义的data  赋值给data 还有vm._data</span>
  <span class="hljs-keyword">let</span> data = vm.$options.data
  <span class="hljs-comment">/**
   * 判断data是不是一个function 保证后续处理的data是一个对象
   * 如果是 执行getData方法
   * 如果不是 返回 data || &#123;&#125;
   */</span>

  data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span>
    ? getData(data, vm)
    : data || &#123;&#125;

  <span class="hljs-comment">//如果不是个对象的话,开发环境下会报一个警告</span>
  <span class="hljs-keyword">if</span> (!isPlainObject(data)) &#123;
    <span class="hljs-comment">//把data重置为一个空对象</span>
    data = &#123;&#125;
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">'data functions should return an object:\n'</span> +
      <span class="hljs-string">'https://vuejs.org/v2/guide/components.html#data-Must-Be-a-Function'</span>,
      vm
    )
  &#125;
  <span class="hljs-comment">//拿到data对象的key 组成一个数组</span>
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(data)
  <span class="hljs-comment">//拿到props</span>
  <span class="hljs-keyword">const</span> props = vm.$options.props
  <span class="hljs-comment">//拿到methods</span>
  <span class="hljs-keyword">const</span> methods = vm.$options.methods

  <span class="hljs-comment">/**
   * 循环判断data中的属性和props,methods中的属性是否冲突
   * 因为所有的data,props,methods最终都会挂载到vm实例上
   */</span>

  <span class="hljs-keyword">let</span> i = keys.length
  <span class="hljs-keyword">while</span> (i--) &#123;
    <span class="hljs-keyword">const</span> key = keys[i]
    <span class="hljs-comment">//非生产环境</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">//与methods判重</span>
      <span class="hljs-keyword">if</span> (methods && hasOwn(methods, key)) &#123;
        warn(
          <span class="hljs-string">`Method "<span class="hljs-subst">$&#123;key&#125;</span>" has already been defined as a data property.`</span>,
          vm
        )
      &#125;
    &#125;
    <span class="hljs-comment">//与props判重</span>
    <span class="hljs-keyword">if</span> (props && hasOwn(props, key)) &#123;
      process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
        <span class="hljs-string">`The data property "<span class="hljs-subst">$&#123;key&#125;</span>" is already declared as a prop. `</span> +
        <span class="hljs-string">`Use prop default value instead.`</span>,
        vm
      )
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isReserved(key)) &#123;
      <span class="hljs-comment">//判重通过,最终交给proxy做代理 ,代理data中的属性到vue实例,支持通过 this.dataKey 的方式访问定义的属性</span>
      proxy(vm, <span class="hljs-string">`_data`</span>, key)
    &#125;
  &#125;
  <span class="hljs-comment">// 对data进行响应式处理</span>
  observe(data, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>)
&#125;

<span class="hljs-comment">//如果data是一个函数 那么会走这个方法</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span> (<span class="hljs-params">data: <span class="hljs-built_in">Function</span>, vm: Component</span>): <span class="hljs-title">any</span> </span>&#123;

  <span class="hljs-comment">// 收集依赖</span>
  pushTarget()
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 调用call 返回的值就是这个对象</span>
    <span class="hljs-keyword">return</span> data.call(vm, vm)
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    handleError(e, vm, <span class="hljs-string">`data()`</span>)
    <span class="hljs-keyword">return</span> &#123;&#125;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-comment">// 释放依赖</span>
    popTarget()
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">代码解读</h2>
<p>⭐ <code>data</code> 为空，直接观测一个空对象 <code>observe(vm._data = &#123;&#125; , true)</code></p>
<p>⭐ <code>data</code> 不为空，判断 <code>data</code> 是不是一个 <code>function</code>，保证后续处理的 <code>data</code> 是一个对象。</p>
<p>⭐ 循环判断 <code>data</code> 中的属性和 <code>props</code> , <code>methods</code> 中的属性是否冲突，由 <code>initState</code> 方法我们知道，<code>props</code> ，<code>methods</code> 是先于 <code>methods</code> 初始化的。</p>
<p>⭐ 对 <code>data</code> 进行响应式处理 <code>observe(data , true)</code></p>
<p>⭐ 本文对 <code>initData</code>  掌握到这里即可，后面会详细分析 <code>observe</code> 方法。</p>
<h1 data-id="heading-17">initComputed</h1>
<h2 data-id="heading-18">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//用于传入Watcher实例的一个对象 懒执行</span>
<span class="hljs-keyword">const</span> computedWatcherOptions = &#123; <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span> &#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化computed
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>computed 定义的computed配置
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initComputed</span> (<span class="hljs-params">vm: Component, computed: <span class="hljs-built_in">Object</span></span>) </span>&#123;

  <span class="hljs-comment">// 声明变量 watchers，与 vm._computedWatchers 保持同一个引用，并且初始化值为空对象。</span>
  <span class="hljs-keyword">const</span> watchers = vm._computedWatchers = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)

  <span class="hljs-comment">// 声明变量isSSR,判断是不是 ssr(服务端渲染)</span>
  <span class="hljs-keyword">const</span> isSSR = isServerRendering()

  <span class="hljs-comment">// 遍历 computed 配置对象 </span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> computed) &#123;
    <span class="hljs-comment">// 获取 key 当次遍历对应的值.</span>
    <span class="hljs-keyword">const</span> userDef = computed[key]
    <span class="hljs-comment">/**
     * 使用过 computed 都知道,它有两种写法  函数写法以及对象写法
     * computed: &#123;
        compA: function() &#123; return this.a + 1 &#125;,
        compB: &#123;
                 get: function() &#123; return this.b + 1 &#125;,
               &#125;
       &#125;
     * 判断是不是函数,如果是函数 getter 就是函数本身,如果是对象,getter就用他的get属性
     */</span>
    <span class="hljs-keyword">const</span> getter = <span class="hljs-keyword">typeof</span> userDef === <span class="hljs-string">'function'</span> ? userDef : userDef.get

    <span class="hljs-comment">// 非开发环境下getter如果为null,警告</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && getter == <span class="hljs-literal">null</span>) &#123;
      warn(
        <span class="hljs-string">`Getter is missing for computed property "<span class="hljs-subst">$&#123;key&#125;</span>".`</span>,
        vm
      )
    &#125;

    <span class="hljs-comment">// 如果不是SSR</span>
    <span class="hljs-keyword">if</span> (!isSSR) &#123;
      <span class="hljs-comment">/**
       * 针对当次循环的 computed，实例化一个 Watcher , 所以computed其实就是通过Watcher来实现的
       * watchers 保存了 vm._computedWatchers 的引用，所以这里同样会将该 watcher 保存到 vm._computedWatchers。
       * 每一个 computed 的 key，都会生成一个 watcher 实例，并且保存到 vm._computedWatchers 这个对象上。
       */</span>

      watchers[key] = <span class="hljs-keyword">new</span> Watcher(
        vm, <span class="hljs-comment">//实例vm</span>
        getter || noop, <span class="hljs-comment">// getter</span>
        noop, <span class="hljs-comment">// 空函数</span>
        computedWatcherOptions <span class="hljs-comment">// 配置对象 懒执行(不可更改)</span>
      )
    &#125;

    <span class="hljs-comment">//if 语句用来检测 computed 的命名是否与 data，props 冲突，在非生产环境将会打印警告信息。</span>
    <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> vm)) &#123;
      <span class="hljs-comment">//不冲突时，调用 defineComputed 方法。</span>
      defineComputed(vm, key, userDef)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> vm.$data) &#123;
      <span class="hljs-comment">//与data中的属性冲突</span>
        warn(<span class="hljs-string">`The computed property "<span class="hljs-subst">$&#123;key&#125;</span>" is already defined in data.`</span>, vm)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vm.$options.props && key <span class="hljs-keyword">in</span> vm.$options.props) &#123;
        <span class="hljs-comment">//与props中的属性冲突</span>
        warn(<span class="hljs-string">`The computed property "<span class="hljs-subst">$&#123;key&#125;</span>" is already defined as a prop.`</span>, vm)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vm.$options.methods && key <span class="hljs-keyword">in</span> vm.$options.methods) &#123;
        <span class="hljs-comment">//与methods中的属性冲突</span>
        warn(<span class="hljs-string">`The computed property "<span class="hljs-subst">$&#123;key&#125;</span>" is already defined as a method.`</span>, vm)
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 为 sharedPropertyDefinition 添加 get， set 属性,将该 computed 属性添加到 Vue 实例 vm 上，并使用 sharedPropertyDefinition 作为设置项。
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target vm实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key 当次循环的computedKey
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>userDef   computed.key
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComputed</span> (<span class="hljs-params">
  target: any,
  key: string,
  userDef: <span class="hljs-built_in">Object</span> | <span class="hljs-built_in">Function</span>
</span>) </span>&#123;
  <span class="hljs-comment">//</span>
  <span class="hljs-keyword">const</span> shouldCache = !isServerRendering()


  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> userDef === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 如果computed.key是function类型走这里</span>

    <span class="hljs-comment">//设置sharedPropertyDefinition配置对象的get方法</span>
    sharedPropertyDefinition.get = shouldCache
      ? createComputedGetter(key)
      : createGetterInvoker(userDef)
    <span class="hljs-comment">//设置sharedPropertyDefinition配置对象的set方法</span>
    sharedPropertyDefinition.set = noop
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//如果computed.key不是function类型走这里</span>

    <span class="hljs-comment">//设置sharedPropertyDefinition配置对象的get方法</span>
    sharedPropertyDefinition.get = userDef.get
      ? shouldCache && userDef.cache !== <span class="hljs-literal">false</span>
        ? createComputedGetter(key)
        : createGetterInvoker(userDef.get)
      : noop
    <span class="hljs-comment">//设置sharedPropertyDefinition配置对象的get方法</span>
    sharedPropertyDefinition.set = userDef.set || noop
  &#125;
  <span class="hljs-comment">//如果是非生产环境 并且sharedPropertyDefinition的set方法是noop</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
      sharedPropertyDefinition.set === noop) &#123;
    <span class="hljs-comment">//将sharedPropertyDefinition的set方法设置为警告</span>
    sharedPropertyDefinition.set = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      warn(
        <span class="hljs-string">`Computed property "<span class="hljs-subst">$&#123;key&#125;</span>" was assigned to but it has no setter.`</span>,
        <span class="hljs-built_in">this</span>
      )
    &#125;
  &#125;
  <span class="hljs-comment">//将computed配置项中的key,代理到vue实例上,支持通过this.computedKey的方式去访问 computed中的属性</span>
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, sharedPropertyDefinition)
&#125;


<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 在这里我们暂时只需要知道sharedPropertyDefinition的 get属性 被设置为这个方法的返回值就行
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key computedKey
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">computedGetter</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComputedGetter</span> (<span class="hljs-params">key</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computedGetter</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//拿到watcher</span>
    <span class="hljs-keyword">const</span> watcher = <span class="hljs-built_in">this</span>._computedWatchers && <span class="hljs-built_in">this</span>._computedWatchers[key]
    <span class="hljs-keyword">if</span> (watcher) &#123;
      <span class="hljs-keyword">if</span> (watcher.dirty) &#123;
        <span class="hljs-comment">//执行watcher.evaluate方法</span>
        watcher.evaluate()
      &#125;
      <span class="hljs-keyword">if</span> (Dep.target) &#123;
        watcher.depend()
      &#125;
      <span class="hljs-keyword">return</span> watcher.value
    &#125;
  &#125;
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 在这里我们暂时只需要知道sharedPropertyDefinition的 get属性 被设置为这个方法的返回值就行
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>fn userDef.get
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">computedGetter</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createGetterInvoker</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computedGetter</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> fn.call(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">代码解读</h2>
<p>⭐ 声明变量 <code>watchers</code>，与 <code>vm._computedWatchers</code> 保持同一个引用，并且初始化值为空对象。</p>
<p>⭐ 声明变量 <code>isSSR</code> , 判断是不是 <code>ssr</code> (服务端渲染)。</p>
<p>⭐ 遍历 <code>computed</code> 配置对象，声明 <code>userDef</code> 变量存放当次遍历 <code>key</code> 对应的值  。 声明  <code>getter</code> 变量， 判断 <code>userDef</code> 是不是函数 , 如果是函数 <code>getter</code> 就是函数本身 , 如果是对象  <code>getter</code> 就用他的 <code>get</code> 属性 。非生产环境下 <code>getter</code> 如果为 <code>null</code> , 发出警告。如果不是 <code>SSR</code>，针对当次循环的 <code>computed</code>，实例化一个 <code>Watcher</code> 。<code>watchers</code> 保存了 <code>vm._computedWatchers</code> 的引用，所以这里同样会将该 <code>watcher</code> 保存到 <code>vm._computedWatchers</code>。每一个 <code>computed</code> 的 <code>key</code>，都会生成一个 <code>watcher</code> 实例，并且保存到 <code>vm._computedWatchers</code> 这个对象上。检测 <code>computed</code> 的命名是否与 <code>data</code>，<code>props</code> 冲突，在非生产环境将会打印警告信息。不冲突时，调用 <code>defineComputed</code> 方法。</p>
<p>⭐ 本文对 <code>initComputed</code>  掌握到这里即可，后面会详细分析 <code>defineComputed</code> 方法。</p>
<h1 data-id="heading-20">initWatch</h1>
<h2 data-id="heading-21">代码注释</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 初始化watch
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>watch  watch配置项 / vm.$options.watch
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initWatch</span> (<span class="hljs-params">vm: Component, watch: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  
  <span class="hljs-comment">//遍历watch配置项  从这可以看出 key 和 watcher 实例可能是 一对多 的关系</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> watch) &#123;
    <span class="hljs-comment">//获取当次遍历 key 对应的值</span>
    <span class="hljs-keyword">const</span> handler = watch[key]
    <span class="hljs-comment">//如果是数组的话</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(handler)) &#123;
      <span class="hljs-comment">//循环数组 为数组的每一项调用createWatcher方法</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < handler.length; i++) &#123;
        createWatcher(vm, key, handler[i])
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果不是数组 直接调用createWatcher方法</span>
      createWatcher(vm, key, handler)
    &#125;
  &#125;
&#125;


<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 兼容性处理，保证 handler 肯定是一个函数,调用 $watch 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例vm
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>expOrFn watchKey
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>handler watch.key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options 配置选项
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWatcher</span> (<span class="hljs-params">
  vm: Component,
  expOrFn: string | <span class="hljs-built_in">Function</span>,
  handler: any,
  options?: <span class="hljs-built_in">Object</span>
</span>) </span>&#123;
  <span class="hljs-comment">//如果是对象 从 handler 属性中获取函数</span>
  <span class="hljs-keyword">if</span> (isPlainObject(handler)) &#123;
    options = handler
    handler = handler.handler
  &#125;
  <span class="hljs-comment">//如果是字符串 表示的是一个methods方法,直接通过 this.methodsKey的方式  拿到这个函数</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> handler === <span class="hljs-string">'string'</span>) &#123;
    handler = vm[handler]
  &#125;
  <span class="hljs-comment">//调用vm.$watch方法</span>
  <span class="hljs-keyword">return</span> vm.$watch(expOrFn, handler, options)
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">代码解读</h2>
<p>⭐ 遍历 <code>watch</code> 配置项  ，获取当次遍历 <code>key</code> 对应的值，如果是数组的话，循环数组，为数组的每一项调用 <code>createWatcher</code> 方法，如果不是数组，直接调用 <code>createWatcher</code> 方法。</p>
<p>⭐ 从这可以看出 <code>key</code> 和 <code>watcher</code> 实例可能是 <strong>一对多</strong> 的关系。</p>
<p>⭐ 本文对 <code>initWatch</code>  掌握到这里即可，后面会详细分析 <code>createWatcher</code> 方法。</p>
<h1 data-id="heading-23">总结</h1>
<h2 data-id="heading-24">最后我们用一张思维导图总结一下</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4daaf967944141818cf41514aba5f699~tplv-k3u1fbpfcp-watermark.image" alt="响应式原理.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-25">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/" ref="nofollow noopener noreferrer">Vue.js 技术揭秘</a></p>
<p><a href="https://juejin.cn/column/6960553066101735461" target="_blank" title="https://juejin.cn/column/6960553066101735461">精通 Vue 技术栈的源码原理</a></p>
<p>本文由 <a href="https://juejin.cn/user/1028798616461326" target="_blank" title="https://juejin.cn/user/1028798616461326">李永宁</a> 教程结合自己的想法整理而来，在此特别感谢前辈。</p></div>  
</div>
            