
---
title: 'ES6 Function 之参数默认值的处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a50e712fab41af848efd79a72b7ad1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 05:23:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a50e712fab41af848efd79a72b7ad1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">1. <code>ES5</code> 中函数参数默认值的设置方式</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y, z</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (y === <span class="hljs-literal">undefined</span>) &#123;
    y = <span class="hljs-number">7</span>
  &#125;
  <span class="hljs-keyword">if</span> (z === <span class="hljs-literal">undefined</span>) &#123;
    z = <span class="hljs-number">42</span>
  &#125;
  <span class="hljs-keyword">return</span> x + y + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>))
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">8</span>))
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">8</span>, <span class="hljs-number">43</span>))

<span class="hljs-comment">/* 运行结果：
50
51
52
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. <code>ES6</code> 中函数参数默认值的设置方式</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 注意：没有默认值的参数写在前面，有默认值的参数写在后面</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y = <span class="hljs-number">7</span>, z = <span class="hljs-number">42</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + y + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>))
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">8</span>))
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">8</span>, <span class="hljs-number">43</span>))
<span class="hljs-comment">// 使用“undefined”实现中间参数的默认值赋值</span>
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">43</span>))

<span class="hljs-comment">/* 运行结果：
50
51
52
51
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数的默认值可以指定为常量，也可以是含有“前面”参数的运算表达式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y = <span class="hljs-number">7</span>, z = x + y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">10</span> + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment">// 1 * 10 + 2 = 12</span>
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 1 * 10 + (1 + 7) = 18</span>
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">9</span>)) <span class="hljs-comment">// 1 * 10 + (1 + 9) = 20</span>
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>)) <span class="hljs-comment">// 1 * 10 + (1 + 7) = 18</span>

<span class="hljs-comment">/* 运行结果：
12
18
20
18
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数的默认值如果指定为含有其它参数的表达式，那么表达式中的参数必须是前面已定义的参数，所以像下面这样指定 <code>y</code> 参数的默认值是错误的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y = x + z, z = <span class="hljs-number">7</span></span>) </span>&#123; <span class="hljs-comment">// 'z' was used before it was defined.</span>
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">10</span> + y
&#125;
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>)) <span class="hljs-comment">// Uncaught ReferenceError: Cannot access 'z' before initialization</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过 <code>arguments</code> 查看当前函数的参数信息：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y = <span class="hljs-number">7</span>, z = x + y</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>) <span class="hljs-comment">// 通过 arguments 查看当前函数的参数的信息</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length) <span class="hljs-comment">// 当前函数传入的参数个数</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>)) <span class="hljs-comment">// 当前函数传入的参数信息，Array.from 用来转换伪数组为数组</span>
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">10</span> + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment">// 传了 3 个参数</span>
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment">// 传了 2 个参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码的运行结果截图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a50e712fab41af848efd79a72b7ad1~tplv-k3u1fbpfcp-watermark.image" alt="image-20200705164938961" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面我们使用了 <code>arguments</code> 来获取当前函数传入的参数信息，但到了 <code>ES6</code> 中，其实是禁止使用 <code>arguments</code> 的，那怎么办呢？有办法，我们后面再讲，这里先讲一下如何获取“<strong>函数定义时未指定默认值的参数个数</strong>”，我们可以使用“<code>函数名.length</code>”的方式实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y = <span class="hljs-number">7</span>, z = x + y</span>) </span>&#123; <span class="hljs-comment">// 注意：没有默认值的参数写在前面，有默认值的参数写在后面</span>
  <span class="hljs-built_in">console</span>.log(f.length) <span class="hljs-comment">// 1</span>
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">10</span> + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">2</span>))

<span class="hljs-comment">/* 运行结果：
1
12
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们把上面函数参数列表中的 <code>y</code> 的默认值去掉，再看 <code>f.length</code> 的值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x, y, z = x + y</span>) </span>&#123; <span class="hljs-comment">// 注意：没有默认值的参数写在前面，有默认值的参数写在后面</span>
  <span class="hljs-built_in">console</span>.log(f.length) <span class="hljs-comment">// 2</span>
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">10</span> + z
&#125;

<span class="hljs-built_in">console</span>.log(f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">2</span>))

<span class="hljs-comment">/* 运行结果：
2
12
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>总结：<code>arguments.length</code> 和 <code>function.length</code> 的区别： <code>arguments.length</code> 获取到的是“函数执行时接收到的参数个数”；而 <code>function.length</code> 获取到是“函数定义时未指定默认值的参数个数（出现首个有默认值的参数前的参数个数）”。</p>
</blockquote></div>  
</div>
            