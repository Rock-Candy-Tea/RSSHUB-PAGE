
---
title: 'Webpack 打包后代码执行时机分析与优化 (www.alloyteam.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8198'
author: 技术头条
comments: false
date: 2022-07-30 07:09:34
thumbnail: 'https://picsum.photos/400/300?random=8198'
---

<div>   
代码执行时机将决定着是否能够正常执行，当依赖文件没加载完成就开始执行、使用对应模块，那么将会导致执行异常。这在 “存在资源加载失败时，加载重试影响原来文件的执行顺序” 的场景下尤为常见。

webpack 构建除了进行模块依赖管理，实际上，也天然地管理了 entry 与 chunk 多文件的执行时机，但缺少了对 external 文件管理，当 external 文件加载失败或未完成时，执行、使用对应模块同样将导致异常。为此，wait-external-webpack-plugin 应运而生，以 webpack 插件的形式，补充 external 的执行管理。本文将进行简要说明。
    
</div>
            