
---
title: '_译_深入了解React中的state和props更新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec3f434e7ca4322a0678d7a049f7f75~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 01:44:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec3f434e7ca4322a0678d7a049f7f75~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<ul>
<li>原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Findepth.dev%2Fposts%2F1009%2Fin-depth-explanation-of-state-and-props-update-in-react" target="_blank" rel="nofollow noopener noreferrer" title="https://indepth.dev/posts/1009/in-depth-explanation-of-state-and-props-update-in-react" ref="nofollow noopener noreferrer">indepth.dev/posts/1009/…</a></li>
<li>原文标题：In-depth explanation of state and props update in React</li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fmaxkoretskyi" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/maxkoretskyi" ref="nofollow noopener noreferrer">Max Koretskyi</a></li>
</ul>
</blockquote>
<p>在我的上篇文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Findepth.dev%2Finside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://indepth.dev/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react/" ref="nofollow noopener noreferrer">Inside Fiber: 深入了解React新协调算法</a>中介绍了理解更新过程细节的所需的基础知识，我将在本文中描述这个更新过程。</p>
<p>我已经概述了将在本文中使用的主要数据结构和概念，特别是Fiber节点，<code>current</code>和<code>work-in-progress</code>树，副作用（side-effects）以及effects链表（effects list）。我也提供了主要算法的高级概述和<code>render</code>阶段与<code>commit</code>阶段的差异。如果你还没有阅读过它，我推荐你从那儿开始。</p>
<p>我还向你介绍了带有一个按钮的示例程序，这个按钮的功能就是简单的增加数字。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec3f434e7ca4322a0678d7a049f7f75~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以在这查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackblitz.com%2Fedit%2Freact-jwqn64" target="_blank" rel="nofollow noopener noreferrer" title="https://stackblitz.com/edit/react-jwqn64" ref="nofollow noopener noreferrer">在线代码</a>。它的实现很简单，就是一个render函数中返回<code>button</code>和<code>span</code>元素的类组件。当你点击按钮的时候，在点击事件的处理函数中更新组件的<code>state</code>。结果就是<code>span</code>元素的文本会更新。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;;
        <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
        &#125;);
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> [
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>Update counter<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>,
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"2"</span>></span>&#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我为这个组件添加了<code>componentDidUpdate</code>生命周期方法。这是为了演示React如何添加<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Freact-in-depth%2Finside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/react-in-depth/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" ref="nofollow noopener noreferrer">effects</a>并在<code>commit</code>阶段调用这个方法。在本文中，我想向你展示React是如何处理状态更新和创建effects list的。我们可以看到<code>render</code>阶段和<code>commit</code>阶段的高级函数中发生了什么。</p>
<p>尤其是在React的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fcbbc2b6c4d0d8519145560bd8183ecde55168b12%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberCompleteWork.js%23L532" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberCompleteWork.js#L532" ref="nofollow noopener noreferrer">completeWork</a>函数中：</p>
<ul>
<li>更新<code>ClickCounter</code>的<code>state</code>中的<code>count</code>属性</li>
<li>调用<code>render</code>方法获取子元素列表并比较</li>
<li>更新<code>span</code>元素的<code>props</code></li>
</ul>
<p>以及，在React的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L523" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L523" ref="nofollow noopener noreferrer">commitRoot</a> 函数中：</p>
<ul>
<li>更新<code>span</code>元素的文本内容属性</li>
<li>调用<code>componentDidUpdate</code>生命周期方法</li>
</ul>
<p>但是在那之前，我们先快速看看当我们在点击处理函数中调用<code>setState</code>时工作是如何调度的。</p>
<p><strong>请注意，你无需了解这些来使用React。本文是关于React内部是如何运作的。</strong></p>
<h2 data-id="heading-0">调度更新</h2>
<p>当我们点击按钮时，<code>click</code>事件被触发，React执行传递给按钮<code>props</code>的回调。在我们的程序中，它只是简单的增加计数器和更新<code>state</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    ...
    <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
        &#125;);
    &#125;
&#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个组件都有相应的<code>updater</code>，它作为组件和React核心之间的桥梁。这允许<code>setState</code>在ReactDOM，React Native，服务端渲染和测试程序中是不同的实现。（译注：从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fmaster%2Fpackages%2Freact%2Fsrc%2FReactBaseClasses.js%23L65" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/master/packages/react/src/ReactBaseClasses.js#L65" ref="nofollow noopener noreferrer">源码</a>可以看出，<code>setState</code>内部是调用<code>updater.enqueueSetState</code>，这样在不同平台，我们都可以调用<code>setState</code>来更新页面）</p>
<p>本文中，我们关注ReactDOM中实现的<code>updater</code>对象，它使用Fiber协调器。对于<code>ClickCounter</code>组件，它是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F6938dcaacbffb901df27782b7821836961a5b68d%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberClassComponent.js%23L186" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/6938dcaacbffb901df27782b7821836961a5b68d/packages/react-reconciler/src/ReactFiberClassComponent.js#L186" ref="nofollow noopener noreferrer">classComponentUpdater</a>。它负责获取Fiber实例，为更新入列，以及调度work。</p>
<p>当更新排队时，它们基本上只是添加到Fiber节点的更新队列中进行处理。在我们的例子中，<code>ClickCounter</code>组件对应的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Freact-in-depth%2Finside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/react-in-depth/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" ref="nofollow noopener noreferrer">Fiber节点</a>将有下面的结构：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> ClickCounter,
    <span class="hljs-attr">type</span>: ClickCounter,
    <span class="hljs-attr">updateQueue</span>: &#123;
         <span class="hljs-attr">baseState</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;
         <span class="hljs-attr">firstUpdate</span>: &#123;
             <span class="hljs-attr">next</span>: &#123;
                 <span class="hljs-attr">payload</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123; <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125; &#125;
             &#125;
         &#125;,
         ...
     &#125;,
     ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如你所见，<code>updateQueue.firstUpdate.next.payload</code>中的函数就我我们在<code>ClickCounter</code>组件中传递给<code>setState</code>的回调。它代表在<code>render</code>阶段中需要处理的第一个更新。</p>
<h2 data-id="heading-1">处理ClickCounter Fiber节点的更新</h2>
<p>我上篇文章中的<a href="https://link.juejin.cn/?target=https%3A%2F%2Findepth.dev%2Finside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://indepth.dev/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react/" ref="nofollow noopener noreferrer">work循环部分中</a>解释了全局变量<code>nextUnitOfWork</code>的角色。尤其是，这个变量保存<code>workInProgress</code>树中有work待做的Fiber节点的引用。当React遍历树的Fiber时，它使用这个变量知道是否存在其他有未完成work的Fiber节点。</p>
<p>我们假定<code>setState</code>方法已经被调用。 React将setState中的回调添加到<code>ClickCounter</code>fiber节点的<code>updateQueue</code>中，然后调度work。React进入<code>render</code>阶段。它使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L1132" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L1132" ref="nofollow noopener noreferrer">renderRoot</a>函数从最顶层<code>HostRoot</code>Fiber节点开始遍历。然而，它会跳过已经处理过得Fiber节点直到遇到有未完成work的节点。基于这点，只有一个节点有work待做。它就是<code>ClickCounter</code>Fiber节点。</p>
<p>所有的work都是基于保存在Fiber节点的<code>alternate</code>字段的克隆副本执行的。如果alternate节点还未创建，React在处理更新前调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F769b1f270e1251d9dbdce0fcbd9e92e502d059b8%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiber.js%23L326" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/react-reconciler/src/ReactFiber.js#L326" ref="nofollow noopener noreferrer">createWorkInProgress</a>函数创建副本。我们假设<code>nextUnitOfWork</code>变量保存代替<code>ClickCounter</code>Fiber节点的引用。</p>
<h2 data-id="heading-2">beginWork</h2>
<p>首先, 我们的Fiber进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fcbbc2b6c4d0d8519145560bd8183ecde55168b12%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L1489" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberBeginWork.js#L1489" ref="nofollow noopener noreferrer">beginWork</a>函数。</p>
<blockquote>
<p>因为这个函数对树中每个节点执行，所以如果你想调试render阶段，它是放置断点的好地方。 我经常这样做，还有检查Fiber节点的type来确定我需要的节点。</p>
</blockquote>
<p><code>beginWork</code>函数大体上是个大的<code>switch</code>语句，通过<code>tag</code>确定Fiber节点需要完成的work的类型，然后执行相应的函数来执行work。在这个例子中，<code>CountClicks</code>是类组件，所以会走这个分支：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">current$$<span class="hljs-number">1</span>, workInProgress, ...</span>) </span>&#123;
    ...
    <span class="hljs-keyword">switch</span> (workInProgress.tag) &#123;
        ...
        <span class="hljs-keyword">case</span> FunctionalComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> ClassComponent:
        &#123;
            ...
            <span class="hljs-keyword">return</span> updateClassComponent(current$$1, workInProgress, ...);
        &#125;
        <span class="hljs-keyword">case</span> HostComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F1034e26fe5e42ba07492a736da7bdf5bf2108bc6%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L428" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/1034e26fe5e42ba07492a736da7bdf5bf2108bc6/packages/react-reconciler/src/ReactFiberBeginWork.js#L428" ref="nofollow noopener noreferrer">updateClassComponent</a>函数。取决于它是首次渲染、恢复work还是React更新，React会创建实例并挂载组件或只是更新它：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClassComponent</span>(<span class="hljs-params">current, workInProgress, Component, ...</span>) </span>&#123;
    ...
    <span class="hljs-keyword">const</span> instance = workInProgress.stateNode;
    <span class="hljs-keyword">let</span> shouldUpdate;
    <span class="hljs-keyword">if</span> (instance === <span class="hljs-literal">null</span>) &#123;
        ...
        <span class="hljs-comment">// In the initial pass we might need to construct the instance.</span>
        constructClassInstance(workInProgress, Component, ...);
        mountClassInstance(workInProgress, Component, ...);
        shouldUpdate = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (current === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// In a resume, we'll already have an instance we can reuse.</span>
        shouldUpdate = resumeMountClassInstance(workInProgress, Component, ...);
    &#125; <span class="hljs-keyword">else</span> &#123;
        shouldUpdate = updateClassInstance(current, workInProgress, ...);
    &#125;
    <span class="hljs-keyword">return</span> finishClassComponent(current, workInProgress, Component, shouldUpdate, ...);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">处理ClickCounter Fiber更新</h2>
<p>我们已经有了<code>ClickCounter</code>组件实例，所以我们进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F6938dcaacbffb901df27782b7821836961a5b68d%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberClassComponent.js%23L976" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/6938dcaacbffb901df27782b7821836961a5b68d/packages/react-reconciler/src/ReactFiberClassComponent.js#L976" ref="nofollow noopener noreferrer">updateClassInstance</a>。这是React为类组件执行大部分work的地方。以下是在这个函数中按顺序执行的最重要的操作：</p>
<ul>
<li>调用<code>UNSAFE_componentWillReceiveProps()</code>钩子（已废弃）</li>
<li>处理<code>updateQueue</code>中的更新以及生成新state</li>
<li>使用新state调用<code>getDerivedStateFromProps</code>并得到结果</li>
<li>调用<code>shouldComponentUpdate</code>确定组件是否需要更新；如果返回结果为<code>false</code>，跳过整个渲染过程，包括在该组件和它的子组件上调用<code>render</code>；否则继续更新</li>
<li>调用<code>UNSAFE_componentWillUpdate</code>（已废弃）</li>
<li>添加一个effect来触发<code>componentDidUpdate</code>生命周期钩子</li>
</ul>
<blockquote>
<p>尽管调用<code>componentDidUpdate</code>的effect是在<code>render</code>阶段添加的，这个方法将在接下来的<code>commit</code>阶段执行。</p>
</blockquote>
<ul>
<li>更新组件实例的<code>state</code>和<code>props</code></li>
</ul>
<p>组件实例的<code>state</code>和<code>props</code>应该在<code>render</code>方法调用前更新，因为<code>render</code>方法的输出通常依赖于<code>state</code>和<code>props</code>。如果我们不这样做，它每次都会返回一样的输出。</p>
<p>下面是该函数的简化版本：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClassInstance</span>(<span class="hljs-params">current, workInProgress, ctor, newProps, ...</span>) </span>&#123;
    <span class="hljs-keyword">const</span> instance = workInProgress.stateNode;

    <span class="hljs-keyword">const</span> oldProps = workInProgress.memoizedProps;
    instance.props = oldProps;
    <span class="hljs-keyword">if</span> (oldProps !== newProps) &#123;
        callComponentWillReceiveProps(workInProgress, instance, newProps, ...);
    &#125;

    <span class="hljs-keyword">let</span> updateQueue = workInProgress.updateQueue;
    <span class="hljs-keyword">if</span> (updateQueue !== <span class="hljs-literal">null</span>) &#123;
        processUpdateQueue(workInProgress, updateQueue, ...);
        newState = workInProgress.memoizedState;
    &#125;

    applyDerivedStateFromProps(workInProgress, ...);
    newState = workInProgress.memoizedState;

    <span class="hljs-keyword">const</span> shouldUpdate = checkShouldComponentUpdate(workInProgress, ctor, ...);
    <span class="hljs-keyword">if</span> (shouldUpdate) &#123;
        instance.componentWillUpdate(newProps, newState, nextContext);
        workInProgress.effectTag |= Update;
        workInProgress.effectTag |= Snapshot;
    &#125;

    instance.props = newProps;
    instance.state = newState;

    <span class="hljs-keyword">return</span> shouldUpdate;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码片段中我删除了一些辅助代码。对于实例，调用生命周期方法或添加effects来触发它们前，React使用<code>typeof</code>操作符检查组件是否实现了这些方法。比如，这是React添加effect前如何检查<code>componentDidUpdate</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> instance.componentDidUpdate === <span class="hljs-string">'function'</span>) &#123;
    workInProgress.effectTag |= Update;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，我们现在知道了<code>render</code>阶段中为<code>ClickCounter</code>Fiber节点执行了什么操作。现在让我们看看这些操作如何改变Fiber节点的值。当React开始work，<code>ClickCounter</code>组件的Fiber节点类似这样：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">elementType</span>: <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span>,
    <span class="hljs-title">firstEffect</span>: <span class="hljs-title">null</span>,
    <span class="hljs-title">memoizedState</span>: </span>&#123;count: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">type</span>: <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span>,
    <span class="hljs-title">stateNode</span>: </span>&#123;
        <span class="hljs-attr">state</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;
    &#125;,
    <span class="hljs-attr">updateQueue</span>: &#123;
        <span class="hljs-attr">baseState</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;,
        <span class="hljs-attr">firstUpdate</span>: &#123;
            <span class="hljs-attr">next</span>: &#123;
                <span class="hljs-attr">payload</span>: <span class="hljs-function">(<span class="hljs-params">state, props</span>) =></span> &#123;…&#125;
            &#125;
        &#125;,
        ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>work完成后，我们得到一个长这样的Fiber节点：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">4</span>,
    <span class="hljs-attr">elementType</span>: <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span>,
    <span class="hljs-title">firstEffect</span>: <span class="hljs-title">null</span>,
    <span class="hljs-title">memoizedState</span>: </span>&#123;count: <span class="hljs-number">1</span>&#125;,
    <span class="hljs-attr">type</span>: <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span>,
    <span class="hljs-title">stateNode</span>: </span>&#123;
        <span class="hljs-attr">state</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">1</span>&#125;
    &#125;,
    <span class="hljs-attr">updateQueue</span>: &#123;
        <span class="hljs-attr">baseState</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">1</span>&#125;,
        <span class="hljs-attr">firstUpdate</span>: <span class="hljs-literal">null</span>,
        ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>花点时间观察属性值的差异</strong></p>
<p>更新被应用后，<code>memoizedState</code>和<code>updateQueue</code>中<code>baseState</code>的属性<code>count</code>的值变为<code>1</code>。React也更新了<code>ClickCounter</code>组件实例的state。</p>
<p>至此，队列中不再有更新，所以<code>firstUpdate</code>为<code>null</code>。更重要的是，我们改变了<code>effectTag</code>属性。它不再是<code>0</code>，它的是为<code>4</code>。 二进制为<code>100</code>，意味着第三位被设置了，代表<code>Update</code><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fb87aabdfe1b7461e7331abb3601d9e6bb27544bc%2Fpackages%2Fshared%2FReactSideEffectTags.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/b87aabdfe1b7461e7331abb3601d9e6bb27544bc/packages/shared/ReactSideEffectTags.js" ref="nofollow noopener noreferrer">副作用标记</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Update = <span class="hljs-number">0b00000000100</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以得出结论，当执行<code>ClickCounter</code>Fiber节点的work时，React低啊用变化前生命周期方法，更新state，定义有关的副作用。</p>
<h2 data-id="heading-4">协调ClickCounter Fiber的子组件</h2>
<p>在那之后，React进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F340bfd9393e8173adca5380e6587e1ea1a23cefa%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L355" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/340bfd9393e8173adca5380e6587e1ea1a23cefa/packages/react-reconciler/src/ReactFiberBeginWork.js#L355" ref="nofollow noopener noreferrer">finishClassComponent</a>。这是调用组件实例render方法和在子组件上使用diff算法的地方。<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Freconciliation.html%23the-diffing-algorithm" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/reconciliation.html#the-diffing-algorithm" ref="nofollow noopener noreferrer">文档中</a>对此有高级概述。以下是相关部分：</p>
<blockquote>
<p>当比较两个相同类型的React DOM元素时，React查看两者的属性（attributes），保留DOM节点，仅更新变化了的属性。</p>
</blockquote>
<p>然而，如果我们深入挖掘，会知道它实际是对比Fiber节点和React元素。但是我现在不会详细介绍因为过程相当复杂。我会单独些篇文章，特别关注子协调过程。</p>
<blockquote>
<p>如果你想自己学习细节，请查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.js%23L732" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactChildFiber.js#L732" ref="nofollow noopener noreferrer">reconcileChildrenArray</a>函数，因为在我们的程序中<code>render</code>方法返回一个React元素数组。</p>
</blockquote>
<p>至此，有两个很重要的事需要理解。<strong>第一</strong>，当React进行子协调时，它会为从<code>render</code>函数返回的子React元素创建或更新Fiber节点。<code>finishClassComponent</code>函数当前Fiber节点的第一个子节点的引用。它被赋值给<code>nextUnitOfWork</code>并在稍后的work循环中处理。<strong>第二</strong>，React更新子节点的props作为父节点执行的一部分work。为此，它使用render函数返回的React元素的数据。</p>
<p>举例来说，这是React协调<code>ClickCounter</code>fiber子节点之前<code>span</code>元素对应的Fiber节点看起来的样式</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-attr">memoizedProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">pendingProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>memoizedProps</code>和<code>pendingProps</code>的<code>children</code>属性都是<code>0</code>。这是<code>render</code>函数返回的<code>span</code>元素对应的React元素的结构。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">$$typeof</span>: <span class="hljs-built_in">Symbol</span>(react.element)
    <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>
    <span class="hljs-attr">props</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">1</span>&#125;
    <span class="hljs-attr">ref</span>: <span class="hljs-literal">null</span>
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，Finer节点和返回的React元素的<strong>props是有差异的</strong>。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F769b1f270e1251d9dbdce0fcbd9e92e502d059b8%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiber.js%23L326" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/react-reconciler/src/ReactFiber.js#L326" ref="nofollow noopener noreferrer">createWorkInProgress</a>内部用这创建替代的Fiber节点，<strong>React把React元素中更新的属性复制到Fiber节点</strong>。</p>
<p>因此，在React完成<code>ClickCounter</code>组件子协调后，<code>span</code>的Fiber节点的<code>pendingProps</code>更新了。它们将匹配<code>span</code>React元素中的值。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-attr">memoizedProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">pendingProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">1</span>&#125;,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍后，React会为<code>span</code>Fiber节点执行work，它将把它们复制到<code>memoizedProps</code>以及添加effects来更新DOM。</p>
<p>好的，这就是render阶段React为<code>ClickCounter</code>fiber节点所执行的所有work。因为button是<code>ClickCounter</code>组件的第一个子节点，它会被赋值给<code>nextUnitOfWork</code>变量。button上无事可做，所有React会移动到它的兄弟节点<code>span</code>Fiber节点上。根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Freact-in-depth%2Finside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/react-in-depth/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react-e1c04700ef6e" ref="nofollow noopener noreferrer">这里描述的</a>算法，这发生在<code>completeUnitOfWork</code>函数内。</p>
<h2 data-id="heading-5">处理Span fiber的更新</h2>
<p><code>nextUnitOfWork</code>变量现在指向<code>span</code>fiber的alternate，React基于它开始工作。和<code>ClickCounter</code>执行的步骤类似，开始于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fcbbc2b6c4d0d8519145560bd8183ecde55168b12%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L1489" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberBeginWork.js#L1489" ref="nofollow noopener noreferrer">beginWork</a>函数。</p>
<p>因为<code>span</code>节点是<code>HostComponent</code>类型，这次在switch语句中React会进入这条分支：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">current$$<span class="hljs-number">1</span>, workInProgress, ...</span>) </span>&#123;
    ...
    <span class="hljs-keyword">switch</span> (workInProgress.tag) &#123;
        <span class="hljs-keyword">case</span> FunctionalComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> ClassComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> HostComponent:
          <span class="hljs-keyword">return</span> updateHostComponent(current, workInProgress, ...);
        <span class="hljs-keyword">case</span> ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结束于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fcbbc2b6c4d0d8519145560bd8183ecde55168b12%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L686" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberBeginWork.js#L686" ref="nofollow noopener noreferrer">updateHostComponent</a>函数。（在这个函数内）你可以看到一系列和类组件调用的<code>updateClassComponent</code>函数类似的函数。对于函数组件是<code>updateFunctionComponent</code>。你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F1034e26fe5e42ba07492a736da7bdf5bf2108bc6%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/1034e26fe5e42ba07492a736da7bdf5bf2108bc6/packages/react-reconciler/src/ReactFiberBeginWork.js" ref="nofollow noopener noreferrer">ReactFiberBeginWork.js</a>文件中找到这些函数。</p>
<h2 data-id="heading-6">协调Span fiber子节点</h2>
<p>在我们的例子中，<code>span</code>节点在<code>updateHostComponent</code>里没什么重要事的发生。</p>
<h2 data-id="heading-7">完成Span Fiber节点的work</h2>
<p>一旦<code>beginWork</code>完成，节点就进入<code>completeWork</code>函数。但是在那之前，React需要更新<code>span</code> Fiber节点的<code>memoizedProps</code>属性。你应该还记得协调<code>ClickCounter</code>组件子节点时更新了<code>span</code>Fiber节点的<code>pendingProps</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-attr">memoizedProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">pendingProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">1</span>&#125;,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以一旦<code>span</code>fiber的<code>beginWork</code>完成，React会将<code>pendingProps</code>更新到<code>memoizedProps</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">workInProgress</span>) </span>&#123;
    ...
    next = beginWork(current$$1, workInProgress, nextRenderExpirationTime);
    workInProgress.memoizedProps = workInProgress.pendingProps;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后调用的<code>completeWork</code>和我们看过的<code>beginWork</code>相似，基本上是一个大的switch语句。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeWork</span>(<span class="hljs-params">current, workInProgress, ...</span>) </span>&#123;
    ...
    <span class="hljs-keyword">switch</span> (workInProgress.tag) &#123;
        <span class="hljs-keyword">case</span> FunctionComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> ClassComponent: &#123;...&#125;
        <span class="hljs-keyword">case</span> HostComponent: &#123;
            ...
            updateHostComponent(current, workInProgress, ...);
        &#125;
        <span class="hljs-keyword">case</span> ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于<code>span</code>Fiber节点是<code>HostComponent</code>，它会执行<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fcbbc2b6c4d0d8519145560bd8183ecde55168b12%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.js%23L686" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberBeginWork.js#L686" ref="nofollow noopener noreferrer">updateHostComponent</a>函数。在这个函数中React大体上做了这些事：</p>
<ul>
<li>准备DOM更新</li>
<li>把它们加到<code>span</code>fiber的<code>updateQueue</code></li>
<li>添加effect用于更新DOM</li>
</ul>
<p>在这些操作执行前，<code>span</code>Fiber节点看起来像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">0</span>
    <span class="hljs-attr">updateQueue</span>: <span class="hljs-literal">null</span>
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>works完成后它看起来像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">4</span>,
    <span class="hljs-attr">updateQueue</span>: [<span class="hljs-string">"children"</span>, <span class="hljs-string">"1"</span>],
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意<code>effectTag</code>和<code>updateQueue</code>字段的差异。它不再是<code>0</code>，它的值是<code>4</code>。用二进制表示是<code>100</code>，意味着设置了第3位，正是<code>Update</code>副作用的标志位。这是React在接下来的commit阶段对这个节点唯一要做的任务。<code>updateQueue</code>保存着用于更新的载荷。</p>
<p>一旦React处理完<code>ClickCounter</code>级它的子节点，<code>render</code>阶段结束。现在它可以将完成的替代树赋值给<code>FiberRoot</code>的<code>finishedWork</code>属性。这是需要被刷新到屏幕上的新树。它可以在<code>render</code>阶段之后马上被处理，或这当React被浏览器给予时间时再处理。</p>
<h2 data-id="heading-8">Effects list</h2>
<p>在我们的例子中，由于<code>span</code>节点<code>ClickCounter</code>组件有副作用，React将添加指向<code>span</code>Fiber节点的链接到<code>HostFiber</code>的<code>firstEffect</code>属性。</p>
<p>React在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fd5e1bf07d086e4fc1998653331adecddcd0f5274%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L999" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/d5e1bf07d086e4fc1998653331adecddcd0f5274/packages/react-reconciler/src/ReactFiberScheduler.js#L999" ref="nofollow noopener noreferrer">compliteUnitOfWork</a>函数内构建effects list。这是带有更新<code>span</code>节点文本和调用<code>ClickCounter</code>上hooks副作用的Fiber树看起来的样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccc1deb97dc543abaca5c0a979eaf938~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是由有副作用的节点组成的线性列表：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c39fef6347fd4c3cb64b606d64f51f0e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">Commit阶段</h2>
<p>这个阶段开始于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L2306" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L2306" ref="nofollow noopener noreferrer">completeRoot</a>函数。它在做其他工作之前，它将<code>FiberRoot</code>的<code>finishedWork</code>属性设为<code>null</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">root.finishedWork = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于之前的<code>render</code>阶段不同的是，<code>commit</code>阶段总是同步的，这样它可以安全地更新<code>HostRoot</code>来表示commit work开始了。</p>
<p><code>commit</code>阶段是React更新DOM和调用突变后生命周期方法<code>componentDidUpdate</code>的地方。为此，它遍历在<code>render</code>阶段中构建的effects list并应用它们。</p>
<p>有以下在<code>render</code>阶段为<code>span</code>和<code>ClickCounter</code>定义的effects：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123; <span class="hljs-attr">type</span>: ClickCounter, <span class="hljs-attr">effectTag</span>: <span class="hljs-number">5</span> &#125;
&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'span'</span>, <span class="hljs-attr">effectTag</span>: <span class="hljs-number">4</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ClickCounter</code>的effect tag的值是<code>5</code>或二进制的<code>101</code>，定义了对于类组件基本上转换为<code>componentDidUpdate</code>生命周期方法的<code>Update</code>工作。最低位也被设置了，表示该Fiber节点在<code>render</code>阶段的所有工作都已完成。</p>
<p><code>span</code>的effect tag的值是<code>4</code>或二进制的<code>100</code>，定义了原生组件DOM更新的<code>update</code>工作。这个例子中的<code>span</code>元素，React需要更新这个元素的<code>textContent</code>。</p>
<h2 data-id="heading-10">应用effects</h2>
<p>让我们看看React如何应用这些effects。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L523" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L523" ref="nofollow noopener noreferrer">commitRoot</a>函数用于应用这些effects，由3个子函数组成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params">root, finishedWork</span>) </span>&#123;
    commitBeforeMutationLifecycles()
    commitAllHostEffects();
    root.current = finishedWork;
    commitAllLifeCycles();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个子函数都实现了一个循环，该循环用于遍历effects list并检查这些effects的类型。当发现effect和函数的目的有关时就应用它。我们的例子中，它会调用<code>ClickCounter</code>组件的<code>componentDidUpdate</code>生命周期方法，更新<code>span</code>元素的文本。</p>
<p>第一个函数 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Ffefa1269e2a67fa5ef0992d5cc1d6114b7948b7e%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberCommitWork.js%23L183" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/fefa1269e2a67fa5ef0992d5cc1d6114b7948b7e/packages/react-reconciler/src/ReactFiberCommitWork.js#L183" ref="nofollow noopener noreferrer">commitBeforeMutationLifeCycles</a> 寻找 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fb87aabdfe1b7461e7331abb3601d9e6bb27544bc%2Fpackages%2Fshared%2FReactSideEffectTags.js%23L25" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/b87aabdfe1b7461e7331abb3601d9e6bb27544bc/packages/shared/ReactSideEffectTags.js#L25" ref="nofollow noopener noreferrer">Snapshot</a> effect然后调用<code>getSnapshotBeforeUpdate</code>方法。但是，我们在<code>ClickCounter</code>组件中没有实现该方法，React在<code>render</code>阶段没有添加这个effect。所以在我们的例子中，这个函数不做任何事。</p>
<h2 data-id="heading-11">DOM更新</h2>
<p>接下来React执行 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F95a313ec0b957f71798a69d8e83408f40e76765b%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L376" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L376" ref="nofollow noopener noreferrer">commitAllHostEffects</a> 函数。这儿是React将<code>span</code>元素的t文本由<code>0</code>变为<code>1</code>的地方。<code>ClickCounter</code> fiber没有要做的，因为类组件的节点没有任何DOM更新。</p>
<p>这个函数的主旨是选择正确类型的effect并应用相应的操作。在我们的例子中我们需要跟新<code>span</code>元素的文本，所以我们采用<code>Update</code>分支：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateHostEffects</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (primaryEffectTag) &#123;
      <span class="hljs-keyword">case</span> Placement: &#123;...&#125;
      <span class="hljs-keyword">case</span> PlacementAndUpdate: &#123;...&#125;
      <span class="hljs-keyword">case</span> Update:
        &#123;
          <span class="hljs-keyword">var</span> current = nextEffect.alternate;
          commitWork(current, nextEffect);
          <span class="hljs-keyword">break</span>;
        &#125;
      <span class="hljs-keyword">case</span> Deletion: &#123;...&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随着<code>commitWork</code>执行，最终会进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2F8a8d973d3cc5623676a84f87af66ef9259c3937c%2Fpackages%2Freact-dom%2Fsrc%2Fclient%2FReactDOMComponent.js%23L326" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/8a8d973d3cc5623676a84f87af66ef9259c3937c/packages/react-dom/src/client/ReactDOMComponent.js#L326" ref="nofollow noopener noreferrer">updateDOMProperties</a>函数。它使用在<code>render</code>阶段添加到Fiber节点的<code>updateQueue</code>载荷更新<code>span</code>元素的<code>textContent</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDOMProperties</span>(<span class="hljs-params">domElement, updatePayload, ...</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < updatePayload.length; i += <span class="hljs-number">2</span>) &#123;
    <span class="hljs-keyword">const</span> propKey = updatePayload[i];
    <span class="hljs-keyword">const</span> propValue = updatePayload[i + <span class="hljs-number">1</span>];
    <span class="hljs-keyword">if</span> (propKey === STYLE) &#123; ...&#125; 
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propKey === DANGEROUSLY_SET_INNER_HTML) &#123;...&#125; 
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propKey === CHILDREN) &#123;
      setTextContent(domElement, propValue);
    &#125; <span class="hljs-keyword">else</span> &#123;...&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用DOM更新后，React将<code>finishedWork</code>赋值给<code>HostRoot</code>。它将替代树是设为当前树：</p>
<pre><code class="hljs language-js copyable" lang="js">root.current = finishedWork;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">调用突变后生命周期hooks</h2>
<p>剩下的函数是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fd5e1bf07d086e4fc1998653331adecddcd0f5274%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberScheduler.js%23L479" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/d5e1bf07d086e4fc1998653331adecddcd0f5274/packages/react-reconciler/src/ReactFiberScheduler.js#L479" ref="nofollow noopener noreferrer"><strong><strong>commitAllLifecycles</strong></strong></a>。这是 React 调用突变后生命周期方法的地方。在<code>render</code>阶段，React为<code>ClickCounter</code>组件添加<code>Update</code> effect。这是<code>commitAllLifecycles</code>寻找的effects之一并调用<code>componentDidUpdate</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitAllLifeCycles</span>(<span class="hljs-params">finishedRoot, ...</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (nextEffect !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> effectTag = nextEffect.effectTag;

        <span class="hljs-keyword">if</span> (effectTag & (Update | Callback)) &#123;
            <span class="hljs-keyword">const</span> current = nextEffect.alternate;
            commitLifeCycles(finishedRoot, current, nextEffect, ...);
        &#125;
        
        <span class="hljs-keyword">if</span> (effectTag & Ref) &#123;
            commitAttachRef(nextEffect);
        &#125;
        
        nextEffect = nextEffect.nextEffect;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数也更新<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Frefs-and-the-dom.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/refs-and-the-dom.html" ref="nofollow noopener noreferrer">refs</a>，但是由于我们没有使用这个特性，所以没什么作用。这个方法在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fe58ecda9a2381735f2c326ee99a1ffa6486321ab%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberCommitWork.js%23L351" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/e58ecda9a2381735f2c326ee99a1ffa6486321ab/packages/react-reconciler/src/ReactFiberCommitWork.js#L351" ref="nofollow noopener noreferrer">commitLifeCycles</a>函数中被调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitLifeCycles</span>(<span class="hljs-params">finishedRoot, current, ...</span>) </span>&#123;
  ...
  <span class="hljs-keyword">switch</span> (finishedWork.tag) &#123;
    <span class="hljs-keyword">case</span> FunctionComponent: &#123;...&#125;
    <span class="hljs-keyword">case</span> ClassComponent: &#123;
      <span class="hljs-keyword">const</span> instance = finishedWork.stateNode;
      <span class="hljs-keyword">if</span> (finishedWork.effectTag & Update) &#123;
        <span class="hljs-keyword">if</span> (current === <span class="hljs-literal">null</span>) &#123;
          instance.componentDidMount();
        &#125; <span class="hljs-keyword">else</span> &#123;
          ...
          instance.componentDidUpdate(prevProps, prevState, ...);
        &#125;
      &#125;
    &#125;
    <span class="hljs-keyword">case</span> HostComponent: &#123;...&#125;
    <span class="hljs-keyword">case</span> ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以看出，这是首次渲染时React调用组件<code>componentDidMount</code>方法的函数。</p></div>  
</div>
            