
---
title: 'Taro 3.2 版本正式发布：React Native 支持，王者归来'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26cef652c0d45b5a8e8fbb1eb3396ac~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 21:45:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26cef652c0d45b5a8e8fbb1eb3396ac~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>Taro</strong> 是一个开放式 <strong>跨端跨框架</strong> 解决方案，支持使用   React/Vue/Nerv 等框架来开发 <code>微信/京东/百度/支付宝/字节跳动/QQ小程序/H5/React Native</code> 等应用。</p>
<p>自从 Taro 3 发布以来，不少开发者期待 Taro 3 可以支持 React Native。基于 58 团队在 React Native 方向的技术积累，我们与 Taro 团队达成战略合作伙伴关系。由 58 团队主导开发 Taro 3 React Native，共同推进 Taro 的发展。</p>
<p>去年 12 月开始，已经完成了 <a href="https://mp.weixin.qq.com/s/-7G7NMHX8ol99QxkswFOxg" target="_blank" rel="nofollow noopener noreferrer">Taro 3 React Native 的支持</a>，共发布了 9 个 canary 版本与 4 个 beta 版，经过较长时间的验证，如今终于迎来了 3.2 正式版。</p>
<h2 data-id="heading-0">一、Highlights</h2>
<h3 data-id="heading-1">1. 更快编译速度</h3>
<p>在 Taro 3 之前版本中，Taro 作为一个编译型框架，React Native 打包 <code>bundle</code> 会分为两个过程。首先，对 Taro 源码进行大量的 AST 操作转换成 React Native 的代码，然后再利用 Metro 打包成 <code>bundle</code>，整个编译速度有待进一步提升。</p>
<p>Taro 3 React Native 对整个编译系统进行较大调整，不再生成中间代码，而是直接利用 Metro 生成 <code>bundle</code>，通过运行时适配 Taro 3 标准，这种方式使得编译过程更简单，大大提升了编译速度，且给我们带来了更多的好处:</p>
<ul>
<li>利用 Metro 打包 React Native ，通过多级缓存以及 hasteFS 让打包速度更快；</li>
<li>更加贴合 React Native 生态，社区基于 Metro 打包优化方案对接更加容易；</li>
</ul>
<p><img alt="Taro 2 与 Taro 3 启动过程对比" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26cef652c0d45b5a8e8fbb1eb3396ac~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2. <code>source-map</code> 支持</h3>
<p>在旧版本的 Taro React Native 中，通过将 Taro 代码转换为 React Native 的中间代码，再利用 Metro 打包成 <code>bundle</code>。 这种方式不仅编译速度不佳，利用中间代码打包成 <code>bundle</code>，不能支持到<code>source-map</code>，调试起来不够直观。</p>
<p>Taro 3 对编译系统进行较大调整，不再生成中间代码，而是直接利用 Metro 对 Taro 源码进行打包，这样在提升编译速度的同时，也天然支持<code>source-map</code>，对于开发体验是一个巨大的提升，能够达到与开发原生 React Native 应用一致的体验。</p>
<p><img alt="基于 source-map 进行debug" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20fc02cc43874e03a89e016db4224884~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3. 多 React Native 版本支持，拥抱最新版 0.64</h3>
<p>过去 Taro 对移动端的支持，React Native 的版本都是相对固定的，修改 React Native 版本存在较多的不便。</p>
<p>Taro 3 对系统架构进行了全面升级，React Native 版本取决于开发者项目中的依赖，<strong>目前支持 0.60 以上的 React Native 版本，当然最新的 0.64 也是完全支持</strong>。</p>
<p>在 React Native 0.64 的版本中，iOS 端完成 了对 Hermes 引擎的支持，默认启用了内联引用，也支持 React 17 等等，想体验这些新特性的开发者只需升级对应依赖即可。</p>
<p><strong>新项目升级</strong></p>
<p>Taro 模板默认依赖 React 17、TypeScript 4，运行 React Native 端会自动安装 0.64 的版本，直接使用即可。</p>
<p><strong>旧项目升级</strong></p>
<blockquote>
<p>从 v2.x 升级的同学需要先按 <a href="https://taro-docs.jd.com/taro/docs/next/migration/" target="_blank" rel="nofollow noopener noreferrer">迁移指南</a>进行操作。</p>
</blockquote>
<p>如果是Taro 3 的旧项目，手动升级对应的依赖：</p>
<ul>
<li><code>react: ^17.0.0</code></li>
<li><code>react-dom: ^17.0.0</code></li>
<li><code>typescript: ^4.1.0</code></li>
<li><code>@typescript-eslint/parser: ^4.15.1</code></li>
<li><code>@typescript-eslint/eslint-plugin: ^4.15.1</code></li>
<li><code>react-native:^0.64.0</code></li>
</ul>
<p>设置 ESLint 配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .eslintrc</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">"extends"</span>: [<span class="hljs-string">"taro/react"</span>],
  <span class="hljs-string">"rules"</span>: &#123;
    <span class="hljs-string">"react/jsx-uses-react"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-string">"react/react-in-jsx-scope"</span>: <span class="hljs-string">"off"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. 更丰富API与组件</h3>
<p>要真正做到一套代码，多端复用，非常重要的一点就是组件和 API 的覆盖度，在 Taro 3.2 之前，适配 React Native  已经实现了很多常用 API 和组件，但与小程序，H5 之间还存在较大的差距，需进一步完善。在新的版本中，我们进一步提升组件和 API 的覆盖度，共新增 <strong>45</strong> 个 API 与 <strong>8</strong> 个组件。</p>
<p>在如今多媒体时代，视频、音频等相关组件与 API 都是必不可少的一部分，在 Taro 3 中，我们也都已经集成进来了，除了多媒体相关，还有扫码，VirtualList 等等，大大丰富了 API 与组件。更多内容请参考<a href="https://docs.taro.zone/docs/apis/about/desc" target="_blank" rel="nofollow noopener noreferrer">文档</a>。</p>
<p><strong>新增的API:</strong></p>

























<table><thead><tr><th>API</th><th>功能</th></tr></thead><tbody><tr><td>scanCode</td><td>扫码</td></tr><tr><td>show/hideTabBar...</td><td>tabBar 相关</td></tr><tr><td>createCameraContext</td><td>相机相关</td></tr><tr><td>...</td><td>...</td></tr></tbody></table>
<p><strong>新增的组件</strong></p>

























<table><thead><tr><th>API</th><th>功能</th></tr></thead><tbody><tr><td>Video</td><td>视频</td></tr><tr><td>Camera</td><td>相机</td></tr><tr><td>VirtualList</td><td>长列表</td></tr><tr><td>...</td><td>...</td></tr></tbody></table>
<h3 data-id="heading-5">5. API与组件按需引入</h3>
<p>在 React Native 应用中，打包后最终 <code>bundle</code> 的大小会影响我们首次打开页面的时间，首次打开时间过长，对用户的体验存在一定的影响。</p>
<p>在 Taro 3 中，我们也对打包后 <code>bundle</code> 大小进行了优化。在实际的业务场景中，可能并不会使用到 Taro 提供的所有组件和 API ，但仍然会将所有的组件与 API 及相关依赖打包到最终的 <code>bundle</code> 中，这无疑会增加 <code>bundle</code> 的大小。</p>
<p>为了减少打包后的大小，我们对组件和 API 实现了按需引入的方式，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Taro <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/taro'</span>

Taro.scanCode(options)

<span class="hljs-comment">//实际打包后的引入会根据页面使用的引入</span>
=> <span class="hljs-keyword">import</span> &#123; scanCode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/taro-rn/dist/lib/scanCode'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，这种实现按需引入，对于项目中未使用的组件与 API 以及对于依赖的库，都不会打包到<code>bundle</code>的中，能够大大减少最终<code>bundle</code>的大小，进一步提升 App 首次打开页面时间。同时因为按需引入的存在，壳工程可自主进行优化定制，降低 APP 包大小。</p>
<h3 data-id="heading-6">6. 与 React Native 应用融合</h3>
<p><strong>有开发者提到，已有react native的项目中，在不修改原有业务的情况下，是否便于接入呢？</strong></p>
<p>在 Taro 3 我们给出了肯定的答案，Taro 3 的整个编译体系进行了升级，直接基于 Taro 源码进行打包 ，通过自定义<code>transformer</code>，运行时适配的方式，生成支持 Taro 的 Metro 配置，并与业务的配置进行合并，根据最终 Metro 配置完成<code>bundle</code>的打包。这种方案比较容易扩展。</p>
<p>我们通过提供支持 Taro 的打包 Metro 配置并提供运行时方法，开发者只需与现有业务打包配置结合，并用运行时方法进行包装处理。这样可以比较方便的与现有导航系统结合，也无需修改原有代码，即可以轻松接入。 详细可参考<a href="https://github.com/wuba/Taro-Code-In-React-Native" target="_blank" rel="nofollow noopener noreferrer">Demo</a>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//metro.config.js 参考配置</span>
<span class="hljs-keyword">const</span> Supporter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@tarojs/rn-supporter'</span>)

<span class="hljs-keyword">const</span> supporter = <span class="hljs-keyword">new</span> Supporter()
<span class="hljs-keyword">const</span> taroMetroConfig = supporter.getMetroConfig()
<span class="hljs-keyword">const</span> busConfig = &#123;
  <span class="hljs-attr">resetCache</span>:<span class="hljs-literal">true</span>,
&#125;
<span class="hljs-built_in">module</span>.exports = mergeConfig(busConfig,taroMetroConfig)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">7. 不跨端使用</h3>
<p><strong>没有跨端需求，是否就不需要使用 Taro 呢？</strong></p>
<p>对于当前没有跨端的需求，仅需要开发 React Native 应用或者小程序的开发者，我们仍然推荐使用 Taro ，主要有以下几点原因：</p>
<ul>
<li>支持快速到其他端，便于后期扩展；</li>
<li>可使用 Taro 组件与 API，提升开发速度；</li>
<li>相比 React Native 样式的写法，写法更加简单便捷，并且支持多种预编译语言；</li>
</ul>
<h2 data-id="heading-8">二、升级指南</h2>
<blockquote>
<p>从 v2.x 升级的同学需要先按 <a href="https://taro-docs.jd.com/taro/docs/next/migration/" target="_blank" rel="nofollow noopener noreferrer">迁移指南</a>进行操作。</p>
</blockquote>
<p>从 v3.x 升级的同学，首先需要安装 v3.2 的 CLI 工具：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -g @tarojs/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后进入项目，删除 <strong>node_modules</strong>、<strong>yarn.lock</strong>、<strong>package-lock.json</strong>。</p>
<p>最后把 <code>package.json</code> 文件中 Taro 相关依赖的版本修改为 <code>^3.2.0</code>，再重新安装依赖，至此升级结束。</p>
<blockquote>
<p>目前 Taro 3 仅支持 React 开发的项目运行在 React Native 端。</p>
</blockquote>
<h2 data-id="heading-9">三、未来规划</h2>
<p>Taro 3 已完成 <strong>React Native</strong> 端的适配，未来我们将从组件和 API 的覆盖度，使用成本等几个方面继续完善。不断提升API与组件的覆盖度，尽可能减少与H5、小程序端的差异。通过增加新手教程，减少项目初始化步骤，提供更多的案例等方面，不断降低使用成本。</p>
<p>Taro 也提供了微信群方便大家与维护者们更及时沟通交流：</p>
<p><img alt="微信群" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79ba9859fb89487aa562e65407bd093d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">四、感谢</h2>
<p>Taro 团队衷心感谢各位参与过本项目开源建设的朋友，无论是为 Taro 提交过代码、建设周边生态，还是反馈过问题，甚至只是茶余饭后讨论、吐槽 Taro 的各位。</p>
<p>现诚挚的邀请您与 Taro 团队交流您的使用情况，也希望能够提出更多宝贵的意见，有你相伴，Taro 会更加精彩。</p>
<p><img alt="问卷调查" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cb3a4dd105e44dea736a4034fb4ccfe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后，特别感谢为 Taro 从 v3.1 走到 v3.2 贡献过代码的各位同学，排名不分先后：</p>
<ul>
<li>@KeenV</li>
<li>@baranwang</li>
<li>@LiHDong</li>
<li>@changcllong</li>
<li>@liuchuzhang</li>
<li>@baranwang</li>
<li>@SyMind</li>
<li>@ryougifujino</li>
<li>@inarol</li>
<li>@huaoguo</li>
<li>@zhiqingchen</li>
<li>@zhenglong</li>
<li>@Qiuz</li>
<li>@shinken008</li>
<li>@skychx</li>
<li>@iambool</li>
<li>@iChengbo</li>
<li>@nickyefei</li>
<li>@xzj</li>
<li>@yechunxi</li>
<li>@Victor</li>
<li>@xieweilyg</li>
<li>@Dugz</li>
<li>@haojie</li>
<li>@b2nil</li>
<li>@doublethinkio</li>
<li>@CodeDaraW</li>
</ul>
<h2 data-id="heading-11">作者简介</h2>
<ul>
<li>陈志庆：58同城 前端架构师，技术委员会委员</li>
<li>叶春喜：58同城 资深前端开发工程师</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            