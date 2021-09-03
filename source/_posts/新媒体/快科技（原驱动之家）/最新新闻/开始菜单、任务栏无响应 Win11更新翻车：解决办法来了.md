
---
title: '开始菜单、任务栏无响应 Win11更新翻车：解决办法来了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210903/b94305f7-0e6a-472b-acdf-374d1c0bb2e4.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 03 Sep 2021 17:38:31 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210903/b94305f7-0e6a-472b-acdf-374d1c0bb2e4.jpg'
---

<div>   
<p class="MsoNormal">下个月初就要发布<span lang="EN-US">Win11</span>正式版了，今天微软又推送了一个重大版本的<span lang="EN-US">Win11</span>更新，<span lang="EN-US">beta</span>渠道升级后为<span lang="EN-US">Windows 11 build 22000.176</span>，<span lang="EN-US">Insider</span>渠道升级后是<span lang="EN-US">Windows 11 build 22449</span>，版本号首次超越<span lang="EN-US">22000</span>。</p>
<p class="MsoNormal">这版升级带来的变化不少，包括启动动画、蓝牙、通知中心等等，<a class="f14_link" href="https://news.mydrivers.com/1/780/780786.htm" target="_blank">详细情况见之前的文章。</a></p>
<p class="MsoNormal">然而重大版本更新不翻车就不是微软的习惯，<span style="color:#ff0000;"><strong>这版<span lang="EN-US">Win11</span>出现了开始菜单、任务栏无响应的问题，有不少人中招了。</strong></span></p>
<p class="MsoNormal">废话不多说，现在网上已经有临时的解决办法了，操作步骤如下：</p>
<p class="MsoNormal">使用<span lang="EN-US"> Ctrl-Alt-Del </span>打开任务管理器</p>
<p class="MsoNormal">选择“详细信息”选项以切换到高级视图</p>
<p class="MsoNormal">从“文件”菜单中选择“运行新任务”</p>
<p class="MsoNormal">在打开的窗口中输入“<span lang="EN-US">cmd”</span>，点击<span lang="EN-US">“</span>确定<span lang="EN-US">”</span></p>
<p class="MsoNormal">在打开的命令行中，现在必须输入命令：</p>
<p class="MsoNormal"><strong>“<span lang="EN-US">reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0”</span></strong></p>
<p class="MsoNormal">按回车键后，电脑重新启动，之后开始菜单和任务栏就正常了。</p>
<p class="MsoNormal">还有一种方法就是卸载最新更新，操作步骤跟上面差不多，不同的是在运行新任务的时候选择控制面板，再转到程序<span lang="EN-US">-</span>程序及应用<span lang="EN-US">-</span>查看已安装的更新，<span style="color:#ff0000;"><strong>找到<span lang="EN-US">Update for Microsoft Windows (KB5006050)</span>补丁并卸载。</strong></span></p>
<p class="MsoNormal">好消息是微软现在已经停止了有问题的推送，服务器端已经升级了最新的补丁，后面在升级的话应该就是正常的了——希望如此。</p>

<p class="MsoNormal" style="text-align: center;"><img alt="开始菜单、任务栏无响应 Win11更新翻车：解决办法来了" h="375" src="https://img1.mydrivers.com/img/20210903/b94305f7-0e6a-472b-acdf-374d1c0bb2e4.jpg" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            