
---
title: '手把手带你写一个Mini 版的React'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac695c48dd6a48beb015a7de0332ef3a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 01:14:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac695c48dd6a48beb015a7de0332ef3a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>还记得我上次给大家安利的<code>build ur own react</code>那篇文章吗, 其实有些同学和我说那个是上万字还全是英文的,有些看不太明白, 于是我...总结了一个中文的版本（根据自己的对react的理解联合上部分觉得他文中说的比较好的一些地方）, 希望能够对大家有所帮助</p>
<p>顺便再安利一下这篇文章, 针不戳, 有能力的同学可以看了我这篇中文文档再去看看这篇英文文档: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpomb.us%2Fbuild-your-own-react%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pomb.us/build-your-own-react/" ref="nofollow noopener noreferrer">pomb.us/build-your-…</a></p>
<p><strong>那么, let's go</strong></p>
<hr>
<p>这篇文章的一个核心目的是带着大家基于react的一个源码架构, 我们来从0实现一个自己的mini版本的react, 为啥是mini呢, 因为抓大放小, 抓的大就是我们把react的核心功能都实现一遍,
放的小就是我们把一些react在源码中做的性能优化和一些平时我们用得少甚至不会去用的功能给忽略掉</p>
<p><strong>本篇博文要实现的功能是基于React16.8存在的</strong></p>
<p>我们要实现的一个功能大致如下:</p>
<ul>
<li>createElement 函数</li>
<li>render 函数</li>
<li>Concurrent Mode & Fiber</li>
<li>render阶段和commit阶段</li>
<li>Reconciliation(react中的diff算法)</li>
</ul>
<h4 data-id="heading-0">基本回顾</h4>
<p>这一块主要是和大家一起回顾一下React, JSX, Dom的一个基本工作模式, 如果你觉得自己对这块已经比较熟了, 那你完全可以跳过这一节直接进入下一节的阅读</p>
<p>来看一个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"foo"</span>></span>hello, div<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);
ReactDOM.render(element, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码完全是基于React架构的一个实现, 他实现了将一个<code>div</code>元素渲染进<code>id</code>为<code>root</code>的真实dom容器中的功能</p>
<p>我们现在不用react, 就用原生JS来实现这个功能, 你可以停下想想, 你会怎么实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比较nice的方式就是我们可以直接用一个对象来描述一个JSX表达式</span>
<span class="hljs-comment">// 当然不限制你的想象力, 只要你有任何方式可以描述出上面的JSX表达式</span>
<span class="hljs-comment">// 最终能够渲染出来, 那都是OK的</span>
<span class="hljs-keyword">const</span> element = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"div"</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">"foo"</span>
    &#125;,
    <span class="hljs-attr">children</span>: [<span class="hljs-string">"hello, div"</span>], <span class="hljs-comment">// 这个children为啥是一个array, 因为你想啊, 我们是可以直接在div中写什么span标签, a标签的, 这个时候我们就必须用array来形容他了</span>
&#125;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>); <span class="hljs-comment">// 这个本身原生JS就提供了支撑, 所以我们压根没必要进行转换</span>

<span class="hljs-comment">// render方法的作用就是将element渲染进container中, 我们暂且不实现render方法本身</span>
<span class="hljs-comment">// 我们详细如果我们自己要达到将element渲染进container中要怎么做</span>
<span class="hljs-keyword">const</span> divDom = <span class="hljs-built_in">document</span>.createElement(element.type); <span class="hljs-comment">// 这样我们就创建了一个div节点</span>
divDom.setAttribute(<span class="hljs-string">"title"</span>, <span class="hljs-string">"foo"</span>); <span class="hljs-comment">// 将属性打上去, 其实你可以直接使用div["title"] = "foo"的形式</span>

<span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode();
textNode.nodeValue = element.children[<span class="hljs-number">0</span>];

divDom.appendChild(textNode);

container.appendChild(divDom);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK, 到了这一步, 上面的代码就给我们不用React但是实现和react一样的功能提供了技术支撑, 这也是一个简单的基本回顾, 下面我们可以正式进入正题了</p>
<h4 data-id="heading-1">createElement函数</h4>
<blockquote>
<p>写<code>createElement</code>函数之前,我们应该要知道一点, 就是我们书写的JSX表达式最终都会被babel编译成<code>createElement</code>的形式</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比如我有一行JSX表达式如下:</span>
<span class="hljs-keyword">const</span> element = (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"wrapper"</span>></span>hello, wrapper<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);

<span class="hljs-comment">// 他最终会被babel编译成如下形式</span>
<span class="hljs-keyword">const</span> element = React.createElement(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"wrapper"</span> &#125;, <span class="hljs-string">"hello wrapper"</span>);

<span class="hljs-comment">// 至于你要说他的怎么编译的, 他还能咋编译, 字符串替换呗, 这个咱就暂且不论</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过之前的回顾认知代码我们应该也基本了解了, 其实本质上来说, 最终React和真实dom的一个连接点就是我们需要拥有一个具备<code>type</code>和其他更多属性的一个对象, 而<code>createElement</code>就是要给我们提供一个<code>element</code>描述对象</p>
<p>那我们怎么去设计这个函数呢？ 你可以停下来想想自己的思路</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们先固定参数</span>
<span class="hljs-comment">// type: 要创建上面说的一个对象, 我们需要知道当前的节点类型</span>
<span class="hljs-comment">// props: 当前节点上都有什么属性, 是一个对象</span>
<span class="hljs-comment">// children: 你可以看到我使用了收集运算符, 那就意味着后续的所有剩余参数我都要</span>
<span class="hljs-comment">// 收集进children作为他的元素存在, 而这样我们也保证了children永远是一个数组</span>
<span class="hljs-comment">// 当然你也可以强行约束用户手动给你传递一个children, 那这样你的createElement</span>
<span class="hljs-comment">// 就固定永远只有三个参数了， 不同的写法都可以</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
    
    <span class="hljs-comment">// 然后我们根据参数将所有的属性返回出去</span>
    <span class="hljs-comment">// 我这里是把children又塞入了props对象里, 这个也没所谓的</span>
    <span class="hljs-comment">// 你想放哪放哪, 只要保证这个返回的对象里有children就ok拉</span>
    <span class="hljs-keyword">return</span> &#123;
        type,
        <span class="hljs-attr">props</span>: &#123;
            ...props,
            children
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们来尝试写个复杂一点的结构, 看看会不会有什么问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们有一个JSX表达式如下</span>
<span class="hljs-keyword">const</span> element = (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>我是标题<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入文字"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);

<span class="hljs-comment">// 根据预期的想法, 上面的代码会被babel转换成如下形式</span>
createElement(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"wrapper"</span> &#125;, 
        React.createElement(<span class="hljs-string">"span"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"title"</span> &#125;, <span class="hljs-string">"我是标题"</span>),
        React.createElement(<span class="hljs-string">"input"</span>, &#123; <span class="hljs-attr">placeholder</span>: <span class="hljs-string">"请输入文字"</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实我们是可以看出一点问题的, 那么就是我们的createElement函数的children去收集到的子节点，他既可以是createElement创建的对象,
又可以是一个原始值(<code>Primitive Value</code>)比如<code>Number</code>或者<code>String</code>, 这样就会造成一个小问题, 日后我们在遍历children的值的时候, 都不能放心的去确定children的子元素是不是一个对象, 需要去做逻辑判定<code>if  (Object.getPrototypeOf 子元素) === Object.prototype</code>, 这样很烦, 所以我们最好是在<code>createElement</code>函数里就给他搞定了,
让children中的所有元素不管你给我的是啥, 我存的就是一个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我新建一个createTextNode的方法, 他专门来为我们生成文本节点</span>
<span class="hljs-comment">// 我们知道只有文本节点才可能是原始值吧, 这里你可以好好想一想</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">textValue</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">nodeValue</span>: textValue,
            <span class="hljs-attr">children</span>: []
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 然后我们稍稍改动一下我们的createElement方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        type,
        <span class="hljs-attr">props</span>: &#123;
            ...props,
            <span class="hljs-attr">children</span>: children.map(<span class="hljs-function"><span class="hljs-params">child</span> =></span> <span class="hljs-built_in">Object</span>.getPrototypeOf(child) === <span class="hljs-built_in">Object</span>.prototype ? child : 
                    createTextNode(child))
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们建立一个自己的<code>myOwnReact</code>文件夹, 创建一个<code>createElement.js</code>, <code>render.js</code>和<code>index.js</code>文件夹, 分别把我们代码加进去, 后续我们就会引入我们自己的<code>myOwnReact</code>, 同时因为本身编译JSX是babel协助react去做的一件事情, 所以我们这里不会对babel怎么去编译JSX做过多的描述(其实我们压根不会使用JSX, 我们会假设已经通过了babel的编译变成了<code>createElement</code>函数了)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// myOwnReact/createElement</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">textValue</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">nodeValue</span>: textValue,
            <span class="hljs-attr">children</span>: []
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, props, ...children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        type,
        <span class="hljs-attr">props</span>: &#123;
            ...props,
            <span class="hljs-attr">children</span>: children.map(<span class="hljs-function"><span class="hljs-params">child</span> =></span> <span class="hljs-built_in">Object</span>.getPrototypeOf(child) === <span class="hljs-built_in">Object</span>.prototype ? child : createTextNode(child))
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// myOwnReact/index.js</span>
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> createElement &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./createElement.js"</span>
<span class="hljs-keyword">import</span> createElement <span class="hljs-keyword">from</span> <span class="hljs-string">"./createElement"</span>


<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    createElement
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">render函数</h4>
<p>接下来, 我们就该编写我们的render函数了</p>
<p>其实render函数的作用就是帮助我们将<code>createElement</code>创建的对象渲染成真实dom</p>
<p>在此之前, 我们需要写一个<code>utils.js</code>来为我们提供一些工具方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  /myOwnReact/utils.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkIsTextNode</span>(<span class="hljs-params">node</span>) </span>&#123; <span class="hljs-comment">// 该方法用来检测一个通过createElement创建出来的节点是不是文本节点</span>
  <span class="hljs-keyword">return</span> node.type === <span class="hljs-string">"text"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// /myOwnReact/render.js</span>

<span class="hljs-keyword">import</span> &#123; checkIsTextNode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils.js"</span>;

<span class="hljs-comment">// render方法他接受两个参数:</span>
<span class="hljs-comment">// 1. element: 通过createElement创建的元素对象</span>
<span class="hljs-comment">// 2. container: 真实的dom容器</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>) </span>&#123;
    <span class="hljs-keyword">const</span> isTextNode = checkIsTextNode(element);
    <span class="hljs-comment">// 首先我们要通过根element的type来创建一个真实节点 </span>
    <span class="hljs-comment">// 但是我们需要区分一下节点类型, 如果是text节点的话我们就不要创建element了</span>
    <span class="hljs-keyword">const</span> rootDom = isTextNode ? <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>) : <span class="hljs-built_in">document</span>.createElement(element.type);
    
    <span class="hljs-comment">//  这里我们还是要区分一下文本节点和dom节点, 因为文本节点是没有setAttribute方法的</span>
    <span class="hljs-comment">// 我们需要将文本节点直接给到文本节点的nodeValue</span>
    <span class="hljs-comment">// 当然其实在一开始我们创建文本节点的时候你就可以将nodeValue作为参数传递进去了</span>
    <span class="hljs-comment">// 只不过我们上面传的是空串, 这个看个人喜好了</span>
    <span class="hljs-keyword">if</span> (isTextNode) &#123;
        rootDom.nodeValue = props.nodeValue;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果是dom节点, 我们要讲所有的props添加到该真实rootDom上, 但是除了children</span>
        <span class="hljs-keyword">const</span> &#123; children = [], ...restProps &#125; = element.props;
        <span class="hljs-keyword">const</span> attrs = <span class="hljs-built_in">Object</span>.keys(restProps);
        attrs.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> domElement.setAttribute(k, restProps[k]));

        <span class="hljs-comment">// 递归子元素</span>
        children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> render(child, domElement));
    &#125;
    
    container.appendChild(rootDom)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们的render方法就写完了</p>
<p>同样我们需要在上面的<code>index.js</code>中做一个具名导出</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// /myOwnReact/index.js</span>
...
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./render.js"</span>
<span class="hljs-keyword">import</span> render <span class="hljs-keyword">from</span> <span class="hljs-string">"./render.js"</span>

<span class="hljs-keyword">export</span> &#123;
    ...,
    render
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里, 我们可以创建一个<code>index.html</code>, 然后书写如下代码, 我们可以看看页面中是不是出现了我们想要的结果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Build Ur Own React<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createElement, render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./index.js"</span>

    <span class="hljs-keyword">const</span> element = createElement(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"wrapper"</span> &#125;, 
    createElement(<span class="hljs-string">"span"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"title"</span> &#125;, <span class="hljs-string">"我是标题"</span>), createElement(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"content"</span> &#125;, <span class="hljs-string">"我是内容"</span>));

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"element"</span>, element);

    render(element, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));

  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开<code>live server</code>, 我们可以看到页面中呈现的效果和浏览器的对<code>element</code>的打印结果如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac695c48dd6a48beb015a7de0332ef3a~tplv-k3u1fbpfcp-watermark.image" alt="2021-07-11-10-16-55.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们可以看到, 我们的标签已经成功在html文档中渲染了, 同时浏览控制台也打印出了我们递归创建的节点。</p>
</blockquote>
<h4 data-id="heading-3">Concurrent Mode & Fiber</h4>
<p>我们来探讨一个一个问题: 当上面的<code>render</code>方法开始执行以后, 我们能中断<code>render</code>方法的执行吗？</p>
<p>很显然, 答案是no, 那么这样会造成一个什么问题呢</p>
<blockquote>
<p>一旦我们开始这个"渲染"操作, 在渲染完整个真实的dom树之前我们都不能中断这个渲染. 那如果我们的虚拟dom树特别的庞大, 那么对应的渲染成真实dom树要花的时间就越长, 我们都知道JS是单线程的,
那么这个渲染操作就会一直在主线程中进行, 并阻塞后续任务的进行, 我们假设有一个场景, 我们最开始渲染了一个input输入框, 然后这个时候后续还有一大堆东西需要渲染并且渲染了十多秒, 那这十多秒内,
用户在input框输入了东西以后, 他虽然可以被事件监听线程发现, 但是主线程会甩他吗, 是不会的, 所以这就是问题所在</p>
</blockquote>
<p>解决这个问题, React的思路是这样的:</p>
<ul>
<li>将整个渲染过程分解成n多个小单元</li>
<li>当每一个小单元渲染完毕以后, 我们就看看现在是否有交互啊, 有没有其他需要中断渲染的操作啊, 如果有的话, 那就中断渲染, 如果没有的话就进行下一个单元的渲染</li>
</ul>
<p>我们需要改造一下我们的<code>render.js</code>文件</p>
<p>我们现在在render方法里是直接进行了渲染, 而且一渲染就直接递归把他的所有子节点都跟着渲染了, 这样肯定是不OK的, 根据我们上面的说法, 我们需要将一项庞大的渲染工作拆分成小而独立的UI单元, 这样渲染起来比较轻松</p>
<p>同时在更新<code>render.js</code>这个文件之前, 我建议大家先去看看<code>requestIdleCallback</code>这个函数: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FrequestIdleCallback" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestIdleCallback" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<blockquote>
<p>简单说的话就是这个函数会帮你去计算浏览器栈中当前有没有需要执行的高优先级任务（比如用户的输入和动画响应等）, 我们就可以直接通过这个函数来协助我们完成对用户输入等高优先级操作的响应</p>
</blockquote>
<p>然后我们再来简单说一说Fiber, 我们都知道Vue中有虚拟dom对把, 而React中也有虚拟dom, 只不过他的名字叫做Fiber</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们通过createElement创建的对象还不是一个虚拟dom哦, 他只是一个基本的描述对象</span>

<span class="hljs-comment">// 简单来说fiber就是一种数据结构</span>
<span class="hljs-keyword">const</span> Fiber = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 该fiber节点对应的标签类型</span>
    <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 父级fiber节点</span>
    <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 兄弟fiber节点</span>
    <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 自己fiber节点</span>
    <span class="hljs-attr">dom</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 该fiber节点对应的真实dom元素</span>
    <span class="hljs-attr">props</span>: &#123;&#125;, <span class="hljs-comment">// 该fiber节点的所有属性</span>
    <span class="hljs-attr">effectTag</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 该fiber节点对应的更新状态, 在更新阶段会用到</span>
&#125;

<span class="hljs-comment">// 里面的每个属性都有自己的用途, 随着我们的书写后续你就知道了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; checkIsTextNode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils.js"</span>;


<span class="hljs-keyword">let</span> nextUnitOfWork = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 我们假设这个变量中存储的就是每一次需要渲染的UI单元, 我们通过不断变动这个变量的值来控制本次渲染的究竟是什么</span>

<span class="hljs-comment">// 我们现在知道, render他的任务其实还是渲染一整个dom树, 但是我们要改变一下策略, 我们通过render来开启一项自动工作的调度任务</span>
<span class="hljs-comment">// 该调度任务会源源不断的帮助我们进行dom的渲染, 就像流水线上的一条业务线一样, 但是该调度任务会在没有东西可以渲染的时候停下来</span>
<span class="hljs-comment">// 同时也会在需要停止的时候停下来（什么时候需要停止？ 比如上面我们说的用户高优先级的输入响应操作）</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>) </span>&#123;
    <span class="hljs-comment">// 我们现在把调度开关的开启决断于 nextUnitOfWork有没有值</span>
    <span class="hljs-comment">// 所以我们要开启调度, 那么就给nextUnitOfWork赋值</span>
    nextUnitOfWork = &#123; <span class="hljs-comment">// nextUnitOfWork其实就是一个fiber节点了</span>
        <span class="hljs-attr">type</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">dom</span>: container,
        <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 父级fiber节点</span>
        <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 兄弟fiber节点</span>
        <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 他的子fiber节点</span>
        <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>, <span class="hljs-comment">// 这是在后续更新阶段会使用到的一个fiber标记, placement表示新增节点</span>
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">children</span>: [element]
        &#125;
    &#125;
&#125;


<span class="hljs-comment">// 那么我们势必是需要一个玩意去感知nextUnitOfWork是不是有值了, 来写个workLoop方法</span>
<span class="hljs-comment">// 这个deadline是啥玩意: 他就是requestIdleCallback给我们传的一个参数, 我们等会会用这个参数来</span>
<span class="hljs-comment">// 决定我们是否需要停止下一个单元的渲染</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">deadline</span>) </span>&#123;
    <span class="hljs-keyword">let</span> shouldYield = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 我们是否需要停止渲染的一个flag, false就是不需要, true就是需要停止了</span>
    <span class="hljs-keyword">while</span> (nextUnitOfWork && !shouldYield) &#123;
        <span class="hljs-comment">// 只要当前要处理的工作对象有值 而且 系统没有让我们停下来(shouldYield为false), 那我们就一直</span>
        <span class="hljs-comment">// 执行任务</span>
        <span class="hljs-comment">// performUnitOfWork是我们下面会补的一个函数</span>
        nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
        <span class="hljs-comment">// deadline是一些关于浏览器闲暇情况的一个参数, 它里面有一个方法timeRemaining, 该方法</span>
        <span class="hljs-comment">// 的调用会返回一个毫秒数, 代表浏览器当前闲置的一个剩余的估计时间, 比如当浏览器有任务要过来了, 他就会知道</span>
        <span class="hljs-comment">// 并且他会大概计算一下这个任务过来还要大概多久时间, 所以当这个时间不多的时候, 我们需要把渲染任务停止, 、</span>
        <span class="hljs-comment">// 让浏览器去做他该做的事情</span>
        shouldYield = deadline.timeRemaining() < <span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-comment">// 当停止以后浏览器其实就有空去响应用户的操作了, 但是我们这里还是要记住需要源源不断的开启监听</span>
    requestIdleCallback(workLoop);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDom</span>(<span class="hljs-params">fiber</span>) </span>&#123;
  <span class="hljs-comment">// 我们会根据传递进来的fiber节点, 然后构建出属于该fiber节点的唯一的真实dom</span>
  <span class="hljs-keyword">const</span> isTextNode = checkIsTextNode(fiber);
  <span class="hljs-keyword">const</span> domElement = isTextNode ? <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>) : <span class="hljs-built_in">document</span>.createElement(fiber.type);

  <span class="hljs-comment">// 同理, 如果是文本节点, 我们就直接将nodeValue进行赋值</span>
  <span class="hljs-keyword">if</span> (isTextNode) domElement.nodeValue = fiber.props.nodeValue;
  <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 否则就对props进行赋值</span>
    <span class="hljs-keyword">const</span> &#123; children = [], ...attrs &#125; = fiber.props;

    <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(attrs);

    keys.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> &#123;
      domElement.setAttribute(k, attrs[k]);
    &#125;)

    <span class="hljs-comment">// 注意: 我们这里不处理子元素, 我们只处理他本人</span>
  &#125;
  <span class="hljs-keyword">return</span> domElement;
&#125;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    <span class="hljs-comment">// 这个方法我们要做的事情就几个:</span>

    <span class="hljs-comment">// 1. 根据当前的fiber节点给他创建对应的真实dom节点</span>
    fiber.dom == <span class="hljs-literal">null</span> && (fiber.dom = createDom(fiber))
    <span class="hljs-comment">// 2. 将nextUnitOfWork的dom推入到父级的dom中</span>
    <span class="hljs-keyword">if</span> (fiber.parent) &#123;
        <span class="hljs-comment">// 如果该fiber节点有父级fiber元素, 那我们就可以将该fiber推入到父级节点中去</span>
        fiber.parent.dom.appendChild(fiber.dom)
    &#125;

    <span class="hljs-comment">// 3. 开始构建该fiber的一些兄弟节点, 子节点的关系</span>
    <span class="hljs-keyword">const</span> elements = fiber.props.children;

    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> prevFiber = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 这是我们用来维护整个fiber链表的一个索引入口</span>
    <span class="hljs-comment">// 请注意哈: 这个elements里面装的可全都是通过createElement创建的描述对象哈</span>
    <span class="hljs-keyword">while</span> (index < elements.length) &#123;
        <span class="hljs-keyword">let</span> newFiber = &#123;
            <span class="hljs-attr">type</span>: elements[index].type,
            <span class="hljs-attr">props</span>: elements[index].props,
            <span class="hljs-attr">parent</span>: fiber, <span class="hljs-comment">// 他的父级节点是不是就是此次的fiber节点, 这个仔细屡一下</span>
            <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>
        &#125;

        <span class="hljs-comment">// 然后其实我们本次的fiber节点还没有child属性吧</span>
        <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) fiber.child = newFiber;
        <span class="hljs-keyword">else</span> &#123;
            prevFiber.sibling = newFiber;
        &#125;
         prevFiber = newFiber;
         index ++;
    &#125;

    <span class="hljs-comment">// 4. 我们还需要将下一次调度的nextUnitOfWork返回出去吧, 来保证每次都有新fiber节点可以被渲染</span>
    <span class="hljs-keyword">if</span> (fiber.child) <span class="hljs-keyword">return</span> fiber.child;
    <span class="hljs-keyword">let</span> nextFiber = fiber;
    <span class="hljs-keyword">while</span> (nextFiber) &#123;
    <span class="hljs-keyword">if</span> (nextFiber.sibling) &#123;
        <span class="hljs-keyword">return</span> nextFiber.sibling;
    &#125;
    nextFiber = nextFiber.parent;
    &#125;
&#125;

<span class="hljs-comment">// 注意哦: 这里我们通过requestIdleCallback直接开启调度任务</span>
requestIdleCallback(workLoop); 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">render phase & commit phase</h4>
<blockquote>
<p>不知道大家有没有考虑另外一个问题, 我们现在会将整个ui的渲染拆分成很多个小的UI单元进行逐步渲染, 假设中途用户有一个输入, 我们假设这个输入的JS处理逻辑为10秒, 那么这10秒内UI都将不会继续渲染, 则用户看到的是一个残缺的UI界面, 这完全不是我们想要的, 所以我们需要改变一下我们的方针</p>
</blockquote>
<p>我们现在不一个一个的塞入dom容器了, 我们将整个fiber tree全部构建完毕以后（代表着这个时候没有任何JS逻辑处理了）, 我们再将整个树直接塞入真实dom里(依靠的就是fiber节点中的dom), 我们之前为什么说用户的响应会不及时, 是因为我们在渲染的时候会有非常多的JS逻辑操作, 而我们将dom塞进真实的容器中, 这消耗的时间远没有上面多, 所以我们更希望这样, 那么这里就涉及到两个概念:</p>
<ul>
<li>render phase: 代表我们进行JS逻辑处理和构建整个fiber 树的阶段, 在这个阶段如果有用户响应必须由我们处理(特别是在<strong>更新</strong>的时候), 那么我们将停止目前的工作, 直接去处理优先级更高的用户响应等操作</li>
<li>commit phase: 代表我们整个fiber tree已经构建完毕了, 正在往真实dom容器里塞入, 这个时候我们是不会去管用户的交互和优先级的, 整个过程不可中断</li>
</ul>
<p>那么我们就又得改改我们的<code>render.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 首先我们现在的每一次nextUnitOfWork都是会不断变化的, 所以我们压根拿不到根节点</span>
<span class="hljs-comment">// 而在render中对nextUnitOfWork的赋值一定是根节点</span>
...
<span class="hljs-keyword">let</span> nextUnitOfWork = <span class="hljs-literal">null</span>;
<span class="hljs-comment">// 我们再多加一个变量</span>
<span class="hljs-keyword">let</span> wipRoot = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 代表整个fiber tree的根节点的引用, 因为我们知道要保存一棵树的引用保存他的根节点就OK了</span>

...

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>) </span>&#123;
    <span class="hljs-comment">// 我们需要更新一下render 方法</span>
    wipRoot = &#123;
        <span class="hljs-attr">dom</span>: container,
        <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">children</span>: [element],
        &#125;,
        <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-literal">null</span>
    &#125;

    nextUnitOfWork = wipRoot;
&#125;
...

<span class="hljs-comment">// 我们的workLoop方法里我们可以用来提交整个fiber tree</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">deadline</span>) </span>&#123;
    ...

    <span class="hljs-comment">// 为什么workLoop里是可以的哈, 主要是因为我们知道, 每一次nextUnitOfWork的值的变换其实都是在workLoop里进行处理的</span>
    <span class="hljs-comment">// 所以我们只能在workLoop里去感知现在的fiber tree是不是已经构建完了</span>
    
    <span class="hljs-comment">// 我们直接在while 循环的下面进行判断</span>
    <span class="hljs-comment">// 如果这个时候我们nextUtilOfWork为null了, 代表整个fiber tree已经构建完毕了, 所以我们要做的就是直接进入commit phase</span>
    <span class="hljs-keyword">if</span> (!nextUnitOfWork && wipRoot) &#123;
        <span class="hljs-comment">// 为啥一定得是nextUnitOfWork为null才行哈, 主要是因为就算不为空也可能会走到这里来</span>
        <span class="hljs-comment">// 因为中断渲染的时候, 这个时候nextUnitOfWork一定还有值, 但是呢 他又一定会走进这个流程</span>
        <span class="hljs-comment">// 我们始终只希望一点, 就是整个fiber 树确定构建完了 我们才会进行提交</span>
        commitRoot();
    &#125;

     <span class="hljs-comment">// 当停止以后浏览器其实就有空去响应用户的操作了, 但是我们这里还是要记住需要源源不断的开启监听</span>
    requestIdleCallback(workLoop);

    ...
&#125;

<span class="hljs-comment">// 同时新增以下两个方法, 这两个方法都比较简单, 我就不说了哈</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
    commitWork(wipRoot.child); <span class="hljs-comment">// 因为wipRoot一定是container这个dom嘛, 所以我们直接从子元素开始提交</span>
    wipRoot = <span class="hljs-literal">null</span>; 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!fiber) <span class="hljs-keyword">return</span>;
    fiber.parent.dom.appendChild(fiber.dom);
    commitWork(fiber.child);
    commitWork(fiber.sibling);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Reconciliation</h4>
<p>大家一定听说过<code>Vue</code>的一个<code>diff</code>算法吧, 同样作为MVVM框架, <code>React</code>也具备自己内部比对虚拟dom的一个算法, 他叫做<code>Reconciliation</code></p>
<p>主要的这个流程就是我们需要在每一次更新的时候去对上一次保存的虚拟dom树进行一个比较, 从而决定我们是有哪些节点更新, 哪些节点被删除, 又有哪些新增的节点</p>
<p>我们再次对我们的<code>render.js</code>文件下手了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 首先我们在全局加一个currentRoot用来保存之前的fiber tree, 同时加一个deleteGroup来保存本次比对需要删除的dom元素</span>
...
<span class="hljs-keyword">let</span> nextUnitOfWork = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> wipRoot = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> currentRoot = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 我们要保存的本次的整个fiber Tree</span>
<span class="hljs-keyword">let</span> deleteGroup = []; <span class="hljs-comment">// 被删除的fiber集合</span>


<span class="hljs-comment">// 然后我们需要在commitRoot里加一些代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 因为这里我们是会把wipRoot清空的, 所以在清空之前我们一定要保存一下引用</span>
    ...
    currentRoot = wipRoot;
    wipRoot = <span class="hljs-literal">null</span>;
    ...
&#125;
...


<span class="hljs-comment">// 然后就是我们要更新一下我们performUnitOfWork函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    ...
    <span class="hljs-comment">// 2. 开始构建该fiber的一些兄弟节点, 子节点的关系</span>
    <span class="hljs-keyword">const</span> elements = fiber.props.children;

    <span class="hljs-comment">// 我们之前在这里写了一大块处理子节点fiber的东西, 我们都不要了, 直接拎出去</span>
    <span class="hljs-comment">// 代码看着怪恶心的</span>
    reconciliationChildren(fiber, elements);
    
    ...
&#125;


<span class="hljs-comment">// 然后编写我们的reconciliationChildren方法</span>
<span class="hljs-comment">// 我们定义一个对子元素进行diff比较的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconciliateChildren</span>(<span class="hljs-params">wipRoot, elements</span>) </span>&#123;
    
    <span class="hljs-comment">// 1. 首先我们拿到最近保存的一个虚拟dom树</span>
    <span class="hljs-keyword">const</span> oldFiber = wipRoot.alternate && wipRoot.alternate.child;



    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> prevFiber = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 这是我们用来维护整个fiber链表的一个索引入口</span>
    <span class="hljs-comment">// 请注意哈: 这个elements里面装的可全都是通过createElement创建的描述对象哈</span>

    <span class="hljs-comment">// 因为我们这里要进行逐层比对, 而且会对oldFiber进行多次值的修改, 所以我们并不能够以</span>
    <span class="hljs-comment">// index < elements.length为结束手段, 因为如果elements.length没有了</span>
    <span class="hljs-comment">// 但是oldFiber还有 那其实代表的是最新的fiber节点里做了删除操作</span>
    <span class="hljs-keyword">while</span> (index < elements.length || oldFiber != <span class="hljs-literal">null</span>) &#123;

        <span class="hljs-keyword">const</span> el = elements[index];

        <span class="hljs-comment">// 如果本次oldFiber和新的el类型相同, 我们就要留存一部分信息以节约性能</span>
        <span class="hljs-keyword">const</span> isSameType = el && oldFiber && el.type === oldFiber.type; 

        <span class="hljs-keyword">let</span> newFiber = <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">if</span> (isSameType) &#123;
            <span class="hljs-comment">// 代表是更新阶段</span>
            newFiber = &#123;
                <span class="hljs-attr">type</span>: oldFiber.type,
                <span class="hljs-attr">parent</span>: wipRoot,
                <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">props</span>: el.props,
                <span class="hljs-attr">alternate</span>: oldFiber,
                <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"update"</span>,
                <span class="hljs-attr">dom</span>: oldFiber.dom
            &#125;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldFiber && !isSameType) &#123;
            <span class="hljs-comment">// 代表做了删除</span>
            oldFiber.effectTag = <span class="hljs-string">"delete"</span>; 
            deleteGroup.push(oldFiber); <span class="hljs-comment">// 往本次被删除的集合中添加一个oldFiber</span>

        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el && !isSameType) &#123;
            <span class="hljs-comment">// 代表做了新增</span>
            newFiber = &#123;
                <span class="hljs-attr">type</span>: elements[index].type,
                <span class="hljs-attr">props</span>: elements[index].props,
                <span class="hljs-attr">parent</span>: wipRoot, <span class="hljs-comment">// 他的父级节点是不是就是此次的fiber节点, 这个仔细屡一下</span>
                <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>,
                <span class="hljs-attr">dom</span>: <span class="hljs-literal">null</span>
            &#125;
        &#125;
        <span class="hljs-comment">// 然后其实我们本次的fiber节点还没有child属性吧</span>
        <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) wipRoot.child = newFiber;
        <span class="hljs-keyword">else</span> &#123;
            prevFiber.sibling = newFiber;
        &#125;
        prevFiber = newFiber;
        index ++;
    &#125;
&#125;

<span class="hljs-comment">// 有了上面的reconciliationChildren 方法来比对虚拟dom以后, 其实我们在commitWork的时候就需要区分一下状态了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!fiber) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"placement"</span>) &#123;
        <span class="hljs-comment">// 新增</span>
        fiber.parent && fiber.parent.dom.appendChild(fiber.dom);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"update"</span>) &#123;
        updateDom(dom, fiber.alternate.props, fiber.props, );
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"delete"</span>) &#123;
        fiber.parent.dom.removeChild(fiber.dom);
    &#125;
    commitWork(fiber.child);
    commitWork(fiber.sibling);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDom</span>(<span class="hljs-params">dom, prevProps, nextProps</span>) </span>&#123;
    <span class="hljs-comment">// 1. 首先我要看的是有没有被移除的属性</span>
    <span class="hljs-keyword">const</span> withoutChildrenPrevProps = <span class="hljs-built_in">Object</span>.keys(prevProps).filter(<span class="hljs-function"><span class="hljs-params">k</span> =></span> k !== <span class="hljs-string">"children"</span>);
    <span class="hljs-keyword">const</span> withoutChildrenNextProps = <span class="hljs-built_in">Object</span>.keys(nextProps).filter(<span class="hljs-function"><span class="hljs-params">k</span> =></span> k !== <span class="hljs-string">"children"</span>);

    <span class="hljs-comment">// 我要做的就是把旧的属性全部遍历一遍, 如果旧的有 新的直接没有了就remove掉</span>
    <span class="hljs-comment">// 否则就是更新掉</span>
    withoutChildrenPrevProps.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (k.startsWith(<span class="hljs-string">"on"</span>)) &#123;
            <span class="hljs-comment">// 这代表是事件啊, 事件得悠着点</span>
            <span class="hljs-keyword">const</span> legalEventName = k.toLowerCase().substring(<span class="hljs-number">2</span>); <span class="hljs-comment">// 我们知道React里是以onClick这种来标注事件的, 我们只需要小写的click</span>
            <span class="hljs-comment">// 事件其实也分移除还是更新</span>
            <span class="hljs-keyword">if</span>(!(k <span class="hljs-keyword">in</span> withoutChildrenNextProps)) &#123;
                <span class="hljs-comment">// 代表都没有了 我还留着干嘛啊</span>
                dom.removeEventListener(legalEventName, prevProps[k]);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 直接绑定</span>
                dom.addEventListener(legalEventName, nextProps[k]);
            &#125;


        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!(k <span class="hljs-keyword">in</span> withoutChildrenNextProps)) &#123;
            <span class="hljs-comment">// 如果在新的属性里都没有这个key了, 直接拜拜</span>
            dom[k] = <span class="hljs-string">""</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 到这里就一定是更新阶段, 全部以新的为主, 当然你也可以进行深层优化比较</span>
            dom[k] = nextProps[k];
        &#125;
    &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止, 我们的reconciliation阶段也完成了</p>
<p>我们最后的render.js文件代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; checkIsTextNode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils.js"</span>;


<span class="hljs-keyword">let</span> nextUnitOfWork = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 我们假设这个变量中存储的就是每一次需要渲染的UI单元, 我们通过不断变动这个变量的值来控制本次渲染的究竟是什么</span>
<span class="hljs-keyword">let</span> wipRoot = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 代表我最后要提交的整个fiber tree</span>
<span class="hljs-keyword">let</span> currentRoot = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 我们要保存的本次的整个fiber Tree</span>
<span class="hljs-keyword">let</span> deleteGroup = []; <span class="hljs-comment">// 被删除的fiber集合</span>

<span class="hljs-comment">// 我们现在知道, render他的任务其实还是渲染一整个dom树, 但是我们要改变一下策略, 我们通过render来开启一项自动工作的调度任务</span>
<span class="hljs-comment">// 该调度任务会源源不断的帮助我们进行dom的渲染, 就像流水线上的一条业务线一样, 但是该调度任务会在没有东西可以渲染的时候停下来</span>
<span class="hljs-comment">// 同时也会在需要停止的时候停下来（什么时候需要停止？ 比如上面我们说的用户高优先级的输入响应操作）</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">element, container</span>) </span>&#123;
    <span class="hljs-comment">// 我们现在把调度开关的开启决断于 nextUnitOfWork有没有值</span>
    <span class="hljs-comment">// 所以我们要开启调度, 那么就给nextUnitOfWork赋值</span>
    wipRoot = &#123; <span class="hljs-comment">// nextUnitOfWork其实就是一个fiber节点了</span>
        <span class="hljs-attr">type</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">dom</span>: container,
        <span class="hljs-attr">parent</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 父级fiber节点</span>
        <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 兄弟fiber节点</span>
        <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 他的子fiber节点</span>
        <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>, <span class="hljs-comment">// 这是在后续更新阶段会使用到的一个fiber标记, placement表示新增节点</span>
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">children</span>: [element]
        &#125;,
        <span class="hljs-attr">alternate</span>: currentRoot, <span class="hljs-comment">// 我们在根节点处也留存一下我们上一次的fiber树</span>
    &#125;

    deleteGroup = []; <span class="hljs-comment">// 每次render我们都应该置空被删除的fiber数组</span>

    nextUnitOfWork = wipRoot;
&#125;


<span class="hljs-comment">// 那么我们势必是需要一个玩意去感知nextUnitOfWork是不是有值了, 来写个workLoop方法</span>
<span class="hljs-comment">// 这个deadline是啥玩意: 他就是requestIdleCallback给我们传的一个参数, 我们等会会用这个参数来</span>
<span class="hljs-comment">// 决定我们是否需要停止下一个单元的渲染</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">deadline</span>) </span>&#123;

    <span class="hljs-keyword">let</span> shouldYield = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 我们是否需要停止渲染的一个flag, false就是不需要, true就是需要停止了</span>
    <span class="hljs-keyword">while</span> (nextUnitOfWork && !shouldYield) &#123;
        <span class="hljs-comment">// 只要当前要处理的工作对象有值 而且 系统没有让我们停下来(shouldYield为false), 那我们就一直</span>
        <span class="hljs-comment">// 执行任务</span>
        <span class="hljs-comment">// performUnitOfWork是我们下面会补的一个函数</span>
        nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
        <span class="hljs-comment">// deadline是一些关于浏览器闲暇情况的一个参数, 它里面有一个方法timeRemaining, 该方法</span>
        <span class="hljs-comment">// 的调用会返回一个毫秒数, 代表浏览器当前闲置的一个剩余的估计时间, 比如当浏览器有任务要过来了, 他就会知道</span>
        <span class="hljs-comment">// 并且他会大概计算一下这个任务过来还要大概多久时间, 所以当这个时间不多的时候, 我们需要把渲染任务停止, 、</span>
        <span class="hljs-comment">// 让浏览器去做他该做的事情</span>
        shouldYield = deadline.timeRemaining() < <span class="hljs-number">1</span>;
    &#125;

    <span class="hljs-comment">// 如果这个时候我们nextUtilOfWork为null了, 代表整个fiber tree已经构建完毕了, 所以我们要做的就是直接进入commit phase</span>
    <span class="hljs-keyword">if</span> (!nextUnitOfWork && wipRoot) &#123;
        <span class="hljs-comment">// 为啥一定得是nextUnitOfWork为null才行哈, 主要是因为就算不为空也可能会走到这里来</span>
        <span class="hljs-comment">// 因为中断渲染的时候, 这个时候nextUnitOfWork一定还有值, 但是呢 他又一定会走进这个流程</span>
        <span class="hljs-comment">// 我们始终只希望一点, 就是整个fiber 树确定构建完了 我们才会进行提交</span>
        commitRoot();
    &#125;

    <span class="hljs-comment">// 当停止以后浏览器其实就有空去响应用户的操作了, 但是我们这里还是要记住需要源源不断的开启监听</span>
    requestIdleCallback(workLoop);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
    deleteGroup.forEach(commitWork); <span class="hljs-comment">// 看看有没有被删除东西</span>
    commitWork(wipRoot.child); <span class="hljs-comment">// 因为wipRoot一定是container这个dom嘛, 所以我们直接从子元素开始提交</span>

    <span class="hljs-comment">// 跑不掉的一定是在commit阶段对本次的一个虚拟dom树进行一个留存</span>
    currentRoot = wipRoot;

    wipRoot = <span class="hljs-literal">null</span>; 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!fiber) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"placement"</span>) &#123;
        <span class="hljs-comment">// 新增</span>
        fiber.parent && fiber.parent.dom.appendChild(fiber.dom);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"update"</span>) &#123;
        updateDom(dom, fiber.alternate.props, fiber.props, );
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (fiber.effectTag === <span class="hljs-string">"delete"</span>) &#123;
        fiber.parent.dom.removeChild(fiber.dom);
    &#125;
    commitWork(fiber.child);
    commitWork(fiber.sibling);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDom</span>(<span class="hljs-params">dom, prevProps, nextProps</span>) </span>&#123;
    <span class="hljs-comment">// 1. 首先我要看的是有没有被移除的属性</span>
    <span class="hljs-keyword">const</span> withoutChildrenPrevProps = <span class="hljs-built_in">Object</span>.keys(prevProps).filter(<span class="hljs-function"><span class="hljs-params">k</span> =></span> k !== <span class="hljs-string">"children"</span>);
    <span class="hljs-keyword">const</span> withoutChildrenNextProps = <span class="hljs-built_in">Object</span>.keys(nextProps).filter(<span class="hljs-function"><span class="hljs-params">k</span> =></span> k !== <span class="hljs-string">"children"</span>);

    <span class="hljs-comment">// 我要做的就是把旧的属性全部遍历一遍, 如果旧的有 新的直接没有了就remove掉</span>
    <span class="hljs-comment">// 否则就是更新掉</span>
    withoutChildrenPrevProps.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (k.startsWith(<span class="hljs-string">"on"</span>)) &#123;
            <span class="hljs-comment">// 这代表是事件啊, 事件得悠着点</span>
            <span class="hljs-keyword">const</span> legalEventName = k.toLowerCase().substring(<span class="hljs-number">2</span>); <span class="hljs-comment">// 我们知道React里是以onClick这种来标注事件的, 我们只需要小写的click</span>
            <span class="hljs-comment">// 事件其实也分移除还是更新</span>
            <span class="hljs-keyword">if</span>(!(k <span class="hljs-keyword">in</span> withoutChildrenNextProps)) &#123;
                <span class="hljs-comment">// 代表都没有了 我还留着干嘛啊</span>
                dom.removeEventListener(legalEventName, prevProps[k]);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 直接绑定</span>
                dom.addEventListener(legalEventName, nextProps[k]);
            &#125;


        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!(k <span class="hljs-keyword">in</span> withoutChildrenNextProps)) &#123;
            <span class="hljs-comment">// 如果在新的属性里都没有这个key了, 直接拜拜</span>
            dom[k] = <span class="hljs-string">""</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 到这里就一定是更新阶段, 全部以新的为主, 当然你也可以进行深层优化比较</span>
            dom[k] = nextProps[k];
        &#125;
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDom</span>(<span class="hljs-params">fiber</span>) </span>&#123;
  <span class="hljs-comment">// 我们会根据传递进来的fiber节点, 然后构建出属于该fiber节点的唯一的真实dom</span>
  <span class="hljs-keyword">const</span> isTextNode = checkIsTextNode(fiber);
  <span class="hljs-keyword">const</span> domElement = isTextNode ? <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">""</span>) : <span class="hljs-built_in">document</span>.createElement(fiber.type);

  <span class="hljs-comment">// 同理, 如果是文本节点, 我们就直接将nodeValue进行赋值</span>
  <span class="hljs-keyword">if</span> (isTextNode) domElement.nodeValue = fiber.props.nodeValue;
  <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 否则就对props进行赋值</span>
    <span class="hljs-keyword">const</span> &#123; children = [], ...attrs &#125; = fiber.props;

    <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(attrs);

    keys.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> &#123;
      domElement.setAttribute(k, attrs[k]);
    &#125;)

    <span class="hljs-comment">// 注意: 我们这里不处理子元素, 我们只处理他本人</span>
  &#125;
  <span class="hljs-keyword">return</span> domElement;
&#125;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">fiber</span>) </span>&#123;
    <span class="hljs-comment">// 这个方法我们要做的事情就几个:</span>

    <span class="hljs-comment">// 1. 根据当前的fiber节点给他创建对应的真实dom节点</span>
    fiber.dom == <span class="hljs-literal">null</span> && (fiber.dom = createDom(fiber))

    <span class="hljs-comment">// 2. 开始构建该fiber的一些兄弟节点, 子节点的关系</span>
    <span class="hljs-keyword">const</span> elements = fiber.props.children;

    reconciliateChildren(fiber, elements);

    <span class="hljs-comment">// 3. 我们还需要将下一次调度的nextUnitOfWork返回出去吧, 来保证每次都有新fiber节点可以被渲染</span>
    <span class="hljs-keyword">if</span> (fiber.child) <span class="hljs-keyword">return</span> fiber.child;
    <span class="hljs-keyword">let</span> nextFiber = fiber;
    <span class="hljs-keyword">while</span> (nextFiber) &#123;
        <span class="hljs-keyword">if</span> (nextFiber.sibling) &#123;
            <span class="hljs-keyword">return</span> nextFiber.sibling;
        &#125;
        nextFiber = nextFiber.parent;
    &#125;
&#125;

<span class="hljs-comment">// 我们定义一个对子元素进行diff比较的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconciliateChildren</span>(<span class="hljs-params">wipRoot, elements</span>) </span>&#123;
    
    <span class="hljs-comment">// 1. 首先我们拿到最近保存的一个虚拟dom树</span>
    <span class="hljs-keyword">const</span> oldFiber = wipRoot.alternate && wipRoot.alternate.child;



    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> prevFiber = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 这是我们用来维护整个fiber链表的一个索引入口</span>
    <span class="hljs-comment">// 请注意哈: 这个elements里面装的可全都是通过createElement创建的描述对象哈</span>

    <span class="hljs-comment">// 因为我们这里要进行逐层比对, 而且会对oldFiber进行多次值的修改, 所以我们并不能够以</span>
    <span class="hljs-comment">// index < elements.length为结束手段, 因为如果elements.length没有了</span>
    <span class="hljs-comment">// 但是oldFiber还有 那其实代表的是最新的fiber节点里做了删除操作</span>
    <span class="hljs-keyword">while</span> (index < elements.length || oldFiber != <span class="hljs-literal">null</span>) &#123;

        <span class="hljs-keyword">const</span> el = elements[index];

        <span class="hljs-comment">// 如果本次oldFiber和新的el类型相同, 我们就要留存一部分信息以节约性能</span>
        <span class="hljs-keyword">const</span> isSameType = el && oldFiber && el.type === oldFiber.type; 

        <span class="hljs-keyword">let</span> newFiber = <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">if</span> (isSameType) &#123;
            <span class="hljs-comment">// 代表是更新阶段</span>
            newFiber = &#123;
                <span class="hljs-attr">type</span>: oldFiber.type,
                <span class="hljs-attr">parent</span>: wipRoot,
                <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">props</span>: el.props,
                <span class="hljs-attr">alternate</span>: oldFiber,
                <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"update"</span>,
                <span class="hljs-attr">dom</span>: oldFiber.dom
            &#125;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldFiber && !isSameType) &#123;
            <span class="hljs-comment">// 代表做了删除</span>
            oldFiber.effectTag = <span class="hljs-string">"delete"</span>; 
            deleteGroup.push(oldFiber); <span class="hljs-comment">// 往本次被删除的集合中添加一个oldFiber</span>

        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el && !isSameType) &#123;
            <span class="hljs-comment">// 代表做了新增</span>
            newFiber = &#123;
                <span class="hljs-attr">type</span>: elements[index].type,
                <span class="hljs-attr">props</span>: elements[index].props,
                <span class="hljs-attr">parent</span>: wipRoot, <span class="hljs-comment">// 他的父级节点是不是就是此次的fiber节点, 这个仔细屡一下</span>
                <span class="hljs-attr">child</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">sibling</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"placement"</span>,
                <span class="hljs-attr">dom</span>: <span class="hljs-literal">null</span>
            &#125;
        &#125;
        <span class="hljs-comment">// 然后其实我们本次的fiber节点还没有child属性吧</span>
        <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) wipRoot.child = newFiber;
        <span class="hljs-keyword">else</span> &#123;
            prevFiber.sibling = newFiber;
        &#125;
         prevFiber = newFiber;
         index ++;
    &#125;
&#125;

<span class="hljs-comment">// 注意哦: 这里我们通过requestIdleCallback直接开启调度任务</span>
requestIdleCallback(workLoop); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok, 你基本已经实现了一个小的react的生态, 从<code>createElement</code>到<code>render</code> 到<code>fiber</code>, 再到<code>render phase & commit phase</code>, 再到<code>reconciliation</code> 你可以思考一下函数组件和类组件应该要怎么处理, 下一次我会出一篇博客专门聊聊他们, 希望本篇博客能够对你有所帮助喽</p></div>  
</div>
            