
---
title: 'Win10新补丁又闯祸！教你如何修复系统Bug'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210928/S036a3652-c232-42bb-a531-64762b7d7bc9.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 28 Sep 2021 08:28:12 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210928/S036a3652-c232-42bb-a531-64762b7d7bc9.jpg'
---

<div>   
<p>微软在不久前面向Win10推送了KB5005565补丁，以修复蓝牙、USB音频等相关问题。然而就如同此前多次发生过的一样，KB5005565又惹出了新毛病。</p>
<p>有用户反馈，KB5005565导致英特尔720等无线适配器蓝牙驱动崩溃。</p>
<p>用户指出，驱动会弹出一个代号为10的错误，<span style="color:#ff0000;"><strong>并提示“POWER FAILURE”，接着Windows会自动安装一个损耗的蓝牙驱动来取代原先的驱动。</strong></span></p>
<p>在支持文件的更新内容中，微软证实了KB5005565补丁会带来应用程序冻结的问题。</p>
<p>根据文件，KB5005565会导致一些应用程序出现意外情况，可能会无法开启应用程序或文件，登录时可能会出现一个白色窗口。</p>
<p>值得庆幸的是，<strong>微软已经为该问题制定了一个修复方案，该方案目前正通过服务器端更新推送。</strong></p>
<p>微软称，该问题是使用“已知问题回滚（KIR）”机制解决了，不过要注意，需要在24小时后该修复才能自动推送到消费者的设备以及处于非管理状态下的商业设备当中。</p>
<p>另外，Win10中还出现了代号为0x0000011b的错误。<strong>这是一个关于网络打印机的错误。在系统更新了2021年9月累积更新后，该错误开始出现。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210928/036a3652-c232-42bb-a531-64762b7d7bc9.jpg" style="text-align: center;" target="_blank"><img alt="Win10新补丁又闯祸！教你如何修复系统Bug" h="315" src="https://img1.mydrivers.com/img/20210928/S036a3652-c232-42bb-a531-64762b7d7bc9.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>2021年9月的Win10累积更新，主要解决了包括CVE-2021-26958的PrintNightmar零日漏洞。</p>
<p>该漏洞快一倍利用于非法获取设备的高权限，但却也导致了0x0000011b错误。很多用户在使用基于网络的打印功能时，遇到了0x0000011b错误。</p>
<p>用户称，这个错误导致无法将主机的共享打印机连接到虚拟机上，系统会提示 "Windows无法连接到打印机 "的错误。</p>
<p>此外，Quick Books应用程序不会显示任何打印机设置窗口，而在试图打开一个窗口时，过了一会儿就崩溃了。</p>
<p>要如何解决0x0000011b错误？下面是具体的步骤。</p>
<p>在注册表编辑器中，<span style="color:#ff0000;"><strong>打开HKEY_LOCAL_MACHINE/System/CurrentControlSet/Control/Print键。</strong></span></p>
<p>创建一个新的DWORD-32位值。</p>
<p><strong>将其命名为 "RpcAuthnLevelPrivacyEnabled"。</strong></p>
<p><strong>将该值设置为0。</strong></p>
<p>保存更改并关闭编辑器。</p>
<p>需要注意的是，该问题不限于特定的硬件。<span style="color:#ff0000;"><strong>如果你无法恢复打印功能，你也可以手动卸载Windows 10更新</strong></span>，并暂停更新几周或直到微软发布新的补丁。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210928/069d626d2ae0477eaada03697dddaf5d.jpg" target="_blank"><img alt="Win10新补丁又闯祸！教你如何修复系统Bug" h="337" src="https://img1.mydrivers.com/img/20210928/s_069d626d2ae0477eaada03697dddaf5d.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a><a href="https://news.mydrivers.com/tag/buding.htm"><i>#</i>补丁</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1459/14595544.html#ad=8518">太平洋电脑网</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            