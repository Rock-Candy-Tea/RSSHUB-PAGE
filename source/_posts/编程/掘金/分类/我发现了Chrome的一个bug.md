
---
title: '我发现了Chrome的一个bug'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5043'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 21:26:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=5043'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">故事的开始</h2>
<p>最近在项目中遇到一个问题，业务逻辑就不在这里介绍了，在排查过程中发现项目里有类似这样一段代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">fetch(url)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> res.text())
  .then(<span class="hljs-function">(<span class="hljs-params">text</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">JSON</span>.parse(text)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面没有对最后一个<code>then</code>进行<code>catch</code>操作，我们怀疑这里出了问题，因为<code>text</code>可能无法解析为合法的<code>JSON</code>，然而事实上我们的项目里是有全局的错误捕获的：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'unhandledrejection'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  sendLog(e)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就奇怪了，华容逢关羽吗？，难道<code>unhandledrejection</code>事件不仅没有捕获到<code>JSON.parse</code>的报错还让它走脱了吗？然后我们做了下面这样代码的尝试：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'unhandledrejection'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'unhandledrejection:'</span>, event);
&#125;)

<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"&#123;"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">JSON</span>.parse(data)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台中出现下下面的报错信息：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">Uncaught (<span class="hljs-keyword">in</span> promise) <span class="hljs-built_in">SyntaxError</span>: Unexpected end <span class="hljs-keyword">of</span> <span class="hljs-built_in">JSON</span> input
  at <span class="hljs-built_in">JSON</span>.parse (<anonymous>)
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这个语法错误是因为<code>JSON.parse</code>无法成功解析的缘故，确实是没有被<code>unhandledrejection</code>捕获，难道是这个事件出了问题吗？索性我们直接抛出错误，看这个事件能不能正常工作：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-number">123</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台出现了下面的信息：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">unhandledrejection: <span class="hljs-number">123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明<code>unhandledrejection</code>事件是没问题的，那为什么<code>JSON.parse</code>的错误不能捕获呢？难道是无法捕获语法错误吗？那我们换一种<code>eval</code>的方式解析<code>JSON</code>，如果无法捕获语法错误，那么<code>eval</code>报的语法错误肯定也无法捕获：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"&#123;"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">eval</span>(data)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再看控制台的输出：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">unhandledrejection: <span class="hljs-built_in">SyntaxError</span>: Unexpected end <span class="hljs-keyword">of</span> input
<span class="copy-code-btn">复制代码</span></code></pre>
<p>蒙圈了吧，这个语法错误居然被捕获到了，我们又想，难道说<code>JSON.parse</code>的报错很特殊吗？我们又做了下面的尝试：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"&#123;"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-built_in">JSON</span>.parse(data)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">throw</span> e
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面尝试将报错通过<code>try...catch...</code>捕获到，然后再重新抛出，然后控制台输出：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">Uncaught (<span class="hljs-keyword">in</span> promise) <span class="hljs-built_in">SyntaxError</span>: Unexpected end <span class="hljs-keyword">of</span> <span class="hljs-built_in">JSON</span> input
  at <span class="hljs-built_in">JSON</span>.parse (<anonymous>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面说明错误仍然没有捕获到，难道是错误信息有问题？那我们把错误包装一下呢：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"&#123;"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-built_in">JSON</span>.parse(data)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">const</span> wraper = <span class="hljs-keyword">new</span> <span class="hljs-built_in">SyntaxError</span>(e.messgae)
      wraper.stack = e.stack
      <span class="hljs-keyword">throw</span> wraper
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面创建了一个<code>SyntaxError</code>的实例<code>wraper</code>，然后把<code>try...catch...</code>捕获到的错误信息放到<code>wraper</code>上，抛出<code>wraper</code>，控制台输出如下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">unhandledrejection: <span class="hljs-built_in">SyntaxError</span>: Unexpected end <span class="hljs-keyword">of</span> input
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看起来错误被捕获到了，我们开始怀疑人生，于是在<code>stackoverflow</code>提了这个疑问：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F68356441%2Fwhy-unhandledrejection-cant-caught-an-error-from-json-parse" title="https://stackoverflow.com/questions/68356441/why-unhandledrejection-cant-caught-an-error-from-json-parse" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">stackoverflow问题地址</a>，内容基本和上文一致，感兴趣的同学可以去看看，另外，对于上面问题在<code>Firefox</code>和<code>Safari</code>中并未出现。</p>
<h2 data-id="heading-1">有意思的事</h2>
<p>在<code>stackoverflow</code>的评论中，一位叫<code>Kaiido</code>的开发者说这可能是<code>Chrome</code>的<code>bug</code>，建议我去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Flist" title="https://bugs.chromium.org/p/chromium/issues/list" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">chromium bug报告网址</a>报告一下，没想到我搜索到了类似的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D1219363%26q%3Dunhandledrejection%26can%3D2" title="https://bugs.chromium.org/p/chromium/issues/detail?id=1219363&q=unhandledrejection&can=2" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">报告</a>，报告人说他发现<code>window.onerror</code>和<code>unhandledrejection</code>这两个事件都无法捕获到<code>JSON.parse</code>的错误：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">window</span>.onerror = <span class="hljs-keyword">async</span> (...args) => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onerror"</span>)
&#125;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'unhandledrejection'</span>, <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"unhandledrejection"</span>)
&#125;)

<span class="hljs-keyword">var</span> elem = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>);
elem.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-literal">undefined</span>); &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面报告人监听的两个事件，说最终都没有被触发，大家也可以试一下，这个例子由于<code>JSON.parse</code>不在<code>Promise</code>中，所以<code>window.onerror</code>是能够捕获的，也就是说报告人的提问不是很恰当，下面维护者的回复就比较搞笑了，这位维护者打开了与报告人相同版本（chrome88）的浏览器和黑暗模式，然后打开<code>chrome</code>空白页，将上面代码粘贴到控制台执行，然后出现下面报错：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">Uncaught <span class="hljs-built_in">TypeError</span>: Cannot read property <span class="hljs-string">'addEventListener'</span> <span class="hljs-keyword">of</span> <span class="hljs-literal">null</span>
  at <anonymous>:<span class="hljs-number">11</span>:<span class="hljs-number">6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后维护者让报告人指出问题的所在，大家应该都看得出来，这个报错是因为页面上没有<code>button</code>元素导致的，与报告人所说的错误没有任何关系，所以我怀疑这个维护者是来搞笑的，时隔几乎一个月，今天上午报告人使用了我在<code>stackoverflow</code>提出的问题作为例子来向维护者说明问题，目前维护者还未回复，大家可以持续关注下</p>
<h2 data-id="heading-2">最后</h2>
<p>在上面问题还没解决的情况下，我们最好还是对现有代码做一下审查，对于使用<code>Promise</code>的地方在<code>then</code>后面一定要加<code>catch</code>方法，对于直接使用<code>JSON.parse</code>的位置，根据对参数的了解情况酌情添加<code>try...catch...</code></p>
<p>对于前端错误监控平台来说，这也是一个棘手的问题，希望未来能从中看到更好的解决方案。</p>
<blockquote>
<p>封面图：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zcool.com.cn%2Fwork%2FZNTM0MzQ2NDg%3D.html" title="https://www.zcool.com.cn/work/ZNTM0MzQ2NDg=.html" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">愚蠢的美人鱼 by 铁柱呆又呆</a></p>
</blockquote>
<p>关注「码生笔谈」公众号，阅读更多有趣文章</p></div>  
</div>
            