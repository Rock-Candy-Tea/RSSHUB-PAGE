
---
title: 'JavaScript 设计模式之职责链模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=690'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:25:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=690'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<blockquote>
<p>职责链模式的定义是：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系，将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。</p>
</blockquote>
<h2 data-id="heading-0">现实中的职责链模式</h2>
<ol>
<li>高峰期间坐公交车的车票问题，需要经过N个人手上传递才可以到达售票员的手里。</li>
<li>考试时，遇到不会答的题目，就把题目编号写在小纸条上往后传递，坐在后面的同学如果也不会答，他就会把这张小纸条继续递给他后面的人。</li>
</ol>
<p>从这两个示例可以找到职责链模式的最大优点：请求发送者只需要知道链中的第一个节点，从而弱化了发送者和一组接收者之间的强联系。</p>
<h2 data-id="heading-1">实际开发中的职责链模式</h2>
<p>促销时针对支付过定金的用户有一定的优惠政策。在正式购买后，已经支付过 500 元定金的用户会收到 100 元的商城优惠券，200 元定金的用户可以收到 50 元的优惠券，而之前没有支付定金的用户只能进入普通购买模式，也就是没有优惠券，且在库存有限的情况下不一定保证能买到。</p>
<p>接收一下三个参数：</p>
<ul>
<li><code>orderType</code>：表示订单类型(定金用户或者普通购买用户)，<code>code</code> 的值为 1 的时候是 500 元定金用户，为 2 的时候是 200 元定金用户，为 3 的时候是普通购买用户。</li>
<li><code>pay</code>：表示用户是否已经支付定金，值为 <code>true</code> 或者 <code>false</code>, 虽然用户已经下过 500 元定金的订单，但如果他一直没有支付定金，现在只能降级进入普通购买模式。</li>
<li><code>stock</code>：表示当前用于普通购买的手机库存数量，已经支付过 500 元或者 200 元定金的用户不受此限制。</li>
</ul>
<p>接下来把这个流程写成代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> order = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">// 500 元定金购买模式</span>
    <span class="hljs-keyword">if</span> (pay === <span class="hljs-literal">true</span>) &#123; <span class="hljs-comment">// 已支付定金</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'500 元定金预购, 得到 100 优惠券'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 未支付定金，降级到普通购买模式</span>
      <span class="hljs-keyword">if</span> (stock > <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 用于普通购买的手机还有库存</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通购买, 无优惠券'</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'手机库存不足'</span>);
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">2</span>) &#123;
    <span class="hljs-keyword">if</span> (pay === <span class="hljs-literal">true</span>) &#123;
      <span class="hljs-comment">// 200 元定金购买模式</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'200 元定金预购, 得到 50 优惠券'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (stock > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通购买, 无优惠券'</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'手机库存不足'</span>);
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">3</span>) &#123;
    <span class="hljs-keyword">if</span> (stock > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通购买, 无优惠券'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'手机库存不足'</span>);
    &#125;
  &#125;
&#125;;
order(<span class="hljs-number">1</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出: 500 元定金预购, 得到 100 优惠券</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">用职责链模式重构代码</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 500 元订单</span>
<span class="hljs-keyword">var</span> order500 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">1</span> && pay === <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'500 元定金预购, 得到 100 优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    order200(orderType, pay, stock); <span class="hljs-comment">// 将请求传递给 200 元订单 </span>
  &#125;
&#125;;
<span class="hljs-comment">// 200 元订单</span>
<span class="hljs-keyword">var</span> order200 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">2</span> && pay === <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'200 元定金预购, 得到 50 优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    orderNormal(orderType, pay, stock); <span class="hljs-comment">// 将请求传递给普通订单 &#125;</span>
  &#125;;
&#125;
<span class="hljs-comment">// 普通购买订单</span>
<span class="hljs-keyword">var</span> orderNormal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (stock > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通购买, 无优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'手机库存不足'</span>);
  &#125;
&#125;;
<span class="hljs-comment">// 测试结果:</span>
order500(<span class="hljs-number">1</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:500 元定金预购, 得到 100 优惠券</span>
order500(<span class="hljs-number">1</span>, <span class="hljs-literal">false</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:普通购买, 无优惠券</span>
order500(<span class="hljs-number">2</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:200 元定金预购, 得到 500 优惠券</span>
order500(<span class="hljs-number">3</span>, <span class="hljs-literal">false</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:普通购买, 无优惠券</span>
order500(<span class="hljs-number">3</span>, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>);<span class="hljs-comment">// 输出:手机库存不足</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，执行结果和之前的 <code>order</code> 函数完全一样，但是代码的结构已经清晰很多，我们把一个大函数拆分了3个小函数，去掉了许多嵌套的条件分支语句。</p>
<p>但是，还有不足之处，可以看到请求在链条中的顺序非常僵硬，传递请求的代码被耦合在了业务函数中。这依然是违反开放-封闭原则的，如果有一天要增加300元预定或者去掉200元预定，以为着必须修改这些业务函数内部。<strong>就像一根环环相扣打了死结的链条，如果要增加、拆除或者移动一个节点，就必须得先砸烂这根链条</strong>。</p>
<h2 data-id="heading-3">灵活可拆分的职责链节点</h2>
<p>首先改写下分别表示3种购买模式的节点函数，如果某个节点不能处理请求，则返回一个特定的字符串“<code>nextSuccessor</code>”来表示该请求需要继续往后面传递。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 500 元订单</span>
<span class="hljs-keyword">var</span> order500 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">1</span> && pay === <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'500 元定金预购, 得到 100 优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'nextSuccessor'</span>; <span class="hljs-comment">// 我不知道下一个节点是谁，反正把请求往后面传递</span>
  &#125;
&#125;;
<span class="hljs-comment">// 200 元订单</span>
<span class="hljs-keyword">var</span> order200 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (orderType === <span class="hljs-number">2</span> && pay === <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'200 元定金预购, 得到 50 优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'nextSuccessor'</span>; <span class="hljs-comment">// 我不知道下一个节点是谁，反正把请求往后面传递</span>
  &#125;;
&#125;
<span class="hljs-comment">// 普通购买订单</span>
<span class="hljs-keyword">var</span> orderNormal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">orderType, pay, stock</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (stock > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通购买, 无优惠券'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'手机库存不足'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来需要把函数包装进职责链节点，我们定义一个构造函数 <code>Chain</code>，在 <code>new Chain</code> 的时候传递的参数即为需要被包装的函数，同时它还拥有一个实例属性 <code>this.successor</code>，表示在链中的下一个节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Chain = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.fn = fn;
  <span class="hljs-built_in">this</span>.successor = <span class="hljs-literal">null</span>;
&#125;;
<span class="hljs-comment">// 指定在链中的下一个节点</span>
Chain.prototype.setNextSuccessor = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">successor</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.successor = successor;
&#125;;
<span class="hljs-comment">// 传递请求给某个节点</span>
Chain.prototype.passRequest = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> ret = <span class="hljs-built_in">this</span>.fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
  <span class="hljs-keyword">if</span> (ret === <span class="hljs-string">'nextSuccessor'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.successor && <span class="hljs-built_in">this</span>.successor.passRequest.apply(<span class="hljs-built_in">this</span>.successor, <span class="hljs-built_in">arguments</span>);
  &#125; <span class="hljs-keyword">return</span> ret;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，把3个订单函数分别包装成职责链的节点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> chainOrder500 = <span class="hljs-keyword">new</span> Chain(order500);
<span class="hljs-keyword">var</span> chainOrder200 = <span class="hljs-keyword">new</span> Chain(order200);
<span class="hljs-keyword">var</span> chainOrderNormal = <span class="hljs-keyword">new</span> Chain(orderNormal);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后指定节点在职责链中的顺序:</p>
<pre><code class="hljs language-js copyable" lang="js">chainOrder500.setNextSuccessor(chainOrder200);
chainOrder200.setNextSuccessor(chainOrderNormal);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后把请求传递给第一个节点:</p>
<pre><code class="hljs language-js copyable" lang="js">chainOrder500.passRequest(<span class="hljs-number">1</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>);<span class="hljs-comment">// 输出:500 元定金预购，得到 100 优惠券</span>
chainOrder500.passRequest(<span class="hljs-number">2</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>);<span class="hljs-comment">// 输出:200 元定金预购，得到 50 优惠券 </span>
chainOrder500.passRequest(<span class="hljs-number">3</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>);<span class="hljs-comment">// 输出:普通购买，无优惠券</span>
chainOrder500.passRequest(<span class="hljs-number">1</span>, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>);<span class="hljs-comment">// 输出:手机库存不足</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过改进，我们可以自由灵活地增加、移除和修改链中的节点顺序，假设某天需要支持 300 元定金购买，可以在该链中增加一个节点即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> order300 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 具体实现略</span>
&#125;;
chainOrder300 = <span class="hljs-keyword">new</span> Chain(order300); 
chainOrder500.setNextSuccessor(chainOrder300); 
chainOrder300.setNextSuccessor(chainOrder200);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">异步的职责链</h2>
<p>在上述的职责链模式中，我们让每个节点函数同步返回一个特定的值 <code>nextSuccessor</code> ，来表示是否把请求传递给下一个节点。而在现实开发中，我们经常会遇到一些异步的问题，比如我们要在节点函数中发起一个 <code>ajax</code> 异步请求，异步请求返回的结果才能决定是否继续在职责链中 <code>passRequest</code>。此时，让节点函数同步返回 <code>nextSuccessor</code> 已经没有意义了，所以要给 <code>Chain</code> 类再增加一个原型方法 <code>Chain.prototype.next</code>，表示手动传递请求给职责链中的下一个节点:</p>
<pre><code class="hljs language-js copyable" lang="js">Chain.prototype.next = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.successor && <span class="hljs-built_in">this</span>.successor.passRequest.apply(<span class="hljs-built_in">this</span>.successor, <span class="hljs-built_in">arguments</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，写一个异步职责链：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fn1 = <span class="hljs-keyword">new</span> Chain(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-string">'nextSuccessor'</span>;
&#125;);
<span class="hljs-keyword">var</span> fn2 = <span class="hljs-keyword">new</span> Chain(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>; <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    self.next();
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
<span class="hljs-keyword">var</span> fn3 = <span class="hljs-keyword">new</span> Chain(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;);
fn1.setNextSuccessor(fn2).setNextSuccessor(fn3); 
fn1.passRequest();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">职责链模式的优缺点</h2>
<h3 data-id="heading-6">优点</h3>
<ol>
<li>解耦了请求发送者和 N 个接收者之间的复杂关系，由于不知道链中的哪个节点可以处理你发出的请求，所以你只需把请求传递给第一个节点即可。</li>
<li>链中的节点对象可以灵活地拆分重组。增加或者删除一个节点，或者改变节点在链中的位置都是轻而易举的事情。</li>
<li>可以手动指定起始节点，请求并不是非得从链中的第一个节点开始传递。</li>
</ol>
<h3 data-id="heading-7">缺点</h3>
<ol>
<li>不能保证某个请求一定会被链中的节点处理。在这种情况下，我们可以在链尾增加一个保底的接受者节点来处理这种即将离开链尾的请求。</li>
<li>职责链模式使得程序中多了一些节点对象，可能在某一次的请求传递过程中，大部分节点并没有起到实质性的作用，它们的作用仅仅是让请求传递下去，从性能方面考虑，我们要避免过长的职责链带来的性能损耗。</li>
</ol>
<h2 data-id="heading-8">用 AOP 实现职责链</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.after = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> ret = self.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    <span class="hljs-keyword">if</span> (ret === <span class="hljs-string">'nextSuccessor'</span>) &#123;
      <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    &#125;
    <span class="hljs-keyword">return</span> ret;
  &#125;
&#125;;
<span class="hljs-keyword">var</span> order = order500yuan.after(order200yuan).after(orderNormal);
order(<span class="hljs-number">1</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:500 元定金预购，得到 100 优惠券</span>
order(<span class="hljs-number">2</span>, <span class="hljs-literal">true</span>, <span class="hljs-number">500</span>); <span class="hljs-comment">// 输出:200 元定金预购，得到 50 优惠券</span>
order(<span class="hljs-number">1</span>, <span class="hljs-literal">false</span>, <span class="hljs-number">500</span>);<span class="hljs-comment">// 输出:普通购买，无优惠券</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">最后说一句</h2>
<p>如果这篇文章对您有所帮助，或者有所启发的话，帮忙点赞关注一下，您的支持是我坚持写作最大的动力，多谢支持。</p></div>  
</div>
            