
---
title: 'Swift 开发 wanandroid 客户端——封装ViewModel层'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e429426ce24d47a853df36c5475acf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 16:21:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e429426ce24d47a853df36c5475acf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这是我参与更文挑战的第22天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></h3>
<h2 data-id="heading-1">什么是MVVM</h2>
<p>其实对于MVVM是什么？有太多的文章与资料。绝对比我写的好，说的漂亮。所以我总结的不够专业和漂亮还请见谅。</p>
<p>作为一个iOS开发，其实站在原生开发角度上说，我是很少接触MVVM模式的，因为iOS的Cocoa框架是一个天然的MVC架构模式。所以我们先从MVC开始说吧。下面的这幅图广为流传：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e429426ce24d47a853df36c5475acf~tplv-k3u1fbpfcp-watermark.image" alt="59157bc07c7dd3399a8ce37413ff2553.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>M即Model，专门用来表示业务数据。</p>
<p>V在iOS中即UIView，专门用来做页面展示。</p>
<p>C在iOS中即UIViewController，用来处理接受到的交互事件，并进行处理后，想改变后的数据Model传递给View，更新页面等。</p>
<p>其实在iOS开发看来，嗯，一切正常，没毛病！</p>
<p>然后就会在Controller里面写UI，写网络请求.....然后，在OC时代，如果没有良好的整理与封装，一个Controller破千行是件容易的事情。写代码一时爽，CodeReview千行泪。</p>
<p>其实我们往往陷入了这样一个误区，<strong>UIViewController</strong>它是一个Controller，但是看看它的前缀<strong>UIView/Controller</strong>，它同时承载的作为UIView的使命啊，一人多职，不臃肿才怪呢！</p>
<p>甚至在最日常的代码中的页面跳转中，比如在某个view页面，点击了需要push到下一个页面，我们必须把view的事件回调到Controller层，然后通过Controller去push（当然这是iOS设计如此）。</p>
<p>但是在其他的开发中（Vue和Flutter），根本就没有所谓的Controller，任意一个页面的事件都可以做跳转。</p>
<p>所以狭隘的看问题，我们总是活生生的把UIView和UIViewController给分开了，明明它们就是一家人呀！所以可以说<strong>UIViewController是被处理数据和逻辑而被耽误的UIView！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d59999a23794a1bacca3e25bad3597e~tplv-k3u1fbpfcp-watermark.image" alt="b7ec292f5129b3cbc05a4c8c10e69e35.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>既然UIViewController不适合做数据处理和逻辑，那么我们就做这样一个层去干这个事吧，于是MVVM就出现了:</p>
<p><code>Model <=> ViewModel <=> UIView/UIViewController</code></p>
<p>UIView/UIViewController的作用仅仅是进行<strong>交互事件与展示数据，数据绑定</strong>。</p>
<p>ViewModel<strong>接受由UIView/UIViewController传递过来的事件，并做Model数据和逻辑业务，然后将处理好的数据由给UIView/UIViewController，进而去驱动UIView/UIViewController视图的变化。</strong></p>
<p>Model还是那个Model，<strong>用来表示业务数据</strong>。</p>
<p>重新分割职能后，我们看事情的角度和方向就有了新的变化。</p>
<p>说白了，MVVM在iOS中就是把UIView/UIViewController都看做是View层，通过新建ViewModel这一层，去处理之前Controller干的事情，由于是通过数据绑定去驱动页面的，所以交互->页面变化，自然而然。</p>
<h2 data-id="heading-2">为什么是MVVM</h2>
<p>我们叫ViewModel层，完全是出于习惯，你把它当做是一个中间层就可以，命名嘛，只不过是大家都这么叫于是就这么一直叫了。</p>
<p>MVVM其实已经在开发中大面积使用，特别是前端，基本上主流的框架的都是MVVM模式，同时它也经受住了考验，证明了这种模式的优越。</p>
<p>只是一般iOS开发中，原生对于数据绑定与驱动鲜有良好的支持，所以使得MVVM这种模式施展不开拳脚。而RxSwift却又恰恰是为MVVM模式而生的！</p>
<p>这里有一篇大佬写的通过原生支持MVVM的文章，大家可以看一看，原生是多么的难——<a href="https://juejin.cn/post/6961982789717606408" target="_blank" title="https://juejin.cn/post/6961982789717606408">MVC和MVVM详解</a>。</p>
<h2 data-id="heading-3">编写和使用ViewModel</h2>
<h3 data-id="heading-4">编写：抽离数据与业务逻辑</h3>
<p>我们新建一个类，叫RxSwiftCoinRankListViewModel，来进行抽离与封装：</p>
<pre><code class="copyable">class RxSwiftCoinRankListViewModel &#123;
    /// 初始化page为1
    private var page: Int = 1
    
    /// DisposeBag
    private let disposeBag: DisposeBag
    
    /// 既是可监听序列也是观察者的数据源,里面封装的其实是BehaviorSubject
    let dataSource: BehaviorRelay<[CoinRank]> = BehaviorRelay(value: [])
    
    /// 既是可监听序列也是观察者的状态枚举
    let refreshSubject: BehaviorSubject<MJRefreshAction> = BehaviorSubject(value: .begainRefresh)
    
    /// 初始化方法
    /// - Parameter disposeBag: 传入的disposeBag
    init(disposeBag: DisposeBag) &#123;
        self.disposeBag = disposeBag
    &#125;
    
    /// 下拉刷新行为
    func refreshAction() &#123;
        resetCurrentPageAndMjFooter()
        getCoinRank(page: page)
    &#125;
    
    /// 上拉加载更多行为
    func loadMoreAction() &#123;
        page = page + 1
        getCoinRank(page: page)
    &#125;
    
    /// 下拉的参数与状态重置行为
    private func resetCurrentPageAndMjFooter() &#123;
        page = 1
        refreshSubject.onNext(.resetNomoreData)
    &#125;
    
    /// 网络请求
    private func getCoinRank(page: Int) &#123;
        myProvider.rx.request(MyService.coinRank(page))
            /// 转Model
            .map(BaseModel<Page<CoinRank>>.self)
            /// 由于需要使用Page,所以return到$0.data这一层,而不是$0.data.datas
            .map&#123; $0.data &#125;
            /// 解包
            .compactMap &#123; $0 &#125;
            /// 转换操作
            .asObservable()
            .asSingle()
            /// 订阅
            .subscribe &#123; event in
                
                /// 订阅事件
                /// 通过page的值判断是下拉还是上拉(可以用枚举),不管成功还是失败都结束刷新状态
                page == 1 ? self.refreshSubject.onNext(.stopRefresh) : self.refreshSubject.onNext(.stopLoadmore)
                
                switch event &#123;
                case .success(let pageModel):
                    /// 解包数据
                    if let datas = pageModel.datas &#123;
                        /// 通过page的值判断是下拉还是上拉,做数据处理,这里为了方便写注释,没有使用三目运算符
                        if page == 1 &#123;
                            /// 下拉做赋值运算
                            self.dataSource.accept(datas)
                        &#125;else &#123;
                            /// 上拉做合并运算
                            self.dataSource.accept(self.dataSource.value + datas)
                        &#125;
                    &#125;
                    
                    /// 解包curPage与pageCount
                    if let curPage = pageModel.curPage, let pageCount = pageModel.pageCount  &#123;
                        /// 如果发现它们相等,说明是最后一个,改变foot而状态
                        if curPage == pageCount &#123;
                            self.refreshSubject.onNext(.showNomoreData)
                        &#125;
                    &#125;
                case .error(_):
                    /// error占时不做处理
                    break
                &#125;
            &#125;.disposed(by: disposeBag)
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">使用</h3>
<pre><code class="copyable">import UIKit

import RxSwift
import RxCocoa
import NSObject_Rx

import MJRefresh


class RxSwiftCoinRankListController: BaseViewController &#123;
    
    /// 懒加载tableView
    private lazy var tableView = UITableView(frame: .zero, style: .plain)
    
    override func viewDidLoad() &#123;
        super.viewDidLoad()
        setupTableView()
    &#125;
    
    private func setupTableView() &#123;
        
        /// 设置tableFooterView
        tableView.tableFooterView = UIView()
        
        /// 设置代理
        tableView.rx.setDelegate(self).disposed(by: rx.disposeBag)
        
        /// 创建vm
        let vm = RxSwiftCoinRankListViewModel(disposeBag: rx.disposeBag)
        
        /// 设置头部刷新控件
        tableView.mj_header = MJRefreshNormalHeader()
        
        tableView.mj_header?.rx.refresh
            .subscribe &#123; _ in
                vm.refreshAction()
        &#125;.disposed(by: rx.disposeBag)
        
        /// 设置尾部刷新控件
        tableView.mj_footer = MJRefreshBackNormalFooter()
        
        tableView.mj_footer?.rx.refresh
            .subscribe &#123; _ in
                vm.loadMoreAction()
        &#125;.disposed(by: rx.disposeBag)
        
        /// 简单布局
        view.addSubview(tableView)
        tableView.snp.makeConstraints &#123; make in
            make.edges.equalTo(view)
        &#125;
        
        /// 数据源驱动
        vm.dataSource
            .asDriver(onErrorJustReturn: [])
            .drive(tableView.rx.items) &#123; (tableView, row, coinRank) in
            if let cell = tableView.dequeueReusableCell(withIdentifier: "Cell") &#123;
                cell.textLabel?.text = coinRank.username
                cell.detailTextLabel?.text = coinRank.coinCount?.toString
                return cell
            &#125;else &#123;
                let cell = UITableViewCell(style: .subtitle, reuseIdentifier: "Cell")
                cell.textLabel?.text = coinRank.username
                cell.detailTextLabel?.text = coinRank.coinCount?.toString
                return cell
            &#125;
        &#125;
        .disposed(by: rx.disposeBag)
        
        /// 下拉与上拉状态绑定到tableView
        vm.refreshSubject
            .bind(to: tableView.rx.refreshAction)
            .disposed(by: rx.disposeBag)
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，是不是Controller中的代码更为精简与明了呢？</p>
<p>反馈下拉与上拉行为给vm，vm的dataSource去绑定tableView，vm中的refreshSubject去绑定tableView的下拉与上拉状态。</p>
<p>这就是所有的逻辑。</p>
<h2 data-id="heading-6">总结</h2>
<p>我用了四天的更新，基本讲解了通过RxSwift构建一个页面的过程：</p>
<ul>
<li>
<p>分别用Swift和RxSwift编写同一个页面，使用Moya与RxMoya，表现其中的不同点。</p>
</li>
<li>
<p>为页面中添加下拉刷新与上拉加载功能。</p>
</li>
<li>
<p>为页面通过RxSwift封装MJRefresh，让编码更简洁，更Rx。</p>
</li>
<li>
<p>在页面中抽离业务逻辑封装成ViewModel，并在页面中进行调用。</p>
</li>
</ul>
<p>到此，一个页面的编写与优化完成。</p>
<p>之前我就有说到过，玩安卓App的中的页面绝大部分都是列表，通过这四天的更新与知识点，很多页面都十分的通用。</p>
<p><strong>后面我在讲解其他页面的时候，就不会在页面的基本网络请求、下拉与上拉方面做具体的分析了，也请各位知晓。</strong></p>
<h2 data-id="heading-7">明日继续</h2>
<p>就如上面总结说的，这个页面写完了，很多页面也都可以依葫芦画瓢了。</p>
<p>后续会对首页ViewModel、页面编写进行讲解。</p>
<p>大家加油！</p></div>  
</div>
            