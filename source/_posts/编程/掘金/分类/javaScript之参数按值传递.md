
---
title: 'javaScript之参数按值传递'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbc0fe6fefb4b838cd22ea0a9f48e36~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 01:47:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbc0fe6fefb4b838cd22ea0a9f48e36~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">javaScript之参数按值传递</h4>
<p>js中基础数据类型在栈中存储：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbc0fe6fefb4b838cd22ea0a9f48e36~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>

<p>js中引用型数据类型，变量名和地址存放在栈，变量值存放在堆内存：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fbd5bf395a42e5b6757c84a4768be7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面来看函数中的参数传值：</p>
<p><strong>按值传递</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> value = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">v</span>) </span>&#123;
    v = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(v); <span class="hljs-comment">//2</span>
&#125;
foo(value);
<span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改变前：</p>

















<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">value: 1</td><td align="center"></td></tr><tr><td align="center">v: 1</td><td align="center"></td></tr></tbody></table>
<p>改变后：</p>

















<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">value：1</td><td align="center"></td></tr><tr><td align="center">v:2</td><td align="center"></td></tr></tbody></table>
<p>很好理解，当传递 value 到函数 foo 中，相当于拷贝了一份 value，假设拷贝的这份叫 _value，函数中修改的都是 _value 的值，而不会影响原来的 value 值。</p>
<p><strong>按引用传递</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">o</span>) </span>&#123;
    o.value = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(o.value); <span class="hljs-comment">//2</span>
&#125;
foo(obj);
<span class="hljs-built_in">console</span>.log(obj.value) <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改变前：</p>













<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">obj, o  ----->指针地址</td><td align="center">&#123;value: 1&#125;</td></tr></tbody></table>
<p>改变后：</p>













<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">obj, o  ----->指针地址</td><td align="center">&#123;value: 2&#125;</td></tr></tbody></table>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">o</span>) </span>&#123;
    o = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(o); <span class="hljs-comment">//2</span>
&#125;
foo(obj);
<span class="hljs-built_in">console</span>.log(obj.value) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改变前：</p>













<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">obj, o  ----->指针地址</td><td align="center">&#123;value: 1&#125;</td></tr></tbody></table>
<p>改变后：</p>

















<table><thead><tr><th align="center">栈内存</th><th align="center">堆内存</th></tr></thead><tbody><tr><td align="center">obj ----->指针地址</td><td align="center">&#123;value: 2&#125;</td></tr><tr><td align="center">o:2</td><td align="center"></td></tr></tbody></table>
<p>看到这里，我其实有点疑惑，既然是按引用传递，即实参和形参指向同一块堆地址，为什么在o赋值为2后，obj.value依旧为1呢？</p>
<p>看到这里我们可以这么理解：<strong>传递对象的引用的副本</strong>，也就是假设obj对应的内存地址是0011，那么变量o在栈里面存放的也是这个地址，我们将常量2赋值给o之后，其实o在栈中存放的就不是0011，而只是常量2.</p></div>  
</div>
            