
---
title: 'React 18 如何支持 Strict Effects'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5827'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 18:24:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=5827'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文来源于翻译文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F18" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/18" ref="nofollow noopener noreferrer">How to support strict effects</a></p>
</blockquote>
<h2 data-id="heading-0">概述</h2>
<p><em>如果你还没有阅读上一篇关于 StrictMode 变化的文章，可以点击<a href="https://juejin.cn/post/6994260903193477128" target="_blank" title="https://juejin.cn/post/6994260903193477128">这里</a>查看</em></p>
<p>首先，让我们看一个组件代码示例：</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ExampleComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// Effect setup code...</span>

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// Effect cleanup code...</span>
    &#125;;
  &#125;, []);

  useLayoutEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// Layout effect setup code...</span>

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// Layout effect cleanup code...</span>
    &#125;;
  &#125;, []);

  <span class="hljs-comment">// Render stuff...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个组件在 mount 和 unmount 时会执行一些 effect，通常这些 effect 只被执行一次（在组件挂载之后），清除函数也只被执行一次（在组件卸载之后）。在 Strict Effects 模式，会触发以下流程：</p>
<ul>
<li>React 渲染组件</li>
<li>React 挂载组件
<ul>
<li>执行 layout effect 启动逻辑代码</li>
<li>执行 effect 启动逻辑代码</li>
</ul>
</li>
<li>React 模拟组件被隐藏或卸载
<ul>
<li>执行 layout effect 清除逻辑代码</li>
<li>执行 effect 清除逻辑代码</li>
</ul>
</li>
<li>React 模拟组件重新显示或挂载
<ul>
<li>执行 layout effect 启动逻辑代码</li>
<li>执行 effect 启动逻辑代码</li>
</ul>
</li>
</ul>
<p>只要一个 effect 在其自身之后进行清理（必要时返回一个清除函数），这通常不会导致问题。大多数 effect 至少有一个依赖项。因此，它们已经能够适应重新挂载多次，并且可以不需要做任何更改。</p>
<p>不过为了多次挂载（卸载）之后组件正常运行，如果 effect 只在挂载时才运行，那么可能需要对 effect 做一些更改。最有可能因为挂载多次而受到影响，导致需要修改 effect 的情况分为以下两类：</p>
<ul>
<li>在卸载时需要执行清理操作的 effect</li>
<li>只执行一次的 effect（挂载时或依赖变化时执行）</li>
</ul>
<h2 data-id="heading-1">Effect 清理操作是对称的</h2>
<p>无论是添加监听事件还是某些命令式 API，一般来说，如果 effect 返回了一个清除函数，那么它应该与启动函数是对应的。当前，大部分组件都是使用下面的示例模式：</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-comment">// A Ref (or Memo) is used to init and cache some imperative API.</span>
<span class="hljs-keyword">const</span> ref = useRef(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">if</span> (ref.current === <span class="hljs-literal">null</span>) &#123;
  ref.current = <span class="hljs-keyword">new</span> SomeImperativeThing();
&#125;

<span class="hljs-comment">// Note this could be useLayoutEffect too; same pattern.</span>
useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> someImperativeThing = ref.current;
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// And an unmount effect (or layout effect) is used to destroy it.</span>
    someImperativeThing.destroy();
  &#125;;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果上面的组件被卸载并重新挂载，那么命令式的 API （这里是指 <code>ref</code>）很可能会被破坏(毕竟，它在第一次卸载后就被销毁了）。要解决这个问题，我们需要在再次挂载时（重新）初始化 <code>ref</code>。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-comment">// Don't use a Ref to initialize SomeImperativeThing!</span>

useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// Initialize an imperative API inside of the same effect that destroys it.</span>
  <span class="hljs-comment">// This way it will be recreated if the component gets remounted.</span>
  <span class="hljs-keyword">const</span> someImperativeThing = <span class="hljs-keyword">new</span> SomeImperativeThing();

  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    someImperativeThing.destroy();
  &#125;;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时，其他函数（如事件处理）也需要以命令的形式进行交互。在这种情况下，可以使用 ref 来共享该值。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-comment">// Use a Ref to hold the value, but initialize it in an effect.</span>
<span class="hljs-keyword">const</span> ref = useRef(<span class="hljs-literal">null</span>);

useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// Initialize an imperative API inside of the same effect that destroys it.</span>
  <span class="hljs-comment">// This way it will be recreated if the component gets remounted.</span>
  <span class="hljs-keyword">const</span> someImperativeThing = ref.current = <span class="hljs-keyword">new</span> SomeImperativeThing();

  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    someImperativeThing.destroy();
  &#125;;
&#125;, []);

<span class="hljs-keyword">const</span> handeThing = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> someImperativeThing = ref.current;
  <span class="hljs-comment">// Now we can call methods on the imperative API...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在有些场景中可能需要与其他组件共享命令式 API。在这种情况下，可以使用惰性初始化函数暴露出相关的 API。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-comment">// This ref holds the imperative thing.</span>
<span class="hljs-comment">// It should only be referenced by the current component.</span>
<span class="hljs-keyword">const</span> ref = useRef(<span class="hljs-literal">null</span>);

<span class="hljs-comment">// This lazy init function ref can be shared with other components,</span>
<span class="hljs-comment">// although it should only be called from an effect or an event handler.</span>
<span class="hljs-comment">// It should not be called during render.</span>
<span class="hljs-keyword">const</span> getterRef = useRef(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (ref.current === <span class="hljs-literal">null</span>) &#123;
    ref.current = <span class="hljs-keyword">new</span> SomeImperativeThing();
  &#125;
  <span class="hljs-keyword">return</span> ref.current;
&#125;);

useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// This component doesn't need to (re)create the imperative API.</span>
  <span class="hljs-comment">// Any code that needs it will do this automatically by calling the getter.</span>

  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// It's possible that nothing called the getter function,</span>
    <span class="hljs-comment">// in which case we don't have to cleanup the imperative code.</span>
    <span class="hljs-keyword">if</span> (ref.current !== <span class="hljs-literal">null</span>) &#123;
      ref.current.destroy();
      ref.current = <span class="hljs-literal">null</span>;
    &#125;
  &#125;;
&#125;, []);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">只执行一次的 effect 可以使用 ref</h2>
<p>如果 effect 没有清理函数，不需要任何更改即可支持新的特性。让我们来看一个将日志发送到服务器的 effect。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX">useEffect(<span class="hljs-function">() =></span> &#123;
  SomeTrackingAPI.logImpression();
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 effect 的作用是在用户浏览了特定的内容时要做一下日志记录。但是，当该内容被隐藏并且再展示给用户时，这个过程要如何处理呢？是否应该再发送一次日志呢？（这个场景与 tabs 标签页的切换类似）如果需要再次发送日志，那么就不需要更改 effect。如果要求只发送一次日志，那么我们应该使用 ref，改动之后的代码如下：</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-keyword">const</span> didLogRef = useRef(<span class="hljs-literal">false</span>);

useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// In this case, whether we are mounting or remounting,</span>
  <span class="hljs-comment">// we use a ref so that we only log an impression once.</span>
  <span class="hljs-keyword">if</span> (didLogRef.current === <span class="hljs-literal">false</span>) &#123;
    didLogRef.current = <span class="hljs-literal">true</span>;

    SomeTrackingAPI.logImpression();
  &#125;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">"auto focus" 然后恢复 focus</h2>
<p>这里介绍一种比较有趣的业务场景：当点击一个按钮时会打开一个弹窗，并自动 focus 到弹窗的某个元素上；当关闭弹窗时，要重新 focus 到之前触发弹窗的按钮上 (也就是恢复到打开弹窗之前的 focus 状态)。在下面的代码中，<code>restoreFocus</code> 记录要恢复 focus 状态的元素。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Modal</span>(<span class="hljs-params">&#123; children &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> restoreFocus = React.useRef(<span class="hljs-literal">null</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleFocus</span>(<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (restoreFocus.current === <span class="hljs-literal">null</span>) &#123;
      restoreFocus.current = event.relatedTarget;
    &#125;
  &#125;

  React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (restoreFocus.current !== <span class="hljs-literal">null</span>) &#123;
        restoreFocus.current.focus();
        restoreFocus.current = <span class="hljs-literal">null</span>;
      &#125;
    &#125;;
  &#125;, []);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onFocus</span>=<span class="hljs-string">&#123;handleFocus&#125;</span>></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在下面的代码中通过按钮控制弹窗的显示和隐藏。正常情况下，打开弹窗后，由于 <code><input></code>  设置了 <code>autoFocus</code> 属性会自动聚焦。进而触发了 Modal 中的 <code>handleFocus</code>，并将<code><button></code> 元素记录到 <code>restoreFocus</code>。</p>
<pre><code class="hljs language-JSX copyable" lang="JSX">  <span class="hljs-keyword">const</span> [open, setOpen] = React.useState(<span class="hljs-literal">false</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Fragment</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setOpen(!open)&#125;>&#123;open ? "close" : "open"&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#123;open && (
        <span class="hljs-tag"><<span class="hljs-name">Modal</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">autoFocus</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span>
      )&#125;
    <span class="hljs-tag"></<span class="hljs-name">React.Fragment</span>></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，在 Strict Effects 模式下会通过元素的隐藏和展示来模仿卸载和重新挂载这个过程时，所以当卸载时会聚焦到 <code><button></code> 元素上，由于重新挂载时元素只是重新显示，这时不会再聚焦到 <code><input></code> 。所以最终看到的结果与上面提到的情况完全不同。</p>
<p>可以通过如下方式实现自动聚焦：</p>
<pre><code class="hljs language-JSX copyable" lang="JSX">  <span class="hljs-keyword">const</span> [open, setOpen] = React.useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> target = React.useRef(<span class="hljs-literal">null</span>);

  React.useEffect(<span class="hljs-function">() =></span> &#123;
    target.current.focus();
  &#125;, []);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Fragment</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setOpen(!open)&#125;>&#123;open ? "close" : "open"&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#123;open && (
        <span class="hljs-tag"><<span class="hljs-name">Modal</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;target&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span>
      )&#125;
    <span class="hljs-tag"></<span class="hljs-name">React.Fragment</span>></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">上面的示例并未覆盖所有情形</h2>
<p>本文只涵盖了一些最常见的场景，但并不是详尽的列表。我们计划在将来写一些不太常见的案例。同时，如果您不确定 effect 是否应该运行多次，或者 effect 与上面场景不匹配，请咨询我们，我们将提供帮助。</p>
<hr>
<p>微信搜索 「ikoofe」, 关注公众号 「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fp3-juejin.byteimg.com%2Ftos-cn-i-k3u1fbpfcp%2Ff37bc98a8bae45269ca7982cbb0d344a~tplv-k3u1fbpfcp-zoom-1.image" target="_blank" rel="nofollow noopener noreferrer" title="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f37bc98a8bae45269ca7982cbb0d344a~tplv-k3u1fbpfcp-zoom-1.image" ref="nofollow noopener noreferrer">KooFE前端团队</a>」, 不定期发布前端技术文章。</p></div>  
</div>
            