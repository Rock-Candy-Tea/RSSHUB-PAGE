
---
title: 'iOS 支付宝支付开发（最新版）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8688fd141e5c4425b1e07ef6d5363447~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 10 Mar 2021 03:52:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8688fd141e5c4425b1e07ef6d5363447~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 介绍</h2>
<p>本文为以前做的项目总结，由于相关支付 SDK 迭代，原文已经不满足需求，故作如下更新，供大家参考，另外增加常见问题总结。</p>
<p>今天我们就主要介绍一下支付宝支付，其他支付介绍后面会尽快更新出来。</p>
<p>在做支付之前，在网上也查寻了资料，大多都说，支付接入坑太多，微信坑最多，银联文档太复杂。
其实如果接入的多的话，那些套路都可以绕着走。
网上的经验什么的大都是比较老的，比较新的能用到的文章不多（但是好文章还是有的，对我帮助也很大），下面给大家详细介绍一下，帮助大家绕开坑。</p>
<h2 data-id="heading-1">2. 交互流程</h2>
<p>建议先把开发文档仔仔细细看一遍，一定要看，刚开始的时候没有老老实实地看完，结果遇到很多的坑，浪费的挺多的时间的，所以建议一定要好好看看，特别是交互流程这一部分。</p>
<h3 data-id="heading-2">2.1 功能流程</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8688fd141e5c4425b1e07ef6d5363447~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.2 数据交互</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/115b15944b364a15a6948eb180f086b1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>支付宝支付的功能流程相比较微信支付来说简单的很，如上面两张图展示的，我们的 App（也就是商户客户端）所做的大概只有三个步骤：</p>
<ul>
<li>生成订单</li>
<li>调用支付宝接口，发送订单</li>
<li>返回订单支付结果并处理</li>
</ul>
<h2 data-id="heading-4">3. 下载支付宝 SDK</h2>
<p>支付宝业务众多，真想找到想要的支付sdk还是要费一番功夫的，这里给出了最新的 SDK 地址
<strong>注意</strong>的是下载出来的 SDK 包里面并没有传说中的开发文档，需要其他地方找或者看网页上的。</p>
<p>公钥、私钥、PID、sellerID、key这些东西的用途和获取方式在文档上都有详细的说明，这里不再赘述，一定要把概念分清楚再去做，不然一会就乱了。如果遇到问题的话咱们可以再一起探讨。</p>
<h2 data-id="heading-5">4.  导入库集成SDK</h2>
<h3 data-id="heading-6">4.1 导入文件和关键库</h3>
<p><strong>通过 CocoaPods 导入</strong></p>
<pre><code class="copyable">pod  'AlipaySDK-iOS' 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>手动导入</strong></p>
<p>官方 demo 截图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36fb998958da4664a3cb2fca96a24958~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>添加 framework 和其他文件
打开 iOS 工程，新版本 SDK 文件 Order 文件，你需要复制粘贴到自己工程里的有：</p>
<ul>
<li>AlipaySDK.framework</li>
<li>AlipaySDK.bundle</li>
<li>Until 文件夹</li>
<li>openssl 文件夹</li>
<li>libcrypto.a 和 libssl.a</li>
</ul>
<p>上面的一部分文件在打开的项目中是看不到的，需要打开项目文件夹找到。</p>
<p>在 Build Phases 选项卡的 Link Binary With Libraries 中，增加以下依赖：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e052992193d427e91285f9187bddff7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中，需要注意的是：</p>
<ul>
<li>如果是Xcode 7.0之后的版本，需要添加libc++.tbd、libz.tbd；</li>
<li>如果是Xcode 7.0之前的版本，需要添加libc++.dylib、libz.dylib（如下图）。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b43efaeb56c4339af14127460fcd0c4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>此时，假如你启动工程，很大几率上你会发现报 error 的情况。</p>
<h3 data-id="heading-7">4.2 引入头文件</h3>
<p>在需要调用 AlipaySDK 的文件中，增加头文件引用。</p>
<pre><code class="copyable">import <AlipaySDK/AlipaySDK.h>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.3 调用支付接口</h3>
<p>在支付宝的接入文档中，是将生成一个订单这步放在客户端来做了，但这个最好是放在服务器端来做。</p>
<p>后台生成订单然后拼接，签名，然后服务器端直接给客户端传一个加密签名过的参数就可以了，这样比较安全。</p>
<p>所有的订单信息，商户信息等都掌握在自己的手中，这样的话APP端就不怕被拦截数据，并且调用起来也就特别简单了，只需要调用支付的接口。</p>
<p>如果只需要发送订单和处理支付返回结果，只需要添加 AlipaySDK.bundle 和AlipaySDK.framework 这两个就行了，下载的SDK中很容易发现。
快捷支付方法是这个：</p>
<pre><code class="copyable">-(void)payOrder:(NSString *)orderStr fromScheme:(NSString *)schemeStr callback:(CompletionBlock)completionBlock;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在支付的按钮中，使用支付宝这个类，再调用这个方法就行啦！如下如：</p>
<pre><code class="copyable">// NOTE: 调用支付结果开始支付
[[AlipaySDK defaultService] payOrder:orderString fromScheme:@"FBYAlipayDemo" callback:^(NSDictionary *resultDic) &#123;
    NSLog(@"reslut = %@",resultDic);
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.4 配置支付宝客户端返回 url 处理方法</h3>
<p>如示例 AliSDKDemo\APAppDelegate.m 文件中，增加引用代码：</p>
<pre><code class="copyable">import <AlipaySDK/AlipaySDK.h>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 *@*implementation  AppDelegate 中以下代码中的 NSLog 改为实际业务处理代码：</p>
<pre><code class="copyable">- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<NSString*, id> *)options
&#123;
    if ([url.host isEqualToString:@"safepay"]) &#123;
        //跳转支付宝钱包进行支付，处理支付结果
        [[AlipaySDK defaultService] processOrderWithPaymentResult:url standbyCallback:^(NSDictionary *resultDic) &#123;
            NSLog(@"result = %@",resultDic);
        &#125;];
    &#125;
    return YES;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4.5 项目配置</h3>
<p>最后，不要忘了还要写一个 URL Scheme，在 Targets -> Info 下最后一个即可找到，
点击 “Info” 选项卡，在 “URL Types ”选项中，点击 “+”。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/743ffb1092bb4cc4ab6f845a7cb7bd55~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">5. 常见问题汇总</h2>
<h3 data-id="heading-12">5.1 支付后无法返回 App</h3>
<p>一般是由于白名单没有设置正确</p>
<pre><code class="copyable">// NOTE: 调用支付结果开始支付
[[AlipaySDK defaultService] payOrder:orderString fromScheme:@"FBYAlipayDemo" callback:^(NSDictionary *resultDic) &#123;
    NSLog(@"reslut = %@",resultDic);
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上方代码中 appScheme 参数需要和文章 <strong>4.5 项目配置</strong>中设置的 URL Schemes 相同，这样才能对应返回 App。</p>
<h3 data-id="heading-13">5.2 #include <openssl/opensslconf.h> not find</h3>
<p>这是一个神奇的大坑，我Google了好久，也不得其解，然后经网友提醒之后想起来#import ""和#import <>的区别。</p>
<p><strong>解决方法</strong>：Targets -> Build Settings 下的 Header Search Paths。
添加如下目录 "$(SRCROOT)/项目名称/文件的绝对地址"
如图：</p>
<p><img alt="3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40f0b9ba81d48bc8ded85bf2fe6ae1e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">5.3 'openssl/asn1.h' file not found</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ae746bcaf0c4c32ae80ed76429b6b2b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于在项目中引入 openssl 库，出现这个问题是因为库文件项目无法找到，只需要在 Header Search Paths 中加入 $(PROJECT_DIR)/项目名称/openssl 即可，如下图操作：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5732304211a5473b9b1ed4edf5e61b32~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">5.4 Undefined symbol: <em>OBJC_METACLASS</em>$_WKWebView</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15de4c63d16e49ba831d344be0e19e3c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>出现上面的问题，需要在项目配置中添加系统类库：WebKit.framework</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b8cff9e3b44418cbb2979ec0e9a2de5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">5.5 如果遇到运行后报错，类似于以下提示信息：</h3>
<pre><code class="copyable">Cannot find interface declaration for 'NSObject', superclass of 'Base64'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么需要打开报错了的文件，增加头文件。</p>
<pre><code class="copyable"># import <Foundation/Foundation.h>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5.6 Swift 中接入 SDK 遇到的问题</h3>
<p>如果项目使用 Swift 为开发语言，需要添加桥接文件，如 Bridging-Header.h</p>
<p>同时，在项目 Build Settings 中设置桥接文件的位置。</p>
<p>运行时如果发生以下报错，则在桥接文件中，写入#import <UIKit/UIKit.h></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4d474efcd7f487887e925a06627a0b7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">5.7 点击支付跳转至支付宝卡在启动页面</h3>
<p>出现这个情况被卡在的页面会出现相应错误提示，一般有以下几种情况：</p>
<ul>
<li>商品信息拼接字符串错误</li>
<li>支付账号过期待续费状态</li>
<li>商户 ID 错误</li>
<li>订单信息验签失败</li>
</ul>
<p>获取源码方式：关注「<strong>网罗开发</strong>」回复 “<strong>支付宝支付</strong>” 即可获取</p>
<p>本文已在公众号「<strong>网罗开发</strong>」发布，如果转载长白请加微信：FBY-fan，备注<strong>转载长白</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            