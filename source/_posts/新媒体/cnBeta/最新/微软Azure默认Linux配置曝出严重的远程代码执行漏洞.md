
---
title: '微软Azure默认Linux配置曝出严重的远程代码执行漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0916/ef3c60542f8de91.jpg'
author: cnBeta
comments: false
date: Thu, 16 Sep 2021 05:11:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0916/ef3c60542f8de91.jpg'
---

<div>   
尽管微软表示深爱 Linux，但这点并没有在 Azure 云端得到很好的贯彻。<strong>Wiz 安全研究团队近日指出，他们在诸多流行的 Azure 服务中，发现了开放管理基础设施（OMI）软件代理中存在的一系列严重漏洞。</strong>问题在于当 Azure 客户在云端设置 Linux 虚拟机服务时，OMI 代理会在他们不知情的情况下自动部署。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0916/ef3c60542f8de91.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution" target="_self">Wiz Research</a>）</p><p>但除非及时打上了补丁，否者攻击者就能够利用四个漏洞来获得提升后的 root 权限，从而远程执行任意恶意代码（比如加密文件以勒索赎金）。</p><p><img src="https://static.cnbetacdn.com/article/2021/0916/60128c31b05db92.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>更糟糕的是，黑客只需发送一个剔除了身份验证标头的数据包，即可渗透并取得远程机器上的 root 访问权限。若 OMI 开放了 5986、5985 或 1270 端口，系统就更容易受到攻击。</p><p><img src="https://static.cnbetacdn.com/article/2021/0916/c3ef8685a1b4993.gif" alt="2.gif" referrerpolicy="no-referrer"></p><p>据悉，由于一个简单的条件语句编程错误、结合未初始化的 auth 结构，任何缺乏 Authorization 标头的请求，都被默认赋予了 uid=0、gid=0 的 root 级别权限。</p><p><img src="https://static.cnbetacdn.com/article/2021/0916/14e5e136e8224b3.gif" alt="3.gif" referrerpolicy="no-referrer"></p><p>Wiz 将该漏洞称作“OMIGOD”，并推测 Azure 上多达 65% 的 Linux 部署都受到影响。庆幸的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已经发布了 1.6.8.1 修补版本的 OMI 软件代理，同时建议客户<a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647" target="_self">手动执行更新</a>。</p><p><a href="https://static.cnbetacdn.com/article/2021/0916/d44a5e5d2138d09.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0916/d44a5e5d2138d09.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>最后，Wiz 建议用户酌情选择是否允许 OMI 监听 5985、5986、1270 这三个端口。如非必要，还请立即限制对这些端口的访问，以封堵 CVE-2021-38647 远程代码执行（RCE）漏洞。</p>   
</div>
            