
---
title: 'JavaScript系列 -- 设计模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b6b27c438d4626addaee5396ccccee~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 22:14:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b6b27c438d4626addaee5396ccccee~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>设计模式是一种<strong>思想</strong>，就像是前人记录下来的经验，就好比是厨师日积月累的经验撰写出来的菜谱</p>
<p>这是定义：</p>
<blockquote>
<p>设计模式是：在面向对象 <strong>软件设计过程</strong> 中针对 <strong>特定问题</strong> 的<code>简洁</code>而<code>优雅</code>的<strong>解决方案</strong></p>
</blockquote>
<p>优雅是指不粗暴，简洁是因为规范化了，我们需要在日常开发中潜意识里去用这样一种思想，这样团队协作，后期的维护、迭代等等之类的会避免不少麻烦</p>
<p>这里只介绍在 JavaScript 中常见的几种设计模式，其他的设计模式详见 <a href="https://juejin.cn/post/6963138441395568653#heading-6" target="_blank">参考文章</a></p>
<h2 data-id="heading-1">单例模式</h2>
<p><strong>应用场景</strong></p>
<p>一个 <code>button</code> 的点击事件是触发弹窗，那无论用户是否重复点击，<strong>弹窗只会创建一个</strong></p>
<p><strong>定义</strong></p>
<blockquote>
<p>单例模式也称为单体模式，规定一个类 <strong>只有一个实例</strong>，并且提供可全局访问点</p>
</blockquote>
<p><strong>具体实现</strong></p>
<p>实现的方法为先判断<code>实例存在与否</code>，如果存在则 <strong>直接返回</strong>，如果不存在就 <strong>创建了再返回</strong>，这就确保了一个类只有一个实例对象。</p>
<p>其中利用了：ES6 的 let 不允许重复声明的特性</p>
<p><strong>方法一：if...else 来判断是否已经存在</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Singleton = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.instance = <span class="hljs-literal">null</span>; 
&#125;
Singleton.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
Singleton.getInstance = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.instace)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance; 
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance = <span class="hljs-keyword">new</span> Singleton(name);
&#125;

<span class="hljs-keyword">let</span> winner = Singleton.getInstance(<span class="hljs-string">"winner"</span>);
<span class="hljs-built_in">console</span>.log(winner.getName());   <span class="hljs-comment">// winner</span>
<span class="hljs-keyword">let</span> sunner = Singleton.getInstance(<span class="hljs-string">"sunner"</span>);
<span class="hljs-built_in">console</span>.log(sunner.getName());   <span class="hljs-comment">// winner</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：<strong>创建对象</strong> 的操作和 <strong>判断实例</strong> 的操作<code>耦合</code>在一起，并不符合“<code>单一职责原则</code>”</p>
<p><strong>方法二：利用自执行函数，将创建对象和判断实例分开</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ProxyCreateSingleton = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(instance)&#123;
            <span class="hljs-keyword">return</span> instance
        &#125;
        <span class="hljs-keyword">return</span> instance = <span class="hljs-keyword">new</span> Singlton(name);
    &#125;
&#125;)();
    
<span class="hljs-keyword">let</span> Singlton = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125; 
Singlton.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;

<span class="hljs-keyword">let</span> winner = <span class="hljs-keyword">new</span> ProxyCreateSingleton(<span class="hljs-string">"winner"</span>);
<span class="hljs-built_in">console</span>.log(winner.getName());   <span class="hljs-comment">// winner</span>
<span class="hljs-keyword">let</span> sunner = <span class="hljs-keyword">new</span> ProxyCreateSingleton(<span class="hljs-string">"sunner"</span>);
<span class="hljs-built_in">console</span>.log(sunner.getName());   <span class="hljs-comment">// winner</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中，ProxyCreateSingleton()只负责 <strong>判断实例</strong>，Singlton只负责 <strong>创建对象和赋值</strong></p>
<h2 data-id="heading-2">策略模式</h2>
<p><strong>应用场景</strong></p>
<p>举个非常简单的例子，一个检验表单的程序：用户输入姓名、性别、年龄、身份证号、手机号等等信息后提交表单，我们首先要检查哪一项没有填写，然后再各自检查输入内容是否合法。</p>
<p><strong>定义</strong></p>
<blockquote>
<p>策略模式的定义：定义 <strong>一系列的算法</strong>，把他们一个个 <strong>封装起来</strong>，并且使他们可以 <strong>相互替换</strong></p>
</blockquote>
<blockquote>
<p>基于策略模式的程序至少由两部分组成：</p>
<ul>
<li>策略类：封装了具体的算法，并负责具体的计算过程</li>
<li>环境类：接受客户的请求，随后将请求委托给某一个策略类</li>
</ul>
</blockquote>
<p><strong>具体实现</strong></p>
<p><strong>1. 使用策略模式前：一大堆的if...return...</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> checkAuth = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(data.name === <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"姓名项不能为空"</span>) <span class="hljs-comment">// 当然里面还可以继续写其他对结果的处理代码，这里省略了</span>
    &#125;
    <span class="hljs-keyword">if</span>(data.gender === <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"性别项不能为空"</span>)
    &#125;
    <span class="hljs-keyword">if</span>(data.age === <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"年龄项不能为空"</span>)
    &#125;
    <span class="hljs-keyword">if</span>(data.id === <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"您未输入身份证号"</span>)
    &#125;
    <span class="hljs-keyword">if</span>(data.phoneNumber === <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"您未输入手机号"</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<ul>
<li>时间上不够优化</li>
<li>checkAuth 函数会爆炸 💥</li>
<li>策略项无法复用</li>
<li>违反开闭原则</li>
</ul>
<p><strong>2. 使用策略模式后：obj + function</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*策略类*/</span>
<span class="hljs-keyword">var</span> checkObj = &#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(!value) <span class="hljs-keyword">return</span> <span class="hljs-string">"姓名项不能为空"</span>;
    &#125;,
    <span class="hljs-string">"gender"</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(!value) <span class="hljs-keyword">return</span> <span class="hljs-string">"性别项不能为空"</span>;
    &#125;,
    <span class="hljs-string">"age"</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(!value) <span class="hljs-keyword">return</span> <span class="hljs-string">"年龄项不能为空"</span>;
    &#125;,
    <span class="hljs-string">"id"</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(!value) <span class="hljs-keyword">return</span> <span class="hljs-string">"您未输入身份证号"</span>;
    &#125;,
    <span class="hljs-string">"phoneNumber"</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(!value) <span class="hljs-keyword">return</span> <span class="hljs-string">"您未输入手机号"</span>;
    &#125;
&#125;;

<span class="hljs-comment">/*环境类*/</span>
<span class="hljs-keyword">var</span> calculateBouns = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Object</span>.entires(data)
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> arr)&#123;
        <span class="hljs-keyword">var</span> res = checkObj[ arr[i][<span class="hljs-number">0</span>] ]( arr[i][<span class="hljs-number">1</span>] )
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
&#125;;

<span class="hljs-comment">// 还能只单独调用其中一个方法</span>
<span class="hljs-keyword">var</span> res = checkObj[<span class="hljs-string">"age"</span>](<span class="hljs-string">""</span>);
<span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// "年龄项不能为空"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只是简单举例，在 data 对象里直接拿取其属性去 checkObj 对象里面找由其命名的方法，然后传入对应属性的值，即可快速抵达。然后后期对各个方法修改起来也方便</p>
<p>这是两种方式的对比：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b6b27c438d4626addaee5396ccccee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">发布 - 订阅模式</h2>
<p><strong>应用场景</strong></p>
<p>需求 : 申请成功后，需要触发对应的订单、消息、审核模块对应逻辑</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d739205f61014be8a8f0756fcf7c1cfa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有其他类似场景：怎么模仿 报社发报的流程 做 公众号推文发布和通知 的功能、小程序抽奖结果通知等等</p>
<p><strong>定义</strong></p>
<blockquote>
<p>发布-订阅模式其实是一种对象间一对多的依赖关系，当一个对象的状态发送改变时，所有依赖于它的对象都将得到状态改变的通知</p>
</blockquote>
<p><strong>具体实现</strong></p>
<p><strong>1. 使用发布 - 订阅模式前：</strong></p>
<p>一个函数包裹三个函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applySuccess</span>(<span class="hljs-params"></span>) </span>&#123;
    MessageCenter.fetch(); <span class="hljs-comment">// 通知消息中心获取最新内容</span>
    Order.update(); <span class="hljs-comment">// 更新订单信息</span>
    Checker.alert(); <span class="hljs-comment">// 通知相关方审核</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<ul>
<li>如果上面的函数还没完成 / 有错误，则下面的函数就会被卡死（无法运行、无法调试）</li>
<li>本应该是并行处理的，结果是串行处理</li>
</ul>
<p><strong>2. 使用发布 - 订阅模式后：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66f97bd23566468182554fbac39fd009~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>实现思路</strong></p>
<ol>
<li>创建一个对象</li>
<li>在该对象上创建一个缓存列表（调度中心）</li>
<li>on 方法用来把函数 fn 都加到缓存列表中（订阅者注册事件到调度中心）</li>
<li>emit 方法取到 arguments 里第一个当做 event，根据 event 值去执行对应缓存列表中的函数（发布者发布事件到调度中心，调度中心处理代码）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 公众号对象</span>
<span class="hljs-keyword">let</span> eventEmitter = &#123;&#125;;

<span class="hljs-comment">// 缓存列表，存放 event 及 fn</span>
eventEmitter.list = &#123;&#125;;

<span class="hljs-comment">// 订阅</span>
eventEmitter.on = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event, fn</span>) </span>&#123;
    <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 如果对象中没有对应的 event 值，也就是说明没有订阅过，就给 event 创建个缓存列表</span>
    <span class="hljs-comment">// 如有对象中有相应的 event 值，把 fn 添加到对应 event 的缓存列表里</span>
    (that.list[event] || (that.list[event] = [])).push(fn);
    <span class="hljs-keyword">return</span> that;
&#125;;

<span class="hljs-comment">// 发布</span>
eventEmitter.emit = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 第一个参数是对应的 event 值，直接用数组的 shift 方法取出</span>
    <span class="hljs-keyword">let</span> event = [].shift.call(<span class="hljs-built_in">arguments</span>),
        fns = [...that.list[event]];
    <span class="hljs-built_in">console</span>.log(event) <span class="hljs-comment">// 'notice'</span>
    <span class="hljs-built_in">console</span>.log(fns) <span class="hljs-comment">// [f user1(content), f user2(content), f user3(content)]</span>
    <span class="hljs-comment">// 如果缓存列表里没有 fn 就返回 false</span>
    <span class="hljs-keyword">if</span> (!fns || fns.length === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-comment">// 遍历 event 值对应的缓存列表，依次执行 fn</span>
    fns.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> &#123;
        fn.apply(that, <span class="hljs-built_in">arguments</span>);
    &#125;);
    <span class="hljs-keyword">return</span> that;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user1</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(content === <span class="hljs-string">'success'</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'收到申请成功的通知，开始执行 MessageCenter.fetch 函数'</span>);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user2</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(content === <span class="hljs-string">'success'</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'收到申请成功的通知，开始执行 Order.update 函数'</span>);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user3</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(content === <span class="hljs-string">'success'</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'收到申请成功的通知，开始执行 Checker.alert 函数'</span>);
&#125;;

<span class="hljs-comment">// 订阅者发起订阅</span>
eventEmitter.on(<span class="hljs-string">'notice'</span>, user1);
eventEmitter.on(<span class="hljs-string">'notice'</span>, user2);
eventEmitter.on(<span class="hljs-string">'notice'</span>, user3);

<span class="hljs-comment">// 发布者发布内容</span>
eventEmitter.emit(<span class="hljs-string">'notice'</span>, <span class="hljs-string">'success'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b07913608460443f996f2af6e70d77c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>补充 once 、off 方法</strong></p>
<ol start="5">
<li>off 方法可以<code>根据 event 值</code>取消订阅（取消订阅）</li>
<li>once 方法只监听一次，调用完毕后<strong>删除缓存函数</strong>（订阅一次）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> eventEmitter = &#123;
    <span class="hljs-comment">// 缓存列表</span>
    <span class="hljs-attr">list</span>: &#123;&#125;,
    <span class="hljs-comment">// 订阅</span>
    on (event, fn) &#123;
        <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// 如果对象中没有对应的 event 值，也就是说明没有订阅过，就给 event 创建个缓存列表</span>
        <span class="hljs-comment">// 如有对象中有相应的 event 值，把 fn 添加到对应 event 的缓存列表里</span>
        (_this.list[event] || (_this.list[event] = [])).push(fn);
        <span class="hljs-keyword">return</span> _this;
    &#125;,
    <span class="hljs-comment">// 监听一次</span>
    once (event, fn) &#123;
        <span class="hljs-comment">// 先绑定，调用后删除</span>
        <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">on</span> (<span class="hljs-params"></span>) </span>&#123;
            _this.off(event, on);
            fn.apply(_this, <span class="hljs-built_in">arguments</span>);
        &#125;
        on.fn = fn;
        _this.on(event, on);
        <span class="hljs-keyword">return</span> _this;
    &#125;,
    <span class="hljs-comment">// 取消订阅</span>
    off (event, fn) &#123;
        <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">let</span> fns = _this.list[event];
        <span class="hljs-comment">// 如果缓存列表中没有相应的 fn，返回false</span>
        <span class="hljs-keyword">if</span> (!fns) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">if</span> (!fn) &#123;
            <span class="hljs-comment">// 如果没有传 fn 的话，就会将 event 值对应缓存列表中的 fn 都清空</span>
            fns && (fns.length = <span class="hljs-number">0</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 若有 fn，遍历缓存列表，看看传入的 fn 与哪个函数相同，如果相同就直接从缓存列表中删掉即可</span>
            <span class="hljs-keyword">let</span> cb;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, cbLen = fns.length; i < cbLen; i++) &#123;
                cb = fns[i];
                <span class="hljs-keyword">if</span> (cb === fn || cb.fn === fn) &#123;
                    fns.splice(i, <span class="hljs-number">1</span>);
                    <span class="hljs-keyword">break</span>
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> _this;
    &#125;,
    <span class="hljs-comment">// 发布</span>
    emit () &#123;
        <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// 第一个参数是对应的 event 值，直接用数组的 shift 方法取出</span>
        <span class="hljs-keyword">let</span> event = [].shift.call(<span class="hljs-built_in">arguments</span>),
            fns = [..._this.list[event]];
        <span class="hljs-comment">// 如果缓存列表里没有 fn 就返回 false</span>
        <span class="hljs-keyword">if</span> (!fns || fns.length === <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-comment">// 遍历 event 值对应的缓存列表，依次执行 fn</span>
        fns.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> &#123;
            fn.apply(_this, <span class="hljs-built_in">arguments</span>);
        &#125;);
        <span class="hljs-keyword">return</span> _this;
    &#125;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user1</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'用户1订阅了:'</span>, content);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user2</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'用户2订阅了:'</span>, content);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user3</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'用户3订阅了:'</span>, content);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user4</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'用户4订阅了:'</span>, content);
&#125;

<span class="hljs-comment">// 订阅</span>
eventEmitter.on(<span class="hljs-string">'article1'</span>, user1);
eventEmitter.on(<span class="hljs-string">'article1'</span>, user2);
eventEmitter.on(<span class="hljs-string">'article1'</span>, user3);

<span class="hljs-comment">// 取消user2方法的订阅</span>
eventEmitter.off(<span class="hljs-string">'article1'</span>, user2);

eventEmitter.once(<span class="hljs-string">'article2'</span>, user4)

<span class="hljs-comment">// 发布</span>
eventEmitter.emit(<span class="hljs-string">'article1'</span>, <span class="hljs-string">'Javascript 发布-订阅模式'</span>);
eventEmitter.emit(<span class="hljs-string">'article1'</span>, <span class="hljs-string">'Javascript 发布-订阅模式'</span>);
eventEmitter.emit(<span class="hljs-string">'article2'</span>, <span class="hljs-string">'Javascript 观察者模式'</span>);
eventEmitter.emit(<span class="hljs-string">'article2'</span>, <span class="hljs-string">'Javascript 观察者模式'</span>);

<span class="hljs-comment">// eventEmitter.on('article1', user3).emit('article1', 'test111');</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c4e4b4eaebc44e4b31abd77dc678c27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由打印结果可看出：</p>
<ul>
<li>user2 虽然 on 订阅了但是<code>又 off 取消了订阅</code>，所以发布者发布的所有内容 user2 <code>全都没有收到</code></li>
<li>只有 user4 订阅了 article2 ，所以虽然发布者<code>发布了两次</code> article2 的内容，但是 user4 <code>只收到一次</code></li>
</ul>
<h2 data-id="heading-4">观察者模式</h2>
<p><strong>应用场景</strong></p>
<p>应用场景与发布-订阅模式类似</p>
<p><strong>定义</strong></p>
<blockquote>
<p>观察者模式就是：设置多个观察者（Observers）观察监听某个被观察对象（Subject），当有关状态发生变化时，Subject 会通知这一系列 Observers 触发更新</p>
</blockquote>
<p>可以理解为：一个班里的学生们都在听老师讲课，当老师布置任务时，会通知学生们都去执行</p>
<p><strong>具体实现</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 被观察者</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Subject</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.observers = [];
&#125;
Subject.prototype = &#123;
    <span class="hljs-comment">// 添加观察者</span>
    <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">observer</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.observers.push(observer);
    &#125;,
    <span class="hljs-comment">// 通知观察者</span>
    <span class="hljs-attr">notify</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> observers = <span class="hljs-built_in">this</span>.observers;
        <span class="hljs-keyword">var</span> len = observers.length;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<len; i++)&#123;
            observers[i].update();
        &#125;
    &#125;,
    <span class="hljs-comment">// 移除观察者</span>
    <span class="hljs-attr">remove</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">observer</span>) </span>&#123;
        <span class="hljs-keyword">var</span> observers = <span class="hljs-built_in">this</span>.observers;
        <span class="hljs-keyword">var</span> len = observers.length;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<len; i++)&#123;
            <span class="hljs-keyword">if</span>(observers[i] === observer) &#123;
                observers.splice(i, <span class="hljs-number">1</span>);
            &#125;
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 观察者</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Observer</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Observer.prototype = &#123;
    <span class="hljs-comment">// 观察者监听到变化后要处理的逻辑</span>
    <span class="hljs-attr">update</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'收到通知，我是观察者：'</span>, <span class="hljs-built_in">this</span>.name);
    &#125;
&#125;

<span class="hljs-comment">// 创建观察者</span>
<span class="hljs-keyword">var</span> observer1 = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'John'</span>);
<span class="hljs-keyword">var</span> observer2 = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'Alice'</span>);

<span class="hljs-comment">// 添加观察者</span>
<span class="hljs-keyword">var</span> subject = <span class="hljs-keyword">new</span> Subject();
subject.add(observer1);
subject.add(observer2);

<span class="hljs-comment">// 发起通知</span>
subject.notify();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aea13552f3514fefa24bfc2f61b5ca37~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">发布-订阅模式与观察者模式的区别</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b547b629df404f9f8ef38bae78e779eb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单来说，<strong>发布订阅模式</strong> 比 <strong>观察者模式</strong> 多了一层 <code>Event Channel</code></p>
<p><strong>观察者模式</strong>：观察者（Observer）<code>直接订阅</code>（Subscribe）主题（Subject），而当主题被激活的时候，会触发（Fire Event）观察者里的事件。</p>
<p><strong>发布订阅模式</strong>：订阅者（Subscriber）把自己想订阅的事件注册（Subscribe）到调度中心（Event Channel），当发布者（Publisher）发布该事件（Publish Event）到调度中心，也就是该事件触发时，由调度中心<code>统一调度</code>（Fire Event）订阅者注册到调度中心的处理代码。</p>
<p><strong>差异：</strong></p>
<ul>
<li>在<strong>观察者模式</strong>中，观察者是<code>知道 Subject </code>的，Subject 一直保持对观察者进行记录。而在<strong>发布订阅模式</strong>中，发布者和订阅者不知道对方的存在。它们只有通过<code>消息代理</code>进行通信。</li>
<li>在<strong>发布订阅模式</strong>中，组件是<code>松散耦合</code>的，正好和<strong>观察者模式</strong>相反。</li>
<li><strong>观察者模式</strong>大多数时候是<code>同步</code>的，比如当事件触发，Subject 就会去调用观察者的方法。而<strong>发布-订阅模式</strong>大多数时候是<code>异步</code>的（使用消息队列）。</li>
<li><strong>观察者模式</strong>需要在单个应用程序地址空间中实现，而<strong>发布-订阅模式</strong>更像交叉应用模式。</li>
</ul>
<h2 data-id="heading-6">参考文章</h2>
<ul>
<li><a href="https://www.cnblogs.com/dengyao-blogs/p/11652566.html" target="_blank" rel="nofollow noopener noreferrer">JavaScript设计模式——单例模式</a></li>
<li><a href="https://segmentfault.com/a/1190000019260857" target="_blank" rel="nofollow noopener noreferrer">JavaScript 发布-订阅模式</a></li>
<li><a href="https://juejin.cn/post/6844903607452581896" target="_blank">前端渣渣唠嗑一下前端中的设计模式（真实场景例子）</a></li>
<li><a href="https://juejin.cn/post/6844903503266054157" target="_blank">JavaScript设计模式</a></li>
<li><a href="https://juejin.cn/post/6844903607452581896" target="_blank">JavaScript 中常见设计模式整理</a></li>
</ul></div>  
</div>
            