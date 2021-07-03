
---
title: 'JavaScript基础知识 001---typeof和instanceof'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1159'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 05:03:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=1159'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">理解typeof和instanceof</h1>
<h2 data-id="heading-1">1.1 typeof</h2>
<h3 data-id="heading-2">1.1.1 理解</h3>
<p>我们都知道type是用来检测数据类型的，包括（string,number,boolean,object,function,undefined,Symbol</p>
<p>但是他也有一定的局限性，比如检测object,array,null都是object，这就使得我们无法具体判断他们的类型.</p>
<h3 data-id="heading-3">1.1.2 语法</h3>
<p>返回值是字符串，表示当前变量的数据类型，可以根据自己喜欢的用法去使用，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span><span class="hljs-keyword">typeof</span>(表达式)
<span class="hljs-number">2.</span><span class="hljs-keyword">typeof</span> 变量名
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.1.3 实例</h3>
<p>可以检测的数据类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-number">1</span>))<span class="hljs-comment">//number    </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-string">''</span>))<span class="hljs-comment">//string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-literal">true</span>))<span class="hljs-comment">//boolean</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(&#123;&#125;))<span class="hljs-comment">//object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-function">()=></span>&#123;&#125;))<span class="hljs-comment">//function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-literal">undefined</span>))<span class="hljs-comment">//undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-built_in">Symbol</span>()))<span class="hljs-comment">//symbol</span>
 
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">1</span> )<span class="hljs-comment">//number当然你也可以这样用(手动狗头),结果都是一样的，就不一一举例了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无法判别的数据类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(&#123;&#125;))<span class="hljs-comment">//object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>(<span class="hljs-literal">null</span>))<span class="hljs-comment">//object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span>([]))<span class="hljs-comment">//object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">1.2 instanceof</h2>
<h3 data-id="heading-6">1.2.1 理解</h3>
<p>用于检测构造函数的 <code>prototype</code> 属性是否出现在某个实例对象的原型链上。如果不懂原型与原型链的请阅读相关文章<a href="https://www.cnblogs.com/loveyaxin/p/11151586.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/loveyaxin/p…</a></p>
<h3 data-id="heading-7">1.2.2 语法</h3>
<p>检测右边变量的prototype是否在左边变量的原型链上，若找到则返回true,否则返回false</p>
<pre><code class="hljs language-js copyable" lang="js">object <span class="hljs-keyword">instanceof</span> <span class="hljs-title">constructor</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1.1.3 实例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">D</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">let</span> o=<span class="hljs-keyword">new</span> C()
<span class="hljs-built_in">console</span>.log(o <span class="hljs-keyword">instanceof</span> C)<span class="hljs-comment">//true</span>
C.prototype=&#123;&#125;<span class="hljs-comment">//使得C的原型指向空对象，则空对象不在o的原型链上</span>
<span class="hljs-built_in">console</span>.log(o <span class="hljs-keyword">instanceof</span> C)<span class="hljs-comment">//false  </span>
<span class="hljs-built_in">console</span>.log(o <span class="hljs-keyword">instanceof</span> D)<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(o <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(D <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)<span class="hljs-comment">//true  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述内容仅仅代表个人观点，如有错误，请指正。如果你也对前端感兴趣，欢迎访问我的个人博客<a href="https://sundestiny.github.io/myblog/" target="_blank" rel="nofollow noopener noreferrer">sundestiny.github.io/myblog/</a></p></div>  
</div>
            