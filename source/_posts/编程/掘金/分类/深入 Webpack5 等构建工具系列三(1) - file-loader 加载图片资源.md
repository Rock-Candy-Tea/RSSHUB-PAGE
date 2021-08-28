
---
title: '深入 Webpack5 等构建工具系列三(1) - file-loader 加载图片资源'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6911546de5e74ba2853bd1c8d7593f59~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 02:33:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6911546de5e74ba2853bd1c8d7593f59~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前期准备</h2>
<p>接<a href="https://juejin.cn/post/7000519839378833416" target="_blank" title="https://juejin.cn/post/7000519839378833416">上篇文章</a>，做如下准备操作：</p>
<ol>
<li>删除 <code>02_webpack配置文件(css)</code> 目录下的 <code>node_modules</code> 和 <code>build</code> 文件夹；</li>
<li>在 <code>01_learn_webpack</code> 目录下拷贝一份 <code>02_webpack配置文件(css)</code>，并重命名为 <code>03_webpack处理其它资源</code>；</li>
<li>解决 <code>03_webpack处理其它资源/src/css/test.css</code> 文件中的警告问题，在 <code>:fullscreen</code> 中添加一些内容，如：<code>color: red;</code>；</li>
<li>打开 <code>VS Code</code> 的终端，切换目录到 <code>03_webpack处理其它资源</code> 下，运行 <code>npm install</code> 安装当前项目所需依赖，安装完成后，项目目录如下：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6911546de5e74ba2853bd1c8d7593f59~tplv-k3u1fbpfcp-watermark.image" alt="image-20210214201140227.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><code>file-loader</code> 加载图片资源</h2>
<p>我们知道，在真实的开发中，项目中会有 <code>js</code>、<code>css</code> 文件，另外，还会依赖很多其它的资源，比如说图片资源。下面，我们在项目的 <code>src</code> 目录下新建 <code>img</code> 目录，在 <code>img</code> 目录下添加以下两张图片（图片大小分别为 <code>36.74KB</code>、<code>287.60KB</code>）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca510b3da9274297b4b12bbe9eba952b~tplv-k3u1fbpfcp-watermark.image" alt="nhlt.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c45e92b44c4a15aaccb03e8817cd2f~tplv-k3u1fbpfcp-watermark.image" alt="zznh.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，我们希望在项目中使用这两张图片，通常情况下，有以下两种方式来使用图片：</p>
<ol>
<li>创建一个 <code>img</code> 元素，设置 <code>src</code> 属性；</li>
<li>创建一个 <code>div</code> 元素，设置背景图片；</li>
</ol>
<p>下面，我们在项目中同时使用上面两种方式来使用图片，来到 <code>./src/js/component.js</code> 文件下，新增以下红框圈出的内容：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a82c345d73240ddbcdba467de7355a5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215140736216.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个 img 元素，设置 src 属性</span>
<span class="hljs-comment">// const imgEl = document.createElement('img'); // 第一种创建 img 元素的方法</span>
<span class="hljs-keyword">const</span> imgEl = <span class="hljs-keyword">new</span> Image(); <span class="hljs-comment">// 第二种创建 img 元素的方法</span>
imgEl.src = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../img/zznh.png'</span>).default; <span class="hljs-comment">// 这里需要将图片当成资源设置到 src 里边，所以不能直接给一个地址，可以通过 require 的方式来加载资源</span>
element.appendChild(imgEl);

<span class="hljs-comment">// 创建一个 div 元素，设置背景图片</span>
<span class="hljs-keyword">const</span> bgDivEl = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
<span class="hljs-comment">// 添加宽高，以显示该 div</span>
bgDivEl.style.width = <span class="hljs-number">200</span> + <span class="hljs-string">'px'</span>;
bgDivEl.style.height = <span class="hljs-number">200</span> + <span class="hljs-string">'px'</span>;
<span class="hljs-comment">// 添加 class，以便后面通过 class 选择器找到该 div，然后设置背景图片</span>
bgDivEl.className = <span class="hljs-string">'bg-image'</span>;
<span class="hljs-comment">// 添加背景颜色，以显示该 div</span>
bgDivEl.style.backgroundColor = <span class="hljs-string">'red'</span>;
element.appendChild(bgDivEl);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，来到 <code>./src/css/index.css</code> 文件下，新增以下红框圈出的内容：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3efc972d68749b89c397ee72316335f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215120901750.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bg-image</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'../img/nhlt.jpg'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面，我们在终端运行 <code>npm run build</code> 命令进行打包，结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fe6bfa0c8fd427ab7782bf3ad468589~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215121246695.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们会发现，打包失败了，这是为甚莫呢？原因非常简单，我们之前讲过，在我们处理 <code>css</code> 文件时，默认情况下，<code>webpack</code> 不知道怎么处理，所以就会报错，同时它会告诉我们需要一个合适的 <code>loader</code> 来处理这个 <code>css</code> 文件。而现在，我们的项目中又引入了一些其它资源（<code>.jpg</code> 文件、<code>.png</code> 文件），那对于 <code>webpack</code> 来说，默认情况下它同样不知道这些资源该怎么处理。所以当我们准备加载 <code>.jpg/.png</code> 图片时，<code>webpack</code> 就会给出大意为“模块解析失败，你可能需要一个合适的 <code>loader</code> 来处理这种文件类型”的报错提示。</p>
<p>既然 <code>webpack</code> 默认情况下不知道怎么处理这些类型的图片文件，那我们就通过配置来告诉它该如何进行处理。这里，我们就需要用到 <code>file-loader</code> 了。</p>
<ul>
<li>
<p>要处理 <code>jpg</code>、<code>png</code> 等格式的图片，我们也需要有对应的 <code>loader</code>：<code>file-loader</code>；</p>
<ul>
<li><code>file-loader</code> 的作用就是帮助我们处理 <strong><code>import/require()</code> 方式</strong>引入的文件资源，并且会将它放到我们<strong>输出的文件夹</strong>中；</li>
<li>当然我们待会还会学习如何修改它的名字和所在文件夹；</li>
</ul>
</li>
</ul>
<p>要使用 <code>file-loader</code>，首先要安装它：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install file-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们去 <code>webpack</code> 的配置文件中编写相应的规则来使用 <code>file-loader</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff2ce5d8f3f0431b8cc4744a79a6d372~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215130311161.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: [
    &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者简写为：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: [
    <span class="hljs-string">'file-loader'</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为只有这一个 loader，所以还可以进一步简写为：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(png|jpe?g|gif|svg)$/</span>,
  use: <span class="hljs-string">'file-loader'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码块中的 <code>test</code> 属性对应的正则表达式中，<code>()</code> 表示分组，匹配小括号内的字符串，可以是一个，也可以是多个，常跟 <code>|</code>（或）符号搭配使用；<code>?</code> 表示前面的字符出现 <code>0</code> 次或 <code>1</code> 次。</p>
<p>完成上述配置后，我们再来运行 <code>npm run build</code> 命令看下效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7fba8e88a10484ba80658bdaabc8c80~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215130516071.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，除了 <code>3</code> 个警告（警告我们先不管），已经没有报错了。同时，我们会发现在 <code>webpack</code> 的输出目录（这里即 <code>build</code> 文件夹）下，除了 <code>bundle.js</code> 文件，还多了两个图片文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6ebc44ac35b47be9da361a9967e622f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215131840575.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这两张图片就是 <code>./src/img</code> 目录下的两张图片打包后生成的图片，并且，它们其实也已经在项目中被正常引入了。我们来到浏览器页面查看效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28708409e5684cdd97f7784a8f2ecbae~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215140850156.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见，已经成功引入了图片。为了让第二张图片能显示完整，我们对 <code>./src/css/index.css</code> 中的代码进行修改：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53f5f402247d485aba078cb63acd16a7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215141109783.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们添加了上图中红框圈出的两行代码，通过设置 <code>background-size: contain;</code> 使图片完整显示出来，而通过设置 <code>display: inline-block;</code> 使 <code>div</code> 的背景图片和前面的内容在同一行显示。</p>
<p>修改完后重新运行 <code>npm run build</code> 命令，再来查看效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4697d19b15f24410925db3c12421848f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215141722843.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，两张图片都能正常显示啦~</p>
<p>当然，除了通过 <code>require()</code> 的方式加载资源，我们还可以使用 <code>import</code> 的方式加载资源，比如我们可以修改 <code>./src/js/component.js</code> 文件中的内容如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be69c7c7937f4a258a6e555ee183571b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210215143341844.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重新打包后浏览器页面效果和之前是一样的。</p>
<p>以上，讲了 <code>file-loader</code> 的使用（使用 <code>file-loader</code> 加载图片文件），但是我们后面可能不再用它了，因为到了 <code>webpack5</code> 中，有了新的方式来替代它。</p>
<p>我们已经知道，通过 <code>file-loader</code> 可以去加载对应的图片资源，但是，它现在做的事情其实是非常简单的，只是把图片复制一份到打包的目录下，并做了下重命名，然后项目中最后引用的都是这些重命名后的图片文件。</p></div>  
</div>
            