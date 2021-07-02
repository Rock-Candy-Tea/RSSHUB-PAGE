
---
title: 'KMP算法分享'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc600db3964472eb75ca7f0dd62145d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 21:55:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc600db3964472eb75ca7f0dd62145d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文是前端内部分享，<a href="https://www.cnblogs.com/yjiyjige/p/3263858.html" target="_blank" rel="nofollow noopener noreferrer">参考文章</a></p>
<h3 data-id="heading-0">1. 什么是KMP</h3>
<p>一种改进的字符串匹配算法</p>
<h3 data-id="heading-1">2. 暴力匹配法</h3>
<p>目标字符串（上面）和模式串（下面）一个接一个的对比</p>
<pre><code class="copyable">      i
A B C A B D A B C E A B D
A B C E
      j               
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当第一次检测到不相同以后</p>
<pre><code class="copyable">  i
A B C A B D A B C E A B D
  A B C E
  j               
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 如果是人来处理，会怎么做？</h3>
<pre><code class="copyable">      i
A B C A B D A B C E A B D
      A B C E
      j               
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">例2</h4>
<pre><code class="copyable">          i
A B C A B C D H I J K
A B C A B B
          j
<span class="copy-code-btn">复制代码</span></code></pre>
<p>移动</p>
<pre><code class="copyable">          i
A B C A B C D H I J K
      A B C A B B
          k
<span class="copy-code-btn">复制代码</span></code></pre>
<p>特点：</p>
<ul>
<li>i不回溯，只需要调整j的位置</li>
<li></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc600db3964472eb75ca7f0dd62145d~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>公式：<code>P[0~k-1] == P[j-k~j-1] </code></p>
<p>（k为下一次跳转的位置）<br>
模式字符串的前k个等于j所在位置的前k个</p>
<p><strong>KMP算法的核心</strong>
找到左右的k（j跳转的下一个位置）</p>
<h3 data-id="heading-4">4. 获取下一个跳转位置的代码</h3>
<p>思路：</p>
<ul>
<li>设置双指针，j指针依次指向每一个元素，通过k指针计算j可以跳转的位置</li>
<li>当k指针与j指针相等时，两个指针同时相加；否则移动k指针到它可以移动的位置</li>
<li>每一次比较都是为了定 j + 1应该跳转的位置</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取下一个要跳转的位置</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNext</span> (<span class="hljs-params">ps</span>) </span>&#123;
  <span class="hljs-keyword">var</span> next = []
  next[<span class="hljs-number">0</span>] = -<span class="hljs-number">1</span> <span class="hljs-comment">// 初始化为-1</span>
  <span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> k = -<span class="hljs-number">1</span>
  <span class="hljs-keyword">while</span> (j < ps.length - <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">if</span> (k == -<span class="hljs-number">1</span> || ps[j] == ps[k]) &#123;
      next[j + <span class="hljs-number">1</span>] = k + <span class="hljs-number">1</span> <span class="hljs-comment">// 如果ps[j]==ps[k]，那么j+1跳转的位置就是k+1</span>
      j++
      k++
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果 ps[j] 和 ps[k] 不相等，要想求 j + 1的跳转值，先将指针移到next[k]的位置，</span>
      <span class="hljs-comment">// 如果k移动到next[k]后，ps[j] == ps[k]，那么立马就可以得出 next[j + 1]的位置</span>
      <span class="hljs-comment">// 如果和第一个元素比较以后还是不相等，那么 k = next[k] 将等于 -1</span>
      k = next[k]
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> next
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例</p>
<pre><code class="copyable">              j
a b c d a b c a b
      k

// [ -1, 0, 0, 0, 0, 1, 2, 3, 1]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5. KMP算法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ts 主串；ps 子字符串</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">KMP</span> (<span class="hljs-params">ts, ps</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span> <span class="hljs-comment">// 主串的位置</span>
  <span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span> <span class="hljs-comment">// 模式串的位置</span>
  <span class="hljs-keyword">let</span> next = getNext(ps) <span class="hljs-comment">// next只与ps有关</span>
  <span class="hljs-keyword">while</span> (i < ts.length && j < ps.length) &#123;
    <span class="hljs-keyword">if</span> (j == -<span class="hljs-number">1</span> || ts[i] == ps[j]) &#123;
      <span class="hljs-comment">// 当j为-1时，要移动的是i，当然j也要归0</span>
      i++
      j++
    &#125; <span class="hljs-keyword">else</span> &#123;
      j = next[j] <span class="hljs-comment">// j回到指定位置，如果赋值后等于0，那么就比较ps[0]与ts[j]是否相等</span>
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (j == ps.length) &#123;
    <span class="hljs-keyword">return</span> i - j <span class="hljs-comment">// 返回ps第一个字符所在的位置，i此时的位置是ps的最后一个字符所在的位置</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例</p>
<pre><code class="copyable">// 第一个不相同，i++
i
a b c d a b c a b
b c d
j


// ts[i]和ps[j]相同两个就同时相加
  i
a b c d a b c a b
  b c d
  j
  
      i
a b c d a b c a b
  b c d
      j
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6. 为什么可以不回溯</h3>
<ol>
<li>如果回溯后，不能保证前面的元素全部匹配就没有意义；</li>
<li>如果回溯后，前面的内容全部匹配了，那么肯定可以通过移动j的方式实现；</li>
</ol>
<h3 data-id="heading-7">7. 总结</h3>
<p>KMS算法就是首先找到模式串当每一个字符不匹配可以跳转的位置next，然后在与目标字符串进行比较时，如果不相同就将模式串的指针重新指向next对应的位置，然后继续比较。</p></div>  
</div>
            