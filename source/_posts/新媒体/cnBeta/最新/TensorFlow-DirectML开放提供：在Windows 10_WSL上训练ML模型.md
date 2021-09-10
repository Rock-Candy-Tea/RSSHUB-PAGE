
---
title: 'TensorFlow-DirectML开放提供：在Windows 10_WSL上训练ML模型'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0910/0a6865e5e91c2f2.jpg'
author: cnBeta
comments: false
date: Fri, 10 Sep 2021 08:23:13 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0910/0a6865e5e91c2f2.jpg'
---

<div>   
1 年多以前，微软宣布和多家硬件厂商合作，在 Windows Subsystem for Linux（WSL）上对 GPU 加速的机器学习（ML）模型进行训练。微软在 2020 年 6 月放出了预览版。<strong>今天，<a href="https://github.com/microsoft/tensorflow-directml" target="_blank">这个开源的 GitHub 项目已经退出预览</a>，正式开放提供。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0910/0a6865e5e91c2f2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0910/0a6865e5e91c2f2.jpg" alt="bspaq87s.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">微软训练了 TensorFlow-DirectML，这是 TensorFlow 的一个分叉，利用 DirectML 为在 Windows 10 和 WSL 上训练 ML 模型提供跨厂商的硬件加速。微软表示，使用 TensorFlow-DirectML 相当容易，因为它可以通过运行"pip install tensorflow-directml"命令在Python环境下安装。之后，它将自动与你现有的训练模型的脚本集成。</p><p style="text-align: left;">微软表示，它直接与学生和专业人士合作，为他们的脚本提供覆盖，并优化批量归一化和卷积等操作。这个过程也涉及加强 GPU 调度和内存管理机制。微软与 Nvidia、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>等供应商合作，确保在 Windows 10 和 WSL 之间提供流畅的体验，以便在支持 DirectX 12 的 GPU 上加速培训。</p><p style="text-align: left;">就目前而言，TensorFlow-DirectML 的系统要求如下</p><p style="text-align: left;"><strong>Windows 10</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 10版本1709，64位（Build 16299或更高）。</p><p style="text-align: left;">● Python x86-64 3.5, 3.6, 或 3.7</p><p style="text-align: left;">● 以下支持的GPU之一。</p><p style="text-align: left;">→ AMD Radeon R5/R7/R9 2xx 系列或更新版本</p><p style="text-align: left;">→ 英特尔HD Graphics 5xx 或更新版本</p><p style="text-align: left;">→ NVIDIA GeForce GTX 9xx 系列 GPU 或更新版本</p><p style="text-align: left;">注意：目前不支持 Python 3.8 或更新版本。要使用官方 PyPi 软件包，需要使用 CPython 解释器。NumPy 1.19.4 需要 KB4598291 才能在 Windows 上正常工作。</p></blockquote><p style="text-align: left;"><strong>Windows Subsystem for Linux</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 10 Insider Preview，64位（Build 20150或更高）。</p><p style="text-align: left;">● Python x86-64 3.5, 3.6, 或 3.7</p><p style="text-align: left;">● 以下支持的GPU之一。</p><p style="text-align: left;">→ AMD Radeon R5/R7/R9 2xx系列或更新版本，以及20.20.01.05 WSL驱动</p><p style="text-align: left;">→ 英特尔HD Graphics 6xx或更新版本，以及28.20.100.8322 WSL驱动程序</p><p style="text-align: left;">→ NVIDIA GeForce GTX 9xx系列GPU或更新版本，以及460.20 WSL驱动</p><p style="text-align: left;">注意：目前不支持Python 3.8或更新版本。要使用官方PyPi软件包，需要使用CPython解释器。</p></blockquote>   
</div>
            