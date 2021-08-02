
---
title: '手把手将Cordova应用上架App Store'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68878689f8804ce1a78751318cacdeff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 18:04:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68878689f8804ce1a78751318cacdeff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">准备工作</h2>
<p>上架ios应用需要准备几样东西</p>
<ol>
<li>
<p>一台装有XCode的MacBook电脑，用来编译项目</p>
</li>
<li>
<p>注册Apple Developer 个人账号，在找掌握Apple Developer企业账号的人，叫他把你加进组织，这样你就能用你自己的账号操作</p>
</li>
<li>
<p>一台苹果手机，主要用来真机测试</p>
</li>
</ol>
<h2 data-id="heading-1">创建证书请求文件</h2>
<p>证书请求文件，一般称呼为CSR，一会请求证书需要用到这个东西，首先打开应用程序 > 实用工具 > 钥匙串访问.app，左上角点击钥匙串访问 > 证书助理 > 从证书颁发机构请求证书...，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68878689f8804ce1a78751318cacdeff~tplv-k3u1fbpfcp-watermark.image" alt="WeChat9afe26fb996f8f93dd742597766da134.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在如下图界面，用户电子邮件地址：填你开发者账号注册邮箱，常用名称：随便起但是要方便寻找，选择储存在磁盘(CA电子邮件地址就不用填了)，放到桌面上，最好跟项目放到一起</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c7a2628130c43878adf969257a27762~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG777.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有CSR之后就可以去苹果开发中心生成证书了</p>
<h2 data-id="heading-2">登陆苹果开发者中心生成证书</h2>
<p>登陆开发者中心后看到如下界面，点击下面框框的那块</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d58f5be117144a7094387ee3782f2fb5~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG778.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>申请证书</p>
<p>一下操作需要执行两次，因为我们需要一个测试证书和一个发布证书</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15785d91d2da41cfa37bbb8998beb873~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG779.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8dbf1015e2d43bc965d9b51710ab7a7~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG780.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a117f50ce08b489b96f1ed31f32faf61~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG781.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击download将证书下载到本地</p>
<p>注意：证书下载到本地后一定要双击一下导入钥匙串里面</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ee675c0a20418f9b859e70998c1f80~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG782.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">注册App Identiifier</h2>
<p>只有注册了App Id，你才可以在App Store Connect中新建App</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/661e9c6734ae4f5bace4052bafb3751e~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG783.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4acacc5703ee4048adb27b598e447177~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG784.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1703579a102b4f43a88cc4725aa80a28~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG785.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/279512fdcaed4f3a90513672f6db81c4~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG786.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bb09c14c467407487b72413f43ec339~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG787.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击Register，App Id注册成功</p>
<h2 data-id="heading-4">注册真机测试所用的设备</h2>
<p>真机测试所用的设备必须在开发者中心注册，否则应用装不上去</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a4e778ad08342ff8ad64bd7559a5047~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG788.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/682959974b704d0990cff6184aaa53c3~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG792.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50af4167baf4698bd5bdb1a1db5f99c~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG790.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击Register注册成功</p>
<h2 data-id="heading-5">注册配置文件</h2>
<p>该操作同上面一样也需要执行两次，分别用测试证书和发布证书注册debug和release的配置文件，生成的文件需要鼠标双击导入XCode，要不然配置时选不到</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/159abb8cf1734beba7603ba65a976cec~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG793.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e28124d1d774a4b8de2174f2cb4d033~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG794.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55d62cc2db44498a8ad4fe2e92f8b6b3~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG795.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击确定后就能download配置文件，download下载后记住一定要双击导入XCode</p>
<h2 data-id="heading-6">在App Store connect中创建新的App</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d49416e191646eaa8b643d2411ef860~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG809.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1506a19d6fba4957a50c594a5c2e7f86~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG810.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e87c1fcef28b4d9085235ffa132d9f44~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG811.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建成功后里面的信息能填的尽量填下，要不会提交不了，里面还有一个构建版本，这个是需要在XCode中打包最后由XCode传上来的</p>
<h2 data-id="heading-7">Xcode构建应用</h2>
<p>在构建应用时说明下，苹果官方发出的声明说：2020年3月之前已经上线的项目，可以继续使用UIWebView继续迭代版本，每次提交审核会收到苹果的警告邮件；2020年3月之后的项目，必须使用WKWebView，提交审核才能通过，不然提示二进制数据错误。详情苹果官方说明点击下面链接</p>
<p>ITMS-90809: Deprecated API Usage - Apple will stop accepting submissions of new apps that use UIWebView APIs starting from April 2020. See <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fuiwebview" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https://developer.apple.com/documentation/uikit/uiwebview" ref="nofollow noopener noreferrer">developer.apple.com/documentati…</a> for more information.</p>
<p>在cordova-ios6.1.0之前我们是通过一个官方插件将UIWebview转成WKWebview，用法如下</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">cordova plugin add cordova-plugin-wkwebview-engine

<span class="hljs-comment">// 在config.xml做出加入配置</span>
<preference name=<span class="hljs-string">"WKWebViewOnly"</span> value=<span class="hljs-string">"true"</span> />
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">feature</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"CDVWKWebViewEngine"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">param</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"ios-package"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"CDVWKWebViewEngine"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">feature</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">preference</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"CordovaWebViewEngine"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"CDVWKWebViewEngine"</span> /></span></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>cordova-ios6.1.0之后已经将UIWebview完全剔除，所以不需要上面那个插件</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">cordova platform add ios@<span class="hljs-number">6.1</span><span class="hljs-number">.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用WKWebview时候，我们会发现请求接口或者获取手机本地图片会发生跨域，这是因为WKWebview安全机制的问题，原先UIWebview是支持跨域的，接口请求的跨域我们可以通过后台配置跨域请求，手机本地图片跨域我们在XCode中找到CDVWKWebViewEngine.m文件</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 在这个文件中找到这个方法</span>
- (WKWebViewConfiguration*) createConfigurationFromSettings:(NSDictionary*)settings
&#123;    
    WKWebViewConfiguration* configuration = [[WKWebViewConfiguration alloc] init];
    ...
    这里还有一部分代码，不用删除
    ...
    <span class="hljs-comment">//在return上面添加下面两行代码</span>
    [configuration.preferences setValue:@YES forKey:@<span class="hljs-string">"allowFileAccessFromFileURLs"</span>];
    [configuration setValue:@YES forKey:@<span class="hljs-string">"_allowUniversalAccessFromFileURLs"</span>];
    <span class="hljs-keyword">return</span> configuration;
&#125;
解决跨域问题，Cookie获取不到的情况。

<span class="copy-code-btn">复制代码</span></code></pre>
<p>进去 platform  >  ios目录，这里就是整个cordova-ios项目，在开始之前我们先把一些能做的东西做了，在这个目录下进入  项目名 > Images.xcassets目录，这里存放的是应用的图表以及启动图，在这里我们把应用图表给替换了，我使用的是一款叫Asset Catalog Creator的软件，导入一张1024*1024的图片就可以生成我们项目所需要的App icon，我们把它生成的AppIcon.appiconset文件夹替换掉原来的AppIcon.appiconset文件夹，这样icon就配置完成了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac8494e532146689c26f9a6c1436bc8~tplv-k3u1fbpfcp-watermark.image" alt="WeChat913f0ecd287e4e9c700360b69443dd55.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>双击xxxxxxx.xcodepro文件将项目导入XCode，下面进行XCode的配置
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e732e94015574a5bb0aa819bcd5740c2~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG816.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f729cd80ddc4327ac427960d4de0155~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG815.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc2d144d9624f3f93b3361d4d26d7c6~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG817.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这一步我们应用基础配置、证书配置、信息配置基本完成</p>
<h2 data-id="heading-8">应用打包和测试</h2>
<p>测试我们分两种方法，模拟器测试和真机测试</p>
<p>真机测试方法一样，前提是用来测试的手机必须是在开发者中心注册过的，要不然安装包装不进去。把手机连接数据线插件来，XCode会自动检测注册过的手机，之后打开下拉框就能看到真机名称，之后选择再点击三角形即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd750483aa1b4308993de96b91198c1b~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG818副本.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">应用提交</h2>
<p>应用经过测试过后就可以打包构建版本提交到App Store Connect中进行审核了</p>
<p>打开下拉框选中小锤子，在点击Product > Archive就可以打包构建版本，打包成功后会出现有图界面，接下来先执行第一步验证构建版本，如果验证不通过的话就算提交上去也是审核不过的，验证通过了就可以执行第二步上传构建版本，一般来说会因为网络问题卡一段时间，不过问题不大，上传成功了一般过一会就能在App Store Connect中找到构建版本，之后填写相关资料就可以提交审核了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b711587cfb6a4701905b1e52b9fb6c6b~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG820.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bb3b5ae1fcb4c6d9d5fe8a163e6465b~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG822.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上传成功了但是又不出现构建版本，这时候请注意自己的邮箱，一般有问题的构建版本都不会出现在App Store Connect中</p>
<h2 data-id="heading-10">问题列举</h2>
<p>列举几个我遇到的问题：</p>
<ul>
<li><strong>TMS-90809: Deprecated API Usage</strong>  - New apps that use UIWebView are no longer accepted. Instead, use WKWebView for improved security and reliability. Learn more (<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fuiwebview" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/uiwebview" ref="nofollow noopener noreferrer">developer.apple.com/documentati…</a>).</li>
</ul>
<p>    这个是原因上面已经提过，因为ios现在已经弃用UIWebView了，所以我们提交的构建版本全部都要是用WKWebview，要不然就算上传成功了 App Store Connect也会因为元数据出错为由拒绝</p>
<ul>
<li><strong>ITMS-90683: Missing Purpose String in Info.plist</strong>  - Your app's code references one or more APIs that access sensitive user data. The app's Info.plist file should contain a NSBluetoothAlwaysUsageDescription key with a user-facing purpose string explaining clearly and completely why your app needs the data. Starting Spring 2019, all apps submitted to the App Store that access user data are required to include a purpose string. If you're using external libraries or SDKs, they may reference APIs that require a purpose string. While your app might not use these APIs, a purpose string is still required. You can contact the developer of the library or SDK and request they release a version of their code that doesn't contain the APIs. Learn more (<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit%2Fcore_app%2Fprotecting_the_user_s_privacy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit/core_app/protecting_the_user_s_privacy" ref="nofollow noopener noreferrer">developer.apple.com/documentati…</a>).</li>
</ul>
<p>    出现这个错误是因为我应用用到了蓝牙功能（NSBluetoothAlwaysUsageDescription）但是并没有在info.plist上声明权限，所以我们回到info.plist上把这个权限声明一下就好</p>
<ul>
<li>Guideline 2.1 - Information Needed - We’re looking forward to continuing our review, but we need more information about your business model and your users to help you find the best distribution option for your app. Our preliminary review of your app suggests that your app may be a good fit for our Apple Business Manager program, which is designed specifically for business apps.</li>
</ul>
<p>    这个问题一般是审核的人对这个应用有一些疑问，他会提出几个问题需要你回答，这时候你只需要认真用双语来回答他的问题就行，记住文字一定要友好</p>
<ul>
<li>一个中规中矩的应用一般不会被拒绝，被拒绝的一般一般是应用功能包含暗示赌博、暴力、色情等内容，或者是集成的原生功能使用了不被apple认可的第三方库，这时候只有更换插件，因为我们应用的原生功能都是通过Cordova plugin集成进来的，例如：下面的错误是因为 我使用的一个插件里面用了一个不被认可的三方库，这种情况连前面版本验证都过不去</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc00b97e8ca743abae06ba6036cb8595~tplv-k3u1fbpfcp-watermark.image" alt="WeChatf127e9540ae61ac279bba41eabeeeb5d.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            