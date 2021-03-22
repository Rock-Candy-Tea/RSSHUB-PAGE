
---
title: 'Flutter2新功能新特性'
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Thu, 04 Mar 2021 19:10:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8292fb99d72144e3a2c5b9109dd8c9ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li><a href="https://juejin.cn/post/6936002027482775583#web">Web</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#sound-null-safety">Sound Null Safety</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#%E6%A1%8C%E9%9D%A2%E7%AB%AFdesktop">桌面端（Desktop）</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#%E5%B9%B3%E5%8F%B0%E8%87%AA%E9%80%82%E5%BA%94%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8Fflutter-folio-sample">平台自适应应用程序：Flutter Folio Sample</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#%E8%B0%B7%E6%AD%8C%E6%89%8B%E6%9C%BA%E5%B9%BF%E5%91%8A%E6%B5%8B%E8%AF%95%E7%89%88">谷歌手机广告测试版</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#ios%E6%96%B0%E7%89%B9%E6%80%A7">iOS新特性</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#%E6%96%B0-widgets-autocomplete-and-scaffoldmessenger">新 widgets: Autocomplete and ScaffoldMessenger</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#add-to-app-%E5%AE%9E%E7%8E%B0%E5%A4%9A%E4%B8%AA-flutter-%E5%AE%9E%E4%BE%8B">Add-to-App 实现多个 Flutter 实例</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#flutter-fix---%E5%B7%A5%E5%85%B7%E6%9B%BF%E6%8D%A2%E5%BA%9F%E5%BC%83api">Flutter Fix - 工具替换废弃API</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#flutter-devtools">Flutter DevTools</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#android-studiointellij-extension">Android Studio/IntelliJ Extension</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#visual-studio-code-extension">Visual Studio Code Extension</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#dartpad-%E6%9B%B4%E6%96%B0%E6%94%AF%E6%8C%81-flutter-2">DartPad 更新支持 Flutter 2</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#ecosystem-%E6%9B%B4%E6%96%B0">Ecosystem 更新</a></li>
<li><a href="https://juejin.cn/post/6936002027482775583#breaking-changes">Breaking Changes</a></li>
</ul>
<p>2021年3月4日，Flutter官方发布了Flutter 2，本文为新特性的介绍。</p>
<p>官方原文：<a href="https://medium.com/flutter/whats-new-in-flutter-2-0-fe8e95ecc65" target="_blank" rel="nofollow noopener noreferrer">medium.com/flutter/wha…</a></p>
<p>从 Flutter 1.0 发布到现在已经有两年多了，但是在这短短的时间里，我们已经关闭了 24541 个 issue，合并了 765 个贡献者的 17039 个 PR。就在9月份发布 Flutter1.22 之后，我们已经关闭了5807 个 issue，合并了298个贡献者的4091个 PR。特别感谢我们的贡献者，他们慷慨地利用业余时间来改进 Flutter 项目。Flutter 2 release 的最大贡献者是 xu-baolin（46个 PR），a14n（32个PR），专注于为 Flutter 引入空类型安全 (null safety)，以及hamdikahloun（20个 PR）改进了许多 Flutter 插件。但不仅仅是编码人员为Flutter项目做出了贡献；一大批志愿者（ PR reviewer） 也负责review 1525 个 PR，其中包括hamdikahloun（再次上榜！），CareF 和 YazeedAlKhalaf（只有16岁！）。Flutter是一个真正的社区工作，如果没有问题提出者、PR贡献者和代码审阅者，我们不可能得到 version 2。这个版本是给你们所有人的。</p>
<p>有很多令人兴奋的事情正在发生，作为 Flutter 2 release 的一部分。有关 Flatter 2 和 Dart 2.12 的新增功能，以及我们的客户和合作伙伴如何使用 Flatter 2 的概述，请参见 <a href="https://developers.googleblog.com/2021/03/announcing-flutter-2.html" target="_blank" rel="nofollow noopener noreferrer">Announcing Flatter 2</a>。有关 Dart 2.12 的详细信息，请参见 <a href="https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87" target="_blank" rel="nofollow noopener noreferrer">Announcing Dart 2.12</a>。对于如何最好地利用Flutter web（现在被推荐用于生产环境），请参阅 <a href="https://medium.com/flutter/flutter-web-support-hits-the-stable-milestone-d6b84e83b425" target="_blank" rel="nofollow noopener noreferrer">Flutter web support hits the stable milestone</a>。</p>
<p>以及，要想了解 Flatter 2本身的新特性，请继续阅读！</p>
<h2 data-id="heading-0">Web</h2>
<p>到今天为止，Flutter 的 web 支持已经从 beta 版过渡到 stable channel。在这个最初的 stable release 中，Flutter 在 web 平台的支持下将代码的复用性提升到了另一个层次。所以现在，当你在 stable 中创建一个 Flutter 应用程序时，web 只是你应用程序的另一个设备目标。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8292fb99d72144e3a2c5b9109dd8c9ae~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Moi Mobiili是一家现代移动虚拟网络运营商，致力于通过数字化实现卓越运营。Moi Mobiili选择了 Flutter 来构建他们的Mun Moi Account 管理应用，并于最近推出了他们的 web 应用。</p>
</blockquote>
<p>通过利用 Web 平台的许多优势，Flutter 为构建丰富的交互式 Web 应用奠定了基础。我们主要关注性能和渲染保真度的改进。除了我们的 HTML 渲染器之外，我们还添加了一个新的基于 CanvasKit 的渲染器。我们还添加了特定于 web 的功能，例如<a href="https://pub.dev/documentation/url_launcher/latest/link/Link-class.html" target="_blank" rel="nofollow noopener noreferrer">Link widget</a>，以确保在浏览器中运行的应用程序感觉像 web 应用程序。</p>
<p>在 <a href="https://medium.com/flutter/web-post-d6b84e83b425" target="_blank" rel="nofollow noopener noreferrer">Flutter’s web support blog post</a> 可以找到关于这个稳定版本的更多细节。</p>
<h2 data-id="heading-1">Sound Null Safety</h2>
<p>空安全声明是 Dart 语言的一个重要补充，它通过区分可空类型和不可空类型进一步加强了类型系统。这使开发人员能够防止空错误 crash，这是应用程序crash的常见原因。通过将空检查合并到类型系统中，可以在开发过程中捕获这些错误，从而防止生产中的 crash。健全空类型安全是完全支持稳定的 Flutter 2，其中包含 Dart 2.12。有关更多详细信息，请参阅 <a href="https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87" target="_blank" rel="nofollow noopener noreferrer">Dart 2.12博客文章</a>。</p>
<p>这个 pub.dev 仓库已经发布了 <a href="https://pub.dev/packages?q=&null-safe=1" target="_blank" rel="nofollow noopener noreferrer">1000 多个null safe package</a>，包括 Dart、Flutter、Firebase 和 Material 团队的数百个 package。如果您是软件包的作者，请查看<a href="https://dart.dev/null-safety/migration-guide" target="_blank" rel="nofollow noopener noreferrer">迁移指南</a>并立即考虑迁移。</p>
<h2 data-id="heading-2">桌面端（Desktop）</h2>
<p>在这个版本中，我们很高兴地宣布，Flutter 的桌面支持在 stable channel 中提供，并带有提前发布的标志。这意味着，我们已经准备好让您尝试将其作为 Flutter 应用程序的部署目标：您可以将其视为一个“beta快照”，预览今年晚些时候即将发布的最终稳定版本。</p>
<p>为了使 Flutter 桌面达到这样的质量，已经有了大大小小的改进，首先要确保文本编辑在每个受支持的平台上都像本地体验一样运行，包括一些基本功能，比如文本选择轴心点，以及一旦处理了键盘事件就能够阻止它的传播。在鼠标输入端，使用高精度定点设备拖动操作，拖动立即开始，而不是等待处理触摸输入时所需的延迟。此外，还为 Material 和 Cupertino 设计语言的 TextField 和 TextFormField widget 添加了一个内置上下文菜单。最后，<a href="https://github.com/flutter/flutter/pull/74299" target="_blank" rel="nofollow noopener noreferrer">抓取句柄被添加到ReorderableListView widget 中</a>。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4d3811eb7764991bb425ad4c779e784~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>ReorderableListView现在有抓取手柄，可以用鼠标轻松地拖放</p>
</blockquote>
<p>ReorderableListView总是很擅长移动项目，作为一个开发人员，您只需花费很少的精力，但它需要用户使用长按启动拖动。这在移动设备上是有意义的，但是很少有桌面用户会想到用鼠标长按一个项目来移动它，所以这个版本包括一个适合鼠标或触摸输入的抓取手柄。平台惯用功能的另一个改进是一个更新的滚动条，可以正确显示桌面的形状。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9718becc0e44e17921a9d87bcd5a762~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这个版本包括一个更新的滚动条小部件，它在桌面环境中工作得非常好</p>
</blockquote>
<p>Scrollbar widget 已经更新，提供了桌面上预期的交互功能，包括拖动拇指、单击轨迹上下翻页以及当鼠标悬停在滚动条的任何部分时显示轨迹的功能。此外，由于 Scrollbar 是使用新的 ScrollbarTheme 类进行主题化的，因此您可以根据应用程序的外观对其进行样式设置。
对于其他特定于桌面的功能，此版本还支持 Flutter 应用程序的命令行参数处理，以便可以使用诸如在 Windows 文件资源管理器中双击数据文件之类的简单操作来打开应用程序中的文件。我们还努力使 Windows 和 macOS 的调整更加顺畅，并为国际用户启用IME（输入法编辑器）。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7414eca3df51492fbcd6e9da3b50e82c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Flutter 桌面现在支持直观的输入法输入</p>
</blockquote>
<p>此外，我们还提供了<a href="https://flutter.dev/desktop#distribution" target="_blank" rel="nofollow noopener noreferrer">更新的文档，说明您需要做什么来开始准备您的桌面应用程序，以便部署到相应的操作系统特定商店</a>。尝试一下，如果我们遗漏了什么，请提供反馈。</p>
<p>当你尝试使用 Flutter 桌面的 beta 测试版时，你可以按照预期切换到 beta channel，并根据<a href="https://flutter.dev/desktop#create-a-new-project" target="_blank" rel="nofollow noopener noreferrer">flutter.dev</a>上面的说明设置目标平台的配置标志。此外，我们还制作了 stable channel 上可用的 beta 位快照。如果您使用“flutter config”来启用某个桌面配置设置（例如，<code>enable-macos-desktop</code>），那么您可以尝试桌面支持的 beta 版功能，而不必经历从移动到beta channel、下载所有最新的 Flutter SDK beta版、构建工具的漫长过程，这是伟大的尝试或使用桌面支持作为一个简单的“Flutter Emulator”。</p>
<p>但是，如果您选择在 stable channel 上访问桌面 beta 版，您将无法像切换到 beta 或 dev channel那样快速获得新功能或错误修复。因此，如果您正积极瞄准 Windows、macOS 或 Linux，我们建议您切换到一个提供更快更新的 channel。</p>
<p>随着Flutter Desktop 的第一个完全生产质量版本的临近，我们知道我们还有更多的工作要做，包括支持与本机顶级菜单的集成、感觉更像是单个平台体验的文本编辑、可访问性支持，以及一般的错误修复和性能增强。如果您认为在桌面进入生产质量之前还需要做其他事情，请务必提供您的反馈。</p>
<h2 data-id="heading-3">平台自适应应用程序：Flutter Folio Sample</h2>
<p>既然 Flutter 支持三种生产应用程序平台（Android、iOS 和 web）和另外三种beta版平台（Windows、macOS 和 Linux），那么一个自然的问题就出现了：如何编写一个能够很好地适应多种不同外形因素（小屏幕、中屏幕和大屏幕）、不同输入模式（触摸屏、键盘、和鼠标）以及不同的习惯用法（移动、web 和 桌面）？为了回答我们自己以及各地的Flutter开发者的这个问题，我们委托了 Flutter Folio scrapbooking 应用。</p>
<p>官方演示视频（需要科学上网）：<a href="https://www.youtube.com/watch?v=x4xZkdlADWo&feature=emb_logo" target="_blank" rel="nofollow noopener noreferrer">www.youtube.com/watch?v=x4x…</a></p>
<p>Folio 是一个简单的应用程序示例，您希望一个代码库在多个平台上运行良好。我们所说的“好”，是指它在小屏幕、中屏幕和大屏幕上都很好看，它利用了触摸、键盘和鼠标输入，而且它对平台的习惯用法也很有效（例如，通过使用 web 上的链接和桌面上的菜单）。我们称这种应用程序为“平台自适应”，因为它能很好地适应运行在任何平台上的应用程序。</p>
<p>如果您想了解如何使自己的应用程序平台自适应，可以查看<a href="https://github.com/gskinnerTeam/flutter-folio" target="_blank" rel="nofollow noopener noreferrer">Folio的源代码</a>。在未来，我们希望能找到更深入探讨这个主题的文档和代码实验室。同时，看看Aloïs Deniel关于这个主题的<a href="https://aloisdeniel.com/#/posts/adaptative-ui" target="_blank" rel="nofollow noopener noreferrer">优秀博客文章和视频</a>。</p>
<h2 data-id="heading-4">谷歌手机广告测试版</h2>
<p>除了 Flutter 桌面升级到 beta 版之外，今天我们很高兴地宣布一个<a href="https://pub.dev/packages/google_mobile_ads" target="_blank" rel="nofollow noopener noreferrer">针对 Flutter 的 Google 移动广告 SDK</a> 的公测版。这是一个全新的插件，提供内联横幅和本地广告，除了现有的覆盖格式（覆盖横幅，间隙，和奖励视频广告）。这个插件统一了对 Ad Manager 和 Admob 的支持，所以不管你是多大的发布者，这个插件都可以根据你的场景定制。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbb5058a2a6b4c6abcf2fc8e062f04f9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们已经在一个私人 beta 测试项目中与一些早期客户试用了这个插件，他们中的许多人已经成功地推出了这些新格式的应用程序。例如，Sua Musica（拉丁美洲最大的独立艺术家音乐平台，拥有超过15k名经验证的艺术家和1000万MAU）推出了他们的新 Flutter 应用程序，其中包含 Google Mobile Ads SDK For Flutter plugin。他们发现 Impressions 增加了350%，CTR增加了43%，eCPM增加了13%。</p>
<p>这个插件可供您今天使用。作为 Flitter Engage 的一部分，Andrew Brogdon 和 Zoey Fan 介绍了一个关于“使用 Flutter 将应用程序货币化”的会议（可在 Flutter Engage 网站上获得），他们讨论了使用 Flutter 构建的应用程序的货币化策略，以及如何在 Flutter 应用程序中加载广告。此外，我们在 flutter.dev 上创建了一个新的<a href="https://flutter.dev/ads" target="_blank" rel="nofollow noopener noreferrer">广告页面</a>，在这里你可以找到所有有用的资源，如插件实现指南，内联横幅和原生广告 codelab，以及覆盖横幅，间隙和奖励视频广告 codelab。请务必检查一下！</p>
<h2 data-id="heading-5">iOS新特性</h2>
<p>就因为我们在不断提高对其他平台的支持质量，别以为我们忘记了iOS。事实上，这个版本带来了178个与iOS相关的PR，包括<a href="https://github.com/flutter/engine/pull/23495" target="_blank" rel="nofollow noopener noreferrer">23495</a>，它为iOS带来了状态恢复，<a href="https://github.com/flutter/flutter/pull/67781" target="_blank" rel="nofollow noopener noreferrer">67781</a>，它满足了一个长期的请求，直接从命令行构建 IPA 而不打开 Xcode，还有 <a href="https://github.com/flutter/flutter/pull/69809" target="_blank" rel="nofollow noopener noreferrer">69809</a>，它更新 CocoaPods 版本以匹配最新的工具。此外，Cupertino 设计语言实现中还添加了一些iOS widget。</p>
<p>新的 <a href="https://api.flutter.dev/flutter/cupertino/CupertinoSearchTextField-class.html" target="_blank" rel="nofollow noopener noreferrer">CupertinoSearchTextField</a> 提供了iOS搜索栏UI。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/920346d26bea48429f018679694ac3de~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><a href="https://api.flutter.dev/flutter/cupertino/CupertinoFormSection-class.html" target="_blank" rel="nofollow noopener noreferrer">CupertinoFormSection</a>、<a href="https://api.flutter.dev/flutter/cupertino/CupertinoFormRow-class.html" target="_blank" rel="nofollow noopener noreferrer">CupertinoFormRow</a> 和 <a href="https://api.flutter.dev/flutter/cupertino/CupertinoTextFormFieldRow-class.html" target="_blank" rel="nofollow noopener noreferrer">CupertinoNotextFormFieldRow</a> widget 使生成具有iOS分区视觉美感的有效表单字段变得更加容易。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d1104dd50434539a996cf4765d6879a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>除了iOS的特性工作之外，我们还在继续研究iOS的性能改进，当涉及到着色器和动画时，通常情况下也会研究 Flutter。iOS 仍然是 Flutter的首要平台，我们将继续致力于带来重要的新功能和性能改进。</p>
<h2 data-id="heading-6">新 widgets: Autocomplete and ScaffoldMessenger</h2>
<p>这个版本的 Flutter 附带了两个新的小部件，AutocompleteCore 和 ScaffoldMessenger。AutocompleteCore 代表了将 auto-complete 功能导入 Flutter 应用程序所需的最小功能。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b4cfdc63db4e6abddf0e367060427a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Autocomplete 是 Flutter 经常需要的特性，所以这个版本开始提供这个功能。您现在可以使用它，但是如果您对完整功能的设计感兴趣，请查看 <a href="https://docs.google.com/document/d/1fV4FDNdcza1ITU7hlgweCDUZdWyCqd-rjz_J7K2KkfY/edit" target="_blank" rel="nofollow noopener noreferrer">autocomplete 设计文档</a>。</p>
<p>同样，<a href="https://github.com/flutter/flutter/pull/64101" target="_blank" rel="nofollow noopener noreferrer">创建 ScaffoldMessenger</a> 是为了处理许多与 SnackBar 相关的问题，包括能够轻松地创建SnackBar 以响应 AppBar 操作，创建 SnackBar 以在 Scaffold 转换之间保持，以及能够在异步操作完成时显示 SnackBar，即使用户已经导航到有不同支架的页面。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6045aa80d66043d7966ce45d3ccae67e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所有这些优点都可以通过几行代码来实现，从现在起，您应该使用这些代码来显示您的 SnackBars：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">final</span> messenger = ScaffoldMessenger.of(context);
messenger.showSnackBar(SnackBar(content: Text(‘I can fly.’)));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正如你可能想象的那样，还有更多的事情要做；有关详细信息，请查看<a href="https://www.youtube.com/watch?v=sYG7HAGu_Eg" target="_blank" rel="nofollow noopener noreferrer">an excellent video from Kate Lovett on ScaffoldMessenger</a>.</p>
<h2 data-id="heading-7">Add-to-App 实现多个 Flutter 实例</h2>
<p>我们从与许多 Flutter 开发者的交谈中了解到，相当一部分人没有启动一个全新应用程序的诉求，但你可以通过将 Flutter 添加到现有的 iOS 和 Android 应用程序中来利用它。这个名为 <a href="https://flutter.dev/docs/development/add-to-app" target="_blank" rel="nofollow noopener noreferrer">Add-to-App</a> 的特性是一个很好的方法，可以在两个移动平台上重用 Flutter 代码，同时保留现有的本地代码库。然而，对于那些这样做的人来说，我们有时会听到，除了将第一个屏幕集成到 Flutter 中之外，还不清楚该如何做。将 Flutter 和本机屏幕交织在一起使得导航状态难以维护，并且在视图级别集成多个 Flutter 会占用大量内存。</p>
<p>在过去，Flutter 的 Flutter 实例与第一个实例具有相同的内存开销。在 Flutter 2 中，我们将创建额外的 Flutter 引擎的静态内存成本降低了99%，减低到每个实例180kB。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bcea3b1b8b04667927aab0033e7a3ea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>用于实现此功能的新 API 在beta chennel 的预览版中，并在 flutter.dev 以及一组演示此新模式的示例项目。有了这个变化，我们不再犹豫，建议您在本机应用程序中创建多个 Flutter 引擎实例。</p>
<h2 data-id="heading-8">Flutter Fix - 工具替换废弃API</h2>
<p>每当任何框架成熟并聚集了越来越大的代码库的用户时，随着时间的推移，趋势是避免对框架API进行任何更改，以避免中断越来越多的代码行。随着越来越多的平台上超过500000名 Flutter 开发人员的加入，Flutter 2 很快就进入了这一类。但是，为了继续改进 Flutter，我们希望能够对API进行突破性的更改。问题是，如何在不打断开发人员的情况下继续改进 Flutter API？</p>
<p>我们的答案是 <a href="http://flutter.dev/docs/development/tools/flutter-fix" target="_blank" rel="nofollow noopener noreferrer">Flutter Fix</a>。</p>
<p>Flutter Fix 是多种因素的结合。首先，dart CLI 工具有一个新的命令行选项，名为 <code>dart fix</code>，它知道在哪里查找不推荐使用的 API 列表，以及如何使用这些 API 更新代码。其次，它是可用修复程序本身的列表，从版本2开始，它与 Flutter SDK 捆绑在一起。最后，它是一组更新的 Flutter 扩展，用于 VS Code、IntelliJ 和 Android Studio IDE，它们知道如何将可用的补丁列表公开为带有小灯泡的快速补丁，这将帮助您通过单击鼠标来更改代码。</p>
<p>例如，假设您的应用程序中有以下代码行：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b301928dea89471ca4dc2d702b29fd92~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>使用废弃的参数创建一个 Flutter widget</p>
</blockquote>
<p>由于此构造函数的参数已弃用，因此应替换为以下参数：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23d986703a74246994245ab91e5c819~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>创建替换了不推荐的参数的 Flutter widget</p>
</blockquote>
<p>随着废弃的 API 越来越多，代码改动就越来越多，就越难应用所有修复，也越容易出错；人类并不擅长这些重复性的任务。但是计算机擅长；通过执行以下命令，您可以看到我们知道如何在整个项目中进行的所有修复：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> dart fix --dry-run</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想批量使用，你可以很容易地做到：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> dart fix --apply</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，如果想在喜爱的 IDE 中以交互方式应用这些修复，也可以这样做。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da5ef280d5d45d58fee42b174512710~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>虽然我们已经将旧的 API 标记为不推荐使用，有很多年了，但是现在我们有了一个关于何时实际删除不推荐使用的 API 的策略，Flutter 2 是我们第一次这样做。尽管我们还没有将所有不推荐使用的 API 作为数据捕获到 Flutter Fix 的列表中，但我们仍将继续从以前不推荐使用的 API 中添加更多内容，并将在将来进行突破性的更改。我们的目标是尽我们最大的努力使 Flutter 的 API 成为最好的 API，同时也使您的代码保持最新。</p>
<h2 data-id="heading-9">Flutter DevTools</h2>
<p>为了明确 DevTools 是一个应该用于调试 Flutter 应用程序的工具，我们在调试 Flutter 应用程序时将其重命名为 Flutter DevTools。此外，我们做了大量的工作，使它在生产环境的能力适配 Flutter 2。</p>
<p>Android Studio、IntelliJ 或 Visual Studio Code 能够在出现常见异常时发出通知，并提供在 DevTools中显示该异常以帮助您进行调试，这是一个新特性，可以帮助您甚至在启动 DevTools 之前就关注您的问题。例如，下面显示了应用程序中引发的溢出异常，这将在 Visual Studio Code 代码中打开一个选项，以便在 DevTools 中调试该问题。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/453df00935ad4597a115eb220104dbc7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当应用程序抛出布局溢出异常时，Flutter IDE 做出提醒</p>
</blockquote>
<p>按下该按钮，您就可以在 DevTools 中找到导致问题的 widget 上的 Flutter Inspector，这样您就可以修复它了。我们今天只针对布局溢出异常进行此操作，但我们的计划是将这种处理包括在 DevTools 可以解决的所有常见异常中。</p>
<p>一旦您运行了 DevTools，选项卡上的新错误徽章将帮助您跟踪应用程序中的特定问题。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60bd76c675584e548a25ca2d56b18272~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>DevTools 中的红点有助于您关注应用程序中出现错误的部分</p>
</blockquote>
<p>DevTools 中的另一个新特性是能够轻松地看到分辨率高于显示分辨率的图像，这有助于跟踪过多的应用程序大小和内存使用情况。要启用此功能，请在 Flutter Inspector 中启用 Oversized Images。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f1d084f00e74814a560075ce225160b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>启用“Invert Oversized Images”选项以突出显示比需要的图像大的图像</p>
</blockquote>
<p>现在，当你显示一个分辨率明显大于其显示尺寸的图像时，它会显示为上下颠倒，以便在你的应用程序中很容易找到。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80382b85102d4a2c850701ab8fc35306~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>此外，根据流行的需求，除了在 Flutter Inspector 的 Layout Explorer 中显示关于灵活布局的详细信息外，我们还添加了显示固定布局的功能，使您能够调试各种布局。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4836770712cd404383589b3cd7c775e1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>还不止这些。这里只是对 Flutter DevTools 2 中的一些新特性的总结：</p>
<ul>
<li>
<p>在 Flutter 框架图中增加了平均FPS信息和可用性改进</p>
</li>
<li>
<p>在 network profiler 中调用带有红色错误标签的失败网络请求</p>
</li>
<li>
<p>新的内存视图图表更快，更小，更易于使用，包括一个新的悬停卡来描述在特定时间的活动
在日志选项卡中添加了搜索和筛选</p>
</li>
<li>
<p>跟踪 DevTools 启动前的日志，以便在启动时可以看到完整的日志记录历史</p>
</li>
<li>
<p>将 “Performance” 视图重命名为“CPU Profiler”，以便更清楚地了解它提供了哪些功能</p>
</li>
<li>
<p>增加了时间网格到 CPU Profiler flame 图表</p>
</li>
<li>
<p>将 “Timeline” 视图重命名为 “Performance”，以便更清楚地了解它提供了哪些功能</p>
</li>
</ul>
<p>但这还不是全部。对于全套更改，我建议您查看以下公告：</p>
<ul>
<li>DevTools <a href="https://groups.google.com/g/flutter-announce/c/mx_hBxuXM9Q/m/Kjy9dqS3AAAJ" target="_blank" rel="nofollow noopener noreferrer">0.9.4</a></li>
<li>DevTools <a href="https://groups.google.com/g/flutter-announce/c/mNqTNPUwBKw/m/_1qyXwTBAQAJ" target="_blank" rel="nofollow noopener noreferrer">0.9.5</a></li>
<li>DevTools <a href="https://groups.google.com/g/flutter-announce/c/Ta5HR39P3go/m/2a43w7iSCwAJ" target="_blank" rel="nofollow noopener noreferrer">0.9.6</a></li>
<li>DevTools <a href="https://groups.google.com/g/flutter-announce/c/IJ97oJ2HpxM/m/909J9Kl8AQAJ" target="_blank" rel="nofollow noopener noreferrer">0.9.7</a></li>
<li>DevTools <a href="https://groups.google.com/g/flutter-announce/c/0xQhJR4nQbI" target="_blank" rel="nofollow noopener noreferrer">2.0</a></li>
</ul>
<h2 data-id="heading-10">Android Studio/IntelliJ Extension</h2>
<p>IDE 的 IntelliJ 家族的 Flutter 插件也为 Flutter 2 提供了许多新特性。首先，有一个新的项目向导，它与 IntelliJ 中的新向导样式相匹配。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9352584b04fe41a0b00fcca3311a3cf0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbd432e06764f31bd0deecd01e036cb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>另外，如果您在Linux上使用 IntelliJ 或 Android Studio 对 <a href="https://snapcraft.io/flutter" target="_blank" rel="nofollow noopener noreferrer">Snap 商店中安装的 Flutter SDK</a> 进行编程，那么 Flutter snap 路径已经添加到已知 SDK 路径的列表中。这使得 Flutter snap的用户更容易在设置中配置 Flutter SDK。感谢 MarcusTomlinson@ 的贡献！</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae5eac9b25c54811bfc5d64446021f8e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Linux 上的 Android Studio 与通过 Snap 安装的 Flutter SDK 一起使用更容易</p>
</blockquote>
<p>在最近更新的公告中，您可以看到更多的好东西：</p>
<ul>
<li>IntelliJ Plugin <a href="https://groups.google.com/g/flutter-announce/c/w65rD73R83Q/m/gV5p0qf2AAAJ" target="_blank" rel="nofollow noopener noreferrer">M51</a></li>
<li>IntelliJ Plugin <a href="https://groups.google.com/g/flutter-announce/c/tQqqMOIg6V0/m/wj7Kbv4-AgAJ" target="_blank" rel="nofollow noopener noreferrer">M52</a></li>
<li>IntelliJ Plugin <a href="https://groups.google.com/g/flutter-announce/c/V335xbsPWUs/m/14LSp05kAQAJ" target="_blank" rel="nofollow noopener noreferrer">M53</a></li>
<li>IntelliJ Plugin <a href="https://groups.google.com/g/flutter-announce/c/-jYDrwG7PmA" target="_blank" rel="nofollow noopener noreferrer">M54</a></li>
</ul>
<h2 data-id="heading-11">Visual Studio Code Extension</h2>
<p>Visual Studio Code 代码的 Flutter 扩展对 Flutter 2 也有了改进，首先是一些测试增强，包括重新运行刚刚失败的测试的能力。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d837b86c9a4d978323fb6e4542cd9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>经过两年的开发，对 Dart 的 LSP（Language Server Protocol，语言服务器协议）支持现在正在推出，作为访问 Dart 分析器以集成到 Visual Studio Code 中进行 Flutter 扩展的默认方式。LSP 支持为 Flutter 开发提供了许多改进，包括能够在当前 Dart 文件中应用所有特定类型的修复，并使代码完成生成完整的函数调用，包括括号和必需的参数。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9e98086263041b6b5766b3f328a4136~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f66e1c80d84d4d6aa7362c5c4dd3f8f0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>而且 LSP 的支持不仅仅针对 Dart，它还支持 <code>pubspec.yaml</code> 和 <code>analysis_options.yaml</code> 文件的代码补全。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb8745c30f140609b6d538d69de5ca8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这些只是 Visual Studio Code 代码扩展为 Flutter 最近的一些更新。您可以阅读这些公告中的完整列表：</p>
<ul>
<li>Visual Studio Code Plugin <a href="https://dartcode.org/releases/v3-16/" target="_blank" rel="nofollow noopener noreferrer">v3.16</a></li>
<li>Visual Studio Code Plugin <a href="https://dartcode.org/releases/v3-17/" target="_blank" rel="nofollow noopener noreferrer">v3.17</a></li>
<li>Visual Studio Code Plugin <a href="https://dartcode.org/releases/v3-18/" target="_blank" rel="nofollow noopener noreferrer">v3.18</a></li>
<li>Visual Studio Code Plugin <a href="https://dartcode.org/releases/v3-19/" target="_blank" rel="nofollow noopener noreferrer">v3.19</a></li>
<li>Visual Studio Code Plugin <a href="https://dartcode.org/releases/v3-20/" target="_blank" rel="nofollow noopener noreferrer">v3.20</a></li>
</ul>
<h2 data-id="heading-12">DartPad 更新支持 Flutter 2</h2>
<p>如果没有提到 DartPad，这个工具更新列表将是不完整的，DartPad 已经更新支持了 Flutter 2。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36d7463b608413396e65e15ad36b27e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>现在您可以尝试新的空安全版本的 Flutter，而不必离开您喜爱的舒适浏览器。</p>
<h2 data-id="heading-13">Ecosystem 更新</h2>
<p>Flutter 开发经验不仅包括框架和工具，还包括 Flutter 应用程序可用的各种软件包和插件。自从上次Flutter stable 发布以来，这个空间也发生了很多事情。例如，在摄像头和视频播放器插件之间，已经合并了近30个 PR，大大提高了两者的质量。如果您在过去使用过这两种方法中的任何一种都有困难，您应该再看一看；我们认为您会发现它们更加强大。</p>
<p>另外，如果您是 Firebase 用户，我们很高兴地宣布，最流行的插件已经提高了产品质量，包括空安全支持，以及针对 Android、iOS、web 和 macOS 的<a href="http://firebase.flutter.dev/" target="_blank" rel="nofollow noopener noreferrer">全套参考文档和常用教程</a>。这些插件包括：</p>
<ul>
<li>Core</li>
<li>Authentication</li>
<li>Cloud Firestore</li>
<li>Cloud Functions</li>
<li>Cloud Messaging</li>
<li>Cloud Storage</li>
<li>Crashlytics</li>
</ul>
<p>另外，如果你正在为你的应用程序寻找崩溃报告，你可能想考虑 Sentry，它已经<a href="https://blog.sentry.io/2021/03/03/with-flutter-and-sentry-you-can-put-all-your-eggs-in-one-repo/" target="_blank" rel="nofollow noopener noreferrer">宣布了一个新的 Flutter 应用程序SDK</a>。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/305b70c9e9df4b5e99384f63fcc13163~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用 Sentry 的 Flutter SDK，可以实时通知您在 Android、iOS 或本机平台上发生的错误。你可以在<a href="https://docs.sentry.io/platforms/flutter/" target="_blank" rel="nofollow noopener noreferrer">the Sentry documentation</a>.中看到细节。</p>
<p>此外，如果您还没有看到<a href="http://plus.fluttercommunity.dev/" target="_blank" rel="nofollow noopener noreferrer">the Flutter Community “plus” plugins</a>，那么您可以查看它们。他们已经 fork 了许多最初由 Flutter 团队开发的流行插件，并添加了空安全支持、对其他平台的支持和一组全新的<a href="https://plus.fluttercommunity.dev/docs/overview/" target="_blank" rel="nofollow noopener noreferrer">文档</a>，以及开始从 flutter/plugin 仓库修复适当的问题。这些插件包括：</p>
<ul>
<li>Android Alarm+</li>
<li>Android Intent+</li>
<li>Battery+</li>
<li>Connectivity+</li>
<li>Device Info+</li>
<li>Network Info+</li>
<li>Package Info+</li>
<li>Sensors+</li>
<li>Share+</li>
</ul>
<p>在这一点上，Flutter 兼容 package 和 plugin 的数量超过15000个，这使得很难找到那些你应该首先考虑的。出于这个原因，我们发布了 Pub Points（静态分析评分）、人气排名、喜欢度，以及为获得特别高的质量，为那些标记为 <a href="https://flutter.dev/docs/development/packages-and-plugins/favorites" target="_blank" rel="nofollow noopener noreferrer">Flutter Favorite</a> 的包提供了一个特殊的名称。在 Flutter 2 中，我们在收藏夹列表中添加了几个新包：</p>
<ul>
<li>animated_text_kit</li>
<li>bottom_navy_bar</li>
<li>chopper</li>
<li>font_awesome_flutter</li>
<li>flutter_local_notifications</li>
<li>just_audio</li>
</ul>
<p>恭喜这些软件包的作者！如果您还没有check out 它们，或者列表中的其他包，您应该试一试。</p>
<p>最后，对于那些对最新版本的软件包是否适用于最新版本的 Flutter 感兴趣的软件包作者或用户来说，您应该看看 Codemagic 的 <a href="http://pub.green/" target="_blank" rel="nofollow noopener noreferrer">pub.green</a> site.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d42534b5e54448396f84c3346026665~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个 pub.green 现场测试 Flutter 的兼容性和 Dart package 上提供 pub.dev 不同的 Flutter 版本。把它当作 Flutter 的“我能用吗”。更多细节，我推荐<a href="https://blog.codemagic.io/pub-green/" target="_blank" rel="nofollow noopener noreferrer">CodeMagic团队的公告博客</a>。</p>
<h2 data-id="heading-14">Breaking Changes</h2>
<p>我们对 Flutter 2 进行了以下突破性的更改，其中许多更改可以使用 <code>dart fix</code> 命令或您选择的 IDE 中的快速修复来自动解决：</p>
<ul>
<li><a href="https://github.com/flutter/flutter/pull/61366" target="_blank" rel="nofollow noopener noreferrer">61366</a> Continue the clipBehavior breaking change</li>
<li><a href="https://github.com/flutter/flutter/pull/66700" target="_blank" rel="nofollow noopener noreferrer">66700</a> Default FittedBox’s clipBehavior to none</li>
<li><a href="https://github.com/flutter/flutter/pull/68905" target="_blank" rel="nofollow noopener noreferrer">68905</a> Remove nullOk parameter from Cupertino color resolution APIs</li>
<li><a href="https://github.com/flutter/flutter/pull/68908" target="_blank" rel="nofollow noopener noreferrer">69808</a> Remove nullOk from Scaffold.of and ScaffoldMessenger.of, create maybeOf for both</li>
<li><a href="https://github.com/flutter/flutter/pull/68910" target="_blank" rel="nofollow noopener noreferrer">68910</a> Remove nullOk parameter from Router.of and make it return a non-nullable value</li>
<li><a href="https://github.com/flutter/flutter/pull/68911" target="_blank" rel="nofollow noopener noreferrer">68911</a> Add maybeLocaleOf to Localizations</li>
<li><a href="https://github.com/flutter/flutter/pull/68736" target="_blank" rel="nofollow noopener noreferrer">68736</a> Remove nullOK in Media.queryOf</li>
<li><a href="https://github.com/flutter/flutter/pull/68917" target="_blank" rel="nofollow noopener noreferrer">68917</a> Remove nullOk parameter from Focus.of, FocusTraversalOrder.of, and FocusTraversalGroup.of</li>
<li><a href="https://github.com/flutter/flutter/pull/68921" target="_blank" rel="nofollow noopener noreferrer">68921 Remove nullOk parameter from Shortcuts.of, Actions.find, and Actions.handler</a></li>
<li><a href="https://github.com/flutter/flutter/pull/68925" target="_blank" rel="nofollow noopener noreferrer">68925</a> Remove nullOk parameter from AnimatedList.of and SliverAnimatedList.of</li>
<li><a href="https://github.com/flutter/flutter/pull/69620" target="_blank" rel="nofollow noopener noreferrer">69620</a> Remove deprecated methods from BuildContex</li>
<li><a href="https://github.com/flutter/flutter/pull/70726" target="_blank" rel="nofollow noopener noreferrer">70726</a> Remove the nullOk parameter from Navigator.of and add Navigator.maybeOft</li>
<li><a href="https://github.com/flutter/flutter/pull/72017" target="_blank" rel="nofollow noopener noreferrer">72017</a> Remove deprecated CupertinoTextThemeData.brightness</li>
<li><a href="https://github.com/flutter/flutter/pull/72395" target="_blank" rel="nofollow noopener noreferrer">72395</a> Remove deprecated [PointerEnterEvent, PointerExitEvent].fromHoverEvent</li>
<li><a href="https://github.com/flutter/flutter/pull/72532" target="_blank" rel="nofollow noopener noreferrer">72532</a> Remove deprecated showDialog.child</li>
<li><a href="https://github.com/flutter/flutter/pull/72890" target="_blank" rel="nofollow noopener noreferrer">72890</a> Remove deprecated Scaffold.resizeToAvoidBottomPadding</li>
<li><a href="https://github.com/flutter/flutter/pull/72893" target="_blank" rel="nofollow noopener noreferrer">72893</a> Remove deprecated WidgetsBinding.[deferFirstFrameReport, allowFirstFrameReport]</li>
<li><a href="https://github.com/flutter/flutter/pull/72901" target="_blank" rel="nofollow noopener noreferrer">72901</a> Remove deprecated StatefulElement.inheritFromElement</li>
<li><a href="https://github.com/flutter/flutter/pull/72903" target="_blank" rel="nofollow noopener noreferrer">72903</a> Remove deprecated Element methods</li>
<li><a href="https://github.com/flutter/flutter/pull/73604" target="_blank" rel="nofollow noopener noreferrer">73604</a> Remove deprecated CupertinoDialog</li>
<li><a href="https://github.com/flutter/flutter/pull/73745" target="_blank" rel="nofollow noopener noreferrer">73745</a> Remove deprecated actionsForegroundColor from Cupertino[Sliver]NavigationBar</li>
<li><a href="https://github.com/flutter/flutter/pull/73746" target="_blank" rel="nofollow noopener noreferrer">73746</a> Remove deprecated ButtonTheme.bar</li>
<li><a href="https://github.com/flutter/flutter/pull/73747" target="_blank" rel="nofollow noopener noreferrer">73747</a> Remove span deprecations</li>
<li><a href="https://github.com/flutter/flutter/pull/73748" target="_blank" rel="nofollow noopener noreferrer">73748</a> Remove deprecated RenderView.scheduleInitialFrame</li>
<li><a href="https://github.com/flutter/flutter/pull/73749" target="_blank" rel="nofollow noopener noreferrer">73749</a> Remove deprecated Layer.findAll</li>
<li><a href="https://github.com/flutter/flutter/pull/74657" target="_blank" rel="nofollow noopener noreferrer">75657</a> Remove vestigial nullOk parameter from Localizations.localeOf</li>
<li><a href="https://github.com/flutter/flutter/pull/74680" target="_blank" rel="nofollow noopener noreferrer">74680</a> Remove nullOk from Actions.invoke, add Actions.maybeInvoke</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            