
---
title: 'Android 架构师之路10 设计模式之责任链模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b83895f6a724166b0e55e638eb09f90~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:08:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b83895f6a724166b0e55e638eb09f90~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、 责任链模式概念</h4>
<h5 data-id="heading-1">1.1 介绍</h5>
<p>客户端发出一个请求，链上的对象都有机会来处理这一请求，而客户端不需要知道谁是具体的处理对象。这样就实现了请求者和接受者之间的解耦，并且在客户端可以实现动态的组合职责链。使编程更有灵活性。</p>
<h5 data-id="heading-2">1.2 定义</h5>
<p>使多个对象都有机会处理请求，从而避免了请求的发送者和接收者之间的耦合关系。将这些对象形成一条链，并沿着这条链传递该请求，直到有对象处理它为止。其过程实际上是一个<strong>递归调用</strong>。</p>
<h5 data-id="heading-3">1.3 使用场景</h5>
<ul>
<li>有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定。。</li>
<li>在请求处理者不明确的情况下向多个对象中的一个提交请求。</li>
<li>需要动态指定处理一个请求的对象集合。</li>
</ul>
<h4 data-id="heading-4">2、责任链模式UML类图</h4>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b83895f6a724166b0e55e638eb09f90~tplv-k3u1fbpfcp-watermark.image" alt="责任链模式UML类图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-5">角色：</h5>
<ul>
<li><strong>Handler：</strong> 定义职责接口，通常在内部定义处理请求的方法，可以在这里实现后继链。</li>
<li><strong>ConcreteHandler：</strong> 实际的职责类，在这里个类里面，实现在它职责范围内的请求处理，如果不处理，就继续转发请求给后继者。</li>
<li><strong>Client：</strong> 客户端，组装职责链，向链上的具体对象提交请求。</li>
</ul>
<h6 data-id="heading-6">图中最关键的点就是：那条从Handler出发又指向自己的线，它就是实现链式调用的关键。</h6>
<h4 data-id="heading-7">3、责任链模式简单实现</h4>
<h5 data-id="heading-8">Handler</h5>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 抽象的处理类
 * Created by Administrator on 2018/1/25.
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span>  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Handler</span> </span>&#123;

    <span class="hljs-keyword">public</span> Handler nextHandler;

    <span class="hljs-comment">/**
     *
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handRequest</span><span class="hljs-params">(AbstractRequest request)</span></span>&#123;
     <span class="hljs-keyword">if</span>(request.getRequestLevel()==getHandlerLevel())&#123;
         handle(request);
     &#125;<span class="hljs-keyword">else</span> &#123;
         <span class="hljs-keyword">if</span>(nextHandler!=<span class="hljs-keyword">null</span>)&#123;
             nextHandler.handRequest(request);
         &#125;<span class="hljs-keyword">else</span> &#123;
             System.out.println(<span class="hljs-string">"----> 所有处理对象 都不能处理 "</span> );
         &#125;
     &#125;
    &#125;
    <span class="hljs-comment">/**
     * 具体的处理方法，给子类实现
     * <span class="hljs-doctag">@param</span> request
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(AbstractRequest request)</span></span>;

    <span class="hljs-comment">/**
     * 能够处理请求的级别
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">int</span>  <span class="hljs-title">getHandlerLevel</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">ConcreteHandler</h5>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 具体处理者
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Handler1</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Handler</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(AbstractRequest request)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"handle1---->处理了对象"</span> + request.getRequestLevel());
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getHandlerLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Handler2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Handler</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(AbstractRequest request)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"handle2---->处理了对象"</span> + request.getRequestLevel());
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getHandlerLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
    &#125;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Handler3</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Handler</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(AbstractRequest request)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"handle3---->处理了对象"</span> + request.getRequestLevel());
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getHandlerLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
    &#125;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Handler4</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Handler</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(AbstractRequest request)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"handle4---->处理了对象"</span> + request.getRequestLevel());
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getHandlerLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">4</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">处理对象Request</h5>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbstractRequest</span> </span>&#123;
    <span class="hljs-keyword">private</span> Object object;
    <span class="hljs-function"><span class="hljs-keyword">public</span>  Object <span class="hljs-title">getContent</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">return</span> object;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getRequestLevel</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Request1</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbstractRequest</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getRequestLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Request2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbstractRequest</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getRequestLevel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">Client</h5>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Client</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span></span>&#123;
        Handler handler1 = <span class="hljs-keyword">new</span> Handler1();
        Handler handler2 = <span class="hljs-keyword">new</span> Handler2();
        Handler handler3 = <span class="hljs-keyword">new</span> Handler3();
        Handler handler4 = <span class="hljs-keyword">new</span> Handler4();

        <span class="hljs-comment">//拼装成链子</span>
        handler1.nextHandler = handler2;
        handler2.nextHandler = handler3;
        handler3.nextHandler = handler4;

        AbstractRequest request = <span class="hljs-keyword">new</span> Request1();
        <span class="hljs-comment">//一定要将请求对象，丢给第一个处理者</span>
        handler1.handRequest(request);

        AbstractRequest request2 = <span class="hljs-keyword">new</span> Request2();
        <span class="hljs-comment">//handler1 不处理 交给handler2处理</span>
        handler1.handRequest(request2);


    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">运行结果</h5>
<hr>
<pre><code class="copyable">handle1---->处理了对象1
handle2---->处理了对象2
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>对于责任链来说，一个请求最终只有两种情况：一是被某个处理对象处理，另一个是所有的对象均为对其处理。 对于前一种情况，我们称该对象为纯的责任链，对于后一种情况我们称为不纯的责任链，在实际应用中，我们所见的责任链模式大多为不纯的责任链模式。</p>
</blockquote>
<h4 data-id="heading-13">4、责任链模式在Android系统中</h4>
<h5 data-id="heading-14">4.1 View事件的分发处理</h5>
<p>ViewGroup事件投递的递归调用就类似于一条责任链，一旦其寻找到责任者，那么将由责任者持有并消费掉该次事件，具体体现在View的onTouchEvent方法中返回值的设置，如果返回false，那么意味着当前的View不会是该次的责任人，将不会对其持有；如果返回true，此时View会持有该事件并不再向外传递。</p>
<h5 data-id="heading-15">4.2 Broadcast广播机制</h5>
<h4 data-id="heading-16">5、总结</h4>
<p>对于责任链中的一个处理者对象，有两个行为。一是处理请求，二是将请求传递到下一节点，不允许某个处理者对象在处理了请求后又将请求传送给上一个节点的情况。</p>
<p>对于一条责任链来说，一个请求最终只有两种情况。一是被某个处理对象所处理，另一个是所有对象均未对其处理，对于前一种情况我们称为纯的责任链模式，后一种为不纯的责任链。实际中大多为不纯的责任链。</p>
<h5 data-id="heading-17">优点：</h5>
<p>职责链模式的最主要功能就是：动态组合，请求者和接受者解耦。</p>
<ul>
<li>请求者和接受者松散耦合：请求者不需要知道接受者，也不需要知道如何处理。每个职责对象只负责自己的职责范围，其他的交给后继者。各个组件间完全解耦。</li>
<li>动态组合职责：职责链模式会把功能分散到单独的职责对象中，然后在使用时动态的组合形成链，从而可以灵活的分配职责对象，也可以灵活的添加改变对象职责。</li>
</ul>
<h5 data-id="heading-18">缺点：</h5>
<ul>
<li>产生很多细粒度的对象：因为功能处理都分散到了单独的职责对象中，每个对象功能单一，要把整个流程处理完，需要很多的职责对象，会产生大量的细粒度职责对象。</li>
<li>不一定能处理：每个职责对象都只负责自己的部分，这样就可以出现某个请求，即使把整个链走完，都没有职责对象处理它。这就需要提供默认处理，并且注意构造链的有效性。</li>
</ul></div>  
</div>
            