
---
title: 'React 中的一些  Router 必备知识点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 16:17:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 109 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Freact-router" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/react-router" ref="nofollow noopener noreferrer">React 中的一些  Router 必备知识点</a></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a150a1399144b15bef33456a8f3ee43~tplv-k3u1fbpfcp-watermark.image" alt="鱼鱼.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>每次开发新页面的时候，都免不了要去设计一个新的 URL，也就是我们的路由。其实路由在设计的时候不仅仅是一个由几个简单词汇和斜杠分隔符组成的链接，偶尔也可以去考虑有没有更“优雅”的设计方式和技巧。而在这背后，路由和组件之间的协作关系是怎样的呢？于是我以 React 中的 Router 使用方法为例，整理了一些知识点小记和大家分享～</p>
<h2 data-id="heading-1">React-Router</h2>
<h3 data-id="heading-2">基本用法</h3>
<p>通常我们使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactrouter.com%2Fnative%2Fguides%2Fquick-start" target="_blank" rel="nofollow noopener noreferrer" title="https://reactrouter.com/native/guides/quick-start" ref="nofollow noopener noreferrer">React-Router</a> 来实现 React 单页应用的路由控制，它通过管理 URL，实现组件的切换，进而呈现页面的切换效果。</p>
<p>其最基本用法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Router, Route &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router'</span>;
render((
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;App&#125;/</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
), <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>亦或是嵌套路由：</p>
<p>在 React-Router V4 版本之前可以直接嵌套，方法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><Router>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>外层<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
      <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/in"</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>内层<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125; />
  <span class="hljs-tag"></<span class="hljs-name">Route</span>></span></span>
</Router>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，理论上，用户访问 <code>/in</code> 时，会先加载 <code><div>外层</div></code>，然后在它的内部再加载 <code><div>内层</div></code>。</p>
<p>然而实际运行上述代码却发现它只渲染出了根目录中的内容。后续对比 React-Router 版本发现，是因为在 V4 版本中变更了其渲染逻辑，原因据说是为了践行 React 的组件化理念，不能让 Route 标签看起来只是一个标签（奇怪的知识又增加了）。</p>
<p>现在较新的版本中，可以使用 Render 方法实现嵌套。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><Route
  path=<span class="hljs-string">"/"</span>
  render=&#123;<span class="hljs-function">() =></span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Route</span>
        <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span>
        <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>外层<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
      />
      <span class="hljs-tag"><<span class="hljs-name">Route</span>
        <span class="hljs-attr">path</span>=<span class="hljs-string">"/in"</span>
        <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>内层<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
      />
      <span class="hljs-tag"><<span class="hljs-name">Route</span>
        <span class="hljs-attr">path</span>=<span class="hljs-string">"/others"</span>
        <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>其他<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
      />
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时访问 <code>/in</code> 时，会将“外层”和“内层”一起展示出来，类似地，访问 <code>/others</code> 时，会将“外层”和“其他”一起展示出来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/728d6b95a7654e1bb207521aebfbf0f7~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">路由传参小 Tips</h3>
<p>在实际开发中，往往在页面切换时需要传递一些参数，有些参数适合放在 Redux 中作为全局数据，或者通过上下文传递，比如业务的一些共享数据，但有些参数则适合放在 URL 中传递，比如页面类型或详情页中单据的唯一标识 <code>id</code>。在处理 URL 时，除了问号带参数的方式，React-Router 能帮我们做什么呢？在这其中，Route 组件的 <code>path</code> 属性便可用于指定路由的匹配规则。</p>
<h4 data-id="heading-4">场景 1</h4>
<blockquote>
<p>描述：就想让普普通通的 URL 带个平平无奇的参数</p>
</blockquote>
<p>那么，接下来我们可以这样干：</p>
<p><strong>Case  A：路由参数</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">"/book/:id"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用冒号 + 参数名字的方式，将想要传递的参数添加到 URL 上，此时，当参数名字（本 Case 中是 id）对应的值改变时，将被认为是不同 URL。</p>
<p><strong>Case B：查询参数</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">"/book"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想要在页面跳转的时候问号带参数，那么 path 可以直接设计成既定的样子，参数由跳转方拼接。
在跳转时，有两种形式带上参数。其一是在 Link 组件的 to 参数中通过配置字符串并用问号带参数，其二是 to 参数可以接受一个对象，其中可以在 search 字段中配置想要传递的参数。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Link to=<span class="hljs-string">"/book?id=111"</span> />
<span class="hljs-comment">// 或者</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;&#123;</span>
  <span class="hljs-attr">pathname:</span> '/<span class="hljs-attr">book</span>',
  <span class="hljs-attr">search:</span> '?<span class="hljs-attr">id</span>=<span class="hljs-string">111</span>',
&#125;&#125;/></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，假设当前页面 URL中的 id 由111 修改为 222 时，该路由对应的组件（在上述例子中就是 React-Route 配置时 <code>path="/book"</code> 对应的页面/组件 ）<strong>会更新</strong>，即执行 componentDidUpdate 方法，但<strong>不会被卸载</strong>，也就是说，不会执行 componentDidMount 方法。</p>
<p><strong>Case C：查询参数隐身式带法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">"/book"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>path 依旧设计成既定的样子，而在跳转时，可以通过 Link 中的 state 将参数传递给对应路由的页面。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Link to=&#123;&#123;
  <span class="hljs-attr">pathname</span>: <span class="hljs-string">'/book'</span>,
  <span class="hljs-attr">state</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">111</span> &#125;
&#125;&#125;/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但一定要注意的是，尽管这种方式下查询参数不会明文传递了，但此时页面刷新会导致参数丢失（存储在 state 中的通病），So，灰常不推荐~~（其实不想明文可以进行加密处理，但一般情况下敏感信息是不建议放在 URL 中传递的～）</p>
<h4 data-id="heading-5">场景 2</h4>
<blockquote>
<p>描述：编辑/详情页，想要共用一个页面，URL 由不同的参数区分，此时我们希望，参数必须为 edit、detail、add 中的 1 个，不然需要跳转到 404 Not Found 页面。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">'/book/:pageType(edit|detail|add)'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不加括号中的内容 <code>(edit|detail|add)</code>，当传入错误的参数（比如用户误操作、随便拼接 URL 的情况），则页面不会被 404 拦截，而是继续走下去开始渲染页面或调用接口，但此时很有可能导致接口传参错误或页面出错。</p>
<h4 data-id="heading-6">场景 3</h4>
<blockquote>
<p>描述：新增页和编辑页辣么像，我的新增页也想和编辑/详情共用一个页面。但是新增页不需要 id，编辑/详情页需要 id，使用同一个页面怎么办？</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">'/book/:pageType(edit|detail|add)/:id?'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>别急，可以用 <code>?</code> 来解决，它意味着 id 不是一个必要参数，可传可不传。</p>
<h4 data-id="heading-7">场景 4</h4>
<blockquote>
<p>描述：我的 id 只能是数字，不想要字符串怎么办？</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">path=<span class="hljs-string">'/book/:id(\\\d+)'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时 id 不是数字时，会跳转 404，被认为 URL 对应的页面找不到啦。</p>
<h4 data-id="heading-8">底层依赖</h4>
<p>有了这么多场景，那 Router 是怎样实现的呢？其实它底层是依赖了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpillarjs%2Fpath-to-regexp%2Ftree%2Fv1.7.0" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pillarjs/path-to-regexp/tree/v1.7.0" ref="nofollow noopener noreferrer">path-to-regexp</a> 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> pathToRegexp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path-to-regexp'</span>)
<span class="hljs-comment">// pathToRegexp(path, keys, options)</span>
<span class="hljs-comment">// 示例</span>
<span class="hljs-keyword">var</span> keys = []
<span class="hljs-keyword">var</span> re = pathToRegexp(<span class="hljs-string">'/foo/:bar'</span>, keys)
<span class="hljs-comment">// re = /^\/foo\/([^\/]+?)\/?$/i</span>
<span class="hljs-comment">// keys = [&#123; name: 'bar', prefix: '/', delimiter: '/', optional: false, repeat: false, pattern: '[^\\/]+?' &#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>delimiter：重复参数的定界符，默认是 '/'，可配置</p>
</blockquote>
<p>一些其他常用的路由正则通配符：</p>
<ul>
<li>
<p>? 可选参数</p>
</li>
<li>
<p>* 匹配 0 次或多次</p>
</li>
<li>
<p>+ 匹配 1 次或多次</p>
</li>
</ul>
<p>如果忘记写参数名字，而只写了路由规则，比如下述代码中 <code>/:foo</code> 后面的参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> re = pathToRegexp(<span class="hljs-string">'/:foo/(.*)'</span>, keys)
<span class="hljs-comment">// 匹配除“\n”之外的任何字符</span>
<span class="hljs-comment">// keys = [&#123; name: 'foo', ... &#125;, &#123; name: 0, ...&#125;]</span>
re.exec(<span class="hljs-string">'/test/route'</span>)
<span class="hljs-comment">//=> ['/test/route', 'test', 'route']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它也会被正确解析，只不过在方法处理的内部，未命名的参数名会被替换成数组下标。</p>
<h3 data-id="heading-9">取路由参数</h3>
<p>path 带的参数，可以通过 <code>this.props.match</code> 获取</p>
<p>例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// url 为 /book/:pageType(edit|detail|add)</span>
<span class="hljs-keyword">const</span> &#123; match &#125; = <span class="hljs-built_in">this</span>.props;
<span class="hljs-keyword">const</span> &#123; pageType &#125; = match.params;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于有 #，# 之后的所有内容都会被认为是 hash 的一部分，window.location.search 是取不到问号带的参数的。</p>
<p>比如：<a href="https://link.juejin.cn/?target=http%3A%2F%2Faaa.bbb.com%2Fbook-center%2F%23%2Fbook%2Flist%3Fid%3D123" target="_blank" rel="nofollow noopener noreferrer" title="http://aaa.bbb.com/book-center/#/book/list?id=123" ref="nofollow noopener noreferrer">aaa.bbb.com/book-center…</a></p>
<p>那么在 React-Router 中，问号带的参数，可以通过 <code>this.props.location</code> （官方墙推 👍）获取。个人理解是因为 React-Router 帮我们做了处理，通过路由和 hash 值（window.location.hash）做了解析的封装。</p>
<p>例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// url 为 /book?pageType=edit</span>
<span class="hljs-keyword">const</span> &#123; location &#125; = <span class="hljs-built_in">this</span>.props;
<span class="hljs-keyword">const</span> searchParams = location.search; <span class="hljs-comment">// ?pageType=edit</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际打印 props 参数发现，<code>this.props.history.location</code> 也可以取到问号参数，但不建议使用，因为 React 的生命周期（componentWillReceiveProps、componentDidUpdate）可能使它变得不可靠。（原因可参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzrq1210%2Farticle%2Fdetails%2F108403772%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zrq1210/article/details/108403772%EF%BC%89" ref="nofollow noopener noreferrer">blog.csdn.net/zrq1210/art…</a></p>
<p>在早期的 React-Router 2.0 版本是可以用 location.query.pageType 来获取参数的，但是 V4.0 去掉了（有人认为查询参数不是 URL 的一部分，有人认为现在有很多第三方库，交给开发者自己去解析会更好，有个对此讨论的 Issue，有兴趣的可以自行获取 😊 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FReactTraining%2Freact-router%2Fissues%2F4410%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ReactTraining/react-router/issues/4410%EF%BC%89" ref="nofollow noopener noreferrer">github.com/ReactTraini…</a></p>
<p>针对上一节中场景 1 的 Case C，查询参数隐身式带法时（从 state 里带过去的），在 <code>this.props.location.state</code> 里可以取到（不推荐不推荐不推荐，刷新会没～）</p>
<h3 data-id="heading-10">Switch</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
    <span class="hljs-attr">path</span>=<span class="hljs-string">"/router/:type"</span>
    <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>影像<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
  /></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
    <span class="hljs-attr">path</span>=<span class="hljs-string">"/router/book"</span>
    <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>图书<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
  /></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code><Route /></code> 是平铺的（用 <code>div</code> 包裹是因为 Router 下只能有一个元素），输入 <code>/router/book</code> 则影像和图书都会被渲染出来，如果想要只精确渲染其中一个，则需要 Switch</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Switch>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
    <span class="hljs-attr">path</span>=<span class="hljs-string">"/router/:type"</span>
    <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>影像<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
  /></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span>
    <span class="hljs-attr">path</span>=<span class="hljs-string">"/router/book"</span>
    <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>图书<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
  /></span>
</Switch>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Switch 的意思便是精准的根据不同的 path 渲染不同 Route 下的组件。
但是，加了 Switch 之后路由匹配规则是从上到下执行，一旦发现匹配，就不再匹配其余的规则了。因此在使用的时候一定要“百般小心”。</p>
<p>上面代码中，用户访问 <code>/router/book</code> 时，不会触发第二个路由规则（不会 展示“图书”），因为它会匹配 <code>/router/:type</code> 这个规则。因此，带参数的路径一般要写在路由规则的底部。</p>
<h3 data-id="heading-11">路由的基本原理</h3>
<p>路由做的事情：管控 URL 变化，改变浏览器中的地址。</p>
<p>Router 做的事情：URL 改变时，触发渲染，渲染对应的组件。</p>
<p>URL 有两种，一种不带 #，一种带 #，分别对应 Browse 模式和 Hash 模式。</p>
<p>一般单页应用中，改变 URL，但是不重新加载页面的方式有两类：</p>
<p><strong>Case 1</strong>（会触发路由监听事件）：点击 前进、后退，或者调用的 history.back( )、history.forward( )</p>
<p><strong>Case 2</strong>（不会触发路由监听事件）：组件中调用 history.push( ) 和 history.replace( )</p>
<p>于是参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzl_alien%2Farticle%2Fdetails%2F109231294" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zl_alien/article/details/109231294" ref="nofollow noopener noreferrer">「源码解析 」这一次彻底弄懂 React-Router 路由原理</a> 一文，针对上述两种 Case，以及这两种 Case 分别对应的两种模式，作出如下总结。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17fafcbe7db443aeabc17154335d782d~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>图片来源：「源码解析 」这一次彻底弄懂 React-Router 路由原理</p>
</blockquote>
<h3 data-id="heading-12">Browser 模式</h3>
<p><strong>Case 1:</strong></p>
<p>URL 改变，触发路由的监听事件 <code>popstate</code>，then，监听事件的回调函数 <code>handlePopState</code> 在回调中触发 history 的 <code>setState</code> 方法，产生新的 location 对象。state 改变，通知 Router 组件更新 <code>location</code> 并通过 context 上下文传递，匹配出符合的 Route 组件，最后由 <code><Route /></code> 组件取出对应内容，传递给渲染页面，渲染更新。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* 简化版的 handlePopState （监听事件的回调） */</span>
<span class="hljs-keyword">const</span> handlePopState = <span class="hljs-function">(<span class="hljs-params">event</span>)=></span>&#123;
     <span class="hljs-comment">/* 获取当前location对象 */</span>
    <span class="hljs-keyword">const</span> location = getDOMLocation(event.state)
    <span class="hljs-keyword">const</span> action = <span class="hljs-string">'POP'</span>
     <span class="hljs-comment">/* transitionManager 处理路由转换 */</span>
    transitionManager.confirmTransitionTo(location, action, getUserConfirmation, <span class="hljs-function">(<span class="hljs-params">ok</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (ok) &#123;
          setState(&#123; action, location &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          revertPop(location)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Case 2:</strong>
以 history.push 为例，首先依据你要跳转的 path 创建一个新的 <code>location</code> 对象，然后通过 <code>window.history.pushState</code> （H5 提供的 API ）方法改变浏览器当前路由（即当前的 url），最后通过 <code>setState</code> 方法通知 Router，触发组件更新。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> push = <span class="hljs-function">(<span class="hljs-params">path, state</span>) =></span> &#123;
   <span class="hljs-keyword">const</span> action = <span class="hljs-string">'PUSH'</span>
   <span class="hljs-comment">/* 创建location对象 */</span>
   <span class="hljs-keyword">const</span> location = createLocation(path, state, createKey(), history.location)
   <span class="hljs-comment">/* 确定是否能进行路由转换 */</span>
   transitionManager.confirmTransitionTo(location, action, getUserConfirmation, <span class="hljs-function">(<span class="hljs-params">ok</span>) =></span> &#123;
   ... <span class="hljs-comment">// 此处省略部分代码</span>
   <span class="hljs-keyword">const</span> href = createHref(location)
   <span class="hljs-keyword">const</span> &#123; key, state &#125; = location
   <span class="hljs-keyword">if</span> (canUseHistory) &#123;
     <span class="hljs-comment">/* 改变 url */</span>
     globalHistory.pushState(&#123; key, state &#125;, <span class="hljs-literal">null</span>, href)
     <span class="hljs-keyword">if</span> (forceRefresh) &#123;
       <span class="hljs-built_in">window</span>.location.href = href
     &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-comment">/* 改变 react-router location对象, 创建更新环境 */</span>
       setState(&#123; action, location &#125;)
     &#125;
   &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-built_in">window</span>.location.href = href
   &#125;
 &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">Hash 模式</h3>
<p><strong>Case 1:</strong></p>
<p>增加监听，当 URL 的 Hash 发生变化时，触发 hashChange 注册的回调，回调中去进行相类似的操作，进而展示不同的内容。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
  <span class="hljs-comment">/* 监听改变 */</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Case 2:</strong>
<code>history.push</code> 底层调用 <code>window.location.hash</code> 来改变路由。<code>history.replace</code> 底层是调用 <code>window.location.replace</code> 改变路由。然后 setState 通知改变。</p>
<p>从一些参考资料中显示，出于兼容性的考虑（H5 的方法 IE10 以下不兼容），路由系统内部将 Hash 模式作为创建 History 对象的默认方法。（此处若有疑议，欢迎指正～）</p>
<h2 data-id="heading-14">Dva/Router</h2>
<p>在实际项目中发现，Link，Route 都是从 <code>dva/router</code> 中引进来的，那么，Dva 在这之中做了什么呢？</p>
<p>答案：貌似没有做特殊处理，Dva 在 React-Router 上做了上层封装，会默认输出 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FReactTraining%2Freact-router" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ReactTraining/react-router" ref="nofollow noopener noreferrer">React-Router</a> 接口。</p>
<h2 data-id="heading-15">我们对 Router 做过的一些处理</h2>
<p><strong>Case 1:</strong></p>
<p>项目代码的 src 目录下，不管有多少文件夹，路由一般会放在同一个 router.js 文件中维护，但这样会导致页面太多时，文件内容会越来越长，不便于查找和修改。</p>
<p>因此我们可以做一些小改造，在 src 下的每个文件夹中，创建自己的路由配置文件，以便管理各自的路由。但这种情况下 React-Router 是不能识别的，于是我们写了一个 Plugin 放在 Webpack 中，目的是将各个文件夹下的路由汇总，并生成 router-config.js 文件。之后，将该文件中的内容解析成组件需要的相关内容。插件实现方式可了解本团队另一篇文章： <a href="https://juejin.cn/post/6968988552075952141" target="_blank" title="https://juejin.cn/post/6968988552075952141">手把手带你入门 Webpack Plugin</a>。</p>
<p><strong>Case 2:</strong></p>
<p>路由的 Hash 模式虽然兼容性好，但是也存在一些问题：</p>
<ol>
<li>对于 SEO、前端埋点不太友好，不容易区分路径</li>
<li>原有页面有锚点时，使用 Hash 模式会出现冲突</li>
</ol>
<p>因此公司内部做了一次 Hash 路由转 Browser 路由的改造。</p>
<p>如原有链接为：<a href="https://link.juejin.cn/?target=http%3A%2F%2Faaa.bbb.com%2Fbook-center%2F%23%2Fbook%2Flist%3Fid%3D123" target="_blank" rel="nofollow noopener noreferrer" title="http://aaa.bbb.com/book-center/#/book/list?id=123" ref="nofollow noopener noreferrer">aaa.bbb.com/book-center…</a></p>
<p>改造方案为：</p>
<p>通过新增以下配置代码去掉 #</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createHistory <span class="hljs-keyword">from</span> <span class="hljs-string">'history/createBrowserHistroy'</span>;
<span class="hljs-keyword">const</span> app = dva(&#123;
  <span class="hljs-attr">history</span>: createHistory(&#123;
    <span class="hljs-attr">basename</span>: <span class="hljs-string">'/book-center'</span>,
  &#125;),
  onError,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，为了避免用户访问旧页面出现 404 的情况，前端需要在 Redirect 中配置重定向以及在 Nginx 中配置旧的 Hash 页面转发。</p>
<p><strong>Case 3:</strong></p>
<p>在实际项目中，其实我们也会去考虑用户未授权时路由跳转、页面 404 时路由跳转等不同情况，以下 Case 和代码仅供读者参考～</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Switch>
  &#123;
    getRoutes(match.path, routerData).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span>
    (
      <span class="hljs-comment">// 用户未授权处理，AuthorizedRoute 为项目中自己实现的处理组件</span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AuthorizedRoute</span>
        &#123;<span class="hljs-attr">...item</span>&#125;
        <span class="hljs-attr">redirectPath</span>=<span class="hljs-string">"/exception/403"</span>
      /></span></span>
    )
    )
  &#125;
  <span class="hljs-comment">// 默认跳转页面</span>
  <Redirect <span class="hljs-keyword">from</span>=<span class="hljs-string">"/"</span> exact to=<span class="hljs-string">"/list"</span> />
  <span class="hljs-comment">// 页面 404 处理</span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;props</span> =></span> <span class="hljs-tag"><<span class="hljs-name">NotFound</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span>&#125; /></span>
</Switch>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">参考链接</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzl_alien%2Farticle%2Fdetails%2F109231294" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zl_alien/article/details/109231294" ref="nofollow noopener noreferrer">「源码解析 」这一次彻底弄懂react-router路由原理</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fpqjwyn%2Fp%2F9936153.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/pqjwyn/p/9936153.html" ref="nofollow noopener noreferrer">react-router v4 路由规则解析</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Faibokalv.oschina.io%2Fmyarticle%2F2017%2F04%2F01%2F20170401%25E4%25BA%258C%25E7%25BA%25A7%25E5%258A%25A8%25E6%2580%2581%25E8%25B7%25AF%25E7%2594%25B1%25E7%259A%2584%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aibokalv.oschina.io/myarticle/2017/04/01/20170401%E4%BA%8C%E7%BA%A7%E5%8A%A8%E6%80%81%E8%B7%AF%E7%94%B1%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/" ref="nofollow noopener noreferrer">二级动态路由的解决方案</a></p>
<h2 data-id="heading-17">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6984547134062198791" target="_blank" title="https://juejin.cn/post/6984547134062198791">最熟悉的陌生人rc-form</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fabout-vite" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/about-vite" ref="nofollow noopener noreferrer">Vite 特性和部分源码解析</a></p>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank" title="https://juejin.cn/post/6974184935804534815">我在工作中是如何使用 git 的</a></p>
<p><a href="https://juejin.cn/post/6987140782595506189" target="_blank" title="https://juejin.cn/post/6987140782595506189">如何搭建适合自己团队的构建部署平台</a></p>
<h2 data-id="heading-18">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Fopenweekly%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/openweekly/" ref="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-19">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            