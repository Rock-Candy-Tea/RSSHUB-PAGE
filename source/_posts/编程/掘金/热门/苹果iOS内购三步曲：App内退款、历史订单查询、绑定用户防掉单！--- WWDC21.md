
---
title: '苹果iOS内购三步曲：App内退款、历史订单查询、绑定用户防掉单！--- WWDC21'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b15b0be087ca41efa838e373161d2eec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 04:10:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b15b0be087ca41efa838e373161d2eec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、前言</h3>
<p>如果大家的 App 有使用 IAP 功能，那么可能会遇到用户反馈苹果充值成功，但是服务没有到账的情况，用户一般会提供这样的苹果收据：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b15b0be087ca41efa838e373161d2eec~tplv-k3u1fbpfcp-watermark.image" alt="16239077635884.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用户反馈时提供的苹果收据中，有一个字段中 <code>ORDER ID</code>，苹果叫 <code>Invoice order ID</code>（发票订单号），与我们开发者从 App 内获取到的 <code>receipt</code> 收据解析后，并没有 ORDER ID 字段！！！所以，我们无法定位和联系这个用户提供的发票与我们后台的订单号，从而无法给用户正常补发服务，开发者也是很无奈！</p>
<p>而今年，这个问题苹果终于提供解决方案啦！是不是很开心！点一个赞吧~</p>
<p>大家都知道，手机游戏的收入重要来源就是<code>虚拟物品</code>购买，而 iOS 需要通过 App Store 必须使用苹果的 <code>In-App Purchase</code> （应用内购买，下文统一使用<code>IAP</code>表示内购功能。）功能。而 37手游 是三七互娱旗下独立子公司，作为国内顶尖的手游发行平台，累计运营超过2000款游戏，所以对于 37手游 来说，IAP 的重要性不言而喻！</p>
<p>去年的 WWDC20，苹果推出 <code>IAP退款通知</code> 时，在 <a href="https://developer.apple.com/videos/play/wwdc2020/10661/" target="_blank" rel="nofollow noopener noreferrer">What’s new with in-app purchase - WWDC 2020</a> 解读时，小编在 <a href="https://juejin.cn/post/6845166890420011022#heading-8" target="_blank">疑问解答</a> 时给出了2个大胆推测：</p>
<p><strong>1、 苹果后台能否查看到退款的订单详情？</strong></p>
<pre><code class="copyable">答：暂无。（估计明年 WWDC2021 会有啦？）
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2、 消耗型、非消耗型、非续期订阅能不能在沙盒环境测试退款？</strong></p>
<pre><code class="copyable">答：暂时不能。（估计未来会有？等更新吧....）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今年的 <a href="https://developer.apple.com/wwdc21/sessions/" target="_blank" rel="nofollow noopener noreferrer">WWDC21</a> 大会开始后，小编第一时间就关注 IAP 相关的 Sessions 会议，大喜！今年的 IAP 功能更加开放和透明，去年大家的2个疑问，今年都给解决了！以下就是苹果今年关于 IAP 的三步曲：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adb177116669433d82a6dc65e7fc37e5~tplv-k3u1fbpfcp-watermark.image" alt="16238945099196.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10114" target="_blank" rel="nofollow noopener noreferrer">Meet StoreKit 2 - WWDC 2021</a></li>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10174/" target="_blank" rel="nofollow noopener noreferrer">Manage in-app purchases on your server - WWDC 2021</a></li>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10175" target="_blank" rel="nofollow noopener noreferrer">Support customers and handle refunds - WWDC 2021</a></li>
</ol>
<p>因为以上三个 Session 内容上是相互之间紧密相连，密不可分，所以小编接下来就在本文将这三步曲混合来解读，主要分成三部分：</p>
<ol>
<li><strong>StoreKit 2</strong>：关于在 App 里 API 的更新和变化，包含应用内更改订阅、退款等；</li>
<li><strong>Server to Server</strong>：苹果服务器与开发者服务器之间的通讯，包括苹果通知、开发者主动请求苹果服务器、新的验证收据流程等；</li>
<li><strong>Sandbox Test</strong>：关于沙盒测试环境相关的更新，还有一些注意事件等。</li>
</ol>
<h3 data-id="heading-1">二、StoreKit 2</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0de6da003ad14c76bc9f629fd673f61c~tplv-k3u1fbpfcp-watermark.image" alt="16238991331773.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>StoreKit 2 主要更新</strong></p>
<ul>
<li>一套新的基于 Swift 语言特性</li>
<li>更新收据和交易（数据格式和字段变更）</li>
<li>更多订阅类型的接口</li>
<li>相同的 StoreKit 框架</li>
</ul>
<h4 data-id="heading-2">2.1、StoreKit 2 for Swift only</h4>
<p><code>StoreKit 2 for Swift only</code>！没错！仅适用于 <strong>Swift</strong> ！<code>StoreKit 2</code> 利用 Swift的最新特性，包括 Swift并发 等新语言接口，简化在App中获取产品信息、商品产品、处理交易以及管理对内容和订阅的访问。并且，StoreKit 2 只支持 iOS 15+ 。</p>
<blockquote>
<p>还在维护 Objective-C 代码的朋友们，是不是瞬间哭晕在洗手间！与新特性无缘，所以现在就是开始学习 Swift 的最佳时刻了，再不学 Swift 开发，连 iOS 开发都不能愉快进行啊~</p>
</blockquote>
<h5 data-id="heading-3">2.1.1、<strong>StoreKit v2 和 v1 是什么关系呢？</strong></h5>
<p>我们开发者要怎么选择呢？苹果在<a href="https://developer.apple.com/documentation/storekit/choosing_a_storekit_api_for_in-app_purchase" target="_blank" rel="nofollow noopener noreferrer">选择文档</a>在给出了答案：</p>
<ul>
<li><a href="https://developer.apple.com/documentation/storekit/in-app_purchase" target="_blank" rel="nofollow noopener noreferrer">In-App Purchase</a>: 一个基于 Swift 的 API，以 JSON Web Signature (JWS) 格式提供 Apple 签名交易验证，从 iOS 15、macOS 12、tvOS 15 和 watchOS 8 开始提供。</li>
<li><a href="https://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase" target="_blank" rel="nofollow noopener noreferrer">Original API for In-App Purchase</a>: 一个使用 App Store 收据提供交易信息的API，从 iOS 3、macOS 10.7、tvOS 9 和 watchOS 6.2 开始提供。</li>
</ul>
<p>苹果现在把原来的 StoreKit v1 定义为 <code>Original API for In-App Purchase</code>，StoreKit v2 定义为 <code>In-App Purchase</code>。（小编注：目前来说，使用 v1 和 v2 版本都可以实现完整的 IAP 购买流程，区别就是 v2 必须使用 Swift 开发，同时提供更加强大的 APIs。）</p>
<h5 data-id="heading-4">2.1.2、<strong>现在什么情况下还需要使用 StoreKit v1 呢？</strong></h5>
<p>很好理解，因为 StoreKit v2 目前是重新设计实现，所以部分 v1 提供的 IAP API 在 v2 版本还没有提供相应的 API，所以还需要使用 v1 版本。</p>
<p><strong>如果您的应用程序依赖于以下任何功能，您可能需要使用原始的应用程序内购买API：</strong></p>
<ol>
<li>为批量购买计划（VPP，Volume Purchase Program）提供支持。有关更多信息，请参阅 <a href="https://developer.apple.com/documentation/devicemanagement" target="_blank" rel="nofollow noopener noreferrer">设备管理</a>。</li>
<li>提供应用预订（app pre-orders）。有关更多信息，请参阅 <a href="https://developer.apple.com/app-store/pre-orders/" target="_blank" rel="nofollow noopener noreferrer">应用预订</a>。</li>
<li>您的 App 从收费更改为免费 App，反之亦然。</li>
<li>对现有和历史遗留的旧 App 使用 v1 API。</li>
</ol>
<p><strong>小编注解：</strong></p>
<ul>
<li>批量购买是针对批量部署设备使用，比如学校有 iPad 提供给学习，可以批量购买应用。</li>
<li>判断用户是否为预订状态时，需要使用 receipt 收据里提供的字段 <a href="https://developer.apple.com/documentation/appstorereceipts/responsebody/receipt" target="_blank" rel="nofollow noopener noreferrer">preorder_date</a>，而 v2 IAP 里已经弃用了 receipt 收据字段。flag：后续有时间，小编在单独写一篇文章来说说应用预订吧。（觉得好就点个赞吧~）</li>
<li>App 在 App Store 更改为收费或者免费模式，在 App 里想查询用户购买历史，需要在 receipt 收据里查询。</li>
</ul>
<h4 data-id="heading-5">2.2、Powerful new APIs</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa046397a964421ea5ec2b467be70e52~tplv-k3u1fbpfcp-watermark.image" alt="16239023498872.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>StoreKit 2</code> 提供了以上更新的类(方法)来轻松访问 IAP 接口，可以理解为增强的版本，详细下文会讲解。</p>
<ul>
<li><strong>Products</strong>：有关在 App Store Connect 中配置的内购品项的信息</li>
<li><strong>Purchases</strong>：更新购买品项接口的可选参数，可绑定用户ID</li>
<li><strong>Transaction info</strong>：更新交易信息的内容格式</li>
<li><strong>Transaction history</strong>：提供查询交易历史记录的接口</li>
<li><strong>Subscription status</strong>：提供订阅品项的状态查询接口</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e40b522708de4566a72d68d6e32597d3~tplv-k3u1fbpfcp-watermark.image" alt="16239024399034.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Product 类增加了品项的类型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> consumable: <span class="hljs-type">Product</span>.<span class="hljs-type">ProductType</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> nonConsumable: <span class="hljs-type">Product</span>.<span class="hljs-type">ProductType</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> nonRenewable: <span class="hljs-type">Product</span>.<span class="hljs-type">ProductType</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> autoRenewable: <span class="hljs-type">Product</span>.<span class="hljs-type">ProductType</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时也扩展订阅类型的信息。订阅类型的品项，包含 <code>isEligibleForIntroOffer</code>，这个字段的作用是判断，用户是否有资格使用优惠价格进行订阅。借助 StoreKit 2，我们以后就可以更轻松地确定客户是否符合您的推介促销优惠的条件。关于订阅类型的复杂度这里就不展开了，大多数同学可能也接触不多，详细可查看<a href="https://developer.apple.com/cn/app-store/subscriptions/" target="_blank" rel="nofollow noopener noreferrer">自动续期订阅</a> 。</p>
<p>另外，StoreKit 2 向前兼容原来的 Product，添加称为 <code>BackingValue</code> 的包装类型来实现这一点，用于与 App Store 通信的数据类型。详见文档：<a href="https://developer.apple.com/documentation/storekit/backingvalue" target="_blank" rel="nofollow noopener noreferrer">BackingValue</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d42a66f1c8ed44e3ac5bfbc18a03177a~tplv-k3u1fbpfcp-watermark.image" alt="16239024780063.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了原有的请示品项信息外，购买时，增加了一些可选参数 <code>Purchase opthons</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d8a31a5e69b44f5a87356e8336d48bd~tplv-k3u1fbpfcp-watermark.image" alt="16239025159619.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了购买数据、<a href="https://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase/subscriptions_and_offers/implementing_promotional_offers_in_your_app" target="_blank" rel="nofollow noopener noreferrer">促销优惠</a> 外，最重要的是新字段：<code>App account token</code>！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3ad9d5414c547b5b7b621738e07e091~tplv-k3u1fbpfcp-watermark.image" alt="16239025509939.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>开发者创建 <code>App account token</code></li>
<li>关联到 App 里的用户账号</li>
<li><code>App account token</code> 使用 <code>UUID</code> 格式</li>
<li>在交易(Transcation)订单中永久保存</li>
</ul>
<p>这个 <code>App account token</code> 是给开发者将用户的 ID 绑定到交易(Transcation)中，也就是把苹果的交易订单数据与用户信息进行映射，可以起到防止充值掉单的问题啊~</p>
<p>示例代码：</p>
<pre><code class="hljs language-Swift copyable" lang="Swift"><span class="hljs-keyword">let</span> uuid <span class="hljs-operator">=</span> <span class="hljs-type">Product</span>.<span class="hljs-type">PurchaseOption</span>.appAccountToken(<span class="hljs-type">UUID</span>.<span class="hljs-keyword">init</span>(uuidString: <span class="hljs-string">"uid"</span>)<span class="hljs-operator">!</span>)

<span class="hljs-comment">//Begin a purchase.</span>
<span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> <span class="hljs-keyword">await</span> product.purchase(options: [uuid])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小编注：<code>UUID</code> 是苹果定义的接口 <code>UUID().uuidString</code> 获取，格式如：<code>4713AE2D-11A5-40EA-B836-CBCD1EC96A76</code>。如果需要关联 用户ID 和开发者订单号，需要开发者自动映射，或者服务器端生成返回等。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec003af63aa34c29a53f728b0184b241~tplv-k3u1fbpfcp-watermark.image" alt="16239025928468.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>签名的交易(Transcation)信息:</p>
<ul>
<li>每笔交易一个对象</li>
<li>签名的交易信息，数据格式使用 JWS（JSON Web Signature）</li>
<li>使用原生接口读取数据</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02937fb09618414d8682daa40bcb66a9~tplv-k3u1fbpfcp-watermark.image" alt="16239043337129.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里插入一下 <a href="https://developer.apple.com/videos/play/wwdc2021/10174/" target="_blank" rel="nofollow noopener noreferrer">Manage in-app purchases on your server</a> 里讲解使用 JWS 数据格式的原因：</p>
<ul>
<li>1、增强安全性</li>
<li>2、更容易解码</li>
<li>3、不用连接苹果服务器验证，开发者本地就可以单独验单！</li>
</ul>
<blockquote>
<p>小编注：JSON Web Token（JWT）是一个规范，这个规范允许我们使用JWT在两个组织之间传递安全可靠的信息。JWT并不等于JWS（JSON Web Signature），JWS只是JWT的一种实现，除了JWS外，JWE(JSON Web Encryption)也是JWT的一种实现。详细查看 <a href="https://tools.ietf.org/html/rfc7515" target="_blank" rel="nofollow noopener noreferrer">JWS (RFC 7515)</a>
JWS的主要目的是保证了数据在传输过程中不被修改，验证数据的完整性。但由于仅采用Base64对消息内容编码，因此不保证数据的不可泄露性。所以不适合用于传输敏感数据。<a href="https://www.jianshu.com/p/50ade6f2e4fd" target="_blank" rel="nofollow noopener noreferrer">引用</a></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331fe6b953da4c38a2945eed6d545361~tplv-k3u1fbpfcp-watermark.image" alt="16239044220386.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里简单的说一下，拿到的 JWS 格式的 transaction info 格式：</p>
<pre><code class="hljs language-JWT copyable" lang="JWT">Base64() + "." + Base64(payload) + "." + sign( Base64(header) + "." + Base64(payload) )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 header 与 payload 通过 header 中声明的 alg 加密方式，使用密钥 secret 进行加密，生成签名。然后逆向构造过程，decode出 JWT 的三个部分：</p>
<ol>
<li>头部（Header）</li>
<li>载荷（PayLoad）</li>
<li>签名（signature）</li>
</ol>
<p>验证相关的文档和流程可查看 <a href="https://developer.apple.com/documentation/appstoreserverapi" target="_blank" rel="nofollow noopener noreferrer">App Store Server API</a>，这里就不展开了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be5e2d2f1d354d529eaac790c0ea3b5d~tplv-k3u1fbpfcp-watermark.image" alt="16239027920065.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2021/10114" target="_blank" rel="nofollow noopener noreferrer">视频中</a> 展示了一个完整的 Demo 示例，这里就不展开了。可以自动 <a href="https://developer.apple.com/documentation/storekit/in-app_purchase/implementing_a_store_in_your_app_using_the_storekit_api" target="_blank" rel="nofollow noopener noreferrer">下载 Dmeo</a> 查看。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224a5b9e45984f5e927e387ad21cf8e1~tplv-k3u1fbpfcp-watermark.image" alt="16239028261035.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>提供了三个新的交易(Transcation)相关的 API:</p>
<ol>
<li>All transactions：全部的购买交易订单</li>
<li>Latest transactions：最新的购买交易订单。（分为订阅品项和除订阅品项外的所有类型二种）</li>
<li>Current entitlements：当前用户有购买的权限。（全部的订阅品项、和非消耗品项）</li>
</ol>
<pre><code class="hljs language-Swift copyable" lang="Swift"><span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">15.0</span>, <span class="hljs-keyword">macOS</span> <span class="hljs-number">12.0</span>, <span class="hljs-keyword">tvOS</span> <span class="hljs-number">15.0</span>, <span class="hljs-keyword">watchOS</span> <span class="hljs-number">8.0</span>, <span class="hljs-operator">*</span>)
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Product</span> </span>&#123;

    <span class="hljs-comment">/// The most recent transaction for the product, or `nil` if the user has never purchased this product.</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> latestTransaction: <span class="hljs-type">VerificationResult</span><<span class="hljs-type">Transaction</span>>? &#123; <span class="hljs-keyword">get</span> <span class="hljs-keyword">async</span> &#125;

    <span class="hljs-comment">/// The transaction that entitles the user to this product, or `nil` if the user is not currently entitled to</span>
    <span class="hljs-comment">/// this product.</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> currentEntitlement: <span class="hljs-type">VerificationResult</span><<span class="hljs-type">Transaction</span>>? &#123; <span class="hljs-keyword">get</span> <span class="hljs-keyword">async</span> &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>反正就是很强大的接口：</p>
<pre><code class="hljs language-Swift copyable" lang="Swift"><span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">15.0</span>, <span class="hljs-keyword">macOS</span> <span class="hljs-number">12.0</span>, <span class="hljs-keyword">tvOS</span> <span class="hljs-number">15.0</span>, <span class="hljs-keyword">watchOS</span> <span class="hljs-number">8.0</span>, <span class="hljs-operator">*</span>)
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Transaction</span> </span>&#123;

    <span class="hljs-comment">/// A sequence of every transaction for this user and app.</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> all: <span class="hljs-type">Transaction</span>.<span class="hljs-type">TransactionSequence</span> &#123; <span class="hljs-keyword">get</span> &#125;

    <span class="hljs-comment">/// Returns all transactions for products the user is currently entitled to</span>
    <span class="hljs-comment">///</span>
    <span class="hljs-comment">/// i.e. all currently-subscribed transactions, and all purchased (and not refunded) non-consumables</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> currentEntitlements: <span class="hljs-type">Transaction</span>.<span class="hljs-type">TransactionSequence</span> &#123; <span class="hljs-keyword">get</span> &#125;

    <span class="hljs-comment">/// Get the transaction that entitles the user to a product.</span>
    <span class="hljs-comment">/// - Parameter productID: Identifies the product to check entitlements for.</span>
    <span class="hljs-comment">/// - Returns: A transaction if the user is entitled to the product, or `nil` if they are not.</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">currentEntitlement</span>(<span class="hljs-params">for</span> <span class="hljs-params">productID</span>: <span class="hljs-type">String</span>)</span> <span class="hljs-keyword">async</span> -> <span class="hljs-type">VerificationResult</span><<span class="hljs-type">Transaction</span>>?

    <span class="hljs-comment">/// The user's latest transaction for a product.</span>
    <span class="hljs-comment">/// - Parameter productID: Identifies the product to check entitlements for.</span>
    <span class="hljs-comment">/// - Returns: A verified transaction, or `nil` if the user has never purchased this product.</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">latest</span>(<span class="hljs-params">for</span> <span class="hljs-params">productID</span>: <span class="hljs-type">String</span>)</span> <span class="hljs-keyword">async</span> -> <span class="hljs-type">VerificationResult</span><<span class="hljs-type">Transaction</span>>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62f1bd820207416f8d504189235d6f96~tplv-k3u1fbpfcp-watermark.image" alt="16239028673420.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Current entitlements</code> 这个目前是，方便开发者直接通过接口就能读取当前用户可用的订阅品项和非消耗品项，不用开发者做硬编码写死 productID 请求苹果查询，直接一个接口搞定！特别是对个人开发者来说，确定是很方便，不用搭服务器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9719b483ae804e04b3bac2091d66f8e0~tplv-k3u1fbpfcp-watermark.image" alt="16239028962697.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查询同一个用户在不同的设备上的交易订单，假设用户在 A 设备购买了一笔交易订单，那么在用户的 B 设备上，可以实时查到这个购买的交易订单。苹果工程师说，一般系统会自动刷新，逼不得已不需要使用同步接口刷新。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b935e1a3aaf4e32b9d21f5c6f0de095~tplv-k3u1fbpfcp-watermark.image" alt="16239029211953.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般情况下，第一次打开 App 时，开发者就可以通过 StoreKit 2 提供的接口在后台实时帮用户恢复购买记录。对于非消耗品项，用户在一个新设备时，可能需要提供给用户恢复购买记录的 UI 入口。而对于订阅类型，比如某个视频网站的月卡，虽然都是登陆一个苹果账号，但是购买时，是绑定到视频网络的用户的，不是绑定到苹果账号下，所以，订阅类型可能就无法直接恢复啊。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c400759d18df41ea980830d4bd132a0a~tplv-k3u1fbpfcp-watermark.image" alt="16239029565139.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有的交易都可以用在所有的 StoreKit 接口；使用 StoreKit v1 的购买记录，在 v2 的接口也可以获取到；使用 v2 进行的购买可在统一收据中获得。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0226732430e94bceb37427d3d70b1bb7~tplv-k3u1fbpfcp-watermark.image" alt="16239029829279.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>订阅类型项目的状态，比如获取最新的交易、获取更新订阅的状态，获取更新订阅的信息等。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51b8e9f90a814c5087d59d4c9e353be3~tplv-k3u1fbpfcp-watermark.image" alt="16239030330448.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中获取更新订阅的信息，可以获取更新的状态、品项 id、如果过期的话，可以知道过期的原因。（比如用户取消、扣费失败、订阅正常过期等。），获取的所有数据都是 JWS 格式验证。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b76d43d2f8334ccaab0e99bc6f19bbb3~tplv-k3u1fbpfcp-watermark.image" alt="16239037808982.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，是签名校验，上面已经提到，这里就不在展开。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3860df68e0ac4a9a8b9012513b07eea5~tplv-k3u1fbpfcp-watermark.image" alt="16239038068883.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>苹果工程师建议，因为校验是用到 bundle ID (应用包名)，所以建议是写死硬编码，不要读取 info.plist 文件配置。然后按规则格式进行验证 payload 是否被篡改。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f9ae01e02ea4825b346d4b839ede901~tplv-k3u1fbpfcp-watermark.image" alt="16239038541866.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>StoreKit v2 提供了验证 JWS 格式的 API，开发者可以直接调用，不需要自行解析。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd1e68df89c4cb780a5f2b9360214a2~tplv-k3u1fbpfcp-watermark.image" alt="16239039254740.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>StoreKit v2 总结来说，强大的新 IAP 接口，新的 JWS 交易信息格式，交易详细内容和历史接口，额外的订阅类型信息。总之，牛逼~</p>
<h4 data-id="heading-6">2.3、Manage subscriptions API</h4>
<h5 data-id="heading-7">How can subscribers manage their subscription inside my app?</h5>
<p>订阅者如何在我的应用内管理他们的订阅？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/231142a320944c0daed9b4dbaf05176b~tplv-k3u1fbpfcp-watermark.image" alt="16239121193616.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>提供了新的 API，可以直接在开发者 App 中显示用户当前的订阅品项界面，不用在跳转到 App Store 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bdda201b3f467ea312c9c37d9a367b~tplv-k3u1fbpfcp-watermark.image" alt="16239121374973.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接口如上，调用后，打开的界面如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/416d9505615c419ea0563074d0d4bd28~tplv-k3u1fbpfcp-watermark.image" alt="16239122177825.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以在开发者 App 中取消订阅、升级或降级订阅等级等。</p>
<h4 data-id="heading-8">2.4、Request refund API</h4>
<h5 data-id="heading-9">How can customers request a refund inside my app?</h5>
<p>客户如何在我的应用内申请退款？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27de47bd950e40a2ad45fe0bce4826f7~tplv-k3u1fbpfcp-watermark.image" alt="16239122897971.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>提供新的 Request refund API，允许用户在开发者的 App 中直接进行退款申请。</p>
<p>用户进行申请退款后，App 可以收到通知、另外苹果服务器也会通知开发者服务器（下文会有说），退款测试在沙盒环境下，可以进行测试啦！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dd76dd902df4235882327260c0fe87a~tplv-k3u1fbpfcp-watermark.image" alt="16239123152291.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接口如上，调用后，打开的界面如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5e23951f0a4965a6adb2f0be7ce7af~tplv-k3u1fbpfcp-watermark.image" alt="16239123369438.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用户退款的流程界面（这个是系统的界面），所以可能对用户是很方便啦，对开发者来说，可能就需要在考虑一下？</p>
<h3 data-id="heading-10">三、Server to Server</h3>
<p>接下来，我们说说，苹果服务器 API 接口的更新。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acc1cbcb437c417dae8c56e926292dcd~tplv-k3u1fbpfcp-watermark.image" alt="16239041139339.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图，苹果服务器、用户设备、开发者服务器，三者之间的交互越来越多，随着苹果的迭代和开放，三者如今已经成循环~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b0e67752060437e8d9d9513139cafea~tplv-k3u1fbpfcp-watermark.image" alt="16239040419267.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>构建开发者的服务器：</p>
<ol>
<li>接收苹果内购的状态改变通知</li>
<li>通过接口跟踪内购状态改变</li>
<li>随时验证访问权限(就是用户的购买是不是有效的，比如用户退款了)</li>
<li>管理订单状态</li>
<li>跟踪退款</li>
</ol>
<p>接下来，将会从以上几个方面展开说：</p>
<h4 data-id="heading-11">3.1、Validate status with receipts</h4>
<p>Receipt 收据验证方式：</p>
<ol>
<li>在用户设备App中验证收据</li>
<li>在开发者服务端通过苹果 <code>/verifyReceipt</code> 接口验证收据</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/410e9ceeed1940c78635f37ffb9debf8~tplv-k3u1fbpfcp-watermark.image" alt="16239042732936.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>旧的 receipts 收据内容如上图。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/468683656d6b41669d326b906f2914ab~tplv-k3u1fbpfcp-watermark.image" alt="16239044220386.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新的 JWS 格式的交易格式内容，如上图。对比 receipts 收据，可以知道有那些变化：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a86119e5abad4a38b506e3a41dd0f1b3~tplv-k3u1fbpfcp-watermark.image" alt="16239046070348.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>旧的有 GMT（格林威治标准时间）、PST（太平洋标准时间）、Unix timestamp（Unix 时间戳），新的格式，只保留了 <code>Unix 时间戳</code>，并且字段做了更新。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5541d86377ff495fb4091dd545e716bd~tplv-k3u1fbpfcp-watermark.image" alt="16239046340854.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>内购的类型，也有返回了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5056435e958b46fcaab891402bab0b4a~tplv-k3u1fbpfcp-watermark.image" alt="16239046558338.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个就是上面提到的关系的用户信息的 UUID。这里苹果用 <code>appAccountToken</code> 字段。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8075281e284e1b84bbd33cc3936331~tplv-k3u1fbpfcp-watermark.image" alt="16239046878608.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个是用户退款时间和退款原因的字段。从之前的 <code>cancellation_date</code> 改成现在的 <code>revocationData</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ab055faf0dd43a8936d6ce6f5c8c04b~tplv-k3u1fbpfcp-watermark.image" alt="16239047119969.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后是促销优惠的类型。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f394c9ea3d34c3796118fa63b2616dd~tplv-k3u1fbpfcp-watermark.image" alt="16239047433331.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>验证签名信息，这里就不多说了，上文已经说过了。</p>
<h4 data-id="heading-12">3.2 Check status with APIs</h4>
<p><strong>使用 APIs 检查状态</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c30d292bbfff488a994cace47559aade~tplv-k3u1fbpfcp-watermark.image" alt="16239049485781.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新提供了2个接口：</p>
<ol>
<li>订阅品项状态查询 API</li>
<li>内购历史订单查询 API</li>
</ol>
<h5 data-id="heading-13">获取用户所有订阅的状态</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b648bf0361704b3895b470e2e4a0c9dd~tplv-k3u1fbpfcp-watermark.image" alt="16239049731702.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先来看看订阅品项状态查询 API。需要参数只有一个：<code>originalTransactionId</code>，这个大家很熟悉了，就不展开了。详细文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/get_all_subscription_statuses" target="_blank" rel="nofollow noopener noreferrer">Get All Subscription Statuses</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0983a7876cda43f5856151eb935afa92~tplv-k3u1fbpfcp-watermark.image" alt="16239052348234.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接口请求和返回的数据格式示意如上。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/586b808a87a04b819a2b033cb350667f~tplv-k3u1fbpfcp-watermark.image" alt="16239052667517.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>lastTransactions</code> 是最后的订阅状态，1是有效，2是过期，3是账号扣费重试，4是账号宽限期(这个是开发者设置，比如到期扣费失败时，可以给用户延期多长时间。)，5是已经撤销。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15154efceee343af943a6d365fde5c0d~tplv-k3u1fbpfcp-watermark.image" alt="16239053630326.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对 <code>signedTransactionId</code> 进行 JWS 解码后的内容，就是单个更新订阅类型的数据内容。</p>
<h5 data-id="heading-14">获取交易的历史订单</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f71e4eb03e4c50a11835d1dc4c7389~tplv-k3u1fbpfcp-watermark.image" alt="16239053896385.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>获取用户的交易历史记录，包括他们在你的 App 中的所有应用内购买。 也是只需要参数一个：<code>originalTransactionId</code>，注意，只需要是用户的任意一个交易的 originalTransactionId 就可以啦。这个大家一看就明白了，就不展开了。详细文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/get_transaction_history" target="_blank" rel="nofollow noopener noreferrer">Get Transaction History</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f9204239eb463f82a98be56b840c38~tplv-k3u1fbpfcp-watermark.image" alt="16239054248179.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的是，这个返回的数据有一个字段 <code>hasMore</code> 为 ture，表示有更新的历史订单有更新，默认是 20 条。目前开发者不能控制这个条数。</p>
<h5 data-id="heading-15">App Store Server API 验证</h5>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf8e153faf4d454d9a0e39f1172790ed~tplv-k3u1fbpfcp-watermark.image" alt="16239054795105.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>App Store Server 接口标准：</p>
<ul>
<li>JWT 认证</li>
<li>JWS 交易内容格式</li>
<li>Json 请求和响应</li>
<li>基于 originalTransactionId 标识参数</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b09de643c0b4ba1826943283568f761~tplv-k3u1fbpfcp-watermark.image" alt="16239056226807.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有的 App Store Server API 接口都必须使用 JWT 认证，关于验证规则和流程，请查看文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/generating_tokens_for_api_requests" target="_blank" rel="nofollow noopener noreferrer">Generating Tokens for API Requests</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0673f69d73446afbbf2dd6d70ce95b0~tplv-k3u1fbpfcp-watermark.image" alt="16239056616443.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在苹果后台生成私钥的示例，详见文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/creating_api_keys_to_use_with_the_app_store_server_api" target="_blank" rel="nofollow noopener noreferrer">Creating API Keys to Use With the App Store Server API</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/786d09df5b1249039f2c006966cb3f3d~tplv-k3u1fbpfcp-watermark.image" alt="16239057988349.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>验证可查看文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/generating_tokens_for_api_requests" target="_blank" rel="nofollow noopener noreferrer">Generating Tokens for API Requests</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e972648c5648492c93fc6a73ef8eed63~tplv-k3u1fbpfcp-watermark.image" alt="16239058531137.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，如果需要使用 App Store Server API 查询订阅品项状态或用户的历史订单，关键要点：</p>
<ul>
<li>独立的状态和历史功能</li>
<li>只需要提供 originalTransactionId</li>
<li>获取已验证签名的交易并存储必要字段（比如 <code>originalTransactionId</code>）</li>
<li>无需存储已验证签名的完整交易数据（也就是验证过的 JWS 内容，只需要保存 originalTransactionId 字段就可以了，<code>一个字段走天下！给我们点个赞吧~</code>）</li>
</ul>
<h4 data-id="heading-16">3.3、Track status with notifications</h4>
<p><strong>通过通知跟踪状态！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b763a55e47344492a7a661593727581d~tplv-k3u1fbpfcp-watermark.image" alt="16239059171973.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>苹果服务器的通知更新，苹果说很好，开发者可以接受通知、更新的状态也及时？不需要开发者主动请求询问！行吧，你说的都对~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d962ed7cd0a4b65a8f7a9d41ae2893d~tplv-k3u1fbpfcp-watermark.image" alt="16239059397630.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>苹果服务器通知 v2 版本的更新，这里就不展开了。好像没有什么好说的，跟上文的差不多。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad917750bd294a019b8cf3a849524ccd~tplv-k3u1fbpfcp-watermark.image" alt="16239059639867.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要变动是，通知的类型，有一部分是删除了，也新增了一些通知类型。</p>
<blockquote>
<p>小编注：变动的原因，有很多方面，主要是苹果的自动订阅类型品项，越来越复杂了，所以有一些字段意义已经不大，另外，苹果新推出的家庭共享功能，主账号可以授权家庭子账号或者撤销授权。所以 <code>CANCEL</code> 取消类型就不明确意义了，所以更新为 <code>REVOKE</code> 撤销，他的含义和作用更多，可以是用户申请退款或者授权取消，都是撤销的一个。</p>
</blockquote>
<p>当然，这里变动这么多，苹果不可能在原来的接口直接改啊！所以是有 v1 和 v2 接口，开发者可以设置，下文会提到，这些先略过。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaa0cde8c3c14e45bc3c90a3b8ec6202~tplv-k3u1fbpfcp-watermark.image" alt="16239060034850.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外，订阅的类型下，还有子类型。这个也好理解。比如 <code>SUBSCRIBED</code> 订阅，可以是首次订阅的状态，也可以是重新订阅的状态，都是订阅。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/042daa6f8cb34627a3271912bd34610a~tplv-k3u1fbpfcp-watermark.image" alt="16239060511979.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就展开了通知主类型，有那些子类型。如下这些，就不展开了，大家看看图片就好：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4d755307ea64634ac45400f40470380~tplv-k3u1fbpfcp-watermark.image" alt="16239060729187.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8f124d469845c48aaf84689e7f2599~tplv-k3u1fbpfcp-watermark.image" alt="16239060939542.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/595b85f112284e2c89f17b27497314a5~tplv-k3u1fbpfcp-watermark.image" alt="16239064391553.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，关于订阅，有非常多的状态，所以，订阅品项的通知的复杂度就不言而喻！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd2f4da5480647db8ebaf69b87f3aeab~tplv-k3u1fbpfcp-watermark.image" alt="16239064941047.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结来说，App Store server notifications V2 提供了多达20多种通知类型！子类型提供了更精细的通知类型！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5990dd90b80b4829a5ab25d7bf13e852~tplv-k3u1fbpfcp-watermark.image" alt="16239065374167.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后就是通知返回的内容，多了一个 <code>subtype</code> 子类型，还有对应的 <code>version</code> 为 2 表示 App Store server notifications V2 版本。</p>
<h4 data-id="heading-17">3.4、New purchase flow</h4>
<p><strong>新的购买流程处理</strong></p>
<p>最后，总结一下，提供了服务端新查询接口后，对开发者服务器有那些变动和更新注意事项等。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95c0f7bb02184ccb84906d3d67d642ae~tplv-k3u1fbpfcp-watermark.image" alt="16239066426944.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于首次订阅的购买，流程上的变化是，开发者 App 与开发者服务器完成订阅流程后，苹果服务器也会发送通知 <code>SUBSCRIBED + INITAL_BUY</code>，然后开发者服务器可以随时通过接口 <code>inApps/v1/subscriptions</code> 随时查询用户订阅项目的状态，不用等苹果服务器的通知也可以啦！避免了开发者处于被动的情况，更好的实时获取。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aa2a1951a7243ac9335325b0a7070a9~tplv-k3u1fbpfcp-watermark.image" alt="16239067594678.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>订阅更新，也是开发者服务器随时通过接口 <code>inApps/v1/subscriptions</code> 随时查询用户订阅项目的状态。是不是爽歪歪啦~ 点个赞吧~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10d5bb3735494c6bac84b248515ffac4~tplv-k3u1fbpfcp-watermark.image" alt="16239068048310.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>订阅类型的账单宽限期和计费重试，也是同样的道理，苹果服务器会发通知 <code>DID_FAIL_TO_RENEW</code> 、<code>DID_RECOVER</code> 给开发者服务器，开发者服务器随时通过接口 <code>inApps/v1/subscriptions</code> 随时查询用户订阅项目的状态，然后对 App 里用户实时操作和限制等。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fe53e573ee74427ba8077447c1a5a03~tplv-k3u1fbpfcp-watermark.image" alt="16239068526652.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首次消耗型购买，还是一样。不同的时，开发者可以用 receipt 收据或者使用 StoreKit v2 新的 signed transactiond 来验证订单啊。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f4c362550cd488fb1bbe0028d9b4b3c~tplv-k3u1fbpfcp-watermark.image" alt="16239069844456.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而用户退款，也出现了新的时代！除了苹果服务器的通知退款 <code>REFUND</code> 后，开发者现在可以主动通过 <code>inApps/v1/history</code> 接口，查询用户的所有交易订单，来确认订单的状态是不是退款（撤销）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66d94b0286c44ca781fd0c5849868821~tplv-k3u1fbpfcp-watermark.image" alt="16239070273983.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是订阅类型的退款，开发者服务器就通过接口 <code>inApps/v1/subscriptions</code> 随时查询用户订阅项目的最新状态。</p>
<h4 data-id="heading-18">3.5、Migrating to JWS transactions</h4>
<p><strong>迁移到 JWS 格式交易验证</strong></p>
<p>对于 StoreKit v2 新的接口，苹果已经弃用了 receip 收据验证，所以，对于开发者来说，应该怎么迁移到新的 JWS 格式验证呢？所以，苹果给出了方案：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f79912305724f0693eb3acde74cf8ea~tplv-k3u1fbpfcp-watermark.image" alt="16239070600438.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果开发者需要兼容 StoreKit v1 版本，那么还可以使用 receipt 收据通过苹果接口 <code>/verifyReceipt</code> 验证收据，收据中是包含 <code>originalTransactionId</code> 的，所以，可以开发者可以通过 <code>inApps/v1/history</code> 接口，随时了解交易的状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b11d6d8ca5446c8493e7d2aa4140f2~tplv-k3u1fbpfcp-watermark.image" alt="16239071180996.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>订阅类型，就通过 <code>inApps/v1/subscriptions</code> 接口查询。</p>
<h4 data-id="heading-19">3.6 Manage family sharing</h4>
<p><strong>管理家庭共享</strong></p>
<p>目前苹果对 <code>非消耗型</code> 和 <code>自动订阅</code> 类型品项是支持 <code>家庭共享</code>（family sharing），另外，苹果会返回一个字段 <code>inAppOwnershipType</code> 表示当前用户是否为购买品项的主用户。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad2fb18714fa46f8b8456d9b5c559ec7~tplv-k3u1fbpfcp-watermark.image" alt="16239071832278.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f00c22ab3ca48f58dc98ce8524c0147~tplv-k3u1fbpfcp-watermark.image" alt="16239072831797.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>家庭共享更新了新的通知，增加了4个类型的通知。</p>
<h3 data-id="heading-20">四、Customer support & Handle refunds（客服支持和退款处理）</h3>
<p>终于来到最后的一节啦！也是很重要的内容，关于用户服务支持和用户申请退款的处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f0ce7d444c647dca088ccb073ea245b~tplv-k3u1fbpfcp-watermark.image" alt="16239081962075.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以前，用户关于内购有问题时，只能自己解决，并且是通过电话、邮件、苹果支持 App、网站、论坛等方式，对用户非常的不友好！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca0d972c425c4187a252d92d835ea905~tplv-k3u1fbpfcp-watermark.image" alt="16239082201717.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般用户遇到问题的情场有那些呢？</p>
<h4 data-id="heading-21">4.1、How do I identify the in-app purchase made by this customer?</h4>
<p><strong>如何识别该客户进行的应用内购买？</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/428b5b9f7a3045e4ac815c2564fad020~tplv-k3u1fbpfcp-watermark.image" alt="16239077635884.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个就是前言提到的用户收到苹果的收据发票时，无法与开发者的订单匹配的问题！现有有新的  API 来解决了：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/532df993904e4411aeacaaf2b45f8ca5~tplv-k3u1fbpfcp-watermark.image" alt="16239100558324.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个新的接口，可以让用户提供的发票上的 <code>ORDER ID</code> 查到对应的 transaction 交易信息。</p>
<blockquote>
<p>小编注：目前2021-06-17，在 <a href="https://developer.apple.com/documentation/appstoreserverapi/" target="_blank" rel="nofollow noopener noreferrer">苹果接口文档</a> 还没有看到此接口，不清楚是没有更新，不是说在开发中....</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46c79fd1bb0f48f5802b7f160bdbd322~tplv-k3u1fbpfcp-watermark.image" alt="16239100916898.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，整个流程，主是这样，用户客诉，提供订单 ID，查询到状态，为用户进行补单或者支持服务。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b31171e0be024c14abcbe81af8508e7f~tplv-k3u1fbpfcp-watermark.image" alt="16239101410506.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>返回的数据格式都是一样的，这里也不展开了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc7b0f769ec46e6aca73a2d72899c7e~tplv-k3u1fbpfcp-watermark.image" alt="16239102303111.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，开发者服务器记得保存对应的用户订单 ID，做好映射？</p>
<h4 data-id="heading-22">4.2、How do I lookup this customer's past refunds?</h4>
<p><strong>我如何查找该客户过去的退款？</strong></p>
<p>同样的，苹果提供了查询所有内购订单的接口，但是不可能让开发者查一次，然后在判断那些是退款订单吧！所以，苹果提供了另一个接口：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81723f303803410e8e6c117cf8579312~tplv-k3u1fbpfcp-watermark.image" alt="16239103365900.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个接口也是一样，通过用户的任一个 <code>originalTransactionId</code> 可以查到这个用户的所有退款记录订单。</p>
<blockquote>
<p>小编注：目前2021-06-17，在 <a href="https://developer.apple.com/documentation/appstoreserverapi/" target="_blank" rel="nofollow noopener noreferrer">苹果接口文档</a> 还没有看到此接口，不清楚是没有更新，不是说在开发中....</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18d8a75afbac4c3ab9cb1e68f59d6e2f~tplv-k3u1fbpfcp-watermark.image" alt="16239103707311.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>返回的格式也是一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99396d477439490aa9e2a8524dcc1c26~tplv-k3u1fbpfcp-watermark.image" alt="16239104717153.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用户退款，是有一个单独的 <code>refundDate</code> 字段，如果有内容时间，就表示是退款啊。</p>
<h4 data-id="heading-23">4.3、How do I compensate subscribers for a service issue?</h4>
<p><strong>我如何补偿订阅者的服务问题？</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b43bdcb2a1af48eea2cd46542228917f~tplv-k3u1fbpfcp-watermark.image" alt="16239105380508.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要的问题是，比如开发者服务器宕机了，导致用户无法使用 App 服务，这时候开发者可以想补偿用户，所以开发者可以提供一个内购对兑码（所有的内购类型都可以），在苹果后台那里生成。然后让用户在 App Store 进行兑换，也可以在  App 里通过 <code>presentCodeRedemptionSheet()</code> 接口调用，弹出系统的兑换界面：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68eda4053cc54438aec6bf9f9e989847~tplv-k3u1fbpfcp-watermark.image" alt="16239105730199.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用户通过对兑码进行获取补偿。</p>
<blockquote>
<p>小编注：针对游戏来说，这个对兑码不太适用，因为游戏里有用户账号、游戏区服、角色账号等，对兑的内容，无法自动分配给某个账号某个角色。另外，国内好像都没有这样的补偿习惯？</p>
</blockquote>
<h4 data-id="heading-24">4.4、How do I appease customers for outages or canceled events?</h4>
<p><strong>我如何安抚客户中断或取消的活动？</strong></p>
<p>如果开发者服务器宕机，或者活动取消，这时候可能想安抚用户，然后想补偿用户一些福利，苹果提供了一个新接口：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158d7ec6a398448bacdb038f124eab7a~tplv-k3u1fbpfcp-watermark.image" alt="16239107619065.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个接口的作用：开发者一年有2次机会给订阅内购用户每次加90天免费补偿。也就是有自动订阅类型的 App，可以开发者主动在服务器给用户补偿(免费延长)用户的订单时间，每次最多是90天。</p>
<blockquote>
<p>小编注：目前2021-06-17，在 <a href="https://developer.apple.com/documentation/appstoreserverapi/" target="_blank" rel="nofollow noopener noreferrer">苹果接口文档</a> 还没有看到此接口，不清楚是没有更新，不是说在开发中....</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2265203f29ba4aa5ae3c25219583e8a9~tplv-k3u1fbpfcp-watermark.image" alt="16239107825736.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要在接口给出延长的天数，还有原因代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1c42b565950469e868a6cf6662186b6~tplv-k3u1fbpfcp-watermark.image" alt="16239108097411.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发者服务中断或宕机，导致用户无法使用服务，开发者主动给用户进行补偿。流程图已经很清晰的表达了，这里就不解析了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/370f9aaa794f4d5e9b3f97f64434f273~tplv-k3u1fbpfcp-watermark.image" alt="16239108301837.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发者主动取消了活动，给用户发补偿。</p>
<h4 data-id="heading-25">4.5、Refund notifications</h4>
<p><strong>退款通知</strong></p>
<p>最后，是关于退款通知，在去年 WWDC20 苹果推出的退款通知开发者的流程：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a721b6f02d0249d7a9a5eef0942277a8~tplv-k3u1fbpfcp-watermark.image" alt="16239125000781.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，现在有没有什么好的最佳实践呢？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c0cbf6c9f64402696d37cf8ea873c9e~tplv-k3u1fbpfcp-watermark.image" alt="16239125216212.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>找到最适合你的应对策略：比如，扣除金币、撤销订单服务</li>
<li>考虑对游戏设计的影响</li>
<li>使用营销和促销工具</li>
<li>通过通讯渠道提供清晰的信息（比如推送、邮件或公告等）</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/432521831f8e425b8caea046987e8261~tplv-k3u1fbpfcp-watermark.image" alt="16239125660800.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>苹果深入解决了退款通知的流程，就是开发者收到退款通知时，这个退款可能是48小时内的任意时刻。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4533bcb5b6e4e8f9eb0c88d4f3ab030~tplv-k3u1fbpfcp-watermark.image" alt="16239125846194.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>决定要不要退款，苹果有一个“退款决策系统”（Refund decisioning system）根据用户的信息、设备信息、购买记录和退款记录等，最终决定是否同意用户退款。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50eb102971be4582abe26d2172e37b12~tplv-k3u1fbpfcp-watermark.image" alt="16239126081800.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而现在！苹果增加了一个新的决策影响因素：<code>Developer signals</code>（开发者信号），这个是什么？就是开发者，可以在用户申请退款时，可以把用户的一些信息给到苹果，协助决策系统来决定。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deeff5ba3d1f4b7383a9e262f4cd3b9f~tplv-k3u1fbpfcp-watermark.image" alt="16239126611622.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当用户申请退款时，苹果通知（<code>CONSUMPTION_REQUEST</code>）开发者服务器，开发者可在12小时内，提供用户的信息（比如游戏金币是否已消费、用户充值过多少钱、退款过多少钱等），最后苹果收到这些信息，协助“退款决策系统” 来决定是否允许用户退款！详细见文档：[Send Consumption Information(<a href="https://developer.apple.com/documentation/appstoreserverapi/send_consumption_information" target="_blank" rel="nofollow noopener noreferrer">developer.apple.com/documentati…</a>)</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c7082e3c88f48909167bc9e2a67c6c8~tplv-k3u1fbpfcp-watermark.image" alt="16239127403213.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要提供给苹果的参数，详细可查看文档：<a href="https://developer.apple.com/documentation/appstoreserverapi/consumptionrequest" target="_blank" rel="nofollow noopener noreferrer">ConsumptionRequest</a></p>
<p>需要注意：<code>customerConsented</code> 字段，表示用户是否同意提供消费数据。所以，这个用户的信息，是要求用户允许共享才行！（赶紧加到用户协议里？）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10aba65f52b047a1ad59c6b1d066b951~tplv-k3u1fbpfcp-watermark.image" alt="16239128013091.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增的退款通知类型有2个，一个是请求开发者提供决策信息，另一个是退款拒绝的通知！（当收到用户申请退款被拒绝后，开发者可以考虑做一些安抚用户的操作？）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/623d09becdee4ae8897b351176a76325~tplv-k3u1fbpfcp-watermark.image" alt="16239128268895.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，整个流程图如上！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a6aab64a70490cb036a3e96ef35d25~tplv-k3u1fbpfcp-watermark.image" alt="16239128739220.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个接口是可以测试的，配合上文中提到的，在 App 里提供让用户退款界面和接口时，当发起退款时，这个测试也会通过苹果服务器通知到开发者服务器。另外，今年新增了设置单独的沙盒环境通知URL！（下文会讲到啊~ 点个赞吧~）</p>
<h4 data-id="heading-26">4.6、Support customers & Shared benefits</h4>
<p><strong>客服支持和共享共赢</strong></p>
<p>不管是内购退款，还是内购补偿，其实目的都是为了用户！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b29293ace01d434ead550cc82705e8bd~tplv-k3u1fbpfcp-watermark.image" alt="16239124162360.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>提高留存率</li>
<li>提高客户满意度</li>
<li>更高的参与感</li>
<li>积极评分和写评论</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da7703a7da0440f0a619c5ebe3115106~tplv-k3u1fbpfcp-watermark.image" alt="16239128998796.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>信息更加透明</li>
<li>改进退款流程</li>
<li>为客户提供更好的服务结果</li>
<li>加强沟通</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/782b1cec5db94453bcb3e182270d9ecd~tplv-k3u1fbpfcp-watermark.image" alt="16239131180060.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结：</p>
<ul>
<li>在 App 中添加自定义帮助界面</li>
<li>回顾客户支持的流程优化</li>
<li>设置服务器以接收通知（退款后采取操作）</li>
<li>响应 App Store 的请求用户申请退款的提供信息</li>
</ul>
<h3 data-id="heading-27">五、Sandbox Test</h3>
<p><strong>沙盒测试环境</strong></p>
<p>最后就是沙盒环境的更新！真最后一节啦！给个点赞吧~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edbfbae5038447a8b7b2ef3a2132415f~tplv-k3u1fbpfcp-watermark.image" alt="16239073105619.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>更新现有沙盒账号</li>
<li>订阅状态 API</li>
<li>应用内购买历史记录 API</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/374a969ff2e9475ca54536faff778ea5~tplv-k3u1fbpfcp-watermark.image" alt="16239065861884.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>App Store server notifications 新增沙盒环境的回调 URL 配置！
App Store server notifications 新增沙盒环境的回调 URL 配置！
App Store server notifications 新增沙盒环境的回调 URL 配置！</p>
<p>这个测试以后就方便啦~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6e4651bfdad49f28b665a7f079a31ef~tplv-k3u1fbpfcp-watermark.image" alt="16239066111609.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>App Store server notifications 设置 URL 支持 V1 或者 V2 配置，因为 V2 变动比较大，所以就增加了一个新的版本，不知道明年会不会有 V3？ -.-</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f89c4165a3b45309fc3438f9124cd6a~tplv-k3u1fbpfcp-watermark.image" alt="16239073434938.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>沙盒测试：</p>
<ul>
<li>清历史购买记录</li>
<li>改帐号所在地区</li>
<li>测试订阅过期时间更多选择</li>
<li>TestFlight 验单将失败等。[社会社会]</li>
</ul>
<p><strong>清历史购买记录:</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bf72517f32b4ebaae3d53025dc69a14~tplv-k3u1fbpfcp-watermark.image" alt="16239073612204.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>改帐号所在地区:</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14e8b9c782464c6183a4d17d1dc450c5~tplv-k3u1fbpfcp-watermark.image" alt="16239073896475.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>测试订阅过期时间更多选择：</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fc242c211247b3886bb4b37382870e~tplv-k3u1fbpfcp-watermark.image" alt="16239074196165.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">五、总结</h3>
<p>最后！最后！到了总结的时候啦，此时应该有掌声！点个赞~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88faf9cc358c4e3cb31ed21618be04f4~tplv-k3u1fbpfcp-watermark.image" alt="16239123644085.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前在 <a href="https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/introduction/" target="_blank" rel="nofollow noopener noreferrer">Human Interface Guidelines</a> 人机设计文档看到苹果关于在 App 中给用户提供退款功能的设计，目前的情况来看，应该不是强制要求所有 App 必须在 App 中提供这个退款功能。所以，也是需要开发者进行思考~ 退款和内购，本质是什么？</p>
<p>其实，对于一般的用户，开发者是不会限制用户退款，正常的退款，但总是存在不合理的情况，有恶意退款的，一般游戏的坏帐率有 5%以上，在去年苹果提供退款通知开发者之前，甚至有 20% 以上。举例来说，一亿的5%就是五百万。</p>
<p>那开发者应该怎么考虑内购和退款的问题呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9333465b879b468faf274c07045f0ee0~tplv-k3u1fbpfcp-watermark.image" alt="16239081117002.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>苹果有给出一些提示：</p>
<ul>
<li>管理您与现有客户的关系</li>
<li>提高留存率</li>
<li>提高客户满意度</li>
<li>增加收入</li>
</ul>
<p>所以，做好一个产品，提高用户的满意度，用户满意了，是不是更多愿意使用开发者提供的服务，从而正向循环~</p>
<p>那要不要 App 里提供退款功能呢？</p>
<p>这是一个值得所有开发者思考和探索的问题~</p>
<p>欢迎大家一起在评论区交流~</p>
<blockquote>
<p>欢迎关注我们“<strong>37手游iOS技术运营团队</strong>”，了解更多 iOS 和 Apple 的资讯~</p>
</blockquote>
<h3 data-id="heading-29">参考引用</h3>
<ul>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10114" target="_blank" rel="nofollow noopener noreferrer">Meet StoreKit 2 - WWDC 2021</a></li>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10174/" target="_blank" rel="nofollow noopener noreferrer">Manage in-app purchases on your server - WWDC 2021</a></li>
<li><a href="https://developer.apple.com/videos/play/wwdc2021/10175" target="_blank" rel="nofollow noopener noreferrer">Support customers and handle refunds - WWDC 2021</a></li>
<li><a href="https://developer.apple.com/videos/play/wwdc2020/10661/" target="_blank" rel="nofollow noopener noreferrer">What’s new with in-app purchase - WWDC 2020</a></li>
<li><a href="https://juejin.cn/post/6845166890420011022" target="_blank">iOS Handle Refunds 处理退款 --- WWDC20（Session 10661）</a></li>
<li><a href="https://developer.apple.com/storekit/" target="_blank" rel="nofollow noopener noreferrer">StoreKit Overview - Apple Developer</a></li>
<li><a href="https://developer.apple.com/documentation/storekit/choosing_a_storekit_api_for_in-app_purchase" target="_blank" rel="nofollow noopener noreferrer">Choosing a StoreKit API for In-App Purchase | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/devicemanagement" target="_blank" rel="nofollow noopener noreferrer">Device Management | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/app-store/pre-orders/" target="_blank" rel="nofollow noopener noreferrer">Offering Your Apps for Pre-Order - App Store - Apple Developer</a></li>
<li><a href="https://developer.apple.com/app-store/whats-new/" target="_blank" rel="nofollow noopener noreferrer">What’s New - App Store - Apple Developer</a></li>
<li><a href="https://developer.apple.com/cn/app-store/subscriptions/" target="_blank" rel="nofollow noopener noreferrer">自动续期订阅 - App Store - Apple Developer</a></li>
<li><a href="https://developer.apple.com/documentation/storekit/backingvalue" target="_blank" rel="nofollow noopener noreferrer">BackingValue | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase/subscriptions_and_offers/implementing_promotional_offers_in_your_app" target="_blank" rel="nofollow noopener noreferrer">Implementing Promotional Offers in Your App | Apple Developer Documentation</a></li>
<li><a href="https://tools.ietf.org/html/rfc7515" target="_blank" rel="nofollow noopener noreferrer">JWS documentation (RFC 7515)</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/creating_api_keys_to_use_with_the_app_store_server_api" target="_blank" rel="nofollow noopener noreferrer">Creating API Keys to Use With the App Store Server API | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/generating_tokens_for_api_requests" target="_blank" rel="nofollow noopener noreferrer">Generating Tokens for API Requests | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi" target="_blank" rel="nofollow noopener noreferrer">App Store Server API | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/storekit/in-app_purchase/implementing_a_store_in_your_app_using_the_storekit_api" target="_blank" rel="nofollow noopener noreferrer">Implementing a Store In Your App Using the StoreKit API | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/get_all_subscription_statuses" target="_blank" rel="nofollow noopener noreferrer">Get All Subscription Statuses | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/get_transaction_history" target="_blank" rel="nofollow noopener noreferrer">Get Transaction History | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/" target="_blank" rel="nofollow noopener noreferrer">App Store Server API | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/send_consumption_information" target="_blank" rel="nofollow noopener noreferrer">Send Consumption Information | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreserverapi/consumptionrequest" target="_blank" rel="nofollow noopener noreferrer">ConsumptionRequest | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/introduction/" target="_blank" rel="nofollow noopener noreferrer">Introduction - In-App Purchase - Human Interface Guidelines - Apple Developer</a></li>
</ul>
<blockquote>
<p><strong>37手游iOS技术运营团队</strong>：分享技术动态、实践和思考！热爱，开放，严谨，担当~</p>
</blockquote>
<ul>
<li>如有侵权，联系必删~</li>
<li>如有不正确的地方，欢迎指正教导~</li>
<li>如有问题，欢迎在评论区一起讨论~</li>
</ul></div>  
</div>
            