
---
title: '写了3个月React，我学到了什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c7354f4196444e8cf926895e37d7ba~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 01:28:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c7354f4196444e8cf926895e37d7ba~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文链接：
<a href="https://github.com/FrankKai/FrankKai.github.io/issues/247" target="_blank" rel="nofollow noopener noreferrer">React那些事儿</a>
<a href="https://github.com/FrankKai/FrankKai.github.io/issues/248" target="_blank" rel="nofollow noopener noreferrer">React hooks那些事儿</a></p>
<p>新环境从Vue转到了React技术栈，这个过程还是比较有趣的。</p>
<p>在React中会看到与Vue很多相似的地方，也有一些不同的地方，学习过程中遇到一些疑惑，做了记录。</p>
<ul>
<li>useRef如何解决空指针问题？</li>
<li>useEffect与useCallback(useMemo)的区别是什么？</li>
<li>React除了可以通过props传递数据以外，如何通过context方式传递数据?</li>
<li>React.createElement(Input, props)中的React.createElement如何理解？</li>
<li>react中的FC是什么?<code>FC<[interface]></code>是什么意思？主要用处及最简写法是怎样的？</li>
<li>React中FC的形参的props, context, propTypes, contextTypes, defaultProps, displayName是什么？</li>
<li><code>import &#123; MouseEvent &#125; from 'react'</code>是什么意思？SyntheticEvent是什么类型？</li>
<li><code>React.forwardRef</code>是什么意思？useImperativeHandle是什么意思？</li>
</ul>
<h3 data-id="heading-0">useRef如何解决空指针问题？</h3>
<p>通常来说，useRef用于引用组件的Dom节点。Vue中的ref则是引用一个vue组件。与Vue不同，react中的ref不仅仅是引用Dom节点，还可以生成一个内存不变的对象引用。</p>
<h4 data-id="heading-1">使用useState导致的空指针示例</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [foo, setFoo] = useState(<span class="hljs-literal">null</span>);

<span class="hljs-keyword">const</span> handler = <span class="hljs-function">() =></span> &#123;
    setFoo(<span class="hljs-string">"hello"</span>)
&#125;

useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 无论怎样foo都是null，给useEffect的deps加入foo也不行</span>
      <span class="hljs-keyword">if</span> (foo === <span class="hljs-string">"hello"</span>) &#123;
          <span class="hljs-comment">// do something...</span>
      &#125;
    &#125;
&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">使用useRef的正确示例（解决事件处理器中对象为null的问题）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> foo = useRef(<span class="hljs-literal">null</span>)

<span class="hljs-keyword">const</span> handler = <span class="hljs-function">() =></span> &#123;
    foo.current = <span class="hljs-string">"hello"</span>
&#125;

useEffect(<span class="hljs-function">() =></span> &#123;

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// foo.current为hello</span>
      <span class="hljs-keyword">if</span> (foo.current === <span class="hljs-string">"hello"</span>) &#123;
          <span class="hljs-comment">// do something...</span>
      &#125;
    &#125;
&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">useRef解决空指针问题的原因是什么？</h4>
<ul>
<li>组件生命周期期间，useRef指向的对象都是一直存在的</li>
<li>每次渲染时，useRef都指向同一个引用的对象</li>
</ul>
<p>总结起来就是：<strong>useRef生成的对象，在组件生命周期期间内存地址都是不变的。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> refContainer = useRef(initialValue);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>useRef returns a mutable ref object whose .current property is initialized to the passed argument (initialValue). The returned object will persist for the <strong>full lifetime of the component</strong>.</p>
<p>This works because useRef() creates a plain JavaScript object. The only difference between useRef() and creating a &#123;current: ...&#125; object yourself is that <strong>useRef will give you the same ref object on every render.</strong></p>
<p>总结一下会使用到useRef解决空指针问题的场景：</p>
<ul>
<li>事件处理器</li>
<li>setTimeout，setInterval</li>
</ul>
<h3 data-id="heading-4">useEffect与useCallback(useMemo)的区别是什么？</h3>
<p>浏览器执行阶段：<strong>可见修改（DOM操作，动画，过渡）->样式规则计算->计算空间和位置->绘制像素内容->多个层合成</strong>
前四个阶段都是针对元素的，最后一个是针对层的。由点到面。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c7354f4196444e8cf926895e37d7ba~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">执行时间不同</h4>
<p>useEffect在渲染完成后执行函数，更加准确的来说是在layout和paint完成之后。</p>
<blockquote>
<p>The function passed to useEffect will run <strong>after the render</strong> is committed to the screen.Unlike componentDidMount and componentDidUpdate, the function passed to useEffect fires <strong>after layout and paint</strong></p>
</blockquote>
<p>useCallback(useMemo)在渲染过程中执行函数。</p>
<blockquote>
<p>Remember that the function passed to useMemo runs during rendering.</p>
</blockquote>
<h4 data-id="heading-6">哪些适合在渲染完成后执行，哪些适合在渲染过程中执行</h4>
<p>渲染完成后执行：Mutations（DOM操作）, subscriptions（订阅）, timers, logging
渲染过程中执行：用于不依赖渲染完成的性能优化，状态一变更立即执行</p>
<h4 data-id="heading-7">一个例子阐明useEffect和useMemo的区别</h4>
<p>useMemo最主要解决的问题：<strong>怎么在DOM改变的时候，控制某些函数不被触发。</strong>
例如下面这个例子，在name变更的时候，useEffect会在DOM渲染完成后出发price的函数，而useMemo可以精准的只触发更新name的函数。</p>
<p>这是一个非常非常好的例子，更加详细的博文在这里：<a href="https://www.jianshu.com/p/94ace269414d" target="_blank" rel="nofollow noopener noreferrer">useMemo和useEffect有什么区别？怎么使用useMemo</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123;Fragment&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; useState, useEffect, useCallback, useMemo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">const</span> nameList = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'peer'</span>, <span class="hljs-string">'banana'</span>, <span class="hljs-string">'lemon'</span>]
<span class="hljs-keyword">const</span> Example = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> [price, setPrice] = useState(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">const</span> [name, setName] = useState(<span class="hljs-string">'apple'</span>)
    
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProductName</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'getProductName触发'</span>)
        <span class="hljs-keyword">return</span> name
    &#125;
    <span class="hljs-comment">// 只对name响应</span>
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name effect 触发'</span>)
        getProductName()
    &#125;, [name])
    
    <span class="hljs-comment">// 只对price响应</span>
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'price effect 触发'</span>)
    &#125;, [price])
  
    <span class="hljs-comment">// memo化的getProductName函数   🧬🧬🧬</span>
    <span class="hljs-keyword">const</span> memo_getProductName = useMemo(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name memo 触发'</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> name  <span class="hljs-comment">// 返回一个函数</span>
    &#125;, [name])

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Fragment</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;price&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>普通的name：&#123;getProductName()&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>memo化的：&#123;memo_getProductName ()&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setPrice(price+1)&#125;>价钱+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setName(nameList[Math.random() * nameList.length << 0])&#125;>修改名字<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Fragment</span>></span></span>
    )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Example
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击价钱+1按钮（通过useMemo，多余的memo_getProductName ()没有被触发，只触发price相关的函数）</p>
<blockquote>
<p>getProductName触发
price effect 触发</p>
</blockquote>
<p>点击修改名字按钮（通过useEffect，只触发name相关）</p>
<blockquote>
<p>name memo 触发
getProductName触发
name effect 触发
getProductName触发</p>
</blockquote>
<h5 data-id="heading-8">总结</h5>
<p>useEffect面对一些依赖于某个state的DOM渲染时，会出现一些性能问题，而useMemo可以优化这个问题。
最后，用一句话来概括useMemo的话，那就是：<strong>useMemo可以避免一些useEffect搞不定的不必要的重复渲染和重复执行问题。</strong></p>
<h3 data-id="heading-9">React除了可以通过props传递数据以外，如何通过context方式传递数据?</h3>
<p>假设组件层级较深，props需要一级一级往下传，可以说是props hell问题。
context方式封装的组件，为需要接受数据的组件，提供了一种<strong>跨组件层级传递，按需引入上级props</strong>的方式。</p>
<h4 data-id="heading-10">组件定义context部分</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// myContext.ts</span>
interface IContext &#123;
     <span class="hljs-attr">foo</span>: string,
     bar?: number,
     <span class="hljs-attr">baz</span>: string
&#125;
<span class="hljs-keyword">const</span> myContext = React.createContext<IContext>(&#123;
     <span class="hljs-attr">foo</span>: <span class="hljs-string">"a"</span>,
     <span class="hljs-attr">baz</span>: <span class="hljs-string">"b"</span>
&#125;)


interface IProps &#123;
    <span class="hljs-attr">data</span>: IContext ,
&#125;

<span class="hljs-keyword">const</span> myProvider: React.FC<IProps> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
     <span class="hljs-keyword">const</span> &#123;data, children&#125; = props
     <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">myContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;data&#125;</span>></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">myContext.Provider</span>></span></span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> myProvider;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useMyContext</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> useContext(myContext)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">使用组件和context部分</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 组件包裹 --></span>
import myProvider from './myContext.ts'

<span class="hljs-tag"><<span class="hljs-name">myProvider</span> <span class="hljs-attr">data</span>=<span class="hljs-string">&#123;&#123;foo:</span> "<span class="hljs-attr">foo</span>", <span class="hljs-attr">baz:</span> "<span class="hljs-attr">baz</span>"&#125;&#125;></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"root"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"parent"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Component1</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">Component2</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">myProvider</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Component1</span>
<span class="hljs-keyword">import</span>  &#123;useMyContext&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./myContext.ts'</span>
<span class="hljs-keyword">const</span> &#123;foo, baz&#125; = useMyContext()

<span class="hljs-keyword">const</span> Compoonent1 = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;foo&#125;&#123;baz&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
&#125;
<span class="hljs-keyword">export</span> Component1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">React.createElement(Input, props)中的React.createElement如何理解？</h3>
<h4 data-id="heading-13">React.createElement()</h4>
<pre><code class="hljs language-js copyable" lang="js">React.createElement(
    type,
    [props],
    [...children]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据指定类型，返回一个新的React element。</p>
<p>类型这个参数可以是：</p>
<ul>
<li>一个“标签名字符串”（例如“div”，“span”）</li>
<li>一个React component 类型（一个class或者一个function）</li>
<li>一个React fragment 类型</li>
</ul>
<p>JSX写法的组件，最终也会被解析为React.createElement()的方式。如果使用JSX的方式的话，不需要显式调用React.createElement()。</p>
<h4 data-id="heading-14">React.createElement(Input, props)</h4>
<p>基于antd，封装通用表单组件方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// generator.js</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Input, Select &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;

<span class="hljs-keyword">const</span> components = &#123;
  <span class="hljs-attr">input</span>: Input,
  <span class="hljs-attr">select</span>: Select
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateComponent</span>(<span class="hljs-params">type, props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> React.createElement(components[type], props);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单使用这个通用表单组件方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> generateComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./generator'</span>

<span class="hljs-keyword">const</span> inputComponent = generateComponent(<span class="hljs-string">'input'</span>, props)
<span class="hljs-keyword">const</span> selectComponent = generateComponent(<span class="hljs-string">'select'</span>, props)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可能会觉得上面这种方式比较鸡肋，但是如果批量地生成组件，这种方式就很有用了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components.js</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> generateComponent <span class="hljs-keyword">from</span> <span class="hljs-string">"./generator"</span>;

<span class="hljs-keyword">const</span> componentsInfos = [
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"input"</span>,
    <span class="hljs-attr">disabled</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">defaultValue</span>: <span class="hljs-string">"foo"</span>
  &#125;,
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"select"</span>,
    <span class="hljs-attr">autoClear</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">dropdownStyle</span>: &#123; <span class="hljs-attr">color</span>: <span class="hljs-string">"red"</span> &#125;
  &#125;
];

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Components</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> componentsInfos.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; type, ...props &#125; = item;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><></span>&#123;generateComponent(type, props)&#125;<span class="hljs-tag"></></span></span>;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的示例可以查看：<a href="https://codesandbox.io/s/react-component-generator-onovg?file=/src/index.js" target="_blank" rel="nofollow noopener noreferrer">codesandbox.io/s/react-com…</a></p>
<p>基于这种方式，可以封装出可重用的业务组件：表单业务组件，表格业务组件等等，会极大程度的解放生产力！</p>
<h3 data-id="heading-15">react中的FC是什么?<code>FC<[interface]></code>是什么意思？主要用处及最简写法是怎样的？</h3>
<h4 data-id="heading-16">react中的FC是什么?</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> FC<P = &#123;&#125;> = FunctionComponent<P>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">interface FunctionComponent<P = &#123;&#125;> &#123;
    (props: PropsWithChildren<P>, context?: any): ReactElement<any, any> | <span class="hljs-literal">null</span>;
    propTypes?: WeakValidationMap<P>;
    contextTypes?: ValidationMap<any>;
    defaultProps?: Partial<P>;
    displayName?: string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>FC是FunctionComponent的缩写，FunctionComponent是一个泛型接口。</p>
<h4 data-id="heading-17"><code>FC<[interface]></code>是什么意思？</h4>
<p>是为了提供一个函数式组件环境，用于包裹组件。
为什么呢？因为在函数式组件内部可以使用hooks。</p>
<p>函数式组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Component = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
    <span class="hljs-comment">// 这里可以使用hooks</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> /></span></span>
&#125;
或者
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Component</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">// 这里可以使用hooks</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">主要用处及最简写法是怎样的？</h4>
<p>项目内的公共函数式组件，作为组件容器使用，用于提供hooks上下文环境。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Container.js</span>
<span class="hljs-keyword">import</span> React, &#123; FC &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

interface IProps &#123;
     <span class="hljs-attr">children</span>: any
&#125;

<span class="hljs-keyword">const</span> Container: FC<IProps> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span>  &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;props.children&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Container
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用</span>
<Container>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component1</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component2</span> /></span></span>
</Container>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">React中FC的形参的props, context, propTypes, contextTypes, defaultProps, displayName是什么？</h3>
<pre><code class="hljs language-js copyable" lang="js">type FC<P = &#123;&#125;> = FunctionComponent<P>;

interface FunctionComponent<P = &#123;&#125;> &#123;
        (props: PropsWithChildren<P>, context?: any): ReactElement | <span class="hljs-literal">null</span>;
        propTypes?: WeakValidationMap<P>;
        contextTypes?: ValidationMap<any>;
        defaultProps?: Partial<P>;
        displayName?: string;
&#125;

type PropsWithChildren<P> = P & &#123; children?: ReactNode &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中props和context都是函数组件的形参。
而propTypes，contextTypes，defaultProps，displayName都是组件的函数组件的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Foo: FC<&#123;&#125;> = <span class="hljs-function">(<span class="hljs-params">props, context</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;props.children&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
Foo.propTypes = ...
Foo.contextTypes = ...
Foo.defaultProps = ...
Foo.displayName = ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">react函数式组件与纯函数组件有什么区别呢？</h4>
<p>1.react函数式组件必须返回ReactElement或者null，纯函数组件返回值没有限定
2.react函数式组件的props限定children的类型为ReactNode，纯函数组件没有限定
3.react函数式组件拥有propTypes，contextTypes，defaultProps，displayName等等类型约束，纯函数组件没有限定</p>
<p><a href="https://stackoverflow.com/questions/53935996/whats-the-difference-between-a-react-functioncomponent-and-a-plain-js-function" target="_blank" rel="nofollow noopener noreferrer">stackoverflow.com/questions/5…</a></p>
<h3 data-id="heading-21"><code>import &#123; MouseEvent &#125; from 'react'</code>是什么意思？SyntheticEvent是什么类型？</h3>
<h4 data-id="heading-22"><code>import &#123; MouseEvent &#125; from 'react'</code>是什么意思？</h4>
<p>好文章：<a href="https://fettblog.eu/typescript-react/events/#1" target="_blank" rel="nofollow noopener noreferrer">fettblog.eu/typescript-…</a></p>
<ul>
<li>用于事件类型约束</li>
<li>除了MouseEvent，还有AnimationEvent, ChangeEvent, ClipboardEvent, CompositionEvent, DragEvent, FocusEvent, FormEvent, KeyboardEvent, MouseEvent, PointerEvent, TouchEvent, TransitionEvent, WheelEvent. As well as SyntheticEvent</li>
<li>可以使用<code>MouseEvent<HTMLButtonElement></code>约束仅触发HTML button DOM的事件</li>
<li>InputEvent较为特殊，因为是一个实验事件，因此可以用SyntheticEvent替代</li>
</ul>
<h4 data-id="heading-23">SyntheticEvent是什么类型？</h4>
<p>Synthetic -> 合成的</p>
<p>在React中，几乎所有的事件都继承了SyntheticEvent这个interface。
SyntheticEvent是一个跨浏览器的浏览器事件wrapper，通常用于替代InpuEvent这样的事件类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SyntheticEvent<T = Element, E = Event> <span class="hljs-keyword">extends</span> BaseSyntheticEvent<E, EventTarget & T, EventTarget> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> BaseSyntheticEvent<E = object, C = any, T = any> &#123;
    <span class="hljs-attr">nativeEvent</span>: E;
    currentTarget: C;
    target: T;
    bubbles: <span class="hljs-built_in">boolean</span>;
    cancelable: <span class="hljs-built_in">boolean</span>;
    defaultPrevented: <span class="hljs-built_in">boolean</span>;
    eventPhase: <span class="hljs-built_in">number</span>;
    isTrusted: <span class="hljs-built_in">boolean</span>;
    preventDefault(): <span class="hljs-built_in">void</span>;
    isDefaultPrevented(): <span class="hljs-built_in">boolean</span>;
    stopPropagation(): <span class="hljs-built_in">void</span>;
    isPropagationStopped(): <span class="hljs-built_in">boolean</span>;
    persist(): <span class="hljs-built_in">void</span>;
    timeStamp: <span class="hljs-built_in">number</span>;
    <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">React.forwardRef是什么意思？useImperativeHandle是什么意思？</h3>
<p><strong>简而言之，refs转发就是为了获取到组件内部的DOM节点。</strong>
React.forwardRef意思是<strong>Refs转发</strong>，主要用于将ref自动通过组件传递到某一子组件，常见于可重用的组件库中。</p>
<p>在使用forwardRef时，可以让某些组件接收ref，并且将其向下传递给子组件，也可以说是”转发“给子组件。</p>
<p>没有使用refs转发的组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FancyButton</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"FancyButton"</span>></span>
      &#123;props.children&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用refs转发的组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> FancyButton = React.forwardRef(<span class="hljs-function">(<span class="hljs-params">props, ref</span>)=></span>&#123;
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"FancyButton"</span>></span>
    &#123;props.children&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何使用？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个ref变量</span>
<span class="hljs-keyword">const</span> ref = React.createRef();
<span class="hljs-comment">// 将ref变量传入FancyButton，FancyButton将ref变量转发给button</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">FancyButton</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FancyButton</span>></span></span>
<span class="hljs-comment">// ref.current指向button DOM节点</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue中也有refs机制不同，但是vue如果想获取到子组件内部的DOM节点，需要一级一级的去获取，比如<code>this.$refs.parent.$refs.child</code>，这会导致组件层级依赖严重。
相比vue而言，React的refs转发组件层级以来较轻，代码可读性和可维护性更高。</p>
<h4 data-id="heading-25">useImperativeHandle是什么意思？</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useRef, useImperativeHandle &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-keyword">const</span> FancyInput = React.forwardRef(<span class="hljs-function">(<span class="hljs-params">props, ref</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> inputRef = useRef();
  useImperativeHandle(ref, <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">publicFocus</span>: <span class="hljs-function">() =></span> &#123;
      inputRef.current.focus();
    &#125;
  &#125;));

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;inputRef&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span></span>
&#125;);

<span class="hljs-keyword">const</span> App = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> fancyInputRef = useRef();

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">FancyInput</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;fancyInputRef&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> fancyInputRef.current.publicFocus()&#125;
      >父组件调用子组件的 focus<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, root);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个例子中与直接转发 ref 不同，直接转发 ref 是将 React.forwardRef 中函数上的 ref 参数直接应用在了返回元素的 ref 属性上，其实父、子组件引用的是同一个 ref 的 current 对象，官方不建议使用这样的 ref 透传，而使用 useImperativeHandle 后，可以让父、子组件分别有自己的 ref，通过 React.forwardRef 将父组件的 ref 透传过来，通过 useImperativeHandle 方法来自定义开放给父组件的 current。</p>
<blockquote>
<p>期待和大家交流，共同进步：</p>
<ul>
<li>微信公众号： 大大大前端 / excellent_developers</li>
<li>Github博客: <a href="https://github.com/FrankKai/FrankKai.github.io" target="_blank" rel="nofollow noopener noreferrer">趁你还年轻233的个人博客</a></li>
<li>SegmentFault专栏：<a href="https://segmentfault.com/blog/chennihainianqing" target="_blank" rel="nofollow noopener noreferrer">趁你还年轻，做个优秀的前端工程师</a></li>
</ul>
</blockquote>
<blockquote>
<p>努力成为优秀前端工程师！</p>
</blockquote></div>  
</div>
            