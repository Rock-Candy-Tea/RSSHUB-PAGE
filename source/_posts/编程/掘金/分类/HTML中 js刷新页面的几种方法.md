
---
title: 'HTML中 js刷新页面的几种方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6139'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 21:26:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=6139'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">reload() 方法：</h3>
<ul>
<li>该方法强迫浏览器刷新当前页面。</li>
<li>语法：location.reload([bForceGet])</li>
<li>参数： bForceGet， 可选参数， 默认为 false，从客户端缓存里取当前页。true, 则以 GET 方式，从服务端取最新的页面, 相当于客户端点击 F5(“刷新”)</li>
</ul>
<h3 data-id="heading-1">replace() 方法：</h3>
<ul>
<li>该方法通过指定URL替换当前缓存在历史里（客户端）的项目，因此当使用replace方法之后，你不能通过“前进”和“后退”来访问已经被替换的URL。</li>
<li>语法： location.replace(URL)</li>
</ul>
<br>
<p>      <strong>在实际应用的时候，重新刷新页面的时候，我们通常使用： location.reload() 或者是 history.go(0) 来做。因为这种做法就像是客户端点F5刷新页面，所以页面的method=”post”的时候，会出现”网页过期”的提示。那是因为Session的安全保护机制。
      可以想到： 当调用 location.reload() 方法的时候， aspx页面此时在服务端内存里已经存在， 因此必定是 IsPostback 的。
      如果有这种应用： 我们需要重新加载该页面，也就是说我们期望页面能够在服务端重新被创建， 我们期望是 Not IsPostback 的。这里，location.replace() 就可以完成此任务。被replace的页面每次都在服务端重新生成。</strong>
<br></p>
<h3 data-id="heading-2">返回并刷新页面：</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">language</span>=<span class="hljs-string">”JavaScript”</span>></span><span class="javascript">
    <span class="hljs-comment">//document.referrer 前一个页面的URL</span>
    location.replace(<span class="hljs-built_in">document</span>.referrer);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>不要用 history.go(-1)，或 history.back();来返回并刷新页面，这两种方法不会刷新页面。</em>
<br></p>
<h3 data-id="heading-3">自动刷新页面的方法：</h3>
<ol>
<li>页面自动刷新：把如下代码加入区域中<code><meta http-equiv=”refresh” content=”20″></code>其中20指每隔20秒刷新一次页面</li>
<li>页面自动跳转：把如下代码加入区域中<code><meta http-equiv=”refresh” content=”20;url=http://www.baidu.con”></code>其中20指隔20秒后跳转到<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.con%25E9%25A1%25B5%25E9%259D%25A2" target="_blank" rel="nofollow noopener noreferrer" title="http://www.baidu.con%E9%A1%B5%E9%9D%A2" ref="nofollow noopener noreferrer">www.baidu.con页面</a></li>
<li>页面自动刷新js版
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">language</span>=<span class="hljs-string">”JavaScript”</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myrefresh</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">window</span>.location.reload();
    &#125;
    <span class="hljs-built_in">setTimeout</span>(‘myrefresh()’,<span class="hljs-number">1000</span>); <span class="hljs-comment">//指定1秒刷新一次</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>如果想关闭窗口时刷新或者想开窗时刷新的话，在中调用以下语句即可。
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">onload</span>=<span class="hljs-string">”opener.location.reload()”</span>></span> 开窗时刷新
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">onUnload</span>=<span class="hljs-string">”opener.location.reload()”</span>></span> 关闭时刷新

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">language</span>=<span class="hljs-string">”javascript”</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.opener.document.location.reload()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>本文转自: <a href="https://link.juejin.cn/?target=https%3A%2F%2Ffddcn.cn%2Fjs-shuxin.html" target="_blank" rel="nofollow noopener noreferrer" title="https://fddcn.cn/js-shuxin.html" ref="nofollow noopener noreferrer">fddcn.cn/js-shuxin.h…</a> 请支持原创</p></div>  
</div>
            