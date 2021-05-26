
---
title: 'vue钩子函数中使用async、await 注意点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=369'
author: 掘金
comments: false
date: Tue, 25 May 2021 00:39:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=369'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>自己在开发中总会遇到很多问题,很多时候不记录就会忘记了,所以我打算记录下来伴随自己成长,如果有幸能帮到小伙伴那更美哉</p>
<hr>
<p>在vue中我们经常会有这种需求:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 需要等到上个代码执行完拿到值再做其他操作</span>
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.userData(); <span class="hljs-comment">//这里可以拿到userType</span>
    <span class="hljs-comment">//拿到userType 判断用户不是代理人展示不同信息</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.userType==<span class="hljs-number">1</span>)&#123;
      <span class="hljs-built_in">this</span>.isAgent=<span class="hljs-literal">true</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先说注意点:</p>
<ol>
<li>钩子函数只会在指定时间执行(Vue生命周期),使用延时器等是不会影响周期执行的</li>
<li>钩子函数里使用async,await, 后面只能跟promise,否则加async,awiat没有意义</li>
<li>我们常用的钩子函数 created、mounted 如果加了async,await,想要同步执行代码,代码必须放在同一个钩子函数里面</li>
</ol>
<hr>
<ul>
<li>钩子函数只会在指定时间执行(Vue生命周期),使用延时器等是不会影响周期执行的</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
    &#125;, <span class="hljs-number">100</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  &#125;,
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
    &#125;, <span class="hljs-number">100</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>);
&#125;
<span class="hljs-comment">// 输出结果: 2 4 1 3</span>
<span class="hljs-comment">// 结论: 所以await 加给setTimeout是没有生效的,延时器并没有影响生命周期执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>钩子函数里使用async,await, 后面只能跟promise,否则加async,awiat没有意义</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 根据上面代码看出, await 后面加延时器等其他类似需要延迟执行的函数是没用的</span>
<span class="hljs-comment">// 然而await 后面加同步代码又多此一举</span>
<span class="hljs-comment">// 而其实async,awiat是专门为了解决promise回调函数多层嵌套的问题</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.userData(); <span class="hljs-comment">// 这个函数负责发请求获取数据,axios就是使用了promise</span>
    <span class="hljs-comment">//拿到userType 判断用户不是代理人展示不同信息</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.userType==<span class="hljs-number">1</span>)&#123;
      <span class="hljs-built_in">this</span>.isAgent=<span class="hljs-literal">true</span>;
    &#125;
&#125;
<span class="hljs-comment">// 结论: 这样写该周期函数下面的代码是会等待请求回来再执行的这样写是没问题的! 但仅仅限该周期函数!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>我们常用的钩子函数 created、mounted 如果加了async,await,想要同步执行代码,代码必须放在同一个钩子函数里面</li>
</ul>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>
  &#125;
&#125;,
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-comment">// this.userInfo() 发送请求获取数据,然后赋值给this.name ---- this.name = res.data.name</span>
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.userInfo()
  ...
&#125;,
<span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name) <span class="hljs-comment">// 打印为''</span>
&#125;

<span class="hljs-comment">// 结论: 不要以为mounted就一定比created后执行, 因为created加了async,await</span>
<span class="hljs-comment">// mounted函数懒得等他伺候promise 就先执行了</span>
<span class="hljs-comment">// 所以你在mounted里面不一定能拿到this.name进行赋值! 所以像这种有依赖上一个代码结果的最好写在一堆</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-comment">// this.userInfo() 发送请求获取数据,然后赋值给this.name ---- this.name = res.data.name</span>
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.userInfo() <span class="hljs-comment">// 拿到数据赋值成功</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name) <span class="hljs-comment">// 打印成功</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结尾:</p>
<p>我想我记录都是些不太高深的问题,但是高深的我也不会哈哈哈~</p></div>  
</div>
            