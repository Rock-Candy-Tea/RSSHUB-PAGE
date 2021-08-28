
---
title: '分析并实现几个常见的es5方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2622'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 02:44:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=2622'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>兀然想起一次面试被问实现ES5的bind方法，当时懵了，后面的回答一下子没了分寸。其实那些都是基础知识，今天就来实现一下Es5的几个重要的方法bind、forEach等，再纪念一下当时的囧态。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">bind</h2>
<p>bind方法解析：</p>
<ul>
<li>每个函数实例都可调用此方法</li>
<li>可指定函数的执行上下文：<code>this</code></li>
<li><code>先前参数</code>和<code>新参数</code>共同组成函数的参数</li>
</ul>
<p>接着我们来确定实现方案：</p>
<ul>
<li>bind函数挂在Function的原型上</li>
<li>返回一个匿名函数</li>
<li>将两种参数组合传递给bind函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.bind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//get context</span>
    <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
    <span class="hljs-comment">//get function invoked in the future</span>
    <span class="hljs-keyword">let</span> fn = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// get front args</span>
    <span class="hljs-keyword">let</span> frontArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>,<span class="hljs-number">1</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> afterArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>,<span class="hljs-number">0</span>);
        <span class="hljs-keyword">let</span> finalArgs = frontArgs.concat(afterArgs);
        <span class="hljs-keyword">return</span> fn.apply(context,finalArgs )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">forEach</h2>
<p>forEach方法解析：</p>
<ul>
<li>仅限数组使用</li>
<li>回调参数为：每一项、索引、原数组</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.forEach = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> index=<span class="hljs-number">0</span>;index<arr.length;index++)&#123;
        fn(arr[index],index,arr)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">filter</h2>
<p>数组的filter解析：</p>
<ul>
<li>数组使用</li>
<li>过滤掉回调函数返回值不为true的项</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.filter = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;
    <span class="hljs-keyword">let</span> result = [];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> index=<span class="hljs-number">0</span>;index<arr.length;index++)&#123;
            <span class="hljs-keyword">let</span> invokedReturn = fn(arr[index],index,arr);
            <span class="hljs-keyword">if</span>( invokedReturn )&#123;
                    result.push(arr[index])
            &#125;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">find</h2>
<p>数组的find解析：</p>
<ul>
<li>数组使用</li>
<li>返回第一个回调函数返回true的项,没有则返回undefined</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.find= <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> index=<span class="hljs-number">0</span>;index<arr.length;index++)&#123;
            <span class="hljs-keyword">let</span> invokedReturn = fn(arr[index],index,arr);
            <span class="hljs-keyword">if</span>( invokedReturn )&#123;
                    <span class="hljs-keyword">return</span> arr[index]
            &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">every</h2>
<p>数组的every解析：</p>
<ul>
<li>数组使用</li>
<li>所有回调函数返回值都为true时 结果为true,否则为false</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.every= <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> index=<span class="hljs-number">0</span>;index<arr.length;index++)&#123;
            <span class="hljs-keyword">let</span> invokedReturn = fn(arr[index],index,arr);
            <span class="hljs-keyword">if</span>( !invokedReturn )&#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
            &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">some</h2>
<p>数组的some解析：</p>
<ul>
<li>数组使用</li>
<li>回调函数返回值一个为true 结果就为true, 否则为false</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.some= <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> index=<span class="hljs-number">0</span>;index<arr.length;index++)&#123;
        <span class="hljs-keyword">let</span> invokedReturn = fn(arr[index],index,arr);
        <span class="hljs-keyword">if</span>( invokedReturn )&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">reduce</h2>
<p>数组的reduce解析：</p>
<ul>
<li>数组使用</li>
<li>相比其他方法多了一个参数，上次调用的返回值</li>
<li>最后一个回调函数的返回值为reduce的结果</li>
<li>可以指定累积的初始值，不指定从第二项开始遍历</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.reduce= <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn,accumulator</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">"function"</span>)&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"参数必须为函数"</span>
    &#125;
    <span class="hljs-comment">//get array going to be iterated</span>
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(arr))&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-string">"只能对数组使用forEach方法"</span>
    &#125;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">if</span>(!accumulator)&#123;
            index = <span class="hljs-number">1</span>;
            accumulator = arr[<span class="hljs-number">0</span>];
    &#125;
    <span class="hljs-keyword">for</span>(;index<arr.length;index++)&#123;
            <span class="hljs-keyword">let</span> invokedReturn = fn(accumulator ,arr[index],index,arr);
            accumulator = invokedReturn ;
    &#125;
    <span class="hljs-keyword">return</span> accumulator ;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">最后</h2>
<p>感谢阅读！</p></div>  
</div>
            