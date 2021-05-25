
---
title: 'Parcel 2 beta 3 发布，极速零配置 Web 应用打包工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a7c0826d0bc69ba90d52ee004aa6ee86360.png'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a7c0826d0bc69ba90d52ee004aa6ee86360.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Parcel 2 beta 3 已于上周发布，这是一款 Web 应用打包工具，它通过利用多核处理提供了极快的速度，并且不需要任何配置。</p> 
<p>新版本的亮点包括：</p> 
<ul> 
 <li>使用 Rust 彻底重写 JavaScript 编译器，整体构建性能提升 10 倍</li> 
 <li>动态导入 Tree shaking</li> 
 <li>支持 tree shaking CSS 模块</li> 
 <li>支持按需构建 (lazy development builds)</li> 
 <li>减少依赖项</li> 
 <li>……</li> 
</ul> 
<h1>Rust 重写的 JavaScript 编译器性能提升 10 倍</h1> 
<p>据介绍，Parcel 团队在过去的几个月里一直在专注于用 Rust 重写 Parcel 的 JavaScript 编译器。Parcel 的 JavaScript 编译器负责检测代码中的依赖项（如<code>import</code>语句和<code>new Worker()</code>调用），内联<code>process.env</code>变量和其他 Node 全局变量以及执行范围提升。</p> 
<p>此外，Parcel 会自动为已配置的<code>browserslist</code>目标转译源代码，包括诸如 JSX 和 TypeScript 之类的非标准语法以及 React Fast Refresh 等开发阶段的功能。</p> 
<p>在此版本之前， 所有这些任务都是在 Babel AST 的基础上用 JavaScript 实现的，虽然 Parcel 团队进行了许多优化，但 JavaScript 编译器仍是 Parcel 最慢的部分。</p> 
<p>新的 JavaScript 编译器基于 Rust 的 SWC 编译器编写，SWC 提供 JavaScript 解析和代码生成功能，以及用于构建超快速 AST 转换的坚实基础。Rust 提供了可预测的性能、即时的启动时间以及对硬件级别进行优化的能力。总体而言，新的编译器将构建性能整体提升了 10 倍。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a7c0826d0bc69ba90d52ee004aa6ee86360.png" referrerpolicy="no-referrer"></p> 
<h1>动态导入 Tree  shaking</h1> 
<p>支持动态导入 Tree  shaking 是一项与作用域提升实现相关的功能。Parcel 可以检测动态导入的哪些属性可以被访问，并排除已解析模块中未使用的导出。这适用于 promise chaining、async/await、解构和静态对象属性访问。如果非静态访问任何内容（例如，计算属性），则将包含所有导出。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-342395d8eed4e9cb3d62f9ff0301bf8f371.png" referrerpolicy="no-referrer"></p> 
<h1>支持 tree shaking CSS 模块</h1> 
<p>新版的 Parcel 支持 tree shaking CSS 模块。在 JavaScript 中导入 CSS 模块时，Parcel 会跟踪使用了哪些类，并自动从编译的 CSS 文件中排除未使用的选择器。此外，类名现在会自动内联到已编译的 JavaScript 中，而不是存储在大型对象图中。这将有助于减小 CSS 和 JS 输出的捆绑包大小。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f46f2281ff1f84b91c7f5aad7c1d072a9de.png" referrerpolicy="no-referrer"></p> 
<h1>路线图</h1> 
<p>根据官方开发团队的说法，Beta 3 应该是第一个候选版本发布之前的最终 Beta 版本，对于第一个候选版本，目前正在研究以下项目：</p> 
<ul> 
 <li>改进缓存无效性 (cache invalidation)，以进行打包和优化</li> 
 <li>确保缓存在机器或不同文件路径之间（例如 CI）可移植</li> 
 <li>改进的自动差分捆绑支持（模块/无模块）</li> 
 <li>API 一致性</li> 
</ul> 
<p>候选版本发布之后，公共 API 将被冻结，期间将专注于修复错误和完善文档，这大约需要一个月的时间。一切准备就绪后，将发布 2.0 稳定版。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv2.parceljs.org%2Fblog%2Fbeta3%2F" target="_blank">详细更新说明查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            