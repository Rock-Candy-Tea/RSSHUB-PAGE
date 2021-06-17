
---
title: 'React Native 点击事件采集方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12458638216244bda460b6aea4e41f80~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 22:35:38 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12458638216244bda460b6aea4e41f80~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>React Native 是由 Facebook 推出的移动应用开发框架，可以用来开发 iOS、Android、Web 等跨平台应用程序，官网为：
<a href="https://facebook.github.io/react-native/%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">facebook.github.io/react-nativ…</a>
React Native 和传统的 Hybrid 应用最大的区别就是它抛开了 WebView 控件。React Native 产出的并不是 “网页应用”、“HTML5 应用” 或者 “混合应用”，而是一个真正的移动应用，从使用感受上和用 Objective-C 或 Java 编写的应用相比几乎是没有区别的。React Native 所使用的基础 UI 组件和原生应用完全一致。我们要做的就是把这些基础组件使用 JavaScript 和 React 的方式组合起来。React Native 是一个非常优秀的跨平台框架。</p>
<p>React Native 可以通过自定义 Module [1] 的方式实现 JavaScript 调用 Native 接口，神策分析的 React Native Module [2]在 v2.0 版本使用新方案实现了 React Native 全埋点功能。本文主要介绍神策分析 React Native Module 是如何实现 $AppClick（全埋点的点击事件） 功能的，内容以 iOS 项目为例。</p>
<h1 data-id="heading-1">二、原理分析</h1>
<h2 data-id="heading-2">2.1触发点击</h2>
<p>在 React Native 中没有专门的按钮组件，为了让视图能够响应用户的点击事件，我们需要借助 Touchable 系列组件来包装我们的视图。</p>
<p>2.1.1 Touchable 系列组件</p>
<p>Touchable 系列组件中的四个组件都可以用来包装视图，从而响应用户的点击事件：</p>
<ul>
<li>TouchableHighlight：在用户手指按下时背景会有变暗的效果；</li>
<li>TouchableNativeFeedback：在 Android 上可以使用 TouchableNativeFeedback，它会在用户手指按下时形成类似水波纹的视觉效果。注意，此组件只支持 Android；</li>
<li>TouchableOpacity：会在用户手指按下时降低按钮的透明度，而不会改变背景的颜色；</li>
<li>TouchableWithoutFeedback：响应用户的点击事件，如果你想在处理点击事件的同时不显示任何视觉反馈，使用它是个不错的选择。</li>
</ul>
<p>以上组件中前三者都是在 TouchableWithoutFeedback 的基础上做了一些扩展，我们从源码中可以看出：</p>
<p><strong>TouchableHighlight</strong></p>
<pre><code class="copyable">type Props = $ReadOnly<&#123;|
  ...TouchableWithoutFeedbackProps,
  ...IOSProps,
  ...AndroidProps,
 
  activeOpacity?: ?number,
  underlayColor?: ?ColorValue,
  style?: ?ViewStyleProp,
  onShowUnderlay?: ?() => void,
  onHideUnderlay?: ?() => void,
  testOnly_pressed?: ?boolean,
|&#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>TouchableNativeFeedback</strong></p>
<pre><code class="copyable">propTypes: &#123;
  /* $FlowFixMe(>=0.89.0 site=react_native_android_fb) This comment
   * suppresses an error found when Flow v0.89 was deployed. To see the
   * error, delete this comment and run Flow. */
  ...TouchableWithoutFeedback.propTypes,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>TouchableOpacity</strong></p>
<pre><code class="copyable">type Props = $ReadOnly<&#123;|
  ...TouchableWithoutFeedbackProps,
  ...TVProps,
  activeOpacity?: ?number,
  style?: ?ViewStyleProp,
|&#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 TouchableWithoutFeedback 有其他组件的共同属性，所以我们只需要来了解下 TouchableWithoutFeedback 是如何实现点击功能的。</p>
<p>2.1.2 Touchable 功能介绍</p>
<p>React Native 的响应系统用起来可能比较复杂，因此官方提供了一个抽象的 Touchable 实现，用来做 “可触控” 的组件。Touchable 系列组件相关文件都在
node_modules/react-native/Libraries/Components/Touchable 文件夹中。在 Touchable 文件夹下也提供了 Touchable.js 文件，点击功能的实现都是在此文件中。
React Native 对 Touchable.js 的描述如下：</p>
<pre><code class="copyable">* ====================== Touchable Tutorial ===============================
* The `Touchable` mixin helps you handle the "press" interaction. It analyzes
* the geometry of elements, and observes when another responder (scroll view
* etc) has stolen the touch lock. It notifies your component when it should
* give feedback to the user. (bouncing/highlighting/unhighlighting).
*
* - When a touch was activated (typically you highlight)
* - When a touch was deactivated (typically you unhighlight)
* - When a touch was "pressed" - a touch ended while still within the geometry
*   of the element, and no other element (like scroller) has "stolen" touch
*   lock ("responder") (Typically you bounce the element).
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从描述中可以看出，Touchable 会帮助开发者处理触摸交互，当有其他响应者响应了触摸交互时，Touchable 也会及时通知控件向用户提供反馈。</p>
<p>2.1.3 Touchable 状态变化</p>
<p>React Native 控件的触摸操作是会发生变化的，为了监听控件触摸状态的变化，React Native 在 Touchable 中声明了 State 和 Signal 类型来描述用户的触摸行为。</p>
<p><strong>State</strong></p>
<pre><code class="copyable">type State =
| typeof States.NOT_RESPONDER // 非响应者
| typeof States.RESPONDER_INACTIVE_PRESS_IN // 无效的按压
| typeof States.RESPONDER_INACTIVE_PRESS_OUT // 无效的抬起
| typeof States.RESPONDER_ACTIVE_PRESS_IN // 有效的按压
| typeof States.RESPONDER_ACTIVE_PRESS_OUT // 有效的抬起
| typeof States.RESPONDER_ACTIVE_LONG_PRESS_IN // 有效的长按
| typeof States.RESPONDER_ACTIVE_LONG_PRESS_OUT // 有效的长按后抬起
| typeof States.ERROR; // 错误
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Signal</strong></p>
<pre><code class="copyable">/**
 * Inputs to the state machine.
 */
const Signals = keyMirror(&#123;
  DELAY: null,
  RESPONDER_GRANT: null,
  RESPONDER_RELEASE: null,
  RESPONDER_TERMINATED: null,
  ENTER_PRESS_RECT: null,
  LEAVE_PRESS_RECT: null,
  LONG_PRESS_DETECTED: null,
&#125;);
 
type Signal =
  | typeof Signals.DELAY // 延迟触发信号
  | typeof Signals.RESPONDER_GRANT // 开始触摸
  | typeof Signals.RESPONDER_RELEASE // 触摸结束
  | typeof Signals.RESPONDER_TERMINATED //触摸中断
  | typeof Signals.ENTER_PRESS_RECT // 进入按压范围内
  | typeof Signals.LEAVE_PRESS_RECT // 离开按压范围
  | typeof Signals.LONG_PRESS_DETECTED; // 检测是否为长按
<span class="copy-code-btn">复制代码</span></code></pre>
<p>交互流程如图 2-1 所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12458638216244bda460b6aea4e41f80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 2-1 交互流程图（参考：React Native 源码 [3]）</p>
<p>从图 2-1 中可以看出，当 State 为 RESPONDER_ACTIVE_PRESS_IN 并且 Signal 为 RESPONDER_RELEASE 时，表示用户正在点击控件。因此，我们可以在这里触发控件的点击事件采集。</p>
<p>_performSideEffectsForTransition 函数中已有此逻辑的判断，我们可以在这里添加打印信息来验证方案的可行性：</p>
<pre><code class="copyable">_performSideEffectsForTransition: function(
    curState: State,
    nextState: State,
    signal: Signal,
    e: PressEvent,
  ) &#123;
      // ...
      const shouldInvokePress =
        !IsLongPressingIn[curState] || pressIsLongButStillCallOnPress;
      if (shouldInvokePress && this.touchableHandlePress) &#123;
        if (!newIsHighlight && !curIsHighlight) &#123;
          // we never highlighted because of delay, but we should highlight now
          this._startHighlight(e);
          this._endHighlight(e);
        &#125;
        if (Platform.OS === 'android' && !this.props.touchSoundDisabled) &#123;
          this._playTouchSound();
        &#125;
        console.log("这里是按钮点击");
        this.touchableHandlePress(e);
      &#125;
    &#125;
 
    this.touchableDelayTimeout && clearTimeout(this.touchableDelayTimeout);
    this.touchableDelayTimeout = null;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目入口文件 App.js 中添加 Button 按钮并运行项目，点击 Button 按钮可以看到终端控制台打印内容 “这里是按钮点击”，如图 2-2 所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebfb1dc0f2cf40e5a977bfdf7df26a26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 2-2 控制台打印信息</p>
<p>至此，我们就找到了触发 $AppClick 事件的时机。</p>
<h2 data-id="heading-3">2.2 创建视图</h2>
<p>上一节中我们已经找到了触发 $AppClick 事件的时机。但是，还存在一个问题：在 React Native 中是无法直接获取到触发点击事件对应的 View 对象。针对这一问题，我们可以通过 reactTag 来解决。</p>
<p>2.2.1 reactTag</p>
<p>在 React Native 项目中会给每个 View 分配一个唯一的 id（reactTag）。reactTag 是一个递增的整型数字，我们可以通过 reactTag 来找到每一个 View 对象。
RCTRootView 作为整个 React Native 项目的入口，初始化时会默认将 1 分配给 RCTRootView 作为 reactTag，即 RootTag 。</p>
<p>我们下面来看下 reactTag 的生成规则：</p>
<pre><code class="copyable">// Counter for uniquely identifying views.
// % 10 === 1 means it is a rootTag.
// % 2 === 0 means it is a Fabric tag.
var nextReactTag = 3;
function allocateTag() &#123;
  var tag = nextReactTag;
  if (tag % 10 === 1) &#123;
    tag += 2;
  &#125;
  nextReactTag = tag + 2;
  return tag;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码片段中可以看出，tag 以 +2 的方式递增，当 tag % 10 === 1 时会再做一次累加。因此，tag % 10 === 1 只会出现一次，即 RootTag。</p>
<p>2.2.2 创建视图</p>
<p>在 React Native 中所有的 View 都是通过 RCTUIManager 类来进行创建并管理的。RCTUIManager 类提供了如下方法来创建 View 对象：</p>
<pre><code class="copyable">RCT_EXPORT_METHOD(createView:(nonnull NSNumber *)reactTag
                  viewName:(NSString *)viewName
                  rootTag:(nonnull NSNumber *)rootTag
                  props:(NSDictionary *)props)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们需要找到此方法是在哪里调用的，这样就可以知道在 JavaScript 端创建 View 的时机。经过在 react-native 源码中查找，定位到 /node_modules/react-native/Renderer/implementations/ReactNativeRenderer-dev.js 中有如下代码片段：</p>
<pre><code class="copyable">ReactNativePrivateInterface.UIManager.createView(
    tag, // reactTag
    viewConfig.uiViewClassName, // viewName
    rootContainerInstance, // rootTag
    updatePayload // props
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，这里就是 JavaScript 端创建 View 的代码位置。我们可以在这里添加 Hook 代码将 View 的 reactTag 保存起来。</p>
<p>2.2.3 方案简述</p>
<p>根据前面两节的内容可知，我们可以在 UIManager 创建视图时将可点击视图的 reactTag 保存起来，当控件触发点击时通过对比 reactTag 判断当前点击的视图是否为可点击，并通过 reactTag 找到对应的 View 对象触发 $AppClick 点击事件。</p>
<h1 data-id="heading-4">三、准备工作</h1>
<h2 data-id="heading-5">3.1创建项目</h2>
<p>在实现 React Native 点击事件采集方案之前，我们首先创建一个演示项目。详细的安装步骤可以参考官网 environment-setup [4]部分，现在使用下面的命令创建一个 React Native 项目。</p>
<pre><code class="copyable">react-native init AwesomeProject --version 0.61.5
cd AwesomeProject
react-native run-ios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：0.62.x 及以上版本针对控件点击功能源码有部分改动，我们已在神策分析 React Native Module 后续版本中进行了兼容。这里为了演示效果，我们仍以 v0.61.5 版本来进行后续功能的说明。
通过以上命令我们已经创建了一个 AwesomeProject 的 React Native 项目，并可以成功运行项目。项目如图 3-1 所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0d52f77d4ab46d98c69e72eb2e147a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3-1 React Native 项目截图</p>
<h2 data-id="heading-6">3.2 集成神策分析</h2>
<ol>
<li>在项目目录下执行 "cd ios" 命令后再执行 "vim Podfile" 命令编辑 Podfile 文件。将" pod 'SensorsAnalyticsSDK' " 添加在文件中后保存，并执行 "pod install" 命令集成神策分析 SDK。Podfile 文件内容如下：</li>
</ol>
<pre><code class="copyable">platform :ios, '9.0'
require_relative '../node_modules/@react-native-community/cli-platform-ios/native_modules'
 
target 'AwesomeProject' do
  # Pods for AwesomeProject
  # ......
  Pod 'SensorsAnalyticsSDK'
 
  target 'AwesomeProjectTests' do
    inherit! :search_paths
    # Pods for testing
  end
 
  use_native_modules!
end
 
target 'AwesomeProject-tvOS' do
  # Pods for AwesomeProject-tvOS
 
  target 'AwesomeProject-tvOSTests' do
    inherit! :search_paths
    # Pods for testing
  end
 
end
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>将AwesomeProject.xcworkspace  打开（在 “ios 文件夹” 下），并在 AppDelegate 中初始化神策分析 SDK：</li>
</ol>
<pre><code class="copyable">#import <SensorsAnalyticsSDK/SensorsAnalyticsSDK.h>
 
@implementation AppDelegate
 
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
&#123;
  ....
 
  SAConfigOptions *options = [[SAConfigOptions alloc] initWithServerURL:@"" launchOptions:launchOptions];
  options.autoTrackEventType = SensorsAnalyticsEventTypeAppStart | SensorsAnalyticsEventTypeAppEnd | SensorsAnalyticsEventTypeAppClick | SensorsAnalyticsEventTypeAppViewScreen;
  options.enableLog = YES;
  [SensorsAnalyticsSDK startWithConfigOptions:options];
 
  return YES;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成初始化 SDK 后运行项目，可以看到控制台会打印出 $AppStart 事件。</p>
<h2 data-id="heading-7">3.3 创建 Module</h2>
<p>集成神策分析 SDK 后我们还需要创建一个 React Native Module 用来将 Native 触发 $AppClick 的接口提供给 JavaScript 端调用。</p>
<ol>
<li>打开 Xcode 并选择 File → New → Project...，输入静态库名称 SensorsAnalyticsModule。如图 3-2 所示：</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e3fb4a401b34e84bebe73e175e01e02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3-2 创建 Module</p>
<ol start="2">
<li>在静态库项目文件夹下添加 SensorsAnalyticsModule.podspec 文件，文件内容如下：</li>
</ol>
<pre><code class="copyable">Pod::Spec.new do |s|
  s.name         = "SensorsAnalyticsModule"
  s.version      = "0.0.1"
  s.summary      = "The official React Native SDK of Sensors Analytics."
  s.homepage     = "http://www.sensorsdata.cn"
  s.license      = &#123; :type => "Apache License, Version 2.0" &#125;
  s.author       = &#123; "Yuanyang Peng" => "pengyuanyang@sensorsdata.cn" &#125;
  s.source       = &#123; :git => "https://github.com/sensorsdata/react-native-sensors-analytics", :tag => "v#&#123;s.version&#125;" &#125;
  s.platform     = :ios, "7.0"
  s.source_files = "SensorsAnalyticsModule/*.&#123;h,m&#125;"
  s.requires_arc = true
  s.dependency   "React"
 
end
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>将创建的 SensorsAnalyticsModule 工程文件夹移动到演示项目根目录下，并在演示项目 “ios 文件夹” 下的 Podfile 文件中，添加 SensorsAnalyticsModule 引用：</li>
</ol>
<pre><code class="copyable">platform :ios, '9.0'
require_relative '../node_modules/@react-native-community/cli-platform-ios/native_modules'
 
target 'AwesomeProject' do
  # Pods for AwesomeProject
  # ......
  pod 'SensorsAnalyticsSDK'
  pod 'SensorsAnalyticsModule', :path => '../SensorsAnalyticsModule/'
  target 'AwesomeProjectTests' do
    inherit! :search_paths
    # Pods for testing
  end
 
  use_native_modules!
end
 
target 'AwesomeProject-tvOS' do
  # Pods for AwesomeProject-tvOS
 
  target 'AwesomeProject-tvOSTests' do
    inherit! :search_paths
    # Pods for testing
  end
 
end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目后可以正常工作，至此准备工作已完成。</p>
<h1 data-id="heading-8">四、代码实现</h1>
<p>通过前面的介绍，我们已经知道了实现 $AppClick 事件功能的关键步骤，下面来详细说明下代码的实现。</p>
<h2 data-id="heading-9">4.1 Module</h2>
<ol>
<li>在 SensorsAnalyticsModule.h 中添加 RCTBridgeModule 引用及实现协议内容：</li>
</ol>
<pre><code class="copyable">#import <React/RCTBridgeModule.h>
 
@interface SensorsAnalyticsModule : NSObject <RCTBridgeModule>
 
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在 SensorsAnalyticsModule.m 中新增 reactTags 集合属性来保存可点击视图的 reactTag 信息：</li>
</ol>
<pre><code class="copyable">#import <SensorsAnalyticsSDK/SensorsAnalyticsSDK.h>
#import <React/RCTRootView.h>
#import <React/RCTUIManager.h>
 
@interface SensorsAnalyticsModule ()
 
@property (nonatomic, strong) NSMutableSet<NSNumber*> *reactTags;
 
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 SensorsAnalyticsModule.m 中添加 Module 声明，并添加 + sharedInstance 方法：</li>
</ol>
<pre><code class="copyable">@implementation SensorsAnalyticsModule
 
RCT_EXPORT_MODULE(SensorsAnalyticsModule)
 
+ (instancetype)sharedInstance &#123;
    static dispatch_once_t onceToken;
    static SensorsAnalyticsModule *module;
    dispatch_once(&onceToken, ^&#123;
        module = [[SensorsAnalyticsModule alloc] init];
    &#125;);
    return module;
&#125;
 
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>新增 saveReactTag:clickable: 方法用来保存可点击视图的 reactTag，并将此方法通过 RCT_EXPORT_METHOD 提供给 JavaScript 端调用：</li>
</ol>
<pre><code class="copyable">RCT_EXPORT_METHOD(saveReactTag:(NSInteger)reactTag clickable:(BOOL)clickable) &#123;
    if (!clickable) &#123;
        return;
    &#125;
    SensorsAnalyticsModule *module = [SensorsAnalyticsModule sharedInstance];
    [module.reactTags addObject:@(reactTag)];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>通过 reactTag 找到对应视图：</li>
</ol>
<pre><code class="copyable">- (UIView *)viewForTag:(NSNumber *)reactTag &#123;
    UIViewController *root = [[[UIApplication sharedApplication] keyWindow] rootViewController];
    RCTRootView *rootView = [root rootView];
    RCTUIManager *manager = rootView.bridge.uiManager;
    return [manager viewForReactTag:reactTag];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>新增 trackViewClick: 方法用来触发 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi><mi>p</mi><mi>p</mi><mi>C</mi><mi>l</mi><mi>i</mi><mi>c</mi><mi>k</mi><mtext>事件。在</mtext><mi>t</mi><mi>r</mi><mi>a</mi><mi>c</mi><mi>k</mi><mi>V</mi><mi>i</mi><mi>e</mi><mi>w</mi><mi>C</mi><mi>l</mi><mi>i</mi><mi>c</mi><mi>k</mi><mo>:</mo><mtext>方法中通过</mtext><mi>r</mi><mi>e</mi><mi>a</mi><mi>c</mi><mi>t</mi><mi>T</mi><mi>a</mi><mi>g</mi><mtext>找到对应的视图后触发</mtext></mrow><annotation encoding="application/x-tex">AppClick 事件。在 trackViewClick: 方法中通过 reactTag 找到对应的视图后触发 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">A</span><span class="mord mathnormal">p</span><span class="mord mathnormal">p</span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">在</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">a</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mord mathnormal" style="margin-right:0.22222em;">V</span><span class="mord mathnormal">i</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02691em;">w</span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">通</span><span class="mord cjk_fallback">过</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">a</span><span class="mord mathnormal">c</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord cjk_fallback">找</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">应</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">视</span><span class="mord cjk_fallback">图</span><span class="mord cjk_fallback">后</span><span class="mord cjk_fallback">触</span><span class="mord cjk_fallback">发</span></span></span></span></span>AppClick 事件：</li>
</ol>
<pre><code class="copyable">RCT_EXPORT_METHOD(trackViewClick:(NSInteger)reactTag) &#123;
    SensorsAnalyticsModule *module = [SensorsAnalyticsModule sharedInstance];
    BOOL clickable = [module.reactTags containsObject:@(reactTag)];
    if (!clickable) &#123;
        return;
    &#125;
    dispatch_async(dispatch_get_main_queue(), ^&#123;
        UIView *view = [module viewForTag:@(reactTag)];
        [[SensorsAnalyticsSDK sharedInstance] trackViewAppClick:view withProperties:nil];
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4.2 手动插入代码</h2>
<p>1.在 /node_modules/react-native/Renderer/implementations/ReactNativeRenderer-dev.js 的“ReactNativePrivateInterface.UIManager.createView” 代码前插入 Hook 代码如下：</p>
<pre><code class="copyable">(function(thatThis)&#123;
    try&#123;
        var clickable = false;
        if(props.onStartShouldSetResponder)&#123;
            clickable = true;
        &#125;
        var ReactNative = require('react-native');
        var dataModule = ReactNative.NativeModules.SensorsAnalyticsModule;
        dataModule && dataModule.saveReactTag && dataModule.saveReactTag(tag, clickable);                           
    &#125; catch (error) &#123;
      throw new Error('SensorsAnalyticsModule Hook Code 调用异常: ' + error);
    &#125;
&#125;)(this); /* SENSORSDATA HOOK */
  ReactNativePrivateInterface.UIManager.createView(
    tag, // reactTag
    viewConfig.uiViewClassName, // viewName
    rootContainerInstance, // rootTag
    updatePayload // props
);
 
// 在此方法前插入代码
ReactNativePrivateInterface.UIManager.createView(
  tag, // reactTag
  viewConfig.uiViewClassName, // viewName
  rootContainerInstance, // rootTag
  updatePayload // props
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在 node_modules/react-native/Libraries/Components/Touchable/Touchable.js 的 “this.touchableHandlePress(e);” 代码前插入 Hook 代码如下：</li>
</ol>
<pre><code class="copyable">(function(thatThis) &#123;
  try &#123;
    var ReactNative = require('react-native');
    var module = ReactNative.NativeModules.SensorsAnalyticsModule;
    thatThis.props.onPress && module && module.trackViewClick && module.trackViewClick(ReactNative.findNodeHandle(thatThis));
  &#125; catch (error) &#123;
    throw new Error('SensorsData RN Hook Code 调用异常: ' + error);
  &#125;
&#125;)(this); /* SENSORSDATA HOOK */
 
// 在此方法前插入代码
this.touchableHandlePress(e);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目并点击 Button ，项目的控制台中已打印出 Button 的 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi><mi>p</mi><mi>p</mi><mi>C</mi><mi>l</mi><mi>i</mi><mi>c</mi><mi>k</mi><mtext>事件信息。至此，完成了</mtext><mi>R</mi><mi>e</mi><mi>a</mi><mi>c</mi><mi>t</mi><mi>N</mi><mi>a</mi><mi>t</mi><mi>i</mi><mi>v</mi><mi>e</mi><mtext>全埋点的</mtext></mrow><annotation encoding="application/x-tex">AppClick 事件信息。至此，完成了 React Native 全埋点的 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">A</span><span class="mord mathnormal">p</span><span class="mord mathnormal">p</span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">信</span><span class="mord cjk_fallback">息</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">至</span><span class="mord cjk_fallback">此</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">完</span><span class="mord cjk_fallback">成</span><span class="mord cjk_fallback">了</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal">e</span><span class="mord mathnormal">a</span><span class="mord mathnormal">c</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">全</span><span class="mord cjk_fallback">埋</span><span class="mord cjk_fallback">点</span><span class="mord cjk_fallback">的</span></span></span></span></span>AppClick 事件采集功能。如图 4-1 所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70aa0ed2f224451ba34a8e2207985dc8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 4-1 触发的点击事件信息</p>
<h2 data-id="heading-11">4.3 自动插入代码</h2>
<p>在上一节中，我们是手动插入了 React Native JavaScript 端的 Hook 代码，这种方案并不利于后期代码的维护以及不同 React Native 版本的兼容。因此，在这里需要新增一个 Hook 文件用来实现源码的自动插入功能。</p>
<ol>
<li>新建 Hook.js 文件放在演示项目的根目录下，并添加系统变量和文件位置：</li>
</ol>
<pre><code class="copyable">// 系统变量
var path = require("path"),
    fs = require("fs"),
    dir = path.resolve(__dirname, "node_modules/");
// RN 点击事件 Touchable.js 源码文件
// 为了兼容不同的 React Native 版本，这里可以再添加路径
var RNClickFilePath = dir + '/react-native/Libraries/Components/Touchable/Touchable.js';
var RNClickableFiles = [
  dir + '/react-native/Libraries/Renderer/implementations/ReactNativeRenderer-dev.js',
  dir + '/react-native/Libraries/Renderer/implementations/ReactNativeRenderer
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>添加后续需要用到的工具类方法：</li>
</ol>
<pre><code class="copyable">// 工具函数- add try catch
addTryCatch = function (functionBody) &#123;
  functionBody = functionBody.replace(/this/g, 'thatThis');
  return "(function(thatThis)&#123;\n" +
      "    try&#123;\n        " + functionBody +
      "    \n    &#125; catch (error) &#123; throw new Error('SensorsData RN Hook Code 调用异常: ' + error);&#125;\n" +
      "&#125;)(this); /* SENSORSDATA HOOK */";
&#125;
// 工具函数 - 计算位置
function lastArgumentName(content, index) &#123;
  --index;
  var lastComma = content.lastIndexOf(',', index);
  var lastParentheses = content.lastIndexOf('(', index);
  var start = Math.max(lastComma, lastParentheses);
  return content.substring(start + 1, index + 1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>添加 Hook Touchable.js 文件的代码片段：</li>
</ol>
<pre><code class="copyable">var sensorsdataClickHookCode =
`(function(thatThis)&#123;
    try &#123;
        var ReactNative = require('react-native');
        var dataModule = ReactNative.NativeModules.SensorsAnalyticsModule;
        thatThis.props.onPress && dataModule && dataModule.trackViewClick && dataModule.trackViewClick(ReactNative.findNodeHandle(thatThis))
    &#125; catch (error) &#123;
        throw new Error('SensorsData RN Hook Code 调用异常: ' + error);
    &#125;&#125;)(this); /* SENSORSDATA HOOK */ `;
   
sensorsdataHookClickRN = function () &#123;
    // 读取文件内容
    var fileContent = fs.readFileSync(RNClickFilePath, 'utf8');
    // 已经 hook 过了，不需要再次 hook
    if (fileContent.indexOf('SENSORSDATA HOOK') > -1) &#123;
        return;
    &#125;
    // 获取 hook 的代码插入的位置
    var hookIndex = fileContent.indexOf("this.touchableHandlePress(");
    // 判断文件是否异常，不存在 touchableHandlePress 方法，导致无法 hook 点击事件
    if (hookIndex == -1) &#123;
        throw "Can't not find touchableHandlePress function";
    &#125;;
    // 插入 hook 代码
    var hookedContent = `$&#123;fileContent.substring(0, hookIndex)&#125;\n$&#123;sensorsdataClickHookCode&#125;\n$&#123;fileContent.substring(hookIndex)&#125;`;
    // 备份 Touchable.js 源文件
    fs.renameSync(RNClickFilePath, `$&#123;RNClickFilePath&#125;_sensorsdata_backup`);
    // 重写 Touchable.js 文件
    fs.writeFileSync(RNClickFilePath, hookedContent, 'utf8');
    console.log(`found and modify Touchable.js: $&#123;RNClickFilePath&#125;`);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>添加 Hook 获取 reactTag 信息的代码片段：</li>
</ol>
<pre><code class="copyable">// hook clickable
sensorsdataHookClickableRN = function (reset = false) &#123;
  RNClickableFiles.forEach(function (onefile) &#123;
      if (fs.existsSync(onefile)) &#123;
          if (reset) &#123;
              // 读取文件内容
              var fileContent = fs.readFileSync(onefile, "utf8");
              // 未被 hook 过代码，不需要处理
              if (fileContent.indexOf('SENSORSDATA HOOK') == -1) &#123;
                  return;
              &#125;
              // 检查备份文件是否存在
              var backFilePath = `$&#123;onefile&#125;_sensorsdata_backup`;
              if (!fs.existsSync(backFilePath)) &#123;
                  throw `File: $&#123;backFilePath&#125; not found, Please rm -rf node_modules and npm install again`;
              &#125;
              // 将备份文件重命名恢复 + 自动覆盖被 hook 过的同名文件
              fs.renameSync(backFilePath, onefile);
          &#125; else &#123;
              // 读取文件内容
              var content = fs.readFileSync(onefile, 'utf8');
              // 已经 hook 过了，不需要再次 hook
              if (content.indexOf('SENSORSDATA HOOK') > -1) &#123;
                  return;
              &#125;
              // 获取 hook 的代码插入的位置
              var newObjRe = /ReactNativePrivateInterface\.UIManager\.createView\([\s\S]&#123;1,60&#125;\.uiViewClassName,[\s\S]*?\)[,;]/
              var match = newObjRe.exec(content);
              if (!match) &#123;
                  var objRe = /UIManager\.createView\([\s\S]&#123;1,60&#125;\.uiViewClassName,[\s\S]*?\)[,;]/
                  match = objRe.exec(content);
              &#125;
              if (!match)
                  throw "can't inject clickable js";
              var lastParentheses = content.lastIndexOf(')', match.index);
              var lastCommaIndex = content.lastIndexOf(',', lastParentheses);
              if (lastCommaIndex == -1)
                  throw "can't inject clickable js,and lastCommaIndex is -1";
              var nextCommaIndex = content.indexOf(',', match.index);
              if (nextCommaIndex == -1)
                  throw "can't inject clickable js, and nextCommaIndex is -1";
              var propsName = lastArgumentName(content, lastCommaIndex).trim();
              var tagName = lastArgumentName(content, nextCommaIndex).trim();
              var functionBody = `var clickable = false;
              if($&#123;propsName&#125;.onStartShouldSetResponder)&#123;
                  clickable = true;
              &#125;
              var ReactNative = require('react-native');
              var dataModule = ReactNative.NativeModules.SensorsAnalyticsModule;
              dataModule && dataModule.saveReactTag && dataModule.saveReactTag($&#123;tagName&#125;, clickable);
              `;
              var call = addTryCatch(functionBody);
              var lastReturn = content.lastIndexOf('return', match.index);
              var splitIndex = match.index;
              if (lastReturn > lastParentheses) &#123;
                  splitIndex = lastReturn;
              &#125;
              var hookedContent = `$&#123;content.substring(0, splitIndex)&#125;\n$&#123;call&#125;\n$&#123;content.substring(splitIndex)&#125;`
 
              // 备份源文件
              fs.renameSync(onefile, `$&#123;onefile&#125;_sensorsdata_backup`);
              // 重写文件
              fs.writeFileSync(onefile, hookedContent, 'utf8');
              console.log(`found and modify clickable.js: $&#123;onefile&#125;`);
          &#125;
      &#125;
  &#125;);
 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>添加代码还原功能：</li>
</ol>
<pre><code class="copyable">// 恢复被 hook 过的代码
sensorsdataResetRN = function (resetFilePath) &#123;
  // 判断需要被恢复的文件是否存在
  if (!fs.existsSync(resetFilePath)) &#123;
      return;
  &#125;
  var fileContent = fs.readFileSync(resetFilePath, "utf8");
  // 未被 hook 过代码，不需要处理
  if (fileContent.indexOf('SENSORSDATA HOOK') == -1) &#123;
      return;
  &#125;
  // 检查备份文件是否存在
  var backFilePath = `$&#123;resetFilePath&#125;_sensorsdata_backup`;
  if (!fs.existsSync(backFilePath)) &#123;
      throw `File: $&#123;backFilePath&#125; not found, Please rm -rf node_modules and npm install again`;
  &#125;
  // 将备份文件重命名恢复 + 自动覆盖被 hook 过的同名 Touchable.js 文件
  fs.renameSync(backFilePath, resetFilePath);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>定义执行命令：</li>
</ol>
<pre><code class="copyable">// 全部 hook 文件恢复
resetAllSensorsdataHookRN = function () &#123;
  sensorsdataResetRN(RNClickFilePath);
  sensorsdataHookClickableRN(true);
&#125;;
// 全部 hook 文件
allSensorsdataHookRN = function () &#123;
  sensorsdataHookClickRN(RNClickFilePath);
  sensorsdataHookClickableRN();
&#125;;
 
// 命令行
switch (process.argv[2]) &#123;
  case '-run':
      allSensorsdataHookRN();
      break;
  case '-reset':
      resetAllSensorsdataHookRN();
      break;
  default:
      console.log('can not find this options: ' + process.argv[2]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>删除手动插入的代码片段，在演示项目的根目录执行 "node Hook.js -run"，Hook 成功后会打印出插入代码的文件路径。运行项目测试 Button 点击，可以在控制台正常打印信息。如图 4-2 所示：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ceba32306ad410c8f4a34edf7aabf7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 4-2 触发的点击事件</p>
<h1 data-id="heading-12">五、总结</h1>
<p>总的来说，神策分析 React Native Module 在 v2.0 版本使用的方案是 Hook React Native JavaScript 端的源码，实现 $AppClick 事件的采集功能。</p>
<p>使用这种方案实现有如下优点：</p>
<ul>
<li>点击控件采集到的信息更准确（主要是 $screen_name 的准确性，这部分内容会在后续的 React Native 页面浏览全埋点方案中重点讲解）；</li>
<li>和 Native SDK 解耦，不再需要 Native SDK 配合 React Native Module 版本更新。</li>
</ul>
<p>但是这种方案也存在如下缺点：</p>
<ul>
<li>对 React Native JavaScript 端源码进行改动，一定程度上会造成 React Native 代码的不稳定性。</li>
</ul>
<p>在这里我们为了保证数据的准确性仍然使用此方案，并且在 Hook 代码中做了一定的代码保护，尽最大的努力减少数据埋点带来的风险性。</p>
<p>参考文献：
[1]<a href="https://reactnative.dev/docs/native-modules-setup" target="_blank" rel="nofollow noopener noreferrer">reactnative.dev/docs/native…</a>
[2]<a href="https://manual.sensorsdata.cn/sa/latest/tech_sdk_client_three_react-7549534.html" target="_blank" rel="nofollow noopener noreferrer">manual.sensorsdata.cn/sa/latest/t…</a>
[3]<a href="https://github.com/facebook/react-native/blob/master/Libraries/Components/Touchable/Touchable.js" target="_blank" rel="nofollow noopener noreferrer">github.com/facebook/re…</a>
[4]<a href="https://reactnative.dev/docs/environment-setup" target="_blank" rel="nofollow noopener noreferrer">reactnative.dev/docs/enviro…</a></p>
<p>文章来源：神策技术社区</p></div>  
</div>
            