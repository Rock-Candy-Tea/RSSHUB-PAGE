
---
title: '无埋点核心技术：iOS Hook在字节的实践经验'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f92ebb6d4674b998fe0e649c74a92d9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 18:29:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f92ebb6d4674b998fe0e649c74a92d9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f92ebb6d4674b998fe0e649c74a92d9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>作者：字节移动技术——段文斌</strong></p>
<h1 data-id="heading-0">前言</h1>
<p>众所周知，字节跳动的推荐在业内处于领先水平，而精确的推荐离不开大量埋点，常见的埋点采集方案是在响应用户行为操作的路径上进行埋点。但是由于App通常会有比较多界面和操作路径，主动埋点的维护成本就会非常大。所以行业的做法是无埋点，而无埋点实现需要AOP编程。</p>
<p>一个常见的场景，比如想在<code>UIViewController</code>出现和消失的时刻分别记录时间戳用于统计页面展现的时长。要达到这个目标有很多种方法，但是AOP无疑是最简单有效的方法。Objective-C的Hook其实也有很多种方式，这里以Method Swizzle给个示例。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface UIViewController (MyHook)

@end

@implementation UIViewController (MyHook)

+ (void)load &#123;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^&#123;
        /// 常规的 Method Swizzle封装
        swizzleMethods(self, @selector(viewDidAppear:), @selector(my_viewDidAppear:));
        /// 更多Hook
    &#125;);
&#125;

- (void)my_viewDidAppear:(BOOL)animated &#123;
  /// 一些Hook需要的逻辑
  
  /// 这里调用Hook后的方法，其实现其实已经是原方法了。
  [self my_viewDidAppear: animated];
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们探讨一个具体场景：</p>
<p><code>UICollectionView</code>或者<code>UITableView</code>是iOS中非常常用的列表UI组件，其中列表元素的点击事件回调是通过<code>delegate</code>完成的。这里以<code>UICollectionView</code>为例，<code>UICollectionView</code>的<code>delegate</code>，有个方法声明，<code>collectionView:didSelectItemAtIndexPath:</code>，实现这个方法我们就可以给列表元素添加点击事件。</p>
<p><strong>我们的目标是Hook这个delegate的方法，在点击回调的时候进行额外的埋点操作。</strong></p>
<h1 data-id="heading-1">方案迭代</h1>
<h2 data-id="heading-2">方案1 Method Swizzle</h2>
<p>通常情况下，Method Swizzle可以满足绝大部分的AOP编程需求。因此首次迭代，我们直接使用Method Swizzle来进行Hook。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface UICollectionView (MyHook)

@end

@implementation UICollectionView (MyHook)

// Hook, setMyDelegate:和setDelegate:交换过
- (void)setMyDelegate:(id)delegate &#123;
    if (delegate != nil) &#123;
        /// 常规Method Swizzle
        swizzleMethodsXXX(delegate, @selector(collectionView:didSelectItemAtIndexPath:), self, @selector(my_collectionView:didSelectItemAtIndexPath:));

    &#125;

    [self setMyDelegate:nil];
&#125;

- (void)my_collectionView:(UICollectionView *)ccollectionView didSelectItemAtIndexPath:(NSIndexPath *)index &#123;
  /// 一些Hook需要的逻辑

  /// 这里调用Hook后的方法，其实现其实已经是原方法了。
  [self my_collectionView:ccollectionView didSelectItemAtIndexPath:index];
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把这个方案集成到今日头条App里面进行测试验证，发现没法办法验证通过。</p>
<p>主要原因今日头条App是一个庞大的项目，其中引入了非常多的三方库，比如IGListKit等，这些三方库通常对<code>UICollectionView</code>的使用都进行了封装，而这些封装，恰恰导致我们不能使用常规的Method Swizzle来Hook这个delegate。直接的原因总结有以下两点：</p>
<ol>
<li><code>setDelegate</code>传入的对象不是实现<code>UICollectionViewDelegate</code>协议的那个对象</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb92bec9b03d40579fbe5fac797e8b46~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图示，<code>setDelegate</code>传入的是一个代理对象proxy，proxy引用了实际的实现<code>UICollectionViewDelegate</code>协议的<code>delegate</code>，proxy实际上并没有实现<code>UICollectionViewDelegate</code>的任何一个方法，它把所有方法都转发给实际的<code>delegate</code>。这种情况下，我们不能直接对proxy进行Method Swizzle</p>
<ol>
<li>多次<code>setDelegate</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f73893b4f97c4721bbed7d21c1d15cac~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述图例中，使用方存在连续调用两次<code>setDelegate</code>的情况，第一次是真实<code>delegate</code>，第二次是<code>proxy</code>，我们需要区别对待。</p>
<h2 data-id="heading-3">代理模式和NSProxy介绍</h2>
<p>使用proxy对原对象进行代理，在处理完额外操作之后再调用原对象，这种模式称为代理模式。而Objective-C中要实现代理模式，使用NSProxy会比较高效。详细内容参考下列文章。</p>
<ul>
<li><a href="https://juejin.cn/post/6844903544965857294" target="_blank">代理模式</a></li>
<li><a href="https://juejin.cn/post/6962720860700409886/" target="_blank">NSProxy使用</a></li>
</ul>
<p>这里面<code>UICollectionView</code>的<code>setDelegate</code>传入的是一个<code>proxy</code>是非常常见的操作，比如IGListKit，同时App基于自身需求，也有可能会做这一层封装。</p>
<p>在<code>UICollectionView</code>的<code>setDelegate</code>的时候，把<code>delegate</code>包裹在<code>proxy</code>中，然后把proxy设置给<code>UICollectionView</code>,使用<code>proxy</code>对<code>delegate</code>进行消息转发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d54f8018473f420989bd12d5a72f70f0~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">方案2 使用代理模式</h2>
<p>方案1已经无法满足我们的需求了，我们考虑到既然对<code>delegate</code>进行代理是一种常规操作，我们何不也使用代理模式，对<code>proxy</code>再次代理。</p>
<h3 data-id="heading-5">代码实现</h3>
<ul>
<li>先Hook <code>UICollectionView</code>的<code>setDelegate</code>方法</li>
<li>代理<code>delegate</code></li>
</ul>
<p>简单的代码示意如下</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">/// 完整封装了一些常规的消息转发方法
@interface DelegateProxy : NSProxy

@property (nonatomic, weak, readonly) id target;

@end

/// 为 CollectionView delegate转发消息的proxy
@interface BDCollectionViewDelegateProxy : DelegateProxy

@end

@implementation BDCollectionViewDelegateProxy <UICollectionViewDelegate>

- (void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath &#123;
    //track event here
    if ([self.target respondsToSelector:@selector(collectionView:didSelectItemAtIndexPath:)]) &#123;
        [self.target collectionView:collectionView didSelectItemAtIndexPath:indexPath];

    &#125;
&#125;

- (BOOL)bd_isCollectionViewTrackerDecorator &#123;
    return YES;
&#125;

// 还有其他的消息转发的代码 先忽略
- (BOOL)respondsToSelector:(SEL)aSelector &#123;
    if (aSelector == @selector(bd_isCollectionViewTrackerDecorator)) &#123;
        return YES;
    &#125;

    return [self.target respondsToSelector:aSelector];
&#125;


@end

@interface UICollectionView (MyHook)

@end

@implementation UICollectionView (MyHook)

- (void) setDd_TrackerProxy:(BDCollectionViewDelegateProxy *)object &#123;
    objc_setAssociatedObject(self, @selector(bd_TrackerProxy), object, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
&#125;

- (BDCollectionViewDelegateProxy *) bd_TrackerProxy &#123;
    BDCollectionViewDelegateProxy *bridge = objc_getAssociatedObject(self, @selector(bd_TrackerProxy));

    return bridge;
&#125;

// Hook, setMyDelegate:和setDelegate:交换过了
- (void)setMyDelegate:(id)delegate &#123;
    if (delegate == nil) &#123;
        [self setMyDelegate:delegate];
        return
    &#125;

    // 不会释放，不重复设置
    if ([delegate respondsToSelector:@selector(bd_isCollectionViewTrackerDecorator)]) &#123;
         [self setMyDelegate:delegate]; 
         return;
    &#125;

    BDCollectionViewDelegateProxy *proxy = [[BDCollectionViewDelegateProxy alloc] initWithTarget:delegate];
    [self setMyDelegate:proxy];
    self.bd_TrackerProxy = proxy;

&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">模型</h3>
<p>下图实线表示强引用，虚线表示弱引用。</p>
<h4 data-id="heading-7">情况一</h4>
<p>如果使用方没有对<code>delegate</code>进行代理，而我们使用代理模式</p>
<ul>
<li><code>UICollectionView</code>，其<code>delegate</code>指针指向DelegateProxy</li>
<li>DelegateProxy，被UICollectionView用runtime的方式强引用，其target弱引用真实Delegate</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d6f916bbda4b77bea90334ea2fe62b~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">情况二</h4>
<p>如果使用方也对<code>delegate</code>进行代理，我们使用代理模式</p>
<ul>
<li>我们只需要保证我们的DelegateProxy处于代理链中的一环即可</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b6c0507e4fd4acca81a4239648a2413~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这里我们可以看出，代理模式有很好的扩展性，它允许代理链不断嵌套，只要我们都遵循代理模式的原则即可。</p>
<p><strong>到这里，我们的方案已经在今日头条App上测试通过了。但是事情远还没有结束。</strong></p>
<h1 data-id="heading-9">踩坑之旅</h1>
<p>目前的还算比较可以，但是也不能完全避免问题。这里其实不仅仅是<strong>UICollectionView的delegate，包括:</strong></p>
<ul>
<li><strong>UIWebView</strong></li>
<li><strong>WKWebView</strong></li>
<li><strong>UITableView</strong></li>
<li><strong>UICollectionView</strong></li>
<li><strong>UIScrollView</strong></li>
<li><strong>UIActionSheet</strong></li>
<li><strong>UIAlertView</strong></li>
</ul>
<p>我们都采用相同的方法来进行Hook。<strong>同时我们将方案封装一个SDK对外提供，以下统称为MySDK。</strong></p>
<h2 data-id="heading-10">第一次踩坑</h2>
<p>某客户接入我们的方案之后，在集成过程中反馈有必现Crash，下面详细介绍一下这一次踩坑的经历。</p>
<h3 data-id="heading-11">堆栈信息</h3>
<p>重点信息是<code>[UIWebView webView:decidePolicyForNavigationAction:request:frame:decisionListener:]</code>。</p>
<pre><code class="copyable">Thread 0 Crashed:

0   libobjc.A.dylib   0x000000018198443c objc_msgSend + 28

1   UIKit             0x000000018be05b4c -[UIWebView webView:decidePolicyForNavigationAction:request:frame:decisionListener:] + 200

2   CoreFoundation    0x0000000182731cd0 __invoking___ + 144

3   CoreFoundation    0x000000018261056c -[NSInvocation invoke] + 292

4   CoreFoundation    0x000000018261501c -[NSInvocation invokeWithTarget:] + 60

5   WebKitLegacy      0x000000018b86d654 -[_WebSafeForwarder forwardInvocation:] + 156
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从堆栈信息不难判断出crash原因是UIWebView的delegate野指针，那为啥出现野指针呢？</p>
<p>这里先说明一下crash的直接原因，然后再来具体分析为什么就出现了问题。</p>
<ol>
<li>MySDK对setDelegate进行了Hook</li>
<li>客户也对setDelegate进行了Hook</li>
<li>先执行MySDK的Hook逻辑调用，然后执行客户的Hook逻辑调用</li>
</ol>
<h3 data-id="heading-12">客户Hook的代码</h3>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface UIWebView (JSBridge)

@end

@implementation UIWebView (JSBridge)

- (void)setJsBridge:(id)object &#123;
    objc_setAssociatedObject(self, @selector(jsBridge), object, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
&#125;

- (WebViewJavascriptBridge *)jsBridge &#123;
    WebViewJavascriptBridge *bridge = objc_getAssociatedObject(self, @selector(jsBridge));
    return bridge;
&#125;

+ (void)load &#123;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^&#123;
        swizzleMethods(self, @selector(setDelegate:), @selector(setJSBridgeDelegate:));
        swizzleMethods(self, @selector(initWithFrame:), @selector(initJSWithFrame:));
    &#125;);

&#125;

- (instancetype)initJSWithFrame:(CGRect)frame &#123;
    self = [self initJSWithFrame:frame];
    if (self) &#123;
        WebViewJavascriptBridge *bridge = [WebViewJavascriptBridge bridgeForWebView:self];
        [self setJsBridge:bridge];
    &#125;
    return self;
&#125;

/// webview.delegate = xxx 会被调用多次且传入的对象不一样
- (void)setJSBridgeDelegate:(id)delegate &#123;
    WebViewJavascriptBridge *bridge = self.jsBridge;
    if (delegate == nil || bridge == nil) &#123;
        [self setJSBridgeDelegate:delegate];
    &#125; else if (bridge == delegate) &#123;
        [self setJSBridgeDelegate:delegate];
    &#125; else &#123;
        /// 第一次进入这里传入 bridge
        /// 第二次进入这里传入一个delegate
        if (![delegate isKindOfClass:[WebViewJavascriptBridge class]]) &#123;
            [bridge setWebViewDelegate:delegate];
            /// 下面这一行代码是客户缺少的
            /// fix with this
            [self setJSBridgeDelegate:bridge];
        &#125; else &#123;
            [self setJSBridgeDelegate:delegate];
        &#125;
    &#125;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">MySDK Hook代码</h3>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface UIWebView (MyHook)

@end

@implementation UIWebView (MyHook)

// Hook, setWebViewDelegate:和setDelegate:交换过
- (void)setWebViewDelegate:(id)delegate &#123;
    if (delegate == nil) &#123;
        [self setWebViewDelegate:delegate];
    &#125;
    BDWebViewDelegateProxy *proxy = [[BDWebViewDelegateProxy alloc] initWithTarget:delegate];
    self.bd_TrackerDecorator = proxy;
    [self setWebViewDelegate:proxy];
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">野指针原因</h3>
<p>UIWebView有两次调用setDelegate方法，第一次是传的WebViewJavascriptBridge，第二次传的另一个实际的WebViewDelegate。暂且称第一次传了bridge第二次传了实际上的delegate。</p>
<ol>
<li>第一次调用，MySDK Hook的时候会用DelegateProxy包装住bridge，所有方法通过DelegateProxy转发到bridge，这里传给 <code>setJSBridgeDelegate:(id)delegate</code>的delegate实际上是DelegateProxy<strong>而非bridge</strong>。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce5ba663e01e4b8dabc5af00ebcbc3b3~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里需要注意，UIWebView的delegate指向DelegateProxy是客户给设置上的，且这个属性<strong>assign而非weak，这个assign很关键，assigin在对象释放之后不会自动变为nil。</strong></p>
<ol>
<li>第二次调用，MySDK Hook的时候会用新的DelegateProxy包装住delegate也就是WebViewDelegate，这个时候MySDK的逻辑是把新的DelegateProxy给强引用中，老的DelegateProxy就失去了强引用因此释放了。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/154fb93cabc94dd680f712b92f2368ca~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时的状态如果不做任何处理，当前状态就如图示：</p>
<ul>
<li>delegate指向已经释放的DelegateProxy，野指针</li>
<li>UIWebview触发回调就导致crash</li>
</ul>
<h3 data-id="heading-15">修复方法</h3>
<p>如果补上那一句，<code>setJSBridgeDelegate:(id)delegate</code>在判断了delegate不是bridge之后，把UIWebView的delegate设置为bridge就可以完成了。</p>
<p><strong>注释中 fix with this下一行代码</strong></p>
<p>修复后模型如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e47fdd3560045c08ee6c678d1b71c7a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">总结</h3>
<p>使用Proxy的方式虽然也可以解决一定的问题，但是也需要使用方遵循一定的规范，要意识到第三方SDK也可能<code>setDelegate</code>进行Hook，也可能使用Proxy</p>
<h2 data-id="heading-17">第二次踩坑</h2>
<p>先补充一些参考资料</p>
<ul>
<li>RxCocoa源码参考 <a href="https://github.com/ReactiveX/RxSwift" target="_blank" rel="nofollow noopener noreferrer">github.com/ReactiveX/R…</a></li>
<li><a href="https://xing-ou.github.io/2017/06/13/rxcocoa%E5%AD%A6%E4%B9%A0-DelegateProxy/" target="_blank" rel="nofollow noopener noreferrer">rxcocoa学习-DelegateProxy</a></li>
</ul>
<p>RxCocoa也使用了代理模式，对delegate进行了代理，按道理应该没有问题。但是RxCocoa的实现有点出入。</p>
<h3 data-id="heading-18">RxCocoa</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff7e6346f7084123b07f694980497768~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果单独只使用了<strong>RxCocoa</strong>的方案，和方案是一致，也就不会有任何问题。</p>
<h3 data-id="heading-19">RxCocoa+MySDK</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7cfe5173084d7dba675665268577d4~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RxCocoa+MySDK之后，变成这样子。UICollectionView的delegate直接指向谁在于谁调用的<code>setDelegate</code>方法后调。</p>
<p>理论也应该没有问题，就是引用链多一个poxy包装而已。但是实际上有两个问题。</p>
<h3 data-id="heading-20">问题1</h3>
<p>RxCocoa的delegate的get方法命中assert</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">//  UIScrollView+Rx.swift</span>
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Reactive</span> <span class="hljs-title">where</span> <span class="hljs-title">Base</span>: <span class="hljs-title">UIScrollView</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> delegate: <span class="hljs-type">DelegateProxy</span><<span class="hljs-type">UIScrollView</span>, <span class="hljs-type">UIScrollViewDelegate</span>> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-type">RxScrollViewDelegateProxy</span>.proxy(for: base)
        <span class="hljs-comment">// base可以理解为一个UIScrollView 实例</span>
    &#125;
&#125;

<span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RxScrollViewDelegateProxy</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">for</span> <span class="hljs-params">object</span>: <span class="hljs-type">ParentObject</span>)</span> -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">let</span> maybeProxy <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.assignedProxy(for: object)
        <span class="hljs-keyword">let</span> proxy: <span class="hljs-type">AnyObject</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> existingProxy <span class="hljs-operator">=</span> maybeProxy &#123;
            proxy <span class="hljs-operator">=</span> existingProxy
        &#125; <span class="hljs-keyword">else</span> &#123;
            proxy <span class="hljs-operator">=</span> castOrFatalError(<span class="hljs-keyword">self</span>.createProxy(for: object))
            <span class="hljs-keyword">self</span>.assignProxy(proxy, toObject: object)
            <span class="hljs-built_in">assert</span>(<span class="hljs-keyword">self</span>.assignedProxy(for: object) <span class="hljs-operator">===</span> proxy)
        &#125;
        <span class="hljs-keyword">let</span> currentDelegate <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>._currentDelegate(for: object)
        <span class="hljs-keyword">let</span> delegateProxy: <span class="hljs-keyword">Self</span> <span class="hljs-operator">=</span> castOrFatalError(proxy)
        <span class="hljs-keyword">if</span> currentDelegate <span class="hljs-operator">!==</span> delegateProxy &#123;
            delegateProxy._setForwardToDelegate(currentDelegate, retainDelegate: <span class="hljs-literal">false</span>)
            <span class="hljs-built_in">assert</span>(delegateProxy._forwardToDelegate() <span class="hljs-operator">===</span> currentDelegate)
            <span class="hljs-keyword">self</span>._setCurrentDelegate(proxy, to: object)
          <span class="hljs-comment">/// 命中下面这一行assert</span>
            <span class="hljs-built_in">assert</span>(<span class="hljs-keyword">self</span>._currentDelegate(for: object) <span class="hljs-operator">===</span> proxy)
            <span class="hljs-built_in">assert</span>(delegateProxy._forwardToDelegate() <span class="hljs-operator">===</span> currentDelegate)
        &#125;
        <span class="hljs-keyword">return</span> delegateProxy
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>重点逻辑</strong></p>
<ul>
<li>delegateProxy即使RxDelegateProxy</li>
<li>currentDelegate为RxDelegateProxy指向的对象</li>
<li>RxDelegateProxy._setForwardToDelegate把RxDelegateProxy指向真实的Delegate</li>
<li>标红的前面一句执行的时候，是调用setDelegate方法，把RxDelegateProxy的proxy设置给UIScrollView(其实是一个UICollectionView实例)</li>
<li>然后进入了MySDK的Hook方法，把RxDelegateProxy给包了一层</li>
<li>最终结果如下图</li>
<li>然后导致self._currentDelegate(for: object) 是DelegateProxy而非RxDelegateProxy，<strong>触发标红断言</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a455cd8ebad491889e03857e7af12ec~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这个断言就很霸道</strong>，相当于RxCocoa认为就只有它能够去使用Proxy包装delegate，其他人不能这样做，只要做了，就断言。</p>
<p><strong>进一步分析</strong></p>
<ul>
<li>当前状态</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfd878666c0a4a189bca9e81e771565d~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>再次进入Rx的方法
<ul>
<li>currentDelegate是UICollectionView指向的DelegateProxy（MySDK的包装）</li>
<li>delegateProxy指向还是RxDelegateProxy</li>
<li>触发Rx的if判断,Rx会把其指向真实的delegate改向UICollectionView指向的DelegateProxy</li>
<li>导致循环指向，引用链中真实的Delegate丢失了</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a945f79e9074c2ca13a593c8509ec83~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">问题2</h3>
<p><strong>上面提到多次调用导致了循环指向，而循环指向导致了在实际的方法转发的时候变成了死循环。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7971b997b8c34cb4a2ec99d2b9689065~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>responds代码</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RxScrollViewDelegateProxy</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">responds</span>(<span class="hljs-params">to</span> <span class="hljs-params">aSelector</span>: <span class="hljs-type">Selector</span>!)</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.responds(to: aSelector)
            <span class="hljs-operator">||</span> (<span class="hljs-keyword">self</span>._forwardToDelegate<span class="hljs-operator">?</span>.responds(to: aSelector) <span class="hljs-operator">??</span> <span class="hljs-literal">false</span>)
            <span class="hljs-operator">||</span> (<span class="hljs-keyword">self</span>.voidDelegateMethodsContain(aSelector) <span class="hljs-operator">&&</span> <span class="hljs-keyword">self</span>.hasObservers(selector: aSelector))
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@implementation BDCollectionViewDelegateProxy

- (BOOL)respondsToSelector:(SEL)aSelector &#123;
    if (aSelector == @selector(bd_isCollectionViewTrackerDecorator)) &#123;
        return YES;
    &#125;
    return [super respondsToSelector:aSelector];
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>似乎只要不多次调用就没有问题了？</strong></p>
<p><strong>关键在于Rx的setDelegate方法也调用了get方法，导致一次get就触发第二次调用。也就是多次调用是无法避免。</strong></p>
<h3 data-id="heading-22">解决方案</h3>
<p>问题的原因比较明显，如果改造RxCocoa的代码，把第三方可能的Hook考虑进来，完全可以解决问题。</p>
<h4 data-id="heading-23">解决方案1</h4>
<p>参考MySDK的proxy方案，在proxy中加入一个特殊方法，来判断RxDelegateProxy是否已经在引用链中，而不去主动改变这个引用链。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8098cefdfff14394936431adb39a3b58~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RxScrollViewDelegateProxy</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">for</span> <span class="hljs-params">object</span>: <span class="hljs-type">ParentObject</span>)</span> -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-operator">...</span>
        <span class="hljs-keyword">let</span> currentDelegate <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>._currentDelegate(for: object)
        <span class="hljs-keyword">let</span> delegateProxy: <span class="hljs-keyword">Self</span> <span class="hljs-operator">=</span> castOrFatalError(proxy)
        <span class="hljs-comment">//if currentDelegate !== delegateProxy</span>
        <span class="hljs-keyword">if</span> <span class="hljs-operator">!</span>currentDelegate.responds(to: xxxMethod) &#123;
            delegateProxy._setForwardToDelegate(currentDelegate, retainDelegate: <span class="hljs-literal">false</span>)
            <span class="hljs-built_in">assert</span>(delegateProxy._forwardToDelegate() <span class="hljs-operator">===</span> currentDelegate)
            <span class="hljs-keyword">self</span>._setCurrentDelegate(proxy, to: object)
            <span class="hljs-built_in">assert</span>(<span class="hljs-keyword">self</span>._currentDelegate(for: object) <span class="hljs-operator">===</span> proxy)
            <span class="hljs-built_in">assert</span>(delegateProxy._forwardToDelegate() <span class="hljs-operator">===</span> currentDelegate)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> currentDelegate
        &#125;

        <span class="hljs-keyword">return</span> delegateProxy
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>类似这样的改造，就可以解决问题。我们与Rx团队进行了沟通，也提了PR，可惜最终被拒绝合入了。Rx给出的说明是，Hook是不优雅的方式，不推荐Hook系统的任何方法，也不想兼容任何第三方的Hook。</strong></p>
<h4 data-id="heading-24">解决方案2</h4>
<p>有没有可能，RxCocoa不改代码，MySDK来兼容？</p>
<p>刚才提到，有可能是两种状态。</p>
<ul>
<li>状态1
<ul>
<li>setDelegate的时候，先进Rx的方法，后进MySDK的Hook方法，</li>
<li>传给Rx的就是delegate</li>
<li>传给MySDK的是RxDelegateProxy</li>
<li>Delegate的get调用就触发bug</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56e0faa2937742b397ecfd5c6b53d21a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>状态2
<ul>
<li>setDelegate的时候，先进MySDK的Hook方法，后进Rx的方法？</li>
<li>传给Rx的就是DelegateProxy</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ffc876e1cd543b5aa40122be6fecef7~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实如果是状态2，似乎Rxcocoa的bug是不会复现的。</p>
<p><strong>但是仔细查看Rxcocoa的setDelegate代码</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Reactive</span> <span class="hljs-title">where</span> <span class="hljs-title">Base</span>: <span class="hljs-title">UIScrollView</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setDelegate</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">delegate</span>: <span class="hljs-type">UIScrollViewDelegate</span>)</span>

    -> <span class="hljs-type">Disposable</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-type">RxScrollViewDelegateProxy</span>.installForwardDelegate(delegate, retainDelegate: <span class="hljs-literal">false</span>, onProxyForObject: <span class="hljs-keyword">self</span>.base)
    &#125;
&#125;

<span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RxScrollViewDelegateProxy</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">installForwardDelegate</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">forwardDelegate</span>: <span class="hljs-type">Delegate</span>, <span class="hljs-params">retainDelegate</span>: <span class="hljs-type">Bool</span>, <span class="hljs-params">onProxyForObject</span> <span class="hljs-params">object</span>: <span class="hljs-type">ParentObject</span>)</span> -> <span class="hljs-type">Disposable</span> &#123;
        <span class="hljs-keyword">weak</span> <span class="hljs-keyword">var</span> weakForwardDelegate: <span class="hljs-type">AnyObject</span>? <span class="hljs-operator">=</span> forwardDelegate <span class="hljs-keyword">as</span> <span class="hljs-type">AnyObject</span>
        <span class="hljs-keyword">let</span> proxy <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.proxy(for: object)
        <span class="hljs-built_in">assert</span>(proxy._forwardToDelegate() <span class="hljs-operator">===</span> <span class="hljs-literal">nil</span>, <span class="hljs-string">""</span>)
        proxy.setForwardToDelegate(forwardDelegate, retainDelegate: retainDelegate)
        <span class="hljs-keyword">return</span> <span class="hljs-type">Disposables</span>.create &#123;
            <span class="hljs-operator">...</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>emmm？Rx里面，UICollectionView的setDelegate和Delegate的get方法<strong>不是Hook...</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift">collectionView.rx.setDelegate(delegate)

<span class="hljs-keyword">let</span> delegate <span class="hljs-operator">=</span> collectionView.rx.delegate
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>最终流程就只能是</strong></p>
<ul>
<li>setDelegate的时候，先进Rx的方法，传给Rx真实的delegate</li>
<li>后进MySDK的Hook方法</li>
<li>传给MySDK的是RxDelegateProxy</li>
<li>Rx里面获取CollectionView的delegate触发判断</li>
<li>Delegate的get调用就触发bug</li>
</ul>
<p>如果MySDK还是采用当前的Hook方案，就没法在MySDK解决了。</p>
<h4 data-id="heading-25">解决方案3</h4>
<p>仔细看了一下，发现Rx里面是通过重写RxDelegateProxy的forwardInvocation来达到方法转发的目的，即</p>
<ul>
<li>RxDelegateProxy没有实现<code>UICollectionViewDelegate</code>的任何方法</li>
<li>forwardInvocation中处理<code>UICollectionViewDelegate</code>相关回调</li>
</ul>
<p>回顾消息转发机制</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad7b9ab920424b3b938af9583c2b0fcd~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以在forwardingTargetForSelector这一步进行处理，这样可以避开与Rx相关的冲突，处理完再直接跳过。</p>
<ul>
<li>forwardingTargetForSelector中针对delegate的回调，target返回一个SDK处理的类，比DelegateProxy</li>
<li>DelegateProxy上报完成之后，直接调用跳到RxDelegateProxy的forwardInvocation方法</li>
</ul>
<p>这个解决方案其实也不完美，只能暂时规避与Rx的冲突。如果后续有其他SDK也来在这个阶段处理Hook冲突，也容易出现问题。</p>
<h1 data-id="heading-26">总结</h1>
<p>确实如Rx团队描述的那样，Hook不是很优雅的方式，任何Hook都有可能存在兼容性问题。</p>
<ol>
<li>谨慎使用Hook</li>
<li>Hook系统接口一定要遵循一定的规范，不能假想只有你在Hook这个接口</li>
<li>不要假想其他人会怎么处理，直接把多种方案集成到一起，构建多种场景，测试兼容性</li>
</ol>
<p>文章列举的方案可能不全或者不完善，如果有更好的方案，欢迎讨论。</p>
<h1 data-id="heading-27">参考文档</h1>
<ul>
<li><a href="https://juejin.cn/post/6962720860700409886/" target="_blank">NSProxy使用</a></li>
<li><a href="https://juejin.cn/post/6844903544965857294" target="_blank">代理模式</a></li>
<li><a href="https://xing-ou.github.io/2017/06/13/rxcocoa%E5%AD%A6%E4%B9%A0-DelegateProxy/" target="_blank" rel="nofollow noopener noreferrer">rxcocoa学习-DelegateProxy</a></li>
<li><a href="https://github.com/ReactiveX/RxSwift" target="_blank" rel="nofollow noopener noreferrer">github.com/ReactiveX/R…</a></li>
</ul>
<h1 data-id="heading-28">关于字节移动平台团队</h1>
<p>字节跳动移动平台团队(Client Infrastructure)是大前端基础技术行业领军者，负责整个字节跳动的中国区大前端基础设施建设，提升公司全产品线的性能、稳定性和工程效率，支持的产品包括但不限于抖音、今日头条、西瓜视频、火山小视频等，在移动端、Web、Desktop等各终端都有深入研究。</p>
<p>就是现在！<strong>客户端／前端／服务端／端智能算法／测试开发</strong> 面向全球范围招聘！<strong>一起来用技术改变世界</strong>，感兴趣可以联系邮箱 <strong><a href="mailto:chenxuwei.cxw@bytedance.com">chenxuwei.cxw@bytedance.com</a></strong>，邮件主题 <strong>简历-姓名-求职意向-期望城市-电话</strong>。</p></div>  
</div>
            