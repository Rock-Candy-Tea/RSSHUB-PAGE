
---
title: 'iOS Swift5从0到1系列（八）：双UIWindow + 启动页 vs 广告页'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6789594f4d04ec5b078c7b6d828bac5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 15 Mar 2021 08:51:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6789594f4d04ec5b078c7b6d828bac5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>我们知道，苹果在2019年WWDC要求，2020.4月开始上架的 APP 都强制要求使用 LaunchScreen.storyboard，删除该 storyboard ，改为各种自定义的广告启动页时代已经过去了，那么，对于各大电商来说，每年有各种大、中、小促（越来越频繁，是个节日就促销），因此，活动广告页仍旧必不可少。启动页不能删除，同时还需要广告页，那我们该如何去做呢？</p>
<p>本篇，你将学到如下知识点：</p>
<ol>
<li>简单了解 LaunchScreen；</li>
<li>制作启动页 + XIB 中设置约束；</li>
<li>双 UIWindow / 单 UIWindow 切换；</li>
</ol>
<h2 data-id="heading-1">二、简单了解 LaunchScreen</h2>
<p>LaunchScreen 很简单，网上有大把的适配方案。你不能动态去设置该 storyboard ，只能提前在 Xcode 中设置。因为要考虑到不同机型分辨率的适配问题，因此，不建议使用一整张图 + 约束，除非你添加一整套不同分辨率的图到工程中，但这样的话，你的整个 app 包就大了。</p>
<p>个人建议：</p>
<ul>
<li>背景为纯色填充；</li>
<li>放置小图 + 约束；</li>
<li>放置文字 + 约束；</li>
</ul>
<p>出于 Demo 好看，我设置了一整张图片 + 两行文字：</p>
<p><img alt="LaunchScreen.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6789594f4d04ec5b078c7b6d828bac5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>图片采用『Aspect Fill』按比例来充满整屏（会被截取），所以为何我会建议用纯背景色了吧，当然，不怕被截的话，那就可以用图片没有问题；</li>
<li>不同颜色的文字设置，如下图：</li>
</ul>
<p><img alt="multi-color-text.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad78758a45c044448d5d19bc81e4dc34~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如何在 XIB 中添加约束？</p>
</blockquote>
<p><img alt="xib-set-constraints.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f6a0a95bc64814a68dd36eb8b25b25~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>拖线的时候，要先按住『 control 』键才行！</p>
<h2 data-id="heading-2">三、UIWindow 与 广告页</h2>
<p>在 AppDelegate 中，我们已经有了一个 window，它的 rootViewController 已经设置为我们的 MainTabBarController，那我们如何先启动我们的广告页，然后再进入我们真正的 TabBarController 呢？</p>
<p>通常，我们有两种办法：</p>
<ol>
<li>单 window，rootViewController 先设置广告页VC，之后再换成 TabBarController；</li>
<li>双 window，rootViewController 分别设置广告页VC 和 TabBarController，只不过，广告页 window 在最上面，然后再切换到 TabBarController 的 window；</li>
</ol>
<p>无论哪种方式，最终的效果都一样，如下图：</p>
<p><img alt="switch-from-adv-to-main.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88a49fa0f644b9d8b89dcea15021514~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3.1、添加广告页 VC</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// AdvertiseViewController.swift</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AdvertiseViewController</span>: <span class="hljs-title">BaseViewController</span> </span>&#123;
    
    <span class="hljs-comment">// 延迟初始化 timer</span>
    <span class="hljs-keyword">lazy</span> <span class="hljs-keyword">var</span> timer <span class="hljs-operator">=</span> <span class="hljs-type">DispatchSource</span>.makeTimerSource(flags: [], queue: <span class="hljs-type">DispatchQueue</span>.global())
    <span class="hljs-comment">// 倒计时的时间</span>
    <span class="hljs-keyword">var</span> seconds <span class="hljs-operator">=</span> <span class="hljs-number">5</span>

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        view.backgroundColor <span class="hljs-operator">=</span> .kRed
        timeCountDown()
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">timeCountDown</span>()</span> &#123;
        timer.schedule(deadline: .now(), repeating: .seconds(<span class="hljs-number">1</span>))
        timer.setEventHandler(handler: &#123;
            <span class="hljs-type">DispatchQueue</span>.main.async &#123; [<span class="hljs-keyword">weak</span> <span class="hljs-keyword">self</span>] <span class="hljs-keyword">in</span>
                
                <span class="hljs-comment">// 小于等于 0 时，结束 timer，并进行两个 rootViewController 的切换</span>
                <span class="hljs-keyword">if</span> <span class="hljs-keyword">self</span><span class="hljs-operator">!</span>.seconds <span class="hljs-operator"><=</span> <span class="hljs-number">0</span> &#123;
                    <span class="hljs-keyword">self</span><span class="hljs-operator">!</span>.terminer()
                &#125;
                <span class="hljs-keyword">self</span><span class="hljs-operator">!</span>.seconds <span class="hljs-operator">-=</span> <span class="hljs-number">1</span>
            &#125;
        &#125;)
        timer.resume()
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">terminer</span>()</span> &#123;
        timer.cancel()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="dir-structure.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c0a201f4a864f03a8ebfb7834d7f24c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3.2、单 window 替换法</h3>
<p>单 window 替换法如我之前所说，用户点击或者倒计时结束时，将 window.rootViewController = MainTabBarController() 即可，当然，还要加点过渡动画，不然就会显示太过生硬，实现代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// AdvertiseViewController.swift</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AdvertiseViewController</span>: <span class="hljs-title">BaseViewController</span> </span>&#123;
    <span class="hljs-operator">......</span>
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">terminer</span>()</span> &#123;
        timer.cancel()
        switchRootController()
    &#125;
    
    <span class="hljs-comment">//</span>
    <span class="hljs-comment">// 一个 window 的情况：只用切换 rootViewController 就行</span>
    <span class="hljs-comment">//</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">switchRootController</span>()</span> &#123;
        <span class="hljs-keyword">let</span> window <span class="hljs-operator">=</span> <span class="hljs-type">UIApplication</span>.shared.windows.first<span class="hljs-operator">!</span>
        
        <span class="hljs-comment">// 过渡动画：0.5s 淡出</span>
        <span class="hljs-type">UIView</span>.transition(with: window,
                          duration: <span class="hljs-number">0.5</span>,
                          options: .transitionCrossDissolve,
                          animations: &#123;
                            
                            <span class="hljs-keyword">let</span> old <span class="hljs-operator">=</span> <span class="hljs-type">UIView</span>.areAnimationsEnabled
                            <span class="hljs-type">UIView</span>.setAnimationsEnabled(<span class="hljs-literal">false</span>)
                            window.rootViewController <span class="hljs-operator">=</span> <span class="hljs-type">MainTabBarController</span>()
                            <span class="hljs-type">UIView</span>.setAnimationsEnabled(old)

                          &#125;, completion: &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
                            <span class="hljs-comment">// Do Nothing</span>
                          &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 AppDelegation</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@main</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppDelegate</span>: <span class="hljs-title">UIResponder</span>, <span class="hljs-title">UIApplicationDelegate</span> </span>&#123;

    <span class="hljs-keyword">var</span> window: <span class="hljs-type">UIWindow</span>?

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">application</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">application</span>: <span class="hljs-type">UIApplication</span>, <span class="hljs-params">didFinishLaunchingWithOptions</span> <span class="hljs-params">launchOptions</span>: [<span class="hljs-type">UIApplication</span>.<span class="hljs-params">LaunchOptionsKey</span>: <span class="hljs-keyword">Any</span>]<span class="hljs-operator">?</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-comment">// Override point for customization after application launch.</span>
        
        window <span class="hljs-operator">=</span> <span class="hljs-type">UIWindow</span>(frame: <span class="hljs-type">UIScreen</span>.main.bounds)
        window<span class="hljs-operator">?</span>.backgroundColor <span class="hljs-operator">=</span> .white
        window<span class="hljs-operator">?</span>.rootViewController <span class="hljs-operator">=</span> <span class="hljs-type">AdvertiseViewController</span>() <span class="hljs-comment">// 修改这里</span>
        window<span class="hljs-operator">?</span>.makeKeyAndVisible()
        
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.3、双 window 切换法</h3>
<p>双 window 顾名思义，就是有两个 window，双 window 不像单 window，是修改 rootViewController，而是通过 api 来控制哪个 window 可见的方式来切换，同样也需要有过渡动画。（先还原代码至 3.1 小节，再开始本小节的demo ）</p>
<p>修改 AppDelegation</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@main</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppDelegate</span>: <span class="hljs-title">UIResponder</span>, <span class="hljs-title">UIApplicationDelegate</span> </span>&#123;

    <span class="hljs-comment">// 多个 window：</span>
    <span class="hljs-comment">// 第 1 个用于主app；</span>
    <span class="hljs-comment">// 第 2 个用于显示广告页；</span>
    <span class="hljs-keyword">var</span> windows: [<span class="hljs-type">UIWindow</span>]<span class="hljs-operator">?</span>

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">application</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">application</span>: <span class="hljs-type">UIApplication</span>, <span class="hljs-params">didFinishLaunchingWithOptions</span> <span class="hljs-params">launchOptions</span>: [<span class="hljs-type">UIApplication</span>.<span class="hljs-params">LaunchOptionsKey</span>: <span class="hljs-keyword">Any</span>]<span class="hljs-operator">?</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-comment">// Override point for customization after application launch.</span>
        
        <span class="hljs-comment">// 后一个 window 盖在前一个之上，可以通过：</span>
        <span class="hljs-comment">// windows?[下标].makeKeyAndVisible() 来切换显示</span>
        windows <span class="hljs-operator">=</span> [
            addWindowWithVC(<span class="hljs-type">MainTabBarController</span>()),
            addWindowWithVC(<span class="hljs-type">AdvertiseViewController</span>())
        ]
        
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addWindowWithVC</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">vc</span>: <span class="hljs-type">UIViewController</span>)</span> -> <span class="hljs-type">UIWindow</span> &#123;
        <span class="hljs-keyword">let</span> window <span class="hljs-operator">=</span> <span class="hljs-type">UIWindow</span>.<span class="hljs-keyword">init</span>(frame: <span class="hljs-type">UIScreen</span>.main.bounds)
        window.backgroundColor <span class="hljs-operator">=</span> .white
        window.rootViewController <span class="hljs-operator">=</span> vc
        window.makeKeyAndVisible()
        <span class="hljs-keyword">return</span> window
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 AdvertiseViewController</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AdvertiseViewController</span>: <span class="hljs-title">BaseViewController</span> </span>&#123;
    <span class="hljs-operator">......</span>
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">terminer</span>()</span> &#123;
        timer.cancel()
        switchWindow() <span class="hljs-comment">// 修改这里</span>
    &#125;
    
    <span class="hljs-comment">// 同样两种方式可以实现：广告页 -> 主页面：</span>
    <span class="hljs-comment">// 1. 两个 window 来分别控制不同的业务，然后基于过渡动画来切换 window；</span>
    <span class="hljs-comment">// 2. 一个 window，两个 vc，分别是 主vc 和 广告vc，通过修改 window.rootViewController 来完成；</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">switchWindow</span>()</span> &#123;
        <span class="hljs-comment">// 第2个 window（广告窗口）</span>
        <span class="hljs-keyword">let</span> window <span class="hljs-operator">=</span> <span class="hljs-type">UIApplication</span>.shared.windows.last<span class="hljs-operator">!</span>
        
        <span class="hljs-comment">// 过渡动画：淡出</span>
        <span class="hljs-type">UIView</span>.transition(with: window,
                          duration: <span class="hljs-number">0.5</span>,
                          options: .transitionCrossDissolve,
                          animations: &#123;

                            <span class="hljs-comment">// 临时保存 UIView 是否开启动画的状态（默认是开启）</span>
                            <span class="hljs-comment">// 之所以先禁止，是防止存在其它动画影响了当前动画</span>
                            <span class="hljs-comment">// ----------------------------------------</span>
                            <span class="hljs-comment">// 设置了禁止动画后：</span>
                            <span class="hljs-comment">// 1. 当前所有正在执行动画的没有任何影响</span>
                            <span class="hljs-comment">// 2. 未执行的将不会执行动画</span>
                            <span class="hljs-comment">// ----------------------------------------</span>
                            <span class="hljs-comment">//</span>
                            <span class="hljs-comment">// 因为我们这个回调是动画已经开始，所以，并不会被强制停止,</span>
                            <span class="hljs-comment">// 最后再恢复 UIView 是否开启动画的状态即可</span>
                            <span class="hljs-keyword">let</span> old <span class="hljs-operator">=</span> <span class="hljs-type">UIView</span>.areAnimationsEnabled
                            <span class="hljs-type">UIView</span>.setAnimationsEnabled(<span class="hljs-literal">false</span>)
                            window.alpha <span class="hljs-operator">=</span> <span class="hljs-number">0</span>
                            <span class="hljs-type">UIView</span>.setAnimationsEnabled(old)

                          &#125;, completion: &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
                            <span class="hljs-comment">// 切换到主 window，即我们的 MainTabBarController</span>
                            <span class="hljs-type">UIApplication</span>.shared.windows.first<span class="hljs-operator">?</span>.makeKeyAndVisible()
                          &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无论哪种用法，对于用户来说，都是一样；同样，最终取决于用单 window 还是双 window 都由项目（可扩展性）、研发（技术、时间、能力）等来决定；但总归，多一种方案多一条路。</p>
<h2 data-id="heading-6">四、总结</h2>
<p>本篇虽然是在介绍如何启动广告页，实际则是让大家学习如何去使用多个 window，以及之间的切换过渡动画（正所谓授之以鱼，不如授之以渔）。多个 window 看似场景不多，其实还是有的，比如：视频类APP，非全屏时，页面滚动，视频控件移出到屏幕外不可见时，APP会在当前创建一个悬浮在右下角的一个单独视频窗口，这就用到了多window 技术。</p>
<p>既然是广告页，一定会有倒计时的控件不断时间递减，倒计时结束后才会进入我们的首页。下一篇，我将介绍本系列的第一个组件：倒计时组件！（本系列会介绍非常多的常用组件的自定义开发）</p>
<p>欢迎交流，敬请期待，谢谢！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            