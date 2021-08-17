
---
title: '.NET MAUI Preview 7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb987d3b486cdf0a122db389bb9032f901a.png'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 06:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb987d3b486cdf0a122db389bb9032f901a.png'
---

<div>   
<div class="content">
                                                                                            <p>.NET MAUI Preview 7 现已发布。该版本中引入了新的布局，此举是对性能和可靠性的重大改变。同时还基于新的 SemanticService、字体缩放选项、对 Xamarin.Forms 效果的兼容性支持等引入了一些新的以可访问性为重点的功能。</p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-cb987d3b486cdf0a122db389bb9032f901a.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong>新布局</strong></h4> 
<p>在此预览版中，旧的布局现在只能在 Microsoft.Maui.Controls.Compatibility 命名空间中找到，而新的布局则默认启用：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Flayouts%2Fgrid" target="_blank">Grid</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Flayouts%2Fflex-layout" target="_blank">FlexLayout</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Flayouts%2Fstacklayout" target="_blank">StackLayout</a> 
  <ul> 
   <li>HorizontalStackLayout</li> 
   <li>VerticalStackLayout</li> 
  </ul> </li> 
</ul> 
<p>StackLayout 现在 包含 两个专注于水平和垂直方向的布局，用户可按需选择。同时，StackLayout 仍然有一个你可以设置的方向属性。</p> 
<p>每个布局都有一个相应的 LayoutManager，负责测量和定位视图。Measure 方法接受高度和宽度约束，并负责测量所有 hte layout’s children。然后ArrangeChildren 根据布局的规则设置每个视图的大小和位置。对于非常高级的情况，你可以覆盖布局的 CreateLayoutManager 方法来提供 ILayoutManager 的自定义实现。</p> 
<p>为方便起见，可在全局样式中设置这些起始值：</p> 
<pre><code><ResourceDictionary> <Style TargetType="StackLayout"> <Setter Property="Spacing" Value="6"/> </Style> <Style TargetType="Grid"> <Setter Property="ColumnSpacing" Value="6"/> <Setter Property="RowSpacing" Value="6"/> </Style> </ResourceDictionary></code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Flayouts%2Fabsolutelayout" target="_blank"><code>AbsoluteLayout</code></a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fuser-interface%2Flayouts%2Frelativelayout" target="_blank"><code>RelativeLayout</code></a>现在只存在于兼容性命名空间，官方建议用户在使用之前先三思。在可能的情况下，使用上面列出的布局之一。同时， 您可以通过添加新命名空间并为 XAML 引用添加前缀来更新代码以使用它们：</p> 
<pre><code><ContentPage
    xmlns:cmp="clr-namespace:Microsoft.Maui.Controls.Compatibility;assembly=Microsoft.Maui.Controls"
    ...
    >
    <cmp:AbsoluteLayout>
        ...
    </cmp:AbsoluteLayout>
</ContentPage></code></pre> 
<p>官方表示，他们将在接下来的几个 sprint 中重点关注这些新布局的改进。</p> 
<h4><strong>可访问性更改和改进</strong></h4> 
<p>此版本对无障碍支持进行了一些更改和补充，使每个人都可以更轻松地制作无障碍应用。</p> 
<h4><strong>SetSemanticFocus and Announce</strong></h4> 
<p>作为新的 SemanticExtensions 类的一部分，开发团队增加了一个新的 SetSemanticFocus 方法，允许用户将屏幕阅读器的焦点移至一个特定的元素。将此与设置输入焦点的 VisualElement.Focus 进行比较：</p> 
<pre><code><VerticalStackLayout> <Label Text="Explore SemanticExtensions below" TextColor="RoyalBlue" FontAttributes="Bold" FontSize="16" Margin="0,10"/> <Button Text="Click to set semantic focus to label below" FontSize="14" Clicked="SetSemanticFocusButton_Clicked"/> <Label x:Name="semanticFocusLabel" Text="Label receiving semantic focus" FontSize="14"/> </VerticalStackLayout></code></pre> 
<pre><code>private void SetSemanticFocusButton_Clicked(object sender, System.EventArgs e) &#123; semanticFocusLabel.SetSemanticFocus(); &#125;</code></pre> 
<p>在 Essentials 中，开发团队添加了另一种新方法<code>Announce</code>，用于设置要由屏幕阅读器朗读的文本。例如，在单击按钮时，你可以触发以下重要消息以供阅读：</p> 
<pre><code>void Announce_Clicked(object sender, EventArgs e)
&#123;
  SemanticScreenReader.Announce("Make accessible apps with .NET MAUI");
&#125;</code></pre> 
<h4><strong>字体缩放</strong></h4> 
<p>所有平台上的所有控件现在都默认启用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1774" target="_blank">字体缩放</a>。这意味着当你的应用程序用户在操作系统中调整他们的文本缩放首选项时，你的 UI 将反映他们的选择。默认情况下，这会生成更易于访问的应用程序。</p> 
<p><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-f8ab577b82d61def0b269ca19a8dc9f4433.png" width="500" referrerpolicy="no-referrer"></p> 
<p>每个控件都有一个附加的 FontAutoScalingEnabled，而且它甚至可以与 FontImageSource 一起用于你的字体图标。</p> 
<pre><code><VerticalStackLayout>    
    <Label 
        Text="Scaling disabled" 
        FontSize="18"
        FontAutoScalingEnabled="False"/>
    <Label 
        Text="Scaling enabled" 
        FontSize="18"/>
</VerticalStackLayout></code></pre> 
<p>值得注意的是，一定要审查你的屏幕并根据需要调整样式，以确保它们适用于所有尺寸。</p> 
<h4><strong>其他亮点</strong></h4> 
<ul> 
 <li>添加了对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fxamarin%2Fxamarin-forms%2Fapp-fundamentals%2Feffects%2Fintroduction" target="_blank"><code>Effects</code></a>的支持，这将支持从 Xamarin.Forms 升级的项目 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1574" target="_blank">＃1574</a>。</li> 
 <li>AppThemeBinding 改进以支持深色和浅色主题模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1657" target="_blank">#1657</a></li> 
 <li>ScrollView 处理程序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1669" target="_blank">#1669</a></li> 
 <li>Android Shell 移植到 core <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F979" target="_blank">#979</a></li> 
 <li>Shell navigation 传递 complex objects <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F2004" target="_blank">#204</a></li> 
 <li>为 XAML 热重载添加了 Visual Tree Helper <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1845" target="_blank">#1845</a></li> 
 <li>切换到 System.ComponentModel.TypeConverter <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1725" target="_blank">#1725</a></li> 
 <li>Window lifecycle events <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1754" target="_blank">#1754</a></li> 
 <li>Page navigation events <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1812" target="_blank">1812</a></li> 
 <li>CSS prefix 更新为<code>-maui</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui%2Fpull%2F1877" target="_blank">#1877</a></li> 
</ul> 
<p>详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-maui-preview-7%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            