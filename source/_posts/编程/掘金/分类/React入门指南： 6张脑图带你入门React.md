
---
title: 'React入门指南： 6张脑图带你入门React'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ff6c06c5154582b0c464f62cf2cb96~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 18:21:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ff6c06c5154582b0c464f62cf2cb96~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>马上到了又一年的秋招， 还不会React？ 没关系！</strong> 我这里有最精简的入门指南😄</p>
<p><strong>通过6张脑图带你入门React</strong>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/" ref="nofollow noopener noreferrer">React</a>文档相对于刚入门的新人来说, 其跳跃性强, 案例的综合性之高让人读起来都费劲. 为此我整理了一份<strong>脑图+超简单的Demo</strong>的笔记, 让你迅速明白ReactAPI的作用, 具体的Demo地址👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide" ref="nofollow noopener noreferrer">react-study-guide</a>， 欢迎star⭐。 所有的脑图， Demo都在仓库里可以直接获取</p>
<p>并且在许多演示片段, 我都录制了GIF图, 让你更直观的体会到代码的实现与Demo的样式</p>
<hr>
<h1 data-id="heading-0">总览</h1>
<blockquote>
<p>放心看起来虽然多, 但是内容都不复杂, 每个分支我都配备了对应的讲解</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ff6c06c5154582b0c464f62cf2cb96~tplv-k3u1fbpfcp-watermark.image" alt="React.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">JSX语法</h1>
<blockquote>
<p>最重要的一点, 大括号 <strong>&#123;&#125;</strong> 内写的是<code>JavaScript</code>的语法</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9601d5c1e60742758b24ac75fb9c8232~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这个Demo就展示了React中JSX语法需要注意的地方， 仅需注意脑图提到的规则即可（完全够用了）</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><div id=<span class="hljs-string">"test"</span>></div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/babel"</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> data = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>]
  <span class="hljs-comment">// 1.创建虚拟DOM</span>
  <span class="hljs-keyword">const</span> VDom = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span> &#123;/* 必须只有一个根标签 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;background:</span> '<span class="hljs-attr">skyblue</span>', <span class="hljs-attr">marginLeft:</span> '<span class="hljs-attr">20px</span>'&#125;&#125;></span>这是大标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'ul-class-name'</span>></span>
        &#123; &#123;/* JS语法 */&#125;
          data.map((item, index) => &#123;
            return <span class="hljs-tag"><<span class="hljs-name">li</span>  <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span>&#123;item&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          &#125;)
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
  ReactDOM.render(VDom, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-2">React组件化</h1>
<blockquote>
<p>组件化是React最核心的内容， 我会将脑图拆分成一个部分一个部分来看</p>
</blockquote>
<ul>
<li>如果你不理解<code>组件化</code>这个词, 没关系继续往下看, 稍后你就会慢慢明白了</li>
</ul>
<h2 data-id="heading-3">函数式与类式组件</h2>
<blockquote>
<p>函数式组件是目前使用最多， 并且是最受欢迎得用法， 但是两者并非谁更加优秀， 用法看个人即可。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21cd5789d2d4475781280299847e454f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">函数式</h3>
<blockquote>
<p>使用简单，没有烦人的this指向， 普遍被人接受， 不过无法使用类式组件中的部分功能<code>State</code>， <code>生命周期函数</code>等（这些后续会做介绍）， 但可以用过hook解决这一问题。</p>
</blockquote>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Functional Component<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">类式</h3>
<blockquote>
<p>书写相对复杂， 要求继承一个通过React暴露的<code>Component</code>类, 但是可以直接使用生命周期函数， state状态</p>
</blockquote>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Class Component<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注 如果你对类的写法不熟悉， 推荐你看一下这篇文章底部对类的简单介绍<a href="https://juejin.cn/post/6933362634574004237#heading-8" target="_blank" title="https://juejin.cn/post/6933362634574004237#heading-8">原型与原型链: 如何自己实现 call, bind, new?</a></li>
</ul>
<h2 data-id="heading-6">事件对象</h2>
<blockquote>
<p>就是各种事件（点击等）， 使用起来除了书写差异， 其实跟原生没有太大区别。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ee50a75ef4e4ec69b8e26241790478f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">书写规范</h3>
<blockquote>
<p>使用 <strong>小驼峰</strong> 的形式,取代传统的写法即可</p>
</blockquote>
<ul>
<li>传统写法</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><a herf=<span class="hljs-string">"#"</span> onclick=<span class="hljs-string">"console.log('ok!')"</span>></a>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>React事件写法</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><a herf=<span class="hljs-string">"#"</span> onClick=&#123;clickFun&#125;></a> 

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickFun</span> (<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ok!'</span>) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>React阻止事件默认行为</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><a herf=<span class="hljs-string">"#"</span> onClick=&#123;clickFun&#125;></a> 

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickFun</span> (<span class="hljs-params">e</span>) </span>&#123; 
    e.preventDefault() 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ok!'</span>) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">this的指向问题</h3>
<ul>
<li>通常情况下由于onClick执行与函数并不同步, 所以this会指向undefined, 需要在实例内改变this指向</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.switchFn = <span class="hljs-built_in">this</span>.switchFn.bind(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// 👈 在构造器内部</span>
                                             <span class="hljs-comment">// 将函数的this绑定为当前实例</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">switchFn</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击成功'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.switchFn&#125;</span>></span>
        这里是事件点击处
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125; 
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过箭头函数的形式来解决， 如果你想了解为什么， 建议你复习一下箭头函数的特性</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
  &#125;
  switchFn = <span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 👈</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击成功'</span>) <span class="hljs-comment">// 将函数改为箭头函数形式</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.switchFn&#125;</span>></span>
        这里是事件点击处
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125; 
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">处理器的参数传递</h3>
<ul>
<li>通过bind解决</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><button click=&#123;<span class="hljs-built_in">this</span>.switch.bind(<span class="hljs-built_in">this</span>, id)&#125;></button>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>写成回调函数的形式</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"> <button click=&#123;<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;<span class="hljs-built_in">this</span>.switch(id, e)&#125;&#125;></button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>讲完三大属性，再来讲讲React的条件渲染与循环</strong></p>
<h2 data-id="heading-10">组件的三大属性</h2>
<blockquote>
<p>了解了三大属性, 我们再来看一个完整的React组件应该长什么样</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10018afdaac4dc8bdf42e1591d03c73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">state（状态）</h3>
<blockquote>
<p>组件本身的状态，是一个挂载在当前组件实例上的一个属性</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce5443c3a2da4a95ac56bfc906a66cd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>this.setState()</strong>: 有两种使用方式:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2949bcef4d6a433d9c64ef993b8c360a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>对象式</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// this.setState((state, props)=>&#123;&#125;, callback)</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    state = &#123; 
        <span class="hljs-attr">name</span>: <span class="hljs-string">'link'</span> 
    &#125;
    switchFn = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;   <span class="hljs-comment">// 👈</span>
            <span class="hljs-attr">name</span>: <span class="hljs-string">'kiki'</span>  
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.switchFn&#125;</span>></span>
          name: &#123;this.state.name&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数式</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// this.setState((state, props)=>&#123;&#125;, callback)</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    state = &#123; 
        <span class="hljs-attr">name</span>: <span class="hljs-string">'link'</span> 
    &#125;
    switchFn = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state, prop</span>) =></span> &#123; <span class="hljs-comment">// 👈</span>
            <span class="hljs-comment">// 可以直接拿到state与prop</span>
            <span class="hljs-attr">name</span>: <span class="hljs-string">'kiki'</span>
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.switchFn&#125;</span>></span>
          name: &#123;this.state.name&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>由于setState的执行是异步的, 在setState（）后如果还需要做一些处理， 这些处理就需要在callbak内了</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> name = <span class="hljs-string">'link'</span>

<span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'kiki'</span>&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.name) <span class="hljs-comment">// 此时还会得到 'link'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>正确操作</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">state = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'link'</span>
&#125;
<span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'kiki'</span>&#125;, <span class="hljs-function">() =></span> &#123;  <span class="hljs-comment">// 👈</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.name) <span class="hljs-comment">// 此时得到 'kiki'</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注</strong>： 以上均是类式组件的用法， 在函数式组件中， 使用 <strong>State</strong> 需要通过 <strong>hook</strong> 实现， 到hook章节我们再来阐述这一点</p>
<h3 data-id="heading-12">prop（属性 property）</h3>
<blockquote>
<p>props也是实例上挂载的一个属性，所有通过标签属性传递的值，都可以由它访问到，包括函数， 对象。(组件通信), 也有一些特殊值无法被访问, 如做唯一表示的key</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebba9e7a4af84a5facb3c51914a0bd7c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 根据JSX语法 假设这是一个组件</span>

<span class="hljs-keyword">let</span> name = <span class="hljs-string">'link'</span>

<TestComponent name=&#123;name&#125; /> <span class="hljs-comment">// 这个name就是一个prop(属性)</span>

<span class="hljs-comment">// TestComponent组件内部</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
   <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>name: &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span> <span class="hljs-comment">// 👈 &#123;&#125;大括号内可以写js语法</span>
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">ref（引用 reference）</h3>
<blockquote>
<p>获取到当前的一个DOM元素</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65c9043396ca452b83276456716596eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>类似于document.getElementById('id') 只是这件事由React帮你做了</p>
</li>
<li>
<p><strong>使用方式</strong></p>
</li>
</ul>
<blockquote>
<p><strong>注意:</strong> ref的使用方式有三种, 但目前为止最被官方推荐的为第三种</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/107f3830e8db49d0b271dcae360bc782~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">字符串形式❌（<strong>不推荐</strong>）</h4>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 这是一个原生的DOM</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleClick = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.refs.index);  <span class="hljs-comment">// 拿到这个实例</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'index'</span>></span> // 👈
              <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'index2'</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">ref回调形式</h4>
<blockquote>
<p>回调函数的形式, 会把DOM挂载到实例上(this)</p>
</blockquote>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleClick = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); 
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;c</span> =></span> this.input1 = c&#125;>  // 👈
              <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">createRef</h4>
<blockquote>
<p>React基于craetRef创建的ref只能存放一个ref, 这种形式的<strong>官方最为推荐</strong>， 但是书写相对比较麻烦</p>
</blockquote>
<ul>
<li>creatRef() 即在每次使用的时候需要自己手动创建一个ref, 并且只能专人专用</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  headerRef = React.createRef()  <span class="hljs-comment">// 👈</span>
  divRef = React.createRef()
  
  handleClick = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.headerRef);  <span class="hljs-comment">// 👈</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.divRef);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.divRef&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span>></span>  // 👈
              <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.headerRef&#125;onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">综合案例</h2>
<blockquote>
<p>结合事件对象与三大属性， 我们来看一个条件渲染的案例</p>
</blockquote>
<ul>
<li>
<p>本案例在项目中的路径地址： <strong>'react-study-guide\study-demo\test-Demo\React-组件化\事件对象\条件渲染.html'</strong></p>
</li>
<li>
<p>组件关系</p>
</li>
</ul>
<blockquote>
<p>请对照这个流程表理清关系</p>
</blockquote>
<pre><code class="hljs language-mermaid" lang="mermaid">stateDiagram-v2
Demo(主组件) --> LogoutBtn: isLogin === true
Demo(主组件) --> Greeting
Demo(主组件) --> LoginBtn: isLogin === false
Greeting --> Welcome: isLogin === true
Greeting --> Bye: isLogin === false
</code></pre>
<ul>
<li>效果</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0a381d16e04460bb6877b7d0fe5559d~tplv-k3u1fbpfcp-watermark.image" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是说, 在全局主组件中有一个<code>isLogin</code>(state)在管控全局状态.根据是否登录,我们来判断展示什么样的组件</p>
<ul>
<li>Demo组件</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  state = &#123;
    <span class="hljs-attr">isLogin</span>: <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> button
    <span class="hljs-keyword">const</span> &#123; isLogin &#125; = <span class="hljs-built_in">this</span>.state
    <span class="hljs-keyword">if</span>(isLogin) &#123;
      <span class="hljs-comment">// 将点击事件函数作为props传入组件</span>
      button = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">LogoutBtn</span> <span class="hljs-attr">onLogoutClick</span>=<span class="hljs-string">&#123;this.logout&#125;/</span>></span></span> 
    &#125; <span class="hljs-keyword">else</span> &#123;
      button = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">LoginBtn</span> <span class="hljs-attr">onLoginClick</span>=<span class="hljs-string">&#123;this.login&#125;/</span>></span></span>
    &#125;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Greeting</span> <span class="hljs-attr">isLogin</span>=<span class="hljs-string">&#123;this.state.isLogin&#125;/</span>></span>
        &#123;button&#125;  &#123;/* 根据state中的islogin判断展示logoutBtn还是LoginBtn */&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
  <span class="hljs-comment">// 控制事件</span>
  login = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">isLogin</span>: <span class="hljs-literal">true</span>&#125;)
  &#125;
  logout = <span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">isLogin</span>: <span class="hljs-literal">false</span>&#125;)
  &#125;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Greeting 组件(UI组件)</li>
</ul>
<blockquote>
<p>它包含了两个UI子组件, 根据isLogin的状态我们来判断展示那个UI组件, <strong>请思考一下主组件Demo是怎么把isLogin的状态传递到UI组件<code>Greeting</code>中的?</strong></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Greeting</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">const</span> isLogin = props.isLogin
  <span class="hljs-keyword">if</span>(isLogin) <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Welcome</span> /></span></span>
  )
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Bye</span> /></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>UI子组件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// UI</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Welcome</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Welcome<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Bye</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Bye<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">组件化思想</h3>
<blockquote>
<p>想想上面的组件之间的关系以及功能, 其实就是每个组件在负责他们自己的功能, 按钮组件负责<code>登录</code>与<code>退出</code>的事件, UI组件负责展示标语, welcome与bye.</p>
</blockquote>
<ul>
<li>在实际开发中也是同理. 你可以将你认为合理的一部分看成一个组件, 以此来提高它的复用性. 组件化开发条例更加清晰, 也能有效降低耦合度.</li>
</ul>
<p>以React的官网为例:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a72722645bb4b52857b599560ed9380~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们就可以把头部的红色部分看成一个头部组件.</li>
<li>底部的橙色看成一个组件, <strong>我们仅需写一个橙色组件, 然后将标题以及内容, 作为prop传递进去即可.</strong></li>
</ul>
<p><strong>那么具体怎么做?</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 数据</span>
<span class="hljs-keyword">let</span> arr = [
    &#123;
      <span class="hljs-attr">title</span>:<span class="hljs-string">'link'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'ok, 我要说点什么'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">title</span>:<span class="hljs-string">'掘金'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'ok, 发文章'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">title</span>:<span class="hljs-string">'公众号'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'ok, 偷个懒'</span>
    &#125;,
]
<span class="hljs-comment">// 通过prop传入Demo组件 </span>
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> <span class="hljs-attr">number</span>=<span class="hljs-string">&#123;arr&#125;</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))  <span class="hljs-comment">// 👈</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">arrInfo</span>: <span class="hljs-built_in">this</span>.props.number
  &#125;
  <span class="hljs-comment">// 根据arr的数据做循环, 将这个组件存到一个数组里</span>
  itemList = <span class="hljs-built_in">this</span>.props.number.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ItemList</span> <span class="hljs-attr">item</span>=<span class="hljs-string">&#123;item&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;/</span>></span></span>
  &#125;)
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>&#123;this.itemList&#125;<span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  &#125;
&#125;
<span class="hljs-comment">// UI组件, 在上方我们循环了这个组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ItemList</span> (<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">let</span> item = props.item
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>title: &#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>content: &#123;item.content&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>一个橙色的框框就是我们一个"信息"组件. 这样我们就复用了这个组件, 而不是自己去复制三个. 当然组件化远远比我形容的要强大, 剩下的就靠你的创造力了.</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca15617a4f754b04b876ca12027409f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注:</strong> 在循环处我加入了一个<code>key</code>属性, 他的作用是<strong>给每一个组件绑定一个唯一的标识, 这有助于react识别组件.但是该标识并不是要求在全局下唯一,而是在兄弟节点之间,也就是非兄弟节点(不同组件),是可以使用一个数据中的id作为标识的.</strong> 目前只需要知道这一点就可以了. 有兴趣可以深入了解, 它的作用与原理比想象的复杂</p>
<h2 data-id="heading-19">组件通信</h2>
<blockquote>
<p>从这里开始, 将会详细的书写一个React组件, 并且这些Demo都在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide" ref="nofollow noopener noreferrer">react-study-guide</a>项目中有对应Demo, 如果看不明白, 可以clone一下项目自己调试一下, 并且强烈建议你自己手敲一下这些Demo</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9d991feaaa426985e73f6d8e98d5d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">父子组件</h3>
<blockquote>
<p>根据上面的例子 父传子 应该非常显而易见了, 就是通过prop传入.</p>
</blockquote>
<ul>
<li>子传父</li>
</ul>
<blockquote>
<p>同样根据prop, 父组件传入一个函数, 子组件内执行的时候传参给它</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
      <span class="hljs-built_in">super</span>(props)
      <span class="hljs-built_in">this</span>.state = &#123;
        <span class="hljs-attr">info</span>: <span class="hljs-string">'还没消息...'</span>
      &#125;
    &#125;
    getInfo = <span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">info</span>: item
      &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>info: &#123;this.state.info&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Clild</span> <span class="hljs-attr">getChildInfo</span>=<span class="hljs-string">&#123;this.getInfo&#125;/</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>子组件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为了让你习惯这两种组件创建方式, 我将会任意切换, 因为两者切换使用并无语法层面的问题</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Clild</span> (<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emitInfo</span>(<span class="hljs-params"></span>) </span>&#123;
    props.getChildInfo(<span class="hljs-string">'我是子组件发送过去的数据'</span>) <span class="hljs-comment">// 👈</span>
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;emitInfo&#125;</span>></span>点击发送消息<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  )
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Father</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#test'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">兄弟组件</h3>
<ul>
<li><strong>状态提升:</strong> 原本两个组件各自管理着自己的state, 例如它们都有一个属性叫做<code>title</code>, 为了他们两个共同使用同一个 <code>title</code> state, 我们可以把 <code>title</code> 提升到父组件, 然后通过<code>prop</code>传入</li>
</ul>
<pre><code class="hljs language-mermaid" lang="mermaid">classDiagram
Father <|-- ChildA
Father <|-- ChildB

class ChildA&#123;
state: "title: 'child'"
&#125;
class ChildB&#123;
state: "title: 'child'"
&#125;
</code></pre>
<ul>
<li>状态提升后</li>
</ul>
<pre><code class="hljs language-mermaid" lang="mermaid">classDiagram
Father --|> ChildA: title=&#123;this.state.title&#125;
Father --|> ChildB: title=&#123;this.state.title&#125;
Father: title 'child'
class ChildA&#123;
prop: "title: 'child'"
&#125;
class ChildB&#123;
prop: "title: 'child'"
&#125;
</code></pre>
<ul>
<li>这里我仅提供思路, 因为它和上面那个案例的实现是一致的, 尝试自己实现一下吧!</li>
</ul>
<h3 data-id="heading-22">非亲组件</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edf523c664b04f7cb39061b8f1e667a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>redux 我们作为一个章节来讲, 这里只看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmroderick%2FPubSubJS" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mroderick/PubSubJS" ref="nofollow noopener noreferrer">pubsub-js</a></li>
</ul>
<blockquote>
<p>$ yarn add pubsub-js</p>
</blockquote>
<h4 data-id="heading-23">pubsub</h4>
<blockquote>
<p>pubsub用的其实不多, 仅做了解, 需要的时候再使用就好了, 通常公共状态管理都是使用Redux, 而隔代的组件我们也可以通过 <strong>renderProp</strong>, 或者<strong>高阶组件</strong>来实现, 甚至可以通过<strong>context</strong>, 这些我们后续都会提及</p>
</blockquote>
<ul>
<li>两个组件之间的关系( 可以没有任何关系)</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Publish</span> /></span>
                <span class="hljs-tag"><<span class="hljs-name">Subscribe</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>发送组件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> PubSub <span class="hljs-keyword">from</span> <span class="hljs-string">'pubsub-js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Publish</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">'我是publish传给Subscribe的数据'</span>
    &#125;
    handleValue = <span class="hljs-function">(<span class="hljs-params">dataType, value</span>) =></span> &#123;
        PubSub.publish(<span class="hljs-string">'data of publish'</span>, <span class="hljs-built_in">this</span>.state.value) <span class="hljs-comment">// 数据发送 👈</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Publish<span class="hljs-tag"></<span class="hljs-name">h1</span>></span> 
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleValue&#125;</span>></span>点击发送数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接收组件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> PubSub <span class="hljs-keyword">from</span> <span class="hljs-string">'pubsub-js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscribe</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">receivedData</span>: <span class="hljs-string">''</span>
    &#125;
<span class="hljs-comment">// 订阅数据</span>
    token = PubSub.subscribe(<span class="hljs-string">'data of publish'</span>, <span class="hljs-function">(<span class="hljs-params">msg, data</span>) =></span> &#123; <span class="hljs-comment">// 👈</span>
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">receivedData</span>: data
        &#125;)
    &#125;)
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Subcribe: <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.receivedData&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
<span class="hljs-comment">// 卸载钩子, 记得清空接收器</span>
    <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        PubSub.unSubscribe(<span class="hljs-built_in">this</span>.token)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">生命周期</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide%2Ftree%2Fmaster%2Fstudy-demo%2Ftest-Demo%2FReact-%25E7%25BB%2584%25E4%25BB%25B6%25E5%258C%2596%2F%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E9%2592%25A9%25E5%25AD%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide/tree/master/study-demo/test-Demo/React-%E7%BB%84%E4%BB%B6%E5%8C%96/%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90" ref="nofollow noopener noreferrer">生命周期Demo</a>可以clone下来调试下面输出的例子,</p>
</blockquote>
<h3 data-id="heading-25">新版</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac7e32cd733e4221b58684dac410e9fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>页面初次渲染时</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bfff64477454a1798c37eecb55122b5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>数据更新时</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb30994e6f74695a124e966c0b6de9f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">旧版</h3>
<blockquote>
<p>旧版的生命周期在Demo中有演示, 这里就不做展示了</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2db5a0e2877a47d980624d6ce21269e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27">注意</h3>
<blockquote>
<p>即便父组件更新与子组件无任何关系, 也会导致子组件刷新, 可以通过继承PureComponent解决, 但是shouldComponentUpdate不可用</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c844bc261a1e4291a83d905c0c53cc74~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这张图可以看出, 尽管我传入的childName没有发生任何改变, 但是子组件还是发生了重新渲染</p>
<h3 data-id="heading-28">新旧生命周期对比</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206fa34143cc4410a9200f94f196db07~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">受控与非受控组件</h2>
<blockquote>
<p>原本表单元素是自己维护自己的值, 并且只能通过用户的输入进行值的修改. 而在React中可变状态的值只能保存于state中, 并且基于setState去修改. 两者结合, 使得用户输入的值保存至state中, 并在事件中基于setState去改变. 组件内部的state就成了唯一的数据源(值都保存于此). 基于这种形式控制的组件就成为 "<strong>受控组件</strong>"</p>
</blockquote>
<p><strong>看不懂? 看gif图</strong></p>
<ul>
<li>上为受控组件， 下为非受控组件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebc55a8ad1764cd78829d1539bd8d87c~tplv-k3u1fbpfcp-watermark.image" alt="受控与非受控.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>发现区别在哪里没？</strong> 受控组件的数据会实时的渲染到页面上， 同步更新页面与数据。而非受控则不会.他们两者用的都是change事件， <strong>受控组件用的是React做过修改的onChange， 而下方的是原生的change事件</strong></p>
<ul>
<li>这就是受控与非受控的区别， 简单吧。当然这只是从视图层面解释， 请仔细看上方的定义</li>
</ul>
<p><strong>请思考一下， 如上方的受控组件， 我要求他们只能通过一个处理器函数去处理 event.target.value值，怎样才能保证两者的值不会覆盖到同一个state状态上？</strong></p>
<ul>
<li>答案地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide%2Ftree%2Fmaster%2Fstudy-demo%2Ftest-Demo%2FReact-%25E7%25BB%2584%25E4%25BB%25B6%25E5%258C%2596" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide/tree/master/study-demo/test-Demo/React-%E7%BB%84%E4%BB%B6%E5%8C%96" ref="nofollow noopener noreferrer">React组件化</a></li>
</ul>
<h3 data-id="heading-30">可被创建为受控组件表</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dab3857aa554c898050f9e08f688b55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-31">React-Router</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9acc8bb933b64e7c817f718e1130fb68~tplv-k3u1fbpfcp-watermark.image" alt="React-Router.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-32">使用</h2>
<blockquote>
<p>$ yarn add react-router</p>
</blockquote>
<ul>
<li>入口文件引入即可</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Route,Link&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">HashRouter与BrowserRouter</h2>
<blockquote>
<p>一般情况下， 与服务器做交互，使用的都是 <strong>BrowserRouter</strong>， 而使用静态文件的服务器的情况才用 <strong>HashRouter</strong>，并且这两者都要求包裹在使用路由的外部</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aff4a135ae745238fc5257fe3acd52c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> &#123; BrowserRouter&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>

ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span> // 👈 包裹
        <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>
    , <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">导航Link</h2>
<blockquote>
<p>导航就是用来进行跳转的交互按钮， 通过点击它后， 它去匹配相同的路径. 等介绍完link与Route组件， 我们再来看一个完整的路由匹配</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a0ae96ad9004754b75c4eaf46dcb6b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-35">to</h3>
<ul>
<li>字符串</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Link to=<span class="hljs-string">"/goWhere"</span> > goWhere </Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Link to=&#123;&#123; 
    <span class="hljs-attr">pathname</span>: <span class="hljs-string">"/goWhere"</span>,
    <span class="hljs-attr">search</span>: <span class="hljs-string">'?id=1'</span>,
    <span class="hljs-attr">hash</span>: <span class="hljs-string">'#nav'</span>
&#125;&#125;> goWhere </Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">NavLink(带激活效果的Link)</h3>
<blockquote>
<p>使用NavLink默认点击后给当前路由加上active类名， 如需更换类名， 使用activeClassName接受， 它能够触发一些点击效果</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><NavLink activeClassName=<span class="hljs-string">"avtive-name"</span> className=<span class="hljs-string">""</span> to=<span class="hljs-string">"/home"</span> >Home</NavLink>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">路由组件Route</h2>
<blockquote>
<p>它就是负责展示与你在Link的to属性中传的路径相对应的组件.</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d47f5b55fd414613867d4771e986bb1d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这是一个完整的路由匹配Demo.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.jsx</span>
<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> About <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/About'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/Home'</span>
<span class="hljs-keyword">import</span> &#123; Link, Route&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>React-Demo<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'left'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span> ></span>About<span class="hljs-tag"></<span class="hljs-name">Link</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span> ></span>Home<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'right'</span>></span>
          &#123;/* 路由切換 */&#125;
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/about'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span> /></span> &#123;/* 👈如果匹配到/about则展示 About组件 */&#125;
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span> &#123;/* 如果匹配到/about则展示 Home组件 */&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这就是一个基本的路由组件的匹配过程, <strong>请注意我后面点击了浏览器的回退键, 它同样回退了我之前的页面, 这就证明Route的跳转, 是会被记录到历史栈中的</strong></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6336965832114c83ad6acabf43fd06d2~tplv-k3u1fbpfcp-watermark.image" alt="基本路由组件.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>如果我们把Link换成 NavLink它就会根据类名高亮被激活的路由</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3efd15870d214557811c4144c9db395a~tplv-k3u1fbpfcp-watermark.image" alt="NavLink.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-38">渲染方式</h3>
<blockquote>
<p>Route的组件有三种传递方式, <code>component</code>, <code>render</code>, <code>children</code></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be9d889cfeff49de8f80150b67ec8f39~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>注意看Route部分</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> About <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/About'</span>
<span class="hljs-keyword">import</span> Nav <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/Nav'</span>
<span class="hljs-keyword">import</span> &#123; Route,Link&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;

  refCallback = <span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(node)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>React-Demo<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'left'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/about'</span>></span>
              About
            <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/nav"</span>></span>Nav<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'right'</span>></span>
          &#123;/* 路由切換 */&#125;
          
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/about'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span> /></span> &#123;/* component */&#125;
          
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;</span>              &#123;/* <span class="hljs-attr">render</span> */&#125;
            <span class="hljs-attr">props</span> =></span> (
              <span class="hljs-tag"><<span class="hljs-name">div</span> &#123;<span class="hljs-attr">...props</span>&#125; ></span>Home<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            )
          &#125; />
          
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/nav'</span> <span class="hljs-attr">children</span>=<span class="hljs-string">&#123;</span>             &#123;/* <span class="hljs-attr">children</span> */&#125;
            (&#123;<span class="hljs-attr">props</span>, <span class="hljs-attr">match</span>&#125;) =></span> (
              match ? <span class="hljs-tag"><<span class="hljs-name">Nav</span> &#123;<span class="hljs-attr">...props</span>&#125;/></span> : <span class="hljs-tag"><<span class="hljs-name">div</span>></span>默认<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            )
              
          &#125; />
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意看这个图, 我们在<code>children</code>中接受到一个<code>match: boolean</code>的属性, 它用来判断当前是否与/nav路径匹配与否, 如不匹配, 则展示默认内容, 匹配则展示我们书写的内容</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a236aa73ec8745e9a7319f36e03c6bfe~tplv-k3u1fbpfcp-watermark.image" alt="三种渲染方式2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>render属性可以直接写一个内联结构, 十分方便, 也可以直接传递prop</p>
</li>
<li>
<p>children 则当你需要展示默认内容的时候, 才需要用到它,其他的与render相似</p>
</li>
</ul>
<h3 data-id="heading-39">switch</h3>
<blockquote>
<p>仅匹配一次, 如果同路径路由, 仅匹配第一次遇到的(提高效率)</p>
</blockquote>
<ul>
<li>假设我们有这么多个相同路径的路由 那么路由就会这样匹配</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div className=<span class="hljs-string">'right'</span>>
  &#123;<span class="hljs-comment">/* 路由切換 */</span>&#125;
    <Route path=<span class="hljs-string">'/about'</span> component=&#123;About&#125; />
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/759fae73ca1e4e40af37af1655bde54f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>给<code>Route</code>组件外部加上<code>Switch</code>标签, 则可以预防这种匹配</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Route, Link, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>

<div className=<span class="hljs-string">'right'</span>>
  &#123;<span class="hljs-comment">/* 路由切換 */</span>&#125;
  <Switch>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/about'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span>  &#123;<span class="hljs-comment">/* 完成匹配 终止 */</span>&#125;
    <Route path=<span class="hljs-string">'/home'</span> component=&#123;Home&#125; />
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span>
  </Switch>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fe0a532735449ebb5cff1c076a1d39~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-40">模糊与严格匹配</h3>
<blockquote>
<p>默认情况下为模糊匹配， 也就是路径如果为多层的，仅匹配到第一层就会渲染</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>React-Demo<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'left'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/about'</span>></span>
              About
            <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/a"</span> ></span>HomeA<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'right'</span>></span>
          &#123;/* 路由切換 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/about'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home/a'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;HomeA&#125;</span> /></span> &#123;/*home子路由*/&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>由于 Router 的模糊匹配机制, 如果我们点击home/a 上方的home组件也会被匹配到</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d051020d91304b21951cd7f9775b9926~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><div className=<span class="hljs-string">'right'</span>>
      &#123;<span class="hljs-comment">/* 路由切換 */</span>&#125;
    <Route path=<span class="hljs-string">'/about'</span> component=&#123;About&#125; />
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> <span class="hljs-attr">exact</span> /></span></span> &#123;<span class="hljs-comment">/*要求严格匹配*/</span>&#125;
    <Route path=<span class="hljs-string">'/home/a'</span> component=&#123;HomeA&#125; /> &#123;<span class="hljs-comment">/*home子路由*/</span>&#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果加上 给对应的路由加上 exact 属性, 就能预防这种情况</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac4ee401221f4beaae07dc1f70cbf23e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-41">传值</h2>
<blockquote>
<p>总的来说， 通过params的形式， React会从路径中解析出对应参数</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fc29abf0304402bbec4ac42ce54cb3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-42">params</h3>
<blockquote>
<p>明文传输, 但是刷新参数不消失</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e1d64b47cc8410f832dc3fbeac39083~tplv-k3u1fbpfcp-watermark.image" alt="路由传参_params.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>将要<strong>传递的值</strong>写到路径上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Link to=&#123;<span class="hljs-string">`/home/cHome/detail/<span class="hljs-subst">$&#123;item.id&#125;</span>/<span class="hljs-subst">$&#123;item.title&#125;</span>`</span>&#125;>&#123;item.title&#125;</Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将要传递的值动态写到路径上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Route path=<span class="hljs-string">'/home/cHome/detail/:id/:title'</span> component=&#123;Detail&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>再从props中结构出来</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Detail</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; id, title &#125; = <span class="hljs-built_in">this</span>.props.match.params
      <span class="hljs-keyword">let</span> content = msData.find( <span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
          <span class="hljs-keyword">return</span> item.id === id
      &#125;)
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">li</span>></span>content: &#123;content.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">li</span>></span>id: &#123;id&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">li</span>></span>title: &#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">search</h3>
<blockquote>
<p>问号传参的形式传递值， 并且无需在Route的path中标明键,  同样刷新不会丢失参数</p>
</blockquote>
<ul>
<li>传值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Link to=&#123;<span class="hljs-string">`/home/cHome/detail/?id=<span class="hljs-subst">$&#123;item.id&#125;</span>&title=<span class="hljs-subst">$&#123;item.title&#125;</span>`</span>&#125;>&#123;item.title&#125;</Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接收(urlencoded)</li>
</ul>
<blockquote>
<p>$ yarn add qs</p>
<blockquote>
<p>一个用于解析urlencoded格式的三方库</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// in component of Route </span>
<span class="hljs-keyword">const</span> &#123;search&#125; = <span class="hljs-built_in">this</span>.props.location 
<span class="hljs-comment">// 接受形式为未处理的字符串 ?id=xx&title=xx </span>
<span class="hljs-keyword">const</span> &#123; id, title &#125; = qs.parse(search.substring(<span class="hljs-number">1</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">query</h3>
<blockquote>
<p>非明文传输, 并且刷新了参数会丢失</p>
</blockquote>
<ul>
<li>传入数据, 并且无需在Route中定义</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><Link to=&#123;&#123;<span class="hljs-attr">pathname</span>:<span class="hljs-string">'/home'</span>, <span class="hljs-attr">query</span>: totalData&#125;&#125;>Home</Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接收参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.props.location)
      <span class="hljs-keyword">const</span> &#123;title, age&#125; = <span class="hljs-built_in">this</span>.props.location.query
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
              Home: &#123;title&#125;
              age: &#123;age&#125;
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>刷新后数据丢失</strong></li>
</ul>
<blockquote>
<p>当让你需要自己做一点处理, 防止错误蔓延, 我们会在ErrorBoundary讲到如何预防子组件的错误蔓延到父组件</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ef67926864445bc9052e03ffce361f3~tplv-k3u1fbpfcp-watermark.image" alt="路由传参_qeury.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-45">state</h3>
<blockquote>
<p>非明文传输, 并且刷新后数据不丢失, 使用方式跟query相同, 只不过键名换成了 state</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><Link to=&#123;&#123;<span class="hljs-attr">pathname</span>:<span class="hljs-string">'/home'</span>, <span class="hljs-attr">query</span>: totalData&#125;&#125;>Home</Link>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; state &#125; = <span class="hljs-built_in">this</span>.props.location
      <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
              Home:&#123;state&#125;
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>四种传参方式感觉都有自己的使用场景, 怎么使用就看个人了</li>
</ul>
<h2 data-id="heading-46">编程式路由</h2>
<blockquote>
<p>编程式路由的使用方式非常简单, 就相当于你无需去写一个Link组件, 而是直接通过函数就能够让页面实现跳转.</p>
</blockquote>
<ul>
<li>如果你使用过小程序或者uniapp就知道, 这个就类似于 navigateTo(&#123;&#125;)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d279f27e7e7041ffbec718b8fe5f3731~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这里的使用非常简单, 就不做演示了</li>
</ul>
<p>添加一个<strong>事件对象</strong>, 当点击这个按钮我们就实现跳转</p>
<pre><code class="hljs language-js copyable" lang="js"><button onClick=&#123;<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.push(item.title, item.id)&#125;>push</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">push (title, id) &#123;
  <span class="hljs-built_in">this</span>.props.history.push(<span class="hljs-string">`/home/cHome/detail`</span>,&#123;title, id&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就完成了一次跳转</p>
<p><code>push</code>意为, 往浏览器历史栈顶放入一个历史记录, 然后跳转.</p>
<p><code>replace</code>则是, 替代掉当前的栈顶的一个记录, 换成当前的. 也就是说, 按回退键是回不到跳转前的页面的.</p>
<p><code>forward</code> 就是浏览器跳转页面的向前键</p>
<p><code>back</code> 就是浏览器跳转页面的回退键</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b900bb119ab408fbef720f54bb18efc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-47">路由懒加载（Lazy-load）</h2>
<blockquote>
<p>与图片懒加载同理, 就是在用到了这个路由组件的时候, 我们才去进行加载, 这是很有必要的优化手段, 可以提高当前页面的渲染速度, 具体案例请查看项目</p>
</blockquote>
<h3 data-id="heading-48">lazy</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, lazy, Suspense &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 通过lazy函数引入 组件</span>
<span class="hljs-keyword">const</span> About = lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./pages/About'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-49">Suspense</h3>
<blockquote>
<p>他可以接受一个fallback属性的组件， 用于产生过渡效果</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><div className=<span class="hljs-string">'right'</span>> 
    &#123;<span class="hljs-comment">/* 路由切換 */</span>&#125; 
    <Suspense fallback=&#123;<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Loading</span> /></span></span>&#125;>  &#123;<span class="hljs-comment">/*过渡效果组件*/</span>&#125;
        <Route path=<span class="hljs-string">'/about'</span> component=&#123;About&#125; /> 
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/home'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span> /></span></span> 
    </Suspense> 
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-50">Redux</h1>
<blockquote>
<p>全局状态管理， 注册至Redux的状态可以在任何组件内直接获取。Redux的使用相对比较复杂, 我十分建议您学习了概念, 要通过Demo看看整个redux是怎么串起来的</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b25488999b6347e0b424fcb0a6b5fa84~tplv-k3u1fbpfcp-watermark.image" alt="Redux.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-51">怎么理解Redux</h2>
<blockquote>
<p>对于这些模块的翻译， 纯粹个人理解， 而非官方翻译</p>
</blockquote>
<ul>
<li><strong>Actions（指令）</strong></li>
<li><strong>Reducers（执行）</strong></li>
<li><strong>Store(存储动作执行的结果)</strong></li>
</ul>
<p><strong>怎么理解？</strong></p>
<blockquote>
<p>可以想象你在银行ATM存钱的过程， 你（<code>Components</code>）按了存款的指令， 并把钱（<code>data: 数据</code>）放入机子中。ATM（<code>Store</code>）接收到你这个指令（<code>Actions</code>）会去在你的存款中加上一笔钱（<code>Reducers</code>）， 也就是执行你的指令</p>
</blockquote>
<ul>
<li>
<p>你无法直接取钱， 存钱， 需要经过ATM操作（无法直接从store[propName]拿到属性， 必须通过<code>getState()</code></p>
</li>
<li>
<p>你可以在全国各地的ATM中拿到你的钱（<strong>公共状态</strong>)</p>
</li>
</ul>
<h2 data-id="heading-52">使用</h2>
<blockquote>
<p>根据我们在银行存钱的过程， 我们来看看一个完整的Redux流程是怎样的</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3078a5f2c021429aa6be3db788b91e12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-53">Store(存储动作执行的结果)</h2>
<blockquote>
<p>在使用Redux， 你需要创建一个store实例， 用来分发， 存储数据。 也就是要有一个store.js的入口文件</p>
</blockquote>
<ul>
<li>这一步就好比， 你在预设提款机的操作， <strong>countReducer</strong> 就是预设文件， 存入 <strong>store</strong> 中告诉它， 它会有哪些操作。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store.js </span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>; 
<span class="hljs-comment">// 需要在一开始就让Redux知道要怎样执行你的指令</span>
<span class="hljs-keyword">import</span> countReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./count-reducers'</span> 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(countReducer)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-54">APIs</h2>
<ul>
<li><strong>store.dispatch(action)</strong> 拿到一个动作，通知Reducer执行</li>
</ul>
<blockquote>
<p>Actions我们在介绍该</p>
</blockquote>
<ul>
<li><strong>store.subscribe</strong> 监听State， 如果State发生变化， 立即执行该函数, 用于通知视图层更新（重新渲染）</li>
</ul>
<p>由于我们更改状态只改变了, store中的状态, 这可能导致页面中有些视图应该基于数据发生改变, 但是没有发起, 以下的监听方式就十分重要的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 项目入口文件</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/store'</span>


ReactDom.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
store.subscribe( <span class="hljs-function">() =></span> &#123;
    ReactDom.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>store.getState</strong> 外部是无法直接获取状态（state）的， 需要通过函数store.getState()获取</li>
</ul>
<hr>
<blockquote>
<p>通常来说, 在一个企业项目中, store, actions 都是单独写成一个文件的, 所以我们下列的代码, 也仿照这个习惯</p>
</blockquote>
<h2 data-id="heading-55">Actions（指令）</h2>
<ul>
<li>一个合法的 Action 对象：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">action = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'whatWillDo'</span>,
    <span class="hljs-attr">payload</span>: data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-56">指令文件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Action.js redux的动作， 单独一个文件管理 </span>
<span class="hljs-keyword">import</span> &#123;INCREMENT, DECREMENT&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./constant'</span> 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> incrementAction = <span class="hljs-function"><span class="hljs-params">data</span> =></span> (&#123;<span class="hljs-attr">type</span>: INCREMENT, data&#125;) 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> decrementAction = <span class="hljs-function"><span class="hljs-params">data</span> =></span> (&#123;<span class="hljs-attr">type</span>: DECREMENT, data&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-57">使用</h3>
<blockquote>
<p><code>Actions</code> 需要通过 <strong>store</strong> 暴露的<code>dispatch（[object]）</code>进行分发</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span> 
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'../../redux/store'</span> 
<span class="hljs-keyword">import</span> &#123; incrementAction, decrementAction&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../redux/count_action'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Header</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123; 
    increament = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123; 
        store.dispatch(incrementAction(value))
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当然如果你不愿意创建Actions文件， 也可以这样</li>
</ul>
<blockquote>
<p>你传入的Action对象， 只要是合法的就能被接受</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Header</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123; 
    increament = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123; 
        store.dispatch(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'increament'</span>, <span class="hljs-attr">data</span>: value&#125;)
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-58">异步的Action</h3>
<blockquote>
<p>组件需要通过</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 异步</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addActionAsync = <span class="hljs-function">(<span class="hljs-params">data, time</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            dispatch(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'add'</span>, <span class="hljs-attr">payload</span>: data&#125;)
        &#125;, time)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们返回了一个函数， 并非常规的<strong>Action对象</strong>， 正常使用这个<code>Action</code>是会报错的， 因为 Redux 的<code>Reducers</code>, 不能接受一个函数作为<code>Action</code></p>
<ul>
<li><strong>怎么解决?</strong></li>
</ul>
<blockquote>
<p>我们需要在store.js中使用一个叫thunk的中间件</p>
<blockquote>
<p>$ yarn add redux-thunk</p>
</blockquote>
</blockquote>
<p>在store中使用中间件, 需要传入一个由 Redux 提供的函数 <code>applyMiddleware()</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>; 
<span class="hljs-keyword">import</span> countReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./count-reducers'</span> 
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(countReducer, applyMiddleware(thunk))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-59">Reducers（执行）</h2>
<blockquote>
<p><strong>Reducers</strong> 从名字来看应该翻译成<strong>累加器</strong>, 它是基于前状态进行加工得到目前的状态</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09bef74bb749483e86fe420bf37ed1de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-60">要求</h3>
<ul>
<li>
<p>在store.js文件中，需要通过createStore()传入reducers， 告诉redux，当接收到什么动作指令的时候， 需要做什么事情</p>
</li>
<li>
<p>要求 reducers 是一个纯函数</p>
</li>
</ul>
<h3 data-id="heading-61">使用</h3>
<ul>
<li>定义一个初始状态, 在传入Reucer函数的时候, 项目初始化就会定义一个相关的 state</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> initState = <span class="hljs-number">0</span> 

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addReudcer</span> (<span class="hljs-params">prevState = initState, action</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; type, payload &#125; = action
    <span class="hljs-keyword">switch</span> (type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'add'</span>:
            <span class="hljs-keyword">return</span> prevState + payload
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">return</span> prevState <span class="hljs-comment">// （初始化的时候，无指令， 返回默认值）</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在<code>store.js</code>中定义</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware  &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> addReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/addReducer"</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(addReducer, applyMiddleware(thunk))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">集中暴露</h3>
<blockquote>
<p>如果你熟悉 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2Fguide%2Fstate.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/guide/state.html" ref="nofollow noopener noreferrer">VueX-State</a> 你肯定很奇怪, 为什么没有类似于 <code>state.js</code> 管理全局状态的文件</p>
</blockquote>
<p>单独使用暴露一个 Reducer 的时候, <strong>其返回值就是当前的state</strong>, 因为 state 内就这么一个值.</p>
<p>但是如果我们使用的 Reducer 特别多, 通常就需要集中暴露, 并且给每一个 Reducer 的返回值定义一个<strong>键名</strong>.</p>
<ul>
<li>集中 Reducer 的文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// allReducers.js</span>
<span class="hljs-keyword">import</span> &#123; combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> addReudcer <span class="hljs-keyword">from</span> <span class="hljs-string">"./addReducer"</span>;
<span class="hljs-comment">// 合并所有的reducers</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> combineReducers(&#123;
    <span class="hljs-attr">add</span>: addReudcer
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以同样的方式传入<code>allReducers</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware  &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> allReducers <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/allReducers"</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(allReducers, applyMiddleware(thunk))
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>请先看一下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide%2Ftree%2Fmaster%2Fstudy-demo%2Ftest-Demo%2FRedux%2Fsrc_1.%25E6%259C%2580%25E7%25AE%2580%25E5%258D%2595%25E7%259A%2584redux_Demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide/tree/master/study-demo/test-Demo/Redux/src_1.%E6%9C%80%E7%AE%80%E5%8D%95%E7%9A%84redux_Demo" ref="nofollow noopener noreferrer"> 最简单的redux_Demo </a>的代码</strong>, 这里我们直接在UI组件内使用了Redux, 但实际上这并<strong>不合规范</strong></p>
<h2 data-id="heading-63">connect（规范）</h2>
<blockquote>
<p>正常情况下使用Redux要求: 我们要将对 store 的 <code>state</code> 做的操作, 剥离出UI组件, 通过prop的形式传入操作函数,以及状态值. <strong>UI组件只负责展示</strong></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43b7d97ff5914181942c49db3ca6acdb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<blockquote>
<p>如果每次都需要自己书写一个父组件,那就太麻烦了, Redux也替我们做了这一步, 通过<strong>connect立即执行函数</strong>,  将能简写这一步</p>
</blockquote>
<h3 data-id="heading-64">使用</h3>
<ul>
<li>假设我们有一个 <code>ComponentA</code> 组件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ComponentA</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'C-A'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>ComponentA<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建一个父容器(无需自己创建), 传入UI组件, 这个<strong>立即执行函数</strong>执行后会默认返回父组件, 也就是供我们使用的组件, 所以我们要将其暴露出去, 好在外部能够使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect()(ComponentA)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-65">父组件如何传值给子组件?</h3>
<blockquote>
<p><strong>connect（mapStateToProps：function， mapDispatchToProps： function)</strong> 函数接收两个参数[<code>mapStateToProps</code>] [<code>mapDispatchToProps</code>]</p>
</blockquote>
<ol>
<li>mapStateToProps(state) 这个函数能够默认接收到 <code>store.state</code> 对象, 假设我们需要获得一个叫 add 的 state</li>
</ol>
<p><strong>这个函数传入connect后会被执行, 并且返回值作为 props 传入UI组件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123; <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">add</span>: state.add &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>mapDispatchToProps(dispatch) 接收到一个 <code>store.dispatch</code> 函数, 用于执行动作</li>
</ol>
<p><strong>这个函数传入connect后会被执行, 并且返回值(函数)作为 props 传入UI组件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">addCount</span>: <span class="hljs-function"><span class="hljs-params">value</span> =></span> dispatch(addAction(value)),
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>传递给connect, 这样子一个完整的父组件我们就创建成功了</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect( mapStateToProps, mapDispatchToProps )(ComponentA)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>看到这里你可能会觉得奇怪, 在[<code>mapStateToProps</code>] [<code>mapDispatchToProps</code>]参数中, 我们都使用了 store对象里面的state, dispatch函数, 那这两个值是从哪里拿到的? 当然是我们自己<strong>让 store 作为 prop</strong> 传进去的,</p>
</blockquote>
<ol start="4">
<li>我们来看看怎么使用这个组件, 非常简单.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ComponentA <span class="hljs-keyword">from</span> <span class="hljs-string">"./containers/ComponentA"</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/store'</span>; <span class="hljs-comment">// 引入 store 对象</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ComponentA</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;/</span>></span> &#123;/* 将store传入 */&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>子组件怎么使用?</li>
</ol>
<blockquote>
<p>就像使用prop传递过来的 数据/函数 一样使用, 没有任何差别, 如果你想看完整代码👉 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide%2Ftree%2Fmaster%2Fstudy-demo%2Ftest-Demo%2FRedux%2Fsrc_2.redux_%25E5%2589%25A5%25E7%25A6%25BB" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide/tree/master/study-demo/test-Demo/Redux/src_2.redux_%E5%89%A5%E7%A6%BB" ref="nofollow noopener noreferrer"><strong>redux_剥离</strong></a></p>
</blockquote>
<h3 data-id="heading-66">connect参数的简写</h3>
<ul>
<li>mapDispatchToProps其实允许做为一个对象传入</li>
<li>并且，原先需要自己执行的 dispatch 也可以交给 <strong>conncet</strong> 来做， 我们仅需将 action作为一个对象的键值对丢进去</li>
</ul>
<p>简写前：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(
    <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            state
        &#125;
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
           <span class="hljs-attr">addCount</span>: <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> dispatch(addAction(value)),
           <span class="hljs-attr">addCountAsync</span>: <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> dispatch(addActionAsync(value)),
        &#125;
    &#125;
)(ComponentA)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简写后：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect( 
    <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123; state &#125;), 
    &#123; 
        <span class="hljs-attr">addCount</span>: addAction, 
        <span class="hljs-attr">addCountAsync</span>: addActionAsync, 
    &#125; 
)(ComponentA)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">无需逐个传入store.js</h3>
<blockquote>
<p>并不是每个这样的组件， 我们都需要自己传入store</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js 入口文件</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/store'</span>
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span> <span class="hljs-comment">// 👈</span>

ReactDom.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>, 
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
    
<span class="hljs-comment">// 也不需要自己监听了</span>
<span class="hljs-comment">// store.subscribe(()=>&#123;</span>
<span class="hljs-comment">//     ReactDom.render(<App />, document.getElementById('root'))</span>
<span class="hljs-comment">// &#125;)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-68">Redux可视化插件</h2>
<blockquote>
<p>更方便地观察数据流动</p>
<blockquote>
<p>$ yarn add redux-devtools-extension</p>
</blockquote>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f85cb3be6c3433ab675e9cc94f957d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store.js</span>
<span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>
<span class="hljs-keyword">import</span> &#123; composeWithDevTools &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-devtools-extension"</span>;
<span class="hljs-keyword">import</span> allReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(allReducer, composeWithDevTools(applyMiddleware(thunk)))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>谷歌浏览器安装一个插件</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141ebf64e7234479a111ef03d76c3250~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>完毕</strong>😄</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8d37b0728ae478cbb9b92511507abbe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-69">Hooks</h1>
<blockquote>
<p>钩子（Hook）勾出React的特性</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/677b3341d84449fbb7b8f67d0d726723~tplv-k3u1fbpfcp-watermark.image" alt="Hooks.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-70">理念</h2>
<blockquote>
<p>hooks为React提供了更加直接, 简单的API.</p>
</blockquote>
<p><strong><code>hook</code>像是一个比起类组件更加底层的概念</strong></p>
<pre><code class="hljs language-mermaid" lang="mermaid">stateDiagram-v2

hook --> class组件

React底层 --> hook

</code></pre>
<p><strong>解决了什么问题？</strong></p>
<ul>
<li>函数式组件无法使用像类组件的一些 React 特性，如： State, 生命周期钩子， ref等</li>
<li>class式组件对于初学者有一定的学习门槛， 函数组件更加友好
类式组件依然可以使用，两者没有任何高低之分</li>
</ul>
<h2 data-id="heading-71">注意</h2>
<ul>
<li>
<p>可以从useState返回的数组中结构出 <strong>state, setState()</strong></p>
</li>
<li>
<p><strong>setState([object | (preState)⇒&#123;&#125;])</strong></p>
</li>
</ul>
<h2 data-id="heading-72">useState</h2>
<blockquote>
<p>函数式组件无法获取到react实例, 也就无法获取state与setState()</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/734442995ad7437595c2700a15495149~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-comment">// 函数- 如果以use开头， React 会认为你使用了自定义hook</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StateHook</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>) <span class="hljs-comment">// 👈</span>

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h5</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            &#123;/* 传函数 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count => count + 1)&#125;>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>对比(class组件)</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 对照(类)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StateHook</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;
    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h5</span>></span>count: &#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123;count: this.state.count + 1&#125;)&#125;>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-73">useEffect</h2>
<blockquote>
<p>函数式组件无法使用生命周期钩子， useEffect就是来解决这个问题的</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2147f07e23354b509b4b5b3fc52ca092~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-comment">// 函数- 如果以use开头， React 会认为你使用了自定义hook</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">EffectHook</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)

    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 这个函数相当于 componentDidMount + componentDidUpdate</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'页面初始化完毕/更新数据完毕'</span>)
        <span class="hljs-comment">// 返回的函数就相当于 componentWillUnmount</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 做一些清理处理， 如清理一个定时器 clearInterval()</span>
            <span class="hljs-comment">// 严格来讲，仅在清理副作用上与componentWillUnmount功能类似， 但是并非等同于卸载钩子</span>
        &#125;
    &#125;)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>) </span>&#123;
        setCount(count + <span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h5</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>对比</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 对照(类)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EffectHook</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;

    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'页面初始化完毕'</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'更新数据完毕'</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h5</span>></span>count: &#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123;count: this.state.count + 1&#125;)&#125;>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'组件即将卸载'</span>) <span class="hljs-comment">// 仅演示， effect函数的返回函数跟它还是有一些差别，</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>useEffect</strong> 相当于三个钩子的整合</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> timer =<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
       add()     <span class="hljs-comment">// 这一部分相当于 componentDidMount 和 componentDidUpdate</span>
    &#125;,<span class="hljs-number">1000</span>)      <span class="hljs-comment">// 至于趋进于哪个取决于第二个参数数组[]</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">clearInterval</span>(timer) <span class="hljs-comment">// 这个返回函数</span>
    &#125;
&#125;,[])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-74">参数2</h3>
<blockquote>
<p>用于监听页面的改动</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 不传递第二个参数， 页面中任何改动都会被监听</span>
React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// .....</span>
&#125;)
<span class="hljs-comment">// 传递一个空数组， 页面中任何改动都不监听</span>
React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// .....</span>
&#125;,[])
<span class="hljs-comment">// 传递具体的状态名， 则该状态改变会被监听</span>
React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// .....</span>
&#125;,[stateName])
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-75">useRef</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fe7e2def267414989ceffcdd273e40e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">RefHook</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">const</span> countRef = useRef() <span class="hljs-comment">//👈</span>
    <span class="hljs-keyword">const</span> headerRef = useRef()
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showInfo</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'countRef'</span>, countRef)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'headerRef'</span>, headerRef)
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h5</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;headerRef&#125;</span>></span>header<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;countRef&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;showInfo&#125;/</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>对比</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">对照(类)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RefHook</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;

    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    showInfo = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'countRef'</span>, <span class="hljs-built_in">this</span>.refs.countRef)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'headerRef'</span>, <span class="hljs-built_in">this</span>.refs.headerRef)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h5</span>  <span class="hljs-attr">ref</span>=<span class="hljs-string">'headerRef'</span> ></span>header<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'countRef'</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.showInfo&#125;/</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-76">自定义Hook</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/591f4d701c42450e970282cc3ec04a4d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>以use开头定义我们的hook函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这部分逻辑就可以使用到任何其他组件中去了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useAllself</span>(<span class="hljs-params">initState</span>) </span>&#123;

    <span class="hljs-keyword">const</span> [count, setCount] = useState(initState)

    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count'</span>, count) <span class="hljs-comment">// 监听</span>
    &#125;)
    <span class="hljs-comment">// 如果值为偶数， 就返回</span>
    <span class="hljs-keyword">return</span> [count, setCount]

&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> SelfHook
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SelfHook</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">const</span> [count, setCount] = useAllself(<span class="hljs-number">0</span>) <span class="hljs-comment">// 使用我们抽象的hook</span>
    
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>Home Component<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h5</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>count add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注：</strong><a href="https://link.juejin.cn/?target=%25E6%259B%25B4%25E5%25A4%259A%25E7%259B%25B8%25E5%2585%25B3%25E7%259A%2584hookAPI" target="_blank" title="%E6%9B%B4%E5%A4%9A%E7%9B%B8%E5%85%B3%E7%9A%84hookAPI" ref="nofollow noopener noreferrer">更多相关的hookAPI</a></p>
<p>在hook的加入以后， 函数组件的优势变得极为明显， 现在绝大多数开发用的也都是函数组件， 并且我认为这也是未来的一种趋势</p>
<hr>
<h1 data-id="heading-77">拓展</h1>
<blockquote>
<p>一些有用的扩展</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e49441c69ca84d0389ac7f5d64af5990~tplv-k3u1fbpfcp-watermark.image" alt="拓展.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-78">Fragment</h2>
<blockquote>
<p>JSX语法要求每一个组件最外层都必须由一个标签包裹， 但是这个标签是多余的， 这时候使用Fragment组件， 可以解决层级多余的问题</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40c5610066c24336ad65e568b50e4f58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-79">使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component,Fragment &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoFrag</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Fragment</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span>
               <span class="hljs-tag"><<span class="hljs-name">p</span>></span>111<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">Fragment</span>></span></span>
        )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这两种写法都有同样的效果， 但是空标签不允许你传入任何属性， 所以如需传入属性，则使用Fragment</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoFrag</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
               <span class="hljs-tag"><<span class="hljs-name">p</span>></span>111<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"></></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-80">Context</h2>
<blockquote>
<p>在通信章节我们提到的 context， 允许你进行祖组件与孙组件的,跨组件通信</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffab062c954f45ca83f7d11c293a7116~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-81">使用</h3>
<blockquote>
<p>建议看一下Demo的代码 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinkSofuny%2Freact-study-guide%2Ftree%2Fmaster%2Fstudy-demo%2Ftest-Demo%2F%25E6%2589%25A9%25E5%25B1%2595%2Fsrc_context" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinkSofuny/react-study-guide/tree/master/study-demo/test-Demo/%E6%89%A9%E5%B1%95/src_context" ref="nofollow noopener noreferrer">context通信</a></p>
</blockquote>
<p>假设你希望在不同的文件使用context， 那我建议你将context单独建立为一个文件去暴露</p>
<ul>
<li>引入context</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyContext = React.createContext() 
<span class="hljs-keyword">const</span> &#123; 
    Provider,     
    Consumer  
&#125; = MyContext 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用</li>
</ul>
<blockquote>
<p>为了看起来更加直观， 假设下列代码都在同一个文件内， 如需看多文件的情况， 请看Demo</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyContext = React.createContext()
<span class="hljs-keyword">const</span> &#123;Provider, Consumer&#125; = MyContext
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Grandpa</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Link'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;name, age&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'grand'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我是祖组件<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;name,age</span> &#125;&#125;></span> // 👈
                    <span class="hljs-tag"><<span class="hljs-name">Father</span> /></span>  &#123;/* 父组件 */&#125;
                <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>孙组件接收(类式)</li>
</ul>
<blockquote>
<p>基于 MyContext 定义一个私有属性contextType</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-keyword">static</span> contextType = MyContext
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;name, age&#125; = <span class="hljs-built_in">this</span>.context
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'son'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我是孙组件<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是:&#123;name&#125;, 今年: &#123;age&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>孙组件接收(函数式)</li>
</ul>
<blockquote>
<p>通过 Context 下的 Consumer 接受到的参数进行传递</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Son</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'son'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我是孙组件<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Consumer</span>></span>
                &#123;
                    value => <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是:&#123;value.name&#125;, 今年: &#123;value.age&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                &#125;
            <span class="hljs-tag"></<span class="hljs-name">Consumer</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-82">PureComponent</h2>
<blockquote>
<p>对数据进行变更的时候, 无论 <code>setState</code> 是否改变数据, <code>render</code> 函数都一定会执行, 并且如果组件内嵌套有其他组件, 子组件的 <code>render</code> 也会被调用, 即时数据没有任何改变.这就造成了很多无谓的组件重渲染</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2816db47beb4ea088b7a1fdb4d8e2c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解决办法</strong></p>
<ol>
<li>重写 <strong>shouldComponentUpdate</strong> 钩子</li>
</ol>
<p>       <code>shouldComponentUpdate</code> 默认情况下都会返回一个 <code>true</code>， 使得组件接下来的生命周期钩子能够被调用， 如果返回 <code>false</code> 则 <strong>像是一个阀门被关闭了一样， 则它以下的钩子不再执行</strong></p>
<p>       根据这一点， 我们就可以重写它， 去判断传入该组件的 state, props 有没有发生改变， 有的话 我们在让其继续执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params">nextProps,nextState</span>)</span> &#123;
    <span class="hljs-comment">// 如数据未变化， 阻止render</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变前'</span>, <span class="hljs-built_in">this</span>.state, <span class="hljs-built_in">this</span>.props);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改变后'</span>, nextState, nextProps);
    <span class="hljs-keyword">return</span> !<span class="hljs-built_in">this</span>.state.name === nextState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里就不提供Demo了， 因为一般不会这么做， 🤭</p>
</blockquote>
<ol start="2">
<li>让你的组件继承 <strong>PureComponent</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, PureComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 改变组件的继承</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123; <span class="hljs-comment">// 👈</span>
<span class="hljs-comment">// ....</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong> <strong>PureComponent</strong> 内对 <strong>shouldComponentUpdate</strong> 进行重写, 更好的检测了 <code>setState</code> , <code>props</code> 的变化, 但是其只对 <code>State</code> 进行浅比较, 只判断<code>SetState([object])</code> 的参数对象object的内存地址是否发生了变化, 也就说, 在不改变State对象地址的情况下,修改值, 依然会导致render调用</p>
</blockquote>
<h2 data-id="heading-83">RenderProps</h2>
<blockquote>
<p>从直接传组件变为回调函数的形式</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/899ec8614a594735899dcb79e5e6889b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-84">常规的props传组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span> ></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> ></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">A</span> <span class="hljs-attr">B</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">B</span> /></span>&#125;/> // 👈
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A Component</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'A'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>AAA<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                &#123;this.props.B&#125; // 👈
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种传递方式很方便， 但无法传参数</p>
<h3 data-id="heading-85">Render属性传递一个函数</h3>
<blockquote>
<p>给A组件传递一个接受 <code>name</code>, <code>age</code> 的函数</p>
</blockquote>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span> ></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> ></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">A</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;(name,</span> <span class="hljs-attr">age</span>) =></span> <span class="hljs-tag"><<span class="hljs-name">B</span>  <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;name&#125;</span> <span class="hljs-attr">age</span>=<span class="hljs-string">&#123;age&#125;/</span>></span>&#125;/> // 👈
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A Component</li>
</ul>
<blockquote>
<p>将数据作为 props 传给 B 组件</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'我是A传递给B的数据'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-string">'我也是呢'</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; name, age &#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'A'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>AAA<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                &#123;this.props.render( name, age )&#125; // 👈
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>B Component</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'B'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>BBB<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                &#123;this.props.name&#125;<span class="hljs-tag"><<span class="hljs-name">br</span> /></span> // 👈
                &#123;this.props.age&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-86">ErrorBoundary</h2>
<blockquote>
<p>防止错误的扩散处理, React如果子组件发生错误, 会导致整个页面渲染不出来, 这时候错误的边界处理就十分重要了, <strong>但只能捕获子组件生命周期内发生的错误</strong></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2554e154fe446fc9efacf28f8c3fee2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-87">使用</h3>
<blockquote>
<p>核心钩子： <strong>getDerivedStateFromError</strong> 这个钩子会返回一个错误对象， 用于捕获子组件是否发生错误</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 从Error中获得一个state状态, </span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromError</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>, err)
    <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">hasErr</span>: err&#125;
&#125;
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span> ></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> ></span>index<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            &#123;/* 错误对象存在,则渲染条件成立的DOM*/&#125;
            &#123;this.state.hasErr ? <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这里发生错误了<span class="hljs-tag"></<span class="hljs-name">h1</span>></span> : <span class="hljs-tag"><<span class="hljs-name">A</span> /></span>&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>记录错误</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, errorInfo</span>)</span> &#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发生错误咯'</span>， error, errorInfo)  <span class="hljs-comment">// 错误发生完毕后， 可进行记录操作 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>注意（摘自React官网）:</strong></li>
</ul>
<blockquote>
<p>错误边界<strong>无法</strong>捕获以下场景中产生的错误：</p>
</blockquote>
<ul>
<li>事件处理（<a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Fdocs%2Ferror-boundaries.html%23how-about-event-handlers" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/docs/error-boundaries.html#how-about-event-handlers" ref="nofollow noopener noreferrer">了解更多</a>）</li>
<li>异步代码（例如 <code>setTimeout</code> 或 <code>requestAnimationFrame</code> 回调函数）</li>
<li>服务端渲染</li>
<li>它自身抛出来的错误（并非它的子组件）</li>
</ul>
<hr>
<p><strong>（完）</strong></p>
<h1 data-id="heading-88">参考资料</h1>
<p><strong>1. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgoshakkk.name%2Fcontrolled-vs-uncontrolled-inputs-react%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://goshakkk.name/controlled-vs-uncontrolled-inputs-react/" ref="nofollow noopener noreferrer">controlled-vs-uncontrolled</a> 受控组件与非受控组件的区别</strong></p>
<p><strong>2. <a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/" ref="nofollow noopener noreferrer">React</a> React官方文档</strong></p>
<p><strong>3. <a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-router.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-router.docschina.org/" ref="nofollow noopener noreferrer">React-router</a> React-Router文档</strong></p>
<hr>
<h1 data-id="heading-89">感谢😘</h1>
<p>这篇文章纯粹是从我个人学习React的角度, 去教自己怎么学习React. 可能很多地方您觉得我一笔带过, 或是讲得不正确, 也希望您能提出来. 这也是我自己可能学习不到位的地方, <strong>十分感谢, 您能看到这里</strong></p>
<hr>
<p><strong>如果觉得文章内容对你有帮助:</strong></p>
<ul>
<li>❤️欢迎关注点赞哦! 我会尽最大努力产出高质量的文章</li>
</ul>
<p>个人公众号: <strong>前端Link</strong><br>
联系作者: <strong>linkcyd</strong> 😁</p></div>  
</div>
            