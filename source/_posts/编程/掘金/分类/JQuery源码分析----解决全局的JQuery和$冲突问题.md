
---
title: 'JQuery源码分析----解决全局的JQuery和$冲突问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1284'
author: 掘金
comments: false
date: Mon, 17 May 2021 19:08:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=1284'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>最近在学习JQuery源码，看到源码中,暴露给去全局的JQuery和<code>$ </code>如果和当前全局的JQuery和<code>$</code>冲突解决办法，很值得学习。特此记录一下！</p>
<h3 data-id="heading-1">解决冲突的方法（源码）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> _jQuery=<span class="hljs-built_in">window</span>.jQuery,_$=<span class="hljs-built_in">window</span>.$;
jQuery.onConflict=<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onConflict</span>(<span class="hljs-params">deep</span>)</span>&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.$===jQuery)&#123;
<span class="hljs-comment">//把$的使用权归还给之前使用它的人</span>
<span class="hljs-built_in">window</span>.$===_$
&#125;
<span class="hljs-keyword">if</span>(deep&&<span class="hljs-built_in">window</span>.jQuery===jQuery)&#123;
<span class="hljs-comment">//传递deep=true，可以把Jquery名字的使用权转移出去</span>
<span class="hljs-built_in">window</span>.jQuery=_jQuery
&#125;
<span class="hljs-comment">//返回自己的：在外面基于一个别名接收，以后别名代表当前自己的</span>
<span class="hljs-keyword">return</span> jQuery;
&#125;
<span class="hljs-built_in">window</span>.jQuery=<span class="hljs-built_in">window</span>.$=jQuery;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">两种冲突问题</h3>
<h4 data-id="heading-3">不同类库之间对$使用权的冲突</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Zepto.js</span>
<span class="hljs-built_in">window</span>.Zepto=<span class="hljs-built_in">window</span>.$=Zepto;
<span class="hljs-comment">//Jquery.js</span>
<span class="hljs-built_in">window</span>.jQuery=<span class="hljs-built_in">window</span>.$=jQuery;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当先引入Zepto.js后，<code>$</code>等于Zepto，然后引入Jquery.js，<code>$</code>变成了Jquery，这样相当于我们自己编写的程序变量和原始全局下的内容冲突了</li>
</ul>
<h5 data-id="heading-4">解决办法</h5>
<ol>
<li>在导入完成JQ之前，先把现有全局下的Jquery和<code>$</code>代表的东西存储到私有变量_jQuery和<code>_$</code>中</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> _jQuery=<span class="hljs-built_in">window</span>.jQuery;
_$=<span class="hljs-built_in">window</span>.$<span class="hljs-comment">//此时window.$是Zepto</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>提供转让使用权的方法 noConfilct,如果当前的<code>window.$===jQuery</code>,那么就把<code>$</code>的使用权归还给之前的Zepto(<code>window.$===_$</code>)</li>
<li>noConfilct方法最后返回一个jQuery，如果发生冲突了，那就自己定义一个变量接收noConfilct方法的返回值，这样可以使用jQuery。<code>let j=$.noConfilct()</code></li>
</ol>
<h4 data-id="heading-5">一个产品导入不同版本的jQuery，$和jQuery都会冲突</h4>
<ul>
<li>当我们引入不同的版本的jquery，会使用最后引用版本的jquery，但这样会导致之前老版本的jquery一些功能出问题。</li>
</ul>
<h5 data-id="heading-6">解决办法</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> _jQuery=<span class="hljs-built_in">window</span>.jQuery <span class="hljs-comment">//老版本的jq</span>
<span class="hljs-comment">//在noConfilct函数中</span>
<span class="hljs-keyword">if</span>(deep&&<span class="hljs-built_in">window</span>.jQuery===jQuery)&#123;
<span class="hljs-built_in">window</span>.jQuery=_jQuery
&#125;
<span class="hljs-keyword">return</span> jQuery;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>deep等于true，把jQuery的使用权归还给之前的老版本，新版本自己再定义一个变量使用。</li>
</ul>
<h3 data-id="heading-7">总结</h3>
<p>Jquery解决冲突的思路很简单，在当前类库没有导入完之前，就是把之前冲突变量代表什么保存到私有变量中，然后让现在全大局的<code>$</code>和Jquery都以最新的自己导入的为主。如果发生冲突，就调用onConflict方法，把<code>$</code>的使用权归还给之前使用它的人,然后在外面定义一个变量接收onConflict返回的jquery。</p></div>  
</div>
            