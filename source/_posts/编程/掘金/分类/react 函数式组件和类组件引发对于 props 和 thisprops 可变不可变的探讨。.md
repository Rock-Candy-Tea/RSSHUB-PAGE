
---
title: 'react 函数式组件和类组件引发对于 props 和 this.props 可变不可变的探讨。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7378'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 20:31:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=7378'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当我在网上搜这个问题 <strong>函数式组件和类组件的区别</strong> 的时候，看到的都是关于大神这篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Foverreacted.io%2Fzh-hans%2Fhow-are-function-components-different-from-classes%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://overreacted.io/zh-hans/how-are-function-components-different-from-classes/" ref="nofollow noopener noreferrer">文章</a>的复制，大家没看过的可以先看看，最主要的一个问题就是讨论就是类组件的 this 是可变的，函数组件的 props 是不可变的，但是却没看到一篇文章说<strong>为什么</strong>，都是文章中说的<strong>React 对于 this 是可变的，对于 props 是不可变的</strong>。我想说***。</p>
<h2 data-id="heading-1">我来说说原因</h2>
<h3 data-id="heading-2">class 组件和类组件的渲染机制</h3>
<p>class 是通过 new class() 创建的实例，调用 render 执行渲染，函数是直接执行渲染。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">jsx</span> /></span></span>
  &#125;
&#125;
<span class="hljs-keyword">new</span> App().render();

<span class="hljs-comment">// 函数组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">jsx</span> /></span></span>
&#125;
App();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">class 组件和类组件的更新机制</h3>
<ul>
<li>组件的 state 变化，class 是通过 this.render() 更新的组件，在执行相关的生命周期。</li>
<li>函数是重新调用方法更新（这也是为什么函数的方法会执行多次的原因）。</li>
</ul>
<h3 data-id="heading-4">props 并不是不可变</h3>
<p>准确来说是 props 在当前作用域不可变，因为形成了闭包。而 props 本身就会变. props依赖于父组件，父组件传给子组件参数改变时候，props就已经变了。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// props 可变，点击  Change Value，你就已经看到 value 的值已经变了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Component</span>(<span class="hljs-params">&#123; value, setValue &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setValue("Change Value");
        &#125;&#125;
      >
        Change Value
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-string">"value"</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">setValue</span>=<span class="hljs-string">&#123;setValue&#125;</span> /></span></span>;
&#125;

<span class="hljs-comment">// props 不可变</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Component</span>(<span class="hljs-params">&#123; value, setValue &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> input = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span>, value);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setValue("Change Value");
          input();
        &#125;&#125;
      >
        Change Value
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-string">"value"</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">setValue</span>=<span class="hljs-string">&#123;setValue&#125;</span> /></span></span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">原因</h3>
<ul>
<li>
<p>函数式组件会形成闭包，劫持 props，所以 props 不可变，</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 如上: props 并不是不可变</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>class 不会形成闭包，this 拿到的一直是最新的值。当 state 改变时，会调用 render 方法更新组件，doSomething 方法并没有形成闭包</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.props.doSomething()&#125;>&#123;this.props.value&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"123"</span> &#125;;
  &#125;

  doSomething = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"value"</span> &#125;);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span>, <span class="hljs-built_in">this</span>.state.value);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">doSomething</span>=<span class="hljs-string">&#123;this.doSomething&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.value&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>class 如何形成闭包</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> props = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-keyword">const</span> input = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"pre props"</span>, props);
    &#125;;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"cur props"</span>, <span class="hljs-built_in">this</span>.props);
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          this.props.doSomething();
          input();
        &#125;&#125;
      >
        Click
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"value"</span> &#125;;
  &#125;

  doSomething = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"cur value"</span> &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"async cur value"</span>, <span class="hljs-built_in">this</span>.state.value);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"cur value"</span>, <span class="hljs-built_in">this</span>.state.value);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">doSomething</span>=<span class="hljs-string">&#123;this.doSomething&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.value&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-6">总结</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fnice-keldysh-mpxic%3Ffile%3D%2Fsrc%2FClass.tsx%3A577-626" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/nice-keldysh-mpxic?file=/src/Class.tsx:577-626" ref="nofollow noopener noreferrer">上面运行的 Demo</a></p>
<p><strong>闭包，自己看去吧</strong></p></div>  
</div>
            