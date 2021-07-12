
---
title: '按照vue的用法封装react路由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3780'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 00:28:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=3780'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>习惯了vue的小伙伴可能对react中路由的使用感到不习惯。在vue中，我们可以下面的方式配置路由并绑定组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
<span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
<span class="hljs-attr">routes</span>: [
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
<span class="hljs-attr">redirect</span>: &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>
&#125;
&#125;,
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/index'</span>,
<span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>,
<span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/Index.vue'</span>),
<span class="hljs-attr">children</span>: [
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/interviewRecord'</span>,
<span class="hljs-attr">name</span>: <span class="hljs-string">'interviewRecord'</span>,
<span class="hljs-attr">meta</span>: &#123;
<span class="hljs-attr">isLogin</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">title</span>: <span class="hljs-string">'面试记录'</span>
&#125;,
<span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/interviewRecord/Index.vue'</span>),
&#125;,

]
&#125;,
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
<span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
<span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/Login.vue'</span>)
&#125;
]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在页面中用<code><vue-router></code>给路由组件占位。这使得不同页面的嵌套路由结构十分直观地展现在Router的配置中</p>
<p>而在react中，我们需要在页面组件中引入并绑定路由组件，比如这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; BrowserRouter, Link, Switch, Route &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;
<span class="hljs-keyword">import</span> Category <span class="hljs-keyword">from</span> <span class="hljs-string">"./category"</span>;
<span class="hljs-keyword">import</span> User <span class="hljs-keyword">from</span> <span class="hljs-string">"./user"</span>;
<span class="hljs-keyword">import</span> Article <span class="hljs-keyword">from</span> <span class="hljs-string">"./article"</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"home"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"header"</span>></span>头部<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"left"</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/category"</span>></span>栏目管理<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/article"</span>></span>文章管理<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/user"</span>></span>用户管理<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                        <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"right"</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/category"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Category&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/article"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Article&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/user"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;User&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
                        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>
        );
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Home;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我个人并不喜欢这种方式，如果存在多级的嵌套路由，则需要在多个页面中引入组件绑定路由。这使得路由组件之间的关系显得不那么直观，所以我自己按照vue-router的用法封装了react的路由。</p>
<h1 data-id="heading-1">封装</h1>
<h2 data-id="heading-2">配置文件</h2>
<p>我们先按照vue-router的配置，将react的路由也抽象成一个列表。比如下面这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Article <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/article/Index"</span>;
<span class="hljs-keyword">import</span> Category <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/category/Index"</span>;
<span class="hljs-keyword">import</span> User <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/user/Index"</span>;
<span class="hljs-keyword">import</span> Index <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/index/Index"</span>;
<span class="hljs-keyword">import</span> Login <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/login/Index"</span>;
<span class="hljs-keyword">import</span> ArticlePassed <span class="hljs-keyword">from</span> <span class="hljs-string">"@v/article/passed/Index"</span>;

<span class="hljs-keyword">const</span> router = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/login"</span>,
        <span class="hljs-attr">component</span>: Login,
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
        <span class="hljs-attr">component</span>: Index,
        <span class="hljs-attr">children</span>: [
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/article"</span>,
                <span class="hljs-attr">component</span>: Article,
                <span class="hljs-attr">children</span>: [
                    &#123;
                        <span class="hljs-attr">path</span>: <span class="hljs-string">"/article/passed"</span>,
                        <span class="hljs-attr">component</span>: ArticlePassed,
                    &#125;,
                ],
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/category"</span>,
                <span class="hljs-attr">component</span>: Category,
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/user"</span>,
                <span class="hljs-attr">component</span>: User,
            &#125;,
        ],
    &#125;,
];
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">封装的路由组件</h2>
<p>有了这个配置列表，我们需要一个组件能将这个配置列表转化为react能认识的<code><Route></code>组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Route, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;

<span class="hljs-keyword">const</span> RouterView = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
            &#123;props.routes.map((item, index) => &#123;
                return (
                    <span class="hljs-tag"><<span class="hljs-name">Route</span>
                        <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>
                        <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;item.path&#125;</span>
                        <span class="hljs-attr">exact</span>=<span class="hljs-string">&#123;item.exact&#125;</span>
                        <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;(routeProps)</span> =></span> &#123;
                            // 判断是否存在子路由
                            if (item.children) &#123;
                                return <span class="hljs-tag"><<span class="hljs-name">item.component</span> &#123;<span class="hljs-attr">...routeProps</span>&#125; <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;item.children&#125;</span> /></span>;
                            &#125; else &#123;
                                return <span class="hljs-tag"><<span class="hljs-name">item.component</span> &#123;<span class="hljs-attr">...routeProps</span>&#125; /></span>;
                            &#125;
                        &#125;&#125;
                    />
                );
            &#125;)&#125;
        <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span></span>
    );
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> RouterView;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置列表遍历的时候，对于存在子路由的组件，我们需要将该路由的children传递给该组件。</p>
<h2 data-id="heading-4">使用</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; BrowserRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;
<span class="hljs-keyword">import</span> RouterView <span class="hljs-keyword">from</span> <span class="hljs-string">"../router/index"</span>;
<span class="hljs-keyword">import</span> config <span class="hljs-keyword">from</span> <span class="hljs-string">"../router/config"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"antd/dist/antd.css"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">RouterView</span> <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;config&#125;</span> /></span>
                <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用时，我们只需要引入封装的RouterView组件和配置列表config，存在子路由时，我们需要在该组件中再次引入RouterView，并将传递过来的子路由信息赋给组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; routes &#125; = <span class="hljs-built_in">this</span>.props;
        <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterView</span> <span class="hljs-attr">routes</span>=<span class="hljs-string">&#123;routes&#125;</span> /></span></span>
        ）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就获得一个使用方式和vue-router基本一致的react路由组件。</p>
<h2 data-id="heading-5">源码</h2>
<p>如果有需要，可以上gitee拉我的代码，地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyu-zhuohao%2Freact_management_frame" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yu-zhuohao/react_management_frame" ref="nofollow noopener noreferrer">gitee.com/yu-zhuohao/…</a></p></div>  
</div>
            