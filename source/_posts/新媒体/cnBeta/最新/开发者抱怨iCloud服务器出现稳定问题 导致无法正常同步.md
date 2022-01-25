
---
title: '开发者抱怨iCloud服务器出现稳定问题 导致无法正常同步'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0125/94a656a277283b9.webp'
author: cnBeta
comments: false
date: Tue, 25 Jan 2022 02:32:20 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0125/94a656a277283b9.webp'
---

<div>   
<strong>近日，不少开发者抱怨苹果 iCloud 服务器存在稳定性问题，导致一些已经实现 iCloud 支持的应用程序无法正常同步。</strong>自去年 11 月以来，在开发者论坛和 Twitter 上就有不少开发者抱怨出现了 CloudKit 连接问题。一些内置 iCloud 支持的应用会出现“请求失败，http状态代码503”的错误。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0125/94a656a277283b9.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">热门笔记应用 GoodNotes 背后的开发者经常看到这个问题，他们为遇到这个错误信息的客户写了一份支持文件。GoodNotes 团队表示，该应用会自动重试连接，因此问题最终会得到解决，但他们不确定是什么原因导致连接错误开始。</p><p style="text-align: left;">GoodNote 团队表示：“HTTP 503 是一个临时错误代码（"服务不可用"），表明 iCloud 服务器没有正确响应来自你设备的请求。该错误通常会随着 GoodNotes 的自动重试而得到解决，但我们收到许多关于该错误持续存在的报告，导致同步失败。这个问题对我们来说并不明显，我们已将此案上报给<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>技术支持团队进行调查。这似乎也发生在其他应用程序上”。</p><p style="text-align: left;">一些开发者指出，在突然出现的iCloud服务器问题之前，他们的应用程序已经工作了多年，没有任何问题，这显然是导致错误信息的原因。来自苹果论坛上的一位开发者：</p><blockquote><p style="text-align: left;">我有同样的问题，我的用户中相对较少的比例。他们现在得到 503 错误，但去年却没有出现过。我的代码并没有改变。我甚至不知道如何提交一份错误报告，因为我无法在我的设备上复现这个问题，而且这个问题只发生在相对较小比例的用户身上。</p></blockquote><p style="text-align: left;">少数开发者已经能够从苹果工程部门获得帮助，其中一个人能够改变他们的开发者账户的iCloud容器以解决这个问题，但似乎有许多开发者仍然有问题。其他开发者已经诉诸于在他们的应用程序中构建iCloud状态仪表板，这样客户就可以看到iCloud什么时候无法运行。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0125/66eed184e533219.webp" referrerpolicy="no-referrer"></p>   
</div>
            