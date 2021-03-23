
---
title: 'Flutter项目中怎么混编原生功能'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af9e94b324b046248d2df63753c7983a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Feb 2021 23:56:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af9e94b324b046248d2df63753c7983a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>依托于与 Skia 的深度定制及优化，Flutter 给我们提供了很多关于渲染的控制和支持，能够实现绝对的跨平台应用层渲染一致性。但对于一个应用而言，除了应用层视觉显示和对应的交互逻辑处理之外，有时还需要原生操作系统（Android、iOS）提供的底层能力支持。比如，我们前面提到的数据持久化，以及推送、摄像头硬件调用等。</p>
<p>由于 Flutter 只接管了应用渲染层，因此这些系统底层能力是无法在 Flutter 框架内提供支持的；而另一方面，Flutter 还是一个相对年轻的生态，因此原生开发中一些相对成熟的 Java、C++ 或 Objective-C 代码库，比如图片处理、音视频编解码等，可能在 Flutter 中还没有相关实现。</p>
<p>Flutter项目中添加原生功能主要可以从两个方面考虑</p>
<ul>
<li>1、Flutter和原生平台的通信</li>
<li>2、Flutter页面中嵌入原生页面</li>
</ul>
<h2 data-id="heading-0">1、Flutter和原生平台的通信</h2>
<p>了解决调用原生系统底层能力以及相关代码库复用问题，Flutter 为开发者提供了一个轻量级的解决方案，即逻辑层的<strong>方法通道（Method Channel）机制</strong>。基于方法通道，我们可以将原生代码所拥有的能力，以接口形式暴露给 Dart，从而实现 Dart 代码与原生代码的交互，就像调用了一个普通的 Dart API 一样。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af9e94b324b046248d2df63753c7983a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当在Flutter中调用原生方法时，调用信息通过平台通道传递到原生，原生收到调用信息后方可执行指定的操作，如需返回数据，则原生会将数据再通过平台通道传递给Flutter。值得注意的是消息传递是异步的，这确保了用户界面在消息传递时不会被挂起。</p>
<h3 data-id="heading-1">平台通信的3中方式</h3>
<p>Flutter 与 Native 端通信有如下3个方法：</p>
<ul>
<li>MethodChannel：Flutter 与 Native 端相互调用，调用后可以返回结果，可以 Native 端主动调用，也可以Flutter主动调用，属于双向通信。此方式为最常用的方式， Native 端调用需要在主线程中执行。</li>
<li>BasicMessageChannel：用于使用指定的编解码器对消息进行编码和解码，属于双向通信，可以 Native 端主动调用，也可以Flutter主动调用。</li>
<li>EventChannel：用于数据流（event streams）的通信， Native 端主动发送数据给</li>
</ul>
<h3 data-id="heading-2">Android、iOS 和 Dart 平台间的常见数据类型转换</h3>
<p>平台通道使用标准消息编/解码器对消息进行编解码，它可以高效的对消息进行二进制序列化与反序列化。由于Dart与原生平台之间数据类型有所差异，下面我们列出数据类型之间的映射关系。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec677c61c064441b4530efec16d3159~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当在发送和接收值时，这些值在消息中的序列化和反序列化会自动进行。</p>
<h3 data-id="heading-3">如何获取平台信息</h3>
<p>Flutter 中提供了一个全局变量<code>defaultTargetPlatform</code>来获取当前应用的平台信息，<code>defaultTargetPlatform</code>定义在<code>platform.dart</code>中，它的类型是<code>TargetPlatform</code>，这是一个枚举类，定义如下：</p>
<pre><code class="copyable">enum TargetPlatform &#123;
  android,
  fuchsia,
  iOS,
  linux,
  macOS,
  windows,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到目前Flutter只支持这三个平台。我们可以通过如下代码判断平台</p>
<pre><code class="copyable">if(defaultTargetPlatform == TargetPlatform.android)&#123;
        // 是安卓系统，do something
    &#125;else if(defaultTargetPlatform == TargetPlatform.iOS)&#123;
      // 是iOS系统，do something
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用示例</h3>
<p>加入我们Flutter要向原生传递一个字典<code>&#123;"flutter":"我是flutter"&#125;</code>，原生向Flutter传递一个数组<code>[1,2,3]</code></p>
<h4 data-id="heading-5">Flutter如何实现一次方法调用请求</h4>
<p>首先，我们需要确定一个唯一的字符串标识符，来构造一个命名通道；然后，在这个通道之上，Flutter 通过指定方法名<code>flutter_postData</code>来发起一次方法调用请求。</p>
<p>可以看到，这和我们平时调用一个 Dart 对象的方法完全一样。因为方法调用过程是异步的，所以我们需要使用非阻塞（或者注册回调）来等待原生代码给予响应。</p>
<pre><code class="copyable">// 声明 MethodChannel
const platform = MethodChannel('flutter_postData');

// 处理按钮点击
onPressed: () async&#123;
    List result;
    try&#123;
         result = await platform.invokeMethod('flutter_postData',&#123;"flutter":"我是flutter"&#125;);
    &#125;catch(e)&#123;
          result = [];
    &#125;
   print(result.toString());
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">iOS端的方法调用响应如何实现</h4>
<p>首先打开Xcode中Flutter应用程序的iOS部分:</p>
<p>在 iOS 平台，方法调用的处理和响应是在 Flutter 应用的入口，也就是在 Applegate 中的 rootViewController（即 FlutterViewController）里实现的，因此我们需要打开 Flutter 的 iOS 宿主 App，找到 AppDelegate.m 文件，并添加相关逻辑。</p>
<pre><code class="copyable">@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate &#123;
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool &#123;
    GeneratedPluginRegistrant.register(with: self)
    
    // 创建命名方法通道
    let methodChannel = FlutterMethodChannel.init(name: "flutter_postData", binaryMessenger: self.window.rootViewController as! FlutterBinaryMessenger)
    // 往方法通道注册方法调用处理回调
    methodChannel.setMethodCallHandler &#123; (call, result) in
        if("flutter_postData" == call.method)&#123;
            //打印flutter传来的值
            print(call.arguments ?? &#123;&#125;)
            //向flutter传递值
            DispatchQueue.main.async &#123;
                result(["1","2","3"]);
            &#125;
            
        &#125;
    &#125;
    
    
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮打印
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5681fdb7aaf415a8d6e79c3bfdf8070~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">android端的方法调用响应如何实现</h4>
<p>首先在Android Studio中打开您的Flutter应用的Android部分：</p>
<p>在 Android 平台，方法调用的处理和响应是在 Flutter 应用的入口，也就是在 MainActivity 中的 FlutterView 里实现的，因此我们需要打开 Flutter 的 Android 宿主 App，找到 MainActivity.java 文件，并在其中添加相关的逻辑。</p>
<p>接下来，在onCreate里创建MethodChannel并设置一个MethodCallHandler。确保使用和Flutter客户端中使用的通道名称相同的名称。</p>
<pre><code class="copyable">import android.os.Bundle;

import io.flutter.Log;
import io.flutter.app.FlutterActivity;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;
import io.flutter.plugin.common.MethodChannel.MethodCallHandler;
import io.flutter.plugin.common.MethodChannel.Result;

public class MainActivity extends FlutterActivity &#123;
    private static final String CHANNEL = "flutter_postData";
    @Override
    public void onCreate(Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        new MethodChannel(getFlutterView(), CHANNEL).setMethodCallHandler(
                new MethodCallHandler() &#123;
                    @Override
                    public void onMethodCall(MethodCall call, Result result) &#123;
                        // TODO
                        if(call.method.equals("flutter_postData"))&#123;
                            //打印flutter传来的值
                            Log.e(call.arguments);
                            //向flutter传递值
                            result.success(new String[]&#123;"1", "2","3"&#125;);
                        &#125;
                    &#125;
                &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">总结</h4>
<p>Flutter 发起方法调用请求开始，请求经由唯一标识符指定的方法通道到达原生代码宿主，而原生代码宿主则通过注册对应方法实现、响应并处理调用请求，最后将执行结果通过消息通道，回传至 Flutter。</p>
<blockquote>
<p>需要注意的是，方法通道是非线程安全的。这意味着原生代码与 Flutter 之间所有接口调用必须发生在主线程。Flutter 是单线程模型，因此自然可以确保方法调用请求是发生在主线程（Isolate）的；而原生代码在处理方法调用请求时，如果涉及到异步或非主线程切换，需要确保回调过程是在原生系统的 UI 线程（也就是 Android 和 iOS 的主线程）中执行的，否则应用可能会出现奇怪的 Bug，甚至是 Crash。</p>
</blockquote>
<h2 data-id="heading-9">2、Flutter视图中嵌套原生视图</h2>
<p>我们来分析一下构建一个复杂 App 都需要什么？我们先按照四象限分析法，把能力和渲染分解成四个维度，分析构建一个复杂 App 都需要什么。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c96646cad15544d9af2a75e2943127f1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>经过分析，我们终于发现，原来构建一个 App 需要覆盖那么多的知识点，通过 Flutter 和方法通道只能搞定应用层渲染、应用层能力和底层能力，对于那些涉及到底层渲染，比如浏览器、相机、地图，以及原生自定义视图的场景，自己在 Flutter 上重新开发一套显然不太现实。</p>
<p>在这种情况下，使用混合视图看起来是一个不错的选择。我们可以在 Flutter 的 Widget 树中提前预留一块空白区域，在 Flutter 的画板中（即 FlutterView 与 FlutterViewController）嵌入一个与空白区域完全匹配的原生视图，就可以实现想要的视觉效果了。</p>
<p>但是，采用这种方案极其不优雅，因为嵌入的原生视图并不在 Flutter 的渲染层级中，需要同时在 Flutter 侧与原生侧做大量的适配工作，才能实现正常的用户交互体验。</p>
<p>幸运的是，Flutter 提供了一个平台视图（Platform View）的概念。它提供了一种方法，允许开发者在 Flutter 里面嵌入原生系统（Android 和 iOS）的视图，并加入到 Flutter 的渲染树中，实现与 Flutter 一致的交互体验。</p>
<p>这样一来，通过平台视图，我们就可以将一个原生控件包装成 Flutter 控件，嵌入到 Flutter 页面中，就像使用一个普通的 Widget 一样</p>
<p><strong>使用方法</strong></p>
<ul>
<li>1、首先，由作为客户端的 Flutter，通过向原生视图的 Flutter 封装类（在 iOS 和 Android 平台分别是 UIKitView 和 AndroidView）传入视图标识符，用于发起原生视图的创建请求；</li>
<li>2、然后，原生代码侧将对应原生视图的创建交给平台视图工厂（PlatformViewFactory）实现；</li>
<li>3、最后，在原生代码侧将视图标识符与平台视图工厂进行关联注册，让 Flutter 发起的视图创建请求可以直接找到对应的视图创建工厂。</li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a48ff6059494000af0291e3f0aa74bc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">Flutter 如何实现原生视图的接口调用</h4>
<pre><code class="copyable">class MyFlutterView extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    // 使用 Android 平台的 AndroidView，传入唯一标识符 MyFlutterView
    if (defaultTargetPlatform == TargetPlatform.android) &#123;
      return AndroidView(viewType: 'MyFlutterView');
    &#125; else &#123;
      // 使用 iOS 平台的 UIKitView，传入唯一标识符 MyFlutterView
      return UiKitView(viewType: 'MyFlutterView');
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">嵌入原生View-iOS</h4>
<ul>
<li>1、创建FlutterPlatformView</li>
</ul>
<pre><code class="copyable">import Foundation
import Flutter

class MyFlutterView: NSObject,FlutterPlatformView &#123;
    
    let label = UILabel()
    
    init(_ frame: CGRect,viewID: Int64,args :Any?,messenger :FlutterBinaryMessenger) &#123;
        label.text = "我是 iOS View"
    &#125;
    
    func view() -> UIView &#123;
        return label
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、注册工厂类<code>MyFlutterViewFactory</code></li>
</ul>
<pre><code class="copyable">import Foundation
import Flutter
class MyFlutterViewFactory: NSObject,FlutterPlatformViewFactory &#123;
    
    var messenger:FlutterBinaryMessenger
    
    init(messenger:FlutterBinaryMessenger) &#123;
        self.messenger = messenger
        super.init()
    &#125;
    
    func create(withFrame frame: CGRect, viewIdentifier viewId: Int64, arguments args: Any?) -> FlutterPlatformView &#123;
        return MyFlutterView(frame,viewID: viewId,args: args,messenger: messenger)
    &#125;
    
    func createArgsCodec() -> FlutterMessageCodec & NSObjectProtocol &#123;
        return FlutterStandardMessageCodec.sharedInstance()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、在 AppDelegate 中注册</li>
</ul>
<pre><code class="copyable">let registrar:FlutterPluginRegistrar = self.registrar(forPlugin: "plugins.flutter.io/custom_platform_view_plugin")!
let factory = MyFlutterViewFactory(messenger: registrar.messenger())
registrar.register(factory, withId: "MyFlutterView")
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6711144ad784f8393fcc2dc6be3f62b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">嵌入原生View-Android</h4>
<ul>
<li>1、在App 项目的 java/包名 目录下创建嵌入 Flutter 中的 Android View，此 View 继承 PlatformView</li>
</ul>
<pre><code class="copyable">// 原生视图封装类
class MyFlutterView implements PlatformView &#123;
    private final TextView textView;// 缓存原生视图
    // 初始化方法，提前创建好视图
    public MyFlutterView(Context context, int id, BinaryMessenger messenger) &#123;
        textView = new TextView(context);
        textView.setText("我是 Android View");
    &#125;

    // 返回原生视图
    @Override
    public View getView() &#123;
        return textView;
    &#125;
    // 原生视图销毁回调
    @Override
    public void dispose() &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、注册工厂类<code>MyFlutterViewFactory</code></li>
</ul>
<pre><code class="copyable">// 视图工厂类
public class MyFlutterViewFactory extends PlatformViewFactory &#123;
    private final BinaryMessenger messenger;
    // 初始化方法
    public MyFlutterViewFactory(BinaryMessenger msger) &#123;
        super(StandardMessageCodec.INSTANCE);
        messenger = msger;
    &#125;
    // 创建原生视图封装类，完成关联
    @Override
    public PlatformView create(Context context, int id, Object obj) &#123;
        return new MyFlutterView(context, id, messenger);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、在 App 中 MainActivity 中注册</li>
</ul>
<pre><code class="copyable">Registrar registrar = registrarFor("plugins.flutter.io/custom_platform_view_plugin");// 生成注册类
MyFlutterViewFactory playerViewFactory = new MyFlutterViewFactory(registrar.messenger());// 生成视图工厂
registrar.platformViewRegistry().registerViewFactory("MyFlutterView", playerViewFactory);// 注册视图工厂
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">总结</h4>
<p>由于 Flutter 与原生渲染方式完全不同，因此转换不同的渲染数据会有较大的性能开销。如果在一个界面上同时实例化多个原生控件，就会对性能造成非常大的影响，所以我们要避免在使用 Flutter 控件也能实现的情况下去使用内嵌平台视图。</p>
<p>因为这样做，一方面需要分别在 Android 和 iOS 端写大量的适配桥接代码，违背了跨平台技术的本意，也增加了后续的维护成本；另一方面毕竟除去地图、WebView、相机等涉及底层方案的特殊情况外，大部分原生代码能够实现的 UI 效果，完全可以用 Flutter 实现</p>
<p>代码地址：<a href="https://github.com/SunshineBrother/FlutterDemo" target="_blank" rel="nofollow noopener noreferrer">github.com/SunshineBro…</a>
本文主要参考：<a href="https://www.kancloud.cn/alex_wsc/flutter_demo/1566549" target="_blank" rel="nofollow noopener noreferrer">www.kancloud.cn/alex_wsc/fl…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            