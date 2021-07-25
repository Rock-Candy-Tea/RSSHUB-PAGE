
---
title: 'Promise、Promise.all、Promise.race的用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3353'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 10:26:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=3353'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Promise 是解决异步问题的统一方案，Promise的用途有：规范回调的名字和顺序；避免回调地狱，使代码可读性更强；方便捕获错误。</p>
<h2 data-id="heading-0">创建一个 Promise</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(result) <span class="hljs-comment">//成功时调用 resolve</span>
    reject(error)   <span class="hljs-comment">//失败时调用 reject</span>
  &#125;)
&#125;

fn().then(success, fail).then(success2, fail2).catch(fail3)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">使用 Promise.all</h2>
<p>Promise.all 需要传入一个数组，数组中的元素都是 Promise 对象。<br>
当这些对象都执行成功时，则 all 对应的 promise 也成功，且执行 then 中的成功回调。<br>
如果有一个失败了，则 all 对应的 promise 失败，且失败时只能获得第一个失败 Promise 的数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'成功了'</span>)
&#125;)
<span class="hljs-keyword">const</span> p2 = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'success'</span>)
<span class="hljs-keyword">const</span> p3 = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'失败'</span>)

<span class="hljs-built_in">Promise</span>.all([p1, p2]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(result)  <span class="hljs-comment">//["成功了", "success"]</span>
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
  <span class="hljs-comment">//未被调用</span>
&#125;)

<span class="hljs-built_in">Promise</span>.all([p1, p3, p2]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-comment">//未被调用</span>
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error)  <span class="hljs-comment">//"失败"</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用 Promise.race</h2>
<p>Promise.race() 里面哪个 Promise 对象最快得到结果，就返回那个结果，不管结果本身是成功状态还是失败状态。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">500</span>, <span class="hljs-string">"one"</span>);
&#125;);
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">"two"</span>);
&#125;);
<span class="hljs-built_in">Promise</span>.race([p1, p2]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// "two"</span>
  <span class="hljs-comment">// 两个都完成，但 p2 更快</span>
&#125;);

<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">"three"</span>);
&#125;);
<span class="hljs-keyword">const</span> p4 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(reject, <span class="hljs-number">500</span>, <span class="hljs-string">"four"</span>);
&#125;);
<span class="hljs-built_in">Promise</span>.race([p3, p4]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// "three"</span>
  <span class="hljs-comment">// p3 更快，所以它完成了</span>
&#125;, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
  <span class="hljs-comment">// 未被调用</span>
&#125;);

<span class="hljs-keyword">const</span> p5 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">500</span>, <span class="hljs-string">"five"</span>);
&#125;);
<span class="hljs-keyword">const</span> p6 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(reject, <span class="hljs-number">100</span>, <span class="hljs-string">"six"</span>);
&#125;);
<span class="hljs-built_in">Promise</span>.race([p5, p6]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-comment">// 未被调用</span>
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error); <span class="hljs-comment">// "six"</span>
  <span class="hljs-comment">// p6 更快，所以它失败了</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            