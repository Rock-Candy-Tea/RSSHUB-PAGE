
---
title: '栈和队列算法题（基于JavaScript数组）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ac1584e5984f9c8f1ddd8459de0534~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 21:57:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ac1584e5984f9c8f1ddd8459de0534~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">栈和队列</h3>
<ul>
<li>基于数组</li>
</ul>
<h3 data-id="heading-1">优先级队列</h3>
<p>即由插入元素的优先级来决定它的位置，而<strong>不是</strong>按照元素进出的顺序排列的。因此元素在插入的时候，还有一个优先级数决定这个元素应该被插到哪里。应用：就比如我们生活中有时候会说女士优先、男士优先等，这些都是优先级的体现。</p>
<p>插入元素步骤：</p>
<ul>
<li>
<p>封装元素和优先级放在一起（封装一个新的构造函数）</p>
<pre><code class="copyable">function QueueElement(element, priority) &#123;
    this.element = element;
    this.priority = priority;
&#125;s
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>添加元素的时候，将新插入元素的优先级和队列中已经存在的元素优先级进行比较，获取这个元素的位置。</p>
<p>当这个队列中没有元素，或者插入的元素的优先级都比队列中的元素靠后的，直接push到队列中即可。</p>
<p><code>splice</code>是一种数组方法。<code>splice(t,v,s)</code>的<code>t: 被删除元素的起始位置</code>；<code>v: 被删除元素个数</code>； <code>s: 被插入的新元素</code></p>
<p><code>splice(i, 0, queueElement)</code>表示把<code>queueElement</code>插入到第i个元素后一位。0表示被删除元素个数为0.</p>
</li>
</ul>
<pre><code class="copyable">PriorityQueue.prototype.enqueue = function (element, priority) &#123;
    var queueElement = new QueueElement(element, priority);
    if (this.items.length == 0) &#123;
        this.items.push(queueElement);
    &#125; else &#123;
        var added = false;
        for (let i = 0; i < this.items.length; i++) &#123;
            if (queueElement.priority < this.items[i].priority) &#123;
                this.items.splice(i, 0, queueElement);
                added = true;
            &#125;
        &#125;
        if (!added) &#123;
            this.items.push(queueElement);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">算法题</h3>
<ol>
<li>
<p>击鼓传花</p>
<p>题目：n个人，从第一个人开始，数到m时这个人就被淘汰，接着下一个人从1开始数起。直到最后剩的那一个人获胜。</p>
<p>这个题目用队列的方式可以很容易的做出来。之前在洛谷刷到过这道题，那时候还没学到数据结构，现在看倒是容易许多。首先把n个人放到一个队列中，当还没有数到m时，队头元素变成队尾元素，当数到m时，队头元素被淘汰（删除），这样子循环下去，最后得到的结果就是那个获胜的元素。</p>
<pre><code class="copyable">function passGame(name, num) &#123;
    let queue = new Queue();
    for (let i = 0; i < name.length; i++) &#123;
        queue.enqueue(name[i]);
    &#125;
    while (queue.items.length > 1) &#123;
        for (let i = 0; i < num - 1; i++) &#123;
            queue.enqueue(queue.dequeue(name[i]));
        &#125;
        queue.dequeue(name[0]);
    &#125;
    let endName = queue.items[0];
    console.log(endName);
&#125;
let nameList = ['Lily', 'Mannqo', 'Ytao', 'mama']
passGame(nameList, 6);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>整数反转</p>
<p>这道题我是用了数组的方式（栈的思想），因为栈的元素是先进后出的，我这里把所给的数字转换为字符串之后一个一个压入栈中，然后再把它一个一个取出来，再转换为数字。比如把<code>1,2,3</code>分别压入栈中，此时的栈顶就是3，顺序出栈的结果就是<code>3,2,1</code>；最后再根据题目要求返回对应值。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ac1584e5984f9c8f1ddd8459de0534~tplv-k3u1fbpfcp-watermark.image" alt="整数反转.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">var reverse = function (x) &#123;
    let arr = [];
    let str = x + '';
    let str2 = '';
    for (let i = 0; i < str.length; i++) &#123;
        arr.push(str[i]);
    &#125;
    for (let i = 0; i < str.length; i++) &#123;
        str2 += arr.pop();
    &#125;
    let num = parseInt(str2);
    if (num < -Math.pow(2, 31) || num > Math.pow(2, 31) - 1) &#123;
        return 0
    &#125; else if (str[0] == '-') &#123;
        return -num;
    &#125; else &#123;
        return num;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<blockquote>
<p>望大佬们多多指教orz，孩子会好好学的好好学的...</p>
</blockquote></div>  
</div>
            