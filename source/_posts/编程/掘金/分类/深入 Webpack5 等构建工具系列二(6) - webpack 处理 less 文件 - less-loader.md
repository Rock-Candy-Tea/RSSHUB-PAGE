
---
title: '深入 Webpack5 等构建工具系列二(6) - webpack 处理 less 文件 - less-loader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f30265eb3e9c4a11b8e5700fa51a3df5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 16:31:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f30265eb3e9c4a11b8e5700fa51a3df5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>在开发中，我们可能会使用 <strong><code>less</code>、<code>sass</code>、<code>stylus</code> 等预处理器</strong>来编写 <code>css</code> 样式，以提高效率。那么，如何可以让我们的<strong>环境支持这些预处理器</strong>呢？</p>
<p>首先我们需要确定，<code>less</code>、<code>sass</code> 等编写的 <code>css</code> 需要通过工具转换成普通的 <code>css</code>；比如说我们现在在项目的 <code>./src/css</code> 路径下新建一个 <code>component.less</code> 的 <code>less</code> 文件，里面编写一些 <code>less</code> 代码：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@fontSize:</span> <span class="hljs-number">50px</span>;
<span class="hljs-variable">@fontWeight:</span> <span class="hljs-number">700</span>;

<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-variable">@fontSize</span>;
  <span class="hljs-attribute">font-weight</span>: <span class="hljs-variable">@fontWeight</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写完之后，先思考一下，当前这个 <code>component.less</code> 文件是否会被 <code>webpack</code> 加载？当然是不会的，因为这个文件不在依赖关系图中。那为了让它可以被加载，我们可以来到 <code>component.js</code> 文件中，在文件的头部添加一行代码文件来引入这个 <code>component.less</code> 文件：<code>import '../css/component.less';</code>，如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f30265eb3e9c4a11b8e5700fa51a3df5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210125070811815.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样引入之后，就意味着在使用 <code>webpack</code> 进行编译打包时，也会对这个 <code>less</code> 文件进行编译和加载了。</p>
<p>下面，我们先运行 <code>npm run build</code> 命令，看下当前这个 <code>less</code> 文件能不能被正常解析：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72269d23882741e1a1836c71c836fd0f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210125185302350.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，运行报错了，报错内容和之前安装 <code>css-loader</code> 后就运行命令出现的报错信息是类似的。那我们该怎么做呢？</p>
<p>首先，我们要知道，浏览器是不认识 <code>less</code> 代码的，所以 <code>less</code> 代码最终必须转换成 <code>css</code> 代码，浏览器才能识别。那么 <code>less</code> 的代码怎么转成 <code>css</code> 的代码呢？你可能会说，用 <code>less-loader</code> 呀，但事实上，<code>less-loader</code> 只不过是做了下处理，真正对 <code>less</code> 的代码做编译的其实是一个独立的工具（跟 <code>webpack</code> 没有任何关系）—— <code>less</code>，就是说，真正把 <code>less</code> 代码转换成 <code>css</code> 代码的是这个 <code>less</code> 工具。</p>
<p>但当前项目中，还没有这个 <code>less</code> 工具，所以我们先安装它（只是开发时需要将 <code>less</code> 代码转换成 <code>css</code> 代码，所以这里使用 <code>-D</code>）：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install less -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后，我们也可以在项目中的 <code>node_modules</code> 文件夹下的 <code>.bin</code> 目录下找到 <code>lessc</code> 这个文件（没有的话可以先刷新一下目录），它能帮助我们对 <code>less</code> 文件进行编译然后转换为 <code>css</code> 文件。</p>
<p>下面，我们就使用 <code>less</code> 这个工具来把 <code>less</code> 文件编译为 <code>css</code> 文件，运行命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx less ./src/css/component.less > component.css
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这条命令的意思是，使用 <code>less</code> 工具将当前路径下的 <code>src</code> 目录下的 <code>css</code> 目录下的 <code>component.less</code> 文件转换为 <code>css</code> 文件，生成文件的位置为当前目录下的 <code>component.css</code> 文件。</p>
<p>成功运行上述命令后，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38ce5cc6511b449e8a6811b069a9affe~tplv-k3u1fbpfcp-watermark.image" alt="image-20210126205220070.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在当前目录（这里为当前项目的根目录）下多了一个 <code>component.css</code> 文件，里面的内容也都是正常的 <code>css</code> 代码，之前 <code>component.less</code> 文件中的变量在这里已经被替换为了数值。可见，通过 <code>shell</code> 命令的方式可以直接把 <code>less</code> 文件转换成 <code>css</code> 文件。</p>
<p>但是，在开发中肯定有大量的 <code>less</code> 文件，如果还是像上面这样一个个地去运行 <code>shell</code> 命令肯定不现实呀~</p>
<p>所以，我们还需要在项目中安装 <code>less-loader</code>，它会基于 <code>less</code> 这个工具（这意味着我们首先得安装好 <code>less</code>，如果之前没有安装 <code>less</code>，那么就得同时安装 <code>less</code> 和 <code>less-loader</code>）帮助我们将 <code>less</code> 文件转成 <code>css</code> 文件。</p>
<p>好，下面我们安装 <code>less-loader</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install less-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装好以后，我们就需要来到 <code>webpack</code> 的配置文件（这里是 <code>wk.config.js</code>）中设置 <code>less</code> 文件的处理规则了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
  <span class="hljs-attr">rules</span>: [
    <span class="hljs-comment">/* 处理 css 文件 */</span>
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">/* 处理 less 文件 */</span>
    &#123;
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
      use: [
        <span class="hljs-string">'style-loader'</span>,
        <span class="hljs-string">'css-loader'</span>,
        <span class="hljs-string">'less-loader'</span>
      ]
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释一下，处理 <code>less</code> 文件需要用到 <code>less-loader</code>，<code>less-loader</code> 又会使用到 <code>less</code>，但我们不需要在配置文件中对 <code>less</code> 做任何配置，因为 <code>less-loader</code> 会自动去加载 <code>less</code> 包然后进行使用的。所以，这里只需要写 <code>less-loader</code>。那 <code>less</code> 文件加载完成后就变成了 <code>css</code> 文件，这时又要对 <code>css</code> 文件做进一步处理，所以就需要 <code>css-loader</code> 了，那接下来为了能让 <code>css</code> 代码插入到页面中，我们又需要 <code>style-loader</code> 了。因此，我们需要依次执行 <code>less-loader</code>、<code>css-loader</code>、<code>style-loader</code>。</p>
<p>配置完成后，再来运行 <code>npm run build</code> 命令，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada4c9e218924d008e01d788d0275707~tplv-k3u1fbpfcp-watermark.image" alt="image-20210126213147215.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，已经没有刚才的报错信息了。来到浏览器页面，也可以看到字体已被放大加粗了：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ccc09af0ed3460b81421d5f007266bc~tplv-k3u1fbpfcp-watermark.image" alt="image-20210126213620987.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上，就是 <code>less-loader</code> 处理 <code>less</code> 文件的过程，匹配上 <code>.less</code> 文件后依次按照 <code>less-loader</code>、<code>css-loader</code>、<code>style-loader</code> 的顺序（即编写顺序为从下往上或从右往左）来处理就可以了。</p></div>  
</div>
            