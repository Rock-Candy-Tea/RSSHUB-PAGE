
---
title: 'Win11最重磅的新功能？抢先体验文件管理多标签'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220709/S487358bd-23ab-4e42-a0b0-ae7d02ebff89.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 09 Jul 2022 00:22:30 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220709/S487358bd-23ab-4e42-a0b0-ae7d02ebff89.jpg'
---

<div>   
<p>我们知道，Windows的文件管理器长久一来都不支持多标签页，这使得如果你要同时访问多个目录的话，就必须开启多个窗口，霸占大量的屏幕面积不说，还占资源。微软终于要对此改进了，据报道，Win11在将来会为文件管理器加入多标签页的支持，而且有可能在今年的年度更新22H2中推送这个新特性。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220709/487358bd-23ab-4e42-a0b0-ae7d02ebff89.jpg" target="_blank"><img alt="Win11最重磅的新功能？抢先体验文件管理多标签" h="382" src="https://img1.mydrivers.com/img/20220709/S487358bd-23ab-4e42-a0b0-ae7d02ebff89.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>不过，也有消息称，Win11 22H2初版推送并不会带来多标签页的文件管理器，可能要再过一段时间才更新。无论如何，如果你已经等不及了的话，可以尝试以下的方法！</p>
<p>首先，需要加入Insider通道，选择Dev版本，将Win11升级为Windows 11 Build 22572以上。需要注意的是Windows 11 Build 25136之后的版本的具体操作和之前并不一样，下面会提到，这里使用Windows 11 Build 25136做示范。</p>
<p>接着，访问ViveTool的GitHub主页，下载ViveTool。</p>
<p><strong>ViveTool：https://github.com/thebookisclosed/ViVe/releases</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220709/d35ab5a1-d20d-4fdb-98eb-4eabf96b4c6e.png" target="_blank"><img alt="Win11最重磅的新功能？抢先体验文件管理多标签" h="372" src="https://img1.mydrivers.com/img/20220709/Sd35ab5a1-d20d-4fdb-98eb-4eabf96b4c6e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>将下载回来的压缩包解压到某个文件夹当中，记录下文件路径，例如C盘目录中的“ViveTool”文件夹。</p>
<p>接着，使用管理员权限运行cmd，定位到ViveTool的目录，具体命令如下：</p>
<p>cd [目录]</p>
<p>例如刚刚的路径是C盘的ViveTool文件夹，那么就输入以下命令：</p>
<p>cd C:\ViveTool</p>
<p>接着，输入以下命令，利用ViviTool来开启文件管理器的多标签特性：</p>
<p>vivetool addconfig 37634385 2</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220709/1162854e-bee5-4409-a13c-dd0a729fabad.png" target="_blank"><img alt="Win11最重磅的新功能？抢先体验文件管理多标签" h="290" src="https://img1.mydrivers.com/img/20220709/S1162854e-bee5-4409-a13c-dd0a729fabad.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>注意，如果系统版本比Windows 11 Build 25136更旧，但比Windows 11 Build 22572新（包含22572），那么则需要输入下面的命令：</p>
<p>vivetool addconfig 34370472 2</p>
<p>之后重启电脑，就可以看到文件管理器出现多标签页了！</p>
<p>如果你想要关闭掉这个特性，那么Windows 11 Build 25136或者更新的版本，可以使用下面的命令：</p>
<p>vivetool.exe delconfig 37634385</p>
<p style="text-align: center"><img alt="Win11最重磅的新功能？抢先体验文件管理多标签" h="251" src="https://img1.mydrivers.com/img/20220709/a8eebe41-8722-4fcb-9f0a-8144d5f4ec82.png" style="border: black 1px solid" w="571" referrerpolicy="no-referrer"></p>
<p>如果是比Windows 11 Build 25136旧、比Windows 11 Build 22572新的版本，则可以使用以下命令：</p>
<p>vivetool delconfig 34370472</p>
<p>输入命令运行后，重启电脑，就生效了。</p>
<p>总的来说，特定版本的Windows 11开启文件管理器多标签功能还是很方便的，主要是借助了ViveTool这款系统工具。希望微软能够早日推送文件管理器多标签的特性，带来更好的体验吧。</p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm">Windows操作系统</a><a href="https://news.mydrivers.com/tag/weiruan.htm">微软</a><a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a>  </p>
        
</div>
            