
---
title: '实现简单版Vue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=230'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:43:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=230'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第8天，活动详情查看： 8月更文挑战” <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">juejin.cn/post/698796…</a></p>
<h3 data-id="heading-0">介绍</h3>
<p>本文目的是实现一个简易版本的Vue用以学习，也是对从网课学习的总结和复习。其中内容仅为简易实现，多有不足之处，请多多交流。</p>
<h3 data-id="heading-1">内容拆分</h3>
<ul>
<li>
<p>数据响应式处理</p>
<ul>
<li>数据拦截</li>
<li>数组和对象的区分处理</li>
<li>数据代理</li>
</ul>
</li>
<li>
<p>模板编译</p>
<ul>
<li>对文本的处理</li>
<li>对元素特性(即指令)的处理</li>
</ul>
</li>
<li>
<p>页面渲染</p>
<ul>
<li>依赖收集</li>
<li>创建watcher实例</li>
<li>触发更新</li>
</ul>
</li>
</ul>
<h3 data-id="heading-2">项目测试</h3>
<p>本文目的仅为简单版Vue实现，用于学习总结。所以采用html引入js方式进行测试即可。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--主要代码--></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;counter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">k-text</span>=<span class="hljs-string">"counter"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">k-html</span>=<span class="hljs-string">"desc"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./kvue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> KVue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">counter</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">desc</span>: <span class="hljs-string">'<p>村长<span style="color:red">真棒</span></p>'</span>
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">onclick</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
        &#125;
      &#125;,
    &#125;)
    <span class="hljs-comment">// 暂时可不放开</span>
    <span class="hljs-comment">/*setInterval(() => &#123;
       app.counter++
    &#125;, 1000);*/</span>
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">vue实现</h2>
<h3 data-id="heading-4">数据响应式处理</h3>
<h4 data-id="heading-5">数据拦截</h4>
<p>有了解过Vue框架原理的同学都知道，vue2.x中数据拦截使用的是Object.defineProperty方法，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj,key,val</span>)</span>&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(obj,key,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> val;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(newVal != val)&#123;
        val = newVal;
      &#125;
    &#125;
  &#125;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>属性拦截</strong></p>
<p>Object.defineProperty方法的三个参数：</p>
<ul>
<li>
<p>obj 要拦截的数据对象</p>
</li>
<li>
<p>key 要给数据对象添加的属性</p>
</li>
<li>
<p>&#123;xxx&#125; 属性描述器</p>
<ul>
<li>属性描述器分为两种：存取描述器和数据描述器，都是对象，此处为存取描述器。</li>
</ul>
</li>
</ul>
































<table><thead><tr><th></th><th>configurable</th><th>enumerable</th><th>value</th><th>writable</th><th>get</th><th>set</th></tr></thead><tbody><tr><td>数据描述符</td><td>可以</td><td>可以</td><td>可以</td><td>可以</td><td>不可以</td><td>不可以</td></tr><tr><td>存取描述符</td><td>可以</td><td>可以</td><td>不可以</td><td>不可以</td><td>可以</td><td>可以</td></tr></tbody></table>
<ul>
<li>此处最重要的属性为get和set属性。相当于给obj设置了key属性，当访问obj.key时触发拦截操作，执行的是get方法；obj.key的值发生变化时执行的是set操作。</li>
<li>因为知道了数据被读取和变化时的地方，所以我们可以在这些地方加入一些其他的操作。</li>
</ul>
<p><strong>闭包写法</strong></p>
<p>在此处利用了闭包的写法。通过函数作用域内的某个函数将局部变量保留出去，即为闭包。</p>
<ul>
<li>局部作用域：val被保存在defineReactive函数中作用域</li>
<li>通过defineProperty的get方法将val暴露出去</li>
</ul>
<p>闭包中的局部变量不会被释放，一直保存在内存中。所以如果对值做了修改就会发生变化。</p>
<h4 data-id="heading-6">数组和对象的区分处理</h4>
<p>相对于普通类型数据，进行拦截时不需要过多考虑，直接返回即可。而对于数组和对象的数据，依据不同的处理方法，需要做不同的处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
      <span class="hljs-comment">// xxx</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj</span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      defineReactive(obj, key, obj[key])
    &#125;)
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">obj</span>)</span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj != <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-keyword">return</span> obj;
  &#125;
  <span class="hljs-keyword">new</span> Observer(obj);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对象嵌套问题</strong></p>
<p>考虑到数据的值可能是嵌套对象，所以需要在数据拦截时进行递归处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj,key,val</span>)</span>&#123;
  observe(obj);
  <span class="hljs-built_in">Object</span>.defineProperty(obj,key,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> val;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(newVal != val)&#123;
        observe(newVal);
        val = newVal;
      &#125;
    &#125;
  &#125;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>observe(obj)：当数据不为对象类型时，observe方法直接将数据返回，继而执行下面的数据拦截操作；当数据是对象类型时，会执行Observer类的操作去区分数组和对象，分别进行处理</li>
<li>observe(newVal)：此处的设置主要是考虑到给数据直接赋值对象的操作，需要将新对象进行数据响应式之后赋给数据。</li>
</ul>
<h4 data-id="heading-7">数据代理</h4>
<p>这一步的操作主要是用于可以通过Vue实例直接访问data中的数据，形如：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fthis.xxx" target="_blank" rel="nofollow noopener noreferrer" title="http://this.xxx" ref="nofollow noopener noreferrer">this.xxx</a>。经过了上一步observe的操作之后，访问data中数据需要通过this.$data.xxx形式访问，比较麻烦。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.keys(vm.$data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(vm, key, &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> vm.$data[key]
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">v</span>)</span> &#123;
        vm.$data[key] = v;
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">模板编译</h3>
<p>对于vue模板语法和指令等，很多人都是了解的，但是对于背后的逻辑实现，却是一知半解。对于模板的编译需要实现一个编译器来进行这些操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compile</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">el, vm</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$vm = vm;
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">document</span>.querySelector(el);
    <span class="hljs-comment">// 执行编译</span>
    <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.$el);
  &#125;
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    el.childNodes.forEach(<span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (node.nodeType === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// element元素</span>
        <span class="hljs-comment">// 遍历元素特性</span>
        <span class="hljs-built_in">this</span>.compileElement(node);
        <span class="hljs-comment">// 递归</span>
        <span class="hljs-keyword">if</span> (node.childNodes.length > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-built_in">this</span>.compile(node);
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isInter(node)) &#123;
        <span class="hljs-comment">// text文本</span>
        <span class="hljs-comment">// 插值表达式</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125;
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">对文本的处理</h4>
<p>对文本的处理，首先需要辨别插值表达式，可以通过一个正则来区分。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">isInter</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span> && <span class="hljs-regexp">/&#123;&#123;(.*)&#125;&#125;/</span>.test(node.textContent);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后对于插值表达式的文本替换，基于上文正则表达式可以获得插值表达式中的变量名为RegExp.$1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
    node.textContent = <span class="hljs-built_in">this</span>.$vm[<span class="hljs-built_in">RegExp</span>.$1];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">对元素特性(即指令)的处理</h4>
<p>对元素的处理，主要是对元素特性的处理。对特性attributes进行遍历。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">compileElement</span>(<span class="hljs-params">node</span>)</span> &#123;
  <span class="hljs-keyword">const</span> attrs = node.attributes;
  <span class="hljs-built_in">Array</span>.from(attrs).forEach(<span class="hljs-function"><span class="hljs-params">attr</span> =></span> &#123;
    <span class="hljs-keyword">const</span> attrName = attr.name;
    <span class="hljs-keyword">const</span> attrExp = attr.value;
    <span class="hljs-keyword">if</span> (attrName.startsWith(<span class="hljs-string">'k-'</span>)) &#123;
      <span class="hljs-comment">// 对指令的处理</span>
      <span class="hljs-keyword">const</span> dir = attrName.substring(<span class="hljs-number">2</span>);
      <span class="hljs-built_in">this</span>[dir] && <span class="hljs-built_in">this</span>[dir](node, attrExp);
    &#125;
  &#125;)
&#125;
<span class="hljs-comment">// k-text</span>
<span class="hljs-function"><span class="hljs-title">text</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
  node.textContent = <span class="hljs-built_in">this</span>.$vm[exp]
&#125;
<span class="hljs-comment">// k-html</span>
<span class="hljs-function"><span class="hljs-title">html</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
  node.innerHTML = <span class="hljs-built_in">this</span>.$vm[exp];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">两步结合</h3>
<p>将前两步结合一起。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KVue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-built_in">this</span>.$data = options.data;
    <span class="hljs-comment">// 1.响应式</span>
    observe(<span class="hljs-built_in">this</span>.$data);
    <span class="hljs-comment">// 1.1  代理：用户可以通过KVue实例直接访问data中数据</span>
    proxy(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// 2.编译:传入宿主元素el和组件实例this</span>
    <span class="hljs-keyword">new</span> Compile(options.el, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">页面渲染</h3>
<p>在Vue中数据与Dep、Watcher的对应关系是：1个数据 => 1个Dep => n个Watcher</p>
<h4 data-id="heading-13">依赖收集</h4>
<p>根据上文的对应关系，Dep中存储着多个Watcher实例，所以应该是数组形式。同时Dep应该有一个添加方法和触发按更新的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 存储所有的watcher</span>
    <span class="hljs-built_in">this</span>.deps = [];
  &#125;
  <span class="hljs-function"><span class="hljs-title">addDep</span>(<span class="hljs-params">watcher</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.deps.push(watcher);
  &#125;
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.deps.forEach(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> dep.update())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">创建watcher实例</h4>
<p>Watcher中需要有一个更新方法，另外需要注意的就是触发依赖筹集的地方，在下一步综合述说。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, key, fn</span>)</span> &#123;
    <span class="hljs-comment">// fn : 更新函数</span>
    <span class="hljs-built_in">this</span>.vm = vm;
    <span class="hljs-built_in">this</span>.key = key;
    <span class="hljs-built_in">this</span>.fn = fn;

    <span class="hljs-comment">// 触发依赖收集：读取一次key</span>
    Dep.target = <span class="hljs-built_in">this</span>;  <span class="hljs-comment">// 保存当前实例</span>
    <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key];  <span class="hljs-comment">// 读取一次key，触发getter</span>
    Dep.target = <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.fn.call(<span class="hljs-built_in">this</span>.vm, <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">触发更新</h3>
<p>这一步的实质就是对Dep和Watcher的应用。</p>
<h4 data-id="heading-16">Dep应用</h4>
<p>首先需要确定dep实例应该被创建的位子在哪里，由 1个数据 => 1个Dep 的关系可以确定，dep创建应与数据拦截在一处。</p>
<pre><code class="hljs language-js copyable" lang="js">unction <span class="hljs-function"><span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, val</span>)</span> &#123;
  observe(val);
  <span class="hljs-comment">//  创建对应的Dep实例</span>
  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep();
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get'</span>, key, val);
      <span class="hljs-comment">//建立映射关系</span>
      <span class="hljs-comment">// Dep.target就是watcher实例，自行触发getter并将自身填入dep中</span>
      Dep.target && dep.addDep(Dep.target);
      <span class="hljs-keyword">return</span> val;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set'</span>, key, newVal);
      <span class="hljs-keyword">if</span> (newVal != val) &#123;
        <span class="hljs-comment">// 新设置的值也可能是对象：解决直接给已有属性赋值对象问题</span>
        observe(newVal)
        val = newVal;
        dep.notify();
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>const dep = new Dep()</li>
</ul>
<p>创建和数据对应的dep实例</p>
<ul>
<li>dep.notify()</li>
</ul>
<p>这里是对数据的属性值进行修改后，需要对应的dep实例通知相关Watcher实例进行更新。</p>
<ul>
<li>Dep.target && dep.addDep(Dep.target)</li>
</ul>
<p>这里是需要配合Watcher中的一段代码进行解释。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 触发依赖收集：读取一次key</span>
Dep.target = <span class="hljs-built_in">this</span>;  <span class="hljs-comment">// 保存当前实例</span>
<span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key];  <span class="hljs-comment">// 读取一次key，触发getter</span>
Dep.target = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Dep.target即为Watcher实例，下一步读取数据的key时会触发数据拦截的get方法，所以在这里通过dep实例的addDep方法将Watcher实例填充进入数据对应的dep数组中。之后再讲Dep.target清空为null。</p>
<h4 data-id="heading-17">Watcher应用</h4>
<p>Watcher和页面上应用的动态数据一一对应，所以创建Watcher实例的地方最好是在编译模板里。结合上文中模板的编译的处理步骤，我们可以建立一个统一的update方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">node, exp, dir</span>)</span> &#123;
  <span class="hljs-comment">// 获取实操函数</span>
  <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>[dir + <span class="hljs-string">'Updater'</span>];
  <span class="hljs-comment">// 初始化</span>
  fn && fn(node, <span class="hljs-built_in">this</span>.$vm[exp]);
  <span class="hljs-comment">// 更新</span>
  <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.$vm, exp, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
    fn && fn(node, val);
  &#125;);
&#125;

<span class="hljs-comment">// k-text</span>
<span class="hljs-function"><span class="hljs-title">text</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.update(node, exp, <span class="hljs-string">'text'</span>)
&#125;
<span class="hljs-function"><span class="hljs-title">textUpdater</span>(<span class="hljs-params">node, val</span>)</span> &#123;
  node.textContent = val;
&#125;
<span class="hljs-comment">// k-html</span>
<span class="hljs-function"><span class="hljs-title">html</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.update(node, exp, <span class="hljs-string">'html'</span>)
&#125;
<span class="hljs-function"><span class="hljs-title">htmlUpdater</span>(<span class="hljs-params">node, val</span>)</span> &#123;
  node.innerHTML = val;
&#125;
<span class="hljs-comment">// 将插值表达式编译为文本</span>
<span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.update(node, <span class="hljs-built_in">RegExp</span>.$1, <span class="hljs-string">'text'</span>)
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，可以进行项目的调试，基本可以实现效果。</p></div>  
</div>
            