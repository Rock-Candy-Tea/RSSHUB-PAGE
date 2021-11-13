
---
title: '神仙斗法：MSEdgeRedirect又成突破微软第三方浏览器限制新选择'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1113/a122dafd7621ca2.png'
author: cnBeta
comments: false
date: Sat, 13 Nov 2021 07:03:45 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1113/a122dafd7621ca2.png'
---

<div>   
昨日晚，微软对第三方浏览器工具Edgedeflecto实行封杀，Edgedeflecto是一款能够帮助用户绕过微软的协议限制，自行选择默认浏览器的工具。今天（11月13日），有用户发现，Github上出现了一款名叫MSEdgeRedirect的工具，<strong>这款小工具能够完成被封杀前Edgedeflecto的任务：修改Windows 11或Windows 10的默认浏览器。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1113/a122dafd7621ca2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1113/a122dafd7621ca2.png" title alt="MSEdgeRedirect.png" referrerpolicy="no-referrer"></a></p><p>不过和Edgedeflecto不同的是，<strong>MSEdgeRedirect想要生效需要用户保持MSEdgeRedirect在电脑后台运行，这是由于两者不同的解决方案导致的。</strong></p><p>Edgedeflecto是通过对<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11和Windows 10的microsoft-edge://协议进行调整实现的，<strong>这一行为无疑违反了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的用户协议，也给了微软封杀Edgedeflecto的理由。</strong></p><p>而MSEdgeRedirect则不同，它的生效是通过过滤并将Microsoft Edge进程的命令行参数传递到你的默认浏览器来实现的。</p><p><img src="https://static.cnbetacdn.com/article/2021/1113/cd6e576b223c068.webp" title alt="msedgeredirect.webp" referrerpolicy="no-referrer"></p><p>简单来说，<strong>MSEdgeRedirect并没有修改任何数据，它只是将原本导向Edge浏览器的数据拦截并传递给了用户设定的默认浏览器而已，这虽然使得MSEdgeRedirect必须维持运行才能够生效，但是也确保了它没有违反任何协议。</strong></p><p>除了在原理上避开微软的干涉外，MSEdgeRedirect的开发者也表示会在将来进行持续的更新，以确保微软无法轻易得使工具失效。</p><p>MSEdgeRedirect已上传至Github，需要的用户可以<a class="f14_link" href="https://github.com/rcmaehl/MSEdgeRedirect" target="_blank">前往下载</a>。</p>   
</div>
            