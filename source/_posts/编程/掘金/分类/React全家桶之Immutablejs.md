
---
title: 'React全家桶之Immutable.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95e2dc5455bb4cbb82b13244f99533a0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:22:14 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95e2dc5455bb4cbb82b13244f99533a0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 React 开发中 React 强调开发者无时无刻去关注 <strong>数据的纯度</strong>
无论是类组件中的 state 还是 redux 中的 state</p>
<p>JavaScript 中的对象一般是可变的（Mutable），因为使用了引用赋值，新的对象简单的引用了原始对象，改变新的对象将影响到原始对象。如 <code>foo=&#123;a: 1&#125;; bar=foo; bar.a=2</code> 此时 <code>foo.a</code> 也被改成了 <code>2</code>。虽然这样做可以节约内存，但当应用复杂后，这就造成了非常大的隐患，Mutable 带来的优点变得得不偿失。为了解决这个问题，一般的做法是使用 shallowCopy（浅拷贝）或 deepCopy（深拷贝）来避免被修改，但这样做造成了 CPU 和内存的浪费。</p>
<p>上述问题等同于在A组件中修改公共状态 在B组件中同样也被修改了</p>
<p>遇到这种问题如何解决呢?</p>
<p>ES6中  (...)扩展运算符 & Object.assign
ES5中  Object.freeze()</p>
<p>但是这种浅层拷贝有什么问题呢?
答:一般没有 除非对象过于庞大 才会带来性能问题以及内存浪费</p>
<h1 data-id="heading-0">可不可以做的更好?</h1>
<p>可以! 使用 ImmutableJS 进行性能优化</p>
<h2 data-id="heading-1">Immutable 优点</h2>
<ol>
<li>
<p>Immutable 降低了 Mutable 带来的复杂度</p>
</li>
<li>
<p>节省内存</p>
</li>
</ol>
<p>Immutable.js 使用了 Structure Sharing 会尽量复用内存，甚至以前使用的对象也可以再次被复用。没有被引用的对象会被垃圾回收。</p>
<ol start="3">
<li>拥抱函数式编程</li>
</ol>
<p>Immutable 本身就是函数式编程中的概念，纯函数式编程比面向对象更适用于前端开发。因为只要输入一致，输出必然一致，这样开发的组件更易于调试和组装。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95e2dc5455bb4cbb82b13244f99533a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Immutable 本意为不可改变的 这个库弥补了 Javascript 没有不可变数据结构的问题 那他是如何做到不可变的呢?</p>
<p>ImmutableJS核心概念就一个 只要修改了对象，就会返回一个新的对象，旧的对象不会发生改变；且新的对象会尽可能利用原来对象的结构 即<strong>结构共享</strong></p>
<p>同时利用了数据结构中的16叉树最大程度保证了树的深度问题 减少更新的结构</p>
<h1 data-id="heading-2">ImmutableJS 基本使用</h1>
<h2 data-id="heading-3">ImutableJS常见API</h2>
<p>ImutableJS数据结构</p>
<ul>
<li>Map：键值对集合，对应于 Object，ES6 也有专门的 Map 对象</li>
<li>List：有序可重复的列表，对应于 Array</li>
<li>Set：无序且不可重复的列表</li>
</ul>
<p>JavaScript和ImmutableJS直接的转换</p>
<ul>
<li>
<p>对象转换成Immutable对象：Map</p>
</li>
<li>
<p>数组转换成Immutable数组：List</p>
</li>
<li>
<p>深层转换：fromJS</p>
</li>
<li>
<p>Immutable类型转换js：toJS()</p>
</li>
</ul>
<p>ImmutableJS的基本操作</p>
<ul>
<li>
<p>修改数据：set</p>
</li>
<li>
<p>获取数据：get</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> im = Immutable;
     <span class="hljs-keyword">const</span> info = &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'xiaoming'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
      <span class="hljs-attr">friends</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'xiaohong'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">32</span>
      &#125;
    &#125;

    <span class="hljs-comment">// 对上方对象进行转化时</span>
    <span class="hljs-keyword">const</span> infoIm = im.Map(info)
    <span class="hljs-keyword">const</span> obj = infoIm;
    <span class="hljs-comment">// 修改时需要用set进行修改 同时这里不会主动改这里对infoIm 而是生成一个新的对象</span>
    <span class="hljs-keyword">const</span> infoIm2 = infoIm.set(<span class="hljs-string">"name"</span>, <span class="hljs-string">'小明'</span>)
    <span class="hljs-built_in">console</span>.log(infoIm2);
    <span class="hljs-comment">// 通过get来取数据</span>
    <span class="hljs-built_in">console</span>.log(obj.get(<span class="hljs-string">'name'</span>));
    <span class="hljs-built_in">console</span>.log(infoIm2.get(<span class="hljs-string">'name'</span>));
    
    <span class="hljs-comment">// list</span>
    <span class="hljs-keyword">const</span> num = [<span class="hljs-string">'1'</span>, <span class="hljs-string">'2'</span>, <span class="hljs-string">'3'</span>, <span class="hljs-string">'4'</span>];

    <span class="hljs-keyword">const</span> numIm = im.List(num)

    <span class="hljs-built_in">console</span>.log(numIm);

    <span class="hljs-keyword">const</span> arr = numIm.set(<span class="hljs-number">0</span>, <span class="hljs-number">11</span>)
    <span class="hljs-built_in">console</span>.log(numIm.get(<span class="hljs-number">0</span>));
    <span class="hljs-built_in">console</span>.log(arr.get(<span class="hljs-number">0</span>));

    <span class="hljs-built_in">console</span>.log(infoIm.get(<span class="hljs-string">'friends'</span>)); <span class="hljs-comment">// &#123;name: "xiaohong", age: 32&#125; 普通对象</span>

    <span class="hljs-comment">// 传入js对象或数组 转化为 Immutable类型</span>
    <span class="hljs-keyword">const</span> infoIm3 = im.fromJS(info)
    <span class="hljs-built_in">console</span>.log(infoIm3.get(<span class="hljs-string">'friends'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">ImutableJS 结合 Redux使用</h2>
<p>yarn add immutable</p>
<p>由于Redux有且仅有一个store 但是可以拆分为多个reducer 我用一个其中一个reducer进行举例</p>
<p>修改前的Reducer</p>
<pre><code class="hljs language-js copyable" lang="js">
    <span class="hljs-keyword">import</span> &#123; CONSTANTS &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./constants"</span>;
    <span class="hljs-comment">// 创建默认状态</span>
    <span class="hljs-keyword">const</span> defaultState = <span class="hljs-built_in">Map</span>&#123;
    <span class="hljs-attr">topBanners</span>: [],
    &#125;;
    <span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state = defaultState, action</span>) =></span> &#123;
        <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> CONSTANTS:
          <span class="hljs-keyword">return</span> &#123;...state, action.data&#125;
        <span class="hljs-attr">default</span>:
          <span class="hljs-keyword">return</span> state;
        &#125;&#125;;
        
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> reducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合ImutableJS后的Reducer</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">import</span> &#123; <span class="hljs-built_in">Map</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"immutable"</span>;
    <span class="hljs-keyword">import</span> &#123; CONSTANTS &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./constants"</span>;
    <span class="hljs-comment">// 将 defaultState 转换成 Map类型</span>
    <span class="hljs-keyword">const</span> defaultState = <span class="hljs-built_in">Map</span>(&#123;
    <span class="hljs-attr">topBanners</span>: [],
    &#125;);
    <span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state = defaultState, action</span>) =></span> &#123;
        <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> CONSTANTS:
          <span class="hljs-comment">// 调用Map对象中的set方法</span>
          <span class="hljs-keyword">return</span> state.set(<span class="hljs-string">"data"</span>, action.data);
        <span class="hljs-keyword">default</span>:
          <span class="hljs-keyword">return</span> state;
        &#125;&#125;;
        
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> reducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在主reducer进行合并</p>
<p>这里要说明一点: immutablejs里面的Map进行包裹 而 Redux 中的 combineReducers 源码里面实现过程是通过Object.key方式将每个模块的小reduer进行传递 如果这时候拿Map进行包裹肯定不是Map想要的数据结构</p>
<p>yarn add redux-immutable</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">import</span> &#123; combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-immutable"</span>;
    <span class="hljs-keyword">import</span> &#123; reducer <span class="hljs-keyword">as</span> recommend &#125; <span class="hljs-keyword">from</span><span class="hljs-string">"@v/xxx/components/xxxxx/store/index"</span>;
    <span class="hljs-keyword">const</span> mergeReducer = combineReducers(&#123;
        recommend,
    &#125;);
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> mergeReducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结</h2>
<p>Immutable 可以给应用带来极大的性能提升，但是由于侵入性较强 是否使用必须考虑项目复杂程度</p></div>  
</div>
            