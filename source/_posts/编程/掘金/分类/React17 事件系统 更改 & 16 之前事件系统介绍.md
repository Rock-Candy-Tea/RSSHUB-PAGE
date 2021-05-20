
---
title: 'React17 事件系统 更改 & 16 之前事件系统介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d6b9d7d7f73431b84fca6a2e168ceca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:34:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d6b9d7d7f73431b84fca6a2e168ceca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一. Breaking change</h4>
<h4 data-id="heading-1">1. 事件委托不再挂到 document 上</h4>
   <p>之前多版本并存的主要问题在于React 事件系统默认的委托机制，出于性能考虑，React 只会给document挂上事件监听，DOM 事件触发后冒泡到document，React 找到对应的组件，造一个 React 事件（SyntheticEvent）出来，并按组件树模拟一遍事件冒泡（此时原生 DOM 事件早已冒出document了）。<br>
    因此，不同版本的 React 组件嵌套使用时，e.stopPropagation()无法正常工作（两个不同版本的事件系统是独立的，都到document已经太晚了<br>
    (If a nested tree has stopped propagation of an event, the outer tree would still receive it).<br>   </p><p>
为了解决这个问题，React 17 不再往document上挂事件委托，而是挂到 DOM 容器上：
</p><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d6b9d7d7f73431b84fca6a2e168ceca~tplv-k3u1fbpfcp-watermark.image" alt="compare.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>react 17 delegation</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rootNode = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);
<span class="hljs-comment">// 以为 render 为例</span>
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, rootNode);
<span class="hljs-comment">// Portals 也一样</span>
<span class="hljs-comment">// ReactDOM.createPortal(<App />, rootNode)</span>
<span class="hljs-comment">// React 16 事件委托（挂到 document 上）</span>
<span class="hljs-built_in">document</span>.addEventListener()
<span class="hljs-comment">// React 17 事件委托（挂到 DOM container 上）</span>
rootNode.addEventListener()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2"><strong>二. React 16 事件系统</strong></h4>
<h5 data-id="heading-3">1. React事件系统</h5>
<p>1-1. React 基于 Virtual DOM 实现了一个SyntheticEvent（合成事件）层，我们所定义的事件处理器会接收到一个SyntheticEvent对象的实例，同样支持事件的冒泡机制，我们可以使用stopPropagation()和preventDefault()来中断它。</p>
<p>1-2. 所有事件都自动绑定到最外层上（document）</p>
<h5 data-id="heading-4">2. 合成事件绑定机制</h5>
<p>在 React 底层，主要对合成事件做了两件事：事件委派和自动绑定。</p>
<h6 data-id="heading-5">2.1 事件委派 <br></h6>
<p>React并不会把事件处理函数直接绑定到真实的节点上，而是把所有事件绑定到结构的最外层，使用一个统一的事件监听器，这个事件监听器上维持了一个映射来保存所有组件内部的事件监听和处理函数。</p>
<p>当组件挂载或卸载时，只是在这个统一的事件监听器上插入或删除一些对象；当事件发生时，首先被这个统一的事件监听器处理，然后在映射里找到真正的事件处理函数并调用。 <br></p>
<p>这样做简化了事件处理和回收机制，效率也有很大提升。</p>
<h6 data-id="heading-6">2.2 自动绑定<br></h6>
<p>在React 组件中，每个方法的上下文都会指向该组件的实例，即自动绑定this为当前组件。而且 React 还会对这种引用进行缓存，以达到 CPU 和内存的最优化。</p>
<h5 data-id="heading-7">3. 在React中使用原生事件</h5>
<p>React 提供了完备的生命周期方法，其中componentDidMount会在组件已经完成安装并且在浏览器中存在真实的 DOM 后调用，此时我们就可以完成原生事件的绑定。
但是React不会自动管理原生事件，所以需要你在卸载组件的时候注销掉原生事件。</p>
<h5 data-id="heading-8">4. 合成事件与原生事件混用</h5>
<ul>
<li>
<p>不要将合成事件与原生事件混用</p>
</li>
<li>
<p>通过e.target判断来避免</p>
<pre><code class="copyable">  用reactEvent.nativeEvent.stopPropagation()来阻止冒泡是不行的。阻止 React 事件冒泡的行为只能用于 React 合成事件系统中，且没办法阻止原生事件的冒泡。
  反之，在原生事件中的阻止冒泡行为，却可以阻止 React 合成事件的传播。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-9">5. React stopPropagation 与 stopImmediatePropagation</h5>
<p>通过 React 绑定的事件，其回调函数中的 event 对象，是经过 React 合成的 SyntheticEvent，与原生的 DOM 事件的 event 不是一回事。准确地说，在 React 中，e.nativeEvent 才是原生 DOM 事件的那个 event。</p>
<h2 data-id="heading-10">React 合成事件与原生事件执行顺序图
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/478d8b32699b42309f02222129736569~tplv-k3u1fbpfcp-watermark.image" alt="3853478932-5a9ff2f3efa39_fix732.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<ul>
<li>DOM 事件冒泡到document上才会触发React的合成事件，所以React 合成事件对象的e.stopPropagation，只能阻止 React 模拟的事件冒泡，并不能阻止真实的 DOM 事件冒泡</li>
<li>DOM 事件的阻止冒泡也可以阻止合成事件原因是DOM 事件的阻止冒泡使事件不会传播到document上</li>
<li>当合成事件和DOM 事件 都绑定在document上的时候，React的处理是合成事件应该是先放进去的所以会先触发，在这种情况下，原生事件对象的 stopImmediatePropagation能做到阻止进一步触发document DOM事件</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f3e7ebf1d8244f99f17783afe4101f3~tplv-k3u1fbpfcp-watermark.image" alt="3262710300-5b546f588d9c2_fix732.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>若想阻止合成事件与除最外层document上的原生事件上的冒泡，通过判断e.target来避免，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;   
    <span class="hljs-keyword">if</span> (e.target && e.target.matches(<span class="hljs-string">'div.code'</span>)) &#123;  
      <span class="hljs-keyword">return</span>;    
    &#125;    
 &#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">6. 源码</h5>
<p>事件注册即在 document 节点，将 React 事件转化为 DOM 原生事件，并注册回调。</p>
<h6 data-id="heading-12">6.1 注册</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// enqueuePutListener 负责事件注册。</span>
<span class="hljs-comment">// inst：注册事件的 React 组件实例</span>
<span class="hljs-comment">// registrationName：React 事件，如：onClick、onChange</span>
<span class="hljs-comment">// listener：和事件绑定的 React 回调方法，如：handleClick、handleChange</span>
<span class="hljs-comment">// transaction：React 事务流，不懂没关系，不太影响对事件系统的理解</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enqueuePutListener</span>(<span class="hljs-params">inst, registrationName, listener, transaction</span>) </span>&#123;
    ... ...
   <span class="hljs-comment">// doc 为找到的 document 节点</span>
    <span class="hljs-keyword">var</span> doc = isDocumentFragment ? containerInfo._node : containerInfo._ownerDocument;
    <span class="hljs-comment">// 事件注册</span>
    listenTo(registrationName, doc);
    <span class="hljs-comment">// 事件存储，之后会讲到，即存储事件回调方法</span>
    transaction.getReactMountReady().enqueue(putListener, &#123;
        <span class="hljs-attr">inst</span>: inst,
        <span class="hljs-attr">registrationName</span>: registrationName,
        <span class="hljs-attr">listener</span>: listener
    &#125;);
&#125;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何在 document 上绑定 DOM 原生事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 事件注册</span>
<span class="hljs-comment">// registrationName：React 事件名，如：onClick、onChange</span>
<span class="hljs-comment">// contentDocumentHandle：要将事件绑定到的 DOM 节点</span>
<span class="hljs-attr">listenTo</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">registrationName, contentDocumentHandle</span>) </span>&#123;
    <span class="hljs-comment">// document</span>
    <span class="hljs-keyword">var</span> mountAt = contentDocumentHandle;      
    <span class="hljs-comment">// React 事件和绑定在根节点的 topEvent 的转化关系，如：onClick -> topClick</span>
    <span class="hljs-keyword">var</span> dependencies = EventPluginRegistry.registrationNameDependencies[registrationName];
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < dependencies.length; i++)&#123;
        <span class="hljs-comment">// 内部有大量判断浏览器兼容等的步骤，提取一下核心代码</span>
        <span class="hljs-keyword">var</span> dependency = dependencies[i];
        
        <span class="hljs-comment">// topEvent 和原生 DOM 事件的转化关系</span>
        <span class="hljs-keyword">if</span> (topEventMapping.hasOwnProperty(dependency)) &#123;
            <span class="hljs-comment">// 三个参数为 topEvent、原生 DOM Event、Document</span>
            <span class="hljs-comment">// 将事件绑定到冒泡阶段</span>
            trapBubbledEvent(dependency, topEventMapping[dependency], mountAt);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将事件绑定到冒泡阶段的具体代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 三个参数为 topEvent、原生 DOM Event、Document（挂载节点）</span>
<span class="hljs-attr">trapBubbledEvent</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, handlerBaseName, element</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!element) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-keyword">return</span> EventListener.listen(element, handlerBaseName, ReactEventListener.dispatchEvent.bind(<span class="hljs-literal">null</span>, topLevelType));
&#125;

<span class="hljs-comment">// 三个参数为 Document（挂载节点）、原生 DOM Event、事件绑定函数</span>
<span class="hljs-attr">listen</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listen</span>(<span class="hljs-params">target, eventType, callback</span>) </span>&#123;
    <span class="hljs-comment">// 去除浏览器兼容部分，留下核心后</span>
    target.addEventListener(eventType, callback, <span class="hljs-literal">false</span>);
    <span class="hljs-comment">// 返回一个解绑的函数</span>
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">remove</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove</span>(<span class="hljs-params"></span>) </span>&#123;
            target.removeEventListener(eventType, callback, <span class="hljs-literal">false</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-13">6.2 存储</h6>
<p>事件注册之后，还需要将事件绑定的回调函数存储下来。这样，在触发事件后才能去寻找相应回调来触发。在一开始的代码中，我们已经看到，是使用 putListener 方法来进行事件回调存储。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// inst：注册事件的 React 组件实例</span>
<span class="hljs-comment">// registrationName：React 事件，如：onClick、onChange</span>
<span class="hljs-comment">// listener：和事件绑定的 React 回调方法，如：handleClick、handleChange</span>
<span class="hljs-attr">putListener</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">inst, registrationName, listener</span>) </span>&#123;
    <span class="hljs-comment">// 核心代码如下</span>
    <span class="hljs-comment">// 生成每个组件实例唯一的标识符 key</span>
    <span class="hljs-keyword">var</span> key = getDictionaryKey(inst);
    <span class="hljs-comment">// 获取某种 React 事件在回调存储银行中的对象</span>
    <span class="hljs-keyword">var</span> bankForRegistrationName = listenerBank[registrationName] || (listenerBank[registrationName] = &#123;&#125;);
    bankForRegistrationName[key] = listener;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">6.3 执行</h6>
<p>每次触发事件都会执行根节点上 addEventListener 注册的回调，也就是 ReactEventListener.dispatchEvent 方法，事件分发入口函数。该函数的主要业务逻辑如下：</p>
<p>找到事件触发的 DOM 和 React Component
从该 React Component，调用 findParent 方法，遍历得到所有父组件，存在数组中。
从该组件直到最后一个父组件，根据之前事件存储，用 React 事件名 + 组件 key，找到对应绑定回调方法，执行，详细过程为：</p>
<p>根据 DOM 事件构造 React 合成事件。
将合成事件放入队列。
批处理队列中的事件（包含之前未处理完的，先入先处理）
React合成事件的冒泡并不是真的冒泡，而是节点的遍历。</p></div>  
</div>
            