
---
title: '【React】动画库：react-transition-group'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3977'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:47:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=3977'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>react-transition-group提供了用于定义动画的简单组件，该库并未定义样式本身，而是以有用的方式操作DOM，从而使过渡和动画的实现更加舒适。换言之，react-transition-group提供了一种更简单的动画和过渡方法。</p>
<h2 data-id="heading-0">安装</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// npm</span>
npm install react-transition-group --save
​
<span class="hljs-comment">// yarn</span>
yarn add react-transition-group
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方提供四个组件，分别为 Transition, CSSTransition,SwitchTransition, TransitonGroup。</p>
<h2 data-id="heading-1">Transition</h2>
<p>Transition组件允许你使用简单的声明性API描述随时间从一个组件状态到另一个组件状态的转换。最常见的是，它被用于动画组件的挂载和卸载，但也可以用于描述就地转换状态。</p>
<p>注意:Transition是一个平台无关的基础组件。如果你在CSS中使用过渡，你可能会想要使用CSS过渡。它继承了Transition的所有特性，但包含了其他必要的特性，以更好地处理CSS过渡(因此该组件的名称)。</p>
<p>默认情况下Transition组件不会改变它呈现的组件的行为，它只跟踪组件的“进入”和“退出”状态。这取决于你赋予这些状态意义和效果。例如，当组件进入或退出时，我们可以向它添加样式。</p>
<p>在一个过渡中有四种主要状态:</p>
<ul>
<li>entering</li>
<li>entered</li>
<li>exiting</li>
<li>exited</li>
</ul>
<p>过渡状态通过in属性切换。当为true时，组件开始“Enter”阶段。在此阶段中，组件将从当前转换状态转移到转换期间的“进入”状态，然后在完成转换后再转移到“进入”状态。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Transition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-transition-group'</span>;
​
<span class="hljs-keyword">const</span> duration = <span class="hljs-number">300</span>;
​
<span class="hljs-keyword">const</span> defaultStyle = &#123;
  <span class="hljs-attr">transition</span>: <span class="hljs-string">`opacity <span class="hljs-subst">$&#123;duration&#125;</span>ms ease-in-out`</span>,
  <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>,
&#125;
​
<span class="hljs-keyword">const</span> transitionStyles = &#123;
  <span class="hljs-attr">entering</span>: &#123; <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span> &#125;,
  <span class="hljs-attr">entered</span>:  &#123; <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span> &#125;,
  <span class="hljs-attr">exiting</span>:  &#123; <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span> &#125;,
  <span class="hljs-attr">exited</span>:  &#123; <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span> &#125;,
&#125;;
​
<span class="hljs-keyword">const</span> Fade = <span class="hljs-function">(<span class="hljs-params">&#123; <span class="hljs-keyword">in</span>: inProp &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Transition</span> <span class="hljs-attr">in</span>=<span class="hljs-string">&#123;inProp&#125;</span> <span class="hljs-attr">timeout</span>=<span class="hljs-string">&#123;duration&#125;</span>></span>
    &#123;state => (
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
        <span class="hljs-attr">...defaultStyle</span>,
        <span class="hljs-attr">...transitionStyles</span>[<span class="hljs-attr">state</span>]
      &#125;&#125;></span>
        I'm a fade Transition!
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    )&#125;
  <span class="hljs-tag"></<span class="hljs-name">Transition</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>





































































































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>children</td><td>可以使用一个函数来代替 React 元素，通过调用这个函数与当前过渡状态(‘enter’、‘enter’、‘exit’、‘exited’、‘unmount’),可用于将特定于代码的props应用于组件。</td><td>Function</td><td>element</td></tr><tr><td>in</td><td>用于显示组件;触发进入或退出状态。</td><td>boolean</td><td>false</td></tr><tr><td>mountOnEnter</td><td>默认情况下，子组件与父转换组件一起立即挂载。如果你想“延迟挂载”第一个in=&#123;true&#125;上的组件，你可以设置mountOnEnter。在第一次进入转换之后，组件将保持挂载状态，即使在“退出”状态下也是如此，除非你还指定unmountOnExit。</td><td>boolean</td><td>false</td></tr><tr><td>unmountOnExit</td><td>默认情况下，子组件在达到“退出”状态后仍然挂载。如果你希望在组件退出后卸载组件，请设置unmountOnExit。</td><td>boolean</td><td>false</td></tr><tr><td>appear</td><td>通常，如果组件挂载时显示组件，则该组件不进行转换。如果你希望在第一个挂载集上进行转换，则显示为true，并且组件将在< transition >挂载后立即进行转换。 <strong>注意:没有特定的“显示”状态。appear只添加一个额外的enter转换</strong>。</td><td>boolean</td><td>false</td></tr><tr><td>enter</td><td>启用或禁用enter转换。</td><td>boolean</td><td>true</td></tr><tr><td>exit</td><td>启用或禁用exit转换。</td><td>boolean</td><td>true</td></tr><tr><td>timeout</td><td>转换的持续时间，单位为毫秒。</td><td>number</td><td>&#123; enter?: number, exit?: number, appear?: number &#125;</td></tr><tr><td>addEndListener</td><td>添加自定义转换结束触发器。使用正在转换的DOM节点和done回调调用。允许更细粒度的转换结束逻辑。注意:如果提供超时，仍将其用作回退。</td><td>Function</td><td></td></tr><tr><td>onEnter</td><td>在应用“输入”状态之前触发的回调。提供了一个额外的参数isAppearing，以指示是否在初始挂载上出现了enter阶段。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td>function noop() &#123;&#125;</td></tr><tr><td>onEntering</td><td>在应用“输入”状态中触发的回调。提供了一个额外的参数isAppearing，以指示是否在初始挂载上出现了entering阶段。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td>function noop() &#123;&#125;</td></tr><tr><td>onEntered</td><td>在应用“输入”状态之后触发的回调。提供了一个额外的参数isAppearing，以指示是否在初始挂载上出现了entered阶段。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td>function noop() &#123;&#125;</td></tr><tr><td>onExit</td><td>在应用“退出”状态之前触发的回调。</td><td>Function(node: HtmlElement) -> void</td><td>function noop() &#123;&#125;</td></tr><tr><td>onExiting</td><td>在应用“退出”状态中触发的回调。</td><td>Function(node: HtmlElement) -> void</td><td>function noop() &#123;&#125;</td></tr><tr><td>onExited</td><td>在应用“退出”状态后触发的回调。</td><td>Function(node: HtmlElement) -> void</td><td>function noop() &#123;&#125;</td></tr></tbody></table>
<h2 data-id="heading-2">CSSTransition</h2>
<p>此Transition组件用于CSS动画过渡，灵感来源于ng-animate库。</p>
<p>CSSTransition：在组件淡入appear，进场enter,出场exit时，CSSTransition组件应用了一系列className名来对这些动作进行描述。首先appear被应用到组件className上，接着添加“active”类名来激活CSS动画。在动画完成后，原class改变为done表明组件动画已经应用完成并加载完成。</p>
<p>当组件的in属性变为true时，组件的className将被赋值为example-enter，并在下一刻添加example-enter-active的CSS class名。这些都是基于className属性的约定。即：原组件带有className="animate-rotate"，则enter状态时，变为"animate-rotate-enter"。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js</span>
<span class="hljs-keyword">import</span> React,&#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> CSSTransition <span class="hljs-keyword">from</span> <span class="hljs-string">'react-transition-group/CSSTransition'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./css/index.css'</span>
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
​
    state = &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
    &#125;
​
    render () &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">CSSTransition</span>
                <span class="hljs-attr">in</span>=<span class="hljs-string">&#123;this.state.show&#125;</span>
                <span class="hljs-attr">classNames</span>=<span class="hljs-string">'show'</span>
                <span class="hljs-attr">timeout</span>=<span class="hljs-string">&#123;300&#125;</span>
                <span class="hljs-attr">unmountOnExit</span>></span>
                &#123;state => &#123;
                    // console.log(state)
                    return (
                        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'circle'</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>this.setState(state=>(&#123;show: !state.show&#125;))&#125;> 
                            show 
                        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                    )
                &#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">CSSTransition</span>></span></span>
        )
    &#125;
&#125;
​
<span class="hljs-comment">//index.css</span>
.circle &#123;
    <span class="hljs-attr">margin</span>: 2px;
    width: 50px;
    height: 50px;
    position: absolute;
    display: inline-block;
    left: 100px;
    box-shadow: 0px 1px 2px #<span class="hljs-number">999</span>;
    text-shadow: 0px 1px 2px #<span class="hljs-number">999</span>;
    line-height: 80px;
    text-align: center;
    color: white;
    font-size: 10px;
&#125;
​
.show-enter &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.01</span>;
    transform: scale(<span class="hljs-number">0.9</span>) translateY(<span class="hljs-number">50</span>%);
  &#125;
.show-enter-active &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
    transform: scale(<span class="hljs-number">1</span>) translateY(<span class="hljs-number">0</span>%);
    transition: all 300ms ease-out;
&#125;
.show-exit &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
    transform: scale(<span class="hljs-number">1</span>) translateY(<span class="hljs-number">0</span>%);
&#125;
.show-exit-active &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.01</span>;
    transform: scale(<span class="hljs-number">0.9</span>) translateY(<span class="hljs-number">50</span>%);
    transition: all 300ms ease-out;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>



























































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>in</td><td>控制组件应用动画的属性值，通常将一个react的组件state赋值给它，通过改变state，从而开启和关闭动画。</td><td>boolean</td><td>false</td></tr><tr><td>classNames</td><td>classNames[注意带s]属性用于当组件被应用动画时，不同的动画状态（enter,exits,done）将作为className属性的后缀来拼接为新的className。 如：className="fade"会被应用为fade-enter,fade-enter-active,fade-enter-done,fade-exit,fade-exite-active,fade-exit-done, fade-appear以及fade-appear-active.每一个独立的className都对应着单独的状态。</td><td>string</td><td>&#123; appear?: string, appearActive?: string, enter?: string, enterActive?: string, enterDone?: string, exit?: string, exitActive?: string, exitDone?: string, &#125;</td></tr><tr><td>onEnter</td><td>组件的回调函数，当组件enter或appear时会立即调用。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td></td></tr><tr><td>onEntering</td><td>组件的回调函数，当enter-active或appear-active时会立即调用。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td></td></tr><tr><td>onEntered</td><td>组件的回调函数，当组件的enter,appearclassName被移除时会立即调用。</td><td>Function(node: HtmlElement, isAppearing: bool)</td><td></td></tr><tr><td>onExit</td><td>当组件应用exit类名时，调用此函数。</td><td>Function(node: HtmlElement)</td><td></td></tr><tr><td>onExiting</td><td>当组件应用exit-active类名时，调用此函数。</td><td>Function(node: HtmlElement)</td><td></td></tr><tr><td>onExited</td><td>当组件exit类名被移除，且添加了exit-done类名时，调用此函数。</td><td>Function(node: HtmlElement)</td><td></td></tr></tbody></table>
<h2 data-id="heading-3">SwitchTransition</h2>
<p>受vue转换模式启发的转换组件。当你想要控制状态转换之间的呈现时，可以使用它。基于所选模式和子节点的键(Transition或cstransition组件)，SwitchTransition在它们之间进行一致的转换。</p>
<p>如果选择了out-in模式，则SwitchTransition会等待旧的子节点离开，然后插入新的子节点。如果选择了in-out模式，SwitchTransition将首先插入一个新的子节点，等待新的子节点进入，然后删除旧的子节点。</p>
<p>注意:如果你想让动画同时发生(也就是说，移除旧的子元素并同时插入新的子元素)，你应该使用TransitionGroup。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-literal">false</span>);
 <span class="hljs-keyword">return</span> (
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SwitchTransition</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">CSSTransition</span>
       <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;state</span> ? "<span class="hljs-attr">Goodbye</span>, <span class="hljs-attr">world</span>!" <span class="hljs-attr">:</span> "<span class="hljs-attr">Hello</span>, <span class="hljs-attr">world</span>!"&#125;
       <span class="hljs-attr">addEndListener</span>=<span class="hljs-string">&#123;(node,</span> <span class="hljs-attr">done</span>) =></span> node.addEventListener("transitionend", done, false)&#125;
       classNames='fade'
     >
       <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setState(state => !state)&#125;>
         &#123;state ? "Goodbye, world!" : "Hello, world!"&#125;
       <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">CSSTransition</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">SwitchTransition</span>></span></span>
 );
&#125;
.fade-enter&#123;
   <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
&#125;
.fade-exit&#123;
   <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
&#125;
.fade-enter-active&#123;
   <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
&#125;
.fade-exit-active&#123;
   <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
&#125;
.fade-enter-active,
.fade-exit-active&#123;
   <span class="hljs-attr">transition</span>: opacity 500ms;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>























<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>mode</td><td>过渡模式。out-in:首先将当前元素移出，然后在完成时将新元素移入。in-out:新元素首先转换进来，完成后，当前元素转换出去。</td><td>out-in</td><td>in-out</td></tr><tr><td>children</td><td>任何Transition 或者 CSSTransition组件.</td><td>element</td><td></td></tr></tbody></table>
<h2 data-id="heading-4">TransitionGroup</h2>
<p>组件在一个列表中管理一组转换组件(< transition >和< cstransition >)。与转换组件一样，是一个状态机，用于管理组件随时间的挂载和卸载。</p>
<p>下面的例子，当项目被删除或添加到TodoList时，内部的prop将由自动切换。</p>
<p>注意没有定义任何动画行为!列表项的动画方式取决于各个转换组件。这意味着你可以混合和匹配不同列表项的动画。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js</span>
<span class="hljs-keyword">import</span> React,&#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; CSSTransition, TransitionGroup &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-transition-group'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./css/index.css'</span>
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
​
  state = &#123;
    <span class="hljs-attr">items</span>: [
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">'Buy eggs'</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">'Pay bills'</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">'Invite friends over'</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">'Fix the TV'</span> &#125;,
    ]
  &#125;
​
  render () &#123;
    <span class="hljs-keyword">const</span> &#123; items &#125; = <span class="hljs-built_in">this</span>.state
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'container'</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">TransitionGroup</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"todo-list"</span>></span>
          &#123;items.map((&#123; id, text &#125;) => (
            <span class="hljs-tag"><<span class="hljs-name">CSSTransition</span>
              <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;id&#125;</span>
              <span class="hljs-attr">timeout</span>=<span class="hljs-string">&#123;500&#125;</span>
              <span class="hljs-attr">classNames</span>=<span class="hljs-string">"show"</span>
              <span class="hljs-attr">unmountOnExit</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"todo-list-item"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span>
                  <span class="hljs-attr">className</span>=<span class="hljs-string">'cancle'</span>
                  <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
                    this.setState(state => (&#123;
                      items: state.items.filter(
                        item => item.id !== id
                      ),
                    &#125;));
                  &#125;&#125;>
                  <span class="hljs-symbol">&times;</span>
                <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'item-text'</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">CSSTransition</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">TransitionGroup</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span>
          <span class="hljs-attr">className</span>=<span class="hljs-string">'add'</span>
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
            const text = prompt('Enter some text');
            if (text) &#123;
              this.setState(state => (&#123;
                items: [
                  ...state.items,
                  &#123; id: 1123, text &#125;,
                ],
              &#125;));
            &#125;
          &#125;&#125;>
          Add Item
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
​
<span class="hljs-comment">//index.css</span>
.show-enter &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.01</span>;
  &#125;
.show-enter-active &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
    transition: all 300ms ease-out;
&#125;
.show-exit &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
&#125;
.show-exit-active &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.01</span>;
    transition: all 300ms ease-out;
&#125;
​
.container &#123;
    <span class="hljs-attr">position</span>: absolute;
    top: 20px;
    left: 100px;
    padding: 20px;
    border-radius: 5px;
    box-shadow: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 10px 1px rgb(<span class="hljs-number">202</span>, <span class="hljs-number">202</span>, <span class="hljs-number">202</span>);
&#125;
​
.todo-list &#123;
    border-radius: 5px;
    box-shadow: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 1px rgb(<span class="hljs-number">202</span>, <span class="hljs-number">202</span>, <span class="hljs-number">202</span>);
&#125;
​
.todo-list-item &#123;
    <span class="hljs-attr">height</span>: 35px;
    line-height: 35px;
    padding: <span class="hljs-number">0</span> 10px;
    border-bottom: 1px solid rgb(<span class="hljs-number">202</span>, <span class="hljs-number">202</span>, <span class="hljs-number">202</span>);
&#125;
​
.todo-list-item:last-<span class="hljs-keyword">of</span>-type &#123;
    border-bottom: <span class="hljs-number">0</span>;
&#125;
​
.item-text &#123;
    margin-left: 10px;
&#125;
​
.cancle &#123;
    <span class="hljs-attr">border</span>: <span class="hljs-number">0</span>;
    color: #fff;
    background-color: #F04134;
    border-radius: 3px;
    box-shadow: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 1px rgb(<span class="hljs-number">202</span>, <span class="hljs-number">202</span>, <span class="hljs-number">202</span>);
&#125;
​
.add &#123;
    <span class="hljs-attr">border</span>: <span class="hljs-number">0</span>;
    height: 30px;
    line-height: 30x;
    width: 120px;
    margin-top: 15px;
    font-size: 14px;
    border-radius: 3px;
    box-shadow: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 1px rgb(<span class="hljs-number">202</span>, <span class="hljs-number">202</span>, <span class="hljs-number">202</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>















































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>component</td><td>default 'div' 也就是TransitionGroup渲染出来的标签为div，也可以就行更改，例如component="span" 渲染出来的就是span标签。如果使用React v16+并且想要避免div元素的换行，你可以传入component=&#123;null&#125;。</td><td>any</td><td>div</td></tr><tr><td>children</td><td>其中给的组件，可以是字符串或者自定义组件等。</td><td>any</td><td></td></tr><tr><td>appear</td><td>为所有的child启用或禁用显示/appear动画。注意，指定此参数将覆盖在各个子转换上的任何默认设置。</td><td>boolean</td><td></td></tr><tr><td>enter</td><td>为所有的child启用或禁用进入/enter动画。注意，指定此参数将覆盖在各个子转换上的任何默认设置。</td><td>boolean</td><td></td></tr><tr><td>exit</td><td>为所有的child启用或禁用退出/exit动画。注意，指定此参数将覆盖在各个子转换上的任何默认设置。</td><td>boolean</td><td></td></tr><tr><td>childFactory</td><td>如果你需要在一个子节点离开时更新它可以提供一个childFactory来包装每个子节点，即使是那些将要离开的子节点。</td><td>Function(child: ReactElement) -> ReactElement</td><td>child => child</td></tr></tbody></table></div>  
</div>
            