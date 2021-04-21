
---
title: 'webpack核心模块-tapable'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://intranetproxy.alipay.com/skylark/lark/0/2020/svg/282482/1588141393634-869a59e7-aff6-409e-a38b-e78919da0a1c.svg'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 19:27:33 GMT
thumbnail: 'https://intranetproxy.alipay.com/skylark/lark/0/2020/svg/282482/1588141393634-869a59e7-aff6-409e-a38b-e78919da0a1c.svg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">简介</h3>
<p>在看L7源码时，看到我们使用了webpack的核心模块<a href="https://github.com/webpack/tapable" target="_blank" rel="nofollow noopener noreferrer">tapable</a>，这个模块是连接webpack各个plugin的关键纽带，简单的说，如果不了解tapable，那肯定看不懂webpack的源码，对于各个plugin的调用机制也不会清楚。</p>
<h3 data-id="heading-1">总览</h3>
<p>tapable我们可以简单的把它理解成webpack中的EventEmitter，用来发布和订阅消息。它暴露了很多hook，这些hook都是为自定义的plugin挂载提供的：
<img alt class="lazyload" src="https://intranetproxy.alipay.com/skylark/lark/0/2020/svg/282482/1588141393634-869a59e7-aff6-409e-a38b-e78919da0a1c.svg" data-width="800" data-height="600" referrerpolicy="no-referrer">### 基础用法
可以知道tapable分为同步和异步两种hook，要注意的是异步hook分为并行和串行，而同步hook自然都是串行的。
先了解一下注册和触发的方法：</p>




















<table><thead><tr><th></th><th>同步Hook</th><th>异步Hook</th></tr></thead><tbody><tr><td>注册</td><td>tap</td><td>tapAsync，tapPromise，tap</td></tr><tr><td>触发</td><td>call</td><td>callAsync，promise</td></tr></tbody></table>
<p>最好在Class的构造函数中使用new初始化Hook：接受一个数组参数，触发方法会根据传参，接受同样数量的参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Kunkun</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.hooks = &#123;
      <span class="hljs-attr">sing</span>: <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"song"</span>]),
      <span class="hljs-attr">dance</span>: <span class="hljs-keyword">new</span> SyncWaterfallHook([<span class="hljs-string">'danceName'</span>]),
      <span class="hljs-attr">rap</span>: <span class="hljs-keyword">new</span> SyncBailHook(),
      <span class="hljs-attr">basketball</span>: AsyncSeriesHook([<span class="hljs-string">"shot"</span>]),
    &#125;;
  &#125;
&#125;
<span class="hljs-keyword">const</span> kunkun = <span class="hljs-keyword">new</span> Kunkun();

<span class="hljs-comment">// 注册方法</span>
<span class="hljs-comment">// 有参数</span>
kunkun.hooks.sing.tap(<span class="hljs-string">"GoSing"</span>, <span class="hljs-function"><span class="hljs-params">song</span> =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`唱了一首<span class="hljs-subst">$&#123;song&#125;</span>`</span>)&#125;);
<span class="hljs-comment">// 无参数</span>
kunkun.hooks.dance.tap(<span class="hljs-string">"GoDance"</span>, <span class="hljs-function"><span class="hljs-params">danceName</span> =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`跳了一支<span class="hljs-subst">$&#123;danceName&#125;</span>`</span>)&#125;);
kunkun.hooks.rap.tap(<span class="hljs-string">"GoRap"</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'来了一首Rap'</span>)&#125;);
<span class="hljs-comment">// 注册异步函数</span>
kunkun.hooks.basketball.tapPromise(<span class="hljs-string">"GoBasketball"</span>, <span class="hljs-function">(<span class="hljs-params">shot, callback</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">`投了一个<span class="hljs-subst">$&#123;shot&#125;</span>分球`</span>);
    &#125;,<span class="hljs-number">1000</span>)
  &#125;)
&#125;);

<span class="hljs-comment">//执行同步Hook</span>
kunkun.hooks.sing.call(<span class="hljs-string">'鸡你太美'</span>);
kunkun.hooks.dance.call(<span class="hljs-string">'华尔兹'</span>);
kunkun.hooks.rap.call();
<span class="hljs-comment">//执行异步Hook</span>
myCar.hooks.basketball.promise(<span class="hljs-number">2</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
<span class="hljs-built_in">console</span>.log(res)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Hook详细场景</h3>
<h4 data-id="heading-3">SyncHook</h4>
<p>在触发事件之后，会按照事件注册的先后顺序执行所有的事件处理函数。</p>
<h4 data-id="heading-4">SyncBailHook</h4>
<p>如果事件处理函数执行时有一个返回值不为空，则跳过剩下未执行的事件处理函数，还依照上述例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">kunkun.hooks.rap.tap(<span class="hljs-string">"GoRap1"</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'来了一首Rap1'</span>)&#125;);
kunkun.hooks.rap.tap(<span class="hljs-string">"GoRap2"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'来了一首Rap2'</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;);
kunkun.hooks.rap.tap(<span class="hljs-string">"GoRap3"</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'来了一首Rap3'</span>)&#125;);

kunkun.hooks.rap.call();

<span class="hljs-comment">// 来了一首Rap1</span>
<span class="hljs-comment">// 来了一首Rap2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">SyncWaterfallHook</h4>
<p>上一个事件处理函数的返回值作为参数传递给下一个事件处理函数，只有第一个绑定的函数里的参数是触发时的实际参数，其他绑定方法里的参数都是上一个的结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">kunkun.hooks.dance.tap(<span class="hljs-string">"Dance1"</span>, <span class="hljs-function"><span class="hljs-params">danceName</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`跳了一支<span class="hljs-subst">$&#123;danceName&#125;</span>1`</span>
&#125;);
kunkun.hooks.dance.tap(<span class="hljs-string">"Dance2"</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">`跳了一支<span class="hljs-subst">$&#123;danceName&#125;</span>2`</span>
&#125;);
kunkun.hooks.dance.tap(<span class="hljs-string">"Dance3"</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`跳了一支<span class="hljs-subst">$&#123;danceName&#125;</span>3`</span>
&#125;);
kunkun.hooks.dance.call(<span class="hljs-string">'华尔兹'</span>);

<span class="hljs-comment">//跳了一支华尔兹123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">SyncLoopHook</h4>
<p>事件处理函数返回 true表示循环执行当前事件处理函数，返回 undefined表示结束循环， 和SyncBailHook不同，SyncBailHook 只决定是否继续向下执行后面的事件处理函数，而 SyncLoopHook 的循环是指循环执行每一个事件处理函数，直到返回 undefined 为止，才会继续向下执行其他事件处理函数，执行机制同理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> syncLoopHook = <span class="hljs-keyword">new</span> SyncLoopHook([<span class="hljs-string">"name"</span>, <span class="hljs-string">"age"</span>]);
<span class="hljs-keyword">let</span> temp = <span class="hljs-number">0</span>;
<span class="hljs-comment">// 注册事件</span>
syncLoopHook.tap(<span class="hljs-string">"1"</span>, <span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"1"</span>, name, temp);
    <span class="hljs-keyword">return</span> temp++ < <span class="hljs-number">2</span> ? <span class="hljs-literal">true</span> : <span class="hljs-literal">undefined</span>;
&#125;);
syncLoopHook.tap(<span class="hljs-string">"2"</span>, <span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"2"</span>, name, temp);
    <span class="hljs-keyword">return</span> temp++ < <span class="hljs-number">5</span> ? <span class="hljs-literal">true</span> : <span class="hljs-literal">undefined</span>;
&#125;);
syncLoopHook.tap(<span class="hljs-string">"3"</span>, <span class="hljs-function"><span class="hljs-params">name</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"3"</span>, name));

syncLoopHook.call(<span class="hljs-string">"maosong"</span>);

<span class="hljs-comment">// 1 maosong 0</span>
<span class="hljs-comment">// 1 maosong 1</span>
<span class="hljs-comment">// 1 maosong 2</span>
<span class="hljs-comment">// 2 maosong 3</span>
<span class="hljs-comment">// 2 maosong 4</span>
<span class="hljs-comment">// 2 maosong 5</span>
<span class="hljs-comment">// 3 maosong</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">AsyncParallelHook</h4>
<p>所有注册的方法同步并行，和Promise.all()一样</p>
<h4 data-id="heading-8">AsyncSeriesHook</h4>
<p>所有注册的方法串行，也就是一个方法执行完，有了结果之后再执行下一个</p>
<h4 data-id="heading-9">AsyncParallelBailHook</h4>
<p>和SyncBailHook一个思想，只不过加入了异步</p>
<h4 data-id="heading-10">AsyncSeriesBailHook</h4>
<p>和SyncBailHook一个思想，只不过加入了异步</p>
<h4 data-id="heading-11">AsyncSeriesWaterfallHook</h4>
<p>AsyncSeriesHook + SyncWaterfallHook  详情去查看这俩Hook</p>
<h3 data-id="heading-12">异步注册和触发两种方式的区别</h3>
<h4 data-id="heading-13">tapAsync / callAsync</h4>
<p>在AsyncParallelHook中，注册时提供done()方法来表明异步结束，触发时可以传入callback来在所有注册的方法都运行结束后触发回调</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; AsyncParallelHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
<span class="hljs-keyword">let</span> asyncParallelHook = <span class="hljs-keyword">new</span> AsyncParallelHook([<span class="hljs-string">"name"</span>]);
asyncParallelHook.tapAsync(<span class="hljs-string">"1"</span>, <span class="hljs-function">(<span class="hljs-params">name, done</span>) =></span> &#123;
  settimeout(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"1"</span>, name);
    done();
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
asyncParallelHook.tapAsync(<span class="hljs-string">"2"</span>, <span class="hljs-function">(<span class="hljs-params">name, done</span>) =></span> &#123;
  settimeout(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"2"</span>, name);
    done();
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
<span class="hljs-comment">// 触发事件，让监听函数执行</span>
asyncParallelHook.callAsync(<span class="hljs-string">"maosong"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"over"</span>);
&#125;);

<span class="hljs-comment">// 1 maosong</span>
<span class="hljs-comment">// 2 maosong</span>
<span class="hljs-comment">// over</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在AsyncSeriesHook中提供next()方法来进入下一个注册的监控方法，用法和上面一样。</p>
<p>done()和next()的区别？</p>
<blockquote>
<p>done 方法只为了检测是否已经满足条件执行 callAsync 的回调，如果中间某个事件处理函数没有调用 done，只是不会调用 callAsync 的回调，但是所有的事件处理函数都会执行。</p>
</blockquote>
<blockquote>
<p>next 执行机制更像 Generator中的next()，在注册事件的回调中如果不调用 next，则在触发事件时会在没有调用 next 的事件处理函数的位置 “卡死”，即不会继续执行后面的事件处理函数，只有都调用 next 才能继续，而最后一个事件处理函数中调用 next 决定是否调用 callAsync 的回调。</p>
</blockquote>
<h4 data-id="heading-14">tapPromise /promise</h4>
<p>具体示例看一开始的kunkun示例就好，需要返回一个promise实例</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            