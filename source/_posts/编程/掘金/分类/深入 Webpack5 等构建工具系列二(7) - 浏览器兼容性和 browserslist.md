
---
title: '深入 Webpack5 等构建工具系列二(7) - 浏览器兼容性和 browserslist'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d841c9d99c5f47b2b57d96b851d40d61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 18:22:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d841c9d99c5f47b2b57d96b851d40d61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>为了引出一个叫 <code>postcss-loader</code> 的 <code>loader</code>，下面我们先来讲一些必要的前端知识。</p>
<h2 data-id="heading-0">1. 浏览器的兼容性</h2>
<ul>
<li>
<p>我们来思考一个问题：开发中，浏览器的兼容问题，我们应该如何去解决和处理？</p>
<ul>
<li>当然这个问题很笼统，这里我说的兼容性问题<strong>不是指屏幕大小的变化适配</strong>；</li>
<li>这里的兼容性指的是<strong>针对不同的浏览器（不同的版本）支持的特性</strong>：比如 <code>css</code> 特性、<code>js</code> 语法之间的兼容性，就是有的浏览器支持而有的浏览器不支持的问题；</li>
</ul>
</li>
<li>
<p>我们知道市面上有大量的浏览器：</p>
<ul>
<li>有 <code>Chorme</code>、<code>Safari</code>、<code>IE</code>、<code>Edge</code>、<code>Chrome for Android</code>、<code>UC Browser</code>、<code>QQ Browser</code> 等等；</li>
<li>它们的<strong>市场占有率是多少</strong>？我们<strong>要不要兼容它们</strong>呢？</li>
</ul>
</li>
<li>
<p>其实在很多的脚手架配置中，都能看到类似于这样的配置信息：</p>
</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">></span><span class="bash"> 1%</span>
last 2 versions
not dead
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何解决这种兼容性问题呢？</p>
<p>事实上，受益于前端工程化的发展，现在处理这个问题已经很简单了，因为现在已经有各种工具帮助我们处理各种特性了。举个例子，<code>css</code> 里面有一个属性叫做 <code>user-select</code>，这个属性不一定所有浏览器都支持，那么为了让所有浏览器都支持，我们可能会给它加上前缀（甚至使用 <code>css</code> 的 <code>polyfill</code> 来做特殊处理），那前缀需要手动加吗？当然不需要，因为已经有一些工具能帮助我们自动添加浏览器前缀了，比如 <code>autoprefixer</code>。但是，是否有必要添加浏览器前缀也要看具体情况，比如某个特性如果只需要适配部分浏览器，而这些浏览器都是支持这个特性的，那就没必要添加前缀，不然还让代码变多了，用户下载到的包也会变大。因此，在做适配的时候到底需不需要使用 <code>autoprefixer</code> 这个工具来添加前缀其实是不一定的。类似的，一些 <code>js</code> 特性要不要转换，要不要使用 <code>babel</code> 来做转化也是不一定的，它<strong>取决于我们到底要适配哪些浏览器</strong>。如果要适配的浏览器需要加前缀那就加，不需要加前缀那就不加。</p>
<p>所以呢，在决定要不要对目标浏览器进行适配之前，我们得先确定个东西，即<strong>项目到底支持哪些浏览器</strong>。你可能会想，把要支持的浏览器一一列举出来。但这样列举肯定不太好，因为浏览器有很多，各个浏览器的版本也有很多。那我们该怎么做呢？怎么样告诉它当前项目支持哪些浏览器呢？</p>
<p>或许你之前在很多脚手架中（比如 <code>vue3</code> 的 <code>.browserslistrc</code> 文件、<code>react</code> 的 <code>package.json</code> 文件中的 "<code>browserslist</code>" 一项）见过类似这样的配置：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">></span><span class="bash"> 1%</span>
last 2 versions
not dead
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些配置其实就是一个个的条件，用来提供给工具（<code>autoprefixer</code>、<code>babel</code> 等）使用，告诉这些工具我现在到底要适配哪些浏览器。</p>
<p>比如上面配置中的 <code>> 1%</code> 就表示适配市场占有率大于 <code>1%</code> 的浏览器，对于 <code>autoprefixer</code> 来说，在这些浏览器中，如果有需要加浏览器前缀的那就加上，如果都不需要加前缀那就都不加；对于 <code>babel</code> 来说，这这些浏览器中，如果支持某个特性那就不需要做转化，如果不支持某个特性那就需要做转化（或者通过 <code>polyfill</code> 的方式增加上一些特性）。</p>
<p>那么问题来了，浏览器的市场占有率等数据从哪里获取呢？那肯定要有一个比较权威、比较专业的地方来对浏览器的信息做统计呀。</p>
<h2 data-id="heading-1">2. 浏览器的市场占有率</h2>
<ul>
<li>在哪里可以查询到浏览器的市场占有率呢？
<ul>
<li>这个最好用的、最权威的网站，也是我们工具通常会查询的一个网站就是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/" ref="nofollow noopener noreferrer">caniuse</a>；</li>
<li>查询地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2Fusage-table" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/usage-table" ref="nofollow noopener noreferrer">caniuse.com/usage-table</a></li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d841c9d99c5f47b2b57d96b851d40d61~tplv-k3u1fbpfcp-watermark.image" alt="image-20210128212110857.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3. 认识 <code>browserslist</code> 工具</h2>
<p>要知道，从上面这个网站上查询到的浏览器的市场占有率等浏览器信息最后会提供给项目中的很多工具（比如 <code>autoprefixer</code>、<code>babel</code>、<code>postcss-preset-env</code> 等等）进行使用。因此，我们最好有另外一个工具专门用来共享这些浏览器数据，这个工具就是 <code>browserslist</code> 哈。<code>browserslist</code> 工具负责帮助我们查询当前条件匹配到的浏览器的信息，并把查询到的结果共享给所有的工具。</p>
<ul>
<li>我们如何可以在 <code>css</code> 兼容性和 <code>js</code> 兼容性下共享我们配置的兼容性条件呢？
<ul>
<li>就是当我们<strong>设置了一个条件：<code>> 1%</code></strong>；</li>
<li>我们表达的意思是 <strong><code>css</code> 要兼容市场占有率大于 <code>1%</code> 的浏览器，<code>js</code> 也要兼容市场占有率大于 <code>1%</code> 的浏览器</strong>；</li>
<li>如果我们是<strong>通过工具来达到这种兼容性</strong>的，比如<strong>后面我们会讲到的 <code>postcss-preset-env</code>、<code>babel</code>、<code>autoprefixer</code> 等</strong></li>
</ul>
</li>
<li>如何可以让它们共享我们的配置呢？
<ul>
<li>答案就是 <strong>Browserslist</strong>；</li>
</ul>
</li>
<li><code>Browserslist</code> 是什么？<code>Browserslist</code> 是一个<strong>在不同的前端工具（举例如下）之间</strong>，共享<strong>目标浏览器和 <code>Node.js</code> 版本的配置</strong>；
<ul>
<li><code>Autoprefixer</code></li>
<li><code>Babel</code></li>
<li><code>postcss-preset-env</code></li>
<li><code>eslint-plugin-compat</code></li>
<li><code>stylelint-no-unsupported-browser-features</code></li>
<li><code>postcss-normalize</code></li>
<li><code>obsolete-webpack-plugin</code></li>
</ul>
</li>
</ul>
<p>上面的 <code>7</code> 个工具都需要通过 <code>Browserslist</code> 查询到的目标浏览器决定最后到底要转换成什么样的结果。</p>
<p>因此，<code>Browserslist</code> 这个工具对于我们工程化的项目非常重要，这也是为什么 <code>vue</code>、<code>react</code> 项目中都有这个东西的原因。而现在我们讲 <code>webpack</code>，也必须讲这个东西。</p>
<h2 data-id="heading-3">4. 浏览器查询过程</h2>
<ul>
<li>我们可以编写类似于这样的配置：</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">></span><span class="bash"> 1%</span>
last 2 versions
not dead
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>那么之后，这些工具会根据我们的配置来获取相关的浏览器信息，以方便决定是否需要进行兼容性的支持：</p>
<ul>
<li>条件查询使用的是 <code>caniuse-lite</code> 工具，这个工具的数据来自于 <code>caniuse</code> 的网站上；</li>
</ul>
</li>
</ul>
<p>编写完规则后，<code>browserslist</code> 这个工具是从哪里帮助我们进行查询呢？答案是 <code>caniuse</code> 网站，但是在 <code>caniuse</code> 网站上查询时，并不是说 <code>browserslist</code> 这个工具里面有发送网络请求到 <code>caniuse</code> 网站进行查询。事实上，<code>caniuse</code> 里面提供了一个叫做 <code>caniuse-lite</code> 的工具，<code>browserslist</code> 是通过这个工具来进行查询的。比如在 <code>vue3</code> 脚手架中的 <code>node_modules/browserslist/index.js</code> 文件的开头部分你就能看到它 <code>require</code> 了 <code>caniuse-lite</code>，最终就是通过 <code>caniuse-lite</code> 这个小工具使用我们传入的条件帮助我们查询匹配的浏览器的。</p>
<p>下面，我们就来演示一下 <code>browserslist</code> 这个工具的使用。那要想使用 <code>browserslist</code>，首先得安装它的包呀，不过我们可以先去看下在安装 <code>webpack</code> 的一些其它东西时有没有安装了 <code>browserslist</code>，我们可以发现已经安装过了。所以我们这里就不需要重新安装了。另外，在 <code>node_modules/.bin</code> 里面也应该是有 <code>browserslist</code> 的可执行文件的。所以，下面我们可以这样来做：在终端中运行如下命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx browserslist "> 1%, last 2 versions, not dead"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是在 <code>MacOS</code> 上运行上述命令，应该能直接在终端中看到一个浏览器信息列表，这些浏览器就是和命令中输入的条件匹配的所有浏览器。那意味着之后我们再做诸如 <code>css</code> 特性、<code>js</code> 特性的适配时，针对的就是这些浏览器。但在 <code>Windows</code> 系统上运行上述命令目前不会在终端输出任何信息（之前是可以的），而是会在当前目录下生成一个名为 <code>1%</code> 的文件，里面的内容也和 <code>MacOS</code> 上显示的不一样，可能是 <code>browserslist</code> 升级之后的问题，但没有关系，对此我们不用纠结（因为我们运行上述命令的目的只是为了演示一下这个 <code>browserslist</code> 工具确实能帮助我们查询到浏览器），我们也可以在项目目录下新建 <code>.browserslistrc</code> 文件，在里面把查询条件写好，然后直接在项目目录下执行 <code>npx browserslist</code>，就会自动去读取配置文件（<code>.browserslistrc</code> 或 <code>package.json</code>）中的查询条件，并输出结果了，修改 <code>.browserslistrc</code> 文件中的查询条件，再次执行 <code>npx browserslist</code>，会看到不同的结果。</p>
<p>但真实开发时，我们不会在命令行中使用 <code>browserslist</code>，而是会对 <code>browserslist</code> 做一个配置，配置完后用来做共享（项目中某个地方要用到时，就自动去读这个配置文件，然后根据配置去查询出对应的浏览器）。那这个配置文件如何编写呢？我们后面再讲。这里再讲一个东西，即关于上述命令中各个条件之间的关系（交集、并集、非）。</p>
<ul>
<li>如果没有配置，那么也会有一个默认配置：</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c96fc16fe80f456190045fd98997c04a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131112934650.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们编写了多个条件之后，多个条件之间是什么关系呢？</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b421235f432141f4a3718521c3ef4d00~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131113114467.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，下面我们就来讲如果想要在多个工具里面共享 <code>browserslist</code> 配置中的条件的话，这些条件应该如何编写。一共有两种编写方式（选择其中一个即可，建议不要同时使用，否则可能会报错（<code>browserslist: xxx contains both .browserslistrc and package.json with browsers</code>））：</p>
<ol>
<li>在 <code>package.json</code> 文件中添加 <code>"browserslist"</code> 字段，对应一个数组，数组中编写一个个条件；</li>
<li>新建 <code>.browserslistrc</code> 文件，在该文件中编写条件；</li>
</ol>
<blockquote>
<p>注：<code>.browserslistrc</code> 中的 <code>rc</code> 应该是指 <code>runtime compiler</code>，表示其它工具在运行时编译的时候，会读取这个文件。</p>
</blockquote>
<h3 data-id="heading-4">4.1 <code>browserslist</code> 配置编写方式 1 示例：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4f35f55b6ea44ffbbd66848f8146120~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131134100922.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编写完上图所示的配置之后，再在项目中使用诸如 <code>babel</code>、<code>autoprefixer</code> 等工具时，就会自动来到这个 <code>browserslist</code> 对应的数组中查询这些条件，然后根据 <code>caniuse-lite</code> 这个小工具去 <code>caniuse</code> 网站上查询出来到底要适配哪些浏览器。</p>
<p>上图中的条件之间是并集的关系，如果要取交集，可以这样编写：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce99c3a0f4ec4836a5b1299ec4dcffeb~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131142649089.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在两种编写格式下分别运行 <code>npx browserslist</code> 命令，可以看到不同的输出结果：</p>
<p>取并集的写法的输出结果：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf366b5361c74fe3ba14fd0ace5b488b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131142926946.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>取交集的写法的输出结果：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f2b1e2d6404605ac0540aa523cd714~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131143028305.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">4.2 <code>browserslist</code> 配置编写方式 2 示例：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0f420c7a3a46549964d7e773d70eb9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131144210400.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在项目目录下新建 <code>.browserslistrc</code> 文件，在其中直接输入条件，换行就表示取并集。如果要取交集，可以这样编写：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd17c1e9ee847e18eedd7246e687c46~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131144635135.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在两种编写格式下分别运行 <code>npx browserslist</code> 命令，可以看到不同的输出结果：</p>
<p>取并集的写法的输出结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1f1145888904faf9496c39cff623443~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131144500978.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>取交集的写法的输出结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e27aae1db897410586a5af7c659657bf~tplv-k3u1fbpfcp-watermark.image" alt="image-20210131144742003.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，如果两种方式都没有使用，则会采用默认配置 <code>> 0.5%, last 2 versions, Firefox ESR, not dead</code>，前面已经说过。</p>
<p>以上，就是关于 <code>browserslist</code> 编写方式的简述。到此为止，相信大家对浏览器适配在工程化中到底怎么做、 <code>.browserslistrc</code> 到底什么样的作用以及 <code>caniuse</code> 网站在整个环节中起到什么样的作用应该有了比较清楚的认识。</p>
<p>这里再提一个东西，可能你以前在创建 <code>vue</code> 项目的时候（比如 <code>vue create</code>），在其中一个步骤中会遇到一个问题，它会问你想要把配置信息写到 <code>package.json</code> 文件里面还是写到单独的一个配置文件里面，其实这就跟这里的 <code>browserslist</code> 的两种配置方式类似了，即一种方式是写到 <code>package.json</code> 文件中，一种方式是写到一个单独的文件中。</p>
<h2 data-id="heading-6">5. <code>Browserslist</code> 的编写规则</h2>
<p>那么在开发中，我们<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbrowserslist%2Fbrowserslist%23full-list" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/browserslist/browserslist#full-list" ref="nofollow noopener noreferrer">可以编写的条件</a>都有哪些呢？（加粗部分是最常用的）</p>
<ul>
<li><strong><code>defaults</code>：Browserslist 的默认浏览器（<code>> 0.5%, last 2 versions, Firefox ESR, not dead</code>）</strong>；</li>
<li><strong><code>> 5%</code>：通过全局使用情况统计信息选择的浏览器版本（也可以使用 <code>>=</code>， <code><</code> 和 <code><=</code>）</strong>；
<ul>
<li><code>5% in US</code>：使用美国使用情况统计信息。它接受两个字母的国家/地区代码；</li>
<li><code>> 5% in alt-AS</code>：使用亚洲地区使用情况统计信息。有关所有区域代码的列表，请参见 <code>caniuse-lite/data/regions</code></li>
<li><code>> 5% in my stats</code>：使用自定义用法数据；</li>
<li><code>> 5% in browserslist-config-mycompany stats</code>：使用来自 <code>browserslist-config-mycompany/browserslist-stats.json</code> 的自定义用法数据；</li>
<li><code>cover 99.5%</code>：提供覆盖率的最受欢迎的浏览器；</li>
<li><code>cover 99.5% in US</code>：与上述相同，但国家/地区代码由两个字母组成；</li>
<li><code>cover 99.5% in my stats</code>：使用自定义用法数据；</li>
</ul>
</li>
<li><strong><code>dead</code>：24 个月内没有官方支持或更新的浏览器。现在是 <code>IE 10</code>, <code>IE_Mob 11</code>, <code>BlackBerry 10</code>, <code>BlackBerry 7</code>, <code>Samsung 4</code> 和 <code>OperaMobile 12.1</code></strong>；</li>
<li><strong><code>last 2 versions</code>：每个浏览器的最后 2 个版本。</strong>
<ul>
<li><code>last 2 Chrome versions</code>：最近 2 个版本的 Chrome 浏览器。</li>
<li><code>last 2 major versions</code> 或 <code>last 2 iOS major versions</code>：最近 2 个主要版本的所有次要/补丁版本。</li>
</ul>
</li>
<li><code>node 10</code> and <code>node 10.4</code>：选择最新的 Node.js <code>10.x.x</code> 或 <code>10.4.x</code> 版本。
<ul>
<li><code>current node</code>：Browserslist 现在使用的 Node.js 版本。</li>
<li><code>maintained node versions</code>：所有还在被 Node.js 基金会维护的 Node.js 版本。</li>
</ul>
</li>
<li><code>iOS 7</code>：直接使用 iOS 浏览器版本 7。
<ul>
<li><code>Firefox > 20</code>：Firefox 的版本高于 20 的。也可以使用 <code>>=</code>、<code><</code> 和 <code><=</code>。它也可以和 Node.js 一起使用。</li>
<li><code>ie 6-8</code>：选择一个版本的包含范围。</li>
<li><code>Firefox ESR</code>：最新的 [Firefox ESR] 版本。</li>
<li><code>PhantomJS 2.1</code> and <code>PhantomJS 1.9</code>：选择类似于 PhantomJS 运行时的  Safari 版本。</li>
</ul>
</li>
<li><code>extends browserslist-config-mycompany</code>：从 <code>browserslist-config-mycompany</code> npm 包中查询。</li>
<li><code>supports es6-module</code>：支持特定功能的浏览器。这里的 <code>es6-module</code> 是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/" ref="nofollow noopener noreferrer">Can I Use</a> 页面 URL 的 <code>feat</code> 参数。所有可用功能的列表可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fben-eb%2Fcaniuse-lite%2Ftree%2Fmaster%2Fdata%2Ffeatures" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ben-eb/caniuse-lite/tree/master/data/features" ref="nofollow noopener noreferrer"><code>caniuse-lite/data/features</code></a> 找到。</li>
<li><code>browserslist config</code>：在 Browserslist 配置中定义的浏览器。在差异服务中很有用，可用于修改用户的配置，例如 <code>browserslist config and supports es6-module</code>。</li>
<li><code>since 2015</code> 或 <code>last 2 years</code>：自 2015 年以来发布的所有版本（从 <code>2015-03</code> 以及从 <code>2015-03-10</code> 开始）。</li>
<li><code>unreleased versions</code> 或 <code>unreleased Chrome versions</code>：alpha 和 beta 版本。</li>
<li><strong><code>not ie <= 8</code>：排除先前查询选择的浏览器（这里表示 ie 版本 <= 8 的就不适配了）。</strong></li>
</ul></div>  
</div>
            