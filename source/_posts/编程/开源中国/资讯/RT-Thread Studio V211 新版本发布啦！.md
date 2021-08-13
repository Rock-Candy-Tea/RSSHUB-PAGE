
---
title: 'RT-Thread Studio V2.1.1 新版本发布啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/daa9961d-95ca-4b02-a89e-382ff7593078.png'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 14:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/daa9961d-95ca-4b02-a89e-382ff7593078.png'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://oscimg.oschina.net/oscnet/daa9961d-95ca-4b02-a89e-382ff7593078.png" referrerpolicy="no-referrer"></p> 
<p>二十四节气的大暑已悄然而过，气温日渐攀升，窗外灿烂的阳光下，响起此起彼伏清脆的知鸟声，仿佛在向大家宣告，盛夏来临啦！此时东京奥运会上的的奥运健儿们正在赛场上向着更高，更快，更强的目标拼搏着，RT-Thread Studio V2.1.1 新版本也已就绪，准备和大家见面了! 本次发布主要更新和上线了一些SDK资源包，其中包括重磅的RT-Thread nano-3.1.5源码包，将在本次更新版Studio中上线，此外本次更新集中完善优化了V2.0.0发布以来大家反馈的大部分问题，并在软件异常信息智能分析和提示方面做了大的改善，实现在软件发生报错的时候，能够智能分析，进行友好的日志补充输出，或弹框信息提示，指引大家快速定位解决问题，让软件的使用体验得到提升。希望在炎炎的夏日，Studio V2.1.1更新版能给大家带来一丝清凉。同时也祝奥运健儿们在东京奥运会取得一个又一个的佳绩。</p> 
<p><strong>下面我们一起来看看V2.1.1更新版本重要的改变:</strong></p> 
<p>1、新资源包上线</p> 
<ul> 
 <li> <p>上线 RT-Thread nano-3.1.5 源码包，支持通过 nano v3.1.5 创建工程</p> </li> 
 <li> <p>上线 pyocd-0.1.2 调试软件包，新增对东软芯片的支持</p> </li> 
 <li> <p>上线 jlink-6.8d2 调试软件包，新增对华芯微特 swm320 芯片的支持</p> </li> 
 <li> <p>上线 7 个新的ST开发板资源包</p> </li> 
</ul> 
<p><img src="https://oscimg.oschina.net/oscnet/fd1e2a8c-169b-411c-b64b-0ba766757989.png" referrerpolicy="no-referrer"></p> 
<p>2、异常日志智能分析提示</p> 
<p>在使用Studio过程中，一些异常日志输出信息过于术语化，造成理解困难，看不出问题在哪里，为此Studio新增了异常日志智能分析功能，能够识别绝大多数先前异常问题，并且在原有异常日志输出基础上，额外以显眼的红色输出智能分析后的友好提示信息，指引用户识别和解决相应问题。大家后面遇到异常时，可以留心一下新的控制台日志输出或弹框提示。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/c1e0ede5-edf0-4b0f-b51a-2f8e8d8250fa.png" referrerpolicy="no-referrer"></p> 
<p>3、新增每日小技巧提示功能</p> 
<p>每日小技巧提示里汇集了大家可能还不知道的一些使用技巧，以及大家平时使用Studio可能会遇到的问题的提示和解决方法，在使用过程中遇到问题除了仔细观察一下日志输出提示外，还可以尝试翻翻每日小技巧，看看是否有你遇到的问题，如果问题还解决不了可以再去论坛发帖寻求支持和帮助。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/84956602-ae42-451e-a10e-7edaff7b3589.png" referrerpolicy="no-referrer"></p> 
<p>4、功能优化</p> 
<p>Studio保持跟进社区用户的体验和反馈，对于一些大家常用的功能，在保持持续地优化。本次优化有十几处，下面挑几个重要讲一讲，其它的点希望大家升级后亲自体验和发现。</p> 
<ul> 
 <li> <p><strong>STM32CubeMX 协同开发优化</strong></p> <p>在上个版本的基础上，优化了打开 CubeMX Settings 后无任何修改的情况下修改工程信息的问题，防止了大家误触 CubeMX Settings 可能产生的异常；在打开 CubeMX Settings 的情况下，也支持操作 Studio 其他窗口；对于少数情况没有打开正确的芯片型号的问题，也得到了完美的解决。</p> </li> 
 <li> <p><strong>MDK 协同开发优化</strong></p> <p>提升了导入 MDK 工程的速度和解决MDK工程使用dap-link调试异常的问题</p> </li> 
 <li> <p><strong>QEMU 终端支持历史命令</strong></p> <p>贴近开发者的使用习惯是 RT-Thread Studio 一直在努力的方向，喜欢使用 QEMU 的开发者也可以想在普通终端中一样使用上下键来切换历史命令啦。</p> </li> 
</ul> 
<p>软件体验优化提升是个漫长而无止境的路，未来Studio仍然会持续在功能性，易用性，资源占用，速度性能，稳定性等方面持续优化完善。</p> 
<p>Stduio V2.1.1新版本的更多功能细节的优化和完善，大家也可通过查看本次更新 <strong>ChangeLog：</strong></p> 
<p>https://docs.rt-thread.org/#/development-tools/rtthread-studio/changelog/changelog</p> 
<p>已经安装过Studio的，打开Studio就可自动检测并升级到V2.1.1版本，没有安装的可以到如下地址(https://www.rt-thread.org/page/download.html#studio)下载安装V2.1.1完整安装包(建议不要覆盖安装)。</p> 
<p>大家都来亲自动手体验一下吧，如果遇到什么问题需要协助，或有什么建议和意见需要反馈的，可以加入studio交流2群(941959043)或者登录论坛的板块( https://club.rt-thread.org/ask/tag/59.html )发帖反馈。</p> 
<p>最后感谢大家地持续使用和关注，期待大家将Studio分享给更多的人，同时也期待收到大家更多宝贵的反馈和建议。</p>
                                        </div>
                                      
</div>
            