
---
title: '前端路由及React-Router解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447d51567c9a428faabebbde2d001a46~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 02:06:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447d51567c9a428faabebbde2d001a46~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前前言</h2>
<p>本文来自推啊前端团队 刘爽 同学，主要介绍一下 前端路由相关内容和解读一下React-Router源码。欢迎在评论区讨论哦！！！</p>
<h2 data-id="heading-1">什么是路由</h2>
<p>通常会在网络工程里面听到路由这个词，前端工程化后路由的概念用语页面的跳转，浏览器监测到路由的变化在页面显示路由所对应的页面。在早期，路由的概念时根据URL的变更重新渲染页面布局和内容的过程，而且这个过程时由服务器端实现的。他所描述的是URL 和 函数之间的映射关系。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447d51567c9a428faabebbde2d001a46~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在web前端的单页面应用，路由描述的是URL 与 UI 之间的映射关系。这种映射关系显著的特点是<strong>URL的改变不会引起页面的刷新。</strong>
**</p>
<h2 data-id="heading-2">两种路由方式</h2>
<p>在前面也说了web前端路由的特点，URL 改变的目的是为了更新UI，与此同时不能够刷新页面，想要更新页面视图UI，我们就需要监听 URL 的变化。所以在前端实现路由引擎需要注意两点</p>
<ol>
<li>URL 的改变不刷页面，</li>
<li>如何监听 URL 的改变</li>
</ol>
<p>在前端领域有两种路由方式能够实现以上标准</p>
<h3 data-id="heading-3">hash 路由</h3>
<p>hash 路由就是我们常说的<strong>锚点</strong>。即在URL后面添加#，# 号后面就是hash路由部分。可以通过监听事件监听hash路由的变化</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"hashchange"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"路由改变"</span>)
&#125;)

<span class="hljs-built_in">window</span>.onhashchange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"路由改变"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">history 路由</h3>
<p>history对象表示，当前窗口用户的导航记录，该对象不会向外暴露用户访问过的URL，但是可以通过方法实现前进和后退。HTML5 添加了新方法 pushState和replaceState，表示添加和替换历史记录的条目，语法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">history.pushState(state, title[, url])
history.replaceState(state, title[, url])
- state: 一个于指定网址相关的状态对象，popstate事件触发时，该对象会传入回调函数中。如果不需要这个对象，此处可以填<span class="hljs-literal">null</span>
- title: 当前大多数浏览器都忽略此参数
- url: 新历史记录条目的URL由此参数指定，新网址必须与当前网址同源
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过popstate监听路由改变</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"路由改变"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">React-Router</h2>
<p>这一栏我们只讨论源码，对应的版本是5.2
history：负责浏览器页面，链接改变通知当前页面location对象发生了改变，开发者根据变化渲染内容。
Router：负责监听页面对象发生了改变，并开始重新渲染页面
Route：页面开始渲染后，根据具体的页面location信息展示具体路由地址对应的内容。</p>
<h3 data-id="heading-6">BrowserRouter 和 Router</h3>
<p>最开始使用 react-router 的时候需要的方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createBrowserHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'history'</span>
<span class="hljs-keyword">import</span> &#123; Router &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router'</span>

<span class="hljs-keyword">const</span> BrowserRouter = React.cloneElement(Router, &#123; <span class="hljs-attr">history</span>: createBrowserHistory() &#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
  ...
  <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>
)
<span class="hljs-comment">// 或者</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span> <span class="hljs-attr">history</span>=<span class="hljs-string">&#123;createBrowserHistory()&#125;</span>></span>
  ...
  <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>react-router V4 版本之后可以直接使用 BrowserRouter 如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; BrowserRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
  ...
  <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BrowserRouter 相关源码如下:
可以看到 BrowserRouter 就是对 Router 组件的一层封装，传入history 属性。其主要部分还是Router的源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/react-router-dom/modules/BrowserRouter.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BrowserRouter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  history = createHistory(<span class="hljs-built_in">this</span>.props);

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span> <span class="hljs-attr">history</span>=<span class="hljs-string">&#123;this.history&#125;</span> <span class="hljs-attr">children</span>=<span class="hljs-string">&#123;this.props.children&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/react-router/modules/Router.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Router</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">computeRootMatch</span>(<span class="hljs-params">pathname</span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>, <span class="hljs-attr">url</span>: <span class="hljs-string">"/"</span>, <span class="hljs-attr">params</span>: &#123;&#125;, <span class="hljs-attr">isExact</span>: pathname === <span class="hljs-string">"/"</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);

    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-comment">// BrowserRouter 传入的 history</span>
      <span class="hljs-attr">location</span>: props.history.location
    &#125;;

    <span class="hljs-keyword">if</span> (!props.staticContext) &#123;
      <span class="hljs-comment">// 监听URL是否改变</span>
      <span class="hljs-built_in">this</span>.unlisten = props.history.listen(<span class="hljs-function"><span class="hljs-params">location</span> =></span> &#123;
        <span class="hljs-comment">// 这里的内容不影响整体逻辑</span>
      &#125;);
    &#125;
  &#125;

  <span class="hljs-comment">// 使用上下文把history location 等信息传入到children</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Provider</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span>
          <span class="hljs-attr">history:</span> <span class="hljs-attr">this.props.history</span>,
          <span class="hljs-attr">location:</span> <span class="hljs-attr">this.state.location</span>,
          <span class="hljs-attr">match:</span> <span class="hljs-attr">Router.computeRootMatch</span>(<span class="hljs-attr">this.state.location.pathname</span>),
          <span class="hljs-attr">staticContext:</span> <span class="hljs-attr">this.props.staticContext</span>
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
<p>**总结：**根据源码可以看到 Router 处理的内容并不多，1. 定义一个上下文把相关信息传入children；2. 监听URL的变化改变当前的state。</p>
<h3 data-id="heading-7">Route</h3>
<p>Route 的源码也十分简单，根据传入的信息匹配要显示的页面，如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/react-router/modules/Route.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Route</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// Consumer 上下文，用于接手上文传入信息</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <RouterContext.Consumer>
        &#123;context => &#123;
          invariant(context, "You should not use <Route> outside a <Router>");
// location 信息 如果用户传入使用用户传入信息，否则使用Provider 传入
          const location = this.props.location || context.location;
    // 核心内容：根据URL路径匹配
    // match: &#123;path,url,isExact,params&#125;
    // 如果没有匹配到 就是上文的 computeRootMatch 内容
          const match = this.props.computedMatch
            ? this.props.computedMatch // <Switch> already computed the match for us
            : this.props.path
            ? matchPath(location.pathname, this.props)
            : context.match;
    
    // 这里略过了一些判断... 

    let &#123; children, component, render &#125; = this.props;
// 开始渲染 children, 一共有三种渲染的方式
    // 1. <Route exact path="/" component=&#123;Home&#125; />
    // 2. <Route exact path="/" render=&#123;props=>&#123;return <Home />&#125;&#125; />
    // 3. <Route exact path="/"><Home /> </Route>
          return (
            <RouterContext.Provider value=&#123;props&#125;>
              &#123;props.match
                ? children
                  ? typeof children === "function"
                    ? children(props)
                    : children
                  : component
                  ? React.createElement(component, props)
                  : render
                  ? render(props)
                  : null
                : typeof children === "function"
                ? children(props)
                : null&#125;
            </RouterContext.Provider>
          );
        &#125;&#125;
      </RouterContext.Consumer>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**总结：**Route 就是用来渲染组件的，根据匹配的URL 即 Route 的path 属性，匹配出需要渲染的内容。在渲染时有三种方式 <code>render</code> <code>component</code> <code>children</code> 。在里面使用三目运算，写了很长，其实并不难理解。先判断有没有children，在判断chidren 是不是一个函数，这是渲染children的逻辑，如果没有children 判断有没有component ，最后判断有没有render方法。</p>
<h3 data-id="heading-8">Switch</h3>
<p>如果 Route 组件被 Switch 包裹，那么匹配到的URL 会返回 被包裹的Route 的第一个匹配到的元素。核心代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/react-router/modules/Switch.js</span>
React.Children.forEach(<span class="hljs-built_in">this</span>.props.children, <span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (match == <span class="hljs-literal">null</span> && React.isValidElement(child)) &#123;
    element = child;

    <span class="hljs-keyword">const</span> path = child.props.path || child.props.from;

    match = path
      ? matchPath(location.pathname, &#123; ...child.props, path &#125;)
    : context.match;
  &#125;
&#125;);

<span class="hljs-keyword">return</span> match
  ? React.cloneElement(element, &#123; location, <span class="hljs-attr">computedMatch</span>: match &#125;)
: <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**总结：**Switch 里面的内容并不多，就是把包裹的Route做了一个遍历，返回第一个匹配到的内容</p>
<h2 data-id="heading-9">总结：</h2>
<p>整体来讲react-router 的源码并不是很难理解，都是一些简单的判断。相对于这一篇内容，对于react-router的如何使用并没有介绍，只是对源码做一个简单的解读。下一篇就实现一个简易版react-router。实现前文所介绍的api。</p></div>  
</div>
            