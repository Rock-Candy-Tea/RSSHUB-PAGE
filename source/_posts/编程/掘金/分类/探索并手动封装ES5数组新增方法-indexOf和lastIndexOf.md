
---
title: '探索并手动封装ES5数组新增方法-indexOf和lastIndexOf'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3416'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 19:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3416'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a></p>
<h1 data-id="heading-0">前言</h1>
<p>之前我封装过ES3数组的核心方法，但后来有新的版本ES5、ES6。一个版本的跟新迭代必然会摈弃一些旧的东西，同时新增一些实用的东西。这次我们一起来看ES5中数组的新增方法并实现封装</p>
<h1 data-id="heading-1">新增方法</h1>
<p>首先，我们将这些方法归类：</p>
<ul>
<li><code>2个索引方法：indexOf() 和 lastIndexOf()</code></li>
<li><code>5个迭代方法：forEach()、map()、filter()、some()、every()</code></li>
<li><code>2个归并方法：reduce()、reduceRight()</code></li>
</ul>
<p>这里我们先来看前面两个方法的模拟实现</p>
<blockquote>
<p>indexOf()和lastIndexOf()</p>
</blockquote>
<p>这两个方法都是用于返回元素在数组中第一次被查找到的索引位置，如果没有找到，那么返回-1。<code> </code>都接收两个参数：</p>
<ol>
<li>第一个参数是要查找的东西</li>
<li>第二个参数是查找起点位置的索引，如果缺省或是格式不正确，那么默认为0。第二个参数可选</li>
</ol>
<p>区别就是一个从前往后找，一个从后往前找</p>
<h1 data-id="heading-2">基本使用</h1>
<p>一起来看例子，先定义一个数组：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>indexOf()：从数组的开头开始向后查找。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>));<span class="hljs-comment">//2   只传一个值，默认从第0项开始查找  知道返回索引</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">10</span>));<span class="hljs-comment">//-1 没找到返回-1</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf());<span class="hljs-comment">//-1   什么都不传，返回-1</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>,<span class="hljs-string">'a'</span>));<span class="hljs-comment">//2   传两个值，第二个格式不正确，默认从第0项开始查找</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>,<span class="hljs-number">2</span>));<span class="hljs-comment">//2   从第2项开始查找，返回找到位置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lastIndexOf()： 从数组的末尾开始向前查找。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">3</span>));<span class="hljs-comment">//2    值传一个值，表示从倒数第一位开始查找，找到返回索引</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">7</span>));<span class="hljs-comment">//-1  没找到返回-1</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf());<span class="hljs-comment">//-1   什么都不传，返回-1</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">3</span>,<span class="hljs-string">'a'</span>));<span class="hljs-comment">//-1   </span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">1</span>,<span class="hljs-string">'a'</span>));<span class="hljs-comment">//0   传两个值，第二个格式不正确，默认从倒数最后一位开始查找，即只是找一位</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">3</span>,<span class="hljs-number">2</span>));<span class="hljs-comment">//2   第二位是正常数值，从该位置开始向前查找，没有找到返回-1  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>观察发现除了一个从前往后找，一个从后往前找的区别外，我们还发现一个小区别，就是当第二个参数错误时，都是默认从0位开始查找，导致indexOf()查找整个数组，lastIndexOf只查找第0位。</p>
<p>查找对比时，会使用全等操作符"==="， 要求必须完全相等,否则返回-1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-string">'1'</span>))<span class="hljs-comment">//-1   这里"1"和1是不相等</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外第二个参数也不存在隐式类型转换</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">3</span>,<span class="hljs-string">'1'</span>));<span class="hljs-comment">//-1 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">模拟封装_indexOf</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype._indexOf = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val, start</span>) </span>&#123;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> _searchFromZero();
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length >= <span class="hljs-number">2</span>) &#123;
    <span class="hljs-comment">// 这里得处理第二个参数：接受负值的情况 和 接受错误值的情况(判断是不是数字)</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> start !== <span class="hljs-string">"number"</span> || <span class="hljs-built_in">isNaN</span>(start)) &#123;
      <span class="hljs-keyword">return</span> _searchFromZero();
    &#125;
    <span class="hljs-comment">//否则就是数字，数字分正数和负数，负数可以通过运算转成正数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> start === <span class="hljs-string">"number"</span> && !<span class="hljs-built_in">isNaN</span>(start)) &#123;
      start = start >= <span class="hljs-number">0</span> ? start : start + <span class="hljs-built_in">this</span>.length;
      <span class="hljs-keyword">var</span> temp = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = start; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
        temp++;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>[i] === val) &#123;
          <span class="hljs-keyword">return</span> start + temp - <span class="hljs-number">1</span>;<span class="hljs-comment">//变成下标</span>
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_searchFromZero</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < self.length; i++) &#123;
      <span class="hljs-keyword">if</span> (self[i] === val) &#123;
        <span class="hljs-keyword">return</span> i;
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// test code</span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>));<span class="hljs-comment">//2   只传一个值，默认从第0项开始查找</span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">7</span>));<span class="hljs-comment">//-1 没找到返回-1</span>
<span class="hljs-built_in">console</span>.log(arr._indexOf());<span class="hljs-comment">//-1   什么都不传，返回-1</span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>, <span class="hljs-string">'a'</span>));<span class="hljs-comment">//2   第二个格式不正确，从第0项开始查找</span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>, <span class="hljs-number">0</span>));<span class="hljs-comment">//2   </span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>, -<span class="hljs-number">4</span>));<span class="hljs-comment">//2   </span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>, -<span class="hljs-number">5</span>));<span class="hljs-comment">//2   </span>
<span class="hljs-built_in">console</span>.log(arr._indexOf(<span class="hljs-number">3</span>, <span class="hljs-number">100</span>));<span class="hljs-comment">//-1  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟实现了indexOf的基本使用！</p>
<h1 data-id="heading-4">模拟封装_lastIndexOf</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype._lastIndexOf = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val, start</span>) </span>&#123;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> _searchFromEnd();
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_searchFromEnd</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = self.length - <span class="hljs-number">1</span>; i > <span class="hljs-number">0</span>; i--) &#123;
      <span class="hljs-keyword">if</span> (self[i] === val) &#123;
        <span class="hljs-keyword">return</span> i;
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length >= <span class="hljs-number">2</span>) &#123;
    <span class="hljs-comment">//  传两个值，第二个格式不正确，默认从倒数最后一位即第0位开始查找，只是找一位.第1位是就返回0，不是返回-1</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> start !== <span class="hljs-string">"number"</span> || <span class="hljs-built_in">isNaN</span>(start)) &#123;
      <span class="hljs-keyword">return</span> self[<span class="hljs-number">0</span>] === val ? <span class="hljs-number">0</span> : -<span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-comment">// 否则就是数字，这里应该也有正负，所以也得转，正数是第几位。</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> start === <span class="hljs-string">"number"</span> && !<span class="hljs-built_in">isNaN</span>(start)) &#123;
      <span class="hljs-comment">// 到时第start位，正数是第几位呢</span>
      start = -start + self.length;
      <span class="hljs-comment">// 正后也有可能是负数或者正数，统一转为正。</span>
      start = start >= <span class="hljs-number">0</span> ? start : start + self.length;
      <span class="hljs-comment">// console.log(start)</span>
          <span class="hljs-comment">// var temp = 0;</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = start; i > <span class="hljs-number">0</span>; i--) &#123;
            <span class="hljs-comment">// temp++;</span>
            <span class="hljs-keyword">if</span> (self[i] === val) &#123;
              <span class="hljs-keyword">return</span> i;<span class="hljs-comment">//变成下标</span>
            &#125;
          &#125;
          <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(arr._lastIndexOf());<span class="hljs-comment">//-1   什么都不传，返回-1</span>
<span class="hljs-built_in">console</span>.log(arr._lastIndexOf(<span class="hljs-number">3</span>));<span class="hljs-comment">//2    值传一个值，表示从倒数第1位开始查找</span>
<span class="hljs-built_in">console</span>.log(arr._lastIndexOf(<span class="hljs-number">3</span>, <span class="hljs-string">'a'</span>));<span class="hljs-comment">//-1   </span>
 <span class="hljs-built_in">console</span>.log(arr._lastIndexOf(<span class="hljs-number">1</span>,<span class="hljs-string">'a'</span>));<span class="hljs-comment">//0   第二个格式不正确，默认从倒数最后一位开始查找，即只是对比数组第0位置。</span>
<span class="hljs-built_in">console</span>.log(arr._lastIndexOf(<span class="hljs-number">3</span>, <span class="hljs-number">2</span>));<span class="hljs-comment">//2   第二位是正常数值，从该位置开始向前查找</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟实现了lastIndexOf的基本使用！</p>
<h1 data-id="heading-5">END</h1>
<p>以上就是本文的所有内容</p>
<p>如有问题欢迎留言评论~</p></div>  
</div>
            