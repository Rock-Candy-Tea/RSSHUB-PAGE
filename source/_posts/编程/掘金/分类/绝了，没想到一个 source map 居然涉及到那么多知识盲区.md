
---
title: '绝了，没想到一个 source map 居然涉及到那么多知识盲区'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7221a39259a648ac9135c6db1889bdef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 18:13:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7221a39259a648ac9135c6db1889bdef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Source map 想必大家都不陌生。线上的代码多是压缩后的，如果线上有报错却只能调试那个代码多半是个噩梦。因此我们需要有一个桥梁帮助我们搭建起源代码及压缩后代码的联系，source map 就是起了这个作用。</p>
<p>以下是 MDN 对于 source map 的解释：</p>
<blockquote>
<p>调试原始源代码会比浏览器下载的转换后的代码更加容易。 <a href="https://www.html5rocks.com/en/tutorials/developertools/sourcemaps/" target="_blank" rel="nofollow noopener noreferrer">source map</a> 是从已转换的代码映射到原始源的文件，使浏览器能够重构原始源并在调试器中显示重建的原始源。</p>
</blockquote>
<p>但是不知道各位读者有没有对 source map 的原理产生过疑问？笔者列出了四个疑问，不知道各位是不是也存在过这样的问题：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7221a39259a648ac9135c6db1889bdef~tplv-k3u1fbpfcp-zoom-1.image" alt="Source map 四问" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来的内容会逐步为读者解答这四问。</p>
<h2 data-id="heading-0">source map 文件是否影响网页性能</h2>
<p>这个答案肯定是不会影响，否则构建相关的优化就肯定会涉及到对于 source map 的处理了，毕竟 source map 文件也不小。</p>
<p>其实 source map 只有在打开 dev tools 的情况下才会开始下载，相信大部分用户都不会去打开这个面板，所以这也就不是问题了。</p>
<p>这时可能会有读者想说：哎，但是我好像从来没有在 Network 里看到 source map 文件的加载呀？其实这只是浏览器隐藏了而已，如果大家使用抓包工具的话就能发现在打开 dev tools 的时候开始下载 source map 了。</p>
<h2 data-id="heading-1">source map 存在标准嘛？</h2>
<p>source map 是存在一个标准的，为 Google 及 Mozilla 的工程师制定，<a href="https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit" target="_blank" rel="nofollow noopener noreferrer">文档地址</a>。正是因为存在这份标准，各个打包器及浏览器才能生成及使用 source map，否则就乱套了。</p>
<p>各个打包器基本都基于<a href="https://github.com/mozilla/source-map" target="_blank" rel="nofollow noopener noreferrer">该库</a>来生成 source map，当然也存在一些魔改的方案，但是标准都是统一的。</p>
<p>通过上面的库生成出来的 source map 格式大致如下，大家也可以对比各个打包器的产物，格式及内容大部分都是一致的：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  version: <span class="hljs-number">3</span>,
  file: <span class="hljs-string">"min.js"</span>,
  names: [<span class="hljs-string">"bar"</span>, <span class="hljs-string">"baz"</span>, <span class="hljs-string">"n"</span>],
  sources: [<span class="hljs-string">"one.js"</span>, <span class="hljs-string">"two.js"</span>],
  sourceRoot: <span class="hljs-string">"http://example.com/www/js/"</span>,
  mappings: <span class="hljs-string">"CAAC,IAAI,IAAM,SAAUA,GAClB,OAAOC,IAAID;CCDb,IAAI,IAAM,SAAUE,GAClB,OAAOA"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来笔者介绍下重要字段的作用：</p>
<ul>
<li>version：顾名思义，指代了版本号，目前 source map 标准的版本为 3，也就是说这份 source map 使用的是第三版标准产出的</li>
<li>file：编译后的文件名</li>
<li>names：一个优化用的字段，后续会在 mappings 中用到</li>
<li>sources：多个源文件名</li>
<li>mappings：这是最重要的内容，表示了源代码及编译后代码的关系，但是先略过这块，下文中会详细解释</li>
</ul>
<p>另外大部分应用都是由 webpack 来打包的，可能有些读者会发现 webpack 的 source map   产出的字段于上面的略微有些不一致。</p>
<p>这是因为 webpack 魔改了一些东西，但是底下还是基于这个库实现的，只是变动了一些不涉及核心的字段，<a href="https://github.com/webpack/webpack-sources/blob/master/lib/SourceMapSource.js" target="_blank" rel="nofollow noopener noreferrer">具体代码</a>。</p>
<h2 data-id="heading-2">浏览器怎么知道源文件和 source map 的关系？</h2>
<p>这里我们以 webpack 做个实验，通过 webpack5 对于以下代码进行打包：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们开启 source map 选项以后，产物应该为两个文件，分别为 <code>bundle.js</code> 以及 <code>bundle.js.map</code>。</p>
<p>查看 <code>bundle.js</code> 文件以后我们会发现代码中存在这一一段注释：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
<span class="hljs-comment">//# sourceMappingURL=bundle.js.map</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sourceMappingURL</code> 就是标记了该文件的 source map 地址。</p>
<p>当然除此之外还有别的方式，通过查阅 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/SourceMap" target="_blank" rel="nofollow noopener noreferrer">MDN 文档</a> 发现还可以通过 response header 的 <code>SourceMap: <url></code> 字段来表明。</p>
<h2 data-id="heading-3">source map 是如何对应到源代码的？</h2>
<p>这是 source map 最核心的功能，也是最涉及知识盲区的一块内容。</p>
<p>大家应该还记得上文中没介绍的 <code>mapping</code> 字段吧，接下来我们就来详细了解这个字段的用处。</p>
<p>我们还是以刚才打包的文件为例，来看看产出的 source map 长啥样（去掉了无关紧要的）：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  sources:[<span class="hljs-string">"webpack://webpack-source-demo/./src/index.js"</span>],
  names: ['console', 'log'],
  mappings: 'AACAA,QAAQC,IADE',
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先 <code>mappings</code> 的内容其实是 Base64 VLQ 的编码表示。</p>
<p>内容由三部分组成，分别为：</p>
<ul>
<li>英文，表示源码及压缩代码的位置关联</li>
<li>逗号，分隔一行代码中的内容。比如说 <code>console.log(a)</code> 就由 <code>console</code> 、<code>log</code> 及 <code>a</code> 三部分组成，所以存在两个逗号。</li>
<li>分号，代表换行</li>
</ul>
<p>逗号和分号想必大家没啥疑问，但是对于这几个英文内容应该会很困惑。</p>
<p>其实这就是一种压缩数字内容的编码方式，毕竟源代码可能很庞大，用数字表示行数及列数的话 source map 文件将也会很庞大，因此选用 Base 64 来代表数字用以减少文件体积。</p>
<p>比如说 <code>A</code> 代表了数字 0，<code>C</code> 代表了数字 1 等等，有兴趣的读者可以通过<a href="https://www.murzwin.com/base64vlq.html" target="_blank" rel="nofollow noopener noreferrer">该网站</a>了解映射关系。</p>
<p>了解了这层编码的映射关系，我们再来聊聊这一串串英文到底代表了什么。</p>
<p>其实这每串英文中的字母都代表了一个位置：</p>
<ol>
<li>压缩代码的第几列</li>
<li>哪个源代码文件，毕竟可以多个文件打包成一个，对应 <code>sources</code> 字段</li>
<li>源代码第几行</li>
<li>源代码第几列</li>
<li><code>names</code> 字段里的索引</li>
</ol>
<p>这时读者可能有个疑惑，为啥没有压缩代码的第几行表示？这是因为压缩后的代码就一行，所以只需要表示第几列就行了。</p>
<p>了解完以上知识以后，我们就来根据上文的内容解析下 <code>AACAA</code> 的具体含义吧，通过<a href="https://www.murzwin.com/base64vlq.html" target="_blank" rel="nofollow noopener noreferrer">该网站</a>我们可以知道 <code>AACAA</code> 对应了 <code>[0,0,1,0,0]</code>，这里需要注意的是数字都从 0 开始，笔者表述的时候会自动加一，毕竟代码第零行听起来怪怪的。</p>
<ol>
<li>压缩代码的第一列</li>
<li>第一个源代码文件，也就是 <code>index.js</code> 文件了</li>
<li>源代码第二行了</li>
<li>源代码的第一列</li>
<li><code>names</code> 数组中的第一个索引，也就是 <code>console</code></li>
</ol>
<p>通过以上的解析，我们就能知道 <code>console</code> 在源代码及压缩文件中的具体位置了。</p>
<p>但是为什么 source map 会知道编译后的代码具体在什么位置呢？这里就要用到 AST 了。让我们打开<a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">网站</a>输入 <code>console.log(a)</code> 后观察右边的内容，你应该会发现如图所示的数据：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7f590b8c7b149369f0641fd12bb196d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210516214636867" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为 source map 是由 AST 产出的，所以我们能用上 AST 中的这个数据。</p>
<h2 data-id="heading-4">source map 的应用</h2>
<p>一般来说 source map 的应用都是在监控系统中，开发者构建完应用后，通过插件将源代码及 source map 上传至平台中。一旦客户端上报错误后，我们就可以通过<a href="https://github.com/mozilla/source-map" target="_blank" rel="nofollow noopener noreferrer">该库</a>来还原源代码的报错位置（具体 API 看文档即可），方便开发者快速定位线上问题。</p>
<h2 data-id="heading-5">最后</h2>
<p>source map 是我们日常中经常用到的东西，但是直到学习这块内容的时候才知道居然涉及到了那么多的知识盲区。</p>
<p>大家如果有什么疑问欢迎在评论区交流。</p>
<p><a href="https://github.com/KieSun/fucking-frontend" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33b5f724190f400f9bed5ddede4b0797~tplv-k3u1fbpfcp-watermark.image" width="350px" loading="lazy" referrerpolicy="no-referrer"></a></p></div>  
</div>
            