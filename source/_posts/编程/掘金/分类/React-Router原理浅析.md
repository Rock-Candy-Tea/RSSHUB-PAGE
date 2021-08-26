
---
title: 'React-Router原理浅析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8459'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 22:37:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=8459'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前前言</h1>
<p>hello各位小伙伴，我是来自推啊前端团队的 <a href="https://juejin.cn/user/2365804756364237" title="https://juejin.cn/user/2365804756364237" target="_blank">jarvis</a>。 今天跟大家简要分享一下<code>React-Router</code>原理。</p>
<h1 data-id="heading-1">1. 原理初探</h1>
<p>借助<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FReactTraining%2Fhistory" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ReactTraining/history" ref="nofollow noopener noreferrer">history库</a>实现<strong>监听路由</strong>，内部支持<strong>hash</strong>和<strong>bowser</strong>两种路由变化。</p>
<p>使用<strong>react-router-dom</strong>时首先选择的就是<strong>BrowserRouter</strong>或<strong>HashRouter</strong>，对应<strong>hash</strong>和<strong>browser</strong>两种路由规则，两个组件的源码实现基本一致，区别是调用了<strong>history</strong>库的两个不同方法创建<strong>history对象</strong>，然后通过<code>React.Context</code>将<strong>history对象</strong>共享给<strong>消费者</strong>使用，在<strong>消费者</strong>内部会注册一个<strong>更新当前组件</strong>的函数，每当路由<strong>变化时</strong>会自动<strong>触发组件更新</strong>，从而实现路由切换的效果。</p>
<p>在源码中二者区别如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// BrowserRouter</span>
<span class="hljs-keyword">import</span> &#123; createBrowserHistory <span class="hljs-keyword">as</span> createHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'history'</span>;

<span class="hljs-comment">// HashRouter</span>
<span class="hljs-keyword">import</span> &#123; createHashHistory <span class="hljs-keyword">as</span> createHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'history'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们任选其一即可，就选<strong>BrowserRouter</strong>吧</p>
<h1 data-id="heading-2">2. 从源码探究细节</h1>
<h2 data-id="heading-3">2.1. BrowserRouter</h2>
<ul>
<li>
<p>作用</p>
<ul>
<li>创建<code>history</code>实例，</li>
<li>将<code>children</code>和<code>history</code>传入组件<code><Router/></code>并返回</li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createBrowserHistory <span class="hljs-keyword">as</span> createHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'history'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BrowserRouter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  history = createHistory(<span class="hljs-built_in">this</span>.props);

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span> <span class="hljs-attr">history</span>=<span class="hljs-string">&#123;this.history&#125;</span> <span class="hljs-attr">children</span>=<span class="hljs-string">&#123;this.props.children&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>history</code>对象实际上是通过<code>createBrowserHistory</code>创建的，核心逻辑都在<code><Router/></code>组件中，<code><Router/></code>组件接收特定的<code>history</code>对象，<code>history</code>对象目前包括hash、browser、memory三种类型。</p>
</li>
</ul>
<h2 data-id="heading-4">2.2. Router</h2>
<ul>
<li>
<p>作用</p>
<ul>
<li>监听路由变化，存储到<code>state</code>中</li>
<li>通过<code>Context</code>向下传递<code>history</code>、<code>location</code>、<code>match</code>等</li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Router</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// 默认命中的路由</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">computeRootMatch</span>(<span class="hljs-params">pathname</span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">url</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">params</span>: &#123;&#125;, <span class="hljs-attr">isExact</span>: pathname === <span class="hljs-string">'/'</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);

    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">location</span>: props.history.location,
    &#125;;

    <span class="hljs-built_in">this</span>._isMounted = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">this</span>._pendingLocation = <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 监听路由变化</span>
    <span class="hljs-keyword">if</span> (!props.staticContext) &#123;
      <span class="hljs-built_in">this</span>.unlisten = props.history.listen(<span class="hljs-function"><span class="hljs-params">location</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._isMounted) &#123;
          <span class="hljs-built_in">this</span>.setState(&#123; location &#125;);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>._pendingLocation = location;
        &#125;
      &#125;);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>._isMounted = <span class="hljs-literal">true</span>;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._pendingLocation) &#123;
      <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">location</span>: <span class="hljs-built_in">this</span>._pendingLocation &#125;);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 取消监听</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.unlisten) &#123;
      <span class="hljs-built_in">this</span>.unlisten();
      <span class="hljs-built_in">this</span>._isMounted = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>._pendingLocation = <span class="hljs-literal">null</span>;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Provider</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span>
          <span class="hljs-attr">history:</span> <span class="hljs-attr">this.props.history</span>,
          <span class="hljs-attr">location:</span> <span class="hljs-attr">this.state.location</span>,
          <span class="hljs-attr">match:</span> <span class="hljs-attr">Router.computeRootMatch</span>(<span class="hljs-attr">this.state.location.pathname</span>),
          <span class="hljs-attr">staticContext:</span> <span class="hljs-attr">this.props.staticContext</span>,
        &#125;&#125;
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">HistoryContext.Provider</span>
          <span class="hljs-attr">children</span>=<span class="hljs-string">&#123;this.props.children</span> || <span class="hljs-attr">null</span>&#125;
          <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.props.history&#125;</span>
        /></span>
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Provider</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先<code><Router/></code>会声明<strong>默认</strong>命中路由的规则，即静态方法<code>computeRootMatch</code>，默认是匹配成功，记住这里的<code>isExact</code>，后续会使用。</p>
<p>在<strong>构造方法</strong>中监听路由变化，使用的<code>history</code>是在<code>BrowserRouter</code>中通过<code>createBrowserHistory</code>库创建的实例。</p>
<p>注意，<code>_isMounted</code>和<code>_pendingLocation</code>是为了处理<strong>懒加载</strong>组件，当路由<strong>匹配</strong>时，此时<strong>懒加载组件</strong>还未<strong>挂载</strong>，所以放到<code>_pendingLocation</code>临时存储，然后在<code>componentDidMount</code>中更新到<code>state</code>。</p>
</li>
</ul>
<h2 data-id="heading-5">2.3. Route</h2>
<ul>
<li>
<p>作用</p>
<ul>
<li>通过<code>matchPath</code>判断当前<code><Route/></code>的<code>path</code>是否匹配</li>
<li>创建<code>Provider</code>，带着当前<code>path</code>是否匹配以及<code>Context</code>的其他内容一起共享给子组件</li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Route</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;context => &#123;
          const location = this.props.location || context.location;
          // 如果没有传入path，则通过matchPath匹配
          const match = this.props.computedMatch
            ? this.props.computedMatch // 包裹<span class="hljs-tag"><<span class="hljs-name">Switch</span>/></span>组件时注入的prop
            : this.props.path
            ? matchPath(location.pathname, this.props)
            : context.match;

          const props = &#123; ...context, location, match &#125;;

          let &#123; children, component, render &#125; = this.props;

          // children必须是单根节点
          if (Array.isArray(children) && isEmptyChildren(children)) &#123;
            children = null;
          &#125;

          return (
            <span class="hljs-tag"><<span class="hljs-name">RouterContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;props&#125;</span>></span>
              &#123;props.match
                ? children
                  ? typeof children === 'function'
                    ? __DEV__
                      ? evalChildrenDev(children, props, this.props.path)
                      : children(props)
                    : children
                  : component
                  ? React.createElement(component, props)
                  : render
                  ? render(props)
                  : null
                : typeof children === 'function'
                ? __DEV__
                  ? evalChildrenDev(children, props, this.props.path)
                  : children(props)
                : null&#125;
            <span class="hljs-tag"></<span class="hljs-name">RouterContext.Provider</span>></span>
          );
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p><code>match</code>：</p>
<ul>
<li>优先比较<code>computedMatch</code>，这是<code><Route/></code>组件被<code><Switch/></code>组件包裹时注入的 <code>prop</code>，如果有则直接使用，</li>
<li>没有<code>computedMatch</code>比较<code>path</code>，若存在<code>path</code>通过<code>matchPath</code>处理</li>
<li>没有<code>path</code>则直接使用<code>match</code>，这是<code><Router/></code>通过<code>provider</code>传递的<strong>默认匹配规则</strong>，这里会<strong>匹配成功</strong>，所以<strong>404 组件</strong>不写<code>path</code></li>
</ul>
</li>
<li>
<p>组件的返回结果：</p>
<ul>
<li><code>match</code>是否匹配成功
<ul>
<li>匹配
<ul>
<li>children 是否存在
<ul>
<li>存在
<ul>
<li>children 是函数：执行</li>
<li>不是函数就是组件：渲染</li>
</ul>
</li>
<li>不存在
<ul>
<li>component 是否存在
<ul>
<li>存在：createElement(component, props)</li>
<li>不存在：
<ul>
<li>render 是否存在
<ul>
<li>存在：执行</li>
<li>不存在：null</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>不匹配
<ul>
<li>children 是函数
<ul>
<li>匹配：执行</li>
<li>不匹配：null</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>由于可见，优先级分别是：<code>children</code>><code>component</code>><code>render</code>，</p>
<p>需要注意的一点是，<strong>component</strong>通过<code>React.createElement</code>创建，在React中会根据<code>type</code>有没有<strong>改变</strong>选择是否<strong>重用组件</strong>，所以为了避免不必要的开销，<strong>component</strong>属性最好不要写<strong>内联函数</strong></p>
<p>最后返回<code>Provider</code>是为了后续使用<strong>高阶组件</strong><code>withRouter</code>。</p>
</li>
</ol>
</li>
</ul>
<h2 data-id="heading-6">2.4. Switch</h2>
<p>也被称为<strong>独占路由</strong></p>
<ul>
<li>
<p>作用</p>
<ul>
<li>只返回<strong>匹配成功</strong>的子组件<code><Route/></code></li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Switch</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <RouterContext.Consumer>
        &#123;context => &#123;
          invariant(context, 'You should not use <Switch> outside a <Router>');

          const location = this.props.location || context.location;

          let element, match;

          // We use React.Children.forEach instead of React.Children.toArray().find()
          // here because toArray adds keys to all child elements and we do not want
          // to trigger an unmount/remount for two <Route>s that render the same
          // component at different URLs.
          React.Children.forEach(this.props.children, child => &#123;
            if (match == null && React.isValidElement(child)) &#123;
              element = child;

              const path = child.props.path || child.props.from;

              match = path
                ? matchPath(location.pathname, &#123; ...child.props, path &#125;)
                : context.match;
            &#125;
          &#125;);

          return match ? React.cloneElement(element, &#123; location, computedMatch: match &#125;) : null;
        &#125;&#125;
      </RouterContext.Consumer>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么不使用<code>React.Children.toArray().find()</code>，源码中的<strong>注释</strong>已经写的很明白了，因为<code>toArray</code>会为所有<strong>子元素</strong>添加<code>key</code>，因而可能出现<strong>不同 url</strong>显示两个相同<code><Route/></code><strong>卸载</strong>或<strong>重新挂载</strong>的情况。</p>
<p>首先看一下最终的渲染结果，若<code>match</code>为真则使用匹配成功的组件，并且为其添加<code>location</code>和<code>computedMatch</code>，这里重点是<code>computedMatch</code>，刚才已经整理，<code><Route/></code>组件在匹配时会优先使用这个<code>computedMatch</code>，如果没有<code>computedMatch</code>才会使用自己的<strong>匹配方式</strong>匹配。而<code><Switch/></code>通过<strong>匹配算法</strong>返回最后一个组件，所以最终在页面呈现的<code><Route/></code>只有一个。</p>
<p>下面看<strong>匹配算法</strong>，<strong>遍历</strong>所有的<strong>子节点（也就是<code><Route/></code>）</strong>，对每个组件的<code>path</code>进行<code>matchPath</code>，如果<strong>匹配成功</strong>则保存到变量<code>element</code>中，一直<strong>遍历</strong>到最后一<strong>个子组件</strong>为止。</p>
<p>在这里不得不提一下<strong>404 组件</strong>的两个条件，</p>
<ol>
<li>不写<code>path</code>，</li>
<li>放在<code><Switch/></code>的最后一个子组件</li>
</ol>
<p>刚才我们已经整理，<strong>Route</strong>组件没有<code>path</code>时会使用<code>Router</code>组件提供的<code>match</code>，<code>match</code>默认是匹配的，所以不写<code>path</code>可以使用默认匹配的条件；
<code><Switch/></code>组件的<strong>匹配方式</strong>通过<strong>循环</strong>完成，一直遍历到最后一个为止，如果放在前面，即使<strong>404 组件</strong>被匹配到，紧接着下次循环也会被覆盖掉，最终渲染一个<code>null</code>，所以必须是<code><Switch/></code>的<strong>最后一个</strong>子组件，保证一定是匹配到的组件。</p>
</li>
</ul>
<h2 data-id="heading-7">2.5. withRouter</h2>
<ul>
<li>
<p>作用</p>
<ul>
<li>这是一个<strong>高阶组件</strong>，取出<code><Route/></code>通过<code>Provider</code>共享的数据，给<strong>目标组件</strong>使用</li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">withRouter</span>(<span class="hljs-params">Component</span>) </span>&#123;
  <span class="hljs-keyword">const</span> C = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; wrappedComponentRef, ...remainingProps &#125; = props;

    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;context => &#123;
          return <span class="hljs-tag"><<span class="hljs-name">Component</span> &#123;<span class="hljs-attr">...remainingProps</span>&#125; &#123;<span class="hljs-attr">...context</span>&#125; <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;wrappedComponentRef&#125;</span> /></span>;
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
    );
  &#125;;

  <span class="hljs-keyword">return</span> hoistStatics(C, Component);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还记得吗，<code><Route/></code>组件最后返回一个<code>provider</code>，共享<code>path</code>的匹配情况，其实就是为了通过<code>withRouter</code>给<strong>组件</strong>使用</p>
</li>
</ul>
<h2 data-id="heading-8">2.6. Link</h2>
<p><strong>Link</strong>本质上也是<code>Context</code>的<code>Consumer</code>，取出<code>history</code>，通过执行<code>history.replace</code>或<code>history.push</code>来<strong>改变路由</strong></p>
<h2 data-id="heading-9">2.7. Redirect</h2>
<ul>
<li>
<p>作用</p>
<ul>
<li>重定向</li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Redirect</span>(<span class="hljs-params">&#123; computedMatch, to, push = <span class="hljs-literal">false</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
      &#123;context => &#123;
        const &#123; history, staticContext &#125; = context;

        const method = push ? history.push : history.replace;
        const location = createLocation(
          computedMatch
            ? typeof to === 'string'
              ? generatePath(to, computedMatch.params)
              : &#123;
                  ...to,
                  pathname: generatePath(to.pathname, computedMatch.params),
                &#125;
            : to
        );

        return (
          <span class="hljs-tag"><<span class="hljs-name">Lifecycle</span>
            <span class="hljs-attr">onMount</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
              method(location);
            &#125;&#125;
            onUpdate=&#123;(self, prevProps) => &#123;
              const prevLocation = createLocation(prevProps.to);
              if (
                !locationsAreEqual(prevLocation, &#123;
                  ...location,
                  key: prevLocation.key,
                &#125;)
              ) &#123;
                method(location);
              &#125;
            &#125;&#125;
            to=&#123;to&#125;
          />
        );
      &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Redirect</strong>和<strong>Route</strong>都作为<strong>Switch</strong>的子组件使用，只是<strong>Redirect 组件</strong>没有渲染实体，只是为了<strong>重定向</strong></p>
<p>最后返回了<code>Lifecycle</code>组件，这是一个<strong>非常值得学习</strong>的内容，在我们的项目场景中可以<strong>借鉴</strong>这种方式来实现<strong>比较复杂的逻辑</strong></p>
<p>源码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lifecycle</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.onMount) <span class="hljs-built_in">this</span>.props.onMount.call(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.onUpdate) <span class="hljs-built_in">this</span>.props.onUpdate.call(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>, prevProps);
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.onUnmount) <span class="hljs-built_in">this</span>.props.onUnmount.call(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到最后<code>render</code>方法返回了<code>null</code>表明<strong>没有渲染真实 dom</strong>，只是借助<strong>react 组件</strong>的<strong>生命周期</strong>做了一些事情，</p>
<p>所以<strong>Redirect 组件</strong>最终只是在<strong>挂载时</strong>执行了<code>history.push</code>或<code>history.replace</code>完成<strong>重定向操作</strong>，</p>
<p><strong>重定向</strong>在<strong>react-router-dom</strong>中有两种方式</p>
<ol>
<li>标签式重定向：<code><Redirect to="/home"></code></li>
<li>编程式重定向：<code>this.props.history.push('/home')</code></li>
</ol>
</li>
</ul>
<h2 data-id="heading-10">2.8. Prompt</h2>
<p>有了刚才的心得，接下来又是<strong>Lifecycle 组件</strong>的一次应用</p>
<ul>
<li>
<p>作用</p>
<ul>
<li>在页面离开前做<strong>拦截询问</strong></li>
</ul>
</li>
<li>
<p>核心源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Prompt</span>(<span class="hljs-params">&#123; message, when = <span class="hljs-literal">true</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <RouterContext.Consumer>
      &#123;context => &#123;
        invariant(context, 'You should not use <Prompt> outside a <Router>');

        if (!when || context.staticContext) return null;

        // 通过 history 调用平台的 询问方法，默认是 window.confirm
        const method = context.history.block;

        return (
          <Lifecycle
            onMount=&#123;self => &#123;
              self.release = method(message);
            &#125;&#125;
            onUpdate=&#123;(self, prevProps) => &#123;
              if (prevProps.message !== message) &#123;
                self.release();
                self.release = method(message);
              &#125;
            &#125;&#125;
            onUnmount=&#123;self => &#123;
              // 发起询问
              self.release();
            &#125;&#125;
            message=&#123;message&#125;
          />
        );
      &#125;&#125;
    </RouterContext.Consumer>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的拦截方法用的是<code>context.history.block</code>，这是在创建<strong>Router</strong>时接收的平台特有的方法，由于当前是<strong>web 环境</strong>，所以默认是<code>window.confirm</code></p>
</li>
</ul>
<h2 data-id="heading-11">2.9. BrowserRouter 与 HashRouter 对⽐</h2>
<p>之前使用<strong>vue-router</strong>遇到一个<a href="https://juejin.cn/post/6844904151206330375" target="_blank" title="https://juejin.cn/post/6844904151206330375">问题</a>，都是<strong>hash</strong>和<strong>browser</strong>的<strong>区别</strong>所导致，所以一并整理了吧</p>
<ol>
<li><strong>HashRouter</strong> 最简单，每次<strong>路由变化</strong>不需要<strong>服务端</strong>接入，根据浏览器的#的来区分 path 就可以；<strong>BrowserRouter</strong>
需要<strong>服务端</strong>解析 <strong>URL</strong> 返回页面，因此使用<strong>BrowserRouter</strong>需要在后端配置<strong>地址映射</strong>。</li>
<li><strong>BrowserRouter</strong> 触发路由变化的本质是使⽤ <strong>HTML5 history API</strong>（ <code>pushState</code>、<code>replaceState</code> 和 <code>popstate</code> 事件）</li>
<li><strong>HashRouter</strong> 不⽀持 <code>location.key</code> 和 <code>location.state</code>，<strong>动态路由</strong>需要通过<code>?</code>传递参数。</li>
<li><strong>Hash history</strong> 只需要服务端配置一个地址就可以上线，但线上的 <strong>web 应⽤</strong> 很少使用这种方式。</li>
</ol>
<h2 data-id="heading-12">2.10. MemoryRouter</h2>
<p>把 <strong>URL</strong> 的<strong>历史记录</strong>保存在内存中的，不读取、不写⼊地址栏。可以用在⾮浏览器环境，如<strong>React Native</strong>。</p>
<h1 data-id="heading-13">3. 思考与总结</h1>
<ol>
<li>
<p><strong>LifeCycle 组件</strong></p>
<p>关于组件化，在看<strong>Vue</strong>源码时给我的启发是<strong>组件化的本质是产生虚拟 dom</strong>，但看了<strong>react-router</strong>源码后发现组件还可以仅作为<strong>生命周期</strong>使用，这也确实是一种很好的逻辑方式，在类组件中一些<strong>只涉及生命周期的处理</strong>或许可以通过这种方式尝试着来实现，比如说websocket数据的接收或特定数据的处理展示。</p>
</li>
<li>
<p>跨平台</p>
<p>作为一名接触<strong>前端</strong>不久的同学，见到的第一个有<strong>跨平台</strong>思路的框架就是<strong>react</strong>，<strong>react-router</strong>也是如此，首先，<strong>源码</strong>的核心放在<strong>react-router</strong>中，目前阶段衍生出<strong>react-router-dom</strong>和<strong>react-router-native</strong>两个库，关于<strong>路由</strong>的核心处理逻辑在另一个库<code>history</code>中，<strong>react-router</strong>只关注路由如何在<strong>react</strong>中使用，具体的平台方案交给<strong>react-router-dom</strong>和<strong>react-router-native</strong>来做，这种<strong>代码低耦合</strong>的方式也是非常值得我们学习的。</p>
<p>ps：<strong>React-native</strong> 什么时候发 1.0 呢？</p>
</li>
<li>
<p><code><Route/></code>中的渲染优先级</p>
<p><code>children</code>><code>component</code>><code>render</code></p>
<p>三者能接收到同样的<code>[route props]</code>，包括 <code>match</code>、<code>location</code>和<code>history</code>，但是当<strong>不匹配</strong>时<strong>children</strong> 的 <code>match</code> 与其他二者的情况不同会是 <code>null</code>。</p>
</li>
<li>
<p>关于 <code>children</code></p>
<p>有时候，不管<strong>当前路由</strong>是否<strong>匹配</strong>我们都需要渲染⼀些内容，这时候可以⽤ <code>children</code>。参数与<code>render</code> 完全⼀样。</p>
</li>
<li>
<p>关于 <code>component</code></p>
<p>如果我们写了<code>component</code>，<strong>react</strong>会通过<code>createElement</code>创建<strong>组件</strong>，所以为了避免不必要的<strong>开销</strong>，尽量不要使用<strong>内联函数</strong></p>
</li>
</ol>
<blockquote>
<p>投稿来自 [<a href="https://juejin.cn/post/6950447819396218911" title="https://juejin.cn/post/6950447819396218911" target="_blank">【我的React笔记】 01. 战术后仰：什么是 React-Router 呀</a>](<a href="https://juejin.cn/post/6950447819396218911" target="_blank" title="https://juejin.cn/post/6950447819396218911">juejin.cn/post/695044…</a>)</p>
</blockquote></div>  
</div>
            