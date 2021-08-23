
---
title: '真实案例引发的iOS底层实现窥探'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7525d4d204344ce8ae36503c0062d50b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 00:29:59 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7525d4d204344ce8ae36503c0062d50b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><strong>导读</strong></h3>
<p>来自搜狐技术产品：</p>
<p>本文源于项目中实际遇到的一个真实案例，从一个具体的UITableView实现的例子引出，试图通过SIL（Swift Intermediate Language）这个中间语言，探究iOS系统框架的实现细节。</p>
<p>在此过程中，我们也讨论了什么是thunk函数，Swift消息派发方式，并通过不断修改代码，进行对比测试的方式，验证结论和猜想，希望抛砖引玉引发大家更多的思考。</p>
<p><strong>一、问题引出</strong></p>
<p>先来看下面这段代码，是一个常见的tableView的使用场景：</p>
<pre><code class="copyable">protocol ListDataProtocol &#123;&#125;class BaseViewController<P: ListDataProtocol>:UIViewController,UITableViewDelegate,UITableViewDataSource &#123;    var tableView: UITableView    var presenter: P?    override func viewDidLoad() &#123;        //省略非必要实现细节    &#125;    override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) &#123;        //省略非必要实现细节    &#125;    required init?(coder: NSCoder) &#123;        //省略非必要实现细节    &#125;    //MARK: UITableViewDataSource    // cell的个数    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int &#123;        return 10    &#125;    // UITableViewCell    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell &#123;        //省略非必要实现细节    &#125;    //MARK: UITableViewDelegate    // 设置cell高度    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat &#123;        return 44.0    &#125;&#125;class ListData: NSObject, ListDataProtocol&#123;&#125;class ViewController: BaseViewController<ListData> &#123;    override func viewDidLoad() &#123;        super.viewDidLoad()        // Do any additional setup after loading the view.    &#125;    // 选中cell后执行此方法   func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) &#123;        print(indexPath.row)   &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们简单了解一下这段代码，基类BaseViewController包含iOS中UITableView的DataSource和Delegate的基础实现，子类ViewController继承基类，由于基类中不知道如何处理具体的业务细节，所以只包含必须的代理实现，而其他可选的代理实现，预期由子类实现，所以在子类ViewController中实现了<strong>table(_:didSelectRowAt:)</strong>，用于处理Cell选中事件。</p>
<p><strong>那么问题来了，请问执行这段代码时，点击cell是否会如预期输出<strong><strong>print(indexPath.row)</strong></strong>？</strong></p>
<p>**答案是：****没有输出，****table(_:didSelectRowAt:)**<strong>不会被调用执行，那么为什么呢？</strong></p>
<p>由于涉及到系统的Fundation框架的具体实现，查找官方文档和Google都不能找到答案，所以想到了利用Swift提供的中间语言SIL（Swift Intermediate Language）去尝试能否发现一些底层的实现的蛛丝马迹，帮助我们理解。</p>
<p>如果你不了解SIL，建议首先阅读<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU3NTY3MTQzMg%3D%3D%26mid%3D2247485644%26idx%3D1%26sn%3D648137faded749e6bc67948906dbee7b%26chksm%3Dfd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=MzU3NTY3MTQzMg==&mid=2247485644&idx=1&sn=648137faded749e6bc67948906dbee7b&chksm=fd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>《Swift Intermediate Language 初探》</strong></a><strong>。</strong><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU3NTY3MTQzMg%3D%3D%26mid%3D2247485644%26idx%3D1%26sn%3D648137faded749e6bc67948906dbee7b%26chksm%3Dfd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=MzU3NTY3MTQzMg==&mid=2247485644&idx=1&sn=648137faded749e6bc67948906dbee7b&chksm=fd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"></a></p>
<p><strong>二、生成SIL</strong></p>
<pre><code class="copyable">swiftc -emit-silgen -target x86_64-apple-ios13.0-simulator -sdk $(xcrun --show-sdk-path --sdk iphonesimulator)  -Onone test.swift > test.swift.sil
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>由于我们需要使用到UIKit这类系统库，所以需要使用-sdk参数指定依赖的SDK路径；</p>
</li>
<li>
<p>-target 指定生成代码对应的target；</p>
</li>
<li>
<p>-Onone 不进行任何优化。</p>
</li>
</ul>
<p><strong>三、SIL分析</strong></p>
<p><strong>thunk函数</strong></p>
<p>thunk函数<strong>①</strong>，是一个不得不提的概念，我借用阮一峰老师博客<strong>②</strong>一段话来说明：</p>
<p>编程语言刚刚起步时，编译器怎么写比较好。一个争论的焦点是**"求值策略"**<strong>③</strong>，即函数的参数到底应该何时求值。</p>
<pre><code class="copyable">var x = 1;function f(m)&#123;  return m * 2;     &#125;f(x + 5)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一种意见是**"传值调用"**<strong>④</strong>（call by value），即在进入函数体之前，就计算 x + 5 的值（等于6），再将这个值传入函数 f 。C语言就采用这种策略。</p>
<pre><code class="copyable">f(x + 5)// 传值调用时，等同于f(6)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种意见是**"传名调用"**<strong>⑤</strong>（call by name），即直接将表达式 x + 5 传入函数体，只在用到它的时候求值。Hskell语言采用这种策略。</p>
<pre><code class="copyable">f(x + 5)// 传名调用时，等同于(x + 5) * 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传值调用和传名调用，哪一种比较好？回答是各有利弊。传值调用比较简单，但是对参数求值的时候，实际上还没用到这个参数，有可能造成性能损失。</p>
<p><strong>编译器的"传名调用"实现，往往是将参数放到一个临时函数之中，再将这个临时函数传入函数体。这个临时函数就叫做 Thunk 函数。</strong></p>
<p>Swift SIL当中的thunk函数的基本思想与上面描述的是一致的，但是作用稍有不同，我们来看文章开头这个例子中，<strong>BaseViewController.viewDidLoad</strong>函数对应的SIL片段，借此了解thunk函数的作用。</p>
<pre><code class="copyable">// BaseViewController.viewDidLoad()sil hidden [ossa] @$s4test18BaseViewControllerC11viewDidLoadyyF : $@convention(method) <P where P : ListDataProtocol> (@guaranteed BaseViewController<P>) -> () &#123;// %0                                             // users: %89, %88, %87, %80, %79, %78, %72, %71, %53, %11, %10, %2, %1bb0(%0 : @guaranteed $BaseViewController<P>)://暂时省略无关代码bb1:                                              // Preds: bb0//暂时省略无关代码// %70                                            // users: %77, %75, %74bb2(%70 : @owned $UIView):                        // Preds: bb0//暂时省略无关代码&#125; // end sil function '$s4test18BaseViewControllerC11viewDidLoadyyF'// @objc BaseViewController.viewDidLoad()sil hidden [thunk] [ossa] @$s4test18BaseViewControllerC11viewDidLoadyyFTo : $@convention(objc_method) <P where P : ListDataProtocol> (BaseViewController<P>) -> () &#123;// %0                                             // user: %1bb0(%0 : @unowned $BaseViewController<P>)://暂时省略无关代码  // function_ref BaseViewController.viewDidLoad()  %3 = function_ref @$s4test18BaseViewControllerC11viewDidLoadyyF : $@convention(method) <τ_0_0 where τ_0_0 : ListDataProtocol> (@guaranteed BaseViewController<τ_0_0>) -> () // user: %4  %4 = apply %3<P>(%2) : $@convention(method) <τ_0_0 where τ_0_0 : ListDataProtocol> (@guaranteed BaseViewController<τ_0_0>) -> () // user: %7//暂时省略无关代码                             // id: %7&#125; // end sil function '$s4test18BaseViewControllerC11viewDidLoadyyFTo'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于篇幅所限，这段代码中省略了一些解释问题非必要的代码，如果需要查看完整代码请参见文末下载地址。</p>
<p>你会发现生成了两段<strong>viewDidLoad</strong>，第一段是一个原生的Swift函数，使用<strong>convention(method)<strong>方式调用和处理，它内部有三个block块，分别实现一些具体的功能：bb0完成一些变量的分配和初始化；bb1完成代码诊断相关工作；bb2完成BaseViewController中TableView的Delegate和DataSource的设置，这三部分构成了完整的</strong>viewDidLoad</strong>函数。</p>
<p>第二段，它是一个thunk函数，它的标识id是**@$$s4test18BaseViewControllerC11viewDidLoadyyFTo**，对比一下第一段id是**@$s4test18BaseViewControllerC11viewDidLoadyyF**，第二段的id是在第一段的基础上增加了两个单词To，并且通过@convention(objc_method)可以看到，它是使用ObjC方式调用的；它的内部使用Swift原生方式调用第一段的函数；</p>
<p>整个流程如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7525d4d204344ce8ae36503c0062d50b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单总结一下，在SIL中生成了一个新的thunk函数，这个函数用于暴露给ObjC进行交互，而thunk函数内部会调用真正的原生Swift函数。那么也就是说，如果一个函数需要被ObjC可见，需要包装为一个支持ObjC方式调用的thunk函数。</p>
<p><strong>Swift消息派发方式</strong></p>
<p>简单来说，Swift有两种消息派发方式：</p>
<ul>
<li>
<p><strong>静态派发(static dispatch)</strong>,静态派发在执行的时候，会直接跳到方法的实现，静态派发可以进行inline和其他编译期优化,值类型总是会使用静态派发，因为不存在继承可变的可能；</p>
</li>
<li>
<p><strong>动态派发(dynamic dispatch)</strong>，动态派发在执行的时候，会根据运行时(Runtime)，采用table的方式，找到方法的执行体，然后执行。动态派发也就没有办法像静态派发那样，进行编译期优化。</p>
</li>
</ul>
<p>有些文章还会提到，第三种派发方式，Objective-C派发，其实Swift代码当中的这种方式的本质就是我们前面提到的thunk函数机制，它涉及两个Swift关键字@objc和dynamic：@objc意味着你的Swift代码，如类，方法，属性，将会被Objective-C可见；dynamic意味着你要是用Objective-C动态派发；</p>
<p>但是这两个参数其实并不是单独使用的，如果使用了dynamic就必须添加@objc，但是反过来可以单独@objc，区分开来使得每个关键字的含义更清晰。使用@objc和dynamic组合生成的函数，采用Objective-C派发，不会出现在SIL的VTable表中的；而单独添加@objc的函数是会出现在VTable表中的， 采用的Swift动态派发。</p>
<p>另外，需要提到的是@objc可见性，在Swift4以前，从NSObject继承的类中的方法是由编译器自动暴露给Objective-C可见，但是从Swift4以后，需要手动添加@objc明确指明，编译器不再进行推断。反映到SIL也是一致的，如果生成的函数标记为@objc才能被Objective-C可见。</p>
<p>关于VTable和Witness Table如果不很了解，建议还是先阅读<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU3NTY3MTQzMg%3D%3D%26mid%3D2247485644%26idx%3D1%26sn%3D648137faded749e6bc67948906dbee7b%26chksm%3Dfd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=MzU3NTY3MTQzMg==&mid=2247485644&idx=1&sn=648137faded749e6bc67948906dbee7b&chksm=fd1ed52bca695c3d2345a907d295a545c73cf61e5ea7cb4063c3d063a0cd8903ad9f1a545424&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>《Swift Intermediate Language 初探》</strong></a><strong>。</strong></p>
<p><strong>四</strong>**、答案探寻**</p>
<p>有了前面的基础，我们来探索答案，把焦点定位到**table(_:didSelectRowAt:)**关键字</p>
<pre><code class="copyable">sil_vtable BaseViewController &#123;//暂时省略无关代码  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, Int) -> Int : @$s4test18BaseViewControllerC05tableC0_21numberOfRowsInSectionSiSo07UITableC0C_SitF    // BaseViewController.tableView(_:numberOfRowsInSection:)  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, IndexPath) -> UITableViewCell : @$s4test18BaseViewControllerC05tableC0_12cellForRowAtSo07UITableC4CellCSo0jC0C_10Foundation9IndexPathVtF    // BaseViewController.tableView(_:cellForRowAt:)  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, IndexPath) -> CGFloat : @$s4test18BaseViewControllerC05tableC0_14heightForRowAt12CoreGraphics7CGFloatVSo07UITableC0C_10Foundation9IndexPathVtF    // BaseViewController.tableView(_:heightForRowAt:)  #BaseViewController.deinit!deallocator.1: @$s4test18BaseViewControllerCfD    // BaseViewController.__deallocating_deinit&#125;sil_vtable ViewController &#123;//暂时省略无关代码  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, Int) -> Int : @$s4test18BaseViewControllerC05tableC0_21numberOfRowsInSectionSiSo07UITableC0C_SitF [inherited]    // BaseViewController.tableView(_:numberOfRowsInSection:)  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, IndexPath) -> UITableViewCell : @$s4test18BaseViewControllerC05tableC0_12cellForRowAtSo07UITableC4CellCSo0jC0C_10Foundation9IndexPathVtF [inherited]    // BaseViewController.tableView(_:cellForRowAt:)  #BaseViewController.tableView!1: <P where P : ListDataProtocol> (BaseViewController<P>) -> (UITableView, IndexPath) -> CGFloat : @$s4test18BaseViewControllerC05tableC0_14heightForRowAt12CoreGraphics7CGFloatVSo07UITableC0C_10Foundation9IndexPathVtF [inherited]    // BaseViewController.tableView(_:heightForRowAt:)  #ViewController.tableView!1: (ViewController) -> (UITableView, IndexPath) -> () : @$s4test14ViewControllerC05tableB0_14didSelectRowAtySo07UITableB0C_10Foundation9IndexPathVtF    // ViewController.tableView(_:didSelectRowAt:)  #ViewController.deinit!deallocator.1: @$s4test14ViewControllerCfD    // ViewController.__deallocating_deinit&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于基类BaseViewController中没有实现<strong>table(_:didSelectRowAt:)</strong>，所以基类sil_vtable表中没有对应函数签名，这很正常；子类ViewController有实现，所以出现<strong>table(_:didSelectRowAt:)</strong>，但是请注意它不是一个thunk函数。</p>
<p>对比如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ec5975fca5b4305ac923b8de33934e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再看**table(_:didSelectRowAt:)**的实现部分SIL</p>
<pre><code class="copyable">// ViewController.tableView(_:didSelectRowAt:)sil hidden [ossa] @$s4test14ViewControllerC05tableB0_14didSelectRowAtySo07UITableB0C_10Foundation9IndexPathVtF : $@convention(method) (@guaranteed UITableView, @in_guaranteed IndexPath, @guaranteed ViewController) -> () &#123;// %0                                             // user: %3// %1                                             // users: %13, %4// %2                                             // user: %5bb0(%0 : @guaranteed $UITableView, %1 : $*IndexPath, %2 : @guaranteed $ViewController):  //省略内部实现&#125; // end sil function '$s4test14ViewControllerC05tableB0_14didSelectRowAtySo07UITableB0C_10Foundation9IndexPathVtF'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先没有@objc的标记，没有thunk的标记，所以根据前面的知识可得，虽然ViewController实现了<strong>table(_:didSelectRowAt:)</strong>，但是这个函数在生成的SIL中是一个纯粹的原生Swift函数，编译器没有帮助它生成对应的Objective-C可见的thunk函数，所以无法被UITabview回调使用，到此我们已经回答了开头的问题。</p>
<p>**那么为什么编译器不去生成呢？**<strong>什么情况下编译器会生成thunk函数呢？</strong></p>
<p>**五、**<strong>对比试验</strong></p>
<p>我们先来做两个对比试验：</p>
<p><strong>Test1</strong></p>
<p>开篇问题的代码中，如果你删除跟presenter泛型相关的代码，删除ListDataProtocol协议，重新运行一下，结果，**print(indexPath.row)**正常输出了，怎么解释呢？</p>
<p>我们还是借助SIL语言，分析去掉前述内容后生成的SIL：</p>
<ul>
<li>
<p>ViewController的sil_vtable表中有**table(_:didSelectRowAt:)**与当前一致；</p>
</li>
<li>
<p>除原始的**table(_:didSelectRowAt:)**实现外，生成了带@objc标记的thunk函数；；</p>
</li>
<li>
<p>BaseViewController和ViewController都被直接标记为@objc（没有泛型，都是基于UIKit，需要依赖Objective-C runtime，所以可以被默认推断Objective-C可见）。</p>
</li>
</ul>
<p><strong>Test2</strong></p>
<p>还是开篇问题的代码中，如果在基类实现<strong>table(_:didSelectRowAt:)</strong>，在子类修改<strong>table(_:didSelectRowAt:)<strong>添加</strong>override</strong>，重新运行一下，执行结果：**print(indexPath.row)**正常输出</p>
<p>查看修改后生成的SIL：</p>
<ul>
<li>
<p>基类BaseViewController和子类的ViewController各自的sil_vtable中，都有<strong>table(_:didSelectRowAt:)</strong>，且子类中对应方法标记为**[override**]；</p>
</li>
<li>
<p>除原始的**table(_:didSelectRowAt:)**实现外，生成了带@objc标记的thunk函数；</p>
</li>
<li>
<p>BaseViewController和ViewController没有被标记@objc。</p>
</li>
</ul>
<p>对比一下，相同点，都生成了thunk函数，所以结果能够正常输出！不同点，没有泛型情况，编译器默认推断生成Objc可见；有泛型情况，只有基类实现对应方法，子类的实现方法才会被编译器推断生成thunk函数。</p>
<p><strong>六、小结</strong></p>
<p>查阅SIL的官方文档<strong>⑥</strong>有这样一段话:</p>
<p>If a derived class conforms to a protocol through inheritance from its base class, this is represented by an inherited protocol conformance, which simply references the protocol conformance for the base class.</p>
<p>简单翻译一下：</p>
<p>如果派生类通过从其基类继承而符合协议，这种称为继承协议一致性表示（inherited protocol conformance），<strong>它会简单引用基类的协议实现</strong>。</p>
<p>这句话就可以解释我们的问题了，设计编译器时在这种场景下，它只会简单引用基类的实现，所以基类中必须有<strong>table(_:didSelectRowAt:)</strong>，子类的**table(_:didSelectRowAt:)**才会被可见！</p>
<p><strong>七、猜想</strong></p>
<p>在文章的末尾，我想再提出一个问题，我们大胆猜想一下为什么编译器设计为<strong>简单引用基类的协议实现</strong>，猜测是编译效率的考量！</p>
<p>以Tableview为例，它的DataSource和Delegate中绝大部分是可选的实现，如果编译器不按照现在的逻辑处理，很可能的方式，就需要层层遍历所有子类，查找所有可能的代理函数实现，然后把他们都转成thunk函数，才能实现文章开头的预期效果，显然是一个十分耗时的过程，并且这样操作就如同swift调整@objc的推断一样，是在代替使用者做决策。</p>
<p>如有错误欢迎批评指正！</p>
<p>所有源文件下载地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank">Github</a></p></div>  
</div>
            