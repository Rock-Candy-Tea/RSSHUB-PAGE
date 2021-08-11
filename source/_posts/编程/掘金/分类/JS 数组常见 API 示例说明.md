
---
title: 'JS 数组常见 API 示例说明'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3296'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:11:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=3296'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">静态方法</h2>
<ol>
<li>
<h3 data-id="heading-1">Array.isArray(): 判断是否为数组</h3>
</li>
<li>
<h3 data-id="heading-2">Array.from(): 把伪数组转换为真数组</h3>
<p><code>注: 伪数组必须有length属性,否则无法转换为真数组,length为几,数组有几个值,如果length大于原数据个数,则多出部分为undefined</code></p>
<h2 data-id="heading-3">实例方法</h2>
</li>
</ol>
<h3 data-id="heading-4">1.concat: 链接数组成为新数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]; 
<span class="hljs-keyword">let</span> a2 = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>]; 
<span class="hljs-keyword">let</span> a3 = [<span class="hljs-number">11</span>, <span class="hljs-number">12</span>, <span class="hljs-number">13</span>]; 
<span class="hljs-keyword">let</span> arr = a1.concat( a2, a3, <span class="hljs-string">'red'</span>); 
<span class="hljs-comment">// 返回拼接后的新数组;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. indexOf: 查找(查找数组中的某个元素, 如果找到了就会返回索引值, 找不到就会返回-1, 且查找的是元素首次出现的位置)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span class="hljs-string">'a'</span>,<span class="hljs-string">'c'</span>]; 
arr.indexOf(<span class="hljs-string">'c'</span>); <span class="hljs-comment">// </span>
返回的索引值为 <span class="hljs-number">2</span> ;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3. lastIndexOf: 查找(查找数组中的某个元素最后一次出现的位置,如果找到了就会返回索引值,找不到就会返回-1)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span class="hljs-string">'a'</span>,<span class="hljs-string">'c'</span>]; 
arr.indexOf(<span class="hljs-string">'c'</span>); 
<span class="hljs-comment">// 返回的索引值为 5 ;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4. join: 用于连接数组的每个元素成为字符串</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span class="hljs-string">'e'</span>,<span class="hljs-string">'f'</span>];
arr.join(<span class="hljs-string">'-'</span>); 
<span class="hljs-number">1.</span>拼接后为 <span class="hljs-string">'a-b-c-d-e-f'</span> 的字符串; 
<span class="hljs-number">2.</span>如果想让数组的内容连起来,只需arr.join(<span class="hljs-string">''</span>);即可; 结果为 <span class="hljs-string">'abcdef'</span> 的字符串;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5. sort: 数组排序(编码排序,只识别首字母)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">23</span>, <span class="hljs-number">6</span>, <span class="hljs-number">13</span>, <span class="hljs-number">199</span>, <span class="hljs-number">28</span>, <span class="hljs-number">96</span>];
公式:
(从小到大排序)
arr.sort( <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a,b</span>)</span>&#123;<span class="hljs-keyword">return</span> a-b &#125;);
(从大到小排序)
arr.sort( <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a,b</span>)</span>&#123;<span class="hljs-keyword">return</span> b-a &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下方法共用一个示例数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span>]; <span class="hljs-comment">// 示例数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">6. find: 返回数组中满足条件的第一个元素</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> refind = arr.find(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-keyword">return</span> i > <span class="hljs-number">5</span>;
        <span class="hljs-comment">// 默认遍历数组,可以写条件,直接返回满足条件的结果;</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(refind);
<span class="hljs-comment">// 控制台结果为: 6;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">7. findIndex: 返回数组中第一个满足条件的元素的索引值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> refindIndex = arr.findIndex(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-keyword">return</span> i > <span class="hljs-number">5</span>;
        <span class="hljs-comment">// 默认遍历数组,可以写条件,直接返回满足条件元素的索引值;</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(refindIndex);
<span class="hljs-comment">// 控制台结果为: 5;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">8. some: 查找满足条件的元素,有一个满足即为ture(满足条件 return ture 立刻停止),否则为false</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> resome = arr.some(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-keyword">return</span> i > <span class="hljs-number">5</span>;
    <span class="hljs-comment">// 默认遍历数组,可以写条件,返回布尔值;</span>
    ** 或 **
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">9. every: 查找满足条件的元素,所有元素都满足返回ture,否则就是false</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> reevery = arr.every(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-keyword">return</span> i > <span class="hljs-number">5</span>;
    <span class="hljs-comment">// 默认遍历数组,可以写条件,返回布尔值;</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(reevery);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">10. filter: 遍历筛选元素, 把满足条件的元素筛选出来后放到新数组中返回</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> refilter = arr.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
       <span class="hljs-keyword">return</span> i > <span class="hljs-number">5</span>;
    <span class="hljs-comment">// 默认遍历数组,可以写条件,返回新数组;</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(refilter);
<span class="hljs-comment">// 控制台结果为:</span>
(<span class="hljs-number">5</span>) [<span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span>]
<span class="hljs-number">0</span>: <span class="hljs-number">6</span>
<span class="hljs-number">1</span>: <span class="hljs-number">7</span>
<span class="hljs-number">2</span>: <span class="hljs-number">8</span>
<span class="hljs-number">3</span>: <span class="hljs-number">9</span>
<span class="hljs-number">4</span>: <span class="hljs-number">10</span>
<span class="hljs-attr">length</span>: <span class="hljs-number">5</span>
<span class="hljs-attr">__proto__</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">0</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">11. map: 遍历元素, 把每项执行一遍回调函数,把结果都放到一个新数组中返回</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> remap = arr.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-keyword">return</span> i * i;
    <span class="hljs-comment">// 默认遍历数组,可以写条件,返回计算后的新数组;</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(remap);
<span class="hljs-comment">// 控制台结果为:</span>
(<span class="hljs-number">10</span>) [<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">9</span>, <span class="hljs-number">16</span>, <span class="hljs-number">25</span>, <span class="hljs-number">36</span>, <span class="hljs-number">49</span>, <span class="hljs-number">64</span>, <span class="hljs-number">81</span>, <span class="hljs-number">100</span>]
<span class="hljs-number">0</span>: <span class="hljs-number">1</span>
<span class="hljs-number">1</span>: <span class="hljs-number">4</span>
<span class="hljs-number">2</span>: <span class="hljs-number">9</span>
<span class="hljs-number">3</span>: <span class="hljs-number">16</span>
<span class="hljs-number">4</span>: <span class="hljs-number">25</span>
<span class="hljs-number">5</span>: <span class="hljs-number">36</span>
<span class="hljs-number">6</span>: <span class="hljs-number">49</span>
<span class="hljs-number">7</span>: <span class="hljs-number">64</span>
<span class="hljs-number">8</span>: <span class="hljs-number">81</span>
<span class="hljs-number">9</span>: <span class="hljs-number">100</span>
<span class="hljs-attr">length</span>: <span class="hljs-number">10</span>
<span class="hljs-attr">__proto__</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">0</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">12. reduce: 遍历元素, 可以得到所有元素累加的结果</h3>
<pre><code class="hljs language-js copyable" lang="js">语法: reduce ( <span class="hljs-function">(<span class="hljs-params"> 累加值, 当前项 </span>) =></span> &#123; 执行代码 &#125;, 初始值 )

    <span class="hljs-keyword">let</span> theSum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">sum, i</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> sum += i
    &#125;, <span class="hljs-number">0</span>)

<span class="hljs-built_in">console</span>.log(theSum)
<span class="hljs-comment">// 控制台输出结果为: 55</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">13. includes: 用来判断一个数组是否包含一个指定的值，如果包含返回 true，否则返回false</h3>
<pre><code class="hljs language-js copyable" lang="js">        arr.includes(<span class="hljs-number">2</span>)  <span class="hljs-comment">// 返回 true</span>
arr.includes(<span class="hljs-number">11</span>)  <span class="hljs-comment">// 返回 false</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            