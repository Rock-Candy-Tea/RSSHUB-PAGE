
---
title: '一看就懂的JS手写函数（call、防抖节流）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5666'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 17:36:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=5666'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看 <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">call函数</h2>
<p>先从改变this指向上简单实现一个方法添加到Function的原型链上：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myCall = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">content</span>) </span>&#123;
    content.fn = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">eval</span>(<span class="hljs-string">`content.fn()`</span>)
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就实现了call函数核心部分，因为使用了字符串的形式，所以函数的参数部分还需要进行特殊处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myCall = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">content</span>) </span>&#123;
    content.fn = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">/** 处理参数 */</span>
    <span class="hljs-keyword">const</span> args = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">arguments</span>.length; i++) &#123;
        args.push(<span class="hljs-string">`arguments[<span class="hljs-subst">$&#123;i&#125;</span>]`</span>) <span class="hljs-comment">// 直接push会导致强转字符串时出现:[]</span>
    &#125;
    <span class="hljs-comment">/** */</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">eval</span>(<span class="hljs-string">`content.fn(<span class="hljs-subst">$&#123;args&#125;</span>)`</span>)
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本可以了，但还有问题，临时属性的处理，最终优化结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myCall = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-keyword">const</span> fn = <span class="hljs-string">`fn_<span class="hljs-subst">$&#123;(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">999</span>).toFixed()&#125;</span>`</span> <span class="hljs-comment">// 防止极端情况下属性名冲突</span>
    content[fn] = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> args = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">arguments</span>.length; i++) &#123;
        args.push(<span class="hljs-string">`arguments[<span class="hljs-subst">$&#123;i&#125;</span>]`</span>)
    &#125;
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">eval</span>(<span class="hljs-string">`content[fn](<span class="hljs-subst">$&#123;args&#125;</span>)`</span>)
    <span class="hljs-keyword">delete</span> content[fn] <span class="hljs-comment">// 使用后释放</span>
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写个例子测试下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;t&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>) &#125;
&#125;
<span class="hljs-keyword">const</span> b = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'b'</span> &#125;

a.say.call(b, <span class="hljs-string">'hi'</span>) <span class="hljs-comment">// hi, b</span>
a.say.myCall(b, <span class="hljs-string">'hello'</span>) <span class="hljs-comment">// hello, b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">防抖</h2>
<p>以滚动事件为例，防抖即是滚动过程中低频率地触发事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onscroll = throttle(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'throttle'</span>); <span class="hljs-comment">// 持续滚动只会间隔1s有节奏地执行打印</span>
&#125;, <span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定时器throttle实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, delay = <span class="hljs-number">1000</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (timer) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
            timer = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 闭包，释放timer</span>
        &#125;, delay)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间戳throttle实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, delayTime = <span class="hljs-number">1000</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> lastTime = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> nowTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
        <span class="hljs-keyword">if</span> (nowTime - lastTime > delayTime) &#123;
            fn.call(<span class="hljs-built_in">this</span>, ...arguments)
            lastTime = nowTime <span class="hljs-comment">// 也是闭包，维护一个时间戳</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">节流</h2>
<p>还是以滚动事件为例，节流即是滚动过程中只触发一次事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onscroll = debounce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'debounce'</span>); <span class="hljs-comment">// 直到完全停止滚动后1s才执行输出</span>
&#125;, <span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定时器debounce实现，与防抖就是一个模子刻出来的，不同的是节流不会多次执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, delay = <span class="hljs-number">1000</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (timer) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer) <span class="hljs-comment">// 与防抖的主要区别，前面的任务清除，只保留最后一次执行</span>
        &#125;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            fn.call(<span class="hljs-built_in">this</span>, ...arguments)
            timer = <span class="hljs-literal">null</span>
        &#125;, delay);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            