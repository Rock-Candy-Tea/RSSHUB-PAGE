
---
title: '夯实基础篇----讲讲js中的循环与迭代'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3074'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 06:36:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=3074'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>；</p>
<h2 data-id="heading-0">写在前面</h2>
<p>日常写代码，难免会需要列表渲染等需要循环的场景，今天我们就来一起回顾一下js中那些用于循环的语句吧。</p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">for语句</h3>
<p>for语句可谓是最经典也最全能的循环语句选手了，使用起来很方便，自由度也很高，比如输出0到100，我们可以这样写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以了，for当中接收三个表达式，第一个为初始值，第二个为循环条件，第三个为循环执行后要执行的表达式。</p>
<h3 data-id="heading-3">do...while语句</h3>
<p>do wilie语句和for最大的不同就是，它至少会执行一次，若满足循环条件就一直执行，输出0到100的代码示例如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">do</span> &#123;
  i += <span class="hljs-number">1</span>;
  <span class="hljs-built_in">console</span>.log(i);
&#125; <span class="hljs-keyword">while</span> (i <= <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">while语句</h3>
<p>while用起来，就比do while语句更符合常理了，只有符合循环条件，才会进行循环，这样就能够防止多执行一次循环内容才进行判断了，同样的输出0到100的代码示例如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">while</span> (i <= <span class="hljs-number">100</span>) &#123;
  <span class="hljs-built_in">console</span>.log(i++);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">break 和 continue语句</h3>
<p>当然，在循环中我们可能会需要跳出当前循环体，或是跳出当前一次的循环进行之后的循环，那么就需要这两个语句了。</p>
<ul>
<li>break 跳出当前循环体</li>
<li>continue 跳出本次循环，继续之后的循环</li>
</ul>
<p>那么，如果我们有一个开始为0，循环条件为小于等于100的一个for循环，我们应该怎样让它输出到50就不继续进行呢？这里break就能够很好的处理了，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
  <span class="hljs-keyword">if</span> (i <= <span class="hljs-number">50</span>) &#123;
      <span class="hljs-built_in">console</span>.log(i);
  &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好，现在如果我们的需求变成了，这里0到100当中不输出50到60，这就需要用到continue了，我们可以这样写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
  <span class="hljs-keyword">if</span> (i <= <span class="hljs-number">50</span> || i >= <span class="hljs-number">60</span>) &#123;
      <span class="hljs-built_in">console</span>.log(i);
  &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">continue</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">总结</h2>
<p>本篇文章我们一起回顾了js中的循环与迭代，以及跳出当前循环即跳出本次循环的方法，大家加油。</p>
<p>前端漫漫长途，我们都在路上，希望可以和小伙伴们一起交流，一起进步。持续更新ing.....</p></div>  
</div>
            