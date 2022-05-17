
---
title: '研究人员：苹果 iPhone 关机后仍在运行，_永远开机_或成恶意软件温床'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/719593c1-7f6b-46f3-b4ea-aff46cacea84.jpeg?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xZC9xZDE5NS5wbmc=,g_9,x_20,y_20,a_0,t_100'
author: IT 之家
comments: false
date: Tue, 17 May 2022 04:40:18 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/719593c1-7f6b-46f3-b4ea-aff46cacea84.jpeg?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xZC9xZDE5NS5wbmc=,g_9,x_20,y_20,a_0,t_100'
---

<div>   
<p data-vmark="6a94">5 月 17 日消息，苹果 <strong>iPhone 中的芯片在设备关机时会继续以低功耗模式（LPM）运行</strong>。日前有研究人员基于这一机制设计出一种恶意软件，<strong>在用户关闭 iPhone 时也能运行</strong>。虽然相应研究目前仍是理论性的，但暴露出苹果设备存在的安全问题。</p><p style="text-align: center;" data-vmark="f029"><img src="https://img.ithome.com/newsuploadfiles/2021/9/719593c1-7f6b-46f3-b4ea-aff46cacea84.jpeg?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xZC9xZDE5NS5wbmc=,g_9,x_20,y_20,a_0,t_100" alt="苹果iPhone 13 Pro Max" title="研究人员：苹果 iPhone 关机后仍在运行，“永远开机”或成恶意软件温床" referrerpolicy="no-referrer"></p><p data-vmark="06b4">当用户关闭 iPhone 时，实际上设备并没有完全关机，内置芯片会继续以低功耗模式运行，<strong>让用户可以使用“查找”功能定位丢失或被盗的设备</strong>，或者<strong>在电池电量耗尽后能继续使用苹果钱包和汽车钥匙</strong>。现在，研究人员利用这种“永远开机”机制来运行恶意软件，让恶意软件在 iPhone 关机的情况下保持运行状态。</p><p data-vmark="6a9d">iPhone 利用内置的蓝牙芯片在关机状态下继续实现“查找”等功能。但事实证明，<strong>这种芯片并没有数字签名机制，甚至不会对运行固件进行加密</strong>。德国达姆施塔特技术大学 (Technical University of Darmstadt) 的学者们设计了一种方法，利用这种缺乏加密的机制来运行恶意固件，<strong>使攻击者能够跟踪手机位置，或在手机关闭时运行恶意功能</strong>。</p><p data-vmark="c9a9">这项研究是研究人员首次研究芯片在低功耗模式下运行时所带来的安全风险。研究中所指的低功耗模式并非 iOS 系统中的低电量模式，而是指苹果设备中负责近场通信、超宽带和蓝牙的芯片会在设备关闭后保持低功耗运行，<strong>能持续 24 小时时间</strong>。</p><p data-vmark="40b0">研究人员在上周发表的一篇论文中写道：“目前苹果 iPhone 上的 LPM 模式运行机制并不透明，并增加了新的安全风险。”“由于 LPM 模式是基于 iPhone 硬件，所以无法通过系统更新来移除，因此对整个 iOS 安全机制有着长期影响。据我们所知，<strong>这是首次研究在 iOS 15 中引入未记录的 LPM 特性并发现各种问题</strong>。”</p><p data-vmark="35c4">研究人员补充说：“LPM 机制的设计似乎主要是从功能角度出发，并没有考虑预期应用程序之外的安全威胁。关机后查找功能会将用户手中的 iPhone 变成追踪设备，而蓝牙固件功能实现并不安全，可能会被恶意软件操纵或篡改。”</p><p data-vmark="b596">当然，研究人员的这些发现在现实世界中的价值有限。因为让恶意软件在关机下继续运行，<strong>首先需要让 iPhone 越狱</strong>，这本身就是一项艰巨的任务。尽管如此，iOS 15 系统中始终有功能运行的机制可能会被恶意软件利用，让不法分子能更方便监视用户。</p><p data-vmark="0b4b">此外，<strong>如果黑客从中发现易受无线攻击的安全漏洞</strong>，也有可能感染 iPhone 的内置芯片，类似于针对 Android 设备的相关漏洞。</p><p data-vmark="a6c0">除了允许恶意软件在 iPhone 关机状态下运行外，<strong>针对 LPM 机制的攻击也可以让恶意软件在后台隐秘运行</strong>，因为 LPM 机制本身能节省运行固件所需的电池电量。当然，检测固件是否感染恶意软件本身就不容易，需要大量的专业知识和昂贵设备。</p><p data-vmark="67a3">研究人员表示，苹果工程师在论文发表前审阅了论文，但公司代表从未对论文内容提供过任何反馈。</p><p data-vmark="1bae">研究表明，虽然苹果 iPhone 中的 LPM 机制能让用户在关机状态下定位丢失或被盗的设备，甚至在电池耗尽时也可以解锁或打开车门。但<strong>在安全方面是一把还没有被注意到的双刃剑</strong>。</p><p data-vmark="5710">固件安全公司 Eclypsium 负责策略的高级副总裁约翰・卢卡德斯（John Loucaide）表示：“与上述攻击相似的硬件和软件攻击已被证明是可行的，因此论文中涉及的研究主题及时且实用。”“这是所有设备的典型现象。制造商一直在增加新功能，每增加一个新功能，就会出现一个新的攻击角度。”</p>
          
</div>
            