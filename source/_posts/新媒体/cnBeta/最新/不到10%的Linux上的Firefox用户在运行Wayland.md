
---
title: '不到10%的Linux上的Firefox用户在运行Wayland'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/02/2fa5696520b8adb.jpg'
author: cnBeta
comments: false
date: Mon, 07 Feb 2022 09:05:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/02/2fa5696520b8adb.jpg'
---

<div>   
由于Mozilla的Telemetry功能，我们可以得知一些有趣的见解，即有多少Linux桌面用户仍然依赖X.Org（X11）服务器而没有Wayland。Jan
E.P.最近在思考Wayland在Linux桌面上的市场份额，并研究了Mozilla的遥测功能。<br>
 <p>虽然telemetry.mozilla.org没有显示显示服务器的分类，但它却跟踪了作为数据集一部分的使用中的显示服务器。</p><p>在他与Mozilla遥测团队联系后，后者很友好地生成了一张图表，显示了由这些公开收集的数据衡量的Firefox用户的X11与Wayland的使用情况。他们允许公开分享这些数据，但希望将这些重要的脚注传递给大家。</p><p>- Y轴从90%开始，以更好地显示不同的层次。</p><p>- 基于所有Firefox for Linux桌面遥测数据的1%的代表性样本。</p><p>- 一些发行版在构建Firefox时禁用了遥测功能，这可能会大大偏离结果。</p><p>- 长期的采用趋势在假期前后会消失（而且gfx.linux_window_protocol还没有被跟踪足够长的时间）。</p><p>- 除了X11，其他都是Wayland。</p><p><strong>具体图表如下：</strong></p><p><a href="https://static.cnbetacdn.com/article/2022/02/2fa5696520b8adb.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/02/2fa5696520b8adb.jpg" referrerpolicy="no-referrer"></a></p><p>在这几个月的数据中，X11的使用率超过了90%，平均而言，目前约为93%，而Wayland约为7%。一旦Ubuntu 22.04 LTS作为他们的第一个长期支持版本发布，并默认使用Wayland会话，以及其他一直在向Wayland发展的Linux发行版的不断出现，看看这个数据是如何演变的将会很有趣。当然，请记住，这些数据只是来自Firefox Telemetry数据。</p>   
</div>
            