
---
title: '🚀详解JavaScript系列之数组(五)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d40d6f78b834a96ad7b28b8c61e3379~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:56:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d40d6f78b834a96ad7b28b8c61e3379~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d40d6f78b834a96ad7b28b8c61e3379~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<hr>
<h4 data-id="heading-0">前言</h4>
<blockquote>
<p>接上一篇文章，我们来详细解读js数组的内容，本篇幅讲述“reverse和sort两个api”，上一篇传送门</p>
</blockquote>
<hr>
<h4 data-id="heading-1"></h4>
<h4 data-id="heading-2">reverse()</h4>
<p>作用：如其名，就是反转数组，返回结果为<strong>反转后的数组</strong>（是在原数组的基础上反转）。</p>
<blockquote>
<p>语法：反转后的数组 = 数组.reverse();</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'d'</span>, <span class="hljs-string">'e'</span>, <span class="hljs-string">'f'</span>];
<span class="hljs-keyword">var</span> result = arr.reverse(); 
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
​
<span class="hljs-comment">//结果</span>
arr =[<span class="hljs-string">"f"</span>,<span class="hljs-string">"e"</span>,<span class="hljs-string">"d"</span>,<span class="hljs-string">"c"</span>,<span class="hljs-string">"b"</span>,<span class="hljs-string">"a"</span>]
result =[<span class="hljs-string">"f"</span>,<span class="hljs-string">"e"</span>,<span class="hljs-string">"d"</span>,<span class="hljs-string">"c"</span>,<span class="hljs-string">"b"</span>,<span class="hljs-string">"a"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-3">sort()方法</h4>
<blockquote>
<p>sort我们可能都不陌生，和很多语言里面一样，就是排序的一个api，大家大同小异，只是有些地方不一样，我来讲讲。</p>
</blockquote>
<p><code>sort()</code>：对数组的元素进行从小到大来排序（原数组基础上，默认升序）。</p>
<h5 data-id="heading-4">无参时(按字典序)</h5>
<p>如果在使用 sort() 方法时不带参，则默认按照<code>Unicode 编码</code>，升序排序。</p>
<h6 data-id="heading-5">字符串sort</h6>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-string">'e'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'d'</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'f'</span>, <span class="hljs-string">'c'</span>];
​
<span class="hljs-keyword">let</span> result = arr1.sort(); <span class="hljs-comment">// 将数组 arr1 进行排序</span>
​
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr1 ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr1));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
​
<span class="hljs-comment">//结果</span>
arr1 =[<span class="hljs-string">"a"</span>,<span class="hljs-string">"b"</span>,<span class="hljs-string">"c"</span>,<span class="hljs-string">"d"</span>,<span class="hljs-string">"e"</span>,<span class="hljs-string">"f"</span>]
result =[<span class="hljs-string">"a"</span>,<span class="hljs-string">"b"</span>,<span class="hljs-string">"c"</span>,<span class="hljs-string">"d"</span>,<span class="hljs-string">"e"</span>,<span class="hljs-string">"f"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">数字sort</h6>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr2 = [<span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">11</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>];
<span class="hljs-keyword">let</span> result = arr2.sort(); <span class="hljs-comment">// 将数组 arr2 进行排序</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr2 ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr2));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
​
<span class="hljs-comment">//结果</span>
arr2 =[<span class="hljs-number">1</span>,<span class="hljs-number">11</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
result =[<span class="hljs-number">1</span>,<span class="hljs-number">11</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>分析</code>：上面结果中，你会发现，数字并没有按大小顺序来，这是为什么了，是我sort不行么？不，当然不是。回到上面的定义，js的sort是按照Unicode编码，默认按照字典序来排列。那怎么样才能按数字大小排序呢？怎么操作呢？继续往下看。</p>
<hr>
<h5 data-id="heading-7">带参时，自定义排序规则</h5>
<p>如果在 sort()方法中带参，那么参数是什么呢？作用是啥？</p>
<p>我们在 sort()传入一个<code>回调函数</code>当做参数，来指定排序规则（就像写C/C++时，经常写的cmp函数来指定排序规则）。回调函数中需要<code>定义两个形参</code>，浏览器将会分别使用数组中的元素作为实参去调用回调函数。那么如何来决定优先顺序呢？别着急，我们慢慢来说。</p>
<p>我们根据回调函数的返回值来决定元素的排序：</p>
<ul>
<li>如果返回一个大于 0 的值，则元素会交换位置</li>
<li><strong>如果返回一个小于 0 的值，则元素位置不变</strong></li>
<li>如果返回一个等于 0 的值，则认为两个元素相等，则不交换位置</li>
</ul>
<p>如果只是看上面的文字，可能不太好理解，我们来看看下面的例子，你肯定就能明白。</p>
<h6 data-id="heading-8">数字升序</h6>
<p><strong>粗糙版本</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">11</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>];
<span class="hljs-comment">// 自定义排序规则</span>
<span class="hljs-keyword">var</span> result = arr.sort(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (a > b) &#123;
        <span class="hljs-comment">// 如果 a 大于 b，则交换 a 和 b 的位置</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (a < b) &#123;
        <span class="hljs-comment">// 如果 a 小于 b，则位置不变</span>
        <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果 a 等于 b，则位置不变</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
<span class="hljs-comment">//结果</span>
arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">11</span>];
result = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">11</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是我们发现上方代码的写法太啰嗦了，其实也可以简化为如下写法：</p>
<p><strong>简化版</strong>：（冒泡排序）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">11</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>];
<span class="hljs-comment">// 自定义排序规则</span>
<span class="hljs-keyword">let</span> result = arr.sort(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a - b; <span class="hljs-comment">// 升序排列</span>
    <span class="hljs-comment">// return b - a; // 降序排列</span>
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上方代码还可以写成 ES6 的形式，也就是将 function 改为箭头函数，其写法如下。</p>
<p><strong>ES6版</strong>：（箭头函数）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">11</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>];
<span class="hljs-comment">// 自定义排序规则</span>
<span class="hljs-keyword">let</span> result = arr.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> a - b; <span class="hljs-comment">// 升序排列</span>
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr ='</span> + <span class="hljs-built_in">JSON</span>.stringify(arr));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result ='</span> + <span class="hljs-built_in">JSON</span>.stringify(result));
​
<span class="hljs-comment">//优化</span>
<span class="hljs-keyword">let</span> result = arr.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6优化版的箭头函数 是我们在实战开发中用得最多的。</p>
<p>为了确保代码的<code>简洁优雅</code>，接下来的代码中，凡是涉及到函数，我们将尽量采用 ES6 中的<code>箭头函数</code>来写。</p></div>  
</div>
            