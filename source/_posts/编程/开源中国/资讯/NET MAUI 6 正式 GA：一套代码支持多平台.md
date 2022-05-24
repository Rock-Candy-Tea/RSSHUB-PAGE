
---
title: '.NET MAUI 6 正式 GA：一套代码支持多平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-32a2f641055e590da8f2a5aa54732d998d2.png'
author: 开源中国
comments: false
date: Tue, 24 May 2022 03:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-32a2f641055e590da8f2a5aa54732d998d2.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>微软<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fintroducing-dotnet-maui-one-codebase-many-platforms%2F" target="_blank">宣布</a> .NET MAUI 已正式 GA。</p> 
<blockquote> 
 <p>.NET MAUI (.NET Multi-platform App UI) 是一个跨平台 UI 框架（前身是 Xamarin.Forms），用于通过 C# 和 XAML 创建原生移动和桌面应用。基于 .NET MAUI，开发者可在单个共享代码库中创建同时支持 Android、iOS、macOS 和 Windows 的原生应用。</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-32a2f641055e590da8f2a5aa54732d998d2.png" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p>微软在公告中表示，此版本是他们实现统一 .NET 平台目标的新里程碑，为打造更广泛的 .NET 生态奠定了基础，并将 .NET Framework 和旧项目系统中的插件、库和服务引入到了 .NET 6 和 SDK 样式项目中。其中包括：</p> 
<table border="0" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border:0px; box-sizing:border-box; color:#333333; font-family:"Segoe UI","Segoe UI Web Regular","Segoe UI Regular WestEuropean","Segoe UI",Tahoma,Arial,Roboto,"Helvetica Neue",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-collapse:collapse; border-width:0px; text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxamarin%2FAndroidX" target="_blank">AndroidX</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjsuarezruiz%2FAlohaKit" target="_blank">AlohaKit</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fwindows%2Fcommunitytoolkit%2Fmvvm%2Fintroduction" target="_blank">CommunityToolkit.MVVM</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fcommunitytoolkit%2Fmaui%2F" target="_blank">CommunityToolkit.Maui</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FXamarin.CommunityToolkit.MauiCompat%2F" target="_blank">CommunityToolkit MauiCompat</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FXamarin.CommunityToolkit.Markup.MauiCompat%2F" target="_blank">CommunityToolkit Markup.MauiCompat</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.devexpress.com%2Fmaui%2F" target="_blank">DevExpress</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxamarin%2FFacebookComponents" target="_blank">Facebook</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFreshMvvm.Maui" target="_blank">FreshMvvm.Maui</a></td> 
   <td style="border-collapse:collapse; border-width:0px; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxamarin%2FGoogleAPIsForiOSComponents" target="_blank">Google APIs for iOS</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxamarin%2FGooglePlayServicesComponents" target="_blank">Google Play Services Client Libraries</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrialkit.com%2F" target="_blank">GrialKit</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjsuarezruiz%2FMauiAnimation" target="_blank">MauiAnimation</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Fuser-interface%2Fgraphics%2F" target="_blank">Microsoft.Maui.Graphics</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mrgestures.com%2F" target="_blank">MR.Gestures</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FPrism.Maui%2F" target="_blank">Prism.Maui</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FPlugin.Fingerprint%2F" target="_blank">Plugin.Fingerprint</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FPlugin.InAppBilling%2F" target="_blank">Plugin.InAppBilling</a></td> 
   <td style="border-collapse:collapse; border-width:0px; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FPlugin.StoreReview%2F" target="_blank">Plugin.StoreReview</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FPlugin.ValidationRules" target="_blank">Plugin.ValidationRules</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FReactiveUI.Maui%2F" target="_blank">ReactiveUI.Maui</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshinylib.net%2F" target="_blank">Shiny</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmono%2FSkiaSharp" target="_blank">SkiaSharp</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.syncfusion.com%2Fmaui-controls" target="_blank">Syncfusion</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.telerik.com%2Fmaui-ui%3Futm_medium%3Dreferral%26utm_source%3Dmicrosoftblogs%26utm_campaign%3Dmaui-awareness-ms-ga-announcement" target="_blank">Telerik UI for .NET MAUI</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjsuarezruiz%2FTemplateUI" target="_blank">TemplateUI</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Faritchie%2Fuserdialogs" target="_blank">User Dialogs</a></td> 
  </tr> 
 </tbody> 
</table> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-928a7c87cb410df5bd9d79d721375e52054.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fzh-cn%2Fplatform%2Fsupport%2Fpolicy%2Fmaui" target="_blank">按照发布计划</a>，.NET MAUI 的主要版本将在后续版本（下一个大版本）发布后至少 6 个月内获得支持。例如，.NET MAUI 6.0 将在 .NET MAUI 7.0 发布后的 6 个月内得到支持。同样，.NET MAUI 7.0 将在 .NET MAUI 8.0 发布后的 6 个月内获得支持。</p> 
<p>未来，.NET MAUI 将与 .NET 保持一致的发布节奏，即 .NET MAUI 7.0 将与 .NET 7.0 一起发布，.NET MAUI 8.0 将随 .NET 8.0 一起发布。</p> 
<h3>.NET MAUI 亮点</h3> 
<p><strong>开箱即用的原生 UI</strong></p> 
<p>针对不同平台（Android、iOS、macOS 和 Windows），.NET MAUI 分别提供了专门设计且开箱即用的最佳应用体验。例如，Windows 上的 .NET MAUI 获得了 WinUI 3 的支持，WinUI 3 是与 Windows App SDK 一起提供的首选原生 UI 组件。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a8080774064e79ad9d1a9a0cb0f5f8c6807.png" referrerpolicy="no-referrer"></p> 
<p><strong>丰富的 API</strong></p> 
<p>.NET MAUI 提供了简单的 API 来访问每个平台的服务和功能，例如加速度计、应用程序操作、文件系统、通知等。在下面的示例中，通过配置 “app actions” ，即可为每个平台上的应用程序图标添加菜单选项：</p> 
<pre><code class="language-cs">AppActions.SetAsync(
    new AppAction("current_info", "Check Current Weather", icon: "current_info"),
    new AppAction("add_location", "Add a Location", icon: "add_location")
);</code></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-75e48fa026b80889238d5e2e7ab26d09da1.png" referrerpolicy="no-referrer"></p> 
<p><strong>提升生产力</strong></p> 
<p>.NET MAUI 使用 .NET 6 引入的 C# 10 新特性，包括全局 using 语句和文件范围命名空间——非常有助于减少文件中的混乱。.NET MAUI 以“单一项目”为重点，将多平台目标提升到了一个新的水平。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-29ccc8b0b3ebcb1e9980967d495daff7bbc.png" referrerpolicy="no-referrer"></p> 
<p>在新的 .NET MAUI 项目中，平台被放置在一个子文件夹中，开发者可将重点放在花费大部分精力的应用程序上。在项目的 Resources 文件夹中，开发者可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Ffundamentals%2Fsingle-project" target="_blank">一个地方</a>管理应用程序的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Fuser-interface%2Ffonts" target="_blank">字体</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Fuser-interface%2Fimages%2Fimages" target="_blank">图像</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Fuser-interface%2Fimages%2Fapp-icons%3Ftabs%3Dandroid" target="_blank">应用程序图标</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fmaui%2Fuser-interface%2Fimages%2Fsplashscreen%3Ftabs%3Dandroid" target="_blank">启动画面</a>、原始资源和样式。.NET MAUI 将针对每个平台的独特要求进行优化。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-240c58b324bc6d70c0ae9997895ff112231.png" referrerpolicy="no-referrer"></p> 
<p><strong>将 Blazor 带入桌面和移动设备</strong></p> 
<p> .NET MAUI 集成了 Blazor，因此开发者可以直接在原生的移动和桌面应用程序中重用现有的 Blazor Web UI 组件。借助 .NET MAUI 和 Blazor，开发者可以重用 Web 开发技能来构建跨平台的原生客户端应用程序，并构建跨移动、桌面和 Web 的单独 UI。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e239e26d9dba25bc9708ecb109ede0e89e1.png" referrerpolicy="no-referrer"></p> 
<p><strong>性能优化</strong></p> 
<p>.NET MAUI 专为提高性能而设计。.NET MAUI 中的 UI 控件在原生平台控件上实现了一种精简的、解耦的处理程序映射器模式——这减少了 UI 渲染中的层数，并简化了控件定制。</p> 
<p>默认情况下会启用这些设置，以提供优化了性能的 release 版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ab64904e1f541683be74681bc812da78546.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fintroducing-dotnet-maui-one-codebase-many-platforms%2F" target="_blank">点此查看更多细节</a>。</p>
                                        </div>
                                      
</div>
            