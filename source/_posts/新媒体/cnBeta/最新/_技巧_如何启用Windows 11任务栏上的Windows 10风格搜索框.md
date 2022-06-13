
---
title: '_技巧_如何启用Windows 11任务栏上的Windows 10风格搜索框'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0613/35f6970c408fa60.jpg'
author: cnBeta
comments: false
date: Mon, 13 Jun 2022 08:53:48 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0613/35f6970c408fa60.jpg'
---

<div>   
对于追求简洁桌面体验的用户来说，或许会在拿到 Windows 10 设备的第一时间，就将任务栏上的非常用功能都给隐藏或关闭掉（比如小编）。<strong>但若你想要在更加一刀切的 Windows 11 任务栏上重新嵌入搜索框，Techdows 也刚刚分享了一招独特的技巧。</strong><br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0613/35f6970c408fa60.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://techdows.com/2022/06/windows-11-search-bar-in-taskbar.html" target="_self">Techdows</a>）</p><p>尽管<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>尚未官宣，但 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 的 Insider 测试者们，<strong>现可尝试在 Build 25136 预览编译版本中执行如下操作：</strong></p><blockquote><p>（1）从 Github 下载 Vivetool；</p><p>（2）将之提取到指定的文件路径；</p><p>（3）以管理员身份打开 CMD 命令提示符；</p><p>（4）使用 CD 命令，转到 Vivetool 路径；</p><p>（5）执行 vivetool addconfig 37010913 2 命令；</p><p>（6）打开 任务管理器，并重启 Explorer.exe 文件资源管理器进程。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0613/f49e0f5db614479.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>如果没有立即看到 Windows 11 任务栏上的搜索框，还请尝试重启计算机。</p><p>不过截止发稿时，Techdows 编辑未能在将鼠标悬停于搜索框上时，看到近期的搜索历史。</p><p>当然，对此感到不习惯的用户，仍可使用点击“开始”菜单（或使用 WinKey）执行搜索。</p><p><strong>想要关闭任务栏搜索框的话，可参考如下步骤：</strong></p><blockquote><p>（1）右键单击 任务栏；</p><p>（2）选择 任务栏设置；</p><p>（3）转至 个性化 → 任务栏 项目；</p><p>（4）通过开关来 启用 / 关闭 搜索框。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0613/c093803ccb6a99b.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p><strong>如果想恢复 Windows 11 的默认设置（禁用 / 移除任务栏上的搜索框），可再次运行 Vivetool：</strong></p><blockquote><p>（1）转至 Vivetool 文件路径；</p><p>（2）以 管理员身份，打开 CMD 命令提示符；</p><p>（3）复制粘贴 Vivetool delconfig 37010913 2 命令；</p><p>（4）确认执行。</p></blockquote><p>【注意】回车确认后，若修改未能即刻生效，还请尝试重启计算机。</p><p>此外由于 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://vivo.jd.com/" target="_blank">vivo</a>Tool 属于第三方工具软件，使用时还请自担相关风险。</p>   
</div>
            