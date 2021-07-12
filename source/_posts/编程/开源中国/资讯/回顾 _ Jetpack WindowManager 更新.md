
---
title: '回顾 _ Jetpack WindowManager 更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/07/vE0y4W.gif'
author: 开源中国
comments: false
date: Mon, 12 Jul 2021 13:42:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/07/vE0y4W.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/07/vE0y4W.gif" referrerpolicy="no-referrer"></p> 
<p>在今年年初，我们发布了 Jetpack WindowManager 库 alpha02 版本，这是一个较为重大的版本更新，并且包含部分已弃用的 API (目前已经发布到 1.0.0-alpha09 版)，本文将为您回顾这次版本更新的内容。</p> 
<p>Jetpack WindowManager 库可帮助您构建能够感知折叠和铰链等新设备功能的应用，使用以前不存在的新功能。在开发 Jetpack WindowManager 库时，我们结合了开发者的反馈意见，并且在 Alpha 版本中持续迭代 API，以提供一个更干净完整的 API 界面。我们一直在关注 WindowManager 空间中的不同领域以提供更多的功能，我们引入了 WindowMetrics，以便您可以在 Android 4.1 (API 级别 16) 及以上版本使用这些在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fkotlin%2Fandroid%2Fview%2FWindowMetrics" target="_blank">Android 11 加入的新 API</a>。</p> 
<p>首版发布后，我们用了大量时间来分析开发者反馈，并在 alpha02 版本中进行了大量的更新，接下来我们来看在 alpha02 版本中更新的具体内容！</p> 
<p><strong>新建一个 WindowManager</strong></p> 
<p>Alpha02 版本提供了一个简单的构造函数，这个构造函数只有一个参数，参数指向一个可见实体 (比如当前显示的 Activity) 的 Context:</p> 
<pre><code>val windowManager = WindowManager(context: Context)
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroidx%2Fwindow%2FWindowManager%23WindowManager%28android.content.Context%2C%2520androidx.window.WindowBackend%29" target="_blank">原有的构造函数</a> 仍可使用，但已被标记为废弃:</p> 
<pre><code>@Deprecated
val windowManager = WindowManager(context: Context, windowBackend: WindowBackend?)
</code></pre> 
<p>当您想在一个常见的设备或模拟器上使用一个自定义的 WindowBackend 模拟一个可折叠设备时，可使用原有的构造函数进行测试。这个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandroid%2Fuser-interface-samples%2Ftree%2Fmain%2FWindowManager" target="_blank">样例工程</a> 中的实现可以供您参考。</p> 
<p>在 alpha02 版本，您仍可给参数 WindowBackend 传参为 null，我们计划在未来的版本中将 WindowBackend 设置为必填参数，移除 deprecation 标志，以推动此接口在测试时使用。</p> 
<p><strong>添加 DisplayFeature 弃用 DeviceState</strong></p> 
<p>另一个重大变化是弃用了 <code>DeviceState</code> 类，同时也弃用了使用它通知您应用的回调。之所以这样做，是因为我们希望提供更加通用的 API，这些通用的 API 允许系统向您的应用返回所有可用的 DisplayFeature 实例，而不是定义全局的设备状态。我们在 alpha06 的版本中已经将 DeviceState 从公共 API 中移除，请改用 FoldingFeature。</p> 
<p>alpha02 版本引入了带有更新了回调协议的新 <code>DisplayFeature</code> 类，以在 <code>DisplayFeature</code> 更改时通知您的应用。您可以注册、反注册回调来使用这些方法:</p> 
<pre><code>registerLayoutChangeCallback(@NonNull Executor executor, @NonNull Consumer<WindowLayoutInfo> callback)

unregisterLayoutChangeCallback(@NonNull Consumer<WindowLayoutInfo> callback)
</code></pre> 
<p><code>WindowLayoutInfo</code> 包含了位于 window 内的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroidx%2Fwindow%2FDisplayFeature" target="_blank"><code>DisplayFeature</code></a> 实例列表。</p> 
<p><code>FoldingFeature</code> 类实现了 <code>DisplayFeature</code> 接口，其中包含了有关下列类型功能的信息:</p> 
<pre><code>TYPE_FOLD（折叠类型）

TYPE_HINGE（铰链类型）
</code></pre> 
<p>设备可能的折叠状态如下:</p> 
<p><img alt="△ DisplayFeature 可能的状态: 完全展开、半开、翻转" src="https://devrel.andfun.cn/devrel/posts/2021/07/mbkH6y.png" referrerpolicy="no-referrer"></p> 
<p>△ DisplayFeature 可能的状态: 完全展开、半开、翻转</p> 
<p>需要注意的是这里没有与 DeviceState 中 POSTURE_UNKNOWN 和 POSTURE_CLOSED 姿态对应的状态。</p> 
<p>要获取最新的状态信息，您可以使用已注册回调返回的 <code>FoldingFeature</code> 信息:</p> 
<pre><code>class LayoutStateChangeCallback : Consumer<WindowLayoutInfo> &#123;
  override fun accept(newLayoutInfo: WindowLayoutInfo) &#123;
    // 检查 newLayoutInfo. getDisplayFeatures() 的返回值，      
    // 看它是否为 FoldingFeature 实例，并获取其中的信息。
  &#125;
&#125;
</code></pre> 
<p>如何使用这些信息，请参阅: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandroid%2Fuser-interface-samples%2Ftree%2Fmain%2FWindowManager" target="_blank">https://github.com/android/user-interface-samples/tree/main/WindowManager</a>。</p> 
<p><strong>更好的回调注册</strong></p> 
<p>上述示例代码的回调 API 也更加健壮了。在之前版本中，如果应用在 window 可用之前注册回调，将会抛出异常。</p> 
<p>在 aplha02 版本中我们修改了上述的行为。您可在对您应用设计有用的任何时候，注册这些回调，库会在 window 可用时发送初始 WindowLayoutInfo。</p> 
<p><strong>R8 规则</strong></p> 
<p>我们在库中添加了 R8 的 "keep" 规则，以保留那些因为内部模块的组织架构而可能被删除的方法或类。这些规则会自动合并到应用最终的 R8 规则中，这样可以防止应用出现如 alpha01 版本上的崩溃。</p> 
<h2><strong>WindowMetrics</strong></h2> 
<p>由于历史的命名习惯和各种可能的 Window Manager 状态，在 Android 上获取当前 window 的尺寸信息比较困难。Android 11 中一些被废弃的方法 (例如 <code>Display#getSize</code> 和 Display#getMetrics) 和在 window 尺寸新的 API 的使用，都凸显了可折叠设备从全屏到多窗口和自适应窗口这一上升的趋势。为了简化这一过渡过程，我们在 Android 11 中增加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fview%2FWindowMetrics" target="_blank">WindowMetrics API</a>。</p> 
<p>在第一次布局完成之前，WindowMetrics 可以让您轻松获取当前 window 状态信息，和系统当前状态下最大 Window 尺寸信息。例如像 Surface Duo 这样的设备，设备会有一个默认的配置决定应用从哪一个屏幕启动，但是也可以跨过设备的铰链扩展到两块屏幕上。在默认的状态，'getMaximumWindowMetrics' 方法返回应用当前所在屏幕的边界信息。当应用被移动到处于跨屏状态，'getMaximumWindowMetrics' 方法返回反映新状态的边界信息。这些信息最早在 onCreate 期间就会提供，您的 Activity 可以利用这些信息进行计算或者尽早做出决定，以便在第一时间选择正确的布局。</p> 
<p>API 返回的结果不包括系统 inset 信息，比如状态栏或导航栏，这是由于目前支持的所有 Android 版本中，在第一次布局完成之前，这些值对应的区域都不可用。关于使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroidx%2Fcore%2Fview%2FViewCompat" target="_blank">ViewCompat</a> 去获取系统可用 inset 信息，Chris Banes 的文章 - <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fp_9Px7BH6DQGNYNqzPCWtw" target="_blank">处理视觉冲突｜手势导航 (二)</a> 是非常好的资源。API 返回的边界信息也不会对布局填充时可能发生变化的布局参数作出响应。</p> 
<p>要访问这些 API，您需要像上文说明的那样先获取一个 WindowManager 对象:</p> 
<pre><code>val windowManager = WindowManager(context: Context)
</code></pre> 
<p>现在您就可以访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fkotlin%2Fandroidx%2Fwindow%2FWindowMetrics" target="_blank">WindowMetrics API</a>，并可轻松获取当前 window 的尺寸以及最大尺寸信息。</p> 
<pre><code>windowManager.currentWindowMetrics

windowManager.maximumWindowMetrics
</code></pre> 
<p>例如，如果您的应用在手机和平板电脑上的布局或导航模式截然不同，那么可以在视图填充之前依赖此信息对布局做出选择。如果您认为用户会对布局的明显变化感到疑惑，您可以忽略当前 window 尺寸信息的变化，选择部分信息作为常量。在选择填充哪些之前，您可以使用 window 最大尺寸信息。</p> 
<p>尽管 Android 11 平台已经包含了在 onCreate 期间获取 inset 信息的 API，但是我们还没有将这个 API 添加到 WindowManager 库中，这是因为我们想了解这些功能中哪些对开发者有用。您可以积极反馈，以便我们了解在您第一次布局之前，需要知道哪些能够使编写布局更为简便的值或抽象。</p> 
<p>我们希望这些可以用在 Android 低版本上的 API 能够帮助您构建响应 window 尺寸变化的应用，同时帮助您替换上文提到的已废弃 API。</p> 
<h2><strong>联系我们</strong></h2> 
<p>我们非常希望得到您对这些 API 的反馈，尤其是您认为缺少的那些，或者可让您开发变得更轻松的那些反馈。有一些使用场景我们可能没有考虑到，所以希望您在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2Fnew%3Fcomponent%3D840395%26template%3D1412556" target="_blank">public tracker</a> 上向我们提交 bug 或功能需求。</p>
                                        </div>
                                      
</div>
            