
---
title: 'iPad 适配指南 - 基础篇'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/779a5e2922b041bd836e80c779719011~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 23:37:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/779a5e2922b041bd836e80c779719011~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「iPad 适配指南」 这个系列会介绍在 iPad 上的一些特殊能力，如何更好地适配 iPad，以及适配 iPad 时的一些注意点。</p>
<p>本文作为基础篇，主要介绍 iPad 的转屏分屏、模态，和 SplitVC 能力。</p>
</blockquote>
<h1 data-id="heading-0">如何判断 iPad 设备</h1>
<blockquote>
<p>如何判断设备， iPad 的各种形态</p>
</blockquote>
<pre><code class="copyable">if UIDevice.current.userInterfaceIdiom == .pad &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在 M1 Mac 上运行的 iOS 应用取到的 <code>userInterfaceIdiom</code>属性为 <code>.pad</code></p>
<p>在 Mac Catalyst 上运行的应用取到的 <code>userInterfaceIdiom</code> 属性为 <code>.mac</code></p>
</blockquote>
<h1 data-id="heading-1">分屏适配篇</h1>
<p>iPad 和 iPhone 最大的不同是，我们往往在 iPhone 上会限定 App 的方向恒定为 Portrait，但在 iPad 上，我们不仅要处理旋转屏，还要处理各种分屏的情况。</p>
<blockquote>
<p>分屏</p>
</blockquote>
<p>iOS 上的分屏最早可以追溯到随 iOS 10 推出的 <code>SlideOver</code>、<code>Split View</code> 和<code>画中画</code>功能。从 iOS 12 开始，应用分屏的概念和操作比较接近于现在的 iPadOS。</p>
<p>在 iPadOS 中，分屏下的应用主要有 8 种状态：<code>横屏 1/3 屏</code>、<code>横屏 1/2 屏</code>、<code>横屏 2/3 屏</code>、<code>横屏全屏</code>、<code>竖屏 1/3 屏</code>、<code>竖屏 2/3 屏</code>、<code>竖屏全屏</code>，以及<code>悬浮窗</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/779a5e2922b041bd836e80c779719011~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>分屏可以通过多种操作唤起，最常见的是长按 Dock 中的图标，然后拖动到屏幕的一侧。</p>
<h2 data-id="heading-2">尺寸变化</h2>
<blockquote>
<p>UITraitCollection 是什么</p>
<p>View / VC 如何兼容大小的变化</p>
<p>viewWillTransition willTransition</p>
</blockquote>
<p>无论是旋转屏幕，还是分屏，我们都可以收敛到「尺寸变化」这个概念上一起处理。</p>
<p>在此之前，需要先介绍 <code>UITraitCollection</code> 的概念。</p>
<h3 data-id="heading-3">UITraitCollection 是什么</h3>
<p><code>traitCollection</code>是<code>UIView</code>，<code>UIViewController</code>，<code>UIWindow</code>，<code>UIWindowScene</code>和<code>UIScreen</code>等的属性。</p>
<ul>
<li><code>Transition</code> 是指 vc 将会变化，变化的新属性集合会在 <code>traitCollection</code> 这个属性集合中。</li>
<li><code>traitCollection</code>‌ 属性集合常用的属性有：纵横宽度的 sizeClass，是否是 darkMode 等属性</li>
</ul>
<p>除了<code>UIWindowScene</code>是直接实现的属性，其他列举到的都是通过 <code>UITraitEnvironment</code> 协议来实现的：</p>
<pre><code class="copyable">public protocol UITraitEnvironment : NSObjectProtocol &#123;

  @available(iOS 8.0, *)

  var traitCollection: UITraitCollection &#123; get &#125;

  /** To be overridden as needed to provide custom behavior when the environment's traits change. */

  @available(iOS 8.0, *)

  func traitCollectionDidChange( _ previousTraitCollection: UITraitCollection?)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>traitCollectionDidChange</code>一般会用在响应 iOS 界面环境的变化，对窗口大小变化的兼容会在接下来的一节中讲到。</p>
<h3 data-id="heading-4">View / VC 兼容大小的变化</h3>
<blockquote>
<p>约束布局不必考虑尺寸的变化</p>
</blockquote>
<ul>
<li>对于 View，可以在<code>layoutSubviews</code>中进行 frame 布局或响应尺寸的变化。当窗口大小发生变化的时候，VC 会调用 View 的该方法。</li>
<li>对于 VC，有两种策略：</li>
</ul>
<ol>
<li>在<code>viewWillLayoutSubviews</code>中进行布局</li>
<li>可以在以下两个方法中进行布局的调整：</li>
</ol>
<pre><code class="copyable">// UIViewController 实现了这个协议

public protocol UIContentContainer : NSObjectProtocol &#123;

  @available(iOS 8.0, *)

  func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator)

  @available(iOS 8.0, *)

  func willTransition(to newCollection: UITraitCollection, with coordinator: UIViewControllerTransitionCoordinator)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>调用时机的区别在于：</p>
<ul>
<li>VC 出现和大小变化时都会调用<code>viewWillLayoutSubviews</code>和<code>willTransition</code></li>
<li>VC 出现时，如果不主动改变 view 大小，不会调用<code>viewWillTransition</code>，仅当 view 的大小变化时才会调用</li>
</ul>
</li>
<li>
<p>2 中的两个函数的区别在于，窗口大小变化时：</p>
<ul>
<li>
<p><code>willTransition</code>会先被调用。可以通过重写该方法获得即将变成的新 traitCollection</p>
<ul>
<li>注意：此时取 view/vc/window 的 traitCollection 仍为旧值</li>
</ul>
</li>
<li>
<p><code>viewWillTransition</code>后被调用。可以通过重写该方法获得即将变成的新 size</p>
<ul>
<li>注意：此时取 view/vc/window 的 traitCollection 和 bounds.size 仍为旧值</li>
<li>最佳实践：如果需要在 viewWillTransition 中获取即将变成的新 traitCollection，可以考虑在 vc 持有一个 <code>lastTraitCollection</code>，并且在 <code>willTransition</code> 时更新其值。</li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<p>这三种方法不仅仅会在上述情形中被调用。</p>
<p>App 在 iPad 退出后台或锁屏时，因为要生成横屏和竖屏的截图以便在 App Switcher 中显示，都会被多次调用。</p>
<p>详见后文「锁屏/退到后台时在 iPad 上的特殊情况」</p>
</blockquote>
<h3 data-id="heading-5">UIScreen 的使用</h3>
<p>大家可能早已习惯直接使用 <code>UIScreen.main.bounds</code>。这在过去的<code>一台设备只有唯一屏幕、一个屏幕只有唯一应用</code>情况下是没有问题的。但事情正在发生改变：在 iPadOS 上，一个屏幕已经能显示多个应用了，在 Apple Silicon Mac 上，一个设备也能有多个显示内容不一样的屏幕，应用并不一定会在 <code>UIScreen.main</code> 上显示。</p>
<p>我们应该遵循的原则是：在每个 UIView 中，获取自身的 bounds 属性，或者利用元素间的相对关系 Auto Layout 进行布局。应该尽量避免获取设备本身的宽高来进行布局。</p>
<h2 data-id="heading-6">SizeClass 介绍</h2>
<blockquote>
<p>介绍 sizeClass 概念，以及各种 iOS 窗口尺寸对应的 CR 值</p>
</blockquote>
<h3 data-id="heading-7">概念</h3>
<p>日常我们所说的Size Class，是<code>UITraitCollection</code>中的两个属性：</p>
<pre><code class="copyable"> @available(iOS 8.0, *)

open class UITraitCollection : NSObject, NSCopying, NSSecureCoding &#123;

  /// 水平 size class，最常用

  open var horizontalSizeClass: UIUserInterfaceSizeClass &#123; get &#125;

  /// 竖直 size class，用的少

  open var verticalSizeClass: UIUserInterfaceSizeClass &#123; get &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Size Class</code> 将界面宽度分成了 <code>Compact</code> 和 <code>Regular</code> 两种类型。</p>
<pre><code class="copyable"> @available(iOS 8.0, *)

public enum UIUserInterfaceSizeClass : Int &#123;

  /// 未指定

  case unspecified = 0

  /// 紧致

  case compact = 1

  /// 正常（宽松）

  case regular = 2

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于每个 View / VC / Window / WindowScene / Screen，都有 size class 的概念。</p>
<blockquote>
<p><code>Size Class</code> 对我们最重要的意义是：</p>
</blockquote>
<blockquote>
<p>响应式布局最重要的即是<code>断点</code>。所谓断点，就是一个分界线，在这个分界线的两边，我们会采取不同的布局策略。而 <code>Size Class</code> 给我们提供了关于<code>断点</code>的指导。</p>
</blockquote>
<h3 data-id="heading-8">系统水平方向 Size Class 规则</h3>
<ul>
<li>目前在 iPhone 竖屏时，<code>horizontalSizeClass</code>都是<code>Compact</code>，其他情况比较复杂，参考官方文档，不展开赘述；</li>
<li>在 iPad 上，<code>全屏</code>和<code>横屏2/3分屏</code>都是<code>Regular</code>；</li>
<li><code>横屏1/2分屏</code>时，只有 12.9 寸的 iPad 是<code>Regular</code>；</li>
<li>除此之外的其他情况都是<code>Compact</code>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/100a7a588a8d4a9e91b0c87751f6d50b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>详见官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdesign%2Fhuman-interface-guidelines%2Fios%2Fvisual-design%2Fadaptivity-and-layout%2F%23multitasking-size-classes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/#multitasking-size-classes" ref="nofollow noopener noreferrer">Size Classes - HIG</a></p>
<h1 data-id="heading-9">布局控件篇</h1>
<h2 data-id="heading-10">模态控件</h2>
<blockquote>
<p>介绍 modalPresentationStyle 各种样式的效果 以及着重介绍一下 popover 的概念</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/102e4d95ee3d4b23aa6ed06c7f0cfc04~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ef91491a38541e49965a8f19d01aac9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 iPad 上，我们经常看到这样的页面。看起来两者差异很大，似乎需要做很多的适配，但其实代码很简单，我们只需要两行代码，就能同时完成在 iPhone 上和 iPad 上的适配：</p>
<pre><code class="copyable">vc.modalPresentationStyle = .formSheet

self.present(vc, animated: true)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里涉及到了 modalPresentationStyle 的概念。</p>
<p>我们知道，一个 VC 可以被 push，也可以被 present。</p>
<p>两者在用法上的区别是，present 的页面会阻挡用户的其他操作，使其专注在当前页面上。</p>
<h3 data-id="heading-11">Sheet</h3>
<p>在 iPad 上有两种种最常见的样式：<code>.formSheet</code>和<code>.pageSheet</code>，这三种都是 present 前可以设置给 VC 的样式。</p>
<p>在 iPhone 上，两种 Sheet 的样式没有什么分别：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20ae064abc794e7d9d0af7efcc330045~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 iPad 上 formSheet 和 pageSheet 的区别是：</p>
<ul>
<li><code>pageSheet</code> 的浮窗大小是系统根据系统字体大小确定的，不能修改大小</li>
<li><code>formSheet</code> 和接下来要提到的 <code>popover</code> 的大小，都可以通过 vc 的 <code>preferredContentSize</code> 来指定实际大小。</li>
</ul>













<table><thead><tr><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df3798c994db4d95bbf3d561783cad30~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fdf2dc3f0ac4195aba14ff2bf0762a8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th></tr></thead><tbody><tr><td>pageSheet适合信息密度较高、阅读写作</td><td>formSheet默认大小，适合信息密度较低或自定义大小的场景</td></tr></tbody></table>
<p>iOS 13 对 formSheet 的窄屏样式从 fullScreen 变成了现在的层叠卡片样式</p>
<p>对于 <code>formSheet</code> 和 <code>pageSheet</code>，在 iPad 上有手势下滑返回的自带功能。</p>
<p>如果希望<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fview_controllers%2Fdisabling_the_pull-down_gesture_for_a_sheet%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/view_controllers/disabling_the_pull-down_gesture_for_a_sheet/" ref="nofollow noopener noreferrer">介入手势下滑事件</a>，可在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fuiadaptivepresentationcontrollerdelegate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate" ref="nofollow noopener noreferrer">UIAdaptivePresentationControllerDelegate</a> 中进行处理。</p>
<h3 data-id="heading-12">Popover 气泡</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cb4f92a488548a6928fafc439f31df7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Popover 是 iPad 上非常常见的一种交互元素。</p>
<p>前面我们介绍到的 <code>modalPresentationStyle</code>，还有一种取值即为 <code>.popover</code></p>
<p>但与前面几种我们提到的 Style 不同的是，除了简单的指定 <code>modalPresentationStyle</code> 之外，我们还需要设置几个属性：</p>
<pre><code class="copyable">// 指定样式

pushvc.modalPresentationStyle = .popover

// 指定 Popover 指向的矩形

pushvc.popoverPresentationController?.sourceRect = btn.frame

// 指定 Popover 指向的 View，必须指定，否则会崩溃

pushvc.popoverPresentationController?.sourceView = self.view

// 指定 Popover 允许的箭头朝向

pushvc.popoverPresentationController?.permittedArrowDirections = .up

self.present(pushvc, animated: true)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">modalPresentationStyle</h3>
<p>我们以 iPad Pro 11-inch, iOS 14, SplitVC detailVC(yellow) present(purple 40% 透明度)VC 的 case 为例，简单介绍一下所有 modalPresentationStyle 的取值区别：</p>


















































<table><thead><tr><th>横屏全屏</th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f102387ff332412196c6fddd7058473b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/514f2484b6724590beed20b1827be70c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f948846e4cd4c61b3941b1b283e970e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf65f84b7537447cb24360bce96fa447~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2892c542a73741bbb30a8dcdfe7be2b6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6f8b06d36c346f2aa66d8a2b04cf883~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th></tr></thead><tbody><tr><td>竖屏全屏</td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4092708864204fccb0c11f3f102e1f21~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec8b744b503f490dbe06fc4bd9f7ceb9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b07acdc7188499e98538c6b03658a13~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7287aa5c4004c339775f9baed4fc453~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14b41866d40b4e9795c112397acf68c2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3604a3c01fa748a08f410f751d698ac1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td>窄屏&iPhone</td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd3d76c39aa9463c8dabfdb3a725fe98~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da9c01d7db341c48477e2cb223e9caf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c546635e357b42699f57bff544351b71~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2252d27d0cba4f63a3cfe9892dc43f8c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cbeae1f8cee49d88be5934b0f9a7a93~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4371e437afc44e70ae2f03b5a1c18188~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td>类型</td><td>fullScreen</td><td>pageSheet</td><td>formSheet</td><td>currentContext</td><td>overFullScreen</td><td>overCurrentContext</td></tr><tr><td>大小特点</td><td>覆盖全屏</td><td>更大尺寸的模态</td><td>可自定义大小的模态，默认大小如图</td><td>只覆盖当前区域</td><td>覆盖全屏</td><td>只覆盖当前区域</td></tr></tbody></table>
<p>当然，系统也提供了 custom 样式，以提供自定义动画和样式的能力。</p>
<blockquote>
<p><code>over*</code> 与 <code>*</code> 的区别是：</p>
</blockquote>
<blockquote>
<p><code>over*</code> 不会将覆盖的视图从视图层级撤下</p>
</blockquote>
<h3 data-id="heading-14">iOS 15 | Customize and resize sheets in UIKit</h3>
<blockquote>
<p>Video: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2021%2F10063%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/videos/play/wwdc2021/10063/" ref="nofollow noopener noreferrer">Customize and resize sheets in UIKit - WWDC 2021 - Videos - Apple Developer</a></p>
</blockquote>
<p>在 iOS 15 中，Sheets 又有了一些新能力：</p>
<p>我们可以更精细化地控制 Sheets 的垂直高度了，比如创建一个半屏 Sheet，或者让 Sheet 可以在半屏高度停靠(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fuisheetpresentationcontroller%2F3801903-detents" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/3801903-detents" ref="nofollow noopener noreferrer">Dedents</a>)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8222c4e1d7d046e2a45c2b17a28581db~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以移除 Sheets 下的阴影遮罩，让我们可以在展示 Sheet 的时候与下层 View 交互；</p>
<p>或者在 Compact 屏幕下展示非全屏 Sheet</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/427cdda4281e4b5386a7ece1cbfa6658~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2803c76a0c884de1bda18c6baa468668~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有的新特性都可以通过新 API：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fuisheetpresentationcontroller" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller" ref="nofollow noopener noreferrer">UISheetPresentationController</a> 来进行行为的控制。</p>
<p>当 VC 的 <code>modalPresentationStyle</code> 为 formSheet / pageSheet (by default) 时，我们可以这样取得 <code>UISheetPresentationController</code></p>
<pre><code class="copyable">// Get a sheet

if let sheet = viewController.sheetPresentationController &#123;

  // Customize the sheet

&#125;

present(viewController, animated: true)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">路由跳转</h2>
<h3 data-id="heading-16">UISplitViewController</h3>
<blockquote>
<p>介绍 UISplitViewController 是什么</p>
<p>master detail 概念</p>
<p>showMaster / showDetail 的概念</p>
<p>各种 displayMode 代表什么</p>
</blockquote>
<p>为了更好地利用 iPad 更大屏幕的尺寸，系统提供了 <code>UISplitViewController</code>，以在宽屏情况下并列显示多个视图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b51e7ac8459d4aed85caca4f7e65cced~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是 iOS 14 中 <code>UISplitViewController</code> 更新的新接口，允许三栏同时展示。我们可以在系统自带的 邮件app 看到实际的效果。</p>
<p>iOS 14 更新了新的初始化接口：<code>init(style:)</code>。通过这个接口我们可以在初始化时设置两栏或者三栏的布局：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d761257d0517428c86e250178d5ba7a9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">DisplayMode</h4>
<blockquote>
<p>规定术语：</p>
</blockquote>
<blockquote>
<p>Master / Primary：两栏时，展示在左侧的单栏</p>
</blockquote>
<blockquote>
<p>Detail / Secondary：两栏时，展示在右侧的详细页面</p>
</blockquote>
<p><code>UISplitViewController</code> 有多种显示模式，我们称之为 <code>DisplayMode</code>。这里简要介绍一下：</p>
































<table><thead><tr><th></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3696b5ffe8b4ffeb3e53050c8134c19~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d47bb4f221946dcae10ee0b73e9971c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e05f2d6dceb4c6e801c4b429ed2689c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe1e8013352646188948e9fab83c86ed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbd42fc9bff9485c89f765a2be88575b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th><th><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1481da4072f4dd69e2d2fcd721280a2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th></tr></thead><tbody><tr><td>automatic</td><td>secondaryOnlyprimaryHidden</td><td>oneBesideSecondaryallVisable</td><td>oneOverSecondaryprimaryOverlay</td><td>twoBesideSecondary <strong>iOS 14 available</strong></td><td>twoOverSecondary <strong>iOS 14 available</strong></td><td>twoDisplaceSecondary <strong>iOS 14 available</strong></td></tr><tr><td>自动模式，根据屏幕大小自动切换</td><td>只展示 detail 页</td><td>Master 和 detail 并列展示</td><td>Master 盖住了 detail</td><td>两栏与 detail 并列</td><td>两栏盖住了 detail</td><td>两栏将 detail 向右挤开，参考 邮件.app</td></tr></tbody></table>
<p>简单概括：Bseide 意为并列显示，over 意为上层会覆盖下层的一个部分，Displace 意为上层会挤开下层。</p>
<h4 data-id="heading-18">常用接口</h4>
<h5 data-id="heading-19">路由行为</h5>
<p>如果是使用 <code>init(style:)</code> 初始化的 iOS 14 列风格 的 SplitVC，一切会变得省心很多：</p>
<ul>
<li>
<p>用 <code>setViewController(_:for:)</code> 来设置 VC 应该展示在哪一列</p>
</li>
<li>
<p>用 <code>viewController(for:)</code> 来获取指定列的 VC</p>
</li>
<li>
<p>SplitVC 会自动把所有的 childVC 用 navigationController 包住。</p>
<ul>
<li>如果设置的时候没有提供 navigationController，SplitVC 会自动创建一个。</li>
<li>通过 SplitVC 的 children 属性可以找到 navigationController。</li>
</ul>
</li>
<li>
<p>用 <code>show(_:)</code> 或者 <code>hide(_:)</code> 来展示或隐藏指定列</p>
</li>
</ul>
<p>如果是传统风格的 SplitVC（只支持 master & detail 的显示，不支持更多栏）：</p>
<ul>
<li>如果需要，应该手动为 master 和 detail 手动设置 navigationController 以实现路由跳转。</li>
<li>直接设置 <code>viewControllers</code> 属性，默认第一个为 master，第二个为 detail，会忽略更多（如果有）</li>
<li>使用 <code>show(_:sender:)</code> 来在 master 中找到 navigationController 进行 push vc</li>
<li>使用 <code>showDetailViewController(_:sender:)</code> 来 在 detail 中找到 navigationController 进行 push vc</li>
</ul>
<h5 data-id="heading-20">尺寸变化</h5>
<p>在 iPad 上，用户可能进行的分屏操作会突然改变程序的视图大小。当视图较窄时，SplitVC 的分栏布局可能不再适合，我们可能需要将所有栏中的 viewControllers 进行合并。当视图变宽时，我们又需要将 viewControllers 分配到不同的列当中。在这里我们称之为 Collapse & Expand。</p>
<p>我们可以在 SplitVC 的 delegate 中控制上述行为：</p>
<pre><code class="copyable">public protocol UISplitViewControllerDelegate &#123;

  // Return the view controller which is to become the primary view controller after `splitViewController` is collapsed due to a transition to

  // the horizontally-compact size class. If you return `nil`, then the argument will perform its default behavior (i.e. to use its current primary view

  // controller).

  @available(iOS 8.0, *)

  optional func primaryViewController(forCollapsing splitViewController: UISplitViewController) -> UIViewController?



   

  // Return the view controller which is to become the primary view controller after the `splitViewController` is expanded due to a transition

  // to the horizontally-regular size class. If you return `nil`, then the argument will perform its default behavior (i.e. to use its current

  // primary view controller.)

  @available(iOS 8.0, *)

  optional func primaryViewController(forExpanding splitViewController: UISplitViewController) -> UIViewController?



   

  // This method is called when a split view controller is collapsing its children for a transition to a compact-width size class. Override this

  // method to perform custom adjustments to the view controller hierarchy of the target controller. When you return from this method, you're

  // expected to have modified the `primaryViewController` so as to be suitable for display in a compact-width split view controller, potentially

  // using `secondaryViewController` to do so. Return YES to prevent UIKit from applying its default behavior; return NO to request that UIKit

  // perform its default collapsing behavior.

  @available(iOS 8.0, *)

  optional func splitViewController( _ splitViewController: UISplitViewController, collapseSecondary secondaryViewController: UIViewController, onto primaryViewController: UIViewController) -> Bool



   

  // This method is called when a split view controller is separating its child into two children for a transition from a compact-width size

  // class to a regular-width size class. Override this method to perform custom separation behavior. The controller returned from this method

  // will be set as the secondary view controller of the split view controller. When you return from this method, `primaryViewController` should

  // have been configured for display in a regular-width split view controller. If you return `nil`, then `UISplitViewController` will perform

  // its default behavior.

  @available(iOS 8.0, *)

  optional func splitViewController( _ splitViewController: UISplitViewController, separateSecondaryFrom primaryViewController: UIViewController) -> UIViewController?

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">锁屏/退到后台时在 iPad 上的特殊情况</h4>
<p>在 iOS 上，因为需要在 App Switcher 中显示各应用在横屏、竖屏、分屏情况下的界面预览，所以系统会提前在应用锁屏或退到后台时，对应用进行模拟界面变化并截图。</p>
<p>系统函数名为beginSnapshotSession。</p>
<p>在 iPad 上的整个模拟界面变化的过程中，一般会模拟横屏、竖屏、分屏等几种大小。处于最上层的 VC 可能会收到多次 willTransition / viewWillTransition / viewWillLayout 的调用。</p>
<p>在存在 SplitVC 的情况中，甚至因为模拟分屏，导致 mergeMasterAndDetail 时隐藏了 VC，调用到 VC 的 viewDidDisappear，也是有可能的。</p>
<h1 data-id="heading-22">加入我们</h1>
<p>飞书 - 字节跳动旗下企业协作平台，集视频会议、在线文档、移动办公、协同软件的一站式企业沟通协作平台。目前飞书业务正在飞速发展中，在北京、深圳等城市都有研发中心，前端、移动端、Rust、服务端、测试、产品等职位都有足够的HC，期待你的加入，和我们一起做有挑战的事情（请戳链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffuture.feishu.cn%2Frecruit%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://future.feishu.cn/recruit%EF%BC%89" ref="nofollow noopener noreferrer">future.feishu.cn/recruit）</a></p>
<p>我们也欢迎和飞书的同学一起进行技术问题的交流，有兴趣的同学请点击 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapplink.feishu.cn%2Fclient%2Fchat%2Fchatter%2Fadd_by_link%3Flink_token%3D850v2629-a47c-4f2c-ae70-04de11f260e2" target="_blank" rel="nofollow noopener noreferrer" title="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=850v2629-a47c-4f2c-ae70-04de11f260e2" ref="nofollow noopener noreferrer">飞书技术交流群</a> 入群交流</p></div>  
</div>
            