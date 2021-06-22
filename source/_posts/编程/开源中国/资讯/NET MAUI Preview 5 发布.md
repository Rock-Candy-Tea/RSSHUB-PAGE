
---
title: '.NET MAUI Preview 5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-964bd6b667d506209216e1a9aa19cde9768.png'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 07:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-964bd6b667d506209216e1a9aa19cde9768.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>.NET MAUI Preview 5 已发布。在此版本中，开发团队启用了动画和视图转换 (view transformation) 功能、完成了多个 UI 组件的移植，并对单个项目模板进行了改进。此外还发布了第一批涵盖 .NET MAUI 介绍和基础方面的预览文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2F" target="_blank">https://docs.microsoft.com/dotnet/maui/</a>。</p> 
<h3>动画</h3> 
<p>目前 .NET MAU 提供了多种方法执行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Fanimation%2F" target="_blank">动画</a>，其中最简单的是利用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Fanimation%2Fsimple" target="_blank">视图扩展方法</a>，例如<code>FadeTo</code>, <code>RotateTo</code>, <code>ScaleTo</code>, <code>TranslateTo</code>等等。在以下示例中，通过使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1200" target="_blank"><code>HandlerAttached</code></a>新事件获取对绑定到布局的每个视图的引用：</p> 
<pre><code><DataTemplate x:Key="FavouriteTemplate">
    <Frame
        AttachedHandler="OnAttached"
        Opacity="0">
        ...
    </Frame>
</DataTemplate></code></pre> 
<pre><code><FlexLayout
    BindableLayout.ItemTemplate="&#123;StaticResource FavouriteTemplate&#125;"
    BindableLayout.ItemsSource="&#123;Binding Favorites&#125;"
    >
    ...
</FlexLayout></code></pre> 
<p>当页面出现时，将视图以轻微交错的方式进行动画处理，以创建美丽的层叠效果。</p> 
<pre><code>public partial class FavoritesPage : ContentPage
&#123;
    List<Frame> tiles = new List<Frame>();

    void OnAttached(object sender, EventArgs e)
    &#123;

        Frame f = (Frame)sender;
        tiles.Add(f);
    &#125;

    protected override async void OnAppearing()
    &#123;
        base.OnAppearing();

        await Task.Delay(300);
        TransitionIn();
    &#125;

    async void TransitionIn()
    &#123;
        foreach (var item in tiles)
        &#123;
            item.FadeTo(1, 800);
            await Task.Delay(50);
        &#125;
    &#125;    
&#125;</code></pre> 
<p>如需了解更完整的视图动画编排，查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Fanimation%2Fcustom" target="_blank">自定义动画文档</a>，该<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Fanimation%2Fcustom" target="_blank">文档</a>演示了添加多个可以并行运行的子动画。</p> 
<h3>UI 组件</h3> 
<p>在这个版本中，多个控件的所有属性和事件都被移植到了 Xamarin.Forms 渲染器架构的处理程序中，包括<code>ActivityIndicator</code>, <code>CheckBox</code>, <code>Image</code>和<code>Stepper</code>。在之前的预览版中，开发者需要检查是否移植了控件并从兼容包中为不可用的渲染器注册渲染器。而在 .NET MAUI Preview 5 中，通过更新<code>UseMauiApp</code>扩展（参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fwiki%2FApplication-Startup" target="_blank">Startup wiki</a>）来为开发者连接所有控件，无论它们是基于处理程序还是渲染器，从而使这变得更加容易。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-964bd6b667d506209216e1a9aa19cde9768.png" referrerpolicy="no-referrer"></p> 
<p>Preview 5 的另一项新功能是首次引入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fapp-fundamentals%2Fshell%2F" target="_blank"><code>Shell</code></a>，这是一个应用程序容器，提供 URI 导航，以及实现弹出菜单和选项卡的快速方法。</p> 
<h3>单个项目模板更新</h3> 
<p>开发团队在此版本中取得了进展：将多个 WinUI 项目合并为一个。现在，当创建一个项目时 (<code>dotnet new maui</code>)，开发者将看到两个项目：多目标的 .NET MAUI 项目和 WinUI 项目。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0e739765f55e88019550a2fc7a096d78ae9.png" referrerpolicy="no-referrer"></p> 
<p>有关 .NET MAUI 入门的其他信息，参阅新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui" target="_blank">文档网站</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-maui-preview-5%2F" target="_blank">详细更新内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            