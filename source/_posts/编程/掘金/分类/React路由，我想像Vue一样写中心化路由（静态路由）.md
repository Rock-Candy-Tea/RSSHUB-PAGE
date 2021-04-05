
---
title: 'React路由，我想像Vue一样写中心化路由（静态路由）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c9db83c4f84f1b9ff5b6ebcb8ddfe0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 04:58:37 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c9db83c4f84f1b9ff5b6ebcb8ddfe0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>最近开始学习React的， 作为一只从Vue转世而来的React萌新，首当其冲的但就是对路由的执着了， Vue在路由这一块的中心化，以及父子路由用的太顺手了， 一下子接受不了React教程中的路由写法， 所以想在React中也实现中心化的路由。</p>
<blockquote>
<p>最后的做法可以通过右侧目录直达。</p>
</blockquote>
<blockquote>
<p>评论区可以用来讨论，也欢迎大手子斧正文中的错误。</p>
</blockquote>
<blockquote>
<p>实际开发中，落地一个功能肯定是有用处或者深意的，比如左侧点赞的功能。</p>
</blockquote>
<h2 data-id="heading-1">二、React推荐的路由写法</h2>
<p><a href="http://react-guide.github.io/react-router-cn/docs/guides/basics/RouteConfiguration.html" target="_blank" rel="nofollow noopener noreferrer">教程可以看这里</a></p>
<p>通过教程可以看出，首先React是建议在当前文件中非公用组件，通过React的React.createClass方法生成一个组件类，或者可以直接写成一个方法。</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 组件类</span>
<span class="hljs-keyword">const</span> Message = React.createClass(&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Message &#123;this.props.params.id&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
  &#125;
&#125;)
<span class="hljs-comment">// 直接写成函数， 上写成组件类的写法类似。</span>
<span class="hljs-keyword">const</span> Index = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.fragment</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span></this is Index>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about/>About</Link>
        </React.fragment></span></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面这一段是因为我初用的时候就仿佛写Vue一样，在当前文件的根节点里写了太多的html，导致代码臃肿，希望看到本文的其他React萌新，能注意下这一点。</p>
</blockquote>
<p>回到主题，React4开始，对路由进行了革命性的创新，让路由更符合React的“组件化”思想，从React3及之前的“中心化路由”（或称“静态”路由）改为“去中心化路由”（“动态路由”）。</p>
<p>而我很头铁，就是想在React新版本也用“中心化路由”，理由是好管理，路由清晰。<strong>（其实就是有点脑子轴了）</strong></p>
<h2 data-id="heading-2">三、“中心化路由”写法</h2>
<p>其实最开始， 是没有认真看完教程，对React的“组件化”思想理解不是很透彻，认为“组件化”是开发者的事，而框架还是停留在Vue，所以选择了“中心化路由”写法。 写法也很简单，如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/route.js</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/index/index'</span>;
<span class="hljs-keyword">import</span> HomeNews <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/index/component/HomeNews'</span>;
<span class="hljs-keyword">import</span> My <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/my/my'</span>;

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/my"</span>,
    <span class="hljs-attr">component</span>: My
  &#125;,&#123; <span class="hljs-comment">// 路由是从新闻页的路由开始写的，首页默认显示的组件在下面，需要在首页文件中判断。</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">component</span>: Home,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/news"</span>,
        <span class="hljs-attr">component</span>: HomeNews
      &#125;
    ]
  &#125;
]

<span class="hljs-keyword">export</span> &#123;
  routes
&#125;

<span class="hljs-comment">// src/index.jsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> reportWebVitals <span class="hljs-keyword">from</span> <span class="hljs-string">'./reportWebVitals'</span>;

<span class="hljs-keyword">import</span> &#123;routes&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./route'</span>;
<span class="hljs-keyword">import</span> &#123;BrowserRouter&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>;
<span class="hljs-keyword">import</span> &#123;renderRoutes&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-config'</span>;

ReactDOM.render(
  (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
      &#123;renderRoutes(routes)&#125;
    <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>
  ),
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);

<span class="hljs-comment">// If you want to start measuring performance in your app, pass a function</span>
<span class="hljs-comment">// to log results (for example: reportWebVitals(console.log))</span>
<span class="hljs-comment">// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals</span>
reportWebVitals();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完上面的代码，应该有小伙伴会疑惑，我为什么把默认路由（“/”）写在最下面，是因为我先开发的个人中心吗？</p>
<p>当然不是，是因为React路由匹配的原因。</p>
<p><strong>在React中，路由默认是模糊匹配的，如果我写在上面，会导致个人中心的路由优先匹配到首页路由。</strong></p>
<p><strong>如果我给首页路由加上exact强匹配，会导致期望的父子组件无效</strong></p>
<p><strong>所以把首页路由写在最下面是无奈之举。</strong></p>
<p>如果有小伙伴也希望在React中采用“中心化路由”的话，那么就需要考虑其中的取舍了，因为还有一个小细节，也是需要注意的。</p>
<p>项目中， Web的首页通常是顶部（Header）不动，下面的内容区（Main）随导航栏动态切换。</p>
<p>比如掘金，红框区域不会变更， 绿框部分随导航栏（首页路由）切换而动态加载。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c9db83c4f84f1b9ff5b6ebcb8ddfe0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>掘金的绿框部分只是类容不同，而工作中，许多项目的绿框（Main）部分是布局也大不相同的，包括后台管理平台也是如此。</strong></p>
<p>所以我在首页中加入了路由判断，以此来确认渲染那一部分的组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/pages/index/index.jsx</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">route</span>: props.route
    &#125;
  &#125;

  <span class="hljs-comment">// 判断用户访问地址，确认加载组件</span>
  <span class="hljs-function"><span class="hljs-title">getPath</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-keyword">let</span> route = <span class="hljs-built_in">this</span>.props.location.pathname
    <span class="hljs-keyword">return</span> route === <span class="hljs-string">'/'</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> route = <span class="hljs-built_in">this</span>.state.route;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span>`$&#123;<span class="hljs-attr">s</span>['<span class="hljs-attr">main</span>']&#125;`&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">HeaderTop</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
         &#123;/*默认路由时加载首页组件， 否则按路由加载组件*/&#125;
          &#123;this.getPath() ? <span class="hljs-tag"><<span class="hljs-name">HomeMain</span> /></span> : renderRoutes(route.children)&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Footer</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，基本就是我写的“中心化路由”的全部思路及细节了。</p>
<h2 data-id="heading-3">四、总结</h2>
<p>如果此时你项目刚刚开始，只是在犹豫、或者寻找怎么在React中写“中心化路由”的话，我希望你能在看看<a href="http://react-guide.github.io/react-router-cn/docs/guides/basics/RouteConfiguration.html" target="_blank" rel="nofollow noopener noreferrer">这篇教程</a>，好好理解下教程中路由的写法， 然后按照<strong>教程中的“去中心化路由”写法在React去写路由。</strong></p>
<p>或许你也觉得这种写法挺难受的，尤其是如果你也和我一样，刚刚从Vue转世过来，但我希望你能试着去接受它。</p>
<p>但不是说你不能写“中心化路由”，当然可以的，这篇文章最详细讲的就是我怎么在React中写的“中心化路由”。 而“去中心化路由”按照官网的模式去写就可以了。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            