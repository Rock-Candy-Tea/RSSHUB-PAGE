
---
title: '设计模式 - State 状态模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef76b93dfc24f48991ebcd27a8c1691~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 02:02:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef76b93dfc24f48991ebcd27a8c1691~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">State（状态模式）</h2>
<p>State（状态模式）属于行为型模式。</p>
<p><strong>意图：允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。</strong></p>
<p>简单来说，就是将 “一个大 class + 一堆 if else” 替换为 “一堆小 class”。一堆小 class 就是一堆状态，用一堆状态代替 if else 会更好拓展与维护。</p>
<h2 data-id="heading-1">举例子</h2>
<p>如果看不懂上面的意图介绍，没有关系，设计模式需要在日常工作里用起来，结合例子可以加深你的理解，下面我准备了三个例子，让你体会什么场景下会用到这种设计模式。</p>
<h3 data-id="heading-2">团队接口人</h3>
<p>团队是由很多同学组成的，但有一位接口人 TL，这位 TL 可能一会儿和产品经理谈需求，一会儿和其他 TL 谈规划，一会儿和 HR 谈人事，总之要做很多事情，很显然一个人是忙不过来的。TL 通过将任务分发给团队中每个同学，而不让他们直接和产品经理、其他 TL、HR 接触，那么这位 TL 的办事效率就会相当高，因为每个同学只负责一块具体的业务，而 TL 在不同时刻叫上不同的同学，让他们出面解决他们负责的专业领域问题，那么在外面看，这位 TL 团队能力很广，在内看，每个人负责的事情也比较单一。</p>
<h3 data-id="heading-3">台灯按钮</h3>
<p>我们经常会看到只有一个按钮的台灯，但是可以通过按钮调节亮度，大概是如下一个循环 “关 -> 弱光 -> 亮 -> 强光 -> 关”，那么每次按按钮后，要跳转到什么状态，其实和当前状态有关。我们可以用 if else 解决这个问题，也可以用状态模式解决。</p>
<p>用状态模式解决，就是将这四个状态封装为四个类，每个类都执行按下按钮后要跳转到的状态，这样未来新增一种模式，只要改变部分类即可。</p>
<h3 data-id="heading-4">数据库连接器</h3>
<p>在数据库连接前后，这个连接器的状态显然非常不同，我们如果仅用一个类描述数据库连接器，则内部免不了写大量分支语句进行状态判断。那么此时有更好的方案吗？状态模式告诉我们，可以创建多个不同状态类，比如连接前、连接中、连接后三种状态类，在不同时刻内部会替换为不同的子类，它们都继承同样的父类，所以外面看上去不需要感知内部的状态变化，内部又可以进行状态拆分，进行更好的维护。</p>
<h2 data-id="heading-5">意图解释</h2>
<p><strong>意图：允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。</strong></p>
<p>重点在 “内部状态” 的理解，也就是状态改变是由对象内部触发的，而不是外部，所以 <strong>外部根本无需关心对象是否用了状态模式</strong>，拿数据库连接器的例子来说，不管这个类是用 if else 堆砌的，还是用状态模式做的，都完全不妨碍它对外提供的稳定 API（接口问题），所以状态模式实质上是一种内聚的设计模式。</p>
<h2 data-id="heading-6">结构图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef76b93dfc24f48991ebcd27a8c1691~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>State: 状态接口，类比为台灯状态。</li>
<li>ConcreteState: 具体状态，都继承于 State，类比为台灯的强光、弱光状态。</li>
</ul>
<h2 data-id="heading-7">代码例子</h2>
<p>下面例子使用 typescript 编写。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 定义状态接口</span>
<span class="hljs-keyword">interface</span> State &#123;
  <span class="hljs-comment">// 模拟台灯点亮</span>
  <span class="hljs-attr">show</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Light1</span> <span class="hljs-title">implements</span> <span class="hljs-title">State</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context: Context</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context = context
  &#125;

  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'关灯'</span>
  &#125;

  <span class="hljs-comment">// 按下按钮</span>
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context.setState(<span class="hljs-keyword">new</span> Light2(<span class="hljs-built_in">this</span>.context))
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Light2</span> <span class="hljs-title">implements</span> <span class="hljs-title">State</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context: Context</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context = context
  &#125;

  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'弱光'</span>
  &#125;

  <span class="hljs-comment">// 按下按钮</span>
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context.setState(<span class="hljs-keyword">new</span> Light3(<span class="hljs-built_in">this</span>.context))
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Light3</span> <span class="hljs-title">implements</span> <span class="hljs-title">State</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context: Context</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context = context
  &#125;

  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'亮'</span>
  &#125;

  <span class="hljs-comment">// 按下按钮</span>
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context.setState(<span class="hljs-keyword">new</span> Light4(<span class="hljs-built_in">this</span>.context))
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Light4</span> <span class="hljs-title">implements</span> <span class="hljs-title">State</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context: Context</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context = context
  &#125;

  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'强光'</span>
  &#125;

  <span class="hljs-comment">// 按下按钮</span>
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context.setState(<span class="hljs-keyword">new</span> Light1(<span class="hljs-built_in">this</span>.context))
  &#125;
&#125;

<span class="hljs-comment">// 台灯</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lamp</span> </span>&#123;
  <span class="hljs-comment">// 当前状态</span>
  <span class="hljs-keyword">private</span> currentState = <span class="hljs-keyword">new</span> Light1(<span class="hljs-built_in">this</span>)

  <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">setState</span>(<span class="hljs-params">state: State</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.currentState = state
  &#125;

  <span class="hljs-comment">// 按下按钮</span>
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.getState().click()
  &#125;
&#125;

<span class="hljs-keyword">const</span> lamp = <span class="hljs-keyword">new</span> Lamp() <span class="hljs-comment">// 关闭</span>
lamp.click() <span class="hljs-comment">// 弱光</span>
lamp.click() <span class="hljs-comment">// 亮</span>
lamp.click() <span class="hljs-comment">// 强光</span>
lamp.click() <span class="hljs-comment">// 关闭</span>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实有很多种方式来实现，不必拘泥于形式，大体上只要保证由多个类实现不同状态，每个类实现到下一个状态切换就好了。</p>
<h2 data-id="heading-8">弊端</h2>
<p>该用 if else 的时候还是要用，不要但凡遇到 if else 就使用状态模式，那样就是书读傻了。一定要判断，是否各状态间差异很大，且使用状态模式后维护性比 if else 更好，才应该用状态模式。</p>
<h2 data-id="heading-9">总结</h2>
<p>在合适场景下，状态模式可以使代码更符合开闭原则，每个类独立维护时，逻辑也更精简、聚焦，更易维护。</p></div>  
</div>
            