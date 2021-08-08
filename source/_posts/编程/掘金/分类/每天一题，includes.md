
---
title: '每天一题，includes'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9489'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 01:41:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=9489'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>每天一题，坚持思考</p>
</blockquote>
<p><strong>题目</strong></p>
<p>实现<code>includes</code>函数，判断当前数组是否包含传入的值。</p>
<pre><code class="hljs language-js copyable" lang="js">includes([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
includes([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-literal">NaN</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>], <span class="hljs-literal">NaN</span>, <span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体实现</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 整数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toInt</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">var</span> resNum = num % <span class="hljs-number">1</span>;
  <span class="hljs-keyword">if</span> (resNum) &#123;
    num = num - resNum;
    <span class="hljs-built_in">Math</span>.abs(resNum) > <span class="hljs-number">0.5</span> && (resNum > <span class="hljs-number">0</span> ? num ++ : num--);
  &#125;
  <span class="hljs-keyword">return</span> num;
&#125;

<span class="hljs-comment">// 数字类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toNumber</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> num !== <span class="hljs-string">'number'</span> || num !== num || (num === <span class="hljs-literal">Infinity</span> || num === -<span class="hljs-literal">Infinity</span>)) &#123;
    num = <span class="hljs-number">0</span>;
  &#125;

  num = toInt(num);
  <span class="hljs-keyword">return</span> num;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">includes</span>(<span class="hljs-params">array, value, fromIndex</span>) </span>&#123;
  <span class="hljs-keyword">var</span> length = isArray(array) ? array.length : <span class="hljs-number">0</span>;
  <span class="hljs-keyword">if</span> (!length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

  fromIndex = toNumber(fromIndex);
  fromIndex = fromIndex > -<span class="hljs-number">1</span> ? fromIndex : fromIndex + length;


  <span class="hljs-keyword">var</span> index = -<span class="hljs-number">1</span> + fromIndex;

  <span class="hljs-keyword">while</span>(++index < length) &#123;
    <span class="hljs-keyword">if</span> (array[index] === value || (array[index] !== array[index] && value !== value)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实现思路</strong></p>
<p><strong>参数：</strong></p>
<ol>
<li><code>array</code>（Array）：被查询的数组；</li>
<li><code>value</code>（*）： 需要查找的值；</li>
<li><code>fromIndex</code> （Number）：查询时候的起始位置 ;</li>
</ol>
<p><strong>步骤：</strong></p>
<ol>
<li>判断当前的<code>array</code>参数是否为数组，并且判断该数组的长度；</li>
<li><code>fromIndex</code>进行类型判断，判断是否为数字类型，不是则赋值为0。因为数字类型中可能存在带小数的数字，所以对小数取整处理，这里用到了取余的方式来处理；</li>
<li>这里使用<code>while</code>遍历，第一次遍历时<code>index</code>的值为0，最后<code>index</code>的值等于数组的长度值；</li>
<li>遍历数组进行成员和<code>value</code>值进行比较，这里有一个值比较特殊就是<code>NaN</code>， 因为<code>NaN </code>不等于自身，所以这里进行了特别的判断处理，即使是<code>NaN</code>存在并对比的时候能够返回正确的值；</li>
</ol>
<p>如果读者发现有不妥或者可以改善的地方，欢迎在评论区指出。如果觉得写得不错或者对你有所帮助，可以点赞、评论、转发分享，谢谢~</p></div>  
</div>
            