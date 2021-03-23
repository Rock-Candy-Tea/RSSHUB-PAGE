
---
title: '一个iOS流畅性优化工具'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea30fc539ccb4c3d94f2960aec1bb38b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 01 Mar 2021 08:21:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea30fc539ccb4c3d94f2960aec1bb38b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">简介</h3>
<ul>
<li>
<p>LNAsyncKit是一个异步渲染工具，它提供了便捷的方法帮助你将多个元素（Element）异步渲染到一张图片上，让这个过程代替UIKit的视图构建过程，进而优化App性能；Prender提供预加载策略帮助你在Feed流中弥补异步渲染带来的延时；除构建视图外，Transaction提供更优雅的方式让主线程与子线程交互，并能根据机器状态控制并发数和主线程回调时机。</p>
</li>
<li>
<p>LNAsyncKit借(ji)鉴(cheng)了很多YYKit和Texture，如果对它们不是很了解可以戳这个比较详细的文章，这篇文章的作者是YY大神：<a href="https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/" target="_blank" rel="nofollow noopener noreferrer">iOS保持页面流畅的技巧</a>。流畅性优化的思想基本上都如这篇文章所述。</p>
</li>
</ul>
<h3 data-id="heading-1">它可以提供哪些帮助</h3>
<ul>
<li>还没有找到方案优化圆角、边框、渐变的优化方案，LNAsyncKit可以异步解决这些。</li>
<li>Feed流需要预加载策略，LNAsyncKit提供预加载区域计算方案（这个方案也用来预合成）。</li>
<li>提供一种与UIKit十分接近的方式构建需要预合成的图层，让你的复杂图层构建都放在子线程进行，且不会创建那么多UIView。</li>
<li>Demo展示了使用：AFNetworking/SDWebImage/IGListKit/YYModel/MJRefresh + LNAsyncKit搭建feed流的方法。除去LNAsyncKit，前面5个构成的这套体系已经比较完整，Demo中也提供了没有使用LNAsyncKit构建的Feed。因此，需要快速学习如何搭建一套Feed流的初学者可以参考这套三方。</li>
</ul>
<h3 data-id="heading-2"><a href="https://github.com/LevisonNN/LNAsyncKit" target="_blank" rel="nofollow noopener noreferrer">Github链接</a></h3>
<p>你可以直接下载这个链接并运行上面的Demo参考代码实现自己的异步列表，也可以直接使用Cocoapods👇</p>
<pre><code class="copyable">pod 'LNAsyncKit'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">流畅性优化</h3>
<p>网络上已经有了很多流畅性优化的文章，再逐一复述这些优化点意义不大；这个文章是为了表达如何在Feed流中实现那些优化思想，并把这个过程简化；所以，不再赘述这些优化点为什么好、好多少，只谈怎么实现它们；如果对这些优化点有疑问可以参考上面链接的文章，以下这些观点成立：</p>
<ul>
<li>图层少的列表比图层多的列表好。</li>
<li>没有圆角、边框、渐变等复杂图层的比有的好。</li>
<li>图片尺寸和控件尺寸一样大的好。</li>
<li>模型解析放在子线程比放在主线程好。</li>
<li>布局计算放在子线程比放在主线程好。</li>
<li>有预加载比没有预加载好（见仁见智，也有喜欢无预加载列表的）。</li>
<li>Layer比View好（无手势时）。</li>
<li>不透明图层比透明图层好。</li>
</ul>
<p>在业务复杂度不变的前提下让这些优化工作变简单、自由就是LNAsyncKit的目标。</p>
<h3 data-id="heading-4">优化一个Cell</h3>
<p>我们将一个Cell视为Feed流的最小优化单元，以一个Bilibili推荐Feed流中一个常规的Cell为例：</p>
<p><a href="https://imgtu.com/i/yXOQO0" target="_blank" rel="nofollow noopener noreferrer"><img alt="yXOQO0.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea30fc539ccb4c3d94f2960aec1bb38b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a></p>
<p>这样一个小Cell中包含了：封面图、人数图标、人数Label、主播昵称、直播间名、[直播]、直播内容分类、负反馈按钮8个元素；除了这些元素外，还包括封面图底部一个黑色渐变的图层、[直播]的圆角、边框和整个Cell的圆角（好像还有些阴影）；这个小Cell已经包含比较多的小元素了，我们在Demo中尝试复原一下并查看视图层级大致如下：</p>
<p><a href="https://imgtu.com/i/69ZH7q" target="_blank" rel="nofollow noopener noreferrer"><img alt="69ZH7q.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e52dbcdb0094cfca5a3c813c76d5e5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a></p>
<p>具体构建代码这里不赘述了，使用LNAsyncKit可以简化这个Cell为如下这个样子：</p>
<p><a href="https://imgtu.com/i/69ZqA0" target="_blank" rel="nofollow noopener noreferrer"><img alt="69ZqA0.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/019933962abd4aca8180672b0db3fc80~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a></p>
<p>（右下角反馈Bug需要响应事件，通常这种控件会保持独立）</p>
<p>以“直播”标签为例，视图构建方式区别如下：</p>
<p>UIKit:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    self.liveTagLabel.layer.cornerRadius = 3.f;
    self.liveTagLabel.layer.borderColor = [UIColor colorWithRed:239.f/255.f green:91.f/255.f blue:156.f/255.f alpha:1.f].CGColor;
    self.liveTagLabel.layer.borderWidth = 1.f;
    self.liveTagLabel.text = @"直播";
    self.liveTagLabel.font = [UIFont systemFontOfSize:12.f];
    self.liveTagLabel.textColor = [UIColor colorWithRed:239.f/255.f green:91.f/255.f blue:156.f/255.f alpha:1.f];
    self.liveTagLabel.textAlignment = NSTextAlignmentCenter;
    [self.cellContentView addSubview:self.liveTagLabel];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LNAsyncKit:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    LNAsyncTextElement *liveTagElement = [[LNAsyncTextElement alloc] init];
    liveTagElement.cornerRadius = 3.f;
    liveTagElement.borderColor = [UIColor colorWithRed:239.f/255.f green:91.f/255.f blue:156.f/255.f alpha:1.f];
    liveTagElement.borderWidth = 1.f;
    liveTagElement.text = @"直播";
    liveTagElement.font = [UIFont systemFontOfSize:12.f];
    liveTagElement.textColor = [UIColor colorWithRed:239.f/255.f green:91.f/255.f blue:156.f/255.f alpha:1.f];
    liveTagElement.textAligment = NSTextAlignmentCenter;
    [cellContentElement addSubElement:liveTagElement];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过LNAsyncKit渲染出与需要展示视图面积一样大的一张完整图片，复杂渲染逻辑全部被子线程消化，反馈到主线程只表现为一张与目标控件大小一致的图片。</p>
<h3 data-id="heading-5">原理</h3>
<p>与UIKit类似,LNAsyncKit也使用视图树构建最终视图。区别是：</p>
<p>A. Element继承自NSObject，这些Element可以在子线程创建、渲染、销毁。可以将Element理解为“一个需要绘制图层”的描述物，它并不是一个实体，它与UIView/CALayer的区别就好像：UIView是你要买的一件物品；Element则是下单信息，里面包含这件物品的各种描述信息，多大、什么颜色等。</p>
<p>B. 所有的Element都是临时的，这些信息在构建出结果后就会被销毁，你可以在进入子线程之后创建这些Element，在渲染出真正的图片后销毁这些Element，然后在主线程返回需要的图片，像这样：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    dispatch_queue_t queue = dispatch_queue_create(0, 0);
    dispatch_async(queue, ^&#123;
        LNAsyncElement *contentElement = [weakSelf rebuildElements];
        [LNAsyncRenderer traversalElement:contentElement];
        UIImage *image = contentElement.renderResult;
        contentElement.renderResult = nil;
        dispatch_async(dispatch_get_main_queue(), ^&#123;
            weakSelf.imageView.image = image;
        &#125;);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rebuildElement的过程可以构建出很复杂的一棵树，但对主线程来说，这并不会造成问题！不在主线程出现Element也是LNAsyncKit推荐的使用方法(拿到resultImage后，把Element.resultImage置为空)，当然，出现了一般也无所谓，NSObject的消耗相对于UIView来讲是很小的。</p>
<p>C.Element是逐层渲染的：实际上是后续遍历，把A的子Element先渲染出来，然后渲染A，再把A当做一个子节点渲染父节点，LNAsyncRendererTraversalStack就是遍历时使用的栈、LNAsyncRenderer.traversal函数是遍历方法。遍历中自带了环检测，不会渲染重复Element，像这样：</p>
<pre><code class="copyable">    LNAsyncRendererTraversalStack *stack = [[LNAsyncRendererTraversalStack alloc] init];
    [stack pushElements:@[element]];
    
    NSMutableSet <LNAsyncElement *> *repeatDetectMSet = [[NSMutableSet alloc] init];
    while (!stack.isEmpty) &#123;
        LNAsyncElement *topElement = [stack top];
        if (topElement.getSubElements.count > 0 && (![repeatDetectMSet containsObject:topElement])) &#123;
            [repeatDetectMSet addObject:topElement];
            [stack pushElements:topElement.getSubElements.reverseObjectEnumerator.allObjects];
        &#125; else &#123;
            [stack pop];
            [self renderElement:topElement];
            for (LNAsyncElement *subElement in topElement.getSubElements) &#123;
                subElement.renderResult = nil;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LNAsync自带了一些Element：</p>
<ul>
<li>LNAsyncElement: 对应于UIKit的UIView，是其他Element的基类，包含了背景色、frame、和常用的边界、圆角等属性。</li>
<li>LNASyncImageElement: 对应于UIImageView，渲染一张图片、提供三种填充方式。</li>
<li>LNAsyncTextElement: 对应于UILabel，渲染一段文字，提供常规文字属性、支持折行。</li>
<li>LNAsyncLinerGradientElement: 对应于CAGradientLayer，渲染一段渐变色。</li>
</ul>
<p>自定义Element：</p>
<p>除原生Element外，我们也推荐封装自己的Element，例如：一个AvatarElement，可以将用户头像、VIP标识、头像边框等修饰物渲染在一起，重写- (void)renderSelfWithContext:(CGContextRef)context，在这个方法中分别绘制这三个元素。</p>
<p>自定义Element的意义在于，所有自定义过的Element都是可复用、可组合的，这样方便保持整个App风格统一，也会适当减少开发成本。</p>
<h3 data-id="heading-6">Feed流</h3>
<p>上面我们已经介绍过单个Cell、单张图片如何异步渲染以优化性能，但性能问题往往不是单张图片所能引发，LNAsyncKit更倾向于性能敏感的场景：Feed流；渲染Feed流相比渲染单个视图需要考虑的事情要多一些：Cell复用、渲染好的图片缓存、多张图片下载和结果合并等问题；除此之外，也考虑使用预加载、预渲染功能来优化用户体验。</p>
<h4 data-id="heading-7">使用到的三方库：</h4>
<ul>
<li>AFNetworking 网络</li>
<li>IGListKit Feed流框架，可以拆分各个模块业务</li>
<li>SDWebImage 图片下载</li>
<li>YYModel 字典转模型</li>
<li>MJRefresh 上拉/下拉刷新组件</li>
<li>一位大佬写的<a href="https://www.kancloud.cn/lizhixuan/free_api/1159536" target="_blank" rel="nofollow noopener noreferrer">免费API</a> ，虽然我不认识这位大佬，但这些接口确实非常方便，在这里面朝空气感谢一下~</li>
</ul>
<p>这些都是非常成熟的三方框架，直接拿来用会减少不少开发时间；这里主要是介绍如何将LNAsyncKit融进这个体系中去。Demo中已经提供了默认的Feed流和异步的Feed流代码，如果遇到了一些奇怪的Bug可以参考Demo中的实现，目前这两个Demo都可以正常运行。</p>
<ul>
<li>默认Demo：我们用此Demo展示一个常规Feed流实现过程，没有使用任何修饰手法或设计思想，可以理解为实现一个Feed流所需要做的最少工作。</li>
<li>异步Demo：我们用此Demo将使用LNAsyncKit实现Feed流时与通常情况下的实现的进行对比，了解从普通Feed转异步Feed的修改点和差异之处。</li>
</ul>
<h4 data-id="heading-8">默认Feed流实现：</h4>
<ol>
<li>ViewDidLoad中使用AFNetworking请求一页数据，使用YYModel解析成Model类型数据，赋值给VC。</li>
<li>VC调用CollectionView/IGList刷新列表，将Model赋值到Cell内部。</li>
<li>Cell内部赋值懒加载的Label、ImageView调用sd_setImage下载图片展示。</li>
</ol>
<h4 data-id="heading-9">异步Feed流的优化：</h4>
<h5 data-id="heading-10">1.图片下载放在Model中进行</h5>
<p>A.因为异步Feed不仅仅需要下载图片，也需要将多个原始图片进行预合成，所以这个过程在Model中进行可以保证不会因Cell复用问题导致同一时间合成多次，如果你在Cell中异步进行图层合成，那可能每次赋值Model都会合成一次，但在Model中合成后可以一直存放在Model中（Model只持有弱引用，存在全局的NSCache中）。</p>
<p>B.考虑预加载，我们认为图层的预加载和预合成是两种优先级的事情，通常距离屏幕焦点区域较远的区域只需要进行图片预下载，而距离较近的地方则需要预合成，不论是哪种方式，Cell通常只会在展示在屏幕上的时间点附近才能拿到，如果图片下载放在Cell中进行，是很难实现“预”的。</p>
<p>MVC中Model的职责之一是提供View展示需要的数据，所以在Model中下载图片并非错误或不恰当的做法。</p>
<h5 data-id="heading-11">2.模型解析和布局计算视为网络请求的一部分</h5>
<p>通常，在使用AFNetworking进行网络请求时，我们通常在成功回调中进行模型解析和列表刷新，列表刷新时走CollectionView的dataSource协议计算布局。</p>
<p>异步列表不推荐这样做：模型解析的过程没有想象中的那样简单，通常进行模型解析时需要逐层遍历Dictionary，然后创建大量Model和子Model，虽然单个NSObject开销不大，但列表视图的模型总是堆积起来的，创建如此多的对象也是个不小的开销。</p>
<p>计算布局的耗时是公认的，所以一般表视图优化都推荐缓存行高，但即便缓存行高，第一次在主线程中的计算也是有一定耗时的。</p>
<p>我们推荐在AFNetworking回调中异步进行模型解析和布局计算，将这两个操作视为网络请求的一部分，这并不会对网络请求的整体响应时间有较大的影响，因为网络回调时间单位通常要比屏幕刷新时间单位高出一个数量级。况且，预加载技术完全可以弥补这段小延时。</p>
<p>在请求回调中赋值给Model的LayoutObj就是对这个过程的封装，像这样：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)transferFeedData:(NSDictionary *)dic comletion:(DemoFeedNetworkCompletionBlock)completion
&#123;
    LNAsyncTransaction *transaction = [[LNAsyncTransaction alloc] init];
    
    [transaction addOperationWithBlock:^id _Nullable&#123;
        DemoFeedModel *feedModel = [DemoFeedModel yy_modelWithDictionary:dic];
        for (DemoFeedItemModel *item in feedModel.result) &#123;
            DemoAsyncFeedDisplayLayoutObjInput *layoutInput = [[DemoAsyncFeedDisplayLayoutObjInput alloc] init];
            layoutInput.contextString = item.title;
            layoutInput.hwScale = 0.3f + ((random()%100)/100.f)*0.5f; 
            DemoAsyncFeedDisplayLayoutObj *layoutObj = [[DemoAsyncFeedDisplayLayoutObj alloc] initWithInput:layoutInput];
            item.layoutObj = layoutObj;
        &#125;
        return feedModel;
    &#125; priority:1 queue:_transferQueue completion:^(id  _Nullable value, BOOL canceled) &#123;
        if (completion) &#123;
            completion(YES, value, nil);
        &#125;
    &#125;];
    
    [transaction commit];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">3.在Model中布局</h5>
<p>这听起来有点诡异，在Model中下载图片也就算了，为什么视图操作也在Model中进行？</p>
<p>我们已经解释了Element的职责，它只是负责描述的类。使用element构建视图的过程就是：Model想好要怎么构建（Element），把想法交付LNAsyncRenderer，renderer交付我们image，Model把image反回给View显示出来。就像我们在开始的时候讲述的那样。</p>
<h5 data-id="heading-13">4.预加载</h5>
<p>预加载主要内容包括两个方面：预加载下一页信息和预加载图片。这里提到的预加载主要是指预加载图片:</p>
<p>根据上面我们提到了图片加载都是在Model中进行的，所以，每个Model都需要一个必要的参数来标记自身所持有的资源已经到了那种紧急的程度了，如果距离当前用户焦点还很远，说明自己的资源目前不是很紧急，可以先静观其变；如果距离用户焦点有点近了，说明自己可能需要开始考虑先把图片下载下来；如果距离用户焦点已经相当近了，就要立刻开始准备把已有资源预合成了。类似这样：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)setStatus:(DemoFeedItemModelStatus)status
&#123;
    if (status > _status) &#123;
        _status = status;
    &#125;
    [self checkCurrentStatus];
&#125;

- (void)checkCurrentStatus
&#123;
    if (self.status >= DemoFeedItemModelStatusPreload) &#123;
        //需要预加载图片
        [self preloadImage];
    &#125;
    
    if (self.status >= DemoFeedItemModelStatusDisplay) &#123;
         //需要渲染视图
         [self renderView];
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LNAsyncCollectionViewPrender提供了一套资源紧急程度标记策略，将距离当前屏幕中心较远的资源标记为不紧急，较近的资源标记为紧急，Model受紧急程度标记影响自主进行预加载或预渲染。</p>
<p>这套智能预加载机制来自于Texture，非常的实用，我将它修改为Objective-C实现，并做了简化处理。你甚至可以参照这个区间计算思路制作一个滚动列表曝光打点类，来计算那些更符合用户视距的曝光区间，而不是仅仅简单依赖cell/View的生命周期，说到这不得不提一嘴：我曾经见过一个埋点系统迭代了两年多依然没啥卵用。</p>
<h5 data-id="heading-14">5.图片一致性校验</h5>
<p>异步Cell渲染图片回调设置图片需要进行渲染的模型与当前模型是否一致的校验，复用可能会导致一个Cell先后被设置两个Model，这样两个Model在异步渲染结束后都可能通知Cell刷新数据，所以需要一致性校验。同步不存在这个问题，后来的内容总是会覆盖掉先来的图片。像这样：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    NSObject *model = self.model;
    __weak DemoAsyncFeedCell *weakSelf = self;
    [self.model demoAsyncFeedItemLoadRenderImage:^(BOOL isCanceled, UIImage * _Nullable resultImage) &#123;
        if (!isCanceled && resultImage && model == weakSelf.model) &#123;
            weakSelf.contentView.layer.contents = (__bridge id)resultImage.CGImage;
        &#125;
    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">6.渲染缓存</h5>
<p>与SDWebImage下载的原生Image不同，渲染后的图片存储在额外的一个渲染缓存中，Model弱引用持有，缓存内部使用LRU管理；不能使用Model强引用，因为有些Feed流是常驻的，我们不希望内存浪费在不是主要消费场景的常驻页面中。LNAsyncCache是统一的存放的地方，你可以在渲染成功后把图片存在这里，使用弱指针指向它，如果被删除了，就重新渲染、存储。</p>
<h5 data-id="heading-16">7.减少渲染次数</h5>
<p>SD下载图片时附带AvoidDecode参数，因为合成过程会将Image渲染到一块内存中，这个过程本身就包含了解码，且也是在子线程中进行；使用这个参数可以减少图片刚下载好时的那次渲染。像这样：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">[[SDWebImageManager sharedManager] loadImageWithURL:[NSURL URLWithString:weakSelf.image]
                                            options:SDWebImageAvoidDecodeImage 
                                           progress:nil 
                                          completed:nil];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">总结</h3>
<p>LNAsyncKit优化的内容就如上所述：</p>
<ul>
<li>从主线程的角度来看：除了刷新CollectionView和计算预加载区域外基本上没有耗时工作，布局计算和模型解析转移到了子线程统一进行，Element创建销毁操作主线程基本上没有感知。</li>
<li>从CPU的角度来看：圆角、边框、渐变等工作都在图层合成的时候异步消化了，返回的图片大小和Layer控件大小也是一致的，图层的复杂层级也被子线程异步消化。</li>
<li>从子线程角度看：子线程有很多。</li>
</ul>
<p>写异步Feed流比普通Feed流难度要稍微大一些，平均开发的时间成本也会有所上升；从效率上来讲，每个需求的开发效率确实降低了，但这将会省去在未来单独成立一个性能优化小组进行优化的效率要高得多。平台类型的开发人员往往没有业务开发对业务更熟悉，因此需要频繁交流确认优化点、改动范围、影响等等。而且，有时遇到优化点时业务受限，可能不敢大刀阔斧地纠正，导致优化后的结果和优化前对比并不明显。LNAsyncKit让业务线从一开始做需求时就考虑到优化内容，从而省去了专项优化的时间。当然，如果App整体不考虑性能问题，选择正常的开发方式就好。</p>
<h3 data-id="heading-18">杂谈</h3>
<p>iPhone手机硬件越来越强，常规业务不进行优化一般也能达到流畅性标准，端内的卡顿只要不是特别严重产品经理通常也都能接受；我在需求中使用了类似的方式进行性能优化，开发时间确实很紧。当然，如果你的公司只考虑需求产出，他们通常不会给你这些时间，你可以在自己的编码追求和实际情况之间决定是否要额外做这些事。</p>
<p>LNAsyncKit可以直接使用，也可以将它当做你更深层次了解性能优化、Texture的垫脚石；总之，它能起到任何帮助，我都将十分荣幸。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            