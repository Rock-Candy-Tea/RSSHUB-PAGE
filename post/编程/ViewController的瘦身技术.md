
---
title: ViewController的瘦身技术
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Sun, 21 Feb 2021 08:19:57 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><p>ViewController中的代码量通常都是很大, 并且其中包含了许多不必要的代码. 所以ViewController中代码的复用率通常都是最低的, 接下来会介绍几种技术对ViewController进行瘦身处理, 让代码变得可以复用, 将代码移动到合适的地方.</p>
<h2 data-id="heading-0">把 Data Source 和其他 Protocols 分离出来</h2>
<p>把UITableViewDataSource的代码提出来放到一个单独的类中, 是为ViewController进行瘦身的一项强大技术.</p>
<p>举个例子, 在项目中会有个<code>PhotoViewController</code>类, 它有以下的一些方法来为tableView提供数据.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"># pragma mark ---

- (Photo*)photoAtIndexPath:(NSIndexPath*)indexPath {
    return photos[(NSUInteger)indexPath.row];
}

- (NSInteger)tableView:(UITableView*)tableView
 numberOfRowsInSection:(NSInteger)section {
    return photos.count;
}

- (UITableViewCell*)tableView:(UITableView*)tableView
        cellForRowAtIndexPath:(NSIndexPath*)indexPath {
    PhotoCell* cell = [tableView dequeueReusableCellWithIdentifier:PhotoCellIdentifier
                                                      forIndexPath:indexPath];
    Photo* photo = [self photoAtIndexPath:indexPath];
    cell.label.text = photo.name;
    return cell;
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到上面的代码都是围绕数组在做事情, 更仔细地说, 是围绕<code>PhotoViewController</code>所管理的photos数组做一些事情. 我们可以将这些与数组相关的代码移动到单独的类中. 然后对于cell的具体内容设置, 我们可以使用代理或者block.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@implementation ArrayDataSource

- (id)itemAtIndexPath:(NSIndexPath*)indexPath {
    return items[(NSUInteger)indexPath.row];
}

- (NSInteger)tableView:(UITableView*)tableView
 numberOfRowsInSection:(NSInteger)section {
    return items.count;
}

- (UITableViewCell*)tableView:(UITableView*)tableView
        cellForRowAtIndexPath:(NSIndexPath*)indexPath {
    id cell = [tableView dequeueReusableCellWithIdentifier:cellIdentifier
                                              forIndexPath:indexPath];
    id item = [self itemAtIndexPath:indexPath];
    configureCellBlock(cell,item);
    return cell;
}

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们将与dataSource都放到了单独的类ArrayDataSource中, 并且让ArrayDataSource遵循UITableViewDataSource协议. 之后我们在ViewController中就可以把UITableViewDataSource所需实现的三个方法去掉, 取而代之的是使用ArrayDataSource作为tableView的datasource. 像下面这样调用:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">void (^configureCell)(PhotoCell*, Photo*) = ^(PhotoCell* cell, Photo* photo) {
   cell.label.text = photo.name;
};
photosArrayDataSource = [[ArrayDataSource alloc] initWithItems:photos
                                                cellIdentifier:PhotoCellIdentifier
                                            configureCellBlock:configureCell];
self.tableView.dataSource = photosArrayDataSource;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到我们只需要简单的把数据传给photosArrayDataSource, 并且将其设置为datasource, 系统就会在合适时机调用数据源方法, 提供数据.</p>
<p>但是上面的代码还存在不足, 可以看到我们在block中设置了cell的内容, 这明显是属于View的逻辑, 不应该放入Controller中, 较好的方法是为cell创建一个分类或者设置一个模型属性. 后者较为常见, 通过调用cell的set方法, 在set方法写入设置cell内容的逻辑, 就可以完成了.</p>
<p>第一种方法是为cell创建一个分类.如下所示:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">#import "PlayerCell+ConfigureForVoice.h"

@implementation PlayerCell (ConfigureForVoice)

- (void)configureForVoice:(NSURL *)voiceUrl Width:(CGFloat)width IndexPath:(NSIndexPath *)indexPath{
    
    self.cellView.playUrl = voiceUrl;
    self.cellView.width = width;
    self.cellView.indexPath = indexPath;
    self.cellView.hidden = NO;
    
}
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就只需要调用cell的分类方法, 在分类中完成内容的设置, 就可以把VIew的逻辑和Controller分开.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">   void(^configureCellBlock)(PlayerCell*, NSURL*, NSIndexPath* ) = ^(PlayerCell *cell, NSURL *url, NSIndexPath *indexPath){

     [cell configureForVoice:url Width:self.tableView.width IndexPath:indexPath];

     cell.cellView.delegate = self;

   };
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过将DataSource的逻辑写入单独的类中, 我们可以让代码在任意ViewController中复用, 并且你还能加入一些额外的方法如<code>tableView:commitEditingStyle:forRowAtIndexPath:</code>, 除此之外你也可以在单独的类中写入UICollectionViewDataSource, 使这个类同时支持两种协议, 使代码得到更好的复用.</p>
<h2 data-id="heading-1">将业务逻辑移到 Model 中</h2>
<p>下面是ViewController中一些代码, 用来查找用户目前的优先事项的列表.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)loadPriorities {
    NSDate* now = [NSDate date];
    NSString* formatString = @"startDate = %@";
    NSPredicate* predicate = [NSPredicate predicateWithFormat:formatString, now, now];
    NSSet* priorities = [self.user.priorities filteredSetUsingPredicate:predicate];
    self.priorities = [priorities allObjects];
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这些逻辑应该是属于Model层面上的, 我们可以为Model创建一个分类, 在分类中实现查找逻辑.</p>
<p>这样ViewController就只需要像下面这样简单的调用, 就可以完成功能.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)loadPriorities {
    self.priorities = [user currentPriorities];
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>User+Extensions.m</code> 中：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (NSArray*)currentPriorities {
    NSDate* now = [NSDate date];
    NSString* formatString = @"startDate = %@";
    NSPredicate* predicate = [NSPredicate predicateWithFormat:formatString, now, now];
    return [[self.priorities filteredSetUsingPredicate:predicate] allObjects];
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>任何像上面这样代码和Model关系紧密并且代码很轻松就可以写入Model中的情况, 我们都可以尝试这么做.</p>
<h2 data-id="heading-2">把网络请求逻辑移到单独的类</h2>
<p>不要在ViewController中请求网络的逻辑, 而是将请求网络逻辑放入单独的类中, 有很多优秀的第三方库比如AFNetWorking和YTKNetWork, 我们只需要简单调用这些类提供的回调(可能是以block形式或者delegate形式), 在成功回调和失败回调中完成对应的逻辑处理. 这样的好处是缓存和出错控制都会在这个类中处理.</p>
<h2 data-id="heading-3">把 View 代码移到 View 层</h2>
<p>不要再ViewController中写入复杂的View逻辑, 我们只需要在控制器中简单调用alloc init方法创建出View, 然后设置成控制器View的subView中. 而那些复杂的View布局, 子View的添加则应直接写到View中, 然后对外提供一些接口给控制器, 在合适的时间通知控制器, 控制器再去做对应的处理. 对于简单的View我们可以使用xib的方式进行创建, 但是记住若View比较复杂最好不要采用这种方法, 不然后期维护更改工作量会特别大.</p>
<h2 data-id="heading-4">创建基类ViewController集成重复代码</h2>
<p>项目中在VIewController中我们经常要写一些重复的代码, 比如设置导航条的标题内容及样式, 向导航栏添加返回按钮等等这些重复操作. 然后我就想到既然这些逻辑所有控制器基本都要实现, 那么为什么不把代码抽取到公共的基类, 然后创建的控制器都继承这个公共基类, 这样就可以使得ViewController变得更加整洁.</p>
<p>如下面我就在基类中写入了返回按钮的代码.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (instancetype)init{
    if (self=[super init]) {
        [self setDefultBackBtn];
       
    }
    return self;
}
- (void)setDefultBackBtn {
    [self backItemWithImage:@"icon_back" highlight:@"icon_back" title:nil];
}
- (void)backItemWithImage:(NSString *)normalImageName
                         highlight:(NSString *)highlighImageName
                            title:(NSString *)title {
    UIButton * leftBtn=[UIButton buttonWithType:UIButtonTypeCustom];
    if (normalImageName) {
        [leftBtn setImage:[UIImage imageNamed:normalImageName] forState:UIControlStateNormal];
    }
    if (highlighImageName) {
        [leftBtn setImage:[UIImage imageNamed:highlighImageName] forState:UIControlStateHighlighted];
    }
    if (title) {
        leftBtn.titleLabel.font=[UIFont systemFontOfSize:18.0f];
        [leftBtn setTitle:title forState:UIControlStateNormal];
        [leftBtn setTitle:title forState:UIControlStateHighlighted];
        [leftBtn setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
        [leftBtn setTitleColor:[UIColor whiteColor] forState:UIControlStateHighlighted];
    }else {
        leftBtn.titleLabel.font=[UIFont systemFontOfSize:18.0f];
        [leftBtn setTitle:@"    " forState:UIControlStateNormal];
        [leftBtn setTitle:@"    " forState:UIControlStateHighlighted];
        [leftBtn setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
        [leftBtn setTitleColor:[UIColor whiteColor] forState:UIControlStateHighlighted];
    }
    
    
    [leftBtn addTarget:self action:@selector(backToLastVC) forControlEvents:UIControlEventTouchUpInside];
    [leftBtn sizeToFit];
    self.navigationItem.leftBarButtonItem=[[UIBarButtonItem alloc]initWithCustomView:leftBtn];
}

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面代码所示, 首先 用init方法时, 就将返回按钮设置到导航栏上, 并且设置一些默认按钮样式以及点击按钮响应的方法, 这样当我们创建一个继承基类控制器的子类控制器时就会默认设置好返回按钮了. 大多数页面都是具有返回按钮的, 但是有时候按钮有些特殊需求或者根本不需要返回按钮. 那么我们只需要在基类中提供一些其他接口就可以适应这些需求. 比如下面:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//调用此方法不使用默认的返回按钮
- (instancetype)initWithDefaultBackBtn:(BOOL)isNeed {
    if (self=[super init]) {
        if (isNeed){
        [self setDefultBackBtn];
        }
    }
    return self;
}
//然后调用此方法设置自定义的返回按钮.
- (void)backItemWithImage:(NSString *)normalImageName
                         highlight:(NSString *)highlighImageName
                            title:(NSString *)title;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只是简单举了一个返回按钮的例子, 但是可以做的远不止于此. 任何ViewController中的公共逻辑, 我们都可以写入到类中.</p>
<h2 data-id="heading-5">通讯</h2>
<p>其他经常在ViewController中发生的事情是与其他ViewController, View, Model进行通讯, 虽然这确实是ViewController应该做的事, 但是我们尽量希望用较少的代码完成.</p>
<p>关于ViewController和Model通讯已经有阐述的很好的技术来完成比如KVO, 但是ViewController之间的消息传递就显的不是那么清晰.</p>
<p>当一个ViewController想把一个状态传递给另外一个ViewController, 就会出现这样不是很清晰的问题. 比较好的做法就是把状态放入到一个单独的对象里, 然后把这个对象传递给其他ViewController, 然后ViewController观察并修改这个状态. 这样做的好处消息传递都在一个地方(被观察的对象)进行, 我们不用再纠结复杂的delegate回调.</p>
<h2 data-id="heading-6">总结</h2>
<p>以上就是一些VIewController瘦身的技术. 他们的核心思想就是把不是ViewController的逻辑放到其他地方, 将控制器的公共逻辑提取出来, 并且使代码逻辑尽量简单. 我们的最终目标:写可维护的代码. 只要把握这些原则, 我们就可以使得笨重的ViewController变得整洁.</p>
<p>参考文章: <a href="https://objccn.io/issue-1-1/" target="_blank" rel="nofollow noopener noreferrer">objccn.io/issue-1-1/</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            