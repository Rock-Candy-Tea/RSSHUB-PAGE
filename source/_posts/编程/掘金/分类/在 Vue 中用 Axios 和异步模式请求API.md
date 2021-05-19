
---
title: '在 Vue 中用 Axios 和异步模式请求API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a64c0b745014a178fdaf2eb2e5b1e00~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 03:10:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a64c0b745014a178fdaf2eb2e5b1e00~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Axios 是 Javascript 中最受欢迎的 HTTP 库之一，我们可以用它在 Vue 程序中调用API。</p>
<p>在本文中我们用 Vue 3 和 Axios 写一个侃爷语录小应用，侃爷是国内粉丝对美国当红饶舌歌手 Kanye West 的昵称。可以用这个小程序学习英语，同时也能从侃爷的话中得到一些启发，而且还可以学习用 Vue 异步请求API，一举多得，何乐而不为呢？</p>
<h2 data-id="heading-0">设置基本 HTTP 请求</h2>
<p>首先在终端中执行下面的命令把 Axios 安装到项目中：</p>
<pre><code class="hljs language-bash copyable" lang="bash">install axiosnpm install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在 Vue 组件中像这样导入axios。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vie - importing axios</span>
<script>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
  
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来用 <code>axios.get</code> 通过 Kanye REST API 的 URL 获取随机语录。之后可以用 <code>Promise.then</code> 等待请求返回响应。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue - sending our HTTP request</span>
<script>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
     axios.get(<span class="hljs-string">'https://api.kanye.rest/'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-comment">// handle response</span>
     &#125;)
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在可以从 API 中获取响应了，先看一下它的含义。 把它保存成名为 <code>quote</code> 的引用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue - storing the response</span>
<script>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
     axios.get(<span class="hljs-string">'https://api.kanye.rest/'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-comment">// handle response</span>
        quote.value = response
     &#125;)
     <span class="hljs-keyword">return</span> &#123;
      quote
     &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后将其输出到模板中并以斜体显示，并用引号引起来，另外还需要给这条语录加上引用来源。</p>
<pre><code class="hljs language-xml copyable" lang="xml">//App.vue - template code
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span>></span>"&#123;&#123; quote &#125;&#125;"<span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>- Kanye West<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检查一下浏览器中的内容。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a64c0b745014a178fdaf2eb2e5b1e00~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我们可以看到随机返回的侃爷语录，还有一些额外的信息，例如请求的响应码等。</strong></p>
<p>对于我们这个小应用，只对这个 <code>data.quote</code> 值感兴趣，所以要在脚本中指定要访问 <code>response</code>  上的哪个属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue - getting only our quote</span>
axios.get(<span class="hljs-string">'https://api.kanye.rest/'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-comment">// handle response</span>
        quote.value = response.data.quote
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码可以得到想要的内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738da50acf7545d48121b0f8d897808a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Axios 配合 async/await</h2>
<p>可以在 Vue 程序中把 Axios 和 <code>async</code> /<code>await</code> 模式结合起来使用。</p>
<p>在设置过程中，首先注释掉当前的 GET 代码，然后创建一个名为 <code>loadQuote</code> 的异步方法。 在内部，可以使用相同的 <code>axios.get</code> 方法，但是我们想用 <code>async</code> 等待它完成，然后把结果保存在一个名为 <code>response</code> 的常量中。</p>
<p>然后设置 <code>quote</code> 的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue - async Axios</span>
<span class="hljs-keyword">const</span> loadQuote = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.getQuote()
      quote.value = response.data.quote
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它和前面的代码工作原理完全一样，但这次用了异步模式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0624cf1b850840e9908118331dd3037d~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Axios 的错误处理</h2>
<p>在 async-await 模式中，可以通过 try 和 catch 来为 API 调用添加错误处理：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//Error handling with async/await</span>
<span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.getQuote()
        quote.value = response.data.quote
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.log(err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用原始的 promises 语法，可以在 API 调用之后添加 <code>.catch</code> 捕获来自请求的任何错误。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//Error handling with Promises</span>
axios.get(<span class="hljs-string">'https://api.kanye.rest/'</span>)
      .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-comment">// handle response</span>
        quote.value = response.data.quote
      &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">发送POST请求</h2>
<p>下面看一下怎样发送 POST 请求。在这里我们使用 <a href="https://jsonplaceholder.typicode.com/" target="_blank" rel="nofollow noopener noreferrer">JSONPlaceholder Mock API 调用</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8bca2bb9a214719b321f14be27a5923~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://jsonplaceholder.typicode.com/guide/" target="_blank" rel="nofollow noopener noreferrer">他们的文档</a>中提供了一个测试 POST 请求的  <code>/posts</code>  接口。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6049abcf4034793ab2480dba5843905~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们需要创建一个按钮，当点击按钮时将会触发我们的API调用。在模板中创建一个名为 <em>“Create Post”</em> 的按钮，单击时调用名为 <code>createPost</code> 方法。</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span>></span>"&#123;&#123; quote &#125;&#125;"<span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>- Kanye West<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"createPost"</span>></span>Create Post<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面在代码中创建 <code>createPost</code> 方法，然后从 <code>setup</code> 返回。</p>
<p>这个方法，类似于前面的 GET 请求，只需要调用 <code>axios.post</code> 并传入URL（即<code>https://jsonplaceholder.typicode.com/posts</code> ）就可以复制粘贴文档中的数据了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue</span>
<span class="hljs-keyword">const</span> createPost = <span class="hljs-function">() =></span> &#123;
      axios.post(<span class="hljs-string">'https://jsonplaceholder.typicode.com/posts'</span>, <span class="hljs-built_in">JSON</span>.stringify(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'foo'</span>,
          <span class="hljs-attr">body</span>: <span class="hljs-string">'bar'</span>,
          <span class="hljs-attr">userId</span>: <span class="hljs-number">1</span>,
      &#125;)).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(response)
      &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单击按钮试一下，可以看到控制台输出了大量信息，告诉我们 POST 请求已成功完成。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb226b12677947e7988ad4fececdba9d~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">用 Axios 编写可复用的 API 调用</h2>
<p>在项目中通过创建一个 <code>src/services</code> 目录，用它来组织所有 api 调用。</p>
<p>目录中包含 2 种类型的文件：</p>
<ul>
<li><code>API.js</code> ：用来创建一个带有定义的 <code>baseURL</code> 的 Axios 实例，这个实例会用于所有的路由</li>
<li><code>*&#123;specific functionality&#125;*API.js</code> ：更具体的文件，可用于将 api 调用组织成<strong>可重用的模块</strong></li>
</ul>
<p>这样做的好处是可以方便的在开发和生产服务器之间进行切换，只需修改一小段代码就行了。</p>
<p>创建 <code>services/API.js</code> 文件，并将 Axios baseURL 设置为默认为 Kanye REST API。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">API.jsimport axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>(url=<span class="hljs-string">'https://api.kanye.rest'</span>) => &#123;
    <span class="hljs-keyword">return</span> axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: url,
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来创建一个 <code>KanyeAPI.js</code> 文件并从 <code>./API</code> 中导入 API。 在这里我们要导出不同的 API 调用。</p>
<p>调用 <code>API()</code> 会给得到一个 Axios 实例，可以在其中调用 <code>.get</code> 或 <code>.post</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//KanyeAPI.js</span>
<span class="hljs-keyword">import</span> API <span class="hljs-keyword">from</span> <span class="hljs-string">'./API'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">getQuote</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> API().get(<span class="hljs-string">'/'</span>)
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>App.vue</code> 内部，让我们的组件通过可复用的 API 调用来使用这个新文件，而不是自己再去创建 Axios。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue</span>
<span class="hljs-keyword">const</span> loadQuote = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.getQuote() <span class="hljs-comment">// <--- THIS LINE</span>
        quote.value = response.data.quote
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.log(err)
      &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面把 <code>createPost</code> 移到其自己的可重用方法中。</p>
<p>回到 <code>KanyeAPI.js</code> 在导出默认设置中添加 <code>createPost</code>，这会将 POST 请求的数据作为参数传递给我们的 HTTP 请求。</p>
<p>与GET请求类似，通过 API 获取 axios 实例，但这次需要覆盖默认 URL 值并传递 JSONplaceholder url。 然后就可以像过去一样屌用 Axios POST 了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//KanyeAPI.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">getQuote</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> API().get(<span class="hljs-string">'/'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">createPost</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-keyword">return</span> API(<span class="hljs-string">'https://jsonplaceholder.typicode.com/'</span>).post(<span class="hljs-string">'/posts'</span>, data)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如此简单</strong></p>
<p>回到 <code>App.vue</code> ，可以像这样调用新的 post 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//App.vue </span>
<span class="hljs-keyword">const</span> createPost = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.createPost(<span class="hljs-built_in">JSON</span>.stringify(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'foo'</span>,
          <span class="hljs-attr">body</span>: <span class="hljs-string">'bar'</span>,
          <span class="hljs-attr">userId</span>: <span class="hljs-number">1</span>,
      &#125;))

      <span class="hljs-built_in">console</span>.log(response)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在单击按钮时，可以看到专用的 API 能够正常工作。</p>
<p>把 API 调用移出这些 Vue 组件并放在它自己的文件的好处在于，可以在整个程序中的任何位置使用这些 API 调用。这样可以创建更多可重用和可伸缩的代码。</p>
<h2 data-id="heading-5">最终代码</h2>
<pre><code class="hljs language-html copyable" lang="html">// App.vue
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span>></span>"&#123;&#123; quote &#125;&#125;"<span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>- Kanye West<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"createPost"</span>></span>Create Post<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> KanyeAPI <span class="hljs-keyword">from</span> <span class="hljs-string">'./services/KanyeAPI'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;

    <span class="hljs-keyword">const</span> quote = ref(<span class="hljs-string">''</span>)

    <span class="hljs-keyword">const</span> loadQuote = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.getQuote()
        quote.value = response.data.quote
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.log(err)
      &#125;
    &#125;

    loadQuote()
    
    <span class="hljs-comment">// axios.get('https://api.kanye.rest/')</span>
    <span class="hljs-comment">//   .then(response => &#123;</span>
    <span class="hljs-comment">//     // handle response</span>
    <span class="hljs-comment">//     quote.value = response.data.quote</span>
    <span class="hljs-comment">//   &#125;).catch(err => &#123;</span>
    <span class="hljs-comment">//   console.log(err)</span>
    <span class="hljs-comment">// &#125;)</span>

    <span class="hljs-keyword">const</span> createPost = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> KanyeAPI.createPost(<span class="hljs-built_in">JSON</span>.stringify(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'foo'</span>,
          <span class="hljs-attr">body</span>: <span class="hljs-string">'bar'</span>,
          <span class="hljs-attr">userId</span>: <span class="hljs-number">1</span>,
      &#125;))

      <span class="hljs-built_in">console</span>.log(response)
      <span class="hljs-comment">// axios.post('https://jsonplaceholder.typicode.com/posts', JSON.stringify(&#123;</span>
      <span class="hljs-comment">//     title: 'foo',</span>
      <span class="hljs-comment">//     body: 'bar',</span>
      <span class="hljs-comment">//     userId: 1,</span>
      <span class="hljs-comment">// &#125;)).then(response => &#123;</span>
      <span class="hljs-comment">//   console.log(response)</span>
      <span class="hljs-comment">// &#125;)</span>

      
    &#125;
    
    <span class="hljs-keyword">return</span> &#123;
      createPost,
      quote
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: Avenir, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//API.js
import axios from 'axios'

export default(url='https://api.kanye.rest') => &#123;
    return axios.create(&#123;
        baseURL: url,
    &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//KanyeAPI.js
import API from './API'
export default &#123;
    getQuote() &#123;
        return API().get('/')
    &#125;,
    createPost(data) &#123;
        return API('https://jsonplaceholder.typicode.com/').post('/posts', data)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">写在最后</h2>
<p>近期在提升 Vue 的过程中，发现一个高逼格的 Vue3+TS 教程。
无偿分享给掘仔们，<a href="https://www.bilibili.com/video/BV1gf4y1W783" target="_blank" rel="nofollow noopener noreferrer">戳我看教程</a></p></div>  
</div>
            