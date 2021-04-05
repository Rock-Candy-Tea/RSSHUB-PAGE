
---
title: 'React Hook简单使用案例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ca05c93171402297776f848a4ba7f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 19:42:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ca05c93171402297776f848a4ba7f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章分享两个使用React Hook以及函数式组件开发的简单示例。</p>
<h3 data-id="heading-0">一个简单的组件案例</h3>
<p>Button组件应该算是最简单的常用基础组件了吧。我们开发组件的时候期望它的基础样式能有一定程度的变化，这样就可以适用于不同场景了。第二点是我在之前做项目的时候写一个函数组件，但这个函数组件会写的很死板，也就是上面没有办法再绑定基本方法。即我只能写入我已有的方法，或者特性。希望编写Button组件，即使没有写onClick方法，我也希望能够使用那些自带的默认基本方法。</p>
<p>对于第一点，我们针对不同的className，来写不同的css，是比较好实现的。</p>
<p>第二点实现起略微困难。我们不能把Button的默认属性全部写一遍，如果能够把默认属性全部导入就好了。</p>
<p>事实上，React已经帮我们实现了这一点。<code>React.ButtonHTMLAttributes<HTMLElement></code>里面就包含了默认的Button属性。可是我们又不能直接使用这个接口，因为我们的Button组件可能还有一些自定义的东西。对此，我们可以使用Typescript的交叉类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> NativeButtonProps = MyButtonProps & React.ButtonHTMLAttributes<HTMLElement>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，我们还需要使用<code>resProps</code>来导入其他非自定义的函数或属性。</p>
<p>下面是Button组件具体实现方案：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>

<span class="hljs-keyword">type</span> ButtonSize = <span class="hljs-string">'large'</span> | <span class="hljs-string">'small'</span>
<span class="hljs-keyword">type</span> ButtonType = <span class="hljs-string">'primary'</span> | <span class="hljs-string">'default'</span> | <span class="hljs-string">'danger'</span>

<span class="hljs-keyword">interface</span> BaseButtonProps &#123;
  className?: <span class="hljs-built_in">string</span>;
  disabled?: <span class="hljs-built_in">boolean</span>;
  size?: ButtonSize;
  btnType?: ButtonType;
  children?: React.ReactNode;
&#125;

<span class="hljs-keyword">type</span> NativeButtonProps = BaseButtonProps & React.ButtonHTMLAttributes<HTMLElement>
<span class="hljs-keyword">const</span> Button: React.FC<NativeButtonProps>= <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    btnType,
    className,
    disabled,
    size,
    children,
    <span class="hljs-comment">// resProps用于取出所有剩余属性</span>
    ...resProps
  &#125; = props
  <span class="hljs-comment">// btn, btn-lg, btn-primary</span>
  <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'btn'</span>, className, &#123;
    [<span class="hljs-string">`btn-<span class="hljs-subst">$&#123;btnType&#125;</span>`</span>]: btnType,
    [<span class="hljs-string">`btn-<span class="hljs-subst">$&#123;size&#125;</span>`</span>]: size,
    <span class="hljs-string">'disabled'</span>: disabled
  &#125;)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span>
      <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span>
      <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;disabled&#125;</span>
      &#123;<span class="hljs-attr">...resProps</span>&#125;
    ></span>
      &#123;children&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  )
&#125;

Button.defaultProps = &#123;
  <span class="hljs-attr">disabled</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">btnType</span>: <span class="hljs-string">'default'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Button
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的方式，我们就可以在我们自定义的Button组件中使用比如<code>onClick</code>方法了。使用Button组件案例如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">disabled</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">btnType</span>=<span class="hljs-string">'primary'</span> <span class="hljs-attr">size</span>=<span class="hljs-string">'large'</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"haha"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">btnType</span>=<span class="hljs-string">'danger'</span> <span class="hljs-attr">size</span>=<span class="hljs-string">'small'</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> alert('haha')&#125;>Test<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>展示效果如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ca05c93171402297776f848a4ba7f0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在这个代码中我们引入了一个新的npm package称之为<code>classnames</code>，具体使用方式可以参考<a href="https://github.com/JedWatson/classnames#readme" target="_blank" rel="nofollow noopener noreferrer">GitHub Classnames</a>，使用它就可以很方便实现className的扩展，它的一个简单使用示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js">classNames(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>); <span class="hljs-comment">// => 'foo bar'</span>
classNames(<span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>
classNames(&#123; <span class="hljs-string">'foo-bar'</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo-bar'</span>
classNames(&#123; <span class="hljs-string">'foo-bar'</span>: <span class="hljs-literal">false</span> &#125;); <span class="hljs-comment">// => ''</span>
classNames(&#123; <span class="hljs-attr">foo</span>: <span class="hljs-literal">true</span> &#125;, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>
classNames(&#123; <span class="hljs-attr">foo</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>

<span class="hljs-comment">// lots of arguments of various types</span>
classNames(<span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">duck</span>: <span class="hljs-literal">false</span> &#125;, <span class="hljs-string">'baz'</span>, &#123; <span class="hljs-attr">quux</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar baz quux'</span>

<span class="hljs-comment">// other falsy values are just ignored</span>
classNames(<span class="hljs-literal">null</span>, <span class="hljs-literal">false</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, &#123; <span class="hljs-attr">baz</span>: <span class="hljs-literal">null</span> &#125;, <span class="hljs-string">''</span>); <span class="hljs-comment">// => 'bar 1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过使用classNames，就可以很方便的在Button中添加个性化的属性。可以看到对于组件的HTML输出结果中有<code>haha</code>className：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn haha btn-primary btn-lg"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与此同时，我们上述代码方式也解决了自定义组件没有办法使用默认属性和方法问题。</p>
<h3 data-id="heading-1">更复杂的父子组件案例</h3>
<p>接下来我们展示一下如何用函数组件完成一个菜单功能。这个菜单添加水平模式和垂直模式两种功能模式。点开某个菜单详情，将这个详情作为子组件。</p>
<p>当然，菜单这个功能根本就不需要父组件传数据到子组件（子组件指的是菜单详情），我们为了学习和演示如何将父组件数据传给子组件，强行给他添加这个功能。有点画蛇添足，大家理解一下就好。</p>
<p>首先介绍父子组件的功能描述。Menu是整体父组件，MenuItem是每一个具体的小菜单，SubMenu里面是可以点开的下拉菜单。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb97db71f66c4167af67c3854dcb443c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下图是展开后的样子：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/118f8e261aec483ab6ef0956f7d763ae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>整体代码结构如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Menu</span> <span class="hljs-attr">defaultIndex</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">0</span>'&#125; <span class="hljs-attr">onSelect</span>=<span class="hljs-string">&#123;(index)</span> =></span> &#123;alert(index)&#125;&#125; mode="vertical" defaultOpenSubMenus=&#123;['2']&#125;>
  <span class="hljs-tag"><<span class="hljs-name">MenuItem</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">0</span>'&#125;></span>
    cool link
  <span class="hljs-tag"></<span class="hljs-name">MenuItem</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">MenuItem</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">1</span>'&#125;></span>
    cool link 2
  <span class="hljs-tag"></<span class="hljs-name">MenuItem</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">SubMenu</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"dropdown"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">MenuItem</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">3</span>'&#125;></span>
      dropdown 1
    <span class="hljs-tag"></<span class="hljs-name">MenuItem</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">MenuItem</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">4</span>'&#125;></span>
      dropdown 2
    <span class="hljs-tag"></<span class="hljs-name">MenuItem</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">SubMenu</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">MenuItem</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">2</span>'&#125;></span>
    cool link 3
  <span class="hljs-tag"></<span class="hljs-name">MenuItem</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Menu</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个组件中，我们用到了<code>useState</code>，另外因为涉及父组件传数据到子组件，所以还用到了<code>useContext</code>（父组件数据传递到子组件是指的父组件的index数据传递到子组件）。另外，我们还会演示使用自定义的<code>onSelect</code>来实现onClick功能（万一你引入React泛型不成功，或者不知道该引入哪个React泛型，还可以用自定义的补救一下）。</p>
<p><strong>如何写onSelect</strong></p>
<p>为了防止后面在代码的汪洋大海中难以找到onSelect，这里先简单的抽出来做一个onSelect书写示例。比如我们在Menu组件中使用onSelect，它的使用方式和onClick看起来是一样的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Menu</span> <span class="hljs-attr">onSelect</span>=<span class="hljs-string">&#123;(index)</span> =></span> &#123;alert(index)&#125;&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在具体这个Menu组件中具体使用onSelect可以这样写：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> SelectCallback = <span class="hljs-function">(<span class="hljs-params">selectedIndex: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>

<span class="hljs-keyword">interface</span> MenuProps &#123;
  onSelect?: SelectCallback;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现handleClick的方法可以写成这样：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">(<span class="hljs-params">index: string</span>) =></span> &#123;
    <span class="hljs-comment">// onSelect是一个联合类型，可能存在，也可能不存在，对此需要做判断</span>
    <span class="hljs-keyword">if</span> (onSelect) &#123;
      onSelect(index)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到时候要想把这个onSelect传递给子组件时，使用<code>onSelect: handleClick</code>绑定一下就好。（可能你没看太懂，我也不知道该咋写，后面会有整体代码分析，可能联合起来看会比较容易理解）</p>
<p><strong>React.Children</strong></p>
<p>在讲解具体代码之前，还要再说说几个小知识点，其中一个是React.Children。</p>
<blockquote>
<p>React.Children 提供了用于处理 this.props.children 不透明数据结构的实用方法。</p>
</blockquote>
<p>具体使用可以参考：<a href="https://zh-hans.reactjs.org/docs/react-api.html#reactchildren" target="_blank" rel="nofollow noopener noreferrer">React.Children.map</a></p>
<p>为什么我们会需要使用React.Children呢？是因为如果涉及到父组件数据传递到子组件时，可能需要对子组件进行二次遍历或者进一步处理。但是我们不能保证子组件是到底有没有，是一个还是两个或者多个。</p>
<blockquote>
<p>this.props.children 的值有三种可能：如果当前组件没有子节点，它就是 undefined ;如果有一个子节点，数据类型是 object ；如果有多个子节点，数据类型就是 array 。所以，处理 this.props.children 的时候要小心<sup>[1]</sup>。</p>
</blockquote>
<blockquote>
<p>React 提供一个工具方法 React.Children 来处理 this.props.children 。我们可以用 React.Children.map 来遍历子节点，而不用担心 this.props.children 的数据类型是 undefined 还是 object<sup>[1]</sup>。</p>
</blockquote>
<p>所以，如果有父子组件的话，如果需要进一步处理子组件的时候，我们可以使用React.Children来遍历，这样不会因为this.props.children类型变化而出错。</p>
<p><strong>React.cloneElement</strong></p>
<p>React.Children出现时往往可能伴随着React.cloneElement一起出现。因此，我们也需要介绍一下React.cloneElement。</p>
<blockquote>
<p>在开发复杂组件中，经常会根据需要给子组件添加不同的功能或者显示效果，react 元素本身是不可变的 (immutable) 对象， props.children 事实上并不是 children 本身，它只是 children 的描述符 (descriptor) ，我们不能修改任何它的任何属性，只能读到其中的内容，因此 React.cloneElement 允许我们拷贝它的元素，并且修改或者添加新的 props 从而达到我们的目的<sup>[2]</sup>。</p>
</blockquote>
<p>例如，有的时候我们需要对子元素做进一步处理，但因为React元素本身是不可变的，所以，我们需要对其克隆一份再做进一步处理。在这个Menu组件中，我们希望它的子组件只能是MenuItem或者是SubMenu两种类型，如果是其他类型就会报警告信息。具体来说，可以大致将代码写成这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (displayName === <span class="hljs-string">'MenuItem'</span> || displayName === <span class="hljs-string">'SubMenu'</span>) &#123;
  <span class="hljs-comment">// 以element元素为样本克隆并返回新的React元素，第一个参数是克隆样本</span>
  <span class="hljs-keyword">return</span> React.cloneElement(childElement, &#123;
    <span class="hljs-attr">index</span>: index.toString()
  &#125;)
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"Warning: Menu has a child which is not a MenuItem component"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>父组件数据如何传递给子组件</strong></p>
<p>通过使用Context来实现父组件数据传递给子组件。如果对Context不太熟悉的话，可以参考官方文档，<a href="https://zh-hans.reactjs.org/docs/context.html#contextprovider" target="_blank" rel="nofollow noopener noreferrer">Context</a>，在父组件中我们通过<code>createContext</code>来创建Context，在子组件中通过<code>useContext</code>来获取Context。</p>
<p><strong>index数据传递</strong></p>
<p>Menu组件中实现父子组件中数据传递变量主要是index。</p>
<p>最后附上完整代码，首先是Menu父组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState, createContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>
<span class="hljs-keyword">import</span> &#123; MenuItemProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./menuItem'</span>

type MenuMode = <span class="hljs-string">'horizontal'</span> | <span class="hljs-string">'vertical'</span>
type SelectCallback = <span class="hljs-function">(<span class="hljs-params">selectedIndex: string</span>) =></span> <span class="hljs-keyword">void</span>

<span class="hljs-keyword">export</span> interface MenuProps &#123;
  defaultIndex?: string;  <span class="hljs-comment">// 用于哪个menu子组件是高亮显示</span>
  className?: string;
  mode?: MenuMode;
  style?: React.CSSProperties;
  onSelect?: SelectCallback;  <span class="hljs-comment">// 点击子菜单时可以触发回调 </span>
  defaultOpenSubMenus?: string[]; 
&#125;

<span class="hljs-comment">// 确定父组件传给子组件的数据类型</span>
interface IMenuContext &#123;
  <span class="hljs-attr">index</span>: string;
  onSelect?: SelectCallback;
  mode?: MenuMode;
  defaultOpenSubMenus?: string[];  <span class="hljs-comment">// 需要将数据传给context</span>
&#125;

<span class="hljs-comment">// 创建传递给子组件的context</span>
<span class="hljs-comment">// 泛型约束，因为index是要输入的值，所以这里写一个默认初始值</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> MenuContext = createContext<IMenuContext>(&#123;<span class="hljs-attr">index</span>: <span class="hljs-string">'0'</span>&#125;)

<span class="hljs-keyword">const</span> Menu: React.FC<MenuProps> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; className, mode, style, children, defaultIndex, onSelect, defaultOpenSubMenus&#125; = props
  <span class="hljs-comment">// MenuItem处于active的状态应该是有且只有一个的，使用useState来控制其状态</span>
  <span class="hljs-keyword">const</span> [ currentActive, setActive ] = useState(defaultIndex)
  <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'menu-demo'</span>, className, &#123;
    <span class="hljs-string">'menu-vertical'</span>: mode === <span class="hljs-string">'vertical'</span>,
    <span class="hljs-string">'menu-horizontal'</span>: mode === <span class="hljs-string">'horizontal'</span>
  &#125;)

  <span class="hljs-comment">// 定义handleClick具体实现点击menuItem之后active变化</span>
  <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">(<span class="hljs-params">index: string</span>) =></span> &#123;
    setActive(index)
    <span class="hljs-comment">// onSelect是一个联合类型，可能存在，也可能不存在，对此需要做判断</span>
    <span class="hljs-keyword">if</span> (onSelect) &#123;
      onSelect(index)
    &#125;
  &#125;

  <span class="hljs-comment">// 点击子组件的时候，触发onSelect函数，更改高亮显示</span>
  <span class="hljs-keyword">const</span> passedContext: IMenuContext = &#123;
    <span class="hljs-comment">// currentActive是string | undefined类型，index是number类型，所以要做如下判断进一步明确类型</span>
    <span class="hljs-attr">index</span>: currentActive ? currentActive : <span class="hljs-string">'0'</span>,
    <span class="hljs-attr">onSelect</span>: handleClick, <span class="hljs-comment">// 回调函数，点击子组件时是否触发</span>
    <span class="hljs-attr">mode</span>: mode,
    defaultOpenSubMenus,
  &#125;

  <span class="hljs-keyword">const</span> renderChildren = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> React.Children.map(children, <span class="hljs-function">(<span class="hljs-params">child, index</span>) =></span> &#123;
      <span class="hljs-comment">// child里面包含一大堆的类型，要想获得我们想要的类型来提供智能提示，需要使用类型断言      </span>
      <span class="hljs-keyword">const</span> childElement = child <span class="hljs-keyword">as</span> React.FunctionComponentElement<MenuItemProps>
      <span class="hljs-keyword">const</span> &#123; displayName &#125; = childElement.type
      <span class="hljs-keyword">if</span> (displayName === <span class="hljs-string">'MenuItem'</span> || displayName === <span class="hljs-string">'SubMenu'</span>) &#123;
        <span class="hljs-comment">// 以element元素为样本克隆并返回新的React元素，第一个参数是克隆样本</span>
        <span class="hljs-keyword">return</span> React.cloneElement(childElement, &#123;
          <span class="hljs-attr">index</span>: index.toString()
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"Warning: Menu has a child which is not a MenuItem component"</span>)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">MenuContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;passedContext&#125;</span>></span>
        &#123;renderChildren()&#125;
      <span class="hljs-tag"></<span class="hljs-name">MenuContext.Provider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  )
&#125;

Menu.defaultProps = &#123;
  <span class="hljs-attr">defaultIndex</span>: <span class="hljs-string">'0'</span>,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'horizontal'</span>,
  <span class="hljs-attr">defaultOpenSubMenus</span>: []
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Menu
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是MenuItem子组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>
<span class="hljs-keyword">import</span> &#123; MenuContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./menu'</span>

<span class="hljs-keyword">export</span> interface MenuItemProps &#123;
  <span class="hljs-attr">index</span>: string;
  disabled?: boolean;
  className?: string;
  style?: React.CSSProperties;
&#125;

<span class="hljs-keyword">const</span> MenuItem: React.FC<MenuItemProps> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; index, disabled, className, style, children &#125; = props
  <span class="hljs-keyword">const</span> context = useContext(MenuContext)
  <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'menu-item'</span>, className, &#123;
    <span class="hljs-string">'is-disabled'</span>: disabled,
    <span class="hljs-comment">// 实现高亮的具体逻辑</span>
    <span class="hljs-string">'is-active'</span>: context.index === index
  &#125;)
  <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// disabled之后就不能使用onSelect，index因为是可选的，所以可能不存在，需要用typeof来做一个判断</span>
    <span class="hljs-keyword">if</span> (context.onSelect && !disabled && (<span class="hljs-keyword">typeof</span> index === <span class="hljs-string">'string'</span>)) &#123;
      context.onSelect(index)
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
      &#123;children&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
  )
&#125;

MenuItem.displayName = <span class="hljs-string">'MenuItem'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MenuItem
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后是SubMenu子组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useContext, FunctionComponentElement, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>
<span class="hljs-keyword">import</span> &#123; MenuContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./menu'</span>
<span class="hljs-keyword">import</span> &#123; MenuItemProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./menuItem'</span>

<span class="hljs-keyword">export</span> interface SubMenuProps &#123;
  index?: string;
  title: string;
  className?: string
&#125;

<span class="hljs-keyword">const</span> SubMenu: React.FC<SubMenuProps> = <span class="hljs-function">(<span class="hljs-params">&#123; index, title, children, className &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> context = useContext(MenuContext)
  <span class="hljs-comment">// 接下来会使用string数组的一些方法，所以先进行类型断言，将其断言为string数组类型</span>
  <span class="hljs-keyword">const</span> openedSubMenus = context.defaultOpenSubMenus <span class="hljs-keyword">as</span> <span class="hljs-built_in">Array</span><string>
  <span class="hljs-comment">// 使用include判断有没有index</span>
  <span class="hljs-keyword">const</span> isOpened = (index && context.mode === <span class="hljs-string">'vertical'</span>) ? openedSubMenus.includes(index) : <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> [ menuOpen, setOpen ] = useState(isOpened)  <span class="hljs-comment">// isOpened返回的会是true或者false，这样就是一个动态值</span>
  <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'menu-item submenu-item'</span>, className, &#123;
    <span class="hljs-string">'is-active'</span>: context.index === index
  &#125;)
  <span class="hljs-comment">// 用于实现显示或隐藏下拉菜单</span>
  <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">(<span class="hljs-params">e: React.MouseEvent</span>) =></span> &#123;
    e.preventDefault()
    setOpen(!menuOpen)
  &#125;
  <span class="hljs-keyword">let</span> timer: any
  <span class="hljs-comment">// toggle用于判断是打开还是关闭</span>
  <span class="hljs-keyword">const</span> handleMouse = <span class="hljs-function">(<span class="hljs-params">e: React.MouseEvent, toggle: boolean</span>) =></span> &#123;
    <span class="hljs-built_in">clearTimeout</span>(timer)
    e.preventDefault()
    timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
      setOpen(toggle)
    &#125;, <span class="hljs-number">300</span>)
  &#125;
  <span class="hljs-comment">// 三元表达式，纵向</span>
  <span class="hljs-keyword">const</span> clickEvents = context.mode === <span class="hljs-string">'vertical'</span> ? &#123;
    <span class="hljs-attr">onClick</span>: handleClick
  &#125; : &#123;&#125;
  <span class="hljs-keyword">const</span> hoverEvents = context.mode === <span class="hljs-string">'horizontal'</span> ? &#123;
    <span class="hljs-attr">onMouseEnter</span>: <span class="hljs-function">(<span class="hljs-params">e: React.MouseEvent</span>) =></span> &#123; handleMouse(e, <span class="hljs-literal">true</span>) &#125;,
    <span class="hljs-attr">onMouseLeave</span>: <span class="hljs-function">(<span class="hljs-params">e: React.MouseEvent</span>) =></span> &#123; handleMouse(e, <span class="hljs-literal">false</span>) &#125;,
  &#125; : &#123;&#125;

  <span class="hljs-comment">// 用于渲染下拉菜单中的内容</span>
  <span class="hljs-comment">// 返回两个值，第一个是child，第二个是index，用i表示</span>
  <span class="hljs-keyword">const</span> renderChildren = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> subMenuClasses = classNames(<span class="hljs-string">'menu-submenu'</span>, &#123;
      <span class="hljs-string">'menu-opened'</span>: menuOpen
    &#125;)
    <span class="hljs-comment">// 下面功能用于实现在subMenu里只能有MenuItem</span>
    <span class="hljs-keyword">const</span> childrenComponent = React.Children.map(children, <span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> childElement = child <span class="hljs-keyword">as</span> FunctionComponentElement<MenuItemProps>
      <span class="hljs-keyword">if</span> (childElement.type.displayName === <span class="hljs-string">'MenuItem'</span>) &#123;
        <span class="hljs-keyword">return</span> React.cloneElement(childElement, &#123;
          <span class="hljs-attr">index</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;index&#125;</span>-<span class="hljs-subst">$&#123;i&#125;</span>`</span>
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"Warning: SubMenu has a child which is not a MenuItem component"</span>)
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;subMenuClasses&#125;</span>></span>
        &#123;childrenComponent&#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
    )
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="hljs-comment">// 展开运算符，向里面添加功能，hover放在外面</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span> &#123;<span class="hljs-attr">...hoverEvents</span>&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"submenu-title"</span> &#123;<span class="hljs-attr">...clickEvents</span>&#125;></span>
        &#123;title&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      &#123;renderChildren()&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
  )
&#125;

SubMenu.displayName = <span class="hljs-string">'SubMenu'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> SubMenu
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">参考资料</h5>
<ol>
<li><a href="https://blog.csdn.net/uuihoo/article/details/79710318?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-1&spm=1001.2101.3001.4242" target="_blank" rel="nofollow noopener noreferrer">React.Children的用法</a></li>
<li><a href="https://fullstackbb.com/react/when-to-use-react-cloneelement/" target="_blank" rel="nofollow noopener noreferrer">React.cloneElement 的使用</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            