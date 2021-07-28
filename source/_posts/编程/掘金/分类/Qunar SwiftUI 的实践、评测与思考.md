
---
title: 'Qunar SwiftUI 的实践、评测与思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996ea9fb10a6488aa898f5c169e11fcb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 23:23:34 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996ea9fb10a6488aa898f5c169e11fcb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996ea9fb10a6488aa898f5c169e11fcb~tplv-k3u1fbpfcp-watermark.image" width="60%" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>赵龙，2020年加入Qunar，担任大前端iOS开发，OC、 SWIFT、 C++、Dart等技能丰富，喜欢优化开发流程，研究增加效率的代码和开发方式。</p>
</blockquote>
<hr>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d21923ccb4243e2bab06b6f2d1dd517~tplv-k3u1fbpfcp-watermark.image" width="60%" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>林书辉，2018年加入Qunar，iOS、RN开发工程师。目前负责大客户端公共产品首页、用户中心等功能的开发和维护。持续关注学习前沿的大前端技术，推崇技术创新带来的效率优化和性能提升。现致力于Native+DSL动态化组件方案的开发与推广。</p>
</blockquote>
<h2 data-id="heading-0">一. 前言</h2>
<p>SwiftUI 出现已经2年，至今尚未大规模推广落地，它局限在 iOS 生态内，暂时闭源的 UI 库，需要 iOS13 版本来适配，这些因素阻碍了更多人使用，但是其实它相对于其他UI框架具有非常高的开发效率与运行效率，相对于 Objective-C+UIKit 更是一个全面的框架升级。<br>
写这篇文章是为了让大家熟悉 SwiftUI ，让客户端同学在技术选型的时候有切实的数据和特性来参考，也希望推进大客户端的 Swift 基础设施建设。</p>
<h2 data-id="heading-1">二. SwiftUI 代码库</h2>
<p>iOS 中 SwiftUI 由2个底层框架驱动 SwiftUI.framework 与 Combine.framework<br>
其中 SwiftUI.framework 负责界面搭建，简洁的 DSL 相比 OC 让开发效率提升不少,例如我们要实现在屏幕中心实现一个带文本按钮， OC 中我们一般这样写：</p>
<pre><code class="copyable">- (void)viewDidLoad &#123;    
    CGRect screen = [[UIScreen mainScreen] bounds];    
    UIButton * centerBtn = [UIButton buttonWithType:UIButtonTypeCustom];    
    [centerBtn setFrame:CGRectMake(screen.size.width / 2 - 30, screen.size.height / 2 - 15, 60, 30)];    
    [centerBtn setTitle:@"测试按钮" forState:UIControlStateNormal];    
    [self.view addSubview:centerBtn]; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在 SwiftUI 中我们这样写：</p>
<pre><code class="copyable">var body: some View &#123;    
    Button()&#123;       
        Text("测试按钮")         
            .frame(width: 60, height: 30, alignment: .center)    
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Combine.framework 负责生成数据流绑定操作与界面，基于观察者模式，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。<br>
只不过，这些框架对这个模式进行了一点扩充，在被观察者与观察者之间引入了可选的转换操作(操作符：Operators)。</p>
<h2 data-id="heading-2">三. 渲染流程</h2>
<p>以我们去哪儿小组件一个页面左下角文本的渲染为例。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a71b0e78c9684d9ca80a9e7055c45aba~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">Text(self.title)        
        .font(Font.system(size:14))        
        .fontWeight(.semibold)        
        .foregroundColor(.white)        
        .frame(alignment: .center)    
    .offset(x: -3.5, y: 2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入页面时每个元素（例子中的 Text ）由代码底层开始，每个单元(每个.开头的一行)进行链式组装返回一个 view ，之后通知它的上级单元（代码中的上面一行），把下面单元生成的 view 当做参数，生成新的 view ，递归形成整个渲染树，进入流水线进行渲染。<br>
当状态发生变化时，首先会对比前后 View 声明的变化， SwiftUI 只会向流水线提交声明中不同的部分。</p>
<h2 data-id="heading-3">四. 生命周期</h2>
<p>WWDC 2020期间，苹果公布 SwiftUI 获得了新的的应用程序生命周期，以摆脱 UIKit 的AppDelegate 和 SceneDelegate 的旧模式。基于此，iOS 14现在提供了一个 App 协议、一个SceneBuilder、 scenePhase枚举器和一个新的属性包装器UIApplicationDelegateAdaptor 。<br>
遵循 APP 协议，我们可以用新的方式构建UI，其中必须实现 SceneBuilder ，它本质上是一个用于构建一个或多个场景的函数构建器，使用 scenePhase 来获取场景当前状态，UIApplicationDelegateAdaptor用来连接老的app生命周期方法。<br>
新的生命周期代码执行顺序为：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddf76da55e3c4f758319fc274e0e7915~tplv-k3u1fbpfcp-watermark.image" alt="4.jpg" loading="lazy" referrerpolicy="no-referrer">
相对 AppDelegate，它使用 WindowGroup 包装在需要监听生命周期的场景之外，可以方便快捷的访问页面生命周期方法，简洁而且可以让页面之间解耦。<br>
现有的渲染流程仍然遵循 iOS Cocoa 框架，使用 Core Animation 为渲染核心库。</p>
<h2 data-id="heading-4">五. 语言特点</h2>
<p>SwiftUI 从根本上不是在构建 UI，而是在描述 UI 。这两者有什么区别？<br>
构建 UI 时，你会明确每一个控件的类型，甚至精确到平台。比如在原生 UI 框架中，你需要一个输入框 ，你就要根据不同的平台，选择具体是使用 UITextFiled（iOS） 还是 NSTextFiled（macOS），而这两个输入框 有着不同的属性、外观和特性。在 Flutter 中，你不需要考虑不同平台的控件类型，但你需要考虑控件的风格，官方提供了符合 Material Design 的 Android 控件和 iOS Style 的 iOS 控件，它们的许多特性也不一致，这一切给 UI 构建带来了更加复杂的逻辑和工作量。<br>
而 SwiftUI 更像是 Web 的模版，它只描述 UI ，而控件具体长什么样子，有什么特性，会根据编译的平台因地制宜的实现，而且是自动的。这就像是给 Web 套上了一个模版，一个主题。<br>
接下来展示一个控件Picker，相同的代码在不同平台上不同的表现。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01e807ee977a45919d059f33d413758b~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f154c9744d54ec387de2d1d05166b90~tplv-k3u1fbpfcp-watermark.image" alt="6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你会发现，同样的代码，展示出来的 UI 却完全不一样，但 UI 表达的内容确实完全一致的。Picker 控件，在iOS上被翻译成了一个选择页面，有滚轮选择效果。而在 macOS 上，Picker 则会被翻译成我们桌面操作系统上常见的下拉列表。它完全符合了平台设计语言和用户使用习惯，同时又极大的降低了开发和适配难度。<br>
从这一点上来看，SwiftUI 和 RN 有着更为相似的思路和技术。只不过 Facebook 无论对 iOS 还是 Android 都几乎没有任何话语权，因此在兼容性、一致性上都跟SwiftUI或者将来的谷歌自有跨平台框架有差距。</p>
<h2 data-id="heading-5">六. SwiftUI 数据状态和绑定</h2>
<p>SwiftUI分三种方式绑定数据与界面。</p>
<h4 data-id="heading-6">1. @State & @Binding</h4>
<p>提供 View 内部的状态存储，应该是被标记为 private 的简单值类型，仅在内部使用。</p>
<h4 data-id="heading-7">2. ObservableObject & @ObservedObject</h4>
<p>针对跨越 View 层级的状态共享，处理更复杂的数据类型，在数据变化时触发界面刷新。</p>
<h4 data-id="heading-8">3. EnvironmentObject</h4>
<p>对于 “跳跃式” 跨越多个 View 层级的状态，更方便地使用 ObservableObject，以简化代码。<br>
它们在使用时，都是通过在对应的属性前加以上修饰符，使用Propertywrapper的包装使得属性成为被观察者，如果它们有变化，就会直接通知对应范围内的UI刷新。<br>
可以看到，苹果在 SwiftUI 引入了前端开发中渐成主流的响应式编程思想，开发者基于苹果提供的原生 API ，就可以轻松实现视图和逻辑处理的解耦，降低了代码的维护成本，从而让开发者可以将更多精力投入业务的实现。反观目前 Qunar 正在使用的Objective-C+UIKit 的开发模式，如果开发者想要体验响应式编程，则面临着引入一系列第三方框架（如ReactiveCocoa）、代码风格受语法限制等一系列问题。从这一点上， SwiftUI 相比于 Objective-C 的优势是十分明显的。</p>
<h2 data-id="heading-9">七. SwiftUI的一些语法特性</h2>
<h4 data-id="heading-10">1. Opaque Result Type</h4>
<p>静态语言中返回对象类型必须在编译时确定，而一些对象在代码中又想隐藏自己的类型，对外使用协议类，对此 SwiftUI 给出了自己的解决方案，不透明返回类型，一句话概括，它就是一个泛型实例化的时候，不依赖调用者指定类型的一种语法特性。<br>
看一个例子:</p>
<pre><code class="copyable">func reverseGeneric() -> some Shape &#123; return Rectangle(...)  &#125;
let x = reverseGeneric()
// type(of: x) == Rectangle
// 并且 x 的类型根据 reverseGeneric 的具体实现决定
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2. Propertywrapper</h4>
<p>这个特性可以在属性 Get、Set 的时候，将部分可复用的代码包装起来，用一个@符接一个自己定义的属性名称来使用这种能力。</p>
<h4 data-id="heading-12">3. FunctionBuilder</h4>
<p>这个特性是一种语法糖，可以用方法参数接受隐式闭包构建复合视图,换句话说就是可以在组件构建参数里直接写我们要构建的内容，而不需要各种语义控制符，例如冒号，逗号，声明参数类型，闭包类型等。<br>
看一个例子：</p>
<pre><code class="copyable">VStack(alignment: .leading) &#123;    
    Text("Hello, World")    
    Text("Longzhao.zhao")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>合理利用这些特性，在去哪儿iOS小组件中，用大约600行的代码就实现了登录，酒店，机票，火车票的状态展示。</p>
<h2 data-id="heading-13">八. SwiftUI比较其他声明式UI框架</h2>
<p>声明式 UI 框架，带给了开发者优秀体验，相比于使用类似 iOS 中的 UIKit 等命令式 UI 框架搭建 UI 界面，声明式 UI 框架让开发者更像在使用自然语言描述自己的需求。从代码维护的角度来看，一个复杂的 UI 结构，如果使用命令式 UI 框架，很难直观的让开发者一眼看出某段代码想要实现一个什么样的 UI 效果，而规范的声明式的代码甚至会给人一种“所见即所得”之感。总结一下，目前业内普遍认为声明式 UI 较命令式UI理念上更为先进的原因，主要表现在如下几点：</p>
<p>1.适合做一次开发，多种不同的设备类型自适应。</p>
<p>2.显示UI和控制逻辑通过响应式思想与数据进行绑定，实现解耦。</p>
<p>3.更易于实现UI控件的局部刷新机制。</p>
<p>我们挑选了目前移动端比较主流的另外两个声明式UI框架 – Flutter、RN，与SwiftUI进行比较，希望可以给大家一些启发。</p>
<p>比较分四个维度：</p>
<h4 data-id="heading-14">关于语法</h4>
<p>SwiftUI 得益于 Swift5.1 加入的 Function Builder 与 Opaque return types（非透明返回类型）特性，增强了构建内置 DSL 的能力，使代码变得简洁有效。配合FuctionBuilder、尾随闭包(Trailing closure)、省略 return（当函数体中只有单独一个表达式，就会自动添加一个 return，返回这个表达式的值）等 Swift 语言特性， SwiftUI 实现了直观的代码风格，效果如下：</p>
<pre><code class="copyable">struct TripCardContentView: View &#123;    
    var cardData: CardData?    
    var body: some View &#123;        
        switch cardData?.cardType &#123;              
            case CARD_TYPE_FLIGHT:                    
                FlightCard(cardData: self.cardData as? FlightData)              
            case CARD_TYPE_TRAIN:                    
                TrainCard(cardData: self.cardData as? TrainData)              
            case CARD_TYPE_HOTEL:                    
                HotelCard(cardData: self.cardData as? HotelData)          
         default:            
           Spacer()        
        &#125;    
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终根据实际业务呈现的效果：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc9a992038274cd29ed804a16280d93c~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5132c1a3a2a44d35bcc55ce8ec1aec99~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/798d228813714e67ab91909794a8f79d~tplv-k3u1fbpfcp-watermark.image" alt="9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RN使用 JSX 来模拟 HTML 标签的方式，更符合 web 开发的思维，个人认为各有优势</p>
<p>相比之下， Flutter 由于没有如此强大的内部 DSL ，所以在开发体验上会有一些不方便，虽然 Flutter 团队通过编辑器的提示插件、保存时强行格式化等方式进行了一些开发体验优化，但是总体上还是不如前两者</p>
<p>基于这些语言特性我们大大加快了开发速度，小组件机票展示业务从零开始搭建 Swift 环境（包含工程适配，打包平台支持）只花了7天就可以上线，酒店和车票展示业务随后开发，代码耗时 2pd 。</p>
<h4 data-id="heading-15">关于热加载</h4>
<p>SwiftUI 的实时预览分为静态预览和动态预览。默认情况下展示的是静态预览，它的速度快，而且支持代码和可视化两种编写方式。不过它没有任何响应事件，无法滚动和跳转页面。如果需要动态调试，则需要切换到动态预览。动态预览需要经过一段编译时间，然后可以以完全动态的形式实时响应 UI 的变化，而且可以在真机上实时调试。但动态预览的限制还比较多，无法做到 Flutter 那种只需编译一次，之后整个 App 都能实现动态更新。</p>
<p>RN的基于HMR(Hot Module Replacement模块热替换机制)实现了hot reload,体验还是很不错的，但是在实际使用中，经常会出现代码写了一半，因为编辑器自动保存触发了watchMan的回调，走到了hot reload逻辑，从而造成红屏。</p>
<p>Flutter是通过将更新后的源代码文件注入正在运行的Dart虚拟机（VM）中来实现的热重载。在虚拟机使用新的的字段和函数更新类后，Flutter框架会自动重新构建widget树，以便开发者快速查看更改的效果。但是由于静态字段惰性初始化等Dart语言特性，在一些场景下，如：更改全局变量和静态字段的初始值设定项、枚举类型更改为常规类或常规类更改为枚举类型等，热重载后会无效，需要完全重启应用才可以。</p>
<p>总体来讲，三个框架的热重载机制体验差不多，都达到了可以实时预览样式的目的，这提升了搭建UI时的工作效率。但是对于一些涉及到逻辑的代码变更，还是完全重载来的更为稳妥。</p>
<h4 data-id="heading-16">跨平台方面</h4>
<p>目前 SwiftUI 支持 iOS、watchOS、iOS14 小组件、MacOS 平台的 APP 开发，理论上是可以一套代码编译出多个平台的应用，但是基于用户体验的考虑，苹果官方并不推荐为不同的设备采用一套 UI 设计，他们更加推崇 “Learn once, apply anywhere” 。相比于 RN 和 Flutter 可以横跨 OS、Android（Flutter最新release版还支持windows、MacOS、web平台），SwiftUI 更关注于苹果自身各个平台的编码统一性和体验的提升，在这一点上，Swift 的理念和其他两个是有一些区别的。</p>
<h4 data-id="heading-17">性能方面</h4>
<p>通过超长列表视图、大批量动画同时播放、大量视图旋转和缩放等测试场景，我们得出了以下结论：在以上场景中，SwiftUI 不出预料确实具有最强的性能。其次就是 Flutter 和 RN。但是如果一定要考虑跨平台的需求，在 CPU 占用率很高的业务中应避免使用RN，相比之下 Flutter 更加适合这种任务。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/615bef8e7bfe40fa8d9c29b8845b5370~tplv-k3u1fbpfcp-watermark.image" alt="10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">九. SwiftUI 在 Qunar 大客户端落地场景的思考</h2>
<p>以上我们从不同的维度比较了各种声明式 UI 框架。我们认为所有的技术都有适合它的场景，抛开场景来做选择必然会带来技术方案选型不合适的问题。下面我们也基于 Qunar 大客户端存在的一些具体场景，进行了上面提及的技术的一些落地的思考，总结如下：</p>
<p>1.对一些性能要求较高，同时为了节约效率而倾向于跨平台开发的页面，可以使用 Flutter 进行开发。但是由于目前 Flutter 还没有官方的动态化热更新方案，所以新功能的迭代，还需要依赖发版来解决。关于 Flutter 框架在大客户端的支持，公司的开发同事已经有了很大的进展，非常期待后续 Flutter 技术在公司全面应用。应用场景方面， IM 聊天会话页，对页面的 UI 一致性要求高，同时要保证绘制的效率，会是 Flutter 落地的理想场景.</p>
<p>2.对一些性能要求较低，更倾向于与高效率跨平台开发及快速迭代需要热更新的页面，可以选择 RN 。这也是去哪儿目前比较主流的解决方案了，它的热更新和越来越丰富的 API 为客户端的功能迭代带来了很大的效率提升，但是由于 RN 框架的机制，注定了一些对性能有苛刻要求的页面不得不去考虑其他方案。</p>
<p>3.针对一些对性能有极高要求的页面，而且可以接受 iOS 与安卓分别投入人力进行开发，并且跟版更新，如大客户端首页、登录页等，目前 native 仍然是不可替代的方案。native 端的UI实现可以考虑使用 UIKit 和 SwiftUI 框架进行开发，但是由于 SwiftUI的最低支持 iOS 版本为 iOS13.0，而我们的大客户端目前的最低支持版本为 iOS10.0，所以在未来 iOS13+ 成为绝对占有率很高的系统之后，这些页面可以考虑首选转型为 swiftUI 为框架实现，它迎合了现在首页的几个需求：始终拥有最高帧率表现，能最大化降低首页启动时间，崩溃与卡顿定位最精确，保持 iOS  新特性最快最全面的支持</p>
<p>4. Objective-C 无论开发还是运行效率都已落后，如果可以有最低版本为 iOS13 的场景， SwiftUI 都是更好的选择，老的 OC 框架只有在对接有历史包袱的需求可能有一些优势</p>
<p>5.因为 Swift 与 Objective-C 可以通过桥接互相调用，现阶段让 Swift 兼容老的 OC 、RN、Flutter 代码最经济的方式是使用Swift建桥链接必要的 OC API。</p>
<p>6.目前我们已经使用 SwiftUI 框架实现了大客户端 iOS14 小组件，从20年11月上线到现在，支撑起了 iOS 桌面待出行行程信息展示的高频场景。</p>
<h2 data-id="heading-19">十. Objective-C 迁移 Swift 与 SwiftUI</h2>
<p>Swift 语言是 iOS 开发的方向，我们也调研了向 Swift 与 SwiftUI 迁移的可行性，大部分OC代码都可以直接找到对应API翻译成Swift，有一些特性需要注意，例如@synchronized，dispatch_once 等在 Swift 中已经移除，需要自己写一个类似功能来实现。举一个自己实现这些特性的例子：</p>
<p>举一个自己实现这些特性的例子</p>
<pre><code class="copyable">//swift同步锁
func synchronized(_ lock: AnyObject, block: () -> Void) &#123;    
    objc_sync_enter(lock)    
    block()    
    objc_sync_exit(lock)&#125;
//
swift dispatch_once
public extension DispatchQueue &#123;   
    private static var _onceTokens = String()   
    public class func once(token: String, block:()->Void) &#123;      
        objc_sync_enter(self)      
        defer &#123; objc_sync_exit(self) &#125;      
        if _onceTokens.contains(token) &#123;         
            return      
        &#125;      
        _onceTokens.append(token)      
        block()   
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在有没有将大客户端的代码全部迁移到 Swift 的必要呢？从迁移成本和收益上考虑，没有太大必要，比较可行的方案是新增一部分功能的 Swift 框架，如网络库、appInfo、通用服务等，框架内部通过桥接封装现有的 OC 框架，提供 Swift 版本的 api 供业务线使用。这样后续 native 代码实现的功能，会多一种 Swift 实现的选择，从而实现逐步迁移。</p>
<h2 data-id="heading-20">十一. 总结</h2>
<p>Swift 做为苹果的战略语言已经发展的越来越壮大，自 2019 年 Swift ABI 稳定后，苹果更是在全力支持 Swift 。我们可以进入苹果源码库 看到， 自 iOS 13 以来 苹果新增了约 10+个纯 Swift 库, 10+个开源 Swift库, 以及针对 144 个公开 Framework，遵守 Swift 风格 重新设计了 57 个 Framework 的API。基于以下事实：</p>
<p>第一．从 WWDC2017 后 苹果已经不再使用 Objective-C 做代码演示；<br>
第二．<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2F%25C2%25A0%25E5%25B7%25B2%25E7%25BB%258F%25E4%25B8%258D%25E5%2586%258D%25E6%259B%25B4%25E6%2596%25B0" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/%C2%A0%E5%B7%B2%E7%BB%8F%E4%B8%8D%E5%86%8D%E6%9B%B4%E6%96%B0" ref="nofollow noopener noreferrer">developer.apple.com/ 已经不再更新</a> Objective-C 相关的文档；<br>
第三．WidgetKit 只支持 Swift，没有支持 Objective-C；<br>
第四．App Clips 限制了包大小为 10M， SwiftUI 是最合适的框架；<br>
第五．开源社区中 Objecive-C 比例逐渐降低甚至废弃 如 Lottie。</p>
<p>可以判断，Swift 是未来 Apple 平台的唯一选择，我们如果可以在 Native 开发中尽早甩掉包袱使用 Swift ，就可以在下一步与其他APP的开发效率及运行效率的比较中取得优势。<br>
Qunar 大客户端开发中我们可以根据以上列举的数据和方案自行做出最适合需求的技术选型，选择了 Swift 语言或者 SwiftUI 框架也可以这篇文章也可以对照这里的实现细节作为参考。<br>
去哪儿 iOS 大客户端已经支持 Swift&OC 混编，各业务线可以直接加入 Swift 文件参与本地编译和 CM 打包，以后我们也会积极推进建立一套大客户端的 Swift 基础框架来支持公司向 Swift 和 SwiftUI 方向发展。</p></div>  
</div>
            