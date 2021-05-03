
---
title: '浅析 MVC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=490'
author: 掘金
comments: false
date: Sun, 02 May 2021 07:50:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=490'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">MVC 三个对象分别做什么？</h3>
<p>MVC是一种设计模式，所有的页面都可以使用 MVC来优化代码结构，MVC包括三类对象，将他们分离以提高灵活性和复用性。</p>
<p><strong>模型model</strong>：用于封装与应用程序的业务逻辑相关的数据以及对数据的处理方法，会有一个或多个视图监听此模型。一旦模型的数据发生变化，模型将通知有关的视图。</p>
<p><strong>视图view</strong>：是在屏幕上的表示，描绘的是model的当前状态。当模型的数据发生变化，视图相应地得到刷新自己的机会。</p>
<p><strong>控制器controller</strong>：定义用户界面对用户输入的响应方式，起到不同层面间的组织作用，用于控制应用程序的流程，它处理用户的行为和数据model上的改变。</p>
<h4 data-id="heading-1">伪代码</h4>
<pre><code class="copyable">const m =&#123;
  data:数据
  update()&#123;
  数据的更新
  &#125;
&#125;
const v = &#123;
   html:页面加载
   init() &#123;初始化数据&#125;
   render()&#123;
   数据发生变化后刷新视图
   &#125;
&#125;

const c = &#123;
绑定事件，响应用户操作
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码</p>
<pre><code class="copyable">import $ from 'jquery'

const eventBus = $(window)
// 数据相关都放到m
const m = &#123;
  data: &#123;
    n: parseInt(localStorage.getItem('n'))
  &#125;,
  create() &#123;&#125;,
  delete() &#123;&#125;,
  update(data) &#123;
    Object.assign(m.data, data)
    eventBus.trigger('m:updated')
    localStorage.setItem('n', m.data.n)
  &#125;,
  get() &#123;&#125;
&#125;
// 视图相关都放到v
const v = &#123;
  el: null,
  html: `
  <div>
    <div class="output">
      <span id="number">&#123;&#123;n&#125;&#125;</span>
    </div>
    <div class="actions">
      <button id="add1">+1</button>
      <button id="minus1">-1</button>
      <button id="mul2">*2</button>
      <button id="divide2">÷2</button>
    </div>
  </div>
`,
  init(container) &#123;
    v.el = $(container)
  &#125;,
  render(n) &#123;
    if (v.el.children.length !== 0) v.el.empty()
    $(v.html.replace('&#123;&#123;n&#125;&#125;', n))
      .appendTo(v.el)
  &#125;
&#125;
// 其他都放在c
const c = &#123;
  init(container) &#123;
    v.init(container)
    v.render(m.data.n) // view = render(data)
    c.autoBindEvents()
    eventBus.on('m:updated', () => &#123;
      v.render(m.data.n)
    &#125;)
  &#125;,
  events: &#123;
    'click #add1': 'add',
    'click #minus1': 'minus',
    'click #mul2': 'mul',
    'click #divide2': 'div',
  &#125;,
  add() &#123;
    m.update(&#123;n: m.data.n + 1&#125;)
  &#125;,
  minus() &#123;
    m.update(&#123;n: m.data.n - 1&#125;)
  &#125;,
  mul() &#123;
    m.update(&#123;n: m.data.n * 2&#125;)
  &#125;,
  div() &#123;
    m.update(&#123;n: m.data.n / 2&#125;)
  &#125;,
  autoBindEvents() &#123;
    for (let key in c.events) &#123;
      const value = c[c.events[key]]
      const spaceIndex = key.indexOf(' ')
      const part1 = key.slice(0, spaceIndex)
      const part2 = key.slice(spaceIndex + 1)
      v.el.on(part1, part2, value)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">EventBus 有哪些 API，是做什么用的？</h3>
<p>EventBus 主要用于对象间的通信，EventBus基本的API有on(监听事件),trigger(触发事件), off(取消监听)方法。<br></p>
<pre><code class="copyable">//伪代码
eventBus.trigger('xxx') //触发事件xxx
eventBus.on('xxx', function())  //监听到xxx 执行function()
eventBus.off('xxx')  //取消监听xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">表驱动编程是做什么的？</h3>
<p>所谓表驱动法(Table-Driven Approach),是指用直接查表的方法获取值，而不通过（if else) 逻辑判断，实现逻辑和数据的分离。事实上，凡是能通过逻辑语句来选择的事物，都可以通过查表来选择。对简单的情况而言，使用逻辑语句更为容易和直白。但随着逻辑链的越来越复杂，查表法也就愈发显得更具吸引力。</p>
<pre><code class="copyable">//代码示例如下
bindEvents()&#123;
  const pause = () => &#123;&#125;
  const play = () => &#123;&#125;
  const slow = () => &#123;&#125;
  const normal = () => &#123;&#125;
  const fast = () => &#123;&#125;
  document.querySelector('#btnPause').onclick = pause
  document.querySelector('#btnPlay').onclick = play
  document.querySelector('#btnSlow').onclick = slow
  document.querySelector('#btnNormal').onclick = normal
  document.querySelector('#btnFast').onclick = fast
&#125;

// 用表驱动法简化代码，易于扩展和重用，只需更改表数据即可
  events:&#123;
    '#btnPause':'pause',
    '#btnPlay':'play',
    '#btnSlow':'slow',
    '#btnNormal':'normal',
    '#btnFast':'fast'
  &#125;,
  bindEvents: () => &#123;
    for(let key in player.events)&#123;
      if(player.events.hasOwnProperty(key))&#123;
        document.querySelector(key).onclick = player[player.events[key]]
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">如何理解模块化？</h3>
<p>模块化就是把功能较多的整体划分成多个更细小的功能模块，每个模块间都是独立的，相互不影响，这样的代码维护起来更方便，不需要知道整体怎样，只需要知道这个模块的知识即可，复用性也更强。</p></div>  
</div>
            