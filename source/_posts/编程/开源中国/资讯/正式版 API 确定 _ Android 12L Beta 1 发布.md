
---
title: '正式版 API 确定 _ Android 12L Beta 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/12/jpRA0h.png'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 11:58:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/12/jpRA0h.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://devrel.andfun.cn/devrel/posts/2021/12/jpRA0h.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>作者 / Maru Ahues Bouza, Director, Android Developer Relations</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在 10 月份的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fevents%2Fdev-summit" target="_blank">Android 开发者峰会</a><span> </span>上，我们强调了平板电脑、可折叠设备和 Chromebook 等大屏幕设备的增长，以及如何通过新的 Jetpack API、工具和指南，让开发者们<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2021%2F11%2Fandroid-developer-summit-21-large-screens.html" target="_blank">更容易为这些设备构建</a><span> </span>出良好的应用体验。我们还发布了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2F12L" target="_blank">Android 12L</a><span> </span>的开发者预览版，这是一个专为大屏幕设计的 Android 12 功能更新。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">通过 12L，我们为大屏幕优化和打磨了系统界面，使多任务处理更加强大和直观，并改善了兼容性支持，让应用在默认情况下也有更好的视觉效果。12L 还为开发者提供了一些新的 API，如空间音频以及改进的拖放操作，以打造更好的大屏幕体验。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">今天，我们正式发布 Android 12L 的第一个 Beta 版，供大家对应用进行测试并提交反馈，从而为明年年初发布的功能更新做好准备。您可以在 Android Studio 中<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fget" target="_blank">设置 Android 模拟器</a><span> </span>来尝试新的大屏幕功能。Android 12L 也适用于手机，只需<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">注册参与测试</a>，即可在受支持的 Pixel 设备上获取 Android 12L Beta 1。如果您已经参与 Android 12 Beta 测试，则会自动获得 12L 更新。我们与联想合作，让您也可以在联想 Tab P12 Pro 平板电脑上体验 Android 12L，更多关于可用构建和支持的信息，请前往<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.lenovo.com" target="_blank">联想官方网站</a><span> </span>查阅。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Android 12L Beta 1 内容一览</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">今天发布的 Beta 1 版本包含对功能和用户体验的改进，最新的 bug 修复和优化，以及 2021 年 12 月安全补丁。对于开发者来说，我们提早完成了 API，因此 Beta 1 还包含 Android 12L 的正式版 API (API 级别 32)，更新的构建工具，以及用于测试的系统映像。您可以用这些来测试应用在 Android 12L 的各种功能中的表现。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在 Android 12L 中，我们专注于完善大屏幕设备上的用户界面，包括通知、快捷设置、锁屏、概览、主屏幕等等。例如，在 600dp 宽度以上的屏幕里，通知栏、锁屏和其他系统界面会采用全新的双列布局，以充分利用屏幕面积。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="△ 双列布局可以显示更多内容，更易于使用" src="https://devrel.andfun.cn/devrel/posts/2021/12/KNy3us.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">△ 双列布局可以显示更多内容，更易于使用</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">多任务处理也更加强大和直观—— Android 12L 在大屏幕上提供了一个新的任务栏，让用户可以随时切换到喜爱的应用，或将应用拖放至分屏模式。请记住，在 Android 12 及以后的版本中，用户可以将任何应用以分屏模式启动，无论该应用是否声明为可以调整大小。所以请务必<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L%2Fsummary%23what-to-test" target="_blank">在分屏模式下测试您的应用</a>！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="△ 将应用拖放至分屏模式" src="https://devrel.andfun.cn/devrel/posts/2021/12/iDPDNa.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">△ 将应用拖放至分屏模式</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最后，通过改进兼容模式的视觉效果和稳定性，我们为用户带来了更好的黑边模式体验，并帮助应用在默认情况下看起来更好。如果您的应用还没有针对大屏幕进行优化，请<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L%2Fsummary%23what-to-test" target="_blank">测试其在新的黑边模式中的表现</a>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>更多 API 和工具助力大屏幕构建</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">我们新推出的这些 API 和工具可以在您为大屏幕优化应用时更轻松地为用户打造流畅体验:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>适用于大屏幕的 Material 模式</strong><span> </span>- 新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fm3.material.io%2Ffoundations%2Fadaptive-design%2Foverview" target="_blank">Material 设计指南</a><span> </span>可以帮您在所有尺寸的屏幕上扩展应用界面。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>支持自适应界面的 Jetpack Compose</strong><span> </span>- Jetpack Compose 可以让您非常轻松地处理不同屏幕尺寸或组件中的界面变化。请通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fcompose%2Flayouts%2Fadaptive" target="_blank">在 Compose 中构建自适应布局</a><span> </span>指南了解这方面的基础知识。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>用于管理用户界面的窗口大小分类</strong><span> </span>-<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Ftopics%2Flarge-screens%2Fsupport-different-screen-sizes%23window_size_classes" target="_blank">窗口大小分类</a><span> </span>(Window Size Classes) 是一组按照视窗大小作为分类 (称为 "断点") 的意见性指导，有助于简化设计、开发和测试可调整大小的应用布局。此 API 即将在 Jetpack<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fandroidx%2Freleases%2Fwindow" target="_blank">WindowManager</a><span> </span>1.1 中推出。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Activity Embedding</strong><span> </span>- 通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Ftopics%2Flarge-screens%2Factivity-embedding" target="_blank">Activity Embedding API</a>，您可以利用大屏幕上的额外显示区域一次显示多个 Activity，从而实现如 "列表-详情" 的布局模式，并且几乎不需要 (或只需少量) 重构应用。此 API 在 Jetpack<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fandroidx%2Freleases%2Fwindow" target="_blank">WindowManager</a><span> </span>1.0 Beta 03 及之后的版本中可用。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Android Studio 中的视觉 lint 工具</strong><span> </span>- 在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview" target="_blank">Android Studio Chipmunk</a><span> </span>中提供了新的视觉 lint 工具，它能在布局验证 (Layout Validation) 中主动给出界面方面的警告和建议，以帮助您识别大屏幕布局中的潜在问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>可调整尺寸的模拟器</strong><span> </span>- 这是随 Android Studio Chipmunk 一同推出的全新模拟器配置，让您可以在四个参考设备 (手机、可折叠设备、平板电脑和台式机) 之间快速切换，以便于测试。</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">请务必查看我们准备的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L%23optimize-for-large-screens" target="_blank">大屏幕开发者资源</a>，以了解这些以及更多 API 和工具的详细信息。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>在设备上开始体验 Android 12L！</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Android 12L 功能更新将在明年初正式发布，现在是时候开始为大屏幕优化自己的应用了。对于开发者来说，我们强烈建议检查您的应用在各种尺寸窗口分屏模式下的工作情况。如果您还没有优化应用，请查看一下它在不同屏幕朝向中的视觉效果，并尝试一下新的兼容模式 (如果适用的话)。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">想要开始使用大屏幕功能，最简单的方法就是使用 Android 模拟器的可折叠设备或平板电脑设置，请参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L%2Fget" target="_blank">完整设置说明</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">您也可以将 Android 12L 刷入大屏幕实体设备中。我们与联想合作，让您可以在联想 Tab P12 Pro 上体验 Android 12L 的预览版本。目前，联想提供的是开发者预览版 1，未来几周内会有更新。请访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.lenovo.com%2F" target="_blank">联想的 Android 12L 预览网站</a><span> </span>了解关于可用版本和支持的完整信息。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Android 12L 也将运行在手机中。虽然大屏幕功能不会出现在小屏幕设备中，但我们也欢迎您体验这一功能更新的最新改进。只需<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">用受支持的 Pixel 设备完成注册</a>，就可以通过 OTA 更新获得最新的 Android 12L Beta 版。如果您已经参与 Android 12 Beta 测试，则会自动获得 12L 更新。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">有关 Android 12L 的更多细节和发布时间表，请访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L" target="_blank">Android 12L 开发者网站</a>。别忘了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F12L%2Ffeedback" target="_blank">提交问题和需求</a>，我们一如既往地感谢来自大家的反馈意见！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎您<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fservices.google.cn%2Ffb%2Fforms%2Fandroiddevswechat2%2F" target="_blank">点击这里</a><span> </span>向我们提交反馈，或分享您喜欢的内容、发现的问题。您的反馈对我们非常重要，感谢您的支持！</p>
                                        </div>
                                      
</div>
            