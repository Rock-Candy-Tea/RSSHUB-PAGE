
---
title: 'Vue3都成熟了、还不来了解了解Vue2的响应式原理吗_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357b7ae57fb1477f89fcc44a9421e612~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 04:07:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357b7ae57fb1477f89fcc44a9421e612~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>随着互联网行业的飞速发展，互联网所携带的产业也迎来了春天，尤其是前端行业更为突出，各种框架层出不穷，<code>Vue</code> <code>React</code> <code>Angular</code> <code>Solid</code> 等优秀框架的出现，不仅使得前端行业发生了翻天覆地的变化，还大大减轻了开发者的学习成本，但是随着框架的不断优化和版本升级，我们不在只追逐如何去使用这些框架，而是把目光留在了框架本身，比如框架的设计思想、框架的实现方案、以及框架的设计模式等等</p>
<h3 data-id="heading-1">为什么介绍Vue2</h3>
<blockquote>
<ul>
<li><code>Vue3</code> 的组合式API，和<code>hooks</code>设计已经成熟,可以说是对<code>Vue2</code>进行了彻底的颠覆</li>
<li>比如<code>Vue2</code>中，响应式拦截采用的是<code>Object.defineProperty</code> 而 <code>Vue3</code>中采用的是 <code>Proxy</code></li>
<li>对于小白是学习<code>Vue2</code> 还是 <code>Vue3</code>,尤大在 Vue Toronto 的主题演讲中也回答了 <code>Vue3</code> 是向下兼容的，可以直接学习 <code>Vue3</code> 即可
那么为什么还要介绍<code>Vue2</code>，我认为虽然<code>Vue2</code>已经要新版本取代，但是<code>Vue2</code>的设计思想和实现原理值得我们去深度刨析，框架的设计思想是不会过期的，这仍是值得我们学习的地方</li>
</ul>
</blockquote>
<h3 data-id="heading-2">观察者模式</h3>
<blockquote>
<p><code>Vue2</code>的响应式开发，采用的就是设计模式中的观察者模式，这个设计模式在开发过程中也是用的最多的一种，下面我们一起来看一下观察者模式的实现原理</p>
</blockquote>
<p>观察者模式下有两个重要的角色，分别是<code>发布者</code>与<code>订阅者</code>，通常情况下，发布者只有一个，而订阅者有很多个，
当状态发生改变（发布者发布信息），会通知所有订阅者进行更新处理，那么这个过程就是观察者模式的实现</p>
<h4 data-id="heading-3">发布者类</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Publisher</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 订阅者 依赖存储器 初始化</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span> = [];
  &#125;

  <span class="hljs-comment">// 增加订阅者</span>
  <span class="hljs-title function_">add</span>(<span class="hljs-params">observer</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span>.<span class="hljs-title function_">push</span>(observer);
  &#125;

  <span class="hljs-comment">// 删除订阅者</span>
  <span class="hljs-title function_">remove</span>(<span class="hljs-params">observer</span>) &#123;
    <span class="hljs-keyword">const</span> eq = <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span>.<span class="hljs-title function_">findIndex</span>(observer);
    <span class="hljs-keyword">if</span> (eq) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span>.<span class="hljs-title function_">splice</span>(eq, <span class="hljs-number">1</span>);
    &#125;
  &#125;

  <span class="hljs-comment">// 通知订阅者更新</span>
  <span class="hljs-title function_">notify</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      item?.<span class="hljs-title function_">update</span>(<span class="hljs-variable language_">this</span>);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看一下这段代码，这是一个<code>发布者</code>类，主要的方法有，添加订阅者<code>add</code>、删除订阅者<code>remove</code>、通知订阅者<code>notify</code></p>
<h4 data-id="heading-4">订阅者类</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Observer</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"订阅者 创建了"</span>);
  &#125;

  <span class="hljs-title function_">update</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"更新"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>订阅者</code>类的解构很简单，只有一个 <code>update</code>方法， <code>订阅者</code> 通过调用 <code>Publisher.add(订阅者)</code> 当<code>发布者</code>发布通知后，会逐个调用 <code>notify</code> 进行调用</p>
<h4 data-id="heading-5">现学现用</h4>
<blockquote>
<p>最近<code>华为mate50</code>和<code>iphone14</code>发布会已经结束，大家都在挣钱恐后的抢购，导致服务器爆炸，特喵的我根本就挤不进去，跑偏了不好意思，哈哈哈。那么我们现在有个需求，有一个手机厂商(<code>phoneFactory</code>)，他会不定时的发布一款新的手机，而我们有A、B、C三位同学(<code>studentObserver</code>)着急换手机，所以就一直在等待这个厂商的新品发布，那么我们如何实现一个当<code>phoneFactory</code>工厂发布新手机时，通知<code>studentObserver</code>购买</p>
</blockquote>
<h5 data-id="heading-6">PhoneFactory</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">PhoneFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Publisher</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 执行继承类的构造函数</span>
    <span class="hljs-variable language_">super</span>();
    <span class="hljs-comment">// 初始化手机 默认是没有</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">phone</span> = <span class="hljs-literal">null</span>;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">phonePrice</span> = <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 订阅者列表 存起来用于通知</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">observers</span> = [];
  &#125;

  <span class="hljs-comment">// 获取当前的产品名称和价格</span>
  <span class="hljs-title function_">getProduct</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">phone</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">phone</span>,
        <span class="hljs-attr">phonePrice</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">phonePrice</span>
    &#125;;
  &#125;

  <span class="hljs-comment">// 修改产品信息</span>
  <span class="hljs-title function_">setPrd</span>(<span class="hljs-params">phone, phonePrice</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">phone</span> = phone;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">phonePrice</span> = phonePrice;
    <span class="hljs-comment">// 通知订阅者可以购买了</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">notify</span>();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">studentObserver</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">StudentObserver</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Observer</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">name, price</span>) &#123;
    <span class="hljs-variable language_">super</span>();
    <span class="hljs-comment">// 订阅者姓名</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">name</span> = name
    <span class="hljs-comment">// 资产</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">price</span> = price;
    <span class="hljs-comment">// 当前手机型号</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">phoneModel</span> = <span class="hljs-string">'HUAWEI nova5 pro'</span>;
  &#125;

  <span class="hljs-comment">// update 购买</span>
  <span class="hljs-title function_">update</span>(<span class="hljs-params">Publisher</span>) &#123;
    <span class="hljs-comment">// 更新需求文档</span>
    <span class="hljs-keyword">let</span> foo, boo = <span class="hljs-literal">false</span>
    foo = <span class="hljs-title class_">Publisher</span>.<span class="hljs-title function_">getProduct</span>();
    <span class="hljs-keyword">if</span>(foo.<span class="hljs-property">phonePrice</span> < <span class="hljs-variable language_">this</span>.<span class="hljs-property">price</span>) &#123;
        <span class="hljs-comment">// 买得起</span>
        boo = <span class="hljs-literal">true</span>
        <span class="hljs-comment">// 换新手机了，修改手机的参数</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">price</span> -= foo.<span class="hljs-property">phonePrice</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">phoneModel</span> = foo.<span class="hljs-property">phone</span>
    &#125; 
    <span class="hljs-comment">// 其他逻辑</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">run</span>(boo);
  &#125;

  <span class="hljs-comment">// 执行的逻辑</span>
  <span class="hljs-title function_">run</span>(<span class="hljs-params">boo</span>) &#123;
     <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(
      <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.name&#125;</span> <span class="hljs-subst">$&#123;boo ? <span class="hljs-string">"购买了新手机"</span> : <span class="hljs-string">"存款买不起"</span>&#125;</span>`</span>,
      <span class="hljs-string">`存款剩余 <span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.price&#125;</span>`</span>, <span class="hljs-string">`当前手机：<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.phoneModel&#125;</span>`</span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码测试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 工厂</span>
<span class="hljs-keyword">const</span> <span class="hljs-title class_">Factory</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">PhoneFactory</span>()
<span class="hljs-comment">// 学生A、B、C</span>
<span class="hljs-comment">// A同学有一万块钱</span>
<span class="hljs-keyword">const</span> A  = <span class="hljs-keyword">new</span> <span class="hljs-title class_">StudentObserver</span>(<span class="hljs-string">'A'</span>, <span class="hljs-number">10000</span>)
<span class="hljs-comment">// B同学有四千块钱</span>
<span class="hljs-keyword">const</span> B  = <span class="hljs-keyword">new</span> <span class="hljs-title class_">StudentObserver</span>(<span class="hljs-string">'B'</span>, <span class="hljs-number">4000</span>)
<span class="hljs-comment">// C同学有两千块钱</span>
<span class="hljs-keyword">const</span> C  = <span class="hljs-keyword">new</span> <span class="hljs-title class_">StudentObserver</span>(<span class="hljs-string">'C'</span>, <span class="hljs-number">2000</span>)
<span class="hljs-comment">// 学生订阅到工厂</span>
<span class="hljs-title class_">Factory</span>.<span class="hljs-title function_">add</span>(A)
<span class="hljs-title class_">Factory</span>.<span class="hljs-title function_">add</span>(B)
<span class="hljs-title class_">Factory</span>.<span class="hljs-title function_">add</span>(C)

<span class="hljs-comment">// 工厂发布手机</span>
<span class="hljs-title class_">Factory</span>.<span class="hljs-title function_">setPrd</span>(<span class="hljs-string">'iphone14 pro max 远峰蓝'</span>, <span class="hljs-number">9999</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们运行代码查看输出的结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357b7ae57fb1477f89fcc44a9421e612~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到，<code>订阅者</code>创建了三次，因为有三名同学订阅了这个工厂，当工厂发布手机时，三名同学会触发购买流程，但是很可惜B、C两位同学因为买不起错过了这次发布会</p>
<p>以上实例就是一个完整的<code>观察者模式</code>的示例，虽然有时候写法大同小异，但是设计思想都是一样的，无非就是通过<code>订阅</code>，然后<code>发布者</code>修改数据并通知<code>订阅者</code>完成具体的逻辑操作</p>
<h3 data-id="heading-8">Vue2 中响应式的实现</h3>
<p>我们先来看一段代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vue</span>(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"yunhe达摩院"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">16</span>,
    <span class="hljs-attr">school</span>: <span class="hljs-string">"郑州大学"</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在使用<code>Vue2</code>时，首先会在<code>data</code>定义一个<code>对象</code>或者<code>闭包</code>, <code>data</code> 存放的是我们响应式处理的数据，当我们在模板中渲染<code>data</code>中的数据后,如果<code>data</code>里面的数据发生了改变，就会通知模板更新绑定的<code>data</code></p>
<p>现在我们撸一撸思路Vue修改参数，通知模板更改，这用的不就是我们的<code>观察者模式</code></p>
<ol>
<li>模板调用<code>data</code>，完成订阅</li>
<li><code>data.xxx = newXxx</code> 修改数据后，通知<code>notify</code>修改页面上的变量，完成响应式更新</li>
</ol>
<p>那么怎么去用代码具体实现<code>Vue2</code>的响应式开发，下面让我们一起来看一下</p>
<h3 data-id="heading-9">文件目录结构如下</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae4e36f9ae1433a99a14d279b489e1f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>main.js</code> 为入口文件 <br>
<code>index.js</code> 为<code>vue</code>文件 <br>
<code>dep.js</code> 为订阅者文件 <br>
<code>proxy.js</code> 为代理文件 <br>
<code>watcher.js</code> 为订阅者文件 <br>
<code>defineReactive.js</code> 为拦截器文件 <br>
<code>mount.js</code> 为渲染文件</p>
</blockquote>
<p>简单的实现<code>Vue2</code>的响应式，大致需要以上几个文件，现在都是空白文件，现在让我们一步一步的根据我们的思路，去实现一下<code>Vue2</code>的响应式处理</p>
<h3 data-id="heading-10">main.js</h3>
<blockquote>
<p><code>main.js</code> 是项目的入口文件，这里通常是使用<code>Vue</code>的地方，所以我们可以根据<code>Vue2</code>的使用原理去编写一个<code>Vue2</code>的解构代码</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">Vue</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./index.js"</span>;
<span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vue</span>(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"达摩院"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">16</span>,
    <span class="hljs-attr">school</span>: <span class="hljs-string">"郑州大学"</span>,
  &#125;,
  <span class="hljs-comment">// data 还可以使用闭包</span>
  <span class="hljs-comment">// data() &#123;</span>
  <span class="hljs-comment">//   return &#123;</span>
  <span class="hljs-comment">//     name: "达摩院",</span>
  <span class="hljs-comment">//     age: 16,</span>
  <span class="hljs-comment">//     school: '郑州大学'</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-comment">// &#125;</span>
&#125;);
<span class="hljs-comment">// 将 $vm 绑定到window全局变量上，帮助我们在控制台可以操作修改变量</span>
<span class="hljs-variable language_">window</span>.<span class="hljs-property">$vm</span> = vm;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">index.js</h3>
<blockquote>
<p>我们在 <code>main.js</code> 中导入了 <code>import Vue from "./index.js"</code>，所以接下来我们要创建它</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Vue</span>(<span class="hljs-params">options</span>) &#123;
    <span class="hljs-comment">// _init 用于初始化;</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">_init</span>(options);
&#125;

<span class="hljs-comment">// 初始化 把data绑定到</span>
<span class="hljs-title class_">Vue</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">_init</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) &#123;
    <span class="hljs-comment">// 把数据配置挂载到Vue.$options 上</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">$options</span> = options;
    <span class="hljs-comment">// 初始数据（data methods props computed等 这里制作简单的处理 data）</span>
    <span class="hljs-title function_">initData</span>(<span class="hljs-variable language_">this</span>);
&#125;

<span class="hljs-comment">// 初始化数据 具体的方法实现</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
    <span class="hljs-keyword">const</span> &#123;
        data,
        el
    &#125; = vm.<span class="hljs-property">$options</span>
    <span class="hljs-comment">// data 就是我们在首页 new Vue(&#123;data()&#123;return &#123;&#125;&#125;&#125;)  的data</span>
    <span class="hljs-keyword">let</span> _data
    <span class="hljs-keyword">if</span> (data) &#123;
        <span class="hljs-comment">// 把data的值挂载到vm实例上</span>
        <span class="hljs-comment">// data 有可能是个闭包方法 所以要判断如果是闭包执行以下获取一下里面的json</span>
        _data = vm.<span class="hljs-property">_data</span> = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span> ? <span class="hljs-title function_">data</span>() : data
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经将 <code>new Vue(&#123;data()&#123;return &#123;&#125;&#125;&#125;)</code>  的 <code>data</code> 绑定到了<code>Vue</code>示例上, 现在让我们打开控制台看一下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5507153cdcb4ad48ce553f1ef36c585~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们不仅可以查看绑定的数据，而且还可以进行修改，那么在Vue2的逻辑中，我们在进行修改属性时，会被系统劫持，也就是说我们所有的赋值操作，都应该被拦截到,这里我们使用的是 <code>defineReactive.js</code></p>
<h3 data-id="heading-12">defineReactive.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">defineReactive</span>(<span class="hljs-params">target, key, val</span>) &#123;
    <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
        <span class="hljs-title function_">get</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-keyword">return</span> val
        &#125;,
        <span class="hljs-title function_">set</span>(<span class="hljs-params">value</span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(val,<span class="hljs-string">'被修改了 '</span>,value);
            <span class="hljs-keyword">if</span> (val === value) <span class="hljs-keyword">return</span>
            val = value
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> defineReactive <span class="hljs-keyword">from</span> <span class="hljs-string">"./defineReactive.js"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Vue</span>(<span class="hljs-params">options</span>) &#123;
  <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">_init</span>(options);
&#125;
<span class="hljs-comment">// 初始化 把data绑定到</span>
<span class="hljs-title class_">Vue</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">_init</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"options ==> "</span>, options);
  <span class="hljs-comment">// 把数据配置挂载到Vue.$options 上</span>
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">$options</span> = options;
  <span class="hljs-comment">// 初始数据  （data methods props computed等 这里制作简单的处理 data）</span>
  <span class="hljs-title function_">initData</span>(<span class="hljs-variable language_">this</span>);
&#125;;

<span class="hljs-comment">// 初始化数据 具体的方法实现</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
  <span class="hljs-keyword">const</span> &#123; data, el &#125; = vm.<span class="hljs-property">$options</span>;
  <span class="hljs-comment">// data 就是我们在首页 new Vue(&#123;data()&#123;return &#123;&#125;&#125;&#125;)  的data</span>
  <span class="hljs-comment">// console.log('data ==> ', data);</span>
  <span class="hljs-keyword">let</span> _data;
  <span class="hljs-keyword">if</span> (data) &#123;
    <span class="hljs-comment">// 把data的值挂载到vm实例上</span>
    <span class="hljs-comment">// data 有可能是个闭包方法 所以要判断如果是闭包执行以下获取一下里面的json</span>
    _data = vm.<span class="hljs-property">_data</span> = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">"function"</span> ? <span class="hljs-title function_">data</span>() : data;
  &#125;

  <span class="hljs-comment">// 给对象属性设置响应式 (只支持对象)</span>
  <span class="hljs-keyword">function</span> <span class="hljs-title function_">walk</span>(<span class="hljs-params">obj</span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;
      <span class="hljs-comment">// 依次给对象设置拦截</span>
      <span class="hljs-title function_">defineReactive</span>(obj, key, obj[key]);
    &#125;
  &#125;
  <span class="hljs-comment">// 设置拦截</span>
  <span class="hljs-title function_">walk</span>(_data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行示例查看效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5110d9cb3554670812ad4d6395d6714~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到目前为止，我们的程序已经可以监听到我们的修改了</p>
<h3 data-id="heading-13">index.html</h3>
<blockquote>
<p>通过上面的示例，我们已经创建了Vue文件，并设置了拦截修改的处理，但是我们发现，我们的数据只能在<code>console.log</code>内运行，现在我们渲染一下我们的数据，看一下我们的效果</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><!<span class="hljs-variable constant_">DOCTYPE</span> html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;shops&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;school&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./main.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5f3bcdc4ea4c3fab0ae2e7074b0a5e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">mount.js</h3>
<blockquote>
<p>现在我们已经将变量放置在了模板块中，但是我们现在还无法渲染数据，因为我们的<code>mount</code>挂载逻辑没有处理,现在让我们完善一下<code>mount.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 把数据挂载到页面上</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">mount</span>(<span class="hljs-params">vm</span>) &#123;
    <span class="hljs-comment">// 获取根节点</span>
    <span class="hljs-keyword">let</span> &#123;
        el
    &#125; = vm.<span class="hljs-property">$options</span>;
    el = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelectorAll</span>(el);
    <span class="hljs-comment">// el[0].childNodes 默认情况下是 NodeList类数组,输出可看,不能直接进行遍历需要转换为普通数组</span>
    <span class="hljs-comment">// 把vm实例传下去 方便替换数据</span>
    <span class="hljs-title function_">compuleNode</span>(<span class="hljs-title class_">Array</span>.<span class="hljs-title function_">from</span>(el[<span class="hljs-number">0</span>].<span class="hljs-property">childNodes</span>), vm)
&#125;

<span class="hljs-comment">// 查找变量并替换</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">compuleNode</span>(<span class="hljs-params">nodes, vm</span>) &#123;
    <span class="hljs-comment">// node 是我们拿到的所有根节点下的dom</span>
    <span class="hljs-comment">// 遍历dom节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> node <span class="hljs-keyword">of</span> nodes) &#123;
        <span class="hljs-comment">// 节点有区别: </span>
        <span class="hljs-comment">// nodeType === 1 表示是元素div span这些元素等</span>
        <span class="hljs-comment">// nodeType === 3 表示是文本 也就是最后一级</span>
        <span class="hljs-keyword">if</span> (node.<span class="hljs-property">nodeType</span> === <span class="hljs-number">3</span> && node.<span class="hljs-property">textContent</span>.<span class="hljs-title function_">match</span>(<span class="hljs-regexp">/&#123;&#123;(.*)&#125;&#125;/</span>)) &#123;
            <span class="hljs-comment">// node.textContent.match(/&#123;&#123;(.*)&#125;&#125;/) 会对我们的结果进行分组 &#123;&#123;name&#125;&#125;  &#123;&#123;age&#125;&#125; </span>
            <span class="hljs-comment">// 通过正则 可以使用下标获取结果</span>
            <span class="hljs-comment">// console.log('RegExp.$1 ==> ', RegExp.$1);</span>
            <span class="hljs-comment">// 既然是文本 那么我们就可以直接查找替换元素即可</span>
            <span class="hljs-comment">// <div>&#123;&#123;name&#125;&#125;</div>  我们要判断他是否有 &#123;&#123;&#125;&#125;</span>
            <span class="hljs-comment">//  是文本节点 并且有 &#123;&#123;(.*)&#125;&#125; 因为我们的变量是通过双括号包含的</span>
            <span class="hljs-title function_">compuleTextNode</span>(node, vm);
        &#125;

        <span class="hljs-comment">// 如果是dom元素 就递归遍历查找他的子元素</span>
        <span class="hljs-keyword">if</span> (node.<span class="hljs-property">nodeType</span> === <span class="hljs-number">1</span>) &#123;
            <span class="hljs-title function_">compuleNode</span>(node.<span class="hljs-property">childNodes</span>, vm)
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 替换数据</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">compuleTextNode</span>(<span class="hljs-params">node, vm</span>) &#123;
    <span class="hljs-comment">// 获取匹配的结果 </span>
    <span class="hljs-comment">// 替换dom得值</span>
    <span class="hljs-keyword">const</span> key = <span class="hljs-title class_">RegExp</span>.<span class="hljs-property">$1</span>
    <span class="hljs-comment">// 写一个回调 专门修改当前这个节点的数据</span>
    <span class="hljs-comment">// 如果 vm[key] 有数据 就返回数据 没有就返回 未找到</span>
    node.<span class="hljs-property">textContent</span> = vm[key] ? <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(vm[key]) : <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> 未定义`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mount <span class="hljs-keyword">from</span> <span class="hljs-string">"./compiler/mount.js"</span>;
<span class="hljs-keyword">import</span> defineReactive <span class="hljs-keyword">from</span> <span class="hljs-string">"./defineReactive.js"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Vue</span>(<span class="hljs-params">options</span>) &#123;
  <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">_init</span>(options);
&#125;
<span class="hljs-comment">// 初始化 把data绑定到</span>
<span class="hljs-title class_">Vue</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">_init</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"options ==> "</span>, options);
  <span class="hljs-comment">// 把数据配置挂载到Vue.$options 上</span>
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">$options</span> = options;
  <span class="hljs-comment">// 初始数据  （data methods props computed等 这里制作简单的处理 data）</span>
  <span class="hljs-title function_">initData</span>(<span class="hljs-variable language_">this</span>);
  <span class="hljs-comment">// 挂在到dom</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">$options</span>.<span class="hljs-property">el</span>) &#123;
    <span class="hljs-variable language_">this</span>.$mount();
  &#125;
&#125;;

<span class="hljs-comment">// 挂在实例</span>
<span class="hljs-title class_">Vue</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">$mount</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
  <span class="hljs-comment">// 挂载到页面上</span>
  <span class="hljs-title function_">mount</span>(<span class="hljs-variable language_">this</span>);
&#125;;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行文件，我们会发现，所有的变量全部都报未定义</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bade6d728e2471e93ab8fcd1b3e8073~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那是因为在这里，我是需要通过 <code>_data.xx</code> 来访问 <code>xx</code> 变量的，在<code>Vue</code>中，我们使用data中的变量的时候，直接使用的方式是 <code>this.xxx</code>，而不是 <code>this.data.xxx</code>, 当然，我们也可以渲染 <code>_data</code> 到页面查看</p>
<p>在 <code>index.html</code> 输出 <code>&#123;&#123;_data&#125;&#125;</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93e63de21f4a4fce9d8f2c25197cdc3c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然使用<code>_data.xxx</code>的方式可行，但是我们总不能一直使用<code>_data.</code>为前缀吧，这样的话会使得我们的代码非常的不堪，那么这个地方，我们可以使用<code>proxy</code>代理，将 <code>xxx</code> 代理到 <code>vm._data</code> 上，这样当我们访问<code>xxx</code>时，会被拦截并代理到<code>_data.xxx</code></p>
<h3 data-id="heading-15">proxy.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxy</span>(<span class="hljs-params">target, sourceKey, key</span>) &#123;
    <span class="hljs-comment">// 代理 当访问指定targert对象时 例：Obj.a 代理到 Obj.data.a </span>
    <span class="hljs-comment">// proxy(Obj, data, a) 代理</span>
    <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
        <span class="hljs-title function_">get</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-comment">// this.a 访问 this._data.a</span>
            <span class="hljs-keyword">return</span> target[sourceKey][key]
        &#125;,
        <span class="hljs-title function_">set</span>(<span class="hljs-params">val</span>) &#123;
            <span class="hljs-comment">// this.a = 1 修改 this._data.a = 1</span>
            target[sourceKey][key] = val
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>index.js</code> 中调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mount <span class="hljs-keyword">from</span> <span class="hljs-string">"./compiler/mount.js"</span>;
<span class="hljs-keyword">import</span> defineReactive <span class="hljs-keyword">from</span> <span class="hljs-string">"./defineReactive.js"</span>;
<span class="hljs-keyword">import</span> proxy <span class="hljs-keyword">from</span> <span class="hljs-string">'./proxy.js'</span>

<span class="hljs-comment">// 初始化数据 具体的方法实现</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
  <span class="hljs-keyword">const</span> &#123; data, el &#125; = vm.<span class="hljs-property">$options</span>;
  <span class="hljs-comment">// data 就是我们在首页 new Vue(&#123;data()&#123;return &#123;&#125;&#125;&#125;)  的data</span>
  <span class="hljs-comment">// console.log('data ==> ', data);</span>
  <span class="hljs-keyword">let</span> _data;
  <span class="hljs-keyword">if</span> (data) &#123;
    <span class="hljs-comment">// 把data的值挂载到vm实例上</span>
    <span class="hljs-comment">// data 有可能是个闭包方法 所以要判断如果是闭包执行以下获取一下里面的json</span>
    _data = vm.<span class="hljs-property">_data</span> = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">"function"</span> ? <span class="hljs-title function_">data</span>() : data;
  &#125;

  <span class="hljs-comment">// 给对象属性设置响应式 (只支持对象)</span>
  <span class="hljs-keyword">function</span> <span class="hljs-title function_">walk</span>(<span class="hljs-params">obj</span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;
      <span class="hljs-comment">// 依次给对象设置拦截</span>
      <span class="hljs-title function_">defineReactive</span>(obj, key, obj[key]);
    &#125;
  &#125;
  <span class="hljs-comment">// 设置拦截</span>
  <span class="hljs-title function_">walk</span>(_data);

  <span class="hljs-comment">// proxy 映射</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> _data) &#123;
    <span class="hljs-comment">// 把data数据代理到 _data 下 是他支持 this.xxx 调用</span>
    <span class="hljs-comment">// 原理 当我们调用 this.xxx 时,会把我们的指向为 this._data.xxx</span>
    <span class="hljs-comment">// props methods computed同理</span>
    <span class="hljs-title function_">proxy</span>(vm, <span class="hljs-string">"_data"</span>, key);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成代理后，我们在浏览器中重新执行，会发现，所有的数据都已经被渲染出来了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c346a9760e16499da51ad5aed18362c3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们已经实现了一个很小的Vue模板渲染功能，但是，我们目前的功能还不能够进行响应式的实现，因为我们修改了数据，也仅仅只是修改了对象中的数据而已，并没有被重新渲染到页面上</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ce1e29799f4d6dbfb85ac6969c52a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">重点来袭</h3>
<blockquote>
<p>在<code>vue</code>中，<code>发布者</code>和<code>订阅者</code>的关系比较抽象</p>
<ul>
<li>我们定义一个<code>Dep</code> 类用来订阅 <code>data</code>，当<code>data</code>修改时通知<code>Dep</code>类更新，<code>data</code> 和 <code>Dep</code> 关系是一对一的订阅模式，一个<code>data</code> 只能被订阅一次，在这里<code>data</code> 等于被 <code>Dep</code> 订阅</li>
<li>在模板渲染中，我们定义一个<code>Watcher</code>类，当我们在模板中渲染<code>data</code>时，我们将调用的地方传递给<code>Watcher</code>，并让 <code>Watcher</code> 订阅 <code>Dep</code>，<code>Dep</code>修改后通知模板<code>Watcher</code>渲染模板,也就是说，<code>Dep</code>和<code>Watcher</code>的关系属于是一对多的关系， 一个<code>Dep</code>可以被多个<code>Watcher</code>调用</li>
</ul>
</blockquote>
<p>具体的流程图如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c8dc30d2b8b45ecbb8684d0f7f1ea95~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们修改<code>name</code> 时，会触发更新<code>Dep</code> 、 <code>Dep</code>更新后会开始遍历更新<code>Watcher</code>,此时只会去更新<code>name</code>的订阅者，而不会影响其他 <br>
<em><strong>也就是说在这里，<code>Dep</code>不仅仅是<code>订阅者</code>，他也是<code>发布者</code></strong></em></p>
<h3 data-id="heading-17">Dep.js</h3>
<blockquote>
<p>理解完上面的原理，我们现在开始创建<code>Dep</code>类</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Dep</span> &#123;
    <span class="hljs-comment">// Dep 不仅是订阅者 他订阅后还要收集watcher来更新模板 所以Dep也可以说是发布者</span>
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">watcher</span> = []
    &#125;
    <span class="hljs-comment">// target 表示节点, 当在模板中调用变量时,target指向哪个dom节点</span>
    <span class="hljs-keyword">static</span> target = <span class="hljs-literal">null</span>

    <span class="hljs-title function_">depend</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 主要用于保存 Watcher，Watcher 会在DOM调用时处理</span>
        <span class="hljs-comment">// Dep.target 就是 当前模板中的 Watcher</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">watcher</span>.<span class="hljs-title function_">push</span>(<span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span>)
    &#125;

    <span class="hljs-comment">// 通知依赖 watcher 更新</span>
    <span class="hljs-title function_">notify</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">watcher</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> &#123;
            sub.<span class="hljs-title function_">update</span>()
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Dep</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理完 <code>Dep</code> 我们开始订阅 <code>data</code> <br>
修改 <code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加引用</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Dep</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./dep.js"</span>;

<span class="hljs-comment">// 修改方法</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
  <span class="hljs-keyword">const</span> &#123; data, el &#125; = vm.<span class="hljs-property">$options</span>;
  <span class="hljs-comment">// data 就是我们在首页 new Vue(&#123;data()&#123;return &#123;&#125;&#125;&#125;)  的data</span>
  <span class="hljs-comment">// console.log('data ==> ', data);</span>
  <span class="hljs-keyword">let</span> _data;
  <span class="hljs-keyword">if</span> (data) &#123;
    <span class="hljs-comment">// 把data的值挂载到vm实例上</span>
    <span class="hljs-comment">// data 有可能是个闭包方法 所以要判断如果是闭包执行以下获取一下里面的json</span>
    _data = vm.<span class="hljs-property">_data</span> = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">"function"</span> ? <span class="hljs-title function_">data</span>() : data;
  &#125;

  <span class="hljs-comment">// proxy 映射</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> _data) &#123;
    <span class="hljs-comment">// 把data数据代理到 _data 下 是他支持 this.xxx 调用</span>
    <span class="hljs-comment">// 原理 当我们调用 this.xxx 时,会把我们的指向为 this._data.xxx</span>
    <span class="hljs-comment">// props methods computed同理</span>
    <span class="hljs-title function_">proxy</span>(vm, <span class="hljs-string">"_data"</span>, key);
  &#125;

  <span class="hljs-comment">// 设置完代理以后 给data数据设置响应式更新 也就是 Dep订阅data</span>
  <span class="hljs-title function_">observe</span>(vm.<span class="hljs-property">_data</span>);
&#125;

<span class="hljs-comment">// 响应式判断和设置响应式</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">observe</span>(<span class="hljs-params">data</span>) &#123;
  <span class="hljs-comment">// 如果数据已经是响应式 就不需要observe进行依赖收集 否则会造成 重复更新指定节点</span>
  <span class="hljs-keyword">if</span> (data.<span class="hljs-property">__ob__</span>) <span class="hljs-keyword">return</span> value.<span class="hljs-property">__ob__</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Observer</span>(data);
&#125;

<span class="hljs-comment">// 订阅</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">Observer</span>(<span class="hljs-params">data</span>) &#123;
  <span class="hljs-comment">// 给每个数据都加上一个 __ob__ 属性 表示已经处理了响应式拦截和更新</span>
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(data, <span class="hljs-string">"__ob__"</span>, &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-variable language_">this</span>,
    <span class="hljs-comment">// 数据可枚举</span>
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 数据可修改</span>
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 数据可配置</span>
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  &#125;);
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"data ==> "</span>, data);
  <span class="hljs-comment">// 对值进行依赖收集也就是订阅</span>
  data.<span class="hljs-property">__ob__</span>.<span class="hljs-property">dep</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Dep</span>();
  <span class="hljs-comment">// 给对象的每一项都设置响应式</span>
  <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">walk</span>(data);
&#125;

<span class="hljs-comment">// 给对象属性设置响应式 (只支持对象)</span>
<span class="hljs-title class_">Observer</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">walk</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;
    <span class="hljs-comment">// 依次给对象设置拦截</span>
    <span class="hljs-title function_">defineReactive</span>(obj, key, obj[key]);
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加完<code>Dep</code>订阅以后，我们在控制台输出查看我们的变量是否被<code>Dep</code>订阅</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e868ea06c7e4335b74e13ebec928beb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里<code>Dep</code>已经成功订阅了<code>data</code></p>
<h3 data-id="heading-18">Watcher.js</h3>
<blockquote>
<p><code>Dep</code>订阅了<code>data</code>之后，我们开始处理模板中使用<code>data</code>时，让<code>Watcher</code>订阅<code>Dep</code></p>
</blockquote>
<p>首先我们要知道 <code>Watcher</code> 其实就是更新<code>Dom</code> 操作的 <br>
我们修改一下<code>mount.js</code>下面的 <code>ompuleTextNode</code>法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 新增引入</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Watcher</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"../watcher.js"</span>;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">compuleTextNode</span>(<span class="hljs-params">node, vm</span>) &#123;
    <span class="hljs-comment">// 获取匹配的结果 </span>
    <span class="hljs-comment">// 替换dom得值</span>
    <span class="hljs-keyword">const</span> key = <span class="hljs-title class_">RegExp</span>.<span class="hljs-property">$1</span>
    <span class="hljs-comment">// 封装成一个方法 专门更新当前的Dom</span>
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">cb</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 如果 vm[key] 有数据 就返回数据 没有就返回 未找到</span>
        node.<span class="hljs-property">textContent</span> = vm[key] ? <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(vm[key]) : <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> 未定义`</span>;
    &#125;
    <span class="hljs-comment">// Watcher 是专门用来处理Dom节点更新的</span>
    <span class="hljs-comment">// 我们把cb回调传递给Watcher，当更新至 执行这个cb() 就可以完成重新渲染</span>
    <span class="hljs-keyword">new</span> <span class="hljs-title class_">Watcher</span>(cb)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Wtcher.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">Dep</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./dep.js"</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Watcher</span> &#123;
    <span class="hljs-comment">// cb 是修改指定dom的闭包回调,只修改某一个</span>
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">cb</span>) &#123;
        <span class="hljs-comment">// Dep.target 是一个静态变量, this就是我们当前的Watcher,赋值给Dep后,Dep放入到订阅数组中</span>
        <span class="hljs-comment">// 为什么要使用Dep.target 因为我们必须要知道我们调用data的时机</span>
        <span class="hljs-comment">// js this.xxx调用时 我们不需要获取依赖，所以 Dep.target 主要适用于判断那我们的时机</span>
        <span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span> = <span class="hljs-variable language_">this</span>
        <span class="hljs-comment">// 这一步是将修改的回调函数存储起来</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">_cb</span> = cb
        <span class="hljs-comment">// 执行一下，因为初始化状态需要执行以下，将 &#123;&#123;name&#125;&#125; 转换为 data 的变量值</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">_cb</span>()
        <span class="hljs-comment">// 处理完毕后 要制空 否则会阻断后面的变量</span>
        <span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span> = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-comment">// 执行更新</span>
    <span class="hljs-title function_">update</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">_cb</span>()
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Watcher</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建完<code>Dep</code>和<code>Watcher</code>之后，我们开始处理最后一步，也就是拦截修改，通知<code>Dep</code>修改，并让<code>Dep</code>通知<code>Watcher</code>修改</p>
<p>修改<code>defineReactive.js</code> <br>
当我们在模板中调用 <code>data</code> 时，我们需要将<code>Dep</code>订阅这个<code>data</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">Dep</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./dep.js"</span>;
<span class="hljs-comment">// 拦截器</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">defineReactive</span>(<span class="hljs-params">target, key, val</span>) &#123;
  <span class="hljs-comment">// Dep 订阅 data  一对一</span>
  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Dep</span>();
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
    <span class="hljs-title function_">get</span>(<span class="hljs-params"></span>) &#123;
      <span class="hljs-comment">// Dep.target 表示 Watcher，可以输出查看</span>
      <span class="hljs-comment">// Dep.target 如果有值，表示是在模板中使用了data，需要订阅</span>
      <span class="hljs-comment">// 如果只是在 js 中使用了，那么不进行订阅</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span>) &#123;
        <span class="hljs-comment">// 订阅</span>
        dep.<span class="hljs-title function_">depend</span>();
      &#125;
      <span class="hljs-keyword">return</span> val;
    &#125;,
    <span class="hljs-title function_">set</span>(<span class="hljs-params">value</span>) &#123;
      <span class="hljs-keyword">if</span> (val === value) <span class="hljs-keyword">return</span>;
      val = value;
      <span class="hljs-comment">// dep 通知 watcher更新</span>
      <span class="hljs-comment">// watcher 就是修改模板方法</span>
      dep.<span class="hljs-title function_">notify</span>();
    &#125;,
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们已经实现了响应式的原理，我们在控制台更改一下数据，看看是否能够完成响应式的更改</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/857bc2f381804232a891a91d0e5e8364~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="t13qa-g04ks.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">总结</h3>
<p><strong><code>Dep</code>是怎么与<code>data</code>进行绑定的</strong> <br>
答：当我们在模板中调用<code>data</code>时，会触发拦截器的<code>get()</code>方法，在这个方法里，会去判断是否是模板文件调用的<code>data</code>,我们在<code>new Watcher()</code>时，会将 <code>Dep.target</code> 指向当前 <code>Watcher</code>,我们通过<code>Dep.target</code>来判断是否是模板调用的<code>data</code>,如果是那么就将<code>Dep</code>订阅到<code>data</code></p>
<h3 data-id="heading-20">结尾</h3>
<p><code>Vue</code>的响应式设计原理，不论是<code>Vue2</code>还是<code>Vue3</code>,都是采用的<code>观察者模式</code>来实现的，这个设计模式不论是在工作中，还是在面试中，都非常的常见，而且非常的重要，如果感兴趣的话，可以去了解一下<code>js中的设计模式</code>，我想一定会对你的思路和间接有一定的提升</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fzxy_cns%2Fvue1x%2Ftree%2Fmaster%2FVue2Write" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/zxy_cns/vue1x/tree/master/Vue2Write" ref="nofollow noopener noreferrer">完整项目文件</a></p></div>  
</div>
            