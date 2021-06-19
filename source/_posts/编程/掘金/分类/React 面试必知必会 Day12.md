
---
title: 'React 面试必知必会 Day12'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8389'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 05:11:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=8389'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. 如何在 create-react-app 中使用 https 而不是 http？</h2>
<p>你只需要是用 <code>HTTPS=true</code> 配置。你可以编辑 <code>package.json</code> scripts 部分：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
 <span class="hljs-attr">"start"</span>: <span class="hljs-string">"set HTTPS=true && react-scripts start"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者运行 <code>set HTTPS=true && npm start</code></p>
<h2 data-id="heading-1">2. 如何避免在 create-react-app 中使用相对路径导入？</h2>
<p>在项目里根目录创建一个叫 <code>.env</code> 的文件并写入导入的路径：</p>
<pre><code class="copyable">NODE_PATH=src/app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后重启调试服务器。现在你应该能够在 <code>src/app</code> 目录下不使用相对路径导入任何东西。</p>
<h2 data-id="heading-2">3. 如何在 React Router 中添加 Google Analytics？</h2>
<p>在 <code>history</code> 对象上添加一个监听器，以记录每个页面的浏览。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">history.listen(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">location</span>) </span>&#123;
  <span class="hljs-built_in">window</span>.ga(<span class="hljs-string">'set'</span>, <span class="hljs-string">'page'</span>, location.pathname + location.search);
  <span class="hljs-built_in">window</span>.ga(<span class="hljs-string">'send'</span>, <span class="hljs-string">'pageview'</span>, location.pathname + location.search);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 如何每秒更新一次组件？</h2>
<p>你需要使用 <code>setInterval()</code> 来触发变化，但你也需要在组件卸载时清除计时器以防止错误和内存泄漏。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">time</span>: <span class="hljs-built_in">Date</span>.now() &#125;), <span class="hljs-number">1000</span>)
&#125;

<span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.interval)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. 如何在 React 中对内联样式使用 CSS 厂商前缀？</h2>
<p>React 不会自动应用 CSS 厂商前缀。你需要手动添加 CSS 厂商前缀。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div
  style=&#123;&#123;
    <span class="hljs-attr">transform</span>: <span class="hljs-string">'rotate(90deg)'</span>,
    <span class="hljs-attr">WebkitTransform</span>: <span class="hljs-string">'rotate(90deg)'</span>, <span class="hljs-comment">// 注意大写 'W'</span>
    <span class="hljs-attr">msTransform</span>: <span class="hljs-string">'rotate(90deg)'</span>, <span class="hljs-comment">// 'ms' 是全小写</span>
  &#125;&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 如何使用 React 和 ES6 导入和导出组件？</h2>
<p>你应该使用默认值来导出组件</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> User <span class="hljs-keyword">from</span> <span class="hljs-string">'user'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyProfile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">User</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"customer"</span>></span>//...<span class="hljs-tag"></<span class="hljs-name">User</span>></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了导出指定符，MyProfile 将成为成员并导出到这个模块，同样可以在其他组件中导入而不提及名称。</p>
<h2 data-id="heading-6">7. 为什么组件构造器只会被调用一次？</h2>
<p>React 的 reconciliation（协调） 算法假定，在没有任何相反信息的情况下，如果一个自定义组件在随后的渲染中出现在相同的地方，它就是之前的那个组件，所以 React 重用之前的实例而不是创建一个新的。</p>
<h2 data-id="heading-7">8. 如何在 React 中定义常量？</h2>
<p>你可以使用 ES7 的 <code>静态</code> 字段来定义常量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> DEFAULT_PAGINATION = <span class="hljs-number">10</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态字段是类字段第三阶段提案的一部分。</p>
<h2 data-id="heading-8">9. 如何在 React 中以编程方式触发点击事件？</h2>
<p>你可以使用 ref props 通过回调获得对底层 <code>HTMLInputElement</code> 对象的引用，将该引用存储为类属性，然后使用该引用从事件处理程序中使用 <code>HTMLElement.click</code> 方法触发点击。</p>
<p>这可以分两步进行。</p>
<ol>
<li>在 render 方法中创建 ref：</li>
</ol>
<pre><code class="hljs language-jsx copyable" lang="jsx"><input ref=&#123;<span class="hljs-function"><span class="hljs-params">input</span> =></span> (<span class="hljs-built_in">this</span>.inputElement = input)&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在你的事件处理程序中应用点击事件。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.inputElement.click();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10. 有可能在纯 React 中使用 async/await 吗？</h2>
<p>如果你想在 React 中使用 <code>async</code>/<code>await</code>，你将需要 Babel 和 <a href="https://babeljs.io/docs/en/babel-plugin-transform-async-to-generator" target="_blank" rel="nofollow noopener noreferrer">transform-async-to-generator</a> 插件。React Native 已经包含了 Babel 和一系列的转换功能。</p></div>  
</div>
            