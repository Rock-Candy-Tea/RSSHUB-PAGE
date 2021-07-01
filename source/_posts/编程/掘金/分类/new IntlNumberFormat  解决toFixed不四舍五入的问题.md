
---
title: 'new Intl.NumberFormat  解决toFixed不四舍五入的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3355'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:24:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=3355'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">toFixed()方法的坑</h2>
<h3 data-id="heading-1">1. 四舍五入并不是真正的四舍五入</h3>
<p>chrome 上的测试结果：</p>
<p>1.35.toFixed(1) // 1.4 正确</p>
<p>1.335.toFixed(2) // 1.33 错误</p>
<p>1.3335.toFixed(3) // 1.333 错误</p>
<p>1.33335.toFixed(4) // 1.3334 正确</p>
<p>1.333335.toFixed(5) // 1.33333 错误</p>
<p>1.3333335.toFixed(6) // 1.333333 错误</p>
<p>IE 上的测试结果：</p>
<p>1.35.toFixed(1) // 1.4 正确</p>
<p>1.335.toFixed(2) // 1.34 正确</p>
<p>1.3335.toFixed(3) // 1.334 正确</p>
<p>1.33335.toFixed(4) // 1.3334 正确</p>
<p>1.333335.toFixed(5) // 1.33334 正确</p>
<p>1.3333335.toFixed(6) // 1.333334 正确</p>
<p><strong>综上可以看到, 四舍五入在 chrome 中并不是真正的四舍五入</strong></p>
<h3 data-id="heading-2">2. 使用 Intl.NumberFormat()构造函数格式化数据</h3>
<p><code>Intl.NumberFormat</code>是浏览器内置的一个做数字做格式化处理的 API, 它是 Intl 命名空间下的一个构造器属性, 功能异常强大 👍
参考 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat" target="_blank" rel="nofollow noopener noreferrer">MDN</a></p>
<h4 data-id="heading-3">1.最少 & 最多保留几位小数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">3</span> &#125;).format(<span class="hljs-number">123456.78967</span>)
<span class="hljs-comment">// "123,456.790"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你这里有严格要求,建议把<code>minimumFractionDigits</code>和<code>maximumFractionDigits</code>都指定上, 要不可能会被舍弃掉, 比如只写<code>maximumFractionDigits</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123;<span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">3</span> &#125;).format(<span class="hljs-number">123456.78967</span>)
<span class="hljs-comment">// "123,456.79"</span>

<span class="hljs-comment">// 如果把原始数据变为123456.78867</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123;<span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">3</span> &#125;).format(<span class="hljs-number">123456.78867</span>)
<span class="hljs-comment">// "123,456.789"   此时又变成了三位了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们最常用的应该是保留两位小数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">2</span> &#125;).format(<span class="hljs-number">123456.78967</span>)
<span class="hljs-comment">// "123,456.79"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来验证一下上面使用<code>toFixed</code>的还有问题吗</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">2</span> &#125;).format(<span class="hljs-number">1.335</span>)
<span class="hljs-comment">// "1.34"</span>

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">3</span> &#125;).format(<span class="hljs-number">1.3335</span>)
<span class="hljs-comment">// "1.334"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完美؏؏☝ᖗ乛◡乛ᖘ☝؏؏</p>
<h4 data-id="heading-4">2.总量统计（以易于阅读的形式）--- notation在IE11不被支持,</h4>
<p>兼容的处理方案在这里: <a href="https://formatjs.io/docs/polyfills/intl-numberformat/" target="_blank" rel="nofollow noopener noreferrer">formatjs.io/docs/polyfi…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> nums = [<span class="hljs-number">1234</span>, <span class="hljs-number">123456.78967</span>, <span class="hljs-number">1223562434</span>, <span class="hljs-number">1223562434454</span>, <span class="hljs-number">12235624344544165</span>]

nums.map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-string">'en-US'</span>, &#123; <span class="hljs-attr">notation</span>: <span class="hljs-string">"compact"</span> &#125;).format(num)
&#125;)
<span class="hljs-comment">// ["1.2K", "123K", "1.2B", "1.2T", "12,236T"]</span>
nums.map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-string">'zh-CN'</span>, &#123; <span class="hljs-attr">notation</span>: <span class="hljs-string">"compact"</span> &#125;).format(num)
&#125;)
<span class="hljs-comment">// ["1234", "12万", "12亿", "1.2万亿", "12,236万亿"]</span>
nums.map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-string">'ja-JP'</span>, &#123; <span class="hljs-attr">notation</span>: <span class="hljs-string">"compact"</span> &#125;).format(num)
&#125;)
<span class="hljs-comment">// ["1234", "12万", "12億", "1.2兆", "12,236兆"]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.百分比显示</h4>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-number">0.01</span>, <span class="hljs-number">1.2</span>, <span class="hljs-number">0.0123</span>].map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">style</span>: <span class="hljs-string">'percent'</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">2</span> &#125;).format(num) 
&#125;)
<span class="hljs-comment">// ["1%", "120%", "1.23%"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">4.不使用千分位</h4>
<ul>
<li><code>useGrouping</code>：是否使用分组分隔符。如千位分隔符或千/万/亿分隔符，可能的值是 true 和 false ，默认值是 true</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">useGrouping</span>: <span class="hljs-literal">false</span> &#125;).format(<span class="hljs-number">123456.78967</span>)
<span class="hljs-comment">// "123456.79"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">5.加上¥符号,表示多少钱</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.NumberFormat(<span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">minimumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">maximumFractionDigits</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">style</span>: <span class="hljs-string">'currency'</span>, <span class="hljs-attr">currency</span>: <span class="hljs-string">'CNY'</span> &#125;).format(<span class="hljs-number">123456.78967</span>)
<span class="hljs-comment">// "¥123,456.79"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结束🔚</p>
<p>我是南飞雁，你可以叫我飞雁，我是一名奋斗者，在实现财富自由的路上……</p>
<p>我喜欢分享，也喜欢思考；我有自己的人生规划和梦想；但有时也很迷茫……</p>
<p>我从事IT行业，研究的技术领域相对比较多而杂： PHP、MySQL、Linux、JavaScript、Node.js、NoSQL、PhotoShop、音视频处理、架构集群、网络通信、生活技巧、人生三观、做人做事读书……</p>
<p>我总是会在自己的公众号和掘金上写下自己的所思所想和近期要做的事，希望你关注我，我是一个奋斗者，我叫南飞雁</p></div>  
</div>
            