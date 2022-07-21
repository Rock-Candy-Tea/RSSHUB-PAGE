
---
title: 'Neutralinojs v4.7.0 发布，轻量级桌面应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9211'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9211'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">Neutralinojs v4.7.0 现已发布。Neutralinojs 是一个轻量级、便携的桌面应用程序开发框架，可以使用 JavaScript、HTML 和 CSS 开发轻量级跨平台桌面应用程序。具体</span><span style="color:rgba(0, 0, 0, 0.87)">更新内容如下：</span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>API：System information API</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此前在计算机命名空间中有<code>getMemoryInfo</code>函数来检索系统内存的统计数据。现在则增加了更多的函数来获取关于 CPU、操作系统、内核和连接的显示器的详细信息：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li> <p><code>computer.getArch</code>：返回 CPU 架构。即<code>x64</code>、<code>arm</code>等</p> </li> 
 <li> <p><code>computer.getKernelInfo</code>：返回操作系统的内核详细信息。</p> </li> 
 <li> <p><code>computer.getOSInfo</code>：返回操作系统详细信息。</p> </li> 
 <li> <p><code>computer.getCPUInfo</code>：返回 CPU 详细信息。</p> </li> 
 <li> <p><code>computer.getDisplays</code>：返回所有已连接显示器的数组，其中包含分辨率、类似频率的信息。</p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>API：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>os dialogs</strong></p> 
<ul> 
 <li> <p>将<code>defaultPath</code>选项添加到<code>showSaveDialog</code>、<code>showOpenDialog</code>和<code>showFolderDialog</code>函数以设置系统对话框的初始路径/文件名。</p> </li> 
</ul> 
<p style="text-align:start"><strong>DevOps</strong></p> 
<ul> 
 <li> <p>在 Windows GitHub Actions 实例上运行测试套件。</p> </li> 
 <li> <p>修复 GitHub Actions 工作流中的<code>armhf</code>框架二进制生成问题。</p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>错误修正/改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>默认隐藏 Chrome 模式下的自动化信息栏 -- 开发人员如果需要特定的命令行开关，可以在配置文件中添加<code>--enable-automation</code>flag 。</p> </li> 
</ul> 
<p style="text-align:start">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneutralinojs%2Fneutralinojs%2Freleases%2Ftag%2Fv4.7.0" target="_blank">https://github.com/neutralinojs/neutralinojs/releases/tag/v4.7.0</a></p>
                                        </div>
                                      
</div>
            