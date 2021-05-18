
---
title: '有关 ECMAScript 最新版本的所有信息｜ECMAScript 2021'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3e0e56e00c49409ac548b0aed37f41~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 05:27:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3e0e56e00c49409ac548b0aed37f41~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://levelup.gitconnected.com/everything-about-the-latest-ecmascript-release-ecmascript-2021-c011e817f41a" target="_blank" rel="nofollow noopener noreferrer">Everything about the latest ECMAScript release | ECMAScript 2021</a></li>
<li>原文作者：<a href="https://medium.com/@kritikasharmablog" target="_blank" rel="nofollow noopener noreferrer">Kritika Sharma</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/everything-about-the-latest-ecmascript-release-ecmascript-2021.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/Hoarfroster" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/KimYangOfCat" target="_blank" rel="nofollow noopener noreferrer">KimYang</a>、<a href="https://github.com/Tong-H" target="_blank" rel="nofollow noopener noreferrer">Tong-H</a></li>
</ul>
</blockquote>
<p>在本文中，我们将通过一些示例代码向大家介绍 ECMAScript 2021 最新版本的功能。</p>
<h2 data-id="heading-0">新的功能</h2>
<h3 data-id="heading-1">1. String.replaceAll( )</h3>
<p>将查找到的目标字符串的所有实例替换为所需的字符串：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fact = <span class="hljs-string">"JavaScript is the best web scripting language. JavaScript can be used for both front end and backend"</span>;
 
<span class="hljs-built_in">console</span>.log(fact.replaceAll(<span class="hljs-string">"JavaScript"</span>, <span class="hljs-string">"TypeScript"</span>));

<span class="hljs-comment">// 输出：</span>
<span class="hljs-comment">// "TypeScript is the best web scripting language. TypeScript can be used for both front end and backend";</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与之前的 <code>replace()</code> 方法（仅将目标字符串的第一个匹配项替换为所需的字符串）相比：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fact = <span class="hljs-string">"JavaScript is the best web scripting language. JavaScript can be used for both front end and backend"</span>;
 
<span class="hljs-built_in">console</span>.log(fact.replace(<span class="hljs-string">"JavaScript"</span>, <span class="hljs-string">"TypeScript"</span>));

<span class="hljs-comment">// 输出：</span>
<span class="hljs-comment">// "TypeScript is the best web scripting language. JavaScript can be used for both front end and backend";</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. Promise.any( )</h3>
<p>只要所提供的<code>Promise</code> 中的任何一个得到解决，<code>Promise.any()</code> 就会直接被解决，而 <code>Promise.all()</code> 则等待所有的 <code>Promise</code> 都得到解决后才会标记为解决，基本上与 <code>Promise.all()</code> 相反。</p>
<p>如果 <strong>“兑现了一个 <code>Promise</code>”</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [   
          <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'错误 A'</span>),           
          <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'错误 B'</span>),   
          <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'结果'</span>), 
]; 

<span class="hljs-built_in">Promise</span>
  .any(promises)
  .then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> assert.equal(result, <span class="hljs-string">'结果'</span>)); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <strong>“所有 <code>Promise</code> 都是被拒绝的”</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [   
          <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'错误 A'</span>),  
          <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'错误 B'</span>),   
          <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'错误 C'</span>), 
]; 

<span class="hljs-built_in">Promise</span>
  .any(promises)   
  .catch(<span class="hljs-function">(<span class="hljs-params">aggregateError</span>) =></span> &#123;
            assert.deepEqual(aggregateError.errors, 
            [<span class="hljs-string">'错误 A'</span>, <span class="hljs-string">'错误 B'</span>, <span class="hljs-string">'错误 C'</span>]); <span class="hljs-comment">//true</span>
   &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3. 逻辑赋值操作符</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3e0e56e00c49409ac548b0aed37f41~tplv-k3u1fbpfcp-zoom-1.image" alt="来源: [https://exploringjs.com/impatient-js/ch_operators.html#logical-assignment-operators]" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>a ||= b</code> 等同于 <code>a || (a = b)</code>（短路运算符）</p>
<p>为何不是 <code>a = a || b</code>？</p>
<p>好吧，因为对于前一个表达式，只有在 <code>a</code> 计算为 <code>false</code> 时，赋值才会被执行。因此，前者仅在必要时才会被赋值。相反，后一个表达式始终执行赋值。</p>
<p><code>a ||= b</code> 的一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;  
<span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>;  
 
a ||= b;   

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>a &&= b</code> 的一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>; 
<span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>; 

a &&= b; 

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>a ??= b</code> 的一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a;  
<span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>;   

a ??= b;   

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. 数字分隔符</h3>
<p>现在，我们可以使用 <strong>下划线（<code>_</code>）</strong> 作为数字文字和 bigInt 文字的分隔符。这将帮助开发人员提高其数字文字的可读性（“下划线”基本上会充当我们平日生活中书写数字时候所用的“逗号”（用于在不同的数字组之间提供分隔））。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> budget = <span class="hljs-number">1000000000000</span>; <span class="hljs-comment">// 可以这样写：</span>

<span class="hljs-keyword">let</span> budget = <span class="hljs-number">1_000_000_000_000</span>; 

<span class="hljs-built_in">console</span>.log(budget); <span class="hljs-comment">// 会打印正常数字：</span>

<span class="hljs-comment">// 输出：</span>
<span class="hljs-comment">// 1000000000000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>希望本文能帮助您了解 ECMAScript 的最新版本。感谢您的阅读，如有任何疑问，请随时发表评论。</p>
<p>参考资料：</p>
<ul>
<li><a href="https://dev.to/faithfulojebiyi/new-features-in-ecmascript-2021-with-code-examples-302h" target="_blank" rel="nofollow noopener noreferrer">dev.to/faithfuloje…</a></li>
<li><a href="https://2ality.com/2020/09/ecmascript-2021.html" target="_blank" rel="nofollow noopener noreferrer">2ality.com/2020/09/ecm…</a></li>
</ul>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            