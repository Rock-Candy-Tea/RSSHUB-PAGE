
---
title: 'Win11 VBS 安全功能导致性能下降，教你如何检测并关闭'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/10/039765bb-47dc-4633-8496-727af3032e28.jpg@s_2,w_820,h_547'
author: IT 之家
comments: false
date: Thu, 07 Oct 2021 00:16:52 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/10/039765bb-47dc-4633-8496-727af3032e28.jpg@s_2,w_820,h_547'
---

<div>   
<p data-vmark="236b"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 10 月 7 日消息 微软 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 操作系统已经正式发布，但是根据 UL benchmarks 公司的报告，该系统默认开启的 Virtualization-based Security (VBS)“基于虚拟化的安全性”会导致游戏、跑分性能下降，<span class="accentTextColor">最多降幅可达 30%</span>。在全新安装的 Windows 11 中，VBS 默认设置为开启状态，而从 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Win10</a> 升级则不会开启该功能。</p><p data-vmark="fe63">微软表示，如果该功能可选，那么人们就不会主动打开它。开启 VBS 功能后，即使有软件/黑客获得了管理员级别的权限（最高级别的权限），他们仍然无法读取这个单独的 VM 中的内容，从而更加安全，这与今天云的工作原理是完全相同的。</p><p data-vmark="42c7">根据外媒 XDA 报道，以下方法可以检测 Windows 11/10 系统是否启用 VBS 功能：</p><p data-vmark="ca0b">1、单击任务栏的搜索按钮，或者使用快捷键“Win+S”打开搜索功能。</p><p data-vmark="0b19">2、键入“MSInfo32”，并单击回车。</p><p data-vmark="e687"><img src="https://img.ithome.com/newsuploadfiles/2021/10/039765bb-47dc-4633-8496-727af3032e28.jpg@s_2,w_820,h_547" w="1200" h="800" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" srcset="https://img.ithome.com/newsuploadfiles/2021/10/039765bb-47dc-4633-8496-727af3032e28.jpg 2x" width="1200" height="547" referrerpolicy="no-referrer"></p><p data-vmark="863b"><img src="https://img.ithome.com/newsuploadfiles/2021/10/0a0750d4-8bea-4e5c-bdd6-b07af430c65c.png" w="518" h="235" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" width="518" height="235" referrerpolicy="no-referrer"></p><p data-vmark="3dc8">3、在弹出的“系统信息”窗口中，向下滚动列表，可以看到“<span class="accentTextColor">基于虚拟化的安全性</span>”项目，即为 VBS 功能。下图可见，该功能正在运行。</p><p data-vmark="5dfd"><img src="https://img.ithome.com/newsuploadfiles/2021/10/f87a7903-bebd-4d14-b2cb-3d671ff7c970.png" w="841" h="415" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" width="841" height="405" referrerpolicy="no-referrer"></p><h2 data-vmark="41ac">关闭 Win10、Win11“基于虚拟化的安全性”功能</h2><p data-vmark="0612">1、快捷键 Win+X 打开菜单，选择 Windows Powershell（管理员）</p><p data-vmark="f25b"><img src="https://img.ithome.com/newsuploadfiles/2021/10/3f2cea3a-6696-496a-8f39-e3a026396922.png" w="365" h="100" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" width="365" height="100" referrerpolicy="no-referrer"></p><p data-vmark="6ba1">2、键入以下命令，按下回车，<span class="accentTextColor">重启电脑后生效</span>。</p><pre class="brush:javascript;toolbar:false">bcdedit /set hypervisorlaunchtype off</pre><p data-vmark="8fa5"><img src="https://img.ithome.com/newsuploadfiles/2021/10/2eaaf521-df8c-44ac-9afd-9d22484cfcc0.png" w="637" h="268" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" width="637" height="268" referrerpolicy="no-referrer"></p><p data-vmark="fd0a"><img src="https://img.ithome.com/newsuploadfiles/2021/10/ca069d3f-808d-47d0-a60c-155864c9ec5f.png" w="714" h="379" title="Win11 VBS 安全功能导致性能下降，教你如何检测并关闭" width="714" height="379" referrerpolicy="no-referrer"></p><p data-vmark="8e80">如上图显示，VBS 功能便被成功关闭。</p><p data-vmark="804d">IT之家提示，有教程表示可以在 Windows 组件中，通过禁用 Windows 虚拟化等技术来关闭 VBS 功能，但是这会导致依赖虚拟化技术的应用，如 Hyper-V、VMWare 等无法正常运行，因此不可以使用这种方法。</p>
          
</div>
            