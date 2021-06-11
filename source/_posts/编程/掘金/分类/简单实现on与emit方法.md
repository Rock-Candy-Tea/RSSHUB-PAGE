
---
title: '简单实现on与emit方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8911'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 17:43:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=8911'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第9天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h4 data-id="heading-0">定义</h4>
<p>发布—订阅模式又叫观察者模式，它定义对象间的一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都将得到通知。在javascript开发中，一般用事件模型来替代传统的发布—订阅模式。将一个系统分割成一系列相互协作的类有一个很不好的副作用，那就是需要维护相应对象间的一致性，这样会给维护、扩展和重用都带来不便。当一个对象的改变需要同时改变其他对象，而且它不知道具体有多少对象需要改变时，就可以使用订阅发布模式了。
一个抽象模型有两个方面，其中一方面依赖于另一方面，这时订阅发布模式可以将这两者封装在独立的对象中，使它们各自独立地改变和复用。订阅发布模式所做的工作其实就是在解耦合。让耦合的双方都依赖于抽象，而不是依赖于具体，从而使得各自的变化都不会影响另一边的变化。</p>
<p>我们可以实现简单的on与emit方法。代码如下：</p>
<pre><code class="copyable">class Event &#123; 
    constructor()&#123;
        this.obj = &#123;&#125;
    &#125;
    //函数接收两个参数，事件名，事件触发后的函数。subscribe函数负责将提供的函数存放到对应的事件数组中。
    this.on = (name,fn)=>&#123;
        if(!this.obj[name])&#123;
            this.obj[name] = [];
        &#125;
        this.obj[name].push(fn);
    &#125;
    //考虑到某个模块可能会触发多个事件
    this.emit = (name,val)=>&#123;
    
        if(this.obj[name])&#123;
            this.obj[name].map((fn)=>&#123;
                fn(val);
            &#125;);
        &#125;
    &#125;
    //模块还可以取消订阅。函数接收两个参数，取消订阅的事件名、对应的函数。若不传入函数，则默认清除事件对应的所有函数。
    this.off = (name,fn)=>&#123;
        if(this.obj[name])&#123;
            if(fn)&#123;
                let index = this.obj[name].indexOf(fn);
                if(index > -1)&#123;
                    this.obj[name].splice(index,1);
                &#125;           
            &#125;else&#123;
                this.obj[name].length = 0;
                //设长度为0比obj[name] = []更优，因为如果是空数组则又开辟了一个新空间，设长度为0则不必开辟新空间
            &#125;  
        &#125;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            