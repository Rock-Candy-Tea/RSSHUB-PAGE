
---
title: 'Redux思想OC简单实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/540ede0a7a164879a4a1a787c8d8ede0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 23:53:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/540ede0a7a164879a4a1a787c8d8ede0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、Redux设计理念</h3>
<p><code>Redux</code>是将整个应用状态存储到一个地方上称为<code>store</code>,里面保存着一个状态树<code>store tree</code>,组件可以派发(<code>dispatch</code>)行为(<code>action</code>)给<code>store</code>,而不是直接通知其他组件，组件内部通过订阅<code>store</code>中的状态<code>state</code>来刷新自己的视图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/540ede0a7a164879a4a1a787c8d8ede0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">二、我们是否需要Redux</h3>
<p>1.首先明确一点，Redux 是一个有用的架构，但不是非用不可。大多数情况，可以不用它。</p>
<ul>
<li>"如果你不知道是否需要 Redux，那就是不需要它。"</li>
<li>"只有遇到 React 实在解决不了的问题，你才需要 Redux 。"</li>
</ul>
<p>2.简单说，如果你的UI层非常简单，没有很多互动，Redux 就是不必要的，用了反而增加复杂性。下面这些情况，都不需要使用 Redux。</p>
<ul>
<li>用户的使用方式非常简单</li>
<li>用户之间没有协作</li>
<li>不需要与服务器大量交互</li>
<li>视图层（View）只从单一来源获取数据</li>
</ul>
<p>3.用户的使用方式复杂，下面这些情况才是 Redux 的适用场景：多交互、多数据源。</p>
<ul>
<li>不同身份的用户有不同的使用方式（比如普通用户和管理员）</li>
<li>多个用户之间可以协作</li>
<li>与服务器大量交互，或者使用了WebSocket</li>
<li>View要从多个来源获取数据</li>
</ul>
<p>从组件角度看，如果你的应用有以下场景，可以考虑使用 Redux。比如像爱奇艺、优酷、腾讯视频这种复杂播放器。</p>
<ul>
<li>某个组件的状态，需要共享</li>
<li>某个状态需要在任何地方都可以拿到</li>
<li>一个组件需要改变全局状态</li>
<li>一个组件需要改变另一个组件的状态</li>
</ul>
<p>总之，不要把 Redux 当作万灵丹，如果你的应用没那么复杂，就没必要用它。</p>
<h3 data-id="heading-2">三、Redux三大原则</h3>
<ul>
<li>唯一数据源</li>
<li>保持只读状态</li>
<li>数据改变只能通过纯函数来执行</li>
</ul>
<h5 data-id="heading-3">1、唯一数据源</h5>
<p>整个应用的state都被存储到一个状态树里面，并且这个状态树，只存在于唯一的store中</p>
<h5 data-id="heading-4">2、保持只读状态</h5>
<p>state是只读的，唯一改变state的方法就是触发action，action是一个用于描述以发生时间的普通对象</p>
<h5 data-id="heading-5">3、数据改变只能通过纯函数来执行</h5>
<p>使用纯函数来执行修改，为了描述action如何改变state的，你需要编写reducers</p>
<h3 data-id="heading-6">四、Redux API介绍</h3>
<h5 data-id="heading-7">1、Store</h5>
<p>Store 就是保存数据的地方，你可以把它看成一个容器。整个应用只能有一个 Store。</p>
<h5 data-id="heading-8">2、State</h5>
<p>Store对象包含所有数据。如果想得到某个时点的数据，就要对 Store 生成快照。这种时点的数据集合，就叫做 State。</p>
<h5 data-id="heading-9">3、Action</h5>
<p>State 的变化，会导致 View 的变化。但是，用户接触不到 State，只能接触到 View。所以，State 的变化必须是 View 导致的。Action 就是 View 发出的通知，表示 State 应该要发生变化了。</p>
<h5 data-id="heading-10">4、Action Creator</h5>
<p>View 要发送多少种消息，就会有多少种 Action。如果都手写，会很麻烦。可以定义一个函数来生成 Action，这个函数就叫 Action Creator。</p>
<h5 data-id="heading-11">5、store.dispatch()</h5>
<p>store.dispatch()是 View 发出 Action 的唯一方法。</p>
<h5 data-id="heading-12">6、Reducer</h5>
<p>Reducer就是一个<code>纯函数</code>，输入就是oldState以及action，然后输出就是一个newState，注意这里就类似<code>函数式编程</code>，reducer是不应该改动到对象的属性的，就是不应该产生副作用，仅仅是用于计算的感觉。也就是无论执行多少次，结果都一样，无论对象是什么，只要输入的一致，输出就不变。</p>
<p>简单来说，Reducer 是一个函数，它接受 Action 和当前 State 作为参数，返回一个新的 State。</p>
<h3 data-id="heading-13">五、OC实现</h3>
<p>根据上面的分析，我们就开始设计我们的类了。为了能够让这个redux更通用，所以我们在设计的时候最好可以抽象一下, 具体结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0192d412831645c4a45721dbdb375ed0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">1. CCAction</h5>
<pre><code class="copyable">@protocol CCAction <NSObject>

/** action，每个行为有唯一的标识 */
@property (nonatomic, copy, readonly) NSString *identifier;

/** 为action添加的额外信息 */
@property (nonatomic, strong, readonly, nullable) id payload;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">2. CCReducer</h5>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCState.h"
#import "CCAction.h"

typedef void (^RDXReduceBlock)(__kindof id <CCState> state, __kindof id <CCAction> action);

@protocol CCReducer <NSObject>

/**
 * 返回 reducer blocks 数组.
 *
 * @return RDXReduceBlock 数组
 */
+ (NSArray <RDXReduceBlock> *)reducers;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">3. CCState</h5>
<pre><code class="copyable">/**
 实现copy协议，为了数据存储
 [NSKeyedUnarchiver unarchiveObjectWithData:[NSKeyedArchiver archivedDataWithRootObject:state]]
 */

@protocol CCState <NSCoding>

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">4. CCStore</h5>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCState.h"
#import "CCAction.h"
#import "CCState.h"
#import "CCReducer.h"

FOUNDATION_EXPORT NSNotificationName const kCCStateDidChangeNotification;

typedef void (^CCStoreNotifationCallback)(void);

@interface CCStore : NSObject

- (instancetype)init NS_UNAVAILABLE;
+ (instancetype)new NS_UNAVAILABLE;

/**
 * 创建一个Store
 *
 * @param reducers reducers 数组
 * @param initialState 初始化状态
 * @return Store
 */
- (instancetype)initWithReducers:(NSArray <RDXReduceBlock> *)reducers state:(id <CCState> )initialState NS_DESIGNATED_INITIALIZER;

/**
 * 要求接受者发送action并立即返回
 * 接受者通过当前的state和action返回给所有的负责更新State的reduce blocks
 * 所有接收到reduce blocks的都会被触发，同时发送通知 CCStateDidChangeNotification
 * @param action The action object to be dispatched.
 */
- (void)dispatchAction:(id <CCAction> )action;

/**
 * 接受者当前状态
 *
 * @return 当前状态，这个状态经过深度copy
 */
- (id <CCState> )currentState;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">六、实际接入</h3>
<p>基于上面我们抽象出来的框架，我们来用实际的Demo演示一下如何使用，这个Demo就是一个简单的加1和减1的功能。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/907750a7279245d3960d34ca5b867b6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对应的代码结构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f09b19f8a14b45c1b98c1c38ac42e88b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们仔细介绍一些，这些类都干了什么？</p>
<h5 data-id="heading-19">1. Action</h5>
<p>.h 头文件内容</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCAction.h"

extern NSString * _Nullable const kActionIdentifierIncreaseCount;
extern NSString * _Nullable const kActionIdentifierDecreaseCount;

@interface Action : NSObject <CCAction>

- (instancetype _Nullable )init NS_UNAVAILABLE;
+ (instancetype _Nullable )new NS_UNAVAILABLE;

/**
 * 创建一个action
 *
 * @param identifier 标识
 * @param payload    额外信息，有效负载信息
 * @return Newly created action object.
 */
+ (instancetype _Nullable )actionWithIdentifier:(NSString *_Nullable)identifier payload:(nullable id)payload;

/**
* 创建一个action
*
* @param identifier 标识
* @param payload    额外信息，负载
* @return Newly created action object.
*/
- (instancetype _Nullable )initWithActionIdentifier:(NSString *_Nullable)identifier payload:(nullable id)payload NS_DESIGNATED_INITIALIZER;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的.m 文件</p>
<pre><code class="copyable">#import "Action.h"

NSString * const kActionIdentifierIncreaseCount = @"ActionIdentifierIncreaseCount";
NSString * const kActionIdentifierDecreaseCount = @"ActionIdentifierDecreaseCount";

@interface Action ()

/** 标识 */
@property (nonatomic, copy, readwrite) NSString *identifier;
/** 有效负载信息 */
@property (nonatomic, strong, readwrite) id payload;

@end

@implementation Action

+ (instancetype)actionWithIdentifier:(NSString *)identifier payload:(nullable id)payload &#123;
    return [[self alloc] initWithActionIdentifier:identifier payload:payload];
&#125;

- (instancetype)initWithActionIdentifier:(NSString *)identifier payload:(id)payload &#123;
    if (self = [super init]) &#123;
        _identifier = [identifier copy];
        _payload = payload;
    &#125;
    return self;
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">2. State</h5>
<p>.h 头文件内容</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCState.h"

@interface State : NSObject<CCState>

@property (nonatomic, assign) NSInteger count;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应.m 实现</p>
<pre><code class="copyable">#import "State.h"

@implementation State

- (instancetype)init &#123;
    if (self = [super init]) &#123;
        _count = 0;
    &#125;
    return self;
&#125;

- (instancetype)initWithCoder:(NSCoder *)aDecoder &#123;
    if (self = [self init]) &#123;
        _count = [aDecoder decodeIntegerForKey:@"count"];
    &#125;
    return self;
&#125;

- (void)encodeWithCoder:(NSCoder *)aCoder &#123;
    [aCoder encodeInteger:self.count forKey:@"count"];
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">3. Reducer</h5>
<p>.h 文件内容</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCReducer.h"

@interface Reducer : NSObject<CCReducer>

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应.m 文件内容</p>
<pre><code class="copyable">#import "Reducer.h"
#import "Action.h"
#import "State.h"

@implementation Reducer

+ (RDXReduceBlock)increaseReducer &#123;
    
    RDXReduceBlock reducer = ^(State *state, Action *action) &#123;
        if ([action.identifier isEqualToString:kActionIdentifierIncreaseCount]) &#123;
            state.count++;
        &#125;
    &#125;;
    return reducer;
&#125;

+ (RDXReduceBlock)decreaseReducer &#123;
    RDXReduceBlock reducer = ^(State *state, Action *action) &#123;
        if ([action.identifier isEqualToString:kActionIdentifierDecreaseCount]) &#123;
            state.count--;
        &#125;
    &#125;;
    return reducer;
&#125;

+ (NSArray <RDXReduceBlock> *)reducers &#123;
    return @[
        [self increaseReducer],
        [self decreaseReducer]
    ];
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">4. Store</h5>
<p>.h 文件内容</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCStore.h"

@interface Store : CCStore

/** 单例 */
+ (instancetype)sharedStore;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>.m 文件内容</p>
<pre><code class="copyable">#import "Store.h"
#import "Reducer.h"
#import "State.h"

@implementation Store

+ (instancetype)sharedStore &#123;
    static id _sharedStore = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^&#123;
        _sharedStore = [[self alloc] init];
    &#125;);

    return _sharedStore;
&#125;

- (instancetype)init &#123;
    NSArray *reducers = [Reducer reducers];
    State *initialState = [[State alloc] init];
    self = [super initWithReducers:reducers state:initialState];
    return self;
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">5. 最后我们的使用姿势</h5>
<pre><code class="copyable">@interface ViewController ()

/** 增加 */
@property (nonatomic, strong) UIButton *increaseButton;
/** 减少 */
@property (nonatomic, strong) UIButton *decreaseButton;
/** 显示 */
@property (nonatomic, strong) UILabel *textLabel;

@end

@implementation ViewController

- (void)viewDidLoad &#123;
    [super viewDidLoad];

    self.view.backgroundColor = [UIColor whiteColor];
    
    self.increaseButton = [UIButton buttonWithType:UIButtonTypeCustom];
    self.increaseButton.frame = CGRectMake(30, 300, 100, 30);
    [self.increaseButton setTitle:@"增加" forState:UIControlStateNormal];
    [self.increaseButton setBackgroundColor:[UIColor orangeColor]];
    [self.increaseButton addTarget:self action:@selector(increaseButtonClick:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:self.increaseButton];
    
    self.decreaseButton = [UIButton buttonWithType:UIButtonTypeCustom];
    self.decreaseButton.frame = CGRectMake(230, 300, 100, 30);
    [self.decreaseButton setTitle:@"减少" forState:UIControlStateNormal];
    [self.decreaseButton setBackgroundColor:[UIColor orangeColor]];
    [self.decreaseButton addTarget:self action:@selector(decreaseButtonClick:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:self.decreaseButton];
    
    self.textLabel = [[UILabel alloc] initWithFrame:CGRectMake(30, 400, self.view.frame.size.width - 60, 30)];
    self.textLabel.textColor = [UIColor orangeColor];
    self.textLabel.textAlignment = NSTextAlignmentCenter;
    self.textLabel.text = @"当前是0";
    [self.view addSubview:self.textLabel];
    
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(updateUI:)
                                                 name:kCCStateDidChangeNotification
                                               object:nil];
&#125;

- (void)increaseButtonClick:(UIButton *)button &#123;
    Action *action = [[Action alloc] initWithActionIdentifier:kActionIdentifierIncreaseCount payload:nil];
    [[Store sharedStore] dispatchAction:action];
&#125;

- (void)decreaseButtonClick:(UIButton *)button  &#123;
    Action *action = [[Action alloc] initWithActionIdentifier:kActionIdentifierDecreaseCount payload:nil];
    [[Store sharedStore] dispatchAction:action];
&#125;

- (void)updateUI:(NSNotification *)note &#123;
    State *state = (State *)[[Store sharedStore] currentState];
    self.textLabel.text = [NSString stringWithFormat:@"当前是%ld", state.count];
&#125;

- (void)dealloc &#123;
    [[NSNotificationCenter defaultCenter] removeObserver:self];
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">7. 传送门</h3>
<p>如果上面大家看完还不是很明白，可以下载demo来仔细研究一下
<a href="https://github.com/zwcshy/ReduxDemo" target="_blank" rel="nofollow noopener noreferrer">OC实现Redux思想</a></p></div>  
</div>
            