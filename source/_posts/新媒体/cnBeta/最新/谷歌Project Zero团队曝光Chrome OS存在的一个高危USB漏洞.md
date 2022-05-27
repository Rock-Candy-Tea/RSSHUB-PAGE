
---
title: '谷歌Project Zero团队曝光Chrome OS存在的一个高危USB漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0527/4999dff5e0bd1dc.webp'
author: cnBeta
comments: false
date: Fri, 27 May 2022 08:34:30 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0527/4999dff5e0bd1dc.webp'
---

<div>   
谷歌 Project Zero 团队擅长发现不同产品中的安全漏洞（涵盖 Windows 操作系统、iPhone 智能机、高通 Adreno GPU、GitHub 代码托管平台），然后及时向供应商进行汇报、并赋予其标准的 90 天补丁修复宽限期。<strong>不过近日，Project Zero 研究人员也披露了自家 Chrome OS 系统中存在的一个高危 USB 漏洞。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0527/4999dff5e0bd1dc.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p>Jann Horn 在<a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2264&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids" target="_self">报告</a>中写道，问题源于 Chrome OS 在设备锁定时的 USB 设备应对策略。</p><p>尽管该系统会通过 USBGuard 为 USB 设备配置黑 / 白名单（允许 / 阻止列表），但错误的配置框架可能导致未经身份验证的 USB 设备访问计算机的内核与存储。</p><p>具体说来是，USBGuard 阻止列表不会在锁屏上使用特定的类接口描述符，对 USB 设备进行身份验证。</p><p>但若攻击者修改了内核，将相关设备伪装成大容量存储设备，便可在通过身份验证后突破限制。</p><p>原因是内核觉得 USB 类有些无关紧要，并允许从看似经过身份验证的设备进行修改。</p><p><img src="https://static.cnbetacdn.com/article/2022/0527/c9cfee13061cf59.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>除了不属于这些 USB 接口类的设备驱动程序中存在较大的攻击面，系统内核通常也不关心设备自诩属于哪种 USB 类型。</p><p>作为一个被广泛使用的标准化协议，驱动程序既能够以低优先级指定其希望使用的适当 USB 接口类（绑定到符合标准的设备），也能够以高优先级来参考制造商 / 产品 ID 来绑定（而不关心其 USB 接口类别）。</p><p>如果利用具有适当硬件的 Linux 机器 —— 本例中选择了 NET2380 开发板，但你也可使用解锁的 Pixel 智能机 / 树莓派 Zero W 等类似设备 —— 来模拟 USB 大容量存储设备。</p><p>接着使用（<a href="https://docs.kernel.org/usb/mass-storage.htm" target="_self">这个</a>）并在攻击者内核中修补一行，便可随它自诩为何（而不被视作存储设备）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0527/4128096954baabc.png" alt="2.png" referrerpolicy="no-referrer"></p><p>Project Zero 将该问题标记为高严重性漏洞，并于 2 月 24 日私信给了 Chrome OS 团队。</p><p>尴尬的是，后来 Chrome OS 团队又将该问题视作低严重性漏洞，并于 3 月 1 日辩称会通过基于驱动程序的适当匹配来解决该问题（而不是类接口描述符）。</p><p>尽管 Chrome OS 团队于 5 月 11 日通报了进度更新，但由于其未能在规定的 90 天内修复该漏洞，Project Zero 安全研究人员最终决定于 5 月 24 日将其公开曝光。</p><p>目前尚不清楚正式的 Chrome OS 补丁将于何时推出，庆幸的是，作为一个本地漏洞，攻击者需要手动连接 USB 来篡改设备及其内核，而无法被远程利用。</p><p>换言之，只有你将 Chrome OS PC 放在无人看管的地方，那即使它被锁定，才可能沦为其它攻击的一个跳板。</p>   
</div>
            