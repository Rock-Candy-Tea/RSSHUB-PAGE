
---
title: 'Vue3 源码分析之 - 手写响应式原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6459'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 02:49:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=6459'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Computed 函数内部实现。 接收一个有返回值的函数作为参数。这个函数的返回值就是计算属性的值。并且我们要监听这个函数内容使用的响应式数据的变化，最后将这个函数执行的结果返回。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> functon <span class="hljs-function"><span class="hljs-title">computed</span>(<span class="hljs-params">getter</span>)</span>&#123;

    <span class="hljs-comment">// 1. 最终要返回一个 ref创建的具有value属性的对象</span>

    <span class="hljs-keyword">const</span> result = ref();

    <span class="hljs-comment">// 2. 监听响应式数据的变化。当数据变化后会重新执行effect函数，把getter的结果再存储到result中</span>

    effect(<span class="hljs-function">() =></span> (result.value = getter()))；

    <span class="hljs-keyword">return</span> result

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>so，你肯定会觉得：</strong> <strong>这么容易就没了？你在逗我玩，你个菜J。</strong></p>
<h1 data-id="heading-0">1.从你用过的reactive开始</h1>
<p><strong><code>reactive</code></strong>：</p>
<ul>
<li>接收一个参数，判断这参数对象是否是Object</li>
<li>创建拦截器对象 <code>handler</code>，设置<code>set/get/deleteProperty</code> 方法</li>
<li><code>return Proxy</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span> (<span class="hljs-params">target</span>) </span>&#123;

  <span class="hljs-comment">// 先判断 target 是否是对象，不是对象之间 return 出去</span>

  <span class="hljs-keyword">if</span> (!isObject(target)) <span class="hljs-keyword">return</span> target

  

  <span class="hljs-comment">// 拦截器对象</span>

  <span class="hljs-keyword">const</span> handler = &#123;

    get (target, key, receiver) &#123;
    <span class="hljs-comment">// code...</span>
    &#125;,

    set (target, key, value, receiver) &#123;
    <span class="hljs-comment">// code...</span>
    &#125;,

    deleteProperty (target, key) &#123;
    <span class="hljs-comment">// code...</span>
    &#125;

  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那我们的 <code>get</code> 方法目的是获取 <code>target</code> 的 <code>key</code> 的值。 如果 <code>key</code> 值本身还是个 <code>Object</code> 的话，那就得继续往下递归？ 来，往下coding。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> convert = <span class="hljs-function"><span class="hljs-params">target</span> =></span> isObject(target) ? reactive(target) : target;


<span class="hljs-comment">// 为了后续不再重复书写辅助类工具函数，先一并写上。直接看函数名你也就明白了。</span>

<span class="hljs-keyword">const</span> isObject = <span class="hljs-function"><span class="hljs-params">val</span> =></span> val !== <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span>

<span class="hljs-keyword">const</span> convert = <span class="hljs-function"><span class="hljs-params">target</span> =></span> isObject(target) ? reactive(target) : target

<span class="hljs-keyword">const</span> hasOwnProperty = <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty

<span class="hljs-keyword">const</span> hasOwn = <span class="hljs-function">(<span class="hljs-params">target, key</span>) =></span> hasOwnProperty.call(target, key);

<span class="hljs-keyword">let</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-comment">// code ...</span>



get (target, key, receiver) &#123;
      <span class="hljs-comment">// 收集依赖</span>
      <span class="hljs-comment">// track(target, key)</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get:'</span>,key);
      <span class="hljs-comment">// 返回target洪的key的值</span>
      <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);

      <span class="hljs-keyword">return</span> convert(result)

&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，人人都说递归、闭包、嵌套循环不好。但你无法否认的是：真香……</p>
<p>继续。我们的 <code>set</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js">set (target, key, value, receiver) &#123;

      <span class="hljs-keyword">const</span> oldValue = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver)

      <span class="hljs-keyword">let</span> result = <span class="hljs-literal">true</span>

      <span class="hljs-keyword">if</span> (oldValue !== value) &#123;

        result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver)

        <span class="hljs-comment">// 触发更新</span>

        <span class="hljs-comment">// trigger(target, key);</span>

        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set key:'</span>,key,<span class="hljs-string">'value:'</span>,value);

      &#125;

      <span class="hljs-keyword">return</span> result

&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，你没看错，你都 <code>set</code> 值了，当然要触发更新了。 但你以为现在就写 <code>trigger</code> 吗？</p>
<p>👌 我们来看 <code>deleteProperty</code> 方法</p>
<pre><code class="copyable">deleteProperty (target, key) &#123;

      const hadKey = hasOwn(target, key); // 头上辣个辅助函数。 23333.

      const result = Reflect.deleteProperty(target, key)

      if (hadKey && result) &#123;

        // 触发更新

        // trigger(target, key)

        console.log('delete:',key);

      &#125;

      return result

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>trigger：</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span> (<span class="hljs-params">target, key</span>) </span>&#123;

  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target); <span class="hljs-comment">// 憋问 targetMap 哪来的，最前面写了。</span>

  <span class="hljs-keyword">if</span> (!depsMap) <span class="hljs-keyword">return</span> 

  <span class="hljs-keyword">const</span> dep = depsMap.get(key)

  <span class="hljs-keyword">if</span> (dep) &#123;

    dep.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;

      effect()

    &#125;)

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">effect & track - 收集依赖</h1>
<p>先来看个使用栗子</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">

    <span class="hljs-keyword">import</span> &#123; reactive, effect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./text2.js'</span>

    <span class="hljs-keyword">const</span> product = reactive(&#123;

      <span class="hljs-attr">name</span>: <span class="hljs-string">'你大爷'</span>,

      <span class="hljs-attr">price</span>: <span class="hljs-number">100</span>,

      <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>

    &#125;)

    <span class="hljs-keyword">let</span> total = <span class="hljs-number">0</span> 

    effect(<span class="hljs-function">() =></span> &#123;

      total = product.price * product.count

    &#125;)

    <span class="hljs-built_in">console</span>.log(total) <span class="hljs-comment">// 100</span>

    product.price = <span class="hljs-number">2000</span>

    <span class="hljs-built_in">console</span>.log(total) <span class="hljs-comment">// 2000</span>

    product.count = <span class="hljs-number">10</span>

    <span class="hljs-built_in">console</span>.log(total) <span class="hljs-comment">// 20000</span>

  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果栗子中三个 <code>console</code> 的结果是正确的话，<strong>那</strong> <strong>effect</strong> <strong>究竟做了哪些事情？</strong></p>
<ul>
<li>首次加载，执行effect内部的箭头函数。 箭头函数中访问了 product 。 product 是 reactive返回的响应式对象，也就是代理对象。当我们访问product. price 属性的时候会触发price属性的get方法。 在get方法中要收集依赖。过程就是存储这个属性和这个回调函数。而属性又跟对象相关，所以在代理对象中的get方法中首先会存储target目标对象。然后是target对象的属性，以及箭头函数。</li>
<li>触发更新时，会根据属性找到对应的函数。</li>
<li>继续收集下一个属性的依赖。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> activeEffect = <span class="hljs-literal">null</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span> (<span class="hljs-params">callback</span>) </span>&#123;

  activeEffect = callback

  callback() <span class="hljs-comment">// 访问响应式对象属性，去收集依赖</span>

  activeEffect = <span class="hljs-literal">null</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><del>（默默吐槽下：和react是真的像，网上那些喷子说的也不是完全没道理。）</del></p>
<p>Track 方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()

<span class="hljs-comment">// 收集依赖</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span> (<span class="hljs-params">target, key</span>) </span>&#123;

  <span class="hljs-keyword">if</span> (!activeEffect) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 如果没有依赖，直接出去</span>

  <span class="hljs-keyword">let</span> depsMap = targetMap.get(target) <span class="hljs-comment">// 寻找目标对象的依赖</span>

  <span class="hljs-keyword">if</span> (!depsMap) &#123;

    targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()))； <span class="hljs-comment">// 没找到就新创建一个depsMap</span>

  &#125;

  <span class="hljs-keyword">let</span> dep = depsMap.get(key) <span class="hljs-comment">// 寻找当前key 的 dep</span>

  <span class="hljs-keyword">if</span> (!dep) &#123;

    depsMap.set(key, (dep = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>())) <span class="hljs-comment">// 没找到，添加new Set</span>

  &#125;

  dep.add(activeEffect) 

&#125;



<span class="hljs-comment">// 然后去 get 方法里收集依赖</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3 trigger - 触发更新</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span> (<span class="hljs-params">target, key</span>) </span>&#123;

  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target)

  <span class="hljs-keyword">if</span> (!depsMap) <span class="hljs-keyword">return</span>

  <span class="hljs-keyword">const</span> dep = depsMap.get(key)

  <span class="hljs-keyword">if</span> (dep) &#123;

    dep.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;

      effect()

    &#125;)

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看实操吧。。</p>
<h1 data-id="heading-3">4. ref</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span> (<span class="hljs-params">raw</span>) </span>&#123;

  <span class="hljs-comment">// 判断 raw 是否是ref 创建的对象，如果是的话直接返回</span>

  <span class="hljs-keyword">if</span> (isObject(raw) && raw.__v_isRef) &#123;

    <span class="hljs-keyword">return</span>

  &#125;

  <span class="hljs-keyword">let</span> value = convert(raw)

  <span class="hljs-keyword">const</span> r = &#123;

    <span class="hljs-attr">__v_isRef</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 不要问为啥这个属性名非得长这样，Vue3源码里就是长这样</span>

    get value () &#123;
      track(r, <span class="hljs-string">'value'</span>)
      <span class="hljs-keyword">return</span> value
    &#125;,

    set value (newValue) &#123;
      <span class="hljs-keyword">if</span> (newValue !== value) &#123;
        raw = newValue
        value = convert(raw)
        trigger(r, <span class="hljs-string">'value'</span>)
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> r

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5. computed</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span> (<span class="hljs-params">getter</span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = ref()
  effect(<span class="hljs-function">() =></span> (result.value = getter()))
  <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>请你回到文章开头，</strong> <strong>此刻还会认为我是个菜J吗？是不是简单到哭？</strong></p>
<h1 data-id="heading-5">End</h1>
<p><strong>最后来比较一下 <code>reactive</code> 和 <code>ref</code> 的区别</strong></p>
<ul>
<li><code>ref</code> 可以把基本数据类型转成响应式对象</li>
<li><code>ref</code> 返回的对象，即使重新赋值新的对象，也依然是响应式的</li>
<li><code>reactive</code> 返回的对象，重新赋值会丢失响应式</li>
<li><code>reactive</code> 返回的对象无法解构。</li>
</ul></div>  
</div>
            