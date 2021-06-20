
---
title: '数据分析复盘报告，用Excel轻松搞掂！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qVLcdzRrJok6d96uNzJN.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 19 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qVLcdzRrJok6d96uNzJN.jpg'
---

<div>   
<blockquote><p>编辑导语：在项目运行流程中，数据分析是常见的业务流程。有效的数据分析可以分析原因及结果，给予方案策划等方面一定的指导。其中，复盘报告也需要利用数据分析手段。本篇文章里，作者总结了利用Excel来做好数据分析复盘报告的方法，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4730913 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qVLcdzRrJok6d96uNzJN.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家好，我是爱学习的小熊妹。才6月第一周，我的领导，作为大厂的得力基层领导，就迫不及待地让我开始写上半年复盘报告了，我真的是一口气差点上不来~</p>
<p>我们知道，做数据分析一般有3个场景：</p>
<ol>
<li>事前：策划类分析、预测类分析；</li>
<li>事中：监控类分析、原因类分析；</li>
<li>事后：总结性分析。</li>
</ol>
<p>到了6月份，有很多的半年总结、季度总结要做，618大促销的总结也要做。估计近期事后总结性分析报告（或者叫复盘报告）非常多，今天小熊妹就为大家整理了复盘报告的极简分析思路，帮助还在苦苦憋报告的小伙伴们早日脱离苦海哦。</p>
<p>复盘报告，有基本的写作思路：</p>
<ol>
<li>基本情况回顾；</li>
<li>整体完成情况；</li>
<li>优点/缺点总结；</li>
<li>未来发展建议。</li>
</ol>
<h2 id="toc-1">一、实例</h2>
<p>为了避免空谈，我们看一个具体例子。</p>
<p>小熊妹的公司做了一次用户拉新为目的的广告投放。运营小组的妹纸们找了16个渠道，投放了一条产品购买广告，希望能吸引<strong>新用户</strong>进行注册+购买。购买商品单价也很便宜，只要20元（单件商品成本8元）。</p>
<p>投放计划花费50000元成本，吸引6000名用户购买。投入产出不低于1:1.2（即花了1万元钱总成本，吸引的用户购买不能少于1.2万）。现在投放结束，数据如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/F9KpkAob7mXHiy3H17Ta.png" alt width="546" height="395" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（处于保密原因，所有数据已做修改，读者们多关注思路）</p>
<h2 id="toc-2">二、该如何复盘呢？</h2>
<p>很多小伙伴看到这么多数据，就感觉脑子嗡嗡的。简直不知道往哪里看了。遇到这种情况不要着急，记得复盘的第一件事：基本情况回顾<strong>。</strong>先把整个工作流程，投入/产出情况看明白。</p>
<p>因此，一上来，不用管具体数值，<strong>先搞清楚指标之间的关系，把投入和产出揪出来</strong>（如下图）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/1cH9UgkkBZ5sfDuhTqry.png" alt width="553" height="413" referrerpolicy="no-referrer"></p>
<p>这里投入和产出指标有好几个，要理清他们之间的关系：</p>
<ul>
<li>投入指标：总成本=曝光成本（要花钱买流量）+商品成本（用户买的产品+包邮，都要钱）</li>
<li>产出指标：付费总金额=付费人数*人均付费（这里人均付费就是20元商品钱）</li>
</ul>
<p>这次活动是用投放广告来吸引用户，广告平台按曝光量收费。用户看到曝光的广告以后，可以选择点击广告，进入落地页，进行注册，之后付费。整个流程如下图。</p>
<p>从这个流程里，可以看出，付费人数、和从曝光到付费的整个操作流程，有很大关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rEWXRlW9aV0BVrodzIr4.png" alt width="549" height="237" referrerpolicy="no-referrer"></p>
<p>这些基础指标梳理与流程梳理，是很重要的。如果没有梳理清楚，就会连数据含义都看不懂，自然是面对一大堆数字，脑袋瓜子嗡嗡嗡……</p>
<p>梳理完流程与指标以后，还是不要着急看细节。</p>
<p><strong>先看整体情况</strong>。</p>
<p>因此，要对各列数字用SUM函数求和，先看这次投放整体上，有没有达成目标。</p>
<ul>
<li>目标1：6000新用户；</li>
<li>目标2：投放成本50000以内；</li>
<li>目标3：投入产出比1：1.2以上。</li>
</ul>
<p>因此，可以先计算整体情况如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/P7rmLiiFKei8T7HEs43z.png" alt width="552" height="400" referrerpolicy="no-referrer"></p>
<p>对比目标，可以看到：</p>
<ul>
<li>目标1：6000新用户（<strong>未达标</strong>）；</li>
<li>目标2：投放成本50000以内（<strong>达标</strong>）；</li>
<li>目标3：投入产出比1:1.2以上（<strong>达标</strong>）。</li>
</ul>
<p>那么可以下结论了：本次投放<strong>未达成</strong>目标，新用户获取太少。</p>
<p>有了这个大结论，可以进一步看：</p>
<ul>
<li>为什么新用户获取的少？</li>
<li>有没有什么亮点？</li>
<li>下一步要改进什么？</li>
</ul>
<p>既然是未达成，那就直奔问题关键：<strong>哪个渠道做烂了</strong>，开始细节分析吧。</p>
<p>要分析哪个渠道做烂了，得先对渠道进行分类。</p>
<p>分类的规则，可以用投入产出比这个指标（表中第J列，A渠道的投入产出比即J2格，B渠道为J3格，以此类推）来制定。因为本次投放有明确的投入产出比要求：大于1.2。因此可制定规则如下：</p>
<ul>
<li>如果投入产出比小于1，则<strong>亏损；</strong></li>
<li>如果投入产出比大于1但小于1,2，则<strong>不合格；</strong></li>
<li>如果投入产出比大于1.2，则<strong>合格。</strong></li>
</ul>
<p>这样，就能把渠道区分开。</p>
<p>在Excel中，可以用if函数轻松实现按条件分类（如下图）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PvD4QCpUs3nJuZWDSAE9.png" alt width="546" height="292" referrerpolicy="no-referrer"></p>
<p>不仅可以做分类，找出明显做得烂的渠道，还能对投入产出情况做排序，找出最好/最差的3个渠道。<strong>用极端情况做对比，最容易发现问题</strong>。很多小伙伴就是栽倒在这里。没有用指端情况做对比，因此看不出来好坏。</p>
<p>在Excel中，可以用RANK函数，轻松实现排序（如下图）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dj00rc7zby3pGefC84xZ.png" alt width="547" height="262" referrerpolicy="no-referrer"></p>
<p>以上所有操作做完，找出了最好/最烂的三个渠道，结果如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/jn0RMmApw0wVEFegB6J2.png" alt width="550" height="339" referrerpolicy="no-referrer"></p>
<p>此时可以回答问题三：</p>
<ul>
<li>亮点：H、I、J三个渠道；</li>
<li>缺点：A、B、C三个渠道。</li>
</ul>
<p>因为我们手上有过程数据，可以<strong>结合转化过程，进一步分析，为啥ABC很烂。</strong>在广告转化中，每个环节都有一些很常见的问题（如下图）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7ODF96yUkWFiHepnsoKM.png" alt width="548" height="216" referrerpolicy="no-referrer"></p>
<p>具体区分出来是哪个问题很难，因为这些因素常常叠加在一起，要很复杂的分析方法才能区分出来。但发现哪个环节有问题，还是相对容易的。</p>
<p>利用过程转化率数据，外加曝光量与单位曝光成本（每个曝光花多少钱买，这是常见的广告采买形式），可以轻松看到问题环节（如下图）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rTyOs2qpc5A7Utsg5SR3.png" alt width="550" height="255" referrerpolicy="no-referrer"></p>
<p>很明显：</p>
<ul>
<li>A、B渠道曝光看起来很高，单价也很便宜，但是到落地页转化很差。很有可能做投放的小伙伴<strong>贪便宜</strong>，高估了这些渠道的转化率。</li>
<li>C、D渠道单位成本并不便宜，但是转化率依然不佳。</li>
<li>H、I、J渠道虽然曝光少，但转化率特别高，属于：粉丝聚集的小众垂直渠道。这种渠道自然转化率高。</li>
</ul>
<p>基于这些判断，可以推导出一些初步结论：</p>
<ol>
<li>A、B渠道太烂，可以直接放弃；</li>
<li>C、D渠道可以再尝试一次，但是如果仍表现不佳就放弃；</li>
<li>多开发像H、I、J的优质渠道注意。</li>
</ol>
<p>综合以上三点，还能推导一个<strong>隐藏结论。</strong></p>
<p>为什么做推广的小伙伴，要选择A、B渠道呢？他们真的不知道这两个渠道很烂吗？</p>
<p>不一定！注意，这些渠道平均价格在1元1个曝光左右，这次的预算有50000，也就是大概要买50000个曝光。如果都选择H、I、J这种1500左右的小渠道，50000/1500=33个！做推广的小伙伴得多一倍的工作量。</p>
<p>很有可能和各种渠道谈判谈到最后，已经筋疲力尽的小伙伴选择了：管他呢，来两发大的试试。结果就试成这样了。</p>
<p>哈哈，只希望他们能吃一堑长一智，多努力咯。以上就是复盘报告的基本思路，供大家参考哦。</p>
<p> </p>
<p>作者：码工小熊，微信公众号：码工小熊</p>
<p>本文由 @码工小熊 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4723516" data-author="1285820" data-avatar="https://static.woshipm.com/APP_U_202106_20210620005424_1343.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            