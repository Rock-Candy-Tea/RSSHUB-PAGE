
---
title: 'CentOS Stream 9在至强和EPYC处理器的性能表现上均有提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1216/e2bb4c71f85101c.jpg'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 11:54:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1216/e2bb4c71f85101c.jpg'
---

<div>   
本月早些时候，CentOS Stream 9作为Red hat Enterprise Linux 9开发的前沿产品全面上市。与CentOS
Stream 8/RHEL8相比，它提供了一些不错的性能升级，特别是在现代硬件平台上，如英特尔至强可扩展"Ice Lake"和AMD EPYC
7003"Milan"服务器处理器。<br>
 <p>下面是CentOS Stream8、CentOS Stream9、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的Clear Linux、Fedora Server 35、Ubuntu 20.04.3 LTS和Ubuntu 21.10在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>和英特尔服务器上的基准测试结论：</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/e2bb4c71f85101c.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>CentOS Stream 9是Red Hat Enterprise Linux 9之前的新的"连续交付版本"，这意味着CentOS Stream 9将包含RHEL9的最新创新，对于RHEL的使用者而言可以提供新的硬件支持和性能优化的早期观察。</p><p>为了了解CentOS Stream 9和RHEL9的情况，我在AMD和英特尔的参考服务器上用最新一代的处理器做了一些基准测试。AMD服务器使用的是EPYC 7763 2P处理器，英特尔服务器使用的是其旗舰产品至强白金8380 2P处理器。两台服务器都使用512GB DDR4-3200内存和英特尔7.6TB D7-P5510 NVme固态硬盘。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/937eed62b89b8ae.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>在这两台最新一代的服务器上，在执行清洁安装并以开箱即用的状态运行后，我们测试对比了以下发行版：</p><p>- CentOS Stream 8用于查看当前的CentOS 8 / RHEL8状态。</p><p>- CentOS Stream 9作为RHEL9的前沿版本，是新版本。</p><p>- Clear Linux是专门针对英特尔的性能优化的滚动发布版本。</p><p>- Fedora Server 35是最新的Fedora上游版本。</p><p>- Ubuntu 20.04.3是目前的长期支持版本。</p><p>- Ubuntu 21.10作为最新的非长期支持版本，其性能目前看起来比Ubuntu 22.04 LTS领先。</p><p>我们进行了一组几十个基准测试，重点是CentOS Stream 9在这些最新一代的AMD/Intel服务器上与CentOS Stream 8相比的表现，以及CentOS Stream 9与其他Linux发行版相比的表现。与CentOS Stream 8 / RHEL8相比，CentOS Stream 9的内核从Linux 4.18升级到Linux 5.14，桌面上的GNOME Shell 40取代了GNOME 3.32，GCC 11.2作为默认的系统编译器而不是旧版GCC 8.5，预装Python 3.9而不是Python 3.6，以及许多其他软件包的升级。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/0c0a01e30ec58a8.png" title alt="YS97X7EJZFTLU&#125;9]3_UH9`E.png" referrerpolicy="no-referrer"></p><p>CentOS Stream 9比已经老化的RHEL8/CentOS Stream 8状态提供了实质性的提升。AMD EPYC 7763 2P服务器从CentOS Stream 8到9有12%的提升，而Xeon Platinum 8380 2P Ice Lake服务器则整体提升了10%。这有助于推动CentOS Stream领先于Ubuntu，甚至是Fedora Server。然而，英特尔Clear Linux的结果仍然表明，在AMD和英特尔上，仍然有更多的优化空间...... 在AMD EPYC Milan和Intel Xeon Ice Lake服务器上，Clear Linux仍然比CentOS Stream 9整体快4%。</p>   
</div>
            