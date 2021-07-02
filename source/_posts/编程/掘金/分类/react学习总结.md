
---
title: 'react学习总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6658'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 03:29:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=6658'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">一、在html中开始一个react</h2>
<h3 data-id="heading-1">步骤 1： 添加一个 DOM 容器到 HTML</h3>
<pre><code class="hljs language-js copyable" lang="js"><!-- ... 其它 HTML ... -->

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"like_button_container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<!-- ... 其它 HTML ... -->
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">步骤 2：添加 Script 标签，引入react文件</h3>
<pre><code class="hljs language-js copyable" lang="js"><!-- 加载 React。-->
  <!-- 注意: 部署时，将 <span class="hljs-string">"development.js"</span> 替换为 <span class="hljs-string">"production.min.js"</span>。-->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/react@17/umd/react.development.js"</span> <span class="hljs-attr">crossorigin</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/react-dom@17/umd/react-dom.development.js"</span> <span class="hljs-attr">crossorigin</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

  <!-- 加载我们的 React 组件。-->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"like_button.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前两个标签加载 React。第三个将加载你的组件代码。</p>
<h3 data-id="heading-3">步骤 3：创建一个 React 组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ... 此前粘贴的代码 ...</span>

<span class="hljs-keyword">const</span> domContainer = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#like_button_container'</span>);
ReactDOM.render(e(LikeButton), domContainer);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">提示：为生产环境压缩 JavaScript 代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"https://unpkg.com/react@17/umd/react.production.min.js"</span> crossorigin></script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"</span> <span class="hljs-attr">crossorigin</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">方案二：使用 React 和 JSX快速开始</h3>
<p>在项目中尝试 JSX 最快的方法是在页面中添加这个 
</p><pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"https://unpkg.com/babel-standalone@6/babel.min.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，你可以在任何 <code><script> </code>标签内使用 JSX，方法是在为其添加 <code>type="text/babel"</code> 属性。</p>
<p>这种方式适合于学习和创建简单的示例。然而，它会使你的网站变慢，并且不适用于生产环境。当你准备好更进一步时，删除你添加的这个新的<code> <script></code> 标签以及type="text/babel" 属性。取而代之的，你将设置一个 JSX 预处理器来自动转换所有 <code><script></code> 标签的内容。</p>
<p>在终端上跳转到你的项目文件夹，然后粘贴这<code>两个命令</code>：</p>
<ul>
<li>步骤 1： 执行 <code>npm init -y </code>（如果失败,<a href="https://gist.github.com/gaearon/246f6380610e262f8a648e3e51cad40d" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/gaearon/246…</a>)</li>
<li>步骤 2： 执行 <code>npm install babel-cli@6 babel-preset-react-app@3</code></li>
</ul>
<p>我们在这里使用 npm 只是用来安装 JSX 预处理器，之后你不再需要它。React 和应用程序代码都可以继续使用 <code><script> </code>标签而不做任何更改。</p>
<h3 data-id="heading-6">运行 JSX 预处理器</h3>
<p>创建一个名为 src 的文件夹并执行这个终端命令：</p>
<p><code>npx babel --watch src --out-dir . --presets react-app/prod</code></p>
<p>注意：</p>
<p><code>npx </code>不是拼写错误 —— 它是 npm 5.2+ 附带的 package 运行工具。</p>
<h2 data-id="heading-7">二、使用工具链创建新的 React 应用</h2>
<p><strong>React 团队主要推荐这些解决方案：</strong></p>
<ul>
<li>如果你是在学习 React 或创建一个新的单页应用，请使用 Create React App。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">npx create-react-app my-app
cd my-app
npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果你是在用 Node.js 构建服务端渲染的网站，试试 Next.js。</li>
<li>如果你是在构建内容主导的静态网站，试试 Gatsby。</li>
<li>如果你是在打造组件库或将 React 集成到现有代码仓库，尝试更灵活的工具链。</li>
</ul></div>  
</div>
            