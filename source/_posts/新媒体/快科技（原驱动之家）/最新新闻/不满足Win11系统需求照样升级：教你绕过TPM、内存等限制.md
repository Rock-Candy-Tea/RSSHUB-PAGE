
---
title: '不满足Win11系统需求照样升级：教你绕过TPM、内存等限制'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211008/s_0d0157eb30fc4a89baca53aa018e378e.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 08 Oct 2021 17:14:36 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211008/s_0d0157eb30fc4a89baca53aa018e378e.jpg'
---

<div>   
<p>本月5日，Windows 11首个正式版（Build 22000.194）发布，并开始推送，你升级更新了吗？</p>
<p>Win11的最系统要求中，受信任的平台模块 (TPM) 2.0 版本通常是“老爷机”们难以逾越的一道坎，毕竟6代酷睿之后，该模块才普及开来。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211008/0d0157eb30fc4a89baca53aa018e378e.jpg" target="_blank"><img alt="不满足Win11系统需求照样升级：教你绕过TPM、内存等限制" h="400" src="https://img1.mydrivers.com/img/20211008/s_0d0157eb30fc4a89baca53aa018e378e.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>下面分享一些绕过TPM版本验证甚至是内存验证的方法：</p>
<p><strong>方法一：绕过一切硬件限制</strong></p>
<p>在遇到<a class="f14_link" href="https://www.microsoft.com/zh-cn/software-download/windows11" target="_blank">Windows 11安装助手</a>提示PC配置不满足时，定位到C:\$WINDOWS.~BT\Sources，找到appraiserres.dll并删除，接着回到安装助手界面，点击后退，再下一步即可。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211008/0f6a59112ddf41a6bdbc83a70ea4aa33.jpg" target="_blank"><img alt="不满足Win11系统需求照样升级：教你绕过TPM、内存等限制" h="425" src="https://img1.mydrivers.com/img/20211008/s_0f6a59112ddf41a6bdbc83a70ea4aa33.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>方法二：</strong></p>
<p>用记事本创建注册表文件bypass.reg，内容如下</p>
<p>Windows Registry Editor Version 5.00</p>
<p>[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]</p>
<p>"BypassTPMCheck"=dword:00000001</p>
<p>"BypassSecureBootCheck"=dword:00000001</p>
<p>"BypassRAMCheck"=dword:00000001</p>
<p>"BypassStorageCheck"=dword:00000001</p>
<p>"BypassCPUCheck"=dword:00000001</p>
<p>U盘启动遇到无法安装提示时，点击后退箭头，接着按下Shift+F10调出命令提示符，输入regedit打开注册表，并导入刚才保存的bypass.reg。之后关闭所有窗口，开始正常安装。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211008/1360c71c3e0341f282f08977f57e4a66.jpg" target="_blank"><img alt="不满足Win11系统需求照样升级：教你绕过TPM、内存等限制" h="450" src="https://img1.mydrivers.com/img/20211008/s_1360c71c3e0341f282f08977f57e4a66.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>方法三：</strong></p>
<p>下载Windows 11安装助手，右键选择属性——兼容性——以Windows7兼容模式运行。</p>
<p><strong>方法四：开源批处理</strong></p>
<p>Aveyo在Github制作了跳过TPM验证的cmd批处理，还有用户下载免验证ISO或制作启动盘的纯净版媒体介质创建工具。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211008/a534063ecd164bb79e8dda861f3e0296.png" target="_blank"><img alt="不满足Win11系统需求照样升级：教你绕过TPM、内存等限制" h="411" src="https://img1.mydrivers.com/img/20211008/s_a534063ecd164bb79e8dda861f3e0296.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     
<span>责任编辑：万南</span>
</p>
        
</div>
            