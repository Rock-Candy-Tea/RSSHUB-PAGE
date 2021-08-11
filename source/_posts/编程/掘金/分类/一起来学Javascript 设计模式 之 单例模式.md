
---
title: '一起来学Javascript 设计模式 之 单例模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1727'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 05:42:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=1727'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">单例模式</h2>
<p><strong>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<p>单例模式也成为了单体模式，规定一个类只有一个实例，并且提供可全局访问点。
JavaScript 中没有类的定义，单例模式的特点是”唯一“和”全局访问“，那么我们可以联想到 JavaScript 中的全局对象，利用 ES6 的 let 不允许重复声明的特性，刚好符合这两个特点；是的，全局对象是最简单的单例模式；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'rudy'</span>,
  <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中可以知道 obj 就是一个单例，因为 obj 刚好就符合单例模式的两大特点："唯一"和"可全局访问"；</p>
<p>但是我们并不建议这么实现单例，因为全局对象/全局变量会有一些弊端：</p>
<ol>
<li>污染命名空间（容易变量名冲突）</li>
<li>维护时不容易管控 (搞不好就直接覆盖了)</li>
</ol>
<p>简单版单例模式：</p>
<p>分析：只能有一个实例，所以我们需要使用if分支来判断，如果已经存在就直接返回，如果不存在就新建一个实例；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> Singleton = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.instance = <span class="hljs-literal">null</span>
&#125;


Singleton.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

Singleton.getInstance = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.instance) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance = <span class="hljs-keyword">new</span> Singleton(name)
&#125;

<span class="hljs-keyword">let</span> winner = Singleton.getInstance(<span class="hljs-string">'winner'</span>) <span class="hljs-comment">// winner</span>
<span class="hljs-keyword">let</span> sunner = Singleton.getInstance(<span class="hljs-string">'sunner'</span>) <span class="hljs-comment">// sunner</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中我们是通过一个变量 instance 的值来进行判断是否已存在实例，如果存在就直接返回 this.instance，如果不存在，就新建实例并赋值给 instance；</p>
<p>　　但是上面的代码还是存在问题，因为创建对象的操作和判断实例的操作耦合在一起，并不符合”单一职责原则“；</p>
<p>改良版：
思路：通过一个闭包，来实现判断实例的操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">let</span> CreateSingleton = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-keyword">if</span> (instance) &#123;
      <span class="hljs-keyword">return</span> instance
    &#125;

    <span class="hljs-keyword">return</span> instance = <span class="hljs-built_in">this</span>
  &#125;
&#125;)()

CreateSingleton.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

<span class="hljs-keyword">let</span> winner = <span class="hljs-keyword">new</span> CreateSingleton(<span class="hljs-string">'winner'</span>)
winner.getName() <span class="hljs-comment">// winner</span>
<span class="hljs-keyword">let</span> sunner = <span class="hljs-keyword">new</span> CreateSingleton(<span class="hljs-string">'sunner'</span>)
sunner.getName() <span class="hljs-comment">// sunner</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>代理版单例模式：</p>
<p>　通过代理的形式，将创建对象的操作和实例判断的操作进行解耦拆分，实现更小粒度的划分，符合”单一职责原则“；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">let</span> ProxyCreateSingleton = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (instance) <span class="hljs-keyword">return</span> instance
    <span class="hljs-keyword">return</span> instance = <span class="hljs-keyword">new</span> Singleton(name)
  &#125;
&#125;)()

<span class="hljs-keyword">let</span> Singleton = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
&#125;

Singleton.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

<span class="hljs-keyword">let</span> winner = <span class="hljs-keyword">new</span> ProxyCreateSingleton(<span class="hljs-string">"winner"</span>);
<span class="hljs-built_in">console</span>.log(winner.getName());
<span class="hljs-keyword">let</span> sunner = <span class="hljs-keyword">new</span> ProxyCreateSingleton(<span class="hljs-string">"sunner"</span>);
<span class="hljs-built_in">console</span>.log(sunner.getName());

<span class="copy-code-btn">复制代码</span></code></pre>
<p>惰性单例模式
　我们经常会有这样的场景：页面多次调用都有弹窗提示，只是提示内容不一样；
　这个时候我们可以立马想到是单例模式，弹窗就是单例实例，提示内容是参数传递；我们可以用惰性单例模式来实现它；</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"loginBtn"</span>></span>this is rudy<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> getSingleton = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">var</span> result;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> result || (result = fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)); <span class="hljs-comment">// 确定this上下文并传递参数</span>
    &#125;
  &#125;
  <span class="hljs-keyword">let</span> createAlertMessage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">html</span>) </span>&#123;
    <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
    div.innerHTML = html;
    div.style.display = <span class="hljs-string">'none'</span>;
    <span class="hljs-built_in">document</span>.body.appendChild(div);
    <span class="hljs-keyword">return</span> div;
  &#125;
  <span class="hljs-keyword">let</span> createSingleAlertMessage = getSingleton(createAlertMessage);
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'loginBtn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> alertMessage = createSingleAlertMessage(<span class="hljs-string">'<a href="https://www.baidu.com/" style="text-decoration:none;" target="_blank">baidu.com</a>'</span>);
    alertMessage.style.display = <span class="hljs-string">'block'</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>　惰性单例是指的是页面开始加载的时候我们的实例是没有进行创建的，是当我们点击页面的div之后才开始创建实例（按需创建），这可以提高我们的网页性能，加快我们的页面渲染速度；</p>
<p>ES6类的写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">name</span>) &#123;
    <span class="hljs-built_in">this</span>.name = name
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getInstance</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.instance) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance = <span class="hljs-keyword">new</span> Singleton(name)
  &#125;
&#125;

<span class="hljs-keyword">let</span> single1 = Singleton.getInstance(<span class="hljs-string">'rudy'</span>)
<span class="hljs-keyword">let</span> single2 = Singleton.getInstance(<span class="hljs-string">'kobe'</span>)

single1 === single2 <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来看看单例模式在Vue中的应用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Vue3</span>
<span class="hljs-keyword">import</span> &#123; createVNode, render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> type &#123;App&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> MessageConstructor <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  install(app: App): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-comment">// 非单例模式</span>
    <span class="hljs-comment">// app.config.globalProperties.$message = function(options: any)&#123;</span>
    <span class="hljs-comment">//     const container = document.createElement('div')</span>
    <span class="hljs-comment">//     const vm = createVNode(</span>
    <span class="hljs-comment">//       MessageConstructor,</span>
    <span class="hljs-comment">//       options as any,</span>
    <span class="hljs-comment">//     )</span>
    <span class="hljs-comment">//     render(vm, container)</span>
    <span class="hljs-comment">//     document.body.appendChild(container);</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// 闭包实现单例模式</span>
    app.config.globalProperties.$message = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
      <span class="hljs-keyword">let</span> vm: any;
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options: any</span>) </span>&#123;
        <span class="hljs-keyword">const</span> nodeList = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">"div.my-prop"</span>);
        <span class="hljs-keyword">if</span> (!nodeList.length) &#123;
          vm = <span class="hljs-literal">null</span>;
        &#125;
        <span class="hljs-keyword">if</span> (!vm) &#123;
          <span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
          container.className=<span class="hljs-string">'my-prop'</span>;
          vm = createVNode(
            MessageConstructor,
            options <span class="hljs-keyword">as</span> any,
          )
          render(vm, container)
          <span class="hljs-built_in">document</span>.body.appendChild(container);
        &#125;
        <span class="hljs-keyword">return</span> vm;
      &#125;
    &#125;)();
  &#125;
&#125;



<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            