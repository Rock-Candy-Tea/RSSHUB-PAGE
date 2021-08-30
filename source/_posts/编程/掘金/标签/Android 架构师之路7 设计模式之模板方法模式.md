
---
title: 'Android 架构师之路7 设计模式之模板方法模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37eb0c47b992481d87171380a43b0929~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 22:08:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37eb0c47b992481d87171380a43b0929~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、模板方法模式概念</h4>
<h5 data-id="heading-1">1.1 介绍</h5>
<p>在模板模式（Template Pattern）中，一个抽象类公开定义了执行它的方法的方式/模板。它的子类可以按需要重写方法实现，但调用将以抽象类中定义的方式进行。这种类型的设计模式属于行为型模式。</p>
<h5 data-id="heading-2">1.2 定义</h5>
<p>模板方法模式:定义一个算法的骨架，将骨架中的特定步骤延迟到子类中。模板方法模式使得子类可以不改变算法的结构即可重新定义该算法的某些特定步骤</p>
<h5 data-id="heading-3">1.3 使用场景</h5>
<ul>
<li>系统需要将请求调用者和请求接收者解耦，使得调用者和接收者不直接交互。</li>
<li>系统需要在不同的时间指定请求、将请求排队（如：线程池+工作队列）和执行请求。</li>
<li>系统需要支持命令的撤销(Undo)操作和恢复(Redo)操作。</li>
<li>系统需要将一组操作组合在一起，即支持宏命令。</li>
</ul>
<h4 data-id="heading-4">2、模板方法模式UML类图</h4>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37eb0c47b992481d87171380a43b0929~tplv-k3u1fbpfcp-watermark.image" alt="模板方法模式UML类图" loading="lazy" referrerpolicy="no-referrer">
</div>
<ul>
<li><strong>抽象类（AbstractClass）</strong> ：实现了模板方法，定义了算法的骨架。</li>
<li><strong>具体类（ConcreteClass)</strong> ：实现抽象类中的抽象方法，已完成完整的算法。</li>
</ul>
<h4 data-id="heading-5">3、模板方法模式代码实现</h4>
<h5 data-id="heading-6">AbstractClass：</h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Game</span> </span>&#123;
       <span class="hljs-function"><span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initialize</span><span class="hljs-params">()</span></span>;
       <span class="hljs-function"><span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">startPlay</span><span class="hljs-params">()</span></span>;
       <span class="hljs-function"><span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">endPlay</span><span class="hljs-params">()</span></span>;

       <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">play</span><span class="hljs-params">()</span></span>&#123;
           initialize();
           startPlay();
           endPlay();
       &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">ConcreteClass：</h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KingGloryGame</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Game</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initialize</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"初始化王者荣耀游戏"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">startPlay</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"王者荣耀游戏开始"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">endPlay</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"王者荣耀游戏结束"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoLGame</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Game</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initialize</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"初始化LOL游戏"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">startPlay</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"LOL游戏开始"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">endPlay</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"LOL游戏结束"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">Client：</h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Client</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span></span>&#123;
        Game game = <span class="hljs-keyword">new</span> LoLGame();
        game.play();
        game = <span class="hljs-keyword">new</span> KingGloryGame();
        game.play();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果输出：</p>
<pre><code class="hljs language-java copyable" lang="java">初始化LOL游戏
LOL游戏开始
LOL游戏结束
初始化王者荣耀游戏
王者荣耀游戏开始
王者荣耀游戏结束
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4、模板方法模式Android中使用</h4>
<pre><code class="copyable">AsyncTask类、activity中的onCreate() 等生命周期
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">5、模式总结</h4>
<h5 data-id="heading-11">5.1 优点</h5>
<ul>
<li>封装不变部分，扩展可变部分。</li>
<li>提取公共代码，便于维护。</li>
<li>行为由父类控制，子类实现。</li>
</ul>
<h5 data-id="heading-12">5.2 缺点</h5>
<ul>
<li>每一个不同的实现都需要一个子类来实现，导致类的个数增加，使得系统更加庞大。</li>
</ul></div>  
</div>
            