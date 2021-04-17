
---
title: '_图_Android 12将允许用户管理隐藏的垃圾桶功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0417/942bf051a01c3fa.jpg'
author: cnBeta
comments: false
date: Sat, 17 Apr 2021 03:03:22 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0417/942bf051a01c3fa.jpg'
---

<div>   
谷歌似乎正在为 Android 设备添加垃圾桶功能（如果你喜欢 Windows 的命名方式，你也可以叫做回收站）。在对 Android 12 偷跑镜像深入挖掘之后，XDA-Developers 在设置应用的代码中发现了一行关于“Trash”（垃圾桶）的引用。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0417/942bf051a01c3fa.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0417/942bf051a01c3fa.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">当你点击 Trash 设置，Android 12 应该会弹出一个对话框，告诉你被删除的文件在系统上占用了多少存储空间，然后提供了选项允许用户清空它。这项功能看起来应该和 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、macOS 一样，不过在实际代码实现方面由于各种原因，可能会更加复杂。</p><p style="text-align: left;">事实上在 Android 11 中，谷歌就引入了 trash API，应用程序可以使用它来隐藏文件，而不是即时和完全删除它们。不过该功能很少被使用。谷歌自己似乎也准备在 Files by Google 应用中支持它，但到目前为止，它还没有出现在实际版本中。</p><p style="text-align: left;">所以，Android 11中已经存在垃圾桶功能，但似乎很少有应用在使用它；即使使用了，也还没有办法真正恢复被垃圾的文件。在Android 12中，XDA 发现的设置似乎也没有提供恢复功能，但个别文件管理应用--比如谷歌自家的就可以。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/b5021f664aabbf7.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/14f03b7de3f4b5e.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/cfa35d6a01752fe.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/422a3f4a1c63942.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Android 文件管理并不像桌面操作系统上那样简单。技术上来说，被删除的文件只是在文件名前面加个句号就隐藏在原地。另外，每个不同的Android制造商都可以选择使用自己的文件管理应用，而不是谷歌提供的应用--而这些应用可能支持也可能不支持新的垃圾桶API。</p><p style="text-align: left;">简而言之，Android 12和谷歌自己的Files应用可以支持垃圾桶和恢复文件，但这并不意味着Android 12上的任何应用都一定会支持。</p>   
</div>
            