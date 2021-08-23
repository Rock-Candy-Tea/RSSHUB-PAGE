
---
title: '四步简易实现vue里的watch'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=700'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 03:49:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=700'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">watch的使用</h2>
<p>这篇文章主要写的是watch(也可称作观察者模式)的实现，所以如何使用直接看代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">msg</span>:<span class="hljs-string">'Hello world'</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">this</span>.count++
        &#125;
      &#125;,
      <span class="hljs-comment">// watch</span>
      <span class="hljs-attr">watch</span>:&#123;
        <span class="hljs-comment">// 函数名必须与data数据源中的对象名一致才可监听</span>
        <span class="hljs-function"><span class="hljs-title">count</span>(<span class="hljs-params">newVal,oldVal</span>)</span>&#123;
          <span class="hljs-comment">// 如果最新的值大于10则修改data中的msg属性</span>
          <span class="hljs-keyword">if</span>(newVal>=<span class="hljs-number">10</span>) <span class="hljs-built_in">this</span>.msg = <span class="hljs-string">'Hello Watch'</span>
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要知道的是：</p>
<ol>
<li>watch里函数名必须是data数据源里对象的key值，这样才能对data数据源里对应key值的对象进行监听。</li>
<li>watch里的函数接收两个参数，第一个参数为赋的新值，第二个参数为初始值。</li>
<li>了解Object.defineProperty的特性</li>
</ol>
<h2 data-id="heading-1">实现</h2>
<h3 data-id="heading-2">第一步，明确需求</h3>
<p>需求：实现一个构造函数，可以放入data数据源和watch方法，watch中函数名对应data中的键名，可以在对应函数中监听到data里对应对象的数据变化(数据劫持)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Watcher(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">n</span>:<span class="hljs-string">'hello'</span>
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">a</span>(<span class="hljs-params">newValue, oldValue</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(newValue,oldValue);
    &#125;
  &#125;
&#125;)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  vm.a = <span class="hljs-number">1</span>
&#125;, <span class="hljs-number">2000</span>) 
<span class="hljs-comment">// 打印出 1 0 就实现了需求</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解了需求，接下来我们来实现它</p>
<h3 data-id="heading-3">第二步，建立构造函数</h3>
<p>首先，Watcher构造函数有一个参数，参数里应该放上data和watch，所以我们需要判断参数里是否能够拿到data和watch，且需要用一个函数来判断data和watch是否是一个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args</span>)</span> &#123;
    <span class="hljs-comment">// 判断传入的参数是否符合条件</span>
    <span class="hljs-built_in">this</span>.$data = <span class="hljs-built_in">this</span>.getBaseType(args.data) === <span class="hljs-string">"Object"</span> ? args.data : &#123;&#125;
    <span class="hljs-built_in">this</span>.$watch = <span class="hljs-built_in">this</span>.getBaseType(args.watch) === <span class="hljs-string">"Object"</span> ? args.watch : &#123;&#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getBaseType</span>(<span class="hljs-params">target</span>)</span> &#123;
    <span class="hljs-keyword">const</span> typeStr = <span class="hljs-built_in">Object</span>.prototype.toString.call(target) <span class="hljs-comment">// "[Object String]"</span>
    <span class="hljs-comment">// 返回类型 </span>
    <span class="hljs-keyword">return</span> typeStr.slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">第三步，监听data里的对象</h3>
<p>如果传入参数里data和watch都为对象，开始做<strong>数据劫持</strong>，使data里的每一个对象都被监听。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$data = <span class="hljs-built_in">this</span>.getBaseType(args.data) === <span class="hljs-string">"Object"</span> ? args.data : &#123;&#125;
    <span class="hljs-built_in">this</span>.$watch = <span class="hljs-built_in">this</span>.getBaseType(args.watch) === <span class="hljs-string">"Object"</span> ? args.watch : &#123;&#125;
    <span class="hljs-comment">// 遍历data里的每一个key，for in也可，它可以遍历对象的key</span>
    <span class="hljs-built_in">Object</span>.keys(args.data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setData(key)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">getBaseType</span>(<span class="hljs-params">target</span>)</span> &#123;
    <span class="hljs-keyword">const</span> typeStr = <span class="hljs-built_in">Object</span>.prototype.toString.call(target)
    <span class="hljs-keyword">return</span> typeStr.slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">setData</span>(<span class="hljs-params">_key</span>)</span> &#123;
    <span class="hljs-comment">// Object.defineProperty(this)会把上下文指向当前的对象</span>
    <span class="hljs-comment">// 这里的this就等同于构造函数里的this.$data</span>
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, _key, &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

      &#125;,
      <span class="hljs-comment">// // 对应值_key的值改变会触发set</span>
      <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
        <span class="hljs-comment">// val为对应key的对象被修改的后的值</span>
        <span class="hljs-built_in">console</span>.log(val)
      &#125;
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：defineProperty第一个参数放的不是<code>this.$data</code>而是<code>this</code>,这里是令人疑惑的一个点，具体原因请看注释,你可能会说为什么不用<code>this.$data</code>作为第一个参数，但是显然，既然defindProperty里的this已经等同于构造函数里的<code>this.$data</code>，那么defindProperty里的<code>this.$data</code>就等同于构造函数里的<code>this.$data.$data</code>。希望这样解释能够消除你的疑惑。</p>
<h3 data-id="heading-5">第四步，实现</h3>
<p>完善defineProperty里的结构，这里是最关键的，这里看代码更好理解</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$data = <span class="hljs-built_in">this</span>.getBaseType(args.data) === <span class="hljs-string">"Object"</span> ? args.data : &#123;&#125;
    <span class="hljs-built_in">this</span>.$watch = <span class="hljs-built_in">this</span>.getBaseType(args.watch) === <span class="hljs-string">"Object"</span> ? args.watch : &#123;&#125;
    <span class="hljs-comment">// 遍历data里的每一个key</span>
    <span class="hljs-built_in">Object</span>.keys(args.data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setData(key)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">getBaseType</span>(<span class="hljs-params">target</span>)</span> &#123;
    <span class="hljs-keyword">const</span> typeStr = <span class="hljs-built_in">Object</span>.prototype.toString.call(target) <span class="hljs-comment">// "[Object String]"</span>
    <span class="hljs-comment">// 返回类型 </span>
    <span class="hljs-keyword">return</span> typeStr.slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">setData</span>(<span class="hljs-params">_key</span>)</span> &#123;
    <span class="hljs-comment">// Object.defineProperty(this)会把上下文指向当前的对象</span>
    <span class="hljs-comment">// 这里的this就等同于构造函数里的this.$data</span>
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, _key, &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$data[_key]
      &#125;,
      <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
        <span class="hljs-comment">// 对应值_key的值改变会触发set</span>
        <span class="hljs-comment">// 先获取修改前的值</span>
        <span class="hljs-keyword">const</span> oldVal = <span class="hljs-built_in">this</span>.$data[_key]
        <span class="hljs-built_in">this</span>.$data[_key] = val
        <span class="hljs-comment">// 这里定义规定了watch里格式必须是同名，且要为函数</span>
        <span class="hljs-built_in">this</span>.$watch[_key] && <span class="hljs-built_in">this</span>.getBaseType(<span class="hljs-built_in">this</span>.$watch[_key]) === <span class="hljs-string">"Function"</span> && (
          <span class="hljs-comment">// 调用watch里的函数并传参</span>
          <span class="hljs-built_in">this</span>.$watch[_key].call(<span class="hljs-built_in">this</span>, val, oldVal)
        )
      &#125;
    &#125;)
  &#125;
&#125;
<span class="hljs-comment">// 检测</span>
<span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Watcher(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">n</span>: <span class="hljs-string">'hello'</span>
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">a</span>(<span class="hljs-params">newValue, oldValue</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(newValue, oldValue);
    &#125;
  &#125;
&#125;)


<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  vm.a = <span class="hljs-number">1</span>
&#125;, <span class="hljs-number">2000</span>) 
<span class="hljs-comment">//1 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里就已经简易实现了，其实vue里watch远比这复杂，但是我们学习的是一个思想，明白需求再代入思路，这对于学习源码的帮助很大。</p>
<p>以上就是实现watch的四步，希望对读者有帮助。如有错误欢迎评论探讨。</p></div>  
</div>
            