
---
title: '在Flutter项目中开发IOS桌面组件(WidgetExtension)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1889e33f1a64452ca32c8c29a96d728c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 22:56:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1889e33f1a64452ca32c8c29a96d728c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">在Flutter项目中开发IOS桌面组件(WidgetExtension)</h4>
<p>具体的WidgetExtension的开发流程这里就不细说了，可以参考文末的链接。</p>
<p>在Flutter项目开发IOSWidget的过程中，主要的问题有：</p>
<ul>
<li>App和Widget的数据共享</li>
<li>点击Widget跳转App的指定界面</li>
<li>在App界面编辑并更新Widget数据</li>
</ul>
<h5 data-id="heading-1">App和Widget数据共享</h5>
<p>数据共享使用的是UserDefaults,前提是需要为WidgetExtension和Runner添加相同的AppGroup。添加AppGroup的方法为：</p>
<blockquote>
<p>Runner -> Target -> Runner -> Signing&Capabilities -> AppGroups -> +</p>
</blockquote>
<p>这里如果没有AppGroups可以XCode点击右上角的+号来添加AppGroups。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1889e33f1a64452ca32c8c29a96d728c~tplv-k3u1fbpfcp-watermark.image" alt="AppGroup.jpg" loading="lazy" referrerpolicy="no-referrer">
WidgetExtension添加方法同上，其中AppGroup要和Runner的相同。</p>
<p><strong>UserDefaults的使用</strong></p>
<p>这里以实际的例子为大家展示UserDefaults的使用。为了方便演示，在App启动时保存相关数据，以供小组件进行读取。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 以下代码在AppDelegate.swift中的Application方法中</span>
<span class="hljs-comment">// suitName: 为上面添加的AppGroup</span>
<span class="hljs-keyword">let</span> userDefaults <span class="hljs-operator">=</span> <span class="hljs-type">UserDefaults</span>.<span class="hljs-keyword">init</span>(suiteName: <span class="hljs-string">"group.com.cc.ToDo"</span>)
userDefaults<span class="hljs-operator">!</span>.setValue(<span class="hljs-string">"defaultID"</span>, forKey: <span class="hljs-string">"id"</span>)
userDefaults<span class="hljs-operator">!</span>.setValue(<span class="hljs-string">"defauleName"</span>, forKey: <span class="hljs-string">"name"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在小组件中读取</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">getTimeline</span>(<span class="hljs-params">in</span> <span class="hljs-params">context</span>: <span class="hljs-type">Context</span>, <span class="hljs-params">completion</span>: <span class="hljs-keyword">@escaping</span> (<span class="hljs-type">Timeline</span><<span class="hljs-type">Entry</span>>) -> <span class="hljs-type">Void</span>)</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"start getTimeline"</span>)
        <span class="hljs-keyword">let</span> userDefaults <span class="hljs-operator">=</span> <span class="hljs-type">UserDefaults</span>(suiteName: <span class="hljs-string">"group.com.cc.ToDo"</span>)
        <span class="hljs-keyword">let</span> id <span class="hljs-operator">=</span> userDefaults<span class="hljs-operator">?</span>.string(forKey: <span class="hljs-string">"id"</span>)
        <span class="hljs-keyword">let</span> name <span class="hljs-operator">=</span> userDefaults<span class="hljs-operator">?</span>.string(forKey: <span class="hljs-string">"name"</span>)
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"timeline:  <span class="hljs-subst">\(id<span class="hljs-operator">!</span>)</span> <span class="hljs-subst">\(name<span class="hljs-operator">!</span>)</span>"</span>)
        <span class="hljs-comment">// ... 这里省略了后续的completion</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">点击Widget跳转App的指定界面</h5>
<p>在小组件点击跳转App这块，本次使用的技术为widgetURL以及URL Schemes。</p>
<p>在小组件中处理点击跳转主要有两种方法：</p>
<ul>
<li>widgetURL：作用于整个小组件，且一个小组件只能有一个</li>
<li>Link：作用于Link包裹的组件的大小，在小尺寸[systemSmall]组件中无法使用Link</li>
</ul>
<p>可以根据实际情况选择合适的组件。</p>
<p><strong>URL Schemes</strong></p>
<p>URL Schemes主要负责处理跳转逻辑，通过配置URL Schemes，在App中捕获对应的url和参数来实现跳转指定页。
注册URL Schemes主要包含以下几步：</p>
<blockquote>
<p>Runner -> Info -> URL Types -> 添加+ -> 编辑URL Schemes</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e3ca960dfc24448bf91b8529420cb6a~tplv-k3u1fbpfcp-watermark.image" alt="URLSchemes.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成之后可以再widgetURL中添加url(以上述配置的URL Schemes开头)，代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> body: <span class="hljs-keyword">some</span> <span class="hljs-type">View</span>&#123;
    <span class="hljs-type">VStack</span>&#123;
        <span class="hljs-type">Text</span>(<span class="hljs-string">"ToDoList"</span>)
        <span class="hljs-type">Text</span>(entry.userid)
        <span class="hljs-type">Text</span>(entry.author)
    &#125;
    <span class="hljs-comment">// URL以配置的URL Schemes开头，可以拼接参数</span>
    .widgetURL(<span class="hljs-type">URL</span>(string: <span class="hljs-string">"dynamictheme://user?userid=<span class="hljs-subst">\(entry.userid)</span>&author=<span class="hljs-subst">\(entry.author)</span>"</span>))
&#125;
<span class="hljs-comment">// 在Link中配置的URL同此</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Flutter端则使用uni_links库来进行链接捕获和跳转，具体实现如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart">
<span class="hljs-keyword">import</span> <span class="hljs-string">'dart:async'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/cupertino.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/services.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:uni_links/uni_links.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'pages/UserPage.dart'</span>;

GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _MyAppState createState() => _MyAppState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyAppState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyApp</span>> </span>&#123;
  StreamSubscription<<span class="hljs-built_in">String</span>> _sub;
  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    initPlatformStateForStringUniLinks();
  &#125;

  Future<<span class="hljs-keyword">void</span>> initPlatformStateForStringUniLinks() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-built_in">String</span> initialLink;
    <span class="hljs-comment">// App未打开的状态在这个地方捕获scheme</span>
    <span class="hljs-keyword">try</span> &#123;
      initialLink = <span class="hljs-keyword">await</span> getInitialLink();
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'跳转地址: <span class="hljs-subst">$initialLink</span>'</span>);
      <span class="hljs-keyword">if</span> (initialLink != <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">'跳转地址不为null --<span class="hljs-subst">$initialLink</span>'</span>);
        <span class="hljs-comment">//  跳转到指定页面</span>
        schemeJump(context, initialLink);
      &#125;
    &#125; <span class="hljs-keyword">on</span> PlatformException &#123;
      initialLink = <span class="hljs-string">'Failed to get initial link.'</span>;
    &#125; <span class="hljs-keyword">on</span> FormatException &#123;
      initialLink = <span class="hljs-string">'Failed to parse the initial link as Uri.'</span>;
    &#125;
    <span class="hljs-comment">// App打开的状态监听scheme</span>
    _sub = getLinksStream().listen((<span class="hljs-built_in">String</span> link) &#123;
      <span class="hljs-keyword">if</span> (!mounted || link == <span class="hljs-keyword">null</span>) <span class="hljs-keyword">return</span>;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'link--<span class="hljs-subst">$link</span>'</span>);
      <span class="hljs-comment">//  跳转到指定页面</span>
      schemeJump(context, link);
    &#125;, onError: (<span class="hljs-built_in">Object</span> err) &#123;
      <span class="hljs-keyword">if</span> (!mounted) <span class="hljs-keyword">return</span>;
    &#125;);
  &#125;

  <span class="hljs-keyword">void</span> schemeJump(BuildContext context, <span class="hljs-built_in">String</span> schemeUrl) &#123;
    <span class="hljs-keyword">final</span> <span class="hljs-built_in">Uri</span> _jumpUri = <span class="hljs-built_in">Uri</span>.parse(schemeUrl.replaceFirst(
      <span class="hljs-string">'dynamictheme://'</span>,
      <span class="hljs-string">'http://path/'</span>,
    ));
    <span class="hljs-keyword">switch</span> (_jumpUri.path) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'/user'</span>:
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"接收到的参数为："</span>);
        <span class="hljs-built_in">String</span> userid = _jumpUri.queryParameters[<span class="hljs-string">"userid"</span>];
        <span class="hljs-built_in">print</span>(userid);
        <span class="hljs-built_in">String</span> author = _jumpUri.queryParameters[<span class="hljs-string">"author"</span>];
        <span class="hljs-built_in">print</span>(author);

        Navigator.of(navigatorKey.currentContext).push(CupertinoPageRoute(
            builder: (context) => UserPage(
                  userid: userid,
                  author: author,
                )));
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">break</span>;
    &#125;
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    <span class="hljs-keyword">super</span>.dispose();
    _sub.cancel();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
      navigatorKey: navigatorKey,
      title: <span class="hljs-string">'Flutter 与 IOS'</span>,
      theme:
      ThemeData(primarySwatch: Colors.blue, platform: TargetPlatform.iOS),
      home: HomePage(),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomePage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"HomePage"</span>)
      ),
      body: Center(
        child: Text(<span class="hljs-string">"Home page"</span>),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">在App界面编辑并更新Widget数据</h5>
<p>在App编辑数据并更新widget功能中，通过MenthodChannel来实现。当编辑完数据，需要更新时，通过MethodChannel来调用原生方法，在原生方法中更新UserDefaults的数据，并返回结果给Flutter端。</p>
<p>数据更新完成并不会刷新Widget，因为Widget中使用的是前一Timeline的快照，在下一个Timeline之前并不会刷新数据，因此需要主动调用相关方法来更新数据。</p>
<p>在原生端想要主动来更新小组件的Timeline，主要有两种方法：</p>
<ul>
<li>WidgetCenter.shared.reloadAllTimelines(): 跟新App下所有组件的Timelines</li>
<li>WidgetCenter.shared.reloadTimelines(ofKind: kind): 更新指定kind类型组件的Timelines</li>
</ul>
<p>具体的实现如下可参考以下代码</p>
<p>Flutter端代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart">MethodChannel channel = MethodChannel(<span class="hljs-string">"com.cc.ToDo.widgets"</span>);
<span class="hljs-keyword">var</span> res = <span class="hljs-keyword">await</span> channel.invokeMethod(<span class="hljs-string">"updateWidgetData"</span>, &#123;
    <span class="hljs-string">"userid"</span>:idController.text,
    <span class="hljs-string">"author"</span>:nameController.text
&#125;);

<span class="hljs-built_in">print</span>(res);
<span class="hljs-built_in">print</span>(res.runtimeType);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Swift端代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">import</span> UIKit
<span class="hljs-keyword">import</span> Flutter
<span class="hljs-keyword">import</span> WidgetKit

<span class="hljs-keyword">@UIApplicationMain</span>
<span class="hljs-keyword">@objc</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppDelegate</span>: <span class="hljs-title">FlutterAppDelegate</span> </span>&#123;
  <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">application</span>(
    <span class="hljs-keyword">_</span> <span class="hljs-params">application</span>: <span class="hljs-type">UIApplication</span>,
    <span class="hljs-params">didFinishLaunchingWithOptions</span> <span class="hljs-params">launchOptions</span>: [<span class="hljs-type">UIApplication</span>.<span class="hljs-params">LaunchOptionsKey</span>: <span class="hljs-keyword">Any</span>]<span class="hljs-operator">?</span>
  )</span> -> <span class="hljs-type">Bool</span> &#123;
    
    <span class="hljs-keyword">let</span> controller:<span class="hljs-type">FlutterViewController</span> <span class="hljs-operator">=</span> window<span class="hljs-operator">?</span>.rootViewController <span class="hljs-keyword">as!</span> <span class="hljs-type">FlutterViewController</span>
    
    <span class="hljs-keyword">let</span> userDefaults <span class="hljs-operator">=</span> <span class="hljs-type">UserDefaults</span>.<span class="hljs-keyword">init</span>(suiteName: <span class="hljs-string">"group.com.cc.ToDo"</span>)
    userDefaults<span class="hljs-operator">!</span>.setValue(<span class="hljs-string">"defaultID"</span>, forKey: <span class="hljs-string">"userid"</span>)
    userDefaults<span class="hljs-operator">!</span>.setValue(<span class="hljs-string">"defauleName"</span>, forKey: <span class="hljs-string">"author"</span>)
    <span class="hljs-comment">// 初始化MethodChannel，设置监听</span>
    <span class="hljs-type">WidgetMenthod</span>.<span class="hljs-keyword">init</span>(messger: controller.binaryMessenger)
    <span class="hljs-type">GeneratedPluginRegistrant</span>.register(with: <span class="hljs-keyword">self</span>)

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.application(application, didFinishLaunchingWithOptions: launchOptions)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 处理Flutter调用</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WidgetMenthod</span></span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">messger</span>:<span class="hljs-type">FlutterBinaryMessenger</span>)</span>&#123;
        <span class="hljs-keyword">let</span> channel <span class="hljs-operator">=</span> <span class="hljs-type">FlutterMethodChannel</span>(name: <span class="hljs-string">"com.cc.ToDo.widgets"</span>, binaryMessenger: messger)
        channel.setMethodCallHandler&#123;(call:<span class="hljs-type">FlutterMethodCall</span>, result: <span class="hljs-keyword">@escaping</span> <span class="hljs-type">FlutterResult</span>) <span class="hljs-keyword">in</span>
            <span class="hljs-comment">// 通过call.method来判断要调用的方法</span>
            <span class="hljs-keyword">if</span>(call.method <span class="hljs-operator">==</span> <span class="hljs-string">"updateWidgetData"</span>)&#123;
            <span class="hljs-comment">// 通过call.arguments来获取参数</span>
                <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> dict <span class="hljs-operator">=</span> call.arguments <span class="hljs-keyword">as?</span> <span class="hljs-type">Dictionary</span><<span class="hljs-type">String</span>,<span class="hljs-keyword">Any</span>>&#123;
                    <span class="hljs-keyword">let</span> userid <span class="hljs-operator">=</span> dict[<span class="hljs-string">"userid"</span>] <span class="hljs-keyword">as?</span> <span class="hljs-type">String</span>
                    <span class="hljs-keyword">let</span> author <span class="hljs-operator">=</span> dict[<span class="hljs-string">"author"</span>] <span class="hljs-keyword">as?</span> <span class="hljs-type">String</span>
                    <span class="hljs-built_in">print</span>(<span class="hljs-string">"<span class="hljs-subst">\(userid)</span> ==== <span class="hljs-subst">\(author)</span>"</span>)
                    <span class="hljs-keyword">let</span> userDefaults <span class="hljs-operator">=</span> <span class="hljs-type">UserDefaults</span>.<span class="hljs-keyword">init</span>(suiteName: <span class="hljs-string">"group.com.cc.ToDo"</span>)
                    userDefaults<span class="hljs-operator">!</span>.setValue(userid, forKey: <span class="hljs-string">"userid"</span>)
                    userDefaults<span class="hljs-operator">!</span>.setValue(author, forKey: <span class="hljs-string">"author"</span>)
                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">#available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">14.0</span>, <span class="hljs-operator">*</span>) &#123;
                        <span class="hljs-built_in">print</span>(<span class="hljs-string">"reload timelines"</span>)
                        <span class="hljs-type">WidgetCenter</span>.shared.reloadTimelines(ofKind: <span class="hljs-string">"todo_list"</span>)
                        <span class="hljs-built_in">print</span>(<span class="hljs-string">"reload complete!"</span>)
                        result([<span class="hljs-string">"code"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"msg"</span>:<span class="hljs-string">"success"</span>])
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        result([<span class="hljs-string">"code"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"msg"</span>:<span class="hljs-string">"系统版本过低"</span>])
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    result([<span class="hljs-string">"code"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"msg"</span>:<span class="hljs-string">"参数异常"</span>])
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，在Flutter项目中开发IOS桌面组件就全部完成了。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F1377283509%2Fflutter_ios_widget" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/1377283509/flutter_ios_widget" ref="nofollow noopener noreferrer">完整案例源码点此下载</a></p>
<h5 data-id="heading-4">参考文章</h5>
<p><a href="https://juejin.cn/post/6887759096506744840?share_token=1869ea18-187d-4997-9101-3e39605adc61" target="_blank" title="https://juejin.cn/post/6887759096506744840?share_token=1869ea18-187d-4997-9101-3e39605adc61">网易云音乐 iOS 14 小组件实战手册</a></p>
<p><a href="https://juejin.cn/post/6885487318208086029?share_token=42de4e4d-776a-4f8b-973d-0cd094a1343b" target="_blank" title="https://juejin.cn/post/6885487318208086029?share_token=42de4e4d-776a-4f8b-973d-0cd094a1343b">【Flutter 混合开发】与原生通信-MethodChannel</a></p></div>  
</div>
            