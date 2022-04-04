
---
title: 'AMD显卡驱动被指绕过用户擅自修改CPU设置'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0404/c4ab09ebab9768b.jpg'
author: cnBeta
comments: false
date: Mon, 04 Apr 2022 03:14:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0404/c4ab09ebab9768b.jpg'
---

<div>   
今天，根据Igor's Lab发布的消息，<strong>AMD的显卡驱动有可能会在用户不知情的情况下，擅自修改CPU设置。</strong>根据用户反馈，在采用“3A平台”，即AMD的CPU、主板和显卡整合平台上，<strong>出现了驱动在应用GPU配置文件时，自动启动PBO或CPU OS设置，且用任意配置覆盖用户配置的情况，对CPU的稳定性造成了影响。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0404/c4ab09ebab9768b.jpg" title alt="Automatische-Uebertaktung-fehlgeschlagen-1.jpg" referrerpolicy="no-referrer"></p><p>有观点认为，是由于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的Ryzen Master模块集成到了Adrenalin 22.3.1或更高版本的软件中，导致了程序绕过用户修改CPU设置的情况。</p><p>在出现这一情况后，用户可以通过进入主板BIOS，并重新输入设置的方式，恢复CPU配置；也能够通过运行Radeon Software Slimmer，删除Ryzen Master SDK，从而解决问题。</p><p>此外，<strong>在Adrenalin中为GPU创建一个新的调整配置文件，也能够阻止驱动在主板BIOS中修改配置。</strong></p><p>目前，已经有用户在AMD官方社区反映了该问题，且有其他“受害者”进行了回复，但AMD官方尚未对该情况做出回应。</p><p>值得一提的是，<strong>只有采用3A平台的用户才会遇到该问题，Intel、AMD、NVIDIA三家“混搭”的用户则完全不受影响。</strong></p><p><strong><a href="https://static.cnbetacdn.com/article/2022/0404/1e6ea3d410457da.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0404/1e6ea3d410457da.jpg" title alt="von-Ryzen-Master-ungefragt-konfiguriert-980x735.jpg" referrerpolicy="no-referrer"></a><a href="https://static.cnbetacdn.com/article/2022/0404/b6dbd4ae7b249d6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0404/b6dbd4ae7b249d6.jpg" title alt="Manuell-konfiguriert-980x735.jpg" referrerpolicy="no-referrer"></a></strong></p>   
</div>
            