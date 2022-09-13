
---
title: '胡渊鸣：import一个_太极_库 让Python代码提速100倍！'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220913/708991af-a39a-43c7-8d10-e6593d411b56.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 13 Sep 2022 19:55:52 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220913/708991af-a39a-43c7-8d10-e6593d411b56.png'
---

<div>   
<p>众所周知，Python的简单和易读性是靠牺牲性能为代价的——</p>
<p>尤其是在计算密集的情况下，比如多重for循环。</p>
<p>不过现在，大佬胡渊鸣说了：</p>
<p>只需import 一个叫做“Taichi”的库，就可以把代码速度提升100倍！</p>
<p style="text-align: center"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="460" src="https://img1.mydrivers.com/img/20220913/708991af-a39a-43c7-8d10-e6593d411b56.png" style="border: black 1px solid" w="460" referrerpolicy="no-referrer"></p>
<p>不信？</p>
<p>来看三个例子。</p>
<p>计算素数的个数，速度x120</p>
<p>第一个例子非常非常简单，求所有小于给定正整数N的素数。</p>
<p>标准答案如下：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/a301869f-ec93-46f0-b091-b9d2a8eee67d.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="425" src="https://img1.mydrivers.com/img/20220913/Sa301869f-ec93-46f0-b091-b9d2a8eee67d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>我们将上面的代码保存，运行。</p>
<p>当N为100万时，需要2.235s得到结果：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/2d7d7d5d-d1fc-48dc-ba2f-f3a8b293e18d.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="126" src="https://img1.mydrivers.com/img/20220913/S2d7d7d5d-d1fc-48dc-ba2f-f3a8b293e18d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>现在，我们开始施魔法。</p>
<p>不用更改任何函数体，import“taichi”库，然后再加两个装饰器：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/4d0a5086-9637-4ac6-87bc-ebdf8c205282.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="466" src="https://img1.mydrivers.com/img/20220913/S4d0a5086-9637-4ac6-87bc-ebdf8c205282.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>Bingo！同样的结果只要0.363s，快了将近6倍。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/faaeb779-507b-4eb7-b2c5-73adbbe76b05.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="121" src="https://img1.mydrivers.com/img/20220913/Sfaaeb779-507b-4eb7-b2c5-73adbbe76b05.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果N=1000万，则只要0.8s；要知道，不加它可是55s，一下子又快了70倍！</p>
<p>不止如此，我们还可以在ti.init()中加个参数变为ti.init(arch=ti.gpu) ，让taich在GPU上进行计算。</p>
<p>那么此时，计算所有小于1000万的素数就只耗时0.45s了，与原来的Python代码相比速度就提高了120倍！</p>
<p>厉不厉害？</p>
<p>什么？你觉得这个例子太简单了，说服力不够？我们再来看一个稍微复杂一点的。</p>
<p>动态规划，速度x500</p>
<p>动态规划不用多说，作为一种优化算法，通过动态存储中间计算结果来减少计算时间。</p>
<p>我们以经典教材《算法导论》中的经典动态规划案例“最长公共子序列问题（LCS）”为例。</p>
<p>比如对于序列a = [0, 1, 0, 2, 4, 3, 1, 2, 1]和序列b = [4, 0, 1, 4, 5, 3, 1, 2]，它们的LCS就是：</p>
<p>LCS(a, b) = [0, 1, 4, 3, 1, 2]。</p>
<p>用动态规划的思路计算LCS，就是先求解序列a的前i个元素和序列b的前j个元素的最长公共子序列的长度，然后逐步增加i或j的值，重复过程，得到结果。</p>
<p>我们用f[i, j]来指代这个子序列的长度，即LCS((prefix(a, i), prefix(b, j)。其中prefix(a, i) 表示序列a的前i个元素，即a[0], a[1], …, a[i - 1]，得到如下递归关系：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/933e3272-9dd0-4e62-8775-4b489dc1db71.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="58" src="https://img1.mydrivers.com/img/20220913/S933e3272-9dd0-4e62-8775-4b489dc1db71.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>完整代码如下：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/bdab30ba-9c47-4d3f-bb54-2d4f4539fcef.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="99" src="https://img1.mydrivers.com/img/20220913/Sbdab30ba-9c47-4d3f-bb54-2d4f4539fcef.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>现在，我们用Taichi来加速：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/368b4050-768e-4e5d-8f3e-efea0d632dce.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="660" src="https://img1.mydrivers.com/img/20220913/S368b4050-768e-4e5d-8f3e-efea0d632dce.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>结果如下：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/f4d12027-d3c0-4263-b0bf-7664bbafb93f.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="122" src="https://img1.mydrivers.com/img/20220913/Sf4d12027-d3c0-4263-b0bf-7664bbafb93f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>胡渊鸣电脑上的程序最快做到了0.9秒内完成，而换成用NumPy来实现，则需要476秒，差异达到了超500倍！</p>
<p>最后，我们再来一个不一样的例子。</p>
<p>反应 - 扩散方程，效果惊人</p>
<p>自然界中，总有一些动物身上长着一些看起来无序但实则并非完全随机的花纹。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/56b44a70-13d9-462a-b38c-17e8f2158e98.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="111" src="https://img1.mydrivers.com/img/20220913/S56b44a70-13d9-462a-b38c-17e8f2158e98.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>图灵机的发明者艾伦·图灵是第一个提出模型来描述这种现象的人。</p>
<p>在该模型中，两种化学物质（U和V）来模拟图案的生成。这两者之间的关系类似于猎物和捕食者，它们自行移动并有交互：</p>
<p>最初，U和V随机分布在一个域上；</p>
<p>在每个时间步，它们逐渐扩散到邻近空间；</p>
<p>当U和V相遇时，一部分U被V吞噬。因此，V的浓度增加；</p>
<p>为了避免U被V根除，我们在每个时间步添加一定百分比 (f) 的U并删除一定百分比 (k) 的V。</p>
<p>上面这个过程被概述为“反应-扩散方程”：</p>
<p style="text-align: center"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="145" src="https://img1.mydrivers.com/img/20220913/4bc58c03-a41a-4d35-ae67-4f1737f6b311.png" style="border: black 1px solid" w="366" referrerpolicy="no-referrer"></p>
<p>其中有四个关键参数：Du（U的扩散速度），Dv（V的扩散速度），f（feed的缩写，控制U的加入）和k（kill的缩写，控制V的去除）。</p>
<p>如果Taichi中实现这个方程，首先创建网格来表示域，用vec2表示每个网格中U, V的浓度值。</p>
<p>拉普拉斯算子数值的计算需要访问相邻网格。为了避免在同一循环中更新和读取数据，我们应该创建两个形状相同的网格W x H×2。</p>
<p>每次从一个网格访问数据时，我们将更新的数据写入另一个网格，然后切换下一个网格。那么数据结构设计就是这样：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/e206f0da-31c7-47e9-8014-9af78334bedd.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="57" src="https://img1.mydrivers.com/img/20220913/Se206f0da-31c7-47e9-8014-9af78334bedd.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>一开始，我们将U在网格中的浓度设置为 1，并将V放置在50个随机选择的位置：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/cc880a8e-61f6-4eb4-bcf1-e76d81882959.png" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="178" src="https://img1.mydrivers.com/img/20220913/Scc880a8e-61f6-4eb4-bcf1-e76d81882959.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>那么实际计算就可以用不到10行代码完成：</p>
<p>@ti.kerneldef compute(phase: int):    for i, j in ti.ndrange(W, H):        cen = uv[phase, i, j]        lapl = uv[phase, i + 1, j] + uv[phase, i, j + 1] + uv[phase, i - 1, j] + uv[phase, i, j - 1] - 4.0 * cen        du = Du * lapl[0] - cen[0] * cen[1] * cen[1] + feed * (1 - cen[0])        dv = Dv * lapl[1] + cen[0] * cen[1] * cen[1] - (feed + kill) * cen[1]        val = cen + 0.5 * tm.vec2(du, dv)        uv[1 - phase, i, j] = val在这里，我们使用整数相位（0或1）来控制我们从哪个网格读取数据。</p>
<p>最后一步就是根据V的浓度对结果进行染色，就可以得到这样一个效果惊人的图案：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220913/d911fa75-7052-41e6-ad17-e0dec1a63d92.jpg" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="267" src="https://img1.mydrivers.com/img/20220913/Sd911fa75-7052-41e6-ad17-e0dec1a63d92.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>有趣的是，胡渊鸣介绍，即使V的初始浓度是随机设置的，但每次都可以得到相似的结果。</p>
<p>而且和只能达到30fps左右的Numba实现比起来，Taichi实现由于可以选择GPU作为后端，轻松超过了 300fps。</p>
<p>pip install即可安装</p>
<p>看完上面三个例子，你这下相信了吧？</p>
<p>其实，Taichi就是一个嵌入在Python中的DSL（动态脚本语言），它通过自己的编译器将被 @ti.kernel 装饰的函数编译到各种硬件上，包括CPU和GPU，然后进行高性能计算。</p>
<p>有了它，你无需再羡慕C++/CUDA的性能。</p>
<p>正如其名，Taichi就出自太极图形胡渊鸣的团队，现在你只需要用pip install就能安装这个库，并与其他Python库进行交互，包括NumPy、Matplotlib和PyTorch等等。</p>
<p>当然，Taichi用起来和这些库以及其他加速方法有什么差别，胡渊鸣也给出了详细的优缺点对比，感兴趣的朋友可以戳下面的链接详细查看：</p>
<p><a class="f14_link" href="https://docs.taichi-lang.org/blog/accelerate-python-code-100x" target="_blank">https://docs.taichi-lang.org/blog/accelerate-python-code-100x</a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220913/b15d2b927624457680ec950d2df5862d.jpg" target="_blank"><img alt="胡渊鸣：import一个“太极”库 让Python代码提速100倍！" h="400" src="https://img1.mydrivers.com/img/20220913/s_b15d2b927624457680ec950d2df5862d.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
             
          <p class="url"><span style="color:#666">责任编辑：若风</span></p>
        </div>
     
        
</div>
            