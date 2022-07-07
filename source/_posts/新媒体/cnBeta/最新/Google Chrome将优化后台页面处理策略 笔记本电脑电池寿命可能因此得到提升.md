
---
title: 'Google Chrome将优化后台页面处理策略 笔记本电脑电池寿命可能因此得到提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0707/ef773da86292f6d.webp'
author: cnBeta
comments: false
date: Thu, 07 Jul 2022 13:45:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0707/ef773da86292f6d.webp'
---

<div>   
Google
Chrome是世界上最受欢迎的互联网浏览器，但在许多情况下，它也因消耗电池寿命而臭名昭著，然而，一个新的幕后变化可能会扭转目前的局面。在Google
Chrome的最近更新中，一个新的测试标记已经浮出水面，显示了浏览器节省电池电量的一个潜在来源。<br>
 <p>这个名为"快速密集节流"(quick intensive throttling)的即将推出的功能，可以阻止位于后台的页面吞噬过多的电池寿命。</p><p><img src="https://static.cnbetacdn.com/article/2022/0707/ef773da86292f6d.webp" title alt="Chrome-OS-105-feature.webp" referrerpolicy="no-referrer"></p><p>Chromebook的用户首先在Chrome OS 105的更新中发现了这一新策略，但它实际上适用于所有提供Google Chrome的平台--包括<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、macOS和Linux。</p><p>Google Chrome的"快速强化节流"功能可以在10秒后停止后台页面加载JavaScript元素，而之前的限制是5分钟，Google解释说。对于在后台加载的页面，在10秒后激活密集节流，而不是默认的5分钟。强化节流将限制唤醒，从具有高嵌套级别的setTimeout和setInterval任务以及延迟的scheduler.postTask任务，最多每分钟1次。</p><p><img src="https://static.cnbetacdn.com/article/2022/0707/5b64560774d2f80.webp" title alt="Chrome-OS-88-Chromebook-Diagnostics-app.webp" referrerpolicy="no-referrer"></p><p>在进一步的评论中，Google把这句话翻译成了更容易听懂的样子：</p><p>这有望延长电池寿命，在"Canary"和"Dev"频道上的实验没有发现我们的指导性指标有任何退步，而且当所有标签都被隐藏和静止时，CPU占用有明显的改善（约10%）。</p><p>当然，这只在正确的情况下适用。对于大多数人来说，电池寿命的节省将来自于同时打开几个标签页的状况。如果一个页面在新标签页中被打开，但没有立即进行互动，这一变化将防止该标签页完全加载，实际上会反过来消耗电池，但这实际上只适用于你正在访问的页面严重依赖JavaScript的情况。</p><p><img src="https://static.cnbetacdn.com/article/2022/0707/dfea4ef10457ef7.webp" title alt="Chromebook-Diagnostics-CPU-test-2.webp" referrerpolicy="no-referrer"></p><p>这个变化目前只在Dev频道显示，所以可能要过一段时间才会扩展到稳定频道的每个人。</p>   
</div>
            