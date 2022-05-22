
---
title: '1 核有难 15 核围观？专业人士反馈微软 Win11 CPU 占用率读数不正确，尤其是 AMD'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/1bbc1d29-4297-4e15-a5b1-e608a06d2956.jpg@s_2,w_820,h_553'
author: IT 之家
comments: false
date: Sat, 21 May 2022 23:35:39 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/1bbc1d29-4297-4e15-a5b1-e608a06d2956.jpg@s_2,w_820,h_553'
---

<div>   
<p data-vmark="66c5"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 22 日消息，虽然不会在玩游戏的时候主动观察硬件资源的占用情况，但也有一些极客和评测者会注重这些数据。</p><p data-vmark="6d6e">在测试过程中，开发者 CapFrameX 发现微软对于 AMD Ryzen 7 5800X3D 的支持不完善，例如他在《古墓丽影: 暗影》(SotTR) 中遇到了一个奇怪的异常。</p><p data-vmark="75b3">在游戏的一个场景中，Win11 显示的 CPU 占用率异常之低，16 个线程中只有一个线程显示了正确的使用情况，而其他所有线程的利用率都低于 10%。</p><p data-vmark="ee1a">CapFrameX 虽然有注意到这个问题，但他也不确定是什么原因造成的：</p><blockquote><p data-vmark="45b7">Windows 11 的核心使用报告完全被破坏了。对于 SotTR + 这个特定的场景和设置，应该是 > 80%。</p><p data-vmark="849d">发生什么事了？？最近的更新是否改变了计时器的行为?</p></blockquote><p data-vmark="133d">从截图中可以看到，CapFrameX 使用了自己的工具在游戏内进行了监测，旁边还有 HWiNFO 的数据。在屏幕上显示的 数值表明，5800X3D 有一个核心达到了 77.9% 的占用率，而其他几乎清一色的个位数。</p><p style="text-align: center;" data-vmark="0b26"><img src="https://img.ithome.com/newsuploadfiles/2022/5/1bbc1d29-4297-4e15-a5b1-e608a06d2956.jpg@s_2,w_820,h_553" w="1440" h="971" title="1 核有难 15 核围观？专业人士反馈微软 Win11 CPU 占用率读数不正确，尤其是 AMD" srcset="https://img.ithome.com/newsuploadfiles/2022/5/1bbc1d29-4297-4e15-a5b1-e608a06d2956.jpg 2x" width="1440" height="553" referrerpolicy="no-referrer"></p><p data-vmark="5e6c">虽然这一 Bug 可能是特定于某一种甚至某一个应用程序的问题，但 CapFrameX 坚持认为它在所有被测试的游戏中都存在：</p><p style="text-align: center;" data-vmark="bda4"><img src="https://img.ithome.com/newsuploadfiles/2022/5/e74ecfd1-8a49-4890-8e43-70a5d9a2fa10.png" w="594" h="734" title="1 核有难 15 核围观？专业人士反馈微软 Win11 CPU 占用率读数不正确，尤其是 AMD" width="594" height="734" referrerpolicy="no-referrer"></p><p data-vmark="5f40">值得一提的是，CapFrameX 和 HWiNFO 也基于 Windows 事件跟踪 (ETW) 的机制运行。因此，他认为是 ETW 中可能存在的某种 Bug 导致了这种错误读数。</p><p data-vmark="0d8f">除此之外，我们还在 Microsoft 论坛上找到了另一个帖子，用户“@AndreasRes 也反馈了一个相似的问题。在这种情况下，我们可以看到 Win11 中性能监测工具或任务管理器的 CPU 占用率非常高，乃至于一度达到 100%，而未基于 ETW 的工具（如 Xbox Game Bar 和主板自带的 MSI Dragon Center）使用率则正常得多。</p><p data-vmark="7f93"><img src="https://img.ithome.com/newsuploadfiles/2022/5/278112f4-d2cc-4f81-b83a-8a176b7204ea.jpg" w="760" h="622" alt="CPU使用错误Windows 11" title="1 核有难 15 核围观？专业人士反馈微软 Win11 CPU 占用率读数不正确，尤其是 AMD" width="760" height="622" referrerpolicy="no-referrer"></p><p data-vmark="14de">值得一提的是， CapFrameX 是在最新的 Windows 11 Beta Channel build 22621 上进行的测试，不出意外这就是即将到来的 22H2 版本。</p><p data-vmark="67aa"><img src="https://img.ithome.com/newsuploadfiles/2022/5/d339f00e-2c90-4707-a011-5204ed3a6e40.jpg" w="575" h="520" alt="出现低 CPU 使用率错误的 Windows 11 版本" title="1 核有难 15 核围观？专业人士反馈微软 Win11 CPU 占用率读数不正确，尤其是 AMD" width="575" height="520" referrerpolicy="no-referrer"></p>
          
</div>
            