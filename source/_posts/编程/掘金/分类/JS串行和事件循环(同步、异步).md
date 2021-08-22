
---
title: 'JS串行和事件循环(同步、异步)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3642'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 23:46:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=3642'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.JS串行</h1>
<p>JS是<code>单线程</code>的,所以JS中的代码都是<code>串行</code>的, <code>前面没有执行完毕后面不能执行</code></p>
<blockquote>
<p>JavaScript的<code>单线程</code>，与它的用途有关。
作为浏览器脚本语言，JavaScript的<code>主要用途</code>是与用户互动，以及操作DOM。
这决定了它只能是单线程，否则会带来很复杂的同步问题。</p>
</blockquote>
<blockquote>
<p>如果JS是多线程的,现在有一个线程要修改元素中的内容, 一个线程要删除该元素, 这时浏览器应该以哪个线程为准？</p>
</blockquote>
<h1 data-id="heading-1">2.事件循环</h1>
<h2 data-id="heading-2">1.同步代码和异步代码</h2>
<pre><code class="copyable">除了"事件绑定的函数"和"回调函数"以外的都是同步代码
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>1.1 程序运行会<code>从上至下</code>依次执行所有的<code>同步代码</code></li>
<li>1.2 在执行的过程中如果遇到<code>异步代码</code>会将<code>异步代码放到事件循环</code>中</li>
<li>1.3 当<code>所有同步代码都执行完毕后</code>, JS会不断检测 <code>事件循环中的异步代码</code>是否满足条件</li>
<li>1.4 一旦满足条件就<code>执行满足条件的异步代码</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"1"</span>); <span class="hljs-comment">// 同步代码</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 异步代码</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"2"</span>);
    &#125;, <span class="hljs-number">500</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"3"</span>); <span class="hljs-comment">// 同步代码</span>
    alert(<span class="hljs-string">"666"</span>); <span class="hljs-comment">// 同步代码</span>
    <span class="hljs-comment">/*
    // 系统添加代码模拟
    let arr = [setTimeout(function () &#123; // 异步代码
        console.log("2");
    &#125;, 500)];
    事件循环
    let index = 0;
    let length = arr.length;
    while(true)&#123;
        let item = arr[index];
        if(item.time === 500)&#123;
            执行异步代码
        &#125;
        index++;
        if(index === length)&#123;
            index = 0;
        &#125;
    &#125;
    */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>系统添加代码在自己编写的代码之后，所以只有当前面的代码全部执行完了之后才会执行事件循环中的内容</p>
</blockquote>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000015042127" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000015042127" ref="nofollow noopener noreferrer">Event Loop - JS执行机制</a></p></div>  
</div>
            