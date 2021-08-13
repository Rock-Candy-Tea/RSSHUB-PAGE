
---
title: 'Flutter应用进行自动化测试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986c751c74d94908916d604997455a17~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 20:25:28 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986c751c74d94908916d604997455a17~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>开发过程中，我们都会有一个很重要的环节，那就是测试。Flutter开发也一样，我们当我们完成了应用的开发之后，需要对我们的软件进行测试。市面上也有很多可以用于测试的一些自动化的软件。在这里介绍一下flutter自带的测试，我们可以通过这个插件，对我们的整个应用进行自动化的测试。</p>
<h2 data-id="heading-1">运行环境</h2>
<pre><code class="hljs language-bash copyable" lang="bash">[√] Flutter (Channel stable, 2.2.3, on Microsoft Windows [Version 10.0.19042.1110], locale zh-CN)
    • Flutter version 2.2.3 at D:\flutter
    • Framework revision f4abaa0735 (6 weeks ago), 2021-07-01 12:46:11 -0700
    • Engine revision 241c87ad80
    • Dart version 2.13.4
    • Pub download mirror https://pub.flutter-io.cn
    • Flutter download mirror https://storage.flutter-io.cn
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">安装依赖</h2>
<p>首先，我们需要安装<code>flutter_driver</code>插件。安装完成以后，我们在项目中新建一个文件夹（我的文件名是<code>test_driver</code>自己定义文件夹名字）。这个文件夹就用于我们的测试代码的编写。</p>
<pre><code class="hljs language-bash copyable" lang="bash">dev_dependencies:
  flutter_driver:
    sdk: flutter
  <span class="hljs-built_in">test</span>: any
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">代码编写</h2>
<p>我要写的一个测试代码，就是我要通过代码去找到我需要的组件，比如按钮，我需要去点击它。滑动列表我需要往下划动到第多少页。然后我再往回划，切换到下一个页面，如此循环的。按照我们人类思维的流程，把整个项目全部模拟操作。</p>
<h4 data-id="heading-4"><code>app.dart</code>测试入口文件</h4>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter_driver/driver_extension.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:dynamic_theme/main.dart'</span> <span class="hljs-keyword">as</span> app;

<span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-comment">// This line enables the extension.</span>
  enableFlutterDriverExtension();

  <span class="hljs-comment">// Call the `main()` function of the app, or call `runApp` with</span>
  <span class="hljs-comment">// any widget you are interested in testing.</span>
  app.main();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><code>app_test.dart</code>执行需要测试模块</h4>
<p>我写了<code>entrance</code>的文件模块，里面包含了页面点击滚动的模拟事件，如果需要全模块的测试可以在<code>main</code>函数加多个<code>group</code>需要测试某个功能也可以按需测试。</p>
<pre><code class="copyable">import 'package:test/test.dart';

import 'entrance.dart';

void main() &#123;
  group('切换导航滑动页面', entrance);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><code>entrance.dart</code>模拟测试脚本</h4>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter_driver/flutter_driver.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:test/test.dart'</span>;

<span class="hljs-keyword">void</span> entrance() &#123;
  <span class="hljs-keyword">late</span> FlutterDriver driver;
  <span class="hljs-comment">// Connect to the Flutter driver before running any tests.</span>
  setUpAll(() <span class="hljs-keyword">async</span> &#123;
    driver = <span class="hljs-keyword">await</span> FlutterDriver.connect();
  &#125;);
  <span class="hljs-comment">// Close the connection to the driver after the tests have completed.</span>
  tearDownAll(() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> driver.close();
  &#125;);
<span class="hljs-comment">// test('starts at 0', () async &#123;</span>
<span class="hljs-comment">// Use the `driver.getText` method to verify the counter starts at 0.</span>
<span class="hljs-comment">// expect(await driver.getText(counterTextFinder), '0');</span>
<span class="hljs-comment">//    &#125;);</span>

  test(<span class="hljs-string">'切换页面'</span>, () <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">2</span>));
    <span class="hljs-keyword">await</span> driver.tap(find.byValueKey(<span class="hljs-string">'tab_3'</span>));
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">5</span>));
    <span class="hljs-keyword">await</span> driver.tap(find.byValueKey(<span class="hljs-string">'tab_2'</span>));
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">5</span>));
    <span class="hljs-keyword">await</span> driver.tap(find.byValueKey(<span class="hljs-string">'tab_1'</span>));
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">5</span>));
    <span class="hljs-keyword">await</span> driver.tap(find.byValueKey(<span class="hljs-string">'tab_0'</span>));
  &#125;);

  test(<span class="hljs-string">'滑动页面到底部'</span>, () <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> driver.runUnsynchronized(() <span class="hljs-keyword">async</span> &#123;
      <span class="hljs-keyword">final</span> listFinder = find.byValueKey(<span class="hljs-string">'message_list'</span>);
      <span class="hljs-keyword">final</span> itemFinder = find.byValueKey(<span class="hljs-string">'item_78'</span>);
      <span class="hljs-keyword">await</span> driver.scrollUntilVisible(
        listFinder,
        itemFinder,
        dyScroll: <span class="hljs-number">-300.0</span>,
      );
    &#125;);
  &#125;);

  test(<span class="hljs-string">'滑动页面到顶部'</span>, () <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> driver.runUnsynchronized(() <span class="hljs-keyword">async</span> &#123;
      <span class="hljs-keyword">final</span> listFinder = find.byValueKey(<span class="hljs-string">'message_list'</span>);
      <span class="hljs-keyword">final</span> itemFinder = find.byValueKey(<span class="hljs-string">'item_1'</span>);
      <span class="hljs-keyword">await</span> driver.scrollUntilVisible(
        listFinder,
        itemFinder,
        dyScroll: <span class="hljs-number">300.0</span>,
      );
    &#125;);
  &#125;);

  test(<span class="hljs-string">'跳转页面'</span>, () <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-comment">// First, tap the button.</span>
    <span class="hljs-keyword">await</span> driver.tap(find.byValueKey(<span class="hljs-string">'jump_list'</span>));

    <span class="hljs-comment">// Then, verify the counter text is incremented by 1.</span>
    expect(<span class="hljs-keyword">await</span> driver.getText(find.byValueKey(<span class="hljs-string">'title'</span>)), <span class="hljs-string">'NewList-路由传参'</span>);
  &#125;);

  test(<span class="hljs-string">'返回页面'</span>, () <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">5</span>));
    <span class="hljs-keyword">final</span> buttonFinder = find.byValueKey(<span class="hljs-string">'back'</span>);
    <span class="hljs-comment">// First, tap the button.</span>
    <span class="hljs-keyword">await</span> driver.tap(buttonFinder);

    <span class="hljs-comment">// Then, verify the counter text is incremented by 1.</span>
    <span class="hljs-comment">// expect(await driver.getText(counterTextFinder), '1');</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">怎样找到我们需要的组件？</h3>
<p>测试脚本使用<code>find.byValueKey('key的名称')</code>来找到我们需要的组件，找到以后我们可以进行点击、滚动、双击等模拟操作。这里我使用的是<code>find.byValueKey</code>方法，下面介绍它的使用。</p>
<h3 data-id="heading-8">找到滚动列表，滚动某个位置</h3>
<p>首先我们要找到我们需要滑动的列表，我<code>find.byValueKey</code>这个方法去找到滑动组件，在开始写业务代码的时候我已经加了一个<code>key</code>名称是<code>message_list</code>。<code>key</code>不要重复避免查找组件出现问题。</p>
<h4 data-id="heading-9">业务代码</h4>
<pre><code class="copyable">EasyRefresh.custom(
  key: Key('message_list'),
  enableControlFinishRefresh: true,
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">测试代码例子</h4>
<p><code>driver.scrollUntilVisible</code>模拟滑动，<code>itemFinder</code>参数表示滑动到<code>key:item_78</code>这个元素的时候就不滑动了，接下来每次滑动300像素。</p>
<pre><code class="hljs language-dart copyable" lang="dart">test(<span class="hljs-string">'滑动页面到底部'</span>, () <span class="hljs-keyword">async</span> &#123;
  <span class="hljs-keyword">await</span> driver.runUnsynchronized(() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> listFinder = find.byValueKey(<span class="hljs-string">'message_list'</span>);
    <span class="hljs-keyword">final</span> itemFinder = find.byValueKey(<span class="hljs-string">'item_78'</span>);
    <span class="hljs-keyword">await</span> driver.scrollUntilVisible(
      listFinder,
      itemFinder,
      dyScroll: <span class="hljs-number">-300.0</span>,
    );
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs-flutter-io.firebaseapp.com%2Fflutter%2Fflutter_driver%2FFlutterDriver-class.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver-class.html" ref="nofollow noopener noreferrer"><code>driver</code>支持的方法</a></h4>
<pre><code class="hljs language-dart copyable" lang="dart">-   [checkHealth](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/checkHealth.html)(​&#123;[Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[Health](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/Health-class.html)></span>

-   Checks the status of the Flutter Driver <span class="hljs-keyword">extension</span>.

-   [clearTimeline](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/clearTimeline.html)(​&#123;[Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout: _kUnusuallyLongTimeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Clears all timeline events recorded up until now. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/clearTimeline.html)</span>

-   [close](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/close.html)(​) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Closes the underlying connection to the VM service. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/close.html)</span>

-   [enterText](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/enterText.html)(​[String](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/String-class.html) text, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Enters `text` into the currently focused text input, such <span class="hljs-keyword">as</span> the [EditableText](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/widgets/EditableText-class.html) widget. [[...]](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/enterText.html)</span>

-   [forceGC](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/forceGC.html)(​) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Force a garbage collection run <span class="hljs-keyword">in</span> the VM.

-   [getRenderTree](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getRenderTree.html)(​&#123;[Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[RenderTree](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/RenderTree-class.html)></span>

-   Returns a dump of the render tree.

-   [getSemanticsId](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getSemanticsId.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[int](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/int-class.html)></span>

-   Retrieves the semantics node id <span class="hljs-keyword">for</span> the object returned by `finder`, or the nearest ancestor <span class="hljs-keyword">with</span> a semantics node. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getSemanticsId.html)</span>

-   [getText](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getText.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[String](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/String-class.html)></span>

-   Returns the text <span class="hljs-keyword">in</span> the `Text` widget located by `finder`.

-   [getVmFlags](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getVmFlags.html)(​) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[List](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/List-class.html)<​[Map](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Map-class.html)<​[String](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/String-class.html), dynamic>>></span>

-   Returns the Flags <span class="hljs-keyword">set</span> <span class="hljs-keyword">in</span> the Dart VM <span class="hljs-keyword">as</span> JSON. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/getVmFlags.html)</span>

-   [requestData](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/requestData.html)(​[String](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/String-class.html) message, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[String](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/String-class.html)></span>

-   Sends a string and returns a string. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/requestData.html)</span>

-   [runUnsynchronized](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/runUnsynchronized.html)<​T>(​[Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​T> action(), &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​T></span>

-   `action` will be executed <span class="hljs-keyword">with</span> the frame <span class="hljs-keyword">sync</span> mechanism disabled. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/runUnsynchronized.html)</span>

-   [screenshot](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/screenshot.html)(​) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[List](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/List-class.html)<​[int](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/int-class.html)>></span>

-   Take a screenshot. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/screenshot.html)</span>

-   [scroll](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scroll.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) dx, [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) dy, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) duration, &#123; [int](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/int-class.html) frequency: 60, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Tell the driver to perform a scrolling action. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scroll.html)</span>

-   [scrollIntoView](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scrollIntoView.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) alignment: 0.0, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Scrolls the Scrollable ancestor of the widget located by `finder` until the widget <span class="hljs-keyword">is</span> completely visible. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scrollIntoView.html)</span>

-   [scrollUntilVisible](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scrollUntilVisible.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) scrollable, [SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) item, &#123; [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) alignment: 0.0, [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) dxScroll: 0.0, [double](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/double-class.html) dyScroll: 0.0, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Repeatedly [scroll](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scroll.html) the widget located by `scrollable` by `dxScroll` and `dyScroll` until `item` is visible, and then use [scrollIntoView](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scrollIntoView.html) to ensure the item's final position matches `alignment`. [[...]](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/scrollUntilVisible.html)</span>

-   [setSemantics](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/setSemantics.html)(​[bool](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/bool-class.html) enabled, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[bool](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/bool-class.html)></span>

-   Turns semantics <span class="hljs-keyword">on</span> or off <span class="hljs-keyword">in</span> the Flutter app under test. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/setSemantics.html)</span>

-   [setTextEntryEmulation](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/setTextEntryEmulation.html)(​&#123;[bool](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/bool-class.html) enabled, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Configures text entry emulation. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/setTextEntryEmulation.html)</span>

-   [startTracing](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/startTracing.html)(​&#123;[List](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/List-class.html)<​[TimelineStream](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/TimelineStream-class.html)> streams: _defaultStreams, [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout: _kUnusuallyLongTimeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Starts recording performance traces. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/startTracing.html)</span>

-   [stopTracingAndDownloadTimeline](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/stopTracingAndDownloadTimeline.html)(​&#123;[Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout: _kUnusuallyLongTimeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[Timeline](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/Timeline-class.html)></span>

-   Stops recording performance traces and downloads the timeline. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/stopTracingAndDownloadTimeline.html)</span>

-   [tap](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/tap.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Taps at the center of the widget located by `finder`.

-   [traceAction](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/traceAction.html)(​[Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html) action(), &#123; [List](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/List-class.html)<​[TimelineStream](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/TimelineStream-class.html)> streams: _defaultStreams, [bool](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/bool-class.html) retainPriorEvents: false &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​[Timeline](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/Timeline-class.html)></span>

-   Runs `action` and outputs a performance trace <span class="hljs-keyword">for</span> it. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/traceAction.html)</span>

-   [waitFor](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/waitFor.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Waits until `finder` locates the target.

-   [waitForAbsent](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/waitForAbsent.html)(​[SerializableFinder](https://docs-flutter-io.firebaseapp.com/flutter/flutter_driver/SerializableFinder-class.html) finder, &#123; [Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Waits until `finder` can no longer locate the target.

-   [waitUntilNoTransientCallbacks](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/waitUntilNoTransientCallbacks.html)(​&#123;[Duration](https://docs-flutter-io.firebaseapp.com/flutter/dart-core/Duration-class.html) timeout &#125;) → [Future](https://docs-flutter-io.firebaseapp.com/flutter/dart-async/Future-class.html)<​void></span>

-   Waits until there are no more transient callbacks <span class="hljs-keyword">in</span> the queue. [[...]](https:<span class="hljs-comment">//docs-flutter-io.firebaseapp.com/flutter/flutter_driver/FlutterDriver/waitUntilNoTransientCallbacks.html)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><code>find</code>方法支持的查找方式<code>find.text</code> <code>find.byValueKey</code> <code>find.bySemanticsLabel</code> <code>find.pageBack</code> <code>find.byType</code></h4>
<pre><code class="copyable">SerializableFinder text(String text) => ByText(text);

/// Finds widgets by [key]. Only [String] and [int] values can be used.
SerializableFinder byValueKey(dynamic key) => ByValueKey(key);

/// Finds widgets with a tooltip with the given [message].
SerializableFinder byTooltip(String message) => ByTooltipMessage(message);

/// Finds widgets with the given semantics [label].
SerializableFinder bySemanticsLabel(Pattern label) => BySemanticsLabel(label);

/// Finds widgets whose class name matches the given string.
SerializableFinder byType(String type) => ByType(type);

/// Finds the back button on a Material or Cupertino page's scaffold.
SerializableFinder pageBack() => const PageBack();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">run <code>flutter drive --target=test_driver/app.dart</code></h2>
<p>现在我们已经写好了自动化测试脚本run <code>flutter drive --target=test_driver/app.dart</code>命令，会在控制台上面看到很多输出的信息，说明已经开始自动化测试了，最后我们会看到控制台输出了<code>All tests passed!</code>的说明已经测试成功了。</p>
<h2 data-id="heading-14">测试模拟</h2>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986c751c74d94908916d604997455a17~tplv-k3u1fbpfcp-watermark.image" width="320" loading="lazy" referrerpolicy="no-referrer">
</div>
<h2 data-id="heading-15">测试输出</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3611fc878844a8c84a7a951aa4223c5~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-08-11 18.19.35.2021-08-11 18_27_12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-bash copyable" lang="bash">D:\project\dynamic_theme>flutter drive --target=test_driver/app.dart
Running <span class="hljs-string">"flutter pub get"</span> <span class="hljs-keyword">in</span> dynamic_theme...                    1,399ms
Running Gradle task <span class="hljs-string">'assembleDebug'</span>...
Running Gradle task <span class="hljs-string">'assembleDebug'</span>... Done                        28.3s
√  Built build\app\outputs\flutter-apk\app-debug.apk.
Installing build\app\outputs\flutter-apk\app.apk...                803ms
00:00 +0: 切换导航滑动页面 (setUpAll)

VMServiceFlutterDriver: Connecting to Flutter application at http://127.0.0.1:62607/4xhdHTUuf_U=/
VMServiceFlutterDriver: Isolate found with number: 3474149526286947
VMServiceFlutterDriver: Isolate is paused at start.
VMServiceFlutterDriver: Attempting to resume isolate
I/flutter ( 2384): debug版本--KK
VMServiceFlutterDriver: Connected to Flutter application.
00:02 +0: 切换导航滑动页面 切换页面

I/flutter ( 2384): initial link:
I/flutter ( 2384): initialLink--
00:20 +1: 切换导航滑动页面 滑动页面到底部

VMServiceFlutterDriver: waitFor message is taking a long time to complete...
00:39 +2: 切换导航滑动页面 滑动页面到顶部

VMServiceFlutterDriver: waitFor message is taking a long time to complete...
00:52 +3: 切换导航滑动页面 跳转页面

I/flutter ( 2384): 进入NewView
I/flutter ( 2384): _NewViewState<span class="hljs-comment">#0c082(lifecycle state: initialized)</span>
00:53 +4: 切换导航滑动页面 返回页面

I/flutter ( 2384): 数据传参
00:58 +5: 切换导航滑动页面 (tearDownAll)

00:58 +5: All tests passed!  -
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTecode%2Fdynamic_theme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Tecode/dynamic_theme" ref="nofollow noopener noreferrer">项目地址</a></h2>
<p>到这里就已经结束，感兴趣的小伙伴可以去下载源码体验。如果不能运行请先检查flutter的版本。</p></div>  
</div>
            