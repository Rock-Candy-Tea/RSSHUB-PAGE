
---
title: '代码分割(精读React官方文档—14)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9249'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 19:24:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=9249'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">打包</h2>
<blockquote>
<p>官方描述：大多数 React 应用都会使用 Webpack，Rollup 或 Browserify 这类的构建工具来打包文件。打包是一个将文件引入并合并到一个单独文件的过程，最终形成一个 “bundle”。接着在页面上引入该 bundle，整个应用即可一次性加载。</p>
</blockquote>
<p><strong>实例：打包前文件和打包后文件对比</strong></p>
<ul>
<li>打包前</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./math.js'</span>;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>)); <span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// math.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打包后</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>)); <span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">代码分割</h2>
<p><strong>打包应该注意的问题：</strong></p>
<ol>
<li>随着应用体积的增加，避免因为体积过大而导致加载过慢的问题。</li>
<li>Webapck等构建工具是支持代码分割的。</li>
<li>代码分割能够懒加载用户所需要的内容，能显著的提高应用的性能。</li>
<li>尽管没有减少应用整体的代码体积，但是避免了加载用户永远不需要的代码，减少了所需的代码量。</li>
</ol>
<h2 data-id="heading-2">import()</h2>
<blockquote>
<p>官方描述：引入代码分割的最佳方式是通过动态imort语法。</p>
</blockquote>
<ul>
<li>使用之前</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./math'</span>;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用之后</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>(<span class="hljs-string">"./math"</span>).then(<span class="hljs-function"><span class="hljs-params">math</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(math.add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>));
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解读</strong></p>
<ol>
<li>当Webpack解析到该语法的时候，会进行自动的代码分割。</li>
<li>如果你是使用的create-react-app等脚手架的情况下，该功能开箱即用。</li>
<li>当自己配置Webpack或者Babel的时候，需要根据相关配置文件进行操作。</li>
</ol>
<h2 data-id="heading-3">React.lazy</h2>
<blockquote>
<p>React.lazy函数能让你像渲染常规这件一样处理动态引入。</p>
</blockquote>
<ul>
<li>使用之前</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> OtherComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./OtherComponent'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用之后</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> OtherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./OtherComponent'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面的代码将会在组件首次渲染的时候，自动导入包含OtherComponent的组件，React.lazy接收一个函数，这个函数动态调用import并返回一个Promise,该Promise需要resolve一个default export 的组件。然后应在Suspense组件中渲染lazy组件。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Suspense &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> OtherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./OtherComponent'</span>));

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
        <span class="hljs-tag"><<span class="hljs-name">OtherComponent</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解读</strong></p>
<ol>
<li>fallback属性中可以接收任何在组件加载过程中想要展示的React组件。</li>
<li>可以将Suspense组件至于懒加载组件之上的任何位置。</li>
<li>可以用一个Suspense组件包裹多个懒加载组件。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Suspense &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> OtherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./OtherComponent'</span>));
<span class="hljs-keyword">const</span> AnotherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./AnotherComponent'</span>));

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">OtherComponent</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">AnotherComponent</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">异常捕获边界</h2>
<blockquote>
<p>为什么需要异常捕获边界？</p>
</blockquote>
<ul>
<li>因为一旦模块加载失败，会触发一个错误，我们可以通过异常捕获边界技术来处理这些情况，以显示良好的用户体验。</li>
</ul>
<p><strong>解读</strong></p>
<p>解决这个问题的本质还是通过Supense和React.lazy进行结合。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Suspense &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> MyErrorBoundary <span class="hljs-keyword">from</span> <span class="hljs-string">'./MyErrorBoundary'</span>;

<span class="hljs-keyword">const</span> OtherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./OtherComponent'</span>));
<span class="hljs-keyword">const</span> AnotherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./AnotherComponent'</span>));

<span class="hljs-keyword">const</span> MyComponent = <span class="hljs-function">() =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">MyErrorBoundary</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">OtherComponent</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">AnotherComponent</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">MyErrorBoundary</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">基于路由的代码分割</h2>
<ol>
<li>如何选择代码分割的位置，需要考虑代码分割不能影响用户的体验。</li>
<li>一般选择从路由开始进行分割。</li>
</ol>
<p><strong>基于路由的分割实例</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Suspense, lazy &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; BrowserRouter <span class="hljs-keyword">as</span> Router, Route, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>;

<span class="hljs-keyword">const</span> Home = lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./routes/Home'</span>));
<span class="hljs-keyword">const</span> About = lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./routes/About'</span>));

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
      <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;/</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/about"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;/</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">命名导出</h2>
<blockquote>
<p>React.lazy目前只支持默认导出，如果想让其支持命名导出，可以考虑创建一个中间模块。</p>
</blockquote>
<h3 data-id="heading-7">第一步：分别暴露组件地址</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ManyComponents.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> MyComponent = <span class="hljs-comment">/* ... */</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> MyUnusedComponent = <span class="hljs-comment">/* ... */</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">第二步：将分别暴露转为默认暴露</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// MyComponent.js</span>
<span class="hljs-keyword">export</span> &#123; MyComponent <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./ManyComponents.js"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">第三步：调用懒加载</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// MyApp.js</span>
<span class="hljs-keyword">import</span> React, &#123; lazy &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> MyComponent = lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"./MyComponent.js"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">欢迎大家关注我的专栏，一起学习React官方文档！</h2></div>  
</div>
            