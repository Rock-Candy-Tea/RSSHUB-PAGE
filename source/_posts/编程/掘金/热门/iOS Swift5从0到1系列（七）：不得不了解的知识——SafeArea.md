
---
title: 'iOS Swift5从0到1系列（七）：不得不了解的知识——SafeArea'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917f65c64d14440d93afb193dac26ee0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 14 Mar 2021 16:54:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917f65c64d14440d93afb193dac26ee0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>苹果在出了刘海屏后（iPhoneX），我们就需要考虑如何来适配竖屏、横屏的边界情况了。如果你百度过，你会发现非常多的，各种根据分辨率来判断是否是刘海屏而调整 UI 布局。然而，我们需要结合着应用的实际情况、使用人群、产品or公司要求，来考虑需要从哪个系统版本开始支持，例如：微信目前就是从 iOS 11 开始支持（IM 这块基本算是其一家独大），而对于电商APP这块，竞争非常的激烈，天猫、淘宝、pdd都还是从 iOS 9开始；站在这些APP的角度出发，电商是尽量不放过每一位用户，而微信是你周围朋友家人都使用，你如果系统低于 iOS 11，就可能『失联』，只能被迫升级至 iOS 11。本系列都是从 iOS 11开始，只是分享给大家学习。</p>
<h2 data-id="heading-1">二、适配考虑</h2>
<h3 data-id="heading-2">2.1、iOS 11 前后差别</h3>
<p>正如我在前言中所说，苹果第一款刘海屏手机是 iPhoneX，其搭载的 iOS 系统就是 11，因此，我们有如下适配选择：</p>
<ul>
<li>如果当前系统 < iOS 11，则不用考虑刘海屏；</li>
<li>如果当前系统 >= iOS 11，就需要考虑刘海屏来适配；</li>
</ul>
<h3 data-id="heading-3">2.2、为何需要考虑有无刘海屏的情况？</h3>
<p>当我们开发无导航栏页面（一级页面）或自定义导航栏时，我们要关注的点是：</p>
<ul>
<li>状态栏</li>
<li>导航栏</li>
<li>有刘海时的四周边界（竖/横屏时 Insets：top, bottom, left, right）</li>
<li>未来可能的变化</li>
</ul>
<p>苹果在出刘海机型之前，内部肯定早就有了屏幕如何适配的解决方案，而其给出的方案就是：『SafeArea』，又称安全区域。对于 iOS 11+的系统，我们只需要拿到 UIViewController.view.safeAreaInsets，就能知道当前四周的边界值，然后，我们就能正确去约束我们的视图和控件。</p>
<blockquote>
<p><strong><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>因此，正确的适配方案是：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;因此，正确的适配方案是：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">因</span><span class="mord cjk_fallback" style="color:red;">此</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">正</span><span class="mord cjk_fallback" style="color:red;">确</span><span class="mord cjk_fallback" style="color:red;">的</span><span class="mord cjk_fallback" style="color:red;">适</span><span class="mord cjk_fallback" style="color:red;">配</span><span class="mord cjk_fallback" style="color:red;">方</span><span class="mord cjk_fallback" style="color:red;">案</span><span class="mord cjk_fallback" style="color:red;">是</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span></strong></p>
<p>我们应当通过获取 SafeArea 后来考虑适配，而不是采用硬编码的方式来适配（这种方式是无穷无尽，无法100%满足的）。</p>
</blockquote>
<p><img alt="diff-screen-safe-area.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917f65c64d14440d93afb193dac26ee0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图通过 XIB 来更加直观的列举了两种屏幕在竖、横屏时的 SafeArea（安全区域），分别是：有刘海屏的（左一、二）和无刘海屏的（左三、四）XIB 。</p>
<p>如果你现在就动手去 coding，比如，尝试在 viewDidLoad 中去拿 SafeArea，实际上你拿出来的结果永远是 4 个 0；想要正确的获取 SafeArea 的值，我们需要先来理解一下 iOS 11 后，UIViewController 的生命周期方法及变动（大家先不看下一小节，也别百度谷歌，你能正确的说出来 UIViewController 的生命周期方式么？以及两个 VC 在 push & pop 后，生命周期又会调用哪些方法么？）。</p>
<h2 data-id="heading-4">三、UIViewController 生命周期</h2>
<p>下图给出了正常的、完整的 UIViewController 生命周期方法流程图：</p>
<ul>
<li>初始 UIViewController 的生命周期方法调用顺序；</li>
<li>push 时，两个 UIViewController 的生命周期方法调用顺序，以及；</li>
<li>pop 时，两个 UIViewController 的生命周期方法调用顺序；</li>
</ul>
<p>我们需要注意或了解的是：</p>
<ul>
<li>『loadViewIfNeeded』和『viewWillAppear』在正常初始化时的顺序，以及未销毁重新可见时的调用顺序；</li>
<li>iOS 11 新增的两个方法『viewLayoutMarginsDidChange』和『viewSafeAreaInsetsDidChange』；</li>
<li>构造器『init』和析构器『deinit』；</li>
<li>自定义 View 时，可能会用到『viewDidLayoutSubviews』；</li>
</ul>
<p><img alt="lifecycle.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a966217b0a444ff6bf524cf03e16c768~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图中已经给出了如何获取 SafeArea 的正确方法，下图将是举例如何设置一个 view 的两种方式：</p>
<p><img alt="two-ways-use-safe-area.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5a9311e6eb40dc8f5b0efaffe5ae8d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>源码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">BaseViewController</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        title <span class="hljs-operator">=</span> <span class="hljs-string">"二级页面"</span>
    &#125;
    
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewSafeAreaInsetsDidChange</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewSafeAreaInsetsDidChange()
        
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"view.safeAreaLayoutGuide = <span class="hljs-subst">\(view.safeAreaLayoutGuide)</span>"</span>)
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"<span class="hljs-subst">\n</span>"</span>)
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"view.safeAreaInsets = <span class="hljs-subst">\(view.safeAreaInsets)</span>"</span>)
        
        <span class="hljs-comment">// 两种方法使用 SafeArea：</span>
        <span class="hljs-comment">// 1. safeAreaLayoutGuide: 就是 frame</span>
        <span class="hljs-keyword">let</span> area <span class="hljs-operator">=</span> <span class="hljs-type">UIView</span>(frame: view.safeAreaLayoutGuide.layoutFrame)
        area.backgroundColor <span class="hljs-operator">=</span> <span class="hljs-type">UIColor</span>(hexVal: <span class="hljs-number">0x00007F7F</span>)
        view.addSubview(area)


        <span class="hljs-comment">// 2. safeAreaInsets: 就是四周边界，分别是 top, bottom, left, right</span>
<span class="hljs-comment">//        let area = UIView(frame: CGRect.zero)</span>
<span class="hljs-comment">//        area.backgroundColor = UIColor(hexVal: 0x00007F7F)</span>
<span class="hljs-comment">//        area.translatesAutoresizingMaskIntoConstraints = false</span>
<span class="hljs-comment">//        view.addSubview(area)</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">//        NSLayoutConstraint.activate([</span>
<span class="hljs-comment">//            area.topAnchor.constraint(equalTo: view.topAnchor, constant: view.safeAreaInsets.top),</span>
<span class="hljs-comment">//            area.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: view.safeAreaInsets.left),</span>
<span class="hljs-comment">//            area.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -view.safeAreaInsets.bottom),</span>
<span class="hljs-comment">//            area.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -view.safeAreaInsets.right)</span>
<span class="hljs-comment">//        ])</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">四、附录（生命周期方法解析）</h2>
<ul>
<li>
<p>init 构造器（类似构造函数）；</p>
<ul>
<li>当使用 Storyboard 时，控制器的构造器为 init(coder:)；</li>
<li>该构造器为必需构造器，如果重写其他构造器，则必须重写该构造器；</li>
<li>该构造器为可失败构造器，即有可能构造失败，返回 nil；</li>
<li>该方法来源自 NSCoding 协议，而 UIViewController 遵从这一协议；</li>
<li>该方法被调用意味着控制器有可能（并非一定）在未来会显示；</li>
<li>在控制器生命周期中，该方法只会被调用一次；</li>
</ul>
</li>
<li>
<p>loadView</p>
<ul>
<li>loadView() 即加载控制器管理的 view；</li>
<li>不能直接手动调用该方法；当 view 被请求却为 nil 时，该方法加载并创建 view；</li>
<li>若控制器有关联的 Nib 文件，该方法会从 Nib 文件中加载 view；如果没有，则创建空白 UIView 对象；</li>
<li>如果使用 Interface Builder 创建 view，则务必不要重写该方法；</li>
<li>可以使用该方法手动创建视图，且需要将根视图分配为 view；自定义实现不应该再调用父类的该方法；</li>
<li>执行其他初始化操作，建议放在 viewDidLoad() 中；</li>
</ul>
</li>
<li>
<p>viewDidLoad</p>
<ul>
<li>view 被加载到内存后调用 viewDidLoad()；</li>
<li>重写该方法需要首先调用父类该方法；</li>
<li>该方法中可以额外初始化控件，例如添加子控件，添加约束；</li>
<li>该方法被调用意味着控制器有可能（并非一定）在未来会显示；</li>
<li>在控制器生命周期中，该方法只会被调用一次；</li>
</ul>
</li>
<li>
<p>loadViewIfNeeded</p>
<ul>
<li>可以主动显式触发加载视图的方法；</li>
<li>只要是触发了 view 加载, 加载完成后就会触发 viewDidLoad 方法；</li>
<li>此时视图控制器的主视图可能还未加入到视图树中, 且绝大多数情况下都是(此时 view 的 window 属性还是 nil)!</li>
<li>不应在 viewDidLoad 中进行一些依赖于屏幕尺寸或窗口尺寸的操作(初学者常犯的错误)；</li>
</ul>
</li>
<li>
<p>viewWillAppear</p>
<ul>
<li>该方法在控制器 view 即将添加到视图层次时以及展示 view 时所有动画配置前被调用；</li>
<li>重写该方法需要首先调用父类该方法；</li>
<li>该方法中可以进行操作即将显示的 view，例如改变状态栏的取向，类型；</li>
<li>该方法被调用意味着控制器将一定会显示；</li>
<li>在控制器生命周期中，该方法可能会被多次调用；</li>
</ul>
</li>
<li>
<p>viewLayoutMarginsDidChange</p>
<ul>
<li>iOS 11后新API，根视图的边距变更时会触发该方法的回调</li>
</ul>
</li>
<li>
<p>viewSafeAreaInsetsDidChange</p>
<ul>
<li>iOS 11后新API，此时可以获取安全区的信息</li>
</ul>
</li>
<li>
<p>viewWillLayoutSubviews</p>
<ul>
<li>该方法在通知控制器将要布局 view 的子控件时调用；</li>
<li>每当视图的 bounds 改变，view 将调整其子控件位置；</li>
<li>该方法可重写以在 view 布局子控件前做出改变；</li>
<li>该方法的默认实现为空；</li>
<li>该方法调用时，AutoLayout 未起作用；</li>
<li>在控制器生命周期中，该方法可能会被多次调用；</li>
</ul>
</li>
<li>
<p>viewDidLayoutSubviews</p>
<ul>
<li>该方法在通知控制器已经布局 view 的子控件时调用；</li>
<li>该方法可重写以在 view 布局子控件后做出改变；</li>
<li>该方法的默认实现为空；</li>
<li>该方法调用时，AutoLayout 已经完成；</li>
<li>在控制器生命周期中，该方法可能会被多次调用；</li>
</ul>
</li>
<li>
<p>viewDidAppear</p>
<ul>
<li>该方法在控制器 view 已经添加到视图层次时被调用；</li>
<li>重写该方法需要首先调用父类该方法；</li>
<li>该方法可重写以进行有关正在展示的视图操作；</li>
<li>在控制器生命周期中，该方法可能会被多次调用；</li>
</ul>
</li>
<li>
<p>viewWillDisappear</p>
<ul>
<li>该方法在控制器 view 将要从视图层次移除时被调用；</li>
<li>该方法可重写以提交变更，取消视图第一响应者状态；</li>
</ul>
</li>
<li>
<p>viewDidDisappear</p>
<ul>
<li>该方法在控制器 view 已经从视图层次移除时被调用；</li>
<li>该方法可重写以清除或隐藏控件；</li>
</ul>
</li>
<li>
<p>deinit</p>
<ul>
<li>控制器销毁时（离开堆），调用该方法</li>
</ul>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            