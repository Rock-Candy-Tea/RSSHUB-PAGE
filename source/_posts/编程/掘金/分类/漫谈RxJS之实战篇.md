
---
title: '漫谈RxJS之实战篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9533'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 19:27:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=9533'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上篇文章我们谈到了一些基础概念，本篇文章我们结合实际案例来继续探索RxJS。</p>
<h2 data-id="heading-0">带来了什么新问题？</h2>
<p>不得不说，Reactive Extensions（Rx）是一种非常棒的编码模式，不过我们得结合实际的业务场景做具体分析。</p>
<ol>
<li>团队内的成员是否具备高度抽象思维，因为这是一种函数式、响应式编程范式，团队成员是否可以快速学习进入开发？</li>
<li>RxJS最擅长处理的是异步事件，那么我们的业务场景是否真的有这么复杂吗？</li>
<li>RxJS的代码是高度抽象的，抽象的代码是不如命令式代码易读，这点无可厚非，那么我们该如何组织我们的业务代码？</li>
</ol>
<h3 data-id="heading-1">函数式编程范式</h3>
<p>这里顺带提一下<code>函数式</code>编程范式，首先，这是一种有约束的编程范式：</p>
<ol>
<li>声明式(Declarative)</li>
</ol>
<p>声明式，与之对应的是命令式，我们可以看下代码有何不同：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-comment">// 命令式</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-built_in">console</span>.log(arr[i])
&#125;

<span class="hljs-comment">// 声明式</span>
arr.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不难发现，使用声明式，代码简洁很多，看不到<code>for</code>了，也没有了额外的变量声明。</p>
<ol start="2">
<li>纯函数(Pure Function)</li>
</ol>
<p>函数的调用不会有额外的副作用（IO操作、DOM操作、网络请求等），每次的输入都有唯一确认的输出。</p>
<ol start="3">
<li>数据不可变性(Immutability)</li>
</ol>
<p>不改变源数据，举个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-comment">// 改变了源数据</span>
arr.push(<span class="hljs-number">6</span>)

<span class="hljs-comment">// 添加了新元素，但并没有改变原始数据，符合数据不可变性原则</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">push2</span>(<span class="hljs-params">source, item</span>) </span>&#123;
    <span class="hljs-keyword">return</span> [...source, item]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">结合实际业务场景</h2>
<p>这也是我最近做的例子，个人觉得结合RxJS会比较合适，就是IM聊天会话页。</p>
<p>我们先来梳理一下逻辑：</p>
<p>事件：</p>
<ol>
<li>通过HTTP GET拉取历史会话列表；</li>
<li>通过websocket协议实时接收消息；</li>
<li>输入事件；</li>
<li>发送内容事件；</li>
<li>点击内容事件（如图片预览、视频播放、语音播放等）;</li>
</ol>
<p>我们结合下UI交互，再组织下逻辑层，不难发现：</p>
<ol>
<li>
<p>对于【聊天内容显示区域】，很明显是订阅者，订阅者的特点是什么？上文已提过：<code>订阅者只负责接收到通知后完成自身的业务逻辑，而并不关心消息的来源</code>。</p>
</li>
<li>
<p>发布者有哪些？</p>
<ul>
<li>通过websocket推送的消息（异步事件）</li>
<li>通过HTTP GET拉取的消息（异步事件）</li>
<li>用户点击发送的消息（同步事件）</li>
</ul>
</li>
</ol>
<p>一个订阅者支持订阅多个事件流吗？RxJS当然支持，我们可以通过合并事件流、转化事件流等手段，来达到我们的目的。</p>
<p>这里代码就不贴了，感兴趣的同学可以按上述思路实践一下。</p>
<h2 data-id="heading-3">小结</h2>
<p>本文还有很多RxJS的概念没有介绍到，比如：</p>
<ul>
<li>Hot Observable和Cold Observable用于解决存在多个订阅者，有人会迟到的问题</li>
<li>经典的弹珠图表示法，让我们可以清晰的看到事件的流向</li>
<li>多播，用于处理一个事件流存在多个订阅者的问题</li>
<li>异常处理，上游的数据出错了如何处理</li>
<li>...</li>
</ul>
<p>如果大家有感兴趣的点，也欢迎随时讨论。</p></div>  
</div>
            