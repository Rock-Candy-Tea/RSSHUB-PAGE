
---
title: '你有一份Rx编程秘籍请签收'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2116a7ed865a485f846420768ca90a96~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:20:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2116a7ed865a485f846420768ca90a96~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>在学习Rx编程的过程中，理解Observable这个概念至关重要，常规学习过程中，通常需要进行多次“碰壁”才能逐渐“开悟”。这个有点像小时候学骑自行车，必须摔几次才能掌握一样。当然如果有办法能“言传”，则可以少走一些弯路，尽快领悟Rx的精妙。</p>
<h1 data-id="heading-1">二、Observable</h1>
<p>Observable从字面翻译来说叫做“可观察者”，换言之就是某种“数据源”或者“事件源”，这种数据源具有可被观察的能力，这个和你主动去捞数据有本质区别。用一个形象的比喻就是Observable好比是水龙头，你可以去打开水龙头——订阅Observable，然后水——数据就会源源不断流出。这就是响应式编程的核心思想——变主动为被动。不过这个不在本篇文章中详解。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2116a7ed865a485f846420768ca90a96~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源自网络）</p>
<p>Observable是一种概念，可以通过不同的方式去具体实现，本文通过高阶函数来实现两个常用Observable：fromEvent和Interval。通过讲解对Observable的订阅和取消订阅两个行为来帮助读者真正理解Observable是什么。</p>
<h1 data-id="heading-2">三、高阶函数</h1>
<p>高阶函数的概念来源于函数式编程，简单的定义就是一个函数的入参或者返回值是一个函数的函数。例如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">foo</span><span class="hljs-params">(arg)</span></span>&#123;
    <span class="hljs-keyword">return</span> function()&#123;
        console.log(arg)
    &#125;
&#125;
<span class="hljs-keyword">const</span> bar = foo(“hello world”)
bar()  <span class="hljs-comment">// hello world</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ps：高阶函数能做的事情很多，这里仅仅针对本文需要的情形进行使用。</p>
</blockquote>
<p>上面这个foo函数的调用并不会直接打印hello world，而只是把这个hello world给缓存起来。后面我们根据实际需要调用返回出来的bar函数，然后真正去执行打印hello world的工作。</p>
<p>为啥要做这么一步封装呢？实际上这么做的效果就是“延迟”了调用。而一切的精髓就在这个“延迟”两个字里面。我们实际上是对一种行为进行了包装，看上去就像某种一致的东西，好比是快递盒子。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbbe561e078a4899b8a1dfbe08d96c90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源自网络）</p>
<p>里面可以装不同的东西，但对于物流来说就是统一的东西。因此，就可以形成对快递盒的统一操作，比如堆叠、运输、存储、甚至是打开盒子这个动作也是一致的。</p>
<p>回到前面的例子，调用foo函数，相当于打包了一个快递盒，这个快递盒里面有一个固定的程序，就是当打开这个快递盒（调用bar）时执行一个打印操作。</p>
<p>我们可以有foo1、foo2、foo3……里面有各种各样的程序，但是这些foos，都有一个共同的操作就是“打开”。（前提是这个foo会返回一个函数，这样才能满足“打开”的操作，即调用返回的函数）。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">foo1</span><span class="hljs-params">(arg)</span></span>&#123;
    <span class="hljs-keyword">return</span> function()&#123;
       console.log(arg+<span class="hljs-string">"?"</span>)
    &#125;
&#125;
<span class="hljs-function">function <span class="hljs-title">foo2</span><span class="hljs-params">(arg)</span></span>&#123;
      <span class="hljs-keyword">return</span> function()&#123;
         console.log(arg+<span class="hljs-string">"!"</span>)
     &#125;
&#125;
<span class="hljs-keyword">const</span> bar1 = foo1(“hello world”)
<span class="hljs-keyword">const</span> bar2 = foo2(<span class="hljs-string">"yes"</span>)
bar1()+bar2() <span class="hljs-comment">// hello world? yes!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">四、快递盒模型</h1>
<h2 data-id="heading-4">4.1 快递盒模型1：fromEvent</h2>
<p>有了上面的基础，下面我们就来看一下Rx编程中最常用的一个Observable—fromEvent(……)。对于Rx编程的初学者，起初很难理解fromEvent(……)和addEventListener(……)有什么区别。</p>
<pre><code class="hljs language-java copyable" lang="java">btn.addEventListener(<span class="hljs-string">"click"</span>,callback)
rx.fromEvent(btn,<span class="hljs-string">"click"</span>).subscribe(callback)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果直接执行这个代码，确实效果是一样的。那么区别在哪儿呢？最直接的区别是，subscribe函数作用在fromEvent(……)上而不是btn上，而addEventListener是直接作用在btn上的。subscribe函数是某种“打开”操作，而fromEvent(……)则是某种快递盒。</p>
<p>fromEvent实际上是对addEventListener的“延迟”调用</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">fromEvent</span><span class="hljs-params">(target,evtName)</span></span>&#123;
    <span class="hljs-keyword">return</span> function(callback)&#123;
        target.addEventListener(evtName,callback)
    &#125;
&#125;
<span class="hljs-keyword">const</span> ob = fromEvent(btn,<span class="hljs-string">"click"</span>)
ob(console.log)<span class="hljs-comment">// 相当于 subscribe</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>哦！fromEvent本质上是高阶函数</strong></p>
<p>至于如何实现subscribe来完成“打开”操作，不在本文讨论范围，在Rx编程中，这个subscribe的动作叫做“订阅”。“订阅”就是所有Observable的统一具备的操作。再次强调：本文中对Observable的“调用”在逻辑上相当于subscribe。</p>
<p>下面再举一个例子，基本可以让读者举二反N了。</p>
<h2 data-id="heading-5">4.2 快递盒模型2：interval</h2>
<p>Rx中有一个interval，它和setInterval有什么区别呢？</p>
<p>估计有人已经开始抢答了，interval就是对setInterval的延迟调用！bingo！</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">interval</span><span class="hljs-params">(period)</span></span>&#123;
    let i = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> function(callback)&#123;
        setInterval(period,()=>callback(i++))
    &#125;
&#125;
<span class="hljs-keyword">const</span> ob = interval(<span class="hljs-number">1000</span>)
ob(console.log)<span class="hljs-comment">// 相当于 subscribe</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面两个例子来看，无论是fromEvent(……)还是Interval(……)，虽然内部是完全不同的逻辑，但是他们同属于“快递盒”这种东西，我们把它称之为<strong>Observable</strong>——<strong>可观察者</strong>。</p>
<p>fromEvent和Interval本身只是制作“快递盒”的模型，只有调用后返回的东西才是“快递盒”，即fromEvent(btn,"click")、interval(1000) 等等...</p>
<h1 data-id="heading-6">五、高阶快递盒</h1>
<p>有了上面的基础，下面开始进阶：我们拥有了那么多快递盒，那么就可以对这些快递盒再封装。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93a43005d25644ae88452ba083a0d7f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在文章开头说了，快递盒统一了一些操作，所以我们可以把许许多多的快递盒堆叠在一起，即组合成一个大的快递盒！这个大的快递盒和小的快递盒一样，具有“打开”操作（即订阅）。当我们打开这个大的快递盒的时候，会发生什么呢？</p>
<p>可以有很多种不同的可能性，比如可以逐个打开小的快递盒（concat），或者一次性打开所有小的快递盒（merge），也可以只打开那个最容易打开的快递盒（race）。</p>
<p>下面是一个简化版的merge方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">merge</span><span class="hljs-params">(...obs)</span></span>&#123;
    <span class="hljs-keyword">return</span> function(callback)&#123;
        obs.forEach(ob=>ob(callback)) <span class="hljs-comment">// 打开所有快递盒</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还是拿之前的fromEvent和interval来举例吧！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bb5a4f862244548b591a72462ec2215~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用merge方法对两个Observable进行组合：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">const</span> ob1 = fromEvent(btn,<span class="hljs-string">'click'</span>) <span class="hljs-comment">// 制作快递盒1</span>
<span class="hljs-keyword">const</span> ob2 = interval(<span class="hljs-number">1000</span>) <span class="hljs-comment">// 制作快递盒2</span>
<span class="hljs-keyword">const</span> ob = merge(ob1,ob2) <span class="hljs-comment">//制作大快递盒</span>
ob(console.log) <span class="hljs-comment">// 打开大快递盒</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们“打开”（订阅）这个大快递盒ob的时候，其中两个小快递盒也会被“打开”（订阅），任意一个小快递盒里面的逻辑都会被执行，我们就合并（merge）了两个Observable，变成了一个。</p>
<p>这就是我们为什么要辛辛苦苦把各种异步函数封装成快递盒（Observable）的原因了——方便对他们进行统一操作！当然仅仅只是“打开”（订阅）这个操作只是最初级的功能，下面开始进阶。</p>
<h1 data-id="heading-7">六、销毁快递盒</h1>
<h2 data-id="heading-8">6.1 销毁快递盒——取消订阅</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7df5f4ad9acb410b8e45e48302a11bba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还是以fromEvent为例子，之前我们写了一个简单的高阶函数，作为对addEventListener的封装：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">fromEvent</span><span class="hljs-params">(target,evtName)</span></span>&#123;
    <span class="hljs-keyword">return</span> function(callback)&#123;
        target.addEventListener(evtName,callback)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们调用这个函数的时候，就生成了一个快递盒（fromEvent(btn,'click'))。当我们调用了这个函数返回的函数的时候，就是打开了快递盒（fromEvent(btn,'click')(console.log)）。</p>
<p><strong>那么我们怎么去销毁这个打开的快递盒呢？</strong></p>
<p>首先我们需要得到一个已经打开的快递盒，上面的函数调用结果是void，我们无法做任何操作，所以我们需要构造出一个打开状态的快递盒。还是使用高阶函数的思想：在返回的函数里面再返回一个函数，用于销毁操作。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">fromEvent</span><span class="hljs-params">(target,evtName)</span></span>&#123;
    <span class="hljs-keyword">return</span> function(callback)&#123;
        target.addEventListener(evtName,callback)
        <span class="hljs-keyword">return</span> function()&#123;
            target.removeEventListener(evtName,callback)
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">const</span> ob = fromEvent(btn,<span class="hljs-string">'click'</span>) <span class="hljs-comment">// 制作快递盒</span>
<span class="hljs-keyword">const</span> sub = ob(console.log) <span class="hljs-comment">// 打开快递盒，并得到一个可用于销毁的函数</span>
sub() <span class="hljs-comment">// 销毁快递盒</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理，对于interval，我们也可以如法炮制：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">interval</span><span class="hljs-params">(period)</span></span>&#123;
    let i = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> function(callback)&#123;
        let id = setInterval(period,()=>callback(i++))
        <span class="hljs-keyword">return</span> function()&#123;
            clearInterval(id)
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">const</span> ob = interval(<span class="hljs-number">1000</span>) <span class="hljs-comment">// 制作快递盒</span>
<span class="hljs-keyword">const</span> sub = ob(console.log) <span class="hljs-comment">// 打开快递盒</span>
sub() <span class="hljs-comment">// 销毁快递盒</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">6.2 销毁高阶快递盒</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97539e13c08c4e078d6279504c2239ef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们以merge为例：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">function <span class="hljs-title">merge</span><span class="hljs-params">(...obs)</span></span>&#123;
    <span class="hljs-keyword">return</span> function(callback)&#123;
        <span class="hljs-keyword">const</span> subs = obs.map(ob=>ob(callback)) <span class="hljs-comment">// 订阅所有并收集所有的销毁函数</span>
        <span class="hljs-keyword">return</span> function()&#123;
            subs.forEach(sub=>sub()) <span class="hljs-comment">// 遍历销毁函数并执行</span>
        &#125;
    &#125;
&#125;
 
<span class="hljs-keyword">const</span> ob1 = fromEvent(btn,<span class="hljs-string">'click'</span>) <span class="hljs-comment">// 制作快递盒1</span>
<span class="hljs-keyword">const</span> ob2 = interval(<span class="hljs-number">1000</span>) <span class="hljs-comment">// 制作快递盒2</span>
<span class="hljs-keyword">const</span> ob = merge(ob1,ob2) <span class="hljs-comment">//制作大快递盒</span>
<span class="hljs-keyword">const</span> sub = ob(console.log) <span class="hljs-comment">// 打开大快递盒</span>
sub() <span class="hljs-comment">// 销毁大快递盒</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们销毁大快递盒的时候，就会把里面所有的小快递盒一起销毁。</p>
<h1 data-id="heading-10">六、补充</h1>
<p>到这里我们已经将Observable的两个重要操作（订阅、取消订阅）讲完了，值得注意的是，取消订阅这个行为并非是作用于Observable上，而是作用于已经“打开”的快递盒（订阅Observable后返回的东西）之上！</p>
<p>Observable除此以外，还有两个重要操作，即发出事件、完成/异常，（这两个操作属于是由Observable主动发起的回调，和操作的方向是相反的，所以其实不能称之为操作）。</p>
<p>这个两个行为用快递盒就不那么形象了，我们可以将Observable比做是水龙头，原先的打开快递盒变成拧开水龙头，而我们传入的回调函数就可以比喻成接水的水杯！由于大家对回调函数已经非常熟悉了，所以本文就不再赘述了。</p>
<h1 data-id="heading-11">七、后记</h1>
<p>总结一下我们学习的内容，我们通过高阶函数将一些操作进行了“延迟”，并赋予了统一的行为，比如“订阅”就是延迟执行了异步函数，“取消订阅”就是在上面的基础上再“延迟”执行了销毁资源的函数。</p>
<p>这些所谓的“延迟”执行就是Rx编程中幕后最难理解，也是最核心的部分。Rx的本质就是将异步函数封装起来，然后抽象成四大行为：订阅、取消订阅、发出事件、完成/异常。</p>
<p>实际实现Rx库的方法有很多，本文只是利用了高阶函数的思想来帮助大家理解Observable的本质，在官方实现的版本中，Observable这个快递盒并非是高阶函数，而是一个对象，但本质上是一样的，这里引出了一个话题：函数式编程与面向对象的异同，请听下回分解。</p>
<blockquote>
<p>作者：vivo互联网开发团队-Li Yuxiang</p>
</blockquote></div>  
</div>
            