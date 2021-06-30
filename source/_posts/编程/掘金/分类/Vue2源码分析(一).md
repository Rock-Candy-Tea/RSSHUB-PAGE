
---
title: 'Vue2源码分析(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3249'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 02:07:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=3249'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.rollup项目搭建</h3>
<h4 data-id="heading-1">1.1.依赖</h4>
<ul>
<li><code>rollup</code>:打包工具</li>
<li><code>@babel/core</code>:babel核心模块</li>
<li><code>@babel/preset-env</code>:es6->es5</li>
<li><code>rollup-plugin-babel</code>:rollup和babel之间的桥梁</li>
</ul>
<pre><code class="hljs language-npm copyable" lang="npm">yarn add rollup @babel/core @babel/preset-env rollup-plugin-babel
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">1.2.<code>rollup.config.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-babel'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">input</span>:<span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>:&#123;
        <span class="hljs-attr">format</span>:<span class="hljs-string">'umd'</span>,<span class="hljs-comment">//支持amd和commonjs</span>
        <span class="hljs-attr">file</span>:<span class="hljs-string">'dist/vue.js'</span>,
        <span class="hljs-attr">sourcemap</span>:<span class="hljs-literal">true</span>,<span class="hljs-comment">//es5->es6映射文件</span>
        <span class="hljs-attr">name</span>:<span class="hljs-string">'Vue'</span>
    &#125;,
    <span class="hljs-attr">plugins</span>:[
        babel(&#123;<span class="hljs-comment">//使用babel进行转化，排除node_moduels</span>
            <span class="hljs-attr">exclude</span>:<span class="hljs-string">'node_modules/**'</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">1.3.<code>.babelrc</code></h4>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">1.4.<code>package.json</code></h4>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"scripts"</span>:&#123;
        <span class="hljs-attr">"serve"</span>:<span class="hljs-string">"rollup -c -w"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.响应式数据</h3>
<blockquote>
<p>测试</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> vm=<span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">name</span>:<span class="hljs-string">'zhangsan'</span>,
                <span class="hljs-attr">family</span>:&#123;
                    <span class="hljs-attr">father</span>:<span class="hljs-string">'李四'</span>,
                    <span class="hljs-attr">mather</span>:<span class="hljs-string">'王武'</span>
                &#125;
            &#125;
        &#125;)
        vm._data.family=&#123;
            <span class="hljs-attr">father</span>:<span class="hljs-string">'章六'</span>
        &#125;
        <span class="hljs-built_in">console</span>.log(vm)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2.1.<code>index.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; initMixin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./init"</span>;

<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options 用户传入的选项
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>)</span>&#123;
    <span class="hljs-comment">//初始化操作</span>
    <span class="hljs-built_in">this</span>._init(options);
&#125;

<span class="hljs-comment">//扩展原型方法</span>
initMixin(Vue);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.2.<code>init.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; initState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./state"</span>;
<span class="hljs-comment">/**
 * 初始化操作
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>Vue 类
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>)</span>&#123;
    Vue.prototype._init=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>)</span>&#123;
        <span class="hljs-keyword">const</span> vm=<span class="hljs-built_in">this</span>;
        vm.$options=options;
        <span class="hljs-comment">//对数据进行初始化</span>
        initState(vm);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2.3.<code>state.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; observe &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./observer/index"</span>;
<span class="hljs-keyword">import</span> &#123;
    isFunction
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils"</span>;

<span class="hljs-comment">/**
 * 初始化状态
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span>(<span class="hljs-params">vm</span>) </span>&#123;
    <span class="hljs-keyword">const</span> opt = vm.$options;
    <span class="hljs-keyword">if</span> (opt.data) &#123;
        initData(vm);
    &#125;
&#125;

<span class="hljs-comment">/**
 * 初始化Data数据
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>) </span>&#123;
    <span class="hljs-keyword">let</span> data = vm.$options.data;
    <span class="hljs-comment">/**
     * //TODO
     * 1.如果data是方法，需要执行，并不this依然是Vue实例
     * 2.需要通过_data将劫持到的数据关联起来
     */</span>
    data = vm._data = isFunction(data) ? data.call(vm) : data;

    <span class="hljs-comment">//对数据进行劫持</span>
    observe(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">2.4.<code>observer/index.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
    isObject
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../utils"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.walk(data);
    &#125;

    <span class="hljs-comment">/**
     * 对象数据劫持
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>data 数据
     */</span>
    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            defineReactive(data, key, data[key]);
        &#125;)
    &#125;
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">TODO:</span>Vue2为什么性能不好，主要原因就是数据的劫持的全量劫持
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>data 原数据
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 值
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">data, key, value</span>) </span>&#123;
    observe(value); <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>如果value是一个对象，需要对value进行深层次的劫持操作</span>
    <span class="hljs-built_in">Object</span>.defineProperty(data, key, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> value;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
            <span class="hljs-keyword">if</span> (newVal === value) <span class="hljs-keyword">return</span>;
            observe(newVal); <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>重新设置的值可能是一个对象，这个时候需要重新对其进行劫持处理</span>
            value = newVal;
        &#125;
    &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>data必须是一个对象,默认最外层必须是一个对象</span>
    <span class="hljs-keyword">if</span> (!isObject(data)) <span class="hljs-keyword">return</span>;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Observer(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2.5.<code>utils.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isFunction</span>(<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'function'</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span> && val !== <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.数据代理</h3>
<blockquote>
<p>为了方便用户取到data的数据，比如：vm._data.name，可以通过vm.name来取值</p>
</blockquote>
<p><code>state.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 初始化Data数据
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 实例
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>) </span>&#123;
    <span class="hljs-keyword">let</span> data = vm.$options.data;
    <span class="hljs-comment">/**
     * //TODO
     * 1.如果data是方法，需要执行，并不this依然是Vue实例
     * 2.需要通过_data将劫持到的数据关联起来
     */</span>
    data = vm._data = isFunction(data) ? data.call(vm) : data;

    <span class="hljs-comment">//对vm._data上的数据进行代理，方便用户后续的取值和设值</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> data) &#123;
        proxy(vm, <span class="hljs-string">'_data'</span>, key)
    &#125;
    <span class="hljs-comment">//对数据进行劫持</span>
    observe(data);
&#125;

<span class="hljs-comment">/**
 * 对数据进行一层代理，方便用户对数据取值和设值，「vm._data.name='李四',可以直接用vm.name='李四'」
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>source _data
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">vm, source, key</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(vm, key, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> vm[source][key];
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
            vm[source][key] = newVal;
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.数组响应式</h3>
<h4 data-id="heading-13">4.1.测试</h4>
<ul>
<li>1.数组里面是对象类型的需要被劫持</li>
<li>2.数组新增的是对象类型需要被劫持</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> vm=<span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">arr</span>:[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'zhangsan'</span>&#125;]
            &#125;
        &#125;)
        vm.arr.push(&#123;<span class="hljs-attr">age</span>:<span class="hljs-number">18</span>&#125;);
        <span class="hljs-built_in">console</span>.log(vm.arr)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">4.2.<code>observe/index.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
    arrayMethods
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./array"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-comment">//给data上添加__ob__属性，值为Observer实例，并且不可枚举，不然死循环</span>
        <span class="hljs-built_in">Object</span>.defineProperty(data, <span class="hljs-string">'__ob__'</span>, &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>
        &#125;)
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(data)) &#123;
            <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>数组劫持，数组原来方法的重写</span>
            data.__proto__ = arrayMethods;
            <span class="hljs-comment">//TODO：如果数组中的数据也可能是对象类型</span>
            <span class="hljs-built_in">this</span>.observeArray(data);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.walk(data);
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * <span class="hljs-doctag">TODO:</span>
     * 1.对数组中的数据进行观察，如果是对象需要继续进行劫持
     * 2.新增的数据可能是对象，也需要进行劫持
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>data 数组
     */</span>
    <span class="hljs-function"><span class="hljs-title">observeArray</span>(<span class="hljs-params">data</span>)</span> &#123;
        data.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> observe(item));
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>data必须是一个对象,默认最外层必须是一个对象</span>
    <span class="hljs-keyword">if</span> (!isObject(data)) <span class="hljs-keyword">return</span>;
    <span class="hljs-comment">//如果观察的数据已经有了__ob__属性，说明这个数据已经被劫持过了，不用再劫持</span>
    <span class="hljs-keyword">if</span> (data.__ob__) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Observer(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.3.<code>observer/array.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//原始Array的原型</span>
<span class="hljs-keyword">const</span> oldArrayPrototype = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-comment">//创建一个新的数组原型，arrayMethods.__proto__=Array.propotype</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(oldArrayPrototype);
<span class="hljs-comment">//需要重写的方法 7个</span>
<span class="hljs-keyword">const</span> methods = [
    <span class="hljs-string">'push'</span>,
    <span class="hljs-string">'unshift'</span>,
    <span class="hljs-string">'shift'</span>,
    <span class="hljs-string">'pop'</span>,
    <span class="hljs-string">'splice'</span>,
    <span class="hljs-string">'sort'</span>,
    <span class="hljs-string">'reverse'</span>
];

methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
    <span class="hljs-comment">//用户调用的如果是上面的7种方法，会先走自己重新的方法</span>
    arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
        <span class="hljs-comment">//原始的数组方法调用</span>
        oldArrayPrototype[method].call(<span class="hljs-built_in">this</span>, ...args);
        <span class="hljs-keyword">let</span> inserted;
        <span class="hljs-keyword">switch</span> (method) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:
            <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>:
                inserted = args; <span class="hljs-comment">//新增内容</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>:
                inserted = args.slice(<span class="hljs-number">2</span>);
                <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-comment">//新增的数据需要对其进行劫持 「this.__ob__是Observer实例」</span>
        <span class="hljs-keyword">if</span> (inserted) <span class="hljs-built_in">this</span>.__ob__.observeArray(inserted);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">5.生成编译模板</h3>
<h4 data-id="heading-17">5.1.<code>init.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; compileToFunction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./compiler/index"</span>;
<span class="hljs-keyword">import</span> &#123;
    initState
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./state"</span>;
<span class="hljs-comment">/**
 * 初始化操作
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>Vue 类
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
    Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        vm.$options = options;
        <span class="hljs-comment">//对数据进行初始化</span>
        initState(vm);

        <span class="hljs-keyword">if</span> (options.el) &#123;
            <span class="hljs-comment">/**
             * <span class="hljs-doctag">TODO:</span>将数据挂载到模板上
             * 用户挂载可以通过两种方式，
             * 1.一种自动挂载，new Vue(&#123;el:'#app'&#125;)
             * 2.手动挂载，vm.$mount('#app')
             */</span>
            vm.$mount(options.el);
        &#125;
    &#125;

    Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> options = vm.$options;
        el = <span class="hljs-built_in">document</span>.querySelector(el);
        <span class="hljs-comment">/**
         * TODO：
         * 1.把模板字符串转化成对应的渲染函数
         * 2.渲染函数执行生成虚拟DOM
         * 3.diff算法，更新虚拟DOM
         * 4.产生真是节点，更新
         */</span>
        <span class="hljs-keyword">if</span> (!options.render) &#123;
            <span class="hljs-keyword">let</span> template = options.template;
            <span class="hljs-keyword">if</span> (!template && el) &#123;
                <span class="hljs-comment">//获取模版字符串 <div id="app"></div></span>
                template = el.outerHTML;
                options.render = compileToFunction(template);
            &#125;
        &#125;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6.模板解析「词法解析」</h3>
<h4 data-id="heading-19">6.1.<code>compiler/index.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; parserHTML &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./parser"</span>;

<span class="hljs-comment">/**
 * 模板编译
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>template 模板
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compileToFunction</span>(<span class="hljs-params">template</span>)</span>&#123;
    parserHTML(template);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">6.2.<code>compiler/parser.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ncname = <span class="hljs-string">`[a-zA-Z_][\\-\\.0-9_a-zA-Z]*`</span>; <span class="hljs-comment">// 标签名 </span>
<span class="hljs-keyword">const</span> qnameCapture = <span class="hljs-string">`((?:<span class="hljs-subst">$&#123;ncname&#125;</span>\\:)?<span class="hljs-subst">$&#123;ncname&#125;</span>)`</span>; <span class="hljs-comment">//  用来获取的标签名的 match后的索引为1的</span>
<span class="hljs-keyword">const</span> startTagOpen = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`^<<span class="hljs-subst">$&#123;qnameCapture&#125;</span>`</span>); <span class="hljs-comment">// 匹配开始标签的 <div</span>
<span class="hljs-keyword">const</span> endTag = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`^<\\/<span class="hljs-subst">$&#123;qnameCapture&#125;</span>[^>]*>`</span>); <span class="hljs-comment">// 匹配闭合标签的 </div></span>
<span class="hljs-comment">//           aa  =   "  xxx "  | '  xxxx '  | xxx</span>
<span class="hljs-keyword">const</span> attribute = <span class="hljs-regexp">/^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/</span>; <span class="hljs-comment">// a=b  a="b"  a='b'</span>
<span class="hljs-keyword">const</span> startTagClose = <span class="hljs-regexp">/^\s*(\/?)>/</span>; <span class="hljs-comment">//   >  /> </span>
<span class="hljs-keyword">const</span> defaultTagRE = <span class="hljs-regexp">/\&#123;\&#123;((?:.|\r?\n)+?)\&#125;\&#125;/g</span>; <span class="hljs-comment">// &#123;&#123;aaaaa&#125;&#125;</span>

<span class="hljs-comment">/**
 * 词法解析
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>html 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parserHTML</span>(<span class="hljs-params">html</span>) </span>&#123; <span class="hljs-comment">//<div id="app">&#123;&#123;name&#125;&#125;</div></span>
    <span class="hljs-keyword">while</span> (html) &#123;
        <span class="hljs-comment">//<当前的位置</span>
        <span class="hljs-keyword">const</span> textEnd = html.indexOf(<span class="hljs-string">'<'</span>);
        <span class="hljs-keyword">if</span> (textEnd === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">//开始位置</span>
            <span class="hljs-keyword">const</span> startTagMatch = parseStartTag(); <span class="hljs-comment">//解析开始标签</span>
            <span class="hljs-keyword">if</span> (startTagMatch) &#123;
                start(startTagMatch.tagName, startTagMatch.attrs);
                <span class="hljs-keyword">continue</span>;
            &#125;
            <span class="hljs-comment">// ["</div>", "div", index: 0, input: "</div>", groups: undefined]</span>
            <span class="hljs-keyword">const</span> endTagMatch = html.match(endTag);
            <span class="hljs-keyword">if</span> (endTagMatch) &#123;
                end(endTagMatch[<span class="hljs-number">1</span>]);
                advance(endTagMatch[<span class="hljs-number">0</span>].length);
                <span class="hljs-keyword">continue</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">let</span> text;
        <span class="hljs-keyword">if</span> (textEnd > <span class="hljs-number">0</span>) &#123;
            text = html.substring(<span class="hljs-number">0</span>, textEnd);
        &#125;
        <span class="hljs-keyword">if</span> (text) &#123;
            chars(text);
            advance(text.length); <span class="hljs-comment">//</div></span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseStartTag</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//<div", "div", index: 0, input: "<div id=\"app\">&#123;&#123;name&#125;&#125;</div>", groups: undefined]</span>
        <span class="hljs-keyword">const</span> start = html.match(startTagOpen);
        <span class="hljs-keyword">if</span> (start) &#123;
            <span class="hljs-keyword">const</span> match = &#123;
                <span class="hljs-attr">tagName</span>: start[<span class="hljs-number">1</span>],
                <span class="hljs-attr">attrs</span>: []
            &#125;
            advance(start[<span class="hljs-number">0</span>].length); <span class="hljs-comment">// id="app">&#123;&#123;name&#125;&#125;</div></span>
            <span class="hljs-keyword">let</span> end, attr;
            <span class="hljs-comment">//不是结束标签，并且有属性</span>
            <span class="hljs-keyword">while</span> (!(end = html.match(startTagClose)) && (attr = html.match(attribute))) &#123;
                <span class="hljs-comment">//attr= [" id=\"app\"", "id", "=", "app", undefined, undefined, index: 0, input: " id=\"app\">&#123;&#123;name&#125;&#125;</div>", groups: undefined]</span>
                match.attrs.push(&#123;
                    <span class="hljs-attr">name</span>: attr[<span class="hljs-number">1</span>],
                    <span class="hljs-attr">value</span>: attr[<span class="hljs-number">3</span>] || attr[<span class="hljs-number">4</span>] || attr[<span class="hljs-number">5</span>]
                &#125;)
                advance(attr[<span class="hljs-number">0</span>].length); <span class="hljs-comment">// >&#123;&#123;name&#125;&#125;</div></span>
            &#125;
            <span class="hljs-keyword">if</span> (end) &#123;
                advance(end[<span class="hljs-number">0</span>].length); <span class="hljs-comment">// &#123;&#123;name&#125;&#125;</div></span>
            &#125;
            <span class="hljs-keyword">return</span> match;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">advance</span>(<span class="hljs-params">len</span>) </span>&#123;
        html = html.substring(len)
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params">tagName, attrs</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'start'</span>, tagName, attrs)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chars</span>(<span class="hljs-params">text</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'chars'</span>, text)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">end</span>(<span class="hljs-params">tagName</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'end'</span>, tagName)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">7.构建AST树</h3>
<h4 data-id="heading-22">7.1.<code>compiler/parser.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js">/构建AST树，栈型结构
<span class="hljs-keyword">let</span> root = <span class="hljs-literal">null</span>,
    stack = [];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params">tagName, attrs</span>) </span>&#123;
    <span class="hljs-comment">//获取父节点</span>
    <span class="hljs-keyword">const</span> parent = stack[stack.length - <span class="hljs-number">1</span>];
    <span class="hljs-comment">//创建节点</span>
    <span class="hljs-keyword">const</span> element = createAstElement(tagName, attrs);
    <span class="hljs-keyword">if</span> (!root) &#123; <span class="hljs-comment">//树里还没用东西</span>
        root = element;
    &#125;
    <span class="hljs-keyword">if</span> (parent) &#123; <span class="hljs-comment">//与父亲建立关联</span>
        element.parent = parent;
        parent.children.push(element);
    &#125;
    stack.push(element);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chars</span>(<span class="hljs-params">text</span>) </span>&#123;
    <span class="hljs-comment">//去除空格</span>
    text = text.replace(<span class="hljs-regexp">/\s/g</span>, <span class="hljs-string">''</span>);
    <span class="hljs-keyword">if</span> (text) &#123;
        <span class="hljs-keyword">const</span> parent = stack[stack.length - <span class="hljs-number">1</span>];
        parent.children.push(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-number">3</span>,
            text
        &#125;)
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">end</span>(<span class="hljs-params">tagName</span>) </span>&#123;
    <span class="hljs-keyword">const</span> last = stack.pop();
    <span class="hljs-keyword">if</span> (last.tag !== tagName) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'标签错误'</span>);
&#125;

<span class="hljs-comment">/**
 * 创建节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>tagName 标签名称
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attrs 属性
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAstElement</span>(<span class="hljs-params">tagName, attrs</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">tag</span>: tagName,
        <span class="hljs-attr">type</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">//TODO：标签是1，文本是3</span>
        attrs,
        <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">children</span>: []
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">8.codeGen生成</h3>
<h4 data-id="heading-24">8.1.<code>compiler/index.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; generate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./generate"</span>;
<span class="hljs-keyword">import</span> &#123; parserHTML &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./parser"</span>;

<span class="hljs-comment">/**
 * 模板编译
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>template 模板
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compileToFunction</span>(<span class="hljs-params">template</span>)</span>&#123;
    <span class="hljs-keyword">const</span> root=parserHTML(template);
    generate(root);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">8.2.<code>compiler/generate.js</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> defaultTagRE = <span class="hljs-regexp">/\&#123;\&#123;((?:.|\r?\n)+?)\&#125;\&#125;/g</span>; <span class="hljs-comment">// &#123;&#123;aaaaa&#125;&#125;</span>
<span class="hljs-comment">/**
 * 属性处理
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>attrs 属性对象 [&#123;name:'id',value:'app'&#125;,&#123;name: "style", value: "color:red;background:green"&#125;]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genProps</span>(<span class="hljs-params">attrs</span>) </span>&#123;
    <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < attrs.length; i++) &#123;
        <span class="hljs-keyword">const</span> attr = attrs[i];
        <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">'style'</span>) &#123; <span class="hljs-comment">//&#123;name: "style", value: "color:red;background:green"&#125;</span>
            <span class="hljs-keyword">let</span> styleObj = &#123;&#125;;
            attr.value.replace(<span class="hljs-regexp">/([^;:]+)\:([^;:]+)/g</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                styleObj[<span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]] = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">2</span>];
            &#125;)
            attr.value = styleObj;
        &#125;
        str += <span class="hljs-string">`<span class="hljs-subst">$&#123;attr.name&#125;</span>:<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(attr.value)&#125;</span>,`</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`&#123;<span class="hljs-subst">$&#123;str.slice(<span class="hljs-number">0</span>,-<span class="hljs-number">1</span>)&#125;</span>&#125;`</span>
&#125;

<span class="hljs-comment">/**
 * // hello &#123;&#123;name&#125;&#125; world 转化为=> _v("hell"+_s(name)+"world")
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">gen</span>(<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (el.type === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">//标签</span>
        <span class="hljs-keyword">return</span> generate(el);
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">//文本</span>
        <span class="hljs-keyword">const</span> text = el.text;
        <span class="hljs-keyword">if</span> (!defaultTagRE.test(text)) &#123; <span class="hljs-comment">//不是&#123;&#123;&#125;&#125;包裹的</span>
            <span class="hljs-keyword">return</span> <span class="hljs-string">`_v('<span class="hljs-subst">$&#123;text&#125;</span>')`</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">const</span> tokens = [];
            <span class="hljs-keyword">let</span> match;
            <span class="hljs-comment">//<span class="hljs-doctag">TODO:</span>defaultTagRE.lastIndex需要制为零，exec会改变下标，每次进入时需要现重新拨回0的位置</span>
            <span class="hljs-keyword">let</span> lastIndex = defaultTagRE.lastIndex = <span class="hljs-number">0</span>;
            <span class="hljs-keyword">while</span> (match = defaultTagRE.exec(text)) &#123;
                <span class="hljs-keyword">let</span> index = match.index; <span class="hljs-comment">//开始索引</span>
                <span class="hljs-keyword">if</span> (index > lastIndex) &#123;
                    tokens.push(<span class="hljs-built_in">JSON</span>.stringify(text.slice(lastIndex, index))); <span class="hljs-comment">//hello</span>
                &#125;
                tokens.push(<span class="hljs-string">`_s(<span class="hljs-subst">$&#123;match[<span class="hljs-number">1</span>].trim()&#125;</span>)`</span>); <span class="hljs-comment">//&#123;&#123;name&#125;&#125;</span>
                lastIndex = index + match[<span class="hljs-number">0</span>].length;
            &#125;
            <span class="hljs-keyword">if</span> (lastIndex < text.length) &#123; <span class="hljs-comment">//</span>
                tokens.push(<span class="hljs-built_in">JSON</span>.stringify(text.slice(lastIndex))); <span class="hljs-comment">//world</span>
            &#125;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`_v(<span class="hljs-subst">$&#123;tokens.join(<span class="hljs-string">'+'</span>)&#125;</span>)`</span>;
        &#125;
    &#125;
&#125;

<span class="hljs-comment">/**
 * 处理孩子
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el =[&#123;"type":3,"text":"&#123;&#123;name&#125;&#125;"&#125;]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genChildren</span>(<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-keyword">const</span> children = el.children;
    <span class="hljs-keyword">if</span> (children) &#123;
        <span class="hljs-keyword">return</span> children.map(<span class="hljs-function"><span class="hljs-params">c</span> =></span> gen(c)).join(<span class="hljs-string">','</span>);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-comment">/**
&#123;
    "tag":"div",
    "type":1,
    "attrs":[
        &#123;
            "name":"id",
            "value":"app"
        &#125;,
        &#123;
            "name":"style",
            "value":"color:red;background:green"
        &#125;
    ],
    "parent":null,
    "children":[
        &#123;
            "type":3,
            "text":"hell&#123;&#123;name&#125;&#125;world"
        &#125;
    ]
&#125;
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generate</span>(<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(el))
    <span class="hljs-keyword">const</span> children = genChildren(el);
    <span class="hljs-keyword">const</span> code = <span class="hljs-string">`_c('<span class="hljs-subst">$&#123;el.tag&#125;</span>',<span class="hljs-subst">$&#123;el.attrs.length?genProps(el.attrs):<span class="hljs-string">'undefined'</span>&#125;</span><span class="hljs-subst">$&#123;children?<span class="hljs-string">`,<span class="hljs-subst">$&#123;children&#125;</span>`</span>:<span class="hljs-string">''</span>&#125;</span>)`</span>;
    <span class="hljs-built_in">console</span>.log(code)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">9.虚拟DOM实现</h3>
<h4 data-id="heading-27">9.1.生成render函数</h4>
<p><code>compiler/index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
    generate
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./generate"</span>;
<span class="hljs-keyword">import</span> &#123;
    parserHTML
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./parser"</span>;

<span class="hljs-comment">/**
 * 模板编译,生成render函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>template 模板
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compileToFunction</span>(<span class="hljs-params">template</span>) </span>&#123;
    <span class="hljs-comment">//生成AST树</span>
    <span class="hljs-keyword">const</span> root = parserHTML(template);
    <span class="hljs-comment">//通过AST树构建codegen 「_('div',&#123;'id':'#app'&#125;,'hello')」</span>
    <span class="hljs-keyword">const</span> code = generate(root);
    <span class="hljs-built_in">console</span>.log(code)
    <span class="hljs-comment">//Function +with构建方式 this=vm</span>
    <span class="hljs-keyword">let</span> render = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">`with(this)&#123;return <span class="hljs-subst">$&#123;code&#125;</span>&#125;`</span>);
    <span class="hljs-keyword">return</span> render;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">9.2.挂载</h4>
<p><code>init.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> options = vm.$options;
    el = <span class="hljs-built_in">document</span>.querySelector(el);
    <span class="hljs-comment">/**
     * TODO：
     * 1.把模板字符串转化成对应的渲染函数
     * 2.渲染函数执行生成虚拟DOM
     * 3.diff算法，更新虚拟DOM
     * 4.产生真是节点，更新
     */</span>
    <span class="hljs-keyword">if</span> (!options.render) &#123;
        <span class="hljs-keyword">let</span> template = options.template;
        <span class="hljs-keyword">if</span> (!template && el) &#123;
            <span class="hljs-comment">//获取模版字符串 <div id="app"></div></span>
            template = el.outerHTML;
            options.render = compileToFunction(template);
        &#125;
    &#125;
    <span class="hljs-comment">//组件挂载流程</span>
    mountComponent(vm, el);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>lifecycle.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lifecycleMixin</span>(<span class="hljs-params">Vue</span>)</span>&#123;
    Vue.prototype._update=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">vnode</span>)</span>&#123;
        <span class="hljs-keyword">const</span> vm=<span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vnode'</span>,vnode);
    &#125;
&#125;
<span class="hljs-comment">/**
 * 组件挂载
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vm 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el <div id='app'></div>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">vm,el</span>)</span>&#123;
    <span class="hljs-comment">/**
     * TODO：更新函数
     * 1.调用_render生成vdom
     * 2.调用_update进行更新操作
     */</span>
    <span class="hljs-keyword">const</span> updateComponent=<span class="hljs-function">()=></span>&#123;
        vm._update(vm._render());
    &#125;
    updateComponent();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">9.3.初始化</h4>
<p><code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//扩展原型方法</span>
initMixin(Vue);
renderMixin(Vue);<span class="hljs-comment">//_render</span>
lifecycleMixin(Vue);<span class="hljs-comment">//_update</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">9.4.生成虚拟DOM</h4>
<p><code>render.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
    createElement,
    createTextElement
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./vdom/index"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
    <span class="hljs-comment">//处理元素</span>
    Vue.prototype._c = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> createElement(vm, ...arguments);
    &#125;
    <span class="hljs-comment">//处理文本</span>
    Vue.prototype._v = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">text</span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> createTextElement(vm, text);
    &#125;
    <span class="hljs-comment">//处理&#123;&#123;&#125;&#125;</span>
    Vue.prototype._s = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(val);
        <span class="hljs-keyword">return</span> val;
    &#125;

    <span class="hljs-comment">//render函数，返回虚拟节点</span>
    Vue.prototype._render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> render = vm.$options.render;
        <span class="hljs-keyword">const</span> vnode = render.call(vm);
        <span class="hljs-keyword">return</span> vnode;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vdom/index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vm, tag, data = &#123;&#125;, ...children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> vnode(vm, tag, data, data.key, children, <span class="hljs-literal">undefined</span>);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextElement</span>(<span class="hljs-params">vm, text</span>) </span>&#123;
    <span class="hljs-keyword">return</span> vnode(vm, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, text);
&#125;
<span class="hljs-comment">//创建虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span>(<span class="hljs-params">vm, tag, data, key, children, text</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        vm,
        tag,
        data,
        key,
        children,
        text,
        <span class="hljs-comment">//...TODO</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">10.vdom创建真实dom</h3>
<h4 data-id="heading-32">10.1.将el绑定到vm上</h4>
<p><code>init.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
        <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> options = vm.$options;
        el = <span class="hljs-built_in">document</span>.querySelector(el);
        vm.$el = el;
&#125;        
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">10.2.虚拟DOM转为真实DOM</h4>
<p><code>lifecycle.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; patch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./vdom/patch"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lifecycleMixin</span>(<span class="hljs-params">Vue</span>)</span>&#123;
    Vue.prototype._update=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">vnode</span>)</span>&#123;
        <span class="hljs-keyword">const</span> vm=<span class="hljs-built_in">this</span>;
        patch(vm.$el,vnode);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vdom/patch.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 根据虚拟DOM创建真实DOM
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 虚拟DOM
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElem</span>(<span class="hljs-params">vnode</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123;
        tag,
        children,
        text
    &#125; = vnode;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> tag === <span class="hljs-string">'string'</span>) &#123; <span class="hljs-comment">//元素</span>
        <span class="hljs-comment">//vdom会添加一个el属性，对应真实节点</span>
        vnode.el = <span class="hljs-built_in">document</span>.createElement(tag);
        children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
            vnode.el.appendChild(createElem(child));
        &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">//文本</span>
        vnode.el = <span class="hljs-built_in">document</span>.createTextNode(text);
    &#125;
    <span class="hljs-keyword">return</span> vnode.el;
&#125;

<span class="hljs-comment">/**
 * 添加新的虚拟DOM，删除老得DOM
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el 可能是真是dom,也可能是虚拟DOM
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 新的虚拟DOM
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">el, vnode</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (el.nodeType === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">//是真是DOM</span>
        <span class="hljs-keyword">const</span> parentNode = el.parentNode;
        <span class="hljs-keyword">const</span> elem = createElem(vnode);
        <span class="hljs-comment">//添加</span>
        parentNode.insertBefore(elem, el.nextSibling);
        <span class="hljs-comment">//删除老得</span>
        parentNode.removeChild(el);
        <span class="hljs-keyword">return</span> elem;
    &#125; <span class="hljs-keyword">else</span> &#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            