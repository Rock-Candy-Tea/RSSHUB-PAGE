
---
title: 'react自动化构建路由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7404d6827c845debb67ab9fb06a34c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 03:02:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7404d6827c845debb67ab9fb06a34c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">react自动化构建路由</h1>
<h2 data-id="heading-1">序</h2>
<p>在使用<code>react-router-dom</code>在编写项目的时候有种感觉就是,使用起来非常的方便,但是若是维护起来,那便是比较麻烦了,因为各大路由分散在各个组件中. 所以我们就会想到,使用<code>react-router-dom</code>中提供的<code>config</code>模式来编写我们的路由,这样写的好处就是我们可以将逻辑集中在一处,配置路由比较方便</p>
<h2 data-id="heading-2">项目地址</h2>
<p><a href="https://gitee.com/d718781500/autoRouter" target="_blank" rel="nofollow noopener noreferrer">gitee.com/d718781500/…</a></p>
<h2 data-id="heading-3">1.路由集中式</h2>
<p>我们先将下列数据定义在<code>/src/router/index.js</code>中</p>
<p>在react的路由官方文档中就提供了配置集中式路由的案例,大致是这样的仿照<code>vue</code>的路由,生成一个配置文件,预期是这样的</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//需要一个路由的配置,它是一个数组</span>
<span class="hljs-keyword">import</span> Discover <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Discover"</span>
<span class="hljs-keyword">import</span> Djradio <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Discover/Djradio"</span>
<span class="hljs-keyword">import</span> Playlist <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Discover/Playlist"</span>
<span class="hljs-keyword">import</span> Toplist <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Discover/Toplist"</span>
<span class="hljs-keyword">import</span> Friends <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Friends"</span>
<span class="hljs-keyword">import</span> Mine <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Mine"</span>
<span class="hljs-keyword">import</span> Page404 <span class="hljs-keyword">from</span> <span class="hljs-string">"../pages/Page404"</span>
<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/friends"</span>,
        <span class="hljs-attr">component</span>: Friends
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/mine"</span>,
        <span class="hljs-attr">component</span>: Mine
    &#125;,
    
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/discover"</span>,
        <span class="hljs-attr">component</span>: Discover,
        <span class="hljs-attr">children</span>: [
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/discover/djradio"</span>,
                <span class="hljs-attr">component</span>: Djradio
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/discover/playlist"</span>,
                <span class="hljs-attr">component</span>: Playlist

            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/discover/toplist"</span>,
                <span class="hljs-attr">component</span>: Toplist
            &#125;
        ]
    &#125;,
    &#123;<span class="hljs-comment">//Page404这个配置一定要在所有路由配置之后</span>
        <span class="hljs-attr">path</span>: <span class="hljs-string">"*"</span>,
        <span class="hljs-attr">component</span>: Page404
    &#125;
]

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> routes
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过上述配置,来生成一个路由.当然上述的配置也只是做了简单的处理,还有<code>redirect exact</code>等属性没有写,我们还是从一个简单的开始吧</p>
<h2 data-id="heading-4">2.文件目录</h2>
<p>上述的配置中使用了类似于vue的集中式路由配置模式,那么下面就展示下我当前这个demo的结构目录吧</p>
<h3 data-id="heading-5">项目目录结构</h3>
<p><img alt="1619084142579.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7404d6827c845debb67ab9fb06a34c3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">src/pages目录结构</h3>
<pre><code class="hljs language-js copyable" lang="js">├─Discover
│  │  abc.js
│  │  index.js
│  │
│  ├─Djradio
│  │  │  index.js
│  │  │  lf.js
│  │  │
│  │  └─gv
│  │          index.js
│  │
│  ├─Playlist
│  │      index.js
│  │
│  └─Toplist
│          index.js
│
├─Entertaiment
│      index.js
│
├─Friends
│      index.js
│      xb.js
│
├─Mine
│      index.js
│
└─Page404
        index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这些结构之后,那么在<code>1</code>中提到的引入文件结合起来看就不懵逼啦,接下来我们可以封装一个组件,给他取个名字叫做<code>CompileRouter</code>这个组件专门用于编译路由</p>
<h2 data-id="heading-7">3.创建CompileRouter</h2>
<p><img alt="1619084411039.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/039d328d530e4d568d9c092b02d0ae83~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个组件我们把它创建在<code>src/utils</code>中,作用就是通过传入的路由配置,然后计算出这个组件,那么问题来了,为什么要创建这个组件呢?</p>
<p>让我们回顾一下react路由的编写方式吧,react路由需要一个基础组件<code>HashRouter</code>或者<code>BrowserRouter</code>这两个相当于一个基石组件</p>
<p>然后还需要一个路由配方这个组件可以接受一个<code>path</code>映射一个<code>component</code></p>
<p>我们来写段伪代码来说明一下</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//引入路由基本组件(要在项目中安装 npm i react-router-dom)</span>
<span class="hljs-keyword">import</span> &#123;HashRouter <span class="hljs-keyword">as</span> Router,Route&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//基石路由</span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
            //路由配方组件 通过path匹配component
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;/</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/mine"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Mine&#125;/</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是基本用法,所以我们CompileRouter这个组件的工作就是,生成如上代码中的Route一样,生成Route然后展示在组件上</p>
<p>在了解到Compile的基本作用之后,下面我们就开始编码吧</p>
<p>我个<code>CompileRouter</code>设计是接受一个数据,这个数据必须是符合路由配置的一个数组,就像<code>1</code>里代码中所示的数组一样,接受的属性为<code>routes</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//这个文件通过routes配置来编译出路由</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; Switch, Route &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CompileRouter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>()
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">c</span>: []
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">renderRoute</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> &#123; routes &#125; = <span class="hljs-built_in">this</span>.props;<span class="hljs-comment">//获取routes路由配置</span>
        <span class="hljs-comment">//1.通过routes生成Route组件</span>
        <span class="hljs-comment">//确保routes是一个数组</span>
        <span class="hljs-comment">// console.log(routes)</span>
        <span class="hljs-comment">//render 不会重复让组件的componentDidMount和componentWillUnmount重复调用</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(routes) && routes.length > <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">//确保传入的routes是个数组</span>
           <span class="hljs-comment">// 循环迭代传入的routes</span>
            <span class="hljs-keyword">let</span> finalRoutes = routes.map(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
                <span class="hljs-comment">//每个route是这个样子的 &#123;path:"xxx",component:"xxx"&#125;</span>
                <span class="hljs-comment">//如果route有子节点 &#123;path:"xxx",component:"xxx",children:[&#123;path:"xxx"&#125;]&#125;</span>
                <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;route.path&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;route.path&#125;</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;</span>
                       // 这么写的作用就是,如果路由还有嵌套路由,那么我们可以把<span class="hljs-attr">route</span>中的<span class="hljs-attr">children</span>中的配置数据传递给这个组件,让组件再次调用<span class="hljs-attr">CompileRouter</span>的时候就能编译出嵌套路由了
                    () =></span> <span class="hljs-tag"><<span class="hljs-name">route.component</span> <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;route.children&#125;</span> /></span>
                &#125; /></span>
            &#125;)

            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">c</span>: finalRoutes
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'routes必须是一个数组,并且长度要大于0'</span>)
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">//确保首次调用renderRoute计算出Route组件</span>
        <span class="hljs-built_in">this</span>.renderRoute()
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> &#123; c &#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
                &#123;c&#125;
            <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码就是用于去处理<code>routes</code>数据并且声称这样的组件,每一步的作用我都已经在上面用注释标明了</p>
<h2 data-id="heading-8">4.使用CompileRouter</h2>
<p>其实我们可以把封装的这个组件当成是<code>vue-router</code>中的视图组件<code><router-view/></code>就暂且先这么认为吧,接下来我们需要在页面上渲染<code>1级路由了</code></p>
<p>在<code>src/app.js</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; HashRouter <span class="hljs-keyword">as</span> Router, Link &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-comment">//引入我们封装的CompileRouter罪案</span>
<span class="hljs-keyword">import</span> CompileRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils/compileRouter"</span>
<span class="hljs-comment">//引入在1中定义的路由配置数据</span>
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>
<span class="hljs-built_in">console</span>.log(routes)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/friends"</span>></span>朋友<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                |
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/discover"</span>></span>发现<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                |
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/mine"</span>></span>我的<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                &#123;/*当成是vue-router的视图组件 我们需要将路由配置数据传入*/&#125;
                <span class="hljs-tag"><<span class="hljs-name">CompileRouter</span> <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;routes&#125;</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写完后,那么页面上其实就可以完美的展示1级路由了</p>
<h2 data-id="heading-9">5.嵌套路由处理</h2>
<p>上面我们已经对1级路由进行了渲染,可以跳转,但是二级路由怎么处理呢?其实也很简单,我们只需要找到二级路由的父路由,继续使用<code>CompileRouter</code>就可以了</p>
<p>我们从配置中可以看到,<code>Discover</code>这个路由是具有嵌套路由的,所以我们就以<code>Discover</code>路由为例子,首先我们看下结构图</p>
<p><img alt="1619085810310.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03c825e5d71240f589dd23b8769f5e81~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图上的<code>index.js</code>就是<code>Discover</code>这个视图组件了,也是嵌套路由的<code>父级路由</code>,所以我们只需要在这个<code>index.js</code>中继续使用<code>CompileRouter</code>就可以了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; Link &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>

<span class="hljs-keyword">import</span> CompileRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"../../utils/compileRouter"</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Discover</span>(<span class="hljs-params">props</span>) </span>&#123;

    <span class="hljs-keyword">let</span> &#123; routes &#125; = props <span class="hljs-comment">//这个数据是从ComileRouter组件编译的时候传递过来的children</span>
    <span class="hljs-comment">// console.log(routes)</span>
    <span class="hljs-keyword">let</span> links = routes.map(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;route.path&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;route.path&#125;</span>></span>&#123;route.path&#125;<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
        )
    &#125;)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">legend</span>></span>发现<span class="hljs-tag"></<span class="hljs-name">legend</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我发现,不能说多喝热水<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                &#123;links&#125;
            <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            &#123;/*核心代码,再次使用即可 这里将通过children数据可以渲染出Route*/&#125;
            <span class="hljs-tag"><<span class="hljs-name">CompileRouter</span> <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;routes&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span></span>
    )
&#125;
Discover.meta = &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"发现"</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">""</span>
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Discover
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们以后记住,只要是有嵌套路由我们要做两件事</p>
<ol>
<li>配置routes</li>
<li>在嵌套路由的父级路由中再次使用<code>CompileRouter</code>,并且传入<code>routes</code>即可</li>
</ol>
<h2 data-id="heading-10">6. require.context</h2>
<p>上面我们实现了一个路由集中式的配置,但是我们会发现一个问题</p>
<p><img alt="1619086123220.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faf5e6c179f74dc6bdedae555e6e695f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>引入了很多的组件,实际上,在项目中引入的更多,如果一个一个引入,对我们来说是灾难性的,所以我们可以使用<code>webpack</code>提供的一个很好用的api,<code>require.context</code>我们先说说它是怎么使用的吧</p>
<p>自动化导入<code>require.context</code>方法,使用这个方法可以减少繁琐的组件引入,而且可以深度的递归目录,做到import做不到的事情 下面我们来看一下这个方法是如何使用的</p>
<h3 data-id="heading-11">使用</h3>
<p>你可以通过 <code>require.context()</code> 函数来创建自己的 context。</p>
<p>可以给这个函数传入4个参数：</p>
<ol>
<li>
<p>一个要搜索的目录，</p>
</li>
<li>
<p>一个标记表示是否还要搜索其子目录，</p>
</li>
<li>
<p>一个匹配文件的正则表达式。</p>
</li>
<li>
<p>mode  模块加载模式，常用值为 sync、lazy、lazy-once、eager</p>
<ul>
<li>
<p><code>sync</code> 直接打包到当前文件，同步加载并执行</p>
<p><code>lazy</code> 延迟加载会分离出单独的 chunk 文件</p>
<p><code>lazy-once</code> 延迟加载会分离出单独的 chunk 文件，加载过下次再加载直接读取内存里的代码。</p>
<p><code>eager</code> 不会分离出单独的 chunk 文件，但是会返回 promise，只有调用了 promise 才会执行代码，可以理解为先加载了代码，但是我们可以控制延迟执行这部分代码。</p>
</li>
</ul>
</li>
</ol>
<p>webpack 会在构建中解析代码中的 <code>require.context()</code> 。</p>
<p>语法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>.context(
  directory,
  (useSubdirectories = <span class="hljs-literal">true</span>),
  (regExp = <span class="hljs-regexp">/^\.\/.*$/</span>),
  (mode = <span class="hljs-string">'sync'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>.context(<span class="hljs-string">'./test'</span>, <span class="hljs-literal">false</span>, <span class="hljs-regexp">/\.test\.js$/</span>);
<span class="hljs-comment">//（创建出）一个 context，其中文件来自 test 目录，request 以 `.test.js` 结尾。</span>
<span class="hljs-built_in">require</span>.context(<span class="hljs-string">'../'</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.stories\.js$/</span>);
<span class="hljs-comment">// （创建出）一个 context，其中所有文件都来自父文件夹及其所有子级文件夹，request 以 `.stories.js` 结尾。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">api</h3>
<p>函数有三个属性：<code>resolve</code>, <code>keys</code>, <code>id</code>。</p>
<ul>
<li>
<p><code>resolve</code> 是一个函数，它返回 request 被解析后得到的模块 id。</p>
</li>
<li>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"..."</span>,<span class="hljs-literal">true</span>,<span class="hljs-string">"xxx"</span>)
p.resolve(<span class="hljs-string">"一个路径"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>keys</code> 也是一个函数，它返回一个数组，由所有可能被此 context module 处理的请求（译者注：参考下面第二段代码中的 key）组成。</p>
</li>
</ul>
<p><code>require.context</code>的返回值是一个函数,我们可以在函数中传入文件的路径,就可以得到模块化的组件了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> components = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">'../pages'</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>, <span class="hljs-string">'sync'</span>)

<span class="hljs-keyword">let</span> paths = components.keys()<span class="hljs-comment">//获得了所有引入文件的地址</span>
<span class="hljs-comment">// console.log(paths)</span>
<span class="hljs-keyword">let</span> routes = paths.map(<span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
    <span class="hljs-keyword">let</span> component = components(path).default
    path = path.substr(<span class="hljs-number">1</span>).replace(<span class="hljs-regexp">/\/\w+\.js$/</span>,<span class="hljs-string">""</span>)
    <span class="hljs-keyword">return</span> &#123;
        path,
        component
    &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(routes)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">总结</h3>
<p>虽然上面有很多api和返回的值,我们只拿两个来做说明</p>
<ol>
<li>
<p>keys方法,这个可以获取所有模块的路径,返回的是一个数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"../pages"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>);

<span class="hljs-keyword">let</span> paths = context.keys()<span class="hljs-comment">//获取了所有文件的路径</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取路径下所有的模块</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"../pages"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>);

<span class="hljs-keyword">let</span> paths = context.keys()<span class="hljs-comment">//获取了所有文件的路径</span>

<span class="hljs-keyword">let</span> routes = paths.map(<span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
    <span class="hljs-comment">//批量获取引入的组件</span>
    <span class="hljs-keyword">let</span> component = context(path).default;
    <span class="hljs-built_in">console</span>.log(component)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>掌握这两个就可以了,下面我们来继续处理</p>
<h2 data-id="heading-14">7.扁平数据转换为树形结构的(convertTree算法)</h2>
<p>这个算法的名字是我自己起的,首先我们要明白为甚么需要将数据转换成tree</p>
<p>我们的预期的<code>routes</code>数据应该是下面这样的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//目的是什么?</span>
<span class="hljs-comment">//生成一个路由配置</span>
 <span class="hljs-keyword">const</span> routes = [
     &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">""</span>,
         <span class="hljs-attr">component</span>:xxx
          <span class="hljs-attr">children</span>:[
                 &#123;
                     <span class="hljs-attr">path</span>:<span class="hljs-string">"xxx"</span>
                     <span class="hljs-attr">component</span>:xxx
                 &#125;
            ]
     &#125;
 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但其实我们使用<code>require.context</code>处理之后的数据是这样的</p>
<p><img alt="1619087189929.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f81fef80f4114679a37a7b71e67b29ab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到这个数据是完全<code>扁平化</code>的,没有任何的嵌套,所以我们第一步就是要实现将这种扁平化的数据转换为符合我们预期的<code>树形</code>结构,下面我们一步一步来</p>
<h3 data-id="heading-15">7.1使用require.context将数据处理成扁平化</h3>
<p>首先要处理成上图那样的结构,代码都有注释,难度也不高</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//require.context()</span>

<span class="hljs-comment">// 1. 一个要搜索的目录，</span>
<span class="hljs-comment">// 2. 一个标记表示是否还要搜索其子目录， </span>
<span class="hljs-comment">// 3. 一个匹配文件的正则表达式。</span>
<span class="hljs-keyword">let</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"../pages"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>);

<span class="hljs-keyword">let</span> paths = context.keys()<span class="hljs-comment">//获取了所有文件的路径</span>


<span class="hljs-keyword">let</span> routes = paths.map(<span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
    <span class="hljs-comment">//批量获取引入的组件</span>
    <span class="hljs-keyword">let</span> component = context(path).default;
    <span class="hljs-comment">//组件扩展属性方便渲染菜单</span>
    <span class="hljs-keyword">let</span> meta = component[<span class="hljs-string">'meta'</span>] || &#123;&#125;
    <span class="hljs-comment">//console.log(path)</span>
    <span class="hljs-comment">//这个正则的目的</span>
    <span class="hljs-comment">//因为地址是./Discover/Djradio/index.js这种类型的并不能直接使用,所以要进行处理</span>
    <span class="hljs-comment">//1.接去掉最前的"." 得到的结果是/Discover/Djradio/index.js</span>
    <span class="hljs-comment">//2.处理了还是不能直接用 因为我们的预期/Discover/Djradio,所以通过正则将index.js干掉了</span>
    <span class="hljs-comment">//3.有可能后面的路径不是文件夹 得到的结果是/Discover/abc.js,后缀名并不能用到路由配置的path属性中,所以.js后缀名又用正则替换掉</span>
    path = path.substr(<span class="hljs-number">1</span>).replace(<span class="hljs-regexp">/(\/index\.js|\.js)$/</span>, <span class="hljs-string">""</span>)
    <span class="hljs-comment">// console.log(path)</span>
    <span class="hljs-keyword">return</span> &#123;
        path,
        component,
        meta
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">7.2 实现convertTree算法</h3>
<p>上面处理好了数据后,我们封装一个方法,专门用于处理扁平化数据变成树形数据,算法<code>时间复杂度为O(n^2)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convertTree</span>(<span class="hljs-params">routes</span>) </span>&#123;
    <span class="hljs-keyword">let</span> treeArr = [];
    <span class="hljs-comment">//1.处理数据 将每条数据的id和parent处理好 (俗称 爸爸去哪儿了)</span>
    routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-keyword">let</span> comparePaths = route.path.substr(<span class="hljs-number">1</span>).split(<span class="hljs-string">"/"</span>)
        <span class="hljs-comment">// console.log(comparePaths)</span>
        <span class="hljs-keyword">if</span> (comparePaths.length === <span class="hljs-number">1</span>) &#123;
            <span class="hljs-comment">//说明是根节点,根节点不需要添加parent_id</span>
            route.id = comparePaths.join(<span class="hljs-string">""</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">//说明具有父节点</span>
            <span class="hljs-comment">//先处理自己的id</span>
            route.id = comparePaths.join(<span class="hljs-string">""</span>);
            <span class="hljs-comment">//comparePaths除去最后一项就是parent_id</span>
            comparePaths.pop()
            route.parent_id = comparePaths.join(<span class="hljs-string">""</span>)
        &#125;
    &#125;)
    <span class="hljs-comment">//2.所有的数据都已经找到了父节点的id,下面才是真正的找父节点了</span>
    routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-comment">//判断当前的route有没有parent_id</span>
        <span class="hljs-keyword">if</span> (route.parent_id) &#123;
            <span class="hljs-comment">//有父节点</span>
            <span class="hljs-comment">//id===parent_id的那个route就是当前route的父节点</span>
            <span class="hljs-keyword">let</span> target = routes.find(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.id === route.parent_id);
            <span class="hljs-comment">//判断父节点有没有children这个属性</span>
            <span class="hljs-keyword">if</span> (!target.children) &#123;
                target.children = []
            &#125;
            target.children.push(route)
        &#125; <span class="hljs-keyword">else</span> &#123;
            treeArr.push(route)
        &#125;
    &#125;)

    <span class="hljs-keyword">return</span> treeArr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述处理之后就可以得到树形结构啦</p>
<p><img alt="1619087541773.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064d62414b4b454a8612056ed2ca0970~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来我们只需要把数据导出去,在app上引入传递给<code>CompileRouter</code>组件就可以了</p>
<h3 data-id="heading-17">7.3 以后要注意的</h3>
<p>以后只需要在pages中创建文件即可自动实现路由的处理以及编译了,不过对于嵌套级别的路由咱们别忘了要在路由组件加上CompileRouter组件,总结为亮点</p>
<ol>
<li>创建路由页面</li>
<li>嵌套路由的父级路由组件中加入</li>
</ol>
<h2 data-id="heading-18">8.扩展静态属性</h2>
<p>我们当前创建出来的效果是有了,但是如果我们用于渲染<code>菜单</code>的时候就会有问题,没有内容可以用于渲染菜单,所以我们可以给组件上扩展<code>静态属性meta(也可以是别的)</code>,然后对我们的自动化编译代码做一些小小的改动就行了</p>
<h3 data-id="heading-19">组件</h3>
<p><img alt="1619087849957.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f48d4bf2fca4d43ac21784d850d52df~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">自动化处理逻辑完整代码</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//require.context()</span>

<span class="hljs-comment">// 1. 一个要搜索的目录，</span>
<span class="hljs-comment">// 2. 一个标记表示是否还要搜索其子目录， </span>
<span class="hljs-comment">// 3. 一个匹配文件的正则表达式。</span>
<span class="hljs-keyword">let</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"../pages"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>);

<span class="hljs-keyword">let</span> paths = context.keys()<span class="hljs-comment">//获取了所有文件的路径</span>


<span class="hljs-keyword">let</span> routes = paths.map(<span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
    <span class="hljs-comment">//批量获取引入的组件</span>
    <span class="hljs-keyword">let</span> component = context(path).default;
    <span class="hljs-comment">//组件扩展属性方便渲染菜单</span>
    <span class="hljs-keyword">let</span> meta = component[<span class="hljs-string">'meta'</span>] || &#123;&#125;
    <span class="hljs-comment">//console.log(path)</span>
    <span class="hljs-comment">//这个正则的目的</span>
    <span class="hljs-comment">//因为地址是./Discover/Djradio/index.js这种类型的并不能直接使用,所以要进行处理</span>
    <span class="hljs-comment">//1.接去掉最前的"." 得到的结果是/Discover/Djradio/index.js</span>
    <span class="hljs-comment">//2.处理了还是不能直接用 因为我们的预期/Discover/Djradio,所以通过正则将index.js干掉了</span>
    <span class="hljs-comment">//3.有可能后面的路径不是文件夹 得到的结果是/Discover/abc.js,后缀名并不能用到路由配置的path属性中,所以.js后缀名又用正则替换掉</span>
    path = path.substr(<span class="hljs-number">1</span>).replace(<span class="hljs-regexp">/(\/index\.js|\.js)$/</span>, <span class="hljs-string">""</span>)
    <span class="hljs-comment">// console.log(path)</span>
    <span class="hljs-keyword">return</span> &#123;
        path,
        component,
        meta
    &#125;
&#125;)
<span class="hljs-comment">//这种数据是扁平化的数据,并不符合我们的路由规则</span>
<span class="hljs-comment">//需要做算法 尽可能将时间复杂度降低o(n)最好</span>
<span class="hljs-comment">//封装一个convertTree算法 时间复杂度o(n^2)</span>
<span class="hljs-comment">// console.log(routes)</span>

<span class="hljs-comment">//id</span>
<span class="hljs-comment">//parent_id</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convertTree</span>(<span class="hljs-params">routes</span>) </span>&#123;
    <span class="hljs-keyword">let</span> treeArr = [];
    <span class="hljs-comment">//1.处理数据 将每条数据的id和parent处理好 (俗称 爸爸去哪儿了)</span>
    routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-keyword">let</span> comparePaths = route.path.substr(<span class="hljs-number">1</span>).split(<span class="hljs-string">"/"</span>)
        <span class="hljs-comment">// console.log(comparePaths)</span>
        <span class="hljs-keyword">if</span> (comparePaths.length === <span class="hljs-number">1</span>) &#123;
            <span class="hljs-comment">//说明是根节点,根节点不需要添加parent_id</span>
            route.id = comparePaths.join(<span class="hljs-string">""</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">//说明具有父节点</span>
            <span class="hljs-comment">//先处理自己的id</span>
            route.id = comparePaths.join(<span class="hljs-string">""</span>);
            <span class="hljs-comment">//comparePaths除去最后一项就是parent_id</span>
            comparePaths.pop()
            route.parent_id = comparePaths.join(<span class="hljs-string">""</span>)
        &#125;
    &#125;)
    <span class="hljs-comment">//2.所有的数据都已经找到了父节点的id,下面才是真正的找父节点了</span>
    routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-comment">//判断当前的route有没有parent_id</span>
        <span class="hljs-keyword">if</span> (route.parent_id) &#123;
            <span class="hljs-comment">//有父节点</span>
            <span class="hljs-comment">//id===parent_id的那个route就是当前route的父节点</span>
            <span class="hljs-keyword">let</span> target = routes.find(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.id === route.parent_id);
            <span class="hljs-comment">//判断父节点有没有children这个属性</span>
            <span class="hljs-keyword">if</span> (!target.children) &#123;
                target.children = []
            &#125;
            target.children.push(route)
        &#125; <span class="hljs-keyword">else</span> &#123;
            treeArr.push(route)
        &#125;
    &#125;)

    <span class="hljs-keyword">return</span> treeArr
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> convertTree(routes)


<span class="hljs-comment">//获取一个模块</span>
<span class="hljs-comment">// console.log(p("./Discover/index.js").default)</span>

<span class="hljs-comment">//目的是什么?</span>
<span class="hljs-comment">//生成一个路由配置</span>
<span class="hljs-comment">// const routes = [</span>
<span class="hljs-comment">//     &#123;</span>
<span class="hljs-comment">//         path: "",</span>
<span class="hljs-comment">//         component,</span>
<span class="hljs-comment">//          children:[</span>
<span class="hljs-comment">//                 &#123;path component&#125;</span>
<span class="hljs-comment">//             ]</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">写在最后</h2>
<p>其实上述的处理并不能作为<code>应用级别</code>用于项目中,主要在于<code>CompileRouter</code>处理的不够细致,下一期我将专门写一篇如何处理<code>CompileRouter</code>用于<code>鉴权</code>等应用在项目中</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            