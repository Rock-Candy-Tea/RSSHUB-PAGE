
---
title: '对UIButton的addTarget方法探究'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=2419'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 01:52:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=2419'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相信做过iOS开发的人，对UIButton都不会陌生，只要用过UIButton，对这个方法都不会陌生<code>- (void)addTarget:(nullable id)target action:(SEL)action forControlEvents:(UIControlEvents)controlEvents;</code>但是这个方法究竟做了什么呢？</p>
<p>在开始本篇文章之前，有这样几个疑问?</p>
<ol start="0">
<li>当我们点击按钮的时候，到响应事件这中间是怎么的一个过程？</li>
<li>UIButton是否会持有target？</li>
<li>target是否可以为nil，若可以为nil，系统是怎么处理的？</li>
<li>action是否可以nil？</li>
</ol>
<h3 data-id="heading-0">当我们点击按钮的时候，到响应事件这中间是怎么的一个过程？</h3>
<p>   既然我们点击的时候，它能够调用我们的方法，我猜想它应该把target，action，event这些东西存储起来，以便我们点击的时候调用。于是我遍历了UIButton及它父类UIControl的实例变量及属性。在UIControl中发现了这个实例变量<code>targetActions</code>他的类型是<code>NSMutableArray</code>,<code>targetActions</code>里面放的是<code>UIControlTargetAction</code>.这个类是一个model类，只有简单的四个属性<code>_target</code>类型id，<code>_action</code>类型SEL，<code>_eventMask</code>类型unsigned long long，<code>_cancelled</code>类型bool。很明显_target,_action,_eventMask就是我们传过去的，target，action,controlEventt.</p>
<p>   这样我们应该就能猜测到。他的实现了，当我们调用<code>- (void)addTarget:(nullable id)target action:(SEL)action forControlEvents:(UIControlEvents)controlEvents;</code>,UIButton会根据我们传过去的信息来生成一个<code>UIControlTargetAction</code>对象，并把这个对象放到数组中去，当我们触摸到按钮的时候，根据event去遍历这个数组，如果event跟数组里model的eventMask相同，则<code>[UIControlTargetAction.target performSelector:UIControlTargetAction.action withObject:self]</code>当然了，这里少不了一系列的判断。</p>
<h3 data-id="heading-1">UIButton是否会持有target？</h3>
<p>   根据文档所说，button不会持有target，所说文档不会骗我们，但是我还是测试了一下,测试代码如下</p>
<pre><code class="hljs language-Person copyable" lang="Person">    [btn addTarget:person action:@selector(btnAction) forControlEvents:UIControlEventTouchUpInside];
    //Person类实现如下
    #import "Person.h"
    @implementation Person
- (void)btnAction&#123;
NSLog(@"btnAction");
&#125;
    - (void)dealloc&#123;
     NSLog(@"%@----dealloc",[self class]);
    &#125;
    @end
    输出：Person----dealloc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>btn</code>持有<code>target</code>的话<code>person</code>,就不会走<code>person</code>的<code>dealloc</code>方法</p>
<h3 data-id="heading-2">如果有相同event添加了多次会怎样</h3>
<pre><code class="copyable">[btn addTarget:self action:@selector(firstAction) forControlEvents:UIControlEventTouchUpInside];
[btn addTarget:self action:@selector(secondAction) forControlEvents:UIControlEventTouchUpInside];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我为btn的TouchUpInside事件添加了2个分别不同的action，他会按照添加action的顺序依次调用。上面的代码，当我点击btn的时候，他会先调用firstAction，再调用secondAction.由于它是找到一个调用一个，若你在firstAction方法里把secondAction对应的UIControlTargetAction对象的_eventMask的值改了，则会导致secondAction调用不了。</p>
<h3 data-id="heading-3">target是否可以为nil</h3>
<p>  答案是肯定的，可以为nil，若果target为nil并不是向nil发一个消息，而是根据响应者链往上找，若找到，则调用，否则什么也不做。</p>
<pre><code class="copyable">[btn addTarget:nil action:@selector(btnAction) forControlEvents:UIControlEventTouchUpInside];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，上面的这个代码，他会先检查btn这个类有没有实现btnAction方法，若实现就调用，否则找btn.nextResponder，再次检查是否实现，一直到AppDelegate，如果他还没实现，则就什么也不做。</p>
<h3 data-id="heading-4">action是否可以为NULL</h3>
<p>   文档上说action 不能为NULL，但是我测试发现action为NULL的时候，程序在运行的时候并不会报错。不知道是Apple添加了判断而没有更新文档，还是我的测试方法有问题，测试的代码如下</p>
<pre><code class="copyable">SEL btnAction = NULL;
[btn addTarget:self action:btnAction forControlEvents:UIControlEventTouchUpInside];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我点击btn的时候什么反应也没有。这个不知道为啥会有文档上的描述不一致。</p></div>  
</div>
            