
---
title: '全面了解Vue3的 ref 以及相关函数和计算属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44606b4c093a4da593a0afb3304364a7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 17:31:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44606b4c093a4da593a0afb3304364a7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">基础类型的响应性 —— ref</h1>
<p>在vue3里面，我们可以通过 reactive 来实现引用类型的响应性，那么基础类型的响应性如何来实现呢？</p>
<p>可能你会想到这样来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = reactive(&#123;<span class="hljs-attr">value</span>: <span class="hljs-number">0</span>&#125;)
count.value += <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么做确实可以实现，而且也很像 ref 的使用方式，都是要 .value 嘛。那么 ref内部 是不是这么实现的呢？</p>
<p>我们先定义两个 ref 的实例并且打印看看。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> refCount = ref(<span class="hljs-number">0</span>) <span class="hljs-comment">// 基础类型</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'refCount '</span>, refCount )

    <span class="hljs-keyword">const</span> refObject = ref(&#123; <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;) <span class="hljs-comment">// 引用类型</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'refObject '</span>, refObject )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下结果：</p>
<p><img alt="基础类型的 ref " class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44606b4c093a4da593a0afb3304364a7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="引用类型的 ref " class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aa14ab3474a42828e378af9b80dd48f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们都知道 reactive 是通过 ES6 的 Proxy 来实现的，基础类型的 ref 显然和 Proxy 没啥关系，而引用类型的 ref 是先把原型变成 reactive， 然后再挂到 value 上面。
这样看来，和我们的猜测不太一样呢，那么 ref 到底是如何实现的呢？我们可以看一下 ref 的源码。</p>
<h1 data-id="heading-1">ref 的源码</h1>
<p>代码来自于 vue.global.js ，调整了一下先后顺序。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">return</span> createRef(value);
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRef</span>(<span class="hljs-params">rawValue, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (isRef(rawValue)) &#123;
          <span class="hljs-keyword">return</span> rawValue;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> RefImpl(rawValue, shallow);
  &#125;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RefImpl</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">_rawValue, _shallow = <span class="hljs-literal">false</span></span>)</span> &#123;
          <span class="hljs-built_in">this</span>._rawValue = _rawValue;
          <span class="hljs-built_in">this</span>._shallow = _shallow;
          <span class="hljs-built_in">this</span>.__v_isRef = <span class="hljs-literal">true</span>;
          <span class="hljs-built_in">this</span>._value = _shallow ? _rawValue : convert(_rawValue); <span class="hljs-comment">// 深层 ref or 浅层ref</span>
      &#125;
      <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
          track(toRaw(<span class="hljs-built_in">this</span>), <span class="hljs-string">"get"</span> <span class="hljs-comment">/* GET */</span>, <span class="hljs-string">'value'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value;
      &#125;
      <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
          <span class="hljs-keyword">if</span> (hasChanged(toRaw(newVal), <span class="hljs-built_in">this</span>._rawValue)) &#123;
              <span class="hljs-built_in">this</span>._rawValue = newVal;
              <span class="hljs-built_in">this</span>._value = <span class="hljs-built_in">this</span>._shallow ? newVal : convert(newVal);
              trigger(toRaw(<span class="hljs-built_in">this</span>), <span class="hljs-string">"set"</span> <span class="hljs-comment">/* SET */</span>, <span class="hljs-string">'value'</span>, newVal);
          &#125;
      &#125;
  &#125;
  <span class="hljs-keyword">const</span> convert = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> isObject(val) ? reactive(val) : val;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ref</li>
</ul>
<p>这是我们使用的函数，里面使用 createRef 来创建一个实例。</p>
<ul>
<li>createRef</li>
</ul>
<p>做一些基础判断，然后进入主题，正式创建ref。这里还可以创建 shallowRef。</p>
<ul>
<li>RefImpl</li>
</ul>
<p>这个才是主体，显然这是 ES6 的 class，constructor 是初始化函数，依据参数创建一个实例，并且设置实例的属性。这个和上面 ref 的打印结果也是可以对应上的。
整个class的代码也是非常简单，设置几个“内部”属性，记录需要的数据，然后设置“外部”属性 value，通过setter、getter 实现对 value 的操作拦截，set 里面主要是 trigger 这个函数，由它调用模板的自动刷新的功能。</p>
<ul>
<li>convert</li>
</ul>
<p>很显然，判断一下参数是不是 object，如果是的话，变成 reactive 的形式。
这个就可以解释，引用类型的 ref 是如何实现响应性的，明显是先变成 reactive，然后在挂到 value 上面（挂之前判断一下是不是浅层的）。</p>
<h1 data-id="heading-2">ref 和 reactive 的关系</h1>
<p>通过打印结果的对比以及分析源码可以发现：</p>
<ul>
<li>基础类型的 ref 和 reactive 没有任何关系。</li>
<li>引用类型的 ref ，先把 object 变成 reactive ，即利用 reactive 来实现引用类型的响应性。</li>
</ul>
<p>关系就是这样的，千万不要再混淆了。</p>
<h1 data-id="heading-3">shallowRef</h1>
<p>浅层响应式，只监听 .value 的变化，真简单类型的响应式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowRef</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">return</span> createRef(value, <span class="hljs-literal">true</span>); <span class="hljs-comment">// true 浅层</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过源码我们可以发现，在把引用类型挂到 value 之前，先判断一下是不是浅层的，如果是浅层的，并不会变成 reactive，而是直接把原来的对象挂在 value 上面，shallowRef 和 ref 的区别就在于这一点。</p>
<p>我们写几个实例看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js">  setup () &#123;
     <span class="hljs-comment">// 浅层的测试 </span>
    <span class="hljs-comment">// 基础类型</span>
    <span class="hljs-keyword">const</span> srefCount = shallowRef(<span class="hljs-number">0</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'refCount '</span>, srefCount )

    <span class="hljs-comment">// 引用类型</span>
    <span class="hljs-keyword">const</span> srefObject = shallowRef(&#123; <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'refObject '</span>, srefObject )

    <span class="hljs-comment">// 嵌套对象</span>
    <span class="hljs-keyword">const</span> srefObjectMore = shallowRef(&#123; <span class="hljs-attr">info</span>: &#123;<span class="hljs-attr">a</span>: <span class="hljs-string">'jyk'</span>&#125; &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shallowRef '</span>, srefObjectMore )

    <span class="hljs-comment">// reactive 的 shallowRef</span>
    <span class="hljs-keyword">const</span> ret = reactive(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'jyk'</span>&#125;)
    <span class="hljs-keyword">const</span> shallowRefRet = shallowRef(ret)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shallowRefRet '</span>, shallowRefRet )

    <span class="hljs-comment">// ==================== 事件 ==================</span>
    <span class="hljs-comment">// 修改基础类型</span>
    <span class="hljs-keyword">const</span> setNumber = <span class="hljs-function">() =></span> &#123;
      srefCount.value = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'srefCount '</span>, srefCount )
    &#125;

    <span class="hljs-comment">// 修改引用类型的属性</span>
    <span class="hljs-keyword">const</span> setObjectProp = <span class="hljs-function">() =></span> &#123;
      srefObject.value.value = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'srefObject '</span>, srefObject )
    &#125;
 
    <span class="hljs-comment">// 修改引用类型的value</span>
    <span class="hljs-keyword">const</span> setObject = <span class="hljs-function">() =></span> &#123;
      srefObject.value = &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf() &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'srefObject '</span>, srefObject )
    &#125;

    <span class="hljs-comment">// 修改嵌套引用类型的属性</span>
    <span class="hljs-keyword">const</span> setObjectMoreProp = <span class="hljs-function">() =></span> &#123;
      srefObjectMore.value.info.a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'srefObjectMore '</span>, srefObjectMore )
    &#125;
    
    <span class="hljs-comment">// 修改嵌套引用类型的value</span>
    <span class="hljs-keyword">const</span> setObjectMore = <span class="hljs-function">() =></span> &#123;
      srefObjectMore.value = &#123; <span class="hljs-attr">qiantao</span>: <span class="hljs-number">1234567</span> &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'srefObjectMore '</span>, srefObjectMore )
    &#125;

    <span class="hljs-comment">// 修改reactive 的浅层ref</span>
    <span class="hljs-keyword">const</span> setObjectreactive = <span class="hljs-function">() =></span> &#123;
      shallowRefRet.value.name = <span class="hljs-string">'浅层的reactive'</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shallowRefRet '</span>, shallowRefRet )
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看结果：</p>
<p><img alt="浅层的ref" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a424a2a34eb455baa745d718221fd63~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>测试了一下响应性：</p>
<ul>
<li>基础类型 srefCount 有响应性；</li>
<li>引用类型 srefObject 的属性没有响应性，但是直接修改 .value 是有响应性的。</li>
<li>嵌套的引用类型 srefObjectMore ，属性和嵌套属性都是没有响应性的，但是直接修改 .value 是有响应性的。</li>
<li>reactive 套上 shallowRef ，然后修改 shallowRef.value.属性 = xxx ，也是可以响应的，所以浅层的ref 也不绝对，还要看内部结构。</li>
</ul>
<h1 data-id="heading-4">triggerRef</h1>
<blockquote>
<p>手动执行与 shallowRef 关联的任何效果。</p>
</blockquote>
<p>官网的中文版里面写的很绕，其实就是 让 shallowRef 原本不具有响应性的部分，具有响应性。
shallowRef 是浅层的，深层部分是没有响应性的，那么如果非得让这部分也具有响应性呢？
这时候可以用 triggerRef 来实现。
好吧，目前还没有想到有啥具体的应用场景，因为一般都直接简单粗暴的用 ref 或者 reactive 了，全都自带响应性。</p>
<p>测试了各种情况，发现 triggerRef 并不支持 shallowReactive，还以为能支持呢。（或许是我写的测试代码有问题吧，官网也没提 shallowReactive）</p>
<p>基于上面的例子，在适当的位置加上  triggerRef(xxx)就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js">  setup () &#123;
    <span class="hljs-comment">// 引用类型</span>
    <span class="hljs-keyword">const</span> srefObject = shallowRef(&#123; <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;)
    <span class="hljs-comment">// 嵌套对象</span>
    <span class="hljs-keyword">const</span> srefObjectMore = shallowRef(&#123; <span class="hljs-attr">value</span>: &#123;<span class="hljs-attr">a</span>: <span class="hljs-string">'jyk'</span>&#125; &#125;)
    <span class="hljs-comment">// reactive 的 shallowRef</span>
    <span class="hljs-keyword">const</span> ret = reactive(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'reactive'</span>&#125;)
    <span class="hljs-keyword">const</span> shallowRefRet = shallowRef(ret)
 
    <span class="hljs-comment">// 浅层的reactive</span>
    <span class="hljs-keyword">const</span> myShallowReactive = shallowReactive(&#123;<span class="hljs-attr">info</span>:&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'myShallowReactive'</span>&#125;&#125;)
    <span class="hljs-keyword">const</span> setsRet = <span class="hljs-function">() =></span> &#123;
      myShallowReactive.info.name = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      triggerRef(myShallowReactive)  <span class="hljs-comment">// 修改后使用，不支持</span>
   &#125;

    <span class="hljs-comment">// ==================== 事件 ==================</span>

    <span class="hljs-comment">// 修改引用类型的属性</span>
    <span class="hljs-keyword">const</span> setObjectProp = <span class="hljs-function">() =></span> &#123;
      srefObject.value.value = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      triggerRef(srefObject) <span class="hljs-comment">// 修改后使用</span>
    &#125;
 
    <span class="hljs-comment">// 修改引用类型的value</span>
    <span class="hljs-keyword">const</span> setObject = <span class="hljs-function">() =></span> &#123;
      srefObject.value = &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf() &#125;
      triggerRef(srefObject)
   &#125;

    <span class="hljs-comment">// 修改嵌套引用类型的属性</span>
    <span class="hljs-keyword">const</span> setObjectMoreProp = <span class="hljs-function">() =></span> &#123;
      srefObjectMore.value.value.a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      triggerRef(srefObjectMore)
  &#125;
    
    <span class="hljs-comment">// 修改嵌套引用类型的value</span>
    <span class="hljs-keyword">const</span> setObjectMore = <span class="hljs-function">() =></span> &#123;
      srefObjectMore.value.value = &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf() &#125;
      triggerRef(srefObjectMore)
    &#125;

    <span class="hljs-comment">// 修改reactive 的浅层ref</span>
    <span class="hljs-keyword">const</span> setObjectreactive = <span class="hljs-function">() =></span> &#123;
      shallowRefRet.value.name = <span class="hljs-string">'浅层的reactive'</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
      triggerRef(shallowRefRet)
    &#125;

    <span class="hljs-keyword">return</span> &#123;
      srefObject, <span class="hljs-comment">// 引用类型</span>
      srefObjectMore, <span class="hljs-comment">// 嵌套引用类型</span>
      shallowRefRet, <span class="hljs-comment">// reactive 的浅层ref</span>
      myShallowReactive, <span class="hljs-comment">// 浅层的reactive</span>
      setsRet, <span class="hljs-comment">// 修改浅层的reactive</span>
      setObjectProp, <span class="hljs-comment">// 修改引用类型的属性</span>
      setObject, <span class="hljs-comment">// 修改引用类型的value</span>
      setObjectMoreProp, <span class="hljs-comment">// 修改嵌套引用类型的属性</span>
      setObjectMore, <span class="hljs-comment">// 修改嵌套引用类型的value</span>
      setObjectreactive <span class="hljs-comment">// 试一试reactive的浅层ref</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>深层部分，不使用  triggerRef 就不会刷新模板，使用了  triggerRef 就可以刷新模板。
话说，为啥会有这个函数？</p>
<h1 data-id="heading-5">isRef</h1>
<p>通过 __v_isRef 属性 判断是否是 ref 的实例。这个没啥好说的。
vue.global.js 源码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isRef</span>(<span class="hljs-params">r</span>) </span>&#123;
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">Boolean</span>(r && r.__v_isRef === <span class="hljs-literal">true</span>);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">unref</h1>
<ul>
<li>使用.value的语法糖</li>
</ul>
<p>unref 是一个语法糖，判断是不是 ref 的，如果是则取.value，不是的话取原型。
vue.global.js 源码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unref</span>(<span class="hljs-params">ref</span>) </span>&#123;
      <span class="hljs-keyword">return</span> isRef(ref) ? ref.value : ref;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>unref 的用途</li>
</ul>
<p>普通对象直接<code>.属性</code>即可使用，但是 ref 却需要.value才可以，混合使用的时候容易晕头，尤其在函数内部接收参数的时候，无法确定传入的是 reactive 还是 ref，如果每次都用 isReactive 或者 isRef 来判断类型，然后决定是否用.value，那就太麻烦了。于是有了这个语法糖。</p>
<h1 data-id="heading-7">toRef 和 toRefs</h1>
<blockquote>
<p>toRef 可以用来为源响应式对象上的 property 性创建一个 <a href="https://www.vue3js.cn/docs/zh/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer"><code>ref</code></a>。然后可以将 ref 传递出去，从而保持对其源 property 的响应式连接。</p>
</blockquote>
<p>toRefs 将响应式对象转换为普通对象，其中结果对象的每个 property 都是指向原始对象相应 property 的<a href="https://www.vue3js.cn/docs/zh/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer"><code>ref</code></a>。</p>
<p>话说，官网的解释为啥总是这么令人费解呢？
我们还是先看看例子</p>
<pre><code class="hljs language-js copyable" lang="js"> setup () &#123;
    <span class="hljs-comment">/**
     * 定义 reactive
     * 直接解构属性，看响应性
     * 使用toRef解构，看响应性
     * 使用toRefs解构，看响应性
     * 按钮只修改reactive
     */</span>
    <span class="hljs-keyword">const</span> person = reactive(&#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'jyk'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
    &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'person '</span>, person )

    <span class="hljs-comment">// 直接获取属性</span>
    <span class="hljs-keyword">const</span> name = person.name
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name '</span>, name )
    
    <span class="hljs-keyword">const</span> refName = toRef(person, <span class="hljs-string">'name'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'refName '</span>, refName )

    <span class="hljs-keyword">const</span> personToRefs = toRefs(person)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'personToRefs '</span>, personToRefs )

    <span class="hljs-keyword">const</span> update = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 修改原型</span>
      person.name = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
    &#125;

    <span class="hljs-keyword">return</span> &#123;
      person, <span class="hljs-comment">// reactive</span>
      name, <span class="hljs-comment">// 获取属性</span>
      refName, <span class="hljs-comment">// 使用toRef</span>
      personToRefs,
      update <span class="hljs-comment">// 修改属性</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们修改person的属性值的时候，toRef 和 toRefs 的实例也会自动变化。而直接获取的name属性并不会变化。</p>
<p>toRef 就是想实现直接使用对象的属性名，并且仍然享有响应性的目的。
toRef 就是对reactive 进行解构，然后仍然享有响应性的目的。</p>
<p>其实，说是变成了ref，但是我们看看打印结果就会发现，其实并不完全是ref。</p>
<p><img alt="toRef" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/763b4d51c0e04606b7832bede90c8954~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="toRefs" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a0dc061a8c24d43a32e764d746fccf5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看类名和属性，toRef 和 ref 也是有区别的。</p>
<h1 data-id="heading-8">toRef 为啥可以响应</h1>
<p>toRef 也是一个语法糖。</p>
<p>如果使用常规的方式对 reactive 进行解构的话就会发现，虽然解构成功了，但是也失去响应性（仅限于基础类型的属性，嵌套对象除外）。</p>
<p>那么如何实现解构后还具有响应性呢？这时候就需要使用 toRef 了。</p>
<p>看上面那个例子，使用 refName 的时候，相当于使用 person['name']，这样就具有响应性了。</p>
<p>你可能会问，就这？对就是这么简单，不信的话，我们来看看源码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRef</span>(<span class="hljs-params">object, key</span>) </span>&#123;
      <span class="hljs-keyword">return</span> isRef(object[key])
          ? object[key]
          : <span class="hljs-keyword">new</span> ObjectRefImpl(object, key);
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObjectRefImpl</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">_object, _key</span>)</span> &#123;
          <span class="hljs-built_in">this</span>._object = _object;
          <span class="hljs-built_in">this</span>._key = _key;
          <span class="hljs-built_in">this</span>.__v_isRef = <span class="hljs-literal">true</span>;
      &#125;
      <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._object[<span class="hljs-built_in">this</span>._key];  <span class="hljs-comment">// 相当于 person['name']</span>
      &#125;
      <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
          <span class="hljs-built_in">this</span>._object[<span class="hljs-built_in">this</span>._key] = newVal;
      &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看 get 部分，是不是 相当于  person['name'] ？</p>
<p>另外，虽然 toRef 看起来好像是变成了 ref，但是其实只是变成了 ref （RefImpl）的双胞胎兄弟（ObjectRefImpl），并没有变成 ref（RefImpl）。
ref 是  RefImpl， 而 toRef 是 ObjectRefImpl，这是两个不同的class 。
toRef 可以看做是 ref 同系列的 class，后面还有一个同系列的。</p>
<h1 data-id="heading-9">toRefs</h1>
<p>了解 toRef 之后，toRefs 就好理解了，从表面上看，可以把 reactive 的所有属性都解构出来，从内部代码来看，就是把多个 toRef 放在了数组（或者对象）里面。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRefs</span>(<span class="hljs-params">object</span>) </span>&#123;
      <span class="hljs-keyword">if</span> ( !isProxy(object)) &#123;
          <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`toRefs() expects a reactive object but received a plain one.`</span>);
      &#125;
      <span class="hljs-keyword">const</span> ret = isArray(object) ? <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(object.length) : &#123;&#125;;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> object) &#123;
          ret[key] = toRef(object, key);
      &#125;
      <span class="hljs-keyword">return</span> ret;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">customRef</h1>
<blockquote>
<p>自定义一个ref，并对其依赖项跟踪和更新触发进行显式控制。它需要一个工厂函数，该函数接收 track 和 trigger 函数作为参数，并应返回一个带有 get 和 set 的对象。</p>
</blockquote>
<p>如果上面那段没看懂的话，可以跳过。</p>
<p>简单的说，就是在 ref 原有的 set、get 的基础上，加入我们自己写的代码，以达到一定的目的。</p>
<p>话说，官网写的例子还真是……
反正一开始我是没看懂，后来又反复看，又把代码敲出来运行，又查了一下“debounce”的意思。
最后终于明白了，这是一个防抖（延迟响应）的代码。</p>
<p>一般用户在文本框里输入内容，立即就会响应，但是如果在查询功能里面的话就会有点小郁闷。
用户输入个“1”，立即就去后端查询“1”，
然后用户又输入个“2”，立即又去后端查询“12”，
然后用户又输入个“3”，立即又去后端查询“123”。
……
这个响应是很快，但是有点“折腾”的嫌疑，那么能不能等用户把“123”都输入好了，再去后端查询呢？</p>
<p>官网的例子就是实现这样的功能的，我们把例子完善一下，就很明显了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> useDebouncedRef = <span class="hljs-function">(<span class="hljs-params">value, delay = <span class="hljs-number">200</span></span>) =></span> &#123;
  <span class="hljs-keyword">let</span> timeout
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        track() <span class="hljs-comment">// vue内部的跟踪函数</span>
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-built_in">clearTimeout</span>(timeout)
        timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          value = newValue
          trigger() <span class="hljs-comment">// vue内部的自动更新的函数。</span>
        &#125;, delay) <span class="hljs-comment">// 延迟时间</span>
      &#125;
    &#125;
  &#125;)
&#125;

  setup () &#123;
    <span class="hljs-keyword">const</span> text = useDebouncedRef(<span class="hljs-string">'hello'</span>, <span class="hljs-number">1000</span>) <span class="hljs-comment">// 定义一个 v-model</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'customRef'</span>, text)

    <span class="hljs-keyword">const</span> update = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 修改后延迟刷新</span>
      text.value = <span class="hljs-string">'1111'</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().valueOf()
    &#125;

    <span class="hljs-keyword">return</span> &#123;
      text,
      update
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">  customRef 对象：&#123;&#123;text&#125;&#125; <span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>get</li>
</ul>
<p>没有改变，直接用原方法。</p>
<ul>
<li>set</li>
</ul>
<p>使用 setTimeout 实现延迟响应的功能，把 Vue 内部的 trigger() 放在  setTimeout 里面就好。</p>
<p>这样就可以了，延迟多长的时间可以自定义，这里是一秒。一秒内用户输入的内容，会一次性更新，而不是每输入一个字符就更新一次。</p>
<ul>
<li>v-model="text"</li>
</ul>
<p>可以作为 v-model 来使用。</p>
<h1 data-id="heading-11">customRef 的 源码</h1>
<p>我们再来看看 customRef 内部源码的实现方式。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">customRef</span>(<span class="hljs-params">factory</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> CustomRefImpl(factory);
  &#125;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomRefImpl</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">factory</span>)</span> &#123;
          <span class="hljs-built_in">this</span>.__v_isRef = <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">const</span> &#123; get, set &#125; = factory(<span class="hljs-function">() =></span> track(<span class="hljs-built_in">this</span>, <span class="hljs-string">"get"</span> <span class="hljs-comment">/* GET */</span>, <span class="hljs-string">'value'</span>), <span class="hljs-function">() =></span> trigger(<span class="hljs-built_in">this</span>, <span class="hljs-string">"set"</span> <span class="hljs-comment">/* SET */</span>, <span class="hljs-string">'value'</span>));
          <span class="hljs-built_in">this</span>._get = get;
          <span class="hljs-built_in">this</span>._set = set;
      &#125;
      <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._get();
      &#125;
      <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
          <span class="hljs-built_in">this</span>._set(newVal);
      &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很简单的是不是，就是先这样，然后在那样，最后就搞定了。
好吧，就是把 factory参数解构出来，分成set和get，做成内部函数，然后在内部的set和get里面调用。</p>
<h1 data-id="heading-12">自定义 ref 的实例 —— 写一个自己的计算属性。</h1>
<p>一提到计算属性，我们会想到 Vue 提供的  computed，那么如果让我们使用自定义ref 来实现计算属性的功能的话，要如何实现呢？（注意：只是练习用）</p>
<p>我们可以这样来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myComputed = <span class="hljs-function">(<span class="hljs-params">_get, _set</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        track()
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _get === <span class="hljs-string">'function'</span>) &#123;
          <span class="hljs-keyword">return</span> _get()
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`没有设置 get 方法`</span>)
        &#125;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _set === <span class="hljs-string">'function'</span>) &#123;
          _set(newValue)
          trigger()
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`没有设置 set 方法`</span>)
        &#125;
      &#125;
    &#125;
  &#125;)
&#125;

setup () &#123;
    <span class="hljs-keyword">const</span> refCount = ref(<span class="hljs-number">0</span>)

    <span class="hljs-keyword">const</span> myCom = myComputed(<span class="hljs-function">() =></span> refCount.value + <span class="hljs-number">1</span>)
    <span class="hljs-comment">// const myCom = myComputed(() => refCount.value, (val) => &#123; refCount.value = val&#125;)</span>

    <span class="hljs-keyword">const</span> update = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 修改原型</span>
      refCount.value = <span class="hljs-number">3</span>
    &#125;


    <span class="hljs-keyword">const</span> setRef = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 直接赋值</span>
      refCount.value += <span class="hljs-number">1</span>
    &#125;

    <span class="hljs-keyword">return</span> &#123;
      refCount, <span class="hljs-comment">// 基础类型</span>
      myCom, <span class="hljs-comment">// 引用类型</span>
      update, <span class="hljs-comment">// 修改属性</span>
      setRef <span class="hljs-comment">// 直接设置</span>
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      展示 自定义 的 customRef 实现计算属性 <span class="hljs-tag"><<span class="hljs-name">br</span>></span>
      ref 对象：&#123;&#123;refCount&#125;&#125; <span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
      自定义的计算属性 对象：&#123;&#123;myCom&#125;&#125; <span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myCom"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"update"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>修改属性<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>myComputed</li>
</ul>
<p>首先定义一个函数，接收两个参数，一个get，一个set。</p>
<ul>
<li>customRef</li>
</ul>
<p>返回一个 customRef 的实例，内部设置get 和 set。</p>
<ul>
<li>调用方法</li>
</ul>
<p>调用的时候，可以只传入get函数，也可以传入get、set两个函数。
修改 refCount.value 的时候，v-model 的 myCom 也会发生变化。</p>
<ul>
<li>实用性</li>
</ul>
<p>那么这种方式有啥使用效果呢？
在做组件的时候，组件的属性props是不能直接用在内部组件的 v-model 里面的，因为props只读，那么怎么办呢？</p>
<p>可以在组件内部设置一个ref，然后对props做监听，或者用computed来做。
除了上面的几种方法外，也可以用这里的方法来实现，把 refCount 变成 props 的属性就可以了，然后set里面使用 smit 提交。</p>
<h1 data-id="heading-13">computed</h1>
<p>写完了自己的计算属性后，我们还是来看看 Vue 提供的计算属性。
代码来自于 vue.global.js ，调整了一下先后顺序。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span>(<span class="hljs-params">getterOrOptions</span>) </span>&#123;
      <span class="hljs-keyword">let</span> getter;
      <span class="hljs-keyword">let</span> setter;
      <span class="hljs-keyword">if</span> (isFunction(getterOrOptions)) &#123;
          getter = getterOrOptions;
          setter =  <span class="hljs-function">() =></span> &#123;
                  <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'Write operation failed: computed value is readonly'</span>);
              &#125;
              ;
      &#125;
      <span class="hljs-keyword">else</span> &#123;
          getter = getterOrOptions.get;
          setter = getterOrOptions.set;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ComputedRefImpl(getter, setter, isFunction(getterOrOptions) || !getterOrOptions.set);
  &#125;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ComputedRefImpl</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">getter, _setter, isReadonly</span>)</span> &#123;
          <span class="hljs-built_in">this</span>._setter = _setter;
          <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">true</span>;
          <span class="hljs-built_in">this</span>.__v_isRef = <span class="hljs-literal">true</span>;
          <span class="hljs-built_in">this</span>.effect = effect(getter, &#123;
              <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">scheduler</span>: <span class="hljs-function">() =></span> &#123;
                  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>._dirty) &#123;
                      <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">true</span>;
                      trigger(toRaw(<span class="hljs-built_in">this</span>), <span class="hljs-string">"set"</span> <span class="hljs-comment">/* SET */</span>, <span class="hljs-string">'value'</span>);
                  &#125;
              &#125;
          &#125;);
          <span class="hljs-built_in">this</span>[<span class="hljs-string">"__v_isReadonly"</span> <span class="hljs-comment">/* IS_READONLY */</span>] = isReadonly;
      &#125;
      <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._dirty) &#123;
              <span class="hljs-built_in">this</span>._value = <span class="hljs-built_in">this</span>.effect();
              <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">false</span>;
          &#125;
          track(toRaw(<span class="hljs-built_in">this</span>), <span class="hljs-string">"get"</span> <span class="hljs-comment">/* GET */</span>, <span class="hljs-string">'value'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value;
      &#125;
      <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newValue</span>) &#123;
          <span class="hljs-built_in">this</span>._setter(newValue);
      &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>computed</li>
</ul>
<p>暴露给我们用的方法，来定义一个计算属性。只有一个参数，可以是一个函数（function），也可以是一个对象。内部会做一个判断，然后做拆分。</p>
<ul>
<li>ComputedRefImpl</li>
</ul>
<p>是不是有点眼熟？这个是 ref 同款系列，都是 RefImpl 风格的，而且内部代码结构也很相似。
这个是computed 的主体类，也是先定义内部属性，然后设置value的get和set。在get和set里面，调用外部设置的函数。</p>
<h1 data-id="heading-14">源码：</h1>
<p><a href="https://gitee.com/naturefw/nf-vue-cdn/tree/master/cdn/project-compositionapi" target="_blank" rel="nofollow noopener noreferrer">gitee.com/naturefw/nf…</a></p>
<h1 data-id="heading-15">在线演示：</h1>
<p><a href="https://naturefw.gitee.io/nf-vue-cdn/cdn/project-compositionapi/" target="_blank" rel="nofollow noopener noreferrer">naturefw.gitee.io/nf-vue-cdn/…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            