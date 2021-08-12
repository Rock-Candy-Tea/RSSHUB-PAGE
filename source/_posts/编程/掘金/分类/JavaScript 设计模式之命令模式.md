
---
title: 'JavaScript 设计模式之命令模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=914'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 01:36:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=914'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<blockquote>
<p>命令模式是最简单和优雅的模式之一，命令模式中的命令指的是一个执行某些特定事情的指令。</p>
</blockquote>
<h2 data-id="heading-0">命令模式的用途</h2>
<p>命令模式最常见的应用场景是：有时候需要向某些对象发送请求，但是并不知道请求的接收者是谁，也不知道被请求的操作是什么。此时，希望用一种松耦合的方式来设计程序，是的请求发送者和请求接收者能够消除彼此之间的耦合关系。</p>
<h2 data-id="heading-1">命令模式的例子——菜单程序</h2>
<p>假设在写一个用户界面程序，该界面上至少有数十个 <code>Button</code> 按钮。因为项目比较复杂，所以我们分工给一个人负责绘制这些按钮，而另一个人负责编写点击按钮后的具体行为，这些行为都被封装在对象里。</p>
<p>那么，对于绘制按钮的程序员来说，他完全不知道某个按钮未来将用来做什么，他只知道点击这个按钮会发生某些事情。当完成这个按钮的绘制之后，应该如何给它绑定 <code>onclick</code> 事件呢。</p>
<p>很明显，在这里运用命令模式的理由是：点击了按钮之后，必须向某些负责具体行为的对象发送请求，这些对象就是请求的接收者。但是目前并不知道接收者是什么对象，也不知道接收者究竟会做什么。此时就需要借助命令对象的帮助，以便解开按钮和负责具体行为对象之间的耦合。</p>
<p><strong>设计模式的主题总是把不变的事物和变化的事物分离开来。</strong> 按下按钮之后会发生一些事情是不变的，而具体发生什么事情是可变的。通过 command 对象的帮助，未来可以很轻易地改变这种关联，因此也可以在未来再次改变按钮的行为。</p>
<p>先在页面中绘制按钮：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button1"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button2"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button3"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> button1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"button1"</span>);
  <span class="hljs-keyword">var</span> button2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"button2"</span>);
  <span class="hljs-keyword">var</span> button3 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"button3"</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来定义 <code>setCommand</code> 函数，<code>setCommand</code> 函数负责往按钮上面安装命令。我们可以确定的是，点击按钮会执行某个 <code>command</code> 命令，执行命令的动作被约定为调用 <code>command</code> 对象的 <code>execute()</code> 方法。负责绘制按钮的程序员只需要预留好安装命令的接口，<code>command</code> 对象知道如何和正确的对象沟通：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> setCommand = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">button, command</span>) </span>&#123;
  button.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    command.execute()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮之后具体行为包括刷新菜单界面、增加子菜单和删除子菜单等，这几个功能被分布在 <code>MenuBar</code> 和 <code>SubMenu</code> 这两个对象中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> MenuBar = &#123;
  <span class="hljs-attr">refresh</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'刷新菜单目录'</span>)
  &#125;
&#125;
<span class="hljs-keyword">var</span> SubMenu = &#123;
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'增加子菜单'</span>)
  &#125;,
  <span class="hljs-attr">del</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'删除子菜单'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在让 <code>button</code> 变得有用起来之前，要先把这些行为都封装在命令类中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> RefreshMenuBarCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver = receiver;
&#125;;
RefreshMenuBarCommand.prototype.execute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.refresh();
&#125;;

<span class="hljs-keyword">var</span> AddSubMenuCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver = receiver;
&#125;;
AddSubMenuCommand.prototype.execute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.add();
&#125;;

<span class="hljs-keyword">var</span> DelSubMenuCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver = receiver;
&#125;;
DelSubMenuCommand.prototype.execute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.del();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后就是把命令接收者传入到 <code>command</code> 对象中，并且把 <code>command</code> 对象安装到 <code>button</code> 上面：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> refreshMenuBarCommand = <span class="hljs-keyword">new</span> RefreshMenuBarCommand(MenuBar);
<span class="hljs-keyword">var</span> addSubMenuCommand = <span class="hljs-keyword">new</span> AddSubMenuCommand(SubMenu);
<span class="hljs-keyword">var</span> delSubMenuCommand = <span class="hljs-keyword">new</span> DelSubMenuCommand(SubMenu);

setCommand(button1, refreshMenuBarCommand);
setCommand(button2, addSubMenuCommand);
setCommand(button3, delSubMenuCommand);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述是一个很简单的命令模式示例，但是从中可以看到我们是如何把请求发送者和请求接收者解耦开的。</p>
<h2 data-id="heading-2">JavaScript 中的命令模式</h2>
<p>从上述看起来，所谓的命令模式，看起来就是给对象的某个方法取了 <code>execute</code> 的名字。引入 <code>command</code> 对象和 <code>receiver</code> 写着两个无中生有的角色无非是把简单的事情复杂化了，即使不用什么模式，用下面寥寥几行代码就可以实现相同的功能：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> bindClick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">button, func</span>) </span>&#123;
  button.onclick = func;
&#125;;
<span class="hljs-keyword">var</span> MenuBar = &#123;
  <span class="hljs-attr">refresh</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"刷新菜单界面"</span>);
  &#125;,
&#125;;
<span class="hljs-keyword">var</span> SubMenu = &#123;
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"增加子菜单"</span>);
  &#125;,
  <span class="hljs-attr">del</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"删除子菜单"</span>);
  &#125;,
&#125;;
bindClick(button1, MenuBar.refresh);
bindClick(button2, SubMenu.add);
bindClick(button3, SubMenu.del);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种说法是正确的，上一节的示例代码是模拟传统面向对象语言的命令模式实现。命令模式将过程式的请求调用封装在 <code>command</code> 对象的 <code>execute</code> 方法里，通过封装方法调用，可以把运算块包装成形。<code>command</code> 对象可以被四处传递，所以在调用命令的时候，客户不需要关心事情是如何进行的。</p>
<p><strong>命令模式的由来，其实是回调（callback）函数的一个面向对象的替代品。</strong></p>
<p>在 <code>JavaScript</code> 中运算块不一定要封装在 <code>command.execute</code> 方法中，也可以封装在普通函数中。即使我们依然需要请求“接收者”，那也未必使用面向对象的方式，闭包可以完成同样的功能。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> setCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">button, func</span>) </span>&#123;
  button.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    func();
  &#125;;
&#125;;
<span class="hljs-keyword">var</span> MenuBar = &#123;
  <span class="hljs-attr">refresh</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"刷新菜单界面"</span>);
  &#125;,
&#125;;
<span class="hljs-keyword">var</span> RefreshMenuBarCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    receiver.refresh();
  &#125;;
&#125;;
<span class="hljs-keyword">var</span> refreshMenuBarCommand = RefreshMenuBarCommand(MenuBar);
setCommand(button1, refreshMenuBarCommand);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果想更明确地表达当前正在使用命令模式，或者除了执行命令之外，将来有可能还要提供撤销命令等操作。那我们最好还是把执行函数改为调用 <code>execute</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> RefreshMenuBarCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      receiver.refresh();
    &#125;,
  &#125;;
&#125;;
<span class="hljs-keyword">var</span> setCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">button, command</span>) </span>&#123;
  button.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    command.execute();
  &#125;;
&#125;;
<span class="hljs-keyword">var</span> refreshMenuBarCommand = RefreshMenuBarCommand(MenuBar);
setCommand(button1, refreshMenuBarCommand);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">撤销命令</h2>
<p>命令模式的作用不仅是封装运算块，而且可以很方便地给命令对象增加撤销操作。</p>
<p>之前写过的一个 <code>Animate</code> 类来编写一个动画，这个动画的表现是让页面上的小球移动到水平方向的某个位置。现在页面中有一个 <code>input</code> 文本框和一个 <code>button</code> 按钮，文本框中可以输入一些数字，表示小球移动后的水平位置，小球在用户点击按钮后立刻开始移动，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
  <span class="hljs-attr">id</span>=<span class="hljs-string">"ball"</span>
  <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; background: #000; width: 50px; height: 50px"</span>
></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
输入小球移动后的位置:<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"pos"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"moveBtn"</span>></span>开始移动<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> ball = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"ball"</span>);
  <span class="hljs-keyword">var</span> pos = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"pos"</span>);
  <span class="hljs-keyword">var</span> moveBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"moveBtn"</span>);
  moveBtn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> animate = <span class="hljs-keyword">new</span> Animate(ball);
    animate.start(<span class="hljs-string">"left"</span>, pos.value, <span class="hljs-number">1000</span>, <span class="hljs-string">"strongEaseOut"</span>);
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果文本框输入200，然后点击 <code>moveBtn</code> 按钮，可以看到小球顺利地移动到水平方向 200px 的位置。现在我们需要一个方法让小球还原到开始移动之前的位置。当然也可以在文本框中再次输入 -200，并且点击 moveBtn 按钮，这也是一个办法，但是很笨拙。页面上最好有一个撤销按钮，点击撤销后，小球便能回到上一次的位置。</p>
<p>在页面中增加撤销按钮之前，先把目前的代码改为用命令模式实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> ball = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"ball"</span>);
<span class="hljs-keyword">var</span> pos = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"pos"</span>);
<span class="hljs-keyword">var</span> moveBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"moveBtn"</span>);
<span class="hljs-keyword">var</span> MoveCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver, pos</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver = receiver;
  <span class="hljs-built_in">this</span>.pos = pos;
&#125;;
MoveCommand.prototype.execute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.start(<span class="hljs-string">"left"</span>, <span class="hljs-built_in">this</span>.pos, <span class="hljs-number">1000</span>, <span class="hljs-string">"strongEaseOut"</span>);
&#125;;
<span class="hljs-keyword">var</span> moveCommand;
moveBtn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> animate = <span class="hljs-keyword">new</span> Animate(ball);
  moveCommand = <span class="hljs-keyword">new</span> MoveCommand(animate, pos.value);
  moveCommand.execute();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来增加撤销按钮：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
  <span class="hljs-attr">id</span>=<span class="hljs-string">"ball"</span>
  <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; background: #000; width: 50px; height: 50px"</span>
></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
输入小球移动后的位置:<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"pos"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"moveBtn"</span>></span>开始移动<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cancelBtn"</span>></span>cancel<span class="hljs-tag"></<span class="hljs-name">cancel</span>></span> <span class="hljs-comment"><!--增加取消按钮--></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>撤销操作的实现一般是给命令对象增加一个名为 <code>unexecude</code> 或者 <code>undo</code> 的方法，在该方法里执行 <code>execute</code> 的反向操作。在 <code>command.execute</code> 方法让小球开始真正运动之前，需要先记录小球的当前位置，在 <code>unexecude</code> 或者 <code>undo</code> 操作中，再让小球回到刚刚记录下的位置，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">var</span> ball = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'ball'</span>);
<span class="hljs-keyword">var</span> pos = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'pos'</span>);
<span class="hljs-keyword">var</span> moveBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'moveBtn'</span>);
<span class="hljs-keyword">var</span> cancelBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'cancelBtn'</span>);
<span class="hljs-keyword">var</span> MoveCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver, pos</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver = receiver;
  <span class="hljs-built_in">this</span>.pos = pos;
  <span class="hljs-built_in">this</span>.oldPos = <span class="hljs-literal">null</span>;
&#125;;

MoveCommand.prototype.execute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.start(<span class="hljs-string">'left'</span>, <span class="hljs-built_in">this</span>.pos, <span class="hljs-number">1000</span>, <span class="hljs-string">'strongEaseOut'</span>);
  <span class="hljs-built_in">this</span>.oldPos = <span class="hljs-built_in">this</span>.receiver.dom.getBoundingClientRect()[<span class="hljs-built_in">this</span>.receiver.propertyName];  <span class="hljs-comment">// 记录小球开始移动前的位置</span>
&#125;;

MoveCommand.prototype.undo = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.receiver.start(<span class="hljs-string">'left'</span>, <span class="hljs-built_in">this</span>.oldPos, <span class="hljs-number">1000</span>, <span class="hljs-string">'strongEaseOut'</span>); <span class="hljs-comment">// 回到小球移动前记录的位置</span>
&#125;;

<span class="hljs-keyword">var</span> moveCommand;
moveBtn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> animate = <span class="hljs-keyword">new</span> Animate(ball);
  moveCommand = <span class="hljs-keyword">new</span> MoveCommand(animate, pos.value); moveCommand.execute();
&#125;;
cancelBtn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  moveCommand.undo();<span class="hljs-comment">// 撤销命令</span>
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在通过命令模式轻松地实现了撤销功能。如果用普通方法调用来实现，也许需要每次都手工记录小球的运动轨迹，才能让它还原到之前的位置。而命令模式中小球的原始位置在小球开始移动前已经作为 <code>command</code> 对象的属性被保存起来，所以只需要再提供一个 <code>undo</code> 方法，并且在 <code>undo</code> 方法中让小球会到刚刚记录的原始位置就可以了。</p>
<p>撤销是命令模式里一个非常有用的功能，同样，撤销命令还可以用于实现文本编辑器的 <code>Ctrl+Z</code> 功能。</p>
<h2 data-id="heading-4">宏命令</h2>
<p>宏命令是一组命令的集合，通过执行宏命令的方式，可以一次执行一批命令。接下来，来逐步创建一个宏命令。</p>
<h3 data-id="heading-5">Step1：创建好各种 Command</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> closeDoorCommand = &#123;
  <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'关门'</span>);
  &#125;
&#125;;
<span class="hljs-keyword">var</span> openPcCommand = &#123;
  <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开电脑'</span>);
  &#125;
&#125;;
<span class="hljs-keyword">var</span> openQQCommand = &#123;
  <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'登录 QQ'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Step2：定义宏命令 MacroCommand</h3>
<p><code>macroCommand.add</code> 方法表示把子命令添加进宏命令对象，当调用宏命令对象的 <code>execute</code> 方法时，会迭代这一组子命令对象，并且依次执行它们的 <code>execute</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> MacroCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">commandsList</span>: [],
    <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">command</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.commandsList.push(command);
    &#125;,
    <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, command; command = <span class="hljs-built_in">this</span>.commandsList[i++];) &#123;
        command.execute();
      &#125;
    &#125;
  &#125;
&#125;;

<span class="hljs-keyword">var</span> macroCommand = MacroCommand();
macroCommand.add(closeDoorCommand);
macroCommand.add(openPcCommand);
macroCommand.add(openQQCommand);
macroCommand.execute();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以为宏命令添加撤销功能，跟 <code>macroCommand.execute</code> 类似，当调用 <code>macroCommand.undo</code> 方法时，宏命令里包含的所有子命令对象要依次执行各自的 <code>undo</code> 操作。</p>
<h2 data-id="heading-7">智能命令与傻瓜命令</h2>
<p>上述的 <code>closeDoorCommand</code> 中没有包含任何 <code>receiver</code> 的信息，它本身就包揽了执行请求的行为，这跟我们之前看到的命令对象都包含了一个 <code>receiver</code> 是矛盾的。</p>
<p>一般来说，命令模式都会在 <code>command</code> 对象中保存一个接收者来负责真正执行客户的请求，这种情况下命令对象是“傻瓜式”的，它只负责把客户的请求转交给执行者来执行，这种模式的好处是<strong>请求发起者和请求接收者之间尽可能地得到了解耦</strong>。</p>
<p>但是我们也可以定义一些更“聪明”的命令对象，“聪明”的命令对象可以直接实现请求，这样一来就不再需要接收者的存在，这种“聪明”的命令对象也叫作智能命令。没有接收者的智能命令，退化到和策略模式非常相近，从代码结构上已经无法分辨它们，能分辨的只有它们意图的不同。策略模式指向的问题域更小，所有策略对象的目标总是一致的，它们只是达到这个目标的不同手段，它们的内部实现是针对“算法”而言的。而智能命令模式指向的问题域更广，<code>command</code> 对象解决的目标更具发散性。命令模式还可以完成撤销、排队等功能。</p>
<h2 data-id="heading-8">最后说一句</h2>
<p>如果这篇文章对您有所帮助，或者有所启发的话，帮忙点赞关注一下，您的支持是我坚持写作最大的动力，多谢支持。</p></div>  
</div>
            