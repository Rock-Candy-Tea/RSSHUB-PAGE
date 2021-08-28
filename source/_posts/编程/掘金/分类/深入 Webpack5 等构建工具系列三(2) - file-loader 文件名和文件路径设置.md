
---
title: '深入 Webpack5 等构建工具系列三(2) - file-loader 文件名和文件路径设置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55c41d353e71405186fc6a229936ac74~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 18:43:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55c41d353e71405186fc6a229936ac74~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第26天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><a href="https://juejin.cn/post/7001055586615820302" target="_blank" title="https://juejin.cn/post/7001055586615820302">上一篇文章</a>我们讲了 <code>file-loader</code> 的使用，我们配置了相关规则，使得当遇到 <code>png</code> 或 <code>jpeg</code> 或 <code>jpg</code> 或 <code>gif</code> 或 <code>svg</code> 图片时，将它们交给 <code>file-loader</code> 处理。</p>
<p>下面，如果我们想要修改 <code>file-loader</code> 默认给我们生成的图片的名字，该怎么做呢？</p>
<p>首先，我们要知道，<code>file-loader</code> 在处理图片文件时，会根据文件内容通过 <code>md4</code> 摘要算法来生成 <code>128</code> 位（<code>bit</code>）长度（然后每 <code>4</code> 位就用 <code>16</code> 进制表示为 <code>1</code> 位，最后显示的就是 <code>32</code> 位长度）的哈希值，作为打包后的图片名称。显然，这样做有一个弊端，就是无法知道打包后的图片和打包前的图片的对应关系。但我们希望能够清楚地知道打包前后图片的对应关系，把图片原来的名字也加到打包后的图片名字中去，即我们希望能对图片进行重命名。</p>
<h2 data-id="heading-0">1. 文件名称的规则</h2>
<ul>
<li>
<p>有时候我们处理后的<strong>文件名称</strong>需要按照一定的规则进行显示：</p>
<ul>
<li>比如保留原来的<strong>文件名、扩展名</strong>，同时为了防止重复，包含一个 <strong><code>hash</code> 值</strong>等；</li>
</ul>
</li>
<li>
<p>这个时候我们可以使用 <strong><code>placeholders</code></strong> 来完成，<code>webpack</code> 给我们提供了大量的 <code>placeholders</code> 来显示不同的内容：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.js.org%2Floaders%2Ffile-loader%2F%23placeholders" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.js.org/loaders/file-loader/#placeholders" ref="nofollow noopener noreferrer">v4.webpack.js.org/loaders/fil…</a></li>
<li>我们可以在文档中查阅自己需要的 <code>placeholder</code>；</li>
</ul>
</li>
<li>
<p>这里介绍几个最常用的 <code>placeholder</code>：</p>
<ul>
<li><strong><code>[ext]</code></strong> ： 处理文件的扩展名；</li>
<li><strong><code>[name]</code></strong> ：处理文件的名称；</li>
<li><strong><code>[hash]</code></strong> ：文件的内容，使用 <code>MD4</code> 的散列函数（哈希函数/摘要函数）处理，生成的一个 <code>128</code> 位的 <code>hash</code> 值（ <code>32</code> 个十六进制）；</li>
<li><strong><code>[contenthash]</code></strong> ：在 <code>file-loader</code> 中和 <strong><code>[hash]</code></strong> 结果是一致的（在 <code>webpack</code> 的一些其它地方不一样，后面会讲到）；</li>
<li><strong><code>[hash:<length>]</code></strong> ：截取 <code>hash</code> 的长度，默认 <code>32</code> 个字符太长了；</li>
<li><strong><code>[path]</code></strong> ：文件相对于 <code>webpack</code> 配置文件的路径；</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">2. 设置文件名称</h2>
<p>下面，我们就对 <code>file-loader</code> 要处理的文件最后打包出来的文件的名字进行自定义配置，来到 <code>webpack</code> 的配置文件中，对处理图片的 <code>Rule</code> 的 <code>use</code> 属性内容进行修改：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55c41d353e71405186fc6a229936ac74~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215164720799.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: [
    &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
      <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'[name].[hash:6].[ext]'</span>
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在当前项目目录下运行 <code>npm run build</code> 命令进行编译打包（建议先把输出目录 <code>build</code> 目录下之前生成的两张图片删除后再运行命令），成功打包后再来看输出目录下的内容：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c82e2f1828b42659ac9d40afcff41e3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215165138813.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，打包后的图片成功地按照我们指定的格式（<code>原文件名称.6 位 hash 值.原文件扩展名</code>）重命名了。</p>
<h2 data-id="heading-2">3. 设置文件的存放路径</h2>
<p>除了文件的名称设置，还有一个问题，就是当有很多文件时，如果所有文件最后都打包到输出目录下，看上去就会有很多文件也很乱。因此，如果有多张图片，我们希望将它们都放到一个文件夹中去（比如名为 <code>img</code> 的文件夹）。这时，我们就可以通过 <code>outputPath</code> 属性来指定目标文件要放置的文件系统路径：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19f86ba12444c5396dd88dbff69684d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215170710011.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: [
    &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
      <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'[name].[hash:6].[ext]'</span>,
        <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'img'</span>
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除 <code>build</code> 目录后重新运行 <code>npm run build</code> 命令打包，重新生成的 <code>build</code> 目录如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b0eac8dc204919bbe6b5c8d7bf5f1f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215170849719.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，两张图片都已经放在了 <code>img</code> 文件夹下。</p>
<p>事实上，还有另外一种更常用的方式来指定目标文件要放置的文件系统路径，即直接在 <code>options.name</code> 中的最前面加上要放置的路径：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a9fbdca284740c0b669efa77714abdc~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215171121267.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: [
    &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
      <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name].[hash:6].[ext]'</span>,
        <span class="hljs-comment">// outputPath: 'img'</span>
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新运行 <code>npm run build</code> 命令打包，也能成功将两张图片放置在输出目录下的 <code>img</code> 文件夹下。</p>
<p>以上，就是对 <code>file-loader</code> 输出的文件进行重命名并且将文件输出到指定文件夹下的操作说明。</p></div>  
</div>
            