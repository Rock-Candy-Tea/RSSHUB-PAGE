
---
title: 'JS中的JSON.Stringify 方法详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6567'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 17:37:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=6567'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在大厂的前端面试过程中，<code>JSON.Stringify</code>常常被问到，那么能够熟练的运用，掌握就必不可少。</p>
<p>那么，到底什么是 <code>JSON.stringify</code> 方法？</p>
<h2 data-id="heading-0">方法基本介绍</h2>
<p>JSON.stringify 是日常开发中经常用到的 JSON 对象中的一个方法，JSON 对象包含两个方法：</p>
<ol>
<li>用于解析成 JSON 对象的 parse()；</li>
<li>用于将对象转换为 JSON 字符串方法的 stringify()。</li>
</ol>
<p><strong>下面我们分别来看下两个方法的基本使用情况。</strong></p>
<h2 data-id="heading-1">JSON.parse</h2>
<p>JSON.parse 方法用来解析 JSON 字符串，构造由字符串描述的 JavaScript 值或对象。该方法有两个参数：第一个参数是需要解析处理的 JSON 字符串，第二个参数是可选参数提供可选的 reviver 函数，用在返回之前对所得到的对象执行变换操作。</p>
<blockquote>
<p>该方法的语法为：JSON.parse(text[, reviver])</p>
</blockquote>
<p>下面通过一段代码来看看这个方法以及 reviver 参数的用法，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> json = <span class="hljs-string">'&#123;"result":true, "count":2&#125;'</span>;
<span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">JSON</span>.parse(json);
<span class="hljs-built_in">console</span>.log(obj.count);
<span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(obj.result);
<span class="hljs-comment">// true</span>
<span class="hljs-comment">/* 带第二个参数的情况 */</span>
<span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">'&#123;"p": 5&#125;'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">k, v</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(k === <span class="hljs-string">''</span>) <span class="hljs-keyword">return</span> v;     <span class="hljs-comment">// 如果k不是空，</span>
    <span class="hljs-keyword">return</span> v * <span class="hljs-number">2</span>;              <span class="hljs-comment">// 就将属性值变为原来的2倍返回</span>
&#125;);                            <span class="hljs-comment">// &#123; p: 10 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码说明了，我们可以将一个符合 JSON 格式的字符串转化成对象返回；带第二个参数的情况，可以将待处理的字符串进行一定的操作处理，比如上面这个例子就是将属性值乘以 2 进行返回。</p>
<p>下面我们来了解一下 JSON.stringify 的基本情况。</p>
<h2 data-id="heading-2">JSON.stringify</h2>
<p>JSON.stringify 方法是将一个 JavaScript 对象或值转换为 JSON 字符串，默认该方法其实有三个参数：第一个参数是必选，后面两个是可选参数非必选。第一个参数传入的是要转换的对象；第二个是一个 replacer 函数，比如指定的 replacer 是数组，则可选择性地仅处理包含数组指定的属性；第三个参数用来控制结果字符串里面的间距，后面两个参数整体用得比较少。</p>
<blockquote>
<p>该方法的语法为：JSON.stringify(value[, replacer [, space]])</p>
</blockquote>
<p>下面我们通过一段代码来看看后面几个参数的妙用，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span> &#125;);
<span class="hljs-comment">// "&#123;"x":1,"y":2&#125;"</span>
<span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-attr">x</span>: [<span class="hljs-number">10</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;, <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">''</span>)] &#125;)
<span class="hljs-comment">// "&#123;"x":[10,null,null,null]&#125;"</span>
<span class="hljs-comment">/* 第二个参数的例子 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replacer</span>(<span class="hljs-params">key, value</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">"string"</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
  &#125;
  <span class="hljs-keyword">return</span> value;
&#125;
<span class="hljs-keyword">var</span> foo = &#123;<span class="hljs-attr">foundation</span>: <span class="hljs-string">"Mozilla"</span>, <span class="hljs-attr">model</span>: <span class="hljs-string">"box"</span>, <span class="hljs-attr">week</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">transport</span>: <span class="hljs-string">"car"</span>, <span class="hljs-attr">month</span>: <span class="hljs-number">7</span>&#125;;
<span class="hljs-keyword">var</span> jsonString = <span class="hljs-built_in">JSON</span>.stringify(foo, replacer);
<span class="hljs-built_in">console</span>.log(jsonString);
<span class="hljs-comment">// "&#123;"week":4,"month":7&#125;"</span>
<span class="hljs-comment">/* 第三个参数的例子 */</span>
<span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">2</span> &#125;, <span class="hljs-literal">null</span>, <span class="hljs-string">" "</span>);
<span class="hljs-comment">/* "&#123;
 "a": 2
&#125;"*/</span>
<span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">2</span> &#125;, <span class="hljs-literal">null</span>, <span class="hljs-string">""</span>);
<span class="hljs-comment">// "&#123;"a":2&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看到，增加第二个参数 replacer 带来的变化：通过替换方法把对象中的属性为字符串的过滤掉，在 stringify 之后返回的仅为数字的属性变成字符串之后的结果；当第三个参数传入的是多个空格的时候，则会增加结果字符串里面的间距数量，从最后一段代码中可以看到结果。</p>
<p>如果本篇内容对您有帮助，帮忙点击此链接，让小编加个鸡腿哟！<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgithub.crmeb.net%2Fu%2Fxingfu" target="_blank" rel="nofollow noopener noreferrer" title="http://github.crmeb.net/u/xingfu" ref="nofollow noopener noreferrer">github.crmeb.net/u/xingfu</a></p></div>  
</div>
            