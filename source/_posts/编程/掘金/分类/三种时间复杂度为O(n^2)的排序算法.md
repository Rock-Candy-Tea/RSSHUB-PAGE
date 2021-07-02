
---
title: '三种时间复杂度为O(n^2)的排序算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9506'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 22:52:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=9506'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>所谓排序算法，即通过特定的算法因式将一组或多组数据按照既定模式进行重新排序。这种新序列遵循着一定的规则，体现出一定的规律，因此，经处理后的数据便于筛选和计算，大大提高了计算效率。对于排序，我们首先要求其具有一定的稳定性，即当两个相同的元素同时出现于某个序列之中，则经过一定的排序算法之后，两者在排序前后的相对位置不发生变化。换言之，即便是两个完全相同的元素，它们在排序过程中也是各有区别的，不允许混淆不清。</p>
</blockquote>
<h1 data-id="heading-0">冒泡排序</h1>
<p>冒泡排序是入门级的算法，但也有一些有趣的玩法。通常来说，冒泡排序有三种写法：</p>
<p>一边比较一边向后两两交换，将最大值 / 最小值冒泡到最后一位；
经过优化的写法：使用一个变量记录当前轮次的比较是否发生过交换，如果没有发生交换表示已经有序，不再继续排序；</p>
<h2 data-id="heading-1">基础算法</h2>
<blockquote>
<p>空间复杂度为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span>，时间复杂度为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><msup><mi>n</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = arr.length; i < len-<span class="hljs-number">1</span>; i++)&#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < len-<span class="hljs-number">1</span>-i; j++) &#123;
            <span class="hljs-keyword">if</span> (arr[j] > arr[j+<span class="hljs-number">1</span>]) &#123;
                [arr[j], arr[j+<span class="hljs-number">1</span>]] = [arr[j+<span class="hljs-number">1</span>], arr[j]];
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最外层的 for 循环每经过一轮，剩余数字中的最大值就会被移动到当前轮次的最后一位，中途也会有一些相邻的数字经过交换变得有序。总共比较次数是 (n-1)+(n-2)+(n-3)+…+1(n−1)+(n−2)+(n−3)+…+1。</p>
<h2 data-id="heading-2">第二种写法是在基础算法的基础上改良而来的：</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = arr.length; i < len - <span class="hljs-number">1</span>; i++) &#123;
        <span class="hljs-keyword">let</span> isSwap = <span class="hljs-literal">false</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < len - <span class="hljs-number">1</span> - i; j++) &#123;
            <span class="hljs-keyword">if</span> (arr[j] > arr[j + <span class="hljs-number">1</span>]) &#123;
                [arr[j], arr[j + <span class="hljs-number">1</span>]] = [arr[j + <span class="hljs-number">1</span>], arr[j]];
                isSwap = <span class="hljs-literal">true</span>
            &#125;
        &#125;
        <span class="hljs-keyword">if</span> (!isSwap) &#123;
            <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>空间复杂度为<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span>;时间复杂度为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><msup><mi>n</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>-最好为O(n);</p>
</blockquote>
<p>最外层的 for 循环每经过一轮，剩余数字中的最大值仍然是被移动到当前轮次的最后一位。这种写法相对于第一种写法的优点是：如果一轮比较中没有发生过交换，则立即停止排序，因为此时剩余数字一定已经有序了。</p>
<h1 data-id="heading-3">选择排序</h1>
<p>选择排序的思想是：双重循环遍历数组，每经过一轮比较，找到最小元素的下标，将其交换至首位。</p>
<h2 data-id="heading-4">基础算法</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = arr.length; i < len - <span class="hljs-number">1</span>; i++) &#123;
        <span class="hljs-keyword">let</span> minIndex = i
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i+<span class="hljs-number">1</span>; j < len; j++) &#123;
            <span class="hljs-keyword">if</span> (arr[i] > arr[j]) &#123;
                minIndex = j
            &#125;
        &#125;
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">二元选择排序-优化</h2>
<p>选择排序算法也是可以优化的，既然每轮遍历时找出了最小值，何不把最大值也顺便找出来呢？这就是二元选择排序的思想。</p>
<p>使用二元选择排序，每轮选择时记录最小值和最大值，可以把数组需要遍历的范围缩小一倍。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = arr.length; i < len / <span class="hljs-number">2</span>; i++) &#123;
        <span class="hljs-keyword">let</span> minIndex = i;
        <span class="hljs-keyword">let</span> maxIndex = i;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < len-i; j++) &#123;
            <span class="hljs-keyword">if</span> (arr[minIndex] > arr[j]) &#123;
                minIndex = j;
            &#125;
            <span class="hljs-keyword">if</span> (arr[maxIndex] < arr[j]) &#123;
                maxIndex = j;
            &#125;
        &#125;
        <span class="hljs-keyword">if</span> (minIndex === maxIndex) <span class="hljs-keyword">break</span>;
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
        <span class="hljs-keyword">if</span> (maxIndex === i) &#123;
            maxIndex = minIndex;
        &#125;
        <span class="hljs-keyword">const</span> lastIndex = len - i - <span class="hljs-number">1</span>;
        [arr[maxIndex], arr[lastIndex]] = [arr[lastIndex], arr[maxIndex]];
    &#125;
    <span class="hljs-keyword">return</span> arr; 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">插入排序</h1>
<p>插入排序的思想非常简单，生活中有一个很常见的场景：在打扑克牌时，我们一边抓牌一边给扑克牌排序，每次摸一张牌，就将它插入手上已有的牌中合适的位置，逐渐完成整个排序。</p>
<p>插入排序有两种写法：</p>
<ul>
<li>交换法：在新数字插入过程中，不断与前面的数字交换，直到找到自己合适的位置。</li>
<li>移动法：在新数字插入过程中，与前面的数字不断比较，前面的数字不断向后挪出位置，当新数字找到自己的位置后，插入一次即可。</li>
</ul>
<h2 data-id="heading-7">交换法插入排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>, len = arr.length; i < len; i++) &#123;
        <span class="hljs-keyword">let</span> j = i;
        <span class="hljs-keyword">while</span> (j >= <span class="hljs-number">1</span> && arr[j] < arr[j - <span class="hljs-number">1</span>]) &#123;
            [arr[j], arr[j - <span class="hljs-number">1</span>]] = [arr[j - <span class="hljs-number">1</span>], arr[j]];
            j--
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当数字少于两个时，不存在排序问题，当然也不需要插入，所以我们直接从第二个数字开始往前插入。</p>
<h2 data-id="heading-8">移动法</h2>
<p>我们发现，在交换法插入排序中，每次都要交换数字。但实际上，新插入的这个数字并不一定适合与它交换的数字所在的位置。也就是说，它刚换到新的位置上不久，下一次比较后，如果又需要交换，它马上又会被换到前一个数字的位置。</p>
<p>由此，我们可以想到一种优化方案：让新插入的数字先进行比较，前面比它大的数字不断向后移动，直到找到适合这个新数字的位置后再插入。</p>
<p>这种方案我们需要把新插入的数字暂存起来，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>, len = arr.length; i < len; i++) &#123;
        <span class="hljs-keyword">let</span> j = i-<span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> cur = arr[i];
        <span class="hljs-keyword">while</span> (j >= <span class="hljs-number">0</span> && cur < arr[j]) &#123;
            arr[j+<span class="hljs-number">1</span>] = arr[j]
            j--;
        &#125;
        arr[j+<span class="hljs-number">1</span>] = cur
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            