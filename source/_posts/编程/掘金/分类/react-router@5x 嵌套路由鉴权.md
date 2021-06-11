
---
title: 'react-router@5.x 嵌套路由鉴权'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8458'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 20:08:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=8458'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><code><Route/></code> 组件渲染优先级</h2>
<blockquote>
<ul>
<li><a href="https://reactrouter.com/web/api/Route/route-render-methods" target="_blank" rel="nofollow noopener noreferrer">route-render-methods</a></li>
<li><a href="https://www.jianshu.com/p/a2a9b469a422" target="_blank" rel="nofollow noopener noreferrer">render 和 component 的区别</a></li>
</ul>
</blockquote>
<p>渲染方式有如下三种:</p>
<ol>
<li>render</li>
<li>component</li>
<li>children</li>
</ol>
<p>三个属性同时存在</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Route
  path=<span class="hljs-string">"/the-path"</span>
  render=&#123;<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by render<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>&#125;
  component=&#123;<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by component<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>&#125;
>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by children<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</Route>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by children<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只有<code>render</code>和<code>component</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Route
  path=<span class="hljs-string">"/the-path"</span>
  render=&#123;<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by render<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>&#125;
  component=&#123;<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by component<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>by component<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此,渲染的优先级为</p>
<pre><code class="copyable">children > component > render
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">使用<code>render</code>渲染嵌套的路由</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1"</span>></span>route 1<span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1/1"</span>></span>route 1-1<span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1/2"</span>></span>route 1-2<span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r2"</span>></span>route 2<span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>

  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Route</span>
      <span class="hljs-attr">path</span>=<span class="hljs-string">"/the-path/r1"</span>
      <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> (
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 1<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/the-path/r1/1"</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-1<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>&#125; />
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/the-path/r1/2"</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-2<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>&#125; />
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      )&#125;
    />
    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/the-path/r2"</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 2<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>&#125; />
  <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span></span>
</>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用路由配置的形式来渲染路由</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 路由配置</span>

<span class="hljs-keyword">const</span> R1 = <span class="hljs-function">(<span class="hljs-params">&#123; children &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 1<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    &#123;children&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="hljs-keyword">const</span> R2 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 2<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="hljs-keyword">const</span> R11 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-1<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;
<span class="hljs-keyword">const</span> R12 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-2<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1"</span>,
    <span class="hljs-attr">component</span>: R1,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/1"</span>,
        <span class="hljs-attr">component</span>: R11,
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/2"</span>,
        <span class="hljs-attr">component</span>: R12,
      &#125;,
    ],
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r2"</span>,
    <span class="hljs-attr">component</span>: R2,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 用于渲染嵌套路由的渲染函数</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderNestedRoute</span>(<span class="hljs-params">&#123;
  path = <span class="hljs-string">""</span>,
  component: Content = () => <span class="hljs-literal">false</span>,
  children = <span class="hljs-literal">undefined</span>,
  ...otherRouteProps
&#125; = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
      <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> (
        <span class="hljs-tag"><<span class="hljs-name">Content</span>></span>
          &#123;Array.isArray(children) && children.map(renderNestedRoute)&#125;
        <span class="hljs-tag"></<span class="hljs-name">Content</span>></span>
      )&#125;
      &#123;...otherRouteProps&#125;
    /></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合使用</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.jsx</span>

<Switch>&#123;routes.map(renderNestedRoute)&#125;</Switch>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">添加 user 的管理模块</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.jsx</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [user, setUser] = useState(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">roles</span>: [] &#125;);

  <span class="hljs-comment">// 在本例中,使用了简单的 state, 真正的业务中一般会使用 redux 或 mobx</span>
  <span class="hljs-keyword">const</span> login = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">"roles"</span>, <span class="hljs-built_in">JSON</span>.stringify([<span class="hljs-string">"account"</span>]));
    setUser(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"nickname"</span>, <span class="hljs-attr">roles</span>: [<span class="hljs-string">"account"</span>] &#125;);
  &#125;;

  <span class="hljs-keyword">const</span> logout = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">window</span>.localStorage.removeItem(<span class="hljs-string">"roles"</span>);
    setUser(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">roles</span>: [] &#125;);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      // ...
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>name: &#123;user.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;login&#125;</span>></span>login<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;logout&#125;</span>></span>logout<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">修改路由配置,添加路由的权限</h2>
<p>本例中,在配置中添加<code>roles</code>属性,类型是<code>string[]</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1"</span>,
    <span class="hljs-attr">component</span>: R1,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">"/the-path/r1/1"</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/1"</span>,
        <span class="hljs-attr">component</span>: R11,
        <span class="hljs-attr">roles</span>: [<span class="hljs-string">"account"</span>],
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/2"</span>,
        <span class="hljs-attr">component</span>: R12,
        <span class="hljs-attr">roles</span>: [<span class="hljs-string">"admin"</span>],
      &#125;,
    ],
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r2"</span>,
    <span class="hljs-attr">component</span>: R2,
    <span class="hljs-attr">roles</span>: [<span class="hljs-string">"admin"</span>, <span class="hljs-string">"super-admin"</span>],
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">修复路由渲染函数</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderNestedRoute</span>(<span class="hljs-params">&#123;
  path = <span class="hljs-string">""</span>,
  component: Content = () => <span class="hljs-literal">false</span>,
  children = <span class="hljs-literal">undefined</span>,
  roles = [],
  ...otherRouteProps
&#125; = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// 从本地缓存中获取当前用户(登录之后)的角色权限</span>
  <span class="hljs-keyword">const</span> currUserRoles = <span class="hljs-built_in">JSON</span>.parse(
    <span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">"roles"</span>) || <span class="hljs-string">"[]"</span>
  );

  <span class="hljs-comment">// 判断当前用户是否有权限访问指定的路由</span>
  <span class="hljs-comment">// 这里的业务逻辑是, 只要用户的角色匹配权限列表中的任意一个即可允许访问</span>
  <span class="hljs-keyword">const</span> hasAuthorization =
    roles.length === <span class="hljs-number">0</span> || currUserRoles.some(<span class="hljs-function">(<span class="hljs-params">r</span>) =></span> roles.includes(r));

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
      <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span>
        hasAuthorization ? (
          <span class="hljs-tag"><<span class="hljs-name">Content</span>></span>
            &#123;Array.isArray(children) && children.map(renderNestedRoute)&#125;
          <span class="hljs-tag"></<span class="hljs-name">Content</span>></span>
        ) : (
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>you have no authorization as &#123;roles.join(" or ")&#125; !<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        )
      &#125;
      &#123;...otherRouteProps&#125;
    /></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">完整例子</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.jsx</span>

<span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Switch, Route, Link &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;

<span class="hljs-keyword">const</span> R1 = <span class="hljs-function">(<span class="hljs-params">&#123; children &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 1<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    &#123;children&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="hljs-keyword">const</span> R2 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Route 2<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="hljs-keyword">const</span> R11 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-1<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;
<span class="hljs-keyword">const</span> R12 = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Route 1-2<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1"</span>,
    <span class="hljs-attr">component</span>: R1,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">"/the-path/r1/1"</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/1"</span>,
        <span class="hljs-attr">component</span>: R11,
        <span class="hljs-attr">roles</span>: [<span class="hljs-string">"account"</span>],
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r1/2"</span>,
        <span class="hljs-attr">component</span>: R12,
        <span class="hljs-attr">roles</span>: [<span class="hljs-string">"admin"</span>],
      &#125;,
    ],
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/the-path/r2"</span>,
    <span class="hljs-attr">component</span>: R2,
    <span class="hljs-attr">roles</span>: [<span class="hljs-string">"admin"</span>, <span class="hljs-string">"super-admin"</span>],
  &#125;,
];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderNestedRoute</span>(<span class="hljs-params">&#123;
  path = <span class="hljs-string">""</span>,
  component: Content = () => <span class="hljs-literal">false</span>,
  children = <span class="hljs-literal">undefined</span>,
  roles = [],
  ...otherRouteProps
&#125; = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> currUserRoles = <span class="hljs-built_in">JSON</span>.parse(
    <span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">"roles"</span>) || <span class="hljs-string">"[]"</span>
  );
  <span class="hljs-keyword">const</span> hasAuthorization =
    roles.length === <span class="hljs-number">0</span> || currUserRoles.some(<span class="hljs-function">(<span class="hljs-params">r</span>) =></span> roles.includes(r));

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
      <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;path&#125;</span>
      <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span>
        hasAuthorization ? (
          <span class="hljs-tag"><<span class="hljs-name">Content</span>></span>
            &#123;Array.isArray(children) && children.map(renderNestedRoute)&#125;
          <span class="hljs-tag"></<span class="hljs-name">Content</span>></span>
        ) : (
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>you have no authorization as &#123;roles.join(" or ")&#125; !<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        )
      &#125;
      &#123;...otherRouteProps&#125;
    /></span>
  );
&#125;

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [user, setUser] = useState(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">roles</span>: [] &#125;);

  <span class="hljs-keyword">const</span> login = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">"roles"</span>, <span class="hljs-built_in">JSON</span>.stringify([<span class="hljs-string">"account"</span>]));
    setUser(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"nickname"</span>, <span class="hljs-attr">roles</span>: [<span class="hljs-string">"account"</span>] &#125;);
  &#125;;

  <span class="hljs-keyword">const</span> logout = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">window</span>.localStorage.removeItem(<span class="hljs-string">"roles"</span>);
    setUser(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">roles</span>: [] &#125;);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>name: &#123;user.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;login&#125;</span>></span>login<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;logout&#125;</span>></span>logout<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>

      <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1"</span>></span>route 1<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1/1"</span>></span>route 1-1<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r1/2"</span>></span>route 1-2<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/the-path/r2"</span>></span>route 2<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>&#123;routes.map(renderNestedRoute)&#125;<span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(App);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            