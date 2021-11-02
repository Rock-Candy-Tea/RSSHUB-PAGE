
---
title: 'Win11 右键设计反人类？教你恢复完整右键菜单'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/3ed971b8-cce1-480f-9595-6b65d752e69a.jpg'
author: IT 之家
comments: false
date: Mon, 01 Nov 2021 15:16:05 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/3ed971b8-cce1-480f-9595-6b65d752e69a.jpg'
---

<div>   
<p data-vmark="2689">微软已经在 10 月 5 日发布了 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 正式版，很多朋友也已经升级了。不过对于 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 的一些新设计，并不是所有人都能适应的，例如新的右键快捷菜单，就不少朋友表示接受不了。</p><p data-vmark="32f0"><img src="https://img.ithome.com/newsuploadfiles/2021/11/3ed971b8-cce1-480f-9595-6b65d752e69a.jpg" w="411" h="383" title="Win11 右键设计反人类？教你恢复完整右键菜单" width="411" height="383" referrerpolicy="no-referrer"></p><p data-vmark="2537">Win11 的新右键菜单相比之前的旧款式，<span class="accentTextColor">颜值上的确大有提升</span>，不仅使用了 Fluent Design 设计语言，而且优化了文字排版，行间距更宽，便于阅读和触控。</p><p data-vmark="d7dd">然而，<span class="accentTextColor">Win11 的右键菜单隐藏了很多选项</span>，如果想要找到一些常用的功能，需要点击“显示更多选项”才能展开，这操作起来颇为麻烦。怎么办？今天就来给大家分享一些恢复 Win11 完整右键菜单的方法！</p><p data-vmark="49bb"><img src="https://img.ithome.com/newsuploadfiles/2021/11/672879e1-087a-42f0-a740-2946252a35ce.jpg" w="620" h="399" title="Win11 右键设计反人类？教你恢复完整右键菜单" width="620" height="399" referrerpolicy="no-referrer"></p><h2 data-vmark="7539">使用注册表修改</h2><p data-vmark="86b4">首先，通过修改注册表，我们就可以将 Win11 的右键菜单改为老样式。下面是具体的方法。</p><ul class=" list-paddingleft-2"><li><p data-vmark="0609">运行“regedit”，开启注册表编辑器，定位到“HKEY_CURRENT_USER\SOFTWARE\CLASSES\CLSID”；</p></li><li><p data-vmark="6152">接着，右键点击“CLSID”键值，新建一个名为 &#123;86ca1aa0-34aa-4e8b-a509-50c905bae2a2&#125; 的项；</p></li><li><p data-vmark="d414">右键点击新创建的项，新建一个名为 InprocServer32 的项，按下回车键保存；</p></li><li><p data-vmark="3aa6">最后选择新创建的项，然后双击右侧窗格中的默认条目，什么内容都不需要输入，按下回车键。</p></li></ul><p data-vmark="4a78">保存注册表后，重启 explorer.exe，即可看到右键菜单恢复成旧样式了。</p><p data-vmark="b500">如果想要恢复成为 Win11 的设计，那么删掉 InprocServer32 的项就可以了。</p><h2 data-vmark="2c8c">使用软件修改</h2><p data-vmark="7da0">注册表的操作比较复杂，没有经验的朋友容易出错，藉此我们也可以利用一些软件进行修改。例如这款“Windows 11 Classic Context Menu”。</p><p data-vmark="4a15">Windows 11 Classic Context Menu：<a href="https://www.sordum.org/14479/windows-11-classic-context-menu-v1-0/" target="_blank">点此直达</a></p><p data-vmark="67c8">Windows 11 Classic Context Menu 的原理是和上文修改注册表的方法一样的，只不过它将这些步骤封装成为了一个绿色小软件，点击一下就可以修改注册表，实现同样的功效。</p><p data-vmark="f643"><img src="https://img.ithome.com/newsuploadfiles/2021/11/f168efda-2b61-4a73-a588-457861049fc9.png" w="620" h="440" title="Win11 右键设计反人类？教你恢复完整右键菜单" width="620" height="440" referrerpolicy="no-referrer"></p><p data-vmark="f877">下载 Windows 11 Classic Context Menu 后，打开则可以看到三个选项，分别对应“经典右键菜单”、“默认右键菜单”和“重启 explorer.exe”。大家只需要点击切换菜单样式后，再点击重启 Explorer，就可以自由切换经典的菜单样式，和 Win11 默认的菜单样式了。</p><p data-vmark="f6e1"><img src="https://img.ithome.com/newsuploadfiles/2021/11/a15f6142-714c-4b86-a086-469505789b11.png" w="620" h="550" title="Win11 右键设计反人类？教你恢复完整右键菜单" width="620" height="550" referrerpolicy="no-referrer"></p><h2 data-vmark="9932">总结</h2><p data-vmark="95f2">总的来说，Win11 的一些设计的确引起了争议，除了右键菜单外，开始菜单和任务栏也有很多朋友表示难以适应。不过这些总有办法解决，之后我们还会介绍更多相关方法，来给用户更多切换会原先经典设计的选择。</p>
          
</div>
            