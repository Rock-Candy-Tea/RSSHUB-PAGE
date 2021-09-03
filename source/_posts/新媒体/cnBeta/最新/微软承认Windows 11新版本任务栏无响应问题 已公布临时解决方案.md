
---
title: '微软承认Windows 11新版本任务栏无响应问题 已公布临时解决方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0903/91285601e3b8472.jpg'
author: cnBeta
comments: false
date: Fri, 03 Sep 2021 06:35:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0903/91285601e3b8472.jpg'
---

<div>   
今天面向 Beta 频道发布的 Windows 11 Build 22000.176 更新存在一个问题，那就是开始和任务栏没有反应，设置和操作系统的其他区域无法加载。目前微软已经承认了这个问题，并中止继续向 Insider 成员推送该版本。而目前已经升级新版本的用户则提供了一个临时解决方案。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0903/91285601e3b8472.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0903/91285601e3b8472.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0903/8f08f0a82af904d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0903/8f08f0a82af904d.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在推文中写道：“再次感谢 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Insider 的耐心。如果您受到这个问题的影响，您可以按照添加到这些博客文章顶部的步骤，在您的 PC 上重新进入工作状态”。</p><p style="text-align: left;">目前已经升级到新版本出现问题的用户，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>也提供了一个临时解决方案</p><p style="text-align: left;">1. 使用 Ctrl+Alt+Del 来打开任务管理器</p><p style="text-align: left;">2. 在任务管理器中选择“更多细节”来扩展任务管理器</p><p style="text-align: left;">3. 访问“文件”并选择“运行新任务”</p><p style="text-align: left;">4. 在“打开”栏中输入“cmd”</p><p style="text-align: left;">5. 复制并粘贴“reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0”（所有内容均为粗体，不包括“”）</p><p style="text-align: left;">6. 点击回车，然后你的电脑应该重新启动。重启后，一切都应该恢复正常。</p>   
</div>
            