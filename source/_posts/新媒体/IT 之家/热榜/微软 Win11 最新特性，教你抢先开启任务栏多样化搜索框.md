
---
title: '微软 Win11 最新特性，教你抢先开启任务栏多样化搜索框'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/7/e708fd61-a2c2-4628-ae2c-1063017b56c6.png'
author: IT 之家
comments: false
date: Sun, 17 Jul 2022 07:29:50 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/7/e708fd61-a2c2-4628-ae2c-1063017b56c6.png'
---

<div>   
<p data-vmark="f0c4"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 17 日消息，微软 7 月 14 日面向所有 Dev 开发人员推送了 <a href="https://www.ithome.com/0/629/466.htm" target="_blank">Windows 11 Insider Preview Build 25158 版本</a>，带来了多样化的任务栏搜索框。</p><p style="text-align: center;" data-vmark="8dff"><img src="https://img.ithome.com/newsuploadfiles/2022/7/e708fd61-a2c2-4628-ae2c-1063017b56c6.png" w="834" h="187" alt="任务栏上搜索条目的新视觉处理示例。" title="微软 Win11 最新特性，教你抢先开启任务栏多样化搜索框" width="834" height="184" referrerpolicy="no-referrer"></p><p data-vmark="4558"><span class="accentTextColor">微软将为不同的设备在任务栏上提供不同的“搜索”效果</span>，然而，并不是所有 Dev 频道的用户都可以体验到，那么现在，IT之家就教大家如何手动抢先开启。</p><h2 data-vmark="3a3a">开启方法：</h2><p data-vmark="8e10">首先，从 GitHub 下载 <a href="https://go.skimresources.com/?id=2728X590260&isjs=1&jv=15.2.4-stackpath&sref=https%3A%2F%2Fwww.neowin.net%2Fnews%2Fguide-how-to-enable-the-updated-taskbar-in-windows-11-dev-build-25158%2F&url=https%3A%2F%2Fgithub.com%2Fthebookisclosed%2FViVe%2Freleases&xs=1&xtz=-480&xuuid=d725e6e9f0e9d21f3c1c2bc2fc669ecf&xjsf=other_click__auxclick%20%5B2%5D" target="_blank">ViveTool 应用</a>，然后将文件提取到任意位置。</p><p data-vmark="b28e">接着，以<span class="accentTextColor">管理员身份</span>运行 Windows 终端，并使用 cd 命令转到 ViveTool 的文件夹。例如，cd C:ViveTool。</p><p data-vmark="887e">然后，输入以下命令，就可以在不同任务栏搜索框之间切换：</p><pre>.\vivetool /enable /id:39072097 /variant:数字</pre><p data-vmark="2027">其中的数字需要用以下替代：</p><ul class=" list-paddingleft-2"><li><p data-vmark="97c2">1 和 2 - 带有“搜索”字样的按钮；</p></li><li><p data-vmark="9e04">3 - 一个带有放大镜的按钮，里面有一个地球仪；</p></li><li><p data-vmark="39f7">4 - 一个带有地球仪和小放大镜的按钮；</p></li><li><p data-vmark="1a06">5 - “搜索网络”按钮。</p></li></ul><p data-vmark="6fe2">例如：</p><pre class="brush:javascript;toolbar:false ai-word-checked">.\vivetool /enable /id:39072097 /variant:4</pre><p data-vmark="ba47">最后，在任务管理器中重新启动 explorer.exe 进程，或者重新启动计算机，即可看到最新效果。</p><p data-vmark="bb2d">如果要还原更改，可以使用以下命令：</p><pre class="brush:javascript;toolbar:false">\vivetool /disable /id:39072097</pre>
          
</div>
            