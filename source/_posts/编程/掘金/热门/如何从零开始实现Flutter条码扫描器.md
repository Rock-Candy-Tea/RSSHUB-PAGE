
---
title: '如何从零开始实现Flutter条码扫描器'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a95fc2e019498487524eea84006ab2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 21:33:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a95fc2e019498487524eea84006ab2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大约两年前，我写了一篇文章，分享了如何用<a href="https://www.dynamsoft.com/barcode-reader/overview/" target="_blank" rel="nofollow noopener noreferrer">Dynamsoft Barcode Reader</a>一步步建立一个<a href="https://www.dynamsoft.com/codepool/flutter-barcode-plugin.html" target="_blank" rel="nofollow noopener noreferrer">Flutter条码插件</a>。那时候，Flutter还在开发中，只支持Android和iOS。如今，谷歌已经发布了Flutter 2，它允许开发者从一个代码库中为移动、网络和桌面构建应用程序。如果你想构建跨平台的应用程序，那么从现在开始，值得在Flutter上投入很多精力。由于新的Flutter与旧的Flutter不兼容，我决定重构Flutter条码插件的API，并添加一个新的方法来支持实时的视频流条码扫描。</p>
<h2 data-id="heading-0">Flutter条码SDK插件</h2>
<p>在下面的段落中，我将演示如何开发一个支持从图像文件和图像缓冲区读取条形码的Flutter条形码插件，以及如何将该插件发布到pub.dev。</p>
<h3 data-id="heading-1">使用Dynamsoft条码阅读器开发Flutter条码SDK插件</h3>
<p>我目前的计划是使该插件适用于Android。因此，我创建了如下的插件包。</p>
<pre><code class="copyable">flutter create --org com.dynamsoft --template=plugin --platforms=android -a java flutter_barcode_sdk
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了在插件项目中添加其他平台的代码，如iOS，我可以运行。</p>
<pre><code class="copyable">flutter create --template=plugin --platforms=ios .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件的API是在<code>lib/flutter_barcode_sdk.dart</code> 文件中定义的，它是Dart代码和平台特定代码之间的桥梁。一个<code>android/src/main/java/com/dynamsoft/flutter_barcode_sdk/FlutterBarcodeSdkPlugin.java</code> 文件被生成，作为Android的入口点。</p>
<h3 data-id="heading-2"><em>Dart代码</em></h3>
<p>让我们开始使用<code>lib/flutter_barcode_sdk.dart</code> 。</p>
<p>第一步是定义一个<code>BarcodeResult</code> 类，它包含条形码格式、结果和坐标点，用于反序列化从平台特定代码返回的JSON数据。</p>
<p>为图片和视频流场景分别创建方法<code>decodeFile()</code> 和<code>decodeImageBuffer()</code> 。</p>
<p><code>_convertResults()</code> 函数用于将<code>List<Map<dynamic, dynamic>></code> 类型转换为<code><List<BarcodeResult>></code> 类型。</p>
<h3 data-id="heading-3"><em>Java代码</em></h3>
<p>当调用Flutter API时，将触发Android<code>onMethodCall()</code> 函数。</p>
<p>以下是特定平台代码的基本步骤。</p>
<ol>
<li>从Dart框架中提取参数。</li>
<li>处理图像数据。</li>
<li>返回结果。</li>
</ol>
<p><code>decodeImageBuffer</code> 方法是为相机流设计的。为了避免阻塞主线程，我使用<code>SingleThreadExectuor</code> ，在一个工作线程中处理CPU密集型工作。</p>
<h3 data-id="heading-4">发布 Flutter Barcode SDK 插件到 Pub.dev</h3>
<p>在发布插件之前，你最好通过运行命令来分析。</p>
<pre><code class="copyable">flutter pub publish --dry-run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有错误，您可以将包发布到pub.dev。</p>
<pre><code class="copyable">flutter pub publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我已经成功发布了Flutter条码SDK到<a href="https://pub.dev/packages/flutter_barcode_sdk" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/fl…</a>。</p>
<p>插件完成后，是时候用几行Dart代码建立一个条码扫描器应用了。</p>
<p>首先，我将Flutter相机插件和flutter_barcode_sdk添加到<code>pubspec.yaml</code> 文件中。</p>
<p>然后，在<code>main.dart</code> 中初始化相机和条码阅读器对象。</p>
<p>该应用程序由一个相机视图、一个文本小部件和两个按钮小部件组成。</p>
<p>在<code>videoScan()</code> 函数中，我调用<a href="https://pub.dev/documentation/camera/latest/camera/CameraController/startImageStream.html" target="_blank" rel="nofollow noopener noreferrer">startImageStream()</a>来持续获得最新的视频帧并调用条码解码API。</p>
<p><code>pictureScan()</code> 函数从图像中读取条形码，并在<a href="https://flutter.dev/docs/cookbook/plugins/picture-using-camera" target="_blank" rel="nofollow noopener noreferrer">图片屏幕</a>上显示图像和结果。</p>
<p>最后，我可以建立并运行该应用程序。</p>
<pre><code class="copyable">flutter run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对Raspberry Pi包装盒上的一维条码和二维码进行识别测试。</p>
<h3 data-id="heading-5"><strong>视频条码扫描</strong></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a95fc2e019498487524eea84006ab2~tplv-k3u1fbpfcp-zoom-1.image" alt="flutter barcode scanner" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6"><strong>图片条码扫描</strong></h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/262db518c14942eda8459473bbf1e924~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">前提条件</h2>
<p>iOS, Web, 和Windows。</p>
<h2 data-id="heading-8">源代码</h2>
<p><a href="https://github.com/yushulx/flutter_barcode_sdk" target="_blank" rel="nofollow noopener noreferrer">github.com/yushulx/flu…</a></p></div>  
</div>
            