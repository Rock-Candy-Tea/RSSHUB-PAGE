
---
title: 'Parcel 2.3 发布，依赖项减少 70%'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6337'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6337'
---

<div>   
<div class="content">
                                                                                            <p>Parcel 是用于 Web 的零配置构建工具。它将出色的开箱即用开发体验与可扩展的体系结构相结合，可将你的项目从零发展为大规模生产应用程序。</p> 
<p>Parcel 2.3 发布，更新内容如下：</p> 
<p>这个版本将 Parcel 所需的 npm 依赖项的数量减少了 60% 以上。这是在之前 2.2 版本的基础上进行的，所以综合来看，Parcel 现在安装的依赖项减少了 70% 以上。这一点是通过以下方式实现的：</p> 
<ul> 
 <li>将一些依赖项预先捆绑到 Parcel 上，而不是从 npm 加载它们。这是为那些小的和 Parcel 内部的包所做的（即你不会在项目中直接与它们交互），这减少了 Parcel 用户的维护负担。</li> 
 <li>根据需要自动安装节点内置的 polyfills（如 <code>buffe</code> 和 <code>stream</code> 等）。这些东西很少使用，但占了大量的安装依赖。</li> 
 <li>删除内置的 Babel 和 PostCSS 模块依赖，只有在实际使用时才按需安装到项目中。</li> 
</ul> 
<h3>其他变化</h3> 
<ul> 
 <li>支持 React 18 预发布版和实验版的自动 JSX 运行时</li> 
 <li>修复 non-module 脚本中的 <code>@swc/helpers</code></li> 
 <li>修复 PNPM monorepos 中的自动安装依赖</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fparcel-bundler%2Fparcel%2Freleases%2Ftag%2Fv2.3.0" target="_blank">https://github.com/parcel-bundler/parcel/releases/tag/v2.3.0</a></p>
                                        </div>
                                      
</div>
            