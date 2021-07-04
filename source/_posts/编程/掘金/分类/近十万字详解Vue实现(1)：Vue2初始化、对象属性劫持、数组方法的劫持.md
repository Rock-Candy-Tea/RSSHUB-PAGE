
---
title: '近十万字详解Vue实现(1)：Vue2初始化、对象属性劫持、数组方法的劫持'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3c5d25a9814b26b84450beaf4a8611~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 01:45:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3c5d25a9814b26b84450beaf4a8611~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><code>vue2</code>是<code>options API</code>的,在<code>vue3</code>中 保留了</p>
<p><code>options api </code>无法 <code>tree-shaking</code></p>
<p><code>vue2</code>是一个<code>构造函数</code>不是类（class），通过<code>原型的方式</code>给<code>vue</code>实现功能：<code>vue.prototype = xxx</code></p>
</blockquote>
<h2 data-id="heading-0">1、vue初始化</h2>
<blockquote>
<p>当用户 new Vue的时候 通过扩展原型的方法 调用_init方法进行vue的初始化</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue.js</span>
<span class="hljs-keyword">import</span> &#123;initMixin&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./init'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-built_in">this</span>._init(options);
&#125;
initMixin(Vue); <span class="hljs-comment">// 给原型上新增_init方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2、将用户输入的选项放到 <code>vm.$options</code> 代表 用户传入的所有属性</h2>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-comment">// init.js</span>
<span class="hljs-keyword">import</span> &#123;initState&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./state'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>)</span>&#123;
    <span class="hljs-comment">// 后续组件开发的时候 Vue.extend 可以创建一个子组件。子组件可以继承Vue，子组件可以调用_init方法</span>
    Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm  = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// 把用户的选项放到vm上，这样在其他方法中可以获取到options</span>
        vm.$options = options
        <span class="hljs-comment">// 初始化状态</span>
        initState(vm)
        
        <span class="hljs-comment">// 如果有 el要将数据挂载到页面上</span>
        <span class="hljs-keyword">if</span>(vm.$options.el)&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'页面要挂载'</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3、初始化状态<code>initState(vm)</code> （包含data、计算属性、方法等）</h2>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span>(<span class="hljs-params">vm</span>)</span>&#123;
    <span class="hljs-keyword">const</span> opts = vm.$options;
    <span class="hljs-keyword">if</span>(opts.props)&#123;
        initProps(vm);
    &#125;
    <span class="hljs-keyword">if</span>(opts.methods)&#123;
        initMethod(vm);
    &#125;
    <span class="hljs-keyword">if</span>(opts.data)&#123;
        <span class="hljs-comment">// 初始化data</span>
        initData(vm);
    &#125;
    <span class="hljs-keyword">if</span>(opts.computed)&#123;
        initComputed(vm);
    &#125;
    <span class="hljs-keyword">if</span>(opts.watch)&#123;
        initWatch(vm);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initProps</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMethod</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initComputed</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initWatch</span>(<span class="hljs-params"></span>)</span>&#123;&#125;s
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3.1、数据的初始化<code>initData</code>，观测的是用户设置的data，和vm没关系</h3>
<blockquote>
<p><code>data</code>有两种情况 ：要么是<code>函数</code>要么是<code>对象</code>，对<code>data</code>类型进行判断  如果是 函数就获取函数返回值</p>
<p>获取函数执行结果的时候 用 <code>data.call(vm)</code>  保证 data函数中的 <code>this</code> 指向<code>vue</code>实例 其实和返回值无关</p>
<p>只有根实例中的data才能是对象</p>
</blockquote>
<h4 data-id="heading-4">将data定义在<code>vm._data</code>属性上将data和_data关联起来，方便在外部能用<code>vm._data</code>获取到被观测过的数据，不写成 vm.data 是为了区分用户获取场景</h4>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-comment">// state.js initData 函数</span>
<span class="hljs-keyword">import</span> &#123;observe&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./observer/index.js'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>)</span>&#123;
    <span class="hljs-keyword">let</span> data = vm.$options.data;
    <span class="hljs-comment">// 将data都定义在vm._data属性上</span>
    <span class="hljs-comment">// 不写成 vm.data 是为了区分用户获取场景</span>
    data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span> ? data.call(vm) : data;
    <span class="hljs-comment">// 需要将data变成响应式的 使用Object.defineProperty 重写data中的所有属性</span>
    observe(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">使用defineProperty将<code>_data</code>中的所有属性都代理到vm上，方便直接获取,'vm.nam === vm._data.name'</h4>
<blockquote>
<p>取值的时候做代理，不是直接把属性添加到vm上，而且直接赋值会出现命名冲突问题</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// state.js proxy 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">vm,key,source</span>)</span>&#123; <span class="hljs-comment">//取值的时候做代理，不是直接把属性添加到vm上，而且直接赋值会出现命名冲突问题</span>
    <span class="hljs-built_in">Object</span>.defineProperty(vm,key,&#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> vm[source][key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span>&#123;
            vm[source][key] = newValue  <span class="hljs-comment">//vm.nam === vm._data.name</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>)</span>&#123;
    <span class="hljs-keyword">let</span> data = vm.$options.data;
    <span class="hljs-comment">// 将data都定义在vm._data属性上</span>
    <span class="hljs-comment">// 不写成 vm.data 是为了区分用户获取场景</span>
    data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span> ? data.call(vm) : data;
    <span class="hljs-comment">// 循环代理所有属性</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> data)&#123;
        proxy(vm,key,<span class="hljs-string">'_data'</span>)
    &#125;
    
    <span class="hljs-comment">// 需要将data变成响应式的 使用Object.defineProperty 重写data中的所有属性</span>
    observe(data);
    
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.2、observe观测数据将data变成响应式的（对象类型拦截）</h3>
<p><code>props</code> 初始化在<code>data</code>之前</p>
<blockquote>
<p>只对<code>对象类型</code>进行观测 <code>非对象类型</code>无法观测<code>直接return</code></p>
<p>通过<code>Observe类</code>来实现对数据的观测，类方便扩展，类会产生实例以作为唯一标识</p>
<p>将对象中的所有<code>key</code> 重新用<code>defineProperty</code>定义为响应式的</p>
<p>如果一个数据已经被观测过，就不要在进行观测，用类来实现，观测过一个数据就添加一个标识，说明观测过了，在观测的时候先检测是否观测过，如果观测过了就跳过</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 观测数据</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">data</span>)</span>&#123;
    <span class="hljs-comment">// console.log(data,'observe')</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> data !== <span class="hljs-string">'object'</span> || data == <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">if</span>(data.__ob__)&#123;  <span class="hljs-comment">//数据上有这个属性表示已经观测过了 防止 循环引用</span>
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// 通过类来实现对数据的观测，类方便扩展，类会产生实例以作为唯一标识</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Observe(data)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.2.1、递归观测数据</h3>
<blockquote>
<p>vue2 应用了<code>defineProperty</code>需要一<code>加载的时候</code>就进行递归操作，所以耗费性能，如果层次过深也会浪费性能</p>
<p>如果给vm设置了一个新的对象类型数据，应该在<code>Object.defineProperty</code> 的<code>set</code>中再次劫持变成响应式的</p>
<p><code>Object.defineProperty</code>监控的是对象的属性，<code>proxy</code>监控的是对象</p>
<p>新设置的可能也是对象 也要递归观测数据</p>
</blockquote>
<h4 data-id="heading-8">性能优化原则：</h4>
<ul>
<li>1）不要把所有的数据都放在data中，因为所有的数据都会增加get和set</li>
<li>2）数据尽量扁平化，不要嵌套过深，递归会耗费性能</li>
<li>3）不要频繁的获取被观测的数据，数据的get拦截器中会有很多操作</li>
<li>4）如果数据不需要响应式，用<code>Object.freeze</code>冻结属性，原理是将属性的<code>configurable</code>设为<code>false</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// observe.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123; <span class="hljs-comment">// 观测值</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.walk(value);
    &#125;
    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span>&#123; <span class="hljs-comment">// 使用 defineProperty 对对象上的所有属性依次进行观测</span>
        <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(data);
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keys.length; i++)&#123;
            <span class="hljs-keyword">let</span> key = keys[i];
            <span class="hljs-keyword">let</span> value = data[key];
            defineReactive(data,key,value);
        &#125;
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">data,key,value</span>)</span>&#123;<span class="hljs-comment">// vue2慢的他原因主要就是这个方法的原因</span>
    <span class="hljs-comment">// 形成了闭包 因为return了上个作用域的value </span>
    observe(value);  <span class="hljs-comment">// value可能也是对象 递归观测数据</span>
    <span class="hljs-built_in">Object</span>.defineProperty(data,key,&#123; 
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> value
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span>&#123;
            <span class="hljs-keyword">if</span>(newValue == value) <span class="hljs-keyword">return</span>;
            observe(newValue); <span class="hljs-comment">// 新设置的可能也是对象 递归观测数据</span>
            value = newValue
        &#125;
    &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> data !== <span class="hljs-string">'object'</span> || data == <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">if</span>(data.__ob__)&#123;  <span class="hljs-comment">//数据上有这个属性表示已经观测过了 防止 循环引用</span>
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// 通过类来实现对数据的观测;类:方便扩展，类会产生实例以作为唯一标识</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Observer(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.3、数组类型拦截：通过改写数组原型，监听(改写)数组自身的方法来实现push、pop、shift、unshift、soplice、reverse、sort 七种方法</h3>
<blockquote>
<p>按照<code>3.2</code>的逻辑也用循环<code>defineProperty</code>的话，虽然可以实现修改索引触发更新，但是，给数组的每一项都进行了数据劫持，这样是有性能问题的，而且数组的属性可能是各种各样的，比如: 函数、length</p>
<p>因此源码中没有采用这个方法，所以 修改数组的索引或者length也不会触发视图更新（直接<code>arr[0]=xx</code>不能被监控）</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3c5d25a9814b26b84450beaf4a8611~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-comment">//* 数组如果也用循环defineProperty的话 每一项都会设置get和set 性能比较差</span>
        <span class="hljs-keyword">if</span>(isArray(value))&#123;
            <span class="hljs-comment">//更改数组原型方法 </span>
            value.__proto__ = arrayMethods <span class="hljs-comment">// 重写数组的方法</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.walk(value)  <span class="hljs-comment">//核心就是循环对象</span>
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123; <span class="hljs-comment">//使用 defineProperty从新定义</span>
            defineReactive(data,key,data[key])

        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.3.1、在监测数据的时候 对数组和对象分类处理，不能直接改写数组的方法，只有被vue控制的数组才需要改写</h3>
<h4 data-id="heading-11">让arrayMethods 继承于Array.prototype，arrayMethods找不到的方法可以通过原型链(__proto__)去Array.prototype找</h4>
<blockquote>
<p>数组的新方法是放在数组的实例上的不是在数组的 <code>__proto__</code> 上</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> oldArrayPrototype = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-keyword">let</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(oldArrayPrototype); <span class="hljs-comment">// 让arrayMethods 继承于Array.prototype，arrayMethods找不到去Array.prototype找</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">不能直接改变原型方法</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 不能用 这是直接改变不是 继承 </span>
arrayMethods = oldArrayPrototype

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">改写方法时使用 AOP切片编程，做一些操作以后 还是要调用数组原来的方法</h4>
<blockquote>
<p>比如新增，我们需要只需要在对应方法呗调用的时候去，将新增的数据放到一个数组中（也就是arguements），然后再调用observeArray就好了</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> methods = [
    <span class="hljs-string">`push`</span>,
    <span class="hljs-string">`pop`</span>,
    <span class="hljs-string">`shift`</span>,
    <span class="hljs-string">`unshift`</span>,
    <span class="hljs-string">`reverse`</span>,
    <span class="hljs-string">`sort`</span>
]
methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123; <span class="hljs-comment">//AOP切片编程</span>
    arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>)</span>&#123; 
        <span class="hljs-comment">//重写数组方法</span>
        <span class="hljs-comment">//todu...</span>
        
        <span class="hljs-keyword">let</span> result = oldArrayPrototypeMethods[method].call(<span class="hljs-built_in">this</span>,...args);  <span class="hljs-comment">//做一些操作以后 还是要调用数组原来的方法</span>
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">3.3.2、数组中原有的对象或者数组，通过observeArray循环调用<code>3.2</code>的observe方法</h3>
<blockquote>
<p>不用判断每一项的数据类型，因为上边的<code>observe</code>函数中已经做了判断</p>
<p>如果数组中的属性是引用数据类型 那么是响应式的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// state.js 中 class Observe的constructor中</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123; <span class="hljs-comment">// 观测值</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(value))&#123;
            value.__proto__ = arrayMethods; <span class="hljs-comment">// 重写数组原型方法</span>
            <span class="hljs-built_in">this</span>.observeArray(value); <span class="hljs-comment">// 递归遍历数组，对数组内部的对象进行观测</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-built_in">this</span>.walk(value);
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">observeArray</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span> ; i < value.length ;i ++)&#123;
            observe(value[i]);
        &#125;
    &#125;
    <span class="hljs-comment">// 或者 </span>
    <span class="hljs-function"><span class="hljs-title">observeArray</span>(<span class="hljs-params">value</span>)</span>&#123;
        value.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> observe(item))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">vm.arr[0].name = "aaa" 可以触发更新，走的是对象的逻辑，vm.arr[0] = "bb" 不行</h5>
<h5 data-id="heading-16">vue2 无法劫持到不存在的属性，新增不存在的属性不会更新视图</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">vm.message = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'aaa'</span>&#125;
vm.message.age = <span class="hljs-number">18</span>  <span class="hljs-comment">// 不会触发更新</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.3.3、 数组新增的对象需要被监测到</h3>
<blockquote>
<p>新增有两种：一种是<code>push、unshift</code>这种参数只有增加项的方法，一种是<code>splice</code>这种参数有好项的增加方式</p>
<p>因此需要获取到加入的数据，并通过<code>observeArray</code>拦截</p>
<p>对数据进行拦截的时候是先赋值再通过<code>observeArray</code>拦截</p>
</blockquote>
<h4 data-id="heading-18">增加__ob__属性 方便别的地方获取</h4>
<blockquote>
<p><code>value.__ob__ = this</code>;  这种写法会导致死循环 因为__ob__会被重复监听 所以要用Objecy.defineproperty改成不可枚举的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
    
        <span class="hljs-comment">//给对象和数组 添加一个自定义属性 指向 察观类的实例 就可以通过__ob__获取到私有和公有方法</span>
        <span class="hljs-comment">//value.__ob__ = this;</span>
        <span class="hljs-built_in">Object</span>.defineProperty(value,<span class="hljs-string">'__ob__'</span>,&#123;
            <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,  <span class="hljs-comment">// 表示属性不能被枚举</span>
            <span class="hljs-attr">configurable</span>:<span class="hljs-literal">false</span>,
            <span class="hljs-attr">value</span>:<span class="hljs-built_in">this</span>
        &#125;);


        <span class="hljs-comment">//* 数组如果也用循环defineProperty的话 每一项都会设置get和set 性能比较差</span>
        <span class="hljs-keyword">if</span>(isArray(value))&#123;
            <span class="hljs-comment">//更改数组原型方法 </span>
            value.__proto__ = arrayMethods <span class="hljs-comment">// 重写数组的方法</span>
            <span class="hljs-built_in">this</span>.observeArray(value) <span class="hljs-comment">// 处理数组中的对象</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.walk(value)  <span class="hljs-comment">//核心就是循环对象</span>
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">observeArray</span>(<span class="hljs-params">value</span>)</span>&#123;
    ...
    &#125;
    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span>&#123;
    ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">监听push、unshift、splice方法，如果有新增需要用observeArray 监听</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// array.js</span>
methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123; <span class="hljs-comment">//AOP切片编程</span>
    arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>)</span>&#123; <span class="hljs-comment">//重写数组方法</span>
        <span class="hljs-comment">//todu...</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数组改变了'</span>);
        
        
        <span class="hljs-comment">// 数组新增的属性  要看一下是不是对象 是对象继续进行劫持</span>
        <span class="hljs-keyword">let</span> inserted = <span class="hljs-literal">null</span>
        <span class="hljs-keyword">switch</span>(method)&#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">`push`</span>:  <span class="hljs-comment">// 修改 删除  添加  arr.splice(位置,个数,添加内容)</span>
            inserted = args.slice(<span class="hljs-number">2</span>)
            <span class="hljs-keyword">case</span> <span class="hljs-string">`pop`</span>:
            <span class="hljs-keyword">case</span> <span class="hljs-string">`unshift`</span>:
                inserted = args  <span class="hljs-comment">//调用 push unshift 传递的参数 就是 新增的逻辑</span>
                <span class="hljs-keyword">break</span>;
        &#125;

        <span class="hljs-comment">// 根据inserted是否有内容 来确定是否需要二次劫持</span>
        <span class="hljs-comment">// 如果有内容 需要用observeArray 监听</span>
        <span class="hljs-comment">// 通过 this.__ob__ 获取到 察观类的实例 然后再获取到公有方法 observeArray</span>
        <span class="hljs-comment">// this是当前调用方法的数据（对象和数组）</span>
        <span class="hljs-keyword">let</span> ob = <span class="hljs-built_in">this</span>.__ob__
        <span class="hljs-keyword">if</span>(inserted) ob.observeArray(inserted)

        <span class="hljs-keyword">let</span> result = oldArrayPrototype[method].call(<span class="hljs-built_in">this</span>,...args);  <span class="hljs-comment">//做一些操作以后 还是要调用数组原来的方法</span>
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">总结</h3>
<ul>
<li>1、<code>new Vu</code>e 会调用 <code>_init</code> 方法进行初始化操作</li>
<li>2、会将用户的选项放到<code> vm.$options</code>上</li>
<li>3、会在当前属性上搜索有没有<code>data</code>数据 <code>initState</code></li>
<li>4、有<code>data</code>判断<code>data</code>是不是一个函数 如果是函数取返回值<code>initdata</code></li>
<li>5、<code>observe</code>去观测<code>data</code>中的数据 和 <code>vm</code>没有关系</li>
<li>6、<code>vm</code>上想取到<code>data</code>中的数据  <code>vm.data = data</code> 这样用户可以通过 <code>vm._data</code> 获取到<code>data</code>了</li>
<li>7、这样取值还是有些麻烦 所以 用<code>Object.defineProperty</code>代理 使 <code>vm.name = vm._data.name</code></li>
<li>8、如果更新对象不存在的属性，会导致视图不更新；更新数组的索引和长度不会触发更新</li>
<li>9、如果替换成一个新的对象，新对象会被劫持，如果数组存放新内容 <code>push unshift slice</code>新增的内容也会被劫持</li>
<li>通过<code>__ob__</code>进行表示这个对象是否被标记过（在<code>vue</code>中被监控的对象身上都有一个<code>__ob__</code>属性）</li>
<li>10、 如果就想改索引可以使用<code>$set</code> 但是<code>$set</code>内部就是<code>splice</code></li>
</ul></div>  
</div>
            