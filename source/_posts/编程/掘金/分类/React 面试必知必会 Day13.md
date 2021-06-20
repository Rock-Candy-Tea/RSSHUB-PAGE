
---
title: 'React 面试必知必会 Day13'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3510'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 07:36:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=3510'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. React 的常见文件夹结构是什么？</h2>
<p>React 项目文件结构有两种常见做法。</p>
<ol>
<li><strong>按特性或路由分组：</strong>*</li>
</ol>
<p>一种常见的项目结构方式是将 CSS、JS 和测试放在一起，按特性或路由分组。</p>
<pre><code class="copyable">common/
├─ Avatar.js
├─ Avatar.css
├─ APIUtils.js
└─ APIUtils.test.js
feed/
├─ index.js
├─ Feed.js
├─ Feed.css
├─ FeedStory.js
├─ FeedStory.test.js
└─ FeedAPI.js
profile/
├─ index.js
├─ Profile.js
├─ ProfileHeader.js
├─ ProfileHeader.css
└─ ProfileAPI.js
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>按文件类型分组：</strong></li>
</ol>
<p>另一种流行的项目结构方式是将类似的文件分组。</p>
<pre><code class="copyable">api/
├─ APIUtils.js
├─ APIUtils.test.js
├─ ProfileAPI.js
└─ UserAPI.js
components/
├─ Avatar.js
├─ Avatar.css
├─ Feed.js
├─ Feed.css
├─ FeedStory.js
├─ FeedStory.test.js
├─ Profile.js
├─ ProfileHeader.js
└─ ProfileHeader.css
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 有哪些流行的动画包？</h2>
<p>React Transition Group 和 React Motion 是 React 生态系统中流行的动画包。</p>
<h2 data-id="heading-2">3. 样式模块的好处是什么？</h2>
<p>我们建议避免在组件中硬编码样式值。任何可能在不同的 UI 组件中使用的值都应该被提取到它们自己的模块中。</p>
<p>例如，这些样式可以被提取到一个单独的组件中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> colors = &#123;
  white,
  black,
  blue,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> space = [<span class="hljs-number">0</span>, <span class="hljs-number">8</span>, <span class="hljs-number">16</span>, <span class="hljs-number">32</span>, <span class="hljs-number">64</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在其他组件中单独导入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; space, colors &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./styles'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 有哪些流行的 React 专用 linter？</h2>
<p>ESLint 是一个很流行的 JavaScript linter。有一些插件可以用来分析特定的代码风格。其中最常见的 React 插件是一个名为 <code>eslint-plugin-react</code> 的 npm 包。默认情况下，它将检查一些最佳实践，其规则是检查从迭代器中的键到一整套道具类型的东西。</p>
<p>另一个流行的插件是 <code>eslint-plugin-jsx-a11y</code>，它将帮助修复可访问性方面的常见问题。由于 JSX 提供了与常规 HTML 稍有不同的语法，例如 <code>alt</code> 文本和 <code>tabindex</code> 的问题将不会被常规插件发现。</p>
<h2 data-id="heading-4">5. 如何进行 AJAX 调用，应该在哪个组件的生命周期方法中进行 AJAX 调用？</h2>
<p>你可以使用 AJAX 库，如 Axios、jQuery AJAX，以及浏览器内置的 <code>fetch</code>。你应该在 <code>componentDidMount()</code> 生命周期方法中获取数据。这样你就可以在获取数据时使用 <code>setState()</code> 来更新你的组件。</p>
<p>例如，从 API 获取的雇员名单并设置本地状态。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">employees</span>: [],
      <span class="hljs-attr">error</span>: <span class="hljs-literal">null</span>,
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    fetch(<span class="hljs-string">'https://api.example.com/items'</span>)
      .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> res.json())
      .then(
        <span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">employees</span>: result.employees,
          &#125;);
        &#125;,
        <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.setState(&#123; error &#125;);
        &#125;,
      );
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; error, employees &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">if</span> (error) &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Error: &#123;error.message&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
          &#123;employees.map(employee => (
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;employee.name&#125;</span>></span>
              &#123;employee.name&#125;-&#123;employee.experience&#125;
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
      );
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 什么是渲染 props？</h2>
<p><strong>渲染 props</strong>是一种简单的技术，使用一个 props 在组件之间共享代码，其值是一个函数。下面的组件使用渲染 props，它返回一个 React 元素。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><DataProvider render=&#123;<span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;`Hello $&#123;data.target&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React Router 和 DownShift 等库正在使用这种模式。</p>
<blockquote>
<p>这是 React 核心面试题最后一篇，后续会有 React Router、Redux 等继续更新，欢迎持续关注。</p>
</blockquote></div>  
</div>
            