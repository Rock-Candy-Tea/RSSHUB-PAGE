
---
title: 'flutter教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8914f570c48454e80e4c0c7cf79a203~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 22:22:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8914f570c48454e80e4c0c7cf79a203~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1:Java环境的安装</h2>
<p>JAVA环境下载地址：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Fjdk8-downloads-2133151.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html" ref="nofollow noopener noreferrer">www.oracle.com/technetwork…</a></p>
<p>配置环境变量详情见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fwindows10-java-setup.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/windows10-java-setup.html" ref="nofollow noopener noreferrer">www.runoob.com/w3cnote/win…</a></p>
<p>cmd输入java,如果出来下面这个图,表示成功
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8914f570c48454e80e4c0c7cf79a203~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2:下载安装 FlutterSDK</h2>
<p>去官网下载Flutter安装包，下载地址:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.io%2Fsdk-archive%2F%23windows" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.io/sdk-archive/#windows" ref="nofollow noopener noreferrer">flutter.io/sdk-archive…</a> ,在Flutter安装目录的flutter文件下找到flutter_console.bat，双击运行并启动flutter命令行，接下来，你就可以在Flutter命令行运行flutter命令了。</p>
<p>同样需要配置环境变量,path:D:\Program Files\flutter\bin</p>
<p>在终端中输入flutter doctor，你可能会得到下面类似的结果
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e40989b23bd4e44a19cbb77b33e9bef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这时候你得到的x比这个会多一些，因为我们还没有安装Android studio那下一步就是进行Android Studio的安装。</p>
<h2 data-id="heading-2">3:Android Studio安装</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/" ref="nofollow noopener noreferrer">developer.android.com/</a> 官网去下载,可能会很慢很慢,耐心等待</p>
<p>再点击这个小手机图标,
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4472fdb567804c6db69827de9060e179~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再添加虚拟机
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/279c76e64ab346e0afc186951a7ee4b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">4:安装Android证书</h2>
<p>命令行输入:flutter doctor --android-licenses</p>
<h2 data-id="heading-4">5:其他错误</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ded11c0d0646e48fd94cd5d230f323~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这是因为我的android sudio的安装路径不是默认的,需要flutter config --android-studio-dir="D:\Program Files\Android\Android Studio",如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d0bbd19fcff427b9fe19259b537d845~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">这样就大功告成了</p></div>  
</div>
            