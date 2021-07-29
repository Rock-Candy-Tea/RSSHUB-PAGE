
---
title: '用 Vite 加速你的生产力'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08a45b62c6c64f548b645c8a89af044e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 21:53:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08a45b62c6c64f548b645c8a89af044e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>目前组里的业务组件库因为一些历史背景原因，源码和展示站点分为两个独立的项目工程维护，而市面上对于组件、组件库、工具库的源码和站点在一个仓库维护或者采用 MonoRepo 的方式开发和维护，因此在不改变项目架构的前提下（暂时不要纠结为什么不放在一起维护），我们对于效率协同和工程化方面进行了一系列的演进，下面首先介绍下我们当前面临的问题：</p>
<h1 data-id="heading-0">面临的问题</h1>
<h2 data-id="heading-1">npm link</h2>
<p>因为源码和站点维护在两个工程下，在本地开发的时候如何关联两个项目是首先面临的问题，最初我们采用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.npmjs.com%2Fcli%2Fv7%2Fcommands%2Fnpm-link" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.npmjs.com/cli/v7/commands/npm-link" ref="nofollow noopener noreferrer">npm link</a> 的方式，但是因为组件库和站点均是基于 react hook 开发，因此每次进行组件迭代开发都需要经历下面几步：</p>
<ul>
<li>站点下: cd node_modules/react && npm link 和 cd node_modules/react-dom && npm link</li>
<li>源码下: npm link react && npm link react-dom</li>
<li>源码下: npm link</li>
<li>站点下: npm link 源码</li>
</ul>
<p>不难发现，这样的方案有以下痛点（每个新参与开发的同学都会吐槽 diss）：</p>
<ul>
<li>操作繁琐易出错；</li>
<li>yarn 和 npm 混和使用使得 link 问题频出；</li>
<li>link 断链；</li>
</ul>
<h2 data-id="heading-2">站点 & 源码，双编译</h2>
<p>这一版我们完全抛弃了 npm link，采取了比较 hack 的方式：</p>
<ul>
<li>源码 watch 文件变更，实时编译构建 ESM；</li>
<li>源码 watch ESM 变更，实时同步到站点 node_modules 下；</li>
<li>站点 watch node_modules 下组件 ESM 变更，热更新；</li>
</ul>
<p>不难发现，这样的方案有以下痛点：</p>
<ul>
<li>监听 node_modules 变更，姿势很 hack；</li>
<li>双边 watch + 编译，严重消耗内存资源；</li>
<li>热更新时间 = 组件 ESM 编译时间 + 同步推送时间（可以忽略不计） + 站点编译时间，10s+妥妥的；</li>
</ul>
<h2 data-id="heading-3">站点单编译</h2>
<p>既然站点和源码都具有编译构建能力，为什么不减少一次编译构建呢？为此我们进行了第三次优化升级：</p>
<ul>
<li>源码 watch 文件变更，实时同步源码到站点缓存目录下 ；</li>
<li>开发环境下，站点 import node_modules 下 ESM 变更为 import 缓存目录下组件源码；</li>
<li>站点 watch 缓存目录下组件源码变更，热更新；</li>
</ul>
<p>虽然这次升级后已经解决了大部分的问题，但是还是存在问题。</p>
<p>源码本地开发的优化使得站点编译压力的增加：</p>
<ul>
<li>热更新慢：改个文案 hotreload 2s +；</li>
<li>冷启动更慢：60s 妥妥的；</li>
</ul>
<p>其实到现在这一步问题已经一定程度往 webpack 衍生方案的通病上靠了，因此，我们把目标聚焦在了新的构建工具上。</p>
<h1 data-id="heading-4">为什么选择 Vite ？</h1>
<p>下面我列举了一常见的构建工具以及以及一些选型思考。</p>
<p>首先是 Webpack 以及 Webpack 衍生方案：</p>
<ul>
<li>基于 CRA 封装的业务脚手架；</li>
<li>CRA；</li>
<li>Webpack 轻量级配置；</li>
</ul>
<p>基于 Webpack 的方案和目前使用的脚手架差异不大，收益不明显，并且从根本上也解决不了 Webpack 带来的生产力问题。</p>
<p>接下来是目前比较火的基于 ESM 的现代方案：</p>
<ul>
<li>Snowpack</li>
<li>Vite</li>
</ul>
<p>关于比较尤大的文章更有说服力：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fcomparisons.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/comparisons.html" ref="nofollow noopener noreferrer">对比</a>。</p>
<p>此外，就我个人而言，我觉得尤大在华人社区以及国内的影响力更大一些，因此尤大开源的工具在国内社区活跃度会更高一些，关注度也会更高，对于后续的可持续发展也比较有利，因此在选型上我们选择了 Vite。</p>
<h1 data-id="heading-5">成果收益</h1>
<ul>
<li>秒级冷启动：60s+ => 3s- （缓存生效后 300ms 左右）</li>
<li>毫秒级热更新：2s+ => 1s- （sync + hotreload）</li>
</ul>
<p>喜大普奔，收效显著！！！</p>
<h1 data-id="heading-6">Vite 为什么快？</h1>
<p>首次冷启动：esbuild 预编译，生成缓存</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08a45b62c6c64f548b645c8a89af044e~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4f53eec533d4e3cafc2452c87c48aa5~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea7e41f76ef749c3b098113c453ffb5b~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再次冷启动：利用缓存</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83af014ec65b4788b9b8185369393031~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">冷启动</h2>
<p>首先冷启动为什么快，因为 Vite 基于原生 ESM，也就是说 Vite 将原来 Webpack 前置构建 bundle 的工作交给了性能强悍的现在浏览器来做，所以冷启动时间大幅缩减（毕竟冷启动最耗时的就是分析代码构建 bundle）。</p>
<p>而在 Vite 中，正如官方文档介绍的那样，Vite 将我们的代码氛围了依赖和源码两部分：</p>
<ul>
<li>依赖：大多为在开发时不会变动的纯 JavaScript。Vite 将会使用 esbuild 预构建依赖。esbuild 使用 Go 编写，并且比以 JavaScript 编写的打包器预构建依赖快 10-100 倍</li>
<li>源码：通常包含一些并非直接是 JavaScript 的文件，需要转换（例如 JSX，CSS 或者 Vue/Svelte 组件），时常会被编辑。同时，并不是所有的源码都需要同时被加载（例如基于路由拆分的代码模块）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f54e047ef94473a92973d51c3be997~tplv-k3u1fbpfcp-zoom-1.image" alt="bundle based dev server" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以 Webpack 为代表的“bundle based dev server”，在冷启动前需要依赖诸如 babel 之类的工具对代码进行分析并编译生成可运行的 bundle，这一<strong>构建时</strong>的过程造成了冷启动时间过长。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed6b92ded0c84fc3b57368b655eea9a6~tplv-k3u1fbpfcp-zoom-1.image" alt="ESM based dev server" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而对于“ESM base dev server”来说，dev server 依赖的是我们 ESM，而我们的代码本身就是以 ESM 编写的，因此进去要告知 dev server 目标模块路径加载即可，编译解析交给浏览器的<strong>运行时</strong>去处理，从而大大加速了我们的冷启动。</p>
<h2 data-id="heading-8">热更新</h2>
<h3 data-id="heading-9">基于原生 ESM</h3>
<p>在 Vite 中，HMR 是在原生 ESM 上执行的。和冷启动一样的道理，当我们修改了一个文件后，不需要在重新编译了，热更新也就大大减少耗时了。</p>
<h3 data-id="heading-10">配合 http 头</h3>
<p>Vite 充份利用了 http 缓存，这也是我们在本地开发时候看到的一个和 webpack 比较大的不同，network 中充满了大量模块请求。</p>
<ul>
<li>源码部分：304 配合 ETag 协商缓存</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19436848241242e2aecc86511bd04284~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>依赖模块：强缓存</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62f020e867fb47da9f38b99b769b02be~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">Webpack to Vite ？</h1>
<p>那么如何平稳的从 Webpack 迁移到 Vite ？ 其实，当你按照 Vite 文档落地的时候已经兼容 80%的 Webpack 场景。只需要考虑一些额外 case：</p>
<h2 data-id="heading-12">ESM 及 ESM 衍生问题</h2>
<p>Vite 利用了 esBuild 去预构建 ESM，因此对包的要求相对严格，对于 esBuild 预编译失败的场景需要 case by case 处理。</p>
<p>例如：</p>
<h3 data-id="heading-13">esBuild 预编译失败</h3>
<p>这里以 react-virtualized 为例，react-virtualized 的 WindowScroll.js 下引入了 flow 的类型文件导致预编译失败。</p>
<p>可以写 esBuild 插件、写 resolutions、拉包本地改。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73494bca28494dec97a27a03ebc11230~tplv-k3u1fbpfcp-watermark.image" alt="888.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ffd4f34ecf245c498b87c23e9522d81~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">dep-scan 依赖分析失败</h3>
<p>以 react-infinite-scroller 为例，他在 package.json 中 ESM 读取目录指向了发包后被忽略的 src 源码目录，导致 dep-scan 插件查找模块失败。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/716908ac3ed447f298842b2c8e93e583~tplv-k3u1fbpfcp-watermark.image" alt="777.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">ESNext bundle</h3>
<p>Vite 构建过程由 esBuild 接管，而 esBuild 支持的 target 的最低版本为 es6，因此想要构建兼容性更强的 bundle 需要对 Vite 的产出二次编译或者使用官方给出的基于 SystemJS 的方案。</p>
<p>下面这张图是截取的 Vite 官网的兼容性一节：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31f2668c7274413da62d1d23f3813ec9~tplv-k3u1fbpfcp-watermark.image" alt="loadimage.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用官方插件：</p>
<ul>
<li>babel 转译并注册为 System.js 模块；</li>
<li>添加 System.js 运行时；</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6233f407c5d24072bff4233ace076188~tplv-k3u1fbpfcp-watermark.image" alt="6666.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-16">说在最后</h1>
<p>向我们组件库的展示站点或者内部系统的工程项目说用了就用了，但是实际投入到对外的项目时我们也不得不考虑一些问题：</p>
<h2 data-id="heading-17">成本</h2>
<p>单说从 Webpack 切换到 Vite 成本很低，甚至比 Webpack 的大版本升级还要简单。但是从 Webpack 到 Vite 不仅仅是构建工具的转换而是整个生态的迁移，那么对于历史项目已存在的 babel 插件、Webpack 插件等都需要等量替换，这是一个成本。此外，就像上一节说的那些，对于一些不规范的三方包我们也需要做额外的适配，这也是一个成本。</p>
<h2 data-id="heading-18">收益</h2>
<p>从目前看，Vite 带来的工程效率收益比较高，但是就我个人而言尝试的仅是简单的展示站点，并不能严格和实际的业务工程划等号，并且企业级项目工程量和复杂度都比较大，Vite 是否能符合预期的带来收益我个人还不敢保证。</p>
<h2 data-id="heading-19">风险</h2>
<p>最后，因为涉及到了 ESM，就算官方给出了 SystemJs 版本的兼容插件，但是实际投入对外项目的兼容性风险也还是未知的。</p></div>  
</div>
            