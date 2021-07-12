
---
title: '尤大亲自评测 Vue3 和 Svelte(19个组件后Vue更好!)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed19f5034ea44c87b2a62222a056e50c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:01:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed19f5034ea44c87b2a62222a056e50c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">点击查看：后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p>近日尤大亲自创建了一个仓库用来对 Svelte 和 Vue3 组件进行了评测。这其实对我来说非常的感兴趣，因为我最近在业务项目中采用了 Svelte 进行了开发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed19f5034ea44c87b2a62222a056e50c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210711185119613" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么到底结果到底是如何呢？(期待的眼神，以为尤大要写 Svelte 代码来进行评测了。</p>
<p>Vue 大家都很熟悉了，如果你不知道 Svelte 是啥？可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FFCy903Rh6837MBDYLwYYIg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/FCy903Rh6837MBDYLwYYIg" ref="nofollow noopener noreferrer">后起之秀前端框架 Svelte 从入门到原理</a>。</p>
<p>大体介绍一下，Svelte 是一个  No Runtime —— 无运行时代码 的框架。</p>
<p>下面是<code>Jacek Schae</code>大神的统计，使用市面上主流的框架，来编写同样的 Realword 应用的体积：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0806e31681ca46248981b0895036617a~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>下面就请看详细的研究步骤，如果你对研究步骤不感兴趣，可以直接跳到最后看结论。</p>
<h2 data-id="heading-0">研究的步骤</h2>
<p>为了公平性，尤大选择了 <code>todomvc</code> 来进行构建比较，然后列举了一系列的步骤方案。</p>
<ol>
<li>
<p>这两个框架都实现了一个简单的符合规范、功能相同的<code> todomvc</code> 组件。</p>
<ul>
<li>Vue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyx990803%2Fvue-svelte-size-analysis%2Fblob%2Fmaster%2Ftodomvc.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyx990803/vue-svelte-size-analysis/blob/master/todomvc.vue" ref="nofollow noopener noreferrer">todomvc.vue</a> （使用了<code> <script setup></code> 语法）</li>
<li>Svelte: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyx990803%2Fvue-svelte-size-analysis%2Fblob%2Fmaster%2Ftodomvc.svelte" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyx990803/vue-svelte-size-analysis/blob/master/todomvc.svelte" ref="nofollow noopener noreferrer">todomvc.svelte</a> (基于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsveltejs%2Fsvelte-todomvc%2Fblob%2Fmaster%2Fsrc%2FTodoMVC.svelte" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sveltejs/svelte-todomvc/blob/master/src/TodoMVC.svelte" ref="nofollow noopener noreferrer">官方的实现</a>, 为了公平去除了 uuid 方法，害，失望了，原来尤大么有亲自写组件)</li>
</ul>
</li>
<li>
<p>组件使用各自框架的在线 SFC 编译器进行单独编译</p>
<ul>
<li>
<p>Vue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsfc.vuejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sfc.vuejs.org/" ref="nofollow noopener noreferrer">sfc.vuejs.org</a> @3.1.4 -> <code>todomvc.vue.js</code></p>
</li>
<li>
<p>Svelte: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Frepl" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/repl" ref="nofollow noopener noreferrer">svelte.dev/repl</a> @3.38.3 -> <code>todomvc.svelte.js</code></p>
</li>
</ul>
</li>
<li>
<p>编译文件使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftry.terser.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://try.terser.org/" ref="nofollow noopener noreferrer">Terser REPL</a> 压缩，然后删除 ES imports 和 exports。 这是因为在一个 <code>bundle</code> 的应用程序中，这些 <code>imports/exports</code>不需要或在多个组件之间共享。（可以理解为类似第三方代码，不会影响组件内部实现的大小）</p>
<ul>
<li>
<p>Vue: <code>todomvc.vue.min.js</code></p>
</li>
<li>
<p>Svelte: <code>todomvc.svelte.min.js</code></p>
</li>
</ul>
</li>
<li>
<p>然后把文件使用<code>gzip</code>和<code>brotli</code>（<strong>Brotli</strong>是一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25BC%2580%25E6%25BA%2590%25E8%25BD%25AF%25E4%25BB%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%BC%80%E6%BA%90%E8%BD%AF%E4%BB%B6" ref="nofollow noopener noreferrer">开源</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%2595%25B0%25E6%258D%25AE%25E5%258E%258B%25E7%25BC%25A9" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%8E%8B%E7%BC%A9" ref="nofollow noopener noreferrer">数据压缩</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%25A8%258B%25E5%25BA%258F%25E5%25BA%2593" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E7%A8%8B%E5%BA%8F%E5%BA%93" ref="nofollow noopener noreferrer">程序库</a>， 类似于 <code>gzip</code> ）压缩</p>
<ul>
<li>Vue: <code>todomvc.vue.min.js.gz</code> / <code>todomvc.vue.min.js.brotli</code></li>
<li>Svelte: <code>todomvc.svelte.min.js.gz</code> / <code>todomvc.svelte.min.js.brotli</code></li>
</ul>
</li>
<li>
<p>另外，在 SSR 的环境下，Svelte 需要在 "hydratable" 模式下编译其组件，这会引入额外的代码生成。 在编译 Svelte 的时候使用选项 <code>hydratable: true</code>  来开启 SSR 并重复 2-4 的步骤。</p>
<p>Vue在 SSR 环境下生成的代码是完全相同的，但是引入了一些额外的 <code>hydration-specific</code> 运行时代码(~0.89kb min + brotli).</p>
</li>
<li>
<p>对于每个框架，默认使用 <code> Vite</code> 来创建和打包构建（Svelte 使用 <code>hyderable: false</code>）。 每个应用程序同时设置SSR的模式再构建一次。</p>
</li>
</ol>
<p>默认 <code>Vite</code> 打包产生一个  vendor chunk（= 框架运行时代码）和一个 index chunk（= 组件代码）。</p>






















































<table><thead><tr><th></th><th>Vue</th><th>Vue (SSR)</th><th>Svelte</th><th>Svelte (SSR)</th></tr></thead><tbody><tr><td>Source</td><td>3.93kb</td><td>-</td><td>3.31kb</td><td>-</td></tr><tr><td>Compiled w/o imports (min)</td><td>2.73kb</td><td>-</td><td>5.01kb (183.52%)</td><td>6.59kb (241.39%)</td></tr><tr><td>Compiled w/o imports (min+gz)</td><td>1.25kb</td><td>-</td><td>2.13kb (170.40%)</td><td>2.68kb (214.40%)</td></tr><tr><td>Compiled w/o imports (min+brotli)</td><td>1.10kb</td><td>-</td><td>1.88kb (170.91%)</td><td>2.33kb (211.82%)</td></tr><tr><td>Vite component chunk (min+brotli)</td><td>1.13kb</td><td>-</td><td>1.95kb (172.26%)</td><td>2.41kb (213.27%)</td></tr><tr><td>Vite vendor chunk (min+brotli)</td><td>16.89kb</td><td>17.78kb</td><td>1.85kb</td><td>2.13kb</td></tr></tbody></table>
<blockquote>
<p>注意： w/o 的意思为 without ，"去除"的意思</p>
</blockquote>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1d3347375f41a59c4983d7eb8f38fb~tplv-k3u1fbpfcp-zoom-1.image" width="600px" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-1">分析</h2>
<p>在客户端模式下，从 Vite vendor chunk (min+brotli) 这一栏分析 。 Svelte App 导入1.85kb min+brotli 框架代码，比 Vue 轻15.04kb。这似乎看起来非常的强悍，但是这是因为框架运行时的差异。(Svelte 没有运行时，Vue有运行时)</p>
<p>再来看看组件代码，Svelte 的  min + compressed  输出大小是Vue的<del>1.7倍。在这种情况下，单个组件会导致0.78kb的大小差异。在 SSR 的情况下，这一比例进一步上升到</del>2.1倍，其中单个组分导致 1.23kb 大小的差异。</p>
<p><code>Todomvc</code> 非常具有代表性，代表大多数用户在应用场景中构建使用的组件。 我们可以合理地假设在现实场景中会发现类似的大小差异。 也就是说，在理论上，如果一个应用程序包含超过15.04 / 0.78〜= 19个 Todomvc 大小的组件，则 Svelte 应用程序将最终比Vue应用程序体积更大。</p>
<p>在 SSR 场景中，这个阈值会更低。 在 SSR 模式下，虽然框架差异为15.65KB，但是 Compnent Count 阈值下降到 15.65 / 1.23〜= 13！</p>
<p>显然在真实世界应用程序中，有许多其他因素：将从框架中导入更多功能，并将使用第三方库。 大小曲线将受到项目中纯组件代码的百分比的影响。 但是，保守估计 <code>应用 APP</code> 如果比 19个组件 这个阈值（或者在SSR模式下的13个 ）越大，Svelte 的体积优势就越少。</p>
<h2 data-id="heading-2">结论</h2>
<p>在仓库的<code>README</code>中尤大给出了两个结论，我就给它移到了最后。</p>
<ul>
<li>Svelte 单组件在普通模式下比 Vue3 单组件约大70% ，在 SSR 模式下大110% （公众号作者秋风注：其实这里尤大说的有点问题，这个70%指的是当前 <code>todomvc</code> 组件的大小对比，并不代表着所有 Svelte 组件 比 vue 3 组件 大 70%， 换句话说如果一个 100k 大小的 Vue 组件，Svelte组件可能就只有 101k，而不是170k !）</li>
<li>对于项目来说，当编写的组件大于19个组件（SSR模式为 13个组件）Svelte 的优势与 Vue3 相比就不存在了。</li>
</ul>
<h2 data-id="heading-3">总的来说</h2>
<p>本研究并的目的不是来说哪种框架更好 —— 它关注的是分析不同框架的策略对体积大小的影响。</p>
<p>从数据中可以看出，两个框架在 bundle 大小方面具有不同的优势 —— 取决于您的使用情况。 Svelte 仍然很棒，适用于一次性组件（例如，作为自定义元素包装），但它在大规模 APP 中在体积大小方面实际上是它的缺点，特别是SSR。</p>
<p>在更广泛的意义上，本研究旨在展示框架如何在<code>compile-time 编译时</code>和<code> runtime spectrum 运行时</code>找到一个平衡点：Vue 在源码上使用了一定的 <code>compile-time 编译时</code> 优化，但选择较重的 <code>compile-time </code> 返回较小的生成代码。 Svelte选择最小的运行时，但具有较重生成的代码的成本。 Svelte 可以进一步改进其代码生成来降低代码输出吗？ Vue可以进一步改善<code>tree-shaking</code>，使基线(运行时框架)变小吗？ 另外一点框架可以找到更好的平衡点吗？ 对以上所有的问题的答案回答可能是肯定的 —— 但现在我们需要明确的是"框架大小"是比单单比较 Hello World 应用程序的大小的更加细致的话题，这项研究就是为了证明这一点。</p>
<h2 data-id="heading-4">个人意见</h2>
<p>以下为公众号作者的个人意见，并非尤大调研中的观点。</p>
<p>其实尤大总体来说就是想要凸显出在框架的对比中，单单使用 <code>Jacek Schae</code>大神 统计的 那个 RealWord 应用程序来说是有些不公平的，应该需要更加细致的对比。其实对于 Svelte 这个包大小这个问题，其实很早之前在 Svelte  Github 中也对 React 和 Svelte 进行了广泛的讨论。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d47df9e3c80f468fa37e56cde32a2d84~tplv-k3u1fbpfcp-zoom-1.image" alt="Inflection Point" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Svelte 确实有一个阈值会使得它在一定程度后让体积大小没有了优势，但是在一般情况下，只要不是特别复杂的中后台管理应用，Svelte 应当会比其他框架体积小。</p>
<p>特别是在一些 H5 游戏中，如果你想要获得 React/Vue 数据驱动的方式编写应用，但是你又不想要引入他们这么大的运行时，确实来说是一个非常不错的方案。最近在开发一个基于 Three.js 的移动端网页，有一个初步的估计大约比使用 React 减少 30 - 50% 的体积，具体的数值因为还没迁移完无法给出完整的数据。还有一点，非运行时的框架，对于首屏的渲染也是有一个极大的帮助，你可以将首屏组件进行拆分，非运行时的首屏组件其实是非常小的，这对移动端来说非常的友好，因为毕竟使用 SSR 对应服务端还是有一定的压力要求的。</p>
<p>以上为个人看完尤大的分析比较后的一点愚见~ 如果不足之处请多多指出。</p>
<h2 data-id="heading-5">调研原文</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyx990803%2Fvue-svelte-size-analysis" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyx990803/vue-svelte-size-analysis" ref="nofollow noopener noreferrer">github.com/yyx990803/v…</a></p>
<p><strong>回看笔者往期高赞文章，也许能收获更多喔！</strong></p>
<ul>
<li>
<p><a href="https://juejin.cn/post/6969401491853410312" target="_blank" title="https://juejin.cn/post/6969401491853410312">又来了！10分钟实现微信 "炸屎"大作战</a> <code>500+</code>点赞量</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6930419481835470861" target="_blank" title="https://juejin.cn/post/6930419481835470861">2021前端学习路径书单—自我成长之路</a>：<code>570+</code>点赞量</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6926010284578603021" target="_blank" title="https://juejin.cn/post/6926010284578603021">教你实现微信8.0『炸裂』的🎉表情特效</a>：<code>400+</code>点赞量</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6900713052270755847" target="_blank" title="https://juejin.cn/post/6900713052270755847">从破解某设计网站谈前端水印(详细教程)</a>：<code>790+</code>点赞量</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6867469476196155400" target="_blank" title="https://juejin.cn/post/6867469476196155400">一文带你层层解锁「文件下载」的奥秘</a>：<code>140+</code>点赞量</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6844904126246027278" target="_blank" title="https://juejin.cn/post/6844904126246027278">10种跨域解决方案（附终极大招）</a>：<code>940+</code>点赞量</p>
</li>
</ul>
<h3 data-id="heading-6">结语</h3>
<p><strong>❤️关注+点赞+收藏+评论+转发❤️</strong>，原创不易，鼓励笔者创作更好的文章</p>
<p><strong>关注公众号<code>秋风的笔记</code>，一个专注于前端面试、工程化、开源的前端公众号</strong></p></div>  
</div>
            