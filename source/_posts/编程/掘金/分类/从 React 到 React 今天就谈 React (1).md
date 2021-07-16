
---
title: '从 React 到 React 今天就谈 React (1)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f438e60df404206a69548b33390018e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 01:00:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f438e60df404206a69548b33390018e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h3 data-id="heading-0">前言</h3>
<p>当前周边的大多数前端都在使用 Vue ，关于 Vue 自己了解的不多。回想一下在这之前自己也将近做的了3 5 年的前端。从 Jqeury 到 Angularjs 再到 React，放下前端后随后从事过一段 Android 开发，现在是一名 AI 工程师。可能是因为 javascript 这门语言引起我对编程兴趣，并且伴我多个那段困难时期，所以对于 javascript 还总是一些感情。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f438e60df404206a69548b33390018e~tplv-k3u1fbpfcp-watermark.image" alt="007.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>想写一篇比较完整全面关于 React 的分享，然后将之前自己模仿去写个 React 捡起来，继续写一个
React 可以用于写个无人驾驶的界面。</p>
<blockquote>
<p>可能无法一次将所有内容都罗列出来，说清楚，所以分享会持续更新，既往内容也会随着自己对 React 不断深入，不断更新</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c64365c5fe024ca7915a7602e64cb7bf~tplv-k3u1fbpfcp-watermark.image" alt="005.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">什么是 React</h3>
<p><strong>React</strong> 是一个用于构建用户界面的 JavaScript 库。官方用 3 个短语给出 React 的特征，声明式、组件化和一次开发处处开花。这里我们就不引用官方对 3 个特点介绍了，用自己话解释解释一下他们都是什么以及为什么官方会拿出这 3 个特点来标注 React 呢。</p>
<h4 data-id="heading-2">声明式</h4>
<p>什么是<strong>声明式</strong>呢，他又有什么好处? 这里举一个你熟悉可能还没有意识到他是声明式语言，在我们开始学前端时，第一个接触通常，或者一定是 html 这个超文本标记语言，他就是一个声明式的语言。学习 html 想必大家都很快吧，简单看看就可以 html 来定义页面结构了。这说明声明式语言对于我们人类来说更好理解，更友好。进一步说明，如果你对 html 有一定了解，当用 html 语言来定义了一个页面，无需浏览器根据 html 代码生成页面，你可能也会在脑子里大概有一个页面的样子，这就是声明式语言的好处。那么声明式语言好处更加可靠，且方便调试，而且具有很好可读性，好的可读性就意味着易于维护。</p>
<h4 data-id="heading-3">组件化</h4>
<p>各种各样设计模式，设计模式的一个目标就是减少代码冗余。其实减少代码冗余不仅仅为了减少工作量，其实还不一定会减少工作量，而是为了好维护，这个我就不多说了，开发过大型项目的一定会深有感触，从项目里 copy 代码随后会带来什么。现在 web 项目越来越负责，将页面进行组件化化，将功能组件化，提供代码和逻辑的复用。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5342b33d6d748009b97cf400af1a597~tplv-k3u1fbpfcp-watermark.image" alt="008.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个组件都是高内聚，组件间低耦合，组件间经过统一方式相互通讯交换信息。</p>
<h4 data-id="heading-4">一次学习，跨平台编写</h4>
<p>这是不仅是 Facebook 的梦想，而且许多大公司梦想。Google 的 Flutter 也在做这件事，通常都会拿 Flutter 和 React 来对比，自己前年也写了几行 Flutter 代码，写起来也有一种在写 React 感觉。大多数新框架和语言都是拥抱未来，不忘过去，例如 这是这样成功的。那么为什么 React 能够做到这一点呢? 这是因为 vDom，这是个人一点理解，Java 之所以可以做到跨平台仅是因为有字节码和虚拟机。那么 React 跨平台也就是将页面表示抽象为 VDom，vDom 作为对视图描述，然后不同平台上只要实现渲染器就可以。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c655ef65393d49dda2c70fd99d9e0fac~tplv-k3u1fbpfcp-watermark.image" alt="009.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">JSX</h4>
<p>JSX 是一个 JavaScript 的语法扩展，好处就是更加直观。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"foo"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后 Babel 会将 JSX 转换为 js 代码，将 html 标签转换 createElement 来创建元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = React.createElement(
    <span class="hljs-string">"h1"</span>,
    &#123;<span class="hljs-attr">title</span>: <span class="hljs-string">"foo"</span>&#125;,
    <span class="hljs-string">"Hello"</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">虚拟 DOM 和 diff 算法</h3>
<p>React 的虚拟DOM 和 Diff 算法是 React 的非常重要的核心特性，没有记错的虚拟 DOM 的概念应该是在 React 首次提出的。所以这部分源码也非常复杂，理解这部分知识的原理对更深入的掌握 React 是非常必要的。在 16 版本 fiber 就对应一个虚拟 DOM。本次分享先保留，随后估计需要拿出一次分享来专门说一说这块内容。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/797998aa93b24b16886ac3676b4f6231~tplv-k3u1fbpfcp-watermark.image" alt="002.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">fiber</h3>
<p>fiber 是小任务，也是数据结构，fiber，为什么叫做 fiber，进程是系统分配给应用内存资源的单位，线程是 CPU 调度的最小单位，都是到一个进程可以包含多个线程，那么 fiber 是纤维意思，其比 thread 还细小，所以就叫 fiber。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cfe54851a004159990f8141d1369064~tplv-k3u1fbpfcp-watermark.image" alt="010.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">运行 javascript 和渲染页面线程</h4>
<p>这个问题源于 javascript 的设计，javascript 是单线程非阻塞的。所以 javascript 代码运行和页面的渲染都在一个线程上。异步也就是非阻塞是借助事件循环(event loop)这个机制实现，之前已经详细介绍，这里就不再过多介绍了。</p>
<p>在这个线程上，需要做许多事，例如事件处理，计时器，启动帧事件，还有 rAF 通常作为这些就开始渲染页面，渲染页面分为布局和绘制两个步骤。其实通常渲染动作优先级低于之前这些处理，随意渲染动作是紧随这些任务之后，但是浏览器很聪明，因为通常我们显示器都是 60 HZ 也就是一秒中刷新 60 次屏幕，那么也就是大概 16.6 毫秒会刷新一下屏幕，随意当其他任何很快被执行后，浏览器也不会离开执行渲染页面动作，而是保持大概 16.6 毫秒频率来更新页面。那么如果 javascript 代码执行时间过长一直占据主线程不放就会出现卡顿的现象。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141121ada4924f73a0e93c35c29b3a53~tplv-k3u1fbpfcp-watermark.image" alt="011.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原先的 stack reconciler 像是一个递归执行的函数，从父组件调用子组件的 reconciler 过程就是一个递归执行的过程，这也是为什么被称为 stack reconciler 的原因。当我们调用 setState 的时候，react 从根节点开始遍历，找出所有的不同，而对于特别庞大的 dom 树来说，这个递归遍历的过程会消耗特别长的时间。在这个期间，任何交互和渲染都会被阻塞，这样就给用户一种“死机”的感觉。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e70b0a047014b3a80ba2eaa1d2ae859~tplv-k3u1fbpfcp-watermark.image" alt="001.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个分享源于网上一篇文章  Build your own React，这篇文章很好教你一步一步自己写一个 React，可以自己简单地写出一个 mini 版本的 React。其中介绍了 hooks 、filter 和 concurrent 模式实现， 麻雀虽小，五脏俱全。推荐大家自己写一遍，自己动手去写一方面了解 React 设计的美，另一方面也会给你在自己开发项目中找到点灵感。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子中代码量不算大，所以一个 index.js 就够用，创建一个 index.html 文件，创建一个用于加载引用的根节点 <code><div id="root"></div></code> 最后再引用一下 <code>index.js</code> 这个开发环境或者说项目就创建完了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = &#123;
    <span class="hljs-attr">type</span>:<span class="hljs-string">"h1"</span>,
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">title</span>:<span class="hljs-string">"foo"</span>,
        <span class="hljs-attr">children</span>:<span class="hljs-string">"Hello"</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);
<span class="hljs-comment">// ReactDOM.render(element, container)</span>


<span class="hljs-keyword">const</span> node = <span class="hljs-built_in">document</span>.createElement(element.type);
node[<span class="hljs-string">"title"</span>] = element.props.title;

<span class="hljs-keyword">const</span> text = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>);
text[<span class="hljs-string">"nodeValue"</span>] = element.props.children;

node.append(text);
container.append(node);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31c1e217737e4013a3024d8549f35f3a~tplv-k3u1fbpfcp-watermark.image" alt="012.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">实现 createElement 函数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"foo"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span>></span>bar<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">b</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);
ReactDOM.render(element,container)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面 React 代码中我们可以出声明式语言的优点，易读性很好。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = React.createElement(
    <span class="hljs-string">"div"</span>,
    &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"foo"</span>&#125;,
    React.createElement(<span class="hljs-string">"a"</span>,<span class="hljs-literal">null</span>,<span class="hljs-string">"bar"</span>),
    React.createElement(<span class="hljs-string">"b"</span>)
)

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);
ReactDOM.render(element,container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>React.createElement</code> 接受 3 参数，第一个参数是结点类型，字符串类型，第二个参数是是一个对象类型，以键值对形式传入结点的属性名以及对应属性值，然后是该结点的子结点，可能是多个子结点。JSX 语法就是由 Babel 将其转换为 <code>createElement</code> 方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>)</span>&#123;
    <span class="hljs-keyword">return</span>&#123;
        type,
        <span class="hljs-attr">props</span>:&#123;
            ...props,
            children
        &#125;,
    &#125;
&#125;

miniReact = &#123;
    createElement
&#125;

<span class="hljs-keyword">const</span> element = miniReact.createElement(
    <span class="hljs-string">"div"</span>,
    &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"foo"</span>&#125;,
    miniReact.createElement(<span class="hljs-string">"a"</span>,<span class="hljs-literal">null</span>,<span class="hljs-string">"bar"</span>),
    miniReact.createElement(<span class="hljs-string">"b"</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用 miniReact 作为我们要写框架的名称，然后将之前的 React 名称都对应替换为 miniReact ，然后 <code>createElement</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>)</span>&#123;
    <span class="hljs-keyword">return</span>&#123;
        type,
        <span class="hljs-attr">props</span>:&#123;
            ...props,
            <span class="hljs-attr">children</span>: children.map(<span class="hljs-function"><span class="hljs-params">child</span> =></span> 
              <span class="hljs-keyword">typeof</span> child === <span class="hljs-string">"object"</span>
                ? child
                : createTextElement(child)  
                
            ),
        &#125;,
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextElement</span>(<span class="hljs-params">text</span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"TEXT_ELEMENT"</span>,
        <span class="hljs-attr">props</span> :&#123;
            <span class="hljs-attr">nodeValue</span>: text,
            <span class="hljs-attr">children</span>: []
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对 props 使用 spread 运算符，对 children 也使用了 spread 运算符这个 ES6 新特性，值得注意 children 的 prop 就总是一个数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextElement</span>(<span class="hljs-params">text</span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"TEXT_ELEMENT"</span>,
        <span class="hljs-attr">props</span> :&#123;
            <span class="hljs-attr">nodeValue</span>: text,
            <span class="hljs-attr">children</span>: []
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3ef2dc4f923416e9956dd44f77621c2~tplv-k3u1fbpfcp-watermark.image" alt="018.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">render 函数</h4>
<p>这里 render 方法是 React 的 commit 阶段，将更新完成虚拟 DOM 渲染到界面上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>)</span>&#123;

&#125;

miniReact = &#123;
    createElement,
    render
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Render 工作就是读取 element 将其转换为 html 的 Dom 元素，然后添加到容器结点。React 通过不同渲染引擎实现将 VMOD 渲染不同设备从而实现跨平台。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"render phase"</span>)
    <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(element.type);
    container.appendChild(dom);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>递归元素的子结点，看到递归大家就应该联想到对内存消耗和线程的占用，之前通过缓存或者替换使用动态规划方式来解决递归中的问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>)</span>&#123;
    <span class="hljs-comment">// console.log("render phase")</span>
    <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(element.type);
    element.props.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> 
        render(child,dom)
    )
    container.appendChild(dom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>)</span>&#123;
    <span class="hljs-comment">// console.log("render phase")</span>
    <span class="hljs-keyword">const</span> dom = element.type == <span class="hljs-string">"TEXT_ELEMENT"</span>
        ? <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>)
        : <span class="hljs-built_in">document</span>.createElement(element.type);
    element.props.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> 
        render(child,dom)
    )
    container.appendChild(dom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在创建 Dom 元素时，对文本结点进行单独处理，所以这里稍作了特殊处理。在判断虚拟节点为 TEXT_ELEMENT 调用<code>createTextNode</code>方法来生成节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>)</span>&#123;
    <span class="hljs-comment">// console.log("render phase")</span>
    <span class="hljs-keyword">const</span> dom = element.type == <span class="hljs-string">"TEXT_ELEMENT"</span>
        ? <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>)
        : <span class="hljs-built_in">document</span>.createElement(element.type);

    <span class="hljs-keyword">const</span> isProperty = <span class="hljs-function"><span class="hljs-params">key</span> =></span> key !== <span class="hljs-string">"children"</span>
    <span class="hljs-built_in">Object</span>.keys(element.props)
        .filter(isProperty)
        .forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
            dom[name] = element.props[name]
        &#125;)
    element.props.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> 
        render(child,dom)
    )
    container.appendChild(dom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今天暂时分享到这里，随后分享  Concurrent 模式实现，会谈到 fiber 这个算法是如何解决上面问题。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6570590657e4188b9c3cdb0624b3449~tplv-k3u1fbpfcp-watermark.image" alt="016.jpeg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            