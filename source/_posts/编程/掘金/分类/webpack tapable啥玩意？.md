
---
title: 'webpack tapable啥玩意？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa77b8438b54c7894e98a2ec861d714~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 02:16:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa77b8438b54c7894e98a2ec861d714~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在看webpack源码的时候，全篇布满了tapable Hooks，创建钩子、挂载钩子和调用钩子回调，看的hin～糟心，so，来吧，硬着头皮上吧！</p>
<p>刚才打开了webpack官网，api下发现webpack竟然有辣么多～的钩子，可以看到每一个钩子下方都会显示自己的钩子类型，这些钩子类型就是tapable提供的。而webpack也是靠这些钩子实现了复杂的功能，我们先来瞧一瞧这些钩子是咋用的，再去看webpack源码吧（🤦‍♀️）</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa77b8438b54c7894e98a2ec861d714~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一.同步钩子</h2>
<ol>
<li>SyncHook</li>
</ol>
<p>这是tapable最简单的一个钩子，它的用法非常简单：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">import</span> &#123; SyncHook &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'tapable'</span>;

<span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> SyncHook(); <span class="hljs-comment">// 创建钩子对象</span>
hook.tap(<span class="hljs-string">'test'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'钩子回调'</span>)); <span class="hljs-comment">// tap方法注册钩子回调</span>
hook.call(); <span class="hljs-comment">// call方法调用钩子，打印‘钩子回调’</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般来说，创建钩子、调用钩子都是在主流程代码中，注册钩子回调函数都是在插件代码中，这样就把插件想要实现的功能与主功能解耦了，插件的功能实际上是丰富了主流程的功能。</p>
<p><strong>向插件传递参数</strong>
需求：我们要在调用钩子的时候向绑定钩子的插件传递参数。
以webpack中一个钩子为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//主流程</span>
<span class="hljs-attr">compilation</span>: <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"compilation"</span>, <span class="hljs-string">"params"</span>]),
...
<span class="hljs-built_in">this</span>.hooks.compilation.call(compilation, params);
<span class="hljs-comment">// 插件</span>
compiler.hooks.compilation.tap(
      <span class="hljs-string">"SingleEntryPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        ...
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，需要在声明钩子的时候，告知它这个钩子需要两个参数，在调用钩子的时候就将这两个参数传入，这样在绑定该钩子的插件函数里就可以接收到这两个参数了。
这样，插件就可以操作主流程的参数了。</p>
<ol start="2">
<li>SyncBailHook</li>
</ol>
<p>bail在英文中的意思是“保释”，这里可以理解为离开，不再执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> <span class="hljs-built_in">this</span>.hooks.test = <span class="hljs-keyword">new</span> SyncBailHook()
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'one'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`one`</span>));
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'two'</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`two`</span>)); <span class="hljs-keyword">return</span> <span class="hljs-string">'success'</span>&#125;
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'three'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`three`</span>));

<span class="hljs-built_in">this</span>.hooks.test.call(); <span class="hljs-comment">// 会打印‘one’‘two’</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SyncBailHook这种类型的钩子会根据上一个钩子返回的值，决定要不要往下走，如果返回一个非undefined的值，就会停止执行之后所有的钩子回调函数。
用法：当一个模块满足A、B、C三个任意一个条件时，就将它单独打包，如果A、B、C需要按照一定的执行顺序时，就要用到SyncBailHook，如果 A 中返回为 true，那么就无须再去判断 B 和 C。</p>
<ol start="3">
<li>SyncWaterfallHook</li>
</ol>
<p>Waterfall在英文中意思为“瀑布”。这里可以理解为下一步需要依赖上一步的执行结果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> <span class="hljs-built_in">this</span>.hooks.test = <span class="hljs-keyword">new</span> SyncWaterfallHook([<span class="hljs-string">'num'</span>])
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'one'</span>, <span class="hljs-function">(<span class="hljs-params">num</span>) =></span> <span class="hljs-keyword">return</span> num + <span class="hljs-number">100</span>);
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'two'</span>, <span class="hljs-function">(<span class="hljs-params">num</span>) =></span> <span class="hljs-keyword">return</span> num + <span class="hljs-number">50</span>);
<span class="hljs-built_in">this</span>.hooks.test.tap(<span class="hljs-string">'three'</span>, <span class="hljs-function">(<span class="hljs-params">num</span>) =></span> <span class="hljs-built_in">console</span>.log(num));

<span class="hljs-built_in">this</span>.hooks.test.call(<span class="hljs-number">100</span>); <span class="hljs-comment">// 会打印250</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用法：当某一个数据需要依次经过A、B、C三个部分的处理，才能得到最后的数据</p>
<ol start="4">
<li>SyncLoopHook</li>
</ol>
<p>这个钩子应该比较好理解，可以理解为如果不返回非undefined值，就会一直执行这个回调函数。</p>
<h2 data-id="heading-1">二.异步钩子</h2>
<p>异步钩子用在当插件中的回调函数是异步的时候。</p>
<ol>
<li>AsyncParallelHook</li>
</ol>
<p>这是用来处理异步并行的钩子类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;AsyncParallelHook&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'tapable'</span>);
<span class="hljs-keyword">const</span> FrontEnd = <span class="hljs-keyword">new</span> AsyncParallelHook([<span class="hljs-string">'name'</span>]);
FrontEnd.tapAsync(<span class="hljs-string">'webpack'</span>,<span class="hljs-function">(<span class="hljs-params">name,cb</span>)=></span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(name+<span class="hljs-string">" get webpack "</span>)
    cb();
  &#125;, <span class="hljs-number">1000</span>);
 
&#125;);
FrontEnd.tapAsync(<span class="hljs-string">'react'</span>,<span class="hljs-function">(<span class="hljs-params">name,cb</span>)=></span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(name+<span class="hljs-string">" get react"</span>)
    cb();
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
  FrontEnd.callAsync(<span class="hljs-string">'小王'</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>);
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 输出结果</span>
小王 get webpack 
小王 get react
end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是网上的一个例子，挂载在钩子上的回调函数是并行执行的，没有任何的前后顺序，在插件的所有异步操作都完成后，会执行主流程中的回调函数。可以确保所有的插件的代码都执行完毕后，再执行某些逻辑。</p>
<ol start="2">
<li>AsyncParallelBailHook</li>
</ol>
<p>这个钩子功能同AsyncParallelHook类似，但是第一个插件注册的钩子执行结束后，会进行bail(熔断), 然后会调用最终的回调，无论其他插件是否执行完。</p>
<ol start="3">
<li>AsyncSeriesHook</li>
</ol>
<p>这是用来处理异步串行的钩子类型。
注册的异步回调函数依次执行，执行结束后，会执行主流程的回调函数。</p>
<ol start="4">
<li>AsyncSeriesBailHook</li>
</ol>
<p>串行执行，并且只要一个插件有返回值，立马调用最终的回调，并且不会继续执行后续的插件。</p>
<ol start="5">
<li>AsyncSeriesWaterfallHook</li>
</ol>
<p>串行执行，并且前一个插件的返回值，会作为后一个插件的参数。</p>
<p>钩子的类型大概可以分为以下几类：</p>
<ul>
<li>同步钩子。Sync开头的钩子</li>
<li>异步串行钩子。AsyncSeries开头的钩子。</li>
<li>异步并行钩子。AsyncParallel开头的钩子。</li>
</ul>
<p><strong>总结：</strong>
在webpack的整个编译打包过程中，暴露出大量的hook供内部和外部的插件使用，而webpack整个主流程的进行也依赖于这些hook，这些功能都是由Tapable实现的，从一个事件钩子到下一个事件钩子，驱动了webpack的整个编译过程。
Tapable其实就是典型的订阅发布模式，但是功能远比EventEmit强大许多，它提供了多种类型的钩子类型来满足不同插件需要的功能。且将插件的执行逻辑与主流程解耦，庞大的webpack却有很清晰的代码执行逻辑，与Tapable有不可分割的关系。</p>
<p>好啦，我们去看webpack源码吧～</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            