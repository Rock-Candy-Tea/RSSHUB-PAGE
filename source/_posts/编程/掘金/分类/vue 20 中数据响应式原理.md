
---
title: 'vue 2.0 中数据响应式原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20001fadb0144288b401b83cb4a0d044~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 16:14:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20001fadb0144288b401b83cb4a0d044~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">首先将数据响应的关系图通过图形的形式画出来</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20001fadb0144288b401b83cb4a0d044~tplv-k3u1fbpfcp-watermark.image" alt="数据响应流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">通过流程图可以看到 大致分为几个不同的方法和类</h3>
<ol>
<li>能够对数据进行观察的 observe 和 observer类 对数组的处理</li>
<li>对数据进行观察的 defineReactive</li>
<li>手机依赖的 Dep</li>
<li>对依赖添加处理的 Watch</li>
</ol>
<h3 data-id="heading-2">几个文件的关系图</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0f2eda8f4024d96a171a20ce8b4f903~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210810072419.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>index.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> defineReactive <span class="hljs-keyword">from</span> <span class="hljs-string">'./data/defineReactive.js'</span>
<span class="hljs-keyword">import</span> &#123;observe&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./data/observer'</span>
<span class="hljs-keyword">import</span> Watcher <span class="hljs-keyword">from</span> <span class="hljs-string">'./data/watcher.js'</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-string">'a'</span>: &#123;
    <span class="hljs-string">"b"</span>:&#123;
      <span class="hljs-string">'n'</span>: <span class="hljs-number">5</span>
    &#125;
  &#125;,
  <span class="hljs-string">'b'</span>: <span class="hljs-number">6</span>,
  <span class="hljs-string">'g'</span>:[<span class="hljs-string">'90'</span>,<span class="hljs-string">'76'</span>,<span class="hljs-string">'766'</span>,<span class="hljs-string">'56'</span>]
&#125;
observe(obj)
<span class="hljs-keyword">new</span> Watcher (obj, <span class="hljs-string">'a.b.n'</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'********'</span>,val)
&#125;)
obj.a.b.n = <span class="hljs-number">890</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>observer.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;def&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.js'</span>
<span class="hljs-keyword">import</span> defineReactive <span class="hljs-keyword">from</span> <span class="hljs-string">'./defineReactive.js'</span>
<span class="hljs-keyword">import</span> &#123;arrayMethods&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./array.js'</span>
<span class="hljs-keyword">import</span> Dep <span class="hljs-keyword">from</span> <span class="hljs-string">'./dep.js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">value</span>) &#123;
    <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
    <span class="hljs-comment">// 一个不可枚举属性   this 在类中不是指的类本身 ， 指的是实例</span>
    <span class="hljs-comment">// 通过def 函数给 value 添加__ob__属性，并且指向 实例本身</span>
    def(value, <span class="hljs-string">'__ob__'</span>, <span class="hljs-built_in">this</span>, <span class="hljs-literal">false</span>)
    <span class="hljs-comment">// Observer 的终极目标是将 obj 中每个层级的属性转化为响应式的</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
      <span class="hljs-comment">// 如果是数组，强行将原型指向 新的地址</span>
      <span class="hljs-built_in">Object</span>.setPrototypeOf(value, arrayMethods)
      <span class="hljs-comment">// 让这个数组变的 observe</span>
      <span class="hljs-built_in">this</span>.observeArray(value)
    &#125;<span class="hljs-keyword">else</span>&#123;
      <span class="hljs-built_in">this</span>.walk(value)
    &#125;
  &#125;
  walk (value) &#123;
    <span class="hljs-comment">// 遍历每个 KEY 值去将每个层级的属性变为响应式</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> value) &#123;
      defineReactive(value,key)
    &#125;
  &#125;
  observeArray (arr) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>, l= arr.length; i<l; i++) &#123;
      observe(arr[i])
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span> (<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是对象，如果不是对象直接返回</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">var</span> ob;
  <span class="hljs-comment">// 判断该对象上是不是绑定了__ob__ 如果绑定了 直接使用</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value.__ob__!==<span class="hljs-string">'undefined'</span>) &#123;
    ob = value.__ob__
  &#125;<span class="hljs-keyword">else</span> &#123;
    ob = <span class="hljs-keyword">new</span> Observer(value)
  &#125;
  <span class="hljs-keyword">return</span> ob
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>utils.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// def 函数利用defineProperty 给对象添加属性和属性值</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">def</span> (<span class="hljs-params">obj, key, val, enumerable</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">value</span> : val,
    enumerable, <span class="hljs-comment">// 是不是课枚举的</span>
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是不是可写的</span>
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 是不是课设置的</span>
  &#125;)
&#125;

<span class="hljs-comment">// 返回一个高阶函数， 在watcher 中使用，是获取对象的值使用的</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parsePath</span> (<span class="hljs-params">str</span>) </span>&#123;
  <span class="hljs-keyword">let</span> segments = str.split(<span class="hljs-string">'.'</span>)
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i =<span class="hljs-number">0</span>; i< segments.length; i++) &#123;
      <span class="hljs-keyword">if</span> (!obj) <span class="hljs-keyword">return</span>;
      obj = obj[segments[i]]
    &#125;
    <span class="hljs-keyword">return</span> obj
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>array.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这里是对数组中的一些函数，利用装饰者模式来添加一些新的功能--触发 数据更新</span>

<span class="hljs-keyword">import</span> &#123;def&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.js'</span>
<span class="hljs-comment">// 找到Array 的原型对象</span>
<span class="hljs-keyword">const</span> arrayPrototype = <span class="hljs-built_in">Array</span>.prototype
<span class="hljs-comment">// 以array.prototype 为原型创建一个 arrayMethods， 这样arrayMethods 上就有了 Array 上的方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(arrayPrototype)
<span class="hljs-keyword">let</span> methodNeedChange = [
  <span class="hljs-string">'push'</span>,<span class="hljs-string">'pop'</span>,<span class="hljs-string">'shift'</span>,<span class="hljs-string">'unshift'</span>,<span class="hljs-string">'splice'</span>,<span class="hljs-string">'sort'</span>,<span class="hljs-string">'reverse'</span>
]

methodNeedChange.forEach(<span class="hljs-function">(<span class="hljs-params">methodName</span>) =></span> &#123;
  <span class="hljs-comment">// 备份原来的方法</span>
  <span class="hljs-keyword">const</span> original = arrayMethods[methodName]
  <span class="hljs-comment">// 对需要改变的函数重新定义</span>
  def(arrayMethods,methodName,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-comment">// 首先执行老方法，利用 apply, 来执行， </span>
    <span class="hljs-keyword">const</span> result = original.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
    <span class="hljs-comment">// 在每个值的本生绑定了__ob__属性， 绑定的实例本生</span>
    <span class="hljs-keyword">let</span> ob = <span class="hljs-built_in">this</span>.__ob__;
    <span class="hljs-keyword">let</span> args = [...arguments] <span class="hljs-comment">// 将类数组变为数组</span>
    <span class="hljs-comment">// 有三种方法 会往数组中添加内容， 需要将添加的内容页变为 observe</span>
    <span class="hljs-comment">// push unshift splice</span>

    <span class="hljs-keyword">let</span> inserted = []
    <span class="hljs-keyword">switch</span> (methodName) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:
      <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>:
        inserted = args;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>:
      <span class="hljs-comment">// splice(开始的下标，数量，要添加的值)</span>
        inserted = args.slice(<span class="hljs-number">2</span>);
        <span class="hljs-keyword">break</span>;
    &#125;

    <span class="hljs-keyword">if</span> (inserted) &#123;
      <span class="hljs-comment">// 让新项也变为 observe</span>
      ob.observeArray(inserted)
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'啦啦啦'</span>)
    ob.dep.notify()
   
    <span class="hljs-keyword">return</span> result
  &#125;,<span class="hljs-literal">false</span>)
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>defineReactive.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> &#123;observe&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./observer'</span>
<span class="hljs-keyword">import</span> Dep <span class="hljs-keyword">from</span> <span class="hljs-string">'./dep.js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span> (<span class="hljs-params">data,key,val</span>) </span>&#123;
  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">2</span>) &#123;
    val = data[key]
  &#125;
  <span class="hljs-keyword">let</span> childOb = observe(val)
  <span class="hljs-built_in">Object</span>.defineProperty(data,key,&#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">//  可被枚举</span>
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 可以被设置，比如删除</span>
    get () &#123;
      <span class="hljs-comment">// 如果处于一个依赖收集阶段</span>
      <span class="hljs-keyword">if</span> (Dep.target) &#123;
        dep.depend()
        <span class="hljs-keyword">if</span> (childOb) &#123;
          childOb.dep.depend()
        &#125;
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'你试图访问obj 的'</span>+key+<span class="hljs-string">'属性'</span> + val)
      <span class="hljs-keyword">return</span> val
    &#125;,
    set (newVal) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'你获取了'</span>+key+<span class="hljs-string">'值'</span> + newVal)
      <span class="hljs-keyword">if</span> (val===newVal) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      val = newVal
      <span class="hljs-comment">// 当设置了新值， 需要继续添加观察</span>
      childOb = observe(val)
      dep.notify()
    &#125;
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>dep.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> uid =<span class="hljs-number">0</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是DEP 类的构造器'</span>)
    <span class="hljs-built_in">this</span>.id = uid++
    <span class="hljs-comment">// 发布订阅者模式 创建一个 订阅者数组  放的是 watcher 实例</span>
    <span class="hljs-built_in">this</span>.subs = []
  &#125;
  addSub (sub) &#123;
    <span class="hljs-built_in">this</span>.subs.push(sub)
  &#125;
  <span class="hljs-comment">// 添加依赖</span>
  depend () &#123;
    <span class="hljs-comment">// Dep.target是指定的一个全局位置</span>
    <span class="hljs-keyword">if</span> (Dep.target) &#123;
      <span class="hljs-built_in">this</span>.addSub(Dep.target)
    &#125;
  &#125;
  notify () &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 notify'</span>)
    <span class="hljs-comment">// 浅克隆一份</span>
    <span class="hljs-keyword">let</span> subs = <span class="hljs-built_in">this</span>.subs.slice()
    <span class="hljs-comment">// 遍历</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>,l=subs.length; i< l; i++) &#123;
      subs[i].update()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>watcher.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Dep <span class="hljs-keyword">from</span> <span class="hljs-string">'./dep.js'</span>;
<span class="hljs-keyword">import</span> &#123;parsePath&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.js'</span>
<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span></span>&#123; 
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">target, expression, callBack</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.id = uid++
    <span class="hljs-built_in">this</span>.target = target;
    <span class="hljs-comment">// parsePath 就是解析表达式的 一个高阶函数</span>
    <span class="hljs-built_in">this</span>.getter = parsePath(expression)
    <span class="hljs-built_in">this</span>.callBack = callBack;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是watcher的构造器'</span>)
  &#125;
  update () &#123;
    <span class="hljs-built_in">this</span>.run()
  &#125;
  get () &#123;
    <span class="hljs-comment">// 进入依赖收集阶段 让全局的Dep.target 设置为 watcher 本身</span>
    Dep.target = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">this</span>.target;
    <span class="hljs-comment">// 只要能找 就一直找</span>
    <span class="hljs-keyword">var</span> value
    <span class="hljs-keyword">try</span> &#123;
      value = <span class="hljs-built_in">this</span>.getter(obj)
    &#125; <span class="hljs-keyword">finally</span> &#123;
      Dep.target = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">return</span> value
  &#125;
  <span class="hljs-comment">// 得到 并且唤起</span>
  run () &#123;
    <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-built_in">this</span>.callBack)
  &#125;
  getAndInvoke (cb) &#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.get();
    <span class="hljs-keyword">if</span> (value !== <span class="hljs-built_in">this</span>.value || <span class="hljs-keyword">typeof</span> value == <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-keyword">const</span> oldVal = <span class="hljs-built_in">this</span>.value
      <span class="hljs-built_in">this</span>.value = value
      <span class="hljs-comment">// 这里就是 watcher 中的 参数， 新值 和旧值</span>
      cb.call(<span class="hljs-built_in">this</span>.target,value,oldVal)
    &#125;
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后总结下：</p>
<ol>
<li>在 observe 中通过遍历的方式，<strong>给对象和数组添加 添加一个__ob__ 属性</strong>，属性值是Observer实例本身。每个实例上也绑定一个 dep</li>
<li>通过对象遍历的方式，给每个值都变为响应式的</li>
<li>在defineReactive 中给对象和对象的属性添加为响应式， <strong>对值再调用 observe 是每个层都变为响应式</strong></li>
<li>调用 new Watcher 的时候 ， 首先会调用 <strong>watcher中的get 方法</strong>，将对象本身设置为Dep.target 的静态属性值,然后获取当前的对象，对应的属性值。  <strong>这样就触发了defineProperty 中的get , 来收集依赖， 实际上就是将 watcher 实例本身收集了。</strong></li>
<li>在index.js 中再改变对象中某个值的时候，会触发 defineProperty 中的set ,触发 notify ,进而将dep 中观察这个对象时收集的依赖触发。<strong>就是出触发 watcher 中的update .update中 会重新获取该对象的该属性值，会得到newVal, 也会再次收集依赖， 最后调用 回调函数，将oldVal和newOld 作为参数。</strong></li>
</ol></div>  
</div>
            