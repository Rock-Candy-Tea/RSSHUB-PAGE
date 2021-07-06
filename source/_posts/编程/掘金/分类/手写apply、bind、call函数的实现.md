
---
title: '手写apply、bind、call函数的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c91ab29593f4bd785677bfc672839ba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:40:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c91ab29593f4bd785677bfc672839ba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c91ab29593f4bd785677bfc672839ba~tplv-k3u1fbpfcp-watermark.image" alt="20210414155100.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">    apply、call、bind是挂载在<span class="hljs-built_in">Function</span>对象上的三个方法，调用这三个方法必须是一个函数。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在浏览器里，全局范围内的this指向window</li>
<li>在函数内，this永远指向最后调用他的那个对象</li>
<li>在构造函数中，this指向new出来的那个对象</li>
<li>call、apply、bind中的this被强制绑定在指向的那个对象上</li>
<li>箭头函数中的this比较特殊，其this指向父作用域的this</li>
</ul>
<h2 data-id="heading-0">实现一个bind函数</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myBind = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
     <span class="hljs-comment">// 不是函数抛出异常</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'类型错误'</span>)
    &#125;
    <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">// 保留上个函数的传值</span>
    <span class="hljs-keyword">let</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// args.concat(arguments) 这两个顺序不能变 arguments为类数组没有concat方法</span>
        _this.apply(context, args.concat(<span class="hljs-built_in">arguments</span>))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">实现一个apply函数</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实现原理 this永远指向最后调用他的那对象</span>
<span class="hljs-built_in">Function</span>.prototype.myApply = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'类型错误'</span>)
    &#125;
    <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'key'</span>)
    context[key] = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> result = context[key](<span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>))
    <span class="hljs-keyword">delete</span> context[key]
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">实现一个call函数</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myCall = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, ...ags</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'类型错误'</span>)
    &#125;
    <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'key'</span>)
    context[key] = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> reslut = context[key](...ags)
    <span class="hljs-keyword">delete</span> context[key]
    <span class="hljs-keyword">return</span> reslut
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            