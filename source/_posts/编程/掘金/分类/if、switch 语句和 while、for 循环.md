
---
title: 'if、switch 语句和 while、for 循环'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8591'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 19:29:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=8591'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0"><code>if</code></h2>
<p>条件判断语句：可以在执行某个语句之前进行判断，如果条件成立才会执行语句，条件不成立则语句不执行</p>
<h3 data-id="heading-1">栗子🌰</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> score = prompt(<span class="hljs-string">"请输入你的期末成绩（0-100）"</span>)
<span class="hljs-keyword">if</span>(score > <span class="hljs-number">100</span> || score < <span class="hljs-number">0</span> || <span class="hljs-built_in">isNaN</span>(score))&#123;
  alert(<span class="hljs-string">"输入不合法"</span>);
&#125;<span class="hljs-keyword">else</span>&#123;
  <span class="hljs-keyword">if</span>(score == <span class="hljs-number">100</span>)&#123;
    alert(<span class="hljs-string">"迪士尼三日游"</span>);
  &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(score >= <span class="hljs-number">80</span>)&#123;
    alert(<span class="hljs-string">"手办一个"</span>);
  &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(score >= <span class="hljs-number">60</span>)&#123;
    alert(<span class="hljs-string">"测试卷"</span>);
  &#125;<span class="hljs-keyword">else</span>&#123;
    alert(<span class="hljs-string">"棍子一根"</span>);
  &#125;
&#125;
<span class="hljs-comment">//只要有一个语句执行，那就不会再往下执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2"><code>switch</code></h2>
<p>也叫条件分支语句</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">switch</span>(<span class="hljs-literal">true</span>)&#123;
  <span class="hljs-keyword">case</span> score >= <span class="hljs-number">60</span>:
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"合格"</span>);
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">default</span>:
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"不合格"</span>);
    <span class="hljs-keyword">break</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在执行时会一次将<code>case</code>后的表达式的值和<code>switch</code>后的条件表达式的值进行全等比较。</li>
<li>如果比较的值为 true，则执行后续代码，可以使用<code>break</code>用来退出<code>switch</code>语句</li>
<li>如果所有比较的结果都为 false，则只执行<code>default</code></li>
</ul>
<h2 data-id="heading-3"><code>while</code>循环</h2>
<p>先判断再执行</p>
<ul>
<li>先对表达式进行求值判断</li>
<li>如果值为 true，则执行循环体</li>
<li>循环体执行完毕后，继续对表达式进行判断</li>
<li>如果值为 true，则继续进行循环体</li>
<li>直到值为 false，终止循环</li>
</ul>
<h3 data-id="heading-4">栗子🌰</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-keyword">var</span> score = prompt(<span class="hljs-string">"请输入你的期末成绩（0-100）"</span>);
  <span class="hljs-keyword">if</span> (score >= <span class="hljs-number">0</span> && score <= <span class="hljs-number">100</span>) &#123;
    <span class="hljs-keyword">break</span>;
  &#125;
  alert(<span class="hljs-string">"请输入有效的分数！！！"</span>);
&#125;
<span class="hljs-keyword">if</span> (score == <span class="hljs-number">100</span>) &#123;
  alert(<span class="hljs-string">"迪士尼三日游"</span>);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (score >= <span class="hljs-number">80</span>) &#123;
  alert(<span class="hljs-string">"手办一个"</span>);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (score >= <span class="hljs-number">60</span>) &#123;
  alert(<span class="hljs-string">"测试卷"</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  alert(<span class="hljs-string">"棍子一根"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"><code>for</code></h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
<span class="hljs-keyword">for</span>(初始化表达式; 条件表达式; 更新表达式)&#123;
  语句···
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++)&#123;
  alert(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>执行初始化表达式，初始化变量</li>
<li>执行条件表达式，判断是否执行循环</li>
<li>执行更新表达式，更新表达式执行完毕继续执行条件表达式</li>
</ol>
<h3 data-id="heading-6">栗子🌰</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = prompt(<span class="hljs-string">"请输入一个大于 1 的整数："</span>);
<span class="hljs-keyword">if</span> (num <= <span class="hljs-number">1</span>) &#123;
  alert(<span class="hljs-string">"该值不合法"</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">var</span> flag = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">2</span>; i < num; i++) &#123;
    <span class="hljs-keyword">if</span> (num % i == <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">//如果 num 能对 i 进行整除，那么 num 的值就不是质数，比如（num=11，那么i 就是 2~10 直接的数字，11 无法整除，就说明 11 是质数。）</span>
      flag = <span class="hljs-literal">false</span>;
    &#125;
  &#125;<span class="hljs-comment">//for循环把所有num 能整除i 的数字都取出来</span>
  <span class="hljs-keyword">if</span> (flag) &#123;
    alert(num + <span class="hljs-string">"是质数！！！"</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    alert(num + <span class="hljs-string">"不是质数"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">嵌套<code>for</code>循环</h3>
<p>内部<code>for</code>循环执行完再执行外的<code>for</code>循环</p>
<h4 data-id="heading-8"></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//场景：打印2~100 之间的质数</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">2</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
  <span class="hljs-keyword">var</span> flag = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">2</span>; j < i; j++) &#123;
    <span class="hljs-keyword">if</span> (i % j == <span class="hljs-number">0</span>) &#123;
      flag = <span class="hljs-literal">false</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (flag) &#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            