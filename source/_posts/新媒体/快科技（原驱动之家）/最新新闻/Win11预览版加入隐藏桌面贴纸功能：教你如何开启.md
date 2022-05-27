
---
title: 'Win11预览版加入隐藏桌面贴纸功能：教你如何开启'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220527/s_8b0026ef6f7841f082a996e680122910.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 27 May 2022 11:16:09 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220527/s_8b0026ef6f7841f082a996e680122910.jpg'
---

<div>   
<p>微软经常会在Windows的更新中，加入一些已经基本完成，但还不能上线的功能，<strong>近日，就有用户在Win11的Build 22621预览版中，发现了隐藏的贴纸功能。</strong></p>
<p>这一贴纸功能的作用非常简单，仅仅是从菜单中选择一个卡通动物或物品的图案“粘”在桌面上，作为桌面装饰。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220527/8b0026ef6f7841f082a996e680122910.jpg" target="_blank"><img alt="Win11预览版加入隐藏桌面贴纸功能：教你如何开启" h="322" src="https://img1.mydrivers.com/img/20220527/s_8b0026ef6f7841f082a996e680122910.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>除此之外，<strong>该功能没有任何实质作用，也无法实现带有注释或其他信息的贴纸。</strong></p>
<p>想要开启贴纸功能，首先用户需要确定自己电脑的Win11版本在Build 22621及以上；之后，用户可以通过Win+R快捷键呼出运行窗口，输入“regedit”进入注册表。</p>
<p>之后，将以下路径复制并粘贴到注册表编辑器的地址栏中：<strong>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\current\device</strong>。</p>
<p>在进入目标菜单后，右键单击“device”目录，并选择新建>项，并将新建的项重命名为“Stickers”。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220527/a4d2d5815f2547b9b04a735676af54d1.png" target="_blank"><img alt="Win11预览版加入隐藏桌面贴纸功能：教你如何开启" h="429" src="https://img1.mydrivers.com/img/20220527/s_a4d2d5815f2547b9b04a735676af54d1.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>接下来，右键注册表右侧的空白区域，选择新建>DWORD (32 位) 值，并将其重命名为“EnableStickers”。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220527/246e5cadada84c208cb82b4769e9d44e.png" target="_blank"><img alt="Win11预览版加入隐藏桌面贴纸功能：教你如何开启" h="429" src="https://img1.mydrivers.com/img/20220527/s_246e5cadada84c208cb82b4769e9d44e.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>最后，<strong>打开EnableStickers，将数值数据修改为1</strong>，保存更改后重启电脑即可。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220527/17070e68a59f465fb89b27d43d583fe4.png" target="_blank"><img alt="Win11预览版加入隐藏桌面贴纸功能：教你如何开启" h="429" src="https://img1.mydrivers.com/img/20220527/s_17070e68a59f465fb89b27d43d583fe4.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>在完成上述操作后，在桌面右键菜单，或是设置>个性化>背景中 ，即可找到该功能。</p>
<p>需要注意的是，<span style="color:#ff0000;"><strong>修改注册表客观存在一定风险，请根据流程进行操作，避免由于误操作，对应用的正常运行造成影响。</strong></span></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220527/30cc9b7b9ec947b7aba6ebf9f04fe513.jpg" target="_blank"><img alt="Win11预览版加入隐藏桌面贴纸功能：教你如何开启" h="400" src="https://img1.mydrivers.com/img/20220527/s_30cc9b7b9ec947b7aba6ebf9f04fe513.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a><a href="https://news.mydrivers.com/tag/windows.htm">Windows</a><a href="https://news.mydrivers.com/tag/zhucebiao.htm">注册表</a>  </p>
        
</div>
            