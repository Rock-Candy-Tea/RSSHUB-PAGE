
---
title: 'React 面试必知必会 Day11'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3170'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 07:58:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=3170'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. <code>setState()</code> 和 <code>replaceState()</code> 方法之间的区别是什么？</h2>
<p>当你使用 <code>setState()</code> 时，当前和之前的状态被合并。 <code>replaceState()</code> 抛出当前的状态，只用你提供的内容来替换它。通常 <code>setState()</code> 会被使用，除非你真的因为某些原因需要删除所有之前的键。你也可以在 <code>setState()</code> 中把状态设置为 <code>false</code>/<code>null</code>，而不是使用 <code>replaceState()</code>。</p>
<h2 data-id="heading-1">2. 如何监听状态变化？</h2>
<p>当状态发生变化时，<code>componentDidUpdate</code> 生命周期方法将被调用。你可以将提供的状态和 props 值与当前的状态和 props 进行比较，以确定是否有意义的变化。</p>
<pre><code class="copyable">componentDidUpdate(object prevProps, object prevState)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> 以前的 ReactJS 版本也使用 <code>componentWillUpdate(object nextProps, object nextState)</code> 监听状态改变。在最新的版本中，它已被弃用。</p>
<h2 data-id="heading-2">3. 在 React 状态下，删除数组元素的推荐方法是什么？</h2>
<p>更好的方法是使用 <code>Array.prototype.filter()</code> 方法。</p>
<p>例如，让我们创建一个 <code>removeItem()</code> 方法来更新状态。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">removeItem</span>(<span class="hljs-params">index</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.state.data.filter(<span class="hljs-function">(<span class="hljs-params">item, i</span>) =></span> i !== index)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 有没有可能在不渲染 HTML 的情况下使用 React 呢？</h2>
<p>在最新版本（>=16.2）中可以实现。以下是可用选项。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Fragment</span>></span><span class="hljs-tag"></<span class="hljs-name">React.Fragment</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><></span><span class="hljs-tag"></></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回 <code>undefined</code> 是不行的。</p>
<h2 data-id="heading-4">5. 如何用 React 打印漂亮的 JSON？</h2>
<p>我们可以使用 <code><pre></code> 标签，这样可以保留 <code>JSON.stringify()</code> 的格式。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> data = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'John'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">42</span> &#125;;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">pre</span>></span>&#123;JSON.stringify(data, null, 2)&#125;<span class="hljs-tag"></<span class="hljs-name">pre</span>></span></span>;
  &#125;
&#125;

React.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">User</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'container'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 为什么你不能在 React 中更新 props？</h2>
<p>React 的理念是，props 应该是<strong>不可变的</strong>和<strong>自上而下</strong>的。这意味着父组件可以向子组件发送任何 props 值，但子组件不能修改收到的 props。</p>
<h2 data-id="heading-6">7. 如何在页面加载时聚焦一个输入框？</h2>
<p>你可以通过为 <code>input</code> 元素创建 ref 并在 <code>componentDidMount()</code> 中使用它。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.nameInput) &#123;
      <span class="hljs-built_in">this</span>.nameInput.focus();
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">defaultValue</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">Won</span>'<span class="hljs-attr">t</span> <span class="hljs-attr">focus</span>"&#125; /></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;input</span> =></span> (this.nameInput = input)&#125;
          defaultValue=&#123;'Will focus'&#125;
        />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8. 更新状态中的对象的方式有哪些？</h2>
<ol>
<li><strong>合并状态和对象后调用 <code>setState()</code>：</strong></li>
</ol>
<ul>
<li>使用 <code>Object.assign()</code> 创建对象的拷贝：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> user = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, <span class="hljs-built_in">this</span>.state.user, &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">42</span> &#125;);
<span class="hljs-built_in">this</span>.setState(&#123; user &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用展开操作符：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> user = &#123; ...this.state.user, <span class="hljs-attr">age</span>: <span class="hljs-number">42</span> &#125;;
<span class="hljs-built_in">this</span>.setState(&#123; user &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>调用 <code>setState()</code> 时传入函数：</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.setState(<span class="hljs-function"><span class="hljs-params">prevState</span> =></span> (&#123;
  <span class="hljs-attr">user</span>: &#123;
    ...prevState.user,
    <span class="hljs-attr">age</span>: <span class="hljs-number">42</span>,
  &#125;,
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">9. 我们如何在浏览器中查看运行时的 React 的版本？</h2>
<p>你可以使用 <code>React.version</code> 来获取版本。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> REACT_VERSION = React.version;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;`React version: $&#123;REACT_VERSION&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10. 在 <code>create-react-app</code> 中包含 polyfills 的方法是什么？</h2>
<p>有一些方法可以在 create-react-app 中包含 polyfills。</p>
<ol>
<li><strong>手动从 <code>core-js</code> 引入：</strong></li>
</ol>
<p>创建一个名为（类似）<code>polyfills.js</code> 的文件并将其导入根 <code>index.js</code> 文件。运行 <code>npm install core-js</code> 或 <code>yarn add core-js</code> 并导入你所需要的特定功能。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/fn/array/find'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/fn/array/includes'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/fn/number/is-nan'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>使用 Polyfill 服务：</strong></li>
</ol>
<p>使用 polyfill.io CDN，通过在 <code>index.html</code> 中添加这一行来检索自定义的、针对浏览器的 polyfills。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.polyfill.io/v2/polyfill.min.js?features=default,Array.prototype.includes"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的脚本中，我们必须明确请求 <code>Array.prototype.includes</code> 功能，因为它不包括在默认功能集中。</p></div>  
</div>
            