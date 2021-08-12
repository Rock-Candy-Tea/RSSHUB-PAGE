
---
title: 'Android 12 Beta 4 发布，已达到平台稳定性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1703'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1703'
---

<div>   
<div class="content">
                                                                                            <p>Google 今天发布了 Android 12 的第四个 Beta 版本，并进入了发布的最后阶段。这也意味着 Android 12 的 API 和所有面向应用的行为都已最终确定。对于应用程序来说，现在的重点是兼容性和质量，以便在今年晚些时候随着 Android 12 的正式发布一同推出。</p> 
<p>此前没有注册登记测试版的开发者可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">点击链接</a>获得 Beta 4 的推送，如果以前已经注册过，则会自动获得 Beta 4 的更新。</p> 
<h3>平台稳定性</h3> 
<p>Android 12 Beta 4 已经达到了平台稳定性，这是一个里程碑，意味着在 Android 12 中所有面向应用的行为都已最终确定。这不仅包括官方 SDK 和 NDK API，还包括最终面向应用的系统行为和可能影响应用的非 SDK 接口的限制。从 Beta 4 开始，开发者可以发布应用的兼容性更新，因为平台不会再发生改变。</p> 
<p>Google 要求所有的应用程序和游戏开发者从现在开始进行最后的兼容性测试，并准备在 Android 12 最终发布前尽快发布应用的兼容性更新。</p> 
<p></p> 
<h3>应用程序的兼容性</h3> 
<p>对于 Android 12 来说，应用兼容性意味着你的应用能在新版本的平台上如期运行。你可以检查你的应用程序的兼容性，只需在设备或模拟器上安装你的应用程序的生产版本并进行测试。</p> 
<p>因为每一个 Android 版本，Google 都会对平台进行整体的改变，以改善隐私和安全以及操作系统的整体用户体验。这些都会影响你的应用程序，所以开发者应该检查一下行为变化，并针对它们进行测试，然后向用户发布一个兼容的更新。</p> 
<p>以下是一些需要测试的变化（适用于你的应用程序的 targetSdkV 版本为 31 或更高的情况）。</p> 
<ul> 
 <li>前台服务启动限制 —— 应用程序不能再从后台启动前台服务。对于高优先级的后台任务，请使用 WorkManager 中的加速作业来代替；</li> 
 <li>近似位置 —— 当应用程序请求精确位置的许可时，用户现在可以选择授予精确或近似位置；</li> 
 <li>新的精确警报权限 —— 想要使用精确警报的应用程序必须申请一个新的权限 <code>SCHEDULE_EXACT_ALARM</code>;</li> 
 <li>WebView 中的现代 SameSite cookie 行为 —— 如果开发者的应用程序使用 WebView，请使用新的 SameSite cookie 行为测试您的应用程序；</li> 
 <li>更安全的组件导出 —— 你的应用必须为任何使用意图过滤器的应用组件明确指定 <code>android:exported</code> 属性；</li> 
 <li>自定义通知 —— 系统将标准通知模板应用于完全自定义的通知，并为应用名称、应用图标和展开/折叠数据提供支持；</li> 
 <li>通知 trampoline 限制 —— 通知不能再使用 “trampoline” 启动您的应用程序 —— 一个启动目标活动的中间广播接收器或服务；</li> 
</ul> 
<p>在未来几周，还有一个 Beta 版将作为候选发布版，供开发者进行最后测试。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2021%2F08%2Fandroid-12-beta-4-and-platform-stability.html" target="_blank">https://android-developers.googleblog.com/2021/08/android-12-beta-4-and-platform-stability.html</a></p>
                                        </div>
                                      
</div>
            