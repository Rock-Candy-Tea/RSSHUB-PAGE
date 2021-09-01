
---
title: '黑客又有新攻击方法，这次是从GPU的显存入手'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/612f586f8e9f09298c0eae63_1024.jpg'
author: ZAKER
comments: false
date: Wed, 01 Sep 2021 05:15:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/612f586f8e9f09298c0eae63_1024.jpg'
---

<div>   
<p>不论是 AMD、NVIDIA 还是 Intel 的 GPU，现在都有机会被恶意软件利用进行攻击，因为根据 Bleeping Computer 报导，有网络不法份子就找到了可以从 GPU 显存上储存及以执行恶意软件的方法。</p><p>虽然说在这之前就已经有差不多类似的方法，但那都是属于学术界的研究而已，并且也并非是完整的方法。而在这个月较早时间，有人就在一个黑客论坛上公开售卖可以让恶意代码避开系统 RAM 检查的 PoC（概念验证）档案，说明不法份子的攻击方法可能已经过渡到更加复杂的程度。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202109/612f586f8e9f09298c0eae63_1024.jpg" data-height="337" data-width="927" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/612f586f8e9f09298c0eae63_1024.jpg" referrerpolicy="no-referrer"></div></div>图片来源：Bleeping Computer<p></p><p>这位卖家没有做过多的说明，只是表示这个方法是利用了 GPU 的显存缓冲来储存以及执行恶意代码。不过这个方法也有一定限制，那就是只能用支持 OpenGL 2.0 或以上的 Windows 系统上。卖家同时也表示他们已经在 Intel UHD 620/630、RX 5700、GTX 740M 以及 GTX 1650 这些显卡上测试过这个方法并且是可行的。</p><p>之后论坛上有人指出，基于 GPU 的恶意软件之前也出现过，就如 JellyFish 一样，这是一个 Linux 系统的 GPU Rootkit 隐遁攻击。不过卖家随后也否认他们这次的新方法与 JellyFish 有任何联系。这份 PoC 是在 8 月 8 日挂出的，在 8 月 25 日卖出，卖家当然也没有公布卖出的价格以及对方为何人。</p><p>这样的攻击方法在理论上来说是非常难被用户的计算机探测到的，而且即便探测到，也很难删掉，可能需要重刷一遍显卡的 vBIOS 才行。</p><p>超能网公众号</p><p><strong>扫码关注我们，浏览热门硬件评测</strong></p><p><strong>随时查看最新天梯榜</strong></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            