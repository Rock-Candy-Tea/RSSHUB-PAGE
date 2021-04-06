
---
title: '前所未有地便利！你可知Win10的CMD还能这么玩'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210406/Sc55fdfdf-6815-4542-bb5d-36013564aa9b.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 06 Apr 2021 06:29:44 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210406/Sc55fdfdf-6815-4542-bb5d-36013564aa9b.png'
---

<div>   
<p>如果你是经验丰富的老用户，那么应该会经常在Win10中用到以CMD为代表的命令行工具。然而这些命令行工具一直以来，都存在一个极其影响体验的点，那就是每次开启，路径都是默认为“C:\Users\用户名”当中。</p>
<p>如果你需要的工具存在于其他目录，需要手动输入“CD 目录”来进行跳转。每次都如此，非常麻烦。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/c55fdfdf-6815-4542-bb5d-36013564aa9b.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="360" src="https://img1.mydrivers.com/img/20210406/Sc55fdfdf-6815-4542-bb5d-36013564aa9b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
CMD也好，PowerShelly也好，开启后的默认目录都未必是最常用的</p>
<p>如果你经常在某个目录下使用CMD之类的命令行，将默认路径改为这个目录，自然方便得多。那么要怎么样自定义CMD、PowerShell之类工具的默认路径？一起来看看吧。</p>
<p>首先，我们需要使用微软最新开发的终端App。在Win10商店中，搜索“Windows Terminal”或者直接点击以下链接，下载安装即可。</p>
<p><strong>Windows终端App下载：<a class="f14_link" href="https://www.microsoft.com/store/productId/9N0DX20HK701" target="_blank">https://www.microsoft.com/store/productId/9N0DX20HK701</a></strong></p>
<p>这个Windows Terminal终端App，和系统自带的相比，界面要华丽得多，使用了最新的Fluent Design设计。</p>
<p>微软将会在今年发布Win10 21H2，届时Win10的UI会全面转变为Fluent Design，或许届时这款App也会成为系统的预装。</p>
<p>无论如何，这次我们先来了解它的自定义默认路径功能。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/4f91f2b4-e885-4a00-bad4-df44077da1c9.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="384" src="https://img1.mydrivers.com/img/20210406/S4f91f2b4-e885-4a00-bad4-df44077da1c9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Win10命令行App</p>
<p>开启终端App后，点击上方的下拉三角，即可找到“设置”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/821ba0aa-df82-4983-9017-507a1f4c00c4.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="384" src="https://img1.mydrivers.com/img/20210406/S821ba0aa-df82-4983-9017-507a1f4c00c4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
找到设置</p>
<p>点击“设置”，就会通过记事本来开启“settings.json”文件，我们通过编辑其中的参数，就可以对终端App进行设定了。</p>
<p>在“default”这一块的参数中，我们就能够编辑包括CMD、PowerShell乃至WSL的种种参数。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/fb75446e-fb18-4baa-999e-4c6c5a936a35.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="384" src="https://img1.mydrivers.com/img/20210406/Sfb75446e-fb18-4baa-999e-4c6c5a936a35.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
找到“Default”</p>
<p>要指定默认的路径，只需要添加以下字符到指定工具的“default”中：</p>
<p>"startingDirectory": "目录\\",</p>
<p>其中，“目录”由你自定义，例如你想要开启命令行，就默认是C盘的根目录，那么添加的字符就应该是：</p>
<p>"startingDirectory": "C:\\",</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/25ae8ccb-75b3-4ee8-8c35-a8de9bf98abf.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="331" src="https://img1.mydrivers.com/img/20210406/S25ae8ccb-75b3-4ee8-8c35-a8de9bf98abf.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
例如在命令行提示符的这个模块中，添加了这行代码，以后打开都会默认指向C盘根目录</p>
<p>在这里，我们可以给各种命令行工具都设定默认的开启路径，只需要找到对应的参数即可。这些参数很容易找到，在相应的字串中都标明了“命令行提示符”、“powershell”等等，大家可以自行动手。</p>
<p>修改后保存文件，再次开启终端App，可以看到默认开启的路径，就已经是刚刚设定的了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210406/7eec4672-9023-4562-a1df-f32aa4bb9137.png" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="338" src="https://img1.mydrivers.com/img/20210406/S7eec4672-9023-4562-a1df-f32aa4bb9137.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>总的来说，这是一个非常实用的小技巧。如果你经常使用命令行工具，遇到这方面的烦恼，不妨尝试一下！</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210406/a71005f8012a4d908d9d1a83acb1f3ad.jpg" target="_blank"><img alt="前所未有地便利！你可知Win10的CMD还能这么玩" h="337" src="https://img1.mydrivers.com/img/20210406/s_a71005f8012a4d908d9d1a83acb1f3ad.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1411/14117885.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            