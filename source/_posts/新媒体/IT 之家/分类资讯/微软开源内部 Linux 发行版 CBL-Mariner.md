
---
title: '微软开源内部 Linux 发行版 CBL-Mariner'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/8f06c7d5-3d30-40d4-b611-270fd3cc8cd0.png'
author: IT 之家
comments: false
date: Tue, 20 Jul 2021 01:43:46 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/8f06c7d5-3d30-40d4-b611-270fd3cc8cd0.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 20 日消息 微软近日在 GitHub 开源了一款内部使用的 Linux 发行版 <span class="accentTextColor">CBL-Mariner</span>。该发行版由 WSL 2 团队开发，主要用于<span class="accentTextColor">服务器端</span>而非桌面端。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/8f06c7d5-3d30-40d4-b611-270fd3cc8cd0.png" w="1136" h="922" title="微软开源内部 Linux 发行版 CBL-Mariner" width="1136" height="666" referrerpolicy="no-referrer"></p><p>据微软官方介绍，CBL-Mariner 旨在为云基础设施以及边缘产品和服务提供一致的平台。该计划是微软对各种 Linux 技术不断增加投资的一部分，例如 SONiC、Azure Sphere OS 和 Windows Subsystem for Linux (WSL)。此外，CBL-Mariner 不会改变他们对任何现有第三方 Linux 发行版的态度或承诺。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/22f55ae0-d3ae-4488-b4ab-89536a8623f2.png" w="1136" h="922" title="微软开源内部 Linux 发行版 CBL-Mariner" width="1136" height="666" referrerpolicy="no-referrer"></p><p>IT之家了解到，CBL-Mariner 的设计理念是，一组小的通用核心包可以满足第一方云和边缘服务的普遍需求，同时允许各个团队在通用核心之上分层附加包，为他们的工作负载生成镜像。这是通过一个简单的构建系统实现的，该系统支持：</p><ul class=" list-paddingleft-2"><li><p><strong>包生成：</strong>从 SPEC 文件和源文件中生成所需的一组 RPM 包。</p></li><li><p><strong>镜像生成：</strong>从给定的一组包中生成所需的镜像，如 ISO 或 VHD。</p></li></ul><p>当出现安全漏洞时，CBL-Mariner 支持基于包的更新模型和基于镜像的更新模型。利用通用的 RPM 包管理器系统，CBL-Mariner 提供最新的安全补丁和修复程序，以实现快速周转时间的目标。</p><p>微软没有给出 CBL-Mariner 的 ISO 镜像，需要大家自行构建，可以<a href="https://blog.jreypo.io/2021/07/09/a-look-into-cbl-mariner-microsoft-internal-linux-distribution/" target="_blank">点此查看教程</a>。</p><p><strong>CBL-Mariner 的 GitHub 页面：</strong><a href="https://github.com/microsoft/CBL-Mariner" target="_blank">点此查看</a></p>
          
</div>
            