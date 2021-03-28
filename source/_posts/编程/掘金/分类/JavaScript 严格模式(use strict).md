
---
title: 'JavaScript 严格模式(use strict)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3677c49f37a46d4b0bcdb1bdef2385a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 04:14:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3677c49f37a46d4b0bcdb1bdef2385a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>"use strict" 指令在 JavaScript 1.8.5 (ECMAScript5) 中新增, 它不是一条语句，但是是一个字面量表达式，在 JavaScript 旧版本中会被忽略<br>
"use strict" 指令只允许出现在脚本或函数的开头<br>
严格模式(strict mode)目的是指定代码在严格条件下执行, 严格模式下你不能使用未声明的变量<br>
⚠️ 支持严格模式的浏览器:Internet Explorer 10 +、 Firefox 4+ Chrome 13+、 Safari 5.1+、 Opera 12+</p>
</blockquote>
<h3 data-id="heading-0">严格模式声明</h3>
<ul>
<li>严格模式通过在脚本或函数的头部添加 "use strict"; 表达式来声明</li>
<li>实例中我们可以在浏览器按下 <strong>F12 (或点击"工具>更多工具>开发者工具")</strong> 开启调试模式，查看报错信息</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>使用 "use strict":<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>不允许使用未定义的变量<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>浏览器按下 F12 开启调试模式，查看报错信息<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"><span class="hljs-meta">
      "use strict"</span>;
      x = <span class="hljs-number">3.14</span>;       <span class="hljs-comment">// 报错 (x 未定义)</span>
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="pic_001.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3677c49f37a46d4b0bcdb1bdef2385a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>在函数内使用 "use strict" 只在函数内报错 <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>浏览器按下 F12 开启调试模式，查看报错信息<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      x = <span class="hljs-number">3.14</span>       <span class="hljs-comment">// 不报错 </span>
      myFunction()
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunction</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">        "use strict"</span>
        y = <span class="hljs-number">3.14</span> <span class="hljs-comment">// 报错 (y 未定义),如果注释作用域中(&#123;&#125;)的"use strict"则不会报错</span>
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">为什么使用严格模式</h3>
<ul>
<li>消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为</li>
<li>消除代码运行的一些不安全之处，保证代码运行的安全；</li>
<li>提高编译器效率，增加运行速度；</li>
<li>为未来新版本的Javascript做好铺垫</li>
</ul>
<p>"严格模式"体现了Javascript更合理、更安全、更严谨的发展方向，包括IE 10在内的主流浏览器，都已经支持它，许多大项目已经开始全面拥抱它。
另一方面，同样的代码，在"严格模式"中，可能会有不一样的运行结果；一些在"正常模式"下可以运行的语句，在"严格模式"下将不能运行。掌握这些内容，有助于更细致深入地理解Javascript，让你变成一个更好的程序员</p>
<h3 data-id="heading-2">严格模式的限制</h3>
<h4 data-id="heading-3">不允许使用未声明的变量</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
x = <span class="hljs-number">3.14</span>               <span class="hljs-comment">// 报错 (x 未定义)</span>
y = &#123;<span class="hljs-attr">p1</span>:<span class="hljs-number">10</span>, <span class="hljs-attr">p2</span>:<span class="hljs-number">20</span>&#125;     <span class="hljs-comment">// 报错 (y 未定义)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">不允许删除变量或对象</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> x = <span class="hljs-number">3.14</span>;
<span class="hljs-keyword">delete</span> x;                <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">不允许删除函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">x</span>(<span class="hljs-params">p1, p2</span>) </span>&#123;&#125;; 
<span class="hljs-keyword">delete</span> x;                <span class="hljs-comment">// 报错 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">不允许变量重名</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">x</span>(<span class="hljs-params">p1, p1</span>) </span>&#123;&#125;;   <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">不允许使用转义字符</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> x = \<span class="hljs-number">010</span>;            <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">不允许对只读属性赋值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> obj = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">"x"</span>, &#123;<span class="hljs-attr">value</span>:<span class="hljs-number">0</span>, <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>&#125;);

obj.x = <span class="hljs-number">3.14</span>;            <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">不允许对一个使用getter方法读取的属性进行赋值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-keyword">get</span> <span class="hljs-title">x</span>() &#123;<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>&#125; &#125;;

obj.x = <span class="hljs-number">3.14</span>;            <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">不允许删除一个不允许删除的属性</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">delete</span> <span class="hljs-built_in">Object</span>.prototype; <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">变量名不能使用 "eval" 字符串</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> <span class="hljs-built_in">eval</span> = <span class="hljs-number">3.14</span>;         <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">变量名不能使用 "arguments" 字符串</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> <span class="hljs-built_in">arguments</span> = <span class="hljs-number">3.14</span>;    <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">不允许使用以下这种语句</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">with</span> (<span class="hljs-built_in">Math</span>)&#123;x = cos(<span class="hljs-number">2</span>)&#125;; <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">由于一些安全原因，在作用域 eval() 创建的变量不能被调用</h4>
<p>eval()能够解析JavaScript 字符串并执行字符串中的脚本代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-built_in">eval</span> (<span class="hljs-string">"var x = 2"</span>);
alert (x);               <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">禁止this关键字指向全局对象</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> !<span class="hljs-built_in">this</span>;
&#125; 
<span class="hljs-comment">// 返回false，因为"this"指向全局对象，"!this"就是false</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123; 
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">return</span> !<span class="hljs-built_in">this</span>;
&#125; 
<span class="hljs-comment">// 返回true，因为严格模式下，this的值为undefined，所以"!this"为true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，使用构造函数时，如果忘了加new，this不再指向全局对象，而是报错</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;
&#125;;
f();<span class="hljs-comment">// 报错，this未定义</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">禁止使用保留关键字</h4>
<p>为了向将来Javascript的新版本过渡，严格模式新增了一些保留关键字：</p>




















<table><thead><tr><th>implements</th><th>interface</th><th>let</th></tr></thead><tbody><tr><td>package</td><td>private</td><td>protected</td></tr><tr><td>public</td><td>static</td><td>yield</td></tr></tbody></table>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> public = <span class="hljs-number">1500</span>;      <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            