
---
title: 'js数组的reduce方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4173'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 01:49:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=4173'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">js数组的reduce方法</h1>
<pre><code class="hljs language-js copyable" lang="js">arr. reduce( <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prev, cur, index,arr</span>)</span>&#123;
&#125;, init);
<span class="hljs-comment">//或者</span>
arr. reduce( <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prev, cur , index,arr</span>)</span>&#123;
&#125;,);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>arr</strong>表示将要的原数组（你要操作的原数组）;</p>
<p><strong>prev</strong>表示上一次调用回调时的返回值，或者初始值init;</p>
<p><strong>cur</strong>表示当前正在处理的数组元素;</p>
<p><strong>index</strong>表示当前正在处理的数组元素的索引，若提供init 值，则索引为0， 否则索引为1;</p>
<p><strong>init</strong> 表示初始值。
<strong>常用的参数只有两个: prev和cur</strong></p>
<h2 data-id="heading-1">作用</h2>
<p>1：数组求和，求乘积。
求积自己推</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
        <span class="hljs-keyword">var</span> sum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> pre + cur
        &#125;)
        <span class="hljs-built_in">console</span>.log(sum);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2:计算数组中每个元素出现的次数</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> sb=[<span class="hljs-string">'sb'</span>,<span class="hljs-string">'sb'</span>,<span class="hljs-string">'dsb'</span>,<span class="hljs-string">'sb'</span>]
        <span class="hljs-keyword">let</span> nameNum=sb.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>)=></span>&#123;
            <span class="hljs-keyword">if</span>(cur <span class="hljs-keyword">in</span> pre)&#123;
                pre[cur]++
            &#125;<span class="hljs-keyword">else</span>&#123;
                pre[cur]=<span class="hljs-number">1</span>
            &#125;
            <span class="hljs-keyword">return</span> pre
        &#125;,&#123;&#125;)
        <span class="hljs-built_in">console</span>.log(nameNum);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3:数组去重</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> sb = [<span class="hljs-string">'sb'</span>, <span class="hljs-string">'sb'</span>, <span class="hljs-string">'dsb'</span>, <span class="hljs-string">'sb'</span>]
        <span class="hljs-keyword">let</span> resNum = sb.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (!pre.includes(cur)) &#123;
                <span class="hljs-keyword">return</span> pre.concat(cur)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span> pre
            &#125;

        &#125;, [])
        <span class="hljs-built_in">console</span>.log(resNum);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4:将二维数组转化成一维数组</p>
<p>5:将多维数组转化成一维数组</p>
<p>ps:4和5几乎一毛一样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, [<span class="hljs-number">9</span>, <span class="hljs-number">8</span>, <span class="hljs-number">7</span>[<span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]]]
<span class="hljs-keyword">const</span> flatten = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
    <span class="hljs-keyword">return</span> arr.reduce(
        <span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> pre.concat(<span class="hljs-built_in">Array</span>.isArray(cur) ? flatten(cur) : cur);
        &#125;, [])
&#125;
<span class="hljs-keyword">const</span> res4 = flatten(arr)

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            