
---
title: 'iOS Swift5从0到1系列（二）：学习UITabBarController'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426ab56e923944bcb679df187f808b34~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 07 Mar 2021 17:06:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426ab56e923944bcb679df187f808b34~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>没想到本系列第一篇开局就能收获这么多朋友的喜爱与鼓励，让我更有动力继续本系列。</p>
<p>之所有出的这么慢，也是因为，我希望尽量把每个知识点讲到位，哪怕你是零基础，致力想成员一名 iOSer 的朋友，也能够再学习本系列的时候，掌握知识细节，所以，每遇到我认为是一个需要展开分析的点的内容，我都会反复再三确认，并认真思考如何用最好的方式来呈现给大家。</p>
<p>既然要做本系列，我们肯定要选择一个模仿的『对象』，而这个『对象』，如果大家之前有看过我分享的<a href="https://juejin.cn/post/6934523636485193735" target="_blank">《抓包工具 Charles》</a>，大家一定可以猜的出来，我们本系列将要模仿的『对象』是：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mtext>京东</mtext><mi>A</mi><mi>P</mi><mi>P</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;京东APP&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">京</span><span class="mord cjk_fallback" style="color:red;">东</span><span class="mord mathnormal" style="color:red;">A</span><span class="mord mathnormal" style="margin-right:0.13889em;color:red;">P</span><span class="mord mathnormal" style="margin-right:0.13889em;color:red;">P</span></span></span></span></span></span></p>
<p>今天先仿京东APP的底部导航栏，如下图：</p>
<p><img alt="jdapp-tabbar.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426ab56e923944bcb679df187f808b34~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、底部导航栏控制器（UITabBarController）</h2>
<p>我们打开京东APP，进入到它的主页，就能看到最底部有一排五个按钮，每个按钮都对应着一个页面（我们称之为 ViewController），因此，最底部我们称之为『底部导航栏』。</p>
<blockquote>
<p>源码注释：
If more than five view controllers are added to a tab bar controller, only the first four will display.
如果创建的个数大于5个，将会直接显示前4个。
The rest will be accessible under an automatically generated More item.
剩下的将会都收敛到一个叫作『更多』的按钮中。</p>
</blockquote>
<p>这也就是为何几乎绝大多数 APP 都只定义不超过 5 个按钮及对应的 ViewController 的原因；源码注释中，并没有说最少定义几个，不过，一般来说至少定义 2 个以上（如果定义为一个，虽然可以，但那使用 UITabBarController 就没有任何意义）。</p>
<p>在正式开始学习使用前，我们先分析下 UIKit.UITabBarController 中的源码。</p>
<h3 data-id="heading-2">2.1、UITabBarController 分析</h3>
<pre><code class="copyable">@available(iOS 2.0, *)
open class UITabBarController : UIViewController, UITabBarDelegate, NSCoding &#123;
    open var viewControllers: [UIViewController]?
    ......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到：</p>
<ul>
<li>UITabBarController 继承于 UIViewController；</li>
<li>实现了 UITabBarDelegate 即 UITabBar（底部按钮的委托）；</li>
<li>以及 NSCoding（归档与反归档数据存取协议）；</li>
<li>定义了 UIViewController 对象可 nil 数组；</li>
</ul>
<h3 data-id="heading-3">2.2、扩展 UIViewController 分析</h3>
<pre><code class="copyable">extension UIViewController &#123;
    // Automatically created lazily with the view controller's title if it's not set explicitly.
    open var tabBarItem: UITabBarItem!
    
    // If the view controller has a tab bar controller as its ancestor, return it. Returns nil otherwise.
    open var tabBarController: UITabBarController? &#123; get &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上源码，对 UIViewController 进行了扩展，内置了 UITabBar 的按钮，即 tabBarItem，该按钮可以添加文件、图标、消息汽泡等。</p>
<h2 data-id="heading-4">三、UITabBarController 的使用</h2>
<p>按照上一篇的内容，我们先创建工程，一切就绪如下：</p>
<p><img alt="ready.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd2287a729254c7f877519f47b2495e7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.1、创建 MainTabBarController</h3>
<p>先创建一个『New Group』，然后『New File』，如下：</p>
<p><img alt="MainTabBarController.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f34e7eac90c041a8a23be613af82297d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>选择『Cocoa Touch Class』，Subclass of 选择 UITabBarController：</p>
<p><img alt="SubClassOf.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e28dd5e14f5a4cc6a44841229c5a1fd7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3.2、添加 Group 及 5个 UIViewController</h3>
<p><img alt="5-vcs.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aea2593b0ff42509579bd39077f1bc2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.3、修改 AppDelegate.swift</h3>
<p>我们修改 AppDelegate.swift，让 window 的 rootViewController 为我们的 MainTabBarController：</p>
<p><img alt="modify-app-delegate.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b59322734d24efb9a066ef78012549d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>运行模拟器如下显示：</p>
<p><img alt="tabbar-run.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1fc3efd03a14b7d874980a259de0919~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最底部灰色区域就是底部导航 UITabBar。</p>
<h3 data-id="heading-8">3.4、添加 icons</h3>
<p>因为现在 macOS App Store 已经不允许下载 app 包到电脑，因此只能去官网下载 Android APK包，zip 解压后，搜索『.png』文件，结果只发现了『分类』、『购物车』和『我的』三种图标，而『首页』和『发现』没有找到。往年，双11 京东 app 底部的 icons 都会变，所以，底部图标默认的应该不是我们现在看到的样子，但总之，不影响我们的 demo 学习。</p>
<p>从 android apk 中拿到资源后，观察尺寸大小，将 40x40 的命名为 @2x，而 60x60 的命名为 @3x，如下：</p>
<p><img alt="images.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/143eb732634d48928a7d47544049b91b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后选择 Xcode 项目中的『Assets.xcassets』，将上面的图标拖进去即可：</p>
<p><img alt="drag-image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e39fa3ca4b7f48b7b9bb8d1a3eb43801~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>释放后，Xcode 会自动识别，如下：</p>
<p><img alt="after-drag.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7ea76548f544c00846f75b21cbb0a5a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">3.5、实现 UITabBarController 功能</h3>
<p>代码如下（以下代码是经过反复优化过后的）：</p>
<pre><code class="copyable">//
//  MainTabBarController.swift
//  JDApp
//
//  Created by qingye on 2021/3/5.
//

import UIKit

class MainTabBarController: UITabBarController &#123;

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        initTabBar()
    &#125;
    
    func initTabBar() &#123;
        let home = HomeViewController()
        home.tabBarItem.title = "首页"

        let category = CategoryViewController()
        category.tabBarItem.title = "分类"
        category.tabBarItem.image = UIImage(named: "category.png")

        let found = FoundViewController()
        found.tabBarItem.title = "发现"

        let cart = CartViewController()
        cart.tabBarItem.title = "购物车"
        cart.tabBarItem.image = UIImage(named: "cart.png")

        let mine = MineViewController()
        mine.tabBarItem.title = "我的"
        mine.tabBarItem.image = UIImage(named: "mine.png")

        viewControllers = [home, category, found, cart, mine]

        // 设置 tabBar & tabBarItem
        setTabBarItemAttributes(bgColor: UIColor(red: 0.95, green: 0.95, blue: 0.95, alpha: 1))
    &#125;

    /// 这种方式比较灵活
    func setTabBarItemAttributes(fontName: String = "Courier",
                                 fontSize: CGFloat = 14,
                                 normalColor: UIColor = .gray,
                                 selectedColor: UIColor = .red,
                                 bgColor: UIColor = .white) &#123;
        // tabBarItem 文字大小
        var attributes: [NSAttributedString.Key: Any] = [.font: UIFont(name: fontName, size: fontSize)!]
        
        // tabBarItem 文字默认颜色
        attributes[.foregroundColor] = normalColor
        UITabBarItem.appearance().setTitleTextAttributes(attributes, for: .normal)
        
        // tabBarItem 文字选中颜色
        attributes[.foregroundColor] = selectedColor
        UITabBarItem.appearance().setTitleTextAttributes(attributes, for: .selected)
        
        // tabBar 文字、图片 统一选中高亮色
        tabBar.tintColor = selectedColor
        
        // tabBar 背景色
        tabBar.barTintColor = bgColor
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>截图如下：</p>
<p><img alt="src-all.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc5534547be244b1ae2a457a9fec25d7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3.6、修改 HomeViewController 及 CategoryViewController</h3>
<ul>
<li>HomeViewController</li>
</ul>
<pre><code class="copyable">//
//  HomeViewController.swift
//  JDApp
//
//  Created by qingye on 2021/3/6.
//

import UIKit

class HomeViewController: UIViewController &#123;

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        
        view.backgroundColor = .green
        
        let label = UILabel(frame: CGRect.zero)
        label.text = "HomeViewController"
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)
        
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>CategoryViewController</li>
</ul>
<pre><code class="copyable">//
//  CategoryViewController.swift
//  JDApp
//
//  Created by qingye on 2021/3/6.
//

import UIKit

class CategoryViewController: UIViewController &#123;

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        
        let label = UILabel(frame: CGRect.zero)
        label.text = "CategoryViewController"
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)
        
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.7、运行模拟器</h3>
<p><img alt="run-home.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d675a8206bb43e287aba31db2b69bf6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="run-category.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec072c022164d0da842538667d6bd95~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>好了，本篇分享就到此结束，如果大家有什么问题，也希望多交流，谢谢！源代码会在下几次分享后，整体上传！后续会再次编辑此文，也可继续关注，谢谢！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            