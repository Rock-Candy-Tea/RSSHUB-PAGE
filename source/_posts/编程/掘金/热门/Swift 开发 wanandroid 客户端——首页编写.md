
---
title: 'Swift 开发 wanandroid 客户端——首页编写'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=8829'
author: 掘金
comments: false
date: Thu, 24 Jun 2021 16:42:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=8829'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这是我参与更文挑战的第25天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></h3>
<h2 data-id="heading-1">前两天的构建回顾</h2>
<p>在之前的文章中，我们分别构建了HomeViewModel以及BaseViewController和BaseTableViewController的构建，由于有这个两个基础组件的编写，我们首页基本上就剩下交互与数据绑定了。</p>
<p>不过在此之前，我们的首页有一个轮播图，我们先把这个给处理了。</p>
<h2 data-id="heading-2">代码编写</h2>
<p>这次轮播图我使用了第三方库——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWenchaoD%2FFSPagerView" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WenchaoD/FSPagerView" ref="nofollow noopener noreferrer">FSPagerView</a>。如果有人使用过FSCalendar，应该应该就有印象了，没错就是那位写日历大佬写的轮播组件。</p>
<p>昨天我也说了，与其费时费力的通过RxSwift去封装第三库，不如直接调用来的简单容易，也可以少掉一些头发。</p>
<p>再加上我完全对这个库不熟悉，所以这里就直接当个Api调用工程师吧。</p>
<p><strong>另外由于之前已经抽取了基类和ViewModel，代码量不大，我就直接上全部的代码，大家仔细看代码注释就好：</strong></p>
<pre><code class="copyable">import Foundation

import RxSwift
import RxCocoa
import NSObject_Rx
import SnapKit
import MJRefresh
import Kingfisher
import FSPagerView

class HomeController: BaseTableViewController &#123;
    /// 接受轮播图的数据源
    var itmes: [Banner] = []
        
    override func viewDidLoad() &#123;
        super.viewDidLoad()
        setupUI()
    &#125;
&#125;

extension HomeController &#123;
    private func setupUI() &#123;
        
        title = "首页"
        
        /// 获取indexPath
        tableView.rx.itemSelected
            .bind &#123; [weak self] (indexPath) in
                self?.tableView.deselectRow(at: indexPath, animated: false)
                print(indexPath)
            &#125;
            .disposed(by: rx.disposeBag)
        
        
        /// 获取cell中的模型
        tableView.rx.modelSelected(Info.self)
            .subscribe(onNext: &#123; [weak self] model in
                print("去下一个页面")
            &#125;)
            .disposed(by: rx.disposeBag)
        
        /// 创建HomeViewModel
        let viewModel = HomeViewModel(disposeBag: rx.disposeBag)
        
        /// 下拉刷新
        tableView.mj_header?.rx.refresh
            .asDriver()
            .drive(onNext: &#123;
                viewModel.loadData(actionType: .refresh)
                
            &#125;)
            .disposed(by: rx.disposeBag)
        
        /// 上拉加载
        tableView.mj_footer?.rx.refresh
            .asDriver()
            .drive(onNext: &#123;
                viewModel.loadData(actionType: .loadMore)
                
            &#125;)
            .disposed(by: rx.disposeBag)

        /// 绑定数据
        viewModel.dataSource
            .asDriver(onErrorJustReturn: [])
            .drive(tableView.rx.items) &#123; (tableView, row, info) in
                if let cell = tableView.dequeueReusableCell(withIdentifier: "Cell") as? InfoViewCell &#123;
                    cell.info = info
                    return cell
                &#125;else &#123;
                    let cell = InfoViewCell(style: .subtitle, reuseIdentifier: "Cell")
                    cell.info = info
                    return cell
                &#125;
            &#125;
            .disposed(by: rx.disposeBag)
        
        /// 空数据绑定
        viewModel.dataSource.map &#123; $0.count == 0 &#125;.bind(to: isEmpty).disposed(by: rx.disposeBag)
        
        /// 下拉与上拉状态绑定到tableView
        viewModel.refreshSubject
            .bind(to: tableView.rx.refreshAction)
            .disposed(by: rx.disposeBag)
        
        //MARK:- 轮播图的设置,这一段基本上就典型的Cocoa代码了
        
        /// 初始化pagerView 
        let pagerView = FSPagerView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.width, height: UIScreen.main.bounds.width / 16.0 * 9))
        
        /// 设置轮播图的代理与数据
        pagerView.dataSource = self
        pagerView.delegate = self
        
        /// 注册轮播图cell
        pagerView.register(FSPagerViewCell.self, forCellWithReuseIdentifier: "FSPagerViewCell")
        
        /// 轮播时间
        pagerView.automaticSlidingInterval = 3.0
        
        /// 无限轮播
        pagerView.isInfinite = true
        
        /// 将pagerView赋值给tableView.tableHeaderView
        tableView.tableHeaderView = pagerView
        
        /// 轮播图的小圆点配置
        
        /// 初始化FSPageControl
        let pageControl = FSPageControl(frame: CGRect.zero)
        
        /// 小圆点的个数
        pageControl.numberOfPages = itmes.count
        
        /// 当前小圆点所在位置
        pageControl.currentPage = 0
        
        /// 数据为1时隐藏pageControl组件
        pageControl.hidesForSinglePage = true
        
        /// 将pageControl添加到pagerView
        pagerView.addSubview(pageControl)
        
        /// pageControl移到pagerView的最上方
        pagerView.bringSubviewToFront(pageControl)
        
        /// 使用SnapKit进行布局，左、右、底与pagerView靠紧，高度为40
        pageControl.snp.makeConstraints &#123; make in
            make.leading.trailing.bottom.equalTo(pagerView)
            make.height.equalTo(40)
        &#125;
        
        /// viewModel的数据驱动，将models赋值给items，重新设置pageControl的小圆点个数，reloadData
        viewModel.banners.asDriver(onErrorJustReturn: []).drive &#123; [weak self] models in
            self?.itmes = models
            pageControl.numberOfPages = models.count
            pagerView.reloadData()
        &#125;.disposed(by: rx.disposeBag)
    &#125;
&#125;

/// FSPagerViewDataSource数据源，基本上和TableView的数据源大同小异
extension HomeController: FSPagerViewDataSource &#123;
    func numberOfItems(in pagerView: FSPagerView) -> Int &#123;
        return itmes.count
    &#125;
    
    func pagerView(_ pagerView: FSPagerView, cellForItemAt index: Int) -> FSPagerViewCell &#123;
        let cell = pagerView.dequeueReusableCell(withReuseIdentifier: "FSPagerViewCell", at: index)
        if let imagePath = itmes[index].imagePath, let url = URL(string: imagePath) &#123;
            cell.imageView?.kf.setImage(with: url)
        &#125;
        return cell
    &#125;
&#125;

/// FSPagerViewDataSource代理，基本上和TableView的代理大同小异
extension HomeController: FSPagerViewDelegate &#123;
    func pagerView(_ pagerView: FSPagerView, didSelectItemAt index: Int) &#123;
        pagerView.deselectItem(at: index, animated: false)
        let item = itmes[index]
        print("点击了轮播图的\(item)")
    &#125;
    
    /// 这里通过willDisplay方法去改变当前的小圆点
    func pagerView(_ pagerView: FSPagerView, willDisplay cell: FSPagerViewCell, forItemAt index: Int) &#123;
        guard let pageControl = pagerView.subviews.last as? FSPageControl else &#123;
            return
        &#125;
        pageControl.currentPage = index
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">说明</h2>
<p>好了上面的代码基本上我都逐行写了注释，应该比较清晰了，挑一些之前没讲过的说说：</p>
<ul>
<li>我尝试使用了序列Driver：</li>
</ul>
<pre><code class="copyable">tableView.mj_header?.rx.refresh
            .asDriver()
            .drive(onNext: &#123;
                viewModel.loadData(actionType: .refresh)
                
            &#125;)
            .disposed(by: rx.disposeBag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实没有什么特别的，就是一种在主线程进行订阅的序列，非常适合去驱动UI。</p>
<ul>
<li>我尝试当数据为空的时候与BaseTableViewController的isEmpty进行绑定：</li>
</ul>
<pre><code class="copyable">viewModel.dataSource.map &#123; $0.count == 0 &#125;.bind(to: isEmpty).disposed(by: rx.disposeBag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是当数据为0时，会走基类的DZNEmptyDataSet中的相关方法，经过验证尝试更改<code>map &#123; $0.count == 0 &#125;</code>中的逻辑，是可行的。</p>
<ul>
<li>由于这次的列表的Cell稍微特殊点，有文字有图，文字有可能会比较长导致单个Cell的高度不确定于是使用了自定义Cell——<strong>InfoViewCell</strong>。</li>
</ul>
<p>如何自定义一个Cell，使得其能自适应高度，撑满Cell，以及Cell中的图片根据模型中的字段显示和不显示，这个篇幅会有点长，需要单独说明。</p>
<ul>
<li>最后说一说轮播图的Banner模型和单个Cell的Info模型，在点击它们后，都是可以跳转到一个WebView页面，加载一个URL的：</li>
</ul>
<p><strong>而关键是这两个模型长的不太一样：</strong></p>
<p>Banner模型</p>
<pre><code class="copyable">struct Banner : Codable &#123;
    
    var id : Int?
    
    var title : String?
    
    var originId: Int? = nil
    
    var link: String? &#123; url &#125;
        
    let desc : String?
    
    let imagePath : String?
    let isVisible : Int?
    let order : Int?
    
    let type : Int?
    let url : String?
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Info模型：</p>
<pre><code class="copyable">/// 单个信息模型,用于首页,项目,公众号,搜索关键词,体系,收藏夹
struct Info : Codable &#123;
    
    var title : String?
    
    var link: String?
    /// 我的收藏接口originId才是文章的标识符,id没有用,不要使用
    var originId: Int?
    /// 不是我的收藏接口,拿到的id就是文章的标识符,需要通过这个字段进行收藏与取消收藏的操作,此时originId为nil
    var id : Int?
    
    let apkLink : String?
    let audit : Int?
    let author : String?
    let canEdit : Bool?
    let chapterId : Int?
    let chapterName : String?
    let collect : Bool?
    let courseId : Int?
    let desc : String?
    let descMd : String?
    let envelopePic : String?
    let fresh : Bool?

    
    let niceDate : String?
    let niceShareDate : String?
    let origin : String?

    let prefix : String?
    let projectLink : String?
    let publishTime : Int?
    let selfVisible : Int?
    let shareDate : Int?
    let shareUser : String?
    let superChapterId : Int?
    let superChapterName : String?
    let tags : [Tag]?

    let type : Int?
    let userId : Int?
    let visible : Int?
    let zan : Int?
&#125;

struct Tag : Codable &#123;

    let name : String?
    let url : String?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家可以看到，banner模型中并没有link字段，而有url字段，于是我自己写了一个只读计算属性<code>var link: String? &#123; url &#125;</code>。</p>
<p>另外要说明的是这个Info这个模型在很多地方通用，同时InfoViewCell也在很多列表通用，但是有两个字段又有些区别：</p>
<p>id字段： <strong>非</strong><code>我的收藏接口</code>，拿到的id就是文章的标识符，需要通过这个字段进行收藏与取消收藏的操作，此时originId为nil。</p>
<p>originId字段：<code>我的收藏接口</code>originId才是文章的标识符，id有值，但是这个id不是文章的标识符，不能使用。</p>
<h3 data-id="heading-4">方式一</h3>
<p>一般要将两个不同的模型糅合成一个模型的方法就是创建一个基类，然后让Info和Banner分别继承这个基类，传值的时候传基类模型即可，基类的写法大概就是这：</p>
<pre><code class="copyable">class SomeBase : Codable &#123;
    
    var title : String?
    
    var link: String?

    var originId: Int?

    var id : Int?
&#125;

class Info: SomeBase &#123;
    ....
&#125;

class Bananer: SomeBase &#123;
    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意我这样写的时候，模型都换成了class，因为struct是无法继承的。</p>
<h3 data-id="heading-5">方式二</h3>
<p>但是既然我写的是Swift编程，Swift编程是鼓励使用<strong>面向协议的编程方式的。</strong></p>
<p>我们通过写一个协议，并使得Banner与Info的分类去遵守协议即可。</p>
<pre><code class="copyable">
import Foundation

protocol WebLoadInfo &#123;
    var id: Int? &#123; set get &#125;
    var originId: Int? &#123; set get &#125;
    var title: String? &#123; set get &#125;
    var link: String? &#123; get &#125;
&#125;

extension Info: WebLoadInfo &#123;&#125;

extension Bananer: WebLoadInfo &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：大家注意看Info与Banner两个模型的id、originId、title、link我都是用var修饰，其实模型用工具类生成的时候都是用let修饰的，只是为了遵守WebLoadInfo协议，改成了var。</strong></p>
<p>虽然有改动，但是侵略性小，问题迎刃而解。</p>
<p>这样我们在传值的时候，使用<code>WebLoadInfo</code>就可以了。</p>
<h2 data-id="heading-6">总结</h2>
<p>本篇文章主要讲解了HomeController的编写：</p>
<ul>
<li>
<p>由于之前有BaseViewController与BaseTableViewController做基类，并且HomeViewModel已经将逻辑写好。重点是FSPagerView的使用，详细的用法我已经在上面的代码注释写过了。</p>
</li>
<li>
<p>另外就是对于Banner模型与Info模型如何将其公共部分糅合成一个公共类便于调用，我通过<strong>继承</strong>与<strong>遵守协议</strong>两种思路进行了讲解，继承是典型的面向对象思路，而面向协议则是Swift比较推荐，每个人有每个人的习惯，这里不做强求。</p>
</li>
</ul>
<h2 data-id="heading-7">明日继续</h2>
<p>本篇其实有一个内容没有讲完，那就是<strong>InfoViewCell</strong>的布局，考虑自己的撸代码和写作的能力，这部分需要另起炉灶讲解了。</p>
<p>大家加油。</p></div>  
</div>
            