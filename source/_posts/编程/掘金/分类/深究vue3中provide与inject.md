
---
title: '深究vue3中provide与inject'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1183'
author: 掘金
comments: false
date: Mon, 19 Apr 2021 04:37:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=1183'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在vue中,组件之间的通讯方式有很多种, 比如父组件向子组件传参使用props、子组件与父组件通信使用emit、兄弟组件通信使用eventBus/(provides/inject)。现在就一起来研究一下provide与inject的实现吧.</p>
<h3 data-id="heading-0">provide</h3>
<p>在开发过程中, 我们经常会在父组件或更上级的组件中使用provide, 然后在子孙组件中使用inject来接受, vue中的provideAPI给我们的开发带来了很大的便利,而且在使用过程中, 父级组件不需要知道哪些子孙组件在调用当前的provide, 而子孙组件也不需要知道当前inject调用的函数来自哪里。
下面让我们一起来看一下vue3源码中关于provideAPI的实现吧。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">provide</span><<span class="hljs-title">T</span>>(<span class="hljs-params">key: InjectionKey<T> | string | number, value: T</span>) </span>&#123;
  <span class="hljs-comment">// 如果定义当前provide的组件不存在 在开发环境下发出警告⚠️</span>
  <span class="hljs-keyword">if</span> (!currentInstance) &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      warn(<span class="hljs-string">`provide() can only be used inside setup().`</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">let</span> provides = currentInstance.provides
    <span class="hljs-keyword">const</span> parentProvides =
      currentInstance.parent && currentInstance.parent.provides
    <span class="hljs-keyword">if</span> (parentProvides === provides) &#123;
      provides = currentInstance.provides = <span class="hljs-built_in">Object</span>.create(parentProvides)
    &#125;
    <span class="hljs-comment">// TS doesn't allow symbol as index type</span>
    <span class="hljs-comment">// 相同key值的情况下 父级组件的provide会覆盖根组件的provide</span>
    provides[key <span class="hljs-keyword">as</span> string] = value
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，相对与watchAPI来说 provide的代码并不是很长, 让我带大家一起分析一下吧.
从代码中可以看到 provide函数其实只做了一件事情, 就是将当前传入的函数添加到了provides对象中, 在其中需要注意的一点是, 当你在根组件传入一个provide之后, 如果key值相同,在父组件中传入的provide会覆盖根组件中的provide, 这点在开发过程中还是需要注意的.
接下来一起在看一下inject的实现吧.</p>
<h3 data-id="heading-1">inject</h3>
<p>上面说到provideAPI方法将接受的所有key、value全部放到了一个provides对象中, 那么有些小伙伴应该可以猜到, inject函数其实是对provides中的方法进行了调用, 接下来就一起来看一下尤大的代码吧</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inject</span>(<span class="hljs-params">
  key: InjectionKey<any> | string,
  defaultValue?: unknown,
  treatDefaultAsFactory = <span class="hljs-literal">false</span>
</span>) </span>&#123;
  <span class="hljs-comment">// fallback to `currentRenderingInstance` so that this can be called in</span>
  <span class="hljs-comment">// a functional component</span>
  <span class="hljs-keyword">const</span> instance = currentInstance || currentRenderingInstance
  <span class="hljs-keyword">if</span> (instance) &#123;
    <span class="hljs-comment">// #2400</span>
    <span class="hljs-comment">// to support `app.use` plugins,</span>
    <span class="hljs-comment">// fallback to appContext's `provides` if the intance is at root</span>
    <span class="hljs-keyword">const</span> provides =
      instance.parent == <span class="hljs-literal">null</span>
        ? instance.vnode.appContext && instance.vnode.appContext.provides
        : instance.parent.provides
    <span class="hljs-comment">// 判断当前的函数是否存在于provides数组 如果存在调用当前函数, 如果不存在则判断第二个参数是否存在, 如果第二个参数存在 判断第二个参数是否为一个函数, 如果为函数则调用这个函数, 否则直接返回第二个参数 如果第二个参数不存在则返回一段警告</span>
    <span class="hljs-keyword">if</span> (provides && (key <span class="hljs-keyword">as</span> string | symbol) <span class="hljs-keyword">in</span> provides) &#123;
      <span class="hljs-comment">// TS doesn't allow symbol as index type</span>
      <span class="hljs-keyword">return</span> provides[key <span class="hljs-keyword">as</span> string]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length > <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> treatDefaultAsFactory && isFunction(defaultValue)
        ? defaultValue()
        : defaultValue
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__DEV__) &#123;
      warn(<span class="hljs-string">`injection "<span class="hljs-subst">$&#123;<span class="hljs-built_in">String</span>(key)&#125;</span>" not found.`</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__DEV__) &#123;
    warn(<span class="hljs-string">`inject() can only be used inside setup() or functional components.`</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在inject函数中, 该函数接收三个参数, 第一个参数为你要调用的provide方法的key, 通过provides去调用当前的key值所对应的方法, 第二个参数为一个默认值, 第三个参数是一个选填的布尔值, 咱们接着往下分析,</p>
<ol>
<li>代码中首先当前实例是否为根组件, 接着判断了provides中是否存在当前需要调用函数的key, 如果存在则返回这个函数的执行结果,</li>
<li>如果不存在则判断inject接收参数的数量, 这时候就要看第二个参数和第三个参数了, 第三个参数treatDefaultAsFactory更像是一个开关, 用来控制是否需要第二个参数,</li>
<li>如果treatDefaultAsFactory为true且第二个参数是个函数, 直接返回这个函数的默认结果, 否则会直接返回第二个参数.</li>
<li>如果不满足上述条件则会返回一段警告.</li>
</ol>
<p>怎么样,看完之后是不是觉得provide很简单呢😄。</p>
<blockquote>
<p>本段代码位于packake/runtime-core/src/apiInject.ts。有兴趣的去看一下吧。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            