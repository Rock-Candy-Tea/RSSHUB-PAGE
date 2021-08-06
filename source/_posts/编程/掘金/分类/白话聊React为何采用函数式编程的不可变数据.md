
---
title: '白话聊React为何采用函数式编程的不可变数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=764'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:20:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=764'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>大家好，今天来聊一下<code>React</code>采用函数式编程的理念：不可变数据。</p>
<p>看到标题的你不用担心，你可能在顾虑需要函数式编程的知识，完全不需要，今天我们就0基础聊聊什么是不可变数据？<code>React</code>采用这种方式有什么好处？</p>
<h2 data-id="heading-1">例子</h2>
<p><code>React</code>采用函数式编程的不可变数据特性。</p>
<p>而在<code>React</code>中不可变值的意思就是：始终保持<code>state</code>的原值不变。</p>
<p>不要直接修改<code>state</code>，遇到数组或者对象，采用<code>copy</code>一份出去做改变。</p>
<p>举个简单的例子：</p>
<h3 data-id="heading-2">基本类型</h3>
<p>错误的做法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.state.count++
<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>:<span class="hljs-built_in">this</span>.state.count
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正确的做法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>:<span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">引用类型</h3>
<p>错误的做法：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">this</span>.state.obj1.a = <span class="hljs-number">100</span>
<span class="hljs-built_in">this</span>.state.obj2.a = <span class="hljs-number">100</span>
<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">obj1</span>: <span class="hljs-built_in">this</span>.state.obj1,
    <span class="hljs-attr">obj2</span>: <span class="hljs-built_in">this</span>.state.obj2
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正确的做法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">obj1</span>: <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, <span class="hljs-built_in">this</span>.state.obj1, &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">100</span>&#125;),
    <span class="hljs-attr">obj2</span>: &#123;...this.state.obj2, <span class="hljs-attr">a</span>: <span class="hljs-number">100</span>&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">函数式编程不可变值的优势</h2>
<p>我们先聊聊函数式编程中不可变值的好处。</p>
<h3 data-id="heading-5">减少bug</h3>
<p>好比我们用<code>const</code>定义一个变量，如果你要改变这个变量，你需要把变量<code>copy</code>出去修改。
这样的做法，可以让你的代码少非常多的<code>bug</code>。</p>
<h3 data-id="heading-6">生成简单的状态管理便于维护</h3>
<p>因为，程序中的状态是非常不好维护的，特别是在并发的情况下更不好维护。
试想一下：如果你的代码有一个复杂的状态，当以后别人改你代码的时候，是很容易出<code>bug</code>的。</p>
<h2 data-id="heading-7">React中采用函数式编程的不可变值</h2>
<p>我们再来看看<code>React</code>中采用函数式编程</p>
<h3 data-id="heading-8">性能优化</h3>
<p>在生命周期 <strong><code>shouldComponentUpdate</code></strong> 中，<code>React</code>会对新旧<code>state</code>进行比较，如果直接修改state去用于其他变量的计算，而实际上<code>state</code>并不需要修改，则会导致怪异的更新以及没必要的更新，因此采用这种方式是非常巧妙，且效率非常的高。</p>
<h3 data-id="heading-9">可追踪修改痕迹，便于排错</h3>
<p>使用<code>this.setState</code>的方式进行修改<code>state</code>的值，相当于开了一个改变值的口子，所有的修改都会走这样的口子，相比于直接修改，这样的控制力更强，能够有效地记录与追踪每个<code>state</code>的改变，对排查bug十分有帮助。</p>
<h2 data-id="heading-10">结尾</h2>
<p>关于<code>React</code>与<code>函数式编程</code>你有什么观点或者想法，欢迎在评论区告诉我。</p></div>  
</div>
            