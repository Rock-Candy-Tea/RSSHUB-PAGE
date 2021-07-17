
---
title: 'Swift 开发 wanandroid 客户端——基类控制器BaseViewController、BaseTableViewController'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/349a34fe1bb74b5c896e5d0cdbff10f5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 23 Jun 2021 16:41:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/349a34fe1bb74b5c896e5d0cdbff10f5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这是我参与更文挑战的第24天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></h3>
<h2 data-id="heading-1">每日更新，我到底在做啥？</h2>
<p>很多朋友总是被我的标题给迷惑了，Swift？玩安卓App？都是些啥？</p>
<p>我反思了一下，确实自己的标题取得不太好。加上有没有附图我到底在做啥，是我的失误。</p>
<p>所以我决定还是传一张Gif给大家看看，我都在写一个什么样的东东，一个没啥太多华丽UI，<strong>用Swift编写的iOS App</strong>，基本上我编写的代码和更文算是同步的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/349a34fe1bb74b5c896e5d0cdbff10f5~tplv-k3u1fbpfcp-watermark.image" alt="RPReplay_Final1624432101.2021-06-24 08_35_54.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">为什么要写基类控制器</h2>
<p>给大家分享一个自己刚入行的经历，我刚刚从事iOS开发。</p>
<p>那会还在写OC代码，新手总是从写UI开始的，我也不例外，由于事先大佬也没有叮嘱写什么，我就开始讲自己写的Controller一个个创建，大概就是这样</p>
<pre><code class="copyable">@interface XXXXController : UIViewController
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没什么啥毛病。</p>
<p>有天，不知道是产品还是UI来了什么灵感，说我们这页面的背景色需要做些许改动，大佬说，好的没事，一行代码的事。然后大佬确实改了一行代码提交看了效果，不错，然后就开开心心提测了。</p>
<p>于是，测试就过来了，你写的这页面好奇怪啊，大部分的页面背景色都是一致的，但是有几个怎么都看起来有色差，怎么回事？</p>
<p>不用多说，有色差的页面都是我写的，至于原因很简单，大佬写的代码都是这样的：</p>
<pre><code class="copyable">@interface XXXXController : BaseViewController
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他页面写的时候都是继承的基类控制器，只有我继承UIViewController，大佬也没有责怪我，因为他以为我知道这种规则就没和我交代，所以出了差错，加上改改继承基本上就解决问题，所以也不是什么大事。</p>
<p>分享我的这个经历，其实在之后的工作中给了我很多思考：</p>
<ul>
<li>
<p>一个App中，大部分页面的UI风格、颜色、样式基本上都是一致，通过继承自定义的BaseViewController可以很快的完成基础配置。</p>
</li>
<li>
<p>其实不仅是Controller层，有的时候包括View层，我们需要定义一个BaseView，来进行基础配置，如果有业务需要BaseTableViewCell等都是可以考虑的。这个就和写BaseModel有些相似。</p>
</li>
<li>
<p>自己写项目，记得要做一些基类的编写，自己接手其他人的项目，我也总会先让别人给我介绍一下他们的基类。</p>
</li>
</ul>
<h2 data-id="heading-3">编写BaseViewController</h2>
<p>基于上面的工作经历与思考，现在我们就来玩安卓App的BaseViewController吧：</p>
<pre><code class="copyable">import UIKit

import RxSwift
import RxCocoa

class BaseViewController: UIViewController &#123;
    
    private lazy var errorImage: UIImageView = &#123;
        let imageView = UIImageView(image: R.image.saber())
        imageView.contentMode = .scaleAspectFit
        return imageView
    &#125;()
    
    override func viewDidLoad() &#123;
        super.viewDidLoad()
        
        /// 最简单的设置统一返回按钮的方法,所有的控制器继承该基类即可
        let leftBarButtonItem = UIBarButtonItem(image: R.image.back(), style: .plain, target: self, action: #selector(leftBarButtonItemAction(_:)))
        navigationItem.leftBarButtonItem = (navigationController?.viewControllers.count ?? 0) > 1 ? leftBarButtonItem : nil
        navigationItem.hidesBackButton = true
        
        /// 这里的代码有问题，需要注释掉
        //navigationController?.interactivePopGestureRecognizer?.delegate = nil
                
        view.backgroundColor = .white
        
        setupErrorImage()
    &#125;
        
    @objc
    private func leftBarButtonItemAction(_ item: UIBarButtonItem) &#123;
        navigationController?.popViewController(animated: true)
    &#125;
    
    deinit &#123;
        print("\(className)被销毁了")
    &#125;

&#125;

//MARK:- 网络请求错误页面的配置项(待用)
extension BaseViewController &#123;
    private func setupErrorImage() &#123;
        view.addSubview(errorImage)
        errorImage.snp.makeConstraints &#123; make in
            make.edges.equalTo(view)
        &#125;
        errorImage.isHidden = true
    &#125;
    
    func showErrorImage() &#123;
        errorImage.isHidden = false
        view.bringSubviewToFront(errorImage)
    &#125;
    
    func hiddenErrorImage() &#123;
        errorImage.isHidden = true
        view.sendSubviewToBack(errorImage)
    &#125;
&#125;

//MARK:- 绑定
extension Reactive where Base: BaseViewController &#123;
    
    /// 显示网络错误
    var networkError: Binder<Void> &#123;
        return Binder(base) &#123; vc, _ in
            vc.showErrorImage()
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这样BaseViewController做了一下几件事情：</p>
<ul>
<li>
<p>自定义返回按钮</p>
<ul>
<li>
<p>这里我们使用自定义的leftBarButtonItem去代替了系统的backButton，代码块中这种方式是目前我见过设置最简单、功能不会缺失的好办法。只要UINavigationControlle初始化方法传入的是BaseViewController的子类即可实现。</p>
</li>
<li>
<p>系统的侧滑没有失效。</p>
</li>
<li>
<p><del>点击leftBarButtonItem的返回事件。</del></p>
</li>
<li>
<p>勘误：上面这段话是有问题的，有大佬<a href="https://juejin.cn/user/1099167357483032" target="_blank" title="https://juejin.cn/user/1099167357483032">nlnlnull</a>留言说，我这样写，会在根控制器中尝试使用侧滑手势后，会出现异常情况，已经验证，确实如此。</p>
</li>
</ul>
<p>自己写的代码没有好好验证与追根朔源，还是非常感谢大佬的提醒，具体地址的问题请看这篇文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F0f5517307eb3" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/0f5517307eb3" ref="nofollow noopener noreferrer">自定义leftBarButtonItem导致侧滑失效</a>。</p>
<p>BaseViewController中需要删除这段代码，在代码块中，删除无法显示，这里单独说明：</p>
<p><strong><del>navigationController?.interactivePopGestureRecognizer?.delegate = nil</del></strong></p>
<p>因此，我们还需要写一个BaseNavigationController，来避免这个问题的发生：</p>
<pre><code class="copyable">import UIKit

class BaseNavigationController: UINavigationController &#123;

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        interactivePopGestureRecognizer?.delegate = self
        delegate = self
    &#125;
&#125;

extension BaseNavigationController: UIGestureRecognizerDelegate, UINavigationControllerDelegate &#123;
    func navigationController(_ navigationController: UINavigationController, didShow viewController: UIViewController, animated: Bool) &#123;
        interactivePopGestureRecognizer?.isEnabled = true
        /// 解决某些情况下push时的假死bug，防止把根控制器pop掉
        if (navigationController.viewControllers.count == 1) &#123;
            interactivePopGestureRecognizer?.isEnabled = false
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置了控制器的背景色为白色。</p>
</li>
<li>
<p>通过RxSwift，针对网络请求导致的页面进行了页面处理，这一块由于Rx我也是一点点学习，目前可能思路与处理都不算太好，这里只是写出来了。</p>
</li>
<li>
<p>在析构函数中添加了一段打印，用于查看控制器的销毁情况。</p>
</li>
</ul>
<p>之前，我也说过，玩安卓App中有很多页面都是列表，考虑到这种情况，编写一个BaseTableViewController也是很有的必要的。</p>
<h2 data-id="heading-4">编写BaseTableViewController</h2>
<p>首先BaseTableViewController它是继承于BaseViewController。</p>
<p>同时由于是为了展示列表，我们需要在里面布局一个UITableView。</p>
<p>考虑列表可能会有数据为空的情况，我们需要对页面做定制化处理，这里我选择使用了OC库——<code>DZNEmptyDataSet</code>。</p>
<pre><code class="copyable">import UIKit

import RxSwift
import RxCocoa

import MJRefresh
import DZNEmptyDataSet

class BaseTableViewController: BaseViewController &#123;
    
    lazy var tableView = UITableView(frame: .zero, style: .plain)
    
    let emptyDataSetButtonTap = PublishSubject<Void>()
    
    let isEmpty = BehaviorRelay(value: false)

    override func viewDidLoad() &#123;
        super.viewDidLoad()
        setupTableView()
    &#125;
    
    private func setupTableView() &#123;
        
        /// 设置tableFooterView
        tableView.tableFooterView = UIView()
        
        /// 设置代理
        tableView.rx.setDelegate(self).disposed(by: rx.disposeBag)
        
        /// 简单布局
        view.addSubview(tableView)
        tableView.snp.makeConstraints &#123; make in
            make.edges.equalTo(self.view)
        &#125;
        
        /// 设置头部刷新控件
        tableView.mj_header = MJRefreshNormalHeader()
        /// 设置尾部刷新控件
        tableView.mj_footer = MJRefreshBackNormalFooter()
        
        /// 设置DZNEmptyDataSet的数据源和代理
        tableView.emptyDataSetSource = self
        tableView.emptyDataSetDelegate = self
        
        /// 订阅点击了数据为空，请重试的行为，里面没有用状态去绑定tableView是因为没有ViewModel
        emptyDataSetButtonTap.subscribe &#123; [weak self] _ in
            self?.tableView.mj_header?.beginRefreshing()
        &#125;.disposed(by: rx.disposeBag)
        
        /// 数据为空的订阅（待用）
        isEmpty.subscribe &#123; event in
            switch event &#123;
            case .next(let noContent):
                break
            default:
                break
            &#125;
        &#125;.disposed(by: rx.disposeBag)
    &#125;

&#125;

//MARK:- UITableViewDelegate
extension BaseTableViewController: UITableViewDelegate &#123;&#125;

//MARK:- DZNEmptyDataSetSource
extension BaseTableViewController: DZNEmptyDataSetSource &#123;

    func title(forEmptyDataSet scrollView: UIScrollView!) -> NSAttributedString! &#123;
        return NSAttributedString(string: "暂无数据")
    &#125;

    func description(forEmptyDataSet scrollView: UIScrollView!) -> NSAttributedString! &#123;
        return NSAttributedString(string: "尝试点击刷新获取数据")
    &#125;

    func backgroundColor(forEmptyDataSet scrollView: UIScrollView!) -> UIColor! &#123;
        return .clear
    &#125;

    func verticalOffset(forEmptyDataSet scrollView: UIScrollView!) -> CGFloat &#123;
        return -60
    &#125;
&#125;

//MARK:- DZNEmptyDataSetSource
extension BaseTableViewController: DZNEmptyDataSetDelegate &#123;

    func emptyDataSetShouldDisplay(_ scrollView: UIScrollView!) -> Bool &#123;
        return isEmpty.value
    &#125;

    func emptyDataSetShouldAllowScroll(_ scrollView: UIScrollView!) -> Bool &#123;
        return true
    &#125;
    
    func emptyDataSet(_ scrollView: UIScrollView!, didTap view: UIView!) &#123;
        emptyDataSetButtonTap.onNext(())
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这段<code>DZNEmptyDataSet</code>的代码，基本上和OC时代写的代码没什么太多差别，我甚至去看了知名开源App——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkhoren93%2FSwiftHub" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/khoren93/SwiftHub" ref="nofollow noopener noreferrer">SwiftHub</a>，想看看大佬有没有对DZNEmptyDataSet做一层RxSwift的封装，写起来更简单。</p>
<p>结论是没有！SwiftHub也是在分类里面写实现数据源和代理的方式对页面为空的情况做处理。</p>
<p><strong>于是我也在想，费尽精力的去写第三库的RxSwift扩展，不如直接用来的省事。</strong></p>
<h2 data-id="heading-5">总结</h2>
<p>由于之前写的积分排行页面——RxSwiftCoinRankListController是一个独立的讲解页面，没有过多去讲解BaseViewController。</p>
<p>虽然当时已经使用过了这个基类了，但是笔墨更多的是讲解网络请求和上拉与下拉的操作行为。</p>
<p>随着我开始写首页的HomeViewModel，我才意识到我漏掉了这一环。</p>
<p>编写基类，虽然不是必须的，但是有了基类，可能会让平时的编码中更为轻松一点，虽然Swift更偏向面向协议编程，但是面向对象编程已经存在这么多年了，它也有它的优势，继承使用的小心慎重，思考是否需要继承都是思考的结晶。</p>
<h2 data-id="heading-6">明日继续</h2>
<p>讲完基类控制器，下面该讲解首页的编写了。</p>
<p>大家加油！</p></div>  
</div>
            