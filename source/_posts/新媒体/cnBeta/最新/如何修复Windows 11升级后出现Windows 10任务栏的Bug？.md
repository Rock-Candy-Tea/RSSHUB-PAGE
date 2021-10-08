
---
title: '如何修复Windows 11升级后出现Windows 10任务栏的Bug？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1006/6a2d5f6d5cf2076.png'
author: cnBeta
comments: false
date: Fri, 08 Oct 2021 06:04:58 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1006/6a2d5f6d5cf2076.png'
---

<div>   
微软已经面向公众发布了Windows 11，并可用于符合条件的设备。一些从Windows
10升级的用户报告说，他们没有收到新的任务栏，而且"开始"菜单也不工作。<strong>在Windows
11测试版期间，内部人士也报告了同样的问题，这意味着这个错误也影响到了生产版本。如果你也受到影响，这里有潜在的修复方法，你可以试试。</strong><br>
<p><a href="https://static.cnbetacdn.com/thumb/article/2021/1006/6a2d5f6d5cf2076.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1006/6a2d5f6d5cf2076.png" referrerpolicy="no-referrer"></a></p><p>Windows 11带有一个居中的任务栏和开始菜单。用户在清洁安装<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的新操作系统时，可能会得到比选择升级时更新鲜的体验。</p><p>随着升级，在某些情况下，开始菜单和任务栏不会得到更新，其中任务栏看起来与Windows 10风格一致，而开始菜单则根本不工作。</p><p><strong>前段时间，微软自己建议受影响的运行Beta通道的内部人士进行以下修复操作，以下是你需要做的：</strong></p><ol style="list-style-type: decimal;" class=" list-paddingleft-2"><li><p>打开设置>Windows更新>更新历史</p></li><li><p>卸载最新的累积更新，KB5004300</p></li><li><p>在提示时重新启动你的设备</p></li></ol><p>访问Windows Update并再次检查更新，当KB5004300被提供时，再次重新安装它。这就使居中的Windows 11任务栏和开始菜单恢复到正常的工作状态。</p><p><strong>如果上述步骤帮助你恢复了Windows 11任务栏，但"开始菜单"仍然无法使用，请尝试以下步骤：</strong></p><p>1. 打开任务管理器</p><p>2. 点击文件>运行新任务</p><p>3. 输入Powershell并勾选"以管理权限创建此任务"。</p><p>4. 在PowerShell窗口中，复制并粘贴以下内容并按回车键</p><blockquote><p>Get-appxpackage -all *shellexperience* -packagetype bundle |% &#123;add-appxpackage -register -disabledevelopmentmode ($_.installlocation +"\appxmet<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://adata.jd.com/" target="_blank">ADATA</a>\appxbundlemanifest.xml")&#125;</p></blockquote><p>5. 显示指示完成之后重新启动系统。</p><p><strong>如果上面的步骤没有帮助，可以创建一个具有管理权限的本地用户账户，并将所有东西移到该账户中。</strong></p><p>正如开头所说，这个问题并不影响已经清洁安装了Windows 11的用户，这可能是你最后的选择，你可以尝试一下，如果上述操作没有任何效果的话。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1187103.htm" target="_blank">一些Windows 11用户发现Windows 10任务栏“意外回归”</a></p></div>   
</div>
            