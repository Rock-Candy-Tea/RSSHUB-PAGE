
---
title: 'Windows 10任务栏_新闻和兴趣_更新已广泛安装 但不是每个人都能看到'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0503/a661ba911fd646c.jpg'
author: cnBeta
comments: false
date: Sun, 02 May 2021 23:59:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0503/a661ba911fd646c.jpg'
---

<div>   
Windows 10的新任务栏馈送功能于4月公布，称为 "新闻和兴趣"，但很多用户报告说，即使应用了Windows 10
KB5001391，该小工具也没有启用。对于那些不知道的人来说，任务栏Feeds，也被称为 "Windows
Feeds"是建立在Microsoft News新闻网络之上的新闻馈送。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0503/a661ba911fd646c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0503/a661ba911fd646c.jpg" title alt="Taskbar-newsfeed.jpg" referrerpolicy="no-referrer"></a><br></p><p>它将被直接内置到任务栏中，并且会自动更新。启用后，用户不必打开浏览器就可以获取新闻或天气更新。</p><p>该功能是可选的，你可以通过右键单击它来轻松删除它。你还可以通过使用 "更多内容"或 "更少这样的内容"等选项对各种新闻主题进行个性化定制。据该公司称，这些新闻将来自4500多个来源，如BBC、CNN和福克斯新闻。</p><p>在KB5001391更新的发布说明中，微软宣布了 "新闻和兴趣"反馈的可用性。不幸的是，根据几个用户的报告，该功能还没有对所有用户开放。看起来，更广泛的推广预计要到本月底才能实现。</p><p>微软意识到了这一点，但该公司会选择维持这种AB测试的形式发布新功能。微软认为，向少数用户发布功能可以提高更新的质量，并允许其在向所有人推出之前解决任何大的错误或者是带来更好的解决方案。</p><p>在测试中，我们观察到，该功能甚至都不能使用组策略编辑器或注册表编辑器强制启用。任务栏的新闻传送功能可以通过注册表编辑器的以下目录进行管理。</p><p>HKEY_LOCAL_MACHINE/SOFTWARE/Policies/Microsoft/<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>/Windows Feeds</p><p>你也可以用组策略编辑器管理任务栏的新闻源。在组策略编辑器中，导航到计算机配置>管理模板>Windows组件，"新闻和兴趣"将在这里出现。</p><p>在某些情况下，收到该功能的用户观察到，"新闻和兴趣"Feeds崩溃时出现一个空白窗口，但可以通过重新启动Windows Explorer（Explorer.exe）来恢复。</p><p>在未来几周内，"新闻和兴趣"反馈将通过服务器端的更新自动启用。预计更多的用户将在5月11日收到该功能，而其他用户将在本月底或6月收到该功能。</p>   
</div>
            