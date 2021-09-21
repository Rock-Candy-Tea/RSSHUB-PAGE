
---
title: 'Linux 5.15-rc2 发布，解决'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0921/083438_Uchj_2720166.png'
author: 开源中国
comments: false
date: Tue, 21 Sep 2021 08:41:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0921/083438_Uchj_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Linux 内核 5.15 的第二个 RC 版本已发布。</p> 
<div>
 Linus Torvalds 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwirexiZR%2BVO%3DH3xemGKOMkh8OasmXaKXTKUmAKYCzi8AQ%40mail.gmail.com%2FT%2F%23u" target="_blank">在发布公告中称</a>，他在上周花了很多时间来研究由于在合并窗口期间，构建 Linux 内核时恢复 -Werror 默认值而引发的问题。他希望搞清楚所有奇怪的警告。此外还包括多项错误修复——例如 DEC Jensen 修复，
 <span style="background-color:#ffffff; color:#121212">来自于将编译器警告提升为错误所引发的问题。</span>
</div> 
<div>
  
</div> 
<div> 
 <div>
  <img src="https://static.oschina.net/uploads/space/2021/0921/083438_Uchj_2720166.png" referrerpolicy="no-referrer">
 </div> 
 <div>
   
 </div> 
 <div>
  其他变化包括：提升 GCC 版本对支持的基线编译器版本的要求；Linux 5.15 现在对 DEC Alpha "Jensen" 系统的破坏性降低，以及对 KSMBD 内核内 SMB3 文件服务器的重要修复。
 </div> 
 <div>
   
 </div> 
 <div>
  按照计划，Linux 5.15 应该在 11 月初左右作为稳定版本正式发布。
 </div> 
 <div>
   
 </div> 
 <div> 
  <div> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Linux 5.15 主要变化：</p> 
   <div> 
    <ul> 
     <li>引入 Paragon Software 开发的 NTFS3 内核驱动</li> 
     <li>支持使用 KSMBD 作为内核空间 SMB3 文件服务器</li> 
     <li>改进对微软 NTFS 文件系统的支持</li> 
     <li>支持在上下文切换时选择进入 L1d 缓存刷新</li> 
     <li>继续改进对 Apple M1 的支持</li> 
     <li>增加 PassThru DMA 引擎驱动</li> 
     <li>对英特尔 DG2/Alchemist 和 XeHP 独立显卡的初步支持</li> 
     <li>以及新增对许多其他新硬件的支持</li> 
    </ul> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            