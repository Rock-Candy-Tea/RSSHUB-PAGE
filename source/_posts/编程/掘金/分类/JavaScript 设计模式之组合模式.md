
---
title: 'JavaScript 设计模式之组合模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152db06ba2ff476ea23c97a3bef660ef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 01:55:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152db06ba2ff476ea23c97a3bef660ef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<blockquote>
<p>在程序设计中，有一些和“事物是由相似的子事物构成”类似的思想。组合模式就是用小的子对象来构建更大的对象，而这些小的子对象本身也许是由更小的“孙对象”构成的。</p>
</blockquote>
<h2 data-id="heading-0">回顾宏命令</h2>
<p>在命令模式中提到了宏命令的结构和作用。宏命令对象包含了一组具体的子命令对象，不管是宏命令对象还是子命令对象，都有一个 <code>execute</code> 方法负责执行命令。现在回顾一下命令模式中的宏命令代码：</p>
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

<span class="hljs-keyword">var</span> MacroCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
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
<p>我们可以看到宏命令中包含了一组子命令，它们组成了一个树形结构，尽管是一颗结构很简单的树。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152db06ba2ff476ea23c97a3bef660ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
其中，<code>macroCommand</code> 被称为组合对象，<code>closeDoorCommand</code>、<code>openPcCommand</code>、<code>openQQCommand</code> 都是叶对象。在 <code>macroCommand</code> 的 <code>execute</code> 方法里，并不执行真正的操作，而是遍历它所包含的叶对象，把真正的 <code>execute</code> 请求委托给这些叶对象。</p>
<p><code>macroCommand</code> 表现得像一个命令，但它实际上只是一组真正命令的“代理”。并非真正的代理，虽然结构上相似，但是 <code>macroCommand</code> 只负责传递请求给叶对象，它的目的不在于控制叶对象的访问。</p>
<h2 data-id="heading-1">组合模式的用途</h2>
<h3 data-id="heading-2">1 表示树形结构</h3>
<p>上述例子，可以很明显看出组合模式的一个优点：提供了一种遍历树形结构的方案，通过调用组合对象的 <code>execute</code> 方法，程序会递归调用组合对象下面的叶对象的 <code>execute</code> 方法。组合模式可以非常方便地描述对象部分——整体层次结构。</p>
<h3 data-id="heading-3">2 利用对象多态性统一对待组合对象和单个对象</h3>
<p>利用对象的多态性表现，可以使客户端忽略组合对象和单个对象的不同。在组合模式中，客户将统一地使用组合结构中的所有对象，而不需要关心它究竟是组合对象还是单个对象。</p>
<h2 data-id="heading-4">请求在树中传递的过程</h2>
<p>在组合模式中，请求在树中传递的过程总是遵循一种逻辑。</p>
<p>以宏命令为例，请求从树最顶端的对象往下传递，如果当前处理请求的对象是叶对象（普通子命令），叶对象自身会对请求作出相应的处理；如果当前处理请求的对象是组合对象（宏命令），组合对象则会遍历它树下的子节点，将请求继续传递给这些子节点。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc4d0f4b0f4414d9cb7e07a41b20763~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>请求从上到下沿着树进行传递，直到树的尽头。作为用户，只需要关心树最顶层的组合对象，只需要请求这个组合对象，请求便会沿着树往下传递，一次到达所有的叶对象。</p>
<h2 data-id="heading-5">更强大的宏命令</h2>
<p>目前的 <code>macroCommand</code> 包括了关门、开电脑和登录QQ这3个命令，现在我们需要一个“超级万能遥控器”，可以控制家里所有的电器，这个遥控器拥有以下功能：</p>
<ul>
<li>打开空调</li>
<li>打开电视和音响</li>
<li>关门、开电脑和登录QQ</li>
</ul>
<p>首先，在节点中放置一个 <code>button</code> 表示这个超级万能遥控器。</p>
<pre><code class="hljs language-js copyable" lang="js"><button id=button>按我</button>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> MacroCommand = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
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

  <span class="hljs-keyword">var</span> openAcCommend = &#123;
    <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'打开空调'</span>);
    &#125;
  &#125;

  <span class="hljs-comment">// 电视和音响一起打开</span>
  <span class="hljs-keyword">var</span> openTvCommand = &#123;
    <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'打开电视'</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">var</span> openSoundCommand = &#123;
    <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'打开音响'</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">var</span> macroCommand1 = MacroCommand()
  macroCommand1.add(openTvCommand)
  macroCommand1.add(openSoundCommand)

  <span class="hljs-comment">// 关门、开电脑、登QQ的命令</span>
  <span class="hljs-keyword">var</span> closeDoorCommand = &#123;
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
  <span class="hljs-keyword">var</span> macroCommand2 = MacroCommand();
  macroCommand2.add(closeDoorCommand);
  macroCommand2.add(openPcCommand);
  macroCommand2.add(openQQCommand);

  <span class="hljs-comment">// 所有命令组合成一个超级命令</span>
  <span class="hljs-keyword">var</span> macroCommand = MacroCommand();
  macroCommand.add(openAcCommend)
  macroCommand.add(macroCommand1)
  macroCommand.add(macroCommand2)

  <span class="hljs-comment">// 给超级遥控器绑定命令</span>
  <span class="hljs-keyword">var</span> setCommand = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">command</span>) </span>&#123;
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      command.execute()
    &#125;
  &#125;)(macroCommand)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当按下遥控器的按钮时，所有命令依次被执行，如图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/977f32f8f6ca4fd1882363298d4c0d35~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">透明性带来的安全问题</h2>
<p>组合模式的透明性使得发起请求的客户不用去顾忌树中组合对象和叶对象的区别，但它们在本质上是有区别的。</p>
<p>组合对象可以拥有叶子节点，叶对象下面就没有子节点，所以我们可能会有一些误操作，比如试图往叶对象中添加子节点。解决方案就是给叶对象也增加 add 方法，并且在调用这个方法时，抛出一个异常来及时提醒用户。</p>
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

<span class="hljs-keyword">var</span> openAcCommend = &#123;
  <span class="hljs-attr">execute</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'打开空调'</span>);
  &#125;,
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'叶对象不能添加子节点'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">一些值得注意的地方</h2>
<h3 data-id="heading-8">1 组合模式不是父子关系</h3>
<p>组合模式是一种 HAS-A（聚合）的关系，而不是 IS-A。组合对象包含一组叶对象，但是 Leaf 并不是 Composite 的子类。组合对象把请求委托给它包含的所有叶对象，它们能够合作的关键是拥有相同的接口。</p>
<p>为了方便描述，有时候会把上下级对象称为父子节点，但是它们并非真正意义上的父子关系。</p>
<h3 data-id="heading-9">2 对叶对象操作的一致性</h3>
<p>组合模式除了要求组合对象和叶对象拥有相同的接口之外，还有一个必要条件，就是对一组叶对象的操作必须具有一致性。</p>
<h3 data-id="heading-10">3 双向映射关系</h3>
<p>如果叶对象从属的组合对象并不单一，那么就需要给叶对象和组合对象建立双向映射关系，一个简单的办法就是给两方都增加集合来保存对方的引用，但是这种相互间的引用相当复杂，而且对象之间产生了过多的耦合性，修改或者删除一个对象都变得困难，此时，我们可以引入中介者模式来管理这些对象。</p>
<h3 data-id="heading-11">用职责链模式提高组合模式性能</h3>
<p>在组合模式中，如果树的结构比较复杂，节点数量很多，在遍历树的过程中，性能方面也许表现得不够理想。在实际操作中避免遍历整棵树，有一种现成的方案是借助职责链模式。职责链模式一般需要我们手动去设置链条，但在组合模式中，父对象和子对象之间实际上形成了天然的职责链。让请求顺着链条从父对象往子对象传递，或者是反过来从子对象往父对象传递，直到遇到可以处理该请求的对象为止，这也是职责链模式的经典运用场景之一。</p>
<h2 data-id="heading-12">何时使用组合模式</h2>
<h3 data-id="heading-13">1 表示对象的部分——整体层次结构</h3>
<p>组合模式可以方便地构造一棵树来表示对象的部分——整体结构。特别是我们在开发期间不确定这棵树到底存在多少层次的时候。在树的构造最终完成之后，只需要通过请求树的最顶层对象，便能对整棵树做统一的操作。在组合模式中增加和删除树的节点非常方便，并且符合开放——封闭原则。</p>
<h3 data-id="heading-14">2 客户希望统一对待树中的所有对象</h3>
<p>组合模式使客户可以忽略组合对象和叶对象的区别，客户在面对这棵树的时候，不用关心当前正在处理的对象是组合对象还是叶对象，也就不用写一堆 if、else 语句来分别处理它们。组合对象和叶对象会各自做自己正确的事情，这是组合模式最重要的能力。</p>
<h2 data-id="heading-15">小结</h2>
<p>组合模式可以让我们使用树形方式创建对象的结构。我们可以把相同的操作应用在组合对象和单个对象上。在大多数情况下，我们都可以忽略掉组合对象和单个对象之间的差别，从而用一致的方式来处理它们。</p>
<p>然而，组合模式并不是完美的，它可能会产生一个这样的系统：系统中的每个对象看起来都与其他对象差不多。它们的区别只有在运行的时候会才会显现出来，这会使代码难以理解。此外，如果通过组合模式创建了太多的对象，那么这些对象可能会让系统负担不起。</p>
<h2 data-id="heading-16">最后说一句</h2>
<p>如果这篇文章对您有所帮助，或者有所启发的话，帮忙点赞关注一下，您的支持是我坚持写作最大的动力，多谢支持。</p></div>  
</div>
            