
---
title: '全面支持 PHP，英特尔代码检测工具 ControlFlag 1.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 07:44:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">ControlFlag 1.1 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.1" target="_blank">发布</a>。ControlFlag 是<span style="background-color:#ffffff">英特尔推出的一个基于机器学习的代码检测工具，</span><span style="background-color:#ffffff">通过</span><span style="background-color:#ffffff">人工智能和超过 10 亿行代码的训练结合，可以做到自动扫描存储库的源代码中的错误，英特尔已经将它应用到软件和</span><span style="background-color:#ffffff">硬件的生产。</span></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">ControlFlag 是一个自监督的特殊模式检测系统，</span><span style="background-color:#ffffff">就是</span><span style="background-color:#ffffff">通过从开源的存储库（在 GitHub 和其他 Git 平台）挖掘经典模式来学习高级编程语言（如 C/C++）的控制结构（if  等），然后用学到的经典结构来检测用户自己代码的异常情况。</span></span></p> 
<p><img height="263" src="https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">去年 11 月发布的<a href="https://www.oschina.net/news/169887/intel-released-controlflag-1.0"> ControlFlag 1.0 </a>版本提供了对 C 语言的全面支持。</span><span style="color:#000000">v1.1 则添加了对 PHP 语言的全面支持，此版本<span style="background-color:#ffffff">完全支持在 C 和 PHP 程序的 if 语句中学习典型模式（训练）和检测异常模式（推理）。为以下方面提供支持：</span></span></p> 
<ul> 
 <li>下载 C 和 PHP 语言的 GitHub 存储库，挖掘条件表达式并使用它们训练 ControlFlag</li> 
 <li>包含来自 GitHub 存储库的预挖掘条件表达式的数据集</li> 
 <li>支持检测目标存储库中的异常条件表达式</li> 
</ul> 
<p>此外，此版本修复了处理输入错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Fpull%2F42" target="_blank">#42</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Fpull%2F45" target="_blank">#45</a>）和拼写错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Fpull%2F43" target="_blank">#43</a>）。 </p> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.1" target="_blank">https://github.com/IntelLabs/control-flag/releases/tag/v1.1</a></p>
                                        </div>
                                      
</div>
            