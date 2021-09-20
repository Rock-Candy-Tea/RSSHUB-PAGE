
---
title: '_iOS_ MVC、MVP、MVVM & ReMVVM'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/5219632-ccc19949144ad931.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/5219632-ccc19949144ad931.png'
---

<div>   
<h4>※ MVC -> MVP -> MVVM</h4>
<p>这部分可能会从MVC->MVP->MVVM都看看，看到几篇不错的文章欢迎大家看一下：<br>
<a href="https://www.jianshu.com/p/52ab0373a1ed" target="_blank">https://www.jianshu.com/p/52ab0373a1ed</a> & <a href="https://www.jianshu.com/p/121ccf669029" target="_blank">https://www.jianshu.com/p/121ccf669029</a> &<br>
<a href="https://www.jianshu.com/p/eedbc820d40a" target="_blank">https://www.jianshu.com/p/eedbc820d40a</a> （强推）&<br>
<a href="https://www.jianshu.com/p/2ad25e2769b5" target="_blank">https://www.jianshu.com/p/2ad25e2769b5</a></p>
<p>这段儿主要也是前几天我们也讨论了一下MVC以及MVP，就顺便学习一下，主要是借鉴强推那一篇写的真的挺好的~</p>
<h6>传统MVC</h6>
<blockquote>
<p>MVC最早存在于桌面程序中的, M是指业务数据, V是指用户界面, C则是控制器.</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="229"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-ccc19949144ad931.png" data-original-width="600" data-original-height="229" data-original-format="image/png" data-original-filesize="63352" src="https://upload-images.jianshu.io/upload_images/5219632-ccc19949144ad931.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">传统MVC</div>
</div>
<p>传统MVC就是View将用户操作给Controller，Controller去干活更新model，model只要变了，由于View给model设置了KVO之类的监听，类似当model的username变了View就会自动把自己的显示用户名的label更新一下。所以在业务场景切换时，通常只需要替换相应的C，复用已有的M和V便可快速搭建新的业务场景。</p>
<p>这种情况MVC三者之间都是可以互相影响通信的，也是任两者之间有引用持有关系的，这大大降低了可重用性：</p>
<ul>
<li>view强耦合了model：那么如果我的view正好有其他model也可以用，难道要再让这个view监听别的model数据改变么？</li>
<li>无法单元测试：如果我想单测view还必须把业务model啥的也建一个，两两耦合严重</li>
</ul>
<blockquote>
<p>我们在代码中经常会直接<code>cell.model = model</code> 其实就是让cell强依赖了model，导致view无法很方便的在其他业务场景被复用。</p>
</blockquote>
<hr>
<h6>苹果的MVC</h6>
<p>iOS里面的MVC没有让M和V强烈互相依赖，而是让controller去对他们两个做控制，无论是model变化还是view触发了action都是通知Controller，然后controller去更新V或者M。</p>
<p><strong>也就是之前可能我们会写<code>cell.model = model</code>，但是如果让C去更新V，cell只要把自己的各个UI组件暴露出来，controller会根据model给cell设置对应的<code>label.text</code>这种。</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="231"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-952c3274dd057dfd.png" data-original-width="600" data-original-height="231" data-original-format="image/png" data-original-filesize="53343" src="https://upload-images.jianshu.io/upload_images/5219632-952c3274dd057dfd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">苹果的MVC</div>
</div>
<p>在iOS里面MVC的实现方式很难做到如上所述的那样，因为由于Apple的规范，一个界面的呈现都需要构建一个view controller，而每个view controller都带有一个根view，这就导致C和V紧密耦合在一起构成了iOS里面的C层，这明显违背了MVC的初衷。</p>
<p>所以我们的view controller经常耦合了自己的view，并且有大量的处理V和M的操作更新的逻辑，非常庞大，于是有了<code>Massive View Controller（大量的视图控制器）</code>的爱称。</p>
<p>苹果官方对于ViewController的解释是酱紫的：<br>
<code>One can merge the MVC roles played by an object, making an object, for example, fulfill both the controller and view roles—in which case, it would be called a view controller. In the same way, you can also have model-controller objects. For some applications, combining roles like this is an acceptable design.</code></p>
<p><code>A model controller is a controller that concerns itself mostly with the model layer. It “owns” the model; its primary responsibilities are to manage the model and communicate with view objects.</code></p>
<p><code>A view controller is a controller that concerns itself mostly with the view layer. It “owns” the interface (the views); its primary responsibilities are to manage the interface and communicate with the model.</code></p>
<p>ViewController 没办法归类到MVC的任何一层，直到看到了apple文档的那段话，才知道VC原来是个组合体。</p>
<p>所以其实VC主要还是去管理自己的view以及和model沟通，而model的管理可以由<code>model controller</code>做。对于简单界面来说，view controller结构确实可以提高开发效率，但是一旦需要构建复杂界面，那么view controller很容易就会出现代码膨胀，逻辑满天飞的问题。</p>
<p>比如不可以把本来view层的代码都堆到了VC、在VC里面构建view、view的显示逻辑，甚至在VC里面发起网络请求。</p>
<p>所以苹果的MVC里面各个角色的责任是啥呢：</p>
<pre><code>* controller层（VC）：
生成view，然后组装view
响应View的事件和作为view的代理
调用model的数据获取接口，拿到返回数据，处理加工，渲染到view显示
处理view的生命周期（不要自己去请求接口）
处理界面之间的跳转


* model层：
业务逻辑封装
提供数据接口给controller使用
数据持久化存储和读取
作为数据模型存储数据


* view层：
界面元素搭建，动画效果，数据展示，
接受用户操作并反馈视觉效果


PS:
model层的业务逻辑一般都是和后台数据交互的逻辑，还有一些抽象的业务逻辑，比如格式化日期字符串为NSDateFormatter类型等
</code></pre>
<p>这里需要注意的是，model层有个职责是<code>提供数据接口给controller使用</code>，好像和我们以为的只有数据几个属性是不一样的，这是为啥子嘞？（可参考：<a href="https://www.jianshu.com/p/33c7e2f3a613" target="_blank">https://www.jianshu.com/p/33c7e2f3a613</a>）其实这里主要是说model可以有业务逻辑，这一点我觉得每个人的理解和实现是不一样的，因为如果耦合了业务逻辑，其实当业务变化的时候，你要去改model而不是controller，即使你底层model的数据结构并没有变化。所以这里仁者见仁叭。</p>
<p><strong>M的正确定义是业务模型。也就是你所有业务数据和业务实现逻辑都应该定义在M层里面，而且业务逻辑的实现和定义应该和具体的界面无关，也就是和视图以及控制之间没有任何的关系，它是可以独立存在的。Controller负责调用模型，而Model则将处理结果发送通知给Controller，Controller再通知View刷新。因此我们不能将M简单的理解为一个个干巴巴的只有属性而没有方法的数据模型。</strong></p>
<p>定义的M层中的代码应该和V层和C层完全无关的，也就是M层的对象是不需要依赖任何C层和V层的对象而独立存在的。</p>
<p><strong>整个框架的设计最优结构是V层不依赖C层而独立存在，M层不依赖C层和V层独立存在，C层负责关联二者，V层只负责展示。</strong></p>
<p>M层持有数据和业务的具体实现，而C层则处理事件响应以及业务的调用以及通知界面更新。三者之间一定要明确的定义为单向依赖，而不应该出现双向依赖。</p>
<p>M层要完成对业务逻辑实现的封装，一般业务逻辑最多的是涉及到客户端和服务器之间的业务交互。</p>
<p><strong>M层里面要完成对使用的网络协议(HTTP, TCP，其他)、和服务器之间交互的数据格式（XML, JSON,其他)、本地缓存和数据库存储（COREDATA, SQLITE,其他)等所有业务细节的封装，而且这些东西都不能暴露给C层。</strong></p>
<p>所有供C层调用的都是M层里面一个个业务类所提供的成员方法来实现。也就是说C层是不需要知道也不应该知道和客户端和服务器通信所使用的任何协议，以及数据报文格式，以及存储方面的内容。这样的好处是客户端和服务器之间的通信协议，数据格式，以及本地存储的变更都不会影响任何的应用整体框架，因为提供给C层的接口不变，只需要升级和更新M层的代码就可以了。比如说我们想将网络请求库从ASI换成AFN就只要在M层变化就可以了，整个C层和V层的代码不变。</p>
<hr>
<p>即使是小的view也可以有自己的MVC，但不是是每个view都要这么做哈，类似强推那篇里面的几个tableview都是有各自的C负责delegate和DataSource，把这个事儿从总的view controller里面解耦了，view controller只要创建table，给他绑定它自己的C就可以了~</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="486"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-573939105f7b7bca.png" data-original-width="1200" data-original-height="486" data-original-format="image/png" data-original-filesize="238377" src="https://upload-images.jianshu.io/upload_images/5219632-573939105f7b7bca.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">MVC分层实例</div>
</div>
<p>如果view controller需要调用网络接口，那么view controller是通过下面的C去调用的，也就是各个part的网络请求是写在自己的Controller里面的。而V的设置例如cell之类的仍旧是放在C里面，不会直接把M给C，复用更好一点。</p>
<hr>
<ul>
<li>MVC到这就说的差不多了, 对比之前错误的MVC方式（把M给V）, 我们看看解决了哪些问题:</li>
</ul>
<ol>
<li><p>代码复用: 三个小模块的V(cell/userInfoView)对外只暴露Set方法, 对M甚至C都是隔离状态, 复用完全没有问题. 三个大模块的MVC也可以用于快速构建相似的业务场景(大模块的复用比小模块会差一些, 下文我会说明).</p></li>
<li><p>代码臃肿: 因为Scene大部分的逻辑和布局都转移到了相应的MVC中, 我们仅仅是拼装MVC的便构建了两个不同的业务场景, 每个业务场景都能正常的进行相应的数据展示, 也有相应的逻辑交互, 而完成这些东西, 加空格也就100行代码左右(当然, 这里我忽略了一下Scene的布局代码).</p></li>
<li><p>易拓展性: 无论产品未来想加回收站还是防御塔, 我需要的只是新建相应的MVC模块, 加到对应的Scene即可.</p></li>
<li><p>可维护性: 各个模块间职责分离, 哪里出错改哪里, 完全不影响其他模块. 另外, 各个模块的代码其实并不算多, 哪一天即使写代码的人离职了, 接手的人根据错误提示也能快速定位出错模块.</p></li>
<li><p>易测试性: 很遗憾, 业务的初始化依然绑定在Scene的生命周期中, 而有些逻辑也仍然需要UI的点击事件触发, 我们依然只能Command+R, 点点点...</p></li>
</ol>
<ul>
<li>MVC的缺点<br>
可以看到, 即使是标准的MVC架构也并非完美, 仍然有部分问题难以解决, 那么MVC的缺点何在? 总结如下:</li>
</ul>
<ol>
<li><p>过度的注重隔离: 这个其实MV(x)系列都有这缺点, 为了实现V层的完全隔离, V对外只暴露Set方法, 一般情况下没什么问题, 但是当需要设置的属性很多时, 大量重复的Set方法写起来还是很累人的.</p></li>
<li><p>业务逻辑和业务展示强耦合: 可以看到, 有些业务逻辑(页面跳转/点赞/分享...)是直接散落在V层的, 这意味着我们在测试这些逻辑时, 必须首先生成对应的V, 然后才能进行测试. 显然, 这是不合理的. 因为业务逻辑最终改变的是数据M, 我们的关注点应该在M上, 而不是展示M的V.</p></li>
</ol>
<hr>
<h6>MVP</h6>
<blockquote>
<p>MVC的缺点在于并没有区分业务逻辑和业务展示，这对单元测试很不友好。</p>
<p>controller要负责view还要负责model，而MVP针对以上缺点做了优化，它将业务逻辑和业务展示也做了一层隔离，对应的就变成了MVCP。M和V功能不变, 原来的C现在只负责布局（也就可以说VC就是V，因为C就是布局和View类似了）, 而所有的逻辑全都转移到了P层。这样就很容易测试逻辑了。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="244"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-82cb601180ca2ee7.png" data-original-width="800" data-original-height="244" data-original-format="image/png" data-original-filesize="81206" src="https://upload-images.jianshu.io/upload_images/5219632-82cb601180ca2ee7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">MVP</div>
</div>
<p>是不是看起来很苹果的MVC？但实际上P已经脱离了ViewController了，它单独就是业务逻辑，可以复用的~ 而真正的VC已经和view组合成为仅做视图管理的部分了。</p>
<pre><code>* VC层
view的布局和组装
view的生命周期控制
通知各个P层去获取数据然后渲染到view上面展示

* Controller层
生成view，实现view的代理和数据源
绑定view和presenter
调用presenter执行业务逻辑

* Model层
和MVC的model层类似

* View层
监听P层的数据更新通知, 刷新页面展示.（MVC里由C层负责）
在点击事件触发时, 调用P层的对应方法, 并对方法执行结果进行展示.（MVC里由C层负责）
界面元素布局和动画
反馈用户操作

* Presenter层职责
实现view的事件处理逻辑，暴露相应的接口给view的事件调用
调用model的接口获取数据，然后加工数据，封装成view可以直接用来显示的数据和状态
处理界面之间的跳转（这个根据实际情况来确定放在P还是C）
</code></pre>
<p>View层现在还要直接调用P的一些方法以及监听P的变化了，主要是因为业务逻辑从C转移到了P，那么view的事件响应和状态变化肯定就依赖P来实现了。</p>
<p>这里又有两种不同的实现方式：</p>
<ol>
<li><p>让P持有V，P通过V的暴露接口改变V的显示数据和状态，P通过V的事件回调来执行自身的业务逻辑<br>
（保持了view的纯粹，但是却导致了P耦合了V，这样业务逻辑和业务展示有糅合到了一起，和上面的MVC一样了。）</p></li>
<li><p>让V持有P，V通过P的代理回调来改变自身的显示数据和状态，V直接调用P的接口来执行事件响应对应的业务逻辑【preferred】<br>
（保证了P的纯粹，让P只做业务逻辑，至于业务逻辑引发的数据显示的变化，让view实现对应的代理事件来实现即可。这增加了view的复杂和view对于P的耦合。如果是一个view对应多个presenter，那么可以考虑把presenter暴露的方法和属性抽象成protocol。让view依赖抽象而不是具体实现。）</p></li>
</ol>
<blockquote>
<p>View is more loosely coupled to the model. The presenter is responsible for binding the model to the view.</p>
</blockquote>
<hr>
<p>下面看一个对比的例子~</p>
<ul>
<li>MVP点赞代码</li>
</ul>
<pre><code>blogViewController.m

//点赞事件
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath &#123;
    
    BlogViewCell *cell = [tableView dequeueReusableCellWithIdentifier:ReuseIdentifier];
    cell.presenter = self.presenter.allDatas[indexPath.row];//PV绑定
    
    __weak typeof(cell) weakCell = cell;
    [cell setDidLikeHandler:^&#123;
        [weakCell.presenter likeBlogWithCompletionHandler:^(NSError *error, id result) &#123;
            !error ?: [weakCell showToastWithText:error.domain];
        &#125;];
    &#125;];
    return cell;
&#125;


==========================================
BlogCellPresenter.m

- (void)likeBlogWithCompletionHandler:(NetworkCompletionHandler)completionHandler &#123;
    
    if (self.blog.isLiked) &#123;
        !completionHandler ?: completionHandler([NSError errorWithDomain:@"你已经赞过了哦~" code:123 userInfo:nil], nil);
    &#125; else &#123;
        
        BOOL response = [self.view respondsToSelector:@selector(blogPresenterDidUpdateLikeState:)];
        
        self.blog.isLiked = YES;
        self.blog.likeCount += 1;
        !response ?: [self.view blogPresenterDidUpdateLikeState:self];
        [[UserAPIManager new] likeBlogWithBlogId:self.blog.blogId completionHandler:^(NSError *error, id result) &#123;
            
            if (error) &#123;
                
                self.blog.isLiked = NO;
                self.blog.likeCount -= 1;
                !response ?: [self.view blogPresenterDidUpdateLikeState:self];
            &#125;
            
            !completionHandler ?: completionHandler(error, result);
        &#125;];
    &#125;
&#125;

==========================================
BlogViewCell.m

#pragma mark - BlogCellPresenterCallBack

- (void)blogPresenterDidUpdateLikeState:(BlogCellPresenter *)presenter &#123;
    
    [self.likeButton setTitle:presenter.blogLikeCountText forState:UIControlStateNormal];
    [self.likeButton setTitleColor:presenter.isLiked ? [UIColor redColor] : [UIColor blackColor] forState:UIControlStateNormal];
&#125;

- (void)blogPresenterDidUpdateShareState:(BlogCellPresenter *)presenter &#123;
    [self.shareButton setTitle:presenter.blogShareCountText forState:UIControlStateNormal];
&#125;


#pragma mark - Action

- (IBAction)onClickLikeButton:(UIButton *)sender &#123;
    !self.didLikeHandler ?: self.didLikeHandler();
&#125;

#pragma mark - Setter

- (void)setPresenter:(BlogCellPresenter *)presenter &#123;
    _presenter = presenter;
    
    presenter.view = self;
    self.titleLabel.text = presenter.blogTitleText;
    self.summaryLabel.text = presenter.blogSummaryText;
    self.likeButton.selected = presenter.isLiked;
    [self.likeButton setTitle:presenter.blogLikeCountText forState:UIControlStateNormal];
    [self.shareButton setTitle:presenter.blogShareCountText forState:UIControlStateNormal];
&#125;
</code></pre>
<ul>
<li>MVC的点赞功能</li>
</ul>
<pre><code>blogViewController.m

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath &#123;
    
    BlogCellHelper *cellHelper = self.blogs[indexPath.row];
    BlogTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:ReuseIdentifier];
    cell.title = cellHelper.blogTitleText;
    cell.summary = cellHelper.blogSummaryText;
    cell.likeState = cellHelper.isLiked;
    cell.likeCountText = cellHelper.blogLikeCountText;
    cell.shareCountText = cellHelper.blogShareCountText;
    
    //点赞的业务逻辑
    __weak typeof(cell) weakCell = cell;
    [cell setDidLikeHandler:^&#123;
        if (cellHelper.blog.isLiked) &#123;
            [self.tableView showToastWithText:@"你已经赞过它了~"];
        &#125; else &#123;
            [[UserAPIManager new] likeBlogWithBlogId:cellHelper.blog.blogId completionHandler:^(NSError *error, id result) &#123;
                if (error) &#123;
                    [self.tableView showToastWithText:error.domain];
                &#125; else &#123;
                    cellHelper.blog.likeCount += 1;
                    cellHelper.blog.isLiked = YES;
                    //点赞的业务展示
                    weakCell.likeState = cellHelper.blog.isLiked;
                    weakCell.likeCountText = cellHelper.blogTitleText;
                &#125;
            &#125;];
        &#125;
    &#125;];
    return cell;
&#125;


===========================================
BlogViewCell.m

- (IBAction)onClickLikeButton:(UIButton *)sender &#123;
    !self.didLikeHandler ?: self.didLikeHandler();
&#125;

#pragma mark - Interface

- (void)setTitle:(NSString *)title &#123;
    self.titleLabel.text = title;
&#125;

- (void)setSummary:(NSString *)summary &#123;
    self.summaryLabel.text = summary;
&#125;

- (void)setLikeState:(BOOL)isLiked &#123;
    [self.likeButton setTitleColor:isLiked ? [UIColor redColor] : [UIColor blackColor] forState:UIControlStateNormal];
&#125;

- (void)setLikeCountText:(NSString *)likeCountText &#123;
    [self.likeButton setTitle:likeCountText forState:UIControlStateNormal];
&#125;

- (void)setShareCountText:(NSString *)shareCountText &#123;
    [self.shareButton setTitle:shareCountText forState:UIControlStateNormal];
&#125;
</code></pre>
<p>Cell的展示我们替换了原来大量的Set方法，让Cell自己根据绑定的CellPresenter做展示。毕竟现在逻辑都移到了P层，V层要做相应的交互也必须依赖对应的P层命令，<strong>好在V和M仍然是隔离的，只是和P耦合了，P层是可以随意替换的，M显然不行，这是一种折中。</strong></p>
<p>下面是MVC下点赞的逻辑：</p>
<pre><code>//点赞的业务逻辑
    __weak typeof(cell) weakCell = cell;
    [cell setDidLikeHandler:^&#123;
        if (cellHelper.blog.isLiked) &#123;
            [self.tableView showToastWithText:@"你已经赞过它了~"];
        &#125; else &#123;
            [[UserAPIManager new] likeBlogWithBlogId:cellHelper.blog.blogId completionHandler:^(NSError *error, id result) &#123;
                if (error) &#123;
                    [self.tableView showToastWithText:error.domain];
                &#125; else &#123;
                    cellHelper.blog.likeCount += 1;
                    cellHelper.blog.isLiked = YES;
                    //点赞的业务展示
                    weakCell.likeState = cellHelper.blog.isLiked;
                    weakCell.likeCountText = cellHelper.blogTitleText;
                &#125;
            &#125;];
        &#125;
    &#125;];
</code></pre>
<p>可以看到业务逻辑（改变model数据）和业务展示（改变cell的数据）糅杂在一起，<strong>如果我要测试点赞这个业务逻辑，那么就必须生成cell，然后点击cell的按钮，去触发点赞的业务逻辑才可以测试</strong></p>
<p>再看看MVP下的点赞逻辑的实现</p>
<pre><code>业务逻辑：
BlogCellPresenter.m

- (void)likeBlogWithCompletionHandler:(NetworkCompletionHandler)completionHandler &#123;
    
    if (self.blog.isLiked) &#123;
        !completionHandler ?: completionHandler([NSError errorWithDomain:@"你已经赞过了哦~" code:123 userInfo:nil], nil);
    &#125; else &#123;
        
        BOOL response = [self.view respondsToSelector:@selector(blogPresenterDidUpdateLikeState:)];
        
        self.blog.isLiked = YES;
        self.blog.likeCount += 1;
        !response ?: [self.view blogPresenterDidUpdateLikeState:self];
        [[UserAPIManager new] likeBlogWithBlogId:self.blog.blogId completionHandler:^(NSError *error, id result) &#123;
            
            if (error) &#123;
                
                self.blog.isLiked = NO;
                self.blog.likeCount -= 1;
                !response ?: [self.view blogPresenterDidUpdateLikeState:self];
            &#125;
            
            !completionHandler ?: completionHandler(error, result);
        &#125;];
    &#125;
&#125;

业务展示：
BlogViewCell.m

#pragma mark - BlogCellPresenterCallBack

- (void)blogPresenterDidUpdateLikeState:(BlogCellPresenter *)presenter &#123;
    
    [self.likeButton setTitle:presenter.blogLikeCountText forState:UIControlStateNormal];
    [self.likeButton setTitleColor:presenter.isLiked ? [UIColor redColor] : [UIColor blackColor] forState:UIControlStateNormal];
&#125;

- (void)blogPresenterDidUpdateShareState:(BlogCellPresenter *)presenter &#123;
    [self.shareButton setTitle:presenter.blogShareCountText forState:UIControlStateNormal];
&#125;
</code></pre>
<p><strong>可以看到在MVP里面业务逻辑和业务展示是分在不同的地方实现，那么就可以分开测试二者了</strong>，而不像MVC那样想测试下业务逻辑，还必须生成一个view，这不合理，因为业务逻辑改变的model的数据，和view无关。</p>
<p>MVP相对于MVC, 它其实只做了一件事情, 即分割业务展示和业务逻辑。展示和逻辑分开后，只要我们能保证V在收到P的数据更新通知后能正常刷新页面, 那么整个业务就没有问题。因为V收到的通知其实都是来自于P层的数据获取/更新操作，所以我们只要保证P层的这些操作都是正常的就可以了。<strong>即我们只用测试P层的逻辑，不必关心V层的情况。</strong></p>
<p>如果真的很care view持有了P，可以把P抽象为protocol，但这样感觉和做一个cell model类似，感觉如果是必要的耦合可以不处理，如果之后有多个presenter再说啦。</p>
<hr>
<h6>MVVM</h6>
<p>MVVM其实是在MVP的基础上发展起来的。那么MVVM在MVP的基础上改良了啥呢？答案就是数据绑定。</p>
<blockquote>
<p>从 Model-View-ViewModel 这个名字来看，它由三个部分组成，也就是 Model、View 和 ViewModel；其中视图模型（ViewModel）其实就是 MVP 模式中的P，在 MVVM 中叫做VM。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="872" data-height="256"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-5b8cae38b467106d.png" data-original-width="872" data-original-height="256" data-original-format="image/png" data-original-filesize="56031" src="https://upload-images.jianshu.io/upload_images/5219632-5b8cae38b467106d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">MVVM</div>
</div>
<p>除了我们非常熟悉的 Model、View 和 ViewModel 这三个部分，在 MVVM 的实现中，还引入了隐式的一个 Binder层，这也是MVVM相对MVP的进步，而声明式的数据和命令的绑定在 MVVM 模式中就是通过binder层来完成的，RAC是iOS下binder的优雅实现，当然MVVM没有RAC也完全可以运行。</p>
<p><strong>MVVM各层的职责和MVP的类似，VM对应P层，只是在MVVM的View层多了数据绑定的操作。</strong></p>
<ul>
<li>MVP的点赞逻辑如下：</li>
</ul>
<p>点击cell按钮--->调用P的点赞逻辑---->点赞成功后，P改变M的数据--->P回调Cell的代理方法改变cell的显示(点赞成功，赞的个数加1，同时点赞数变红，否则不改变赞的个数也不变色)</p>
<blockquote>
<p>上面就是一个事件完整过程，可以看到要通过四步来完成，而且每次都要把P的状态同步到view，当事件多起来的时候，这样写就很麻烦了。那有没有一种简单的机制，让view的行为和状态和P的行为状态同步呢？</p>
<p>答案就是MVVM的binder机制。</p>
</blockquote>
<p>点赞的MVP的代码看上面MVP章节即可，我们来看下在MVVM下的点赞如何实现的：</p>
<pre><code>BlogCellViewModel.h

- (BOOL)isLiked;
- (NSString *)blogTitleText;
- (NSString *)blogSummaryText;
- (NSString *)blogLikeCount;
- (NSString *)blogShareCount;

- (RACCommand *)likeBlogCommand;

========================================
BlogCellViewModel.m

@weakify(self);
        self.likeBlogCommand = [[RACCommand alloc] initWithSignalBlock:^RACSignal *(id input) &#123;
            @strongify(self);
         
            RACSubject *subject = [RACSubject subject];
            if (self.isLiked) &#123;

                dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(.5 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
                    
                    self.isLiked = NO;
                    self.blogLikeCount = self.blog.likeCount - 1;
                    [subject sendCompleted];
                &#125;);
            &#125; else &#123;
                
                self.isLiked = YES;
                self.blogLikeCount = self.blog.likeCount + 1;
                [[UserAPIManager new] likeBlogWithBlogId:self.blog.blogId completionHandler:^(NSError *error, id result) &#123;
                    
                    if (error) &#123;
                        
                        self.isLiked = NO;
                        self.blogLikeCount = self.blog.likeCount - 1;
                    &#125;
                    error ? [subject sendError:error] : [subject sendCompleted];
                &#125;];
            &#125;
            return subject;
        &#125;];


=========================cell==================
- (void)awakeFromNib &#123;
    [super awakeFromNib];
    
    //数据绑定操作
    @weakify(self);
    RAC(self.titleLabel, text) = RACObserve(self, viewModel.blogTitleText);
    RAC(self.summaryLabel, text) = RACObserve(self, viewModel.blogSummaryText);
    RAC(self.likeButton, selected) = [RACObserve(self, viewModel.isLiked) ignore:nil];
    [RACObserve(self, viewModel.blogLikeCount) subscribeNext:^(NSString *title) &#123;
        @strongify(self);
        [self.likeButton setTitle:title forState:UIControlStateNormal];
    &#125;];
    [RACObserve(self, viewModel.blogShareCount) subscribeNext:^(NSString *title) &#123;
        @strongify(self);
        [self.shareButton setTitle:title forState:UIControlStateNormal];
    &#125;];
    
&#125;

- (IBAction)onClickLikeButton:(UIButton *)sender &#123;
    //事件响应
    if (!self.viewModel.isLiked) &#123;
        [[self.viewModel.likeBlogCommand execute:nil] subscribeError:^(NSError *error) &#123;
            [self showToastWithText:error.domain];
        &#125;];
    &#125; else &#123;
        [self showAlertWithTitle:@"提示" message:@"确定取消点赞吗?" confirmHandler:^(UIAlertAction *confirmAction) &#123;
            [[self.viewModel.likeBlogCommand execute:nil] subscribeError:^(NSError *error) &#123;
                [self showToastWithText:error.domain];
            &#125;];
        &#125;];
    &#125;
&#125;
</code></pre>
<p><strong>可以看到相对MVP的view触发P的业务逻辑，然后P再回调改变View的显示的操作，使用MVVM的数据绑定来实现让逻辑更加清晰，代码也更少。这就是MVVM相对于MVP的改进之处。</strong></p>
<hr>
<p>最后做个简单的总结吧:</p>
<ol>
<li><p>MVC作为老牌架构, 优点在于将业务场景按展示数据类型划分出多个模块, 每个模块中的C层负责业务逻辑和业务展示, 而M和V应该是互相隔离的以做重用, 另外每个模块处理得当也可以作为重用单元. 拆分在于解耦, 顺便做了减负, 隔离在于重用, 提升开发效率. 缺点是没有区分业务逻辑和业务展示, 对单元测试不友好.</p></li>
<li><p>MVP作为MVC的进阶版, 提出区分业务逻辑和业务展示, 将所有的业务逻辑转移到P层, V层接受P层的数据更新通知进行页面展示. 优点在于良好的分层带来了友好的单元测试, 缺点在于分层会让代码逻辑优点绕, 同时也带来了大量的代码工作, 对程序员不够友好.</p></li>
<li><p>MVVM作为集大成者, 通过数据绑定做数据更新, 减少了大量的代码工作, 同时优化了代码逻辑, 只是学习成本有点高, 对新手不够友好.</p></li>
<li><p>MVP和MVVM因为分层所以会建立MVC两倍以上的文件类, 需要良好的代码管理方式.</p></li>
<li><p>在MVP和MVVM中, V和P或者VM之间理论上是多对多的关系, 不同的布局在相同的逻辑下只需要替换V层, 而相同的布局不同的逻辑只需要替换P或者VM层. 但实际开发中P或者VM往往因为耦合了V层的展示逻辑退化成了一对一关系(比如SceneA中需要显示"xxx+Name", VM就将Name格式化为"xxx + Name". 某一天SceneB也用到这个模块, 所有的点击事件和页面展示都一样, 只是Name展示为"yyy + Name", 此时的VM因为耦合SceneA的展示逻辑, 就显得比较尴尬), 针对此类情况, 通常有两种办法, 一种是在VM层加状态进而判断输出状态, 一种是在VM层外再加一层FormatHelper. 前者可能因为状态过多显得代码难看, 后者虽然比较优雅且拓展性高, 但是过多的分层在数据还原时就略显笨拙, 大家应该按需选择.</p></li>
</ol>
<p>这里随便瞎扯一句, 有些文章上来就说MVVM是为了解决C层臃肿, MVC难以测试的问题, 其实并不是这样的. 按照架构演进顺序来看, C层臃肿大部分是没有拆分好MVC模块, 好好拆分就行了, 用不着MVVM. 而MVC难以测试也可以用MVP来解决, 只是MVP也并非完美, 在VP之间的数据交互太繁琐, 所以才引出了MVVM.</p>
<p><strong>我自己的感觉是，其实无论是那种模式，其实我们只是想满足SOLID原则，让类的职责更单一，更容易测试，可以复用的能复用。</strong> 只是实现的方式不一样，没有说吧必须要MVVM来替代MVP，如果你的确回调很少也可以用delegate不一定用KVO。</p>
<blockquote>
<p>我感觉至少要保证的是M和V不要过于耦合，把业务逻辑单独拿出来成为P或者VM，MVC的拆分要细一点不要把每个模块的view都搞到ViewController管理，自己要有自己的C位~</p>
</blockquote>
<hr>
<h4>※ Redux</h4>
<p>redux其实也是单向数据流，和之前用过的Flux很像(<a href="https://www.jianshu.com/p/59408fb10652" target="_blank">https://www.jianshu.com/p/59408fb10652</a>)，其实Redux是就是flux思想在react中的实现：</p>
<ul>
<li>The whole state of your app is stored in an object tree inside a single store.</li>
<li>The only way to change the state tree is to emit an action, an object describing what happened.</li>
<li>To specify how the actions transform the state tree, you write pure reducers.</li>
</ul>
<p>这里的<code>Reducer</code>就是接受action并且改变state的角色，注意state可以是一个比较复杂的structure也可能其实很简单，问题是当你改变state的时候需要新建一个state赋值，不要用旧的指针哦。<code>The only important part is that you should not mutate the state object, but return a new object if the state changes.</code></p>
<hr>
<h6>※ web里面的redux</h6>
<ol>
<li><p>npm install redux -S</p></li>
<li><p>定义一个reducer，处理数据</p></li>
</ol>
<pre><code>function counter(state = 0, action) &#123;
  switch (action.type) &#123;
    case 'INCREMENT':
      return state + 1
    case 'DECREMENT':
      return state - 1
    default:
      return state
  &#125;
&#125;
</code></pre>
<ol start="3">
<li>创建一个store，传入reducer</li>
</ol>
<pre><code>let store = Redux.createStore(counter)
// store分发action
store.dispatch(&#123; type: 'INCREMENT' &#125;)
store.dispatch(&#123; type: 'INCREMENT' &#125;)
store.dispatch(&#123; type: 'DECREMENT' &#125;)
</code></pre>
<ol start="4">
<li>store订阅一个VM的方法，当数据发生改变时，会执行这个方法，通常这部分使用react</li>
</ol>
<pre><code>store.subscribe(() => &#123;
    document.getElementById("app").innerHTML = store.getState.count;
&#125;)
</code></pre>
<hr>
<h4>※ ReMVVM</h4>
<p>如果你看到这里那么其实MVVM可以说算是不错的方式了，为啥还要和redux在一起呢？而且MVVM里面VM改变以后，View会自动更新的part是不是有点像redux里面state更新以后，页面自动变化。</p>
<p>但是为啥还要引入redux以及flux这种单向数据流呢？其实是因为当如果只有一套MVVM/MVC那是木有问题的，非常清晰。但如果有很多套， 并且彼此之间可能会有数据操作那么就会变得像下面酱紫：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="426" data-height="417"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-8785d7e2a4cafd0a.png" data-original-width="426" data-original-height="417" data-original-format="image/png" data-original-filesize="110115" src="https://upload-images.jianshu.io/upload_images/5219632-8785d7e2a4cafd0a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">混乱的MVC</div>
</div>
<p>前面我们提到“单向流”的思维状态可以让大脑更加轻松驾驭，本质上而言，这也是为什么上面这种杂乱的双向图示让我们感到无所适从的原因。我们注意到：之所以图示中 Model-View （MVC中的Model大体上可以看作是前面提到的State）的“单向流”被破坏，<strong>是由于修改Model的Controller代码像一把黄豆一样散落在了各个View组件的内部</strong>，如果可以用某种方式把这些散落的代码单独收拢到一起，是不是就让这可以让这张图示恢复秩序呢？好，我们顺着这个思路想下去。</p>
<p>现在我们又可以从服务器端的MVC模式中获得灵感了！因为我们注意到，服务器端的controller通常也需要对很多Model产生修改，但在代码结构中却集中在一起，没有散落一地。原因很简单，由于server和client是远程通信的关系，因此为了尽量减少通信耦合，client每个操作的全部信息都以http请求的形式被概括成了精简的“作用量”（action）。请求的url路径约定了用户的操作意图（当然RESTful概念中，请求的method也可以反映操作意图），request参数表征了该“意图”的具体内容。正是基于这个action的抽象，client端的交互操作才可以被<strong>集中</strong>转移到server端的controller中做统一响应。</p>
<p>对比之下，我们立刻发现上述代码片断中前端MVC模式的“痛点”所在：不是MVC模式错了，而是我们压根<strong>缺少了一个和用户交互行为有关的action抽象</strong>！因此，对model的具体操作才没法从各个view组件中被剥离出来，放到一处。</p>
<p>参考http请求，我们将要定义的action，需要一个typeName用来表示对model操作的意图（<strong>类似于http请求的url路径</strong>），还可能需要其他字段，用来描述怎样具体操作model（<strong>类似于http请求的参数</strong>）。</p>
<p>也就是说，当用户在view上的交互行为（例如点击提交按钮）应当引起Model发生变化时，我们不直接修改model，而是简单地dispatch一个action（其实跟常见的event机制没有什么区别）以表达修改model的意图，这些action将被<strong>集中</strong>转移给数据端（models），然后数据端会根据这些action做出需要的自我更新。同时，我们考虑到react中view组件的树状分流结构，所以有如下图所示：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="343"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-a59969ee1fcbd8ce.jpg" data-original-width="600" data-original-height="343" data-original-format="image/jpeg" data-original-filesize="20478" src="https://upload-images.jianshu.io/upload_images/5219632-a59969ee1fcbd8ce.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>图中A表示Action，V表示View组件，Models部分的结构会进一步讨论。稍微总结一下：<strong>从代码层面而言，flux无非就是一个常见的event dispatcher，其目的是要将以往MVC中各个View组件内的controller代码片断提取出来放到更加恰当的地方进行集中化管理，并从开发体验上实现了舒适清爽、容易驾驭的“单向流”模式。</strong> 所以我觉得，Flux与其说是对前端MVC模式的颠覆，倒不如说是对前端MVC思想的补充和优化。</p>
<p>但为了区分于以往的MVC模式，并向facebook的贡献表达敬意，后面我们将把这种优化后的 Model-View-Controller 开发模式在React背景下正式称为<strong>Flux模式</strong>。</p>
<hr>
<p>凌波微步指的是redux中的reducer机制，可以用来将state端的数据处理过程作“原子化”拆分。redux是来自函数式编程（Functional Programming）的一朵奇葩，据说很有背景（[参考链接](<a href="https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fredux.js.org%2Fdocs%2Fintroduction%2FPriorArt.html" target="_blank">Prior Art | Redux</a>) ）。本人还没有深究过，但一接触redux，就立刻被其reducer机制的轻盈小巧惊艳到（redux库本身也只有几kb，有必要的化，自己重写也不是难事），因此称其为“凌波微步”。</p>
<p>reducer，从代码上说，其实就是一个函数，具有如下形式：</p>
<p><code>(previousState, action) => newState</code></p>
<p>即，reducer作为一个函数，可以根据web应用之前的状态（previousState）和交互行为（通过flux中提到的action来表征），决定web应用的下一状态（newState），从而实现state端的数据更新处理。这个函数行为和大名鼎鼎的“Map-Reduce”概念中的Reduce操作非常类似，因而称这个函数为“Reducer”。</p>
<p><strong>"shut up and show me the code"</strong></p>
<p>ok，我们还是以todoList应用为例, 此处有[完整代码](<a href="https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fredux.js.org%2Fdocs%2Fbasics%2FExampleTodoList.html" target="_blank">Example: Todo List</a>)。这里不打算详细讲解Redux的具体使用，而只想通过一个Redux对state数据进行操作的代码片断，管窥一下reducer机制对数据进行拆分和组装的简洁过程。代码片断如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="566" data-height="624"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-2727a163657e2065.jpg" data-original-width="566" data-original-height="624" data-original-format="image/jpeg" data-original-filesize="51252" src="https://upload-images.jianshu.io/upload_images/5219632-2727a163657e2065.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>其中的todos是和任务列表数据相关的reducer，todo是和单条任务数据有关的reducer。注意：在todos的函数体内调用了todo，并将action作为参数原样传递给了todo，这种干净利落地通过函数调用将action由 “parent reducer” 传递给 “child reducer”，是redux实现数据处理拆分的普遍方式。回味一下，我们应该可以体会到，<strong>这种数据处理“原子化”拆分的方式和react中view组件的拆分有异曲同工之妙，二者都会形成一种“树状”分流结构</strong>（在react的view hierarchy中，数据通过props的直接赋值实现单向流；在redux的reducer hierarchy中，数据通过action的函数传参实现单向流）。</p>
<p>visibilityFilter是和列表显示状态相关的另一个reducer；combineReducers将visibilityFilter和todos合并为整个应用的reducer，也就是todoApp。这个过程，从感觉上也和react中view组件的合并过程非常相像。</p>
<p>createStore是一个工厂函数。通过它，todoApp（相当于一个数据处理的引擎）被装配到整个应用的state容器，也就是store中。可以通过store的getState方法获取整个应用的state；同时，store也是一个event dispatcher，可以通过其dispatch和subscribe方法，分别实现触发action事件和注册对action事件的响应函数。</p>
<blockquote>
<p>总言之，从概念上来说 <strong>Redux ＝ Reducer ＋ Flux</strong></p>
</blockquote>
<hr>
<p>好，现在React开发模式中的几个核心概念已经全部出场亮相。我们俯瞰一下整个开发流程：首先，react框架为我们理顺了 store --> view 的<strong>“单向”工作流</strong>（store是state的容器）；然后，redux框架为我们理顺了 view --> store 的<strong>“单向”</strong>工作流。并且，react和redux都以组件化的形式可以将各自负责的功能进行<strong>灵活地组装或拆分</strong>，最大程度上确保我们<strong>“一次只需要专注于一个局部问题”</strong>。具体来说，分为以下步骤：</p>
<ol>
<li>单例store的数据在react中可以通过view组件的属性（props）不断由父模块<strong>“单向”</strong>传递给子模块，形成一个树状分流结构。如果我们把redux比作整个应用的“心肺” （redux的flux功能像心脏，reducer功能像肺部毛细血管），那么这个过程可以比作<strong>心脏（store）将氧分子（数据）通过动脉毛细血管（props）送到各个器官组织（view组件）</strong>
</li>
<li>末端的view组件，又可以通过flux机制，将携带交互意图信息的action反馈给store。这个过程有点像将<strong>携带代谢产物的“红细胞”（action）通过静脉毛细血管又泵回心脏（store）</strong>
</li>
<li>action流回到store以后，action以参数的形式又被分流到各个具体的reducer组件中，这些reducer同样构成一个树状的hierarchy。这个过程像<strong>静脉血中的红细胞（action）被运输到肺部毛细血管（reducer组件）</strong>
</li>
<li>接收到action后，各个child reducer以返回值的形式，将最新的state返回给parent reducer，最终确保整个单例store的所有数据是最新的。这个过程可以比作<strong>肺部毛细血管的血液充氧后，又被重新泵回了心脏</strong>
</li>
<li>回到步骤1</li>
</ol>
<p>用图示的方式来表达，即，</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="345"><img data-original-src="//upload-images.jianshu.io/upload_images/5219632-1771faef1a855ffa.jpg" data-original-width="600" data-original-height="345" data-original-format="image/jpeg" data-original-filesize="24548" src="https://upload-images.jianshu.io/upload_images/5219632-1771faef1a855ffa.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">redux</div>
</div>
<p>图中A表示Action，V表示View组件，R表示Reducer。为了确保我们比较容易理解程序的全局行为，或者说提高程序行为的确定性（predictable），我们一般期望具有类似职能的代码片断被“平铺”着摆放在一。因此图示中相同颜色区域的代码通常会被放到同一个文件夹／文件中。另外，同样出于提高程序的确定性，redux所遵循的函数式编程鼓励我们使用pure function和immutable。（函数式编程是另一个漫长的故事，这里就不再展开）</p>
<hr>
<p>具体ReMVVM要咋做可以参考 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.ctolib.com%2Fdgrzeszczak-ReMVVM.html" target="_blank">https://www.ctolib.com/dgrzeszczak-ReMVVM.html</a> 里面的例子哈，总体而言就是VM会发发或者订阅action然后改变model，会有不同的reducer处理state和action。</p>
<blockquote>
<p>Reference:<br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Facademy.realm.io%2Fposts%2Fbenji-encz-unidirectional-data-flow-swift%2F" target="_blank">https://academy.realm.io/posts/benji-encz-unidirectional-data-flow-swift/</a><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FReSwift%2FReSwift" target="_blank">https://github.com/ReSwift/ReSwift</a><br>
<a href="https://www.jianshu.com/p/999898789f93" target="_blank">https://www.jianshu.com/p/999898789f93</a><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fdreamingbaobei%2Fp%2F8476984.html" target="_blank">https://www.cnblogs.com/dreamingbaobei/p/8476984.html</a></p>
</blockquote>
  
</div>
            