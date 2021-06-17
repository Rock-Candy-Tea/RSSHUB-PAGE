
---
title: 'Dart语言async函数不正确的异常处理引发的异常'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c91a88e944841a2b08f81502aa1561f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 22:51:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c91a88e944841a2b08f81502aa1561f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文介绍了当你使用了Dart异步函数并进行try-catch异常处理的时候，很容易陷入的一个坑。并且它可能有助于分析并解决一些跟异步调用有关的Dart崩溃问题。</p>
</blockquote>
<h1 data-id="heading-0">小测试</h1>
<p>这样写platform channel调用并处理异常的代码，有啥问题？</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> MethodChannel channel = MethodChannel(<span class="hljs-string">'my_platform_channel'</span>);
<span class="hljs-keyword">try</span> &#123;
  channel.invokeMethod(<span class="hljs-string">'my_method'</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  debugPrint(<span class="hljs-string">'Caught an exception: <span class="hljs-subst">$e</span>'</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果往下看：</p>
<p>代码这样直接用try-catch是无效的，不会走到catch块里！且日志里直接显示Unhandled Exception。</p>
<p>因为<code>channel.invokeMethod</code>是一个异步函数，它的返回值是Future:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 省略巨长的官方函数文档</span>

Future<T?> invokeMethod<T>(<span class="hljs-built_in">String</span> method, [ <span class="hljs-built_in">dynamic</span> arguments ]) &#123;
  <span class="hljs-keyword">return</span> _invokeMethod<T>(method, missingOk: <span class="hljs-keyword">false</span>, arguments: arguments);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多的分析和正确的写法，请看下文。</p>
<h1 data-id="heading-1">最佳实践</h1>
<ol>
<li>如果使用了await调用了异步函数（返回Future的函数）并且需要做异常处理，在await外面直接try-catch即可</li>
<li>如果没有使用await调用了异步函数（返回Future的函数）并且需要做异常处理，千万不要直接try-catch（否则起不到捕获作用，代码会继续误导下一个人），需要使用<code>onError</code>或者<code>catchError</code>做对应的处理或者re-throw。</li>
</ol>
<p>背景</p>
<p>先说下这个问题的背景是，调查了一个webview_flutter和一个settings插件的platform调用异常问题，两个异常很类似：</p>
<p>有如下异常：</p>
<pre><code class="hljs language-dart copyable" lang="dart">MissingPluginException(No implementation found <span class="hljs-keyword">for</span> method evaluateJavascript <span class="hljs-keyword">on</span> channel plugins.flutter.io/webview_0)
#<span class="hljs-number">0</span>      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:<span class="hljs-number">253</span>)
<asynchronous suspension>
<span class="hljs-comment">// 然后就没有然后了，没有调用者的行号</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这应该是一个类似于上面提到的 <code>channel.invokeMethod('evaluateJavascript')</code> 的调用。在查看webview plugin部分出现的invokeMethod的dart代码后，看到代码是这样写的：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// js_bridge.dart</span>
            <span class="hljs-string">""" // 省略一些js代码
            &#125;
            return result;
        &#125;)(<span class="hljs-subst">$s</span>)"""</span>;
  <span class="hljs-keyword">try</span> &#123;
    _webViewController.evaluateJavascript(js);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>evaluateJavascript</code>里面的实现是这样</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-meta">@override</span>
Future<<span class="hljs-built_in">String</span>> evaluateJavascript(<span class="hljs-built_in">String</span> javascriptString) &#123;
  <span class="hljs-keyword">return</span> _channel.invokeMethod<<span class="hljs-built_in">String</span>>(
      <span class="hljs-string">'evaluateJavascript'</span>, javascriptString);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一反应，🤔 try-catch 为什么没有catch住异常呢？</p>
<h1 data-id="heading-2">做了5个测试</h1>
<p>看下面的5种情况的异常处理的测试代码，前提是：<code>getPlatformVersion</code>故意弄成了一个没有注册过的channel method的名字，一定会抛出<code>MissingPluginException</code>异常。</p>
<p>那么猜想5种写法分别会得到什么结果？</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlutterPluginDemo</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MethodChannel _channel =
      <span class="hljs-keyword">const</span> MethodChannel(<span class="hljs-string">'flutter_plugin_demo'</span>);

  <span class="hljs-keyword">static</span> Future<<span class="hljs-built_in">String</span>> <span class="hljs-keyword">get</span> platformVersion <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">var</span> future;
    <span class="hljs-comment">// 第1种错误处理: 错误</span>
    <span class="hljs-keyword">try</span> &#123;
      future = _channel.invokeMethod(<span class="hljs-string">'getPlatformVersion'</span>);
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'1. future.type: <span class="hljs-subst">$&#123;future.runtimeType&#125;</span>'</span>); <span class="hljs-comment">// invoke的返回值是个Future</span>
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-comment">// 所以这里基本永远不会走到</span>
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'1. caught a exception: <span class="hljs-subst">$e</span>'</span>);
    &#125;

    <span class="hljs-comment">// 第2种错误处理: 正确</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">await</span> future;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'2. result.type: <span class="hljs-subst">$&#123;result.runtimeType&#125;</span>'</span>);
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'2. caught a exception by try-catch: <span class="hljs-subst">$e</span>'</span>); <span class="hljs-comment">// 这里可以正确catch住上面第1个future的异常</span>
    &#125;

    <span class="hljs-comment">// 第3种错误处理: 正确</span>
    _channel.invokeMethod(<span class="hljs-string">'getPlatformVersion'</span>).onError(
        (error, stackTrace) => <span class="hljs-built_in">print</span>(<span class="hljs-string">'3. caught a exception by onError: <span class="hljs-subst">$error</span>'</span>));

    <span class="hljs-comment">// 第4种：不处理,也不用await,会抛出异常,但是<asynchronous suspension>找不到调用来源代码的行号信息</span>
    _channel.invokeMethod(<span class="hljs-string">'getPlatformVersion'</span>);

    <span class="hljs-comment">// 第5种: 默认不处理异常,但是用await,并且<asynchronous suspension>可以找到来源行号信息</span>
    <span class="hljs-keyword">await</span> _channel.invokeMethod(<span class="hljs-string">'getPlatformVersion'</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">"test"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是（看图）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c91a88e944841a2b08f81502aa1561f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是：</p>
<ul>
<li>第1种，是错误的，catch块永远不会调用到，且future变量的type是<code>Future<dynamic></code></li>
<li>第2种，是正确的，拿到future对象并对它做了await操作，此时catch可以正常捕获</li>
<li>第3种，是正确的，onError是Future的一个方法，可以在内部抛出异常的时候，转成异常处理的lambda函数，并且此时这个异常从unhandled转换成handled状态</li>
<li>第4种，是不推荐的，不用await且不做异常处理，直接在日志中抛出如下异常：</li>
</ul>
<pre><code class="copyable">com.eggfly.flutter_plugin_demo_example E/flutter: [ERROR:flutter/lib/ui/ui_dart_state.cc(186)] Unhandled Exception: MissingPluginException(No implementation found for method getPlatformVersion on channel flutter_plugin_demo)
    #0      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:156:7)
    <asynchronous suspension>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且注意到，这种异常的里面，是没有调用来源信息的（没有调用地方的行号，只有platform_channel.dart的行号）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/900e4096b6ea474ba9576091549f7b6c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第5种，是不推荐的，使用了await但是没有onError或者try-catch做异常处理，遇到异常可能日志会出现如下异常信息：</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">com.eggfly.flutter_plugin_demo_example E/flutter: [ERROR:flutter/lib/ui/ui_dart_state.cc(<span class="hljs-number">186</span>)] Unhandled Exception: MissingPluginException(No implementation found <span class="hljs-keyword">for</span> method getPlatformVersion <span class="hljs-keyword">on</span> channel flutter_plugin_demo)

    #<span class="hljs-number">0</span>      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:<span class="hljs-number">156</span>:<span class="hljs-number">7</span>)

    <asynchronous suspension>

    #<span class="hljs-number">1</span>      FlutterPluginDemo.platformVersion (package:flutter_plugin_demo/flutter_plugin_demo.dart:<span class="hljs-number">35</span>:<span class="hljs-number">5</span>)

    <asynchronous suspension>

    #<span class="hljs-number">2</span>      _MyAppState.initPlatformState (package:flutter_plugin_demo_example/main.dart:<span class="hljs-number">30</span>:<span class="hljs-number">25</span>)

    <asynchronous suspension>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42af8bf43b934eceb3e10bf5cef99ccb~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意到这种使用了await的情况下，里面是有嵌套的异步调用信息的。这里对于解决Dart异常会有很大帮助。</p>
<h1 data-id="heading-3">解决方法</h1>
<ul>
<li>webview_flutter的Dart异常可以改成：</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// try catch cannot catch exceptions using Future</span>
_webViewController.evaluateJavascript(js).catchError((e) &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：在evaluateJavascript的这里的场景下catchError暂时不做其他处理；</p>
<p>在其他场景下，可以根据具体exception的类型做区分，并相应处理或者re-throw出来。</p>
<h1 data-id="heading-4">参考 & read more:</h1>
<ul>
<li>官方文档： <a href="https://dart.cn/guides/libraries/futures-error-handling" target="_blank" rel="nofollow noopener noreferrer">Future 和错误处理</a></li>
</ul></div>  
</div>
            