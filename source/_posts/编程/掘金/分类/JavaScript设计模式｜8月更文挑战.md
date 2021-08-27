
---
title: 'JavaScript设计模式｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8703'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 07:01:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=8703'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>为了方便回忆快速使用设计模式</p>
<h2 data-id="heading-0">设计模式介绍</h2>
<p>设计模式（Design pattern）代表了最佳的实践，通常被有经验的面向对象的软件开发人员所采用。设计模式是软件开发人员在软件开发过程中面临的一般问题的解决方案。这些解决方案是众多软件开发人员经过相当长的一段时间的试验和错误总结出来的。</p>
<h4 data-id="heading-1">1.单例模式</h4>
<blockquote>
<p>这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。</p>
</blockquote>
<p>总结: 保证一个类只有唯一的实例对象, 全局登陆框</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> createLoginLayer = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  div.innerHTML = <span class="hljs-string">'唯一登陆框'</span>
  div.style.display = <span class="hljs-string">'none'</span>
  <span class="hljs-built_in">document</span>.body.appendChild(div)
  <span class="hljs-keyword">return</span> div
&#125;

<span class="hljs-keyword">const</span> getSingle = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> result || (result = fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>))
  &#125;
&#125;
<span class="hljs-keyword">const</span> createSingleLoginLayer = getSingle(createLoginLayer)

<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'loginBtn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  createSingleLoginLayer()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">2.策略模式</h4>
<blockquote>
<p>在策略模式中，我们创建表示各种策略的对象和一个行为随着策略对象改变而改变的 context 对象。策略对象改变 context 对象的执行算法。</p>
</blockquote>
<p>总结: 根据不同状态参数执行不同的方法, 红绿灯,播放器的状态</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> strategy = &#123;
  <span class="hljs-string">'S'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
  &#125;,
  <span class="hljs-string">'A'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
  &#125;,
  <span class="hljs-string">'B'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
  &#125;
&#125;

<span class="hljs-keyword">const</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">level, salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> strategy[level](salary)
&#125;

calculateBonus(<span class="hljs-string">'A'</span>, <span class="hljs-number">10000</span>) <span class="hljs-comment">// 30000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">3.代理模式</h4>
<blockquote>
<p>在代理模式（Proxy Pattern）中，一个类代表另一个类的功能。这种类型的设计模式属于结构型模式。
在代理模式中，我们创建具有现有对象的对象，以便向外界提供功能接口。</p>
</blockquote>
<p>总结: 为其他对象提供一种代理以控制对这个对象的访问, 起到中间层作用,不让过多接触该对向的所有属性或方法,eg:图片预览</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myImage = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> imgNode = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'img'</span>)
  <span class="hljs-built_in">document</span>.body.appendChild(imgNode)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">setSrc</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">src</span>) </span>&#123;
      imgNode.src = src
    &#125;
  &#125;
&#125;)()

<span class="hljs-keyword">const</span> proxyImage = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image()
  img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// http 图片加载完毕后才会执行</span>
    myImage.setSrc(<span class="hljs-built_in">this</span>.src)
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">setSrc</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">src</span>) </span>&#123;
      myImage.setSrc(<span class="hljs-string">'loading.jpg'</span>) <span class="hljs-comment">// 本地 loading 图片</span>
      img.src = src
    &#125;
  &#125;
&#125;)()
proxyImage.setSrc(<span class="hljs-string">'http://loaded.jpg'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4.迭代器模式</h3>
<blockquote>
<p>这种模式用于顺序访问集合对象的元素，不需要知道集合对象的底层表示。</p>
</blockquote>
<p>总结: 获取对象的顺序和元素方法,eg: es6的迭代器</p>
<h3 data-id="heading-5">5.命令模式</h3>
<p>将一个请求封装成一个对象，从而使您可以用不同的请求对客户进行参数化,像图片编辑这种多个命令操作记录、撤销、重做</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> setCommand = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">button, command</span>) </span>&#123;
  button.onClick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    command.excute()
  &#125;
&#125;

<span class="hljs-comment">// --------------------  上面的界面逻辑由A完成, 下面的由B完成</span>

<span class="hljs-keyword">const</span> menu = &#123;
  <span class="hljs-attr">updateMenu</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'更新菜单'</span>)
  &#125;,
&#125;

<span class="hljs-keyword">const</span> UpdateCommand = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">receive</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">excute</span>: receive.updateMenu,
  &#125;
&#125;

<span class="hljs-keyword">const</span> updateCommand = UpdateCommand(menu) <span class="hljs-comment">// 创建命令</span>

<span class="hljs-keyword">const</span> button1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button1'</span>)
setCommand(button1, updateCommand)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6.组合模式</h3>
<blockquote>
<p>依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，它创建了对象组的树形结构。
这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。</p>
</blockquote>
<h3 data-id="heading-7">7.责任链模式</h3>
<blockquote>
<p>通常每个接收者都包含对另一个接收者的引用。如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。</p>
</blockquote>
<p>不断执行,直到所有流程通过后</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类似这样的链路代码</span>
<span class="hljs-keyword">const</span> order500 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;&#125;
<span class="hljs-keyword">const</span> order200 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;&#125;
<span class="hljs-keyword">const</span> orderCommon = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;&#125;

<span class="hljs-built_in">Function</span>.prototype.after = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> result = self.apply(self, <span class="hljs-built_in">arguments</span>)
    <span class="hljs-keyword">if</span> (result === <span class="hljs-string">'nextSuccess'</span>) &#123;
      <span class="hljs-keyword">return</span> fn.apply(self, <span class="hljs-built_in">arguments</span>) <span class="hljs-comment">// 这里 return 别忘记了~</span>
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> order = order500.after(order200).after(orderCommon)

order( <span class="hljs-number">3</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span> ) <span class="hljs-comment">// 普通购买, 无优惠券</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有更多的设计模式</p></div>  
</div>
            