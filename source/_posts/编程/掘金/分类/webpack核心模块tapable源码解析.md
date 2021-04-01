
---
title: 'webpack核心模块tapable源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e36aeb7e1fe47bcb7ea3e05b79b8b7f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 23:56:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e36aeb7e1fe47bcb7ea3e05b79b8b7f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.cn/post/6939794845053485093" target="_blank">上一篇文章我写了<code>tapable</code>的基本用法</a>，我们知道他是一个增强版版的<code>发布订阅模式</code>，本文想来学习下他的源码。<code>tapable</code>的源码我读了一下，发现他的抽象程度比较高，直接扎进去反而会让人云里雾里的，所以本文会从最简单的<code>SyncHook</code>和<code>发布订阅模式</code>入手，再一步一步抽象，慢慢变成他源码的样子。</p>
<p><strong>本文可运行示例代码已经上传GitHub，大家拿下来一边玩一边看文章效果更佳：<a href="https://github.com/dennis-jiang/Front-End-Knowledges/tree/master/Examples/Engineering/tapable-source-code" target="_blank" rel="nofollow noopener noreferrer">github.com/dennis-jian…</a></strong>。</p>
<h2 data-id="heading-0"><code>SyncHook</code>的基本实现</h2>
<p>上一篇文章已经讲过<code>SyncHook</code>的用法了，我这里就不再展开了，他使用的例子就是这样子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; SyncHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);

<span class="hljs-comment">// 实例化一个加速的hook</span>
<span class="hljs-keyword">const</span> accelerate = <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"newSpeed"</span>]);

<span class="hljs-comment">// 注册第一个回调，加速时记录下当前速度</span>
accelerate.tap(<span class="hljs-string">"LoggerPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">newSpeed</span>) =></span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"LoggerPlugin"</span>, <span class="hljs-string">`加速到<span class="hljs-subst">$&#123;newSpeed&#125;</span>`</span>)
);

<span class="hljs-comment">// 再注册一个回调，用来检测是否超速</span>
accelerate.tap(<span class="hljs-string">"OverspeedPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">newSpeed</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (newSpeed > <span class="hljs-number">120</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"OverspeedPlugin"</span>, <span class="hljs-string">"您已超速！！"</span>);
  &#125;
&#125;);

<span class="hljs-comment">// 触发一下加速事件，看看效果吧</span>
accelerate.call(<span class="hljs-number">500</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这种用法就是一个最基本的<code>发布订阅模式</code>，我之前<a href="https://juejin.cn/post/6844904101331877895" target="_blank">讲发布订阅模式的文章</a>讲过，我们可以仿照那个很快实现一个<code>SyncHook</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SyncHook</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args = []</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._args = args;       <span class="hljs-comment">// 接收的参数存下来</span>
        <span class="hljs-built_in">this</span>.taps = [];          <span class="hljs-comment">// 一个存回调的数组</span>
    &#125;

    <span class="hljs-comment">// tap实例方法用来注册回调</span>
    <span class="hljs-function"><span class="hljs-title">tap</span>(<span class="hljs-params">name, fn</span>)</span> &#123;
        <span class="hljs-comment">// 逻辑很简单，直接保存下传入的回调参数就行</span>
        <span class="hljs-built_in">this</span>.taps.push(fn);
    &#125;

    <span class="hljs-comment">// call实例方法用来触发事件，执行所有回调</span>
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-comment">// 逻辑也很简单，将注册的回调一个一个拿出来执行就行</span>
        <span class="hljs-keyword">const</span> tapsLength = <span class="hljs-built_in">this</span>.taps.length;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
            <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
            fn(...args);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码非常简单，是一个最基础的<code>发布订阅模式</code>，使用方法跟上面是一样的，将<code>SyncHook</code>从<code>tapable</code>导出改为使用我们自己的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// const &#123; SyncHook &#125; = require("tapable");</span>
<span class="hljs-keyword">const</span> &#123; SyncHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncHook"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果是一样的：</p>
<p><img alt="image-20210323153234354" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e36aeb7e1fe47bcb7ea3e05b79b8b7f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>注意：</strong> 我们构造函数里面传入的<code>args</code>并没有用上，<code>tapable</code>主要是用它来动态生成<code>call</code>的函数体的，在后面讲代码工厂的时候会看到。</p>
<h2 data-id="heading-1"><code>SyncBailHook</code>的基本实现</h2>
<p>再来一个<code>SyncBailHook</code>的基本实现吧，<code>SyncBailHook</code>的作用是当前一个回调返回不为<code>undefined</code>的值的时候，阻止后面的回调执行。基本使用是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; SyncBailHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);    <span class="hljs-comment">// 使用的是SyncBailHook</span>

<span class="hljs-keyword">const</span> accelerate = <span class="hljs-keyword">new</span> SyncBailHook([<span class="hljs-string">"newSpeed"</span>]);

accelerate.tap(<span class="hljs-string">"LoggerPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">newSpeed</span>) =></span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"LoggerPlugin"</span>, <span class="hljs-string">`加速到<span class="hljs-subst">$&#123;newSpeed&#125;</span>`</span>)
);

<span class="hljs-comment">// 再注册一个回调，用来检测是否超速</span>
<span class="hljs-comment">// 如果超速就返回一个错误</span>
accelerate.tap(<span class="hljs-string">"OverspeedPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">newSpeed</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (newSpeed > <span class="hljs-number">120</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"OverspeedPlugin"</span>, <span class="hljs-string">"您已超速！！"</span>);

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'您已超速！！'</span>);
  &#125;
&#125;);

<span class="hljs-comment">// 由于上一个回调返回了一个不为undefined的值</span>
<span class="hljs-comment">// 这个回调不会再运行了</span>
accelerate.tap(<span class="hljs-string">"DamagePlugin"</span>, <span class="hljs-function">(<span class="hljs-params">newSpeed</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (newSpeed > <span class="hljs-number">300</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"DamagePlugin"</span>, <span class="hljs-string">"速度实在太快，车子快散架了。。。"</span>);
  &#125;
&#125;);

accelerate.call(<span class="hljs-number">500</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他的实现跟上面的<code>SyncHook</code>也非常像，只是<code>call</code>在执行的时候不一样而已，<code>SyncBailHook</code>需要检测每个回调的返回值，如果不为<code>undefined</code>就终止执行后面的回调，所以代码实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SyncBailHook</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args = []</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._args = args;       
        <span class="hljs-built_in">this</span>.taps = [];          
    &#125;

    <span class="hljs-function"><span class="hljs-title">tap</span>(<span class="hljs-params">name, fn</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.taps.push(fn);
    &#125;

    <span class="hljs-comment">// 其他代码跟SyncHook是一样的，就是call的实现不一样</span>
    <span class="hljs-comment">// 需要检测每个返回值，如果不为undefined就终止执行</span>
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-keyword">const</span> tapsLength = <span class="hljs-built_in">this</span>.taps.length;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
            <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
            <span class="hljs-keyword">const</span> res = fn(...args);

            <span class="hljs-keyword">if</span>( res !== <span class="hljs-literal">undefined</span>) <span class="hljs-keyword">return</span> res;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后改下<code>SyncBailHook</code>从我们自己的引入就行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// const &#123; SyncBailHook &#125; = require("tapable"); </span>
<span class="hljs-keyword">const</span> &#123; SyncBailHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncBailHook"</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果是一样的：</p>
<p><img alt="image-20210323155857678" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce47227a914a4e6b98602dd525f3257c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">抽象重复代码</h2>
<p>现在我们只实现了<code>SyncHook</code>和<code>SyncBailHook</code>两个<code>Hook</code>而已，上一篇讲用法的文章里面总共有9个<code>Hook</code>，如果每个<code>Hook</code>都像前面这样实现也是可以的。但是我们再仔细看下<code>SyncHook</code>和<code>SyncBailHook</code>两个类的代码，发现他们除了<code>call</code>的实现不一样，其他代码一模一样，所以作为一个有追求的工程师，我们可以把这部分重复的代码提出来作为一个基类：<code>Hook</code>类。</p>
<p><code>Hook</code>类需要包含一些公共的代码，<code>call</code>这种不一样的部分由各个子类自己实现。所以<code>Hook</code>类就长这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CALL_DELEGATE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
<span class="hljs-built_in">this</span>.call = <span class="hljs-built_in">this</span>._createCall();
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.call(...args);
&#125;;

<span class="hljs-comment">// Hook是SyncHook和SyncBailHook的基类</span>
<span class="hljs-comment">// 大体结构是一样的，不一样的地方是call</span>
<span class="hljs-comment">// 不同子类的call是不一样的</span>
<span class="hljs-comment">// tapable的Hook基类提供了一个抽象接口compile来动态生成call函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hook</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args = []</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._args = args;       
        <span class="hljs-built_in">this</span>.taps = [];          

        <span class="hljs-comment">// 基类的call初始化为CALL_DELEGATE</span>
        <span class="hljs-comment">// 为什么这里需要这样一个代理，而不是直接this.call = _createCall()</span>
        <span class="hljs-comment">// 等我们后面子类实现了再一起讲</span>
        <span class="hljs-built_in">this</span>.call = CALL_DELEGATE;
    &#125;

    <span class="hljs-comment">// 一个抽象接口compile</span>
    <span class="hljs-comment">// 由子类实现，基类compile不能直接调用</span>
    <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">options</span>)</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Abstract: should be overridden"</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">tap</span>(<span class="hljs-params">name, fn</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.taps.push(fn);
    &#125;

    <span class="hljs-comment">// _createCall调用子类实现的compile来生成call方法</span>
    <span class="hljs-function"><span class="hljs-title">_createCall</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.compile(&#123;
        <span class="hljs-attr">taps</span>: <span class="hljs-built_in">this</span>.taps,
        <span class="hljs-attr">args</span>: <span class="hljs-built_in">this</span>._args,
      &#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方对应的源码看这里：<a href="https://github.com/webpack/tapable/blob/master/lib/Hook.js" target="_blank" rel="nofollow noopener noreferrer">github.com/webpack/tap…</a></p>
<h3 data-id="heading-3">子类SyncHook实现</h3>
<p>现在有了<code>Hook</code>基类，我们的<code>SyncHook</code>就需要继承这个基类重写，<code>tapable</code>在这里继承的时候并没有使用<code>class extends</code>，而是手动继承的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Hook = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./Hook'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SyncHook</span>(<span class="hljs-params">args = []</span>) </span>&#123;
    <span class="hljs-comment">// 先手动继承Hook</span>
  <span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args);
    hook.constructor = SyncHook;

    <span class="hljs-comment">// 然后实现自己的compile函数</span>
    <span class="hljs-comment">// compile的作用应该是创建一个call函数并返回</span>
hook.compile = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
        <span class="hljs-comment">// 这里call函数的实现跟前面实现是一样的</span>
        <span class="hljs-keyword">const</span> &#123; taps &#125; = options;
        <span class="hljs-keyword">const</span> call = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
            <span class="hljs-keyword">const</span> tapsLength = taps.length;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
                <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
                fn(...args);
            &#125;
        &#125;

        <span class="hljs-keyword">return</span> call;
    &#125;;
    
<span class="hljs-keyword">return</span> hook;
&#125;

SyncHook.prototype = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：我们在基类<code>Hook</code>构造函数中初始化<code>this.call</code>为<code>CALL_DELEGATE</code>这个函数，这是有原因的，最主要的原因是<strong>确保<code>this</code>的正确指向</strong>。思考一下假如我们不用<code>CALL_DELEGATE</code>，而是直接<code>this.call = this._createCall()</code>会发生什么？我们来分析下这个执行流程：</p>
<ol>
<li>用户使用时，肯定是使用<code>new SyncHook()</code>，这时候会执行<code>const hook = new Hook(args);</code></li>
<li><code>new Hook(args)</code>会去执行<code>Hook</code>的构造函数，也就是会运行<code>this.call = this._createCall()</code></li>
<li>这时候的<code>this</code>指向的是基类<code>Hook</code>的实例，<code>this._createCall()</code>会调用基类的<code>this.compile()</code></li>
<li>由于基类的<code>complie</code>函数是一个抽象接口，直接调用会报错<code>Abstract: should be overridden</code>。</li>
</ol>
<p><strong>那我们采用<code>this.call = CALL_DELEGATE</code>是怎么解决这个问题的呢</strong>？</p>
<ol>
<li>采用<code>this.call = CALL_DELEGATE</code>后，基类<code>Hook</code>上的<code>call</code>就只是被赋值为一个代理函数而已，这个函数不会立马调用。</li>
<li>用户使用时，同样是<code>new SyncHook()</code>，里面会执行<code>Hook</code>的构造函数</li>
<li><code>Hook</code>构造函数会给<code>this.call</code>赋值为<code>CALL_DELEGATE</code>，但是不会立即执行。</li>
<li><code>new SyncHook()</code>继续执行，新建的实例上的方法<code>hook.complie</code>被覆写为正确方法。</li>
<li>当用户调用<code>hook.call</code>的时候才会真正执行<code>this._createCall()</code>，这里面会去调用<code>this.complie()</code></li>
<li>这时候调用的<code>complie</code>已经是被正确覆写过的了，所以得到正确的结果。</li>
</ol>
<h3 data-id="heading-4">子类SyncBailHook的实现</h3>
<p>子类<code>SyncBailHook</code>的实现跟上面<code>SyncHook</code>的也是非常像，只是<code>hook.compile</code>实现不一样而已：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Hook = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./Hook'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SyncBailHook</span>(<span class="hljs-params">args = []</span>) </span>&#123;
    <span class="hljs-comment">// 基本结构跟SyncHook都是一样的</span>
  <span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args);
    hook.constructor = SyncBailHook;

    
    <span class="hljs-comment">// 只是compile的实现是Bail版的</span>
hook.compile = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
        <span class="hljs-keyword">const</span> &#123; taps &#125; = options;
        <span class="hljs-keyword">const</span> call = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
            <span class="hljs-keyword">const</span> tapsLength = taps.length;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
                <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
                <span class="hljs-keyword">const</span> res = fn(...args);

                <span class="hljs-keyword">if</span>( res !== <span class="hljs-literal">undefined</span>) <span class="hljs-keyword">break</span>;
            &#125;
        &#125;

        <span class="hljs-keyword">return</span> call;
    &#125;;
    
<span class="hljs-keyword">return</span> hook;
&#125;

SyncBailHook.prototype = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">抽象代码工厂</h2>
<p>上面我们通过对<code>SyncHook</code>和<code>SyncBailHook</code>的抽象提炼出了一个基类<code>Hook</code>，减少了重复代码。基于这种结构子类需要实现的就是<code>complie</code>方法，但是如果我们将<code>SyncHook</code>和<code>SyncBailHook</code>的<code>complie</code>方法拿出来对比下：</p>
<p><strong>SyncHook</strong>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">hook.compile = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; taps &#125; = options;
  <span class="hljs-keyword">const</span> call = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">const</span> tapsLength = taps.length;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
      <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
      fn(...args);
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> call;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>SyncBailHook</strong>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">hook.compile = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; taps &#125; = options;
  <span class="hljs-keyword">const</span> call = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">const</span> tapsLength = taps.length;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tapsLength; i++) &#123;
      <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.taps[i];
      <span class="hljs-keyword">const</span> res = fn(...args);

      <span class="hljs-keyword">if</span>( res !== <span class="hljs-literal">undefined</span>) <span class="hljs-keyword">return</span> res;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> call;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现这两个<code>complie</code>也非常像，有大量重复代码，所以<code>tapable</code>为了解决这些重复代码，又进行了一次抽象，也就是代码工厂<code>HookCodeFactory</code>。<code>HookCodeFactory</code>的作用就是用来生成<code>complie</code>返回的<code>call</code>函数体，而<code>HookCodeFactory</code>在实现时也采用了<code>Hook</code>类似的思路，也是先实现了一个基类<code>HookCodeFactory</code>，然后不同的<code>Hook</code>再继承这个类来实现自己的代码工厂，比如<code>SyncHookCodeFactory</code>。</p>
<h3 data-id="heading-6">创建函数的方法</h3>
<p>在继续深入代码工厂前，我们先来回顾下JS里面创建函数的方法。一般我们会有这几种方法：</p>
<ol>
<li>
<p>函数申明</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>函数表达式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>但是除了这两种方法外，还有种不常用的方法：<strong>使用Function构造函数</strong>。比如上面这个函数使用构造函数创建就是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> add = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'return a + b;'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的调用形式里，最后一个参数是函数的函数体，前面的参数都是函数的形参，最终生成的函数跟用函数表达式的效果是一样的，可以这样调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);    <span class="hljs-comment">// 结果是3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：上面的<code>a</code>和<code>b</code>形参放在一起用逗号隔开也是可以的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> add = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'a, b'</span>, <span class="hljs-string">'return a + b;'</span>);    <span class="hljs-comment">// 这样跟上面的效果是一样的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然函数并不是一定要有参数，没有参数的函数也可以这样创建：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sayHi = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'alert("Hello")'</span>);

sayHi(); <span class="hljs-comment">// Hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样创建函数和前面的函数申明和函数表达式有什么区别呢？<strong>使用Function构造函数来创建函数最大的一个特征就是，函数体是一个字符串，也就是说我们可以动态生成这个字符串，从而动态生成函数体</strong>。因为<code>SyncHook</code>和<code>SyncBailHook</code>的<code>call</code>函数很像，我们可以像拼一个字符串那样拼出他们的函数体，为了更简单的拼凑，<code>tapable</code>最终生成的<code>call</code>函数里面并没有循环，而是在拼函数体的时候就将循环展开了，比如<code>SyncHook</code>拼出来的<code>call</code>函数的函数体就是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> _x = <span class="hljs-built_in">this</span>._x;
<span class="hljs-keyword">var</span> _fn0 = _x[<span class="hljs-number">0</span>];
_fn0(newSpeed);
<span class="hljs-keyword">var</span> _fn1 = _x[<span class="hljs-number">1</span>];
_fn1(newSpeed);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的<code>_x</code>其实就是保存回调的数组<code>taps</code>，这里重命名为<code>_x</code>，我想是为了节省代码大小吧。这段代码可以看到，<code>_x</code>，也就是<code>taps</code>里面的内容已经被展开了，是一个一个取出来执行的。</p>
<p>而<code>SyncBailHook</code>最终生成的<code>call</code>函数体是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> _x = <span class="hljs-built_in">this</span>._x;
<span class="hljs-keyword">var</span> _fn0 = _x[<span class="hljs-number">0</span>];
<span class="hljs-keyword">var</span> _result0 = _fn0(newSpeed);
<span class="hljs-keyword">if</span> (_result0 !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">return</span> _result0;
    ;
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">var</span> _fn1 = _x[<span class="hljs-number">1</span>];
    <span class="hljs-keyword">var</span> _result1 = _fn1(newSpeed);
    <span class="hljs-keyword">if</span> (_result1 !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">return</span> _result1;
        ;
    &#125; <span class="hljs-keyword">else</span> &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段生成的代码主体逻辑其实跟<code>SyncHook</code>是一样的，都是将<code>_x</code>展开执行了，他们的区别是<code>SyncBailHook</code>会对每次执行的结果进行检测，如果结果不是<code>undefined</code>就直接<code>return</code>了，后面的回调函数就没有机会执行了。</p>
<h3 data-id="heading-7">创建代码工厂基类</h3>
<p>基于这个目的，我们的代码工厂基类应该可以生成最基本的<code>call</code>函数体。我们来写个最基本的<code>HookCodeFactory</code>吧，目前他只能生成<code>SyncHook</code>的<code>call</code>函数体：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 构造函数定义两个变量</span>
        <span class="hljs-built_in">this</span>.options = <span class="hljs-literal">undefined</span>;
        <span class="hljs-built_in">this</span>._args = <span class="hljs-literal">undefined</span>;
    &#125;

    <span class="hljs-comment">// init函数初始化变量</span>
    <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.options = options;
        <span class="hljs-built_in">this</span>._args = options.args.slice();
    &#125;

    <span class="hljs-comment">// deinit重置变量</span>
    <span class="hljs-function"><span class="hljs-title">deinit</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.options = <span class="hljs-literal">undefined</span>;
        <span class="hljs-built_in">this</span>._args = <span class="hljs-literal">undefined</span>;
    &#125;

    <span class="hljs-comment">// args用来将传入的数组args转换为New Function接收的逗号分隔的形式</span>
    <span class="hljs-comment">// ['arg1', 'args'] --->  'arg1, arg2'</span>
    <span class="hljs-function"><span class="hljs-title">args</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._args.join(<span class="hljs-string">", "</span>);
    &#125;

    <span class="hljs-comment">// setup其实就是给生成代码的_x赋值</span>
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">instance, options</span>)</span> &#123;
        instance._x = options.taps.map(<span class="hljs-function"><span class="hljs-params">t</span> =></span> t);
    &#125;

    <span class="hljs-comment">// create创建最终的call函数</span>
    <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.init(options);
        <span class="hljs-keyword">let</span> fn;

        <span class="hljs-comment">// 直接将taps展开为平铺的函数调用</span>
        <span class="hljs-keyword">const</span> &#123; taps &#125; = options;
        <span class="hljs-keyword">let</span> code = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < taps.length; i++) &#123;
            code += <span class="hljs-string">`
                var _fn<span class="hljs-subst">$&#123;i&#125;</span> = _x[<span class="hljs-subst">$&#123;i&#125;</span>];
                _fn<span class="hljs-subst">$&#123;i&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.args()&#125;</span>);
            `</span>
        &#125;

        <span class="hljs-comment">// 将展开的循环和头部连接起来</span>
        <span class="hljs-keyword">const</span> allCodes = <span class="hljs-string">`
            "use strict";
            var _x = this._x;
        `</span> + code;

        <span class="hljs-comment">// 用传进来的参数和生成的函数体创建一个函数出来</span>
        fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-built_in">this</span>.args(), allCodes);

        <span class="hljs-built_in">this</span>.deinit();  <span class="hljs-comment">// 重置变量</span>

        <span class="hljs-keyword">return</span> fn;    <span class="hljs-comment">// 返回生成的函数</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码最核心的其实就是<code>create</code>函数，这个函数会动态创建一个<code>call</code>函数并返回，所以<code>SyncHook</code>可以直接使用这个<code>factory</code>创建代码了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// SyncHook.js</span>

<span class="hljs-keyword">const</span> Hook = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./Hook'</span>);
<span class="hljs-keyword">const</span> HookCodeFactory = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HookCodeFactory"</span>);

<span class="hljs-keyword">const</span> factory = <span class="hljs-keyword">new</span> HookCodeFactory();

<span class="hljs-comment">// COMPILE函数会去调用factory来生成call函数</span>
<span class="hljs-keyword">const</span> COMPILE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
factory.setup(<span class="hljs-built_in">this</span>, options);
<span class="hljs-keyword">return</span> factory.create(options);
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SyncHook</span>(<span class="hljs-params">args = []</span>) </span>&#123;
<span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args);
    hook.constructor = SyncHook;

    <span class="hljs-comment">// 使用HookCodeFactory来创建最终的call函数</span>
    hook.compile = COMPILE;

<span class="hljs-keyword">return</span> hook;
&#125;

SyncHook.prototype = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">让代码工厂支持<code>SyncBailHook</code></h3>
<p>现在我们的<code>HookCodeFactory</code>只能生成最简单的<code>SyncHook</code>代码，我们需要对他进行一些改进，让他能够也生成<code>SyncBailHook</code>的<code>call</code>函数体。你可以拉回前面再仔细观察下这两个最终生成代码的区别：</p>
<ol>
<li><code>SyncBailHook</code>需要对每次执行的<code>result</code>进行处理，如果不为<code>undefined</code>就返回</li>
<li><code>SyncBailHook</code>生成的代码其实是<code>if...else</code>嵌套的，我们生成的时候可以考虑使用一个递归函数</li>
</ol>
<p>为了让<code>SyncHook</code>和<code>SyncBailHook</code>的子类代码工厂能够传入差异化的<code>result</code>处理，我们先将<code>HookCodeFactory</code>基类的<code>create</code>拆成两部分，将代码拼装的逻辑单独拆成一个函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
    <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 省略其他一样的代码</span>
  <span class="hljs-comment">// ...</span>

    <span class="hljs-comment">// create创建最终的call函数</span>
    <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.init(options);
        <span class="hljs-keyword">let</span> fn;

        <span class="hljs-comment">// 拼装代码头部</span>
        <span class="hljs-keyword">const</span> header = <span class="hljs-string">`
            "use strict";
            var _x = this._x;
        `</span>;

        <span class="hljs-comment">// 用传进来的参数和函数体创建一个函数出来</span>
        fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-built_in">this</span>.args(),
            header +
            <span class="hljs-built_in">this</span>.content());         <span class="hljs-comment">// 注意这里的content函数并没有在基类HookCodeFactory实现，而是子类实现的</span>

        <span class="hljs-built_in">this</span>.deinit();

        <span class="hljs-keyword">return</span> fn;
    &#125;

    <span class="hljs-comment">// 拼装函数体</span>
  <span class="hljs-comment">// callTapsSeries也没在基类调用，而是子类调用的</span>
    <span class="hljs-function"><span class="hljs-title">callTapsSeries</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; taps &#125; = <span class="hljs-built_in">this</span>.options;
        <span class="hljs-keyword">let</span> code = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < taps.length; i++) &#123;
            code += <span class="hljs-string">`
                var _fn<span class="hljs-subst">$&#123;i&#125;</span> = _x[<span class="hljs-subst">$&#123;i&#125;</span>];
                _fn<span class="hljs-subst">$&#123;i&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.args()&#125;</span>);
            `</span>
        &#125;

        <span class="hljs-keyword">return</span> code;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上面代码里面要特别注意<code>create</code>函数里面生成函数体的时候调用的是<code>this.content</code>，但是<code>this.content</code>并没与在基类实现，这要求子类在使用<code>HookCodeFactory</code>的时候都需要继承他并实现自己的<code>content</code>函数，所以这里的<code>content</code>函数也是一个抽象接口。那<code>SyncHook</code>的代码就应该改成这样：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// SyncHook.js</span>

<span class="hljs-comment">// ... 省略其他一样的代码 ...</span>

<span class="hljs-comment">// SyncHookCodeFactory继承HookCodeFactory并实现content函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SyncHookCodeFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">content</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callTapsSeries();    <span class="hljs-comment">// 这里的callTapsSeries是基类的</span>
    &#125;
&#125;

<span class="hljs-comment">// 使用SyncHookCodeFactory来创建factory</span>
<span class="hljs-keyword">const</span> factory = <span class="hljs-keyword">new</span> SyncHookCodeFactory();

<span class="hljs-keyword">const</span> COMPILE = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    factory.setup(<span class="hljs-built_in">this</span>, options);
    <span class="hljs-keyword">return</span> factory.create(options);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**注意这里：**子类实现的<code>content</code>其实又调用了基类的<code>callTapsSeries</code>来生成最终的函数体。所以这里这几个函数的调用关系其实是这样的：</p>
<p><img alt="image-20210401111739814" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8783fc54c4dd4725b2fcb0c200ef8d6b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>那这样设计的目的是什么呢</strong>？<strong>为了让子类<code>content</code>能够传递参数给基类<code>callTapsSeries</code>，从而生成不一样的函数体</strong>。我们马上就能在<code>SyncBailHook</code>的代码工厂上看到了。</p>
<p>为了能够生成<code>SyncBailHook</code>的函数体，我们需要让<code>callTapsSeries</code>支持一个<code>onResult</code>参数，就是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
    <span class="hljs-comment">// ... 省略其他相同的代码 ...</span>

    <span class="hljs-comment">// 拼装函数体，需要支持options.onResult参数</span>
    <span class="hljs-function"><span class="hljs-title">callTapsSeries</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; taps &#125; = <span class="hljs-built_in">this</span>.options;
        <span class="hljs-keyword">let</span> code = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;

        <span class="hljs-keyword">const</span> onResult = options && options.onResult;
        
        <span class="hljs-comment">// 写一个next函数来开启有onResult回调的函数体生成</span>
        <span class="hljs-comment">// next和onResult相互递归调用来生成最终的函数体</span>
        <span class="hljs-keyword">const</span> next = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span>(i >= taps.length) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;

            <span class="hljs-keyword">const</span> result = <span class="hljs-string">`_result<span class="hljs-subst">$&#123;i&#125;</span>`</span>;
            <span class="hljs-keyword">const</span> code = <span class="hljs-string">`
                var _fn<span class="hljs-subst">$&#123;i&#125;</span> = _x[<span class="hljs-subst">$&#123;i&#125;</span>];
                var <span class="hljs-subst">$&#123;result&#125;</span> = _fn<span class="hljs-subst">$&#123;i&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.args()&#125;</span>);
                <span class="hljs-subst">$&#123;onResult(i++, result, next)&#125;</span>
            `</span>;

            <span class="hljs-keyword">return</span> code;
        &#125;

        <span class="hljs-comment">// 支持onResult参数</span>
        <span class="hljs-keyword">if</span>(onResult) &#123;
            code = next();
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 没有onResult参数的时候，即SyncHook跟之前保持一样</span>
            <span class="hljs-keyword">for</span>(; i< taps.length; i++) &#123;
                code += <span class="hljs-string">`
                    var _fn<span class="hljs-subst">$&#123;i&#125;</span> = _x[<span class="hljs-subst">$&#123;i&#125;</span>];
                    _fn<span class="hljs-subst">$&#123;i&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.args()&#125;</span>);
                `</span>
            &#125;
        &#125;

        <span class="hljs-keyword">return</span> code;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们的<code>SyncBailHook</code>的代码工厂在继承工厂基类的时候需要传一个<code>onResult</code>参数，就是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Hook = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./Hook'</span>);
<span class="hljs-keyword">const</span> HookCodeFactory = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HookCodeFactory"</span>);

<span class="hljs-comment">// SyncBailHookCodeFactory继承HookCodeFactory并实现content函数</span>
<span class="hljs-comment">// content里面传入定制的onResult函数，onResult回去调用next递归生成嵌套的if...else...</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SyncBailHookCodeFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">content</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callTapsSeries(&#123;
            <span class="hljs-attr">onResult</span>: <span class="hljs-function">(<span class="hljs-params">i, result, next</span>) =></span>
                <span class="hljs-string">`if(<span class="hljs-subst">$&#123;result&#125;</span> !== undefined) &#123;\nreturn <span class="hljs-subst">$&#123;result&#125;</span>;\n&#125; else &#123;\n<span class="hljs-subst">$&#123;next()&#125;</span>&#125;\n`</span>,
        &#125;);
    &#125;
&#125;

<span class="hljs-comment">// 使用SyncHookCodeFactory来创建factory</span>
<span class="hljs-keyword">const</span> factory = <span class="hljs-keyword">new</span> SyncBailHookCodeFactory();

<span class="hljs-keyword">const</span> COMPILE = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    factory.setup(<span class="hljs-built_in">this</span>, options);
    <span class="hljs-keyword">return</span> factory.create(options);
&#125;;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SyncBailHook</span>(<span class="hljs-params">args = []</span>) </span>&#123;
    <span class="hljs-comment">// 基本结构跟SyncHook都是一样的</span>
    <span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args);
    hook.constructor = SyncBailHook;

    <span class="hljs-comment">// 使用HookCodeFactory来创建最终的call函数</span>
    hook.compile = COMPILE;

    <span class="hljs-keyword">return</span> hook;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在运行下代码，效果跟之前一样的，大功告成~</p>
<h2 data-id="heading-9">其他Hook的实现</h2>
<p>到这里，<code>tapable</code>的源码架构和基本实现我们已经弄清楚了，但是本文只用了<code>SyncHook</code>和<code>SyncBailHook</code>做例子，其他的，比如<code>AsyncParallelHook</code>并没有展开讲。因为<code>AsyncParallelHook</code>之类的其他<code>Hook</code>的实现思路跟本文是一样的，比如我们可以先实现一个独立的<code>AsyncParallelHook</code>类：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AsyncParallelHook</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args = []</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._args = args;
        <span class="hljs-built_in">this</span>.taps = [];
    &#125;
    <span class="hljs-function"><span class="hljs-title">tapAsync</span>(<span class="hljs-params">name, task</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.taps.push(task);
    &#125;
    <span class="hljs-function"><span class="hljs-title">callAsync</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-comment">// 先取出最后传入的回调函数</span>
        <span class="hljs-keyword">let</span> finalCallback = args.pop();

        <span class="hljs-comment">// 定义一个 i 变量和 done 函数，每次执行检测 i 值和队列长度，决定是否执行 callAsync 的最终回调函数</span>
        <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">let</span> done = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span> (++i === <span class="hljs-built_in">this</span>.taps.length) &#123;
                finalCallback();
            &#125;
        &#125;;

        <span class="hljs-comment">// 依次执行事件处理函数</span>
        <span class="hljs-built_in">this</span>.taps.forEach(<span class="hljs-function"><span class="hljs-params">task</span> =></span> task(...args, done));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后对他的<code>callAsync</code>函数进行抽象，将其抽象到代码工厂类里面，使用字符串拼接的方式动态构造出来就行了，整体思路跟前面是一样的。具体实现过程可以参考<code>tapable</code>源码：</p>
<p><a href="https://github.com/webpack/tapable/blob/v2.2.0/lib/Hook.js" target="_blank" rel="nofollow noopener noreferrer">Hook类源码</a></p>
<p><a href="https://github.com/webpack/tapable/blob/v2.2.0/lib/SyncHook.js" target="_blank" rel="nofollow noopener noreferrer">SyncHook类源码</a></p>
<p><a href="https://github.com/webpack/tapable/blob/v2.2.0/lib/SyncBailHook.js" target="_blank" rel="nofollow noopener noreferrer">SyncBailHook类源码</a></p>
<p><a href="https://github.com/webpack/tapable/blob/v2.2.0/lib/HookCodeFactory.js" target="_blank" rel="nofollow noopener noreferrer">HookCodeFactory类源码</a></p>
<h2 data-id="heading-10">总结</h2>
<p><strong>本文可运行示例代码已经上传GitHub，大家拿下来一边玩一边看文章效果更佳：<a href="https://github.com/dennis-jiang/Front-End-Knowledges/tree/master/Examples/Engineering/tapable-source-code" target="_blank" rel="nofollow noopener noreferrer">github.com/dennis-jian…</a></strong>。</p>
<p>下面再对本文的思路进行一个总结：</p>
<ol>
<li><code>tapable</code>的各种<code>Hook</code>其实都是基于发布订阅模式。</li>
<li>各个<code>Hook</code>自己独立实现其实也没有问题，但是因为都是发布订阅模式，会有大量重复代码，所以<code>tapable</code>进行了几次抽象。</li>
<li>第一次抽象是提取一个<code>Hook</code>基类，这个基类实现了初始化和事件注册等公共部分，至于每个<code>Hook</code>的<code>call</code>都不一样，需要自己实现。</li>
<li>第二次抽象是每个<code>Hook</code>在实现自己的<code>call</code>的时候，发现代码也有很多相似之处，所以提取了一个代码工厂，用来动态生成<code>call</code>的函数体。</li>
<li>总体来说，<code>tapable</code>的代码并不难，但是因为有两次抽象，整个代码架构显得不那么好读，经过本文的梳理后，应该会好很多了。</li>
</ol>
<p><strong>文章的最后，感谢你花费宝贵的时间阅读本文，如果本文给了你一点点帮助或者启发，请不要吝啬你的赞和GitHub小星星，你的支持是作者持续创作的动力。</strong></p>
<p><strong>欢迎关注我的公众号<a href="https://test-dennis.oss-cn-hangzhou.aliyuncs.com/QRCode/QR430.jpg" target="_blank" rel="nofollow noopener noreferrer">进击的大前端</a>第一时间获取高质量原创~</strong></p>
<p><strong>“前端进阶知识”系列文章：<a href="https://juejin.im/post/5e3ffc85518825494e2772fd" target="_blank" rel="nofollow noopener noreferrer">juejin.im/post/5e3ffc…</a></strong></p>
<p><strong>“前端进阶知识”系列文章源码GitHub地址： <a href="https://github.com/dennis-jiang/Front-End-Knowledges" target="_blank" rel="nofollow noopener noreferrer">github.com/dennis-jian…</a></strong></p>
<h2 data-id="heading-11">参考资料</h2>
<p><code>tapable</code>用法介绍：<a href="https://juejin.cn/post/6939794845053485093" target="_blank">juejin.cn/post/693979…</a></p>
<p><code>tapable</code>源码地址：<a href="https://github.com/webpack/tapable" target="_blank" rel="nofollow noopener noreferrer">github.com/webpack/tap…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            