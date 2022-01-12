
---
title: '如何看待IOS版手机QQ新安装包高达800M+，内置虚幻4游戏引擎？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=8673'
author: 知乎
comments: false
date: Wed, 12 Jan 2022 05:53:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=8673'
---

<div>   
虚幻引擎的回答<br><br><p data-pid="vj79ltKW">只谈技术。</p><p data-pid="Gmkg-ycu">一，UE as Lib。 首先表扬一下QQ团队的一点点技术实力。虽然UE4.27推出了<a href="http://link.zhihu.com/?target=https%3A//docs.unrealengine.com/4.27/zh-CN/SharingAndReleasing/BuildAsALibrary/" class=" wrap external" target="_blank" rel="nofollow noreferrer">UE as Lib功能</a>(<a href="http://link.zhihu.com/?target=https%3A//docs.unrealengine.com/4.27/zh-CN/SharingAndReleasing/BuildAsALibrary/" class=" wrap external" target="_blank" rel="nofollow noreferrer">文档</a>)，但依然只是Beta版本，且依然限制只在Windows平台和Single Viewport。因此这次QQ的IOS内嵌UE4应该是他们团队自己改造的。盲猜也可能是QQ团队也获得了其他QQ内部游戏团队的技术帮助，不过对于一个App团队能否拥抱最新的技术，应该给个赞。</p><p data-pid="H2zBwJm8">二，期待之后的技术更新优化。实话讲，放进一个100多M的UE4.so，特别是对于QQ这种国民app来说，这个决策的背后肯定是有非常多的考量的。目前也只是刚刚整合进去，相信在技术优化上还有一些空间的，且在渲染展示的效果上也可以继续提高。相信QQ团队是有更大的愿景的，我们拭目以待就好。</p><p data-pid="fyZzDEkD">三，给其他家的借鉴。QQ这种内嵌UE4的方式，说白了，就是在App内嵌一个3D渲染交互的功能，只不过UE4的渲染效果好一些，内容开发工具链完善一些，有源码改造便利一些，因此采用了UE4而已，这样就不需要自己再手动去开发3D的一系列功能。这种内嵌的模式，在移动App上目前还只是QQ先吃了螃蟹，未来可能还会有其他家。但在PC企业软件上，其实大家就完全可以尝试起来了，通过在自己的传统软件里内嵌UE4窗口的方式来做可视化效果的升级，同时也不需要重写自己的业务逻辑。以往的方式大家都往往纠结于如何在QT里内嵌UE4进程的窗口，但到现在利用UE as Lib的功能就可以更方便的开发了。</p><p data-pid="LpF0k-rk">3D形态终将渗透到越来越多的领域，而这也是游戏引擎这种基础设施的作用所在。不说了，看代码去了。</p>  
</div>
            