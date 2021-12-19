
---
title: 'Win11新设定太容易误操！教你找回删除确认框'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211219/Sa31424b0-efd3-4fec-81f9-ade8f3d1a953.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 19 Dec 2021 07:26:44 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211219/Sa31424b0-efd3-4fec-81f9-ade8f3d1a953.png'
---

<div>   
<p>在Win11当中，有朋友发现了一个令人崩溃的设定——放在桌面上好好的一个文件，突然就不见了！经过调查，就更加崩溃了，原来这个文件并非是真的消失了，而是被移动到了回收站！</p>
<p>为什么会这样？因为Win11当中，删除文件并不会弹出提示框，一旦不小心误触了Delete键，选中的文件就会悄无声息地被删除，放到回收站当中。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211219/a31424b0-efd3-4fec-81f9-ade8f3d1a953.png" target="_blank"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="230" src="https://img1.mydrivers.com/img/20211219/Sa31424b0-efd3-4fec-81f9-ade8f3d1a953.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在Win11中，按“Delete”删除文件默认不弹窗了！</p>
<p>毫无疑问，这个设定带来了更多误操作，很多从老系统升级到Win11的朋友可能会习惯不了这样的机制。要如何才能让Win11在删除文件时，像旧系统一样弹出删除确认框？今天就给大家分享一些方法。</p>
<p><strong>回收站设置</strong></p>
<p>这是最简单的方法。找到回收站的图标，点击右键，选择“属性”。</p>
<p style="text-align: center"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="383" src="https://img1.mydrivers.com/img/20211219/3da3271d-b7f3-4b2b-821b-1fce99a359f7.png" style="border: black 1px solid" w="511" referrerpolicy="no-referrer"></p>
<p>在回收站的属性面板当中，可以看到“显示删除确认对话框”的选项，将其勾选后，点击“确定”或者“应用”保存。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211219/f8b7d23c-ffe0-4482-9fd5-c7f5bee08c50.png" target="_blank"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="696" src="https://img1.mydrivers.com/img/20211219/Sf8b7d23c-ffe0-4482-9fd5-c7f5bee08c50.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>之后删除文件，就会弹出确认框了。</p>
<p><strong>修改注册表</strong></p>
<p>这是另一个没那么方便的方法，起到的效果也是一样的。</p>
<p>首先，通过系统搜索，直接开启注册表编辑器，定位到以下目录。</p>
<p>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\</p>
<p>观察有没有Explorer的项，如果没有，就右键点击“Policies”，新创建一个名为“Explorer”的项。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211219/17a90fee-e2de-4741-9b71-74294350af8d.png" target="_blank"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="444" src="https://img1.mydrivers.com/img/20211219/S17a90fee-e2de-4741-9b71-74294350af8d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>右键点击Explorer项，新建一个“DWORD(32 位)值”，将其命名为“ConfirmFileDelete”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211219/fd511071-ec79-42aa-9f79-f48882f3459c.jpg" target="_blank"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="444" src="https://img1.mydrivers.com/img/20211219/Sfd511071-ec79-42aa-9f79-f48882f3459c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>双击“ConfirmFileDelete”，将它的值改为“1”，保存退出注册表编辑器，重启系统即可。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211219/76170da5-a91c-4a8f-925b-3529081dd7e8.png" target="_blank"><img alt="Win11新设定太容易误操！教你找回删除确认框" h="444" src="https://img1.mydrivers.com/img/20211219/S76170da5-a91c-4a8f-925b-3529081dd7e8.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>总的来说，Win11删除文件不提示的新设定，的确会造成更多的误操作，不过也提高了效率。所幸这个功能调整起来并不困难，大家按照自己的习惯去调节即可。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win11/1475/14752844.html#ad=8387">太平洋电脑网</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            