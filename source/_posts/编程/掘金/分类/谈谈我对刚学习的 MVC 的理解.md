
---
title: '谈谈我对刚学习的 MVC 的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6429'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 03:06:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=6429'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. MVC 三个对象是什么？分别做什么？</h1>
<ul>
<li>M：即 Model（数据模型），负责操作所有数据</li>
</ul>
<p>有以下伪代码为示例：</p>
<pre><code class="copyable">const m = &#123;
    data:&#123;数据源&#125;,
    create()&#123;增&#125;,
    delete()&#123;删&#125;,
    update(data)&#123;
        Object.assign(m.data, data) // 新数据替换旧数据
        eventBus.trigger('m:update') // eventBus触发'm:update'信息，通知 View 刷新页面
    &#125;,
    get()&#123;查&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>V： 即 View（视图），负责所有的 UI 界面</li>
</ul>
<p>有以下伪代码为示例：</p>
<pre><code class="copyable">const v = &#123;
    el: null, // 要重新渲染的元素
    html:` 显示内容的代码`,
    init(container)&#123;
        v.el = $(container)
    &#125;,
    render()&#123;
        重新渲染内容
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>C： 即 Controller（控制器），负责除了 M 和 V 以外的其他事情</li>
</ul>
<p>有以下伪代码为示例：</p>
<pre><code class="copyable">const c = &#123;
    v.init(container)&#123; 
       // 初始化 View
       // view = render(data)
    v.render(m.data.n) // 第一次渲染
    c.autoBindEvents() // 自动事件绑定
    eventBus.on('m:updated',()=>&#123;
          // eventBus 触发'm:update' ，View 重新渲染，如
          // v.render(m.data.n)
        &#125;)
    &#125;,
    events:&#123;
        // 哈希表记录
        // 如
        // 'click #add1': 'add',
        // 'click #minus1': 'minus',
    &#125;,
    add()&#123;
        // 如
        // m.update(&#123;n: m.data.n + 1&#125;)
    &#125;,
    minus()&#123;
        // 如 
        //  m.update(&#123;n: m.data.n - 1&#125;)
    &#125;,
    autoBindEvents()&#123;
        // 自动绑定事件，如
        // for(let key in c.events) &#123;
        //     const value = c[c.events[key]]
        //     const spaceIndex = key.indexOf(' ')
        //     const part1  = key.slice(0, spaceIndex)
        //     const part2 = key.slice(spaceIndex + 1)
        //     v.el.on(part1, part2, value)
        // &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2. EventBus 有哪些 API，是做什么用的？</h1>
<ul>
<li>EventBus 基本的 API 有 on（监听事件），trigger（触发事件）,off（取消监听）方法。</li>
<li>用于模块间的通讯，view 组件层面，父子组件、兄弟组件通信都可以 EventBus 处理</li>
</ul>
<pre><code class="copyable">//EventBus.js
class EventBus&#123;
    constructor()&#123;
        this._eventBus =$(window)
    &#125;
    on(eventName, fn)&#123;
        return this._eventBus.on(eventName,fn)
    &#125;
    trigger(eventName,data)&#123;
        return this._trigger.tiggger(eventName,data)
    &#125;
    off(eventName, fn)&#123;
        return this._eventBus.off(eventName,fn)
    &#125;
&#125;
export default EventBus

//new.js
import EventBus from 'EventBus.js'
const e =new EventBus()
e.on()
e.trigger()
e.off()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. 什么是表驱动编程？</h1>
<ul>
<li>表驱动法是一种编程模式，从表(哈希表)里面查找信息而不是使用逻辑语句（if…else…switch，可以减少重复代码，只将重要的信息放在表里，然后利用表来编程，与逻辑语句相比较有着更稳定的复杂度。</li>
<li>以下代码就有着相似度很高的问题</li>
</ul>
<pre><code class="copyable">bindEvents()&#123;
    v.el.on('click','#add1',()=>&#123;
        m.data.n +=1
        v.render(m.data.n)
    &#125;)
    v.el.on('click','#minus1',()=>&#123;
        m.data.n-=1
        v.render(m.data.n)
    &#125;)
    v.el.on('click','#mul2',()=>&#123;
        m.data.n*=2
        v.render(m.data.n)
    &#125;)
    v.el.on('click','#divide2',()=>&#123;
        m.data.n/=2
        v.render(m.data.n)
    &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用表驱动编程后，将代码不重复的部分提取到哈希表，代码简洁许多</li>
</ul>
<pre><code class="copyable">events:&#123;
    'click #aa1':'add',
    'click #minus1':'minus',
    'click #mul2':'mul',
    'click #divide2':'div'
&#125;,
add()&#123;
    m.update( data: &#123;n:m.data.n +1&#125;)
&#125;,
minus()&#123;
    m.update( data:&#123;n:m.data.n -1&#125;)
&#125;,
mul()&#123;
    m.update( data: &#123;n:m.data.n *2&#125;)
&#125;,
div()&#123;
    m.update(data: &#123;n:m.data.n /2&#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4. 我是如何理解模块化的</h1>
<ul>
<li>我个人理解的模块化，用最简单的话来说就是：块的内部数据与实现是私有的, 只是向外部暴露一些接口(方法)与外部其它模块通信，这可以让每个模块都独立出来。如果某个模块出了问题就不会影响别的模块，所以在模块化编程的时候可以不用太过于关注当前模块对其他模块的影响。</li>
</ul>
<p>模块化的好处</p>
<ol>
<li>避免变量污染，命名冲突</li>
<li>提高代码复用率</li>
<li>提高维护性</li>
<li>依赖关系的管理</li>
</ol></div>  
</div>
            