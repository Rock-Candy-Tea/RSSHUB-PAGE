
---
title: 'iOS Swift5从0到1系列（三）：学习UINavigationController（1）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1798ca0c6c8946d386c06ca914660776~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 08 Mar 2021 19:32:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1798ca0c6c8946d386c06ca914660776~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>上篇，我们仿了京东的底部导航栏，显示了5个页面（UIViewController），它的作用你可以理解为页面之间的切换，每个页面都属于一级页面；而一级页面一般只是一些吸引用户的的主要流量入口，实际的功能页面都是通过这些一级页面的入口导航到下一级或是更深一级的页面（从用户角度来看，核心重要的页面最多不超过三级，否则层级太深，用户可能就没兴趣继续点下去了，除了『确认订单』和『支付』页面）。</p>
<p>N级页面之间的切换，不会再涉及到底部导航控制器，它没那功能；在 iOS 中，具体页面间导航功能的就是我们今天要学习的 UINavigationController，即导航控制器，它能够实现不同页面之间的进入与退出。</p>
<h2 data-id="heading-1">二、导航控制器（UINavigationController）</h2>
<p>导航控制器就是负责页面切换的，同样，我们先来看看官方源码注释：</p>
<blockquote>
<p>UINavigationController manages a stack of view controllers and a navigation bar.</p>
<p>导航控制器通过数据结构『栈』的方式来管理一组 ViewController，并且它自带导航栏。</p>
<p>It performs horizontal view transitions for pushed and popped views while keeping the navigation bar in sync.</p>
<p>默认情况下，push 操作（进入下一级页面）和 pop 操作（返回到上一级页面）的转场动画是一个平移，并且，导航控制器会保持导航栏（状态的）同步。</p>
</blockquote>
<p>如果你觉得上面的注释看不懂也没关系，接下来我会分析，知道的朋友可以直接跳下一小节（不太建议，有些细节『老司机』也不一定掌握 -_-|||）。我们先来看看 UIKit.UINavigationController 源码，了解其内部的核心对象和方法。</p>
<h3 data-id="heading-2">2.1、UINavigationController 分析</h3>
<p><strong>精华注释.....</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">2.0</span>, <span class="hljs-operator">*</span>)
<span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UINavigationController</span> : <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-comment">// 构造器，需要一个 UIViewController 作为根视图控制器</span>
    <span class="hljs-comment">// 初始化时，它会将这个 UIViewController 以 push 且没有动画的方式放入栈中</span>
    <span class="hljs-comment">// 该 UIViewController 将是栈中第一个视图控制器</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">rootViewController</span>: <span class="hljs-type">UIViewController</span>)</span> 
    
    <span class="hljs-comment">// 默认使用平移动画进入下一个页面，如果当前的页面已在栈顶，则没有任何效果</span>
    <span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">pushViewController</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">viewController</span>: <span class="hljs-type">UIViewController</span>, <span class="hljs-params">animated</span>: <span class="hljs-type">Bool</span>)</span> 

    <span class="hljs-comment">// 返回页面有三种方式：</span>
    <span class="hljs-comment">// 1. 返回上一级页面：即从哪里来的，回到哪里去</span>
    <span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">popViewController</span>(<span class="hljs-params">animated</span>: <span class="hljs-type">Bool</span>)</span> -> <span class="hljs-type">UIViewController</span>? 
    <span class="hljs-comment">// 2. 返回到指定的页面：你可以使用该方法返回上一级面页，也可以直接返回到根页面</span>
    <span class="hljs-comment">// 对于返回到指定的页面，则该页面所在栈中之上的所有页面都将出栈并销毁（这些页面的出栈不可见）</span>
    <span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">popToViewController</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">viewController</span>: <span class="hljs-type">UIViewController</span>, <span class="hljs-params">animated</span>: <span class="hljs-type">Bool</span>)</span> -> [<span class="hljs-type">UIViewController</span>]<span class="hljs-operator">?</span> 
    <span class="hljs-comment">// 3. 返回到第一个页面</span>
    <span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">popToRootViewController</span>(<span class="hljs-params">animated</span>: <span class="hljs-type">Bool</span>)</span> -> [<span class="hljs-type">UIViewController</span>]<span class="hljs-operator">?</span> 
    
    <span class="hljs-comment">// 当前栈中存在的页面，我们可以通过遍历：</span>
    <span class="hljs-comment">// 1. pop操作来返回到我们想要返回的页面</span>
    <span class="hljs-comment">// 2. 通过个数来做一些判断操作（后面会用到）</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> viewControllers: [<span class="hljs-type">UIViewController</span>] 
    
    <span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">7.0</span>, <span class="hljs-operator">*</span>)
    <span class="hljs-comment">// 这个没有英文注释，不过，我们都会用到</span>
    <span class="hljs-comment">// 我们也看到了它的出现是在 7.0 以后，而它的功能就是：（右）侧滑返回上一级而面的手势</span>
    <span class="hljs-comment">// 因为苹果手机屏幕越来越大了嘛，总是让用户点『返回』按钮来返回到上一级，体验不好嘛</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> interactivePopGestureRecognizer: <span class="hljs-type">UIGestureRecognizer</span>? &#123; <span class="hljs-keyword">get</span> &#125;
    
    <span class="hljs-comment">// 导航栏，管理 navigationItem，同样使用栈来管理（为啥？）</span>
    <span class="hljs-comment">// 因为每个 VC 都对应着一个 navigationItem</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> navigationBar: <span class="hljs-type">UINavigationBar</span> &#123; <span class="hljs-keyword">get</span> &#125; 
    
    <span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">3.0</span>, <span class="hljs-operator">*</span>)
    <span class="hljs-comment">// tool条，含有 title 和 image</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> toolbar: <span class="hljs-type">UIToolbar</span>! &#123; <span class="hljs-keyword">get</span> &#125;
    
    <span class="hljs-comment">// 其它请自行查看</span>
    <span class="hljs-operator">......</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上列出的方法和成员都是我们将来会用的着的，且会经常打交道，不过，类似于 UITabBarController，基本上只会打交道一次，为啥？因为一般我们都会在封装在基类中，由基类来统一管理，如果每个页面自己管理，则很容易乱套（苹果自己对这块都是非常混乱），而我给大家分享的，都是通过实践来告诉大家避免踩坑的最终结果。</p>
<h3 data-id="heading-3">2.2、扩展 UINavigationController 分析</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-comment">// 大家可以自行创建导航栏的外观（左、右按钮，标题，文字、图片、颜色和透明度）</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> navigationItem: <span class="hljs-type">UINavigationItem</span> &#123; <span class="hljs-keyword">get</span> &#125; 
    <span class="hljs-comment">// 这个属性默认是 Swift: false / OC: NO，但这个属性在遇到 UITabBarController 时会有用处</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> hidesBottomBarWhenPushed: <span class="hljs-type">Bool</span> 
    <span class="hljs-comment">// 我们通过 navigationController 来 push / pop 操作</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> navigationController: <span class="hljs-type">UINavigationController</span>? &#123; <span class="hljs-keyword">get</span> &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.3、导航栏元素：UINavigationItem 分析</h3>
<p>我们可以结合着如下图片来分析了解：</p>
<p><img alt="navigation-bar-elements.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1798ca0c6c8946d386c06ca914660776~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">2.0</span>, <span class="hljs-operator">*</span>)
<span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UINavigationItem</span> : <span class="hljs-title">NSObject</span>, <span class="hljs-title">NSCoding</span> </span>&#123;
    <span class="hljs-comment">// 标题，默认 nil，在 UI层级的最顶层</span>
    <span class="hljs-comment">// 可以通过：Debug View Hierachy 查看视图的层级</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> title: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 可以自定义标题视图（比如：放张图片），只有它在 UI最顶层才有效</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> titleView: <span class="hljs-type">UIView</span>?

    <span class="hljs-comment">// 返回键 （左边按钮）</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> backBarButtonItem: <span class="hljs-type">UIBarButtonItem</span>?
    
    <span class="hljs-comment">// leftBarButtonItems 和 rightBarButtonItems 在以前只是一个单一按钮，现在管理着一组按钮；</span>
    <span class="hljs-comment">// 这两分别对应着每个数组中的第一个元素</span>
    <span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">5.0</span>, <span class="hljs-operator">*</span>)
    <span class="hljs-comment">// 左按钮</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> leftBarButtonItems: [<span class="hljs-type">UIBarButtonItem</span>]<span class="hljs-operator">?</span>

    <span class="hljs-keyword">@available</span>(<span class="hljs-keyword">iOS</span> <span class="hljs-number">5.0</span>, <span class="hljs-operator">*</span>)
    <span class="hljs-comment">// 右按钮</span>
    <span class="hljs-keyword">open</span> <span class="hljs-keyword">var</span> rightBarButtonItems: [<span class="hljs-type">UIBarButtonItem</span>]<span class="hljs-operator">?</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要就是以上元素，如果在这里你没有任何疑惑，那么我是非常疑惑的！为啥？你没发现有两个元素都能控制『左侧按钮』么？分别是：</p>
<ul>
<li>backBarButtonItem；</li>
<li>leftBarButtonItem；</li>
</ul>
<hr>**如果同时设置了这两会有什么结果？**
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>官方没有说，我们都是通过实践得出的真理：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;官方没有说，我们都是通过实践得出的真理：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">官</span><span class="mord cjk_fallback" style="color:red;">方</span><span class="mord cjk_fallback" style="color:red;">没</span><span class="mord cjk_fallback" style="color:red;">有</span><span class="mord cjk_fallback" style="color:red;">说</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">我</span><span class="mord cjk_fallback" style="color:red;">们</span><span class="mord cjk_fallback" style="color:red;">都</span><span class="mord cjk_fallback" style="color:red;">是</span><span class="mord cjk_fallback" style="color:red;">通</span><span class="mord cjk_fallback" style="color:red;">过</span><span class="mord cjk_fallback" style="color:red;">实</span><span class="mord cjk_fallback" style="color:red;">践</span><span class="mord cjk_fallback" style="color:red;">得</span><span class="mord cjk_fallback" style="color:red;">出</span><span class="mord cjk_fallback" style="color:red;">的</span><span class="mord cjk_fallback" style="color:red;">真</span><span class="mord cjk_fallback" style="color:red;">理</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span></p>
<blockquote>
<p>前提：previousVC 是上一个页面，nextVC 是下一个页面，当发生 push 时，有如下规则：</p>
<ol>
<li>如果 nextVC 的 leftBarButtonItem != nil，那么将在 navigationBar 的左边显示 nextVC 指定的 leftBarButtonItem；</li>
<li>如果 nextVC 的 leftBarButtonItem == nil，previousVC 的 backBarButtonItem != nil，那么将在 navigationBar 的左边显示 previousVC 指定的 backBarButtonItem；</li>
<li>如果两者都为 nil 则：</li>
</ol>
<ul>
<li>3.1. nextVC 的 navigationItem.hidesBackButton = YES，那么 navigationBar 将隐藏左侧按钮；</li>
<li>3.2. 否则 navigationBar的左边将显示系统提供的默认返回按钮；</li>
</ul>
</blockquote>
<hr>
<blockquote>
<p>我们从以上规则中发现：</p>
<ol>
<li>leftBarButtonItem 的优先级比 backBarButtonItem 要高；</li>
<li>backBarButtonItem 是来自上一个页面，如果当前 VC 是第一个页面，那么它没有上一个页面，也就没有 backBarButtonItem；</li>
<li>leftBarButtonItem 是来自当前页面，与上个页面无关，因此，如果当前 VC 是第一个页面，那么设置了 leftBarButtonItem 就会很奇怪；</li>
</ol>
</blockquote>
<p>因此，请注意上面的左侧按钮规则，千万不要同时设置，虽然有优先级保证不会显示两个按钮，但是你的显示逻辑可能就不一样了！</p>
<p>分析完了这么多，我们用一张大图来总结一下：</p>
<p><img alt="UINavigationController.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60b240fec1474158819c7f40b3a5fb96~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">三、UINavigationController 的使用</h2>
<h3 data-id="heading-6">3.1、使用方式</h3>
<p>它的使用很简单，逃脱不开的模式，即 window.rootViewController 的设置有以下三种：</p>
<ol>
<li>直接设置；</li>
</ol>
<pre><code class="copyable">// AppDelegate 中
window?.rootViewController = UINavigationController(rootViewController: XXXViewController())
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>UITabBarController 嵌套 UINavigationController；</li>
</ol>
<pre><code class="copyable">// AppDelegate 中
window?.rootViewController = MainTabBarController()

// MainTabBarController 中
let xxx = UINavigationController(rootViewController: XXXViewController())
xxx.tabBarItem.title = "xxx"
viewControllers = [xxx, ......]
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>UINavigationController 嵌套 UITabBarController（可能再嵌套 UINavigationController，就和第2种差不多了）；</li>
</ol>
<pre><code class="copyable">// AppDelegate 中
window?.rootViewController = UINavigationController(rootViewController: MainTabBarController())

// 可能再嵌套如下
// MainTabBarController 中
let xxx = UINavigationController(rootViewController: XXXViewController())
xxx.tabBarItem.title = "xxx"
viewControllers = [xxx, ......]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上方式，我们能发现，常用的模式不是第 1 种，就是第 2 种。</p>
<h3 data-id="heading-7">3.2、实战出真理</h3>
<p>基于我们上一篇的例子，我们采用第 2 种方式来使用。</p>
<ul>
<li>简单改造如下</li>
</ul>
<p><img alt="wrap-with-uinavigation-controller.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1962563bc51f4c98be8af4c681dc25c7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>修改 HomeViewController</li>
</ul>
<p><img alt="homevc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07bc69fd196944f494bb43005feb5166~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>运行模拟器</li>
</ul>
<p><img alt="run-simu.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7205e6053c40c48e92094ccb4495cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们的导航栏（带标题）就出来了，这里需要注意一点：iOS 7.0 后，改为了扁平风格，这里的导航栏也就变成的半透明效果！</p>
<h3 data-id="heading-8">3.3、页面跳转 push & pop</h3>
<ul>
<li>修改我们的 HomeViewController</li>
</ul>
<p><img alt="tap.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/992c8cf2acc84092b970b23363b7e647~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>点击 label，push 到下一级页面</li>
</ul>
<p><img alt="push.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86aef2dba3014091ae3b29cea33dfd77~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>跳转稳定后，如下图</li>
</ul>
<p><img alt="back.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd9ae438ea264596beb33747ab64f072~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">四、总结</h2>
<p>本篇只是分析了导航控制器和最基本的使用，下一篇，我们会根据实际的场景及需求（<strong>上小节最后一张图，我们可以看到，push 到下级页面，底部 tabbar 仍旧显示，虽然少数 app 会这么做，但大多数 app 都会隐藏</strong>），结合着 UITabBarController 和 UINavigationController 来讲述我在实际工作中是如何来配置的。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            