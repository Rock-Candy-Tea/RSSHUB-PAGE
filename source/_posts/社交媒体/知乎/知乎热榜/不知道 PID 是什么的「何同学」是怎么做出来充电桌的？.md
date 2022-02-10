
---
title: '不知道 PID 是什么的「何同学」是怎么做出来充电桌的？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic3.zhimg.com/v2-1705b99e80c13769e2eed9d53710ffd1_1440w.jpg'
author: 知乎
comments: false
date: Thu, 10 Feb 2022 06:41:39 GMT
thumbnail: 'https://pic3.zhimg.com/v2-1705b99e80c13769e2eed9d53710ffd1_1440w.jpg'
---

<div>   
森山的回答<br><br><p data-pid="ZtXJ95wT"><b>PID是什么，网上一大堆资料，但是你真的会用吗？</b></p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-1705b99e80c13769e2eed9d53710ffd1_1440w.jpg" data-caption data-size="normal" data-rawwidth="700" data-rawheight="291" data-default-watermark-src="https://pic1.zhimg.com/v2-8f4d2500e3d22ee041361d6f5a8379c7_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-1705b99e80c13769e2eed9d53710ffd1_r.jpg" referrerpolicy="no-referrer"></figure><p data-pid="mepKKCRR">那么多算法公式和函数，有几个人不做实验就能整明白的？只有你真正在项目上用到了，调P调I调D，一个个调了有什么效果变化，才会体验到，PID到底是什么？</p><h2>我的理解是，通过P、I、D这3个参数中的某一项或者某几项参数的调整，来实现你的设备以较快的速度、较平滑的变化、较小的抖动，达到并维持在目标状态。</h2><p data-pid="h6EX4JcF">比如我自己做的这个真空吸力的控制装置：</p><a href="https://www.zhihu.com/zvideo/1353732451110375424" data-draft-node="block" data-draft-type="link-card"></a><a href="https://www.zhihu.com/zvideo/1355106569936367616" data-draft-node="block" data-draft-type="link-card"><p data-pid="YhFI0R89">但并不是所有电机控制都需要用到PID的。</p><p data-pid="9grddW8S">比如对速度性能要求不高的步进电机，它本身就带有步进计数，就算发生失步现象，也可以通过位置传感器、编码器等东西来判断状态量。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-0903e25f7bccf3aac20a59c8ab24e612_1440w.jpg" data-caption data-size="normal" data-rawwidth="600" data-rawheight="400" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-0903e25f7bccf3aac20a59c8ab24e612_r.jpg" referrerpolicy="no-referrer"></figure><p data-pid="-RlvVu2S">其实PID在程序中就是简单几行代码，你没有去调试是很难体会到它的精髓，PID最重要的还是整定，不断地尝试修改参数，最后获得一组近似完美的方案，然后多调几个项目，你就会积累一些PID的整定经验，知道什么样的目标状态下，需要去修改哪些参数，大致的修改幅度等等。</p><hr><p data-pid="DFaRhSUr">何同学的桌子我看过，下面应该就是2个丝杠滑台，由2个步进电机，或者伺服电机做的，原理上比较简单，只是隔行如隔山，大家不熟悉，觉得很酷罢了。</p><p data-pid="_ZK2MiGH">何同学做的东西，技术深度都一般，主要是以创意吸引人，当然人家就是做媒体的，不是做产品的。和稚晖那种产品创意结合的制作比起来，真的不是一个量级的差距。我们做产品的最难的地方不是功能，而是性能和稳定性。</p><p data-pid="No8dVGmL">很多机器人的技术也就是以这些步进电机、伺服、舵机为基础的控制应用。</p></a><a href="https://zhuanlan.zhihu.com/p/169841389" data-draft-node="block" data-draft-type="link-card" data-image="https://pic4.zhimg.com/v2-721e5bc088cbab3ee89f4d80f913c898_bh.jpg" data-image-width="988" data-image-height="440" class="internal">森山：如何打造自己的低成本电子实验室？</a><a href="https://zhuanlan.zhihu.com/p/183240859" data-draft-node="block" data-draft-type="link-card" data-image="https://pic1.zhimg.com/v2-d218c8ac1fc862e14d95f96f33c7a008_bh.jpg" data-image-width="1920" data-image-height="1080" class="internal">森山：一条布的诞生-DIY纺织机控制系统</a><p data-pid="S7nLX3vz">还有啊，现在“AI”这个词真的是被用滥了，明明就是简单的自动控制原理，现在都叫“AI”，都是蹭热点，高大上。</p>  
</div>
            