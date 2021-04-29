
---
title: '回顾 babel 6和7，来预测下 babel 8'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db108c413baa4d4b9aff199538839015~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 07:10:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db108c413baa4d4b9aff199538839015~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>babel 最开始叫 6to5，顾名思义，功能是 es6 转 es5。我们知道，es 版本一年一个，有了 es7（es2016）、es8（es2017）等等。显然，6to5 的名字已经不合适了，所以 6to5 改名为了 babel。</p>
<p>babel 来自<a href="https://baike.baidu.com/item/%E5%B7%B4%E5%88%AB%E5%A1%94/67557?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">巴别塔</a>的典故：</p>
<blockquote>
<p>当时人类联合起来兴建希望能通往天堂的高塔，为了阻止人类的计划，上帝让人类说不同的语言，使人类相互之间不能沟通，计划因此失败，人类自此各散东西。此事件，为世上出现不同语言和种族提供解释。这座塔就是巴别塔。</p>
</blockquote>
<p>这个巴别塔的典故很符合 babel 的转译器的定位。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db108c413baa4d4b9aff199538839015~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">babel 的编译流程</h2>
<p>babel 从最初到现在一直的目的都很明确，就是把源码中的新语法和 api 转成目标浏览器支持的。它采用了微内核的架构，整个流程比较精简，所有的转换功能都是通过插件来完成的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7929fa847a469a8d1ec554b22ab68d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>babel 的编译流程就是 parse、transform、generate 3步， parse 是把源码转成 AST，transform 是对 AST 的转换，generate 是把 AST 转成目标代码，并且生成 sourcemap。</p>
<p>在 transform 阶段，会应用各种内置的插件来完成 AST 的转换。内置插件做的转换包括两部分，一是把不支持的语法转成目标环境支持的语法来实现相同功能，二是不支持的 api 自动引入对应的 polyfill。</p>
<p>babel 的编译流程和目的从没有变过，但是完成这个目的的方式却变化很大，我们来回顾一下 <code>babel 6</code>，<code>babel 7</code>
都是怎么设计的，<code>babel 8</code> 又会怎么做，或许能帮你真正理解 babel。</p>
<h2 data-id="heading-1">babel 6</h2>
<p>es 的标准一年一个版本，也就意味着 babel 插件要实时的去跟进，一年实现一系列插件。</p>
<p>新的语法和 api 进入 es 标准也是有个过程的，这个过程分为这几个阶段：</p>
<ul>
<li>阶段 0 - Strawman: 只是一个想法，可能用 babel plugin 实现</li>
<li>阶段 1 - Proposal: 值得继续的建议</li>
<li>阶段 2 - Draft: 建立 spec</li>
<li>阶段 3 - Candidate: 完成 spec 并且在浏览器实现</li>
<li>阶段 4 - Finished: 会加入到下一年的 es20xx spec</li>
</ul>
<p>有这么多特性要 babel 去转换，每个特性用一个 babel 插件来做。但是特性多啊，也就是说插件多，总不能让用户自己去配一个个插件吧，所以 babel 6 引入了 preset 的概念，就是 plugin 的集合。</p>
<p>如果我们想用 es6 语法就用 babel-preset-es2015，es7 就在引入 babel-preset-es2016 等等。如果是想用还没加入标准的特性，则分别用 babel-preset-stage0、babel-preset-stage1 等来引入。这样通过选择不同的 preset，加上手动引入一些插件，就是所有 babel 会做的转换。</p>
<p>可以把这个过程理解为集合求并集的过程。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c165ed6cc58c4256a81ecc36730e96ad~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>并集的结果就是所有支持的特性。</p>
<p>babel 6 就是通过这样的方式来支持各种目标环境不支持的特性转换的配置。</p>
<p><strong>细想一下，这样的方式有没有问题？</strong></p>
<p>这样虽然能达到目的，但是是有问题的，主要有两点：</p>
<ul>
<li>
<p>es 的标准每年都在变，现在的 stage-0 可能很快就 stage-2 了，那 preset 怎么维护，要不要跟着变，用户怎么知道这个 stage-x 都支持什么特性？</p>
</li>
<li>
<p>只能转成 es5，那目标环境支持一些 es6 特性了，那这些转换和 polyfill 岂不是无用功？ 而且还增加了产物的体积。</p>
</li>
<li>
<p>polyfill 手动引入，比较麻烦，有没有更好的方式</p>
</li>
</ul>
<p>这两个问题是 babel 6 的时候一直存在的。所以这种方案算是及格，但是还是有问题的，我们给 70 分不过分吧。
（能完成功能就可以给 60 分，多加 10 分是给 babel 6 引入的 preset，确实简化了很多配置）</p>
<p>那怎么解决 babel 6 的问题呢？babel 7 给出了答案。</p>
<h2 data-id="heading-2">babel 7</h2>
<p>babel 7 改动挺大的，比如所有的包都迁移到了 @babel 的 scope 下，也就是 @babel/xxx，这些我们不管，只看 babel 7 是怎么解决 babel 6 的问题的，</p>
<p>babel 7 废弃了 preset-20xx 和 preset-stage-x 的 preset 包，而换成了 preset-env，preset-env 默认会支持所有 es 标准的特性，如果没进入标准的，不再封装成 preset，需要手动指定 plugin-proposal-xxx。</p>
<p>它的集合是这样的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b69661e6ac64ddfb6a44f6708d2b71f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是比起 babel 6 更简单了。</p>
<p>（preset-react 等不是 es 标准语法，也没有啥变化，就不包括在里面了）。</p>
<p>但是 preset 和 plugin proposal 的改变只是解决了之前的 preset 经常变的问题。那么多转换了一些环境支持的特性，这个问题是怎么解决的呢？</p>
<p>答案是 compat-table，它给出了每个特性在不同浏览器或者 node 环境中的最低支持版本，babel 基于这个自己维护了一份数据库，在 <a href="https://github.com/babel/babel/blob/main/packages/babel-compat-data/data/plugins.json" target="_blank" rel="nofollow noopener noreferrer">@babel/compat-data</a> 下。</p>
<p>其中有每个特性在不同环境的什么版本支持的数据：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86651896f9f34194b567ab74e7e5c35d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了这些数据，那么只要用户指定他的目标环境是啥就可以了，这时候可以用 browserslist 的 query 来写，比如 last 1 version, > 1% 这种字符串，babel 会使用 brwoserslist 来把它们转成目标环境具体版本的数据。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a318db95f7cb4f139981f2f453bdc39e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了不同特性支持的环境的最低版本的数据，有了具体的版本，那么过滤出来的就是目标环境不支持的特性，然后引入它们对应的插件即可。这就是 preset-env 做的事情。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ccb1144f8924fb99cc6073859289124~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置方式比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"@babel/preset-env"</span>, &#123; <span class="hljs-string">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span> &#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就通过 preset-env 解决了转换了目标环境已经支持的特性的问题。其实 polyfill 也可以通过 targets 来过滤。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d8df3916feb4da7b445e8771e779353~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不再手动引入 polyfill，那么怎么引入？ 当然是用 preset-env 自动引入了。但是也不是默认就会启用这个功能，需要配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"@babel/preset-env"</span>, &#123; 
        <span class="hljs-string">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span>,
        <span class="hljs-string">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>,<span class="hljs-comment">// or "entry" or "false"</span>
        <span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>
    &#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置下 corejs 和 useBuiltIns。</p>
<ul>
<li>
<p>corejs 就是 babel 7 所用的 polyfill，需要指定下版本，corejs 3 才支持实例方法（比如 Array.prototype.fill ）的 polyfill。</p>
</li>
<li>
<p>useBuiltIns 就是使用 polyfill （corejs）的方式，是在入口处全部引入（entry），还是每个文件引入用到的（usage），或者不引入（false）。</p>
</li>
</ul>
<p>配置了这两个 option 就可以自动引入 polyfill 了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea48ded51f04512bac80b8e4db809cb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>polyfill 默认是全局引入的，有的时候不想污染全局变量就要用 @babel/plugin-transform-runtime 转换下。（这个插件 babel 6 就有了）。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64df84f32f6945c19bac48cc7185dee7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就不再污染全局环境了，而是使用一个唯一的标识符来引入。</p>
<p>看起来，babel 7 好像已经很完美了，可以打 90 多分了？</p>
<p>不是的，babel 7 有 babel 7 的问题。</p>
<p><strong>babel 7 的问题</strong></p>
<p>@babel/plugin-transform-runtime 是不支持配置 targets 的，因为不知道目标环境支持啥，它只能全部做转换。你可能说不是有 preset-env 么？</p>
<p>babel 中插件的应用顺序是：先 plugin 再 preset，plugin 从左到右，preset 从右到左，这样 plugin-transform-runtime 是在 preset-env 前面的。</p>
<p>等 @babel/plugin-transform-runtime 转完了之后，再交给 preset-env 这时候已经做了无用的转换了。</p>
<p>我们来试验一下：</p>
<p>我们先看一下 Array.prototype.fill 的环境支持情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cae7d0873384728a404963eff4861c4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到在 Chrome 45 及以上支持这个特性，而在 Chrome 44 就不支持了。</p>
<p>我们先单独试一下 preset-env：</p>
<p>当指定 targets 为 Chrome 44 时，应该自动引入polyfill：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d43b57304a4d2f9f64af086f5d6098~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当指定 targets 为 Chrome 45 时，不需要引入polyfill：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f68b5ad95f644518c8419c1847f7765~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果都符合预期，44 引入，45 不引入。</p>
<p>我们再来试试 @babel/plugin-transform-runtime：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9677f1aaba654728aec933b31e632fe0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是发现问题了，Chrome 45 不是支持 Array.prototype.fill 方法么，为啥还是引入了 polyfill。</p>
<p>于是我就去问了下作者，提了个 <a href="https://github.com/babel/babel/issues/13226" target="_blank" rel="nofollow noopener noreferrer">feature request</a>，作者说可以用最新的 @babel/polyfills 解决了这个问题.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd7e3023e674eeb83da0a0608fda08e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我去看了下，这个包还在试验阶段，确实解决了这个问题。</p>
<p>这个包估计在 babel 8 会内置到 babel。</p>
<p>那么给 babel 7 打个分吧，本来 preset-env 的引入使我们能更精准的转换代码和引入 polyfill，想给 90 分，但是 plugin-transform-runtime 的问题让我给它减了 10 分，综合给 80 分吧。</p>
<h2 data-id="heading-3">babel 8</h2>
<p>babel 8 还没出来，但是我们知道 babel 再怎么更新也是围绕主线来的，也就是对目标环境不支持的特性自动进行精准的转换和 polyfill。每个版本都是解决了上个版本的问题的，babel 8 的 @babel/polyfills 包就解决了 babel 7 的 @babel/plugin-transform-runtime 的遗留问题，可以通过 targets 来按需精准引入 polyfill 了。</p>
<p>它支持配置一个 polyfill provider，也就是说你可以指定 corejs2、corejs3、es-shims 等 polyfill，还可以自定义 polyfil，也就是你可以使用自己的 polyfill。</p>
<p>然后有了 polyfill 源之后，使用 polyfill 的方式也把之前 transform-runtime 做的事情内置了，也就是从之前的 useBuiltIns: entry、 useBuiltIns: usage 的两种，变成了 3 种：</p>
<ul>
<li>entry-global: 这个和之前的 useBuiltIns: entry 对标，就是全局引入 polyfill。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202c38690dfe455b8c033d6e54ede9b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>usage-entry: 这个和 useBuiltIns: usage 对标，就是具体模块引入用到的 polyfill。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21d206affa374e53a786592e6a0cfa6e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>usage-pure：这个就是之前需要 transform-runtime 插件做的事情，使用不污染全局变量的 pure 的方式引入具体模块用到的 polyfill.</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51c65f9672d34c04814142bf04ccc8b9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实这三种方式 babel 7 也支持，但是现在不再需要插件了，而且还支持了 polyfill provider 的配置，所以到了 babel 8 的阶段， @babel/preset-env 才是功能完备的。</p>
<p><strong>那么插件如果想用 targets 该怎么用呢？</strong></p>
<p>因为我最近在写 《babel 插件通关秘籍》 的小册，所以比较关注对插件的影响，我就问了一下 babel 维护者是不是需要在 @babel/core 调用插件的时候注入到 api 中，让插件可以拿到 targets。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6049cc21d344aa09497c95778e4aae9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上午问的，下午我就惊喜的发现 babel 文档补充了 @babel/helper-compilation-targets 的文档。helper 是用于插件之间复用代码的方式，也就是给插件开发用的库。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/943ef82a40464dd69a7f4b1899172e53~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我看了下，这个库提供了 3 个 api：</p>
<ul>
<li>根据 query 查询目标环境版本： getTargets</li>
<li>过滤目标环境: filterItems</li>
<li>判断某个插件是否需要：isRequired</li>
</ul>
<p>分别对应我们前面聊到的需要 先<strong>通过 query 确定目标环境</strong>，然后<strong>对目标环境做过滤</strong>，之后<strong>判断某个插件是否需要</strong>的 3个阶段。</p>
<p>插件里面通过 api.targets() 拿到环境的配置，然后通过 isRequired 来确定某个插件有没有必要用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d52e7a8de9348de81eeff3827d4e53b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，不管是内置 plugin 和 preset 的实现方式也好，还是插件所能用的 api 也好，都完美支持了 targets，到了这个阶段 targets 才算真正融入进了 babel 中。</p>
<p>这个阶段的 babel，我觉得已经可以给出 90 分的分数了：</p>
<p>支持按照配置的目标环境按需进行 polyfill 和 transform，支持 polyfill 的切换和自定义，配置方式也足够简单，插件中也可以用 targets，而且提供了方便的 helper 包。</p>
<h2 data-id="heading-4">babel 发展规律</h2>
<p>babel 8 还在路上，但是我们已经能够隐约看到他会是什么样子了，其实 babel 从最开始到现在，核心的思路始终没有变过，就像最开始的名字 6to5 一样，就是为了 <strong>把目标环境中不支持的语法和 api 进行转换或 polyfill，尽量的准确、配置尽量的简单、插件更容易书写能做到更多事情</strong>。</p>
<p>所以针对这个目标，babel 一路发展而来， 设计出了 preset（babel 6）、preset-env (babel 7)、polyfill provider（babel 8），plugin-transform-runtime （babel 6）等。</p>
<p>插件能够用的 api、helper 等也越来越丰富。</p>
<p>babel 一直在发展，但是目标和本质从未变过。我们去学习一个东西，也要去抓住它的本质来学，所以我写了《babel 插件通关秘籍》 的小册（即将上线），希望能帮你“通关” babel！</p></div>  
</div>
            