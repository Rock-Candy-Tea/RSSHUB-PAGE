
---
title: 'Swift：玩安卓App——页面下拉刷新和上拉加载功能'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=2612'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 16:29:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=2612'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这是我参与更文挑战的第20天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></h3>
<h2 data-id="heading-1">实现下拉刷新与上拉加载功能</h2>
<p>在昨天的代码中，我们通过RxSwift对积分排行榜的第一页进行网络请求和数据返回，然后使用数据去驱动页面的加载。</p>
<p>当然仅仅1页的加载，对于一个有分页功能的页面是根本是没有意义，做到做好下拉与上拉功能非常重要。</p>
<p>这里我们需要分析一下几点：</p>
<ul>
<li>
<p>集成什么控件去做下拉刷新与上拉加载？</p>
<ul>
<li><strong>MJRefresh，该控件虽然是OC写的，但是调用与封装都比较完善，新老手都可以使用。</strong></li>
</ul>
</li>
</ul>
<hr>
<ul>
<li>
<p>下拉刷新逻辑：</p>
<ul>
<li>
<p><strong>下拉刷新是要将page的页数重置为第1页，重置footer的状态。</strong></p>
</li>
<li>
<p><strong>对第1页的数据进行网络请求，将获取的数据赋值给数据源dataSource，让其驱动页面。</strong></p>
</li>
<li>
<p><strong>网络请求完成，注意不管是成功还是失败都应该结束下拉刷新的状态。</strong></p>
</li>
<li>
<p><strong>请求完第一页需要判断是否有下页，保持foot的显示与状态：</strong></p>
<ul>
<li><strong>这里使用的是玩安卓后台返回的两个字段来判断curPage与pageCount，如果相等就说明是最后一页，没有更多数据，如果curPage小于pageCount，说明还有下一页。</strong></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr>
<ul>
<li>上拉加载更多逻辑：
<ul>
<li>
<p><strong>上拉加载是要将page的页数加1。</strong></p>
</li>
<li>
<p><strong>对第page + 1页的数据进行网络请求，将获取的数据与之前的dataSourc进行合并，注意是合并，而不是直接赋值，让其驱动页面。</strong></p>
</li>
<li>
<p><strong>网络请求完成，注意不管是成功还是失败都应该结束上拉加载更多的状态。</strong></p>
</li>
<li>
<p><strong>请求完第page + 1页需要判断是否有下页，保持foot的显示与状态：</strong></p>
<ul>
<li><strong>这里使用的是玩安卓后台返回的两个字段来判断curPage与pageCount，如果相等就说明是最后一页，没有更多数据，如果curPage小于pageCount，说明还有下一页。</strong></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr>
<p>好了上面的分析做完了，那么就按照这个思路修改代码了，<strong>请注意看代码注释喔</strong>：</p>
<pre><code class="copyable">import UIKit

import RxSwift
import RxCocoa
import NSObject_Rx
import Moya
import MJRefresh


class RxSwiftCoinRankListController: BaseViewController &#123;
    
    /// 懒加载tableView
    private lazy var tableView = UITableView(frame: .zero, style: .plain)
    
    /// 初始化page为1
    private var page: Int = 1
    
    /// 既是可监听序列也是观察者的数据源
    private var dataSource: BehaviorRelay<[CoinRank]> = BehaviorRelay(value: [])
    
    override func viewDidLoad() &#123;
        super.viewDidLoad()
        setupTableView()
    &#125;
    
    private func setupTableView() &#123;
        
        /// 设置tableFooterView
        tableView.tableFooterView = UIView()
        
        /// 设置代理
        tableView.rx.setDelegate(self).disposed(by: rx.disposeBag)
        
        /// 设置头部刷新控件
        tableView.mj_header = MJRefreshNormalHeader()
        
        tableView.mj_header?.beginRefreshing &#123; [weak self] in
            self?.refreshAction()
        &#125;
        
        /// 设置尾部刷新控件
        tableView.mj_footer = MJRefreshBackNormalFooter()
        
        tableView.mj_footer?.beginRefreshing &#123; [weak self] in
            self?.loadMoreAction()
        &#125;
        
        /// 简单布局
        view.addSubview(tableView)
        tableView.snp.makeConstraints &#123; make in
            make.edges.equalTo(view)
        &#125;
        
        /// 数据源驱动
        dataSource
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
    &#125;

&#125;

extension RxSwiftCoinRankListController &#123;
    /// 下拉刷新行为
    private func refreshAction() &#123;
        resetCurrentPageAndMjFooter()
        getCoinRank(page: page)
    &#125;
    
    /// 上拉加载更多行为
    private func loadMoreAction() &#123;
        page = page + 1
        getCoinRank(page: page)
    &#125;
    
    /// 下拉的参数与状态重置行为
    private func resetCurrentPageAndMjFooter() &#123;
        page = 1
        self.tableView.mj_footer?.isHidden = false
        self.tableView.mj_footer?.resetNoMoreData()
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
                page == 1 ? self.tableView.mj_header?.endRefreshing() : self.tableView.mj_footer?.endRefreshing()
                
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
                            self.tableView.mj_footer?.endRefreshingWithNoMoreData()
                        &#125;
                    &#125;
                case .error(_):
                    /// error占时不做处理
                    break
                &#125;
            &#125;.disposed(by: rx.disposeBag)
    &#125;
&#125;

extension RxSwiftCoinRankListController: UITableViewDelegate &#123;&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码已经写完了完善的注释，这里单独说一下：</p>
<p><code>private var dataSource: BehaviorRelay<[CoinRank]> = BehaviorRelay(value: [])</code>中的<code>dataSource</code>。</p>
<p><strong>不同于一般的dataSource是一个数组，这里我们使用了RxSwift中的BehaviorRelay，它既是一个序列也可以是一个观察者，并且可以对数据进行赋值运算。序列可以转为特化序列Driver，并驱动tableView，可以做赋值运算，于是可以将网络请求的数据进行赋值和合并操作，在我上面的代码中非常关键。</strong></p>
<h2 data-id="heading-2">那么下一步是？</h2>
<p>其实上面的代码运行起来没有什么问题，只是并不<strong>RxSwifty</strong>，没有那种rx.xxxx回调的感觉。</p>
<p>我个人的理解是，有的是时候不能光顾着面子的上的事，先保证功能没有问题了，再来考虑拓展与深度。掌握好基础的知识与技能是基石。</p>
<p>同时，在写上面的代码的时候，我也在考虑<strong>如何用一个值去绑定tableView，通过状态来改变header与footer的UI状态。</strong></p>
<p>这个其实和声明式UI编写的原则一致了，<code>UI = f(state)</code>。</p>
<h2 data-id="heading-3">明日继续</h2>
<p>我继续围绕着MJRefresh与下拉刷新和上拉加载，考虑使用RxSwift对其进行一层，来进行更好的编程。</p>
<p>为啥我会抓着一个简单的列表不放：玩安卓App很多页面都是列表，写好一个，其他的都可以按照这个思路编写与复用。</p>
<p>大家加油。</p></div>  
</div>
            