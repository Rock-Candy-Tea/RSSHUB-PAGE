
---
title: 'React & Typescript：组件的入门实例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9205'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 02:29:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=9205'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">React 组件的演化</h2>



































<table><thead><tr><th>组件复用方式</th><th>优势</th><th>劣势</th><th>状态</th></tr></thead><tbody><tr><td>类组件（<code>Class</code>）</td><td>发展时间长，接受度广泛</td><td>只能继承父类</td><td>作为一种传统开发模式，会长期存在</td></tr><tr><td><del><code>Mixin</code></del></td><td>可以复制任意对象的任意多个方法，实现组件间的复用</td><td>组件间相互依赖、耦合，可能产生冲突，不利于维护</td><td>被官方抛弃</td></tr><tr><td>高阶组件（HOC）</td><td>利用装饰器模式，在不改变组件的基础上，动态地为其添加新的能力</td><td>嵌套过多调试困难，需要遵循某些约定（不改变原始组件，透传 <code>props</code> 等）</td><td>能力强大，广泛引用</td></tr><tr><td><code>Hooks</code></td><td>替代类组件，多个 <code>Hooks</code> 间互不影响，避免嵌套地狱，开发效率高</td><td>切换新思维需要成本</td><td><code>React</code> 的未来（官方主推）</td></tr></tbody></table>
<h2 data-id="heading-1">函数组件</h2>
<h3 data-id="heading-2">普通函数组件</h3>
<p>上一篇中，我们创建了一个无状态组件（没有状态影响，作为纯静态展示） <code><Hello /></code>，同时它也是一个函数组件。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;

<span class="hljs-keyword">interface</span> Greeting &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  firstName: <span class="hljs-built_in">string</span>;
  lastName: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">const</span> Hello = <span class="hljs-function">(<span class="hljs-params">props: Greeting</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>hello &#123;props.name&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>;

Hello.defaultProps = &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span>,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Hello;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">React.FC</h3>
<p>在 react 的声明文件中，对函数组件单独定义了一个类型 -- <code>React.FC</code>:</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">type</span> React.FC<P = &#123;&#125;> = React.FunctionComponent<P>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在使用 <code>React.FC</code> 重新定义一下 <code><Hello /></code>：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> Hello: React.FC<Greeting> = <span class="hljs-function">(<span class="hljs-params">&#123; name, firstName, lastName &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>hello &#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用 React.FC 后的区别</h3>
<p><code>FC</code> 是 <code>FunctionComponent</code> 的简写，这个类型定义了默认的 <code>props</code> (如 <code>children</code>)。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> Hello: React.FC<Greeting> = <span class="hljs-function">(<span class="hljs-params">&#123; name, firstName, lastName, children &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>hello &#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用 <code>React.FC</code>后定义 <code>defaultProps</code> 时，默认属性必须是可选的（这和普通函数组件不同）：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">interface</span> Greeting &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  firstName?: <span class="hljs-built_in">string</span>;
  lastName?: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">const</span> Hello: React.FC<Greeting> = <span class="hljs-function">(<span class="hljs-params">&#123; name, firstName, lastName, children &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>hello &#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);

Hello.defaultProps = &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">小结</h3>
<p>在 <code>TypeScript</code> 中，函数组件需要为 <code>props</code> 定义类型。</p>
<h2 data-id="heading-6">类组件</h2>
<h3 data-id="heading-7">Component</h3>
<p>类组件需要继承 <code>Components</code> 组件，在 <code>react</code> 的声明文件中，<code>Component</code> 被定义为泛型类：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// P: 属性的类型，默认&#123;&#125;</span>
<span class="hljs-comment">// S: 状态的类型，默认&#123;&#125;</span>
<span class="hljs-comment">// SS: snapshot</span>
(alias) <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span><<span class="hljs-title">P</span> </span>= &#123;&#125;, S = &#123;&#125;, SS = <span class="hljs-built_in">any</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">实现</h3>
<p>将上面的函数组件改造成类组件：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// src/componets/demo/HellpClass.tsx</span>
<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;

<span class="hljs-keyword">interface</span> Greeting &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  firstName: <span class="hljs-built_in">string</span>;
  lastName: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> State &#123;
  <span class="hljs-attr">count</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloClass</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span><<span class="hljs-title">Greeting</span>, <span class="hljs-title">State</span>> </span>&#123;
  <span class="hljs-comment">// 初始化 state</span>
  <span class="hljs-attr">state</span>: State = &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;;
  <span class="hljs-comment">// 默认属性值</span>
  <span class="hljs-keyword">static</span> defaultProps = &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span>,
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>hello &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HelloClass;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>setState</code> 为 <code><HelloClass /></code> 添加一个点击计数功能。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloClass</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span><<span class="hljs-title">Greeting</span>, <span class="hljs-title">State</span>> </span>&#123;
  <span class="hljs-attr">state</span>: State = &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;;
  <span class="hljs-keyword">static</span> defaultProps = &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span>,
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>您点击了 &#123;this.state.count&#125; 次<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span>
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
            this.setState(&#123; count: this.state.count + 1 &#125;);
          &#125;&#125;
        >
          hello &#123;this.props.name&#125;
        <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">小结</h3>
<p>在 <code>TypeScript</code> 中，类组件需要为 <code>props</code> 和 <code>state</code> 定义类型。</p>
<h2 data-id="heading-10">高阶组件</h2>
<p>我们现在要利用高阶组件包装一下 <code><HelloClass /></code>，包装后的组件有一个新属性 <code>loading</code>，通过该属性控制被包装组件的 显示/隐藏。</p>
<h3 data-id="heading-11">React.ComponentType</h3>
<p>指定被包装组件的类型为 <code>React.ComponentType</code>（一种 <code>React</code> 预定义类型），既可以是类组件，也可以是函数组件：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> React.ComponentType<P = &#123;&#125;> = React.ComponentClass<P, <span class="hljs-built_in">any</span>> | React.FunctionComponent<P>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">实现</h3>
<p>添加 <code><HelloHOC /></code> 组件：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> HelloClass <span class="hljs-keyword">from</span> <span class="hljs-string">"./HelloClass"</span>;

<span class="hljs-keyword">interface</span> Loading &#123;
  <span class="hljs-attr">loading</span>: <span class="hljs-built_in">boolean</span>;
&#125;

<span class="hljs-comment">/*
 ** WrapperComponetn: 需要被包装的组件
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HelloHOC</span><<span class="hljs-title">P</span>>(<span class="hljs-params">WrapperComponetn: React.ComponentType<P></span>) </span>&#123;
  <span class="hljs-comment">// 定义 props 为 P 和 Loading 的交叉类型</span>
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span><<span class="hljs-title">P</span> & <span class="hljs-title">Loading</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 解构 props，拆分出 loading</span>
      <span class="hljs-keyword">const</span> &#123; loading, ...props &#125; = <span class="hljs-built_in">this</span>.props;
      <span class="hljs-comment">// &#123;...props&#125;：属性透传</span>
      <span class="hljs-keyword">return</span> loading ? (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      ) : (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrapperComponetn</span> &#123;<span class="hljs-attr">...</span>(<span class="hljs-attr">props</span> <span class="hljs-attr">as</span> <span class="hljs-attr">P</span>)&#125; /></span></span>
      );
    &#125;
  &#125;;
&#125;

<span class="hljs-comment">// 导出经过高阶组件包装后的组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HelloHOC(HelloClass);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">有个报错</h3>
<p>我们在 <code>index.tsx</code> 中引入这个组件，这时会有一个报错：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> HelloHOC <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/demo/HelloHOC"</span>;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">HelloHOC</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"typescript"</span> <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;true&#125;</span> /></span></span>,
  <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".app"</span>)[<span class="hljs-number">0</span>]
);

<span class="hljs-comment">// ERROR! 因为 HelloClass 的静态属性 defaultProps 传不出来。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解决方案</strong>：将 <code>defaultProps</code> 设置为可选属性。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">interface</span> Greeting &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  firstName?: <span class="hljs-built_in">string</span>;
  lastName?: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">小结</h3>
<p>在 <code>TypeScript</code> 中，高阶组件的使用会遇到很多类型问题，还有可能遇到一些已知的 <code>bug</code>，但这并不是高阶组件本身的问题，而是因为 <code>react</code> 声明文件没有很好的兼容。其实官方最推荐的是使用 <code>Hooks</code>，下面就再用 <code>Hooks</code> 实现一下吧</p>
<h2 data-id="heading-15">hooks</h2>
<p><code>hooks</code> 也是一种函数组件，对比类组件，明显简化了许多：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React, &#123; useEffect, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;

<span class="hljs-keyword">interface</span> Greeting &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  firstName: <span class="hljs-built_in">string</span>;
  lastName: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">const</span> HelloHooks = <span class="hljs-function">(<span class="hljs-params">props: Greeting</span>) =></span> &#123;
  <span class="hljs-comment">// 定义 [组件的状态，设置状态的方法]，给定状态的初始值：不需要再定义类型</span>
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [text, setText] = useState<<span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>您点击了 &#123;count&#125; 次<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setCount(count + 1);
        &#125;&#125;
      >
        hello &#123;props.name&#125;
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;;

HelloHooks.defaultProps = &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span>,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HelloHooks;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用 <code>useEffect</code> 新增一个功能： 点击超过 5 次给出提示。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> HelloHooks = <span class="hljs-function">(<span class="hljs-params">props: Greeting</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [text, setText] = useState<<span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>);

  <span class="hljs-comment">// 只有当 count 改变时，渲染逻辑才会执行。</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (count > <span class="hljs-number">5</span>) &#123;
      setText(<span class="hljs-string">"休息一下"</span>);
    &#125;
  &#125;, [count]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        您点击了 &#123;count&#125; 次，&#123;text&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setCount(count + 1);
        &#125;&#125;
      >
        hello &#123;props.name&#125;
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">为什么要定义为泛型？</h2>
<p>不用泛型变量，<code>this.props</code> 的类型无法确定，在内部只能使用类型断言来访问属性：</p>
<pre><code class="hljs language-ts copyable" lang="ts">(<span class="hljs-built_in">this</span>.props <span class="hljs-keyword">as</span> Greeting).name;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样很麻烦，而 <code>React</code> 声明文件把这些约束关系都用泛型定义好了。</p></div>  
</div>
            