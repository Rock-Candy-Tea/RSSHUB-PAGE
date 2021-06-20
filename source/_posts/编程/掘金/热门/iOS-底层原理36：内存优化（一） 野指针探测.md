
---
title: 'iOS-底层原理36：内存优化（一） 野指针探测'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05dfee0d05264912a585e077cf2007ba~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 21:57:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05dfee0d05264912a585e077cf2007ba~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p><a href="https://juejin.cn/post/6949574423837933575" target="_blank">iOS 底层原理 文章汇总</a></p>
</blockquote>
<p>本文主要讲解两种野指针检测的原理及实现</p>
<h1 data-id="heading-0">技术点：野指针探测</h1>
<p>本文的主要目的是理解野指针的形成过程以及如何去检测野指针</p>
<h2 data-id="heading-1">引子</h2>
<p>在介绍野指针之前，首先说下目前的异常处理类型，附上<a href="https://developer.apple.com/documentation/xcode/understanding-the-exception-types-in-a-crash-report" target="_blank" rel="nofollow noopener noreferrer">苹果官网链接</a>）</p>
<h3 data-id="heading-2">异常类型</h3>
<p>异常大致可以分为两类：</p>
<ul>
<li>
<p>1、<code>软件异常</code>：主要是来自kill()、pthread_kill()、iOS中的NSException未捕获、absort等</p>
</li>
<li>
<p>2、<code>硬件异常</code>：硬件的信号始于处理器trap，是和平台相关的，野指针崩溃大部分是硬件异常</p>
</li>
</ul>
<p>而在处理异常时，需要关注两个概念</p>
<ul>
<li><code>Mach异常</code>：<code>Mach层</code>捕获</li>
<li><code>UNIX信号</code>：<code>BSD层</code>获取</li>
</ul>
<p>iOS中的POSIX API就是通过Mach之上的BSD层实现的，如下图所示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05dfee0d05264912a585e077cf2007ba~tplv-k3u1fbpfcp-zoom-1.image" alt="层图示" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><code>Mach</code> 是一个受 Accent 启发而搞出的Unix兼容系统。</p>
</li>
<li>
<p><code>BSD</code>层是建立在Mach之上，是XNU中一个不可分割的一部分。BSD负责提供可靠的、现代的API</p>
</li>
<li>
<p><code>POSIX</code>表示可移植操作系统接口(Portable Operating System Interface）</p>
</li>
</ul>
<p>所以，综上所述，Mach异常和UNIX信号存在对应的关系
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9090474d5d0e47d782fac4e1f8120315~tplv-k3u1fbpfcp-zoom-1.image" alt="Mach异常和UNIX信号对应关系" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1、硬件异常流程：硬件异常 -> Mach异常 -> UNIX信号</li>
<li>2、软件异常流程：软件异常 -> UNIX信号</li>
</ul>
<p><strong>Mach异常与UNIX信号的转换</strong></p>
<p>下面是<code>Mach异常</code> 与 <code>UNIX信号</code> 的转换关系代码，来自 <code>xnu</code> 中的 <code>bsd/uxkern/ux_exception.c</code></p>
<pre><code class="copyable">switch(exception) &#123;
case EXC_BAD_ACCESS:
    if (code == KERN_INVALID_ADDRESS)
        *ux_signal = SIGSEGV;
    else
        *ux_signal = SIGBUS;
    break;

case EXC_BAD_INSTRUCTION:
    *ux_signal = SIGILL;
    break;

case EXC_ARITHMETIC:
    *ux_signal = SIGFPE;
    break;

case EXC_EMULATION:
    *ux_signal = SIGEMT;
    break;

case EXC_SOFTWARE:
    switch (code) &#123;

    case EXC_UNIX_BAD_SYSCALL:
    *ux_signal = SIGSYS;
    break;
    case EXC_UNIX_BAD_PIPE:
    *ux_signal = SIGPIPE;
    break;
    case EXC_UNIX_ABORT:
    *ux_signal = SIGABRT;
    break;
    case EXC_SOFT_SIGNAL:
    *ux_signal = SIGKILL;
    break;
    &#125;
    break;

case EXC_BREAKPOINT:
    *ux_signal = SIGTRAP;
    break;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将其对应关系汇总成一个表格，如下所示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4a69632d5345ee89dc8efc501f1dec~tplv-k3u1fbpfcp-zoom-1.image" alt="Mach异常和UNIX信号对应表格" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>其中Mach异常有以下</li>
</ul>









































<table><thead><tr><th>Mach异常</th><th>说明</th></tr></thead><tbody><tr><td><code>EXC_BAD_ACCESS</code></td><td>不能访问的内存</td></tr><tr><td><code>EXC_BAD_INSTRUCTION</code></td><td>非法或未定义的指令或操作数</td></tr><tr><td><code>EXC_ARITHMETIC</code></td><td>算术异常(例如除以0)。iOS 默认是不启用的，所以我们一般不会遇到</td></tr><tr><td><code>EXC_EMULATION</code></td><td>执行打算用于支持仿真的指令</td></tr><tr><td><code>EXC_SOFTWARE</code></td><td>软件生成的异常，我们在 Crash 日志中一般不会看到这个类型，苹果的日志里会是 EXC_CRASH</td></tr><tr><td><code>EXC_BREAKPOINT</code></td><td>跟踪或断点</td></tr><tr><td><code>EXC_SYSCALL</code></td><td>UNIX 系统调用</td></tr><tr><td><code>EXC_MACH_SYSCALL</code></td><td>Mach 系统调用</td></tr></tbody></table>
<ul>
<li>UNIX信号有以下几种</li>
</ul>













































<table><thead><tr><th>UNIX信号</th><th>说明</th></tr></thead><tbody><tr><td><code>SIGSEGV</code></td><td>段错误。访问未分配内存、写入没有写权限的内存等。</td></tr><tr><td><code>SIGBUS</code></td><td>总线错误。比如内存地址对齐、错误的内存类型访问等。</td></tr><tr><td><code>SIGILL</code></td><td>执行了非法指令，一般是可执行文件出现了错误</td></tr><tr><td><code>SIGFPE</code></td><td>致命的算术运算。比如数值溢出、NaN数值等。</td></tr><tr><td><code>SIGABRT</code></td><td>调用 abort() 产生，通过 pthread_kill() 发送。</td></tr><tr><td><code>SIGPIPE</code></td><td>管道破裂。通常在进程间通信产生。比如采用FIFO(管道)通信的两个进程，读管道没打开或者意外终止就往管道写，写进程会收到SIGPIPE信号。根据苹果相关文档，可以忽略这个信号。</td></tr><tr><td><code>SIGSYS</code></td><td>系统调用异常。</td></tr><tr><td><code>SIGKILL</code></td><td>此信号表示系统中止进程。崩溃报告会包含代表中止原因的编码。exit(), kill(9) 等函数调用。iOS 系统杀进程，如 watchDog 杀进程。</td></tr><tr><td><code>SIGTRAP</code></td><td>断点指令或者其他trap指令产生。</td></tr></tbody></table>
<h2 data-id="heading-3">野指针</h2>
<p>所指向的<code>对象被释放或者收回</code>，但是该<code>指针没有作任何的修改</code>，以至于<code>该指针仍旧指向已经回收的内存地址</code>。这个指针就是<code>野指针</code></p>
<p><strong>野指针分类</strong></p>
<p>这个参考腾讯Bugly团队的总结，大致分为两类</p>
<ul>
<li>内存没被覆盖</li>
<li>内存被覆盖</li>
</ul>
<p>如下图所示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a67cd60fec3742fb8b305bc366ecbffa~tplv-k3u1fbpfcp-zoom-1.image" alt="腾讯Bugly总结" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>为什么OC野指针的crash这么多？</strong>
我们一般在app发版前，都会经过多轮的<code>自测、内侧、灰度测试</code>等，按照常理来说，大部分的crash应该都被覆盖了，但是由于<code>野指针的随机性</code>，使得经常在测试时不会出现crash，而是在<code>线上出现crash</code>，这对app体验来说是非常致命的</p>
<p>而野指针的随机性问题大致可以分为两类：</p>
<ul>
<li>1、跑不进出错的逻辑，执行不到出错的代码，这种可以通过<code>提高测试场景覆盖率</code>来解决</li>
<li>2、跑进有问题的逻辑，但是野指针指向的地址并不一定会导致crash，原因是因为：<code>野指针</code>其本质是一个指向<code>已经删除的对象</code>或<code>受限内存区域</code>的<code>指针</code>。这里说的<code>OC野指针</code>，是指<code>OC对象释放后指针未置空而导致的野指针</code>。这里不必现的原因是因为<code>dealloc</code>执行后只是告诉系统，这片<code>内存我不用了，而系统并没有让这片内存不能访问</code></li>
</ul>
<h2 data-id="heading-4">野指针解决思路</h2>
<p>这里主要是借鉴Xcode中的两种处理方案：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56968976a1934aa990806e5f672fe99a~tplv-k3u1fbpfcp-zoom-1.image" alt="xcode图示" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1、<strong>Malloc Scribble</strong> ，其<a href="https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MallocDebug.html" target="_blank" rel="nofollow noopener noreferrer">官方解释</a>如下：申请内存 <code>alloc</code> 时在内存上填<code>0xAA</code>，释放内存 <code>dealloc</code> 在内存上填 <code>0x55</code>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/338ef8f6c3194ca78a484f8b6376e1f6~tplv-k3u1fbpfcp-zoom-1.image" alt="Malloc Scribble官方解释" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>2、<strong>Zombie Objects</strong>，其<a href="https://developer.apple.com/documentation/xcode/investigating-crashes-for-zombie-objects?preferredLanguage=occ" target="_blank" rel="nofollow noopener noreferrer">官方解释</a>如下：一个对象已经解除了它的引用，已经被释放掉，但是此时仍然是可以接受消息，这个对象就叫做<code>Zombie Objects</code>（僵尸对象）。这种方案的重点就是<code>将释放的对象，全都转为僵尸对象</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adaf66a5e7d742c3bec3fc79dba62a4f~tplv-k3u1fbpfcp-zoom-1.image" alt="Zombie Objects官方解释" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>两种方案对比</strong></p>
<ul>
<li>
<p>1、<code>僵尸对象</code> 相比 <code>Malloc Scribble</code>，<code>不需要考虑会不会崩溃的问题</code>，只要野指针指向僵尸对象，那么再次访问野指针就一定会崩溃</p>
</li>
<li>
<p>2、僵尸对象这种方式，<code>不如Malloc Scribble覆盖面广</code>，可以通过hook free方法将c函数也包含在其中</p>
</li>
</ul>
<h3 data-id="heading-5">1、Malloc Scribble</h3>
<p>思路：当访问到对象内存中填充的是<code>0xAA、0x55</code>时，程序就会出现异常</p>
<ul>
<li>
<p>申请内存 <code>alloc</code> 时在内存上填<code>0xAA</code>，</p>
</li>
<li>
<p>释放内存 <code>dealloc</code> 在内存上填 <code>0x55</code>。</p>
</li>
</ul>
<p>以上的申请和释放的填充分别对应一下两种情况</p>
<ul>
<li>申请：没有做初始化就直接被访问</li>
<li>释放：释放后访问</li>
</ul>
<p>所以综上所述，针对野指针，我们的解决办法是：在对象释放时做数据填充<code>0x55</code>即可。关于对象的释放流程可以参考这篇文章<a href="https://www.jianshu.com/p/5ddd62fdaea9" target="_blank" rel="nofollow noopener noreferrer">iOS-底层原理 33：内存管理（一）TaggedPointer/retain/release/dealloc/retainCount 底层分析</a></p>
<h4 data-id="heading-6">野指针探测实现1</h4>
<p>这个实现主要依据<a href="https://github.com/fangjinfeng/MySampleCode/tree/master/FJFZombieSnifferDemo" target="_blank" rel="nofollow noopener noreferrer">腾讯Bugly工程师:陈其锋</a>的分享，在其代码中的主要思路是</p>
<ul>
<li>1、通过<code>fishhook</code>替换<code>C函数</code>的<code>free</code>方法为自定义的<code>safe_free</code>，类似于Method Swizzling</li>
<li>2、在<code>safe_free</code>方法中对<code>已经释放变量的内存</code>，填充<code>0x55</code>，使已经释放变量<code>不能访问</code>，从而使某些野指针的crash从不必现安变成<code>必现</code>。
<ul>
<li>
<p>为了<code>防止填充0x55的内存被新的数据内容填充</code>，使野指针crash变成不必现，在这里采用的策略是，<code>safe_free不释放这片内存，而是自己保留着</code>，即safe_free方法中不会真的调用free。</p>
</li>
<li>
<p>同时为了<code>防止系统内存过快消耗</code>（因为要保留内存），需要在<code>保留的内存大于一定值时释放一部分</code>，防止被系统杀死，同时，在收到<code>系统内存警告</code>时，也需要<code>释放一部分内存</code></p>
</li>
</ul>
</li>
<li>3、发生crash时，得到的崩溃信息有限，不利于问题排查，所以这里采用代理类（即继承自<code>NSProxy</code>的子类），重写消息转发的三个方法（参考这篇文章<a href="https://www.jianshu.com/p/b838f04a9249" target="_blank" rel="nofollow noopener noreferrer">iOS-底层原理 14：消息流程分析之 动态方法决议 & 消息转发</a>），以及NSObject的实例方法，来获取异常信息。但是这的话，还有一个问题，就是NSProxy只能做OC对象的代理，所以需要在safe_free中增加对象类型的判断</li>
</ul>
<p>以下是完整的野指针探测实现代码</p>
<ul>
<li>引入fishhook</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e605075519a4ff79e71c7ade9fc515b~tplv-k3u1fbpfcp-zoom-1.image" alt="引入fishhook" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>实现NSProxy的代理子类</li>
</ul>
<pre><code class="copyable"><!--1、MIZombieProxy.h-->
@interface MIZombieProxy : NSProxy

@property (nonatomic, assign) Class originClass;

@end

<!--2、MIZombieProxy.m-->
#import "MIZombieProxy.h"

@implementation MIZombieProxy

- (BOOL)respondsToSelector:(SEL)aSelector&#123;
    return [self.originClass instancesRespondToSelector:aSelector];
&#125;

- (NSMethodSignature *)methodSignatureForSelector:(SEL)sel&#123;
    return [self.originClass instanceMethodSignatureForSelector:sel];
&#125;

- (void)forwardInvocation: (NSInvocation *)invocation
&#123;
    [self _throwMessageSentExceptionWithSelector: invocation.selector];
&#125;

#define MIZombieThrowMesssageSentException() [self _throwMessageSentExceptionWithSelector: _cmd]
- (Class)class&#123;
    MIZombieThrowMesssageSentException();
    return nil;
&#125;
- (BOOL)isEqual:(id)object&#123;
    MIZombieThrowMesssageSentException();
    return NO;
&#125;
- (NSUInteger)hash&#123;
    MIZombieThrowMesssageSentException();
    return 0;
&#125;
- (id)self&#123;
    MIZombieThrowMesssageSentException();
    return nil;
&#125;
- (BOOL)isKindOfClass:(Class)aClass&#123;
    MIZombieThrowMesssageSentException();
    return NO;
&#125;
- (BOOL)isMemberOfClass:(Class)aClass&#123;
    MIZombieThrowMesssageSentException();
    return NO;
&#125;
- (BOOL)conformsToProtocol:(Protocol *)aProtocol&#123;
    MIZombieThrowMesssageSentException();
    return NO;
&#125;
- (BOOL)isProxy&#123;
    MIZombieThrowMesssageSentException();
    return NO;
&#125;

- (NSString *)description&#123;
    MIZombieThrowMesssageSentException();
    return nil;
&#125;

#pragma mark - MRC
- (instancetype)retain&#123;
    MIZombieThrowMesssageSentException();
    return  nil;
&#125;
- (oneway void)release&#123;
    MIZombieThrowMesssageSentException();
&#125;
- (void)dealloc
&#123;
    MIZombieThrowMesssageSentException();
    [super dealloc];
&#125;
- (NSUInteger)retainCount&#123;
    MIZombieThrowMesssageSentException();
    return 0;
&#125;
- (struct _NSZone *)zone&#123;
    MIZombieThrowMesssageSentException();
    return  nil;
&#125;


#pragma mark - private
- (void)_throwMessageSentExceptionWithSelector:(SEL)selector&#123;
    @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:[NSString stringWithFormat:@"(-[%@ %@]) was sent to a zombie object at address: %p", NSStringFromClass(self.originClass),NSStringFromSelector(selector), self] userInfo:nil];
&#125;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>hook free方法的具体实现</li>
</ul>
<pre><code class="copyable"><!--1、MISafeFree.h-->
@interface MISafeFree : NSObject

//系统警告时，用函数释放一些内存
void free_safe_mem(size_t freeNum);

@end

<!--2、MISafeFree.m-->
#import "MISafeFree.h"
#import "queue.h"
#import "fishhook.h"
#import "MIZombieProxy.h"

#import <dlfcn.h>
#import <objc/runtime.h>
#import <malloc/malloc.h>

//用于保存zombie类
static Class kMIZombieIsa;
//用于保存zombie类的实例变量大小
static size_t kMIZombieSize;

//用于表示调用free函数
static void(* orig_free)(void *p);
//用于保存已注册的类的集合
static CFMutableSetRef registeredClasses = nil;
/*
 用来保存自己保留的内存
 - 1、队列要线程安全或者自己加锁
 - 2、这个队列内部应该尽量少申请和释放堆内存
 */
struct DSQueue *_unfreeQueue = NULL;
//用来记录自己保存的内存的大小
int unfreeSize = 0;

//最多存储的内存，大于这个值就释放一部分
#define MAX_STEAL_MEM_SIZE 1024*1024*100
//最多保留的指针个数，超过就释放一部分
#define MAX_STEAL_MEM_NUM 1024*1024*10
//每次释放时释放的指针数量
#define BATCH_FREE_NUM 100

@implementation MISafeFree

#pragma mark - Public Method
//系统警告时，用函数释放一些内存
void free_safe_mem(size_t freeNum)&#123;
#ifdef DEBUG
    //获取队列的长度
    size_t count = ds_queue_length(_unfreeQueue);
    //需要释放的内存大小
    freeNum = freeNum > count ? count : freeNum;
    //遍历并释放
    for (int i = 0; i < freeNum; i++) &#123;
        //获取未释放的内存块
        void *unfreePoint = ds_queue_get(_unfreeQueue);
        //创建内存块申请的大小
        size_t memSize = malloc_size(unfreePoint);
        //原子减操作，多线程对全局变量进行自减
        __sync_fetch_and_sub(&unfreeSize, (int)memSize);
        //释放
        orig_free(unfreePoint);
    &#125;
#endif
&#125;

#pragma mark - Life Circle

+ (void)load&#123;
#ifdef DEBUG
    loadZombieProxyClass();
    init_safe_free();
#endif
&#125;

#pragma mark - Private Method
void safe_free(void* p)&#123;
    
    //获取自己保留的内存的大小
    int unFreeCount = ds_queue_length(_unfreeQueue);
    //保留的内存大于一定值时就释放一部分
    if (unFreeCount > MAX_STEAL_MEM_NUM*0.9 || unfreeSize>MAX_STEAL_MEM_SIZE) &#123;
        free_safe_mem(BATCH_FREE_NUM);
    &#125;else&#123;
        //创建p申请的内存大小
        size_t memSize = malloc_size(p);
        //有足够的空间才覆盖
        if (memSize > kMIZombieSize) &#123;
            //指针强转为id对象
            id obj = (id)p;
            //获取指针原本的类
            Class origClass = object_getClass(obj);
            //判断是不是objc对象
            char *type = @encode(typeof(obj));
            /*
             - strcmp 字符串比较
             - CFSetContainsValue 查看已注册类中是否有origClass这个类
             
             如果都满足，则将这块内存填充0x55
             */
            if (strcmp("@", type) == 0 && CFSetContainsValue(registeredClasses, origClass)) &#123;
                //内存上填充0x55
                memset(obj, 0x55, memSize);
                //将自己类的isa复制过去
                memcpy(obj, &kMIZombieIsa, sizeof(void*));
                //为obj设置指定的类
                object_setClass(obj, [MIZombieProxy class]);
                //保留obj原本的类
                ((MIZombieProxy*)obj).originClass = origClass;
                //多线程下int的原子加操作，多线程对全局变量进行自加，不用理会线程锁了
                __sync_fetch_and_add(&unfreeSize, (int)memSize);
                //入队
                ds_queue_put(_unfreeQueue, p);
            &#125;else&#123;
                orig_free(p);
            &#125;
        &#125;else&#123;
            orig_free(p);
        &#125;
    &#125;
&#125;

//加载野指针自定义类
void loadZombieProxyClass()&#123;
    registeredClasses = CFSetCreateMutable(NULL, 0, NULL);
    
    //用于保存已注册类的个数
    unsigned int count = 0;
    //获取所有已注册的类
    Class *classes = objc_copyClassList(&count);
    //遍历，并保存到registeredClasses中
    for (int i = 0; i < count; i++) &#123;
        CFSetAddValue(registeredClasses, (__bridge const void *)(classes[i]));
    &#125;
    //释放临时变量内存
    free(classes);
    classes = NULL;
    
    kMIZombieIsa = objc_getClass("MIZombieProxy");
    kMIZombieSize = class_getInstanceSize(kMIZombieIsa);
&#125;

//初始化以及free符号重绑定
bool init_safe_free()&#123;
    //初始化用于保存内存的队列
    _unfreeQueue = ds_queue_create(MAX_STEAL_MEM_NUM);
    //dlsym 在打开的库中查找符号的值，即动态调用free函数
    orig_free = (void(*)(void*))dlsym(RTLD_DEFAULT, "free");
    /*
     rebind_symbols:符号重绑定
     - 参数1：rebindings 是一个rebinding数组，其定义如下
         struct rebinding &#123;
           const char *name;  // 目标符号名
           void *replacement; // 要替换的符号值（地址值）
           void **replaced;   // 用来存放原来的符号值（地址值）
         &#125;;
     - 参数2：rebindings_nel 描述数组的长度
     */
    //重绑定free符号，让它指向自定义的safe_free函数
    rebind_symbols((struct rebinding[])&#123;&#123;"free", (void*)safe_free&#125;&#125;, 1);
    return true;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>测试</li>
</ul>
<pre><code class="copyable">- (void)viewDidLoad &#123;
    [super viewDidLoad];
    
    id obj = [[NSObject alloc] init];
    self.assignObj = obj;
    
//    [MIZombieSniffer installSniffer];
&#125;
- (IBAction)mallocScribbleAction:(id)sender &#123;
    
    UIView* testObj = [[UIView alloc] init];
    [testObj release];
    for (int i = 0; i < 10; i++) &#123;
        UIView* testView = [[UIView alloc] initWithFrame:CGRectMake(0,200,CGRectGetWidth(self.view.bounds), 60)];
        [self.view addSubview:testView];
    &#125;
    [testObj setNeedsLayout];
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f382c00daf54a0db25ed1cbda18bfdb~tplv-k3u1fbpfcp-zoom-1.image" alt="测试结果" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">2、Zombie Objects</h3>
<p><strong>僵尸对象</strong></p>
<ul>
<li>
<p>可以用来检测内存错误（<code>EXC_BAD_ACCESS</code>），它可以捕获任何阐释访问坏内存的调用</p>
</li>
<li>
<p>给僵尸对象发送消息的话，它仍然是可以响应的，然后会发生崩溃，并输出错误日志来显示野指针对象调用的类名和方法</p>
</li>
</ul>
<p><strong>苹果的僵尸对象检测原理</strong>
首先我们来看下Xcode中僵尸对象是如何实现的，具体操作步骤可以参考这篇文章<a href="https://zhiyongzou.github.io/2017/08/25/iOS-Zombie-Object-%E5%83%B5%E5%B0%B8%E5%AF%B9%E8%B1%A1-%E5%8E%9F%E7%90%86%E6%8E%A2%E7%B4%A2/" target="_blank" rel="nofollow noopener noreferrer">iOS Zombie Objects(僵尸对象)原理探索</a></p>
<ul>
<li>从<code>dealloc</code>的源码中，我们可以看到<code>“Replaced by NSZombie”</code>，即<code>对象释放</code>时， <code>NSZombie 将在 dealloc 里做替换</code>，如下所示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e0c841b4092462391a512f1338c6255~tplv-k3u1fbpfcp-zoom-1.image" alt="Zombie Objects原理-01" loading="lazy" referrerpolicy="no-referrer">
所以僵尸对象的生成过程伪代码如下</p>
<pre><code class="copyable">//1、获取到即将deallocted对象所属类（Class）
Class cls = object_getClass(self);

//2、获取类名
const char *clsName = class_getName(cls)

//3、生成僵尸对象类名
const char *zombieClsName = "_NSZombie_" + clsName;

//4、查看是否存在相同的僵尸对象类名，不存在则创建
Class zombieCls = objc_lookUpClass(zombieClsName);
if (!zombieCls) &#123;
     //5、获取僵尸对象类 _NSZombie_
 Class baseZombieCls = objc_lookUpClass(“_NSZombie_");

     //6、创建 zombieClsName 类
 zombieCls = objc_duplicateClass(baseZombieCls, zombieClsName, 0);
&#125;
//7、在对象内存未被释放的情况下销毁对象的成员变量及关联引用。
   objc_destructInstance(self);

//8、修改对象的 isa 指针，令其指向特殊的僵尸类
objc_setClass(self, zombieCls);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当僵尸对象再次被访问时，将进入消息转发流程，开始处理僵尸对象访问，输出日志并发生crash</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce3593eee0c40b69fce82233b8b39ed~tplv-k3u1fbpfcp-zoom-1.image" alt="Zombie Objects原理-02" loading="lazy" referrerpolicy="no-referrer">
所以僵尸对象触发流程伪代码如下</p>
<pre><code class="copyable">//1、获取对象class
Class cls = object_getClass(self);

//2、获取对象类名
const char *clsName = class_getName(cls);

//3、检测是否带有前缀_NSZombie_
if (string_has_prefix(clsName, "_NSZombie_")) &#123;
//4、获取被野指针对象类名
  const char *originalClsName = substring_from(clsName, 10);

　//5、获取当前调用方法名
　const char *selectorName = sel_getName(_cmd);
　　
　//6、输出日志
　Log(''*** - [%s %s]: message sent to deallocated instance %p", originalClsName, selectorName, self);

　//7、结束进程
　abort();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以综上所述，这中野指针探测方式的思路是：<code>dealloc</code>方法的替换，其关键是调用<code>objc_destructInstance</code> 来解除对象的关联引用</p>
<h4 data-id="heading-8">野指针探测实现2</h4>
<p>这种方式的思路主要是来源<a href="https://juejin.cn/post/LXDZombieSniffer">sindrilin</a>的源码，其主要思路是：</p>
<ul>
<li><strong>野指针检测流程</strong>
<ul>
<li>
<p>1、开启野指针检测</p>
</li>
<li>
<p>2、设置监控到野指针时的回调block，在block中打印信息，或者存储堆栈</p>
</li>
<li>
<p>3、检测到野指针是否crash</p>
</li>
<li>
<p>4、最大内存占用空间</p>
</li>
<li>
<p>5、是否记录dealloc调用栈</p>
</li>
<li>
<p>6、监控策略</p>
<ul>
<li>
<p>1）只监控自定义对象</p>
</li>
<li>
<p>2）白名单策略</p>
</li>
<li>
<p>3）黑名单策略</p>
</li>
<li>
<p>4）监控所有对象</p>
</li>
</ul>
</li>
<li>
<p>7、交换NSObject的dealloc方法</p>
</li>
</ul>
</li>
<li><strong>触发野指针</strong>
<ul>
<li>
<p>1、开始处理对象</p>
</li>
<li>
<p>2、是否达到替换条件</p>
<ul>
<li>1）根据监控策略，是否属于要检测的类</li>
<li>2）空间是否足够</li>
</ul>
</li>
<li>
<p>3、如果符合条件，则获取对象，并解除引用，如果不符合则正常释放，即调用原来的dealloc方法</p>
</li>
<li>
<p>4、向对象内填充数据</p>
</li>
<li>
<p>5、赋值僵尸对象的类指针替换isa</p>
</li>
<li>
<p>6、对象+dealloc调用栈，保存在僵尸对象中</p>
</li>
<li>
<p>7、根据情况是否清理内存和对象</p>
</li>
</ul>
</li>
</ul>
<p><strong>通过僵尸对象检测的实现思路</strong></p>
<ul>
<li>
<p>1、通过OC中<code>Mehod Swizzling</code>，交换<code>根类NSObject和NSProxy</code>的<code>dealloc</code>方法为<code>自定义的dealloc</code>方法</p>
</li>
<li>
<p>2、为了<code>避免内存空间释放后被重写造成野指针</code>的问题，通过<code>字典存储被释放的对象</code>，同时设置在<code>30s后调用dealloc方法将字典中存储的对象释放，避免内存增大</code></p>
</li>
<li>
<p>3、为了获取更多的崩溃信息，这里同样需要创建NSProxy的子类</p>
</li>
</ul>
<p><strong>具体实现</strong></p>
<ul>
<li>
<p>1、创建NSProxy的子类，其实现与上面的<code>MIZombieProxy</code>是一模一样的</p>
</li>
<li>
<p>2、hook dealloc函数的具体实现</p>
</li>
</ul>
<pre><code class="copyable"><!--1、MIZombieSniffer.h-->
@interface MIZombieSniffer : NSObject

/*!
 *  @method installSniffer
 *  启动zombie检测
 */
+ (void)installSniffer;

/*!
 *  @method uninstallSnifier
 *  停止zombie检测
 */
+ (void)uninstallSnifier;

/*!
 *  @method appendIgnoreClass
 *  添加白名单类
 */
+ (void)appendIgnoreClass: (Class)cls;

@end

<!--2、MIZombieSniffer.m-->
#import "MIZombieSniffer.h"
#import "MIZombieProxy.h"
#import <objc/runtime.h>

//
typedef void (*MIDeallocPointer) (id objc);
//野指针探测器是否开启
static BOOL _enabled = NO;
//根类
static NSArray *_rootClasses = nil;
//用于存储被释放的对象
static NSDictionary<id, NSValue*> *_rootClassDeallocImps = nil;

//白名单
static inline NSMutableSet *__mi_sniffer_white_lists()&#123;
    //创建白名单集合
    static NSMutableSet *mi_sniffer_white_lists;
    //单例初始化白名单集合
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^&#123;
        mi_sniffer_white_lists = [[NSMutableSet alloc] init];
    &#125;);
    return mi_sniffer_white_lists;
&#125;


static inline void __mi_dealloc(__unsafe_unretained id obj)&#123;
    //获取对象的类
    Class currentCls = [obj class];
    Class rootCls = currentCls;
    
    //获取非NSObject和NSProxy的类
    while (rootCls != [NSObject class] && rootCls != [NSProxy class]) &#123;
        //获取rootCls的父类，并赋值
        rootCls = class_getSuperclass(rootCls);
    &#125;
    //获取类名
    NSString *clsName = NSStringFromClass(rootCls);
    //根据类名获取dealloc的imp指针
    MIDeallocPointer deallocImp = NULL;
    [[_rootClassDeallocImps objectForKey:clsName] getValue:&deallocImp];
    
    if (deallocImp != NULL) &#123;
        deallocImp(obj);
    &#125;
&#125;

//hook交换dealloc
static inline IMP __mi_swizzleMethodWithBlock(Method method, void *block)&#123;
    /*
     imp_implementationWithBlock ：接收一个block参数，将其拷贝到堆中，返回一个trampoline
     可以让block当做任何一个类的方法的实现，即当做类的方法的IMP来使用
     */
    IMP blockImp = imp_implementationWithBlock((__bridge id _Nonnull)(block));
    //method_setImplementation 替换掉method的IMP
    return method_setImplementation(method, blockImp);
&#125;

@implementation MIZombieSniffer

//初始化根类
+ (void)initialize
&#123;
    _rootClasses = [@[[NSObject class], [NSProxy class]] retain];
&#125;

#pragma mark - public
+ (void)installSniffer&#123;
    @synchronized (self) &#123;
        if (!_enabled) &#123;
            //hook根类的dealloc方法
            [self _swizzleDealloc];
            _enabled = YES;
        &#125;
    &#125;
&#125;

+ (void)uninstallSnifier&#123;
    @synchronized (self) &#123;
        if (_enabled) &#123;
            //还原dealloc方法
            [self _unswizzleDealloc];
            _enabled = NO;
        &#125;
    &#125;
&#125;

//添加百名单
+ (void)appendIgnoreClass:(Class)cls&#123;
    @synchronized (self) &#123;
        NSMutableSet *whiteList = __mi_sniffer_white_lists();
        NSString *clsName = NSStringFromClass(cls);
        [clsName retain];
        [whiteList addObject:clsName];
    &#125;
&#125;

#pragma mark - private
+ (void)_swizzleDealloc&#123;
    static void *swizzledDeallocBlock = NULL;
    
    //定义block，作为方法的IMP
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^&#123;
        swizzledDeallocBlock = (__bridge void *)[^void(id obj) &#123;
            //获取对象的类
            Class currentClass = [obj class];
            //获取类名
            NSString *clsName = NSStringFromClass(currentClass);
            //判断该类是否在白名单类
            if ([__mi_sniffer_white_lists() containsObject: clsName]) &#123;
                //如果在白名单内，则直接释放对象
                __mi_dealloc(obj);
            &#125; else &#123;
                //修改对象的isa指针，指向MIZombieProxy
                /*
                 valueWithBytes:objCType  创建并返回一个包含给定值的NSValue对象，该值会被解释为一个给定的NSObject类型
                 - 参数1：NSValue对象的值
                 - 参数2：给定值的对应的OC类型，需要使用编译器指令@encode来创建
                 */
                NSValue *objVal = [NSValue valueWithBytes: &obj objCType: @encode(typeof(obj))];
                //为obj设置指定的类
                object_setClass(obj, [MIZombieProxy class]);
                //保留对象原本的类
                ((MIZombieProxy *)obj).originClass = currentClass;
                
                //设置在30s后调用dealloc将存储的对象释放，避免内存空间的增大
                dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(30 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
                    __unsafe_unretained id deallocObj = nil;
                    //获取需要dealloc的对象
                    [objVal getValue: &deallocObj];
                    //设置对象的类为原本的类
                    object_setClass(deallocObj, currentClass);
                    //释放
                    __mi_dealloc(deallocObj);
                &#125;);
            &#125;
        &#125; copy];
    &#125;);
    
    //交换了根类NSObject和NSProxy的dealloc方法为originalDeallocImp
    NSMutableDictionary *deallocImps = [NSMutableDictionary dictionary];
    //遍历根类
    for (Class rootClass in _rootClasses) &#123;
        //获取指定类中dealloc方法
        Method oriMethod = class_getInstanceMethod([rootClass class], NSSelectorFromString(@"dealloc"));
        //hook - 交换dealloc方法的IMP实现
        IMP originalDeallocImp = __mi_swizzleMethodWithBlock(oriMethod, swizzledDeallocBlock);
        //设置IMP的具体实现
        [deallocImps setObject: [NSValue valueWithBytes: &originalDeallocImp objCType: @encode(typeof(IMP))] forKey: NSStringFromClass(rootClass)];
    &#125;
    //_rootClassDeallocImps字典存储交换后的IMP实现
    _rootClassDeallocImps = [deallocImps copy];
&#125;

+ (void)_unswizzleDealloc&#123;
    //还原dealloc交换的IMP
    [_rootClasses enumerateObjectsUsingBlock:^(Class rootClass, NSUInteger idx, BOOL * _Nonnull stop) &#123;
        IMP originDeallocImp = NULL;
        //获取根类类名
        NSString *clsName = NSStringFromClass(rootClass);
        //获取hook后的dealloc实现
        [[_rootClassDeallocImps objectForKey:clsName] getValue:&originDeallocImp];
        
        NSParameterAssert(originDeallocImp);
        //获取原本的dealloc实现
        Method oriMethod = class_getInstanceMethod([rootClass class], NSSelectorFromString(@"dealloc"));
        //还原dealloc的实现
        method_setImplementation(oriMethod, originDeallocImp);
    &#125;];
    //释放
    [_rootClassDeallocImps release];
    _rootClassDeallocImps = nil;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、测试</li>
</ul>
<pre><code class="copyable">@interface ViewController ()

@property (nonatomic, assign) id assignObj;

@end

@implementation ViewController

- (void)viewDidLoad &#123;
    [super viewDidLoad];
    
    id obj = [[NSObject alloc] init];
    self.assignObj = obj;
    
    [MIZombieSniffer installSniffer];
&#125;
- (IBAction)zombieObjectAction:(id)sender &#123;

    NSLog(@"%@", self.assignObj);
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印崩溃信息如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2df4a362a34e5f90bc101211ad317e~tplv-k3u1fbpfcp-zoom-1.image" alt="Zombie Objects运行结果" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">参考文章</h3>
<ul>
<li><a href="https://www.jianshu.com/p/4c8a68bd066c" target="_blank" rel="nofollow noopener noreferrer">质量监控-野指针定位</a></li>
<li><a href="https://juejin.cn/post/6930979515552235528" target="_blank">iOS野指针处理</a></li>
<li><a href="https://www.jianshu.com/p/9fd4dc046046" target="_blank" rel="nofollow noopener noreferrer">iOS野指针定位：野指针嗅探器</a></li>
<li><a href="https://juejin.cn/post/6844903747538141191#heading-6" target="_blank">iOS野指针定位总结</a></li>
<li><a href="https://zhiyongzou.github.io/2017/08/25/iOS-Zombie-Object-%E5%83%B5%E5%B0%B8%E5%AF%B9%E8%B1%A1-%E5%8E%9F%E7%90%86%E6%8E%A2%E7%B4%A2/" target="_blank" rel="nofollow noopener noreferrer">iOS Zombie Objects(僵尸对象)原理探索</a></li>
</ul></div>  
</div>
            