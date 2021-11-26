
---
title: '淘系技术飞冰团队正式发布 icejs 2.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-08afdce5636fa6c81efc5163c651b23e7e8.png'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 00:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-08afdce5636fa6c81efc5163c651b23e7e8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p style="color:rgba(0, 0, 0, 0.8); margin-left:8px; margin-right:8px"><span style="color:rgba(52, 48, 48, 0.92)">这应该是最完善的 React+Vite 解决方案</span></p> 
</blockquote> 
<h2><span>icejs是什么？</span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">icejs 是一个基于 React 的渐进式研发框架，由淘系前端飞冰（ICE）团队于 2020.02 发布 1.0 版本，icejs 目前广泛服务于阿里内部以及社区用户，如下图所示，在阿里内部每天至少有 400 多个仓库基于 icejs 构建并发布，目前已经服务了内部 3K 多的开发者以及 5K 多项目。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><img alt src="https://oscimg.oschina.net/oscnet/up-08afdce5636fa6c81efc5163c651b23e7e8.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">很多人可能会问，为什么需要或者什么场景下需要使用 icejs？这里把其中的 icejs 换成 Next.js、UmiJS 或者 Nuxt.js 问题依然成立，核心的问题都是此类研发框架的价值是什么？我尝试讲一下飞冰团队对于这个问题的思考：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">通过内置功能+插件化能力保证跨项目的一致性：对于稍具规模的前端团队往往会涉及很多个前端项目以及跨团队的协同，一致性的开发&使用方式能够更好的保证协同效率。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">通过开箱即用的框架能力降低重复劳作：小到 TypeScript、CSS Modules 之类的构建配置，大到 MPA/SPA/微前端等不同模式的能力提供。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">某些原本很复杂的功能可以让业务低成本接入：诸如 SSR/SSG、一体化这些能力，基于 Webpack/Vite 需要做非常多的事情，框架可以让这个成本大幅度降低。</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">同时也必须承认的是相比于直接基于 Webpack/Vite 这样的构建工具，研发框架会带来黑盒、带来约束、不够灵活……而这也是对框架开发团队最大的挑战：在提供各种能力的基础上如何还能保证良好的研发体验。</span></p> 
<h2 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span>全新的2.0版</span></h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-868fa87567778baea70cd4f07e65cf5ca7d.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">自 2020.02 发布 1.0 版本至今一年半的时间里，icejs 结合社区的反馈迭代了 70 多个正式版本（平均每周一个版本），这也使得框架的功能丰富度&稳定性不断提升。而在 2021 年前端社区非常重要的两个趋势：</span></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li style="text-align:justify"> <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#ff6827"><strong><span style="background-color:#ffffff">基于 ES modules 的 Bundleless 模式:<span> </span></span></strong></span><span style="background-color:#ffffff">随着浏览器对于 ES modules 的原生支持，社区也出现配套的构建工具 Snowpack 以及后续的 Vite，Bundleless 模式正在撼动着以 Webpack 为主流的 Bundle everything 模式</span></p> </li> 
 <li style="text-align:justify"> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">基于 Rust/Go 重写前端工具链：</span></strong><span style="background-color:#ffffff">替代 babel 的 swc，替代 Webpack 的 esbuild，Rome 用 rust 重写，Next.js 引入 Rust 后构建速度提升 5x</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">这两个趋势也让大家更清晰的认识到传统 Webpack 工程体系构建速度太慢了，前端的调试构建体验有很大的提升空间，因此飞冰团队围绕「开发者体验」开始探索 icejs 2.0 版本，经过 3 个月的研发周期，总共 100+ Pull Requests，我们在 2021.09.28 正式发布了 2.0 版本，目前阿里内部 200+ 的项目已经基于 2.0 版本，我们也在今天向社区正式输出 icejs 2.0 的介绍文章。2.0 的一些重要特性：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">Vite 模式：</span></strong><span style="background-color:#ffffff">在原先 Webpack 基础上，同步支持了 Vite 模式，同时在工程配置和框架能力上尽量保持一致性。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">Webpack 5：</span></strong><span style="background-color:#ffffff">将 Webpack 从 V4 版本升级到 V5 版本，引入新版本的 Module Federation、Cache 等相关能力。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">swc&esbuild：</span></strong><span style="background-color:#ffffff">试验性的在 Webpack 模式下引入 swc 替换 babel，尝试提升 Webpack 模式下最耗时的代码编译阶段，同时压缩链路也支持使用 esbuild 替代 terser。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">更加完善的业务解决方案：</span></strong><span style="background-color:#ffffff">提供状态管理、请求库、环境配置、微前端、SSR、SSG（新增）、PWA（新增）、keep-alive（新增）等完备的解决方案。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="background-color:#ffffff; color:#ff6827">全新的文档：</span></strong><span style="background-color:#ffffff">通过 Docusaurus 构建全新的文档站点，得益于 Docusaurus 丰富的能力，文档在 SEO、加载体验、Dark Mode、搜索、手机端体验等能力上有了大幅度的提升。</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">对于 2.0 版本，可以通过命令行快速创建，支持 antd/fusion/... 等多种模板：</span></p> 
<pre><code>$ npm init ice icejs-example
# 同时支持 yarn
$ yarn init ice icejs-example</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">为了保证基础的开发体验，建议使用 cnpm 或者国内的 npm registry 安装依赖。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">除了 CLI 以外，我们同时提供了研发工具 AppWorks 用于可视化创建项目，只需要在 VS Code 插件市场中搜索并安装 AppWorks 即可：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1bff0faadb7f0739670da00214b73b65d81.png" referrerpolicy="no-referrer"></p> 
<h2><span>Vite 模式：突破</span></h2> 
<p><span>随着社区不断涌现的基于 ES modules 的构建工具，以及逐步完善的生态支持度，ES modules 的开发方式被越来越多的开发者所接受和尝试。得益于 Vite 本身的成熟度，icejs 也是能够快速的支持 ES modules 开发模式，同时我们的官方脚手架也已经默认开启了 Vite 模式。</span></p> 
<pre><code>// build.json
&#123;
  "vite": true
&#125;</code></pre> 
<h3><span style="background-color:#ffffff"><strong style="color:#ff6827">快速适配 Vite 模式</strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>对于完全基于 Webpack 建设的框架体系，引入 Vite 最大的问题就是两种模式在使用上如何尽量保持一致、框架代码如何更好的维护。针对这个问题，首先在配置上统一沿用原先的 </span><code><span>build.json</span></code><span> 配置文件，支持 </span><code><span>publicPath</span></code><span>、</span><code><span>alias</span></code><span> 等工程配置，对于框架中所有的工程配置操作都基于原先的 </span><code><span>webpack-chain</span></code><span> 进行，</span><span>一般情况下不需要面对 Vite/Webpack 的配置差异，通过抽象的 webpack-service 以及 vite-service 两个适配层，在 service 这一层实现对应的 start/devServer/build 能力，同时借助 wp2vite 将 Webpack 的配置一次性转换为 Vite 配置。</span><span>如下为大体的架构设计，后续我们也会有专门的文章来介绍这部分的设计和实现。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-742428cf69922fbb07e286a74a5eb713968.png" referrerpolicy="no-referrer"></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><strong style="color:#ff6827">启动与热更新</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在引入 Vite 之后，我们针对 fusion-design-pro 这个较为复杂的项目做了一些测试，首先是项目启动时间，首次启动时间上，Vite 本身有按需构建的机制，加上借助 esbuild 的加持比 Webpack 快了 50%，但是二次启动时间上，得益于 Webpack 5 Cache 机制的加持下反而是 Webpack 要稍快于 Vite。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>由于 Vite 的 devServer 启动不依赖源码编译，因此 Vite 的 启动编译结束时间基于源码开始执行时间计算。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-65dfbd9f63e30af6abc17bb959b3e2a5774.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">其次是热更新时间，与启动时间相比热更新时间 Vite 是完全碾压 Webpack 模式的，Vite 模式下热更新时间提升了 10 倍以上，只需要 100ms，并且不会随着项目变复杂而劣化。这也是我们觉得 ES modules 模式带来的最大收益点。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3f7dbad825afc7a72ddcefb672be2508b77.png" referrerpolicy="no-referrer"></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><strong style="color:#ff6827">框架能力适配</strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>除了上述基础的配置以外，框架还提供了更上层的能力，对于这些能力我们也做了同步的支持：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>MPA/SPA/微前端/一体化等不同应用模式的工程能力适配</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>本地调试实时的 TypeScript/ESlint 检测能力：实现 vite-plugin-ts-checker 以及 vite-plugin-eslint-report 插件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>JSX+ 语法支持：结合 Babel 实现对应的 vite-plugin-jsx-plus 插件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>SSR/SSG：支持中</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>通过上述工作，我们保证了 icejs Webpack 模式下 80% 的能力在 Vite 模式下一致性的使用方式，其他能力我们也在结合业务诉求同步支持中。</span></p> 
<h2><span>Webpack 模式：稳中求进</span></h2> 
<p><span>icejs 1.0 有大量存量的 Webpack 模式项目需要持续支持，同时在某些场景也无法切换到 ES modules 模式，因此在 2.0 中我们对于 Webpack 模式依然跟随社区的脚步在做持续的优化。</span></p> 
<h3><span><span><strong style="color:#ff6827">Webpack 5</strong></span></span></h3> 
<p><span>从 ice.js 2.0 版本开始，底层工程依赖的 Webpack 版本将默认采用 v5 版本，工程上对 Webpack 相关的生态进行适配升级，确保开发者能够顺利过渡到 Webpack 5。借助 Webpack 5 的 Cache 能力，在 2.0 中热启动时间提升了近 5 倍，同时将 React Fast Refresh 做了内置将热更新的时间减少了 30%。另一方面我们也将诸如 postcss, less-loader, sass-loader 等依赖升级到了最新版本，确保开发者可以享受到新的功能。</span></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><span><span><strong style="color:#ff6827">基于 Module Federation 的预编译方案</strong></span></span></span></h3> 
<p><span>借助 Webpack 5 的 Module Federation 特性，icejs 2.0 支持将应用的依赖预构建为一个 Module Federation 的 remote 应用，供当前应用进行消费，应用依赖不再编译到一个文件中，以减少 Webpack 对于依赖打包所需的时间。</span></p> 
<pre><code>&#123;
  "remoteRuntime": true
&#125;</code></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-87f02c03bf6bb7b0b6a27384c6c7d807da7.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-00376f5a131a8f66ae96f6e6ed467f9f55d.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">通过 Module Federation 预编译的开启，热启动相比 1.x 版本提升明显，并且让热更新时间缩短近 60%。</span></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><span><span><strong style="color:#ff6827">使用 SWC 替代 Babel（试验）</strong></span></span></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><code><span>swc</span></code><span> </span><span>利用 rust 大大提升 JavaScript 源码的编译效率，目前已支持大部分 babel 编译的场景。因此 icejs 提供一键开启 swc 编译能力：</span></p> 
<pre><code>&#123;
  "swc": true
&#125;</code></pre> 
<p style="margin-left:0; margin-right:0"><span>开启 swc 编译后，除了 babel 被替换以外，默认的压缩器也从 terser 切换至 swc，进一步缩短时间：</span></p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-5d4a18a36fbba31ecfca43d58f0c60ab3ea.png" referrerpolicy="no-referrer"></p> 
<p><span>开启 swc 编译后，编译速度平均提升 50%，压缩速度提升近 35%。不过 swc 目前对于自定义插件支持还不友好，因此如果强依赖了一些其他 babel 插件，那么 swc 下目前是很难对齐，因此我们也将该项能力标识为「试验性」。目前前端社区对于 swc 越加重视， 飞冰团队也在积极参与 swc 相关方案的讨论，相信在不远的未来我们可以使用 swc 完全替代掉 babel。</span></p> 
<h2 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span>更多新特性</span></h2> 
<h3><span><span><span><strong style="color:#ff6827">微前端 x ESM</strong></span></span></span></h3> 
<p><span>在 icejs 支持 Vite 模式之后，同为飞冰团队开源的微前端框架 icestark 也同步支持了 ESM 规范的微应用，只需要在微应用上配置</span><span style="background-color:#ffffff"> </span><code><span>loadScriptMode: import</span></code><span>参数即可开启：</span></p> 
<pre><code><AppRouter>
  <AppRoute
    title="商家平台"
+   loadScriptMode="import"
    url=&#123;[
      '//unpkg.com/icestark-child-seller/build/js/index.js',
      '//unpkg.com/icestark-child-seller/build/css/index.css',
    ]&#125;
  />
</AppRouter></code></pre> 
<p><span style="background-color:#ffffff; color:#333333">在开启该选项之后，icestark 会通过 dynamic import API 加载微应用资源。由于 ES modules 脚本只执行一次的策略，微应用二次加载渲染的速度提升非常明显。</span></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><span><span><strong style="color:#ff6827">跟 SSR 一致的 SSG 方案</strong></span></span></span></h3> 
<p><span>SSG(Static Site Generation) 即静态站点生成，对于一些官网或者文档的场景，SSG 能够提供更好的 SEO 以及首屏渲染能力。icejs 1.0 中 SSG 方案基于 puppeteer 实现，开发者经常会遇到环境依赖的问题，在 2.0 中我们将 SSG 和 SSR 的方案做了更好的对齐，使用起来更加简单，仅需在工程配置中开启即可：</span></p> 
<pre><code>// build.json
&#123;
  "ssr": "static"
&#125;</code></pre> 
<p><span style="color:#333333">仅需上述配置，在 build 之后就会生成每个路由的静态 HTML 文件，并且也同时支持 SSR 下的</span><span style="background-color:#ffffff; color:#333333"> </span><code><span>Page.getInitialProps</span></code><span style="background-color:#ffffff; color:#333333"> </span><span style="color:#333333">在构建时获取初始数据能力：</span></p> 
<pre><code>├── build
|  ├── dashboard
|  |  └── index.html   # 预渲染 Dashboard 页面组件得到的 HTML
|  ├── index.html      # 预渲染 Home 页面组件得到的 HTML
|  └── js
|     └── index.js</code></pre> 
<p><span style="color:#333333">针对动态路由的场景，也支持在页面路由组件上设置</span><strong style="color:#333333"><span style="background-color:#ffffff"> </span><code><span>getStaticPaths</span></code><span style="background-color:#ffffff"> </span></strong><span style="color:#333333">属性：</span></p> 
<pre><code>// src/pages/Project/index.tsx: /project/:id
const Project = (props) => &#123;
  return <>Hello</>;
&#125;

+Project.getStaticPaths = async () => &#123;
+  return Promise.resolve(['/project/1', '/project/100', '/project/1001']);
+&#125;

export default Project;</code></pre> 
<p><span style="background-color:#ffffff; color:#333333">SSG 的构建产物支持直接使用 nginx、oss 以及后端服务等多种部署方式，而应用的渲染模式上也支持按页面维度分别以 SSR 或者 SSG 方式渲染。</span></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><span><span><span><strong style="color:#ff6827">更定的依赖管理方案</strong></span></span></span></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>研发框架往往会包含非常多的工程相关依赖，而我们也时不时会遇到社区依赖发包导致框架不可用的问题，因此在 2.0 中我们将依赖的 70+ 社区 NPM 包进行了预打包，只要 icejs 不主动升级，这些包以及其依赖的包版本就不会变化，以此来保证框架不会受这些依赖包发版影响，同时预打包也能间接提升框架安装的速度。</span></p> 
<h2><span>未来</span></h2> 
<h3><span><span><span><strong style="color:#ff6827">Vite 模式下的能力完善</strong></span></span></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>目前我们核心的工程能力已支持 Webpack/Vite 两种模式一键切换，包括 SPA/MPA/微前端等场景，但是 Vite 模式下依然有很多需要突破的地方：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>SSR/SSG 能力支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>进一步对齐 Vite/Webpack 的工程能力，比如 Vite 中更为简洁直观的 Static Assets 使用方式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>统一 Vite 模式下 AST 转换的能力，受限于 Vite 内置编译工具 esbuild 的开放 API 能力，强依赖 Babel 的场景（react-rerefsh、jsx、jsx+）都是插件各自调用 Babel，我们会在框架层面对这一层进行统一，同时会尝试直接引入 swc</span></p> </li> 
</ol> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><span><span><strong style="color:#ff6827">更轻量的一体化研发模式</strong></span></span></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在很多中小型中后台系统的业务场景下，往往都是一个开发者从前到后负责整体的研发，在这种场景下以往的前后端分离反而会增加代码管理、接口联调、发布部署流程等成本。得益于前后端都使用 JavaScript 带来的语言一致性，以及 Serverless 基建保障低运维成本，过去一年里，我们基于 icejs + midway-hooks 的一体化研发模式在阿里内部落地了众多中小型中后台系统，同时也为 C 端业务低成本的实现 SSR 方案提供了巨大支持。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在 2.0 版本里，我们希望进一步完善一体化方案，一方面会让服务端框架更加轻量以提升 API 的开发调试体验，另一方面也会在 FaaS 基础上支持 Node.js 部署，保障即便在没有 Serverless 基建的公司中也能够使用一体化能力。</span></p> 
<h2><span>团队介绍</span></h2> 
<p><span>飞冰（ICE）团队隶属于淘系前端架构团队，希望能通过研发框架和研发工具改善前端开发者的体验。如果对 icejs、Vite、Webpack、VS Code 插件、Electron 等领域比较感兴趣，欢迎</span><span>关注我们的 GitHub 仓库：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps%3A%2F%2Fgithub.com%2Falibaba%2Fice" target="_blank"><span>https://github.com/alibaba/ice</span></a></p>
                                        </div>
                                      
</div>
            