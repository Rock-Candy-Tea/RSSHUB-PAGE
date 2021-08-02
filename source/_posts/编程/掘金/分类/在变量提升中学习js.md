
---
title: '在变量提升中学习js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63304c2d9c87467c8a06bb07b777969d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 22:45:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63304c2d9c87467c8a06bb07b777969d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前提</h2>
<p>众所周知，js的变量提升很烦人，常见的语言大部分都是函数声明提升，这很好理解，方便程序员，但是变量提升就常常会产生各种意想不到的输出结果。js之父<strong>Brendan Eich</strong>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Ftwitter.com%2FBrendanEich%2Fstatus%2F522395336615428097" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//twitter.com/BrendanEich/status/522395336615428097" ref="nofollow noopener noreferrer">twitter说过这样的话</a>，</p>
<blockquote>
<p>var hoisting was thus unintended consequence of function hoisting, no block scope, JS as a 1995 rush job. ES6 'let' may help.</p>
</blockquote>
<p>大概意思就是当年开发js这个需求太赶了，开发函数提升时，不小心带来了<strong>var变量提升</strong>。</p>
<h2 data-id="heading-1">例子</h2>
<p>1️⃣</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(a) &#123;
        <span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
f()
<span class="hljs-comment">// 结果是undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咋看一下，会觉得结果是<code>10</code>，再看一下，会觉得结果是<code>1</code>, 但其实结果是<code>undefined</code>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63304c2d9c87467c8a06bb07b777969d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在执行<code>f</code>时，会把函数和变量的声明进行提升，所以对于<code>f</code>而言， <code>var a</code>存在变量提升并且初始化为undefined，这时候f里面的a就是undefined，而不是我们<strong>直觉的外部的a</strong>，所以不会命中判断逻辑，a也就不会被赋值, 所以输出的a就是undefined。</p>
<p>2️⃣</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(a) &#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
f()
<span class="hljs-comment">// 结果是1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>题目稍微改一下，<code>var a</code>改成<code>let a</code>, 这时候输出的结果就是1，这就是涉及到我们老生常谈的块作用域，<code>let a </code>里的<code>a</code>只会在块里生效，一旦出了块，作用域就失效，所以下面输出的<code>a</code>其实是全局的<code>a</code>。 把if改成普通的块其实结果也是一样的，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    &#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
f()
<span class="hljs-comment">// 结果是1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以看到这里，那道经典的面试题你们应该会了吧, <strong>把结果打在公屏上(bushi)</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1adf83c7da34423bec95c0aa00dec7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>; a < <span class="hljs-number">5</span>; a ++) &#123;
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
f()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3️⃣</p>
<p>题目继续改一下，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(a) &#123;
       <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
f()
<span class="hljs-comment">// 结果是undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候可能就会有人抢答，说答案是<code>function a() &#123;&#125;</code>,</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1fd13bb3784d42983ff47eaf7d93b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我上面明明写了结果是<code>undefined</code>。<br>
<strong>很多资料不都好说function是创建，初始化，赋值一起的吗？</strong> 大部分情况确实是这样，但是这里产生了块作用域，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fblock" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/block" ref="nofollow noopener noreferrer">MDN</a>上面还特别标注了出来，</p>
<blockquote>
<p>使用<code>function</code><br>
函数声明同样被限制在声明他的语句块内:</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">foo(<span class="hljs-string">'outside'</span>);  <span class="hljs-comment">// TypeError: foo is not a function  </span>
&#123;  
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">location</span>) </span>&#123;  
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo is called '</span> + location);  
   &#125;  
  foo(<span class="hljs-string">'inside'</span>); <span class="hljs-comment">// 正常工作并且打印 'foo is called inside'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">送分题</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> ff()
    <span class="hljs-keyword">var</span> ff = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>&#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ff</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-number">2</span>&#125;
&#125;
<span class="hljs-built_in">console</span>.log(f())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路过可以把答案打在评论区～</p></div>  
</div>
            