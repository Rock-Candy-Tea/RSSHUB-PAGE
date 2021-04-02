
---
title: '雪球 iOS Widget 从零到壹'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f277662fe394003a19610cc47d6b0d5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 21 Mar 2021 21:33:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f277662fe394003a19610cc47d6b0d5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">雪球 iOS Widget 从零到壹</h1>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f277662fe394003a19610cc47d6b0d5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作者：春春</p>
<h1 data-id="heading-1">引言</h1>
<p>在 2020 的 WWDC 上苹果发布了 <code>WidgetKit</code> 小组件，重新设计后的 Widgets，其展示不再局限于负一屏，而且支持在 macOS 和 iOS 的主屏幕上提供动态信息和个性化内容。苹果对小组件定位重点在于信息展示，而非应用程序的快捷方式或者小程序。因此，它的运行限制较多。如何在有限的条件里做好用户体验，就成为了雪球设计师和产品的重要挑战。</p>
<h1 data-id="heading-2">WidgetKit 简介</h1>
<p>为了提供符合苹果美学与规范的小组件，团队在雪球小组件的产品设计前期就召集相关设计师和产品经理，一起学习了 WWDC20 中关于 Widgets 的 Sessions。</p>
<h2 data-id="heading-3">Widgets 核心要素</h2>
<p>苹果对于优秀 Widget 的介绍如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e66a486eb044a5b8f9a3229baedc5f8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>在快速切换应用的主屏幕里，复杂交互的应用界面并不切合用户需求，<strong>简单明了的内容才是用户关注的重点</strong>。</p>
</li>
<li>
<p>Widget 会在<strong>恰当时机展示正确的内容</strong>， 同时支持预渲染、复用，并提供灵活可控的更新策略来保证内容即时性。</p>
</li>
<li>
<p>Widget 提供了<strong>个性化定制</strong>，可针对不同尺寸及用户配置来展示不同的内容。</p>
</li>
</ol>
<h2 data-id="heading-4">Widgets 的限制</h2>
<p>Widget 设计的初衷是简单明了的在恰当的时机展示一些带有个性化定制的内容，为了不让主屏幕的整体使用体验变得复杂，Widget 限制了很多能力：</p>
<ol>
<li>
<p>不提供动画，仅支持静态页面展示。</p>
</li>
<li>
<p>不支持拖拽、滚动等复杂的交互，不支持 Switch 等控件。</p>
</li>
<li>
<p>仅支持点击指定的 URL 跳转到 App。</p>
</li>
<li>
<p>更新频率由系统通过机器学习来动态分配。</p>
</li>
</ol>
<h2 data-id="heading-5">Widget 的生命周期</h2>
<p>运行在主屏幕的小组件，其生命周期理论上与桌面进程一致。不过由于系统的限制，小组件只能在预定的时间节点提交刷新请求，由系统来决定是否需要进行响应。在其生命周期中，小组件的逻辑有三次被系统调用的机会：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a1d673602a448ebe17609999f8de07~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>当用户编辑主屏幕添加小组件时，先触发 <code>placeholder(in:)</code> 来优先显示占位效果。</p>
</li>
<li>
<p>在预览状态，触发 <code>getSnapshot(for:in:completion:)</code> 创建快照以提供相对完整的信息展示。</p>
</li>
<li>
<p>最终在主屏上成功添加小组件后，将执行 <code>getTimeline(for:in:completion:)</code> 获取未来时间节点上的数据和相关更新策略。</p>
</li>
</ol>
<blockquote>
<p>❝</p>
<p>Tips: 一般而言，在创建快照时渲染合适的视图以供预览，在刷新 timeline 时获取网络数据。</p>
</blockquote>
<p>要理解小组件的生命周期，读懂 timeline 的概念就十分重要了。小组件的内容变化都依赖于此。</p>
<p>timeline 本质上是基于时间驱动的一连串静态视图。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe0a3875ee948ec90301c3a1f8d7296~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过 timeline provider 提供在未来特定的时间节点的一连串 <code>TimelineEntry</code> 数据，并且可以设置更新策略：</p>
<ul>
<li>
<p>after：在特定时间后触发更新。</p>
</li>
<li>
<p>atEnd：在 timeline 中所有的 entry 都展示完之后更新。</p>
</li>
<li>
<p>never：仅在主 App 触发更新。</p>
</li>
</ul>
<p>当然，所提供的这些数据是否更新，最终仍取决于系统。对于股价行情和热点事件这些不可预测的信息，我们选采用 <code>after</code> 策略，在一定时间后更新信息。同时我们会在主应用退到后台时，调用 <code>WidgetCenter</code> 来触发定向更新。</p>
<h3 data-id="heading-6">Timeline 刷新</h3>
<p>苹果提供了两种刷新小组件的方式，<code>System reloads</code> 和 <code>App-driven reload</code>。</p>
<p><strong>System reload</strong></p>
<p>由系统发起，刷新频次也由系统控制。为了保证性能，系统会根据各个 reload 请求的重要程度来控制是否刷新 timeline。因此，过于频繁的提交刷新请求可能无法达到预期。</p>
<p><strong>App-driven reloads</strong></p>
<p>由 App 触发小组件的 timeline 刷新。当主程序在后台时，可通过后台推送触发刷新；当主程序在前台时，可以通过 <code>WidgetCenter</code> 实现。不过 <code>WidgetCenter</code> API 仅提供了 Swift 版本，对于像雪球采用了 Swift + ObjC 混编的项目无法直接在 AppDelegate 中使用，需要通过 bridge 的方式暴露到 ObjC 来完成调用。</p>
<h1 data-id="heading-7">雪球 Widget</h1>
<h2 data-id="heading-8">Widget 设计</h2>
<p>雪球希望为用户提供其所关心的市场行情和及时的交易信息。而借助小组件这一新的内容展现形式，能够在一定程度上帮助用户聚集和触达他所关注的信息。</p>
<p>然而 💡 想法无限，时间有限，我们最终决定先尝试几个实用功能：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/672d12312e234cf49c72ac8aa6b0e49d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>分别选取了用户所关心的大盘行情、自选股、热门话题以及雪球日历。</p>
<p>另外针对自选股还支持了大、中、小三种尺寸：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7669985351ab4d019a2eb6444639f128~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>关于 Widget 设计可以参考这两个 Session：</p>
<ul>
<li>
<p>Design great Widgets</p>
</li>
<li>
<p>Meet WidgetKit</p>
</li>
</ul>
<h2 data-id="heading-9">0x01 环境搭建</h2>
<p>首先，Widgets 小组件本质上是存在于主项目之外的独立进程 (即 App Extension) ，它拥有自己的生命周期和存储空间，系统会根据用户触发的事件进行管理。App Extension 依赖主应用程序为载体，如果将主应用程序卸载，那么 App Extension 也将不复存在。</p>
<p>因此，我们需要为小组件搭建基础设施，如网络通信，图片缓存，数据持久化等等。除此之外，你还需要熟悉 Swift 并且了解 SwiftUI 的一些基础用法。</p>
<h3 data-id="heading-10">网络通信</h3>
<p>小组件中可以使用 <code>URLSession</code>，而雪球在 Swift 2.0 已接入 Swift，且基于 <code>Alamofire + SwiftyJSON</code> 封装了一层内部网络库。仅需简单抽离即完成了小组件网络库的封装。</p>
<p>作为独立于主工程的小组件，我们需要在 <code>Podfile</code> 中为小组件的 target 引入所需的依赖框架。</p>
<pre><code class="copyable">`target 'Snowball' do`
 `...`
 `target 'SnowballWidgets' do`
 `inherit! :search_paths`
 `pod 'Alamofire', '~> 5.0.2'`
 `pod 'SwiftyJSON', '~> 5.0.0'`
 `...`
 `end`
`end`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体网络封装本文不做展开。</p>
<h3 data-id="heading-11">数据共享</h3>
<p>由于 App Extension 不能直接同主程序直接通讯，不过苹果提供了 <code>App Groups</code> 的方式来进行通讯。<code>App Groups</code> 有两种共享数据的方式：<code>UserDefaults</code> 和 <code>FileManager</code>。</p>
<p>对于将要展示的用户自选数据，必须要先获取登录授权信息。同时雪球的认证机制比较复杂，其完整功能存在于内部独立的 OAuth SDK 中，无法直接在 extension 中使用。因此，我们决定通过 <code>UserDefaults</code> 来共享 access_token 及用户偏好设置，如涨跌颜色等。</p>
<p><strong>UserDefaults 共享数据</strong></p>
<p>共享 UserDefaults 数据要设置 <code>suitename</code> 为对应项目的 App GroupID，有两种设置方式：</p>
<pre><code class="copyable">`init?(suiteName suitename: String?)`
`// or`
`func addSuite(named suiteName: String)`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置之后即可使用该实例来储存和获取共享数据了。我们以 access_token 为例：</p>
<pre><code class="copyable">`public extension UserDefaults &#123;`
 `@objc`
 `static var shared: UserDefaults &#123;`
 `if let value = Bundle.main.object(forInfoDictionaryKey: "GroupIdentifier") as? String &#123;`
 `return UserDefaults(suiteName: value) ?? .stander`
 `&#125; else &#123;`
 `return UserDefaults(suiteName: "group.xxx") ?? .stander`
 `&#125;`
 `&#125;`
`&#125;`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们通过读取 <code>Info.plist</code> 中预设的 <code>GroupIdentifier</code> 作为 App GroupID。用来解决内网发布所用的企业证书和 App Store 的个人证书不同，导致 App GroupID 不同的问题。</p>
<p>完整的 Widget token 获取流程如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c910816adc4c42288e57817fb0fffe1f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>用户在雪球登录后，从服务端获取 token。</p>
</li>
<li>
<p>雪球 App 退到后台时，将 token 写入 App Group。</p>
</li>
<li>
<p>刷新 Widget 时，从 App Group 获取 token 来进行接口请求。</p>
</li>
<li>
<p>用户在雪球退出后，将 token 从 App Group 中删除。</p>
</li>
</ol>
<p>不过，这个流程中还有一处缺陷，就是当用户首次添加小组件时，可能并未在雪球 App 上完成登录操作。这里就需要添加未登录 ⏰。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa1e9eb720d448248c6484e1136f6461~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后，对于数据量较大的文件共享，可以通过 <code>FileManager</code> 的 <code>containerURL(forSecurityApplicationGroupIdentifier:)</code> 获取 App Group 共享的储存空间地址，进行文件的存取操作。</p>
<p>由于我们在 Userdefaults 中所使用到 key 都需要在主工程中赋值，在 Widget 中读取。为了避免 key 的多处重复定义，以及方便 API 的统一调用，将公共逻辑抽离到单独文件中，通过 <code>Comple Source</code> 分别在主工程和 Widget 中引用，来实现逻辑共用。</p>
<pre><code class="copyable">`@propertyWrapper`
`public struct UserDefaultsWrapper<Value> &#123;`
 `let key: String`
 `let defaultValue: Value`
 `var storage: UserDefaults = .shared`
 `public var wrappedValue: Value &#123;`
 `get &#123;`
 `let value = storage.value(forKey: key) as? Value`
 `return value ?? defaultValue`
 `&#125;`
 `set &#123;`
 `storage.setValue(newValue, forKey: key)`
 `&#125;`
 `&#125;`
`&#125;`
`public extension UserDefaultsWrapper where Value: ExpressibleByNilLiteral &#123;`
 `init(key: String, storage: UserDefaults = .shared) &#123;`
 `self.init(key: key, defaultValue: nil, storage: storage)`
 `&#125;`
`&#125;`
`public extension UserDefaults &#123;`
 `@UserDefaultsWrapper(key: "com.xxx.Widgets.token")`
 `@objc static var WidgetToken: String?`
 `@UserDefaultsWrapper(key: "com.xxx.Widgets.stockColor", defaultValue: 0)`
 `@objc static var WidgetStockColor: Bool`
 `...`
`&#125;`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里还利用了 @propertyWrapper 特性，将 key 收口，使用者仅需关心对应的属性即可。</p>
<h2 data-id="heading-12">0x02 SwiftUI & Custom View</h2>
<p>本节我们简单谈谈使用 SwiftUI 来开发 Widget 的一些小细节和注意事项。</p>
<p>由于雪球工程历史包袱较大，在上面进行 Widget 的开发调试效率较低，且无法充分利用 SwiftUI 的 preview 特性进行 UI 调试。基于这个考虑，笔者直接在新建的 Xcode 工程中进行 SwiftUI 构建，完成后再同步回主工程。</p>
<p>对于界面开发而言，工作量最大的就是进行元素布局，在 <code>SwiftUI</code> 中每个元素是如何确定位置和大小的呢 ?</p>
<p>大致分为三步：</p>
<ol>
<li>
<p>父视图为子视图提供预估尺寸大小。</p>
</li>
<li>
<p>子视图计算自己的实际尺寸大小。</p>
</li>
<li>
<p>父视图根据自身和子视图的尺寸以及属性，来计算子视图的布局。</p>
</li>
</ol>
<p>其中在第二步，子视图计算自身尺寸时，<code>SwiftUI</code> 提供了三种设置尺寸的方式：</p>
<ul>
<li>
<p>无需设置，根据内容自行计算，如 Text。</p>
</li>
<li>
<p>手动设置 <code>frame + position</code></p>
</li>
<li>
<p>设置 aspectRatio 宽高比，例如 Image</p>
</li>
</ul>
<p>详细可参照：WWDC19 - Building Custom Views with SwiftUI</p>
<h3 data-id="heading-13">自选背景实现</h3>
<p>在 Widget 设计一节中，可以看到在自选、热门话题及雪球日历均有一个浅色渐变的 logo 背景，只是颜色不同。</p>
<p>由于背景是撑满整个 Widget 且 logo 位于顶点的相对位置，即顶部或底部。因此，这里采用了手动布局 <code>frame + position</code> 的方式。</p>
<pre><code class="copyable">`func logoPosition(_ contentSize: CGSize) -> CGPoint &#123;`
 `let offset: CGFloat = logoSize / 3`
 `if edge == .top &#123;`
 `return CGPoint(x: contentSize.width - offset, y: offset)`
 `&#125; else &#123;`
 `return CGPoint(x: contentSize.width - offset, y: contentSize.height - offset)`
 `&#125;`
 `&#125;`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外为了方便对比调试，直接添加了多种状态的预览视图：</p>
<pre><code class="copyable">`struct LogoView_Previews: PreviewProvider &#123;`
 `static var previews: some View &#123;`
 `Group &#123;`
 `LogoBackgroundView(edge: .top, style: .custom(.blue99))`
 `LogoBackgroundView(edge: .top, style: .custom(.gold))`
 `LogoBackgroundView(edge: .bottom, style: .custom(.gold))`
 `.environment(\.colorScheme, .dark)`
 `&#125;`
 `.previewContext(WidgetPreviewContext(family: .systemMedium))`
 `&#125;`
`&#125;`

<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码和预览效果如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9757f8d3877643f3ad4083390d6ede1b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">自选列表项实现</h3>
<p>自选列表项在整个小组件中算是相对复杂的布局了，需要支持用户的不同登录状态、自选展示内容和数量的可编辑、不同的画布尺寸以及用户涨跌幅颜色配置等。不过相比 UIKit 而言简，SwiftUI 进行页面编写简直不要太爽，以自选列表项 <code>PortfolioItemView</code> 为例，仅需 50 行不到的代码就能完成 UI 与数据逻辑。</p>
<p>效果如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54fe7e88e3f4456d9a6b3b7c3d255deb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>另外，当获取的股票数据正常时，会将整个视图用 <code>Link</code> 包装，以响应用户点击。股票链接将会跳转到雪球上对应的个股页。</p>
<p>这里需要注意的是 ⚠️ ，在 Widget 中自定义的 Button 事件时无法被响应的，我们能做的仅仅是配置 <code>Link</code>。除了 <code>Link</code> 控件之外，还可以通过 <code>WidgetURL</code> 来设置跳转链接，不过它仅针对最后一次设置的 URL 生效。</p>
<h2 data-id="heading-15">0x03 编辑你的自选</h2>
<p>雪球支持用户添加几百只的股票作为其关注标的，而自选小组件最多可展示的股票数量仅 6 只。为此，我们需要提供能够根据用户的选择来展示对应自选的配置项。而该功能需要利用 <code>Intents</code> 框架来定义股票选择界面，之后系统会根据事先定义好的数据来构建配置页。</p>
<p>交互效果如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f36fd87df9704e6398505dd6705500c2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>❝</p>
<p>Tips: 关于如何创建和使用 <code>Intent</code> 框架，推荐 WWDC20 - Widgets Code-along, part 3: Advancing timelines。</p>
</blockquote>
<h3 data-id="heading-16">配置 IntentDefinition</h3>
<p>当我们创建小组件时就可以选择对应的 Intent 配置:</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf840be4787444a99cf62279d9400861~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>Include Configuration Intent</code> 选框决定了 Xcode 所使用配置，☑️ 表示支持用户配置，反之则不支持。</p>
<ul>
<li>
<p>StaticConfiguration：无配置属性的 Widget。</p>
</li>
<li>
<p>IntentConfiguration：可动态配置的 Widget。</p>
</li>
</ul>
<blockquote>
<p>❝</p>
<p>Tips：动态配置的功能是集成在 SiriKit 中，这是因为在 iOS 中 Springboard 上的很多配置均与 SiriKit 相关。</p>
</blockquote>
<p>勾选了 <code>Include Configuration Intent</code>，Xcode 会自动生成 <code>IntentDefinition</code> 文件，并且在编译通过后会自动生成一个名称为 <code>PortfolioSelectionIntent</code> 的 ConfigurationIntent 类。类名可通过 Custom Class 来指定。</p>
<p>每当我们更新 <code>IntentDefintion</code> 配置，需要重新编译以生成对应的方法。</p>
<p>自选小组件的 <code>IntentDefintion</code> 文件如下：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f39debeefc341eeae83ba60856e9da4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里我们定义了一个 <code>Portfolio</code> 类用于处理股票数据，属于自定义的参数模版同样也由系统生成。另外，我们勾选了 <strong>Dynamic Optional</strong> 中的 <code>provides search results</code> 用于支持用户输入结果查询。</p>
<p>编译后系统自动生成的 <code>PortfolioSelectionIntent</code> 类：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df2a81dd53af41abac19b9f47e1b520c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最终我们在 Widget 的 <strong>IntentTimelineProvider</strong> 入口关联 Intent：</p>
<pre><code class="copyable">`typealias Intent = PortfolioSelectionIntent`

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6cd41b5e29047d4a9d9ec0c87eda58a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">处理 IntentHandler</h3>
<p>完成绑定后，还需要新建一个 <code>PortfolioSelectionIntentHandler</code> 的 Target 用来处理和响应用户输入。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfacfbe74f9d4d8ab3c011a75564a3c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后在 <code>IntentHandler</code> 文件中实现 <code>PortfolioSelectionIntentHandling</code> 协议即可。如果在开发过程找不到对应的协议，可以确认一下对应的 <code>.intentdefinition</code> 文件是否添加到 target 中。当用户完成操作后，系统会通过 <strong>IntentTimelineProvider</strong> 来刷新小组件。在 <code>getTimeline(for:in:completion:)</code> 的 configuration 中将返回包含了用户的所挑选的自选股票。</p>
<p>至此，整个小组件开发就告一段落。大家可以前往 AppStore 下载 12.27 版本的雪球 iOS App 进行体验（需要升级到 iOS 14）。</p>
<h1 data-id="heading-18">总结</h1>
<p>在实际的 Widget 开发上涉及到多样的知识盲区，也算是摸着石头过河。另外，得益于 SwiftUI 的高效开发模式，使得 Widget 这样轻交互的 UI 能够被快速开发出来，还顺带推广了一波 Swift 可谓一 🐟 多吃。</p>
<p>尽管 Widget 在功能和交互上同 App 有着极大的限制，但是它也大大提高了用户主屏幕的丰富程度，且适合展示像股票行情和新闻资讯类信息。</p>
<p>Widget 特点总结如下：</p>
<ul>
<li>
<p>仅支持展示文本和静态图片资源，亦无法保证实时刷新。</p>
</li>
<li>
<p>增加了产品的曝光入口，自定义配置结合智能堆叠，为用户带来更多个性化的内容。</p>
</li>
<li>
<p>缩短了功能的访问路径，一键触达用户所需，提供用户想要的功能入口。</p>
</li>
</ul>
<h2 data-id="heading-19">还有一件事</h2>
<p>雪球业务正在突飞猛进的发展，工程师团队期待牛人的加入。如果你对「做中国人首选的在线财富管理平台」感兴趣，希望你能一起来添砖加瓦，点击「阅读原文」查看热招职位，就等你了。</p>
<p>热招岗位：大前端架构师、Android/iOS/FE 工程师、推荐算法工程师、Java 开发工程师。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            