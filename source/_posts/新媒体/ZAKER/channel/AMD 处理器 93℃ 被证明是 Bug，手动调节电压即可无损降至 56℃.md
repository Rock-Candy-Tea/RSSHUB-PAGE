
---
title: 'AMD 处理器 93℃ 被证明是 Bug，手动调节电压即可无损降至 56℃'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb7_1024.jpg'
author: ZAKER
comments: false
date: Thu, 01 Sep 2022 22:33:35 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb7_1024.jpg'
---

<div>   
<p>IT 之家 9 月 2 日消息，AMD 刚刚发布了 Ryzen 7000 系列 "Zen 4" 处理器，基于台积电 5nm 打造，可提供最多 16 个内核、5.7 GHz 加速频率，IPC 提升 13%，但实际上 IPC 只是性能提升的一小部分，更多的性能优势则来自超高主频和 TDP，新品将于 9 月 27 日上市，299 美元起。</p><p>据介绍，16 核的 AMD Ryzen 9 7950X 处理器在 V-Ray Render 中可提供比竞品高出 57% 的媒体性能，而即便是 6 核的 AMD Ryzen 5 7600X 处理器也有着比竞争对手的旗舰游戏处理器快 5% 的性能。</p><p>此外，AMD 称 Ryzen 7950X 处理器的能效比竞争对手高出 47%。IT 之家提醒，上述数据参考对象是 12 代酷睿，但实际上英特尔 13 代酷睿同样也通过高主频和高功耗实现了大幅性能提升，单纯看下一代产品两者并没有太大差距。</p><p>AMD 新品发布后，有 UP 主发现，AMD Ryzen 7000 CPU 运行时会非常热，R9 7950X 在 230W 时达到了 95 摄氏度，Ryzen 5 7600X 在 120W 时也能达到 90 ℃以上。</p><p>不过他也强调这是基于 ES / QS 处理器得出的结论，因此最终结果可能会有所不同。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb7_1024.jpg" data-height="430" data-width="610" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb7_1024.jpg" referrerpolicy="no-referrer"></div></div>现在有另一位数码爱好者给出了一组数据，表明上述 UP 主测试时使用的 ES / QS 处理器存在问题。<p></p><p>@Harukaze5719 给出了一组 AIDA64 数据，据称是来自 AMD Ryzen 5 7600X CPU。</p><p>第一个结果向我们展示了 ES 芯片运行频率为 5.05 GHz 的配置，此时它在 AIDA64 FPU 压力测试中温度达到了 93.1 ℃，功率为 122W。</p><p>但在第二个窗口中，我们可以看到手动调节 Vcore 后这颗 CPU 依然可以保持着 5.05GHz 的频率，而温度则直接砍半降低到 56.5 ℃，并且在不影响性能的同时将功率降至 68W，这一点与 AMD 官方给出的数据基本相同。</p><p>他认为，AMD Ryzen 7000 ES / QS 版本处理器中默认的电源或电压配置似乎存在错误，从而导致了如此高的温度，但要想解决这个问题倒也不难，不过要想达到更高频率仍需要设置为更高的电压。</p><p>他表示，只需要手动调节 CLK 即可获得非常合理的结果，并且还会有很多 CLK / temp 余量。目前距离这款处理器上市还有超过 3 周以上的时间，预计 AMD 能够在量产版中解决这个问题。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb8_1024.jpg" data-height="1020" data-width="599" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/631189488e9f094f394e7fb8_1024.jpg" referrerpolicy="no-referrer"></div></div>值得一提的是，该 UP 主尝试之后发现确实有效，遂主动道歉。<p></p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres2.myzaker.com/202209/631189488e9f094f394e7fb9_1024.jpg" data-height="301" data-width="907" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202209/631189488e9f094f394e7fb9_1024.jpg" referrerpolicy="no-referrer"></div></div>更多详情可参见 IT 之家此前报道。<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            