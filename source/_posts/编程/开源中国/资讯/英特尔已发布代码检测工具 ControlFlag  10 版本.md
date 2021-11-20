
---
title: '英特尔已发布代码检测工具 ControlFlag  1.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1120/080035_wAvP_5430600.jpeg'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 08:01:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1120/080035_wAvP_5430600.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">11 月 19 日，<span style="color:#121212">由英特尔实验室开发的 ControlFlag<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.0" target="_blank"><span style="color:#121212">发布了 1.0 版本</span></a><span style="color:#121212">，ControlFlag 通过</span>人工智能和超过 10 亿行代码的训练结合，可以做到自动扫描存储库的源代码中的错误，英特尔已经将它应用到软件和<span style="color:#121212">硬件的生产。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">ControlFlag 是一个自监督的特殊模式检测系统，<span style="color:#24292f">就是</span>通过从开源的存储库（在 GitHub 和其他 Git 平台）挖掘经典模式来学习高级编程语言（如 C/C++）的控制结构（if  等），然后用学到的经典结构来检测用户自己代码的异常情况。目前<strong><span> </span>ControlFlag 已经学习了 6000+ 个 Github 存储库</strong>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">（简单来说就是去别人那学习 C 语言的代码到底该怎么写，学完了就回来看看自己的代码有没有哪里写错了。）</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">下图显示了 ControlFlag 的两个运行阶段：模式挖掘阶段（到处学习）和扫描异常模式阶段（检查自己代码）。模式挖掘阶段是一个“训练阶段”，根据用户提供的 GitHub 存储库中的典型控制结构来建立决策树。然后到扫描异常的阶段会用前面训练出来的决策树来标查找用户自己 Git 库里面异常的代码表达式。</span></p> 
<p><br> <img alt height="394" src="https://static.oschina.net/uploads/space/2021/1120/080035_wAvP_5430600.jpeg" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">ControlFlag 1.0 版本的发布意味着已经全面支持学习 C 程序（不过按<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIntelLabs%2Fcontrol-flag%2Freleases%2Ftag%2Fv1.0" target="_blank">更新公告</a>的意思，现在只能学<span> </span><code>if</code><span> </span>条件语句相关的 C 语言结构）和异常推断功能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>依赖项</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>CMake 3.4.3 或以上</li> 
 <li>兼容 C++17 的编译器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftree-sitter%2Ftree-sitter.git" target="_blank">Tree-sitter</a><span> </span>解析器（会作为 cmake 的一部分自动下载）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gnu.org%2Fsoftware%2Fparallel%2F" target="_blank">GNU parallel</a>（可选，如果你想生成训练数据）</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            