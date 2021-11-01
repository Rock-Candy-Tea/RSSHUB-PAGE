
---
title: 'Win11右键设计反人类？教你恢复完整右键菜单'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211101/3f014e8c-2c21-4476-bda0-56d61dd08552.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 01 Nov 2021 14:19:43 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211101/3f014e8c-2c21-4476-bda0-56d61dd08552.jpg'
---

<div>   
<p>]微软已经在10月5日发布了Windows 11正式版，很多朋友也已经升级了。不过对于Win11的一些新设计，并不是所有人都能适应的，例如新的右键快捷菜单，就不少朋友表示接受不了。</p>
<p style="text-align: center"><img alt="Win11右键设计反人类？教你恢复完整右键菜单" h="383" src="https://img1.mydrivers.com/img/20211101/3f014e8c-2c21-4476-bda0-56d61dd08552.jpg" style="border: black 1px solid" w="411" referrerpolicy="no-referrer"></p>
<p>Win11的新右键菜单相比之前的旧款式，颜值上的确大有提升，不仅使用了Fluent Design设计语言，而且优化了文字排版，行间距更宽，便于阅读和触控。</p>
<p>然而，Win11的右键菜单隐藏了很多选项，如果想要找到一些常用的功能，需要点击“显示更多选项”才能展开，这操作起来颇为麻烦。</p>
<p>怎么办？今天就来给大家分享一些恢复Win11完整右键菜单的方法！</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/f718d6e1-75e5-412f-b6bf-35ccb9df032c.jpg" target="_blank"><img alt="Win11右键设计反人类？教你恢复完整右键菜单" h="386" src="https://img1.mydrivers.com/img/20211101/Sf718d6e1-75e5-412f-b6bf-35ccb9df032c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>使用注册表修改</strong></p>
<p>首先，通过修改注册表，我们就可以将Win11的右键菜单改为老样式。下面是具体的方法。</p>
<p>·运行“regedit”，开启注册表编辑器，定位到“HKEY_CURRENT_USER\SOFTWARE\CLASSES\CLSID”；</p>
<p>·接着，右键点击“CLSID”键值，新建一个名为&#123;86ca1aa0-34aa-4e8b-a509-50c905bae2a2&#125;的项；</p>
<p>·右键点击新创建的项，新建一个名为InprocServer32的项，按下回车键保存；</p>
<p>·最后选择新创建的项，然后双击右侧窗格中的默认条目，什么内容都不需要输入，按下回车键。</p>
<p>保存注册表后，重启explorer.exe，即可看到右键菜单恢复成旧样式了。</p>
<p>如果想要恢复成为Win11的设计，那么删掉InprocServer32的项就可以了。</p>
<p><strong>使用软件修改</strong></p>
<p>注册表的操作比较复杂，没有经验的朋友容易出错，藉此我们也可以利用一些软件进行修改。例如这款“Windows 11 Classic Context Menu”。</p>
<p><strong>Windows 11 Classic Context Menu：<a class="f14_link" href="https://www.sordum.org/14479/windows-11-classic-context-menu-v1-0/" target="_blank">https://www.sordum.org/14479/windows-11-classic-context-menu-v1-0/</a></strong></p>
<p>Windows 11 Classic Context Menu的原理是和上文修改注册表的方法一样的，只不过它将这些步骤封装成为了一个绿色小软件，点击一下就可以修改注册表，实现同样的功效。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/e5511c49-75aa-4b6e-9afb-04f2d992af7a.png" target="_blank"><img alt="Win11右键设计反人类？教你恢复完整右键菜单" h="425" src="https://img1.mydrivers.com/img/20211101/Se5511c49-75aa-4b6e-9afb-04f2d992af7a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>下载Windows 11 Classic Context Menu后，打开则可以看到三个选项，分别对应“经典右键菜单”、“默认右键菜单”和“重启explorer.exe”。</p>
<p>大家只需要点击切换菜单样式后，再点击重启Explorer，就可以自由切换经典的菜单样式，和Win11默认的菜单样式了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/237b9749-16da-4007-9a28-a89fed0913bf.png" target="_blank"><img alt="Win11右键设计反人类？教你恢复完整右键菜单" h="532" src="https://img1.mydrivers.com/img/20211101/S237b9749-16da-4007-9a28-a89fed0913bf.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>总结</strong></p>
<p>总的来说，Win11的一些设计的确引起了争议，除了右键菜单外，开始菜单和任务栏也有很多朋友表示难以适应。不过这些总有办法解决，之后我们还会介绍更多相关方法，来给用户更多切换会原先经典设计的选择。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211101/7fd006b384e743c4b31dfb7d1f4a1933.jpg" target="_blank"><img alt="Win11右键设计反人类？教你恢复完整右键菜单" h="400" src="https://img1.mydrivers.com/img/20211101/s_7fd006b384e743c4b31dfb7d1f4a1933.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win11/1463/14637599.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            