
---
title: 'flutter 资源管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fbea477e934a068bceaa5a0759e806~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 02:21:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fbea477e934a068bceaa5a0759e806~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Flutter APP安装包中会包含代码和assets(资源)两部分.Assets是会被打包到程序安装包中的,可在运行时访问.常见类型的assets包括静态数据(例如json文件),配置文件,图标和图片(JPEG,WebP,GIF,动画WebP/GIF,PNG,BMP和WEMP)等</p>
<h2 data-id="heading-0">指定assets</h2>
<p>和包管理一样,Flutter也是有<code>pubspec.yaml</code>文件来管理应用程序所需的资源,举个例子:</p>
<pre><code class="copyable">flutter:
  assets:
    - assets/my_icon.png
    - assets/background.png
<span class="copy-code-btn">复制代码</span></code></pre>
<p>assets指定应包含在应用程序中的文件， 每个asset都通过相对于pubspec.yaml文件所在的文件系统路径来标识自身的路径。asset的声明顺序是无关紧要的，asset的实际目录可以是任意文件夹（在本示例中是assets文件夹）。</p>
<h2 data-id="heading-1">加载文本assets</h2>
<ul>
<li>通过<code>rootBundle</code>对象加载：每个Flutter应用程序都有一个<code>rootBundle</code>对象， 通过它可以轻松访问主资源包，直接使用<code>package:flutter/services.dart</code>中全局静态的<code>rootBundle</code>对象来加载<code>asset</code>即可。</li>
<li>通过 <code>DefaultAssetBundle</code>加载：建议使用 <code>DefaultAssetBundle</code>来获取当前<code>BuildContext</code>的<code>AssetBundle</code>。 这种方法不是使用应用程序构建的默认<code>asset bundle</code>，而是使父级widget在运行时动态替换的不同的<code>AssetBundle</code>，这对于本地化或测试场景很有用。</li>
</ul>
<p>通常，可以使用<code>DefaultAssetBundle.of()</code>在应用运行时来间接加载<code>asset</code>（例如JSON文件），而在widget上下文之外，或其它<code>AssetBundle</code>句柄不可用时，可以使用<code>rootBundle</code>直接加载这些<code>asset</code>，例如：</p>
<pre><code class="copyable">import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;

Future<String> loadAsset() async &#123;
  return await rootBundle.loadString('assets/config.json');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">加载图片</h2>
<p>类似于原生开发，Flutter也可以为当前设备加载适合其分辨率的图像。</p>
<h3 data-id="heading-3">声明分辨率相关的图片 assets</h3>
<p><code>AssetImage</code>可以将asset的请求逻辑映射到最接近当前设备像素比例（dpi）的asset。为了使这种映射起作用，必须根据特定的目录结构来保存asset：</p>
<pre><code class="copyable">…/image.png
…/Mx/image.png
…/Nx/image.png
…etc.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中M和N是数字标识符，对应于其中包含的图像的分辨率，也就是说，它们指定不同设备像素比例的图片。
主资源默认对应于1.0倍的分辨率图片。看一个例子：</p>
<pre><code class="copyable">…/my_icon.png
…/2.0x/my_icon.png
…/3.0x/my_icon.png
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在设备像素比率为1.8的设备上，<code>.../2.0x/my_icon.png</code> 将被选择。对于2.7的设备像素比率，<code>.../3.0x/my_icon.png</code>将被选择。</p>
<p>如果未在<code>Image widget</code>上指定渲染图像的宽度和高度，那么<code>Image widget</code>将占用与主资源相同的屏幕空间大小。 也就是说，如果<code>.../my_icon.png</code>是72px乘72px，那么<code>.../3.0x/my_icon.png</code>应该是216px乘216px; 但如果未指定宽度和高度，它们都将渲染为72像素×72像素（以逻辑像素为单位）。</p>
<p><code>pubspec.yaml</code>中asset部分中的每一项都应与实际文件相对应，但主资源项除外。当主资源缺少某个资源时，会按分辨率从低到高的顺序去选择 ，也就是说1x中没有的话会在2x中找，2x中还没有的话就在3x中找。</p>
<h3 data-id="heading-4">加载图片</h3>
<p>要加载图片，可以使用 <code>AssetImage</code>类。例如，我们可以从上面的asset声明中加载背景图片：</p>
<pre><code class="copyable">Widget build(BuildContext context) &#123;
  return new DecoratedBox(
    decoration: new BoxDecoration(
      image: new DecorationImage(
        image: new AssetImage('graphics/background.png'),
      ),
    ),
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>AssetImage</code> 并非是一个widget， 它实际上是一个<code>ImageProvider</code>，有些时候你可能期望直接得到一个显示图片的widget，那么你可以使用<code>Image.asset()</code>方法，如：</p>
<pre><code class="copyable">Widget build(BuildContext context) &#123;
  return Image.asset('graphics/background.png');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用默认的 <code>asset bundle</code> 加载资源时，内部会自动处理分辨率等，这些处理对开发者来说是无感知的。 (如果使用一些更低级别的类，如 <code>ImageStream</code>或 <code>ImageCache</code>时你会注意到有与缩放相关的参数)</p>
<h2 data-id="heading-5">特定平台 assets</h2>
<p>上面的资源都是flutter应用中的，这些资源只有在Flutter框架运行之后才能使用，如果要给我们的应用设置APP图标或者添加启动图，那我们必须使用特定平台的assets。</p>
<h3 data-id="heading-6">设置APP图标</h3>
<p>更新Flutter应用程序启动图标的方式与在本机Android或iOS应用程序中更新启动图标的方式相同。</p>
<ul>
<li>Android</li>
</ul>
<p>在Flutter项目的根目录中，导航到<code>.../android/app/src/main/res</code>目录，里面包含了各种资源文件夹（如<code>mipmap-hdpi</code>已包含占位符图像“<code>ic_launcher.png</code>”）。 只需按照Android开发人员指南中的说明， 将其替换为所需的资源，并遵守每种屏幕密度（dpi）的建议图标大小标准。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fbea477e934a068bceaa5a0759e806~tplv-k3u1fbpfcp-watermark.image" alt="2-8.89d0af83.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意: 如果您重命名.png文件，则还必须在您<code>AndroidManifest.xml</code>的标签的android:icon属性中更新名称。</p>
</blockquote>
<ul>
<li>iOS</li>
</ul>
<p>在Flutter项目的根目录中，导航到<code>.../ios/Runner</code>。该目录中<code>Assets.xcassets/AppIcon.appiconset</code>已经包含占位符图片， 只需将它们替换为适当大小的图片，保留原始文件名称。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64cb210fcffa4011a9bc42a6d22fdde6~tplv-k3u1fbpfcp-watermark.image" alt="2-9.0a86cf44.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">更新启动页</h3>
<p>在Flutter框架加载时，Flutter会使用本地平台机制绘制启动页。此启动页将持续到Flutter渲染应用程序的第一帧时。</p>
<ul>
<li>Android</li>
</ul>
<p>要将启动屏幕（splash screen）添加到您的Flutter应用程序， 请导航至<code>.../android/app/src/main</code>。在<code>res/drawable/launch_background.xml</code>，通过自定义drawable来实现自定义启动界面（你也可以直接换一张图片）。</p>
<ul>
<li>iOS</li>
</ul>
<p>要将图片添加到启动屏幕（splash screen）的中心，请导航至.../ios/Runner。在<code>Assets.xcassets/LaunchImage.imageset</code>， 拖入图片，并命名为LaunchImage.png、<a href="mailto:LaunchImage@2x.png">LaunchImage@2x.png</a>、<a href="mailto:LaunchImage@3x.png">LaunchImage@3x.png</a>。 如果你使用不同的文件名，那您还必须更新同一目录中的Contents.json文件，图片的具体尺寸可以查看苹果官方的标准。</p>
<p>您也可以通过打开Xcode完全自定义storyboard。在<code>Project Navigator</code>中导航到<code>Runner/Runner</code>然后通过打开<code>Assets.xcassets</code>拖入图片，或者通过在<code>LaunchScreen.storyboard</code>中使用<code>Interface Builder</code>进行自定义</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a602d051502d4c0e8cb60c4852acadb3~tplv-k3u1fbpfcp-watermark.image" alt="2-11.9f54d13a.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            