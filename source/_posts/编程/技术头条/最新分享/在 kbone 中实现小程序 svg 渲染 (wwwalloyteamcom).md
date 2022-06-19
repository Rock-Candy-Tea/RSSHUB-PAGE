
---
title: '在 kbone 中实现小程序 svg 渲染 (www.alloyteam.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=5571'
author: 技术头条
comments: false
date: 2022-06-19 15:08:42
thumbnail: 'https://picsum.photos/400/300?random=5571'
---

<div>   
kbone 是微信团队开源的微信小程序同构框架，与基于语法树转换的 Wepy、Taro 等传统框架不同，kbone 的思路是在逻辑层用类似 SSR 的方式模拟出 DOM 和 BOM 结构，让逻辑层的 HTML5 代码正常运行；而 kbone 会负责将逻辑层中的虚拟 DOM 以 setData 的形式传递给视图层，让视图层利用小程序组件递归渲染的能力，产生出真实的 DOM 结构。

使用 kbone 之后，我们可以将小程序页面理解为一个独立的 html 文档（而不是 SPA 中的一个 router page）。在每个页面的 JS 中初始化 kbone，为逻辑层提供虚拟 DOM 和 BOM 的环境，然后就可以像 H5 一样加载各种主流前端框架和业务代码，kbone 会负责逻辑层和视图层之间的 DOM 和事件同步。
    
</div>
            