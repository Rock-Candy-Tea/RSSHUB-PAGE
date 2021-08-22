
---
title: 'React中的JSX原理渐析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61db42d3671e45329fa4d3afafb938cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 04:29:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61db42d3671e45329fa4d3afafb938cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><code>JSX</code></h1>
<p>相信使用<code>react</code>的大家对于<code>jsx</code>已经游刃有余了，可是你真的了解<code>jsx</code>的原理吗？</p>
<p>让我们由浅入深，来一层一层揭开<code>jsx</code>的真实面目。</p>
<h2 data-id="heading-1"><code>React.createElement</code></h2>
<p>在<code>react</code>官方中讲到，关于<code>jsx</code>语法最终会被<code>babel</code>编译成为<code>React.createElement()</code>方法。</p>
<p>我们来看看这段<code>jsx</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"wang.haoyu"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过<code>babel</code>编译后它变成这样的代码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">React.createElement(<span class="hljs-string">"div"</span>, &#123;
    <span class="hljs-attr">className</span>:<span class="hljs-string">'wang.haoyu'</span>
&#125;, <span class="hljs-string">"hello"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当<code>jsx</code>中存在多个节点元素时，比如:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>hello<span class="hljs-tag"><<span class="hljs-name">span</span>></span>world<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它会将多个节点的<code>jsx</code>中<code>children</code>属性变成多个参数进行传递下去:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">React.createElement(<span class="hljs-string">"div"</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">"hello"</span>, React.createElement(<span class="hljs-string">"span"</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">"world"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，外层的<code>div</code>元素包裹的<code>children</code>元素依次在<code>React.createElement</code>中铺平排列进去，并不是树型结构排列。</p>
<blockquote>
<p>需要注意的是，旧的<code>react</code>版本中，只要我们使用<code>jsx</code>就需要引入react这个包。而且引入的变量必须大写<code>React</code>，因为上边我们看到<code>babel</code>编译完<code>jsx</code>之后会寻找<code>React</code>变量。</p>
</blockquote>
<blockquote>
<p>新版本中，不再需要引入<code>React</code>这个变量了。有兴趣的同学可以去看看打包后的<code>react</code>代码,内部会处理成为<code>Object(s.jsx)("div",&#123; children: "Hello" &#125;)</code>，而老的版本是<code>React.createElement('div',null,'Hello')</code>。</p>
</blockquote>
<blockquote>
<p>这两种方式效果和原理是一模一样的，只是新版额外引入包去处理了引入。所以不需要单独进行引入<code>React</code>。</p>
</blockquote>
<h2 data-id="heading-2"><code>React</code>元素</h2>
<p><code>React</code>之中元素是构建<code>React</code>的最小单位,其实也就是虚拟Dom对象。</p>
<p>本质上<code>jsx</code>执行时就是在执行函数调用，是一种工厂模式通过<code>React.createElement</code>返回一个元素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="hljs-built_in">console</span>.log(element,<span class="hljs-string">'element'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61db42d3671e45329fa4d3afafb938cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先忽略掉一些<code>ref/key</code>之类的属性，这个时候来看我们发现它其实就是一个<code>js</code>对象，记录了<code>type</code>表示元素类型。<code>props</code>表示元素的接受的<code>prop</code>,注意这里会将<code>jsx</code>内部标签内容插入到<code>props</code>的<code>children</code>属性中。</p>
<blockquote>
<p>需要注意的是这里的<code>children</code>属性，如果内部标签元素存在多个子元素时候。<code>children</code>会是一个数组。因为这里仅仅只有文本节点，所以只有一个<code>Hello</code>。</p>
</blockquote>
<p>在我们平常使用<code>react</code>项目的时候，<code>index.tsx</code>中总是会存在这样一段代码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合上边我们所讲的<code>React.createElement</code>，我们不难猜出<code>ReactDOM.render</code>这个方法它的作用其实就是<strong>按照<code>React.createElement</code>生成的虚拟DOM节点对象，生成真实DOM插入到对应节点中去</strong>，这就是简单的渲染过程。</p>
<h3 data-id="heading-3">元素的更新</h3>
<p><strong><code>react</code>中元素本身是不可变的。</strong></p>
<p>比如:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span> ></span>Hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(element,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f942fbc373044bceb1be8dd30458fad1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们想将它的内容改成<code>world</code>时，如果直接通过</p>
<pre><code class="copyable">element.props.children = 'world'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样是不可以的，<code>react</code>会提示:</p>
<pre><code class="copyable">Uncaught TypeError: Cannot assign to read only property 'children' of object '#<Object>'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无法给一个只读属性<code>children</code>进行赋值，修改其他属性比如<code>type</code>之类同理也是不可以的。</p>
<p>当我们通过这种方式给<code>react</code>元素增加属性时，也是增加的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Cannot add property xxx, object is not extensible
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>not extensible</code>是<code>react</code>17之后才进行增加的。通过<code>Object.freeze()</code>将对象进行处理元素。</p>
</blockquote>
<blockquote>
<p>需要注意<code>Object.freeze()</code>是一层浅冻结，在<code>react</code>内部进行了递归<code>Object.freeze()</code>。</p>
</blockquote>
<p>所以在<code>react</code>中元素本身是不可变的，当元素被创建后是无法修改的。只能通过重新创建一个新的元素来更新旧的元素。</p>
<p>你可以这样理解，在<code>react</code>中每一个元素类似于动画中的每一帧，都是不可以变得。</p>
<blockquote>
<p>当然在<code>react</code>更新中仅仅会更新需要更新的内容，内部会和Vue相同的方式去进行diff算法，高效更新变化的元素而不是更新重新渲染所有元素。</p>
</blockquote>
<h2 data-id="heading-4"><code>jsx</code>原理分析</h2>
<blockquote>
<p>需要注意我们这里使用旧的<code>React.createElement</code>方法，如果是<code>^17</code>版本下，需要在环境变量中添加<code>DISABLE_NEW_JSX_TRANSFORM=true</code>。</p>
</blockquote>
<p>上边我们已经分析过<code>React.createElement</code>这个方法的返回值，接下来我们就尝试自己来实现<code>jsx</code>的渲染。</p>
<p>先来看看原本React中<code>createElement</code>方法的返回值:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-keyword">const</span> element = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"header"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">red</span>' &#125;&#125;></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">span</span>></span>world
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(element, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>), <span class="hljs-string">'element'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34edc972edad43b182fe06ef5a496564~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们就根据结果来推写法，实现一个简单的<code>createElement</code>方法</p>
<h3 data-id="heading-5">实现<code>React.crateElement</code>方法-原生<code>DOM</code>元素的渲染</h3>
<ul>
<li>实现<code>utils/react.js</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">// 这里之所以额外书写一个 wrapToDom元素 是为了方便对比 react源码中没有这段方法是特殊处理的</span>
<span class="hljs-comment">// 我们为了方便 将普通类型 也统一处理成为Object</span>

<span class="hljs-keyword">const</span> React = &#123;
  <span class="hljs-attr">createElement</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, config, children</span>) </span>&#123;
    <span class="hljs-keyword">const</span> props = &#123;
      ...config,
    &#125;;
    <span class="hljs-comment">// 上边讲到babel编译jsx后</span>
    <span class="hljs-comment">// 如果参数大于3个 那么就有多个children props.children是一个数组</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length > <span class="hljs-number">3</span>) &#123;
      props.children = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">2</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      props.children = children;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      type,
      props,
    &#125;;
  &#125;,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步我们已经实现了基础的<code>React.createElement</code>方法。</p>
<ul>
<li><code>index.tsx</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils/react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-comment">// babel编译后的代码会引入 React.createElement</span>
<span class="hljs-comment">// 此时的React指向的是我们自己写的React</span>
<span class="hljs-keyword">const</span> element = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"header"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">red</span>' &#125;&#125;></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">span</span>></span>world
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);

ReactDOM.render(element, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">实现<code>ReactDOM.render</code>方法-将<code>react</code>中源生DOM元素变成真实元素插入页面</h3>
<ul>
<li>接着咱们先来实现一个对于<code>children</code>类型的判断方法</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// utils.js </span>
<span class="hljs-comment">// 常亮 判断文本类型</span>
<span class="hljs-keyword">const</span> REACT_TEXT = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'REACT_TEXT'</span>)

<span class="hljs-comment">// 无论以前是什么元素，都转成VDOM的对象形式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformVom</span>(<span class="hljs-params">element</span>) </span>&#123;
    <span class="hljs-comment">// 额外处理文本节点 将文本节点输出和其他节点一样的Object类型</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> element === <span class="hljs-string">'string'</span> || <span class="hljs-keyword">typeof</span> element === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">type</span>: REACT_TEXT, <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">content</span>: element &#125; &#125;
    &#125;
    <span class="hljs-keyword">return</span> element
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接下来我们改造一下我们之前写好的<code>React.createElement</code>方法</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; transformVNode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils'</span>;

<span class="hljs-keyword">const</span> React = &#123;
  <span class="hljs-attr">createElement</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, config, children</span>) </span>&#123;
    <span class="hljs-keyword">const</span> props = &#123;
      ...config,
    &#125;;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length > <span class="hljs-number">3</span>) &#123;
      props.children = <span class="hljs-built_in">Array</span>.prototype.slice
        .call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">2</span>)
        .map(transformVNode);
    &#125; <span class="hljs-keyword">else</span> &#123;
      props.children = transformVNode(children);
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      type,
      props,
    &#125;;
  &#125;,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接下来我们已经拥有了对应的<code>VDom</code>对象，就可以开始实现<code>React.render</code>方法。</li>
</ul>
<blockquote>
<p><code>React.render</code>核心思想就是将我们的<code>Vdom</code>对象编程浏览器可以识别的标签节点挂载在对应<code>元素上</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 把虚拟DOM变成真实DOM插入
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>vDom 虚拟DOM
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;HTMLElement&#125;</span> </span>el 元素
 */</span>

<span class="hljs-keyword">import</span> &#123; REACT_TEXT &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./constant'</span>;

<span class="hljs-comment">// 真正渲染方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">vDom, el</span>) </span>&#123;
  <span class="hljs-keyword">const</span> newDom = createDom(vDom);
  el.appendChild(newDom);
&#125;

<span class="hljs-comment">// 先不考虑自定义组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDom</span>(<span class="hljs-params">vDom</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; type, props &#125; = vDom;
  <span class="hljs-keyword">let</span> dom;
  <span class="hljs-comment">// 文本节点</span>
  <span class="hljs-keyword">if</span> (type === REACT_TEXT) &#123;
    dom = <span class="hljs-built_in">document</span>.createTextNode(props.content);
  &#125; <span class="hljs-keyword">else</span> &#123;
    dom = <span class="hljs-built_in">document</span>.createElement(type);
  &#125;
  <span class="hljs-comment">// 更新属性</span>
  <span class="hljs-keyword">if</span> (props) &#123;
    <span class="hljs-comment">// 更新跟节点Dom属性</span>
    updateProps(dom, &#123;&#125;, props);
    <span class="hljs-comment">// 处理children 考虑undefined/null 不做任何处理</span>
    <span class="hljs-comment">// 考虑 children是一个数组 那么就表示他拥有多个儿子</span>
    <span class="hljs-comment">// 考虑children是一个Object 那么他就只有一个儿子节点</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> props.children === <span class="hljs-string">'object'</span> && props.children.type) &#123;
      <span class="hljs-comment">// 单个元素</span>
      render(props.children, dom);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(props.children)) &#123;
      <span class="hljs-comment">// 多个元素</span>
      reconcileRender(props.children, dom);
    &#125;
  &#125;
  <span class="hljs-comment">// 记录挂载节点</span>
  vDom.__dom = dom;
  <span class="hljs-keyword">return</span> dom;
&#125;

<span class="hljs-comment">// 挂载多个dom元素 React.createElement先不考虑递归</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileRender</span>(<span class="hljs-params">vLists, parentDom</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> node <span class="hljs-keyword">of</span> vLists) &#123;
    render(node, parentDom);
  &#125;
&#125;

<span class="hljs-comment">/**
 * 把虚拟DOM变成真实DOM插入
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;HTMLElement&#125;</span> </span>dom 元素
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>oldProps 元素本身的props 用于更新这里暂时用不到
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>newProps 元素新的props
 */</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateProps</span>(<span class="hljs-params">dom, oldProps, newProps</span>) </span>&#123;
  <span class="hljs-comment">// 合并props 暂时没有老的 仅处理新的</span>
  <span class="hljs-built_in">Object</span>.keys(newProps).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'children'</span>) &#123;
      <span class="hljs-comment">// 单独处理children</span>
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'style'</span>) &#123;
      addStyleToElement(dom, newProps[key]);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'content'</span>) &#123;
      <span class="hljs-comment">// 文本不做任何操作</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      dom[key] = newProps[key];
    &#125;
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addStyleToElement</span>(<span class="hljs-params">dom, styleObject</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.keys(styleObject).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> value = styleObject[key];
    dom.style[key] = value;
  &#125;);
&#125;

<span class="hljs-keyword">const</span> ReactDOM = &#123;
  render,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ReactDOM;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这里的的核心思想就是通过<code>render</code>方法将虚拟DOM根据对应的属性转化成为真实DOM节点进行递归挂载，最终通过<code>appendChild</code>渲染到页面上。</p>
<h2 data-id="heading-7">写在最后</h2>
<p>目前来说，我们已经基本实现了<code>React.createElement</code>和<code>ReactDom.render</code>这两个方法。
只不过目前来说仅仅针对于源生<code>DOM</code>节点进行了处理。</p>
<p>在<code>React</code>中我们知道会有各种各样我们自己定义的组件，接下来我们会一步一步去看看这些组件的渲染流程。</p></div>  
</div>
            