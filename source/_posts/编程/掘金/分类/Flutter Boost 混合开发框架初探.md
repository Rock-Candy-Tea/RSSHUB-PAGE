
---
title: 'Flutter Boost 混合开发框架初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2401426e7da746aa9c197bb5c7620554~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 04:11:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2401426e7da746aa9c197bb5c7620554~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Flutter Boost简介</h1>
<p>众所周知，Flutter是一个由C++实现的Flutter Engine和由Dart实现的Framework组成的跨平台技术框架。其中，Flutter Engine负责线程管理、Dart VM状态管理以及Dart代码加载等工作，而Dart代码所实现的Framework则负责上层业务开发，如Flutter提供的组件等概念就是Framework的范畴。</p>
<p>随着Flutter的发展，国内越来越多的App开始接入Flutter。为了降低风险，大部分App采用渐进式方式引入Flutter，在App里选几个页面用Flutter来编写，但都碰到了相同的问题，在原生页面和Flutter页面共存的情况下，如何管理路由，以及原生页面与Flutter页面之间的切换和通信都是混合开发中需要解决的问题。然而，官方没有提供明确的解决方案，只是在混合开发时，官方建议开发者，应该使用同一个引擎支持多窗口绘制的能力，至少在逻辑上做到FlutterViewController是共享同一个引擎里面的资源。换句话说，官方希望所有的绘制窗口共享同一个主Isolate，而不是出现多个主Isolate的情况。不过，对于现在已经出现的多引擎模式问题，Flutter官方也没有提供好的解决方案。除了内存消耗严重外，多引擎模式还会带来如下一些问题。</p>
<ul>
<li>冗余资源问题。多引擎模式下每个引擎的Isolate是相互独立的，虽然在逻辑上这并没有什么坏处，但是每个引擎底层都维护了一套图片缓存等比较消耗内存的对象，因此设备的内存消耗是非常严重的。</li>
<li>插件注册问题。在Flutter插件中，消息传递需要依赖Messenger，而Messenger是由FlutterViewController去实现的。如果一个应用中同时存在多个FlutterViewController，那么插件的注册和通信将会变得混乱且难以维护。</li>
<li>Flutter组件和原生页面的差异化问题。通常，Flutter页面是由组件构成的，原生页面则是由ViewController或者Activity构成的。逻辑上来说，我们希望消除Flutter页面与原生页面的差异，否则在进行页面埋点和其它一些操作时增加一些额外的工作量。</li>
<li>增加页面通信的复杂度。如果所有的Dart代码都运行在同一个引擎实例中，那么它们会共享同一个Isolate，可以用统一的框架完成组件之间的通信，但是如果存在多个引擎实例会让Isolate的管理变得更加复杂。</li>
</ul>
<p>如果不解决多引擎问题，那么混合项目的导航栈如下图所示。
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2401426e7da746aa9c197bb5c7620554~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
目前，对于原生工程混编Flutter工程出现的多引擎模式问题，国内主要有两种解决方案，一种是字节跳动的修改Flutter Engine源码方案，另一种是闲鱼开源的FlutterBoost。由于字节跳动的混合开发的方案没有开源，所以现在能使用的就剩下FlutterBoost方案。</p>
<p>FlutterBoost是闲鱼技术团队开发的一个可复用页面的插件，旨在把Flutter容器做成类似于浏览器的加载方案。为此，闲鱼技术团队为希望FlutterBoost能完成如下的基本功能：</p>
<ul>
<li>可复用的通用型混合开发方案。</li>
<li>支持更加复杂的混合模式，比如支持Tab切换的场景。</li>
<li>无侵入性方案，使用时不再依赖修改Flutter的方案。</li>
<li>支持对页面生命周期进行统一的管理。</li>
<li>具有统一明确的设计概念。</li>
</ul>
<p>并且，最近Flutter Boost升级了3.0版本，并带来了如下的一些更新：</p>
<ul>
<li>不侵入引擎，兼容Flutter的各种版本，Flutter sdk的升级不需要再升级FlutterBoost，极大降低升级成本。</li>
<li>不区分Androidx和Support分支。</li>
<li>简化架构和接口，和FlutterBoost2.0比，代码减少了一半。</li>
<li>双端统一，包括接口和设计上的统一。</li>
<li>支持打开Flutter页面，不再打开容器场景。</li>
<li>页面生命周期变化通知更方便业务使用。</li>
<li>解决了2.0中的遗留问题，例如，Fragment接入困难、页面关闭后不能传递数据、dispose不执行，内存占用过高等。</li>
</ul>
<h1 data-id="heading-1">二、Flutter Boost集成</h1>
<p>在原生项目中集成Flutter Boost只需要将Flutter Boost看成是一个插件工程即可。和其他Flutter插件的集成方式一样，使用FlutterBoost之前需要先添加依赖。使用Android Studio打开混合工程的Flutter工程，在pubspec.yaml中添加FlutterBoost依赖插件，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">flutter_boost:
    git:
        url: <span class="hljs-string">'https://github.com/alibaba/flutter_boost.git'</span>
        ref: <span class="hljs-string">'v3.0-hotfixes'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要说明的是，此处的所依赖的FlutterBoost的版本与Flutter的版本是对应的，如果不对应使用过程中会出现版本不匹配的错误。然后，使用flutter packages get命令将FlutterBoost插件拉取到本地。</p>
<h2 data-id="heading-2">2.1 Android集成</h2>
<p>使用Android Studio打开新建的原生Android工程，在原生Android工程的settings.gradle文件中添加如下代码。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">setBinding(<span class="hljs-keyword">new</span> Binding([gradle: <span class="hljs-keyword">this</span>]))
evaluate(<span class="hljs-keyword">new</span> File(
  settingsDir.parentFile,
  <span class="hljs-string">'flutter_library/.android/include_flutter.groovy'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，打开原生Android工程app目录下的build.gradle文件，继续添加如下依赖脚本。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">dependencies &#123;
  <span class="hljs-function">implementation <span class="hljs-title">project</span><span class="hljs-params">(<span class="hljs-string">':flutter_boost'</span>)</span>
  implementation <span class="hljs-title">project</span><span class="hljs-params">(<span class="hljs-string">':flutter'</span>)</span>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>重新编译构建原生Android工程，如果没有任何错误则说明Android成功了集成FlutterBoost。使用Flutter Boost 之前，需要先执行初始化。打开原生Android工程，新建一个继承FlutterApplication的Application，然后在onCreate()方法中初始化FlutterBoost，代码如下。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApplication</span> <span class="hljs-title">extends</span> <span class="hljs-title">FlutterApplication</span> &#123;</span>


    @<span class="hljs-function">Override
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
        super.onCreate();

        FlutterBoost.instance().setup(<span class="hljs-keyword">this</span>, <span class="hljs-keyword">new</span> FlutterBoostDelegate() &#123;

            @Override
            <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> pushNativeRoute(String pageName, HashMap<String, String> arguments) &#123;
                Intent intent = <span class="hljs-keyword">new</span> Intent(FlutterBoost.instance().currentActivity(), NativePageActivity.class);
                FlutterBoost.instance().currentActivity().startActivity(intent);
            &#125;

            @Override
            <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> pushFlutterRoute(String pageName, HashMap<String, String> arguments) &#123;
                Intent intent = <span class="hljs-keyword">new</span> FlutterBoostActivity.CachedEngineIntentBuilder(FlutterBoostActivity.class, FlutterBoost.ENGINE_ID)
                        .backgroundMode(FlutterActivityLaunchConfigs.BackgroundMode.opaque)
                        .destroyEngineWithActivity(<span class="hljs-literal">false</span>)
                        .url(pageName)
                        .urlParams(arguments)
                        .build(FlutterBoost.instance().currentActivity());
                FlutterBoost.instance().currentActivity().startActivity(intent);
            &#125;

        &#125;,engine->&#123;
            engine.getPlugins();
        &#125; );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，打开原生Android工程下的AndroidManifest.xml文件，将Application替换成自定义的MyApplication，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><manifest xmlns:android=<span class="hljs-string">"http://schemas.android.com/apk/res/android"</span>
          xmlns:tools=<span class="hljs-string">"http://schemas.android.com/tools"</span>
          package=<span class="hljs-string">"com.idlefish.flutterboost.example"</span>>

    <application
        android:name=<span class="hljs-string">"com.idlefish.flutterboost.example.MyApplication"</span>
        android:label=<span class="hljs-string">"flutter_boost_example"</span>
        android:icon=<span class="hljs-string">"@mipmap/ic_launcher"</span>>

        <activity
            android:name=<span class="hljs-string">"com.idlefish.flutterboost.containers.FlutterBoostActivity"</span>
            android:theme=<span class="hljs-string">"@style/Theme.AppCompat"</span>
            android:configChanges=<span class="hljs-string">"orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density"</span>
            android:hardwareAccelerated=<span class="hljs-string">"true"</span>
            android:windowSoftInputMode=<span class="hljs-string">"adjustResize"</span> >
            <meta-data android:name=<span class="hljs-string">"io.flutter.embedding.android.SplashScreenDrawable"</span> android:resource=<span class="hljs-string">"@drawable/launch_background"</span>/>

        </activity>
        <meta-data android:name=<span class="hljs-string">"flutterEmbedding"</span>
                   android:value=<span class="hljs-string">"2"</span>>
        </meta-data>
    </application>
</manifest>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于Flutter Boost 是以插件的方式集成到原生Android项目的，所以我们可以在Native 打开和关闭Flutter模块的页面。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">FlutterBoost.instance().open(<span class="hljs-string">"flutterPage"</span>,params);
FlutterBoost.instance().close(<span class="hljs-string">"uniqueId"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而Flutter Dart的使用如下。首先，我们可以在main.dart文件的程序入口main()方法中进行初始化。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
  runApp(MyApp());
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-title">extends</span> <span class="hljs-title">StatefulWidget</span> &#123;</span>
  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  _MyAppState <span class="hljs-title">createState</span><span class="hljs-params">()</span> </span>=> _MyAppState();
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> _<span class="hljs-title">MyAppState</span> <span class="hljs-title">extends</span> <span class="hljs-title">State</span><</span>MyApp> &#123;
   <span class="hljs-keyword">static</span> Map<String, FlutterBoostRouteFactory>
   routerMap = &#123;
    <span class="hljs-string">'/'</span>: (settings, uniqueId) &#123;
      <span class="hljs-keyword">return</span> PageRouteBuilder<dynamic>(
          settings: settings, pageBuilder: (_, __, ___)
          => Container());
    &#125;,
    <span class="hljs-string">'embedded'</span>: (settings, uniqueId) &#123;
      <span class="hljs-keyword">return</span> PageRouteBuilder<dynamic>(
          settings: settings,
          pageBuilder: (_, __, ___) =>
          EmbeddedFirstRouteWidget());
    &#125;,
    <span class="hljs-string">'presentFlutterPage'</span>: (settings, uniqueId) &#123;
      <span class="hljs-keyword">return</span> PageRouteBuilder<dynamic>(
          settings: settings,
          pageBuilder: (_, __, ___) =>
          FlutterRouteWidget(
                params: settings.arguments,
                uniqueId: uniqueId,
              ));
    &#125;&#125;;
   <span class="hljs-function">Route<dynamic> <span class="hljs-title">routeFactory</span><span class="hljs-params">(RouteSettings settings, String uniqueId)</span> </span>&#123;
    FlutterBoostRouteFactory func =routerMap[settings.name];
    <span class="hljs-keyword">if</span> (func == null) &#123;
      <span class="hljs-keyword">return</span> null;
    &#125;
    <span class="hljs-keyword">return</span> func(settings, uniqueId);
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">initState</span><span class="hljs-params">()</span> </span>&#123;
    super.initState();
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  Widget <span class="hljs-title">build</span><span class="hljs-params">(BuildContext context)</span> </span>&#123;
    <span class="hljs-keyword">return</span> FlutterBoostApp(
      routeFactory
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，还可以监听页面的生命周期，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SimpleWidget</span> <span class="hljs-title">extends</span> <span class="hljs-title">StatefulWidget</span> &#123;</span>
  <span class="hljs-keyword">final</span> Map params;
  <span class="hljs-keyword">final</span> String messages;
  <span class="hljs-keyword">final</span> String uniqueId;

  <span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">SimpleWidget</span><span class="hljs-params">(<span class="hljs-keyword">this</span>.uniqueId, <span class="hljs-keyword">this</span>.params, <span class="hljs-keyword">this</span>.messages)</span></span>;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  _SimpleWidgetState <span class="hljs-title">createState</span><span class="hljs-params">()</span> </span>=> _SimpleWidgetState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> _<span class="hljs-title">SimpleWidgetState</span> <span class="hljs-title">extends</span> <span class="hljs-title">State</span><</span>SimpleWidget>
    with PageVisibilityObserver &#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> String _kTag = <span class="hljs-string">'xlog'</span>;
  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">didChangeDependencies</span><span class="hljs-params">()</span> </span>&#123;
    super.didChangeDependencies();
    print(<span class="hljs-string">'$_kTag#didChangeDependencies, $&#123;widget.uniqueId&#125;, $this'</span>);

  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">initState</span><span class="hljs-params">()</span> </span>&#123;
    super.initState();
   PageVisibilityBinding.instance.addObserver(<span class="hljs-keyword">this</span>, ModalRoute.of(context));
   print(<span class="hljs-string">'$_kTag#initState, $&#123;widget.uniqueId&#125;, $this'</span>);
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">dispose</span><span class="hljs-params">()</span> </span>&#123;
    PageVisibilityBinding.instance.removeObserver(<span class="hljs-keyword">this</span>);
    print(<span class="hljs-string">'$_kTag#dispose, $&#123;widget.uniqueId&#125;, $this'</span>);
    super.dispose();
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">onForeground</span><span class="hljs-params">()</span> </span>&#123;
    print(<span class="hljs-string">'$_kTag#onForeground, $&#123;widget.uniqueId&#125;, $this'</span>);
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">onBackground</span><span class="hljs-params">()</span> </span>&#123;
    print(<span class="hljs-string">'$_kTag#onBackground, $&#123;widget.uniqueId&#125;, $this'</span>);
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  <span class="hljs-keyword">void</span> <span class="hljs-title">onAppear</span><span class="hljs-params">(ChangeReason reason)</span> </span>&#123;
    print(<span class="hljs-string">'$_kTag#onAppear, $&#123;widget.uniqueId&#125;, $reason, $this'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onDisappear</span><span class="hljs-params">(ChangeReason reason)</span> </span>&#123;
    print(<span class="hljs-string">'$_kTag#onDisappear, $&#123;widget.uniqueId&#125;, $reason, $this'</span>);
  &#125;

  @<span class="hljs-function"><span class="hljs-keyword">override</span>
  Widget <span class="hljs-title">build</span><span class="hljs-params">(BuildContext context)</span> </span>&#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">'tab_example'</span>),
      ),
      body: SingleChildScrollView(
          physics: BouncingScrollPhysics(),
          child: Container(
              child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Container(
                margin: <span class="hljs-keyword">const</span> EdgeInsets.only(top: <span class="hljs-number">80.0</span>),
                child: Text(
                  widget.messages,
                  style: TextStyle(fontSize: <span class="hljs-number">28.0</span>, color: Colors.blue),
                ),
                alignment: AlignmentDirectional.center,
              ),
              Container(
                margin: <span class="hljs-keyword">const</span> EdgeInsets.only(top: <span class="hljs-number">32.0</span>),
                child: Text(
                  widget.uniqueId,
                  style: TextStyle(fontSize: <span class="hljs-number">22.0</span>, color: Colors.red),
                ),
                alignment: AlignmentDirectional.center,
              ),
              InkWell(
                child: Container(
                    padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">8.0</span>),
                    margin: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">30.0</span>),
                    color: Colors.yellow,
                    child: Text(
                      <span class="hljs-string">'open flutter page'</span>,
                      style: TextStyle(fontSize: <span class="hljs-number">22.0</span>, color: Colors.black),
                    )),
                onTap: () => BoostNavigator.of().push(<span class="hljs-string">"flutterPage"</span>,
                    arguments: <String, String>&#123;<span class="hljs-string">'from'</span>: widget.uniqueId&#125;),
              )
              Container(
                height: <span class="hljs-number">300</span>,
                width: <span class="hljs-number">200</span>,
                child: Text(
                  <span class="hljs-string">'',
                  style: TextStyle(fontSize: 22.0, color: Colors.black),
                ),
              )
            ],
          ))),
    );
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，运行项目，就可以从原生页面跳转到Flutter页面，如下图所示效果。
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52949968e33e41d19ac1a673df3f9ae1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2.2 iOS集成</h2>
<p>和Android的集成步骤一样，使用Xcode打开原生iOS工程，然后在iOS的AppDelegate文件中初始化Flutter Boost ，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">@<span class="hljs-function">interface <span class="hljs-title">AppDelegate</span> <span class="hljs-params">()</span>

@end

@implementation AppDelegate

- <span class="hljs-params">(BOOL)</span>application:<span class="hljs-params">(UIApplication *)</span>application didFinishLaunchingWithOptions:<span class="hljs-params">(NSDictionary *)</span>launchOptions
</span>&#123;
  MyFlutterBoostDelegate* delegate=[[MyFlutterBoostDelegate alloc ] init];
    [[FlutterBoost instance] setup:application delegate:delegate callback:^(FlutterEngine *engine) &#123;
    &#125; ];

    <span class="hljs-keyword">return</span> YES;
&#125;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是自定义的FlutterBoostDelegate的代码，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">@interface MyFlutterBoostDelegate : NSObject<FlutterBoostDelegate>
@property (nonatomic,strong) UINavigationController *navigationController;
@end

@implementation MyFlutterBoostDelegate

- (<span class="hljs-keyword">void</span>) pushNativeRoute:(FBCommonParams*) params&#123;
    BOOL animated = [params.arguments[@<span class="hljs-string">"animated"</span>] boolValue];
    BOOL present= [params.arguments[@<span class="hljs-string">"present"</span>] boolValue];
    UIViewControllerDemo *nvc = [[UIViewControllerDemo alloc] initWithNibName:@<span class="hljs-string">"UIViewControllerDemo"</span> bundle:[NSBundle mainBundle]];
    <span class="hljs-keyword">if</span>(present)&#123;
        [self.navigationController presentViewController:nvc animated:animated completion:^&#123;
        &#125;];
    &#125;<span class="hljs-keyword">else</span>&#123;
        [self.navigationController pushViewController:nvc animated:animated];
    &#125;
&#125;

- (<span class="hljs-keyword">void</span>) pushFlutterRoute:(FBCommonParams*)params &#123;

    FlutterEngine* engine =  [[FlutterBoost instance ] getEngine];
    engine.viewController = nil;

    FBFlutterViewContainer *vc = FBFlutterViewContainer.<span class="hljs-keyword">new</span> ;

    [vc setName:params.pageName params:params.arguments];

    BOOL animated = [params.arguments[@<span class="hljs-string">"animated"</span>] boolValue];
    BOOL present= [params.arguments[@<span class="hljs-string">"present"</span>] boolValue];
    <span class="hljs-keyword">if</span>(present)&#123;
        [self.navigationController presentViewController:vc animated:animated completion:^&#123;
        &#125;];
    &#125;<span class="hljs-keyword">else</span>&#123;
        [self.navigationController pushViewController:vc animated:animated];

    &#125;
&#125;

- (<span class="hljs-keyword">void</span>) popRoute:(FBCommonParams*)params
         result:(NSDictionary *)result&#123;

    FBFlutterViewContainer *vc = (id)self.navigationController.presentedViewController;

    <span class="hljs-keyword">if</span>([vc isKindOfClass:FBFlutterViewContainer.class] && [vc.uniqueIDString isEqual: params.uniqueId])&#123;
        [vc dismissViewControllerAnimated:YES completion:^&#123;&#125;];
    &#125;<span class="hljs-keyword">else</span>&#123;
        [self.navigationController popViewControllerAnimated:YES];
    &#125;

&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要在原生iOS代码中打开或关闭Flutter页面，可以使用下面的方式。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">[[FlutterBoost instance] open:@<span class="hljs-string">"flutterPage"</span> arguments:@&#123;@<span class="hljs-string">"animated"</span>:@(YES)&#125;  ];
[[FlutterBoost instance] open:@<span class="hljs-string">"secondStateful"</span> arguments:@&#123;@<span class="hljs-string">"present"</span>:@(YES)&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">三、Flutter Boost架构</h1>
<p>对于混合工程来说，原生端和Flutter端对于页面的定义是不一样的。对于原生端而言，页面通常指的是一个ViewController或者Activity，而对于Flutter来说，页面通常指的是Flutter组件。FlutterBoost框架所要做的就是统一混合工程中页面的概念，或者说弱化Flutter组件对应容器页面的概念。换句话说，当有一个原生页面存在的时候，FlutteBoost就能保证一定有一个对应的Flutter的容器页面存在。</p>
<p>FlutterBoost框架其实就是由原生容器通过消息驱动Flutter页面容器，从而达到原生容器与Flutter容器同步的目的，而Flutter渲染的内容是由原生容器去驱动的，下面是Flutter Boost 给的一个Flutter Boost 的架构示意图。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e49eb0dc24245b599b4acb3a7790d3a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
可以看到，Flutter Boost插件分为平台和Dart两端，中间通过Message Channel连接。平台侧提供了Flutter引擎的配置和管理、Native容器的创建/销毁、页面可见性变化通知，以及Flutter页面的打开/关闭接口等。而Dart侧除了提供类似原生Navigator的页面导航接口的能力外，还负责Flutter页面的路由管理。</p>
<p>总的来说，正是基于共享同一个引擎的方案，使得FlutterBoost框架有效的解决了多引擎的问题。简单来说，FlutterBoost在Dart端引入了容器的概念，当存在多个Flutter页面时，FlutterBoost不需要再用栈的结构去维护现有页面，而是使用扁平化键值对映射的形式去维护当前所有的页面，并且每个页面拥有一个唯一的id</p>
<h1 data-id="heading-5">四、FlutterBoost3.0更新</h1>
<h2 data-id="heading-6">4.1 不入侵引擎</h2>
<p>为了解决官方引擎复用引起的问题，FlutterBoost2.0拷贝了Flutter引擎Embedding层的一些代码进行改造，这使得后期的升级成本极高。而FlutterBoost3.0采用继承的方式扩展FlutterActivity/FlutterFragment等组件的能力，并且通过在适当时机给Dart侧发送appIsResumed消息解决引擎复用时生命周期事件错乱导致的页面卡死问题，并且，FlutterBoost 3.0 也兼容最新的官方发布的 Flutter 2.0。</p>
<h2 data-id="heading-7">4.2 不区分Androidx和Support分支</h2>
<p>FlutterBoost2.0通过自己实现FlutterActivityAndFragmentDelegate.Host接口来扩展FlutterActivity和FlutterFragment的能力，而getLifecycle是必须实现的接口，这就导致对androidx的依赖。这也是为什么FlutterBoostView的实现没有被放入FlutterBoost3.0插件中的原因。而FlutterBoost3.0通过继承的方式扩展FlutterActivity/FlutterFragment的能力的额外收益就是，可以做到不依赖androidx。</p>
<h2 data-id="heading-8">4.3 双端设计统一，接口统一</h2>
<p>很多Flutter开发者只会一端，只会Android 或者只会IOS，但他需要接入双端，所以双端统一能降低他的 学习成本和接入成本。FlutterBoost3.0，在设计上 Android和IOS都做了对齐，特别接口上做到了参数级的对齐。</p>
<h2 data-id="heading-9">4.4 支持 【打开flutter页面不再打开容器】 场景</h2>
<p>在Flutter模块内部，Flutter 页面跳转Flutter 页面是可以不需要再打开Flutter容器的，不打开容器，能节省内存开销。在FlutterBoost3.0上，打开容器和不打开容器的区别表现在用户接口上仅仅是withContainer参数是否为true就好。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">InkWell(
  child: Container(
      color: Colors.yellow,
      child: Text(
        <span class="hljs-string">'打开外部路由'</span>,
        style: TextStyle(fontSize: <span class="hljs-number">22.0</span>, color: Colors.black),
      )),
  onTap: () => BoostNavigator.of().push(<span class="hljs-string">"flutterPage"</span>,
      arguments: <String, String>&#123;<span class="hljs-string">'from'</span>: widget.uniqueId&#125;),
),
InkWell(
  child: Container(
      color: Colors.yellow,
      child: Text(
        <span class="hljs-string">'打开内部路由'</span>,
        style: TextStyle(fontSize: <span class="hljs-number">22.0</span>, color: Colors.black),
      )),
  onTap: () => BoostNavigator.of().push(<span class="hljs-string">"flutterPage"</span>,
      withContainer: <span class="hljs-literal">true</span>,
      arguments: <String, String>&#123;<span class="hljs-string">'from'</span>: widget.uniqueId&#125;),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4.5 生命周期的精准通知</h2>
<p>在FlutterBoost2.0上，每个页面都会收到页面生命周期通知，而FlutterBoost3.0只会通知页面可见性实际发生了变化的页面，接口也更符合flutter的设计。</p>
<h2 data-id="heading-11">4.6 其他Issue</h2>
<p>除了上面的一些特性外，Flutter Boost 3.0版本还解决了如下一些问题：</p>
<ul>
<li>页面关闭后参数的传递，之前只有iOS支持，android不支持，目前在dart侧实现，Ios 和Android 都支持。</li>
<li>解决了Android 状态栏字体和颜色问题。</li>
<li>解决了页面回退willpopscope不起作用问题。</li>
<li>解决了不在栈顶的页面也收到生命周期回调的问题</li>
<li>解决了多次setState耗性能问题。</li>
<li>提供了Framgent 多种接入方式的Demo，方便tab 场景的接入。</li>
<li>生命周期的回调代码，可以用户代码里面with的方式接入，使用更简单。</li>
<li>全面简化了，接入成本，包括 dart侧，android侧和ios</li>
<li>丰富了demo，包含了基本场景，方便用户接入 和测试回归</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            