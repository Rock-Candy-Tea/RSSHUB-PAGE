
---
title: '实现一套轻量级MVVM框架'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=6083'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 00:14:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=6083'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><em>2021-04-04</em></p>
<h2 data-id="heading-0">前言</h2>
<p>在客户端开发项目中，MVC 仍然是主流架构，但是 MVC 也存在十分明显的弊端：Controller 作为中介者常常需要负担大量的业务处理逻辑，所以 MVC 也被戏称为 Masive View Controller 架构。缓解这个问题其实有很多途径，例如：</p>
<ul>
<li>用胖模型分担 Controller 的模型数据处理工作，提供尽量熟成的业务数据；</li>
<li>引入 Manager 或提取 Service 模块，负责特定业务模块数据管理；</li>
<li>将膨胀的 Controller 业务分摊到多个 Child View Controller；</li>
<li>通过 Category 对 Controller 业务逻辑做分文件处理；</li>
</ul>
<p>此外，MVC 架构模式还普遍存在单元测试推进困难的问题，该问题还是来源于 Controller 负担过重，由于 Controller 通常需要依赖 View 层和 Model 层模块，引入 Manager 和 Service 则依赖模块更加繁多，因此测试 Controller 时通常需要 Mock 很多模块，打很多的 Stub 以剔除依赖模块的影响。另外，Controller 的单元测试需要考虑 Controller 复杂的生命周期。</p>
<p>MVVM 可以说是为了解决 MVC 的以上两个弊端而存在的。</p>
<h2 data-id="heading-1">一、MVVM架构</h2>
<p>View Model 是 MVVM 架构的核心逻辑层。View Model 用于表征 View 的特性，并通过数据双向绑定 View Model 和 View，使 View Model 可以驱动 View 刷新界面，同时 View 接收的用户交互动作也可以更新 View Model 的数据。双向绑定下的 View Model 和 View 是完全解耦的，因此单元测试工作比起 MVC 架构简单得多。MVVM 中 Controller 的职能只局限于 View Model 和 View 的双向绑定，Controller 逻辑层变得很薄，因此周期问题基本可以忽略不计。</p>
<p>MVVM 之所以能达到以上效果，很大程度上是因为它将 View 和 View Model 之间的双向数据流下沉到了框架层。不过这也给 MVVM 带来了最大的缺点：数据流动控制的实现细节隐藏于核心框架层。近乎黑盒的双向数据绑定实现，有时会给代码调试带来不小的麻烦。另外，随着核心逻辑大量转移到 View Model，同样会带来 View Model 规模膨胀的问题，另外需要注意，MVVM 通常不能减少代码量，MVC 仍然是最省代码的客户端架构。总之就是，MVVM 值得尝试，但也没有想象中神奇。</p>
<blockquote>
<p>在强大的 MVVM 框架支持下是可以达到更省代码的效果的。</p>
</blockquote>
<h2 data-id="heading-2">二、MVVM架构实现</h2>
<p>iOS 客户端开发中应用最为广泛的 MVVM 框架应该是 Objective-C 语言实现的 RAC 框架和 Swift 语言实现的 RxSwift 框架。RAC 框架给人的第一感觉就是重，在现有的 MVC 架构项目中引入 RAC 框架基本是颠覆性的，需要学习响应式编程、函数式编程、链式编程，需要熟悉 RAC 对 UIKit 框架的封装，更遑论还有一堆基于 RAC 的衍生框架。RxSwift 则还好一点，因为 RxSwift 的实现本身非常契合 Swift 语言的特点，不过依然是有点重。总之，在传统 MVC 项目中启用 RAC 或 RxSwift，绝对不比引入新编程语言的 Flutter、RN 来得简单。</p>
<p>那么可不可以用常规的，更轻量的方式来实现 MVVM 框架层逻辑呢？通常第一个想到的就是观察者模式，恰好 Objective-C 有强大的 KVO 机制。各逻辑分工大致如下：</p>
<ul>
<li>Model：模型层；</li>
<li>View：视图层；</li>
<li>View Model：表征视图特性；</li>
<li>Controller：通过 KVO 设置 View 观察 View Model 的各个属性，则 View Model 属性值变更会驱动 View 刷新。另外，将来自 View 的用户交互触发的 Action 或者回调消息转发到 View Model 中处理；</li>
</ul>
<p>但是在实现时你会发现，KVO 是通过 Key Path 来配置的，这个 Key Path 有个很致命的弱点，它是字符串！这会有什么问题呢？想象一下，有一天你要重构代码，发现某个 View Model 属性名设置不太合理，你用 Refactor Rename 工具给这个属性重命名了，此时所有通过 KVO 绑定 View Model 的该属性的业务逻辑都会出问题，这个时候你只能再手动修改该属性的数据绑定代码中对应的 Key Path 字符串。另外，字符串终究是字符串，IDE 不能为字符串提供编译时检查以及提示，所以可以预见开发体验极差。而且我认为 KVO 比较适用于上层业务实现，如果将其下沉到框架层则很容易和上层业务逻辑发生冲突。最简单的例子，如果上层模块实现<code>observeValueForKeyPath:</code>时，没有调用<code>[super observeValueForKeyPath:]</code>，那底层的数据双向绑定框架就直接被旁路了。</p>
<p>KVO 方案被 Out 了，还有没有更好的实现方案呢？这就是下面所要探讨的问题。</p>
<h2 data-id="heading-3">三、轻量级MVVM架构方案</h2>
<p>首先要引入 Observable 和 Observer 的概念，注意这里的 Observable 和 Observer 和 RAC 和 RxSwift 中 Observable 和 Observer 并不一致，甚至有点相反的意味。</p>
<ul>
<li>Observable：可被观察对象；</li>
<li>Observer：观察者，可以订阅 Observable，当 Observable 刷新数据时，会触发 Observer 刷新；</li>
</ul>
<p>非常直观地，有了 Observable 和 Observer 就可以打通数据（View Model）驱动界面刷新的单向数据流。那么从界面的用户交互 Action 或委托回调到 View Model 的反向数据流呢？其实也是可以通过 Observable 和 Observer 来打通，因为 Action 的本质其实也是传递数据，只要将来自 View 的用户交互 Action 所传递的数据定义为 Observable，将 View Model 定义为 Observer 即可以打通反向数据流。总之：</p>
<ul>
<li>View Model 在数据驱动界面刷新数据流中扮演 Observable 的角色，此时 View 扮演 Observer 的角色；</li>
<li>View Model 在用户交互驱动数据更新数据流中扮演 Observer，View 扮演 Observable；</li>
</ul>
<p>虽然用的是观察者模式，但是这里不使用 Notification 和 KVO，而是采用最简单粗暴的方法，Observable 强持有所有订阅该 Observable 的 Observer，Observable 值更新时直接触发所有 Observer 所注册的操作逻辑。看到这里可能会有这样的疑问，这不就循环引用了么？其实并不是，因为 Observable 的数据粒度要比 View Model 和 View 低一个等级，也就是说扮演 Observable 角色是指持有若干个 Observable 成员，扮演 Observer 角色是指持有若干个 Observer 成员。这样一来，View Model 和 View 就不会存在循环引用的问题。</p>
<h3 data-id="heading-4">3.1 基本接口</h3>
<p>接下来是设计接口。首先按照 Observable 和 Observer 的定义，将其分别定义为两套协议：</p>
<p><code>Observable</code>协议定义了可被观察者的基本特征：</p>
<ul>
<li><code>Observable</code>对应一个值<code>value</code>（公开 API）；</li>
<li>可以通过调用<code>addObserver:</code>方法向<code>Observable</code>添加观察者（供<code>Observer</code>调用）；</li>
<li>可以通过调用<code>removeObserver:</code>方法从<code>Observable</code>移除观察者（供<code>Observer</code>调用）；</li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">Observer</span>;</span>
<span class="hljs-comment">/// 可观察对象，value 成员更新 setter 会驱动注册的观察者刷新。注册观察者后，观察者被可观察对象强持有</span>
<span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">Observable</span> <<span class="hljs-title">NSObject</span>></span>

<span class="hljs-comment">/// 值</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">nullable</span>) <span class="hljs-keyword">id</span> value;

<span class="hljs-comment">/// 添加观察者</span>
-(<span class="hljs-keyword">void</span>)addObserver:(<span class="hljs-keyword">id</span><Observer>)observer;

<span class="hljs-comment">/// 移除观察者</span>
-(<span class="hljs-keyword">void</span>)removeObserver:(<span class="hljs-keyword">id</span><Observer>)observer;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Observer</code>协议定义了观察者的基本特征：</p>
<ul>
<li>可以通过访问<code>subscribe</code>属性订阅<code>Observable</code>（公开 API）；</li>
<li>可以通过调用<code>invoke:</code>方法触发刷新（供<code>Observable</code>调用）；</li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">Observable</span>;</span>
<span class="hljs-comment">/// 观察者</span>
<span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">Observer</span> <<span class="hljs-title">NSObject</span>></span>

<span class="hljs-comment">/// 订阅可观察对象</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">void</span> (^subscribe)(<span class="hljs-keyword">id</span><Observable> observable);

<span class="hljs-comment">/// 触发值刷新</span>
-(<span class="hljs-keyword">void</span>)invoke:(<span class="hljs-keyword">id</span>)newValue;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于两个协议再进一步定义两个具体类型分别实现这两套协议。可以发现公开 API 都通过属性提供，之所以设计为这种形式，是为了在开发过程中使用优雅的链式调用风格。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">/// 可观察对象</span>
<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">Observable</span> : <span class="hljs-title">NSObject</span><<span class="hljs-title">Observable</span>></span>

<span class="hljs-comment">/// 构建</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">class</span>, <span class="hljs-keyword">readonly</span>) Observable *(^create)(<span class="hljs-keyword">id</span> _Nullable defaultValue);

<span class="hljs-keyword">@end</span>

<span class="hljs-comment">/// 观察者所注册的操作</span>
<span class="hljs-keyword">typedef</span> <span class="hljs-keyword">void</span>(^ObserverHandler)(<span class="hljs-keyword">id</span> newValue);

<span class="hljs-comment">/// 观察者</span>
<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">Observer</span> : <span class="hljs-title">NSObject</span> <<span class="hljs-title">Observer</span>></span>

<span class="hljs-comment">/// 构建</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">class</span>, <span class="hljs-keyword">readonly</span>) Observer *(^create)(<span class="hljs-keyword">void</span>);

<span class="hljs-comment">/// 处理值刷新</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>) Observer * (^handle)(ObserverHandler);

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.2 基本实现</h3>
<p>实现代码也非常简单，四个字概括：简单粗暴。<code>Observable</code>只管理一个值，而且必须是<code>id</code>类型。需要注意，<code>Observable</code>是具有原子性的（不是属性<code>atomic</code>那种原子性），也就是说，该框架只能区分<code>Observable</code>的值“改变”或者“不改变”，不存在<code>Observable</code>的值“只改变了其中一部分属性”这种状态。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">Observable</span> ()</span>

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSMutableArray</span> *observers;

<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">Observable</span></span>

<span class="hljs-keyword">@synthesize</span> value = _value;

-(<span class="hljs-keyword">void</span>)setValue:(<span class="hljs-keyword">id</span>)value&#123;
    <span class="hljs-keyword">if</span>(![<span class="hljs-keyword">self</span>.value isEqual:value])&#123;
        _value = value;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">id</span><Observer> observer <span class="hljs-keyword">in</span> <span class="hljs-keyword">self</span>.observers)&#123;
            [observer invoke:value];
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">static</span> Observable *(^create)(<span class="hljs-keyword">id</span>) = ^Observable *(<span class="hljs-keyword">id</span> defaultValue)&#123;
    Observable *observable = [[Observable alloc] init];
    observable.value = defaultValue;
    <span class="hljs-keyword">return</span> observable;
&#125;;

+(Observable *(^)(<span class="hljs-keyword">id</span>))create&#123;
    <span class="hljs-keyword">return</span> create;
&#125;


-(<span class="hljs-keyword">void</span>)addObserver:(<span class="hljs-keyword">id</span><Observer>)observer&#123;
    [<span class="hljs-keyword">self</span>.observers addObject:observer];
&#125;

-(<span class="hljs-keyword">void</span>)removeObserver:(<span class="hljs-keyword">id</span><Observer>)observer&#123;
    [<span class="hljs-keyword">self</span>.observers removeObject:observer];
&#125;

-(<span class="hljs-built_in">NSMutableArray</span> *)observers&#123;
    <span class="hljs-keyword">if</span>(!_observers)&#123;
        _observers = [[<span class="hljs-built_in">NSMutableArray</span> alloc] init];
    &#125;
    <span class="hljs-keyword">return</span> _observers;
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Observer</code>实现同样简单粗暴。观察者持有一个 Block，<code>Observer</code>的<code>invoke:</code>方法只是简单调用了该 Block。在<code>Observer</code>订阅<code>Observable</code>时需要指定该 Block 的实现。问题又来了，这不就有循环引用的风险了么？没错，就是<strong>有循环引用的风险</strong>。但是只需要在调用<code>subscribe</code>时，在 Block 实现中使用<code>__weak</code>和<code>__strong</code>避免强引用<code>self</code>即可，就是基本的 Block 防止循环引用的套路。<strong>虽然套路简单，但是需要注意这条规则一定要遵循</strong>。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">Observer</span> ()</span>

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>) Observer * (^handle)(ObserverHandler);

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>) ObserverHandler handler;

<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">Observer</span></span>

<span class="hljs-keyword">@synthesize</span> subscribe = _subscribe;

-(<span class="hljs-keyword">void</span> (^)(<span class="hljs-keyword">id</span><Observable>))subscribe&#123;
    <span class="hljs-keyword">if</span>(!_subscribe)&#123;
        __<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
        _subscribe = ^(<span class="hljs-keyword">id</span><Observable> observable)&#123;
            __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(weakSelf) strongSelf = weakSelf;
            [observable addObserver:strongSelf];
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> _subscribe;
&#125;

-(<span class="hljs-keyword">void</span>)invoke:(<span class="hljs-keyword">id</span>)newValue&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">self</span>.handler)&#123;
        <span class="hljs-keyword">self</span>.handler(newValue);
    &#125;
&#125;

<span class="hljs-keyword">static</span> Observer *(^create)(<span class="hljs-keyword">void</span>) = ^Observer *()&#123;
    Observer *observer = [[Observer alloc] init];
    <span class="hljs-keyword">return</span> observer;
&#125;;

+(Observer *(^)(<span class="hljs-keyword">void</span>))create&#123;
    <span class="hljs-keyword">return</span> create;
&#125;

-(Observer * (^)(ObserverHandler))handle&#123;
    <span class="hljs-keyword">if</span>(!_handle)&#123;
        __<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
        _handle = ^Observer *(ObserverHandler handler)&#123;
            __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(weakSelf) strongSelf = weakSelf;
            strongSelf.handler = handler;
            <span class="hljs-keyword">return</span> strongSelf;
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> _handle;
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.3 能力扩展</h3>
<p>基本实现框架有了，不过仅有<code>Observable</code>和<code>Observer</code>的话，貌似只能组织最简单的数据流拓扑，即从单个<code>Observable</code>分发到多个<code>Observer</code>，其实开发过程中还希望具备多个<code>Observable</code>合成单个<code>Observable</code>的能力。为此定义<code>ObservableCombiner</code>用于实现<code>Observable</code>合成。</p>
<p><code>ObservableCombiner</code>继承<code>Observable</code>类型，可以通过调用其<code>combine</code>属性合成多个<code>Observable</code>，同时<code>ObservableCombiner</code>具备一定<code>Observer</code>的特征（但不是遵循<code>Observer</code>协议），其<code>handle</code>和<code>Observer</code>的<code>subscribe</code>是相同的原理，只是传参上，前者是<code>NSArray</code>表示所有合成<code>Observable</code>的值的数组。当合成的<code>Observable</code>值更新时，会触发<code>handle</code>所注册的 Block。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">/// 合成可观察对象的触发策略</span>
<span class="hljs-keyword">typedef</span> <span class="hljs-built_in">NS_ENUM</span>(<span class="hljs-built_in">NSUInteger</span>, CombineStrategy) &#123;
    <span class="hljs-comment">/// 第一次值更新才刷新</span>
    CombineStrategyFirst,
    <span class="hljs-comment">/// 所有值更新才刷新</span>
    CombineStrategyAll,
    <span class="hljs-comment">/// 任何值更新均刷新</span>
    CombineStrategyEvery,
&#125;;

<span class="hljs-comment">/// 合成可观察对象处理值刷新</span>
<span class="hljs-keyword">typedef</span> _Nullable <span class="hljs-keyword">id</span> (^CombinerHandler)(<span class="hljs-built_in">NSArray</span> *newValues);

<span class="hljs-comment">/// 合成多个可观察对象</span>
<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">ObservableCombiner</span> : <span class="hljs-title">Observable</span></span>

<span class="hljs-comment">/// 安全获取值</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>, <span class="hljs-keyword">class</span>) <span class="hljs-keyword">id</span> _Nullable (^safeValue)(<span class="hljs-built_in">NSArray</span> *, <span class="hljs-built_in">NSInteger</span>);

<span class="hljs-comment">/// 构建</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>, <span class="hljs-keyword">class</span>) ObservableCombiner *(^create)(CombineStrategy strategy);

<span class="hljs-comment">/// 合并可观察对象</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>) ObservableCombiner * (^combine)(<span class="hljs-keyword">id</span><Observable> observable);

<span class="hljs-comment">/// 处理值刷新</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>) ObservableCombiner * (^handle)(CombinerHandler);

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现代码直接贴在文章最后，这里不作详细介绍了。</p>
<blockquote>
<p>后面再尝试扩展支持从多个<code>Observable</code>映射到多个<code>Observable</code>的能力。</p>
</blockquote>
<h2 data-id="heading-7">四、轻量级MVVM框架Demo</h2>
<p>基于该框架的开发同样需要以组织数据流的思想作为指导，框架提供的公开 API 基本是用于组织数据流，核心操作是构建（create）、订阅（subscribe）和处理（handle）。为便于描述将 View Model 驱动 View 刷新数据流简称为<strong>正向数据流</strong>，将来自 View 的界面交互动作驱动 View Model 更新数据流简称为<strong>反向数据流</strong>，代码逻辑分布基本如下：</p>
<ul>
<li>View Model：
<ul>
<li>构建正向数据流的 Observable；</li>
<li>构建正向数据流的合成 Observable；</li>
<li>处理正向数据流的合成 Observable；</li>
<li>构建反向数据流的 Observer；</li>
<li>处理反向数据流的 Observer；（交互驱动数据刷新）</li>
</ul>
</li>
<li>View：
<ul>
<li>构建反向数据流的 Observable；</li>
<li>构建反向数据流的合成 Observable；</li>
<li>处理反向数据流的合成 Observable；</li>
</ul>
</li>
<li>Controller：
<ul>
<li>订阅正向数据流的 Observable；</li>
<li>订阅反向数据流的 Observable；</li>
<li>构建正向数据流的 Observer；</li>
<li>处理正向数据流的 Observer（数据驱动视图刷新）；</li>
</ul>
</li>
</ul>
<p>看起来很绕，实际上原则可以归结为四条：</p>
<ul>
<li>在数据流来源构建 Observable；</li>
<li>在 Controller 中订阅 Observable；</li>
<li>在数据流终点处理 Observable；</li>
<li>在数据流终点构建 Observer；</li>
</ul>
<blockquote>
<p>注意：虽然在 Controller 中处理正向数据流，但是处理逻辑必须是非常简单的操作，基本是原子操作，符合操作可以通过在 View 层定义并实现接口，对外向 Controller 提供。其实最合理的布局是在 View 中构建和处理正向数据流 Observer，不过当 View Model 可以提供非常熟成的数据时，Controller 通过一两句代码就可以调起 View 刷新视图，则没有必要因此引入实现逻辑过于简单的新接口。</p>
</blockquote>
<p>接下来以登录业务来演示轻量级 MVVM 框架的使用。业务描述如下：</p>
<ul>
<li>用户名必须超过 6 个字节不能超过 24 个字节；</li>
<li>密码必须超过 6 个字节不能超过 24 个字节；</li>
<li>用户名和密码不合法时登录按钮不可点击；</li>
<li>用户名和密码不合法时给出相应提示，优先显示用户名的错误提示；</li>
</ul>
<p>首先定义 View Model：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">LoginViewModel</span> : <span class="hljs-title">NSObject</span></span>

<span class="hljs-comment">//MARK: 数据驱动UI刷新</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *username;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *password;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *instruction;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) ObservableCombiner *usernameValid;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) ObservableCombiner *passwordValid;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) ObservableCombiner *loginEnabled;

<span class="hljs-comment">//MARK: 用户交互动作订阅</span>
<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observer *usernameDidChange;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observer *passwordDidChange;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observer *loginTouched;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次定义 View：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">LoginView</span> : <span class="hljs-title">UIView</span></span>

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">UITextField</span> *usernameTextField;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">UITextField</span> *passwordTextField;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">UILabel</span> *instructionLabel;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">UIButton</span> *loginButton;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *usernameDidChange;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *passwordDidChange;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) Observable *loginButtonTouched;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.1 数据流组织</h3>
<p>正向数据流组织及反向数据流处理是 View Model 的核心逻辑。组织正向数据流的代码如下，通过代码可以非常直观地阅读出以下关键信息，从而生成非常清晰的正向数据流拓扑：</p>
<ul>
<li><code>usernameValid</code>依赖于<code>username</code>和<code>passwordValid</code>的值；</li>
<li><code>passwordValid</code>依赖于<code>password</code>和<code>usernameValid</code>的值；</li>
<li><code>loginEnabled</code>依赖于<code>usernameValid</code>和<code>passwordValid</code>的值；</li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc">-(<span class="hljs-keyword">void</span>)doDataWeaving&#123;
    <span class="hljs-keyword">self</span>.usernameValid
        .combine(<span class="hljs-keyword">self</span>.username)
        .combine(<span class="hljs-keyword">self</span>.passwordValid)
        .handle(^<span class="hljs-keyword">id</span> _Nullable(<span class="hljs-built_in">NSArray</span> * _Nonnull newValues) &#123;
            <span class="hljs-built_in">NSString</span> *username = ObservableCombiner.safeValue(newValues, <span class="hljs-number">0</span>);
            <span class="hljs-keyword">if</span>(!username.length)&#123;
                <span class="hljs-keyword">self</span>.instruction.value = <span class="hljs-string">@"*用户名不能为空"</span>;
                <span class="hljs-keyword">return</span> @(<span class="hljs-literal">NO</span>);
            &#125;
            
            <span class="hljs-keyword">if</span>(username.length < <span class="hljs-number">6</span>)&#123;
                <span class="hljs-keyword">self</span>.instruction.value = <span class="hljs-string">@"*用户名必须超过6个字符"</span>;
                <span class="hljs-keyword">return</span> @(<span class="hljs-literal">NO</span>);
            &#125;
            
            <span class="hljs-keyword">if</span>(username.length > <span class="hljs-number">24</span>)&#123;
                <span class="hljs-keyword">self</span>.instruction.value = <span class="hljs-string">@"*用户名不能超过24个字符"</span>;
                <span class="hljs-keyword">return</span> @(<span class="hljs-literal">NO</span>);
            &#125;
            
            <span class="hljs-built_in">BOOL</span> passwordValid = [ObservableCombiner.safeValue(newValues, <span class="hljs-number">1</span>) boolValue];
            <span class="hljs-keyword">if</span>(passwordValid)&#123;
                <span class="hljs-keyword">self</span>.instruction.value = <span class="hljs-string">@""</span>;
            &#125;
            <span class="hljs-keyword">return</span> @(<span class="hljs-literal">YES</span>);
        &#125;);
    
    <span class="hljs-keyword">self</span>.passwordValid
        .combine(<span class="hljs-keyword">self</span>.usernameValid)
        .combine(<span class="hljs-keyword">self</span>.password)
        .handle(^<span class="hljs-keyword">id</span> _Nullable(<span class="hljs-built_in">NSArray</span> * _Nonnull newValues) &#123;
            <span class="hljs-built_in">NSString</span> *password = ObservableCombiner.safeValue(newValues, <span class="hljs-number">1</span>);
            <span class="hljs-built_in">BOOL</span> usernameValid = [ObservableCombiner.safeValue(newValues, <span class="hljs-number">0</span>) boolValue];
            
            <span class="hljs-built_in">BOOL</span> passwordValid;
            <span class="hljs-built_in">NSString</span> *passwordInstruction;
            <span class="hljs-keyword">if</span>(!password.length)&#123;
                passwordInstruction = <span class="hljs-string">@"*密码不能为空"</span>;
                passwordValid = <span class="hljs-literal">NO</span>;
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(password.length < <span class="hljs-number">6</span>)&#123;
                passwordInstruction = <span class="hljs-string">@"*密码必须超过6个字符"</span>;
                passwordValid = <span class="hljs-literal">NO</span>;
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(password.length > <span class="hljs-number">24</span>)&#123;
                passwordInstruction = <span class="hljs-string">@"*密码不能超过24个字符"</span>;
                passwordValid = <span class="hljs-literal">NO</span>;
            &#125;<span class="hljs-keyword">else</span>&#123;
                passwordInstruction = <span class="hljs-string">@""</span>;
                passwordValid = <span class="hljs-literal">YES</span>;
            &#125;
            
            <span class="hljs-keyword">if</span>(usernameValid)&#123;
                <span class="hljs-keyword">self</span>.instruction.value = passwordInstruction;
            &#125;
            <span class="hljs-keyword">return</span> @(passwordValid);
        &#125;);
    
    <span class="hljs-keyword">self</span>.loginEnabled
        .combine(<span class="hljs-keyword">self</span>.usernameValid)
        .combine(<span class="hljs-keyword">self</span>.passwordValid)
        .handle(^<span class="hljs-keyword">id</span> _Nullable(<span class="hljs-built_in">NSArray</span> * _Nonnull newValues) &#123;
            <span class="hljs-built_in">BOOL</span> usernameValid = [ObservableCombiner.safeValue(newValues, <span class="hljs-number">0</span>) boolValue];
            <span class="hljs-built_in">BOOL</span> passworkValid = [ObservableCombiner.safeValue(newValues, <span class="hljs-number">1</span>) boolValue];
            <span class="hljs-keyword">return</span> @(usernameValid && passworkValid);
        &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理反向数据流的代码如下，代码比较简单不作赘述：</p>
<pre><code class="hljs language-objc copyable" lang="objc">-(<span class="hljs-keyword">void</span>)doActionHandlings&#123;
    WS
    <span class="hljs-comment">// 用户交互处理</span>
    <span class="hljs-keyword">self</span>.usernameDidChange = Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.username.value = newValue;
    &#125;);
    <span class="hljs-keyword">self</span>.passwordDidChange = Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.password.value = newValue;
    &#125;);
    <span class="hljs-keyword">self</span>.loginTouched = Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        <span class="hljs-keyword">self</span>.instruction.value = [<span class="hljs-built_in">NSString</span> stringWithFormat:<span class="hljs-string">@"登录成功(*^▽^*)"</span>];
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.2 订阅的实现</h3>
<p>订阅是 Controller 绝对的核心逻辑，包括正向数据流和反向数据流订阅。正向数据流订阅的实现代码如下，包括：</p>
<ul>
<li>正向数据流 Observable 订阅；</li>
<li>正向数据流 Observer 构建及处理；</li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">/// 数据驱动UI刷新</span>
-(<span class="hljs-keyword">void</span>)doDataBindings&#123;
    WS
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.usernameTextField.text = newValue;
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.username);
    
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.passwordTextField.text = newValue;
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.password);
    
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.instructionLabel.text = newValue;
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.instruction);
    
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.usernameTextField.backgroundColor = [newValue boolValue] ? [<span class="hljs-built_in">UIColor</span> whiteColor] : LightRed;
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.usernameValid);
    
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.passwordTextField.backgroundColor = [newValue boolValue] ? [<span class="hljs-built_in">UIColor</span> whiteColor] : LightRed;
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.passwordValid);
    
    Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
        SS
        <span class="hljs-keyword">self</span>.loginView.loginButton.enabled = [newValue boolValue];
        <span class="hljs-keyword">self</span>.loginView.loginButton.backgroundColor = [newValue boolValue] ? ThemeColor : LightGray;
        [<span class="hljs-keyword">self</span>.loginView.loginButton setTitleColor:[newValue boolValue] ? [<span class="hljs-built_in">UIColor</span> whiteColor] : [<span class="hljs-built_in">UIColor</span> darkGrayColor] forState:<span class="hljs-built_in">UIControlStateNormal</span>];
    &#125;).subscribe(<span class="hljs-keyword">self</span>.loginViewModel.loginEnabled);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>反向数据流订阅的实现代码如下；</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">/// 用户交互动作订阅</span>
-(<span class="hljs-keyword">void</span>)doActionBindings&#123;
    <span class="hljs-keyword">self</span>.loginViewModel.usernameDidChange.subscribe(<span class="hljs-keyword">self</span>.loginView.usernameDidChange);
    
    <span class="hljs-keyword">self</span>.loginViewModel.passwordDidChange.subscribe(<span class="hljs-keyword">self</span>.loginView.passwordDidChange);
    
    <span class="hljs-keyword">self</span>.loginViewModel.loginTouched.subscribe(<span class="hljs-keyword">self</span>.loginView.loginButtonTouched);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码上看，不难发现，该框架是一点都不省代码，同等的 MVC 架构实现比上面的实现在代码空间行数上少 50% 左右，但是基于该框架实现的业务代码数据流非常清晰，代码逻辑分布更加均匀，View Model 处理纯粹的业务逻辑，也非常契合引入 Manager 和 Service 模块分流数据管理负担的优化方式。</p>
<h2 data-id="heading-10">五、总结</h2>
<p>虽然只定义了<code>Observable</code>、<code>Observer</code>、<code>ObservableCombiner</code>，但是它已经具备了构建 MVVM 架构的基本能力了。首先，肉眼可见的，它足够轻量。其次，不存在前文所述 KVO 方案的缺陷。最后，它麻雀虽小，其实五脏俱全，正确使用该框架可以获得漂亮工整的代码逻辑结构。在后面 Demo 开发过程中实际应用该框架时，感觉开发体验总体还是不错的。</p>
<p>当然本方案还是有非常明显的缺陷的，例如：</p>
<ul>
<li><code>Observable</code>值类型只支持<code>id</code>类型；</li>
<li>组织数据流拓扑结构支持还存在不小的缺失；</li>
<li>存在冗余的数据刷新次数；</li>
<li>实现代码增幅十分明显，本文 Demo 相对 MVC 架构同等实现，代码行数增加了 50%（空间行数）；</li>
<li>调试过程中数据流向跟踪困难；</li>
<li>订阅时需要避免 Block 循环引用问题；</li>
</ul>
<p>总之，本文的轻量级 MVVM 框架方案可以用来体验 iOS 客户端开发中的 MVVM 架构模式的应用，或者理解 MVVM 架构的原理。本方案优点和缺点同等明显，由于目前缺乏完备的测试，以及对复杂业务场景的实践案例支撑，<strong>暂时不打算直接应用到开发项目中</strong>。</p>
<h2 data-id="heading-11">附录</h2>
<p>ObservableCombiner 实现代码如下。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">// ObservableCombiner.m</span>

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">ObservableCombiner</span> ()</span>

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">strong</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSMutableArray</span> *observables;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">assign</span>, <span class="hljs-keyword">nonatomic</span>) CombineStrategy strategy;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">assign</span>, <span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSUInteger</span> accessFlags;

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>) ObservableCombiner * (^combine)(<span class="hljs-keyword">id</span><Observable> observable);

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>) ObservableCombiner * (^handle)(CombinerHandler);

<span class="hljs-keyword">@property</span>(<span class="hljs-keyword">copy</span>, <span class="hljs-keyword">nonatomic</span>) CombinerHandler handler;

<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">ObservableCombiner</span></span>

<span class="hljs-keyword">static</span> ObservableCombiner *(^create)(CombineStrategy strategy) = ^ObservableCombiner *(CombineStrategy strategy)&#123;
    ObservableCombiner *combiner = [[ObservableCombiner alloc] init];
    combiner.strategy = strategy;
    <span class="hljs-keyword">return</span> combiner;
&#125;;

+(ObservableCombiner *(^)(CombineStrategy))create&#123;
    <span class="hljs-keyword">return</span> create;
&#125;

-(ObservableCombiner * (^)(<span class="hljs-keyword">id</span><Observable>))combine&#123;
    <span class="hljs-keyword">if</span>(!_combine)&#123;
        __<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
        _combine = ^ObservableCombiner * (<span class="hljs-keyword">id</span><Observable> observable)&#123;
            __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(weakSelf) strongSelf = weakSelf;
            
            <span class="hljs-built_in">NSInteger</span> index = strongSelf.observables.count;
            <span class="hljs-keyword">id</span><Observer> observer = Observer.create().handle(^(<span class="hljs-keyword">id</span>  _Nonnull newValue) &#123;
                __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(weakSelf) strongSelf = weakSelf;
                [strongSelf handleNewValue:newValue index:index];
            &#125;);
            
            [observable addObserver:observer];
            [strongSelf.observables addObject:observable];
            <span class="hljs-keyword">return</span> strongSelf;
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> _combine;
&#125;

-(ObservableCombiner * (^)(CombinerHandler))handle&#123;
    <span class="hljs-keyword">if</span>(!_handle)&#123;
        __<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
        _handle = ^ObservableCombiner *(CombinerHandler handler)&#123;
            __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(weakSelf) strongSelf = weakSelf;
            strongSelf.handler = handler;
            <span class="hljs-keyword">return</span> strongSelf;
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> _handle;
&#125;

-(<span class="hljs-built_in">NSMutableArray</span> *)observables&#123;
    <span class="hljs-keyword">if</span>(!_observables)&#123;
        _observables = [[<span class="hljs-built_in">NSMutableArray</span> alloc] init];
    &#125;
    <span class="hljs-keyword">return</span> _observables;
&#125;

-(<span class="hljs-keyword">void</span>)handleNewValue:(<span class="hljs-keyword">id</span>)newValue index:(<span class="hljs-built_in">NSInteger</span>)index&#123;
    <span class="hljs-comment">// 根据不同的策略触发完成事件</span>
    <span class="hljs-built_in">BOOL</span> isFirst = !<span class="hljs-keyword">self</span>.accessFlags;
    <span class="hljs-keyword">self</span>.accessFlags |= (<span class="hljs-number">1</span> << index);
    <span class="hljs-keyword">switch</span> (<span class="hljs-keyword">self</span>.strategy) &#123;
        <span class="hljs-keyword">case</span> CombineStrategyFirst:&#123;
            <span class="hljs-keyword">if</span>(isFirst)&#123;
                <span class="hljs-keyword">self</span>.value = <span class="hljs-keyword">self</span>.handler([<span class="hljs-keyword">self</span> getAllValues]);
            &#125;
        &#125;<span class="hljs-keyword">break</span>;
        
        <span class="hljs-keyword">case</span> CombineStrategyEvery:&#123;
            <span class="hljs-keyword">self</span>.value = <span class="hljs-keyword">self</span>.handler([<span class="hljs-keyword">self</span> getAllValues]);
        &#125;<span class="hljs-keyword">break</span>;
        
        <span class="hljs-keyword">case</span> CombineStrategyAll:&#123;
            <span class="hljs-built_in">NSUInteger</span> allFlags = pow(<span class="hljs-number">2</span>, <span class="hljs-keyword">self</span>.observables.count) - <span class="hljs-number">1</span>;
            <span class="hljs-built_in">BOOL</span> isAll = (allFlags & <span class="hljs-keyword">self</span>.accessFlags) == allFlags;
            <span class="hljs-keyword">if</span>(isAll)&#123;
                <span class="hljs-keyword">self</span>.value = <span class="hljs-keyword">self</span>.handler([<span class="hljs-keyword">self</span> getAllValues]);
            &#125;
        &#125;<span class="hljs-keyword">break</span>;
            
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">break</span>;
    &#125;
&#125;

-(<span class="hljs-built_in">NSArray</span> *)getAllValues&#123;
    <span class="hljs-built_in">NSMutableArray</span> *result = [[<span class="hljs-built_in">NSMutableArray</span> alloc] init];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">id</span><Observable> observable <span class="hljs-keyword">in</span> <span class="hljs-keyword">self</span>.observables)&#123;
        [result addObject:observable.value ?: [<span class="hljs-built_in">NSNull</span> null]];
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-keyword">id</span> _Nullable (^safeValue)(<span class="hljs-built_in">NSArray</span> *, <span class="hljs-built_in">NSInteger</span>) = ^<span class="hljs-keyword">id</span> (<span class="hljs-built_in">NSArray</span> *values, <span class="hljs-built_in">NSInteger</span> index)&#123;
    <span class="hljs-keyword">return</span> values[index] == [<span class="hljs-built_in">NSNull</span> null] ? <span class="hljs-literal">nil</span> : values[index];
&#125;;

+(<span class="hljs-keyword">id</span>  _Nullable (^)(<span class="hljs-built_in">NSArray</span> * _Nonnull, <span class="hljs-built_in">NSInteger</span>))safeValue&#123;
    <span class="hljs-keyword">return</span> safeValue;
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            