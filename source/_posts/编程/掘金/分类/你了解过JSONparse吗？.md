
---
title: '你了解过JSON.parse吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d88e37fa62452b9daf5a858e12aaa5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 16:36:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d88e37fa62452b9daf5a858e12aaa5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天</p>
<p>JavaScript的JSON字符串转换为JS对象的方式我们常常用的有三种:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'&#123;"name":"悟空","age":500&#125;'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>将字符串转换为Java对象的方式</strong></p>
<ul>
<li>var json = JSON.parse(str); <strong>推荐使用</strong></li>
<li>var json = eval("(" + str + ")"); 很早之前用过</li>
<li>var json = (new Function("return " + str))(); 没有用过</li>
</ul>
<p>运行结果为:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d88e37fa62452b9daf5a858e12aaa5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">1.JSON.parse() 使用</h2>
<p><strong>JSON.parse()</strong> 方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象。提供可选的reviver函数用以在返回之前对所得到的对象执行变换(操作)。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'&#123;"name":"悟空","age":18&#125;'</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.parse(str));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法结构: <code>JSON.parse(text[, reviver])</code></p>
<p><strong>text</strong>: 要被解析成JavaScript值的字符串，查看 JSON 对象学习的JSON 语法的说明。</p>
<p><strong>reviver[可选]</strong>: 如果是一个函数，则规定了原始值如何被解析改造，在被返回之前。</p>
<p><strong>返回值</strong>: Object对应给定的JSON文本。</p>
<p><strong>异常</strong>: 若被解析的 JSON 字符串是非法的，则会抛出 一个 <code>语法错误</code> 异常。</p>
<p><strong>测试reviver参数使用</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">var</span> user = &#123;
    name: <span class="hljs-string">'pangsir'</span>,
    email: <span class="hljs-string">'hanpang8983@foxmail.com'</span>,
    age: <span class="hljs-number">18</span>,
    status:<span class="hljs-keyword">false</span>
&#125;;

<span class="hljs-keyword">var</span> userStr = JSON.stringify(user);

<span class="hljs-keyword">var</span> newUserStr = JSON.parse(userStr, function(key, value)&#123;
    <span class="hljs-keyword">if</span> (typeof value === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> value.toUpperCase();
    &#125;
    <span class="hljs-keyword">if</span>(typeof value === <span class="hljs-string">'number'</span>)&#123;
        <span class="hljs-keyword">return</span> value*<span class="hljs-number">2</span>;
    &#125;
    <span class="hljs-keyword">return</span> value;
&#125;);

console.log(newUserStr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果为</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c92edaf69a06474ebd0c4cce62924ae3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果指定了 <code>reviver</code> 函数，则解析出的 JavaScript 值（解析值）会经过一次转换后才将被最终返回（返回值）。更具体点讲就是：解析值本身以及它所包含的所有属性，会按照一定的顺序（从最最里层的属性开始，一级级往外，最终到达顶层，也就是解析值本身）分别的去调用 <code>reviver</code> 函数，在调用过程中，当前属性所属的对象会作为 <code>this</code> 值，当前属性名和属性值会分别作为第一个和第二个参数传入 <code>reviver</code> 中。如果 <code>reviver</code> 返回 <code>undefined</code>，则当前属性会从所属对象中删除，如果返回了其他值，则返回的值会成为当前属性新的属性值。</p>
<p>当遍历到最顶层的值（解析值）时，传入 <code>reviver</code> 函数的参数会是空字符串 <code>""</code>（因为此时已经没有真正的属性）和当前的解析值（有可能已经被修改过了），当前的 <code>this</code> 值会是 <code>&#123;"": 修改过的解析值&#125;</code>，在编写 <code>reviver</code> 函数时，要注意到这个特例。（这个函数的遍历顺序依照：从最内层开始，按照层级顺序，依次向外遍历）</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">'&#123;"p": 5&#125;'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">k, v</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(k === <span class="hljs-string">''</span>) <span class="hljs-keyword">return</span> v;     <span class="hljs-comment">// 如果到了最顶层，则直接返回属性值，</span>
    <span class="hljs-keyword">return</span> v * <span class="hljs-number">2</span>;              <span class="hljs-comment">// 否则将属性值变为原来的 2 倍。</span>
&#125;);                            <span class="hljs-comment">// &#123; p: 10 &#125;</span>

<span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">'&#123;"1": 1, "2": 2,"3": &#123;"4": 4, "5": &#123;"6": 6&#125;&#125;&#125;'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">k, v</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(k); <span class="hljs-comment">// 输出当前的属性名，从而得知遍历顺序是从内向外的，</span>
                    <span class="hljs-comment">// 最后一个属性名会是个空字符串。</span>
    <span class="hljs-keyword">return</span> v;       <span class="hljs-comment">// 返回原始属性值，相当于没有传递 reviver 参数。</span>
&#125;);

<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 4</span>
<span class="hljs-comment">// 6</span>
<span class="hljs-comment">// 5</span>
<span class="hljs-comment">// 3 </span>
<span class="hljs-comment">// ""</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.注意的坑点</h2>
<h3 data-id="heading-2">A.JSON.parse() 不允许用逗号作为结尾</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// both will throw a SyntaxError</span>
<span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">"[1, 2, 3, 4, ]"</span>);
<span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">'&#123;"foo" : 1, &#125;'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">B.单引号与双引号</h3>
<p>我们看到一开始的举例中 <code>var str = '&#123;"name":"悟空","age":18&#125;';</code></p>
<p>使用单引号来套双引号，如果反过来写呢，</p>
<p>如：<code>var str = "&#123;'name':'小明', 'age':18&#125;";</code>（相信也不少人习惯用双引号套单引号）</p>
<p>结果使用JSON.parse()来转化也会报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33ae18370fc94d91b64d8ec136b1e164~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">C.兼容问题</h3>
<p>IE6/7浏览器中不支持使用JSON.parse()方法转成json对象，所以需要引入一个json2.js文件。可以在这个网站（<a href="https://github.com/douglascrockford/JSON-js" target="_blank" rel="nofollow noopener noreferrer">json2.js</a>）去下载对象文件。</p>
<p>最后总结来说，如果使用JSON.parse()方法来转化成json对象的数据格式的话，需要注意的是被转化的字符串里面的属性要使用引号，并且总体是单引号套双引号的方式，以及IE6/7浏览器是不支持该方法。</p>
<p>当然，如果你使用eval()或者new Function()的方式来转化，那就完全可以忽略上述的这两点需要注意的地方!</p></div>  
</div>
            