
---
title: 'Windows 11右键设计反人类？教您恢复旧版右键菜单'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1101/227f6d1fe829d7d.jpg'
author: cnBeta
comments: false
date: Mon, 01 Nov 2021 06:36:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1101/227f6d1fe829d7d.jpg'
---

<div>   
微软已经在10月5日发布了Windows 11正式版，很多朋友也已经升级了。不过对于Windows 11的一些新设计，并不是所有人都能适应的，例如新的右键快捷菜单，就不少朋友表示接受不了。Windows 11的新右键菜单相比之前的旧款式，颜值上的确大有提升，不仅使用了Fluent Design设计语言，而且优化了文字排版，行间距更宽，便于阅读和触控。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1101/227f6d1fe829d7d.jpg" referrerpolicy="no-referrer"><br></p><p>然而，Windows 11的右键菜单隐藏了很多选项，如果想要找到一些常用的功能，需要点击“显示更多选项”才能展开，这操作起来颇为麻烦。怎么办？今天就来给大家分享一些恢复Windows 11完整右键菜单的方法！</p><p><img src="https://static.cnbetacdn.com/article/2021/1101/9762daae435cd7a.jpg" referrerpolicy="no-referrer"><br></p><p><strong>使用注册表修改</strong></p><p>首先，通过修改注册表，我们就可以将Windows 11的右键菜单改为老样式。下面是具体的方法。</p><p>·运行“regedit”，开启注册表编辑器，定位到“HKEY_CURRENT_USERSOFTWARECLASSESCLSID”；</p><p>·接着，右键点击“CLSID”键值，新建一个名为&#123;86ca1aa0-34aa-4e8b-a509-50c905bae2a2&#125;的项；</p><p>·右键点击新创建的项，新建一个名为InprocServer32的项，按下回车键保存；</p><p>·最后选择新创建的项，然后双击右侧窗格中的默认条目，什么内容都不需要输入，按下回车键。</p><p>保存注册表后，重启explorer.exe，即可看到右键菜单恢复成旧样式了。</p><p>如果想要恢复成为Windows 11的设计，那么删掉InprocServer32的项就可以了。</p><p><strong>使用软件修改</strong></p><p>注册表的操作比较复杂，没有经验的朋友容易出错，藉此我们也可以利用一些软件进行修改。例如这款“Windows 11 Classic Context Menu”。</p><p><strong>Windows 11 Classic Context Menu：<a href="https://www.sordum.org/14479/windows-11-classic-context-menu-v1-0/">https://www.sordum.org/14479/windows-11-classic-context-menu-v1-0/</a></strong></p><p>Windows 11 Classic Context Menu的原理是和上文修改注册表的方法一样的，只不过它将这些步骤封装成为了一个绿色小软件，点击一下就可以修改注册表，实现同样的功效。</p><p><img src="https://static.cnbetacdn.com/article/2021/1101/289cd926118f3af.png" referrerpolicy="no-referrer"><br></p><p>下载Windows 11 Classic Context Menu后，打开则可以看到三个选项，分别对应“经典右键菜单”、“默认右键菜单”和“重启explorer.exe”。大家只需要点击切换菜单样式后，再点击重启Explorer，就可以自由切换经典的菜单样式，和Windows 11默认的菜单样式了。</p><p><img alt="Windows 11右键菜单" src="https://img0.pconline.com.cn/pconline/2110/22/14637599_3_thumb.png" title="Windows 11右键菜单" width="620" height="550" referrerpolicy="no-referrer"><br></p><p><strong>总结</strong></p><p>总的来说，Windows 11的一些设计的确引起了争议，除了右键菜单外，开始菜单和任务栏也有很多朋友表示难以适应。不过这些总有办法解决，之后我们还会介绍更多相关方法，来给用户更多切换会原先经典设计的选择。</p>   
</div>
            