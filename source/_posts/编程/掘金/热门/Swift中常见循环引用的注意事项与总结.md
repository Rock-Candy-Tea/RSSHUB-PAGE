
---
title: 'Swift中常见循环引用的注意事项与总结'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 00:25:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></h3>
<h2 data-id="heading-1">RxSwift编写wanandroid客户端现已开源</h2>
<p>前略，在肝完了6月的每日更文活动后，我并没有立刻参与掘金7月的好文活动。主要干了下面几件事情：</p>
<ul>
<li>
<p>自我休整，每日更文，使得我自己也落下了很多掘金的文章没有看，我自己需要看一下并学习一下。</p>
</li>
<li>
<p>wanandroid客户端的代码CodeReview，之前写的有些匆匆忙忙，很多细节功能没有实现。</p>
</li>
<li>
<p>整理思路，想想7月的思路该如何开始。</p>
</li>
</ul>
<p><strong>目前RxSwift编写wanandroid客户端已经开源了——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FseasonZhu%2FRxStudy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seasonZhu/RxStudy" ref="nofollow noopener noreferrer">项目链接</a>，切记切换到play_android分支上喔。</strong></p>
<p><strong>附上一张效果图片：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image" alt="RPReplay_Final1625472730.2021-07-05 16_13_58.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>本篇文章就得益于wanandroid客户端的代码CodeReview，因为使用RxSwift大量使用闭包，导致循环引用。</strong></p>
<p><strong>废话了这么多，那么我们进入主题吧。</strong></p>
<h2 data-id="heading-2">Timer导致循环引用</h2>
<h3 data-id="heading-3">为什么Timer不能被销毁</h3>
<p>虽然绝大部分的循环引用是对象与对象相互的强引用导致，<strong>但是Timer却是另有隐情：</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2727de3501724f78ac8ed1558731dc3b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>主线程的runloop在程序运行期间是不会销毁的， runloop引用着timer，timer就不会自动销毁。timer引用着target，target也不会销毁。</p>
</blockquote>
<p>关于Swift中的Timer会导致循环引用，如果是一个新手，基本上可能都会陷进去而不能自拔。</p>
<p>由于Timer导致的循环引用，苹果自己都要负很大一部分责任。</p>
<p>所幸的是苹果在<strong>iOS1 0</strong>的时候对Timer引入了新的API来改善这个问题，我强烈建议，如果你的App工程配置文件支持<strong>iOS 10之后使用系统的新API做定时任务！</strong></p>
<h3 data-id="heading-4">iOS 10之后的处理方式</h3>
<p>我们先来看一看Timer的源码：</p>
<pre><code class="copyable">open class Timer : NSObject &#123;

    /// 不建议使用
    public /*not inherited*/ init(timeInterval ti: TimeInterval, invocation: NSInvocation, repeats yesOrNo: Bool)
    
    /// 不建议使用
    open class func scheduledTimer(timeInterval ti: TimeInterval, invocation: NSInvocation, repeats yesOrNo: Bool) -> Timer

    /// 不建议使用
    public /*not inherited*/ init(timeInterval ti: TimeInterval, target aTarget: Any, selector aSelector: Selector, userInfo: Any?, repeats yesOrNo: Bool)

    /// 不建议使用
    open class func scheduledTimer(timeInterval ti: TimeInterval, target aTarget: Any, selector aSelector: Selector, userInfo: Any?, repeats yesOrNo: Bool) -> Timer

    /// 建议使用
    /// Creates and returns a new NSTimer object initialized with the specified block object. This timer needs to be scheduled on a run loop (via -[NSRunLoop addTimer:]) before it will fire.
    /// - parameter:  timeInterval  The number of seconds between firings of the timer. If seconds is less than or equal to 0.0, this method chooses the nonnegative value of 0.1 milliseconds instead
    /// - parameter:  repeats  If YES, the timer will repeatedly reschedule itself until invalidated. If NO, the timer will be invalidated after it fires.
    /// - parameter:  block  The execution body of the timer; the timer itself is passed as the parameter to this block when executed to aid in avoiding cyclical references
    @available(iOS 10.0, *)
    public /*not inherited*/ init(timeInterval interval: TimeInterval, repeats: Bool, block: @escaping (Timer) -> Void)

    /// 建议使用
    /// Creates and returns a new NSTimer object initialized with the specified block object and schedules it on the current run loop in the default mode.
    /// - parameter:  ti    The number of seconds between firings of the timer. If seconds is less than or equal to 0.0, this method chooses the nonnegative value of 0.1 milliseconds instead
    /// - parameter:  repeats  If YES, the timer will repeatedly reschedule itself until invalidated. If NO, the timer will be invalidated after it fires.
    /// - parameter:  block  The execution body of the timer; the timer itself is passed as the parameter to this block when executed to aid in avoiding cyclical references
    @available(iOS 10.0, *)
    open class func scheduledTimer(withTimeInterval interval: TimeInterval, repeats: Bool, block: @escaping (Timer) -> Void) -> Timer
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上面4个方法，我都写了明确的不建议使用，因为你可能按部就班的编写，也会循环引用。</strong></p>
<p><strong>最后下面2个方法，是iOS 10 之后的新API，创建定时任务，并通过block的方式进行回调，使用得当的话，就不会出现循环引用了。注意，block中请弱引用。</strong></p>
<h3 data-id="heading-5">iOS 10之前处理方式</h3>
<p>虽然目前已经在iOS系统已经是14了，但是很多App可能会向上兼容很多历史版本，导致上述API无法使用，这个时候，我们可以自己通过<strong>编写一个Timer分类，来解决循环引用：</strong></p>
<pre><code class="copyable">extension Timer &#123;
    
    /// Timer将userInfo作为callback的定时方法
    /// 目的是为了防止Timer导致的内存泄露
    /// - Parameters:
    ///   - timeInterval: 时间间隔
    ///   - repeats: 是否重复
    ///   - callback: 回调方法
    /// - Returns: Timer
    public static func scheduledTimer(timeInterval: TimeInterval, repeats: Bool, with callback: @escaping () -> Void) -> Timer &#123;
        return scheduledTimer(timeInterval: timeInterval,
                              target: self,
                              selector: #selector(callbackInvoke(_:)),
                              userInfo: callback,
                              repeats: repeats)
    &#125;
    
    /// 私有的定时器实现方法
    ///
    /// - Parameter timer: 定时器
    @objc
    private static func callbackInvoke(_ timer: Timer) &#123;
        guard let callback = timer.userInfo as? () -> Void else &#123; return &#125;
        callback()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里其实调用的系统API实际上是上面源代码中的第4个：</p>
<pre><code class="copyable">open class func scheduledTimer(timeInterval ti: TimeInterval, target aTarget: Any, selector aSelector: Selector, userInfo: Any?, repeats yesOrNo: Bool) -> Timer
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这里其实将Timer的定时任务在Timer里面实现了，而不是在target中进行了实现，推测iOS 10之后的系统API和这个实现类似。</strong></p>
<p>这里其实用了一个小技巧：<code>userInfo: Any?</code>传入的参数是<code>Any</code>类型，而我们在封装的入参中传入的是<code>callback: @escaping () -> Void</code>，没错，是一个闭包，<strong>闭包也是Any类型嘛</strong>，所以后面的实现Timer任务时，才有了<code>guard let callback = timer.userInfo as? () -> Void else &#123; return &#125;</code>这一段，来保证调用的合法性与合理性。</p>
<h3 data-id="heading-6">init(timeInterval...)与scheduledTimer(timeInterval...)方法的区别</h3>
<blockquote>
<ul>
<li>init(timeInterval...)创建出来的timer无法立刻使用，需要添加到NSRunloop中才可以正常工作</li>
</ul>
<p>「After creating it， you must add the timer to a run loop manually by calling the addTimer:forMode: method of the corresponding NSRunLoop object。」</p>
</blockquote>
<blockquote>
<ul>
<li>scheduledTimer(timeInterval...)创建出来的runloop已经被添加到当前线程的currentRunloop中来了。</li>
</ul>
<p>「Schedules it on the current run loop in the default mode。」</p>
</blockquote>
<h2 data-id="heading-7">WKScriptMessageHandler导致循环引用</h2>
<p>在之前的文章中我，我讲到<a href="https://juejin.cn/post/6971221137522966565" target="_blank" title="https://juejin.cn/post/6971221137522966565">Swift与JS方法互调</a>，讲到了在WebView中通过监听方法句柄，来进行JS调用Swift的方法，不知道注意到没有，<strong>在添加句柄的时候，没有使用self，而是通过WeakScriptMessageDelegate中间类来进行添加。</strong></p>
<pre><code class="copyable">let config = WKWebViewConfiguration()
config.userContentController.add(WeakScriptMessageDelegate(scriptDelegate: self), name: JSCallback)
let preferences = WKPreferences()
preferences.javaScriptCanOpenWindowsAutomatically = true
config.preferences = preferences

let webView = WKWebView(frame: CGRect.zero, configuration: config)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>因为如果直接这样<code>config.userContentController.add(self, name: JSCallback)</code>这样的话，是会导致循环引用的。</strong></p>
<p>WebViewController根本不会走析构函数，也就无法移除对应的监听方法的句柄：</p>
<pre><code class="copyable">deinit &#123;
    webView.configuration.userContentController.removeScriptMessageHandler(forName: JSCallback)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而WeakScriptMessageDelegate并没有什么特别支持，仅仅是让<strong>强持有</strong>变为<strong>弱持有</strong>：</p>
<pre><code class="copyable">import Foundation
import WebKit

class WeakScriptMessageDelegate: NSObject &#123;

    //MARK:- 属性设置 之前这个属性没有用weak修饰,所以一直持有,无法释放
    private weak var scriptDelegate: WKScriptMessageHandler!

    //MARK:- 初始化
    convenience init(scriptDelegate: WKScriptMessageHandler) &#123;
        self.init()
        self.scriptDelegate = scriptDelegate
    &#125;
&#125;

extension WeakScriptMessageDelegate: WKScriptMessageHandler &#123;
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) &#123;
        scriptDelegate.userContentController(userContentController, didReceive: message)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网上也有另外一种方式来解决WKScriptMessageHandler的循环引用问题，那就是在UIViewController的声明周期去解决，Timer也有这种方式：</p>
<pre><code class="copyable">    override func viewWillAppear(_ animated: Bool) &#123;
        super.viewWillAppear(animated)
        webView.configuration.userContentController.add(self, name: JSCallback)
    &#125;
    
    override func viewWillDisappear(_ animated: Bool) &#123;
        super.viewWillDisappear(animated)
        webView.configuration.userContentController.removeScriptMessageHandler(forName: JSCallback)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种与Controller声明周期绑定的方式并不好，因为它依赖的是其他类去触发条件，有不可控的因素在其中！</p>
<hr>
<p><strong>可以说Timer与WKScriptMessageHandler的循环引用，有一部分原因是苹果自身API设计的陷阱导致，那么一般我们怎么发现某个Controller、某个View、某个ViewModel有没有循环引用呢？</strong></p>
<h2 data-id="heading-8">如何发现自己编写的代码是否循环引用</h2>
<h3 data-id="heading-9">Cococa框架下的class</h3>
<ol>
<li>对于Cocoa框架下的类，由于都是继承于NSObject，所以在处理上会比较有统一性，我们先在NSObject上写一个分类，便于我们获取一个类的名称：</li>
</ol>
<pre><code class="copyable">// MARK: - 获取类的字符串名称
extension NSObject &#123;
    
    /// 对象获取类的字符串名称
    public var className: String &#123;
        return runtimeType.className
    &#125;
    
    /// 类获取类的字符串名称
    public static var className: String &#123;
        return String(describing: self)
    &#125;
    
    /// NSObject对象获取类型
    public var runtimeType: NSObject.Type &#123;
        return type(of: self)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>编写BaseViewController与BaseView，重写<code>deinit</code>方法，这里以BaseViewController为例子：</li>
</ol>
<pre><code class="copyable">class BaseViewController: UIViewController &#123;
    /// 其他业务代码省略
    
    deinit &#123;
        print("\(className)被销毁了")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>所有的子Controller与子View继承基类，通过在push到某个页面后，然后在进行pop操作，看看控制台是否有析构函数的打印。</li>
</ol>
<p>通过以上方式，我们可以看到页面是否有没有被销毁，进而排查问题了。</p>
<h3 data-id="heading-10">非Cococa框架下的的class</h3>
<p>针对非Cococa框架下的的class，我们可以写一个基类，这里我以<code>BaseViewModel</code>为例子：</p>
<pre><code class="copyable">class BaseViewModel &#123;
    /// 其他业务代码省略
    
    /// 模型名称
    var className: String &#123; String(describing: self) &#125;
    
    deinit &#123;
        print("\(className)被销毁了")
    &#125;
&#125;

class HotKeyViewModel: BaseViewModel &#123;
    /// 其他业务代码省略
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我同样在BaseViewModel中重<code>deinit</code>方法，然后其他的ViewModel都继承BaseViewModel，也可以通过打印日志查看对象是否销毁。</p>
<p>下图是打印的日志：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3bf54bfac3042c79074be252c9fec65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">需要注意的struct</h3>
<p><strong>注意struct创建的对象在栈中，而不是堆中，不需要进行其析构管理，你甚至根本就无法在struct中调用deinit函数。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a0d84b02f2a425e911cfb55704a989f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">Kingfisher中的处理方式</h2>
<p>如果你读过Kingfisher5的源码，你会发现，喵神对于对象的强弱引用导致的问题通过一个Delegate类进行了解决：</p>
<pre><code class="copyable">public class Delegate<Input, Output> &#123;
    public init() &#123;&#125;

    private var block: ((Input) -> Output?)?
    public func delegate<T: AnyObject>(on target: T, block: ((T, Input) -> Output)?) &#123;
        self.block = &#123; [weak target] input in
            guard let target = target else &#123; return nil &#125;
            return block?(target, input)
        &#125;
    &#125;

    public func call(_ input: Input) -> Output? &#123;
        return block?(input)
    &#125;

    public func callAsFunction(_ input: Input) -> Output? &#123;
        return call(input)
    &#125;
&#125;

extension Delegate where Input == Void &#123;
    public func call() -> Output? &#123;
        return call(())
    &#125;

    public func callAsFunction() -> Output? &#123;
        return call()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其具体例子，Kingfisher中的Delegate的注释已经做出了很好的说明：</p>
<pre><code class="copyable">/// You can create a `Delegate` and observe on `self`. Now, there is no retain cycle inside:
///
/// ```swift
/// // MyClass.swift
/// let onDone = Delegate<(), Void>()
/// func done() &#123;
///     onDone.call()
/// &#125;
///
/// // ViewController.swift
/// var obj: MyClass?
///
/// func doSomething() &#123;
///     obj = MyClass()
///     obj!.onDone.delegate(on: self) &#123; (self, _)
///         // `self` here is shadowed and does not keep a strong ref.
///         // So you can release both `MyClass` instance and `ViewController` instance.
///         self.reportDone()
///     &#125;
/// &#125;
/// ```
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然会麻烦一点，但是在闭包中，可以安全的使用self，而不用[weak self]的修饰，以及self的健壮性判断，可以少掉写头发。</p>
<h2 data-id="heading-13">weak还是unowned</h2>
<p>我们可能在一个对象的闭包中使用对象本身，经常用[weak target]修饰，其实还有一种修饰方式是[unowned target]，两者有什么差异？</p>
<p>下面这段话是我引用的网络上的一点说明：</p>
<blockquote>
<p>在 Swift 中除了 weak 以外，还有另一个冲着编译器叫喊着类似的 "不要引用我" 的标识符，那就是 unowned。它们的区别在哪里呢？如果您是一直写 Objective-C 过来的，那么从表面的行为上来说 unowned 更像以前的 unsafe_unretained，而 weak 就是以前的 weak。用通俗的话说，就是 unowned 设置以后即使它原来引用的内容已经被释放了，它仍然会保持对被已经释放了的对象的一个 "无效的" 引用，它不能是 Optional 值，也不会被指向 nil。如果你尝试调用这个引用的方法或者访问成员属性的话，程序就会崩溃。而 weak 则友好一些，在引用的内容被释放后，标记为 weak 的成员将会自动地变成 nil (因此被标记为 @weak 的变量一定需要是 Optional 值)。关于两者使用的选择，Apple 给我们的建议是如果能够确定在访问时不会已被释放的话，尽量使用 unowned，如果存在被释放的可能，那就选择用 weak。</p>
</blockquote>
<p>就问你读完了累不累，懂了没？</p>
<p>我说说我的理解：</p>
<ul>
<li>
<p>unowned使用，需要清晰的理解<code>target</code>对象的生命周期，万一调用的不好，就翻车了导致崩溃问题。<strong>简而言之，就是抓头发，掉头发。</strong></p>
</li>
<li>
<p>weak使用，可能需要使用<code>guard</code>去守护一下<code>target</code>，<strong>简而言之，就是多写点代码，但是不掉头发。</strong></p>
</li>
</ul>
<p>所以，我选择多写点代码而不掉头发的weak，如果使用喵神的<code>Delegate</code>类，[weak self]也可以不写，虽然会增添其他的代码量。</p>
<h2 data-id="heading-14">WeakProxy</h2>
<p>其实针对<strong>Cocoa框架下的强弱引用导致的循环应用</strong>，我们可以通过写一个比较通用的中间层来处理：</p>
<pre><code class="copyable">class WeakProxy: NSObject &#123;
    
    weak var target: NSObjectProtocol?
    
    init(target: NSObjectProtocol) &#123;
        self.target = target
        super.init()
    &#125;
    
    override func responds(to aSelector: Selector!) -> Bool &#123;
        return (target?.responds(to: aSelector) ?? false) || super.responds(to: aSelector)
    &#125;

    override func forwardingTarget(for aSelector: Selector!) -> Any? &#123;
        return target
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个运用了NSObject中的消息转发机制，以保证方法正确传递，同时通过弱引用消除了强引用导致的循环引用。</p>
<p>如果对WeakProxy增加一点扩展（实际上就是协议的实现），WeakScriptMessageDelegate是可以被代替的喔：</p>
<pre><code class="copyable">extension WeakProxy: WKScriptMessageHandler &#123;
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) &#123;
        (target as? WKScriptMessageHandler)?.userContentController(userContentController, didReceive: message)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>WeakProxy在WebView中的使用：</p>
<pre><code class="copyable">let config = WKWebViewConfiguration()

/// 之前这里是
/// config.userContentController.add(WeakScriptMessageDelegate(scriptDelegate: self), name: JSCallback)
config.userContentController.add(WeakProxy(target: self), name: JSCallback)
let preferences = WKPreferences()
preferences.javaScriptCanOpenWindowsAutomatically = true
config.preferences = preferences

let webView = WKWebView(frame: CGRect.zero, configuration: config)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">总结</h2>
<ul>
<li>
<p>大部分的循环引用是对象与对象相互的强引用导致，解决对象与对象的这种相互强引用方式是解决问题的根本。</p>
</li>
<li>
<p>Timer的导致循环引用情况特殊，它是由于主线程的runloop引用着timer，timer就不会自动销毁。timer引用着target，target也不会销毁。</p>
</li>
<li>
<p>本文通过Timer、WKScriptMessageHandler为出发点，通过引入中间层来减少相互强引用导致的循环引用问题，而Kingfisher中的<code>Delelgate</code>类，以及通用的<code>WeakProxy</code>是比较好的经验与例子分享。</p>
</li>
<li>
<p>通过对class基类重写<code>deinit</code>方法，通过继承打日志的方式去排查对象的销毁情况，有助于进行循环引用的问题分析。</p>
</li>
</ul>
<h2 data-id="heading-16">参考文章：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F9f387abfb2e8" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/9f387abfb2e8" ref="nofollow noopener noreferrer">深入浅出了解NSTimer循环引用的原因</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F9494ea08fe3a%3Futm_campaign%3Dmaleskine%26utm_content%3Dnote%26utm_medium%3Dseo_notes%26utm_source%3Drecommendation" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/9494ea08fe3a?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation" ref="nofollow noopener noreferrer">内存管理，weak 和 unowned</a></p>
<p><a href="https://juejin.cn/post/6844903944867545096#heading-0" target="_blank" title="https://juejin.cn/post/6844903944867545096#heading-0">iOS卡顿监测方案总结</a></p></div>  
</div>
            