
---
title: 'JavaScript底层实现数组的一些方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=798'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 18:33:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=798'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h4 data-id="heading-0">数组方法有 push、pop、slice、map 和 reduce</h4>
<h4 data-id="heading-1">push的实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...items</span>) </span>&#123;
        <span class="hljs-keyword">let</span> O = <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// ecma 中提到的先转换为对象</span>
        <span class="hljs-keyword">let</span> len = <span class="hljs-built_in">this</span>.length >>> <span class="hljs-number">0</span>;
        <span class="hljs-keyword">let</span> argCount = items.length >>> <span class="hljs-number">0</span>;
        <span class="hljs-comment">// 2 ^ 53 - 1 为JS能表示的最大正整数</span>
        <span class="hljs-keyword">if</span> (len + argCount > <span class="hljs-number">2</span> ** <span class="hljs-number">53</span> - <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"The number of array is over the max value"</span>)
        &#125;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < argCount; i++) &#123;
            O[len + i] = items[i];
        &#125;
        <span class="hljs-keyword">let</span> newLength = len + argCount;
        O.length = newLength;
        <span class="hljs-keyword">return</span> newLength;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码可以看出，关键点就在于给数组本身循环添加新的元素 item，然后调整数组的长度 length 为最新的长度，即可完成 push 的底层实现。</p>
<p>其中关于长度的部分需要做无符号位移，无符号位移在很多源码中你都会看到。关于为什么一些变量要进行无符号位移，你可以自己研究一下，比如在 Stack Overflow 中有一些高票的回答，这里就不占用篇幅了。下面我们再看来一下 pop 的实现。</p>
<h3 data-id="heading-2">pop 方法的底层实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> O = <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">let</span> len = <span class="hljs-built_in">this</span>.length >>> <span class="hljs-number">0</span>;
    <span class="hljs-keyword">if</span> (len === <span class="hljs-number">0</span>) &#123;
        O.length = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
    &#125;
    len --;
    <span class="hljs-keyword">let</span> value = O[len];
    <span class="hljs-keyword">delete</span> O[len];
    O.length = len;
    <span class="hljs-keyword">return</span> value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其核心思路还是在于删掉数组自身的最后一个元素，index 就是数组的 len 长度，然后更新最新的长度，最后返回的元素的值，即可达到想要的效果。另外就是在当长度为 0 的时候，如果执行 pop 操作，返回的是 undefined，需要做一下特殊处理。</p>
<p>看完了 pop 的实现，我们再来看一下 map 方法的底层逻辑。</p>
<h3 data-id="heading-3">map 方法的底层实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.map = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callbackFn, thisArg</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> === <span class="hljs-literal">null</span> || <span class="hljs-built_in">this</span> === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot read property 'map' of null"</span>);
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.toString.call(callbackfn) != <span class="hljs-string">"[object Function]"</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callbackfn + <span class="hljs-string">' is not a function'</span>)
    &#125;
    <span class="hljs-keyword">let</span> O = <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">let</span> T = thisArg;
    <span class="hljs-keyword">let</span> len = O.length >>> <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> A = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len);
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> k = <span class="hljs-number">0</span>; k < len; k++) &#123;
    <span class="hljs-keyword">if</span> (k <span class="hljs-keyword">in</span> O) &#123;
      <span class="hljs-keyword">let</span> kValue = O[k];
      <span class="hljs-comment">// 依次传入this, 当前项，当前索引，整个数组</span>
      <span class="hljs-keyword">let</span> mappedValue = callbackfn.call(T, KValue, k, O);
      A[k] = mappedValue;
    &#125;
    &#125;
    <span class="hljs-keyword">return</span> A;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了上面实现 push 和 pop 的基础思路，map 的实现也不会太难了，基本就是再多加一些判断，循环遍历实现 map 的思路，将处理过后的 mappedValue 赋给一个新定义的数组 A，最后返回这个新数组 A，并不改变原数组的值。</p>
<h3 data-id="heading-4">reduce 方法的底层实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.reduce = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callbackfn, initialValue</span>) </span>&#123;

<span class="hljs-comment">// 异常处理，和 map 类似</span>

<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> === <span class="hljs-literal">null</span> || <span class="hljs-built_in">this</span> === <span class="hljs-literal">undefined</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot read property 'reduce' of null"</span>);
&#125;

<span class="hljs-comment">// 处理回调类型异常</span>

<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.toString.call(callbackfn) != <span class="hljs-string">"[object Function]"</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callbackfn + <span class="hljs-string">' is not a function'</span>)
&#125;

<span class="hljs-keyword">let</span> O = <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">this</span>);
<span class="hljs-keyword">let</span> len = O.length >>> <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> k = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> accumulator = initialValue; <span class="hljs-comment">// reduce方法第二个参数作为累加器的初始值</span>
<span class="hljs-keyword">if</span> (accumulator === <span class="hljs-literal">undefined</span>) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Each element of the array is empty'</span>);
  <span class="hljs-comment">// 初始值不传的处理</span>
<span class="hljs-keyword">for</span>(; k < len ; k++) &#123;
  <span class="hljs-keyword">if</span> (k <span class="hljs-keyword">in</span> O) &#123;
    accumulator = O[k];
    k++;
    <span class="hljs-keyword">break</span>;
  &#125;

&#125;

&#125;

<span class="hljs-keyword">for</span>(;k < len; k++) &#123;
<span class="hljs-keyword">if</span> (k <span class="hljs-keyword">in</span> O) &#123;
  <span class="hljs-comment">// 注意 reduce 的核心累加器</span>
  accumulator = callbackfn.call(<span class="hljs-literal">undefined</span>, accumulator, O[k], O);
&#125;
&#125;

<span class="hljs-keyword">return</span> accumulator;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            