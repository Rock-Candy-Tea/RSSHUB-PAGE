
---
title: 'VUE 状态变化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726b40b43d0147e48819b1810080f75c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:11:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726b40b43d0147e48819b1810080f75c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726b40b43d0147e48819b1810080f75c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>Data通过Observer转换成getter/setter形式追踪数据变化。</li>
<li>浏览器从Watcher读取数据，Watcher触发getter，getter将Watcher收集到依赖。注意，这里的Watcher是组件，不是一个具体的DOM节点。</li>
<li>数据发生变化，触发setter，通知Dep中的依赖(Watcher)。</li>
<li>Watcher收到通知，向浏览器发送通知，可能触发视图更新，也可能触发用户的回调。</li>
</ol>
<p><strong>defineReactive</strong></p>
<p>Object可以通过Object.defineProperty将属性转化成getter/setter 的形式来追踪变化。读取数据时会触发getter,修改数据时会触发setter。</p>
<p>需要在getter中收集有哪些依赖使用了数据，当setter被触发时，去通知getter中收集的依赖数据发生了变化。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">data, key, val</span>) </span>&#123;
  <span class="hljs-keyword">let</span> dep = <span class="hljs-keyword">new</span> Dep();

  <span class="hljs-built_in">Object</span>.defineProperty(data, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 收集依赖</span>
      dep.depend();
      <span class="hljs-keyword">return</span> val;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newVal</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (val === newVal) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      val = newVal;
      <span class="hljs-comment">// 触发依赖</span>
      dep.notify();
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Watcher</strong></p>
<p>watcher的原理是先把自己设置到全局唯一的指定位置（例如window.target），然后读取数据。因为读取了数据，所以会触发这个数据的getter。接着，在getter中就会从全局唯一的哪个位置读取当前正在读取数据的watcher，并把这个watcher收集到Dep中去。通过这样的方式watcher可以主动去订阅任意一个数据的变化。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, expOrFn, cb</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.vm = vm;
    <span class="hljs-comment">// 执行this.getter()，就可以读取data.a.b.c的内容</span>
    <span class="hljs-built_in">this</span>.getter = parsePath(expOrFn);
    <span class="hljs-built_in">this</span>.cb = cb;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get();
  &#125;

  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.target = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> value = <span class="hljs-built_in">this</span>.getter.call(<span class="hljs-built_in">this</span>.vm, <span class="hljs-built_in">this</span>.vm);
    <span class="hljs-built_in">window</span>.target = <span class="hljs-literal">undefined</span>;
    <span class="hljs-keyword">return</span> value;
  &#125;

  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> oldValue = <span class="hljs-built_in">this</span>.value;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get();
    <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, <span class="hljs-built_in">this</span>.value, oldValue);
  &#125;
&#125;

<span class="hljs-comment">// Watcher的一个使用方式</span>
vm.$watch(<span class="hljs-string">"a.b.c"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newVal, oldVal</span>) </span>&#123;
  <span class="hljs-comment">// 做点什么</span>
&#125;);

<span class="hljs-comment">// 解析路径</span>
<span class="hljs-keyword">const</span> bailRE = <span class="hljs-regexp">/[^\w.$]/</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parsePath</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (bailRE.test(path)) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">const</span> segments = path.split(<span class="hljs-string">"."</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < segments.length; i++) &#123;
      <span class="hljs-keyword">if</span> (!obj) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;

      obj = obj[segments[i]];
    &#125;
    <span class="hljs-keyword">return</span> obj;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Dep</strong></p>
<p>收集依赖需要为依赖找一个存储依赖的地方，为此我们创建了Dep，它用来收集依赖、删除依赖和向依赖发送消息等</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.subs = [];
  &#125;

  <span class="hljs-function"><span class="hljs-title">addSub</span>(<span class="hljs-params">sub</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.subs.push(sub);
  &#125;

  <span class="hljs-function"><span class="hljs-title">removeSub</span>(<span class="hljs-params">sub</span>)</span> &#123;
    remove(<span class="hljs-built_in">this</span>.subs, sub);
  &#125;

  <span class="hljs-function"><span class="hljs-title">depend</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.target) &#123;
      <span class="hljs-built_in">this</span>.addSub(<span class="hljs-built_in">window</span>.target); <span class="hljs-comment">// watcher</span>
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> subs = <span class="hljs-built_in">this</span>.subs.slice();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < subs.length; i++) &#123;
      subs[i].update();
    &#125;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove</span>(<span class="hljs-params">arr, item</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (arr.length) &#123;
    <span class="hljs-keyword">const</span> index = arr.indexOf(item);
    <span class="hljs-keyword">if</span> (index > -<span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> arr.splice(index, <span class="hljs-number">1</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            