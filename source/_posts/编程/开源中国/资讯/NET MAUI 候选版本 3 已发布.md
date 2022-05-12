
---
title: '.NET MAUI 候选版本 3 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7a567032070e3f4d1a29b98d6c40311a54b.png'
author: 开源中国
comments: false
date: Thu, 12 May 2022 07:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7a567032070e3f4d1a29b98d6c40311a54b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NET MAUI （多平台应用程序 UI）候选版本 3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-maui-rc-3%2F" target="_blank">已发布</a>！其中包含一批新的改进，比如使用 <strong>shell 控件</strong>实现导航。</p> 
<p>与以前的候选版本一样，RC3 包含在“上线”支持政策中，这意味着微软为开发者的生产级应用程序提供  .NET MAUI支持。</p> 
<h2>导航优化：<strong>shell 控件</strong></h2> 
<p>.NET MAUI 提供了两种在应用程序中实现导航的主要方法。其中，简单但功能强大的选项是在 <code><span>Shell</span></code>中运行应用程序，<code><span>Shell</span></code>是一个 UI 控件，用于托管应用程序页面并提供弹出菜单和选项卡菜单，且提供针对桌面和移动双模式优化的详细信息。</p> 
<p>第二种选择是直接使用基本导航页面控件：FlyoutPage、TabbedPage 和 NavigationPage。两种方法的属性对比：</p> 
<p><img height="258" src="https://oscimg.oschina.net/oscnet/up-7a567032070e3f4d1a29b98d6c40311a54b.png" width="500" referrerpolicy="no-referrer"></p> 
<p>模板项目包括一个带有单个页面的“AppShell.xaml”，并将其分配给 App.MainPage。 要查看浮出控件，只需添加更多页面，并通过更改 Shell.FlyoutBehavior 来启用浮出控件。</p> 
<pre><code><Shell
    x:Class="MauiApp2.AppShell"
    xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:MauiApp2"
    Shell.FlyoutBehavior="Flyout">

    <ShellContent
        Title="Home"
        ContentTemplate="&#123;DataTemplate local:MainPage&#125;"
        Route="MainPage" />

    <ShellContent
        Title="Items"
        ContentTemplate="&#123;DataTemplate local:ItemsPage&#125;"
        Route="ItemsPage" />

</Shell></code></pre> 
<p><img alt height="129" src="https://oscimg.oschina.net/oscnet/up-765780f7fc2aeee436c87c4360303926c28.png" width="700" referrerpolicy="no-referrer"></p> 
<p><code><span>ShellContent</span></code>能够描述用于导航的 URI 路由，并使用数据模板，以便按需加载页面以保持启动性能。比如可以将<code><span>ShellContent</span></code>导航别名包装起来，以清楚地指示 Shell 如何呈现 UI。</p> 
<pre><code><FlyoutItem Title="Home" FlyoutIcon="home.png">
    <ShellContent ...>
</FlyoutItem>

<FlyoutItem Title="Items" FlyoutIcon="store.png">
    <ShellContent ...>
</FlyoutItem></code></pre> 
<p>Shell 支持浮出控件的许多自定义，包括设置背景样式、覆盖内容的背景、模板页眉、页脚、整个内容或仅菜单项。还可以设置弹出按钮的宽度，并使其保持打开或完全隐藏。以下是一些不同设计的示例：</p> 
<p><img alt height="403" src="https://oscimg.oschina.net/oscnet/up-455aa93ad672648311c56d9517eb6823701.png" width="700" referrerpolicy="no-referrer"></p> 
<p>有关使用 Shell 导航的更多信息，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Ffundamentals%2Fshell%2Fnavigation" target="_blank">Shell 文档</a>。 </p> 
<p>有关 .NET MAUI 候选版本 3 的更多内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-maui-rc-3%2F" target="_blank">官方博客</a>。</p>
                                        </div>
                                      
</div>
            