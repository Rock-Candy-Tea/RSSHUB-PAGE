
---
title: '_图_微软详解Windows 11右键菜单和共享菜单的改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0720/053a47490306f6c.jpg'
author: cnBeta
comments: false
date: Tue, 20 Jul 2021 02:19:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0720/053a47490306f6c.jpg'
---

<div>   
<a href="https://blogs.windows.com/windowsdeveloper/2021/07/19/extending-the-context-menu-and-share-dialog-in-windows-11/" target="_blank">在今天发布的官方博文中</a>，微软详细介绍了 Windows 11 系统中对右键菜单和共享菜单的改进。右键菜单是 Windows 系统中最受欢迎的功能之一，但它也存在很多不足。在即将到来的 Windows 11 系统中，微软正通过以下改变和改进来修复和改进：<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0720/053a47490306f6c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0720/053a47490306f6c.jpg" alt="全景图.jpg" referrerpolicy="no-referrer"></a></p><blockquote style="text-align: left;"><p style="text-align: left;">● 在右键菜单被调用的时候常见命令会放置在右侧</p><p style="text-align: left;">● “打开”和“打开方式”被归为一组</p><p style="text-align: left;">● 应用程序使用 IExplorerCommand + 应用程序身份识别来扩展菜单选项。未打包的 Win32 应用程序可以使用稀疏的 Manifests。IExplorerCommand 支持延伸到 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 7。</p><p style="text-align: left;">● 应用程序扩展被分组在一起，并放在 Shell 动作下方</p><p style="text-align: left;">● Cloud 文件的应用程序被放置在 Shell 命令旁边，以便于 hydrate 或者 dehydrate 文件</p><p style="text-align: left;">● 具有 1 个以上动作的应用程序被分组到一个带有应用程序属性的弹出菜单。</p><p style="text-align: left;">● “显示更多选项”按原样加载 Windows 10 右键菜单，以访问低使用率的 Shell 动作和仍在进行移植的应用程序。没有命令被完全删除。</p><p style="text-align: left;">● Shift-F10 或键盘菜单键也将加载 Windows 10 右键菜单。</p></blockquote><p style="text-align: left;">和右键菜单一样，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>也在积极改进 Windows 11 系统中的共享菜单。以下共享菜单的改进将在 Windows 11 中出现：</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0720/ebe7c435163cb3e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0720/ebe7c435163cb3e.jpg" referrerpolicy="no-referrer"></a></p><blockquote style="text-align: left;"><p style="text-align: left;">● Nearby Sharing 更易用。在上面可以轻松控制你的可发现性设置，在对话框的页脚有一个指向更多设置的链接。</p><p style="text-align: left;">● 如果你使用邮件应用，联系人列表中的第一个条目可以帮助你轻松发送电子邮件给自己。</p><p style="text-align: left;">● 所有的应用程序现在都可以作为目标参与到共享对话框中。对于未打包的Win32应用程序，这在与上下文菜单相同的样本中涵盖。如果通过Microsoft Edge安装的PWA实现了Web Share Target API，也会得到支持。</p></blockquote>   
</div>
            