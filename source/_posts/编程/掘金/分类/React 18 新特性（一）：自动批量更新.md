
---
title: 'React 18 新特性（一）：自动批量更新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4777'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 00:35:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=4777'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文已收录在 Github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbeichensky%2FBlog" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/beichensky/Blog" ref="nofollow noopener noreferrer">github.com/beichensky/…</a> 中，欢迎 Star，欢迎 Follow！</p>
<h2 data-id="heading-1">18 版本之前</h2>
<h3 data-id="heading-2">经典面试题：setState 是同步还是异步</h3>
<p>在 <code>react 18</code> 版本之前，在面试中经常会出现这个问题，那么答案又是什么样的呢？</p>
<ul>
<li>
<p>在 <code>React</code> 合成事件中是异步的</p>
</li>
<li>
<p>在 <code>hooks</code> 中是异步的</p>
</li>
<li>
<p>其他情况皆是同步的，例如：原生事件、<code>setTimeout</code>、<code>Promise</code> 等</p>
</li>
</ul>
<p>看看下面这段代码的执行结果，就知道所言非虚了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;

    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);
            <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);
        &#125;);
        
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Count: &#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有经验的同学肯定都知道，最终的结果是： <code>0 0 2 3</code>。</p>
<p>原因就是因为 <code>componentDidMount</code> 中的 <code>setState</code> 是批量更新，在整体逻辑没走完之前，不会进行更新。所以前两次打印结果都是 0，并且将两次更新合并成了一次。</p>
<p>而在 <code>setTimeout</code> 中，脱离了 <code>React</code> 的掌控，变成了同步更新，因为下方的 <code>log</code> 可以实时打印出即时的状态。</p>
<p>此时 <code>React</code> 的内部的处理逻辑我们可以写一段代码简单模拟一下：</p>
<ul>
<li>
<p>先声明三个变量，用来记录数据</p>
<ul>
<li>
<p><code>isBatchUpdate</code>: 判断是否批量更新的标志</p>
</li>
<li>
<p><code>count</code>: 状态</p>
</li>
<li>
<p><code>queue</code>: 存储状态的数组</p>
</li>
</ul>
</li>
<li>
<p>声明一个 <code>handleClick</code> 方法，来模拟 <code>React</code> 合成事件</p>
</li>
<li>
<p>声明一个 <code>setState</code> 方法，来模拟 <code>React</code> 的 <code>setState</code></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断是否批量更新的标志</span>
<span class="hljs-keyword">let</span> isBatchUpdate = <span class="hljs-literal">false</span>;
<span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
<span class="hljs-comment">// 存储最新状态的数组</span>
<span class="hljs-keyword">let</span> queue = [];
<span class="hljs-keyword">const</span> setState = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
    <span class="hljs-comment">// 批量更新，则将状态暂存，否则直接更新</span>
    <span class="hljs-keyword">if</span> (isBatchUpdate) &#123;
        queue.push(state);
    &#125; <span class="hljs-keyword">else</span> &#123;
        count = state;
    &#125;
&#125;

<span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 进入事件，先将 isBatchUpdate 设置为 true</span>
    isBatchUpdate = <span class="hljs-literal">true</span>

    setState(count + <span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(count);
    setState(count + <span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(count);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        setState(count + <span class="hljs-number">1</span>)
        <span class="hljs-built_in">console</span>.log(count);
        setState(count + <span class="hljs-number">1</span>)
        <span class="hljs-built_in">console</span>.log(count);
    &#125;)
    
    <span class="hljs-comment">// 事件结束，将 isBatchUpdate 置为 false</span>
    isBatchUpdate = <span class="hljs-literal">false</span>;
&#125;

handleClick();

count = queue.pop();

<span class="hljs-comment">// 更新完成，重置状态数组 queue</span>
queue = [];

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，上面这段代码的打印结果也是 <code>0 0 2 3</code>。</p>
<h3 data-id="heading-3">手动批量更新</h3>
<p>上面提到，在原生事件以及 <code>setTimeout</code> 等情况下，<code>setState</code> 是同步的，那<strong>如果我们仍然希望这种情况下可以同步更新</strong>，该怎么办呢？</p>
<p><strong><code>React</code> 也提供了一种解决方案：从 <code>react</code> 包中暴露了一个 <code>API</code>: <code>unstable_batchedUpdates</code></strong></p>
<p>那我们简单用一下看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;

    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            React.unstable_batchedUpdates(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
            &#125;) 
        &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Count: &#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到此时的打印结果为 <code>0 0 1 1</code>。</p>
<blockquote>
<p>Ok，React 18 之前 <code>setState</code> 的更新方式就说到这里，那 React 18 里做了什么改动呢？</p>
</blockquote>
<h2 data-id="heading-4">React 18 版本之后</h2>
<p>上面提到了默认批量更新以及手动批量更新，那有些同学不满足了呀，觉得手动的还是不够智能，在很多情况下还得手动去调用 <code>unstable_batchedUpdates</code> 这个函数，用起来不爽。</p>
<p>别急，React 18 新版本就可以解决这些同学的痛点了！</p>
<p>Ok，直接上代码，看看 React 18 到底怎么用的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;

    state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
            <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>&#125;)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
        &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Count: &#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
&#125;

<span class="hljs-comment">// 使用 react 18 新的并发模式写法进行 dom render</span>
ReactDOM.createRoot(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'#root'</span>)!).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件代码保持和第一版的一致，没有使用 <code>unstable_batchedUpdates</code>。</p>
<p>可以看到，此时的打印结果也是: <code>0 0 1 1</code></p>
<p>仅仅是使用了新的 <code>API</code>： <code>ReactDOM.createRoot(root).render(jsx)</code>。React 就能实现自动的批量更新了。感觉有点神奇。</p>
<p>我们依然写一段代码来模拟一下这个过程：</p>
<ul>
<li>
<p>此时不需要 <code>isBatchUpdate</code> 来判断是否批量更新了，而是通过更新的优先级来进行判断</p>
</li>
<li>
<p>每次更新会进行优先级的判定，相同优先级的任务会被合并。</p>
</li>
<li>
<p>事件执行完毕，进行任务的执行和更新</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
<span class="hljs-comment">// 存储状态的数组</span>
<span class="hljs-keyword">let</span> queue = [];
<span class="hljs-keyword">const</span> setState = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newState = &#123;<span class="hljs-attr">payload</span>: state, <span class="hljs-attr">priority</span>: <span class="hljs-number">0</span> &#125;
    <span class="hljs-comment">// 判断当前优先级的任务集合是否存在，不存在则初始化，存在则存到对应由县级的任务集合中</span>
    <span class="hljs-keyword">if</span> (queue[newState.priority]) &#123;
        queue[newState.priority].push(newState.payload)
    &#125; <span class="hljs-keyword">else</span> &#123;
        queue[newState.priority] = [newState.payload]
    &#125;
&#125;

<span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
    setState(count + <span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(count);
    setState(count + <span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(count);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        setState(count + <span class="hljs-number">1</span>);
        <span class="hljs-built_in">console</span>.log(count);
        setState(count + <span class="hljs-number">1</span>)
        <span class="hljs-built_in">console</span>.log(count);
    &#125;)
&#125;

handleClick();

count = queue.pop().pop();

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    count = queue.pop().pop();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，上面这段代码的执行结果也是 <code>0 0 1 1</code></p>
<p><em>上述模拟代码仅为了展示优先级批量更新，不代表任何 React 源码的逻辑和思想</em></p>
<p>好了，自动批量更新的新特性就说到这里了。这里引入了三个问题：</p>
<ol>
<li>
<p>Q: React 18 之后提供了 <code>ReactDOM.createRoot</code>(root).render(jsx) 的 API，那之前 <code>ReactDOM.render</code> 的 API 还支持吗？</p>
<p>A: 支持的，并且行为和之前版本是一致的。只有使用了 <code>ReactDOM.createRoot</code> 这种方式，才会启用新的并发模式。</p>
</li>
<li>
<p>Q: React 全自动更新后，那如果我就是想拿到更新之后的数据怎么办呢？
A: 类组件中可以使用 <code>setState(state, callback)</code> 的方式，在 <code>callback</code> 中取到最新的值，函数组件可以使用 <code>useEffect</code>，将 <code>state</code> 作为依赖。即可以拿到最新的值。</p>
</li>
<li>
<p>Q: 文章中说到的优先级的概念是怎么回事呢？
A: 这个涉及到 React 最新的调度以及更新的机制，优先级的概念以及其他优先级的任务如何创建，我们之后会一一展开来说。</p>
<p>目前的话，可以理解为 React 的更新机制进行了变化，不再依赖于批量更新的标志。而是根据任务优先级来进行更新：高优先级的任务先执行，低优先级的任务后执行。</p>
</li>
</ol>
<h2 data-id="heading-5">写在后面</h2>
<p>代码量很少，主要是修改了 <code>ReactDOM</code> 的渲染方式，可以亲自尝试一下，有疑惑的地方可以说出来一起进行讨论。</p>
<p>如果有写的不对或不严谨的地方，欢迎大家能提出宝贵的意见，十分感谢。</p>
<p>如果喜欢或者有所帮助，欢迎 Star，对作者也是一种鼓励和支持。</p></div>  
</div>
            