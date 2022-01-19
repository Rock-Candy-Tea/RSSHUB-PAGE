
---
title: '苹果正修复Safari漏洞：可提取你的近期浏览历史'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0119/48dd41a65e93642.webp'
author: cnBeta
comments: false
date: Wed, 19 Jan 2022 03:29:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0119/48dd41a65e93642.webp'
---

<div>   
<strong>上周，存在于 WebKit 中的一个 BUG 被曝光，黑客可以通过名为 IndexedDB 的 JavaScript API 实现入侵。</strong>浏览器指纹服务 FingerprintJS 表示，这个错误可以揭示你最近的浏览历史，甚至是你的身份。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0119/48dd41a65e93642.webp" alt="1m8byt2u.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">根据 GitHub 上的 WebKit 提交，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>此后为该 BUG 准备了一个修复方案，但该修复方案要等到苹果发布 macOS Monterey、iOS 15 和 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>OS 15 更新版本的 Safari 后才会向用户提供。当被要求提供向公众发布修复程序的时间框架时，苹果拒绝发表评论。</p><p style="text-align: left;">该漏洞允许任何使用 IndexedDB 进行客户端数据存储的网站访问其他网站在用户浏览会话期间生成的 IndexedDB 数据库的名称。这个错误可以让一个网站跟踪用户在不同标签或窗口中访问的其他网站，因为数据库名称往往是每个网站所特有的，有时数据库名称包含用户特定的标识符，可能会暴露用户的身份。</p><p style="text-align: left;">FingerprintJS 有一个关于这个 BUG 的动态演示，它影响到使用苹果开源浏览器引擎 WebKit 的较新版本的浏览器，包括 MacOS 的 Safari 15 和所有版本的 iOS 15/iPadOS 15 的 Safari。该错误还影响到iOS 15和iPadOS 15上的Chrome和Edge等第三方浏览器，因为苹果要求所有<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a>和iPad浏览器都使用WebKit。</p>   
</div>
            