
---
title: 'Ncdu 2 首个 Beta 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d6e70afcabf69e79cd8a8205392b781cfe4.png'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 23:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d6e70afcabf69e79cd8a8205392b781cfe4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ncdu (NCurses Disk Usage) 是一个基于终端的磁盘使用分析工具，（此前）使用 C 语言编写，适用于 Linux 和其他 POSIX 系统，大多数发行版的软件包仓库均有提供。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.yorhel.nl%2Fdoc%2Fncdu2" target="_blank">发布公告写道</a>，作者在过去的几个月里对 Ncdu 进行了全面的重写，并于近日发布了 2.0-beta1。据介绍，Ncdu 2 是 ncdu 1.x 的完全替代方案，它保留了所有相同的功能、相同的用户界面、键盘绑定和命令行标志。作者表示，之所以这样做是为了让它成为一个合适的替代方案。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d6e70afcabf69e79cd8a8205392b781cfe4.png" referrerpolicy="no-referrer"></p> 
<p>2.0 主要变化：</p> 
<ul> 
 <li>开发语言从 C 专为 Zig</li> 
 <li>优化内存数，普通场景中的内存占用只有原来的一半，但如果有许多硬链接，在某些情况下可能会使用更多的内存</li> 
 <li>新增共享链接 (Shared links) 功能</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-30781b460a5ebc637257bccb41de5886782.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-f71559b6290c04fdb56dd4780a506d4693e.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>改进对 Unicode 文件名的处理，支持识别全角字符</li> 
 <li>提升使用性能</li> 
 <li>在硬链接信息窗口的“链接”选项卡中，支持直接跳转到所选路径</li> 
 <li>文件浏览器现在可以更好地记住切换目录时所选项目在屏幕上的位置</li> 
 <li>……</li> 
</ul> 
<p>但 2.0 也带来了一些不好的变化，例如刷新目录可能会出现内存泄露的情况。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.yorhel.nl%2Fdoc%2Fncdu2" target="_blank">更多内容点此查看</a>。</p>
                                        </div>
                                      
</div>
            