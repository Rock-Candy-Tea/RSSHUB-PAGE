
---
title: '全面支持 C++，英特尔代码检测工具 ControlFlag 1.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png'
author: 开源中国
comments: false
date: Wed, 11 May 2022 07:46:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">ControlFlag 1.2 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.2" target="_blank">发布</a>。ControlFlag 是<span style="background-color:#ffffff">英特尔推出的一个基于机器学习的代码检测工具，</span><span style="background-color:#ffffff">通过</span><span style="background-color:#ffffff">人工智能和超过 10 亿行代码的训练结合，可以做到自动扫描存储库的源代码中的错误，英特尔已经将它应用到软件和</span><span style="background-color:#ffffff">硬件的生产。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">ControlFlag 是一个自监督的特殊模式检测系统，</span><span style="background-color:#ffffff">就是</span><span style="background-color:#ffffff">通过从开源的存储库（在 GitHub 和其他 Git 平台）挖掘经典模式来学习高级编程语言（如 C/C++）的控制结构（if  等），然后用学到的经典结构来检测用户自己代码的异常情况。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="316" src="https://static.oschina.net/uploads/space/2021/1022/081825_SDQD_4252687.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">去年 11 月发布的<a href="https://www.oschina.net/news/169887/intel-released-controlflag-1.0"><span> </span>ControlFlag 1.0<span> </span></a>版本提供了对 C 语言的全面支持，<a href="https://www.oschina.net/news/191120/controlflag-1-1-released">v1.1 </a>则添加了对 PHP 语言的全面支持，而该 v1.2 版本则是添加对 C++ 的全面支持，现在ControlFlag的整体功能如下：</span></p> 
<ul> 
 <li>下载 C、C++ 和 PHP 语言的 GitHub 存储库，挖掘条件表达式并使用它们训练 ControlFlag</li> 
 <li>包含来自 GitHub 存储库的预挖掘条件表达式的数据集</li> 
 <li>支持检测目标存储库中的异常条件表达式</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.2" target="_blank">https://github.com/IntelLabs/control-flag/releases/tag/v1.2</a></p>
                                        </div>
                                      
</div>
            