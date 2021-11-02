
---
title: '跟 Win10 相同，Win11 也会在 System32 目录下创建大量空文件夹'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/26f5f5b2-f121-40de-b021-27648c9bf003.png'
author: IT 之家
comments: false
date: Tue, 02 Nov 2021 01:24:06 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/26f5f5b2-f121-40de-b021-27648c9bf003.png'
---

<div>   
<p data-vmark="b375"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 2 日消息，据 gHacks 报道，不少用户反映称，似乎跟 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 一样，<a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 操作系统也会在 System32 目录下创建数百至数千个空文件夹。</p><p data-vmark="8910"><img src="https://img.ithome.com/newsuploadfiles/2021/11/26f5f5b2-f121-40de-b021-27648c9bf003.png" w="1036" h="681" title="跟 Win10 相同，Win11 也会在 System32 目录下创建大量空文件夹" width="1036" height="539" referrerpolicy="no-referrer"></p><p data-vmark="7ad3">据悉，这些文件夹是由供应包运行时处理工具（ProvTool.exe）创建的，这些文件夹以 tw 开头，以.tmp 结尾。当打开它们时，会发现它们不包含任何文件。可以删除，删除似乎对系统没有负面影响。</p><p data-vmark="80eb">这个问题自 2019 年以来一直存在于 Windows 10 中，现在看来 Windows 11 也继承下来了。</p><p data-vmark="d851">IT之家了解到，这个 bug 似乎不会对系统造成任何影响，<span class="accentTextColor">空的文件夹不会占用很多磁盘空间，也不会干扰系统的运行</span>。如果你想检查你的电脑是否受到影响，并清理一下，可以在 C:\Windows\System32\config\systemprofile\AppData\Local 查看，有些文件夹可能是隐藏的，可能需要打开“显示隐藏的操作系统文件”选项。</p><p data-vmark="faff">这个 bug 再次表明，Windows 11 与 Windows 10 非常相似，Windows 10 存在的 bug 很可能 Windows 11 也会存在。</p>
          
</div>
            