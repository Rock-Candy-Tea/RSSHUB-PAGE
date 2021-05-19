
---
title: 'Android 12 Beta 1 发布，改善 UI 和隐私，引入设备高性能标准'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0519/074630_bYpn_4937141.jpeg'
author: 开源中国
comments: false
date: Wed, 19 May 2021 07:50:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0519/074630_bYpn_4937141.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在今天的 Google I/O 大会上，Google 发布了 Android 12 的第一个测试版。Android 12 Beta 对 Android 系统进行的非常大的改动，以下是一些值得关注的变化。</p> 
<p><strong>适用于 Android 的新用户界面</strong></p> 
<p>正如 Android Developer 在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.google%2Fproducts%2Fandroid%2Fandroid-12-beta" target="_blank">消费者博客</a>中强调的那样，Android 12 带来了 Android 历史上最大的设计变化。Google 重新思考了整个体验，从色彩到形状、光线和动画，使 Android 12 更具表现力、活力和个性化。这项工作是在 Google 的软件、硬件和 Material Design 团队之间的深度合作下完成的，Google 正在将软件和硬件生态系统统一在一种名为 Material You 的设计语言之下。</p> 
<p><img alt height="395" src="https://static.oschina.net/uploads/space/2021/0519/074630_bYpn_4937141.jpeg" width="700" referrerpolicy="no-referrer"></p> 
<p>Google 已经将新的设计语言扩展到整个平台和 UI 组件，因此你的应用程序将自动获得这些升级。</p> 
<p>重新设计的小部件 - 随着 Android 12 的设计变化，Google 已经更新了应用程序的小部件，使它们更好用、更漂亮，也更容易被发现。Google 增加了新的交互式控件，如复选框、开关和单选按钮。Android 12 的小部件与新的系统 UI 和主题搭配起来非常漂亮，圆角和填充会自动适应每个启动器和主屏幕。响应式布局可以让小部件适应手机、平板电脑、可折叠设备和其他屏幕类型的设备。Google 还添加了动态颜色 API，这样你的小部件就可以使用系统颜色来创建一个个性化但一致的外观。我们还通过改进的小部件选择器和与 Assistant 的集成，使小部件更容易被发现。</p> 
<p><img alt height="971" src="https://static.oschina.net/uploads/space/2021/0519/074649_TIxV_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>拉伸滚动 - Google 还增加了一个新的系统范围内的 "拉伸" 滚动效果，让用户知道他们已经滚动到了用户界面中可用内容的末端。拉伸效果提供了一个自然的垂直和水平滚动停止的指示器，在所有的应用程序中都是通用的，它在整个平台和 AndroidX 的滚动容器中默认启用。新的拉伸滚动取代了以前版本中支持的 Glow 滚动。请确保用新的滚动行为测试你的应用程序和内容。</p> 
<p>更流畅的音频过渡 - UI 不仅仅是视觉效果。Google 还改进了处理音频的方式。当一个应用程序播放的音频会被另一个应用程序的音频内容取代时，前者的音频会自动淡出，从而在播放音频的应用程序之间提供一个更平滑的过渡，并防止多个应用程序之间相互播放音频。这在可折叠和多屏幕的安卓环境中尤为重要。</p> 
<p><strong>性能</strong></p> 
<p>在 Android 12 中，Google 对性能进行了重大而深入的投入——从使系统和应用更快、更流畅的基础性能，到帮助开发者在这些设备上提供更丰富体验的高性能设备新标准。</p> 
<p>更快、更高效的系统性能 - Google 将核心系统服务所需的CPU时间减少了22％，因此设备运行速度将更快，响应速度也更快。我们还通过将系统服务器对大内核的使用减少了 15％，以帮助设备在需要充电之前运行更长的时间，从而提高了 Android 的电源效率。</p> 
<p><img alt height="122" src="https://static.oschina.net/uploads/space/2021/0519/074717_Zfqg_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Google 通过减少 lock 争用和等待时间的变化来改善过渡和应用程序的启动时间，并优化了 I/O 以加快应用程序的加载。在 PackageManager 中，只读快照减少了 92% 的 lock 争用。在 Binder 中，轻量级缓存从根本上改善了目标调用的延迟，最高可达 47 倍。在 I/O 中，加速了 dex/odex/vdex 文件，以改善应用的加载时间，特别是在低内存手机上。Google 对 notification trampolines 的限制也有助于减少从通知中启动应用程序的延迟。例如，在这样的背景下 Google 相册现在的启动速度提高了 34%。</p> 
<p>为了提高数据库查询性能，Google 通过在 Binder 事务中内联结果来优化 CursorWindow。对于小窗口，CursorWindow 的速度提高了36%，而对于超过 1000 行的窗口，改进幅度高达49倍。</p> 
<p>性能等级 - 从 Android 12 开始，Google 与生态系统的合作伙伴一起合作，为高性能的 Android 设备引入了一个通用标准。</p> 
<p>这个标准被称为性能等级，定义了一套超越 Android 基线要求的能力。符合性能等级要求的设备可以支持更苛刻的用例并提供更高质量的内容。开发人员可以在运行时检查性能等级，然后可靠地提供增强的体验，充分利用设备的性能。</p> 
<p>最初，Google 将性能等级的能力集中在媒体使用案例上，要求包括相机启动延迟、编解码器的可用性和编码质量，以及最低内存大小、屏幕分辨率和读/写性能。</p> 
<p><strong>设计中的隐私</strong></p> 
<p>隐私是 Google 当前一切工作的核心，在 Android 12 中，Google 将继续为人们提供更多的透明度和控制权，同时保证他们的设备和数据安全。</p> 
<p>应用程序休眠 - 去年 Google 推出了权限自动重置，在过去的两周里，已经为超过 850 万个没有被使用的应用程序重置了权限——因此已经被用户遗忘的应用程序仍然无法访问他们的数据。在 Android 12 中，我们在权限自动重置的基础上，对长时间未使用的应用进行智能休眠，从而对设备存储、性能和安全进行优化。休眠不仅撤销了用户之前授予的权限，而且还会强制停止应用程序，并回收了内存、存储和其他临时资源。在这种状态下，系统还可以防止应用程序在后台运行或接收推送通知，帮助用户保持安全。</p> 
<p><img alt height="890" src="https://static.oschina.net/uploads/space/2021/0519/074753_N0MY_4937141.gif" width="412" referrerpolicy="no-referrer"></p> 
<p>附近设备权限 - 以前，蓝牙扫描要求应用拥有位置权限，这对需要与附近设备配对但实际上不需要设备位置的应用是一个挑战。我们现在允许应用程序扫描附近的设备，而不需要位置许可。以 Android 12 为目标的应用程序可以使用新的 BLUETOOTH_SCAN 权限进行扫描，并使用 usesPermissionFlags="neverForLocation" 属性。与设备配对后，使用 BLUETOOTH_CONNECT 权限与之交互。这些权限促进了隐私友好的应用设计。</p> 
<p>近似位置 - 此前 Google 给用户提供了更好的方法来管理应用对位置的访问，例如用户可以选择是否允许应用在前台或后台访问位置，以及“仅允许一次”的选项。现在，对于针对 Android 12 的应用程序，Google 通过新的 "近似位置" 选项提供了更多控制。当应用程序请求精确的位置数据时，用户现在可以选择授予精确或近似的位置。用户还可以在 "设置" 中改变一个应用程序的位置精度。</p> 
<p><strong>应用程序的兼容性</strong></p> 
<p>如果开发者还没有测试你的应用程序与 Android 12 的兼容性，现在是时候随着 Android 12 进入测试阶段开始这么做了，Google 将向早期用户和开发者开放 Pixel 和其他设备的访问权限。这意味着在未来几周内，预计会有更多的用户在 Android 12 上尝试你的应用程序，并提出他们发现的任何问题。</p> 
<p>为了测试兼容性，从 Google Play 或其他来源将你发布的应用程序安装在运行 Android 12 Beta 的设备或模拟器上，并通过应用程序的所有流程。审查行为变化以集中测试。在你解决了任何问题后，尽快发布更新。</p> 
<p>通过 Beta 版，Google 正越来越接近设定的 2021 年 8 月的平台稳定期。从那时起，面向应用程序的系统行为、SDK/NDK API 和非 SDK 列表将被最终确定。届时，完成最后的兼容性测试，并发布你的应用程序、SDK 或库的完全兼容版本。</p> 
<p><img alt height="160" src="https://static.oschina.net/uploads/space/2021/0519/074816_BC29_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>开始使用 Android 12</strong></p> 
<p>今天的 Beta 版提供了尝试 Android 12 功能，测试开发者的应用并向 Google 提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Ffeedback" target="_blank">反馈</a>所需的一切。只需<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">在此处注册受支持的 Pixel 设备</a>即可通过 OTA 的方式获取更新。如果您已经安装了预览版本，则将自动获取 Beta 更新。</p> 
<p>用户还可以从参与 Android 12 开发者预览计划的一些顶级设备制造商合作伙伴的设备上获取 Android 12 Beta。访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">android.com/beta</a>，查看合作伙伴的完整列表，以及指向其网站的链接和其支持设备的详细信息。</p> 
<p>有关如何获取Beta的完整详细信息，请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2F12" target="_blank">Android 12开发人员网站</a>。</p>
                                        </div>
                                      
</div>
            