
---
title: 'Angular 和 React 背后的秘密(上)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a0639ae3fcc4dd2a638276039cde746~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 00:53:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a0639ae3fcc4dd2a638276039cde746~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 11 天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=NewsSidebar&utm_source=20210609" target="_blank">更文挑战</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a0639ae3fcc4dd2a638276039cde746~tplv-k3u1fbpfcp-zoom-1.image" alt="封面" loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天我们不会讨论 Angular 和 React 谁是老大问题，而是讨论在 React 和 Angular 框架中使用到共同点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/907bfea290964c0da0a0e873835bfac1~tplv-k3u1fbpfcp-zoom-1.image" alt="react_vs_angular.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些 Angular 和 React 都有共同点分别是</p>
<ul>
<li>Monomorphism</li>
<li>Bit fields</li>
<li>Bloom filters</li>
</ul>
<p>分三次分享我们把他们一一给您解释清楚。</p>
<h2 data-id="heading-0">Monomorphism</h2>
<blockquote>
<p>we use one type for all <strong>View nodes</strong> so that property access in loops stay <strong>monomorphic</strong>
Misko Hevery, technical lead of Angular</p>
</blockquote>
<blockquote>
<p><strong>Fiber node</strong> ... shares the same <strong>hidden class</strong>.Never add fields outside of construction in ReactFiber
sebastian Markbage technical lead of React</p>
</blockquote>
<p>调试代码时，偶尔会查看一下框架中实现原理，在 Angular 和 React 源码看到了他们框架技术负责人的注释。这些注释中不约而同谈到隐藏类(hidden class)，这种框架内部的数据结构在 Angular 和 React 分别叫做 Fiber node 和 View nodes。确保这些内部的数据结构共享同一个隐藏类，也就是说使属性访问成为单态的(monomorphic)。他们为什么要这么做，这么做有什么好处是今天我们要讨论的内容。</p>
<p>在 Angular 中 View nodes 和数据结构来表示模板。定义了呈现 DOM 所需的元数据，还指定了 DOM 的哪个部分需要更新。</p>
<p>同样在 React 中定义了组件，定义了模板时， React 也使用了 fibre nodes。这是新的React fibre 16 架构。</p>
<pre><code class="copyable">@Component(&#123;
    template:`
    <h1>&#123;&#123;title&#125;&#125; tuts </h1>
    <h2>author &#123;&#123;name&#125;&#125; </h2>
    `
&#125;)

export class AppComponent &#123;
    title = 'optimized code in js';
    name='zidea'
&#125;

bindings:&#123;
    text:'optimized code in js'
&#125;

bindings:&#123;
    text:"zidea"
&#125;

class App extends Component&#123;
    state = &#123;
        title = 'optimized code in js',
        name='zidea'
    &#125;;

    render()&#123;
        return(
            [
                <h1>&#123;&#123;title&#125;&#125; tuts </h1>
                <h2>author &#123;&#123;name&#125;&#125; </h2>
            ]
        )
    &#125;
&#125;

props:&#123;
    children:"optimized code in js"
&#125;

props:&#123;
    children:"zidea"
&#125;

function updateNode(node,...)&#123;
    let value = node.property;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Fibre nodes 和 view nodes 分别在 Angular 和 React 都是用来表示框架中模板，都是用于介于 DOM 元素和模板组件之间。接下来看看这两种数据结构有什么共同点，他们都在框架处理更新时，会被经常使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf0cf9b86b54c60b289c4df82516084~tplv-k3u1fbpfcp-zoom-1.image" alt="Chrome-V8-v65.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fb91337aad46f2bc916397f1857708~tplv-k3u1fbpfcp-zoom-1.image" alt="组件" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c03954e7ee462584bbf784eccadb10~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如此做的原因何在，也就是为什么做的这么复杂的，答案是因为一些叫做shape(形状)或 hidden class （隐藏类）的东西。这正是 Sebastian 在注释中提到的隐藏类。每天在写 javascript 时，javascript 对象(object) 在虚拟机内部表现为 shape 对象,因此 shape 定义了用于描述对象的属性，如何分配内存(layout).例如 用于在内存中查找的 offset(偏移)值。可能你会问为什么我们需要 shape，为什么不直接将这些属性定义对象上 。其实这样做是有好处的，可以节省内存空间，我们可能有两对象(object),甚至更多，成千上万的对象。</p>
<pre><code class="copyable">let a  = &#123;x:5,y:6&#125;;
let b  = &#123;x:7,y:8&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69397baa51c74488abdf852466b43c96~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为这些对象都具有相同结构(布局）我们就可以把这些共性东西抽取出来用 shape 来表示。这也就是说明即使我们有很多对象，我们也只是描述一次即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38c0c5ce5c7f40dd9397f22398467bd8~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">let a  = &#123;x:5,y:6&#125;;
let b  = &#123;x:7,y:8&#125;;
b.w = 9
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要对象 b 进行扩展属性 w 赋值 9，我们就需要引入新的 shape 。我们无法将 w 引入到原有 shape，因为 a 对象还依赖于 shape 而 a 并没有新增属性。所以需要引入新的 shape 并且更新他们之间关系。</p>
<pre><code class="copyable">let a  = &#123;x:5,y:6&#125;;
let b  = &#123;x:7,y:8&#125;;
b.w = 9
b.z = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d1d12958ddb47bc92ed6a337664d7cd~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以想象不断为对象添加许属性，并修改对象 shape (形状)，则可能会有一个具有数百个中间过渡的 shape(形状)。这样每次访问对象某个属性时，虚拟机都必须经历所有这些过程，以找出描述该属性的布局和内存的形状来检索该信息。所以 V8 使用的一种技术是使这个过程更快。.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30eeebc925ba40b198ffe4dbfb603850~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6485cf7c2924a5199f1a19a3f52e523~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个 JavaScript 函数在内部都表示为名为 closure 的对象。这是虚拟机缓存有关函数的一些信息的地方，这些对象用于向该函数添加参数，以及其他信息。。这是虚拟机将缓存某些信息的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getX</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-keyword">return</span> o.x
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面通过以例子来介绍其如何运行的。假设调用 <code>getX </code>函数，并传入一个具有 x 属性的对象。虚拟机将计算出这个对象的 shape (形状)，虚拟机可以缓存对象的 shape (形状)，随后当访问这个对象的 x 属性，可以记录下 offset (偏移量)，当下次接受相同 shape 的对象来执行函数时，虚拟机只需比较 shape(形状)，如果匹配，就不再需要计算出对象 shape(形状)。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de170a41bf174e0c84eb5a0e95c29144~tplv-k3u1fbpfcp-zoom-1.image" alt="图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以从缓存中获取 offset (偏移量)值，来解析内存中的值。还定义了函数的状态，状态可以有三种类型：单态、单态属性访问和多态。在这种情况下，是单态的，是单态的表示只具有一种形状。多态性是指一个函数被调用对象类型每一次并不相同，而 megamorphic 是指当输入不同 shape (形状)的对象作为参数时，通常操作四种类型的 shape 形状。</p>
<p>对象输入给一个函数，以使 state (状态)保持单态是很重要的。单态属性访问的速度可以比megamorphic 快 100 倍。</p>
<p>如果考虑到在每一个更新检测周期中，每秒可能发生几百次的10000 次访问，可以想象访问单态属性对速度的影响会有多大。所以要求对象使用相同的 shape (形状)，对 fibre和view nodes 使用相同的隐藏类，为了是确保属性访问是单态的。你可以有 HTML 元素，子对象，如果遵循面向对象的编程原则，会为不同的元素创建不同的类。这些框架实际上将所有内容合并为一个数据结构、一个类好处可想而知。</p>

























<table><thead><tr><th>Fiber node(react)</th><th>Template element</th><th>View node(Angular)</th></tr></thead><tbody><tr><td>HostComponent</td><td>HTMLElementNode</td><td>TypeElement</td></tr><tr><td>HostText</td><td>HTMLTextNode</td><td>TypeText</td></tr><tr><td>FunctionComponent, \nClassComponent</td><td>Component</td><td>Component</td></tr></tbody></table>
<p>最后希望大家关注我们微信公众号</p></div>  
</div>
            