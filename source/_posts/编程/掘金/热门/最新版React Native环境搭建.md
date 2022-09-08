
---
title: '最新版React Native环境搭建'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80801744b5c245b9b00163256826a152~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 24 Aug 2022 18:53:40 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80801744b5c245b9b00163256826a152~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>工欲善其事，必先利其器。搭建React Native开发环境，需要安装以下辅助工具。</p>
<ul>
<li>Node.js：React Native需要借助Node.js来创建和运行JavaScript代码。</li>
<li>原生开发工具及环境：React Native的运行需要依赖原生Android和iOS环境，因此需要分别安装原生Android和iOS的开发环境。</li>
<li>其他开发工具：代码编辑器Visual Studio Code或WebStorm，远程调试具Chrome浏览器等。</li>
</ul>
<h1 data-id="heading-0">一、基础环境</h1>
<h2 data-id="heading-1">1.1 安装Node.js</h2>
<p>首先，我们需要安装Homebrew，Homebrew是一款Mac OS平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能，Homebrew的安装命令如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">/bin/bash -c <span class="hljs-string">"<span class="hljs-subst">$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完Homebrew之后，接下来就是安装Node 、Watchman和 Yarn等必须的工具。</p>
<pre><code class="hljs language-perl copyable" lang="perl">brew install node
brew install watchman
<span class="hljs-comment"># 使用nrm工具切换淘宝源</span>
npx nrm <span class="hljs-keyword">use</span> taobao

npm install -g yarn
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，如果还在使用旧版本React Native工具（0.60.0版本以下），为了避免冲突，请使用下面的命令先卸载。
npm uninstall -g react-native-cli</p>
<h2 data-id="heading-2">1.2 添加Android原生环境</h2>
<p>由于React Native项目的编译运行需要依赖原生平台，所以在搭建React Native开发环境过程中，需要事先搭建好原生Android和iOS的开发环境。</p>
<p>在搭建原生Android开发环境过程中，由于Android项目的开发和运行需要依赖Java环境，如果还没有安装Java环境，可以从JDK官网下载操作系统对应的JDK版本然后进行安装。安装成功之后，可以使用java -version命令来验证Java开发环境，如下图所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80801744b5c245b9b00163256826a152~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，为了方便后面项目中使用Java的命令行，还需要在.bash_profile文件中配置环境变量，如下所示。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 如果你不是通过Android Studio安装的sdk，则其路径可能不同，请自行确定清楚</span>
<span class="hljs-built_in">export</span> ANDROID_HOME=/Users/XXX/Library/Android/sdk
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/tools
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/platform-tools
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/emulator
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/tools/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果配置文件使用的是~/.zshrc，那么可以使用下面的命令使上面的配置生效。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">source</span> ～/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们还需要安装Android开发工具Android Studio和Android开发套件Android SDK Tools。</p>
<p>首先，从Android官网下载最新的Android Studio，安装完成之后，第一次启动会自动下载Android SDK，下载Android SDK需要在Android Studio的设置板中配置Android SDK Tools的路径。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4844c3944fbb4c2ab70f8879d45756ac~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样，为了方便在项目中使用Android命令行工具，还需要配置一下Android系统环境变量。</p>
<pre><code class="hljs language-ini copyable" lang="ini">export <span class="hljs-attr">ANDROID_HOME</span>=<span class="hljs-string">"/Users/xxx/Android/sdk"</span>    
export <span class="hljs-attr">PATH</span>=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/tools
export <span class="hljs-attr">PATH</span>=<span class="hljs-variable">$&#123;PATH&#125;</span>:<span class="hljs-variable">$&#123;ANDROID_HOME&#125;</span>/platform-tools
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">1.3 添加iOS原生环境</h2>
<p>众所周知，开发iOS应用需要macOS操作系统支持，所以如果经济条件允许最好准备一台Mac电脑。也只有这样，才能使用React Native开发可以同时运行在iOS和Android设备上的跨平台应用，发挥React Native跨平台应用开发的优势。</p>
<p>由于使用React Native开发iOS端的应用时需要Xcode 7及更高版本的支持，如果本地还没有安装Xcode应用程序，可以从App Store上下载最新的Xcode进行安装，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97923fe8ed8e4d7088d12d469d1bd65a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要说明的是，Xcode安装程序必须通过Apple官网或者App Store进行下载，否则容易出现代码植入和代码泄漏的风险。比如，2015年9月发生的XcodeGhost非法代码植入事件，就是因为开发者使用的是非官方的Xcode安装程序引起的。</p>
<p>同时，React Native项目的原生iOS部分使用的是CocoaPods来管理第三方依赖库，所以在搭建iOS开发环境时还需要安装CocoaPods库管理工具。如果还没有安装CocoaPods，可以使用下面的命令进行安装。</p>
<pre><code class="hljs copyable">brew install cocoapods
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于React Native项目的运行需要依赖ruby的2.7.5版本，所以请确保本地已经安装了ruby依赖。如果本地安装了多个ruby版本，那么可以使用下面的命令进行切换。</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">rvm use ruby<span class="hljs-number">-2.7</span><span class="hljs-number">.5</span> --<span class="hljs-keyword">default</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">二、创建示例项目</h1>
<h2 data-id="heading-5">2.1 创建项目</h2>
<p>React Native支持使用命令和IDE集成开发工具两种方式来创建项目。其中，使用命令行方式初始化React Native项目如下所示。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">npx react-native <span class="hljs-keyword">init</span> RNDemos
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，初始化React Native项目时，项目名称不能包含中文、空格和特殊符号，也不能使用JavaScript关键字作为项目名，如 class、native、new等。
同时，React Native在初始化项目时还支持指定版本和项目模板，如下所示。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//指定版本</span>
npx react-<span class="hljs-keyword">native</span> init AwesomeProject --version <span class="hljs-number">0.66</span><span class="hljs-number">.0</span>   
<span class="hljs-comment">//指定模版</span>
npx react-<span class="hljs-keyword">native</span> init AwesomeTSProject --template react-<span class="hljs-keyword">native</span>-template-typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，除了命令行方式外，我们更推荐使用VSCode或WebStrom等可视化编辑工具来创建React Native项目。</p>
<p>等待React Native项目构建成功之后，系统还会自动安装项目所需的第三方依赖库。接着，再使用VSCode或WebStrom打开React Native项目，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2eb31394e2754553b4ab85e23f19e6b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">2.2 运行项目</h2>
<p>运行React Native项目之前，需要配置好原生开发环境。即运行iOS 需要正确安装和配置Xcode工具，运行Android App需要正确安装和配置Android Studio和Android SDK Tools。
同时，为了能够正常的运行项目，还需要在项目运行之前启动模拟器或者真机设备。启动模拟器或真机后，我们可以使用如下的命令来查看连接情况。</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">xcrun simctl list devices   <span class="hljs-comment">//查看可用的iOS设备</span>
adb devices            <span class="hljs-comment">//查看可用的Android设备</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在项目的根目录运行执行如下命令即可启动React Native项目。</p>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-comment">//启动iOS</span>
yarn ios或者yarn react-native run-ios
<span class="hljs-comment">//启动Android</span>
yarn android或者yarn react-native run- android
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此命令会对项目的原生部分进行编译，同时在后台启动Metro服务对 JavaScript代码进行实时打包处理。当然，Metro服务也可以使用yarn start命令单独启动。如果此命令无法正常运行，可以使用Android Studio或者Xcode打开对应的原生工程来查看报错信息。如果没有任何错误提示，那么运行效果如下图所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca706ff8cef741aabf1108d8ea0b52f6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">2.3 调试项目</h2>
<p>调试是软件开发过程中重要的步骤，也是保证软件质量的重要手段。应用调试不仅可以帮助开发者快读的定位软件中存在的问题，同时也是初学者快速理解软件功能的重要途径。</p>
<p>由于React Native项目主要使用React前端语言进行开发，所以调试React Native需要使用到Chrome的DevTools，而Chrome浏览器默认就集成了这一工具。React Native集成了对Chrome的DevTools的支持，开发者可以很容易地使用它调试React Native应用。</p>
<p>使用真机开发时，调试应用只需要晃动下设备即可打开调试选项。如果开发使用的是模拟器，那么可以使用快捷键来打开调试功能，Android模拟器调试的快捷键是【Command +M】，iOS模拟器的快捷键是【Command +D】，如下图所示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9368ea8ecb3142698bfcc25c58e096a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要说明的是，如果是使用真机进行调试，需要调试的真机和开发程序的电脑处于同一个Wi-Fi网络，否则将会出现无法连接的情况。
接着，只需要点击屏幕上的【Debug】选项即可开启远端调试功能。开启远端调试时，系统会自动打开Chrome浏览器的调试界面，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3c80f4249f3427ca97228955b2e3ff3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，依次点击【Chrome菜单】→【选择更多工具】→【选择开发者工具】，或者使用快捷键【Command +Option +I】即可打开调试窗口，开始调试。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f08530336a4d32953056826b4af458~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果大家有前端开发的基础，那么React Native开发可以做到快速上手。</p>
<h1 data-id="heading-8">三、集成到原生应用</h1>
<h2 data-id="heading-9">3.1 集成到原生Android应用</h2>
<p>首先，在原生Android项目的根目录下执行yarn init命令创建一个名为package.json的空文件。然后，根据提示输入对应的配置信息。等待命令执行完成之后，会发现原生Android项目的根目录多了一个package.json文件，该文件就是。
接着，使用如下命令添加React和React Native运行环境的支持脚本。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">yarn <span class="hljs-keyword">add</span> react react-native
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完命令后，会发现Android项目的根目录下多了一个node_modules文件夹，里面包含了React Native开发也运行所需的依赖模块，原则上这个文件目录是不能复制、移动和修改的。并且，node_modules文件夹中的内容是不需要上传仓库的，所以还需要将node_modules文件目录记录到.gitignore文件中。
接下来，使用文本编辑器打开package.json文件，配置React Native的启动脚本，如下代码。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"start"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"yarn react-native start"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，React Native所需的环境就配置完成了。此时，package.json文件的全部内容如下所示。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"AndroidDemo"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0.0"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"main"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"index.js"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"license"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MIT"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"dependencies"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"react"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^17.0.1"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"react-native"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^0.66.0"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"start"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"yarn react-native start"</span>
  <span class="hljs-punctuation">&#125;</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在Android项目的根目录下创建一个index.js文件，用于作为React Native模块的入口，代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;<span class="hljs-title class_">AppRegistry</span>, <span class="hljs-title class_">StyleSheet</span>, <span class="hljs-title class_">Text</span>, <span class="hljs-title class_">View</span>&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">HelloWorld</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">React.Component</span> &#123;
    <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.container&#125;</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.hello&#125;</span>></span>Hello, React Native<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
        );
    &#125;
&#125;

<span class="hljs-keyword">const</span> styles = <span class="hljs-title class_">StyleSheet</span>.<span class="hljs-title function_">create</span>(&#123;
    <span class="hljs-attr">container</span>: &#123;
        <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">justifyContent</span>: <span class="hljs-string">'center'</span>,
    &#125;,
    <span class="hljs-attr">hello</span>: &#123;
        <span class="hljs-attr">fontSize</span>: <span class="hljs-number">20</span>,
        <span class="hljs-attr">textAlign</span>: <span class="hljs-string">'center'</span>,
        <span class="hljs-attr">margin</span>: <span class="hljs-number">10</span>,
    &#125;,
&#125;);

<span class="hljs-title class_">AppRegistry</span>.<span class="hljs-title function_">registerComponent</span>(<span class="hljs-string">'MyReactNativeApp'</span>, <span class="hljs-function">() =></span> <span class="hljs-title class_">HelloWorld</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们使用Android Studio打开原生Android项目，并在app目录的build.gradle文件的dependencies代码块中添加React Native和JSC引擎依赖，如下所示。</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">dependencies &#123;
    ...
    implementation <span class="hljs-string">"com.facebook.react:react-native:+"</span> 
    implementation <span class="hljs-string">"org.webkit:android-jsc:+"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不指定依赖的版本，那么默认使用的是package.json文件中React Native对应的版本。然后，在项目的build.gradle文件的allprojects代码块中添加React Native和JSC引擎的路径，如下所示。</p>
<pre><code class="hljs language-bash copyable" lang="bash">allprojects &#123;
    repositories &#123;
        maven &#123;
            url <span class="hljs-string">"<span class="hljs-variable">$rootDir</span>/../node_modules/react-native/android"</span>
        &#125;
        maven &#123;
            url(<span class="hljs-string">"<span class="hljs-variable">$rootDir</span>/../node_modules/jsc-android/dist"</span>)
        &#125;
        ...
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，打开AndroidManifest.xml清单文件，添加网络权限代码，如下所示。</p>
<pre><code class="hljs language-ini copyable" lang="ini"><uses-permission android:<span class="hljs-attr">name</span>=<span class="hljs-string">"android.permission.INTERNET"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要访问开发者调试菜单，还需要在AndroidManifest.xml清单文件中注册DevSettingsActivity界面，如下所示。</p>
<pre><code class="hljs language-ini copyable" lang="ini"><activity android:<span class="hljs-attr">name</span>=<span class="hljs-string">"com.facebook.react.devsupport.DevSettingsActivity"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，新建一个Activity作为React Native的容器页面，并在Activity中创建一个ReactRootView对象，然后在这个对象之中启动React Native应用代码，如下所示。</p>
<pre><code class="hljs language-scala copyable" lang="scala">public <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyReactActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Activity</span> <span class="hljs-title">implements</span> <span class="hljs-title">DefaultHardwareBackBtnHandler</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-type">ReactRootView</span> mReactRootView;
<span class="hljs-keyword">private</span> <span class="hljs-type">ReactInstanceManager</span> mReactInstanceManager;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">protected</span> void onCreate(<span class="hljs-meta">@Nullable</span> <span class="hljs-type">Bundle</span> savedInstanceState) &#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
        <span class="hljs-type">SoLoader</span>.init(<span class="hljs-keyword">this</span>, <span class="hljs-literal">false</span>);
        mReactRootView = <span class="hljs-keyword">new</span> <span class="hljs-type">ReactRootView</span>(<span class="hljs-keyword">this</span>);
        mReactInstanceManager = <span class="hljs-type">ReactInstanceManager</span>.builder()
                .setApplication(getApplication())
                .setCurrentActivity(<span class="hljs-keyword">this</span>)
                .setBundleAssetName(<span class="hljs-string">"index.android.bundle"</span>)
                .setJSMainModulePath(<span class="hljs-string">"index"</span>)
                .addPackage(<span class="hljs-keyword">new</span> <span class="hljs-type">MainReactPackage</span>())
                .setUseDeveloperSupport(<span class="hljs-type">BuildConfig</span>.<span class="hljs-type">DEBUG</span>)
                .setInitialLifecycleState(<span class="hljs-type">LifecycleState</span>.<span class="hljs-type">RESUMED</span>)
                .build();
        mReactRootView.startReactApplication(mReactInstanceManager, <span class="hljs-string">"MyReactNativeApp"</span>, <span class="hljs-literal">null</span>);
        setContentView(mReactRootView);
    &#125;

    <span class="hljs-meta">@Override</span>
    public boolean onKeyUp(int keyCode, <span class="hljs-type">KeyEvent</span> event) &#123;
        <span class="hljs-keyword">if</span> (keyCode == <span class="hljs-type">KeyEvent</span>.<span class="hljs-type">KEYCODE_MENU</span> && mReactInstanceManager != <span class="hljs-literal">null</span>) &#123;
            mReactInstanceManager.showDevOptionsDialog();
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.onKeyUp(keyCode, event);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用Android Studio的【Alt + Enter】快捷键自动导入缺失的语句，并且BuildConfig是编译时自动生成的，无需额外引入。
由于React Native应用调试还需要悬浮窗权限，所以在需要在Android项目的代码中添加悬浮窗权限逻辑，如下所示。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-type">int</span> <span class="hljs-variable">OVERLAY_PERMISSION_REQ_CODE</span> <span class="hljs-operator">=</span> <span class="hljs-number">1</span>; 

<span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">requestPermission</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) &#123;
            <span class="hljs-keyword">if</span> (!Settings.canDrawOverlays(<span class="hljs-built_in">this</span>)) &#123;
                <span class="hljs-type">Intent</span> <span class="hljs-variable">intent</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Intent</span>(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                        Uri.parse(<span class="hljs-string">"package:"</span> + getPackageName()));
                startActivityForResult(intent, OVERLAY_PERMISSION_REQ_CODE);
            &#125;
        &#125;
&#125;

<span class="hljs-meta">@Override</span>
<span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">onActivityResult</span><span class="hljs-params">(<span class="hljs-type">int</span> requestCode, <span class="hljs-type">int</span> resultCode, Intent data)</span> &#123;
    <span class="hljs-keyword">if</span> (requestCode == OVERLAY_PERMISSION_REQ_CODE) &#123;
        <span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) &#123;
            <span class="hljs-keyword">if</span> (!Settings.canDrawOverlays(<span class="hljs-built_in">this</span>)) &#123;
                <span class="hljs-comment">// SYSTEM_ALERT_WINDOW permission not granted</span>
            &#125;
        &#125;
    &#125;
    mReactInstanceManager.onActivityResult( <span class="hljs-built_in">this</span>, requestCode, resultCode, data );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们在AndroidManifest.xml清单文件中注册MyReactActivity，此处我们直接使用MyReactActivity替换MainActivity作为应用的主页面，如下所示。</p>
<pre><code class="hljs language-ini copyable" lang="ini"><activity
      android:<span class="hljs-attr">name</span>=<span class="hljs-string">".MyReactActivity"</span>
      android:<span class="hljs-attr">theme</span>=<span class="hljs-string">"@style/Theme.AppCompat.Light.NoActionBar"</span>>
<intent-filter>
          <action android:<span class="hljs-attr">name</span>=<span class="hljs-string">"android.intent.action.MAIN"</span> />
          <category android:<span class="hljs-attr">name</span>=<span class="hljs-string">"android.intent.category.LAUNCHER"</span> />
      </intent-filter>
</activity>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成上述操作后，我们在src/main目录下创建一个assets资源文件夹，然后执行如下打包命令。</p>
<pre><code class="hljs language-css copyable" lang="css">react-native bundle <span class="hljs-attr">--platform</span> android <span class="hljs-attr">--entry-file</span> index<span class="hljs-selector-class">.js</span> <span class="hljs-attr">--bundle-output</span> app/<span class="hljs-attribute">src</span>/<span class="hljs-selector-tag">main</span>/assets/index<span class="hljs-selector-class">.android</span><span class="hljs-selector-class">.bundle</span> <span class="hljs-attr">--dev</span> false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，执行yarn start命令启动React Native所需的服务，然后重新运行原生Android项目即可看到效果，如图下图所示。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/681f515bcda043e8aea6e02d38666bb4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">3.2 集成到原生iOS应用</h2>
<p>在原生iOS项目中集成React Native的步骤和Android是一样的。首先，需要在原生iOS项目的根目录下创建一个package.json文件，然后添加如下脚本代码。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"RNiOS"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0.0"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"main"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"index.js"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"license"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MIT"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"dependencies"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"react"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^17.0.1"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"react-native"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^0.66.0"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"start"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"yarn react-native start"</span>
  <span class="hljs-punctuation">&#125;</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，执行yarn install命令安装React Native需要的依赖包。接着，我们再新建一个index.js文件作为React Native部分的入口，代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;<span class="hljs-title class_">AppRegistry</span>,<span class="hljs-title class_">StyleSheet</span>,<span class="hljs-title class_">Text</span>,<span class="hljs-title class_">View</span>&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">ReactHost</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">React.Component</span> &#123;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.container&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.hello&#125;</span>></span>2048 High Scores<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
  &#125;
&#125;
<span class="hljs-title class_">AppRegistry</span>.<span class="hljs-title function_">registerComponent</span>(<span class="hljs-string">'MyReactNativeApp'</span>, <span class="hljs-function">() =></span> <span class="hljs-title class_">ReactHost</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在iOS项目的根目录下使用pod init命令创建一个Podfile文件，添加如下依赖包脚本。</p>
<pre><code class="hljs language-ruby copyable" lang="ruby"><span class="hljs-comment"># target的名字一般与你的项目名字相</span>
  pod <span class="hljs-string">'FBLazyVector'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/Libraries/FBLazyVector"</span>
  pod <span class="hljs-string">'FBReactNativeSpec'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/Libraries/FBReactNativeSpec"</span>
  pod <span class="hljs-string">'RCTRequired'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/Libraries/RCTRequired"</span>
  pod <span class="hljs-string">'RCTTypeSafety'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/Libraries/TypeSafety"</span>
  pod <span class="hljs-string">'React'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/'</span>
  pod <span class="hljs-string">'React-Core'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/'</span>
  pod <span class="hljs-string">'React-CoreModules'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/React/CoreModules'</span>
  pod <span class="hljs-string">'React-Core/DevSupport'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/'</span>
  pod <span class="hljs-string">'React-RCTActionSheet'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/ActionSheetIOS'</span>
  pod <span class="hljs-string">'React-RCTAnimation'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/NativeAnimation'</span>
  pod <span class="hljs-string">'React-RCTBlob'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Blob'</span>
  pod <span class="hljs-string">'React-RCTImage'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Image'</span>
  pod <span class="hljs-string">'React-RCTLinking'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/LinkingIOS'</span>
  pod <span class="hljs-string">'React-RCTNetwork'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Network'</span>
  pod <span class="hljs-string">'React-RCTSettings'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Settings'</span>
  pod <span class="hljs-string">'React-RCTText'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Text'</span>
  pod <span class="hljs-string">'React-RCTVibration'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/Libraries/Vibration'</span>
  pod <span class="hljs-string">'React-Core/RCTWebSocket'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/'</span>

  pod <span class="hljs-string">'React-cxxreact'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/ReactCommon/cxxreact'</span>
  pod <span class="hljs-string">'React-jsi'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/ReactCommon/jsi'</span>
  pod <span class="hljs-string">'React-jsiexecutor'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/ReactCommon/jsiexecutor'</span>
  pod <span class="hljs-string">'React-jsinspector'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/ReactCommon/jsinspector'</span>
  pod <span class="hljs-string">'ReactCommon/callinvoker'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/ReactCommon"</span>
  pod <span class="hljs-string">'ReactCommon/turbomodule/core'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">"../node_modules/react-native/ReactCommon"</span>
  pod <span class="hljs-string">'Yoga'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../node_modules/react-native/ReactCommon/yoga'</span>

  pod <span class="hljs-string">'DoubleConversion'</span>, <span class="hljs-symbol">:podspec</span> => <span class="hljs-string">'../node_modules/react-native/third-party-podspecs/DoubleConversion.podspec'</span>
  pod <span class="hljs-string">'glog'</span>, <span class="hljs-symbol">:podspec</span> => <span class="hljs-string">'../node_modules/react-native/third-party-podspecs/glog.podspec'</span>
  pod <span class="hljs-string">'Folly'</span>, <span class="hljs-symbol">:podspec</span> => <span class="hljs-string">'../node_modules/react-native/third-party-podspecs/Folly.podspec'</span>

<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要说明的是，上面的脚本是启动React Native部分所必须的，并且每个版本会有细微的区别。完成上述配置之后，使用pod install命令安装所需的依赖包。
接着，使用Xcode打开原生iOS项目，在ViewController.m启动文件中添加如下代码。</p>
<pre><code class="hljs language-scss copyable" lang="scss">- (IBAction)highScoreButtonPressed:(id)sender &#123;
    <span class="hljs-built_in">NSLog</span>(@"High Score Button Pressed");
    NSURL *jsCodeLocation = <span class="hljs-selector-attr">[NSURL URLWithString:@<span class="hljs-string">"http://localhost:8081/index.bundle?platform=ios"</span>]</span>;

    RCTRootView *rootView =
      <span class="hljs-selector-attr">[[RCTRootView alloc]</span> initWithBundleURL: jsCodeLocation
                                  moduleName: @<span class="hljs-string">"RNHighScores"</span>
                           initialProperties:
                             @&#123;
                               @<span class="hljs-string">"scores"</span> : @[
                                 @&#123;
                                   @<span class="hljs-string">"name"</span> : @<span class="hljs-string">"Alex"</span>,
                                   @<span class="hljs-string">"value"</span>: @<span class="hljs-string">"42"</span>
                                  &#125;,
                                 @&#123;
                                   @<span class="hljs-string">"name"</span> : @<span class="hljs-string">"Joel"</span>,
                                   @<span class="hljs-string">"value"</span>: @<span class="hljs-string">"10"</span>
                                 &#125;
                               ]
                             &#125;
                               <span class="hljs-attribute">launchOptions</span>: nil];
    UIViewController *vc = <span class="hljs-selector-attr">[[UIViewController alloc]</span> init];
    vc<span class="hljs-selector-class">.view</span> = rootView;
    <span class="hljs-selector-attr">[self presentViewController:vc animated:YES completion:nil]</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当上面的代码被执行时，应用会打开React Native的index.js页面，并且将从原生iOS部分获取的数据也显示到屏幕上。最后，使用yarn start命令启动Node.js服务，重新运行原生iOS项目即可看到效果，如图下图所示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c7bd73e5fb34c88b3f630f5e9a53f99~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            