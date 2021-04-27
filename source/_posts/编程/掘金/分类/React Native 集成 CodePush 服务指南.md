
---
title: 'React Native 集成 CodePush 服务指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c20871ad3c1648ee85fb5af11b12f4cb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 03:27:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c20871ad3c1648ee85fb5af11b12f4cb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文由团队成员<a href="https://juejin.cn/user/325111174662855/posts" target="_blank">洛竹</a>撰写，已授权涂鸦大前端独家使用，包括但不限于编辑、标注原创等权益。</p>
</blockquote>
<p>目前现存的热更新方案有腾讯的 <a href="https://bugly.qq.com/v2/products/upgrade" target="_blank" rel="nofollow noopener noreferrer"> Bugly 应用升级</a>、React Native 中文网的 <a href="https://update.reactnative.cn/home" target="_blank" rel="nofollow noopener noreferrer">Pushy</a>、微软的 <a href="https://bre.is/r3Y9hJvB" target="_blank" rel="nofollow noopener noreferrer">CodePush</a> 和用来搭建私服的 <a href="https://github.com/lisong/code-push-server" target="_blank" rel="nofollow noopener noreferrer">code-push-server</a>。</p>
<p>本文分享的是基于微软 AppCenter 的 CodePush 服务实现热更新，这个比较有代表性，也方便各位读者大大实践。当然鉴于国内的网络环境，后期会发布一篇如何基于 <code>code-push-server</code> 实现热更新功能。</p>
<h2 data-id="heading-0">环境</h2>
<ul>
<li>Xcode：Version 11.3.1 (11C504)</li>
<li>react-native：0.61.5</li>
<li>react-native-code-push: 6.1.0</li>
<li>appcenter-cli：2.3.3</li>
</ul>
<h2 data-id="heading-1">CodePush介绍</h2>
<p>CodePush 是一个 App Center 云服务，使 Apache Cordova 和 React Native 开发人员可以将移动应用程序更新直接部署到其用户的设备上。它充当中央存储库的角色，开发人员可以将某些更新（例如JS，HTML，CSS和图像更改）发布到该存储库，并且应用程序可以（使用提供的客户端SDK）从中查询更新。这使你可以与最终用户建立更具确定性和直接的参与度模型，同时解决错误和/或添加一些小的功能，这些功能不需要你重建二进制文件和/或通过任何公共应用商店重新分发二进制文件。默认情况下，在 App Center 上创建的所有 React Native 应用程序都启用了 CodePush。</p>
<blockquote>
<p>注意：对于 Android 设备，CodePush 仅在兼容 TLS 1.2 的设备上运行</p>
</blockquote>
<h3 data-id="heading-2">1.安装 App Center CLI</h3>
<p>你可以使用 App Center CLI 管理 CodePush 的大多数功能。要安装 CLI，请打开终端窗口或命令提示符并执行以下命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install -g appcenter-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功安装 App Center CLI 后，执行<code>appcenter login</code>命令为你的 App Center 帐户详细信息配置 CLI：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c20871ad3c1648ee85fb5af11b12f4cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.应用管理</h3>
<p>部署更新之前，必须使用以下命令使用 App Center 创建应用：</p>
<pre><code class="hljs language-shell copyable" lang="shell">appcenter apps create -d <appDisplayName> -o <operatingSystem> -p <platform>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您的应用同时针对 Android 和 iOS，我们强烈建议您使用 CodePush 创建单独的应用。每个平台一个。这样，您可以分别管理和发布更新，从长远来看，这会使事情变得更简单。大多数人只是在应用名称后缀<code>-Android</code>和<code>-iOS</code>。例如：</p>
<pre><code class="hljs language-shell copyable" lang="shell">appcenter apps create -d MyApp-Android -o Android -p React-Native
appcenter apps create -d MyApp-iOS -o iOS -p React-Native
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：在 Android 和 iOS 上使用相同的应用程序可能会导致安装异常，因为为 iOS 生成的 CodePush 更新包将具有与为 Android 生成的更新不同的内容。</p>
</blockquote>
<blockquote>
<p>通过 <code>appcenter apps list</code> 可以查看所有的应用。</p>
</blockquote>
<blockquote>
<p>在App中心CLI的一个重要的新功能是设置一个应用程序的能力<strong>当前应用程序</strong>使用<code>appcenter apps set-current <ownerName>/<appName></code>。通过将一个应用程序设置为当前应用程序，您无需<code>-a</code>在其他CLI命令中使用该标志。例如，<code>appcenter codepush deployment list -a <ownerName>/<appName></code>可以将命令缩短<code>appcenter codepush deployment list</code>为设置当前应用程序的时间。您可以使用来检查哪个应用程序被设置为您帐户的当前应用程序<code>appcenter apps get-current</code>。设置当前应用程序可以缩短大多数CLI命令的键入时间。</p>
</blockquote>
<p>使用 <code>code-push-cli</code>，应用程序会自动进行两次部署（<code>Staging</code>和 <code>Production</code>）。在 App Center 中，你必须使用以下命令自行创建它们：</p>
<pre><code class="hljs language-shell copyable" lang="shell">appcenter codepush deployment add -a <ownerName>/<appName> Staging
appcenter codepush deployment add -a <ownerName>/<appName> Production
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建部署后，您可以使用来访问两个部署的部署密钥<code>appcenter codepush deployment list --displayKeys</code>，您可以开始通过它们各自的SDK（用于<a href="https://docs.microsoft.com/en-us/appcenter/distribution/codepush/cordova" target="_blank" rel="nofollow noopener noreferrer">Cordova</a>和<a href="https://docs.microsoft.com/en-us/appcenter/distribution/codepush/react-native" target="_blank" rel="nofollow noopener noreferrer">React Native的</a>详细信息）来配置移动客户端。</p>
<h3 data-id="heading-4">3.修改versionNam</h3>
<p>在 <code> android/app/build.gradle</code> 中有个 <code>android.defaultConfig.versionName</code> 属性（在 <code>ios/**/Info.plist</code> 是 <code><key>CFBundleShortVersionString</key></code> 属性 ）；我们需要把应用版本改成 <code>1.0.0</code>（默认<code>1.0</code>，但是 <code>codepush</code> 需要三位数）</p>
<h3 data-id="heading-5">3.发布应用更新</h3>
<p>更改应用程序的代码或资产后，请按照以下说明使用 App Center CLI 将更新发布到App Center。</p>
<p>执行 App Center CLI <code>release-react </code> 命令以捆绑应用程序的代码和资产文件，然后将它们作为新版本发布到 App Center 服务器。例如：</p>
<pre><code class="hljs language-shell copyable" lang="shell">appcenter codepush release-react -a <ownerName>/<appName> -d Staging -t 1.0.0 -m  --development false --description <description>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>[-a|--app <ownerName>/<appName>]</code>:  指定应用</li>
<li><code>[-d|--deployment-name <deploymentName></code>]:  此参数指定要将更新发布到的部署。它默认为<code>Staging</code>，但是当您准备部署到<code>Production</code>或您自己的自定义部署之一时，只需显式设置此参数即可。</li>
<li><code>[-t|--target-binary-version <targetBinaryVersion>]</code>:  指定要更新的应用的原生版本</li>
<li><code>[-m|--mandatory]</code>:  是强制更新，默认 <code>false</code></li>
<li><code>[--development]</code>: 此参数指定是否生成未缩小的开发JS包。如果未指定，则默认为<code>false</code>禁用警告并缩小包的位置。</li>
<li><code>[--description <description></code>]:  此参数为部署提供了可选的“更改日志”。该值将往返传送给客户端，以便在检测到更新时，您的应用可以选择将其显示给最终用户（例如，通过“新功能”对话框）。该字符串接受诸如<code>\n</code>和的控制字符，<code>\t</code>因此您可以在描述中包括空格格式，以提高可读性。</li>
</ul>
<blockquote>
<p>CodePush客户端支持差异更新，因此，即使您在每次更新中释放JS捆绑包和资产，最终用户也只会实际下载他们需要的文件。该服务会自动处理此问题，因此您可以专注于创建出色的应用程序，而我们会担心优化最终用户的下载。</p>
</blockquote>
<h2 data-id="heading-6">React Native Client SDK</h2>
<p>该插件为 CodePush 服务提供了客户端集成，使你可以轻松地向你的 React Native 应用添加动态更新体验。</p>
<blockquote>
<p>注意：以下配置均基于 react-native 0.60 版本。</p>
</blockquote>
<h3 data-id="heading-7">它是如何工作的？</h3>
<p>React Native 应用程序由 JavaScript 文件和任何相关的图片组成，它们由打包程序 <a href="https://facebook.github.io/metro/" target="_blank" rel="nofollow noopener noreferrer">metro</a> 捆绑在一起, 并作为特定于平台的二进制文件（<code>.ipa</code> 或 <code>.apk</code> 文件）的一部分进行分发。发行该应用程序时，更新 JavaScript 代码（例如进行错误修复，添加新功能）或更新图片资源要求你重新编译并重新分发整个二进制文件，其中包括与商店相关的所有时间。</p>
<p>通过使你的 JavaScript 和图片资源与您发布到 CodePush 服务器的更新同步，CodePush 插件可帮助你立即在最终用户面前获得产品改进。</p>
<p>为了确保您的最终用户始终拥有你的应用程序的正常运行版本，CodePush 插件会维护先前更新的副本，因此，如果您不小心推送了包含崩溃的更新，它可以自动回滚。这样，你可以放心，新发现的发行版不会导致用户被阻塞。</p>
<blockquote>
<p>注意：任何涉及本机代码的产品更改（例如，修改<code>AppDelegate.m</code>/<code>MainActivity.java</code>、添加 <code>ttf</code> 或添加原生插件）都无法通过 CodePush 分发，因此必须通过相应的商店进行更新。</p>
</blockquote>
<h3 data-id="heading-8">支持的React Native平台</h3>
<ul>
<li>iOS（7以上）</li>
<li>Android（4.1以上）</li>
<li>Windows（UWP）</li>
</ul>
<h3 data-id="heading-9">安装 react-native-code-push</h3>
<pre><code class="hljs language-sh copyable" lang="sh">yarn add react-native-code-push
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与其他所有React Native插件一样，iOS 和 Android 的集成体验也有所不同，因此请根据您的应用目标平台执行以下设置步骤。请注意，如果您同时针对两个平台，建议为每个平台创建单独的 CodePush 应用程序。</p>
<blockquote>
<p>本指南假定您已使用该<code>react-native init</code>命令初始化React Native项目。</p>
</blockquote>
<h3 data-id="heading-10">iOS设置</h3>
<p>获得 CodePush 插件后，必须将其集成到 React Native 应用程序的 Xcode 项目中并正确配置。</p>
<ol>
<li>
<p>运行<code>cd ios && pod install && cd ..</code>以安装所有必需的CocoaPods依赖项。</p>
</li>
<li>
<p>打开<code>AppDelegate.m</code>文件，并为CodePush标头添加导入语句：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">#import <CodePush/CodePush.h>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查找以下代码行，该代码为生产版本的网桥设置源URL：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">return [[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>用以下行替换它：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">return [CodePush bundleURL];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此更改将你的应用配置为始终加载应用JS捆绑包的最新版本。在首次启动时，这将与使用该应用程序编译的文件相对应。但是，在通过CodePush推送更新后，这将返回最近安装的更新的位置。</p>
<p>通常，您只想使用 CodePush 来解决发行版本中的 JS 包位置，因此，我们建议使用<code>DEBUG</code>预处理器宏在是否使用打包程序服务器和 CodePush 之间进行动态切换。这样可以更轻松地确保您在生产中获得所需的正确行为，同时仍可以在调试时使用Chrome开发工具，实时重新加载等。</p>
<p>你的<code>sourceURLForBridge</code>方法应如下所示：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (NSURL *)sourceURLForBridge:(RCTBridge *)bridge
&#123;
  #if DEBUG
    return [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index" fallbackResource:nil];
  #else
    return [CodePush bundleURL];
  #endif
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>将部署密钥添加到<code>Info.plist</code>：</p>
<p>为了让 CodePush 运行时知道应该针对哪个部署查询更新，请打开你的应用的 <code>Info.plist</code> 文件，并添加一个名为<code>CodePushDeploymentKey</code>的新条目，其值是你要配置的应用的 <code>Staging Deployment Key</code>。</p>
<p>你可以通过 <code>appcenter codepush deployment list -k</code> 来检索这个值（该 <code>-k</code> 标志是必需的，因为默认情况下不会显示键），然后复制相对应的 <code>Deployment Key</code> 即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ba62b9084464784a0a525de8a710757~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了有效利用与 CodePush 应用程序一起创建的 <code>Staging</code> 和 <code>Production</code> 部署，请在实际将你的应用程序对 CodePush 的使用移入生产环境之前，进行<a href="https://juejin.cn/post/6955426002910576671#%E5%A4%9A%E9%83%A8%E7%BD%B2%E6%B5%8B%E8%AF%95">多部署测试</a>的配置。</p>
<blockquote>
<p>如果您需要动态使用其他部署，还可以使用<a href="https://juejin.cn/post/6955426002910576671#%E5%8A%A8%E6%80%81%E9%83%A8%E7%BD%B2%E5%88%86%E9%85%8D">动态部署分配</a>在JS代码中覆盖部署密钥</p>
</blockquote>
</li>
</ol>
<h3 data-id="heading-11">Android设置</h3>
<p>为了将CodePush集成到您的Android项目中，请执行以下步骤：</p>
<ol>
<li>
<p>在<code>android/app/build.gradle</code>文件中，将文件<code>codepush.gradle</code>添加为下面的其他构建任务定义：</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">...
apply <span class="hljs-attr">from:</span> <span class="hljs-string">"../../node_modules/react-native-code-push/android/codepush.gradle"</span>
...
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>MainApplication.java</code>通过以下更改更新文件以使用 CodePush：</p>
<pre><code class="hljs language-java copyable" lang="java">...
<span class="hljs-comment">// 1. 导入插件的类</span>
<span class="hljs-keyword">import</span> com.microsoft.codepush.react.CodePush;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainApplication</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">ReactApplication</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> ReactNativeHost mReactNativeHost = <span class="hljs-keyword">new</span> ReactNativeHost(<span class="hljs-keyword">this</span>) &#123;
        ...
        <span class="hljs-comment">// 2. 重写 getJSBundleFile 方法，每次 app 启动的时候让 CodePush 运行时决定从哪里加载 JS bundle</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">protected</span> String <span class="hljs-title">getJSBundleFile</span><span class="hljs-params">()</span> </span>&#123;
            <span class="hljs-keyword">return</span> CodePush.getJSBundleFile();
        &#125;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>将部署密钥添加到<code>strings.xml</code>：</p>
<p>为了让 CodePush 运行时知道它应该查询哪些部署更新，请打开您的应用程序的 <code>string.xml</code> 文件，并添加一个名为 <code>CodePushDeploymentKey</code> 的新字符串，它的值是应用的 <code>Staging</code> 部署。你可以通过 <code>appcenter deployment list <ownerName>/<appName> -k</code> 获取该值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d879fb9b3546cfa6f10b743ac96648~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>您<code>strings.xml</code>应该看起来像这样：</p>
<pre><code class="hljs language-xml copyable" lang="xml"> <span class="hljs-tag"><<span class="hljs-name">resources</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">string</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"app_name"</span>></span>AppName<span class="hljs-tag"></<span class="hljs-name">string</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">string</span> <span class="hljs-attr">moduleConfig</span>=<span class="hljs-string">"true"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"CodePushDeploymentKey"</span>></span>DeploymentKey<span class="hljs-tag"></<span class="hljs-name">string</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">resources</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了有效利用与CodePush应用程序一起创建的<code>Staging</code>和<code>Production</code>部署，请在实际将您的应用程序对CodePush的使用移入生产环境之前，请参考下面的<a href="https://juejin.cn/post/6955426002910576671#%E5%A4%9A%E9%83%A8%E7%BD%B2%E6%B5%8B%E8%AF%95">多部署测试</a>文档。</p>
<blockquote>
<p>如果您需要动态使用其他部署，还可以使用<a href="https://juejin.cn/post/6955426002910576671#%E5%8A%A8%E6%80%81%E9%83%A8%E7%BD%B2%E5%88%86%E9%85%8D">动态部署分配</a>在JS代码中覆盖部署密钥</p>
</blockquote>
</li>
</ol>
<h3 data-id="heading-12">使用插件</h3>
<p>下载并链接了 CodePush 插件，并且为你的应用程序询问 CodePush 从何处获取正确的 JS bundle 包后，剩下的唯一一件事就是向你的应用程序添加必要的代码，以控制以下策略：</p>
<ol>
<li>什么时候（多久）检查一次更新？（例如，应用程序启动，在设置页面中单击按钮或按固定时间间隔定期进行）</li>
<li>当有可用更新时，如何将其呈现给最终用户？</li>
</ol>
<p>最简单的方式是 <code>CodePush-ify</code> 应用程序的根组件。为此，您可以选择一下两个选项之一：</p>
<ul>
<li>
<p>选项1：将您的根组件与 codePush 高阶组件包装在一起：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> codePush <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-code-push'</span>
<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;&#125;
App = codePush(App)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>选项2：使用 <a href="https://github.com/wycats/javascript-decorators" target="_blank" rel="nofollow noopener noreferrer">ES7装饰器 </a>语法：</p>
<blockquote>
<p>Babel 6.x 尚不支持装饰器。您可能需要通过安装和使用 <a href="https://github.com/skevy/babel-preset-react-native-stage-0#babel-preset-react-native-stage-0" target="_blank" rel="nofollow noopener noreferrer">babel-preset-react-native-stage-0</a> 来启用装饰器。</p>
</blockquote>
<blockquote>
<p>Babel 7.x 支持装饰器语法。你可以使用 <a href="https://babeljs.io/docs/en/next/babel-plugin-proposal-decorators.html" target="_blank" rel="nofollow noopener noreferrer">@babel/plugin-proposal-decorators</a> 来启用装饰器。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> codePush <span class="hljs-keyword">from</span> <span class="hljs-string">"react-native-code-push"</span>

@codePush
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>默认情况下，CodePush 将在每次启动应用程序时检查更新。如果有可用更新，它将在下一次重新启动应用程序时（由最终用户或操作系统明确显示）以静默方式下载并安装，从而确保最终用户获得最少的侵入性体验。如果必须使用可用的更新，则将立即安装该更新，以确保最终用户尽快获得它。</p>
<p>如果您希望应用程序更快地发现更新，则还可以选择每次应用程序从后台恢复时与 CodePush 服务器同步。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> codePushOptions = &#123; <span class="hljs-attr">checkFrequency</span>: codePush.CheckFrequency.ON_APP_RESUME &#125;
<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> codePush(codePushOptios)(App)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，如果您想对检查发生的时间进行细粒度的控制（例如按按钮或定时器间隔），则可以使用 <a href="https://bre.is/dPuwHWre" target="_blank" rel="nofollow noopener noreferrer">CodePush.sync()</a> 随时进行调用，还可以通过 <code>SyncOptions</code> 通过 <code>CheckFrequency.MANUAL</code> 来关闭 CodePush 的自动检查功能:</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;View, StyleSheet&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> codePush <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-code-push'</span>;
<span class="hljs-keyword">import</span> AwesomeButton <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-really-awesome-button'</span>;

<span class="hljs-keyword">const</span> codePushOptions = &#123; <span class="hljs-attr">checkFrequency</span>: codePush.CheckFrequency.MANUAL &#125;;

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> checkForUpdate = <span class="hljs-function">() =></span> &#123;
    codePush.sync(&#123;
      <span class="hljs-attr">updateDialog</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">installMode</span>: codePush.InstallMode.IMMEDIATE,
    &#125;);
  &#125;;

  <span class="hljs-keyword">const</span> clear = <span class="hljs-function">() =></span> &#123;
    codePush.clearUpdates();
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.container&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">AwesomeButton</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"secondary"</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;checkForUpdate&#125;</span>></span>
        检查更新
      <span class="hljs-tag"></<span class="hljs-name">AwesomeButton</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">AwesomeButton</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"secondary"</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;clear&#125;</span>></span>
        清除更新
      <span class="hljs-tag"></<span class="hljs-name">AwesomeButton</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">justifyContent</span>: <span class="hljs-string">'center'</span>,
    <span class="hljs-attr">alignItems</span>: <span class="hljs-string">'center'</span>,
  &#125;,
&#125;);

<span class="hljs-comment">// 注意：这是可选的，完全可以不使用 codePush 这里包装</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> codePush(codePushOptions)(App);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想要显示一个更新确认弹窗（一个主动安装）。配置何时安装可用更新（例如强制立即重启）或以任何其他方式自定义更新体验，请参阅 <a href="https://docs.microsoft.com/en-us/appcenter/distribution/codepush/react-native#api-reference" target="_blank" rel="nofollow noopener noreferrer">codepush</a> API参考以获取有关一下信息：如何调整此默认行为。</p>
<h3 data-id="heading-13">应用商店规则</h3>
<ul>
<li>
<p>苹果App允许使用热更新<a href="https://developer.apple.com/programs/ios/information/iOS_Program_Information_4_3_15.pdf" target="_blank" rel="nofollow noopener noreferrer">Apple's developer agreement</a>, 为了不影响用户体验，规定必须使用静默更新。</p>
</li>
<li>
<p>Google Play不能使用静默更新，必须弹框告知用户App有更新。</p>
</li>
<li>
<p>中国的android市场必须采用静默更新（如果弹框提示，App会被“请上传最新版本的二进制应用包”原因驳回）。</p>
</li>
</ul>
<h2 data-id="heading-14">多部署测试</h2>
<p>在入门文档中，我们说明了如何使用特定的部署密钥配置 CodePush 插件。但是，为了有效地测试发型版，至关重要的是，在首次创建 CodePush 应用程序（或你可能已经创建的任何自定义部署）时，利用我们建议进行的 <code>Staging</code> 和 <code>Production</code> 部署。</p>
<blockquote>
<p>我们的客户端回滚功能可以帮助您在安装导致崩溃的版本后解除对用户的阻止，服务器端的回滚（例如<code>appcenter codepush rollback</code>）使您可以防止其他用户在发现错误的版本后再安装它。但是，如果可以从一开始就防止广泛发布错误更新，那显然更好。</p>
</blockquote>
<p>利用<code>Staging</code>和<code>Production</code>部署，您可以实现类似于以下的工作流程（随意定制！）：</p>
<ol>
<li><code>Staging</code> 使用 <code>appcenter codepush release-react</code> 命令将 CodePush 更新发布到您的部署中（如果你需要更多的控制权可以使用 <code>appcenter codepush release</code> ）</li>
<li>构建应用程序的 staging<code>/</code>beta` 版本，从服务器同步更新，并验证其是否按预期工作</li>
<li>使用以下命令将测试的发行版从 <code>Staging</code> 升级到 <code>Prouction</code>: <code>appcenter codepush promote -a <ownerName>/<appName> -s Staging -d Production</code></li>
<li>构建应用程序的 <code>production</code>/<code>release</code>，从服务其同步更新并验证其是否按预期工作</li>
</ol>
<blockquote>
<p>如果您想采取更为谨慎的方法，甚至可以选择在“＃3”中执行 <strong>分阶段推出</strong>，这使您可以减轻更新带来的额外潜在风险（例如，＃2中的测试是否接触了所有可能的设备），仅使一定比例的用户可以使用生产更新（例如<code>code-push promote -a / -s Staging -d Production -r 20%</code>）。然后，在等待了一段合理的时间以查看是否有崩溃报告或客户反馈后，您可以通过运行将其扩展到整个受众<code>appcenter codepush patch -a / Production -r 100%</code>。</p>
</blockquote>
<h3 data-id="heading-15">安卓系统</h3>
<p>在<a href="https://google.github.io/android-gradle-dsl/current/index.html" target="_blank" rel="nofollow noopener noreferrer">Android Gradle plugin </a>允许您定义自定义配置设置，每个“构建类型”（如调试，发布）。此机制使您可以轻松地使用 CodePush 部署密钥配置调试版本，而发行版本也可以配置为使用 CodePush 生产部署密钥。</p>
<p>提醒一下，您可以通过<code>appcenter codepush deployment list  -k</code>从终端运行来检索这些键。</p>
<p>要进行设置，请执行以下步骤：</p>
<ol>
<li>
<p>打开项目的应用程序级别<code>build.gradle</code>文件（例如标准 React Native 项目中的 <code>android/app/build.gradle</code>）</p>
</li>
<li>
<p>查找此<code>android &#123; buildTypes &#123;&#125; &#125;</code>部分，并<code>resValue</code>为您<code>debug</code>和<code>release</code>构建类型定义条目，分别引用您的密钥<code>Staging</code>和<code>Production</code>部署密钥。</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">android &#123;
  ...
  buildTypes &#123;
    debug &#123;
      signingConfig signingConfigs.debug
      <span class="hljs-comment">// Note: CodePush updates should not be tested in Debug mode as they are overriden by the RN packager. However, because CodePush checks for updates in all modes, we must supply a key.</span>
      resValue <span class="hljs-string">"string"</span>, <span class="hljs-string">"CodePushDeploymentKey"</span>, <span class="hljs-string">'""'</span>
    &#125;
    release &#123;
      <span class="hljs-comment">// Caution! In production, you need to generate your own keystore file.</span>
      <span class="hljs-comment">// see https://facebook.github.io/react-native/docs/signed-apk-android.</span>
      signingConfig signingConfigs.release
      minifyEnabled enableProguardInReleaseBuilds
      proguardFiles getDefaultProguardFile(<span class="hljs-string">"proguard-android.txt"</span>), <span class="hljs-string">"proguard-rules.pro"</span>
      resValue <span class="hljs-string">"string"</span>, <span class="hljs-string">"CodePushDeploymentKey"</span>, <span class="hljs-string">'""'</span>
    &#125;
    releaseStaging.initWith(release)
    releaseStaging &#123;
        resValue <span class="hljs-string">"string"</span>, <span class="hljs-string">"CodePushDeploymentKey"</span>, <span class="hljs-string">'""'</span>
        <span class="hljs-comment">// Note: It is a good idea to provide matchingFallbacks for the new buildType you create to prevent build issues</span>
        <span class="hljs-comment">// Add the following line if not already there</span>
        matchingFallbacks = [<span class="hljs-string">'release'</span>]
    &#125;
  &#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<blockquote>
<p>如果要在构建过程中配置部署密钥，请记住从<code>strings.xml</code>中删除密钥。</p>
</blockquote>
<blockquote>
<p><code>releaseStaging</code>由于<a href="https://github.com/facebook/react-native/blob/e083f9a139b3f8c5552528f8f8018529ef3193b9/react.gradle#L79" target="_blank" rel="nofollow noopener noreferrer">此行</a>，的命名约定，这不能改。</p>
</blockquote>
<h3 data-id="heading-16">iOS</h3>
<blockquote>
<p>该部分适用于 Xcode 11</p>
</blockquote>
<p>Xcode 允许你为每个<strong>配置</strong> (如 <code>debug</code>, <code>release</code>) 自定义构建设置，然后可以将其引用为 <code>Info.plist</code> 文件中的键值（如 <code>CodePushDeploymentKey</code> 设置）。此机制是您可以轻松地进行构建配置以生成二进制文件，这些二进制文件被配置为与不同的 CodePush 部署同步。</p>
<p>要进行设置，请执行以下步骤：</p>
<ol>
<li>
<p>打开您的 Xcode 项目，然后在 <code>Project navigator</code> 窗口中选择您的项目</p>
</li>
<li>
<p>确保已选择 <code>PROJECT</code> 节点，而不是 <code>TARGETS</code></p>
</li>
<li>
<p>选择 <code>Info</code> 标签</p>
</li>
<li>
<p>点击 <code>+</code> 的内部按钮<code>Duplicate "Release" Configuration</code></p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c7a6411057d41dfbd64d70f0a90f8db~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>
<p>将新配置命名为 <code>Staging</code>（或您喜欢的任何名称）</p>
</li>
<li>
<p>选择 <code>Build Settings</code> 选项卡</p>
</li>
<li>
<p>单击工具栏上的 <code>+</code> 按钮，创建一个名为  <code>CONFIGURATION_BUILD_DIR</code> 的  <code>User-Defined Setting</code>，配置如图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48020c5fb0ea4ce1a1e310e892bad206~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：每次创建这个 Xcode 都会崩溃，只能先把值写入之后，在 <code>project.pbxproj</code> 中修改。</p>
</blockquote>
</li>
<li>
<p>点击工具栏的 <code>+</code>  并选择 <code>Add User-Defined Setting</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1e3dee9bd048f0b3755b2f08eb9f28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>将此新设置命名为<code>CodePushDeploymentKey</code>，展开它，然后为 <code>Staging </code>配置指定您的 <code>Staging</code> 部署密钥，为 <code>Release</code> 配置指定您的 <code>Production</code> 部署密钥。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/191f88644f1c49b1be9d405198c4b84b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提醒一下，您可以通过<code>appcenter codepush deployment list -a <ownerName>/<appName> --displayKeys</code>从终端运行来检索这些键。</p>
</blockquote>
</li>
<li>
<p>打开项目的 <code>Info.plist</code> 文件，然后将<code>CodePushDeploymentKey</code>条目的值更改为<code>$(CODEPUSH_KEY)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f20190ca7c3040eea6b1e96287f1b66f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
<p>就是这样了，现在当你运行或构建你的App，你的 <code>Staging</code> 包将自动同步你的 <code>Staging</code> 部署，你的 <code>Release</code> 包将自动同步你的 <code>Production</code> 部署。</p>
<blockquote>
<p>注意：如果你遇到 <code>ld: library not found for ...</code> 错误信息，请看一下这个 <a href="https://github.com/Microsoft/react-native-code-push/issues/426" target="_blank" rel="nofollow noopener noreferrer">issuse</a></p>
</blockquote>
<p>此外，如果你想给他们不同的名称和/或图标，你可以修改<code>Product Bundle Identifier</code>，<code>Product Name</code>以及<code>Asset Catalog App Icon Set Name</code></p>
<h2 data-id="heading-17">动态部署分配</h2>
<p>上一节说明了如何利用多个<code>CodePush</code>部署，以便在更新发布给用户之前，有效地测试您的更新内容。 但是，由于该工作流静态地将部署分配嵌入到实际二进制文件中，因此<code>临时构建</code>和<code>生产构建</code>只会同步该部署的更新内容。</p>
<p>在许多情况下，这是足够的，因为您只希望您的团队，客户，利益相关者等与您的预生产版本同步，因此，他们只需要知道如何与该版本同步构建。</p>
<p>但是，如果你希望能够进行 <code>A / B</code> 测试，或者为某些用户提供应用程序的早期访问权限，那么能够在运行时将特定用户（或受众）动态地置于特定部署中将非常有用。</p>
<p>为了实现此工作流程，你需要做的就是指定调用该<code>codePush</code>方法时希望当前用户与之同步的部署密钥。指定后，此密钥将覆盖应用程序的 <code>Info.plist</code>（iOS）或 <code>MainActivity.java</code>（Android）文件中提供的“默认”密钥。这允许您生成临时或生产构建，也可以根据需要动态“重定向”。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Imagine that "userProfile" is a prop that this component received</span>
<span class="hljs-comment">// which includes the deployment key that the current user should use.</span>
codePush.sync(&#123; <span class="hljs-attr">deploymentKey</span>: userProfile.CODEPUSH_KEY &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这样的变化后，现在只需选择应用程序如何为当前用户配置正确的部署密钥。 在实践中，通常有两种解决方案：</p>
<ol>
<li>将更改部署的功能开放给用户。例如，您的设置页面可能会有一个切换按钮以启用“测试版”的访问权限。 如果您不在乎预生产更新的内容被得知，并且您的某些用户可能希望根据自己的意愿选择使用最新（并且可能有错误）的更新（有点像Chrome渠道）。 但是，此解决方案将决策权交给您的用户，这无法帮助您透明地执行 <code>A / B</code> 测试。</li>
<li>使用额外的元数据注释用户的服务器端配置文件，标明与其同步的部署。 默认情况下，您的应用只能使用二进制嵌入密钥，但在用户通过身份验证后，您的服务器可以选择将其“重定向”到其他部署，这样您就可以根据需要逐步将某些用户或组放置在不同的部署中。您甚至可以选择将服务器响应存储在本地存储中，以使其成为新的默认值。 如何将密钥与用户的配置文件一起存储完全取决于您的身份验证解决方案（例如 <code>Auth0</code>，<code>Firebase</code>，自定义<code>DB</code> + <code>REST API</code>），但这通常非常简单。</li>
</ol>
<blockquote>
<p>注意：如果需要，您还可以实施混合解决方案，允许最终用户在不同部署之间切换，同时还允许您的服务器覆盖该决策。 这样，您就拥有了“部署解决方案”的层次结构，可确保您的应用程序能够自行更新，用户可以通过获得最新内容的访问权限来获得最新体验，但您也有能力根据需要对用户进行 <code>A / B</code> 测试。</p>
</blockquote>
<p>由于我们建议将<code>Staging</code>部署用于更新的预发布测试（如上一节中所述），因此使用该部署对用户执行 <code>A / B</code> 测试并不一定有意义，与此相反，你应该允许早期访问（如上面选项1中所述）。因此，我们建议充分利用自定义应用程序部署，以便您可以按用户需求对用户进行细分。例如，您可以创建长期甚至是一次性的部署，向其发布应用程序的变体，然后将某些用户放入其中，以查看其参与度。</p>
<pre><code class="hljs language-sh copyable" lang="sh">// <span class="hljs-comment">#1) Create your new deployment to hold releases of a specific app variant</span>
appcenter codepush deployment add -a <ownerName>/<appName> test-variant-one

// <span class="hljs-comment">#2) Target any new releases at that custom deployment</span>
appcenter codepush release-react -a <ownerName>/<appName> -d test-variant-one
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：从一个部署“切换”到另一个部署的用户数，被纳入到部署中的“安装度量”中报告的总用户数。例如，如果您的<code>Production</code> 部署当前报告的用户总数为1，但您将该用户动态切换为 <code>Staging</code> 部署，则 <code>Production</code> 部署将报告 0个总用户，而 <code>Staging</code> 部署将报告1（刚刚切换的用户）。 即使在使用基于运行时的部署重定向解决方案的情况下，这种行为可以让你准确地跟踪您的版本使用情况。</p>
</blockquote>
<h2 data-id="heading-18">最佳实践</h2>
<blockquote>
<p>源码：<a href="https://github.com/youngjuning/AppCenterCodePushDemo" target="_blank" rel="nofollow noopener noreferrer">github.com/youngjuning…</a></p>
</blockquote>
<h3 data-id="heading-19">App.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123;useEffect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;View, StyleSheet&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> codePush <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-code-push'</span>;
<span class="hljs-keyword">import</span> AwesomeButton <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-really-awesome-button'</span>;
<span class="hljs-keyword">import</span> &#123;codePushSync, checkForUpdate&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./CodePushUtils'</span>;
<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> getUpdateMetadata = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> running = <span class="hljs-keyword">await</span> codePush.getUpdateMetadata(
      codePush.UpdateState.RUNNING,
    );
    <span class="hljs-keyword">const</span> pending = <span class="hljs-keyword">await</span> codePush.getUpdateMetadata(
      codePush.UpdateState.PENDING,
    );
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[CodePush] running'</span>, running);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[CodePush] pending'</span>, pending);
  &#125;;

  useEffect(<span class="hljs-function">() =></span> &#123;
    codePushSync();
  &#125;, []);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.container&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">AwesomeButton</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;checkForUpdate&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;marginBottom:</span> <span class="hljs-attr">10</span>&#125;&#125;></span>
        Check For Update!
      <span class="hljs-tag"></<span class="hljs-name">AwesomeButton</span>></span>
<span class="hljs-tag"><<span class="hljs-name">AwesomeButton</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;()</span> =></span> codePush.clearUpdates()&#125; style=&#123;&#123;marginBottom: 10&#125;&#125;>
        Clear Updates!
      <span class="hljs-tag"></<span class="hljs-name">AwesomeButton</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">AwesomeButton</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;getUpdateMetadata&#125;</span>></span>
        getUpdateMetadata!
      <span class="hljs-tag"></<span class="hljs-name">AwesomeButton</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">justifyContent</span>: <span class="hljs-string">'center'</span>,
    <span class="hljs-attr">alignItems</span>: <span class="hljs-string">'center'</span>,
  &#125;,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">CodePushUtils.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;AppState, Platform, Alert&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> codePush <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-code-push'</span>;
<span class="hljs-keyword">import</span> configReader <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-config-reader'</span>;

<span class="hljs-keyword">const</span> CodePushDeploymentKey = &#123;
  <span class="hljs-attr">ios</span>: &#123;
    <span class="hljs-attr">debug</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">staging</span>: <span class="hljs-string">'944zuIiRSds-ZZY6AQF82aRl0b1vUL_mMxiie'</span>,
    <span class="hljs-attr">release</span>: <span class="hljs-string">'yyJfk2vtpLUUlOCg3FnvCcky9o4U1lEWR1UJV'</span>,
  &#125;,
  <span class="hljs-attr">android</span>: &#123;
    <span class="hljs-attr">debug</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">releasestaging</span>: <span class="hljs-string">'tOncLvKACzzSkUaML9tCOUfPZxHVnobfaNIUe'</span>,
    <span class="hljs-attr">release</span>: <span class="hljs-string">'Gtc4iXTPn24yu6CBrbl_V2GTy21xtdQyfm6x1'</span>,
  &#125;,
&#125;;

<span class="hljs-keyword">const</span> getDeploymentKey = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> buildType = configReader.BUILD_TYPE.toLowerCase();
  <span class="hljs-keyword">const</span> deploymentKey = CodePushDeploymentKey[Platform.OS][buildType];
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[CodePushUtils]'</span>, deploymentKey);
  <span class="hljs-keyword">return</span> deploymentKey;
&#125;;

<span class="hljs-keyword">const</span> codePushStatusDidChange = <span class="hljs-keyword">async</span> syncStatus => &#123;
  <span class="hljs-keyword">switch</span> (syncStatus) &#123;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.CHECKING_FOR_UPDATE:
      <span class="hljs-comment">// 0 - 正在查询CodePush服务器以进行更新。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Checking for update.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.AWAITING_USER_ACTION:
      <span class="hljs-comment">// 1 - 有可用的更新，并且向最终用户显示了一个确认对话框。（仅在updateDialog使用时适用）</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Awaiting user action.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.DOWNLOADING_PACKAGE:
      <span class="hljs-comment">// 2 - 正在从CodePush服务器下载可用更新。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Downloading package.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.INSTALLING_UPDATE:
      <span class="hljs-comment">// 3 - 已下载一个可用的更新，并将其安装。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Installing update.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.UP_TO_DATE:
      <span class="hljs-comment">// 4 - 应用程序已配置的部署完全最新。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] App is up to date.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.UPDATE_IGNORED:
      <span class="hljs-comment">// 5 该应用程序具有可选更新，最终用户选择忽略该更新。（仅在updateDialog使用时适用）</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] User cancelled the update.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.UPDATE_INSTALLED:
      <span class="hljs-comment">// 6 - 安装了一个可用的更新，它将根据 SyncOptions 中的 InstallMode指定在 syncStatusChangedCallback 函数返回后立即或在下次应用恢复/重新启动时立即运行。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Installed update.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.SYNC_IN_PROGRESS:
      <span class="hljs-comment">// 7 - 正在执行的 sync 操作</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] Sync already in progress.'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> codePush.SyncStatus.UNKNOWN_ERROR:
      <span class="hljs-comment">// -1 - 同步操作遇到未知错误。</span>
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'[CodePush] An unknown error occurred.'</span>);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> codePushDownloadDidProgress = <span class="hljs-function"><span class="hljs-params">progress</span> =></span> &#123;
  <span class="hljs-keyword">const</span> curPercent = (
    (progress.receivedBytes / progress.totalBytes) *
    <span class="hljs-number">100</span>
  ).toFixed(<span class="hljs-number">0</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[CodePushUtils] Downloading Progress'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;curPercent&#125;</span>%`</span>);
  <span class="hljs-comment">// console.log(`$&#123;progress.receivedBytes&#125; of $&#123;progress.totalBytes&#125; received.`);</span>
&#125;;

<span class="hljs-keyword">const</span> syncImmediate = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> deploymentKey = getDeploymentKey();
  codePush.sync(
    &#123;
      <span class="hljs-attr">updateDialog</span>: &#123;
        <span class="hljs-comment">// 是否显示更新描述</span>
        <span class="hljs-attr">appendReleaseDescription</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 更新描述的前缀。 默认为"Description"</span>
        <span class="hljs-attr">descriptionPrefix</span>: <span class="hljs-string">'\n\n更新内容：\n'</span>,
        <span class="hljs-comment">// 强制更新按钮文字，默认为continue</span>
        <span class="hljs-attr">mandatoryContinueButtonLabel</span>: <span class="hljs-string">'立即更新'</span>,
        <span class="hljs-comment">// 强制更新时的信息. 默认为"An update is available that must be installed."</span>
        <span class="hljs-attr">mandatoryUpdateMessage</span>: <span class="hljs-string">'必须更新后才能使用'</span>,
        <span class="hljs-comment">// 非强制更新时，按钮文字,默认为"ignore"</span>
        <span class="hljs-attr">optionalIgnoreButtonLabel</span>: <span class="hljs-string">'稍后'</span>,
        <span class="hljs-comment">// 非强制更新时，确认按钮文字. 默认为"Install"</span>
        <span class="hljs-attr">optionalInstallButtonLabel</span>: <span class="hljs-string">'后台更新'</span>,
        <span class="hljs-comment">// 非强制更新时，检查到更新的消息文本</span>
        <span class="hljs-attr">optionalUpdateMessage</span>: <span class="hljs-string">'有新版本了，是否更新？'</span>,
        <span class="hljs-comment">// Alert窗口的标题</span>
        <span class="hljs-attr">title</span>: <span class="hljs-string">'更新'</span>,
      &#125;,
      deploymentKey,
      <span class="hljs-attr">installMode</span>: codePush.InstallMode.IMMEDIATE,
    &#125;,
    codePushStatusDidChange,
    codePushDownloadDidProgress,
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> checkForUpdate = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> deploymentKey = getDeploymentKey();
  <span class="hljs-keyword">const</span> update = <span class="hljs-keyword">await</span> codePush.checkForUpdate(deploymentKey);
  <span class="hljs-keyword">if</span> (!update) &#123;
    Alert.alert(<span class="hljs-string">'提示'</span>, <span class="hljs-string">'已是最新版本'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    syncImmediate();
  &#125;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> codePushSync = <span class="hljs-function">() =></span> &#123;
  AppState.addEventListener(<span class="hljs-string">'change'</span>, <span class="hljs-function"><span class="hljs-params">newState</span> =></span> &#123;
    newState === <span class="hljs-string">'active'</span> && syncImmediate();
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">Npm Scripts</h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    ...
    <span class="hljs-attr">"gradle:clean"</span>: <span class="hljs-string">"cd android && ./gradlew clean"</span>,
    <span class="hljs-attr">"an:release"</span>: <span class="hljs-string">"yarn gradle:clean && cd android && ./gradlew app:assembleRelease"</span>,
    <span class="hljs-attr">"an:installRelease"</span>: <span class="hljs-string">"yarn gradle:clean && cd android && ./gradlew app:installRelease"</span>,
    <span class="hljs-attr">"an:staging"</span>: <span class="hljs-string">"yarn gradle:clean && cd android && ./gradlew app:assembleReleaseStaging"</span>,
    <span class="hljs-attr">"an:installStaging"</span>: <span class="hljs-string">"yarn gradle:clean && cd android && ./gradlew app:installReleaseStaging"</span>,
    <span class="hljs-attr">"displayKeys"</span>: <span class="hljs-string">"yarn disPlayIosKeys && yarn disPlayAndroidKeys"</span>,
    <span class="hljs-attr">"disPlayIosKeys"</span>: <span class="hljs-string">"appcenter codepush deployment list --app youngjuning/AppCenterCodePushDemo-iOS --displayKeys"</span>,
    <span class="hljs-attr">"disPlayAndroidKeys"</span>: <span class="hljs-string">"appcenter codepush deployment list --app youngjuning/AppCenterCodePushDemo-Android --displayKeys"</span>,
    <span class="hljs-attr">"release-react"</span>: <span class="hljs-string">"yarn release-react-ios && yarn release-react-android"</span>,
    <span class="hljs-attr">"release-react-ios"</span>: <span class="hljs-string">"appcenter codepush release-react --app youngjuning/AppCenterCodePushDemo-iOS"</span>,
    <span class="hljs-attr">"release-react-android"</span>: <span class="hljs-string">"appcenter codepush release-react --app youngjuning/AppCenterCodePushDemo-Android"</span>
    ...
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">扩展</h2>
<h3 data-id="heading-23">CodePush 什么情况下不会立即重启应用</h3>
<ol>
<li>自上一次<code>disallowRestart</code>被调用，没有新的更新。</li>
<li>有更新，但<code>installMode</code>为<code>InstallMode.ON_NEXT_RESTART</code>的情况下。</li>
<li>有更新，但<code>installMode</code>为<code>InstallMode.ON_NEXT_RESUME</code>，并且程序一直处于前台，并没有从后台切换到前台的情况下。</li>
<li>自从上次<code>disallowRestart</code>被调用，没有再调用<code>restartApp</code>。</li>
</ol>
<h3 data-id="heading-24">TypeSctipt</h3>
<p>如果使用 TypeScript，再浏览一次文档的API部分之后，就可以依靠类型系统的提示来工作啦： <a href="https://github.com/microsoft/react-native-code-push/blob/master/typings/react-native-code-push.d.ts" target="_blank" rel="nofollow noopener noreferrer">react-native-code-push.d.ts</a></p>
<h3 data-id="heading-25">iOS 添加 BUILD_TYPE</h3>
<p>在 <code>Info.plist</code> 中添加 <code>BUILD_TYPE</code>，取值为 <code>$(CONFIGURATION)</code></p>
<h3 data-id="heading-26">react-native bundle</h3>
<p>生成  <code>bundle</code> 命名：<code>react-native bundle --platform</code> 平台 <code> --entry-file</code>启动文件 <code>--bundle-output</code> 打包js输出文件 <code> --assets-dest</code>  资源输出目录 <code> --dev</code>  是否调试：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ react-native bundle --platform android --entry-file index.js --bundle-output ./bundle/android/main.jsbundle --assets-dest ./bundle/android --dev <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            