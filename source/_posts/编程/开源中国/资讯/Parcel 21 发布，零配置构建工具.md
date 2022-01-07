
---
title: 'Parcel 2.1 发布，零配置构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8507'
author: 开源中国
comments: false
date: Fri, 07 Jan 2022 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8507'
---

<div>   
<div class="content">
                                                                                            <p>Parcel 是用于 Web 的零配置构建工具。它将出色的开箱即用开发体验与可扩展的体系结构相结合，可将你的项目从零发展为大规模生产应用程序。</p> 
<p>Parcel 2.1 发布，更新内容如下：</p> 
<h3>新增：</h3> 
<ul> 
 <li>默认情况下启用转译 node_modules</li> 
 <li>重写核心图形数据结构</li> 
 <li>在开发中静态分析符号并为重新导出的模块启用延迟编译</li> 
 <li>将大的 blob 作为单独的文件存储在缓存中，而不是存储在 LMDB 中</li> 
 <li>添加<code>@parcel/optimizer-css</code></li> 
 <li>添加 <code>@parcel/bundler-experimental</code></li> 
 <li>支持 HTML 中 SVG <code><image></code> 标签的 <code>href</code> 属性</li> 
 <li>在加载 JSON5 配置时抛出代码框架的诊断</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>修复 CSS 模块的 HMR 行为</li> 
 <li>修复未被接受时 HMR 整页重新加载的问题</li> 
 <li>修复当一个 asset 有多个 ancestry 时的 HMR</li> 
 <li>修复<code>@parcel/transformer-typescript-tsc</code>中的源映射</li> 
 <li>修复<code>@parcel/transformers-typescript-types</code>中的TypeScript模块增量</li> 
 <li>修复 tsconfig 的"增量"选项为 true 时 TypeScript 类型生成的问题</li> 
 <li>修复使用 TypeScript 4.5以上版本的<code>createImportSpecifier</code>的问题</li> 
 <li>修复在构建 TypeScript 定义时，重新导出的类型的错误</li> 
 <li>修复了显示 "未导出" 错误提示时的一个错误</li> 
 <li>确保在缓存构建过程中显示"未导出"错误</li> 
 <li>修复 package.json<code>"sideEffects"</code>字段中的 glob 匹配问题</li> 
 <li>修复 <code>semver</code> 依赖的版本范围</li> 
 <li>当 React 别名为 Preact 时，使用现代 JSX 运行时</li> 
 <li>修复依赖关系为 URL 时的 React 版本检查</li> 
 <li>修复 SASS 中的 Tailwind</li> 
 <li>不要在开发中运行 Gzip 和 Brotli</li> 
 <li>默认情况下使用 Level 9 Zlib 压缩</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fparcel-bundler%2Fparcel%2Fblob%2Fv2%2FCHANGELOG.md%23210---2021-01-05" target="_blank">https://github.com/parcel-bundler/parcel/blob/v2/CHANGELOG.md#210---2021-01-05</a></p>
                                        </div>
                                      
</div>
            