
---
title: 'iOS架构浅谈从 MVC、MVP 到 MVVM'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6622f8772414381b107c78911d5779c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:18:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6622f8772414381b107c78911d5779c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">概述</h3>
<p>做了这么多年的客户端研发一直在使用苹果爸爸推荐的MVC架构模式。MVC从应用层面进行分层开发，极大优化了我们的代码结构，简单易上手，很容易被程序员所接受。程序员刚接手一个新项目，如果是MVC的架构模式，会减少代码熟悉时间，快速的进行开发和维护工作，实际上对于多人开发维护的项目，MVC仍然是非常好的架构模式，这也是这种架构模式经久不衰的原因。<br>但是任何事物都有两面性，随着项目需求的增加，业务逻辑、网络请求、代理方法等都往Controller层加塞，导致Controller层变得越来越臃肿，动辄上千行的代码量绝对是维护人员的噩梦，因此在MVC基础上逐渐衍生出来了MVP、MVVM等架构模式。
<br>本文是基于<code>OC</code>代码进行阐述的，使用iOS开发经典的 <code>TableView</code> 列表来分析每个架构模式。相信看了这篇文章你会有所领悟。当然一千个人眼中有一千种哈姆雷特，具体在业务开发中使用哪种模式需要你自己去衡量。</p>
<h3 data-id="heading-1">1.传统的<code>MVC</code>设计模式</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6622f8772414381b107c78911d5779c~tplv-k3u1fbpfcp-zoom-1.image" alt="MVC" loading="lazy" referrerpolicy="no-referrer"><br>
<code>M</code>: Model 数据层，负责网络数据的处理，数据持久化存储和读取等工作<br>
<code>V</code>: View 视图层，负责呈现从数据层传递的数据渲染工作，以及与用户的交互工作<br>
<code>C</code>: Controller控制器，负责连接Model层跟View层，响应View的事件和作为View的代理，以及界面跳转和生命周期的处理等任务</p>
<h4 data-id="heading-2">用户的交互逻辑</h4>
<p>用户点击 View(视图) --> 视图响应事件 -->通过代理传递事件到Controller-->发起网络请求更新Model--->Model处理完数据-->代理或通知给Controller-->改变视图样式-->完成</p>
<blockquote>
<p>可以看到Controller强引用View与Model，而View与Model是分离的，所以就可以保证Model和View的可测试性和复用性，但是Controller不行，因为Controller是Model和View的中介，所以不能复用，或者说很难复用。</p>
</blockquote>
<h4 data-id="heading-3">iOS开发实际使用的MVC架构</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66e1920e4c2c483cbfa617098ab440dc~tplv-k3u1fbpfcp-zoom-1.image" alt="实际MVC" loading="lazy" referrerpolicy="no-referrer">
在我们实际开发中使用的MVC模式可以看到，View与Controller耦合在一起了。这是由于每一个界面的创建都需要一个Controller，而每一个Controller里面必然会带一个View，这就导致了C和V的耦合。这种结构确实可以提高开发效率，但是一旦界面复杂就会造成Controller变得非常臃肿和难以维护。</p>
<h4 data-id="heading-4">MVC代码示例</h4>
<p>我们要实现一个简单的列表页面，每行cell都一个按钮，点击按钮前面数字➕1操作。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b1f99ef3a942469fd848b31b558b66~tplv-k3u1fbpfcp-zoom-1.image" alt="mvcexamp" loading="lazy" referrerpolicy="no-referrer">
核心代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">// Controller
- (UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath&#123;
    
    __weak typeof(self) wealSelf = self;
    MVCTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Cell_identifer"];
    if(cell == nil)&#123;
        cell = [[MVCTableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"Cell_identifer"];
    &#125;
    DemoModel *model = self.dataArray[indexPath.row];
    [cell loadDataWithModel:model];
    cell.clickBtn = ^&#123;
        NSLog(@"id===%ld",model.num);
        [wealSelf changeNumWithModel:model];
    &#125;;
    cell.selectionStyle = UITableViewCellSelectionStyleNone;
    return cell;
&#125;
/*
* 用户点击事件通过Block传递过来后，在Controller层处理更新Mdoel以及更新视图的逻辑
*/
- (void)changeNumWithModel:(DemoModel*)model&#123;
    
    model.num++;
    NSIndexPath *path = [NSIndexPath indexPathForRow:model.Id inSection:0];
    [self.mainTabelView reloadRowsAtIndexPaths:@[path] withRowAnimation:UITableViewRowAnimationLeft];
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以看到用户点击事件通过Block传递过来后，在Controller层处理更新Mdoel以及更新视图的逻辑</li>
</ul>
<h3 data-id="heading-5">2.<code>MVP</code>设计模式</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b74184f1aa3f46cda054fd4268f98648~tplv-k3u1fbpfcp-zoom-1.image" alt="MVP" loading="lazy" referrerpolicy="no-referrer">
<code>M</code>: Model 数据层，负责网络数据的处理，数据持久化存储和读取等工作<br>
<code>V</code>: View 视图层，负责呈现从数据层传递的数据渲染工作，以及与用户的交互，这里把Controller层也合并到视图层<br>
<code>P</code>: Presenter层，负责视图需要数据的获取，获取到数据后刷新视图。响应View的事件和作为View的代理。</p>
<p>可以看到 MVP模式跟原始的MVC模式非常相似，完全实现了View与Model层的分离，而且把业务逻辑放在了Presenter层中，视图需要的所有数据都从Presenter获取，而View与 Presenter通过协议进行事件的传递。</p>
<h4 data-id="heading-6">用户的交互逻辑</h4>
<p>用户点击 View(视图) --> 视图响应事件 -->通过代理传递事件到Presenter-->发起网络请求更新Model-->Model处理完数据-->代理或通知给视图(View或是Controller)-->改变视图样式-->完成</p>
<h4 data-id="heading-7">MVP代码示例</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730230047a9342628d703669a3b9ec62~tplv-k3u1fbpfcp-zoom-1.image" alt="项目结构" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//DemoProtocal
import <Foundation/Foundation.h>

@protocol DemoProtocal <NSObject>
@optional
//用户点击按钮 触发事件： UI改变传值到model数据改变  UI --- > Model 点击cell 按钮
-(void)didClickCellAddBtnWithIndexPathRow:(NSInteger)index;
//model数据改变传值到UI界面刷新 Model --- > UI
-(void)reloadUI;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>我们把所有的代理抽象出来，成为一个Protocal文件。这两个方法的作用：</li>
<li><code>-(void)didClickCellAddBtnWithIndexPathRow:(NSInteger)index;</code>:Cell视图调用它去Presenter层实现点击逻辑的处理</li>
<li><code>-(void)reloadUI;</code>: Presenter调用它去更新主视图View或者Controller</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//Presenter.h
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import "DemoProtocal.h"

NS_ASSUME_NONNULL_BEGIN

@interface Presenter : NSObject
@property (nonatomic, strong,readonly) NSMutableArray *dataArray;
@property (nonatomic, weak) id<DemoProtocal>delegate;//协议，去更新主视图UI
// 更新 TableView UI 根据需求
- (void)requestDataAndUpdateUI;
//更新 cell UI
- (void)updateCell:(UITableViewCell*)cell withIndex:(NSInteger)index;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>dataArray </code>: 视图需要的数据源</li>
<li><code>- (void)requestDataAndUpdateUI;</code>:主视图Controller调用，去更新自己的UI</li>
<li><code>- (void)updateCell:(UITableViewCell*)cell withIndex:(NSInteger)index;</code>:更新 Cell的UI</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//Controller 层
- (void)iniData&#123;
    self.presenter = [[Presenter alloc] init];
    self.presenter.delegate = self;
    [self.presenter requestDataAndUpdateUI];
&#125;
...

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section&#123;
    return self.presenter.dataArray.count;
&#125;
- (UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath&#123;
    
    MVPTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Cell_identifer"];
    if(cell == nil)&#123;
        cell = [[MVPTableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"Cell_identifer"];
    &#125;
    //更新cell UI 数据
    [self.presenter updateCell:cell withIndex:indexPath.row];
    cell.selectionStyle = UITableViewCellSelectionStyleNone;
    return cell;
&#125;

#pragma mark - DemoProtocal
//Presenter 的代理回调 数据更新了通知View去更新视图
- (void)reloadUI&#123;
    [self.mainTabelView reloadData];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Controller层初始化Presenter，调用其方法更新自己的UI，可以看到网络数据的获取，处理都在Presenter中，处理完成后通过协议回调给Controller去reload数据</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//Cell
- (void)addBtnDown:(UIButton*)btn&#123;
    NSLog(@"%s",__func__);
    if([self.delegate respondsToSelector:@selector(didClickCellAddBtnWithIndexPathRow:)])&#123;
        [self.delegate didClickCellAddBtnWithIndexPathRow:self.index];
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Cell层点击事件通过协议调用，而这个协议方法的实现是在Presenter中实现的。</li>
</ul>
<blockquote>
<p>MVP模式也有自身的缺点，所有的用户操作和更新UI的回调需要定义，随着交互越来越复杂，这些定义都要有很大一坨代码。逻辑过于复杂的情况下，Present本身也会变得臃肿。所以衍生出了MVVM模式。</p>
</blockquote>
<h3 data-id="heading-8">3.<code>MVVM+RAC</code>设计模式</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e614c58dc450400481e57c4e4a83d6c8~tplv-k3u1fbpfcp-zoom-1.image" alt="MVVM" loading="lazy" referrerpolicy="no-referrer"><br>
<code>M</code>: Model 数据层，负责网络数据的处理，数据持久化存储和读取等工作<br>
<code>V</code>: View 视图层，此时的视图层包括Controller，负责呈现从数据层传递的数据渲染工作，以及与用户的交互<br>
<code>VM</code>:ViewModel层，负责视图需要数据的获取，获取到数据后刷新视图。响应View的事件和作为View的代理等工作。<br>
通过架构图可以看到，MVVM模式跟MVP模式基本类似。主要区别是在MVP基础上加入了双向绑定机制。当被绑定对象某个值的变化时，绑定对象会自动感知，无需被绑定对象主动通知绑定对象。可以使用KVO和RAC实现。我们这里采用了RAC的实现方式。关于RAC如果不熟悉的小伙伴可以点<a href="https://juejin.cn/post/6953808004307222564" target="_blank">这里</a>,我们这篇文章不在涉及。</p>
<h4 data-id="heading-9">MVVM代码示例</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b4e399c71c4dbab31c55bffcd8d20c~tplv-k3u1fbpfcp-zoom-1.image" alt="项目结构" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们这里包括两层视图：主视图Controller以及Cell，分别对应两层ViewModel：ViewModel和CellViewModel</p>
</blockquote>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//ViewModel.h

@interface ViewModel : NSObject
//发送数据请求的Rac，可以去订阅获取 请求结果
@property (nonatomic,strong,readonly) RACCommand *requestCommand;
@property (nonatomic,strong) NSArray *dataArr;//返回子级对象的ViewModel
- (CellViewModel *)itemViewModelForIndex:(NSInteger)index;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>RACCommand *requestCommand</code>:提供供主视图调用的命令，调用它去获取网络数据</li>
<li><code>NSArray *dataArr</code>: 提供供主视图使用的数据源，注意这里不能用NSMutableArray，因为NSMutableArray不支持KVO，不能被RACObserve。</li>
<li><code>- (CellViewModel *)itemViewModelForIndex:(NSInteger)index;</code> 根据Cell的index返回它需要的的ViewModel</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface CellViewModel : NSObject

@property (nonatomic,copy,readonly) NSString *titleStr;

@property (nonatomic,copy,readonly) NSString *numStr;

@property (nonatomic,copy,readonly) RACCommand *addCommand;

- (instancetype)initWithModel:(DemoModel *)model;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>CellViewModel</code>: 暴露出Cell渲染需要的所有数据</li>
<li><code>RACCommand *addCommand;</code>: 按钮点击事件的指令，触发后需要在CellViewModel里面做处理。</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//controller
- (void)iniData&#123;
    self.viewModel = [[ViewModel alloc] init];
    // 发送请求
    RACSignal *signal = [self.viewModel.requestCommand execute:@&#123;@"page":@"1"&#125;];
    [signal subscribeNext:^(id x) &#123;
        NSLog(@"x=======%@",x);
        if([x boolValue] == 1)&#123;//请求成功
            [self.mainTabelView reloadData];
        &#125;
    &#125;];
&#125;
- (UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath&#123;
    
    MVVMTableVIewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Cell_identifer"];
    if(cell == nil)&#123;
        cell = [[MVVMTableVIewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"Cell_identifer"];
    &#125;
    //更新cell UI 数据
    cell.cellViewModel = [self.viewModel itemViewModelForIndex:indexPath.row];
    cell.selectionStyle = UITableViewCellSelectionStyleNone;
        
    return cell;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>iniData</code>:初始化ViewModel，并发送请求命令。这里可以监听这个完成信号，进行刷新视图操作</li>
<li><code>cell.cellViewModel = [self.viewModel itemViewModelForIndex:indexPath.row];</code> 根据主视图的ViewModel去获取Cell的ViewModel，实现cell的数据绑定。</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//TableViewCell

    RAC(self.titleLabel,text) = RACObserve(self, cellViewModel.titleStr);
    RAC(self.numLabel,text) = RACObserve(self, cellViewModel.numStr);

    [[self.addBtn rac_signalForControlEvents:UIControlEventTouchUpInside] subscribeNext:^(id x) &#123;
        NSLog(@">>>>>");
        [self.cellViewModel.addCommand execute:nil];
    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在Cell里面进行与ViewModel的数据绑定，这边有个注意Racobserve左边只有self右边才有viewModel.titleStr这样就避Cell重用的问题。</li>
<li><code>[self.cellViewModel.addCommand execute:nil];</code>:按钮的点击方法触发，事件的处理在CellViewModel中。</li>
</ul>
<h3 data-id="heading-10">总结</h3>
<ul>
<li>经过几十年的发展和演变MVC模式出现了各种各样的变种，并在不同的平台上有着自己的实现。在实际项目开发中，根据具体的业务需求找到适合的架构才是最好的，架构本身并没有好坏之分。</li>
<li>最后对文中的MVC、MVP、MVVM架构的描述也掺杂了作者的主观意见，如果对文中的内容有疑问，欢迎提出不同的意见进行讨论。</li>
<li>本文的Demo已上传<a href="https://github.com/chenXming/MVVMDemo" target="_blank" rel="nofollow noopener noreferrer">作者GitHub</a></li>
</ul></div>  
</div>
            