
---
title: '微软将 Linux XDP 项目引入 Windows，带来高性能网络'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/b5f5a74c-1176-41ec-976e-53778e660881.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE3MS5wbmc=,g_3,x_17,y_17,a_0,t_100'
author: IT 之家
comments: false
date: Wed, 25 May 2022 07:05:40 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/b5f5a74c-1176-41ec-976e-53778e660881.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE3MS5wbmc=,g_3,x_17,y_17,a_0,t_100'
---

<div>   
<p data-vmark="1c4b"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 25 日消息，Linux 有一个名为 <span class="accentTextColor">eXpress Data Path</span> (XDP) 的高性能网络项目，自 4.8 版以来一直是 Linux 内核的一部分。包括谷歌、亚马逊和英特尔在内的多家大型科技公司都参与了这个项目，XDP 允许应用在网络中实现<span class="accentTextColor">低延迟和高吞吐量</span>。</p><p data-vmark="1275">在 Build 2022 开发者大会上，微软宣布在 GitHub 推出基于 XDP 的开源项目“<span class="accentTextColor">XDP for Windows</span>”，采用 MIT 许可证。微软称这是其对 XDP 社区的首次贡献，并使 XDP 真正得到跨平台体验。</p><p style="text-align: center;" data-vmark="a7d3"><img src="https://img.ithome.com/newsuploadfiles/2022/5/b5f5a74c-1176-41ec-976e-53778e660881.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE3MS5wbmc=,g_3,x_17,y_17,a_0,t_100" w="1112" h="672" title="微软将 Linux XDP 项目引入 Windows，带来高性能网络" width="1112" height="496" referrerpolicy="no-referrer"></p><p data-vmark="7e90">据介绍，XDP for Windows 包含一个网络驱动程序和一个占位符用户模式 API。使用 AF_XDP 用户模式接口的应用程序可以将数据包直接传递到 Windows XDP 驱动程序和 NDIS 或直接传递到兼容的网卡驱动程序，从而避免通过 TCP / IP 堆栈的开销。</p><p style="text-align: center;" data-vmark="6ba6"><img src="https://img.ithome.com/newsuploadfiles/2022/5/a12469db-131e-4ddc-9e4d-61a0bc2e5479.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzIyMi5wbmc=,g_3,x_22,y_22,a_0,t_100" w="1440" h="583" title="微软将 Linux XDP 项目引入 Windows，带来高性能网络" width="1440" height="332" referrerpolicy="no-referrer"></p><p data-vmark="68e8">IT之家了解到，<span class="accentTextColor">XDP for Windows 仍在开发中</span>，微软希望在开发过程的早期将其开源，以获得 XDP 社区的反馈。当前形式的 XDP for Windows 已准备好进行测试和原型设计。</p><p data-vmark="b6e8">不过需要注意的是，XDP 并不适用于所有硬件，目前仅支持少数网卡 (NIC) 和驱动程序。</p><p data-vmark="e5f3"><strong>XDP for Windows：</strong><a href="https://github.com/microsoft/xdp-for-windows/" target="_blank">点此查看 GitHub 页面</a></p>
          
</div>
            