
---
title: 'javascript —— 如何理解Function.prototype.bind.apply'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5566'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 00:35:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=5566'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在学习javascript的时候，发现了一个有趣东西，那就是<code>Function.prototype.call.apply(handleFn,obj)</code>。咋一看，还有点懵逼，这用法有啥用啊？别急，我们来一步一步分析它。</p>
<p>首先我们先来看一个最基本的例子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">payload</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = payload || <span class="hljs-string">"默认值"</span>
&#125;
fn.call(obj, <span class="hljs-string">"张三"</span>);
<span class="hljs-built_in">console</span>.log(obj);<span class="hljs-comment">//&#123;name:"张三"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码输出为<code>&#123;name:"张三"&#125;</code>,这个结果不奇怪，就是<code>call</code>的简单用法，至于apply、bind这里不做演示，不知道的读者，请自行查阅。</p>
<hr>
<p>接下来分析<code>Function.prototype.call.apply(handleFn,obj)</code>:</p>
<blockquote>
<p>参数分析：handleFn（函数）  obj（想要绑定的对象）</p>
</blockquote>
<ul>
<li>你可以把Function.prototype.call看出一个整体，将参数按照apply的形式传进去
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.call.apply(handleFn,[obj,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>])
<span class="hljs-comment">//相当于</span>
handleFn.apply(obj,[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>如果不明白我们继续看另一种
<pre><code class="copyable">Function.prototype.call.call(handleFn,obj,1,2,3)
//相当于
handleFn.call(obj,1,2,3)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>写一段代码，看一下输出，验证我们上面说的结果</p>
<ul>
<li>
<p>示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"杨志强"</span>,
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">arg1, arg2</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    <span class="hljs-built_in">console</span>.log(arg1);
    <span class="hljs-built_in">console</span>.log(arg2);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>输出验证：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.call.apply(fn, [obj, <span class="hljs-string">"参数一"</span>, <span class="hljs-string">"参数二"</span>]);<span class="hljs-comment">//杨志强 参数一 参数二</span>
<span class="hljs-comment">// 等价于</span>
<span class="hljs-built_in">Function</span>.prototype.call.call(fn,obj,<span class="hljs-string">"参数一"</span>，<span class="hljs-string">"参数二"</span>);<span class="hljs-comment">//杨志强 参数一 参数二</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面结果我们可以看出，<code>Function.prototype.XXX.YYY</code>,这个<code>XXX</code>是call或者apply都可以，但是<code>YYY</code>是决定传递参数形式的。</p>
</li>
<li>
<p>实际场景：计算每个学生的成绩</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> stu1 = &#123;
    <span class="hljs-attr">chinese</span>: <span class="hljs-number">58</span>,
    <span class="hljs-attr">math</span>: <span class="hljs-number">68</span>,
    <span class="hljs-attr">english</span>: <span class="hljs-number">90</span>
&#125;
<span class="hljs-keyword">var</span> stu2 = &#123;
    <span class="hljs-attr">chinese</span>: <span class="hljs-number">80</span>,
    <span class="hljs-attr">math</span>: <span class="hljs-number">38</span>,
    <span class="hljs-attr">english</span>: <span class="hljs-number">90</span>
&#125;


<span class="hljs-keyword">var</span> utils = &#123;
    <span class="hljs-function"><span class="hljs-title">getSum</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.chinese + <span class="hljs-built_in">this</span>.math + <span class="hljs-built_in">this</span>.english

    &#125;
&#125;
<span class="hljs-keyword">const</span> calc = <span class="hljs-built_in">Function</span>.prototype.call.bind(utils.getSum);
<span class="hljs-keyword">const</span> res = calc(stu1);
<span class="hljs-keyword">const</span> res2 = calc(stu2);
<span class="hljs-built_in">console</span>.log(res);
<span class="hljs-built_in">console</span>.log(res2);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            