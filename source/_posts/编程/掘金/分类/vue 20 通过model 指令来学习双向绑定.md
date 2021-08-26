
---
title: 'vue 2.0 通过model 指令来学习双向绑定'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afea0ceae1ab4d1b88d51b145e962623~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 07:00:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afea0ceae1ab4d1b88d51b145e962623~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这里通过讲解model 指令的实现来学习双向绑定的实现过程</h3>
<h4 data-id="heading-1">首先将整个实现的思路顺下。</h4>
<ul>
<li><strong>在初始化中，首先 new一个vue 实例，通过调用的过程我们可以知道，</strong></li>
</ul>
<ol>
<li>先将参数options 对象存为$options</li>
<li>要想实现双向绑定，需要将传过来的data 参数进行 observe</li>
<li>然后将data 中的值绑定到当前实例上</li>
<li>然后根据传入的el 参数，编译模板</li>
</ol>
<ul>
<li><strong>接着探讨编译模板的过程，我们这里做一个简单版的，用fragment来实现，实际上使用的是ATS</strong></li>
</ul>
<ol>
<li>调用函数 让节点变为 fragment</li>
<li>编译模板</li>
<li>将编译好的模板挂载到dom</li>
</ol>
<ul>
<li><strong>第二步骤中的1和3.思路比较简单，这里重点讲第二个编译模板。这里也只是简单实现，不使用递归。</strong></li>
</ul>
<ol>
<li>通过根节点，获取子节点，然后遍历子节点。遍历过程中根据节点的nodeType 不同，来处理元素节点，和文本节点</li>
<li>元素节点的处理：获取元素节点的attributes 值， 然后遍历它。遍历过程找到v-model 这个指令</li>
<li>文本节点的处理：通过正则获取&#123;&#123;&#125;&#125;里面的值。</li>
</ol>
<ul>
<li><strong>找到v-model 的指令后，获取绑定的值 比如v-model="a" 中的a,对这个找到的值做处理</strong></li>
</ul>
<ol>
<li>对找到的a添加 watcher</li>
<li>获取a这个属性的值，并给绑定的元素赋值</li>
<li>给input 添加监听事件，来实时更新最新的输入值</li>
</ol>
<ul>
<li><strong>文本节点的处理，找到&#123;&#123;&#125;&#125;中的值后，通过添加watcher 来添加处理</strong></li>
</ul>
<h4 data-id="heading-2">下面是实现过程中的代码粘贴，有一部分代码参考之前讲过的 数据响应式原理，<a href="https://juejin.cn/post/6994587064398250015" target="_blank" title="https://juejin.cn/post/6994587064398250015">juejin.cn/post/699458…</a></h4>
<p>代码结构如下图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afea0ceae1ab4d1b88d51b145e962623~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210825225558.png" loading="lazy" referrerpolicy="no-referrer">
index.html</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    你好&#123;&#123;a&#125;&#125;
    <input v-model="a" type="text">
    <ul>
      <li>a</li>
      <li>b</li>
      <li>c</li>
    </ul>
    <button onclick="add()">点我加1</button>
  </div>
  <script src='/xuni/bundle.js'></script>
  <script>
    var vm = new Vue(&#123;
      el: 'app',
      data :&#123;
        a:'33'
      &#125;
    &#125;)
    function add () &#123;
      vm._data.a++
    &#125;
    console.log(vm)
  </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Compile <span class="hljs-keyword">from</span> <span class="hljs-string">'./Compile'</span>
<span class="hljs-keyword">import</span> &#123; observe &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./initdata/data/observer'</span>
<span class="hljs-keyword">import</span> Watcher <span class="hljs-keyword">from</span> <span class="hljs-string">'./initdata/data/watcher.js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 把参数options 对象存为$options</span>
    <span class="hljs-built_in">this</span>.$options = options || &#123;&#125;
    <span class="hljs-built_in">this</span>._data = options.data || <span class="hljs-literal">undefined</span>;
    observe(<span class="hljs-built_in">this</span>._data)
    <span class="hljs-built_in">this</span>._initData()
    <span class="hljs-keyword">new</span> Compile(options.el, <span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">_initData</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>._data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(self, key,&#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> self._data[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
          self._data[key] = newVal
        &#125;
      &#125;)
    &#125;)
  &#125;
&#125;

<span class="hljs-built_in">window</span>.Vue = Vue

<span class="copy-code-btn">复制代码</span></code></pre>
<p>compile.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Watcher <span class="hljs-keyword">from</span> <span class="hljs-string">'./initdata/data/watcher.js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compile</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">el, vue</span>) &#123;
    <span class="hljs-built_in">this</span>.$vue = vue
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#'</span>+el)
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$el) &#123;
      <span class="hljs-comment">// 如果传入了挂载点 调用函数 让节点变为 fragment  实际上用的AST 这里就是轻量级的</span>
      <span class="hljs-keyword">let</span> fragment = <span class="hljs-built_in">this</span>.node2Fragment(<span class="hljs-built_in">this</span>.$el)
      <span class="hljs-comment">// 编译模板</span>
      <span class="hljs-built_in">this</span>.compile(fragment)
      <span class="hljs-comment">// 将编译完的模板上树</span>
      <span class="hljs-built_in">this</span>.$el.appendChild(fragment)
    &#125;

  &#125;
  node2Fragment (el) &#123;
    <span class="hljs-built_in">console</span>.log(el)
    <span class="hljs-keyword">var</span> fragment = <span class="hljs-built_in">document</span>.createDocumentFragment();

    <span class="hljs-keyword">var</span> child 
    <span class="hljs-comment">// 让所有的dom 都进入 fragment</span>
    <span class="hljs-keyword">while</span> (child = el.firstChild) &#123;
      fragment.appendChild(child)
    &#125;
    <span class="hljs-keyword">return</span> fragment
  &#125;
  compile (el) &#123;
    <span class="hljs-keyword">var</span> childNodes = el.childNodes;
    <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> reg = <span class="hljs-regexp">/\&#123;\&#123;(.*)\&#125;\&#125;/</span>

    childNodes.forEach(<span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">var</span> text = node.textContent;
      <span class="hljs-keyword">if</span> (node.nodeType==<span class="hljs-number">1</span>) &#123;
        self.compileElement(node)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (node.nodeType==<span class="hljs-number">3</span> && reg.test(text)) &#123;
        <span class="hljs-keyword">let</span> name = text.match(reg)[<span class="hljs-number">1</span>]
        self.compileText(node, name)
      &#125;
    &#125;)
  &#125;
  compileElement (node) &#123;
    <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 这里的方便之处是在 操作真正的属性列表  结构比较像虚拟节点</span>
    <span class="hljs-keyword">var</span> nodeAttrs = node.attributes;
    [].slice.call(nodeAttrs).forEach(<span class="hljs-function"><span class="hljs-params">attr</span> =></span> &#123;
      <span class="hljs-comment">// 这里分析指令  不用之前的虚拟dom 是因为这样比较简单， 思量逻辑是一致的</span>
      <span class="hljs-keyword">var</span> attrName = attr.name;
      <span class="hljs-keyword">var</span> value = attr.value;
      <span class="hljs-comment">// 指令是从 v-开头的</span>
      <span class="hljs-keyword">var</span> dir = attrName.substring(<span class="hljs-number">2</span>)
      <span class="hljs-comment">// 看看是不是指令</span>
      <span class="hljs-keyword">if</span> (attrName.indexOf(<span class="hljs-string">'v-'</span>) == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 这里去判断是哪个指令</span>
        <span class="hljs-keyword">if</span> (dir==<span class="hljs-string">'model'</span>) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发现是指令'</span> + dir)
          
          <span class="hljs-comment">// 对指令添加watch</span>
          <span class="hljs-keyword">new</span> Watcher(self.$vue, value, <span class="hljs-function"><span class="hljs-params">newVal</span> =></span> &#123;
            node.value = newVal
          &#125;)
          <span class="hljs-comment">// 获取该值，赋值</span>
          <span class="hljs-keyword">var</span> val = <span class="hljs-built_in">this</span>.getVueVal(<span class="hljs-built_in">this</span>.$vue, value)
          node.value = val
          <span class="hljs-comment">// 添加input 事件来触发</span>
          node.addEventListener(<span class="hljs-string">'input'</span>,<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> newValue = e.target.value
            <span class="hljs-built_in">console</span>.log(newValue)
            self.setVueVal(self.$vue, value, newValue)
          &#125;)
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (dir ==<span class="hljs-string">'if'</span>) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发现是指令'</span> + dir)
        &#125;
      &#125;

    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node, name</span>)</span> &#123;
    node.textContent = <span class="hljs-built_in">this</span>.getVueVal(<span class="hljs-built_in">this</span>.$vue, name)
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.$vue, name, <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
      node.textContent = value
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">getVueVal</span>(<span class="hljs-params">vue, name</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(vue,name)
    <span class="hljs-keyword">let</span> val = vue._data
    <span class="hljs-keyword">let</span> keys = name.split(<span class="hljs-string">'.'</span>)
    keys.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      val = val[key]
    &#125;)
    <span class="hljs-keyword">return</span> val
  &#125;
  <span class="hljs-function"><span class="hljs-title">setVueVal</span>(<span class="hljs-params">vue, name, value</span>)</span> &#123;
    
    <span class="hljs-keyword">let</span> val = vue
    <span class="hljs-keyword">let</span> keys = name.split(<span class="hljs-string">'.'</span>)
    keys.forEach(<span class="hljs-function">(<span class="hljs-params">key,index</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (index==keys.length-<span class="hljs-number">1</span>) &#123;
        val[key] = value
      &#125;<span class="hljs-keyword">else</span> &#123;
        val = val[key]
      &#125;
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引用的响应式代码就不粘贴了，可以参考 <a href="https://juejin.cn/post/6994587064398250015" target="_blank" title="https://juejin.cn/post/6994587064398250015">juejin.cn/post/699458…</a></p></div>  
</div>
            