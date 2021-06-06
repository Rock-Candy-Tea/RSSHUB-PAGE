
---
title: 'js解无重复字符的最长子串'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2584'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 18:23:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=2584'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<div class="tab-pane__1SHj css-12hreja-TabContent e16udao5"><div class="description__2b0C"><div class="css-xfm0cl-Container eugt34i0"><h4 class="css-10c1h40-Title eugt34i1" data-id="heading-0">无重复字符的最长子串</h4><div class="css-1e1vffy-Tools e1o5n5iy0"><span class="css-1p5igso-Difficulty e1o5n5iy1">难度</span><span class="css-1p5igso-Difficulty e1o5n5iy1">中等</span><span>5565</span></div></div><div class="content__1Y2H"><div class="notranslate"><p>给定一个字符串，请你找出其中不含有重复字符的 <strong>最长子串 </strong>的长度。</p>
<p> </p>
<p><strong>示例 1:</strong></p>
<pre><strong>输入: </strong>s = "abcabcbb"
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code class="copyable">"abc"，所以其<span class="copy-code-btn">复制代码</span></code>长度为 3。
</pre>
<p><strong>示例 2:</strong></p>
<pre><strong>输入: </strong>s = "bbbbb"
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code class="copyable">"b"<span class="copy-code-btn">复制代码</span></code>，所以其长度为 1。
</pre>
<p><strong>示例 3:</strong></p>
<pre><strong>输入: </strong>s = "pwwkew"
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是 <code class="copyable">"wke"<span class="copy-code-btn">复制代码</span></code>，所以其长度为 3。
     请注意，你的答案必须是 <strong>子串 </strong>的长度，<code class="copyable">"pwke"<span class="copy-code-btn">复制代码</span></code> 是一个<em>子序列，</em>不是子串。
</pre>
<p><strong>示例 4:</strong></p>
<pre><strong>输入: </strong>s = ""
<strong>输出: </strong>0
</pre>
<p> </p>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 <= s.length <= 5 * 10<sup>4</sup></code></li>
<li><code>s</code> 由英文字母、数字、符号和空格组成</li>
</ul>
<div class="e1ak08xt1 css-154e5au-StyledRenderedMarkdown">
<h3 data-id="heading-1">📖 文字题解</h3>
<h4 id="user-content-方法一：滑动窗口" data-id="heading-2"><a class="header-anchor" href="https://juejin.cn/post/6969758380835471373#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3"></a> 方法一：滑动窗口</h4>
<p><strong>思路和算法</strong></p>
<p>我们先用一个例子考虑如何在较优的时间复杂度内通过本题。</p>
<p>我们不妨以示例一中的字符串 <span class="katex"><span class="katex-mathml">abcabcbb\texttt&#123;abcabcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcabcbb</span></span></span></span></span> 为例，找出<strong>从每一个字符开始的，不包含重复字符的最长子串</strong>，那么其中最长的那个字符串即为答案。对于示例一中的字符串，我们列举出这些结果，其中括号中表示选中的字符以及最长的字符串：</p>
<ul>
<li>以 <span class="katex"><span class="katex-mathml">(a)bcabcbb\texttt&#123;(a)bcabcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">(a)bcabcbb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">(abc)abcbb\texttt&#123;(abc)abcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">(abc)abcbb</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">a(b)cabcbb\texttt&#123;a(b)cabcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">a(b)cabcbb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">a(bca)bcbb\texttt&#123;a(bca)bcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">a(bca)bcbb</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">ab(c)abcbb\texttt&#123;ab(c)abcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">ab(c)abcbb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">ab(cab)cbb\texttt&#123;ab(cab)cbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">ab(cab)cbb</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">abc(a)bcbb\texttt&#123;abc(a)bcbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abc(a)bcbb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">abc(abc)bb\texttt&#123;abc(abc)bb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abc(abc)bb</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">abca(b)cbb\texttt&#123;abca(b)cbb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abca(b)cbb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">abca(bc)bb\texttt&#123;abca(bc)bb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abca(bc)bb</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">abcab(c)bb\texttt&#123;abcab(c)bb&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcab(c)bb</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">abcab(cb)b\texttt&#123;abcab(cb)b&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcab(cb)b</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">abcabc(b)b\texttt&#123;abcabc(b)b&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcabc(b)b</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">abcabc(b)b\texttt&#123;abcabc(b)b&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcabc(b)b</span></span></span></span></span>；</li>
<li>以 <span class="katex"><span class="katex-mathml">abcabcb(b)\texttt&#123;abcabcb(b)&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcabcb(b)</span></span></span></span></span> 开始的最长字符串为 <span class="katex"><span class="katex-mathml">abcabcb(b)\texttt&#123;abcabcb(b)&#125;</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord text"><span class="mord texttt">abcabcb(b)</span></span></span></span></span>。</li>
</ul>
<p>发现了什么？如果我们依次递增地枚举子串的起始位置，那么子串的结束位置也是递增的！这里的原因在于，假设我们选择字符串中的第 <span class="katex"><span class="katex-mathml">kk</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">k</span></span></span></span> 个字符作为起始位置，并且得到了不包含重复字符的最长子串的结束位置为 <span class="katex"><span class="katex-mathml">rkr_k</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>。那么当我们选择第 <span class="katex"><span class="katex-mathml">k+1k+1</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">k</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">1</span></span></span></span> 个字符作为起始位置时，首先从 <span class="katex"><span class="katex-mathml">k+1k+1</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">k</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">1</span></span></span></span> 到 <span class="katex"><span class="katex-mathml">rkr_k</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span> 的字符显然是不重复的，并且由于少了原本的第 <span class="katex"><span class="katex-mathml">kk</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">k</span></span></span></span> 个字符，我们可以尝试继续增大 <span class="katex"><span class="katex-mathml">rkr_k</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>，直到右侧出现了重复字符为止。</p>
<p>这样一来，我们就可以使用「滑动窗口」来解决这个问题了：</p>
<ul>
<li>
<p>我们使用两个指针表示字符串中的某个子串（或窗口）的左右边界，其中左指针代表着上文中「枚举子串的起始位置」，而右指针即为上文中的 <span class="katex"><span class="katex-mathml">rkr_k</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>；</p>
</li>
<li>
<p>在每一步的操作中，我们会将左指针向右移动一格，表示 <strong>我们开始枚举下一个字符作为起始位置</strong>，然后我们可以不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符。在移动结束后，这个子串就对应着 <strong>以左指针开始的，不包含重复字符的最长子串</strong>。我们记录下这个子串的长度；</p>
</li>
<li>
<p>在枚举结束后，我们找到的最长的子串的长度即为答案。</p>
</li>
</ul>
<p><strong>判断重复字符</strong></p>
<p>在上面的流程中，我们还需要使用一种数据结构来判断 <strong>是否有重复的字符</strong>，常用的数据结构为哈希集合（即 <code>C++</code> 中的 <code>std::unordered_set</code>，<code>Java</code> 中的 <code>HashSet</code>，<code>Python</code> 中的 <code>set</code>, <code>JavaScript</code> 中的 <code>Set</code>）。在左指针向右移动的时候，我们从哈希集合中移除一个字符，在右指针向右移动的时候，我们往哈希集合中添加一个字符。</p>
<p>至此，我们就完美解决了本题。</p>
<div class="css-hhbtqi">
<pre><i></i><code class="copyable"><span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-comment">// 哈希集合，记录每个字符是否出现过</span>
    <span class="hljs-keyword">const</span> occ = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
    <span class="hljs-keyword">const</span> n = s.length;
    <span class="hljs-comment">// 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动</span>
    <span class="hljs-keyword">let</span> rk = <span class="hljs-number">-1</span>, ans = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; ++i) &#123;
        <span class="hljs-keyword">if</span> (i != <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">// 左指针向右移动一格，移除一个字符</span>
            occ.delete(s.charAt(i - <span class="hljs-number">1</span>));
        &#125;
        <span class="hljs-keyword">while</span> (rk + <span class="hljs-number">1</span> < n && !occ.has(s.charAt(rk + <span class="hljs-number">1</span>))) &#123;
            <span class="hljs-comment">// 不断地移动右指针</span>
            occ.add(s.charAt(rk + <span class="hljs-number">1</span>));
            ++rk;
        &#125;
        <span class="hljs-comment">// 第 i 到 rk 个字符是一个极长的无重复字符子串</span>
        ans = <span class="hljs-built_in">Math</span>.max(ans, rk - i + <span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-keyword">return</span> ans;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</div><p><strong>复杂度分析</strong></p>
<ul>
<li>
<p>时间复杂度：<span class="katex"><span class="katex-mathml">O(N)O(N)</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">O</span><span class="mopen">(</span><span class="mord mathdefault">N</span><span class="mclose">)</span></span></span></span>，其中 <span class="katex"><span class="katex-mathml">NN</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">N</span></span></span></span> 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。</p>
</li>
<li>
<p>空间复杂度：<span class="katex"><span class="katex-mathml">O(∣Σ∣)O(|\Sigma|)</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">O</span><span class="mopen">(</span><span class="mord">∣</span><span class="mord">Σ</span><span class="mord">∣</span><span class="mclose">)</span></span></span></span>，其中 <span class="katex"><span class="katex-mathml">Σ\Sigma</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord">Σ</span></span></span></span> 表示字符集（即字符串中可以出现的字符），<span class="katex"><span class="katex-mathml">∣Σ∣|\Sigma|</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord">∣</span><span class="mord">Σ</span><span class="mord">∣</span></span></span></span> 表示字符集的大小。在本题中没有明确说明字符集，因此可以默认为所有 ASCII 码在 <span class="katex"><span class="katex-mathml">[0,128)[0, 128)</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mopen">[</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace"></span><span class="mord">1</span><span class="mord">2</span><span class="mord">8</span><span class="mclose">)</span></span></span></span> 内的字符，即 <span class="katex"><span class="katex-mathml">∣Σ∣=128|\Sigma| = 128</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord">∣</span><span class="mord">Σ</span><span class="mord">∣</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">1</span><span class="mord">2</span><span class="mord">8</span></span></span></span>。我们需要用到哈希集合来存储出现过的字符，而字符最多有 <span class="katex"><span class="katex-mathml">∣Σ∣|\Sigma|</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord">∣</span><span class="mord">Σ</span><span class="mord">∣</span></span></span></span> 个，因此空间复杂度为 <span class="katex"><span class="katex-mathml">O(∣Σ∣)O(|\Sigma|)</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathdefault">O</span><span class="mopen">(</span><span class="mord">∣</span><span class="mord">Σ</span><span class="mord">∣</span><span class="mclose">)</span></span></span></span></p>
</li>
</ul>
</div></div></div></div></div></div>  
</div>
            