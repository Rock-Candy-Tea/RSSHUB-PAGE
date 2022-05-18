
---
title: '拳头游戏就_MSI 延迟_问题发长文回应：釜山选手 Ping 值显示不准确'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://picsum.photos/400/300?random=6567'
author: IT 之家
comments: false
date: Tue, 17 May 2022 13:43:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=6567'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1866414" rel="nofollow">手写的从前</a> 的线索投递！</div>
            <p data-vmark="1a53"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 17 日消息，5 月 10 日，《英雄联盟》2022 季中冠军赛于在韩国釜山举办，LPL 赛区的季中冠军赛参赛队伍 RNG 在国内远程参加比赛。赛后，<strong>《英雄联盟》MSI 延迟不一的问题引起人们关注，一度登上微博热搜榜第八名</strong>。之后，拳头游戏就 MSI 上的延迟与重赛事件致歉，并表示将尽快分享一篇详细的技术说明。</p><p data-vmark="629b">今天，拳头正式公布了一篇 8000 多字超级详细的技术说明，以下是拳头回应的概述：</p><blockquote><p data-vmark="dc08" style="text-align: start;">在过去的几天，拳头游戏电竞技术团队在努力解决围绕着 2022 季中冠军赛的一系列技术问题，尤其在我们用来为线下选手和远程参赛选手平衡 ping 值的工具上。</p><p data-vmark="fa1a" style="text-align: start;">我们初次发现的问题是一个存在于我们称之为“延迟服务工具”中的错误 -这个工具是用来将所有参赛选手的延迟（ping 值）调整到 35ms 范围，而该错误会使在釜山场馆中的选手在比赛时产生额外的延迟，并使得其实际延迟高于场馆现场电脑屏幕上显示的延迟（35ms）。因此，<strong>在远程对局中，在中国的选手是在 35ms ping 值区间进行比赛的，但在釜山的选手 ping 值则较之更高</strong>。很不幸，我们并没有在季中冠军赛开始之前发现这个问题，其根本原因是一个代码漏洞错误计算了延迟，导致该数值在日志中也是错误的。因此，即使我们的监控显示一切正常，而实际上却存在着错误。</p><p data-vmark="5f3c" style="text-align: start;">我们在 5 月 13 日对该延迟服务工具进行了配置修改，以解决这个漏洞。考虑到之前实际网络延迟增加对釜山场馆中的比赛造成的影响，我们做出了艰难但是必要的决定：<strong>对 B 组对局 ping 值不相同的三场比赛进行重赛</strong>。</p><p data-vmark="86c8" style="text-align: start;">然而，5 月 13 日这一配置修改带来的另一个问题是，<strong>现在在釜山选手电脑屏幕上显示的是错误的、低于实际 ping 值的数字 </strong>—— 尽管实际 ping 值现在已被修正并确保对等。其后果是，当我们播放选手屏幕画面时，屏幕上会呈现一个错误的较低的 ping 值。同时，由于我们团队没能及时将这个外显误差进行有效沟通，故而观众会认为在场馆里的选手正在以低于他们实际延迟的 ping 值进行比赛。</p></blockquote><p data-vmark="d740">全文请见：<a href="https://weibo.com/ttarticle/p/show?id=2309404770219460790187" target="_blank">点此前往</a></p>
          
</div>
            