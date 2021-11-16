
---
title: '私钥失窃：慧与证实Aruba Networks客户数据泄露事件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1116/9d63e82dbd7f779.png'
author: cnBeta
comments: false
date: Tue, 16 Nov 2021 02:20:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1116/9d63e82dbd7f779.png'
---

<div>   
作为慧与（HPE）的一家网络设备制造子公司，Aruba Networks 于早些时候发生了数据泄露事件。<strong>这家企业技术巨头在一份声明中称，未经授权者利用一把私钥，访问了存储于 Aruba Central 云端的客户数据。</strong>尽管未详细说明黑客是如何获取到私钥的，但 HPE 确认它可被用于访问存储客户数据的多个地区的云服务器。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1116/9d63e82dbd7f779.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Aruba Networks <a href="https://www.arubanetworks.com/support-services/security-bulletins/central-incident-faq/" target="_self">官网</a>）</p><p>据悉，HPE 于 2015 年以 30 亿美元现金收购了 Aruba Networks，后者主要经营为企业提供网络设备（如无线接入点 / 网络安全等）。此外通过 Aruba Central 仪表板，企业可方便、集中监控和管理其 Wi-Fi 网络。</p><p>至于本次事件，HPE 声称在 Aruba Central 中收集的 Wi-Fi 数据遭到了泄露。在公开的两个数据集中，其中一份涉及客户 Wi-Fi 网络的设备信息，另一份则包含网络上有关设备的位置数据。</p><p>HPE 没有进一步披露位数数据的细粒度，但指出攻击者可借此推测大致的附近区域。通常情况下，这包括设备 MAC / IP 地址、主机名、操作系统，以及某些情况下的 Wi-Fi 网络名称。</p><p>HPE 表示 Wi-Fi 网络名称支持用户自定义，但也可能涵盖了用户名 / 电子邮件地址。更糟糕的是，尽管数据经过了加扰 / 加密，但攻击者仅凭 Aruba Networks 的私钥就有权解密。</p><p>庆幸的是，虽然目前尚不清楚数据是否最终被解密，但就算有，泄露的数据量还是相当有限的。此外由于 HPE 不会保留个人文件的访问日志，所以一时无法精确辨别哪些特定客户的哪些文件被泄露。</p><p>此外一份声明称黑客于 10 月 9 日首次使用了涉案密钥，但 HPE 直到 11 月 2 日才检测到入侵事件。不过由于云服务器会每隔 30 天清除相关数据，因此失窃数据的记录也只能追溯到 9 月 10 日。</p><p>最后，HPE 表示其正在向客户通报这一事件。</p>   
</div>
            