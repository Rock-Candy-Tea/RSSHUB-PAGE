
---
title: 'Google Chrome新下载UI或向Microsoft Edge看齐'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1214/75a6a662a697e19.png'
author: cnBeta
comments: false
date: Tue, 14 Dec 2021 12:56:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1214/75a6a662a697e19.png'
---

<div>   
<strong>频繁更新的 Google Chrome 浏览器，即将迎来一项新变化 —— 它的下载 UI，将很快向 Microsoft Edge 看齐。</strong>通常情况下，Google 会先在 Canary 和 Dev 通道试验或大或小的新功能，然后才会更广泛地推出。最新消息是，该公司似乎正在探索一种用于活跃下载的新 UI，且看起来与 Microsoft Edge 非常相似。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/75a6a662a697e19.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Google Chrome 下载 UI</p><p>现阶段，当你通过 Google Chrome 下载文件时，浏览器会在下载过程中 / 下载完成后在窗口底部显示。但若 Chromium 主线提交有任何进展，这种行为方式或很快发生改变。</p><p>正如眼尖的 <a href="https://www.reddit.com/r/chrome/comments/rfxkfa/google_is_working_on_a_new_user_experience_for/" target="_self">Reddit</a> 网友 Leopeva64-2 发现的那样，<a href="https://chromium-review.googlesource.com/c/chromium/src/+/3311121" target="_self">Chromium Gerrit</a> 上出现了一个有关“在工具栏中添加下载图标”的新补丁，<strong>且相关注释描述也相当值得玩味：</strong></p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/cc98b26932948f9.png" alt="1.png" referrerpolicy="no-referrer"></p><p>作为下载用户体验（UX）重新设计的一部分，该补丁为下载工具栏的图标添加了基础支持。此 CL 仅跟踪下载状态，并在工具栏中生成一个消失的图标。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/2c637f96be3fe25.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">// 是否要用下载气泡来替代‘书架’？</p><p>// 已下载的图标将显示在工具栏的可信区域中，时效与父工具栏视图（parent ToolbarView）相关 —— 比如下载正在进行 / 或在过去 24 消失内启动下载，该图标才可见。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/e2331c7bf424ef9.png" alt="0.png" referrerpolicy="no-referrer"></p><p>此外还有对‘环形进度栏’（RingProgressBar）变量的引用。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/e379839fde76765.png" alt="Edge Download.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Microsoft Edge 下载 UI</p><p>许多人推测，Google 很可能将 Chrome 下载 UI 挪动到浏览器的工具栏、而不是留在窗口底部，此外下载图标也将变成一个简单的进度环。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1214/0ad5f52b038825a.gif" alt="5.gif" referrerpolicy="no-referrer"></p><p>若真如此，那新版 Google Chrome 的下载体验将更加接近于 Microsoft Edge 。至于这项变动最终是否会走入稳定版通道，仍有待进一步观察。</p>   
</div>
            