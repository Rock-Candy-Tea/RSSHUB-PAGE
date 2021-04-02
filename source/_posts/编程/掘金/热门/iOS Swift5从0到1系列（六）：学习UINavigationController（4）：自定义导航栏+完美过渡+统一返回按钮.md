
---
title: 'iOS Swift5从0到1系列（六）：学习UINavigationController（4）：自定义导航栏+完美过渡+统一返回按钮'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f175fe326244d82822d43a965f53c69~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 11 Mar 2021 08:13:22 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f175fe326244d82822d43a965f53c69~tplv-k3u1fbpfcp-watermark.image'
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
<p>上篇，我们虽然给出了统一处理 navigationBar 的显示与隐藏，但用户体验非常差，在上篇最后，我说到了自定义导航栏，我们能够实现如下功能：</p>
<ul>
<li>ViewController 控制各自的导航栏；</li>
<li>push & pop 相互不会影响；</li>
<li>基于以上两点，即便颜色、背景不一样，都能较为完美的过渡；</li>
</ul>
<p>废话不多说，直接开干！</p>
<h2 data-id="heading-2">二、自定义导航栏</h2>
<h3 data-id="heading-3">2.1、透明化导航栏</h3>
<p>在添加自定义导航栏前，我们需要做一件事，就是修改一个导航栏，怎么修改呢？有两种办法：</p>
<ul>
<li>通过 isHidden 来隐藏导航栏；</li>
<li>直接将半透明的背景变为全透明；</li>
</ul>
<p>我们考虑到隐藏导航栏可能会存在不确定的系统因素影响，因此，我们建议还是保留系统导航栏，只不过将其完全透明化，以及还可以利用系统的渐变过渡动画，提升用户体验；而完全透明化的方式很简单，通过设置 navigationBar.setBackgroundImage:for: 的方式来设置一张透明的 UIImage 即可；UIImage() 直接构造就是透明的，因为此时 cgImage 默认为 nil 。</p>
<p>同时，导航栏下还有一条阴影线条，该线条也是一个 UIImage，因此，同样将其透明化；其它代码不变，我们统一在基类 BaseViewController 中修改即可，如下图（左）：</p>
<p><img alt="transparent-nav-bar.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f175fe326244d82822d43a965f53c69~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后运行，可以看到上图中，我们的导航栏已经透明，只剩下一个标题。</p>
<p>在上一篇我就提到过，修改 navigationBar 将会影响当前 navigationController 栈中所有的 ViewController，因此，所有页面的导航栏都将透明，接下来，我们将提供一个方法，来添加一个新的导航栏背景（提前透露：该新加的导航栏背景，实际是覆盖在原来的导航栏之上而已）。</p>
<h3 data-id="heading-4">2.2、添加导航栏背景（覆盖原始导航栏）</h3>
<p>我们先来看一下修改后的运行图，直观感受一下：</p>
<p><img alt="self-def-navigation-bar.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7251475944e94c63a336f1bb4f7ded2a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>整体效果应该说，对比上一篇，那种糟糕的用户体验，这次几乎完全达到了我们想要的结果，同样，还是统一处理，在基类 BaseViewController 中修改即可，代码如下：</p>
<pre><code class="copyable">class BaseViewController: UIViewController &#123;

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        
        // 设置导航栏背景为透明色图片
        navigationController?.navigationBar.setBackgroundImage(UIImage(), for: .default)
        // 设置导航栏阴影为透明色图片
        navigationController?.navigationBar.shadowImage = UIImage()
    &#125;
    
    // 添加自定义导航栏背景
    func addNavBar(_ color: UIColor) &#123;
        // 目前有点小瑕疵，高度是写死的，并没有考虑到 SafeArea
        // 我会在之后的一篇中分析 SafeArea 时，给出如何正确的适配不同机型
        let size = CGSize(width: view.bounds.width, height: 91)
        let navImageView = UIImageView(image: UIImage(size: size, color: color))
        view.addSubview(navImageView)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在需要使用的地方，调用一下该方法即可，例如，在二级页面中调用：</p>
<pre><code class="copyable">class ViewController: BaseViewController &#123;
    override func viewDidLoad() &#123;
        super.viewDidLoad()
        view.backgroundColor = .red
        title = "二级页面"
        addNavBar(.cyan)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想完全让首页的导航栏不可见，我们只需把 title 去掉，就真的完全透明不可见了。</p>
<h2 data-id="heading-5">三、统一返回按钮</h2>
<p>我们已经完成了大部分的统一工作，我想，如果我不把统一返回按钮的方案给出来，就感觉整体方案少了点什么，在 UINavigationController 最后，我再给出导航栏上左侧按钮的统一封装，基本上就完成了 UINavigationController 这个小系列，实现也很简单，估计大家都想到了，在 BaseViewController 中统一修改就行，但你还记得我之前说的那个 backBarButtomItem 和 leftBarButtomItem 的规则吗？</p>
<p>代码实现如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
        
        <span class="hljs-comment">/// 如果所有的 ChildViewController 都继承于 BaseViewController，且想在 viewDidLoad 中统一设置导航栏的『左按钮』，</span>
        <span class="hljs-comment">/// 那么，只能设置 backBarButtonItem ，而不能设置 leftBarButtonItem，原因如下：</span>
        <span class="hljs-comment">///</span>
        <span class="hljs-comment">/// previousVC 是上一个页面，nextVC 是下一个页面，当发生 push 时，有如下规则：</span>
        <span class="hljs-comment">/// 1、如果 nextVC 的 leftBarButtonItem != nil，那么将在 navigationBar 的左边显示 nextVC 指定的 leftBarButtonItem；</span>
        <span class="hljs-comment">/// 2、如果 nextVC 的 leftBarButtonItem == nil，previousVC 的 backBarButtonItem != nil，那么将在 navigationBar 的左边显示 previousVC 指定的 backBarButtonItem；</span>
        <span class="hljs-comment">/// 3、如果两者都为 nil 则：</span>
        <span class="hljs-comment">///   3.1、nextVC 的 navigationItem.hidesBackButton = YES，那么 navigationBar 将隐藏左侧按钮；</span>
        <span class="hljs-comment">///   3.2、否则 navigationBar的左边将显示系统提供的默认返回按钮；</span>
        <span class="hljs-comment">///</span>
        <span class="hljs-comment">/// 我们从以上规则中发现：</span>
        <span class="hljs-comment">/// 1、leftBarButtonItem 的优先级比 backBarButtonItem 要高；</span>
        <span class="hljs-comment">/// 2、backBarButtonItem 是来自上一个页面，如果当前 VC 是第一个页面，那么它没有上一个页面，也就没有 backBarButtonItem；</span>
        <span class="hljs-comment">/// 3、leftBarButtonItem 是来自当前页面，与上个页面无关，因此，如果当前 VC 是第一个页面，那么设置了 leftBarButtonItem 就会很奇怪；</span>
        <span class="hljs-comment">///</span>
        navigationItem.backBarButtonItem <span class="hljs-operator">=</span> <span class="hljs-type">UIBarButtonItem</span>.<span class="hljs-keyword">init</span>(title: <span class="hljs-string">"返回"</span>, image: <span class="hljs-literal">nil</span>, primaryAction: <span class="hljs-literal">nil</span>, menu: <span class="hljs-literal">nil</span>)
        navigationItem.backBarButtonItem<span class="hljs-operator">?</span>.tintColor <span class="hljs-operator">=</span> .black
        
        <span class="hljs-operator">......</span>
    &#125;
    <span class="hljs-operator">......</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后如下图：</p>
<p><img alt="back-with-text.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74d0fe147e648778069282bc0fc90bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果想只留箭头，去掉文字呢？嗯，设置一下 image，优先级比文字高：</p>
<p><img alt="back-without-text.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/175ab5c2c2b34040a16737bf68114a75~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OK！至此，本小小系列 UINavigationController 总算圆满完结~ 另外，Swift 上所有的实现，OC 完全可以实现，所有的思路和实现和 Swift 一样，只是 api 名字有一点点不同（OC 有前缀，Swift 没有）。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            