
---
title: 'CommonJS 与 ES6 Module 的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4347'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 07:14:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=4347'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这两者的主要区别主要有以下两点：</p>
<ol>
<li>对于模块的依赖，CommonJS是动态的，ES6 Module 是静态的</li>
<li>CommonJS导入的是值的拷贝，ES6 Module导入的是值的引用</li>
</ol>
<h3 data-id="heading-0">exports和module.exports</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//首先明白</span>
<span class="hljs-built_in">exports</span> === <span class="hljs-built_in">module</span>.exports <span class="hljs-comment">//true</span>
<span class="hljs-comment">//也就是说他们指向同一个地址</span>
<span class="hljs-comment">//相当于</span>
<span class="hljs-keyword">let</span> <span class="hljs-built_in">module</span> = &#123;
  <span class="hljs-attr">exports</span>:&#123;
    ...
  &#125;
&#125;
<span class="hljs-keyword">let</span> <span class="hljs-built_in">exports</span> = <span class="hljs-built_in">module</span>.exports
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">export和export default</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//export.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;&#125;;
<span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> &#123; Clock, a&#125;

<span class="hljs-comment">//import.js</span>
<span class="hljs-keyword">import</span> App, &#123;Clock <span class="hljs-keyword">as</span> Clock1,a&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./export.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">区别一</h3>
<p>对于模块的依赖，何为动态？何为静态？
动态是指对于模块的依赖关系建立在代码执行阶段； 静态是指对于模块的依赖关系建立在代码编译阶段；
上文提到，CommonJS导入时，require的路径参数是支持表达式的，例如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// A.js</span>
<span class="hljs-keyword">let</span> fileName = <span class="hljs-string">'example.js'</span>
<span class="hljs-keyword">const</span> bModule = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./'</span> + fileName)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为该路径在代码执行时是可以动态改变的，所以如果在代码编译阶段就建立各个模块的依赖关系，那么一定是不准确的，只有在代码运行了以后，才可以真正确认模块的依赖关系，因此说CommonJS是动态的。
那么现在你也应该也知道为什么 ES6 Module 是静态的了吧</p>
<h3 data-id="heading-3">区别二</h3>
<p>为了验证这一点，我准备用实例来演示一下
首先来验证CommonJS，代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// B.js</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">3</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params"></span>) </span>&#123;
    count ++    <span class="hljs-comment">// 变量count + 1</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'原count值为：'</span>, count);  <span class="hljs-comment">// 打印B.js模块中count的值</span>
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
    count,
    change
&#125;
<span class="hljs-comment">// A.js</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./B.js'</span>).count 
<span class="hljs-keyword">let</span> change = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./B.js'</span>).change
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变前：'</span>, count);   
change()     <span class="hljs-comment">// 调用模块B.js中的change方法，将原来的count + 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变后：'</span>, count); 
<span class="hljs-comment">// 运行A.js文件的结果</span>
改变前：<span class="hljs-number">3</span>
原count值为：<span class="hljs-number">4</span>
改变后：<span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中我们可以看到，在A.js文件中导入了B.js文件中的变量count和 函数change，因为导入的count只是对原有值的一个拷贝，因此尽管我们调用了函数change改变了B.js文件中变量count的值，也不会影响到A.js文件中的变量count
根据这个结果得出结论：CommonJS导入的变量是对原值的拷贝
接下来再来验证一下ES6 Module，代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// B.js</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">3</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params"></span>) </span>&#123;
    count ++        <span class="hljs-comment">// 变量count + 1</span>
    <span class="hljs-built_in">console</span>.log(count);   <span class="hljs-comment">// 打印B.js模块中count的值</span>
&#125;
<span class="hljs-keyword">export</span> &#123;count, change&#125;
<span class="hljs-comment">// A.js</span>
<span class="hljs-keyword">import</span> &#123;count, change&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./B.js'</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变前：'</span>,count);
change()         <span class="hljs-comment">// 调用模块B.js中的change方法，将原来的count + 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变后：'</span>, count);
<span class="hljs-comment">// 运行A.js文件的结果</span>
改变前：<span class="hljs-number">3</span>
原count值为：<span class="hljs-number">4</span>
改变后：<span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比较于CommonJS的结果，ES6 Module导入的变量count随着原值的改变而改变了
根据这个结果得出结论：ES6 Module导入的变量是对原值的引用</p></div>  
</div>
            