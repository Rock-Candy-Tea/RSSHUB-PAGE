
---
title: 'React 03 __ Redux状态管理(续) -- 使用thunk中间件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145687da2c8e43fb93e27d2216b0fe0e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 06:40:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145687da2c8e43fb93e27d2216b0fe0e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇中，我们介绍了<code>Redux</code>的一些基础知识，还有基本实现，还介绍了如何实现同步和异步的<code>Action</code>与<code>ActionCreator</code>。</p>
<p>如果还没有看上一篇的小伙伴，可以去看看一看我的上一篇帖子。</p>
<p><a href="https://juejin.cn/post/6967273308446261262" target="_blank">juejin.cn/post/696727…</a></p>
<p>在这篇帖子里，我将继续上次的demo，讲述如何实现thunk中间件。虽然国内有很多小伙伴也都给出了如何使用<code>React</code> + <code>Redux</code> + <code>typescript</code>实现<code>thunk</code>中间件，但是好像使用到<code>connect</code>模式的比较少。</p>
<p>在这篇帖子里，我会详细地讲述如何使用thunk中间件实现异步<code>Action</code>与<code>ActionCreator</code>。再次重申，本文不涉及到如何实现，对于新手入门来说，如何实现没那么重要，学会使用才是第一步！Lol</p>
<p>本文Demo的Repo地址：</p>
<p><a href="https://gitlab.com/yafeya/react-demo/-/tree/yafeya/redux-thunk" target="_blank" rel="nofollow noopener noreferrer">gitlab.com/yafeya/reac…</a></p>
<h1 data-id="heading-1">0. 安装<code>thunk</code>中间件</h1>
<pre><code class="hljs language-bash copyable" lang="bash">npm i redux-thunk
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">1. 修改<code>ClockComponent</code></h1>
<p>在这个Demo中，我们基于上一次的Demo，把<code>ClockComponent</code>从<code>Promise</code>中间件修改成了<code>thunk</code>中间件，其实修改的代码很少，主要改了如下几点：</p>
<ul>
<li><code>Action</code></li>
<li><code>ActionCreator</code></li>
<li><code>Reducer</code></li>
<li><code>connect</code>方法的第二个参数<code>mapDispatchToProps</code>方法</li>
<li><code>Index</code>中使用的中间件</li>
</ul>
<p>下面我们对这些修改的点进行逐一的详细分析。</p>
<h1 data-id="heading-3">2. 详细分析</h1>
<h2 data-id="heading-4">2.1 <code>Action</code></h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> FETCHING_TIME = <span class="hljs-string">'FETCHING_TIME'</span>;
<span class="hljs-keyword">const</span> FETCHED_TIME = <span class="hljs-string">'FETCHED_TIME'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FetchingTimeAction &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FetchedTimeAction &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>;
    payload: <span class="hljs-built_in">Date</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145687da2c8e43fb93e27d2216b0fe0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>ActionType</code>从4个变成了2个
<blockquote>
<p>在上一篇文章里面我们提到过，<code>Promise</code>中间件会为我们自动生成3个<code>Action</code></p>
<p>他们的<code>Type</code>分别为：</p>
<ul>
<li><code>*_PENDING</code></li>
<li><code>*_FULFILLED</code></li>
<li><code>*_REJECTED</code></li>
</ul>
<p>然后，由<code>Promise</code>中间件负责将这3个<code>Action</code>分发到<code>Reducer</code>中，这个是我们控制不了的。但是对于<code>thunk</code>中间件来说，一切都是我们可以控制的，包括生成几个中间状态的Action，如何<code>dispatch</code>，都是我们自己控制的。所以，显而易见的是，我们需要的<code>ActionType</code>变少了。</p>
<p>其实，这也恰恰说明了一个问题，相对于<code>promise</code>中间件，<code>thunk</code>中间件更为灵活，但是需要自己做的事情更多了。<code>promise</code>中间件虽然代码会稍微多一点，但是大部分的事情，由中间件帮我们做好了。孰优孰劣，大家自己把握。</p>
</blockquote>
</li>
<li><code>ActionPayload</code>从<code>Promise<Date></code>变成了<code>Date</code>
<blockquote>
<p>这一点，也是我觉得<code>thunk</code>做的更好一点的事情，<code>Action</code>摆脱了业务逻辑，变成了一个更纯粹的数据格式，业务逻辑交给了<code>ActionCreator</code>。</p>
<p>为什么说<code>Promise<Date></code>中带有业务逻辑呢，因为，如果返回值带有Promise的话，它的消费端就必然需要对Promise进行处理，如果得到正确结果如何处理，如果失败如何处理，所以我说<code>Promise</code>对象是贷业务逻辑的。</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-5">2.2 <code>ActionCreator</code></h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//Action Creator</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchTime</span>(<span class="hljs-params">parameter: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">ThunkAction</span><
                                                        // <span class="hljs-title">Promise</span> <span class="hljs-title">of</span> <span class="hljs-title">last</span> <span class="hljs-title">dispatched</span> <span class="hljs-title">action</span>
                                                        <span class="hljs-title">Promise</span><<span class="hljs-title">FetchedTimeAction</span>>,
                                                        // <span class="hljs-title">Data</span> <span class="hljs-title">type</span> <span class="hljs-title">of</span> <span class="hljs-title">the</span> <span class="hljs-title">last</span> <span class="hljs-title">action</span>
                                                        <span class="hljs-title">Date</span>,
                                                        // <span class="hljs-title">The</span> <span class="hljs-title">type</span> <span class="hljs-title">of</span> <span class="hljs-title">the</span> <span class="hljs-title">parameter</span> <span class="hljs-title">for</span> <span class="hljs-title">the</span> <span class="hljs-title">nested</span> <span class="hljs-function"><span class="hljs-keyword">function</span>
                                                        <span class="hljs-title">string</span>,
                                                        // <span class="hljs-title">The</span> <span class="hljs-title">type</span> <span class="hljs-title">of</span> <span class="hljs-title">last</span> <span class="hljs-title">action</span> <span class="hljs-title">to</span> <span class="hljs-title">dispatch</span>.
                                                        <span class="hljs-title">FetchedTimeAction</span>> </span>&#123;
            <span class="hljs-title">return</span> <span class="hljs-title">async</span> (<span class="hljs-params">dispatch: ThunkDispatch<<span class="hljs-built_in">Date</span>, <span class="hljs-built_in">string</span>, AnyAction></span>)=></span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`parameter is <span class="hljs-subst">$&#123;parameter&#125;</span>`</span>);
                <span class="hljs-keyword">let</span> fetchingAction:FetchingTimeAction = &#123;<span class="hljs-attr">type</span>: FETCHING_TIME&#125;;
                <span class="hljs-comment">// we can dispatch middle action in the creator.</span>
                dispatch(fetchingAction);
                <span class="hljs-keyword">let</span> time = <span class="hljs-keyword">await</span> getTimeAsync();
                <span class="hljs-keyword">let</span> fetchedTimeAction: FetchedTimeAction = &#123;
                    <span class="hljs-attr">type</span>: FETCHED_TIME,
                    <span class="hljs-comment">// property name must be 'payload'</span>
                    <span class="hljs-attr">payload</span>: time
                &#125;;
                <span class="hljs-keyword">return</span> dispatch(fetchedTimeAction);
            &#125;;
        &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这部分是变化最大的部分，相当于重写了，只保留了原有的函数名，所以就没有啥可比性了，我们直接来分析一下变化吧。</p>
<blockquote>
<p>这个参数，大家可以忽略掉，这个是我用来做测试的，其实没有什么实际意义。</p>
</blockquote>
<ul>
<li>
<p><code>ThunkAction<R, S, E, A></code>返回值
我们首先来说这几个泛型的参数类型：</p>
<ul>
<li>R: 最后一次<code>dispatch</code>的<code>Action</code>类型的<code>Promise</code>对象</li>
</ul>
<blockquote>
<pre><code class="copyable">e.g. 我们最后一次要`dispatch`的`action`类型为`FetchedTimeAction`，所以这里填`Promise<FetchedTimeAction>`.
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<ul>
<li>S: 最后一次<code>dispatch</code>的<code>Action</code>类型的<code>Payload</code>类型</li>
</ul>
<blockquote>
<pre><code class="copyable">e.g. `FetchedTimeAction`的`Payload`类型为`Date`，所以这里要填`Date`.
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<ul>
<li>E: <code>ActionCreator</code>方法的参数类型</li>
</ul>
<blockquote>
<pre><code class="copyable">e.g. 本例中，这个函数的参数为`string`, 所以这里我填了`string`.
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<ul>
<li>A: 最后一次<code>dispatch</code>的<code>Action</code>的类型</li>
</ul>
<blockquote>
<pre><code class="copyable">e.g. 本例中，最后一次`dispath`的是`FetchedAction`，所以填这个.
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</li>
<li>
<p><code>ActionCreator</code>的实现
<code>fetchTime</code>这个方法要返回的类型是<code>ThunkAction<R,S,E,A></code>, 第一次看到的时候，说实话，我裂开了，什么鬼？</p>
<p>不过，<code>vscode</code>的智能感知，实在太NB了，我们看一下！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c7904a75a804257a25e01b19e62e583~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-typescript copyable" lang="typescript">ThunkAction<R,S,E,A> = <span class="hljs-function">(<span class="hljs-params">dispatch: ThunkDispatch<S,E,A></span>) =></span> R
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这说明，我们需要一个<code>dispatch: ThunkDispatch<S,E,A></code>作为参数，返回值是我们那个<code>Promise<A></code>就可以了，因为<code>R=Promise<A></code>.</p>
<p>当然，我看有些小伙伴们会把第一个参数也就是R填成<code>void</code>，也可以了，更简单。</p>
</li>
<li>
<p><code>ActionCreator</code>中<code>dispatch</code>我们需要的<code>Action</code></p>
<p>相信上面的一顿操作，大家都有点蒙圈，说实话，我第一次看的时候，也蒙了半天，不过慢慢的看一两遍，基本上就能明白了，如果还有问题，那么你就记住这是个固定写法，按照我的<code>Demo</code>去套你<code>Action</code>就好了，因为最主要的是我们下面要讲的，这个代理里面的实现。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//...</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`parameter is <span class="hljs-subst">$&#123;parameter&#125;</span>`</span>);
<span class="hljs-keyword">let</span> fetchingAction:FetchingTimeAction = &#123;<span class="hljs-attr">type</span>: FETCHING_TIME&#125;;
<span class="hljs-comment">// we can dispatch middle action in the creator.</span>
dispatch(fetchingAction);
<span class="hljs-keyword">let</span> time = <span class="hljs-keyword">await</span> getTimeAsync();
<span class="hljs-keyword">let</span> fetchedTimeAction: FetchedTimeAction = &#123;
    <span class="hljs-attr">type</span>: FETCHED_TIME,
    <span class="hljs-comment">// property name must be 'payload'</span>
    <span class="hljs-attr">payload</span>: time
&#125;;
<span class="hljs-keyword">return</span> dispatch(fetchedTimeAction);
<span class="hljs-comment">//...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>dispatch FetchingTimeAction</code>
<blockquote>
<p><code>Reducer</code>会根据这个<code>action</code>修改<code>state</code>中的<code>isFetching=true</code>，<code>ux</code>上可以根据<code>isFetching=true</code>做相应的处理，比如显示进度条啥的，不过我们的<code>demo</code>里面比较懒，啥都没做LoL.</p>
</blockquote>
</li>
<li>调用<code>Api</code>
<blockquote>
<p>调用了<code>await getTimeAsync()</code>, 这一步在真实环境下一般都比较慢，所以这是真正的异步意义所在。</p>
</blockquote>
</li>
<li><code>dispatch FetchedTimeAction</code>
<blockquote>
<p>当上一步调用完成，我们就可以发送<code>FetchedTimeAction</code>，<code>Reducer</code>根据这个<code>Action</code>会将<code>state</code>中的<code>isFetching=false</code>并且设置<code>succeed=true</code>，<code>ux</code>得到<code>new-state</code>也会做相应的处理。</p>
<p>而且很巧妙的是<code>dispatch(fetchedTimeAction)</code>正好也返回的是这个<code>Action</code>，正好能对应上我们之前说的<code>ThunkAction</code>的要求。</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-6">2.3 <code>Reducer</code></h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clockReducer</span>(<span class="hljs-params">state = initState, action: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">ClockState</span> </span>&#123;
    <span class="hljs-keyword">let</span> result = initState;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> FETCHING_TIME:
            result = &#123;
                ...state,
                <span class="hljs-attr">isFetching</span>: <span class="hljs-literal">true</span>
            &#125;;
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> FETCHED_TIME:
            result = &#123;
                ...state,
                <span class="hljs-attr">isFetching</span>: <span class="hljs-literal">false</span>,
                <span class="hljs-attr">succeed</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">time</span>: action.payload
            &#125;;
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>:
            result = state;
            <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实，从某种意义上讲，<code>Reducer</code>的逻辑没有变化，还是根据<code>ActionType</code>的不同而生成新的<code>State</code>，其实严格意义上来讲，变化的只有<code>Action</code>与<code>ActionCreator</code>。</p>
<h2 data-id="heading-7">2.4 <code>connect</code>方法的第二个参数<code>mapDispatchToProps</code>方法</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function">(<span class="hljs-params">dispatch: ThunkDispatch<<span class="hljs-built_in">any</span>, <span class="hljs-built_in">any</span>, AnyAction></span>) =></span> (&#123;
    <span class="hljs-attr">fetchTime</span>: <span class="hljs-function">(<span class="hljs-params">parameter: <span class="hljs-built_in">string</span></span>) =></span> dispatch(fetchTime(parameter))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5215604bd91f4ffbbfe442cdf875d50a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里之所以变化，是因为，dispatch方法的类型变化了，变成了ThunkDispatch类型。</p>
<h2 data-id="heading-8">2.5 <code>Index</code>中使用的中间件</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1706ed113eea40288a36854ba90cddbe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的变化更小，就是将<code>promise</code>中间件改换成为<code>thunk</code>中间件。</p></div>  
</div>
            