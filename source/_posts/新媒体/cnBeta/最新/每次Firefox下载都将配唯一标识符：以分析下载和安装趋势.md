
---
title: '每次Firefox下载都将配唯一标识符：以分析下载和安装趋势'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0319/18596682183f880.jpg'
author: cnBeta
comments: false
date: Sat, 19 Mar 2022 00:29:51 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0319/18596682183f880.jpg'
---

<div>   
<strong>现在从 Mozilla 网站下载 Firefox 浏览器，用户会发现在安装程序上有个唯一标识符，该标识符会在安装和首次运行时提交给 Mozilla。</strong>该标识符被 Mozilla 内部称为 dltoken，用于将下载与 Firefox 浏览器的安装和首次运行联系起来。该标识符对每个 Firefox 浏览器安装程序来说都是唯一的，这意味着每当使用它时都会提交给 Mozilla。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0319/18596682183f880.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0319/18596682183f880.jpg" alt="7exvnvs8.jpg" referrerpolicy="no-referrer"></a></p><p>虽然每次有新的 Firefox 浏览器版本发布时都可以下载新的安装程序，但也有可能为此再次使用已下载的安装程序。Mozilla 官方错误跟踪网站上的一份错误报告证实了下载令牌的使用。链接的文件并不公开，但列表本身证实了这种使用，并提供了关于为什么实施这种做法的解释：</p><blockquote><p>这些数据将使我们能够将遥测ID与下载令牌和Google分析ID联系起来。这将使我们能够跟踪哪些安装是由哪些下载产生的，以确定诸如"为什么我们每天看到这么多的安装，但每天没有那么多的下载？"等问题的答案。</p></blockquote><p>根据Mozilla的描述，该标识符被用来分析下载和安装趋势等。该功能由 Firefox 中的 Telemetry 提供，它适用于所有 Firefox 频道。有兴趣的用户可以验证这些发现。</p><p>其中一个比较简单的方法是检查两个或更多的 Firefox 浏览器安装程序下载的哈希值（相同的版本、语言和架构）。每个哈希值都是不同的。使用任何十六进制编辑器搜索 dltoken，就会发现 Firefox 安装程序中的字符串。</p>   
</div>
            