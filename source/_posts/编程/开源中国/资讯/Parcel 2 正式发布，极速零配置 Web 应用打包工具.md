
---
title: 'Parcel 2 正式发布，极速零配置 Web 应用打包工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6439'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6439'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Parcel v2.0.0 稳定版已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fparceljs.org%2Fblog%2Fv2%2F" target="_blank">发布</a>。公告写道，此版本延续了 Parcel 1 的零配置打包体验，并使其拥有了强大的拓展能力以适应任何规模和复杂度的项目。</p> 
<p>据介绍，Parcel 2 是对 Parcel 的彻底重写，涉及到许多方面。更新亮点包括：</p> 
<ul> 
 <li>新的插件系统：为 Parcel 提供了完整的拓展能力，允许 Parcel 从小规模项目拓展到具有复杂构建要求的大规模生产环境的应用程序</li> 
 <li>默认开启 Tree Shaking：包括 ES modules、CommonJS、dynamic import 和 CSS modules 的支持</li> 
 <li>巨大性能提升：包括用 Rust 写的新的 JavaScript 编译器和新的多任务并行架构，能够利用所有的 CPU 内核并行执行</li> 
 <li>自动拆分代码：包括将公共模块去重到可以并行加载和缓存的共享包中</li> 
 <li>图像大小调整、转换和优化，包括对 AVIF 和 WebP 等现代图像格式的支持，以及对 JPEG 和 PNG 的自动无损优化</li> 
 <li>显着提高缓存可靠性，包括跨机器的可移植性，以及所有配置、插件、开发依赖项等的自动跟踪，这些操作均无需配置</li> 
 <li>改进热加载功能，包括对 React Fast Refresh 的支持</li> 
 <li>支持 bundle inlining ，它允许您将一个 bundle 的编译内容嵌入到另一个 bundle 中，例如将图像内联为数据 URL</li> 
 <li>支持构建库，包括输出到 ES 模块、CommonJS，甚至绑定 TypeScript 定义</li> 
 <li>改进了 web worker 支持，包括对原生 ES 模块 worker、worklets、service worker manifests 等的支持</li> 
 <li>更好的诊断，提供漂亮的语法高亮代码框架、提示，甚至文档链接以了解更多信息</li> 
 <li>更可靠的文件观察器，用 C++ 编写并与底层操作系统 API 集成，即使在 Parcel 重新启动时也能快速使缓存失效</li> 
 <li>使用 Parcel 的新源映射库带来了更快、更准确的源映射，该库使用 Rust 编写，性能比 Parcel 1 提升 20 倍</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fparceljs.org%2Fblog%2Fv2%2F" target="_blank">更多内容查看发布公告</a>。</p> 
<p>迁移指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fparceljs.org%2Fgetting-started%2Fmigration%2F" target="_blank">https://parceljs.org/getting-started/migration/</a></p>
                                        </div>
                                      
</div>
            