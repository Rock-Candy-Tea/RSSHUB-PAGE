
---
title: '5分钟学会Flutter开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b3520b2e9de4a47af69683f9852faf8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:00:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b3520b2e9de4a47af69683f9852faf8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导读</strong>：Flutter是Google开源的构建用户界面（UI）工具包，帮助开发者通过一套代码库高效构建多平台应用，支持移动、Web、桌面和嵌入式平台。Flutter使用Dart为开发语言，利用Skia绘图引擎，直接通过CPU、GPU进行绘制，不需要依赖任何原生的控件，相比React Native（依赖中间者JSCore引擎）性能更高。</p>
<p><em>全文3560字，预计阅读时间 14分钟。</em></p>
<p>目前Flutter混合栈技术成熟，基础建设完善，百度贴吧、网盘、地图、阅读、输入法等均已接入Flutter，一套代码双端运行，约节省50%人力。</p>
<h1 data-id="heading-0"><strong>一、环境配置：</strong></h1>
<h2 data-id="heading-1"><strong>1.1 下载Flutter SDK</strong></h2>
<pre><code class="copyable">git clone https://github.com/flutter/flutter.git
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2"><strong>1.2 配置环境变量</strong></h2>
<p>编辑~/.bash_profile，将环境变量添加至末尾。（如终端安装了zsh插件，则添加环境变量至 ~/.zshrc）</p>
<pre><code class="copyable"># FLUTTER_HOME为下载的Flutter文件夹路径
export FLUTTER_HOME=/Users/.../flutter
export PATH=$PATH:$FLUTTER_HOME/bin
export PATH=$PATH:$FLUTTER_HOME/bin/cache/dart-sdk/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3"></h5>
<h2 data-id="heading-4"><strong>1.3 刷新环境变量</strong></h2>
<pre><code class="copyable">source ~/.bash_profile
source ~/.zshrc（如安装zsh插件）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"><strong>1.4 开发工具</strong></h2>
<blockquote>
<p>1. Xcode + Android Studio（推荐）</p>
<p>2. Visual Studio Code</p>
</blockquote>
<p>以 Xcode + Android Studio为例，配置Android Studio插件：</p>
<p><strong>1.4.1 安装 Flutter，Dart插件</strong></p>
<p>Android Studio - Preferences - Plugins - Marketplace</p>
<p><strong>1.4.2 安装最新 Android SDK Command</strong></p>
<p>Android Studio - Preferences - SystemSettings - Android SDK - SDK Tools - 勾选Android SDK Command-line Tools</p>
<p><strong>1.4.3 运行 flutter doctor</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b3520b2e9de4a47af69683f9852faf8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>*报错：Unable to find bundled Java version on Flutter</p>
<pre><code class="copyable">cd /Applications/Android\ Studio.app/Contents/jre
ln -s ../jre jdk
ln -s "/Library/Internet Plug-Ins/JavaAppletPlugin.plugin" jdk
flutter doctor
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6"></h5>
<h1 data-id="heading-7"><strong>二、工程创建</strong></h1>
<h2 data-id="heading-8"><strong>2.1 创建Flutter项目</strong></h2>
<pre><code class="copyable">flutter create xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9"><strong>2.2 创建Flutter模块（用于原生集成Flutter）</strong></h2>
<pre><code class="copyable">create --template module xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10"><strong>2.3 工程结构</strong></h2>
<pre><code class="copyable">bd_flutter
  .dart_tool.............记录依赖库信息
  .idea..................当前项目配置
  android................Android工程目录
  iOS....................iOS工程目录
  lib....................Flutter代码目录
  test...................单元测试目录
  web....................Web工程目录
  pubspec.yaml...........Pub第三方依赖配置文件，类似Cocoapods、Gradle
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11"><strong>三、编程范式</strong></h1>
<p>在 Flutter 中界面布局使用 Dart 语言声明式编程范式，更易于开发与阅读。</p>
<h2 data-id="heading-12"><strong>3.1 命令式编程</strong></h2>
<p>命令“机器”如何去做事情(注重 how) 。</p>
<h2 data-id="heading-13"><strong>3.2 声明式编程</strong></h2>
<p>告诉“机器”你想要的是什么(注重 what) 。</p>
<p>2009年开始Vue、React、SwiftUI、Flutter以声明式编程为主，正逐步成为大前端的一种编程趋势。</p>
<h2 data-id="heading-14"><strong>3.3 我们举一个栗子，来帮我我们理解这两者的区别</strong></h2>
<p><strong>3.3.1 点击按钮修改文本（OC、Java版本）</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcb27dec738841a8bb2f161c2eb7a4de~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.3.2 点击按钮修改文本（Flutter、SwiftUI版本）</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e849e91e26e741fc81d7d22e7d928f5f~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在声明式编程中，首先代码是结构化的；其次，开发者无需关注Label/Text控件更新，引擎会自动根据num值的改变修改引用控件的值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c1eb8b753cf4984bfe047f61bbdfe1f~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-15"><strong>四、基础架构</strong></h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7199e005db9e48918fff1e0b5ace3430~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Flutter被设计为一个可扩展的分层系统。它可以被看作是各个独立的组件的系列合集，上层组件各自依赖下层组件。组件无法越权访问更底层的内容，并且框架层中的各个部分都是可选且可替代的。从下到上分为三层，依次为：Embedder、Engine、Framework。</p>
<h2 data-id="heading-16"><strong>4.1 Embedder</strong></h2>
<p>Embedder是操作系统适配层，实现了渲染 Surface 设置，线程设置等。</p>
<h2 data-id="heading-17"><strong>4.2 Engine</strong></h2>
<p>Engine层是 Flutter 的核心，它主要使用 C++ 编写，并提供了 Flutter 应用所需的原语。当需要绘制新一帧的内容时，引擎将负责对需要合成的场景进行栅格化。它提供了 Flutter 核心 API 的底层实现，包括图形（通过 Skia 链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fskia.org%2F%25EF%25BC%2589%25E3%2580%2581%25E6%2596%2587%25E6%259C%25AC%25E5%25B8%2583%25E5%25B1%2580%25E3%2580%2581%25E6%2596%2587%25E4%25BB%25B6%25E5%258F%258A%25E7%25BD%2591%25E7%25BB%259C" target="_blank" rel="nofollow noopener noreferrer" title="https://skia.org/%EF%BC%89%E3%80%81%E6%96%87%E6%9C%AC%E5%B8%83%E5%B1%80%E3%80%81%E6%96%87%E4%BB%B6%E5%8F%8A%E7%BD%91%E7%BB%9C" ref="nofollow noopener noreferrer">skia.org/）、文本布局、文件及网…</a> IO、辅助功能支持、插件架构和 Dart 运行环境及编译环境的工具链。</p>
<h2 data-id="heading-18"><strong>4.3 Framework</strong></h2>
<p>Framework 层是一个用 Dart 实现的 UI SDK，包含了动画、图形绘制和手势识别等功能。开发者可以通过 Flutter 框架层与 Flutter 交互，该框架提供了以 Dart 语言编写的现代响应式框架。它包括由一系列层组成的一组丰富的平台，布局和基础库。从下层到上层，依次有：</p>
<p>1、基础的Foundation 类及一些基层之上的构建块服务，如 animation、 painting 和 gestures，它们可以提供上层常用的抽象。</p>
<p>2、渲染层用于提供操作布局的抽象。有了渲染层，你可以构建一棵可渲染对象的树。在你动态更新这些对象时，渲染树也会自动根据你的变更来更新布局。</p>
<p>3、widget层是一种组合的抽象。每一个渲染层中的渲染对象，都在 widgets 层中有一个对应的类。此外，widgets 层让你可以自由组合你需要复用的各种类。响应式编程模型就在该层级中被引入。</p>
<p>4、Material 和 Cupertino 库提供了全面的 widgets 层的原语组合，这套组合分别实现了 Material 和 iOS 设计规范。</p>
<h1 data-id="heading-19"><strong>五、视图渲染</strong></h1>
<h2 data-id="heading-20"><strong>5.1 Widget</strong></h2>
<p>Flutter中没有Controller、Activity概念，只有一种控件Widget（相当于View），一切皆 Widget。</p>
<p>Widget 是 Flutter 功能的抽象描述，是视图的配置信息，同样也是数据的映射，是 Flutter 开发框架中最基本的概念。</p>
<p>两个比较重要的Widget：StatelessWidget和StatefulWidget。</p>
<h2 data-id="heading-21"><strong>5.2 渲染过程</strong></h2>
<p><strong>5.2.1</strong> Flutter引擎不会直接渲染widget树，因为widget是特别不稳定的，会频繁的调用build方法，widget又相互依赖，一旦调用build，后面的widget都会重新创建，直接去解析widget的话会非常消耗性能，布局需要重新计算。由此引出了Element，RenderObject的概念，Flutter引擎解析的是RenderObject树，并非widget。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c48c63b36b4f10b14f60819d9b0dbe~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>5.2.2</strong> Widget会转化成RenderObject，但并不是所有的widget都会转成RenderObject。</p>
<p><strong>非RenderObject转化：</strong></p>
<pre><code class="copyable">//Text -> StatelessWidget -> Widget

class Text extends StatelessWidget &#123;
&#125;
abstract class StatelessWidget extends Widget &#123;
StatelessElement createElement() => StatelessElement(this);
&#125;
abstract class Widget extends DiagnosticableTree &#123;
Element createElement(); // 创建element抽象方法
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>RenderObject转化：</strong></p>
<pre><code class="copyable">//Column -> Flex -> MultiChildRenderObjectWidget - > RenderObjectWidget -> Widget
class Column extends Flex &#123;
&#125;
class Flex extends MultiChildRenderObjectWidget &#123;
// ⽅法实现
RenderFlex createRenderObject(BuildContext context) &#123;
//返回RenderFlex
return RenderFlex -> RenderBox -> RenderObject
&#125; &#125;
abstract class MultiChildRenderObjectWidget extends RenderObjectWidget &#123;
&#125;
abstract class RenderObjectWidget extends Widget &#123;
RenderObjectElement createElement();
RenderObject createRenderObject(BuildContext context); // 抽象⽅法-创建RenderObject
void updateRenderObject(BuildContext context, covariant RenderObject renderObject) &#123;
&#125;
void didUnmountRenderObject(covariant RenderObject renderObject) &#123; &#125;
&#125;
abstract class Widget extends DiagnosticableTree &#123;
Element createElement(); // 抽象⽅法-创建element
&#125;
class RenderFlex extends RenderBox with ContainerRenderObjectMixin<RenderBox,
FlexParentData>,
 RenderBoxContainerDefaultsMixin<RenderBox,
FlexParentData>,
 DebugOverflowIndicatorMixin &#123;
&#125;
abstract class RenderBox extends RenderObject &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22"><strong>六、混合开发</strong></h1>
<h2 data-id="heading-23"><strong>6.1 Flutter调用原生方法</strong></h2>
<p>1.Platform channels</p>
<p>2.Pigeon</p>
<p>3.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/" ref="nofollow noopener noreferrer">pub.dev/</a> 中搜索第三方开源包</p>
<p>以Platform channels为例：Flutter调用原生获取UDID</p>
<pre><code class="copyable">/*
Flutter代码
*/
static const platform = const MethodChannel("leo.com/getudid");
void getUDID() async &#123;
final result = await platform.invokeMethod("nativeGetUDID"); // 要调⽤的⽅法
// final result = await platform.invokeMethod("nativeGetUDID",["flutter参数"]);
setState(() &#123;
_udid = result;
 &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">/*
iOS代码
*/
// 1.获取FlutterViewController
let controller: FlutterViewController = window.rootViewController as!
FlutterViewController;
// 2.创建FlutterMethodChannel，跟controller⼆进制消息通信
let channel = FlutterMethodChannel(name: "leo.com/getudid", binaryMessenger:
controller.binaryMessenger);
// 3.监听channel调⽤⽅法，当flutter调⽤nativeGetUDID的时候调⽤
channel.setMethodCallHandler &#123; (call: FlutterMethodCall, result: @escaping
FlutterResult) in
// 1.判断当前是否是nativeGetUDID
guard call.method == "nativeGetUDID" else &#123;
result(FlutterMethodNotImplemented); // 报⼀个没有⽅法的错误
return;
 &#125;
call.arguments; //传递过来的参数
// 2.获取UDID
let udid = "xxxx-xxxx-xxxx-xxxx"
result(udid) //回调值
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">/*
Android代码
*/
private val CHANNEL = "leo.com/getudid"
override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) &#123;
GeneratedPluginRegistrant.registerWith(flutterEngine);
// 1.创建MethodChannel对象
val methodChannel = MethodChannel(flutterEngine.dartExecutor.binaryMessenger,
CHANNEL)
// 2.添加调⽤⽅法的回调
methodChannel.setMethodCallHandler &#123;
// Note: this method is invoked on the main thread.
call, result ->
// 2.1.如果调⽤的⽅法是nativeGetUDID,那么正常执⾏
if (call.method == "nativeGetUDID") &#123;
// 2.1.1.调⽤另外⼀个⾃定义⽅法回去电量信息
val udid = "xxxx-xxxx-xxxx-xxxx";
result.success(udid)
 &#125; else &#123;
//⽅法找不到，回调notImplemented
result.notImplemented()
 &#125;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.2 原⽣集成Flutter创建Flutter模块</strong></p>
<pre><code class="copyable">create --template module native_add_flutter
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.2.1 iOS集成Flutter</strong></p>
<pre><code class="copyable">// CocoaPods集成
flutter_application_path = '../native_add_flutter'
load File.join(flutter_application_path, '.ios', 'Flutter', 'podhelper.rb’)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 初始化Flutter引擎 , 为引擎起名为leo
let flutterEngine:FlutterEngine = FlutterEngine(name: "leo");
// 启动flutter引擎，默认函数⼊⼝为main
flutterEngine.run();
let flutterVC = FlutterViewController(engine: engine, nibName: nil, bundle: nil);
flutterVC.modalPresentationStyle = .fullScreen;
self.present(flutterVC, animated: true, completion: nil);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.2.2 Android集成Flutter</strong></p>
<pre><code class="copyable">// 在gradle进⾏配置
// 创建Android项⽬、添加相关的依赖
// 1、修改Android项⽬settings.gradle
setBinding(new Binding([gradle: this])) // new
evaluate(new File( // new
settingsDir.parentFile, // new
'native_add_flutter/.android/include_flutter.groovy' // new
))
include ':native_add_flutter'
project(':native_add_flutter').projectDir = new File('../native_add_flutter')
// 2、配置Android项⽬的build.gradle
dependencies &#123;
 ...
implementation project(':flutter') //增加flutter依赖
&#125;
// 3、AndroidManifest.xml配置
<activity android:name="io.flutter.embedding.android.FlutterActivity"
android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDi
rection|fontScale|screenLayout|density|uiMode"
android:hardwareAccelerated="true"
android:windowSoftInputMode="adjustResize"
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import io.flutter.embedding.android.FlutterActivity;
public class MainActivity extends AppCompatActivity &#123;
@Override
protected void onCreate(Bundle savedInstanceState) &#123;
super.onCreate(savedInstanceState);
startActivity(
FlutterActivity.createDefaultIntent(this)
 );
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-24"><strong>七、案例讲解 - 计数器</strong></h1>
<blockquote>
<p><strong>flutter create flutterdemo</strong></p>
<p><strong>main.dart</strong></p>
</blockquote>
<pre><code class="copyable">// 导⼊类
import 'package:flutter/material.dart';
//⼊⼝函数，程序加载时调⽤
void main() &#123;
runApp(MyApp()); //调⽤runApp⽅法，并初始化MyApp
&#125;
class MyApp extends StatelessWidget &#123;
// This widget is the root of your application.
@override
Widget build(BuildContext context) &#123; //初始化会调⽤build⽅法
return MaterialApp( //Material为Google的⼀种UI⻛格，MaterialApp可为项⽬配置App标题、主题
等
title: 'Flutter Demo',
theme: ThemeData(
// This is the theme of your application.
//
// Try running your application with "flutter run". You'll see the
// application has a blue toolbar. Then, without quitting the app, try
// changing the primarySwatch below to Colors.green and then invoke
// "hot reload" (press "r" in the console where you ran "flutter run",
// or simply save your changes to "hot reload" in a Flutter IDE).
// Notice that the counter didn't reset back to zero; the application
// is not restarted.
primarySwatch: Colors.blue,
 ),
home: MyHomePage(title: 'Flutter Demo Home Page'), //设置主⻚为MyHomePage
 );
 &#125;
&#125;
//由于点击需要更改Text显示,所以此处继承StatefulWidget
class MyHomePage extends StatefulWidget &#123;
MyHomePage(&#123;Key? key, required this.title&#125;) : super(key: key);
// This widget is the home page of your application. It is stateful, meaning
// that it has a State object (defined below) that contains fields that affect
// how it looks.
// This class is the configuration for the state. It holds the values (in this
// case the title) provided by the parent (in this case the App widget) and
// used by the build method of the State. Fields in a Widget subclass are
// always marked "final".
final String title;
@override
_MyHomePageState createState() => _MyHomePageState();
&#125;
class _MyHomePageState extends State<MyHomePage> &#123;
int _counter = 0;
//下的按钮的点击事件
void _incrementCounter() &#123;
// setState会标记需要刷新UI
setState(() &#123;
// This call to setState tells the Flutter framework that something has
// changed in this State, which causes it to rerun the build method below
// so that the display can reflect the updated values. If we changed
// _counter without calling setState(), then the build method would not be
// called again, and so nothing would appear to happen.
_counter++; //点击按钮时候，counter+1, 并⾃动更新UI显示
 &#125;);
 &#125;
@override
Widget build(BuildContext context) &#123;
// This method is rerun every time setState is called, for instance as done
// by the _incrementCounter method above.
//
// The Flutter framework has been optimized to make rerunning build methods
// fast, so that you can just rebuild anything that needs updating rather
// than having to individually change instances of widgets.
return Scaffold(
appBar: AppBar( //配置导航
// Here we take the value from the MyHomePage object that was created by
// the App.build method, and use it to set our appbar title.
title: Text(widget.title),
 ),
body: Center( //配置布局显示在中⼼
// Center is a layout widget. It takes a single child and positions it
// in the middle of the parent.
child: Column( //⼀种竖向布局⽅式，相当于listview
// Column is also a layout widget. It takes a list of children and
// arranges them vertically. By default, it sizes itself to fit its
// children horizontally, and tries to be as tall as its parent.
//
// Invoke "debug painting" (press "p" in the console, choose the
// "Toggle Debug Paint" action from the Flutter Inspector in Android
// Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
// to see the wireframe for each widget.
//
// Column has various properties to control how it sizes itself and
// how it positions its children. Here we use mainAxisAlignment to
// center the children vertically; the main axis here is the vertical
// axis because Columns are vertical (the cross axis would be
// horizontal).
mainAxisAlignment: MainAxisAlignment.center,
children: <Widget>[ //返回多个widget数组，
Text(
'You have pushed the button this many times:',
 ),
Text( '$_counter',//显示_counter的值
style: Theme.of(context).textTheme.headline4,//显示样式，使⽤主题的headline4
显示
 ),
 ],
 ),
 ),
floatingActionButton: FloatingActionButton( //⼀个可点击的按钮，固定在右下⻆
onPressed: _incrementCounter, //点击事件
tooltip: 'Increment',
child: Icon(Icons.add), //按钮显示为内部⾃带的add图⽚
 ), // This trailing comma makes auto-formatting nicer for build methods.
  );
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25"><strong>八、附：近期重要更新</strong></h1>
<p><strong>1.2版本 2019/02/26</strong><br>
支持java1.8<br>
增加了JavaScript与Dart的通信通道<br>
增加了对Android App Bundles的支持<br>
通过减少调用构造函数和静态方法，提升AOT(预编译)10%-20%的性能</p>
<p><strong>1.5版本 <strong>2019/05/07</strong></strong><br>
添加了集成测试<br>
提高热重载性能<br>
决定删除动态更新计划<br>
添加对Linux和Windows的Flutter运行支持</p>
<p><strong>1.7版本 2019/07/09</strong><br>
优化Flutter tools支持<br>
支持32位和64位Android bundles<br>
开始支持web端和实验性支持桌面端</p>
<p><strong>1.9版本 2019/09/10</strong></p>
<p>完善Web平台支持<br>
桌面平台实验性支持<br>
新增24种语言环境支持<br>
支持macOS Catalina和iOS 13<br>
Android增加对构建AAR的支持</p>
<p><strong>1.12版本 2019/12/11</strong><br>
支持Android 10<br>
支持iOS13暗黑模式<br>
可以将Flutter模块集成到Android或iOS应用中<br>
将Web支持从开发版转变为beta版；将MacOS支持纳入开发版本<br>
推出新工具DartPad（DartPad 是一个可以让你在任何现代化的浏览器中体验 Dart 编程语言线上工具）</p>
<p><strong>1.17版本 2020/05/06</strong><br>
减少18.5%应用体积<br>
提升了20%-37%导航性能<br>
降低了40% iOS动画CPU/GPU使用率<br>
增加对谷歌字体的支持：fonts.google.com<br>
完成对Type Scale部分的重构，符合 2018 Material 设计规范<br>
提升了iOS 50%渲染速度（iPhone5s+、iOS10+支持Metal 渲染）；不完全支持扔使用OpenGL渲染</p>
<p><strong>1.20版本 2020/08/05</strong><br>
增强了UTF-8解码<br>
pubspec.yaml插件不再支持旧格式<br>
在Visual Studio Code中预览嵌入式Dart DevTools<br>
引入新的混编插件-Pigeon，可以在Dart方法中直接调用Java/Objective-C/Kotlin/Swift方法并传递非原始数据对象。</p>
<p><strong>1.22版本 2020/10/01</strong><br>
增加应用体积分析工具<br>
提供了国际化和本地化工具，并实现了热重载支持<br>
支持Android 11；支持新的屏幕类型 (如挖孔屏和瀑布屏)，以及同步Android 11动画效果<br>
支持iOS 14、Xcode 12新图标以及对新iOS 14 App Clips功能的预览支持；默认模板版本从8.0升级到9.0<br>
可正式使用的 Google Maps 和 WebView 插件,将 Android 和 iOS 系统的原生界面组件托管在 Flutter 应用中</p>
<p><strong>2.0版本 2021/03/03</strong><br>
Web支持从测试版转变为稳定版<br>
除了HTML渲染，增加了CanvasKit渲染，桌面端浏览器会默认调用CanvasKit版本，移动端的浏览器会调用HTML版本。<br>
混合开发多flutter实例（经测试iOS平台存在内存问题）<br>
桌面平台的支持（beta)<br>
Google Mobile Ads（Beta）<br>
Dart 2.12 增加了空安全</p>
<p><strong>2.2版本 2021/05/18</strong><br>
更好的iOS、Android、Web跨平台支持<br>
Dart 2.13 更新，引入Type aliases<br>
Flutter Web 提升稳定性<br>
优化iOS端渲染动画帧时间、实现了增量iOS安装，缩短更新安装时间。<br>
Android中引入延迟组件，允许Flutter应用在运行时下载包含提前编译的代码模块，减少初始安装大小。</p>
<p><strong>招聘信息</strong>：</p>
<p>短视频研发部，负责好看视频、全民小视频以及多款创新APP的孵化研发工作。是公司级战略产品，承担百度系产品矩阵短视频内容供给任务，重点支持百度搜索和信息流视频化，肩负百度内容生态视频化转型使命。仅用两年的时间就实现用户规模从零到亿级增长，日活数千万。拥有百亿级流量，亿级数据量，丰富新奇和全面的产品玩法，多类型的技术系统和领先的技术架构。</p>
<p>欢迎加入短视频研发部，社招，实习，校招都要哦</p>
<p>简历投递邮箱：<a href="https://link.juejin.cn/?target=mailto%3Ageektalk%40baidu.com" target="_blank" title="mailto:geektalk@baidu.com" ref="nofollow noopener noreferrer">geektalk@baidu.com</a> （投递备注【短视频】）</p>
<p><strong>推荐阅读</strong>：</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498828%26idx%3D1%26sn%3D70422ee59299dbe640bb9d192579fb43%26chksm%3Dc03ecc30f74945262a80f2f04873ea759d56b780a9bff6fcf9ff22880bb8929481fc85589681%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498828&idx=1&sn=70422ee59299dbe640bb9d192579fb43&chksm=c03ecc30f74945262a80f2f04873ea759d56b780a9bff6fcf9ff22880bb8929481fc85589681&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">百度信誉认证中台架构解析</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498745%26idx%3D1%26sn%3D88ab93caf2e8a3662b307206954bbcdb%26chksm%3Dc03ecb85f749429346766d992c69ffbe58037d33ae55642693efe497a5da722b5ae484b38d11%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498745&idx=1&sn=88ab93caf2e8a3662b307206954bbcdb&chksm=c03ecb85f749429346766d992c69ffbe58037d33ae55642693efe497a5da722b5ae484b38d11&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498782%26idx%3D1%26sn%3D20b01f2eccf6ccd827fba5a97f1f333c%26chksm%3Dc03ecc62f74945747ad8e8ef207f7a1a140bafe66c93119e5e11889d14f3edfe601b8f8afe0c%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498782&idx=1&sn=20b01f2eccf6ccd827fba5a97f1f333c&chksm=c03ecc62f74945747ad8e8ef207f7a1a140bafe66c93119e5e11889d14f3edfe601b8f8afe0c&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">图数据库在百度汉语中的应用</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498745%26idx%3D1%26sn%3D88ab93caf2e8a3662b307206954bbcdb%26chksm%3Dc03ecb85f749429346766d992c69ffbe58037d33ae55642693efe497a5da722b5ae484b38d11%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498745&idx=1&sn=88ab93caf2e8a3662b307206954bbcdb&chksm=c03ecb85f749429346766d992c69ffbe58037d33ae55642693efe497a5da722b5ae484b38d11&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜从lowcode看下一代前端应用框架</a></p>
<p>---------- END ----------</p>
<p>百度Geek说</p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            