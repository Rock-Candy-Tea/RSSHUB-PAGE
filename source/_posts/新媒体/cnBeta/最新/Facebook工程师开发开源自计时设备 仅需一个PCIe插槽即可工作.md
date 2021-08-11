
---
title: 'Facebook工程师开发开源自计时设备 仅需一个PCIe插槽即可工作'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0811/e035ab6c8d58d86.webp'
author: cnBeta
comments: false
date: Wed, 11 Aug 2021 12:57:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0811/e035ab6c8d58d86.webp'
---

<div>   
大多数人可能没有意识到我们的设备在多大程度上是由时间驱动的，无论是你的手机、你的笔记本电脑还是网络服务器。在大多数情况下，设备保持准确的时间一直是一个深奥的苦差事，由有限的硬件制造商负责处理。虽然这些设备达到了它们的目的，但几位Facebook的工程师认为必须有一个更好的方法。<br>
 <p>因此，他们建立了一个新的更准确的计时设备，它只需要一个PCI Express（PCIe）接口，Facebook将其作为一个开源项目贡献给了开放计算项目。</p><p>Facebook的生产工程师Olag Obleukhov说，在一个基本的层面上，所有的设备只是对NTP计时服务器进行访问操作，以确保每个设备都报告相同的时间。他解释说："今天几乎所有的电子设备都使用NTP--网络时间同步协议--你的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>、手表、笔记本电脑，到处都有，它们都连接到这些NTP服务器，它们只是会问服务器，'现在是什么时间'，随后NTP服务器提供时间，"。</p><p>在Facebook开发出一种新的方法之前，基本上有两种方法来检查时间。如果你是一个开发者，你可能会使用像NTP这样的东西作为时间检查机制，但是像Facebook这样的公司，在大规模工作时需要一些即使在没有互联网连接的情况下也能工作，运行这种封闭式数据中心的公司会有一个叫Stratum One的硬件设备，这是一个大盒子，放在数据中心里，除了充当时间保持者没有其他工作。</p><p>因为这些记时盒是由少数几家公司自行制作的，它们很牢固也很好用，但很难获得新的功能。更重要的是，像Facebook这样的公司无法控制这些盒子，因为它们具有专利性质。Obleukhov和他的同事研究科学家Ahmad Byagowi开始着手解决这个问题，他们寻找一种方法，用现成的部件建立一个PCIe卡，可以把它插入任何有开放插槽的PC中，从而实现同样的功能。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0811/e035ab6c8d58d86.webp" title alt="facebook-time-card.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">Facebook的计时PCI卡</p><p>他们在<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>上画出了第一个设计图，并开始将这一设想制作成原型。一个时间装置依赖于几个关键部件：一个GNSS接收器和所谓的高稳定性振荡器。在一篇描述该项目的博文中，Obleukhov和Byagowi维解释了这两个部分的作用。</p><p>"这一切都从一个GNSS接收器开始，它提供一天中的时间（ToD）以及每秒1个脉冲（PPS）。当接收器得到高稳定性振荡器（如原子钟或<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C752%2C759" target="_blank">烤箱</a>控制的晶体振荡器）的支持时，它可以提供纳秒级精度的时间。这使得在PCIe卡上放一个计时装置成为可能的一件事是原子钟/振荡器的微型化进展。</p><p>当设计开始形成时，工程师们决定使其具有灵活性，以使工程师们能够发挥基本设计的作用，并将符合他们需要的任何部件放入其中。有些人可能需要高度复杂的昂贵部件，但根据需求的不同也可以用更便宜的部件。</p><p>他们还在早期决定将设计过程开源，并让开放计算项目参与进来，以便其他公司和工程师能够为设计做出贡献。现在已经有十几家供应商参与了这个项目，并有许多种类似的计时器被制造出来，包括由奥Obleukhov设计的这种PCIe卡片。</p>   
</div>
            