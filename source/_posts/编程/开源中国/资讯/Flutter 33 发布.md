
---
title: 'Flutter 3.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e9e52f53359deec9f227d2aee4293bc2eb8.png'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 08:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e9e52f53359deec9f227d2aee4293bc2eb8.png'
---

<div>   
<div class="content">
                                                                                            <p>Flutter 3.3 现已发布，此版本的专注于完善和性能改进，以强化三个月前发布的 Flutter 3 中所提供的功能。自 Flutter 3 发布以来，Flutter 已经合并了 5,687 个 PR。此版本通过几个新组件和一些错误修复扩展了对不断发展的 Material 3 规范的支持，包括针对平板电脑和桌面开发人员的新功能，iPad 上的涂鸦手写支持、可选择的文本分组和触控板支持。</p> 
<p>还包括 Dart 2.18，它为使用 Swift 或 Objective-C 编写的库和代码引入了 FFI 支持。公告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fannouncing-flutter-3-3-at-flutter-vikings-6f213e068793" target="_blank">称</a>，基于此版本构建的应用程序将在桌面、Web 和移动设备上体验到更高的性能。此版本带来了 Flutter Web、桌面、文本处理性能的更新等等，还为<code>go_router</code>包、DevTools 和 VS Code 扩展引入了更新。</p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-e9e52f53359deec9f227d2aee4293bc2eb8.png" width="500" referrerpolicy="no-referrer"></p> 
<h4>Framework</h4> 
<p><strong>全局选择</strong></p> 
<p>随着 SelectableArea widget 的引入，任何 child of the SelectableArea widget 都可以免费启用选择。更多详情可查看 <code>[SelectableArea](https://api.flutter.dev/flutter/material/SelectionArea-class.html)</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapi.flutter.dev%2Fflutter%2Fmaterial%2FSelectionArea-class.html" target="_blank">API</a>页面。</p> 
<p><img alt height="239" src="https://oscimg.oschina.net/oscnet/up-57d264e768da1e67c7956c093b492570866.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>触控板输入</strong><br> Flutter 3.3 改进了对触控板输入的支持。不仅提供了更丰富、更流畅的控制，还减少了某些情况下的误解。有关这种误解的示例，可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Fcookbook" target="_blank">Drag a UI element page in the Flutter cookbook</a>。滚动到页面底部以访问 DartPad 实例，然后执行以下步骤：</p> 
<ol> 
 <li>缩小窗口大小，使上部呈现滚动条</li> 
 <li>悬停在上部</li> 
 <li>使用触控板滚动</li> 
 <li>在安装 Flutter 3.3 之前，在触控板上滚动会拖动项目，因为 Flutter 正在 dispatching 模拟的一般事件</li> 
 <li>安装 Flutter 3.3 后，在触控板上滚动会正确滚动列表，因为 Flutter 提供的是“滚动”手势，该手势无法被卡片识别，但可以被滚动视图识别</li> 
</ol> 
<p>更多详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1oRvebwjpsC3KlxN1gOYnEdxtNpQDYpPtUFAkmTUe-K8%2Fedit%3Fresourcekey%3D0-pt4_T7uggSTrsq2gWeGsYQ" target="_blank">Flutter Trackpad Gesture</a> 以及 PR。</p> 
<ul> 
 <li>PR 89944:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F89944" target="_blank">Support trackpad gestures in framework</a></li> 
 <li>PR 31591:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F31591" target="_blank">iPad trackpad gestures</a></li> 
 <li>PR 34060:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F34060" target="_blank">Re-land “ChromeOS/Android trackpad gestures”</a></li> 
 <li>PR 31594:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F31594" target="_blank">Win32 trackpad gestures</a></li> 
 <li>PR 31592:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F31592" target="_blank">Linux trackpad gestures</a></li> 
 <li>PR 31593:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F31593" target="_blank">Mac trackpad gesturesmacOS</a></li> 
</ul> 
<p><strong>Scribble</strong></p> 
<p>Flutter 现在支持在 iPadOS 上使用 Apple Pencil 进行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.apple.com%2Fguide%2Fipad%2Fenter-text-with-scribble-ipad355ab2a7%2Fipados" target="_blank">Scribble</a> 手写输入。默认情况下，此功能在<code>CupertinoTextField</code>、<code>TextField</code>和<code>EditableText</code>上启用。</p> 
<p><img alt height="114" src="https://oscimg.oschina.net/oscnet/up-5a2db01fb2415d42b5da6d1f09db74bd471.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>文字输入</strong></p> 
<p>为了改进对富文本编辑的支持，此版本引入了从平台的<code>TextInputPlugin</code>接收细化文本更新的能力。以前，<code>TextInputClient</code>只交付新的编辑状态，新旧之间没有差异，<code>TextEditingDeltas</code>和<code>DeltaTextInputClient</code>填补了这个信息空白。了解更多信息，可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflutter.github.io%2Fsamples%2Frich_text_editor.html" target="_blank">富文本编辑器演示</a>。</p> 
<p><strong>Material Design 3</strong></p> 
<p>Flutter 团队继续将更多 Material Design 3 组件迁移到 Flutter。此版本包括对<code>[IconButton](https://api.flutter.dev/flutter/material/IconButton-class.html)</code>、<code>[Chips](https://api.flutter.dev/flutter/material/Chip-class.html)</code>以及<code>[AppBar](https://api.flutter.dev/flutter/material/AppBar-class.html)</code>的大号和中号变体的更新。要监控 Material Design 3 迁移的进度，可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F91605" target="_blank">Bring Material 3 to Flutter</a>。</p> 
<p><strong>图标按钮</strong></p> 
<p><strong><img alt height="134" src="https://oscimg.oschina.net/oscnet/up-fe4eb98fd33ed119efb9b29a580625917a2.png" width="500" referrerpolicy="no-referrer"></strong></p> 
<p><strong>Chip</strong></p> 
<p><strong><img alt height="521" src="https://oscimg.oschina.net/oscnet/up-0ff39342c084d41bbfcb44d77466eb363c7.png" width="500" referrerpolicy="no-referrer"></strong></p> 
<p><strong>大中型 AppBar</strong></p> 
<p><strong><img alt height="167" src="https://oscimg.oschina.net/oscnet/up-040968acfed7cc4c4c803c3e285a0913207.gif" width="300" referrerpolicy="no-referrer"><img alt height="167" src="https://oscimg.oschina.net/oscnet/up-11eff918bbb28a8ab39e2d18ddbffcd6167.gif" width="300" referrerpolicy="no-referrer"></strong></p> 
<h4><strong>桌面</strong></h4> 
<p><strong>Windows</strong></p> 
<p>以前，Windows 桌面应用程序的版本由特定于 Windows 应用程序的文件设置。此行为与其他平台设置其版本的方式不一致。现在可以从你的项目<code>pubspec.yaml</code>文件和构建参数中设置 Windows 桌面应用程序版本。</p> 
<p>有关设置应用程序版本的更多信息，建议遵循 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Fdeployment%2Fwindows%23updating-the-apps-version-number" target="_blank">docs.flutter.dev</a> 上的文档和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Fdevelopment%2Fplatform-integration%2Fwindows%2Fversion-migration" target="_blank">迁移指南</a>。在 Flutter 3.3 之前创建的项目需要更新才能获得此功能。</p> 
<h4>Packages</h4> 
<p><strong>go_router</strong></p> 
<p>为了扩展 Flutter 的 native navigation API，该团队发布了一个新版本的<code>go_router</code>包，使设计适用于移动设备、桌面和 Web 的路由逻辑变得更加简单。</p> 
<p>该<code>[go router](https://pub.dev/packages/go_router)</code>包由 Flutter 团队维护，通过提供声明性的、基于 url 的 API 来简化路由，从而更容易 navigate 和处理 deep-links。最新版本 (4.3) 允许应用程序使用异步代码重定向，并包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F10l22o4ml4Ss83UyzqUC8_xYOv_QjZEi80lJDNE4q7wM%2Fedit%3Fusp%3Dsharing%26resourcekey%3D0-U-BXBQzNfkk4v241Ow-vZg" target="_blank">迁移指南</a>中描述的其他 breaking changes。有关更多信息，可查看 docs.flutter.dev 上的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Fdevelopment%2Fui%2Fnavigation" target="_blank">Navigation and routing</a> 页面。</p> 
<h4><strong>VS Code 扩展增强</strong></h4> 
<p>Flutter 的 Visual Studio Code 扩展有几个更新，包括添加依赖项的改进。**现在可以使用 Dart: Add Dependency **一步添加多个以逗号分隔的依赖项。</p> 
<p><img alt height="203" src="https://oscimg.oschina.net/oscnet/up-3ea1d2590a5048d0352a37942a90baf936e.gif" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong>Flutter 开发者工具更新</strong></h4> 
<p>自上一个稳定的 Flutter 版本以来，DevTools 进行了许多更新，包括对数据显示表的 UX 和性能改进，以便更快、更好地滚动大型事件列表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fdevtools%2Fpull%2F4175" target="_blank">#4175</a> )。</p> 
<h4><strong>Performance</strong></h4> 
<p><strong>Raster cache 改进</strong></p> 
<p>此版本通过消除 copies 和减少 Dart 垃圾收集 (GC) 压力来提高从 assets 加载 image 的性能。以前，在加载 asset images 时，<code>ImageProvider</code>API 需要多次复制压缩数据。首先，当打开 asset 并将其作为类型化数据数组公开给 Dart 时，它被复制到 native heap 中。然后，当该类型化数据数组被复制到 ui.ImmutableBuffer 的内部存储时，它又被第二次复制。</p> 
<p>随着 ui.ImmutableBuffer.fromAsse t的加入，压缩的 image bytes 可以直接加载到用于解码的结构中。这种方法需要对 ImageProviders 的 byte loading pipeline 进行修改。这个过程也更快，因为它绕过了之前基于通道的加载器方法所需的一些额外的调度开销。</p> 
<p>其测试结果表明，image 加载时间提高了近 2 倍。</p> 
<p><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-a1725d470f32c217a60a0fe1dc5166145c6.png" width="500" referrerpolicy="no-referrer"></p> 
<p>有关更多信息和迁移指南，可参阅 docs.flutter.dev 上的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Frelease%2Fbreaking-changes%2Fimage-provider-load-buffer" target="_blank"> Adding ImageProvider.loadBuffer 。</a></p> 
<h4><strong>Stability</strong></h4> 
<p><strong>iOS 指针压缩已禁用</strong></p> 
<p>虽然禁用指针压缩会增加 Dart 对象消耗的内存，但它也增加了 Flutter 应用程序的非 Dart 部分的可用内存，因此总体上更可取。</p> 
<h4><strong>API 改进</strong></h4> 
<p><strong>PlatformDispatcher.onError</strong></p> 
<p>在此版本中，你应该通过设置<code>PlatformDispatcher.onError</code>回调来捕获所有错误和异常，而不是使用自定义<code>Zone</code>。有关更多信息，可查看 docs.flutter.dev 上 更新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Ftesting%2Ferrors" target="_blank">Handling errors in Flutter</a> 页面。</p> 
<p><strong>FragmentProgram 更改</strong></p> 
<p>用 GLSL 编写并列在应用程序 pubspec.yaml 文件的 Flutter manifest 中 shaders: 部分下的片段着色器现在将被自动编译为引擎理解的正确格式，并作为资产与应用程序捆绑。由于这一变化，你将不再需要使用第三方工具手动编译着色器。今后，你应该将 Engine 的 FragmentProgram API 视为只接受 Flutter 的构建工具的输出。目前还没有这种情况，但计划在未来的版本中进行此更改，如 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fflutter.dev%2Fgo%2Ffragment-program-support" target="_blank">FragmentProgram API 支持改进</a>设计文档中所述。</p> 
<p>有关此更改的示例，可参阅此 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzanderso%2Ffragment_shader_example" target="_blank">Flutter</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzanderso%2Ffragment_shader_example" target="_blank">shader example</a>。</p> 
<p><strong>Fractional translation</strong></p> 
<p>以前，Flutter Engine 总是将合成层与精确的像素边界对齐，因为它提高了旧款（32 位）iPhone 的渲染性能。自从添加桌面支持以来，开发团队注意到这导致了可观察到的捕捉行为，因为屏幕设备像素比通常要低得多。例如，在低 DPR 屏幕上，可以看到工具提示在淡入时明显捕捉。在确定这种像素捕捉对于新 iPhone 型号的性能不再必要后，其从 Flutter Engine 中删除了这种像素捕捉以提高桌面保真度。此外，去除这种像素捕捉还可以稳定一些 golden image 测试，因为这些图像经常会出现细微的渲染差异。</p> 
<h4><strong>对支持平台的更改</strong></h4> 
<h4><strong>32 位 iOS 弃用</strong></h4> 
<p>由于使用量减少，该版本是<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fflutter.dev%2Fgo%2Frfc-32-bit-ios-unsupported" target="_blank">最后一个支持 32 位 iOS 设备和 iOS 版本 9 和 10</a>的版本。此更改影响 iPhone 4S、iPhone 5、iPhone 5C 以及第 2、3d 和第 4 代 iPad 设备。Flutter 3.3 稳定版本和所有后续稳定版本不再支持 32 位 iOS 设备以及 iOS 9 和 10 版本。这意味着基于 Flutter 3.3 及更高版本构建的应用程序将无法在这些设备上运行。</p> 
<p><strong>停用 macOS 10.11 和 10.12</strong></p> 
<p>在 2022 年第四季度稳定版本中，预计将放弃对 macOS 版本 10.11 和 10.12 的支持。这意味着在那之后针对稳定的 Flutter SDK 构建的应用程序将不再在这些版本上运行，并且 Flutter 支持的最低 macOS 版本将增加到 10.13 High Sierra。</p> 
<p><strong>Bitcode 弃用</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fxcode-release-notes%2Fxcode-14-release-notes" target="_blank">在即将发布的 Xcode 14 版本中，iOS 应用程序提交将不再接受</a> Bitcode ，并且启用了 bitcode 的项目将在此版本的 Xcode 中发出构建警告。鉴于此，Flutter 将在未来的稳定版本中放弃对 Bitcode 的支持。</p> 
<p>默认情况下，Flutter 应用程序没有启用 Bitcode，因此其预计此举不会影响许多开发人员。但是，如果你在 Xcode 项目中手动启用了 bitcode，需在升级到 Xcode 14 后立即禁用它；可以通过打开<code>ios/Runner.xcworkspace</code>并将构建设置 **Enable Bitcode **设置为 <strong>No</strong>。Add-to-app 开发者也建议在 host Xcode 项目中禁用它。</p> 
<p><img alt height="237" src="https://oscimg.oschina.net/oscnet/up-655196a6bbb8b0d64b3b3867bf77663730e.png" width="500" referrerpolicy="no-referrer"></p> 
<p>可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhelp.apple.com%2Fxcode%2Fmac%2F11.0%2Findex.html%3FlocalePath%3Den.lproj%23%2Fdevde46df08a" target="_blank">Apple 的文档</a>以了解更多信息。</p>
                                        </div>
                                      
</div>
            