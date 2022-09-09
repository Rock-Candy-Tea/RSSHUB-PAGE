
---
title: 'Flutter混合开发-集成到iOS项目中'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=6850'
author: 掘金
comments: false
date: Tue, 16 Aug 2022 02:18:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=6850'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1，创建一个flutter模块儿</h2>
<p>创建Flutter Module</p>
<p><code>flutter create --template module my_flutter</code></p>
<p>创建完成后，该模块和普通的Flutter项目可以通过Android Studio或VSCode打开、运行；</p>
<h2 data-id="heading-1">2，创建一个iOS项目</h2>
<p>创建一个工程名称为 mix_flutter 的iOS项目，使用 CocoaPods 依赖管理和已安装的 Flutter SDK</p>
<h3 data-id="heading-2">1) 将项目加入CocoaPods进行管理</h3>
<p>CD到项目根目录，然后依次执行</p>
<p>初始化CocoaPods：<code>pod init</code></p>
<p>安装CocoaPods的依赖：<code>pod install</code></p>
<p>编译Podfile文件：</p>
<pre><code class="hljs language-js copyable" lang="js"># <span class="hljs-title class_">Uncomment</span> the next line to define a <span class="hljs-variable language_">global</span> platform <span class="hljs-keyword">for</span> your project

# platform :ios, <span class="hljs-string">'9.0'</span>


# 添加模块儿所在路径

flutter_application_path = <span class="hljs-string">'../my_flutter'</span>

load <span class="hljs-title class_">File</span>.<span class="hljs-title function_">join</span>(flutter_application_path, <span class="hljs-string">'.ios'</span>, <span class="hljs-string">'Flutter'</span>, <span class="hljs-string">'podhelper.rb'</span>)


target <span class="hljs-string">'mix_flutter'</span> <span class="hljs-keyword">do</span>

  # <span class="hljs-title class_">Comment</span> the next line <span class="hljs-keyword">if</span> you don<span class="hljs-string">'t want to use dynamic frameworks

  use_frameworks!

  

  #安装 Flutter 模块儿

  install_all_flutter_pods(flutter_application_path)


  # Pods for mix_flutter


  target '</span>mix_flutterTests<span class="hljs-string">' do

    inherit! :search_paths

    # Pods for testing

  end


  target '</span>mix_flutterUITests<span class="hljs-string">' do

    # Pods for testing

  end


end
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2) 在iOS项目编写代码展示Flutter页面</h3>
<p>为了在既有的iOS应用中展示Flutter页面，需要启动 <code>Flutter Engine</code>和 <code>FlutterViewController</code>。</p>
<p>Appdelegate.h 代码</p>
<pre><code class="hljs language-js copyable" lang="js">#<span class="hljs-keyword">import</span> <<span class="hljs-title class_">UIKit</span>/<span class="hljs-title class_">UIKit</span>.<span class="hljs-property">h</span>>

@<span class="hljs-keyword">import</span> <span class="hljs-title class_">Flutter</span>;

@interface <span class="hljs-title class_">AppDelegate</span> : <span class="hljs-title class_">FlutterAppDelegate</span>

@property (nonatomic,strong) <span class="hljs-title class_">FlutterEngine</span> *flutterEngine;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Appdelegate.m 代码</p>
<pre><code class="hljs language-js copyable" lang="js">
- (<span class="hljs-variable constant_">BOOL</span>)<span class="hljs-attr">application</span>:(<span class="hljs-title class_">UIApplication</span> *)application <span class="hljs-attr">didFinishLaunchingWithOptions</span>:(<span class="hljs-title class_">NSDictionary</span> *)launchOptions &#123;

    

    <span class="hljs-comment">// 1.创建一个FlutterEngine对象</span>

    self.<span class="hljs-property">flutterEngine</span> = [[<span class="hljs-title class_">FlutterEngine</span> alloc] <span class="hljs-attr">initWithName</span>:@<span class="hljs-string">"my flutter engine"</span>];

    <span class="hljs-comment">// 2.启动flutterEngine</span>

    [self.<span class="hljs-property">flutterEngine</span>  run];

    [<span class="hljs-title class_">GeneratedPluginRegistrant</span> <span class="hljs-attr">registerWithRegistry</span>:self.<span class="hljs-property">flutterEngine</span>];
    

    self.<span class="hljs-property">window</span> = [[<span class="hljs-title class_">UIWindow</span> alloc] <span class="hljs-attr">initWithFrame</span>:[[<span class="hljs-title class_">UIScreen</span> mainScreen] bounds]];

    self.<span class="hljs-property">window</span>.<span class="hljs-property">backgroundColor</span> = <span class="hljs-title class_">UIColor</span>.<span class="hljs-property">whiteColor</span>;

    <span class="hljs-title class_">ViewController</span> *vc = [[<span class="hljs-title class_">ViewController</span> alloc] init];

    self.<span class="hljs-property">window</span>.<span class="hljs-property">rootViewController</span> = vc;

    [self.<span class="hljs-property">window</span> makeKeyAndVisible];

    <span class="hljs-keyword">return</span> [<span class="hljs-variable language_">super</span> <span class="hljs-attr">application</span>:application <span class="hljs-attr">didFinishLaunchingWithOptions</span>:launchOptions];

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ViewController.m 代码</p>
<pre><code class="hljs language-js copyable" lang="js">- (<span class="hljs-keyword">void</span>)viewDidLoad &#123;

    [<span class="hljs-variable language_">super</span> viewDidLoad];

    <span class="hljs-title class_">UIButton</span> *button = [<span class="hljs-title class_">UIButton</span> <span class="hljs-attr">buttonWithType</span>:<span class="hljs-title class_">UIButtonTypeCustom</span>];

    [button <span class="hljs-attr">addTarget</span>:self

              <span class="hljs-attr">action</span>:@<span class="hljs-title function_">selector</span>(showFlutter)

    <span class="hljs-attr">forControlEvents</span>:<span class="hljs-title class_">UIControlEventTouchUpInside</span>];

    [button <span class="hljs-attr">setTitle</span>:@<span class="hljs-string">"Hello Flutter!"</span> <span class="hljs-attr">forState</span>:<span class="hljs-title class_">UIControlStateNormal</span>];

    button.<span class="hljs-property">backgroundColor</span> = <span class="hljs-title class_">UIColor</span>.<span class="hljs-property">blueColor</span>;

    button.<span class="hljs-property">frame</span> = <span class="hljs-title class_">CGRectMake</span>(<span class="hljs-number">80.0</span>, <span class="hljs-number">210.0</span>, <span class="hljs-number">160.0</span>, <span class="hljs-number">40.0</span>);

    [self.<span class="hljs-property">view</span> <span class="hljs-attr">addSubview</span>:button];
&#125;

- (<span class="hljs-keyword">void</span>)showFlutter &#123;

    <span class="hljs-title class_">FlutterEngine</span> *flutterEngine =

        ((<span class="hljs-title class_">AppDelegate</span> *)<span class="hljs-title class_">UIApplication</span>.<span class="hljs-property">sharedApplication</span>.<span class="hljs-property">delegate</span>).<span class="hljs-property">flutterEngine</span>;

    <span class="hljs-title class_">FlutterViewController</span> *flutterViewController =

    [[<span class="hljs-title class_">FlutterViewController</span> alloc] <span class="hljs-attr">initWithEngine</span>:flutterEngine <span class="hljs-attr">nibName</span>:nil <span class="hljs-attr">bundle</span>:nil];

    [self <span class="hljs-attr">presentViewController</span>:flutterViewController <span class="hljs-attr">animated</span>:<span class="hljs-variable constant_">YES</span> <span class="hljs-attr">completion</span>:nil];

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 Xocde 运行项目即可</p>
<h2 data-id="heading-4">3，让 Flutter 模块儿通过Android Studio在iOS模拟器，hot reload, hot restart</h2>
<p>由于在 XCode 调试项目每次修改都需要运行项目，所以最好能通过 Android Studio 来调试Flutter模块儿</p>
<h3 data-id="heading-5">1） 注意：首先使用Xcode运行 mix_flutter 项目，并保持</h3>
<h3 data-id="heading-6">2） 在 Android Studio 打开Flutter 模块儿，然后打开终端,执行命令<code>flutter attach</code></h3>
<p>由于我同时连接了我的手机，和打开了模拟器，所以有多个选项，所以我们需要选一个设备，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">mqingiMac</span>:my_flutter tiansifang$ flutter attach
<span class="hljs-title class_">Multiple</span> devices <span class="hljs-attr">found</span>:
iPhoneMQ (mobile)  • <span class="hljs-number">00008030</span>-001C04D21E89802E            • ios • iOS <span class="hljs-number">13.4</span> <span class="hljs-number">17E255</span>
iPhone <span class="hljs-number">13</span> (mobile) • <span class="hljs-title class_">DE390EED</span>-<span class="hljs-variable constant_">B28A</span>-4D7E-8C2A-<span class="hljs-title class_">EA9EF</span>2637000 • ios • com.<span class="hljs-property">apple</span>.<span class="hljs-property">CoreSimulator</span>.<span class="hljs-property">SimRuntime</span>.<span class="hljs-property">iOS</span>-<span class="hljs-number">15</span>-<span class="hljs-number">0</span> (simulator)
[<span class="hljs-number">1</span>]: iPhoneMQ (<span class="hljs-number">00008030</span>-001C04D21E89802E)
[<span class="hljs-number">2</span>]: iPhone <span class="hljs-number">13</span> (<span class="hljs-title class_">DE390EED</span>-<span class="hljs-variable constant_">B28A</span>-4D7E-8C2A-<span class="hljs-title class_">EA9EF</span>2637000)
<span class="hljs-title class_">Please</span> choose one (<span class="hljs-title class_">To</span> quit, press <span class="hljs-string">"q/Q"</span>): 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入 2 来选中模拟器,出现如下错误</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title class_">Please</span> choose one (<span class="hljs-title class_">To</span> quit, press <span class="hljs-string">"q/Q"</span>): <span class="hljs-number">2</span>
<span class="hljs-title class_">There</span> are multiple observatory ports available.
<span class="hljs-title class_">Rerun</span> <span class="hljs-variable language_">this</span> command <span class="hljs-keyword">with</span> one <span class="hljs-keyword">of</span> the following passed <span class="hljs-keyword">in</span> <span class="hljs-keyword">as</span> the <span class="hljs-attr">appId</span>:

  flutter attach --app-id com.<span class="hljs-property">example</span>.<span class="hljs-property">myFlutter</span>
  flutter attach --app-id com.<span class="hljs-property">example</span>.<span class="hljs-property">myFlutter</span> (<span class="hljs-number">2</span>)
  flutter attach --app-id com.<span class="hljs-property">mingqing</span>.<span class="hljs-property">mix</span>-flutter
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行<code> flutter attach --app-id com.mingqing.mix-flutter</code> 又出现如下错误</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">mqingiMac</span>:my_flutter tiansifang$ flutter attach --app-id com.<span class="hljs-property">mingqing</span>.<span class="hljs-property">mix</span>-flutter
<span class="hljs-title class_">Multiple</span> devices <span class="hljs-attr">found</span>:
iPhoneMQ (mobile)  • <span class="hljs-number">00008030</span>-001C04D21E89802E            • ios • iOS <span class="hljs-number">13.4</span> <span class="hljs-number">17E255</span>
iPhone <span class="hljs-number">13</span> (mobile) • <span class="hljs-title class_">DE390EED</span>-<span class="hljs-variable constant_">B28A</span>-4D7E-8C2A-<span class="hljs-title class_">EA9EF</span>2637000 • ios • com.<span class="hljs-property">apple</span>.<span class="hljs-property">CoreSimulator</span>.<span class="hljs-property">SimRuntime</span>.<span class="hljs-property">iOS</span>-<span class="hljs-number">15</span>-<span class="hljs-number">0</span> (simulator)
[<span class="hljs-number">1</span>]: iPhoneMQ (<span class="hljs-number">00008030</span>-001C04D21E89802E)
[<span class="hljs-number">2</span>]: iPhone <span class="hljs-number">13</span> (<span class="hljs-title class_">DE390EED</span>-<span class="hljs-variable constant_">B28A</span>-4D7E-8C2A-<span class="hljs-title class_">EA9EF</span>2637000)
<span class="hljs-title class_">Please</span> choose one (<span class="hljs-title class_">To</span> quit, press <span class="hljs-string">"q/Q"</span>): 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次输入 2 来选中模拟器，成功了，然后通过Android Studio 修改flutter 模块儿代码，
通过命令提示
(如下r Hot reload. 🔥🔥🔥R Hot restart.)
来热更新界面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title class_">Please</span> choose one (<span class="hljs-title class_">To</span> quit, press <span class="hljs-string">"q/Q"</span>): <span class="hljs-number">2</span>
<span class="hljs-title class_">Syncing</span> files to device iPhone <span class="hljs-number">13.</span>..                                <span class="hljs-number">6.</span>3s

<span class="hljs-title class_">Flutter</span> run key commands.
r <span class="hljs-title class_">Hot</span> reload. 🔥🔥🔥
R <span class="hljs-title class_">Hot</span> restart.
h <span class="hljs-title class_">List</span> all available interactive commands.
d <span class="hljs-title class_">Detach</span> (terminate <span class="hljs-string">"flutter run"</span> but leave application running).
c <span class="hljs-title class_">Clear</span> the screen
q <span class="hljs-title class_">Quit</span> (terminate the application on the device).

💪 <span class="hljs-title class_">Running</span> <span class="hljs-keyword">with</span> sound <span class="hljs-literal">null</span> safety 💪

<span class="hljs-title class_">An</span> <span class="hljs-title class_">Observatory</span> <span class="hljs-keyword">debugger</span> and profiler on iPhone <span class="hljs-number">13</span> is available <span class="hljs-attr">at</span>: <span class="hljs-attr">http</span>:<span class="hljs-comment">//127.0.0.1:51772/O29OVOaScrA=/</span>
<span class="hljs-title class_">The</span> <span class="hljs-title class_">Flutter</span> <span class="hljs-title class_">DevTools</span> <span class="hljs-keyword">debugger</span> and profiler on iPhone <span class="hljs-number">13</span> is available <span class="hljs-attr">at</span>: <span class="hljs-attr">http</span>:<span class="hljs-comment">//127.0.0.1:9101?uri=http://127.0.0.1:51772/O29OVOaScrA=/</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>总结 flutter attach 命令
最开始直接使用命令选中模拟器和iOS工程</li>
</ol>
<p><code>flutter attach -d DE390EED-B28A-4D7E-8C2A-EA9EF2637000 --app-id com.mingqing.mix-flutter</code></p></div>  
</div>
            