
---
title: 'React源码解析-TinyReact分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=657'
author: 掘金
comments: false
date: Tue, 25 May 2021 04:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=657'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>基于TinyReact, 分析React主要原理，React框架由于兼容过多业务，代码量庞大读起来比较吃力。本文选取TinyReact其中包含了React框架的主要实现思想。</p>
<h4 data-id="heading-0">JSX是什么</h4>
<p>弄清JSX对理解虚拟DOM有很重要的作用JSX只是看起来像是HTML，但它却是JavaScript,在React代码执行之前，Babel会将JSX编译为React API。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 编译前</span>
<div className=<span class="hljs-string">"content"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Hello React<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>React is great<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>
<span class="hljs-comment">// 编译后</span>
React.createElement(
    <span class="hljs-string">'div'</span>,
    &#123;
        <span class="hljs-attr">className</span>: <span class="hljs-string">'content'</span>
    &#125;,
    React.createElement(<span class="hljs-string">'h3'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'Hello World'</span>),
    React.createElement(<span class="hljs-string">'p'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'React is greate'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React.createElement代表一个节点元素，第一个参数是节点的名称，第二个是节点的属性，后面的参数都是子节点。我们可以自己在babeljs.is网站试验。React.createElement就是用来创建虚拟DOM的，返回的就是一个虚拟DOM对象。React再将虚拟DOM转换为真实DOM显示到页面中。</p>
<p>jsx在运行时会被Babel转换为React.createElement对象，React.createElement会被React转换成虚拟DOM对象，虚拟DOM对象会被React转换成真实DOM对象。</p>
<p>JSX语法的出现就是为了让React开发人员编写用户界面代码更加轻松。</p>
<h4 data-id="heading-1">什么是虚拟DOM</h4>
<p>在React中，每个DOM对象都有一个对应的虚拟DOM对象，他是DOM对象的JavaScript表现形式，其实就是使用JavaScript对象来描述DOM对象信息，比如DOM对象的类型是什么，它身上有哪些属性，它拥有哪些子元素。</p>
<p>可以把虚拟DOM对象理解为DOM对象的一个副本，不过虚拟DOM不能直接显示在屏幕上。虚拟DOM就是为了解决React操作DOM的性能问题。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 编译前</span>
<div className=<span class="hljs-string">"content"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Hello React<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>React is great<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>
<span class="hljs-comment">// 编译后</span>
&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"div"</span>,
    <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">className</span>: <span class="hljs-string">"content"</span>&#125;,
    <span class="hljs-attr">children</span>: [
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">"h3"</span>,
            <span class="hljs-attr">props</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">children</span>: [
                &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
                    <span class="hljs-attr">props</span>: &#123;
                        <span class="hljs-attr">textContent</span>: <span class="hljs-string">"Hello React"</span>
                    &#125;
                &#125;
            ]
        &#125;,
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">"p"</span>,
            <span class="hljs-attr">props</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">children</span>: [
                &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
                    <span class="hljs-attr">props</span>: &#123;
                        <span class="hljs-attr">textContent</span>: <span class="hljs-string">"React is greate"</span>
                    &#125;
                &#125;
            ]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React采用最小化的DOM操作来提升DOM操作的优势，只更新需要更新的，在React第一次创建DOM对象的时候会为每一个DOM对象创建虚拟的DOM对象，在DOM对象发生更新之前React会更新所有的虚拟DOM对象, 然后将更新前的虚拟DOM和更新后的虚拟DOM进行对比，找到变更的DOM对象，只将发生变化的DOM更新到页面中从而提升了js操作DOM的性能。</p>
<p>虽然在操作真实DOM之前进行的虚拟DOM更新和对比的操作，但是由于JS操作自有对象效率是很高的，成本几乎可以忽略不计的。</p>
<p>在React代码执行前，JSX会被Babel转换为React.createElement方法的调用，在调用createElement方法时会传入元素的类型，元素的属性，以及元素的子元素，createElement方法的返回值为构建好的虚拟DOM对象。这里我们自己来实现一个createElement方法。</p>
<p>createElement方法接收type, props, childrens三个参数。分别表示标签类型，标签属性和标签子元素。在这个方法中要返回一个虚拟DOM对象，在这个对象中有个type属性其实就是参数传入的值，接着是props和children。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        type,
        props,
        children
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里使用TinyReact来分析React代码。首先要配置babel将jsx编译为Tiny的createElement方法，这样方便我们调试</p>
<p>.babelrc</p>
<pre><code class="hljs language-JSON copyable" lang="JSON">&#123;
    <span class="hljs-attr">"presets"</span>: [
        <span class="hljs-string">"@babel/preset-env"</span>,
        [
            <span class="hljs-string">"@babel/preset-react"</span>,
            &#123;
                <span class="hljs-attr">"pragma"</span>: <span class="hljs-string">"TinyReact.createElement"</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>脚手架仓库自取地址 <a href="https://github.com/xiaoyindong/tinyReact" target="_blank" rel="nofollow noopener noreferrer">链接</a></p>
<p>src/index.js</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> TinyReact <span class="hljs-keyword">from</span> <span class="hljs-string">"./TinyReact"</span>

<span class="hljs-keyword">const</span> virtualDOM = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>你好 我是虚拟DOM<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)

<span class="hljs-built_in">console</span>.log(virtualDOM);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台打印结果。</p>
<pre><code class="hljs language-JSON copyable" lang="JSON">&#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"div"</span>,
    <span class="hljs-attr">"props"</span>: &#123;
        <span class="hljs-attr">"className"</span>: <span class="hljs-string">"container"</span>
    &#125;,
    <span class="hljs-attr">"children"</span>: [
        &#123;
            <span class="hljs-attr">"type"</span>:<span class="hljs-string">"h1"</span>,
             <span class="hljs-attr">"props"</span>:<span class="hljs-literal">null</span>,
            <span class="hljs-attr">"children"</span>: [
                <span class="hljs-string">"你好 我是虚拟DOM"</span>
            ]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们就打印出来一个简单的虚拟DOM，不过也有一个问题，这里的文本节点"你好 我是虚拟DOM"直接以字符串添加到了children数组中，这是不对的，正确的做法应该是文本节点也应该是一个虚拟DOM对象。</p>
<p>我们只需要循环children数组，判断如果不是一个对象就认为他是一个文本节点，我们将它替换成一个对象，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
    <span class="hljs-comment">// 遍历children对象</span>
    <span class="hljs-keyword">const</span> childElements = [].concat(...children).map(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(child <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) &#123;
        <span class="hljs-keyword">return</span> child; <span class="hljs-comment">// 是对象直接返回</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不是对象 调用createElement方法生成一个对象</span>
        <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'text'</span>, &#123; <span class="hljs-attr">textContent</span>: child &#125;);
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
    type,
    props,
    <span class="hljs-attr">children</span>: childElements
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文本节点变成了一个对象。</p>
<pre><code class="hljs language-JSON copyable" lang="JSON">&#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"div"</span>,
    <span class="hljs-attr">"props"</span>: &#123;
        <span class="hljs-attr">"className"</span>: <span class="hljs-string">"container"</span>
    &#125;,
    <span class="hljs-attr">"children"</span>: [
        &#123;
            <span class="hljs-attr">"type"</span>:<span class="hljs-string">"h1"</span>,
             <span class="hljs-attr">"props"</span>:<span class="hljs-literal">null</span>,
            <span class="hljs-attr">"children"</span>: [
                &#123;
                    <span class="hljs-attr">"type"</span>:<span class="hljs-string">"text"</span>,
                    <span class="hljs-attr">"props"</span>: &#123;
                        <span class="hljs-attr">"textContent"</span>: <span class="hljs-string">"你好 我是虚拟DOM"</span>
                    &#125;,
                    <span class="hljs-attr">"children"</span>: []
                &#125;
            ]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们都知道在组件模板中如果是布尔值或者null值，节点是不显示的。我们这里需要处理一下。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div className=<span class="hljs-string">"container"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>你好 我是虚拟DOM<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#123;
        <span class="hljs-number">1</span> === <span class="hljs-number">2</span> && <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>布尔值节点<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
  <span class="hljs-comment">// 遍历children对象</span>
  <span class="hljs-keyword">const</span> childElements = [].concat(...children).reduce(<span class="hljs-function">(<span class="hljs-params">result, child</span>) =></span> &#123;
    <span class="hljs-comment">// 判断child不能是布尔也不能是null</span>
    <span class="hljs-comment">// 因为使用reduce，所以result是前一次循环的返回值，最终返回result就可以</span>
    <span class="hljs-keyword">if</span> (child !== <span class="hljs-literal">false</span> && child !== <span class="hljs-literal">true</span> && child !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">if</span> (child <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) &#123;
        result.push(child); <span class="hljs-comment">// 是对象直接返回</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不是对象 调用createElement方法生成一个对象</span>
        result.push(createElement(<span class="hljs-string">'text'</span>, &#123;
          <span class="hljs-attr">textContent</span>: child
        &#125;));
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> result;
  &#125;, [])
  <span class="hljs-keyword">return</span> &#123;
    type,
    props,
    <span class="hljs-attr">children</span>: childElements
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还需要将children放入到props中，只需要使用Object.assign将props和children合并返回就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> &#123;
    type,
    <span class="hljs-attr">props</span>: <span class="hljs-built_in">Object</span>.assign(&#123; <span class="hljs-attr">children</span>: childElements&#125;, props),
    <span class="hljs-attr">children</span>: childElements
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">将虚拟DOM转换为真实DOM</h4>
<p>我们要定义一个render方法,。</p>
<p>src/tinyReact/render.js</p>
<p>这个方法要接收三个参数，第一个参数是虚拟DOM，第二个参数是要渲染到的页面元素，第三个参数是旧的虚拟DOM用于进行对比。render方法的主要作用就是将虚拟DOM转换为真实DOM并且渲染到页面中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> diff <span class="hljs-keyword">from</span> <span class="hljs-string">'./diff'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">virtualDOM, container, oldDOM</span>) </span>&#123;
    diff(virtualDOM, container, oldDOM);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要在diff方法中进行一次处理，如果旧的虚拟DOM存在就进行对比，如果不存在就直接将当前的虚拟DOM放置在container中。</p>
<p>src/tinyReact/diff.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mountElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./mountElement'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff</span> (<span class="hljs-params">virtualDOM, container, oldDOM</span>) </span>&#123;
    <span class="hljs-comment">// 判断oldDOM是否在巡</span>
    <span class="hljs-keyword">if</span> (!oldDOM) &#123;
        <span class="hljs-keyword">return</span> mountElement(virtualDOM, container);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要判断需要转换的虚拟DOM是组件还是普通的标签。需要分别进行处理, 这里我们先默认只有原生jsx标签，写死调用mountNativeElement方法。</p>
<p>src/tinyReact/mountElement.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mountNativeElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./mountNativeElement'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountElement</span>(<span class="hljs-params">virtualDOM, container</span>) </span>&#123;
    <span class="hljs-comment">// 处理原生的jsx和组件的jsx</span>
    mountNativeElement(virtualDOM, container);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mountNativeElement文件用于将原生的虚拟DOM转换成真实的DOM，这里调用createDOMElement方法来实现。</p>
<p>src/tinyReact/mountNativeElement.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> createDOMElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./createDOMElement'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountNativeElement</span>(<span class="hljs-params">virtualDOM, container</span>) </span>&#123;
    <span class="hljs-comment">// 将虚拟dom转换成真实的对象</span>
    <span class="hljs-keyword">let</span> newElement = createDOMElement(virtualDOM);
    <span class="hljs-comment">// 将转换之后的DOM对象放在页面中</span>
    container.appendChild(newElement);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建真实DOM的方法单独定义文件，方便复用。需要判断如果是元素节点就创建相应的元素，如果是文本节点就创建对应的文本。然后通过递归的方式创建子节点。最后将我们创建的这个节点放在指定的容器container中就可以了。</p>
<p>src/tinyReact/createDOMElement.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mountElement <span class="hljs-keyword">from</span> <span class="hljs-string">"./mountElement"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDOMElement</span>(<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">let</span> newElement = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
        <span class="hljs-comment">// 文本节点 使用createTextNode创建</span>
        newElement = <span class="hljs-built_in">document</span>.createTextNode(virtualDOM.props.textContent);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 元素节点 使用 createElement 创建</span>
        newElement = <span class="hljs-built_in">document</span>.createElement(virtualDOM.type);
    &#125;
    <span class="hljs-comment">// 递归创建子节点</span>
    virtualDOM.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
        mountElement(child, newElement);
    &#125;)
    <span class="hljs-keyword">return</span> newElement;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">为真实的DOM对象添加属性</h4>
<p>我们知道属性是存储在虚拟DOM的props中的，我们只需要在创建元素的时候循环这个属性，将这些属性放在真实的元素中就可以了。</p>
<p>在添加属性的时候需要考虑不同的情况，比如说事件和静态属性都是不同的，而且添加属性的方法也是不同的，布尔属性和值属性的设置方式有所不同。还需要判断属性是不是children，因为children并不是属性，是我们自己定义的子元素，属性如果是className还需要转换成class进行添加。</p>
<p>src/tinyReact/createDOMElement.js</p>
<p>我们单独定一个方法来为元素添加属性，在创建元素之后调用这个方法，这里叫做updateNodeElement</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mountElement <span class="hljs-keyword">from</span> <span class="hljs-string">"./mountElement"</span>;
<span class="hljs-keyword">import</span> updateNodeElement <span class="hljs-keyword">from</span> <span class="hljs-string">"./updateNodeElement"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDOMElement</span>(<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">let</span> newElement = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
        <span class="hljs-comment">// 文本节点 使用createTextNode创建</span>
        newElement = <span class="hljs-built_in">document</span>.createTextNode(virtualDOM.props.textContent);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 元素节点 使用 createElement 创建</span>
        newElement = <span class="hljs-built_in">document</span>.createElement(virtualDOM.type);
        <span class="hljs-comment">// 调用添加属性的方法</span>
        updateNodeElement(newElement, virtualDOM)
    &#125;
    <span class="hljs-comment">// 递归创建子节点</span>
    virtualDOM.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
        mountElement(child, newElement);
    &#125;)
    <span class="hljs-keyword">return</span> newElement;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先需要获取节点对象的属性列表，使用Object.keys来获得属性名，然后使用forEach来遍历。</p>
<p>src/tinyReact/updateNodeElement.js</p>
<p>如果属性名以on开头我们就认为他是一个事件, 然后我们截取出事件名称也就是去掉首部的on并且将字符串小写，使用addEventListener来绑定事件。</p>
<p>如果属性名是value或者checked是不能使用setAttribute来设置的，直接属性名等于属性值即可。</p>
<p>最后判断属性名如果是className就转换成class，如果不为children则其它属性全部可以使用setAttribute来设置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateNodeElement</span>(<span class="hljs-params">newElement, virtualDOM</span>) </span>&#123;
    <span class="hljs-comment">// 获取节点对应的属性对象</span>
    <span class="hljs-keyword">const</span> newProps = virtualDOM.props;
    <span class="hljs-built_in">Object</span>.keys(newProps).forEach(<span class="hljs-function"><span class="hljs-params">propName</span> =></span> &#123;
        <span class="hljs-keyword">const</span> newPropsValue = newProps[propName];
        <span class="hljs-comment">// 判断是否是事件属性</span>
        <span class="hljs-keyword">if</span> (propName.startsWith(<span class="hljs-string">'on'</span>)) &#123;
            <span class="hljs-comment">// 截取出事件名称</span>
            <span class="hljs-keyword">const</span> eventName = propName.toLowerCase().slice(<span class="hljs-number">2</span>);
            <span class="hljs-comment">// 为元素添加事件</span>
            newElement.addEventListener(eventName, newPropsValue);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propName === <span class="hljs-string">'value'</span> || propName === <span class="hljs-string">'checked'</span>) &#123;
            <span class="hljs-comment">// 如果属性名是value或者checked不能使用setAttribute来设置，直接以属性方式设置即可</span>
            newElement[propName] = newPropsValue;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propName !== <span class="hljs-string">'children'</span>) &#123;
            <span class="hljs-comment">// 排除children</span>
            <span class="hljs-keyword">if</span> (propName === <span class="hljs-string">'className'</span>) &#123;
                newElement.setAttribute(<span class="hljs-string">'class'</span>, newPropsValue)
            &#125; <span class="hljs-keyword">else</span> &#123;
                newElement.setAttribute(propName, newPropsValue)
            &#125;
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">组件渲染 - 区分函数组件还是类组件</h4>
<p>在渲染组件之前首先我们要明确地是，组件的虚拟DOM类型值为函数，函数组件和类组件都是如此。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> Head = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span>></span>head<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件的虚拟DOM</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;,
    <span class="hljs-attr">props</span>: &#123;&#125;,
    <span class="hljs-attr">children</span>: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在渲染组件时，要先将Component与Native Element区分开，如果是Native Element可以直接进行渲染，这个我们之前已经处理过了，如果是组件需要特别处理。</p>
<p>我们可以在入口文件src/index.js中渲染一个组件。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> TinyReact <span class="hljs-keyword">from</span> <span class="hljs-string">"./TinyReact"</span>

<span class="hljs-keyword">const</span> root = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Head</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

TinyReact.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Head</span> /></span></span>, root);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就需要在mountElement方法中区分原生标签和组件。</p>
<p>src/tinyReact/isFunction.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isFunction</span>(<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">return</span> virtualDOM && <span class="hljs-keyword">typeof</span> virtualDOM.type === <span class="hljs-string">'function'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在mountComponent方法中处理组件。首先我们要考虑这个组件是类组件还是函数组件，因为他们的处理方式是不同的，可以使用原型上是否存在render函数。我们可以借助isFunctionComponent函数来判断</p>
<p>src/tinyReact/mountComponent.js</p>
<p>如果type存在，并且对象是一个函数，并且对象上不存在render方法，那就是一个函数组件
src/tinyReact/isFunctionComponent.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> isFunctionComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./isFunctionComponent'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">virtualDOM, container</span>) </span>&#123;
    <span class="hljs-comment">// 判断组件是类组件还是函数组件</span>
    <span class="hljs-keyword">if</span> (isFunctionComponent(virtualDOM)) &#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/tinyReact/isFunctionComponent.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> isFunction <span class="hljs-keyword">from</span> <span class="hljs-string">"./isFunction"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isFunctionComponent</span>(<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">const</span> type = virtualDOM.type;
    <span class="hljs-keyword">return</span> type && isFunction(virtualDOM) && !(type.prototype && type.prototype.render)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">处理函数组件</h4>
<p>我们先来处理函数组件, 函数组件其实很简单，只需要调用type函数就可以了，就可以获取返回的虚拟dom。获取之后我们需要判断新获取的虚拟DOM是否是一个组件，如果是继续调用mountComponent，如果不是则为原生DOM元素直接调用mountNativeElement方法将虚拟DOM渲染到页面中。</p>
<p>src/tinyReact/mountComponent.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> isFunction <span class="hljs-keyword">from</span> <span class="hljs-string">'./isFunction'</span>;
<span class="hljs-keyword">import</span> isFunctionComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./isFunctionComponent'</span>;
<span class="hljs-keyword">import</span> mountNativeElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./mountNativeElement'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">virtualDOM, container</span>) </span>&#123;
    <span class="hljs-comment">//存储得到的虚拟DOM</span>
    <span class="hljs-keyword">let</span> nextVirtualDOM = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 判断组件是类组件还是函数组件</span>
    <span class="hljs-keyword">if</span> (isFunctionComponent(virtualDOM)) &#123;
        <span class="hljs-comment">// 处理函数组件</span>
        nextVirtualDOM = buildFunctionComponent(virtualDOM);
    &#125;
    <span class="hljs-comment">// 判断是否仍是一个函数组件</span>
    <span class="hljs-keyword">if</span> (isFunction(nextVirtualDOM)) &#123;
        mountComponent(nextVirtualDOM, container);
    &#125;
    <span class="hljs-comment">// 渲染nextVirtualDOM</span>
    mountNativeElement(nextVirtualDOM, container);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildFunctionComponent</span> (<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">return</span> virtualDOM.type();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">函数组件的props属性</h4>
<p>我们可以在Head组件渲染的时候传入一个title参数。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> root = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Head</span> (<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    &#123;props.title&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

TinyReact.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Head</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span> /></span></span>, root);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据以往的了解我们知道，在组件的身上是有一个props参数的，在组件的内部是可以在props上面拿到这个值的，当我们去渲染函数组件的时候我们可以在buildFunctionComponent这个方法，在这个方法中调用了组件函数，我们可以在调用的时候将props传入进去。这里我们要兼容一下空对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildFunctionComponent</span> (<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-keyword">return</span> virtualDOM.type(virtualDOM.props || &#123;&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">类组件渲染</h4>
<p>这里我们先创建一个类组件, 在React中类组件是需要继承Component类的。我们可以都创建一下。</p>
<p>src/index.js</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Alert</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">TinyReact</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Hello Class Component<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;

TinyReact.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Alert</span> /></span></span>, root);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/tinyReact/Component.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>准备工作完成之后我们需要去渲染类组件，同样是在mountComponent.js中来实现，之前我们已经在这里实现了渲染函数组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isFunctionComponent(virtualDOM)) &#123;
    <span class="hljs-comment">// 处理函数组件</span>
    nextVirtualDOM = buildFunctionComponent(virtualDOM);
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 处理类组件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们创建一个buildClassComponent方法来处理类组件, 这个函数接收虚拟DOM，在这个函数中我们需要得到组件的实例对象，因为只有得到了实例对象我们才能获得render方法，通过调用render方法才能获得组件输出的虚拟DOM对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 处理类组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildClassComponent</span> (<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-comment">// 获取实例对象</span>
    <span class="hljs-keyword">const</span> component = <span class="hljs-keyword">new</span> virtualDOM.type();
    <span class="hljs-comment">// 获得虚拟DOM对象</span>
    <span class="hljs-keyword">const</span> nextVirtualDOM = component.render();
    <span class="hljs-keyword">return</span> nextVirtualDOM;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剩下的逻辑和函数组件相同，判断返回的DOM是否是组件DOM或者原生DOM。如果是组件DOM就继续递归传递给mountComponent，如果是原生DOM就调用mountNativeElement进行渲染。</p>
<h4 data-id="heading-8">类组件props处理</h4>
<p>我们知道在类组件中可以通过this.props拿到传递的参数，我们的类组件是集成了Component父类，我们可以在子类中调用父类的方法，让父类中的props等于传入的props，这样子类就可以拿到props了。</p>
<p>我们在子类中添加一个构造函数，接收props，然后调用super父类，将props传入给父类。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Alert</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">TinyReact</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.props.name&#125; &#123;this.props.age&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父类的构造函数中拿到props然后赋值给props属性。这样子类继承了父类，子类也就有这个属性了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.props = props;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们在实例化组件的时候将props传递进来就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildClassComponent</span> (<span class="hljs-params">virtualDOM</span>) </span>&#123;
    <span class="hljs-comment">// 获取实例对象</span>
    <span class="hljs-keyword">const</span> component = <span class="hljs-keyword">new</span> virtualDOM.type(virtualDOM.props || &#123;&#125;);
    <span class="hljs-comment">// 获得虚拟DOM对象</span>
    <span class="hljs-keyword">const</span> nextVirtualDOM = component.render();
    <span class="hljs-keyword">return</span> nextVirtualDOM;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">更新DOM元素 - 文本节点</h4>
<p>要实现更新页面中的DOM元素，就要用到虚拟DOM对比，要拿新的虚拟DOM和老的虚拟DOM进行对比，找出差异部分，将差异部分更新到页面中，实现DOM的最小化更新。</p>
<p>在进行虚拟DOM比对时，需要用到更新后的虚拟DOM和更新前的虚拟DOM，更新后的虚拟DOM目前我们可以通过render方法进行传递，现在的问题是更新前的虚拟DOM要如何获取。</p>
<p>对于更新前的虚拟DOM，对应的其实就是已经在页面中显示的真实DOM，既然这样，那么我们再创建真实DOM对象时，就可以将虚拟DOM添加到真实DOM对象的属性中，在进行虚拟DOM对比之前，就可以通过真实DOM对象获取其对应的虚拟DOM对象，其实就是通弄过render方法的第三个参数获取的，container.firstChild.</p>
<p>首先我们要为真实DOM添加对应的虚拟DOM对象。我们可以在createDOMElement方法中找到我们创建的真实DOM对象，然后给他添加一个_virtualDOM属性存储对应的虚拟DOM。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 添加虚拟DOM属性</span>
newElement._virtualDOM = virtualDOM;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在render方法中我们最初定义的时候实际上传递了三个参数，当前的虚拟DOM对象，要渲染到的容器对象以及老的虚拟DOM对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">virtualDOM, container, oldDOM</span>) </span>&#123;
    diff(virtualDOM, container, oldDOM);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上第三个参数并不是render方法传递进来的，而是从页面获取到的，应该是container.firstChild对象。也就是当前容器内渲染的内容对象。因为我们都知道jsx代码是必须有一个包裹标签的，也就是说container只能有一个子元素，所以使用firstChild就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">virtualDOM, container, oldDOM = container.firstChild</span>) </span>&#123;
    diff(virtualDOM, container, oldDOM);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们就可以在oldDOM中过去到老的虚拟DOM对象了，我们在diff算法中先获取。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> oldVirtualDOM = oldDOM && oldDOM._virtualDOM;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们就可以去进行对比了。如果oldVirtualDOM存在的话，我们首先对比两个元素的标签类型相同，如果两个元素类型相同，需要判断是文本类型节点还是元素类型节点，文本类型直接更新内容，元素类型就要更新标签的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mountElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./mountElement'</span>;
<span class="hljs-keyword">import</span> updateTextNode <span class="hljs-keyword">from</span> <span class="hljs-string">'./updateTextNode'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff</span> (<span class="hljs-params">virtualDOM, container, oldDOM</span>) </span>&#123;
    <span class="hljs-comment">// 获取老的虚拟DOM对象</span>
    <span class="hljs-keyword">const</span> oldVirtualDOM = oldDOM && oldDOM._virtualDOM;
    <span class="hljs-comment">// 判断oldDOM是否在巡</span>
    <span class="hljs-keyword">if</span> (!oldDOM) &#123;
        <span class="hljs-keyword">return</span> mountElement(virtualDOM, container);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVirtualDOM && virtualDOM.type === oldVirtualDOM.type) &#123;
        <span class="hljs-comment">// 两个元素类型相同，需要判断是文本类型节点还是元素类型节点</span>
        <span class="hljs-comment">// 文本类型直接更新内容</span>
        <span class="hljs-comment">// 元素类型就要更新标签的属性</span>
        <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
            <span class="hljs-comment">// 更新内容</span>
            updateTextNode(virtualDOM, oldVirtualDOM, oldDOM);

        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 更新元素属性</span>
        &#125;
        <span class="hljs-comment">// 遍历子元素进行对比</span>
        virtualDOM.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
            diff(child, oldDOM, oldDOM.childNodes[i]);
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样这里我们抽出一个更新方法。在这个方法中判断内容是否相同，如果不相同就更新。</p>
<p>src/tinyReact/updateTextNode.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateTextNode</span> (<span class="hljs-params">virtualDOM, oldVirtualDOM, oldDOM</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (virtualDOM.props.textContent !== oldVirtualDOM.props.textContent) &#123;
        <span class="hljs-comment">// 更新DOM节点内容</span>
        oldDOM.textContent = virtualDOM.props.textContent;
        <span class="hljs-comment">// 更新老的虚拟DOM</span>
        oldDOM._virtualDOM = virtualDOM;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">更新DOM元素 - 节点属性</h4>
<p>其实也就是将新旧节点属性对象进行对比，从中找到差异部分，然后将差异部分更新到节点属性上。我们这里使用之前定义好的updateNodeElement方法，之前我们使用这个方法实现给元素更新属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
    <span class="hljs-comment">// 更新内容</span>
    updateTextNode(virtualDOM, oldVirtualDOM, oldDOM);

&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 更新元素属性</span>
    <span class="hljs-comment">// 要更新的哪个元素，更新的虚拟DOM，旧的虚拟DOM</span>
    updateNodeElement(oldDOM, virtualDOM, oldVirtualDOM)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们修改updateNodeElement这个方法，在里面添加oldVirtualDOM参数。获取到新旧节点属性对象newProps和oldProps，这里的oldVirtualDOM不是一直存在的，更新的时候才存在，所以需要兼容一下空状态。</p>
<p>再循环新的属性对象的时候可以拿到属性名称，可以通过属性名称对比旧的属性值，来对比两个属性值是否相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateNodeElement</span>(<span class="hljs-params">newElement, virtualDOM, oldVirtualDOM</span>) </span>&#123;
    <span class="hljs-comment">// 获取节点对应的属性对象</span>
    <span class="hljs-keyword">const</span> newProps = virtualDOM.props || &#123;&#125;;
    <span class="hljs-comment">// 获取旧的属性对象</span>
    <span class="hljs-keyword">const</span> oldProps = oldVirtualDOM.props || &#123;&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比两个值是否相同，如果不相同就做更新操作。在更新操作中事件需要注意，清除原有事件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 如果存在原有事件，需要删除掉。</span>
<span class="hljs-keyword">if</span> (oldPropsValue) &#123;
    newElement.addEventListener(eventName, oldPropsValue);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有属性被删除了，需要删除DOM对象上的属性。我们可以循环oldProps，如果newProps中没有，则是被删除的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断属性被删除的情况</span>
<span class="hljs-built_in">Object</span>.keys(oldProps).forEach(<span class="hljs-function"><span class="hljs-params">propName</span> =></span> &#123;
    <span class="hljs-comment">// 新的属性值</span>
    <span class="hljs-keyword">const</span> newPropsValue = newProps[propName];
    <span class="hljs-comment">// 旧的属性值</span>
    <span class="hljs-keyword">const</span> oldPropsValue = oldProps[propName];
    <span class="hljs-keyword">if</span> (!newPropsValue) &#123;
        <span class="hljs-comment">// 判断是否是事件属性</span>
        <span class="hljs-keyword">if</span> (propName.startsWith(<span class="hljs-string">'on'</span>)) &#123;
                <span class="hljs-comment">// 截取出事件名称</span>
                <span class="hljs-keyword">const</span> eventName = propName.toLowerCase().slice(<span class="hljs-number">2</span>);
                <span class="hljs-comment">// 删除事件</span>
                newElement.removeEventListener(eventName, oldPropsValue);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (propName !== <span class="hljs-string">'children'</span>) &#123;
            newElement.removeAttribute(propName);
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虚拟DOM类型相同，如果是元素节点，就对比元素节点属性是否发生变化，如果是文本节点就对比文本节点内容是否发生变化。要实现对比，需要先从已存在的DOM对象中获取对应的虚拟DOM对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> oldVirtualDOM = oldDOM && oldDOM._virtualDOM
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断oldVirtualDOM是否存在，如果存在则继续判断要对比的虚拟DOM类型是否相同，如果类型相同则判断节点类型是否是文本，如果是文本节点对比，就调用updateTextNode方法，如果是元素节点对比就调用updateNodeElement方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVirtualDOM && virtualDOM.type === oldVirtualDOM.type) &#123;
    <span class="hljs-comment">// 两个元素类型相同，需要判断是文本类型节点还是元素类型节点</span>
    <span class="hljs-comment">// 文本类型直接更新内容</span>
    <span class="hljs-comment">// 元素类型就要更新标签的属性</span>
    <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
        <span class="hljs-comment">// 更新内容</span>
        updateTextNode(virtualDOM, oldVirtualDOM, oldDOM);

    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 更新元素属性</span>
        <span class="hljs-comment">// 要更新的哪个元素，更新的虚拟DOM，旧的虚拟DOM</span>
        updateNodeElement(oldDOM, virtualDOM, oldVirtualDOM)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比对的都是最上层元素，上层元素比对完成以后还需要递归比对子元素</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 遍历子元素进行对比</span>
virtualDOM.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
    diff(child, oldDOM, oldDOM.childNodes[i]);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果两个节点类型不相同我们要如何处理，如果两个节点类型不同他们之间就没有必要进行比对了，只需要使用新的虚拟DOM生成新的DOM对象，替换旧的DOM对象就可以了。</p>
<p>在diff.js中使用else if来处理这种情况。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!oldDOM) &#123;
    <span class="hljs-keyword">return</span> mountElement(virtualDOM, container);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (virtualDOM.type !== oldVirtualDOM.type && <span class="hljs-keyword">typeof</span> virtualDOM.type !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 如果标签类型不相同，并且不是组件。</span>
    <span class="hljs-keyword">const</span> newElement = createDOMElement(virtualDOM);
    <span class="hljs-comment">// 替换DOM元素</span>
    oldDOM.parentNode.replaceChild(newElement, oldDOM);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">删除节点</h4>
<p>删除节点发生在节点更新之后，并且发生在同一个父节点下的所有子节点身上，在节点更新完成以后，如果旧节点对象的数量多于新虚拟DOM节点的数量，就说明有节点需要被删除。</p>
<p>这里我们获取就得DOM节点的数量，如果新旧节点数量不相同，我们就循环旧的DOM节点，然后从后先前删除，直到新旧DOM节点数量相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除节点</span>
<span class="hljs-comment">// 获取旧节点</span>
<span class="hljs-keyword">const</span> oldChildNodes = oldDOM.childNodes;
<span class="hljs-comment">// 判断旧节点的数量</span>
<span class="hljs-keyword">if</span> (oldChildNodes.length > virtualDOM.children.length) &#123;
    <span class="hljs-comment">// 循环删除节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldChildNodes.length - <span class="hljs-number">1</span>; i > virtualDOM.children.length -<span class="hljs-number">1</span>; i--) &#123;
        oldDOM.removeChild(oldChildNodes[i]);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为前面我们已经时候更新方法保证了对应的Node相同，多余的Node节点可以直接删除，不用再关心保留下的Node节点不同步的问题。</p>
<h4 data-id="heading-12">类组件的状态更新</h4>
<p>要实现类组件的更新，需要实现setState方法，我们先定义一个Alert组件，点击按钮的时候更新组件内的title属性，更新到页面中。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Alert</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">TinyReact</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'default'</span>
    &#125;
    <span class="hljs-built_in">this</span>.handileClick = <span class="hljs-built_in">this</span>.handileClick.bind(<span class="hljs-built_in">this</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">handileClick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Changed'</span>
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> 
      <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
        this.handileClick();
      &#125;&#125;>改变Title<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这里我们调用的setState应该是父类Component中的setState。当子类调用setState的时候首先要明确setState里面的this指向的是子类的实例对象。</p>
<pre><code class="hljs language-js copyable" lang="js">setState (state) &#123;
    <span class="hljs-built_in">this</span>.state = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, <span class="hljs-built_in">this</span>.state, state);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当state发生改变的时候我们需要重新去触发render方法，当state发生改变之后需要更新页面中的state，我们可以通过render获取到最新的虚拟DOM，然后和旧的虚拟DOM进行对比更新。</p>
<p>比对这里比较麻烦，调用render方法我们是可以获取到当前的虚拟DOM的，但是确无法获取到页面展示的DOM，我们可以定义一个setDOM方法将页面展示的DOM存储起来。在类组件被实例化的时候将它传给setDOM。然后调用diff方法进行对比更新就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.props = props;
    &#125;
    setState (state) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, <span class="hljs-built_in">this</span>.state, state);
        <span class="hljs-comment">// 获取最新的DOM对象</span>
        <span class="hljs-keyword">const</span> virtualDOM = <span class="hljs-built_in">this</span>.render();
        <span class="hljs-comment">// 获取旧的virtualDOM对象进行比对</span>
        <span class="hljs-keyword">const</span> oldDOM = <span class="hljs-built_in">this</span>.getDOM();
        <span class="hljs-comment">// 实现对比</span>
        diff(virtualDOM, container, oldDOM);
    &#125;
    setDOM (dom) &#123; <span class="hljs-comment">// 存储页面中展示的DOM对象</span>
        <span class="hljs-built_in">this</span>._dom = dom;
    &#125;
    getDOM () &#123; <span class="hljs-comment">// 获取页面展示的DOM</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._dom;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">组件更新功能</h4>
<p>在组件更新时可能渲染的是同一个组件也可能渲染的是不同的组件，我们两种都要兼顾。</p>
<p>首先我们要在diff中判断要更新的虚拟DOM是否是组件，如果是组件在判断要更新的组件和未更新前的组件是否是同一个组件，如果不是同一个组件就不需要做组件更新操作，直接调用mountElement方法将组件返回的虚拟DOM添加到页面中。</p>
<p>如果是同一个组件，就执行更新组件操作，其实就是将最新的props传递到组件中，再调用组件的render方法获取组件返回的最新的虚拟DOM对象，再将虚拟DOM对象传递给diff方法，让diff方法找出差异，从而将差异更新到真实DOM对象中。</p>
<p>在更新组件的过程中还要在不同阶段调用器不同的生命周期函数。</p>
<p>我们首先在diff方法中判断要更新的虚拟DOM是否是组件。</p>
<p>如果是组件又分为多种情况，新增diffComponent方法进行处理。这个方法接收四个参数，第一个参数是组件本身的虚拟DOM对象，通过它可以获取到组件最新的props，第二个参数是要更新的组件的实例对象，通过它可以调用组件的生命周期函数，可以更新组件的props属性，可以获取到组件返回的最新的虚拟DOM对象，第三个参数是要更新的DOM对象，在更新组件时，需要在已有DOM对象的身上进行修改，实现DOM最小化操作，获取旧的虚拟DOM对象，第四个参数是要更新到的容器元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> virtualDOM.type === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 渲染是一个组件</span>
    diffComponent(virtualDOM, oldComponent, oldDOM, container);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在diffComponent中我们要判断virtualDOM和oldComponent是否是同一个组件，只要判断他们的构造函数是否是同一个即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diffComponent</span>(<span class="hljs-params">virtualDOM, oldComponent, oldDOM, container</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isSameComponent(virtualDOM, oldComponent)) &#123;
        <span class="hljs-comment">// 是同一个组件</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不是同一个组件</span>
        <span class="hljs-comment">// 替换页面原有的对象，也就是删除原有DOM，增加新的DOM</span>
        mountElement(virtualDOM, container, oldDOM);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSameComponent</span>(<span class="hljs-params">virtualDOM, oldComponent</span>) </span>&#123;
    <span class="hljs-comment">// 判断是否是同一个组件，只要判断他们的构造函数是否是同一个即可</span>
    <span class="hljs-keyword">return</span> oldComponent && virtualDOM.type === oldComponent.constructor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不是同一个组件就替换原有的组件。需要在mountNativeElement接收oldDOM，然后删除这个DOM。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountNativeElement</span>(<span class="hljs-params">virtualDOM, container, oldDOM</span>) </span>&#123;
    <span class="hljs-comment">// 将虚拟dom转换成真实的对象</span>
    <span class="hljs-comment">// 判断旧的DOM对象是否存在，如果存在则删除</span>
    <span class="hljs-keyword">if</span> (oldDOM) &#123;
        unmountNode(oldDOM);
    &#125;
    <span class="hljs-keyword">let</span> newElement = createDOMElement(virtualDOM);
    <span class="hljs-comment">// 将转换之后的DOM对象放在页面中</span>
    container.appendChild(newElement);
    <span class="hljs-comment">// 获取实例对象</span>
    <span class="hljs-keyword">const</span> component = virtualDOM.component;
    <span class="hljs-keyword">if</span> (component) &#123;
        component.setDOM(newElement);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要更新的组件和旧组件是同一个组件，我们使用updateComponent方法实现。传入virtualDOM, container, oldDOM, container四个参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diffComponent</span>(<span class="hljs-params">virtualDOM, oldComponent, oldDOM, container</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isSameComponent(virtualDOM, oldComponent)) &#123;
        <span class="hljs-comment">// 是同一个组件</span>
        updateComponent(virtualDOM, container, oldDOM, container);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不是同一个组件</span>
        <span class="hljs-comment">// 替换页面原有的对象，也就是删除原有DOM，增加新的DOM</span>
        mountElement(virtualDOM, container, oldDOM);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个方法中要做的事情就是组件更新。首先我们要去更新组件里面的props属性，这个最新的props存储在virtualDOM的props中，我们需要在通过oldComponent实例调用一个更新props的方法，将props传递给他。</p>
<p>我们需要在Comonent.js这个类中定义这个更新props的方法，updateProps, 接收一个props。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">updateProps</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.props = props;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们就可以通过oldComponent调用updateProps方法更新props了。</p>
<pre><code class="hljs language-js copyable" lang="js">oldComponent.updateProps(virtualDOM.props);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新之后我们需要获取到最新的虚拟DOM。然后通过diff算法进行比较更新。不要忘记将更新后的实例赋值给新的虚拟DOM实例中，方便后面使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateComponent</span>(<span class="hljs-params">virtualDOM, oldComponent, oldDOM, container</span>) </span>&#123;
    <span class="hljs-comment">// 组件更新</span>
    oldComponent.updateProps(virtualDOM.props);
    <span class="hljs-comment">// 获取最新的虚拟DOM，</span>
    <span class="hljs-keyword">let</span> nextVirtualDOM = oldComponent.render();
    <span class="hljs-comment">// 更新实例</span>
    nextVirtualDOM.component = oldComponent;
    <span class="hljs-comment">// diff分别和更新。</span>
    diff(nextVirtualDOM, container, oldDOM)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">组件生命周期</h4>
<p>在组件的更新过程中我们还需要去调用组件的生命周期函数，我们先在Component类中将生命周期默认添加进去。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">componentWillReceviceProps</span>(<span class="hljs-params">nextProps</span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params">nextProps, nextState</span>)</span> &#123;
    <span class="hljs-keyword">return</span> nextProps !== <span class="hljs-built_in">this</span>.props || nextState !== <span class="hljs-built_in">this</span>.state;
&#125;
<span class="hljs-function"><span class="hljs-title">componentWillUpdate</span>(<span class="hljs-params">nextProps, nextState</span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, preState</span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在updateComponent这个函数中我们应该先调用componentWillReceviceProps生命周期，在调用这个生命周期的时候要传入最新的props。</p>
<pre><code class="hljs language-js copyable" lang="js">oldComponent.componentWillReceviceProps(virtualDOM.props);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们要调用shouldComponentUpdate生命周期,来判断组件是否需要更新。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (oldComponent.shouldComponentUpdate(virtualDOM.props)) &#123;
    <span class="hljs-comment">// 组件更新</span>
    oldComponent.updateProps(virtualDOM.props);
    <span class="hljs-comment">// 获取最新的虚拟DOM，</span>
    <span class="hljs-keyword">let</span> nextVirtualDOM = oldComponent.render();
    <span class="hljs-comment">// 更新实例</span>
    nextVirtualDOM.component = oldComponent;
    <span class="hljs-comment">// diff分别和更新。</span>
    diff(nextVirtualDOM, container, oldDOM)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着要调用componentWillUpdate生命周期。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生命周期</span>
oldComponent.componentWillUpdate(virtualDOM.props);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件更新结束之后需要执行componentDidUpdate生命周期, 这里传入的应该是更新前的props，我们可以提前定义一个变量存储起来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateComponent</span>(<span class="hljs-params">virtualDOM, oldComponent, oldDOM, container</span>) </span>&#123;
    <span class="hljs-comment">// 生命周期</span>
    oldComponent.componentWillReceviceProps(virtualDOM.props);
    <span class="hljs-comment">// 判断是否更新生命周期</span>
    <span class="hljs-keyword">if</span> (oldComponent.shouldComponentUpdate(virtualDOM.props)) &#123;
        <span class="hljs-comment">// 存储更新前的props</span>
        <span class="hljs-keyword">let</span> prevProps = oldComponent.props;
        <span class="hljs-comment">// 生命周期</span>
        oldComponent.componentWillUpdate(virtualDOM.props);
        <span class="hljs-comment">// 组件更新</span>
        oldComponent.updateProps(virtualDOM.props);
        <span class="hljs-comment">// 获取最新的虚拟DOM，</span>
        <span class="hljs-keyword">let</span> nextVirtualDOM = oldComponent.render();
        <span class="hljs-comment">// 更新实例</span>
        nextVirtualDOM.component = oldComponent;
        <span class="hljs-comment">// diff分别和更新。</span>
        diff(nextVirtualDOM, container, oldDOM)
        <span class="hljs-comment">// 生命周期</span>
        oldComponent.componentDidUpdate(prevProps);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">实现ref功能</h4>
<p>为节点添加ref属性可以获取到这个节点的DOM对象，比如在Demo中，为p标签添加了ref属性，目的是获取p元素对象，在点击按钮时获取p中的内容。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">TinyReact</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'default'</span>
    &#125;
  &#125;

  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;p</span> =></span> this.p = p&#125;>&#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> 
      <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
        // this.handileClick();
        console.log(this.p.innerText);
      &#125;&#125;>获取内容<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;

TinyReact.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"yindong"</span>/></span></span>, root);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现起来也比较简单，在创建节点时判断其虚拟DOM对象中是否存在ref属性，如果有就调用ref属性中所存储的方法并且将创建出来的DOM对象作为参数传递给ref方法，这样在渲染组件节点的时候就可以拿到元素对象并将元素对象存储为组件属性。在createDOMElement方法中添加。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (virtualDOM.props && virtualDOM.props.ref) &#123;
    virtualDOM.props.ref(newElement);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在类组件身上也可以添加ref属性，目的是获取组件的实例对象。可以在mountComponent方法中，判断了如果当前处理的是类组件，就通过类组件返回的虚拟DOM对象中获取到实例对象，在实例对象中的props属性中寻找ref，如果存在就调用ref并且参数传入实例对象即可。</p>
<p>同时在这里我们也可以将componentDidMount生命周期函数添加上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 用于存储实例对象</span>
<span class="hljs-keyword">let</span> component = <span class="hljs-literal">null</span>;
<span class="hljs-comment">// 判断组件是类组件还是函数组件</span>
<span class="hljs-keyword">if</span> (isFunctionComponent(virtualDOM)) &#123;
    <span class="hljs-comment">// 处理函数组件</span>
    nextVirtualDOM = buildFunctionComponent(virtualDOM);
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 处理类组件</span>
    nextVirtualDOM = buildClassComponent(virtualDOM);
    component = nextVirtualDOM.component;
&#125;
<span class="hljs-keyword">if</span> (isFunction(nextVirtualDOM)) &#123;
    mountComponent(nextVirtualDOM, container);
&#125;
<span class="hljs-keyword">if</span> (component) &#123;
    component.componentDidMount();
&#125;
<span class="hljs-comment">// 执行ref</span>
<span class="hljs-keyword">if</span> (component && component.props && component.props.ref) &#123;
    omponent.props.ref(component);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">key属性实现</h4>
<p>在React中，渲染类型数据时通常会在被渲染的列表元素上添加key属性，key属性就是数据的唯一标识，帮助React识别哪些元素被修改或者删除了，从而达到DOM最小化操作的目的。</p>
<p>key属性不需要全局唯一，但是在同一个父节点下的兄弟节点之间必须是唯一的。也就是说，在比对同一个父节点下类型相同的子节点时需要用到key属性。</p>
<p>在之前我们删除节点的讲解中的实现方式是，从后向前依次删除，让前面的节点保持相同，删除多余的节点。其实这是很低效的，正确的做法是应该找到不需要的节点直接删除。使用key属性就可以达到这个效果。</p>
<p>在两个元素进行比对时，如果类型相同，就循环旧的DOM对象的子元素，查看其身上是否有key属性，如果有就将这个子元素的DOM对象存储在一个JavaScirpt对象中，接着循环要渲染的虚拟DOM对象的子元素，在循环过程中获取到这个子元素的key属性，然后使用这个key属性到JavaScript对象中查到DOM对象，如果能够找到就说明这个元素是已经存在的，是不需要重新渲染的，如果通过key属性找不到这个元素，就说明这个元素是新增的。</p>
<p>在diff算法中开始添加此功能。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将拥有key属性的子元素放置在一个单独的对象中</span>
<span class="hljs-keyword">const</span> keyedElements = &#123;&#125;;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = oldDOM.childNodes.length; i < len; i++) &#123;
    <span class="hljs-keyword">let</span> domElement = oldDOM.childNodes[i];
    <span class="hljs-comment">// 判断节点类型，元素节点才获取</span>
    <span class="hljs-keyword">if</span> (domElement.nodeType === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">const</span> key = domElement.getAttribute(<span class="hljs-string">'key'</span>)
        <span class="hljs-keyword">if</span> (key) &#123;
            keyedElements[key] = domElement;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环要渲染的虚拟DOM的子元素，获取子元素的key属性，查看这个元素是否存在，如果存在就查看当前位置的元素是否是我们期望的元素。如果不是就插入到这个位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 循环要渲染的虚拟DOM的子元素，获取子元素的key属性</span>
virtualDOM.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> key = child.props.key;
    <span class="hljs-keyword">if</span> (key) &#123;
        <span class="hljs-keyword">const</span> domElement = keyedElements[key];
        <span class="hljs-keyword">if</span> (domElement) &#123;
            <span class="hljs-comment">// 查看当前位置的元素是否是我们期望的元素，如果不是就插入到这个位置</span>
            <span class="hljs-keyword">if</span> (oldDOM.childNodes[i] && oldDOM.childNodes[i] !== domElement ) &#123;
                oldDOM.insertBefore(domElement, oldDOM.childNodes[i]);
            &#125;
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还需要判断keyedElements是否存在元素, 如果没有元素就是没有key，那我们通过索引去对比，如果有key就通过key做对比。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> hasNoKey = <span class="hljs-built_in">Object</span>.keys(keyedElements).length === <span class="hljs-number">0</span>;

<span class="hljs-keyword">if</span> (hasNoKey) &#123;
    <span class="hljs-comment">// 遍历子元素进行对比</span>
    virtualDOM.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
        diff(child, oldDOM, oldDOM.childNodes[i]);
    &#125;)
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 循环要渲染的虚拟DOM的子元素，获取子元素的key属性</span>
    virtualDOM.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, i</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> key = child.props.key;
        <span class="hljs-keyword">if</span> (key) &#123;
            <span class="hljs-keyword">const</span> domElement = keyedElements[key];
            <span class="hljs-keyword">if</span> (domElement) &#123;
                <span class="hljs-comment">// 查看当前位置的元素是否是我们期望的元素，如果不是就插入到这个位置</span>
                <span class="hljs-keyword">if</span> (oldDOM.childNodes[i] && oldDOM.childNodes[i] !== domElement) &#123;
                    oldDOM.insertBefore(domElement, oldDOM.childNodes[i]);
                &#125;
            &#125;
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们还要处理一下通过key属性找不到DOM元素的情况，如果找不到就说明这是新增的，我们可以通过mountElement方法直接渲染到页面中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (key) &#123;
    <span class="hljs-keyword">const</span> domElement = keyedElements[key];
    <span class="hljs-keyword">if</span> (domElement) &#123;
        <span class="hljs-comment">// 查看当前位置的元素是否是我们期望的元素，如果不是就插入到这个位置</span>
        <span class="hljs-keyword">if</span> (oldDOM.childNodes[i] && oldDOM.childNodes[i] !== domElement) &#123;
            oldDOM.insertBefore(domElement, oldDOM.childNodes[i]);
        &#125;
    &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 新增元素</span>
    mountElement(child, oldDOM, oldDOM.childNodes[i])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要在mountNativeElement这个方法中判断，如果oldDOM存在，我们应该使用container.insertBefore方法插入到oldDOM前面，如果不存在才appendChild到最后。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> newElement = createDOMElement(virtualDOM);
<span class="hljs-keyword">if</span> (oldDOM) &#123;
    container.insertBefore(newElement, oldDOM);
&#125; <span class="hljs-keyword">else</span> &#123;
    container.appendChild(newElement);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">卸载节点</h4>
<p>在节点比对的过程中，如果旧节点的数量多于要渲染的新节点的数量，就说明有节点被删除了，继续判断keyedElements对象中是否有元素，如果没有就使用索引方式删除，如果有就要使用key属性比对的方式进行删除。</p>
<p>实现思路是循环旧节点，在循环旧节点的过程中获取旧节点对应的key属性，然后根据key属性在新节点中查找这个旧节点，如果找到就说明这个节点没有被删除，如果没有找到就说明节点被删除了，调用卸载节点的方法删除节点即可。</p>
<p>我们在diff删除节点的时候判断hasNoKey是否有key。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除节点</span>
<span class="hljs-comment">// 获取旧节点</span>
<span class="hljs-keyword">const</span> oldChildNodes = oldDOM.childNodes;
<span class="hljs-comment">// 判断旧节点的数量</span>
<span class="hljs-keyword">if</span> (oldChildNodes.length > virtualDOM.children.length) &#123;
    <span class="hljs-keyword">if</span> (hasNoKey) &#123;
        <span class="hljs-comment">// 循环删除节点</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldChildNodes.length - <span class="hljs-number">1</span>; i > virtualDOM.children.length - <span class="hljs-number">1</span>; i--) &#123;
            unmountNode(oldChildNodes[i]);
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 通过key属性删除节点</span>
        <span class="hljs-comment">// 拿旧的key去新的里面寻找，找不到就删除</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < oldChildNodes.length; i++) &#123;
            <span class="hljs-keyword">const</span> oldChild = oldChildNodes[i];
            <span class="hljs-keyword">const</span> oldChildKey = oldChild._virtualDOM.props.key;
            <span class="hljs-keyword">let</span> found = <span class="hljs-literal">false</span>;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>; n < virtualDOM.children.length; n++) &#123;
                <span class="hljs-keyword">if</span> (oldChildKey === virtualDOM.children[n].props.key) &#123;
                    found = <span class="hljs-literal">true</span>;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
            <span class="hljs-keyword">if</span> (!found) &#123;
                unmountNode(oldChild);
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然卸载节点并不是说将节点直接删除就可以了，还需要考虑以下情况，如果要删除的节点是文本节点的话可以直接删除，如果过是组件生成的，需要调用组件的卸载生命周期函数，如果节点中包含了其他组件生成的节点，需要调用其他组件的卸载生命周期，如果节点身上有ref属性还需要删除通过ref属性传递给组件的DOM节点对象，如果有事件也需要删除事件。我们可以在unmountNode函数中处理这些情况。</p>
<p>如果是文本节点就直接删除。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmountNode</span>(<span class="hljs-params">node</span>) </span>&#123;
    <span class="hljs-comment">// 获取虚拟DOM对象</span>
    <span class="hljs-keyword">const</span> virtualDOM = node._virturalDOM;
    <span class="hljs-comment">// 文本节点直接删除</span>
    <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
        node.remove();
        <span class="hljs-keyword">return</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不是文本节点需要判断一下节点是否是组件生成的，如果是组件生成的需要调用组件的卸载生命周期。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断节点是否是组件生成的。</span>
<span class="hljs-keyword">const</span> component = virtualDOM.component;
<span class="hljs-keyword">if</span> (component) &#123;
    component.componentWillUnmount();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还需要判断节点身上是否有ref属性，如果有的话需要清理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断节点身上是否有ref属性，如果有的话需要清理</span>
<span class="hljs-keyword">if</span> (virtualDOM.props && virtualDOM.props.ref) &#123;
    virtualDOM.props.ref(<span class="hljs-literal">null</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也要判断节点上是否有事件存在，如果有需要卸载事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断事件是否存在</span>
<span class="hljs-built_in">Object</span>.keys(virtualDOM.props).forEach(<span class="hljs-function"><span class="hljs-params">propsName</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (propsName.startsWith(<span class="hljs-string">'on'</span>)) &#123;
        <span class="hljs-keyword">const</span> eventName = propsName.toLocaleLowerCase().slice(<span class="hljs-number">0</span>, <span class="hljs-number">2</span>);
        <span class="hljs-keyword">const</span> eventHandler = virtualDOM.props[propsName];
        node.removeEventListener(eventName, eventHandler);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断节点中是否存在子节点，如果存在需要递归删除他们，因为子节点也需要判断上述内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 递归删除子节点</span>
<span class="hljs-keyword">if</span> (node.childNodes.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < node.childNodes.length; i++) &#123;
        unmountNode(node.childNodes[i]);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们需要执行node.remove删除掉当前的节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除节点</span>
node.remove();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此删除DOM节点我们这里就写完了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmountNode</span>(<span class="hljs-params">node</span>) </span>&#123;
    <span class="hljs-comment">// 获取虚拟DOM对象</span>
    <span class="hljs-keyword">const</span> virtualDOM = node._virtualDOM;
    <span class="hljs-comment">// 文本节点直接删除</span>
    <span class="hljs-keyword">if</span> (virtualDOM.type === <span class="hljs-string">'text'</span>) &#123;
        node.remove();
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// 判断节点是否是组件生成的。</span>
    <span class="hljs-keyword">const</span> component = virtualDOM.component;
    <span class="hljs-keyword">if</span> (component) &#123;
        component.componentWillUnmount();
    &#125;
    <span class="hljs-comment">// 判断节点身上是否有ref属性，如果有的话需要清理</span>
    <span class="hljs-keyword">if</span> (virtualDOM.props && virtualDOM.props.ref) &#123;
        virtualDOM.props.ref(<span class="hljs-literal">null</span>)
    &#125;
    <span class="hljs-comment">// 判断事件是否存在</span>
    <span class="hljs-built_in">Object</span>.keys(virtualDOM.props).forEach(<span class="hljs-function"><span class="hljs-params">propsName</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (propsName.startsWith(<span class="hljs-string">'on'</span>)) &#123;
            <span class="hljs-keyword">const</span> eventName = propsName.toLocaleLowerCase().slice(<span class="hljs-number">0</span>, <span class="hljs-number">2</span>);
            <span class="hljs-keyword">const</span> eventHandler = virtualDOM.props[propsName];
            node.removeEventListener(eventName, eventHandler);
        &#125;
    &#125;)

    <span class="hljs-comment">// 递归删除子节点</span>
    <span class="hljs-keyword">if</span> (node.childNodes.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < node.childNodes.length; i++) &#123;
            unmountNode(node.childNodes[i]);
        &#125;
    &#125;
    <span class="hljs-comment">// 删除节点</span>
    node.remove();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            