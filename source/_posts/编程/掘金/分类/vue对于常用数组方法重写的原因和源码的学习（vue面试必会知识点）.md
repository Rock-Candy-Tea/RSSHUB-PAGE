
---
title: 'vue对于常用数组方法重写的原因和源码的学习（vue面试必会知识点）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4072'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:34:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=4072'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>由于Object.defineproperty方法无法监听到数组和对象内的新增变化，所以vue2重写了常用的数组方法来使数组更新时能触发页面更新，对于对象的更新则采用this.$set的方法，使得对象更新时同时触发视图更新，这个之后再谈，今天我们来看一下vue内部是怎么重写常用的数组方法的。
1.vue2重写了哪些数组方法？
如下图，一共7中常用数组方法（来自源码）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> methodsToPatch = [
    <span class="hljs-string">'push'</span>,
    <span class="hljs-string">'pop'</span>,
    <span class="hljs-string">'shift'</span>,
    <span class="hljs-string">'unshift'</span>,
    <span class="hljs-string">'splice'</span>,
    <span class="hljs-string">'sort'</span>,
    <span class="hljs-string">'reverse'</span>
  ];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就意味着，如果使用这7种以外的数组方法更新数组，且需要视图也更新，则需要使用this.$set。
2.怎么重写数组方法
在重写之前先进行了以下两个步骤:</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> arrayProto = <span class="hljs-built_in">Array</span>.prototype;
  <span class="hljs-keyword">var</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(arrayProto);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>arrayProto用来存储原生js的数组方法，用于接下来的遍历，arrayMethods定义一个空对象用来存放vue重写的数组方法以避免污染Array.prototype上的数组方法。
接下来是重写数组方法：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/**
   * Intercept mutating methods and emit events
   */</span>
  methodsToPatch.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">method</span>) </span>&#123;
    <span class="hljs-comment">// cache original method</span>
    <span class="hljs-keyword">var</span> original = arrayProto[method];
    def(arrayMethods, method, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mutator</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> args = [], len = <span class="hljs-built_in">arguments</span>.length;
      <span class="hljs-keyword">while</span> ( len-- ) args[ len ] = <span class="hljs-built_in">arguments</span>[ len ];

      <span class="hljs-keyword">var</span> result = original.apply(<span class="hljs-built_in">this</span>, args);
      <span class="hljs-keyword">var</span> ob = <span class="hljs-built_in">this</span>.__ob__;
      <span class="hljs-keyword">var</span> inserted;
      <span class="hljs-keyword">switch</span> (method) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>:
          inserted = args;
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>:
          inserted = args.slice(<span class="hljs-number">2</span>);
          <span class="hljs-keyword">break</span>
      &#125;
      <span class="hljs-keyword">if</span> (inserted) &#123; ob.observeArray(inserted); &#125;
      <span class="hljs-comment">// notify change</span>
      ob.dep.notify();
      <span class="hljs-keyword">return</span> result
    &#125;);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上述代码可见，由于push、unshift、splice会让数组索引发生改变，所以需要手动触发observer，这里的方法是定义一个inserted来控制是否触发响应式更新，如果为true，则用<code>ob.observeArray(inserted);</code>来手动给新插入的值设置响应式监听，再用<code>ob.dep.notify()</code>通知依赖更新，最后返回原生数组方法处理后的值<code> return result</code>。</p>
<p>3.相关知识点：</p>
<p>3.1  def方法源码，在数组方法的重写中，用到了该方法来定义vue自己的一些数组方法，便于vue对一些需要重写的数组方法进行数据劫持。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">def</span> (<span class="hljs-params">obj, key, val, enumerable</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-attr">value</span>: val,
      <span class="hljs-attr">enumerable</span>: !!enumerable,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.2 observeArray方法的源码，在数组方法重写中，用于将新增的数组元组变成响应式的。</p>
<pre><code class="hljs language-js copyable" lang="js">Observer.prototype.observeArray = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observeArray</span> (<span class="hljs-params">items</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, l = items.length; i < l; i++) &#123;
      observe(items[i]);
    &#125;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            