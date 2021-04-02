
---
title: 'iOS Swift5从0到1系列（四）：学习UINavigationController（2）：底部TabBar的显示与隐藏'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b55c7753ac45d6ae7fd278ee935288~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 09 Mar 2021 20:31:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b55c7753ac45d6ae7fd278ee935288~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<h2 data-id="heading-0">UINavigationController 小系列 <a href="https://github.com/qingye/ios-swift5-demo" target="_blank" rel="nofollow noopener noreferrer">【源码 Github 传送门】</a>：</h2>
<p><a href="https://juejin.cn/post/6937492008160198663" target="_blank">学习UINavigationController（1）：基础</a></p>
<p><a href="https://juejin.cn/post/6937878071370334215/" target="_blank">学习UINavigationController（2）：底部TabBar的显示与隐藏</a></p>
<p><a href="https://juejin.cn/post/6938056448056229896/" target="_blank">学习UINavigationController（3）：NavigationBar 显示与隐藏</a></p>
<p><a href="https://juejin.cn/post/6938429340275179557/" target="_blank">学习UINavigationController（4）：自定义导航栏+完美过渡+统一返回按钮</a></p>
</blockquote>
<h2 data-id="heading-1">一、前言</h2>
<p>上篇我们分享了 UINavigationController 基础知识，以及导航栏左侧按钮的显示规则，文章的最后，留了个小问题给让大家思考，如何从一级页面 push 到二级页面时，隐藏 tabbar；当然，pop 时，再显示 tabbar。</p>
<p>我们在源码分析中，有讲到过一个 Bool 变量，不知道大家有没有特别注意过，或者自己去尝试过，如下图：</p>
<p><img alt="hidesBottomBarWhenPushed.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b55c7753ac45d6ae7fd278ee935288~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图我特别标注了该变量，该变量是在 UIViewController 中的，<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mtext>（问题</mtext><mn>1</mn><mtext>）</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;（问题 1）&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">（</span><span class="mord cjk_fallback" style="color:red;">问</span><span class="mord cjk_fallback" style="color:red;">题</span><span class="mord" style="color:red;">1</span><span class="mord cjk_fallback" style="color:red;">）</span></span></span></span></span></span><strong>那如何使用呢？</strong></p>
<p>本系列仿京东，我们看到大多数电商APP，一级页面的导航栏都是自定义的，也有可能是隐藏；push 到二级页面会使用系列默认的（颜色、左右按钮个数可自定义），但肯定是显示的；<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mtext>（问题</mtext><mn>2</mn><mtext>）</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;（问题 2）&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">（</span><span class="mord cjk_fallback" style="color:red;">问</span><span class="mord cjk_fallback" style="color:red;">题</span><span class="mord" style="color:red;">2</span><span class="mord cjk_fallback" style="color:red;">）</span></span></span></span></span></span><strong>如何控制导航栏的显示与隐藏，以及如何自定义导航栏？</strong></p>
<p>同时，我们还应该想到，不同的APP有不同的风格，而这风格可能是导航栏颜色不同，比如主流电商APP，导航栏可能都是红色的，有些页面则是白色；其它的APP可能因为不同的模块功能而展示不同颜色，或者图片；然而，这里会涉及到，用户侧滑返回是，导航栏的过渡过于生硬，如下图：</p>
<p><img alt="navigation-bar-bg-color.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dddad21c5a040f892b5426ba759bfe6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mtext>（问题</mtext><mn>3</mn><mtext>）</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;（问题 3）&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">（</span><span class="mord cjk_fallback" style="color:red;">问</span><span class="mord cjk_fallback" style="color:red;">题</span><span class="mord" style="color:red;">3</span><span class="mord cjk_fallback" style="color:red;">）</span></span></span></span></span></span><strong>如何优化页面切换时，导航栏的过渡显的相对自然？</strong></p>
<p>好了，先总结一下，我们遇到的问题：</p>
<ol>
<li>当 UITabBarController 作为 rootViewController 时，嵌套 UINavigationController，在页面切换时，如何做到 TabBar 显示与隐藏自如？</li>
<li>有些页面需要隐藏导航栏，有些又面要显示，在页面切换时，如何控制 NavigationBar 显示与隐藏自如？</li>
<li>如何自定义不同风格的导航栏？</li>
<li>如何做到页面切换时，导航栏的过渡自然而不生硬？</li>
</ol>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>以上这些问题，我们将分篇章来依次学习如何处理，因为涉及的内容会越来越多，一篇写完，时间太久，也太累。</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;以上这些问题，我们将分篇章来依次学习如何处理，因为涉及的内容会越来越多，一篇写完，时间太久，也太累。&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">以</span><span class="mord cjk_fallback" style="color:red;">上</span><span class="mord cjk_fallback" style="color:red;">这</span><span class="mord cjk_fallback" style="color:red;">些</span><span class="mord cjk_fallback" style="color:red;">问</span><span class="mord cjk_fallback" style="color:red;">题</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">我</span><span class="mord cjk_fallback" style="color:red;">们</span><span class="mord cjk_fallback" style="color:red;">将</span><span class="mord cjk_fallback" style="color:red;">分</span><span class="mord cjk_fallback" style="color:red;">篇</span><span class="mord cjk_fallback" style="color:red;">章</span><span class="mord cjk_fallback" style="color:red;">来</span><span class="mord cjk_fallback" style="color:red;">依</span><span class="mord cjk_fallback" style="color:red;">次</span><span class="mord cjk_fallback" style="color:red;">学</span><span class="mord cjk_fallback" style="color:red;">习</span><span class="mord cjk_fallback" style="color:red;">如</span><span class="mord cjk_fallback" style="color:red;">何</span><span class="mord cjk_fallback" style="color:red;">处</span><span class="mord cjk_fallback" style="color:red;">理</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">因</span><span class="mord cjk_fallback" style="color:red;">为</span><span class="mord cjk_fallback" style="color:red;">涉</span><span class="mord cjk_fallback" style="color:red;">及</span><span class="mord cjk_fallback" style="color:red;">的</span><span class="mord cjk_fallback" style="color:red;">内</span><span class="mord cjk_fallback" style="color:red;">容</span><span class="mord cjk_fallback" style="color:red;">会</span><span class="mord cjk_fallback" style="color:red;">越</span><span class="mord cjk_fallback" style="color:red;">来</span><span class="mord cjk_fallback" style="color:red;">越</span><span class="mord cjk_fallback" style="color:red;">多</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">一</span><span class="mord cjk_fallback" style="color:red;">篇</span><span class="mord cjk_fallback" style="color:red;">写</span><span class="mord cjk_fallback" style="color:red;">完</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">时</span><span class="mord cjk_fallback" style="color:red;">间</span><span class="mord cjk_fallback" style="color:red;">太</span><span class="mord cjk_fallback" style="color:red;">久</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">也</span><span class="mord cjk_fallback" style="color:red;">太</span><span class="mord cjk_fallback" style="color:red;">累</span><span class="mord cjk_fallback" style="color:red;">。</span></span></span></span></span></span></p>
<h2 data-id="heading-2">二、掌控 TabBar 的显示与隐藏</h2>
<p>既然我们已经说了，在 UIViewController 中有 hidesBottomBarWhenPushed = true 才能在 push 到下一个页面时隐藏，那我们就先尝试这个属性，先尝试在 HomeViewController 中尝试一下，代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomeViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        title <span class="hljs-operator">=</span> <span class="hljs-string">"首页"</span>
        
        <span class="hljs-comment">// 若被 UITabBarController 嵌套，则设置该属性进入下一个页面时，隐藏底部 TabBar</span>
        hidesBottomBarWhenPushed <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
        <span class="hljs-operator">......</span>
    &#125;
    <span class="hljs-operator">......</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整体截图如下：</p>
<p><img alt="home-vc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1c1e9e3b60478e89002bb167cf023c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后运行一下：</p>
<p><img alt="hidesBottomBarWhenPushed.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e42d01fcfbc84518b58f61c0382fb497~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后我们看到，push 到二级页面，确实隐藏了 TabBar，但是 pop 时， TabBar 却没有再显示...如果，这时也许有的人会说，我把这个属性放到二级页面中呢？我们可以试试：</p>
<ul>
<li>先去掉 HomeViewController 中添加的 hidesBottomBarWhenPushed 代码；</li>
<li>修改二级页面，如下：</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        view.backgroundColor <span class="hljs-operator">=</span> .red
        
        title <span class="hljs-operator">=</span> <span class="hljs-string">"二级页面"</span>
        
        <span class="hljs-comment">// 若被 UITabBarController 嵌套，则设置该属性进入下一个页面时，隐藏底部 TabBar</span>
        hidesBottomBarWhenPushed <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再运行，你会发现，这回没有任何的变化....为什么呢？那是因为，我们放置代码的位置不对，我们要放在 init构造器中才行！代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">nibName</span> <span class="hljs-params">nibNameOrNil</span>: <span class="hljs-type">String</span>?, <span class="hljs-params">bundle</span> <span class="hljs-params">nibBundleOrNil</span>: <span class="hljs-type">Bundle</span>?)</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        
        <span class="hljs-comment">// 若被 UITabBarController 嵌套，则设置该属性进入下一个页面时，隐藏底部 TabBar</span>
        hidesBottomBarWhenPushed <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
    &#125;
    
    <span class="hljs-keyword">required</span> <span class="hljs-function"><span class="hljs-keyword">init?</span>(<span class="hljs-params">coder</span>: <span class="hljs-type">NSCoder</span>)</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>(coder: coder)
    &#125;
    
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        view.backgroundColor <span class="hljs-operator">=</span> .red
        
        title <span class="hljs-operator">=</span> <span class="hljs-string">"二级页面"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后运行一下：</p>
<p><img alt="run-right.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f4036ad2664226a0e509197a312851~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OK!  TabBar 在页面切换时，我们确实解决了这个小问题，但是随之又带来了新问题：</p>
<ol>
<li>我们 rootViewController 是 UITabBarController，有 5 个 UINavigationController + VC，难道每个对应的下一级页面都要这么做？</li>
<li>实际项目中，我们所有的 UIViewController 肯定都有一个共同的基类：BaseViewController，一般不会有多个这样的基类，但如果在 BaseViewController 的 init 构造器中处理，其结果就会导致和开始的情况一样，push 隐藏，pop 仍旧不会显示，那该如何统一呢？</li>
</ol>
<h2 data-id="heading-3">三、统一处理</h2>
<h3 data-id="heading-4">3.1、统一基类 BaseViewController</h3>
<p>首先，我们要统一基类，现在可能没用，但常识上大家都知道，肯定会封装一些内容，这些封装的内容也会在后续文章中不断的去丰富！</p>
<ol>
<li>新建『New Group』，命名为：BaseControllers；</li>
<li>新建『New File...』，选择『Cocoa Touch Class』，如下，然后点完成即可；</li>
</ol>
<p><img alt="base-vc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaf18361f48444e1829e0c66d14641f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该基类我们暂时什么都不干，然后，将我们之前创建的所有 ViewController 的继承换成该 BaseViewController，例如：</p>
<p><img alt="re-inherit.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5abbc0af7e2041b3bc5777ca0f28b2f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.2、创建继承 UINavigationController 的子类 CustomNavigationController</h3>
<p><img alt="CustomNavigationController.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d08c2cc1166d400994dfb7fa93f2dbc7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们先来捋一捋思路：</p>
<ol>
<li>在一级页面中，添加 hidesBottomBarWhenPushed，虽然 push OK，但 pop 不OK；</li>
<li>在二级页面中，只有在 init构造器中添加 hidesBottomBarWhenPushed ，push & pop 才都OK；</li>
</ol>
</blockquote>
<p>从这两条中，我们可以看出，hidesBottomBarWhenPushed 属性需要添加在非嵌套在 UITabBarController 的 ViewController 上，且在初始化时添加才能正常，而我们 push 时，实际上是通过 UINavigationController 的 pushViewController 方法来进行跳转的，因此，我们最好的解决方案就是：</p>
<ol>
<li>继承 UINavigationController；</li>
<li>重写 pushViewController 方法；</li>
<li>根据 UINavigationController 中的 viewControllers 该对象来判断是否需要添加 hidesBottomBarWhenPushed 属性；</li>
</ol>
<p>具体做法如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomNavigationController</span>: <span class="hljs-title">UINavigationController</span> </span>&#123;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
    &#125;
    
    <span class="hljs-comment">// 重写 pushViewController 方法，不修改 pushViewController 的逻辑</span>
    <span class="hljs-comment">// 仅在跳转前，判断目标 VC 是否为一级页面还是二级页面，通过 viewControllers.count 来判断：</span>
    <span class="hljs-comment">// viewControllers.count > 0，那么目标 VC 肯定是第二个页面（即二级页面）；我们就添加上 hidesBottomBarWhenPushed = true</span>
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">pushViewController</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">viewController</span>: <span class="hljs-type">UIViewController</span>, <span class="hljs-params">animated</span>: <span class="hljs-type">Bool</span>)</span> &#123;
        <span class="hljs-keyword">if</span> viewControllers.count <span class="hljs-operator">></span> <span class="hljs-number">0</span> &#123;
            viewController.hidesBottomBarWhenPushed <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
        &#125;
        <span class="hljs-keyword">super</span>.pushViewController(viewController, animated: animated)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图：</p>
<p><img alt="cnc-realize.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ef5c14421be4b23987b9ef00fae1b1a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后，修改 MainTabBarController，代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainTabBarController</span>: <span class="hljs-title">UITabBarController</span> </span>&#123;
    <span class="hljs-operator">......</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">initTabBar</span>()</span> &#123;
        <span class="hljs-keyword">let</span> home <span class="hljs-operator">=</span> <span class="hljs-type">CustomNavigationController</span>(rootViewController: <span class="hljs-type">HomeViewController</span>())
        home.tabBarItem.title <span class="hljs-operator">=</span> <span class="hljs-string">"首页"</span>
        <span class="hljs-operator">......</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图（5 个 VC 即一级页面，都替换掉）：</p>
<p><img alt="modify-main-tabbar-ctrl.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c1f9b353dc044beadd30fedd08639c6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>恢复二级页面的代码：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">BaseViewController</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        view.backgroundColor <span class="hljs-operator">=</span> .red
        
        title <span class="hljs-operator">=</span> <span class="hljs-string">"二级页面"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终，我们再次运行效果如下：</p>
<p><img alt="perfect-hides-and-show.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b064ee2fb014fa6809f9ac8f8f599d9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>完美！至此，本篇内容：正确的控制底部 TabBar 的显示与隐藏就到这里，欢迎交流！谢谢。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            