
---
title: '【译】JavaScript 中的延迟加载属性模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=665'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 00:35:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=665'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a> （不知道翻译算不算）。</p>
<blockquote>
<p>英文原文 ：<a href="https://humanwhocodes.com/blog/2021/04/lazy-loading-property-pattern-javascript/" target="_blank" rel="nofollow noopener noreferrer">The lazy-loading property pattern in JavaScript</a> by Nicholas C. Zakas（红宝书第三版作者）</p>
</blockquote>
<p>通常，开发者在 JavaScript 类中为实例中可能需要的任意数据而创建属性。对于在构造函数中随时可用的一小部分数据来说，这不是问题。但是，如果在实例中可用之前需要计算某些数据，您可能并不想预先就造成计算开销。例如，考虑这个类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.data = someExpensiveComputation();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面，<code>data</code>属性是作为执行一些开销大计算的结果而创建的。如果您不确定是否会使用该属性，则预先执行该计算可能效率不高。幸运的是，有几种方法可以将这些操作推迟到以后。</p>
<h2 data-id="heading-0">按需属性模式</h2>
<p>优化计算开销大操作的最简单方法是等到需要数据后再进行计算。例如，您可以使用带有 <code>getter</code>的访问器属性来按需进行计算，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">get</span> <span class="hljs-title">data</span>() &#123;
        <span class="hljs-keyword">return</span> someExpensiveComputation();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，直到有人第一次读取数据属性时才会进行计算，这算是一个改进。然而，每次<code>data</code>属性被访问的时候都会造成同样的计算开销，它甚至比之前至少执行一次计算的例子还要更加糟糕。这并不是一个很好的解决方法，但是您可以在此基础上创造一个更好的。</p>
<h2 data-id="heading-1">凌乱的延迟加载属性模式</h2>
<p>只在访问属性时才执行计算是一个良好的开端。您真正需要的是在此之后就缓存信息并且之后只使用缓存版本就可以了。但是您将这些信息缓存在哪里以便于访问？最简单的方法是定义一个具有相同名称的属性并将其值设置为计算数据，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">get</span> <span class="hljs-title">data</span>() &#123;
        <span class="hljs-keyword">const</span> actualData = someExpensiveComputation();

        <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"data"</span>, &#123;
            <span class="hljs-attr">value</span>: actualData,
            <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>
        &#125;);

        <span class="hljs-keyword">return</span> actualData;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面，<code>data</code>属性又一次在类中被定义为一个<code>getter</code>，但是这次它缓存了结果。<code>Object.defineProperty()</code>的调用创建了一个新属性<code>data</code>，它有一个固定的<code>actualData</code>值，并切它被设置为不可写、不可配置、不可枚举（以匹配<code>getter</code>）。然后，这个值本身被返回。下次<code>data</code>属性被访问的时候，它会读取最近创建的属性的值，而不是调用<code>getter</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> object = <span class="hljs-keyword">new</span> MyClass();

<span class="hljs-comment">// calls the getter</span>
<span class="hljs-keyword">const</span> data1 = object.data;

<span class="hljs-comment">// reads from the data property</span>
<span class="hljs-keyword">const</span> data2 = object.data;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，所有计算仅在第一次读取数据属性时完成。每次对数据属性的后续读取都返回缓存的版本。</p>
<p>这种模式的一个缺点是 <code>data</code> 属性开始是不可枚举的原型属性，最终是不可枚举的实例属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> object = <span class="hljs-keyword">new</span> MyClass();
<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// false</span>

<span class="hljs-keyword">const</span> data = object.data;
<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这种区别在很多情况下并不重要，但理解这种模式很重要，因为当对象被传递时它可能会导致微妙的问题。幸运的是，使用改进的模式很容易解决这个问题。</p>
<blockquote>
<p>译者注：属性有两种类型：数据属性和访问器属性。它们都有<code>configurable（可配置）</code>、<code>enumerable（可枚举）</code>两个特性，区别在于数据属性有<code>value</code>、<code>writable（可写）</code>，访问器属性有<code>setter</code>、<code>getter</code>。它们是不能同时存在的，如果同时设置了数据属性和访问器属性会报错。原文说之后再读取<code>data</code>属性不会调用<code>getter</code>是因为第二次调用时把<code>data</code>设置为了不可配置的数据属性，也就是说<code>Object.defineProperty</code>并不会在下一次执行。</p>
</blockquote>
<h2 data-id="heading-2">类的特有的延迟加载属性模式</h2>
<p>如果您有一个场景是让延迟加载的属性始终存在于实例自身中，那么您可以使用<code>Object.defineProperty()</code>在类构造函数中创建属性。它比前面的例子还要混乱，但它会确保该属性只存在于实例中。下面是一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;

        <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"data"</span>, &#123;
            <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">const</span> actualData = someExpensiveComputation();

                <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"data"</span>, &#123;
                    <span class="hljs-attr">value</span>: actualData,
                    <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>,
                    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>
                &#125;);

                <span class="hljs-keyword">return</span> actualData;
            &#125;,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
        &#125;);

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面，构造函数使用 <code>Object.defineProperty()</code> 创建数据访问器属性。该属性在实例中创建（通过使用<code>this</code>）并且定义了一个<code>getter</code>以及将属性指定为可枚举和可配置（典型的实例自身属性）。设置<code>data</code>为可配置的属性是尤为重要的，这样你下一次还可以调用<code>Object.defineProperty()</code>。</p>
<p><code>getter</code>函数执行了计算并且再次调用了<code>Object.defineProperty()</code>。<code>data</code>属性现在被重新定义为一个被指定由明确值的数据属性并且配置了不可写和不可配置来保护最终的数据。然后被计算的数据从<code>getter</code>中返回。下次<code>data</code>访问的时候，它会从缓存中读取。另外，<code>data</code>属性现在只作为实例自身属性存在没并且在第一次读取之前和之后的行为都相同：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> object = <span class="hljs-keyword">new</span> MyClass();
<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> data = object.data;
<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于类，这很可能是您要使用的模式，而对于对象字面量可以使用更简单的方法。</p>
<h2 data-id="heading-3">对象字面量的延迟加载属性模式</h2>
<p>如果您使用对象字面量而不是类，则过程要简单得多，因为在对象字面量上定义的 <code>getter</code> 被定义为可枚举的自身属性（而不是原型属性），就像数据属性一样。这意味着您可以对类使用"凌乱的延迟加载属性模式"而不会混乱：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> object = &#123;
    <span class="hljs-keyword">get</span> <span class="hljs-title">data</span>() &#123;
        <span class="hljs-keyword">const</span> actualData = someExpensiveComputation();

        <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"data"</span>, &#123;
            <span class="hljs-attr">value</span>: actualData,
            <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>
        &#125;);

        <span class="hljs-keyword">return</span> actualData;
    &#125;
&#125;;

<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> data = object.data;
<span class="hljs-built_in">console</span>.log(object.hasOwnProperty(<span class="hljs-string">"data"</span>));     <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<p>在 JavaScript 中重新定义对象属性的能力提供了一个特有的机会来缓存可能计算开销大的信息。通过从重新定义为数据属性的访问器属性开始，您可以将计算推迟到第一次读取属性时，然后缓存结果以供以后使用。这种方法既适用于类，也适用于对象字面量，并且在对象字面量中更简单一些，因为您不必担心您的 <code>getter </code>会在原型上结束。</p>
<p>提高性能的最好方法之一是避免重复执行相同的工作，因此任何时候您可以缓存结果以供以后使用，您都可以加快程序的运行速度。延迟加载属性模式等技术允许任何属性成为缓存层以提高性能。</p></div>  
</div>
            