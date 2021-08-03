
---
title: 'JavaScript 设计模式之策略模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228287d5b6ee48918a65f3b147e055f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 02:01:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228287d5b6ee48918a65f3b147e055f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第2天，活动详情查看：[8月更文挑战]</p>
<blockquote>
<p>定义：定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换。</p>
</blockquote>
<h2 data-id="heading-0">使用策略模式计算奖金</h2>
<p>以计算年终奖为例，例如：绩效为S的人年终奖4倍工资，绩效为A的人年终奖3倍工资，绩效为B的人年终奖2倍，写一段代码来实现计算员工的年终奖。</p>
<h3 data-id="heading-1">1 最初的代码实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">performanceLevel, salary</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'S'</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'A'</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'B'</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
  &#125;
&#125;
calculateBonus(<span class="hljs-string">'B'</span>, <span class="hljs-number">20000</span>) <span class="hljs-comment">// 输出:40000 </span>
calculateBonus( <span class="hljs-string">'S'</span>, <span class="hljs-number">6000</span> ); <span class="hljs-comment">// 输出:24000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，这段代码非常简单，但是存在很多显而易见的缺点。</p>
<ul>
<li><code>calculateBonus</code> 包含很多 <code>if-else</code> 语句，需要覆盖所有的逻辑分支。</li>
<li><code>calculateBonus</code> 缺乏弹性，如果增加了绩效C，或者调整了奖金系数，都必须重新深入 <code>calculateBonus</code> 函数的内部去修改，这是违反开放-封闭原则。</li>
<li>算法的复用性查，如果其他地方需要用，只有复制粘贴。</li>
</ul>
<h3 data-id="heading-2">2 使用组合函数重构代码</h3>
<p>将各种算法封装到一个个小函数里面，这些小函数有良好的命名，可以一目了然的知道对应哪种算法，它们也可以被复用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> performanceS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
&#125;
<span class="hljs-keyword">var</span> performanceA = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
&#125;
<span class="hljs-keyword">var</span> performanceB = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
&#125;
<span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">performanceLevel, salary</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'S'</span>) &#123;
    <span class="hljs-keyword">return</span> performanceS(salary)
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'A'</span>) &#123;
    <span class="hljs-keyword">return</span> performanceA(salary)
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">'B'</span>) &#123;
    <span class="hljs-keyword">return</span> performanceB(salary)
  &#125;
&#125;
calculateBonus(<span class="hljs-string">'A'</span>, <span class="hljs-number">10000</span>) <span class="hljs-comment">// 输出:30000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3 使用策略模式重构代码</h3>
<p>策略模式指定义一系列算法，把它们一个个封装起来。将不变的部分和变化的部分隔开是每个设计模式的主题，策略模式的目的就是将算法的使用与算法的实现分离开来。</p>
<p>一个基于策略模式的程序至少由两部分组成。第一个部分是一组策略类，策略类封装了具体的算法，并负责具体的计算过程。第二部分是环境类 <code>Context</code>，<code>Context</code> 接受客户的请求，随后把请求委托给某一个策略类。</p>
<p>第一个版本模仿传统面向对象语言中的实现，先把每种绩效的计算规则都封装在对应的策略类里面：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> performanceS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
performanceS.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
&#125;
<span class="hljs-keyword">var</span> performanceA = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
performanceA.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
&#125;
<span class="hljs-keyword">var</span> performanceB = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
performanceB.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来定义奖金类 <code>Bonus</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Bonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.salary = <span class="hljs-literal">null</span> <span class="hljs-comment">// 原始工资</span>
  <span class="hljs-built_in">this</span>.strategy = <span class="hljs-literal">null</span> <span class="hljs-comment">// 绩效等级对应的策略对象</span>
&#125;
Bonus.prototype.setSalary = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.salary = salary <span class="hljs-comment">// 设置员工原始工资</span>
&#125;
Bonus.prototype.setStrategy = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">strategy</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.strategy = strategy <span class="hljs-comment">// 设置员工绩效工资</span>
&#125;
Bonus.prototype.getBouns = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.strategy.calculate(<span class="hljs-built_in">this</span>.salary) <span class="hljs-comment">// 计算奖金的操作委托给对应的策略对象</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>策略模式的思想：<strong>定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换。在 <code>JavaScript</code> 中表现为他们具有相同的目标和意图</strong></p>
<p>接下来，来完成剩下的代码。先创建一个 <code>bonus</code> 对象，并且给 <code>bonus</code> 对象设置一些原始的数据。将计算奖金的策略对象也传入 <code>bonus</code> 对象内部保存。当调用 <code>bonus.getBonus()</code> 来计算奖金时，<code>bonus</code> 对象本身没有能力计算，而是把请求委托给了之前保存好的策略对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> bonus = <span class="hljs-keyword">new</span> Bonus()

bonus.setSalary(<span class="hljs-number">10000</span>)
bonus.setStrategy(<span class="hljs-keyword">new</span> performanceS()) <span class="hljs-comment">// 设置策略对象</span>
<span class="hljs-built_in">console</span>.log(bonus.getBonus()) <span class="hljs-comment">// 输出:40000</span>

bonus.setStrategy(<span class="hljs-keyword">new</span> performanceA()) <span class="hljs-comment">// 设置策略对象</span>
<span class="hljs-built_in">console</span>.log(bonus.getBonus()) <span class="hljs-comment">// 输出:30000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">JavaScript 版本的策略模式</h2>
<p>在 <code>JavaScript</code> 中，函数也是对象，因此更简单和直接的做法是把 <code>strategy</code> 直接定义为函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> strategies = &#123;
  <span class="hljs-attr">S</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
  &#125;,
  <span class="hljs-attr">A</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
  &#125;,
  <span class="hljs-attr">B</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，<code>Context</code> 也没必要必须用 <code>Bonus</code> 类来表示，定义 <code>calculateBonus</code> 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">level, salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> strategies[level](salary)
&#125;
<span class="hljs-built_in">console</span>.log(calculateBonus(<span class="hljs-string">'S'</span>, <span class="hljs-number">20000</span>)) <span class="hljs-comment">// 输出:80000</span>
<span class="hljs-built_in">console</span>.log(calculateBonus(<span class="hljs-string">'A'</span>, <span class="hljs-number">10000</span>)) <span class="hljs-comment">// 输出:30000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">使用策略模式实现缓动动画</h2>
<p>我们的目的的实现一个小球按照不同的算法进行运动。</p>
<h3 data-id="heading-6">实现动画效果的原理</h3>
<p>使用 <code>JavaScript</code> 实现动画效果的原理跟动画片的制作一样，动画片是把一些差距不大的原画以较快的帧数播放，来达到视觉上的动画效果。在 <code>JavaScript</code> 中，可以通过连续改编元素的某个 <code>css</code> 属性，比如 <code>left</code>、<code>top</code>、<code>background-position</code> 来实现动画效果</p>
<h3 data-id="heading-7">思路和一些准备工作</h3>
<p>在运动开始前，需要记录一些信息，至少包括：</p>
<ul>
<li>动画开始时，小球所在的原始位置</li>
<li>小球移动的目标位置</li>
<li>动画开始时的准确时间点</li>
<li>小球运动持续的时间</li>
</ul>
<p>随后，使用 <code>setInterval</code> 创建一个定时器，每隔19ms循环一次，在定时器的每一帧里，将动画已消耗的时间、小球原始位置、小球目标位置以及动画持续总时间传入缓动算法，计算出小球当前应该所在的位置，然后更新 <code>div</code> 对应的 <code>css</code> 属性。如此小球便可顺利的运动起来。</p>
<h3 data-id="heading-8">让小球运动起来</h3>
<p>缓动算法接受 4 个参数，这 4 个参数的含义分别是动画已消耗的时间、小球原始位置、小球目标位置、动画持续的总时间，返回的值则是动画元素应该处在的当前位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> tween = &#123;
  <span class="hljs-attr">linear</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> (c * t) / d + b;
  &#125;,
  <span class="hljs-attr">easeIn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> c * (t /= d) * t + b;
  &#125;,
  <span class="hljs-attr">strongEaseIn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> c * (t /= d) * t * t * t * t + b;
  &#125;,
  <span class="hljs-attr">strongEaseOut</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> c * ((t = t / d - <span class="hljs-number">1</span>) * t * t * t * t + <span class="hljs-number">1</span>) + b;
  &#125;,
  <span class="hljs-attr">sineaseIn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> c * (t /= d) * t * t + b;
  &#125;,
  <span class="hljs-attr">sineaseOut</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">t, b, c, d</span>) </span>&#123;
    <span class="hljs-keyword">return</span> c * ((t = t / d - <span class="hljs-number">1</span>) * t * t + <span class="hljs-number">1</span>) + b;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面的代码思想来自 <code>jQuery</code> 库，先在页面放置一个 <code>div</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; background: blue"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div"</span>></span>我是 div<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来定义 <code>Animate</code> 类，<code>Animate</code> 的构造函数接受一个参数：即将运动起来的 <code>dom</code> 节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Animate = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">dom</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.dom = dom; <span class="hljs-comment">// 进行运动的 dom 节点</span>
  <span class="hljs-built_in">this</span>.startTime = <span class="hljs-number">0</span>; <span class="hljs-comment">// 动画开始时间</span>
  <span class="hljs-built_in">this</span>.startPos = <span class="hljs-number">0</span>; <span class="hljs-comment">// 动画开始时，dom 节点的位置，即 dom 的初始位置</span>
  <span class="hljs-built_in">this</span>.endPos = <span class="hljs-number">0</span>; <span class="hljs-comment">// 动画结束时，dom 节点的位置，即 dom 的目标位置</span>
  <span class="hljs-built_in">this</span>.propertyName = <span class="hljs-literal">null</span>; <span class="hljs-comment">// dom 节点需要被改变的 css 属性名</span>
  <span class="hljs-built_in">this</span>.easing = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 缓动算法</span>
  <span class="hljs-built_in">this</span>.duration = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 动画持续时间</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来 <code>Animate.prototype.start</code> 启动这个动画，需要记录一些信息供以后计算小球位置时使用，此方法还负责启动定时器。</p>
<pre><code class="hljs language-js copyable" lang="js">Animate.prototype.start = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
  propertyName,
  endPos,
  duration,
  easing
</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.startTime = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(); <span class="hljs-comment">// 动画启动时间</span>
  <span class="hljs-built_in">this</span>.startPos = <span class="hljs-built_in">this</span>.dom.getBoundingClientRect()[propertyName]; <span class="hljs-comment">// dom 节点初始位置</span>
  <span class="hljs-built_in">this</span>.propertyName = propertyName; <span class="hljs-comment">// dom节点需要被改编的 css 属性名</span>
  <span class="hljs-built_in">this</span>.endPos = endPos; <span class="hljs-comment">// dom 节点目标位置</span>
  <span class="hljs-built_in">this</span>.duration = duration; <span class="hljs-comment">// 动画持续时间</span>
  <span class="hljs-built_in">this</span>.easing = tween[easing]; <span class="hljs-comment">// 缓动算法</span>

  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">var</span> timeId = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 启动定时器，开始执行动画</span>
    <span class="hljs-keyword">if</span> (self.step() === <span class="hljs-literal">false</span>) &#123;
      <span class="hljs-comment">// 如果动画已结束，则清除定时器</span>
      <span class="hljs-built_in">clearInterval</span>(timeId);
    &#125;
  &#125;, <span class="hljs-number">19</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Animate.prototype.start</code> 方法接受一下四个参数：</p>
<ul>
<li><code>propertyName</code>： 要改变的 <code>css</code> 属性名，比如 <code>left</code>、<code>top</code>，分别表示左右移动和上下移动。</li>
<li><code>endPos</code>：小球运动的目标位置。</li>
<li><code>duration</code>：动画持续时间。</li>
<li><code>easing</code>：缓动算法。</li>
</ul>
<p><code>Animate.prototype.step</code> 代表小球运动的每一帧要做的事情。</p>
<pre><code class="hljs language-js copyable" lang="js">Animate.prototype.step = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> t = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(); <span class="hljs-comment">// 取得当前时间</span>
  <span class="hljs-keyword">if</span> (t >= <span class="hljs-built_in">this</span>.startTime + <span class="hljs-built_in">this</span>.duration) &#123;
    <span class="hljs-comment">// 动画结束时修正小球的位置</span>
    <span class="hljs-built_in">this</span>.update(<span class="hljs-built_in">this</span>.endPos); <span class="hljs-comment">// 更新小球的 CSS 属性值</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-keyword">var</span> pos = <span class="hljs-built_in">this</span>.easing(
    t - <span class="hljs-built_in">this</span>.startTime,
    <span class="hljs-built_in">this</span>.startPos,
    <span class="hljs-built_in">this</span>.endPos - <span class="hljs-built_in">this</span>.startPos,
    <span class="hljs-built_in">this</span>.duration
  );
  <span class="hljs-comment">// pos 为小球当前位置</span>
  <span class="hljs-built_in">this</span>.update(pos); <span class="hljs-comment">// 更新小球的 CSS 属性值</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Animate.prototype.update</code> 更新小球 <code>css</code> 属性值：</p>
<pre><code class="hljs language-js copyable" lang="js">Animate.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">pos</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.dom.style[<span class="hljs-built_in">this</span>.propertyName] = pos + <span class="hljs-string">"px"</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"div"</span>);
<span class="hljs-keyword">var</span> animate = <span class="hljs-keyword">new</span> Animate(div);
animate.start(<span class="hljs-string">"left"</span>, <span class="hljs-number">500</span>, <span class="hljs-number">1000</span>, <span class="hljs-string">"strongEaseOut"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228287d5b6ee48918a65f3b147e055f0~tplv-k3u1fbpfcp-watermark.image" alt="0802.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">更广义的“算法”</h2>
<p>策略模式指的是定义一系列的算法，并且把他们封装起来。</p>
<p>从定义上看，策略模式就是用来封装算法的。但如果把策略模式仅仅用来封装算法，有点大材小用。实际开发中，通常会把算法的含义扩散开来，使策略模式也可以用来封装一系列的“业务规则”。只要业务规则指向的目标一致，并且可以被替换使用，我们就可以使用策略模式来封装。</p>
<h2 data-id="heading-10">策略模式的优缺点</h2>
<h3 data-id="heading-11">优点：</h3>
<ul>
<li>策略模式利用组合、委托和多态等技术和思想，可以有效地避免多重条件选择语句。</li>
<li>策略模式提供了对开放-封闭原则的完美支持，将算法封装在独立的 <code>strategy</code> 中，使得它们易于切换，易于理解，易于扩展。</li>
<li>策略模式中的算法也可以复用在系统的其他地方，从而避免许多重复的复制粘贴工作。</li>
<li>在策略模式中利用组合和委托来让 <code>Context</code> 拥有执行算法的能力，这也是继承的一种更轻便的替代方案。</li>
</ul>
<h3 data-id="heading-12">缺点：</h3>
<ul>
<li>使用策略模式会在程序中增加许多策略类或者策略对象</li>
<li>使用策略模式必须了解所有的 <code>strategy</code>，了解各个 <code>strategy</code> 之间的不同点，才能选择一个合适的。</li>
</ul>
<h2 data-id="heading-13">最后说一句</h2>
<p>如果这篇文章对您有所帮助，或者有所启发的话，帮忙点赞关注一下，您的支持是我坚持写作最大的动力，多谢支持。</p></div>  
</div>
            