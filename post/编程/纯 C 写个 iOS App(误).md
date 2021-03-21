
---
title: 纯 C 写个 iOS App(误)
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Tue, 23 Feb 2021 06:22:35 GMT
thumbnail: https://user-gold-cdn.xitu.io/2020/2/26/1708075eb52fc0cd?imageView2/0/w/1280/h/960/ignore-error/1
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><p>一个 <strong>iOS app</strong> 首先是由 <code>main.m</code> 内的 main 函数开始的. 现在就先创建 <strong>Single View App</strong> 项目, 然后把所有的 <code>.m</code> 文件都删掉, 建一个 <code>main.c</code> 文件.<br>
通常我们看到的 <code>main.m</code> 的内的代码是这样的</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">// main.m</span>
<span class="hljs-meta">#import <span class="hljs-meta-string"><UIKit/UIKit.h></span></span>
<span class="hljs-meta">#import <span class="hljs-meta-string">"AppDelegate.h"</span></span>

<span class="hljs-keyword">int</span> main(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> * argv[]) {
    <span class="hljs-keyword">@autoreleasepool</span> {
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">UIApplicationMain</span>(argc, argv, <span class="hljs-literal">nil</span>, <span class="hljs-built_in">NSStringFromClass</span>([AppDelegate <span class="hljs-keyword">class</span>]));
    }
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那先照着这个写就好了, 但是这个 <code>@autoreleasepool</code> 这个怎么处理?<br>
我们晓得这是个语法糖, 在 ARC 出来之后编译器就不让我们使用 NSAutoreleasePool, 原先是这样的</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-built_in">NSAutoreleasePool</span> *pool = [[<span class="hljs-built_in">NSAutoreleasePool</span> alloc] init];
[pool release];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那就仿照着这玩意写成 <strong>C</strong> 版本的</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> **argv)</span> </span>{
    id pool = objc_msgSend(
            objc_msgSend((id) objc_getClass(<span class="hljs-string">"NSAutoreleasePool"</span>),
            sel_registerName(<span class="hljs-string">"alloc"</span>)),
            sel_registerName(<span class="hljs-string">"init"</span>));
    UIApplicationMain(argc, argv, nil, CFSTR(<span class="hljs-string">"AppDelegate"</span>));
    objc_msgSend(pool, sel_registerName(<span class="hljs-string">"drain"</span>));
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>CFSTR</code> 这个宏可以从 <strong>C</strong> 字符串创建一个 <code>CFString</code> 的引用(<code>CFStringRef</code>), 这玩意可以用来代替我们这里的 <code>NSStringFromClass([AppDelegate class])</code>.</p>
<p>现在已经抄作业抄了一个 <code>main.c</code>, 不过还有个问题, <code>UIApplicationMain</code> 这个函数从哪里跑出来的.<br>
这个是一个用于创建我们应用实例的函数, 但是我们没法直接使用它, 因为它是在 <code>UIApplication.h</code> 文件, 不过我们可以这样搞(这里顺便把 <strong>runtime</strong> 那些头文件补上吧)</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><CoreFoundation/CoreFoundation.h></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><objc/runtime.h></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><objc/message.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">extern</span> <span class="hljs-keyword">int</span> <span class="hljs-title">UIApplicationMain</span><span class="hljs-params">(<span class="hljs-keyword">int</span>, ...)</span></span>;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> **argv)</span> </span>{
    id pool = objc_msgSend(
            objc_msgSend((id) objc_getClass(<span class="hljs-string">"NSAutoreleasePool"</span>),
            sel_registerName(<span class="hljs-string">"alloc"</span>)),
            sel_registerName(<span class="hljs-string">"init"</span>));
    UIApplicationMain(argc, argv, nil, CFSTR(<span class="hljs-string">"AppDelegate"</span>));
    objc_msgSend(pool, sel_registerName(<span class="hljs-string">"drain"</span>));
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里再讲一下 <code>UIApplicationMain</code> 这个函数, 它虽然有 <code>int</code> 类型的返回值, 但是它永远不会返回.</p>
<p>然后这玩意的前两个参数就不管了, 就是处理一下 <code>main</code> 函数传进来的参数, 第三个参数是需要传入 <code>UIApplication</code> 或者其子类的名称, 这里传 <code>nil</code> 就默认用 <code>UIApplication</code>.<br>
我们需要关注的是最后一个参数, 这个参数让我们传一个代理类的字符串, 就是给应用设置个代理, 也就是讲接下来我们要实现一个代理类.</p>
<p>所以我们现在来创建个 <code>AppDelegate.c</code> 的文件. 继续照之前的套路走, 先看 <code>AppDelegate.m</code> 代码, <code>AppDelegate</code> 这个类有个 <code>window</code> 的属性, 有下面这个函数</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-built_in">BOOL</span>)application:(<span class="hljs-built_in">UIApplication</span> *)application didFinishLaunchingWithOptions:(<span class="hljs-built_in">NSDictionary</span> *)launchOptions {
    <span class="hljs-keyword">return</span> <span class="hljs-literal">YES</span>;
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先得实现一个 <code>AppDelegate</code> <strong>class</strong> 才行. 一般稍微了解过 <code>NSObject</code> 定义的都晓得, 每个类有个 <code>isa</code> 用来标记这个类是什么, 具体怎样就不解释了, 反正很多 <strong>runtime</strong> 以及 <code>header</code> 文件的定义都能找到.</p>
<p>除了搞个 <strong>class</strong>, 我们还要实现那个 <code>application:didFinishLaunchingWithOptions:</code> 函数</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// AppDelegate.c</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><objc/runtime.h></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><objc/message.h></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><CoreGraphics/CoreGraphics.h></span></span>

<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AppDelegate</span> {</span>
    Class isa;
    id window;
} AppDelegate;

Class AppDelegateClass;

<span class="hljs-function">BOOL <span class="hljs-title">applicationDidFinishLaunchingWithOptions</span><span class="hljs-params">(
        AppDelegate *self, SEL _cmd, <span class="hljs-keyword">void</span> *application, <span class="hljs-keyword">void</span> *options)</span> </span>{
    self->window = objc_msgSend((id) objc_getClass(<span class="hljs-string">"UIWindow"</span>), sel_getUid(<span class="hljs-string">"alloc"</span>));
    self->window = objc_msgSend(self->window, sel_getUid(<span class="hljs-string">"initWithFrame:"</span>),
            (struct CGRect) {<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">320</span>, <span class="hljs-number">568</span>});
    id viewController = objc_msgSend(
            objc_msgSend((id) objc_getClass(<span class="hljs-string">"UIViewController"</span>), sel_getUid(<span class="hljs-string">"alloc"</span>)),
            sel_getUid(<span class="hljs-string">"init"</span>));
    id view = objc_msgSend(
            objc_msgSend((id) objc_getClass(<span class="hljs-string">"View"</span>), sel_getUid(<span class="hljs-string">"alloc"</span>)),
            sel_getUid(<span class="hljs-string">"initWithFrame:"</span>),
            (struct CGRect) {<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">320</span>, <span class="hljs-number">568</span>});
    objc_msgSend(objc_msgSend(viewController, sel_getUid(<span class="hljs-string">"view"</span>)), sel_getUid(<span class="hljs-string">"addSubview:"</span>), view);
    objc_msgSend(self->window, sel_getUid(<span class="hljs-string">"setRootViewController:"</span>), viewController);
    objc_msgSend(self->window, sel_getUid(<span class="hljs-string">"makeKeyAndVisible"</span>));

    <span class="hljs-keyword">return</span> YES;
}
__attribute__((constructor))
<span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initAppDelegate</span><span class="hljs-params">()</span> </span>{
    AppDelegateClass = objc_allocateClassPair((Class) objc_getClass(<span class="hljs-string">"UIResponder"</span>), <span class="hljs-string">"AppDelegate"</span>, <span class="hljs-number">0</span>);
    class_addIvar(AppDelegateClass, <span class="hljs-string">"window"</span>, <span class="hljs-keyword">sizeof</span>(id), <span class="hljs-number">0</span>, <span class="hljs-string">"@"</span>);
<span class="hljs-comment">//    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions</span>
    class_addMethod(AppDelegateClass, sel_registerName(<span class="hljs-string">"application:didFinishLaunchingWithOptions:"</span>), (IMP) applicationDidFinishLaunchingWithOptions, <span class="hljs-string">"i@:@@"</span>);
    objc_registerClassPair(AppDelegateClass);
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里通过 <code>__attribute__((constructor))</code> 这个编译属性让这个函数在 <code>main</code> 函数之前走. 通过 <strong>runtime</strong> 搞了个 <code>AppDelegateClass</code> 出来. 由于我比较穷, 手机还是 iPhone 5s, 所以设了 <code>(struct CGRect) {0, 0,320, 568})</code>.</p>
<p>通过引入 <code>CoreGraphics.h</code> 才可以让编译通过 <code>CGRect</code>.<br>
现在了解到创建一个 <strong>class</strong> 的套路之后, 这里在 <code>applicationDidFinishLaunchingWithOptions</code> 使用到了 <code>View</code> <strong>class</strong>, 我们就创建一个 View.c 文件来自定义视图什么</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// View.c</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><objc/runtime.h></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><CoreGraphics/CoreGraphics.h></span></span>

Class ViewClass;

<span class="hljs-function"><span class="hljs-keyword">extern</span> CGContextRef <span class="hljs-title">UIGraphicsGetCurrentContext</span><span class="hljs-params">()</span></span>;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">viewDrawRect</span><span class="hljs-params">(id self, SEL _cmd, CGRect rect)</span> </span>{
    CGContextRef context = UIGraphicsGetCurrentContext();

    CGContextSetFillColor(context, (CGFloat[]) {<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>});
    CGContextAddRect(context, (struct CGRect) {<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">320</span>, <span class="hljs-number">568</span>});
    CGContextFillPath(context);
}

__attribute__((constructor))
<span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initView</span><span class="hljs-params">()</span> </span>{
    ViewClass = objc_allocateClassPair((Class) objc_getClass(<span class="hljs-string">"UIView"</span>), <span class="hljs-string">"View"</span>, <span class="hljs-number">0</span>);
    class_addMethod(ViewClass, sel_getUid(<span class="hljs-string">"drawRect:"</span>), (IMP) viewDrawRect, <span class="hljs-string">"v@:"</span>);
    objc_registerClassPair(ViewClass);
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里直接用 <code>CoreGraphics</code> 来绘制视图.</p>
<p>然后编译执行看看效果, 应该是一个空白的红色视图. 如果编译出错了, 可能是现在的 <strong>Xcode</strong> 禁止 <code>objc_msgSend</code> 函数的调用, 在 <strong>Build Settings</strong> 启用它就好了.</p>
<p><img alt="设置 Xcode objc_msgSend" class="lazyload" src="https://user-gold-cdn.xitu.io/2020/2/26/1708075eb52fc0cd?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="289" referrerpolicy="no-referrer"></p>
<p>忘了还有个事要做, 那就是把这几个东西导入到项目中</p>
<p><img alt="导入库" class="lazyload" src="https://user-gold-cdn.xitu.io/2020/2/26/17080764e701e1f5?imageView2/0/w/1280/h/960/ignore-error/1" data-width="458" data-height="122" referrerpolicy="no-referrer"></p>
<p>其实就是通过 <strong>runtime</strong> 来各种调用函数, 这个拿来玩玩就好了. 好吧, 先这样吧.</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            