
---
title: '浅析 MVC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3828'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 22:52:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=3828'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. MVC 三个对象分别做什么，给出伪代码示例</h3>
<ul>
<li>M- Model(数据模型)负责操作所有数据</li>
</ul>
<pre><code class="copyable">const m = &#123;
    data:&#123;&#125;,//数据源
    create:&#123;&#125;,//增
    delete:&#123;&#125;,//删
    update(data)&#123;//改
        Object.assign(m.data,data)//用新数据替换旧数据
        eventBus.trigger('m:update')//eventBus触发事件
    &#125;,
    get:&#123;&#125;//查
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>V-View(视图)负责所有 IU 界面</li>
</ul>
<pre><code class="copyable">const v = &#123;
    el:null，
    html：``
    init(container)&#123;
        v.el:$(container)
    &#125;，
    render()&#123;//刷新页面
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>C-Controller(控制器)负善其他</li>
</ul>
<pre><code class="copyable">const c = &#123;
    init()&#123;
        v.init()//初始化View
        v.render()
        c.autoBindEvents()
        eventBus.on('m:update',()=>&#123;v.render()&#125;//
    &#125;，
    events:&#123;&#125;,
    method()&#123;&#125;,
    autoBindEvents()&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. EventBus 有哪些 API，是做什么用的，给出伪代码示例</h3>
<p>API：</p>
<ul>
<li><code>EventBus.on()</code>//监听事件</li>
<li><code>EventBus.trigger()</code>//触发事件</li>
<li><code>EventBus.off()</code>//取消监听</li>
</ul>
<p>用于模块间的通讯， view组件层面，父子组件、兄弟组件通信都可以使EventBus处理</p>
<p>伪代码示例：</p>
<pre><code class="copyable">class EventBus &#123;
    constructor() &#123;
        this._eventBus = $(window)
    &#125;
    on(eventName, fn) &#123;
        return this._eventBus.on(eventName, fn)
    &#125;
    trigger(eventName, data) &#123;
        return this._trigger.trigger(eventName, data)
    &#125;
    off(eventName, fn) &#123;
        return this._eventBus.off(eventName, fn)
    &#125;
&#125;
export default EventBus
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 表驱动编程是做什么的</h3>
<p>表驱动方法是一种使你可以在表中查找信息，而不必用逻辑语句（if 或 case）来把他们找出来的方法。任何信息都可以通过表来挑选。在简单的情况下，逻辑语句往往更简单而且更直接。但随着逻辑链的复杂，表就变得越来越富于吸引力了。</p>
<p>例如：</p>
<pre><code class="copyable">bindEvents()&#123;
  v.el.on('click', '#add1', () => &#123;
    m.data.n += 1
    v.render(m.data.n)
  &#125;)
  v.el.on('click', '#minus1', () => &#123;
    m.data.n -= 1
    v.render(m.data.n)
  &#125;)
  v.el.on('click', '#mul2', () => &#123;
    m.data.n *= 2
    v.render(m.data.n)
  &#125;)
  v.el.on('click', '#divide2', () => &#123;
    m.data.n /= 2
    v.render(m.data.n)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 我是如何理解模块化的</h3>
<p>每一个模块都相对独立，可以使用使用不同的技术，在代码量特别多之后，更方便我们在不同的模块中找到相应的代码，对其进行操作。同时也可以使用 <code>import</code> 和 <code>export</code> 引入别的文件或者输出文件让其他文件可以引入。</p></div>  
</div>
            