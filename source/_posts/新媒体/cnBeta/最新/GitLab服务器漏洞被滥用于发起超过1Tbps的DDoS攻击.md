
---
title: 'GitLab服务器漏洞被滥用于发起超过1Tbps的DDoS攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1105/8d8500df95840ac.png'
author: cnBeta
comments: false
date: Fri, 05 Nov 2021 08:15:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1105/8d8500df95840ac.png'
---

<div>   
Google 云安全可靠性工程师 Damian Menscher 在今日披露的 CVE-2021-22205 漏洞利用报告中指出：<strong>有攻击者正在利用 GitLab 托管服务器上的安全漏洞来构建僵尸网络，并发起规模惊人的分布式拒绝服务攻击（DDoS）。</strong>其中一些攻击的峰值流量，甚至超过了 1 Tbps 。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1105/8d8500df95840ac.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">攻击盯上了 GitLab 的元数据删除功能</p><p>The Record 报道称：该漏洞由 William Bowling 发现，并通过漏洞赏金计划提交给了 GitLab 官方。</p><p>具体受影响的组件被称作 ExifTool，它是一个用于将图像上传到 Web 服务器、并剔除元数据的库。</p><p>GitLab 在社区版（CE）和企业版（EE）上均使用了 ExifTool，且公司能够将其服务的开源 / 商业版本安装在自己的服务器上。</p><p>这样一来，企业能够专注于他们想要处理专有代码的场景安全环境，而无需使用基于云端的 GitLab 服务。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1105/41468966d660abc.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：HN Security）</p><p>然而在向 HackerOne 提交的一份报告中，Bowling 称其发现了一种滥用 ExifTool 的方法，可被用于扫描 DjVu 格式的文档上传，进而获得对整个底层 GitLab 网络服务器的控制。</p><p>上周首次披露漏洞利用迹象的意大利安全公司 <a href="https://security.humanativaspa.it/gitlab-ce-cve-2021-22205-in-the-wild/" target="_self">HN Security</a> 指出，攻击可追溯到今年 6 月份。</p><p>当时安全研究员 Piergiovanni Cipolloni 表示，在发现有随机命名的用户被添加到受感染的 GitLab 服务器后，他们随即对此展开了调查。这些用户很可能是由攻击者一手创建，旨在对受害系统实施远程控制。</p><p>尽管 HN Security 尚不清楚这些攻击的目的，但 Google 工程师 Damian Menscher 已于昨日表示，被黑服务器属于某个巨型僵尸网络的一部分。</p><p>该网络包含成千上万个受感染的 GitLab 实例，且正被用于发起大规模的 DDoS 攻击。遗憾的是，尽管 GitLab 已于 2021 年 4 月完成了修补，仍有大约 30000 个 GitLab 服务器尚未打上补丁。</p>   
</div>
            