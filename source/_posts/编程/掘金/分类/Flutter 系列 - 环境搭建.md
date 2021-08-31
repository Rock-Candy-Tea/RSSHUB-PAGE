
---
title: 'Flutter 系列 - 环境搭建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f00d6d97b64baca65be10890698e43~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 17:33:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f00d6d97b64baca65be10890698e43~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/" ref="nofollow noopener noreferrer">Flutter</a> 作为火热的跨端工具包，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter" ref="nofollow noopener noreferrer">github</a> 上超过 <strong>120k</strong> 的关注量，可见一斑。</p>
<p>基于目前本人正在学习 <code>Flutter</code> 的路上，会将整个学习的过程记录下来。</p>
<p>本博文主要讲解<code>环境的搭建</code>，先把项目搭建好，跑通 <code>demo</code> 才有玩下去的必要和成就感，你说是吧？</p>
<h3 data-id="heading-0">本人开发环境</h3>
<ul>
<li>
<p>macOS Big Sur 版本 11.2 芯片 Apple M1</p>
</li>
<li>
<p>磁盘空间：> 2.8 GB （要求的最小的空间）</p>
</li>
<li>
<p>$SHELL</p>
</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">echo</span> <span class="hljs-variable">$SHELL</span>
/bin/bash
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>⚠️ 之后出现并解决的问题都是基于本人的环境</p>
</blockquote>
<h3 data-id="heading-1">安装 Flutter</h3>
<p>通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2Fdocs%2Fget-started%2Finstall%2Fmacos%23get-sdk" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/docs/get-started/install/macos#get-sdk" ref="nofollow noopener noreferrer">官网</a>下载安装包。</p>
<p>将安装包放到自己想存放的地方。这里，我放在 <code>文稿 -> sdk</code> 方便管理，然后解压下载包。</p>
<p>配置 <code>flutter</code> 的 <code>PATH</code> 环境变量，格式如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$&#123;pwd&#125;</span>/flutter/bin
或
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$&#123;pwd&#125;</span>/flutter/bin:<span class="hljs-variable">$PATH</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我需要编辑 <code>~/.bash_profile</code> 文件，添加下面这行内容：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">export</span> PATH=/Users/jimmy/Documents/sdk/flutter/bin:<span class="hljs-variable">$PATH</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">安装 IDE</h3>
<p>作为一个前端开发者，比较偏向 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/" ref="nofollow noopener noreferrer">VS code</a>，直接安装其稳定版即可。</p>
<p>因为需要调试安卓平台，还需要安装编辑器 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.google.cn/studio" ref="nofollow noopener noreferrer">Android Studio</a>。 <code>Android Studio</code> 为 <code>Flutter</code> 提供了一个完整的集成开发环境。</p>
<p>不管 <code>VS code</code> 还是 <code>Android Studio</code> 都需要安装 <code>Flutter</code> 插件。</p>
<blockquote>
<p><strong>Android Studio</strong> 我还是安装在 <strong>文稿 -> sdk</strong></p>
</blockquote>
<p>注意安装android studio的路径，也许会报sdk的错误。类似错误 ❌</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># [Flutter-Unable to find bundled Java version(flutter doctor), after updated android studio Arctic Fox(2020.3.1) on M1 Apple Silicon](https://stackoverflow.com/questions/68569430/flutter-unable-to-find-bundled-java-versionflutter-doctor-after-updated-andro)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的解决方法：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F68569430%2Fflutter-unable-to-find-bundled-java-versionflutter-doctor-after-updated-andro" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/68569430/flutter-unable-to-find-bundled-java-versionflutter-doctor-after-updated-andro" ref="nofollow noopener noreferrer">flutter-unable-to-find-bundled-java-versionflutter-doctor-after-updated-andro</a></p>
<h3 data-id="heading-3">验证</h3>
<p>之后，运行 <code>flutter doctor</code> 或者 <code>flutter doctor -v</code> 来检查是否安装了必要的安装包。</p>
<p>下面是自己搭建环境的情况<code>flutter doctor -v</code>：</p>
<pre><code class="hljs language-bash copyable" lang="bash">[✓] Flutter (Channel stable, 2.2.3, on macOS 11.2 20D64 darwin-arm, locale

    zh-Hans-CN)

    • Flutter version 2.2.3 at /Users/jimmy/Documents/sdk/flutter

    • Framework revision f4abaa0735 (9 weeks ago), 2021-07-01 12:46:11 -0700

    • Engine revision 241c87ad80

    • Dart version 2.13.4

[✓] Android toolchain - develop <span class="hljs-keyword">for</span> Android devices (Android SDK version 31.0.0)

    • Android SDK at /Users/jimmy/Library/Android/sdk

    • Platform android-31, build-tools 31.0.0

    • Java binary at: /Users/jimmy/Documents/sdk/Android

      Studio.app/Contents/jre/jdk/Contents/Home/bin/java

    • Java version OpenJDK Runtime Environment (build 11.0.10+0-b96-7249189)

    • All Android licenses accepted.
    
[✓] Xcode - develop <span class="hljs-keyword">for</span> iOS and macOS

    • Xcode at /Applications/Xcode.app/Contents/Developer

    • Xcode 12.5.1, Build version 12E507

    • CocoaPods version 1.10.2

[✓] Chrome - develop <span class="hljs-keyword">for</span> the web

    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Android Studio (version 2020.3)

    • Android Studio at /Users/jimmy/Documents/sdk/Android Studio.app/Contents  <span class="hljs-comment"># 留意 Android Studio 路径</span>

    • Flutter plugin can be installed from:

      🔨 https://plugins.jetbrains.com/plugin/9212-flutter

    • Dart plugin can be installed from:

      🔨 https://plugins.jetbrains.com/plugin/6351-dart

    • Java version OpenJDK Runtime Environment (build 11.0.10+0-b96-7249189)

[✓] VS Code (version 1.59.1)

    • VS Code at /Applications/Visual Studio Code.app/Contents

    • Flutter extension version 3.25.0

[✓] Connected device (1 available)

    • Chrome (web) • chrome • web-javascript • Google Chrome 92.0.4515.159

• No issues found!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出现 <code>No issues found!</code> 的提示，说明你捣鼓成功了～</p>
<h3 data-id="heading-4">运行 Demo</h3>
<p>我们在 <code>VS code</code> 上新建一个项目：</p>
<pre><code class="hljs language-bash copyable" lang="bash">查看 -> 命令面板 -> Flutter: New Application Project
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化项目之后，<code>运行 -> 启动调试</code>，然后按照下图运行应用：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f00d6d97b64baca65be10890698e43~tplv-k3u1fbpfcp-watermark.image" alt="vscode_demo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果选中 <code>Chrome web</code> 会直接调起你安装好的谷歌浏览器。</p>
<p>如果选中 <code>Start iOS Simulator</code> 会调起 <code>xCode</code> 的模拟器。</p>
<p>如果选中 <code>Start Pixel 2 API 31</code> 会调起 <code>Android Studio</code> 的模拟器。</p>
<blockquote>
<p>当然你得在 <code>Android Studio</code> 上预设手机型号是哪个，不然初次在 <code>VS code</code> 上调不起来。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9269fa7afdb54ff291d748c3679aa676~tplv-k3u1fbpfcp-watermark.image" alt="effect_result.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>【完】～ 下次可以更加愉快玩耍了</p></div>  
</div>
            