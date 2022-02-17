
---
title: '有AI学会控制核聚变反应堆了，来自DeepMind，登上今日Nature'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220217/v2_6a55c4e285d945b898dddbcbb58a2252_img_000'
author: 36kr
comments: false
date: Thu, 17 Feb 2022 09:03:34 GMT
thumbnail: 'https://img.36krcdn.com/20220217/v2_6a55c4e285d945b898dddbcbb58a2252_img_000'
---

<div>   
<p><span style="letter-spacing: 0px;">DeepMind在蛋白质折叠问题上实现巨大突破后，目标又转向</span><strong style="letter-spacing: 0px;">核聚变</strong><span style="letter-spacing: 0px;">了。</span></p> 
<p>最近，它开发出了世界上第一个深度强化学习AI——可以在模拟环境和真正的核聚变装置（托卡马克）中实现对等离子体的自主控制。</p> 
<p>陌生名词不要急，后面马上解释。</p> 
<p class="image-wrapper"><img data-img-size-val="934,744" src="https://img.36krcdn.com/20220217/v2_6a55c4e285d945b898dddbcbb58a2252_img_000" referrerpolicy="no-referrer"></p> 
<p>这比传统的计算机控制要更高效且精准，成果登上今天的Nature。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,447" src="https://img.36krcdn.com/20220217/v2_527710f77234441f947258d6075d9458_img_000" referrerpolicy="no-referrer"></p> 
<p>作为强化学习最具有挑战性的一个应用，这一成果也对加速可控核聚变有很大意义。</p> 
<h2><strong>用强化学习控制核聚变反应</strong></h2> 
<p>核聚变是未来最有潜力的清洁能源：只靠一个原子核就能产生巨大能量，除了相对少量的放射性废物（可在一个世纪内分解），不会产生任何温室气体。</p> 
<p class="image-wrapper"><img data-img-size-val="628,410" src="https://img.36krcdn.com/20220217/v2_13c478e7e5464fb6b74aa87347ef5222_img_000" referrerpolicy="no-referrer"></p> 
<p>但要在地球上实现这一反应无比困难，需要制造一个极端高温和高压的条件，在其中创建一个由裸原子核组成的<strong>“等离子体”</strong>。</p> 
<p>磁约束聚变装置——托卡马克（tokamak），是最有希望的一个实现方法。</p> 
<p>它是一个环形反应堆，可以在超过1亿摄氏度的环境下把氢加热（superheat）成等离子体的状态。</p> 
<p class="image-wrapper"><img data-img-size-val="804,803" src="https://img.36krcdn.com/20220217/v2_09482d4914d449b5838753a7cd4a2c69_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style><strong>△</strong> 托卡马克内部图</p> 
<p>由于等离子体温度太高，任何材料都无法容纳，要通过强大的磁场将它悬浮在托卡马克内部。</p> 
<p>在操作磁线圈时必须非常仔细，因为一旦碰壁，就可能导致容器损坏，并减缓聚变反应。</p> 
<p>而一个托卡马克装共有19个磁线圈，一秒需要调整线圈及其电压数千次。</p> 
<p>传统的装置中，每个线圈配备单独的控制器。</p> 
<p>每当研究人员想要改变等离子体的结构，尝试不同的形状以产生更高的能量时，就需要大量的工程和设计工作。</p> 
<p>DeepMind这个强化学习系统则可以<strong>一次控制全部19个线圈</strong>，并精确操纵等离子体自主呈现各种形状，呈现产生科学家们一直在探索的更高能量的新配置：</p> 
<p>比如下图中第二个“负三角”以及第四个“雪花”（这个形状可以通过将废能量分散到托卡马克壁上的不同接触点来降低冷却成本）。</p> 
<p>以及第一个“droplets”，这也是第一次在托卡马克内同时稳定两个等离子体。</p> 
<p class="image-wrapper"><img data-img-size-val="600,330" src="https://img.36krcdn.com/20220217/v2_288d9163c51f4d7b93d228f2c03e8d54_img_000" referrerpolicy="no-referrer"></p> 
<p>这个AI系统由<strong>DeepMind和瑞士</strong>洛桑联邦理工学院等离子体中心的物理学家共同完成。</p> 
<p>瑞士中心的一位成员表示：“这里面有的形状已经逼近装置的极限，很可能对系统造成损坏，如果不是AI给的信心，我们可能不会冒这个险。”</p> 
<p>这个AI是在模拟器<a class="project-link" data-id="3969191" data-name="中通" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969191" target="_blank">中通</a>过反复试验来训练的。</p> 
<p>在核聚变研究中，模拟器非常有必要，因为目前运行的反应堆一次只能维持等离子体最多几秒钟，之后需要时间来重置。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/20220217/v2_a91dc9665edc46a296ca2fd2de7d1f4c_img_000" referrerpolicy="no-referrer"></p> 
<p>不过一个问题是：该模拟器并没有准确捕获真实托卡马克中存在的所有变量，能迁移到真正的托卡马克上吗？</p> 
<p>对此，DeepMind研究员表示，通过用随机数表示足够训练出一个灵活的AI。</p> 
<p>另一个问题是：为了保持对托卡马克内部等离子体的控制，控制算法必须能够做出极快的决定，在短短几秒钟内对磁场进行调整。但许多人工智能系统在如此高速的环境下需要很长时间才能做出预测。</p> 
<p>为此，该团队先训<a class="project-link" data-id="633086" data-name="练了" data-logo="https://img.36krcdn.com/20210814/v2_629e80f4761842a0a85efd53a2ec3783_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/633086" target="_blank">练了</a>一个大型神经网络，它可以对磁场的变化如何塑造等离子体进行长程预测（longer-term prediction）。</p> 
<p>然后用这个网络来训练一个远小得多的系统，学习执行第一个网络所推荐的决策的最佳方法。</p> 
<p>这个较小的网络能与托卡马克控制系统直接交互，在不到50微秒（50百万分之一秒）的时间内做出决定。</p> 
<p>最后，作者表示，虽然这个成果意义非凡，但只是朝着人类实现可控核聚变迈出了一小步。</p> 
<p>比如实现一秒钟的实时运行需要模拟托卡马克数小时的时间，而它的条件每天都可能发生变化，算法还需各方面改进。</p> 
<p>此外，还要看现在这个系统能否转移到更大的托卡马克装置中。</p> 
<p>聚变能源何时实现商用还很难说，但DeepMind断言，人工智能可以加速这一过程。</p> 
<p>不知道它能否再次像AlphaFold一样，在核聚变领域实现惊艳全世界的新成果。</p> 
<p>拭目以待。</p> 
<p>（也有一些网友在担心，要是控制核聚变的AI哪天想不开……）</p> 
<h3 label="二级标题" style>论文地址</h3> 
<p>https://www.nature.com/articles/s41586-021-04301-9</p> 
<h3 label="二级标题" style>参考链接</h3> 
<p>[1]https://venturebeat.com/2022/02/16/deepmind-applies-ai-to-controlling-nuclear-fusion-reactors/</p> 
<p>[2]https://fortune.com/2022/02/16/deepmind-ai-nuclear-fusion-reactor-control/</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/GQZR1WkAkUhdNLHJM6nq5A">“量子位”（ID:QbitAI）</a>，作者：丰色，36氪经授权发布。</p>  
</div>
            