
---
title: 'OC底层原理（七）：Runimte运行时&objc_msgSend分析上'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c53d40fc482742c684cc1428ff0fe28d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 05:06:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c53d40fc482742c684cc1428ff0fe28d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><code>Runtime</code></h2>
<h3 data-id="heading-1"><code>编译时</code>与<code>Runtime运行时</code></h3>
<ul>
<li><code>编译时</code>：顾名思义正在编译的时候，啥叫编译呢？就是<code>编译器把源代码</code>翻<code>译成机器</code>能够识别的代<code>码</code>。<code>编译时会</code>进行<code>词法分析</code>，语法分析主要是检<code>查代码</code>是否符合苹果的<code>规范</code>，这个检查的过程通常<code>叫</code>做<code>静态类型检查</code>。</li>
<li><code>Runtime运行时</code>：<code>代码</code>跑起来，<code>被装</code>装载<code>到内存中</code>。<code>运行时</code>检查错误和<code>编译时</code>检查错误不一样，不是简单的代码扫描，而是在<code>内存中做操作</code>和<code>判断</code>。</li>
</ul>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FCocoa%2FConceptual%2FObjCRuntimeGuide%2FIntroduction%2FIntroduction.html%23%2F%2Fapple_ref%2Fdoc%2Fuid%2FTP40008048" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048" ref="nofollow noopener noreferrer"><code>Runtime</code>版本</a></h3>
<p><code>Runtime</code>有两个版本: 一个<code>Legacy</code>版本（<code>早期版本</code>），一个<code>Modern</code>版本（<code>现行版本</code>）</p>
<ul>
<li><code>Legacy</code>早期版本对应的编程接口：<code>Objective-C 1.0</code>,用于<code>32位</code>的<code>Mac OS X</code>的平台</li>
<li><code>Modern</code>现行版本对应的编程接口：<code>Objective-C 2.0</code>，源码中经常看到的<code>OBJC2</code>，用于<code>iPhone</code>程序和<code>Mac OS X v10.5</code>及<code>以后</code>的系统中的<code>64位</code>程序</li>
</ul>
<h3 data-id="heading-3"><code>Runtime</code>调用<code>三种</code>方式</h3>
<ul>
<li><code>Objective-C</code>方式: <code>[penson sayNB]</code></li>
<li><code>Framework & Serivce</code>方式:<code>isKindOfClass</code></li>
<li><code>Runtime API</code>方式: <code>class_getInstanceSize</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c53d40fc482742c684cc1428ff0fe28d~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-05 at 6.41.40 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">方法的本质</h2>
<h3 data-id="heading-5">方法底层的实现</h3>
<p>探究方法的<code>底层</code>有<code>两种方式</code>。第一种<code>汇编</code>，第二种<code>C++代码</code>。汇编方式的方法的参数需要读寄存器不方便，所以采用第二种方式生成<code>main.cpp</code>文件。</p>
<ul>
<li>首先自定义<code>LGPerson类</code>，在类中添加实例方法，在<code>main</code>函数中调用</li>
</ul>
<p>代码:</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import <objc/message.h>

@interface LGPerson : NSObject
- (void)sayHello;
- (void)say:(NSString *)str;
@end

@implementation LGPerson
- (void)sayHello&#123;
    NSLog(@"666 %s",__func__);
&#125;

- (void)say:(NSString *)str&#123;
    NSLog(@"----say %@---",str);
&#125;
@end

@interface LGTeacher: LGPerson
- (void)sayHello;
- (void)sayNB;
@end

@implementation LGTeacher
- (void)sayNB&#123;
    NSLog(@"666");
&#125;
@end

int main(int argc, char * argv[]) &#123;
 
    @autoreleasepool &#123;
        LGTeacher *teach = [LGTeacher alloc];
        [teach sayNB];
        [teach say:@"runtime -- msg"];
    &#125;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在终端使用<code>xcrun -sdk iphonesimulator clang -arch arm64 -rewrite-objc main.m -o main-arm64.cpp</code>把<code>main.m</code>生成<code>main64.cpp</code>文件，查询<code>main</code>函数的实现:</li>
</ul>
<p>c++代码:</p>
<pre><code class="copyable">int main(int argc, const char * argv[]) &#123;
    /* @autoreleasepool */ &#123; __AtAutoreleasePool __autoreleasepool; 
        LGTeacher *teach = ((LGTeacher *(*)(id, SEL))(void *)objc_msgSend)((id)objc_getClass("LGTeacher"), sel_registerName("alloc"));

        ((void (*)(id, SEL))(void *)objc_msgSend)((id)teach, sel_registerName("sayNB"));
        ((void (*)(id, SEL, NSString *))(void *)objc_msgSend)((id)teach, sel_registerName("say:"), (NSString *)&__NSConstantStringImpl__var_folders_gy__p7f70ys54s2c4h_8hjgv8k80000gn_T_main_2163a1_mi_3);
    &#125;
    return 0;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li>所有的方法调用都是通过<code>objc_msgSend</code>发送的，所以<code>方法</code>的<code>本质</code>就是<code>消息发送</code></li>
</ul>
</blockquote>
<h3 data-id="heading-6">验证<code>objc_msgSend</code>发送消息</h3>
<p>既然方法调用都是通过<code>objc_msgSend</code>的，那么我直接通过<code>objc_msgSend</code>发消息</p>
<p>代码:</p>
<pre><code class="copyable">int main(int argc, char * argv[]) &#123;
    @autoreleasepool &#123;
        LGTeacher *teach = [LGTeacher alloc];
        [teach sayNB];
        objc_msgSend((id)teach, sel_registerName("sayNB"));
        [teach say:@"runtime -- msg"];
        objc_msgSend((id)teach, sel_registerName("say:"),@"runtime -- msg2");
    &#125;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>llvm打印:</p>
<pre><code class="copyable">2021-07-05 23:16:26.051908+0800 001-运行时感受[7416:606713] 666
2021-07-05 23:16:26.052382+0800 001-运行时感受[7416:606713] 666
2021-07-05 23:16:26.052454+0800 001-运行时感受[7416:606713] ----say runtime -- msg---
2021-07-05 23:16:26.052491+0800 001-运行时感受[7416:606713] ----say runtime -- msg2---
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li>通过<code>objc_msgSend</code>和<code>[teach sayNB]</code>、<code>[teach say:@"runtime -- msg"]</code>无论带不带<code>输入参数</code>,结果是一样的;验证了<code>方法的本质</code>是<code>消息发送</code>。</li>
<li>在<code>main</code>函数里<code>LGTeacher</code>的<code>对象</code>是直接调用<code>objc_msgSend</code>，传入的<code>id</code>也是一样的<code>LGTeacher</code>对象<code>teach</code>，说明<code>objc_msgSend</code>内部会自动判断当前<code>类class</code>是否有这个方法，没有就会找到该类的<code>父类</code>看看有没有，有就调用父类方法。</li>
<li>在用<code>objc_msgSend</code>方式发送消息，验证过程需要注意两点:</li>
</ul>
<blockquote>
<ul>
<li>导入消息发送的头文件<code>#import <objc/message.h></code></li>
<li>关闭<code>objc_msgSend</code>检查机制：<code>target</code> --> <code>Build Setting</code> --><code>搜索objc_msgSend</code> -- <code>Enable strict checking of obc_msgSend calls</code>设置为<code>NO</code></li>
</ul>
</blockquote>
</blockquote>
<h3 data-id="heading-7">父类方法<code>[super function]</code></h3>
<ul>
<li>由于在<code>objc</code>的对象<code>object</code>是可以直接使用<code>父类的方法</code>,而调用本类中的方法实际是通过<code>objc_msgSend</code>发送的，那么在子类<code>复写override</code>方法时调用父类的方法<code>[super function]</code>,<code>消息发送</code>是什么样的呢？</li>
<li>自定义<code>LGTeacher</code>类，<code>LGTeacher</code>继承<code>LGPerson</code>类。在<code>LGPerson</code>类中自定义方法<code>sayHello</code>，子类<code>LGTeacher</code>对象调用<code>sayHello</code>方法。</li>
</ul>
<h4 data-id="heading-8">父类的方法<code>[super function]</code>的底层</h4>
<ul>
<li>在<code>LGTeacher</code>中复写调用父类<code>LGPerson</code>方法<code>[super sayHello]</code>。</li>
</ul>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import <objc/message.h>

@interface LGPerson : NSObject
- (void)sayHello;
- (void)say:(NSString *)str;
@end

@implementation LGPerson
- (void)sayHello&#123;
    NSLog(@"666 %s",__func__);
&#125;

- (void)say:(NSString *)str&#123;
    NSLog(@"----say %@---",str);
&#125;
@end

@interface LGTeacher : LGPerson
- (void)sayNB;
@end

@implementation LGTeacher
- (void)sayNB&#123;
    NSLog(@"666");
&#125;

- (void)sayHello &#123;
    [super sayHello];
    NSLog(@"7777");
&#125;
@end

int main(int argc, char * argv[]) &#123;
    @autoreleasepool &#123;
        LGTeacher * teach  = [LGTeacher alloc];
        [teach sayHello];
        NSLog(@"Hello, World!");
    &#125;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用<code>xcrun -sdk iphonesimulator clang -arch arm64 -rewrite-objc main.m -o main-arm64.cpp</code>把<code>main.m</code>生成<code>mian-arm64.cpp</code>文件，</li>
</ul>
<p><code>c++</code>的<code>main</code>方法:</p>
<pre><code class="copyable">int main(int argc, const char * argv[]) &#123;
    /* @autoreleasepool */ &#123; __AtAutoreleasePool __autoreleasepool; 
        LGTeacher * teach = ((LGTeacher *(*)(id, SEL))(void *)objc_msgSend)((id)objc_getClass("LGTeacher"), sel_registerName("alloc"));
        ((void (*)(id, SEL))(void *)objc_msgSend)((id)teach, sel_registerName("sayHello"));
        NSLog((NSString *)&__NSConstantStringImpl__var_folders_9t_c60fhy096zg_yjphk3kd3ch40000l2_T_main_906af2_mi_4);
    &#125;
    return 0;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>c++</code>的<code>LGPerson</code>、<code>LGPerson</code>的函数:</p>
<pre><code class="copyable">#ifndef _REWRITER_typedef_LGPerson
#define _REWRITER_typedef_LGPerson
typedef struct objc_object LGPerson;
typedef struct &#123;&#125; _objc_exc_LGPerson;
#endif

struct LGPerson_IMPL &#123;
struct NSObject_IMPL NSObject_IVARS;
&#125;;
// - (void)sayHello;
// - (void)say:(NSString *)str;
/* @end */


// @implementation LGPerson

static void _I_LGPerson_sayHello(LGPerson * self, SEL _cmd) &#123;
    NSLog((NSString *)&__NSConstantStringImpl__var_folders_9t_c60fhy096zg_yjphk3kd3ch40000l2_T_main_906af2_mi_0,__func__);
&#125;


static void _I_LGPerson_say_(LGPerson * self, SEL _cmd, NSString *str) &#123;
    NSLog((NSString *)&__NSConstantStringImpl__var_folders_9t_c60fhy096zg_yjphk3kd3ch40000l2_T_main_906af2_mi_1,str);
&#125;
// @end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>c++的<code>LGTeacher</code>和<code>LGTeacher</code>函数:</p>
<pre><code class="copyable">#ifndef _REWRITER_typedef_LGTeacher
#define _REWRITER_typedef_LGTeacher
typedef struct objc_object LGTeacher;
typedef struct &#123;&#125; _objc_exc_LGTeacher;
#endif

struct LGTeacher_IMPL &#123;
struct LGPerson_IMPL LGPerson_IVARS;
&#125;;

// - (void)sayNB;
/* @end */


// @implementation LGTeacher

static void _I_LGTeacher_sayNB(LGTeacher * self, SEL _cmd) &#123;
    NSLog((NSString *)&__NSConstantStringImpl__var_folders_9t_c60fhy096zg_yjphk3kd3ch40000l2_T_main_906af2_mi_2);
&#125;

static void _I_LGTeacher_sayHello(LGTeacher * self, SEL _cmd) &#123;
    ((void (*)(__rw_objc_super *, SEL))(void *)objc_msgSendSuper)((__rw_objc_super)&#123;(id)self, (id)class_getSuperclass(objc_getClass("LGTeacher"))&#125;, sel_registerName("sayHello"));
    NSLog((NSString *)&__NSConstantStringImpl__var_folders_9t_c60fhy096zg_yjphk3kd3ch40000l2_T_main_906af2_mi_3);
&#125;
// @end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li>子类对象可以通过<code>objc_msgSendSuper</code>方式调用父类的方法，方法的本质还是消息发送，只不过通过的不同发送流程，同样现在用<code>objc_msgSendSuper</code>向父类发消息。</li>
</ul>
</blockquote>
<h4 data-id="heading-9"><code>objc_msgSendSuper</code>底层实现</h4>
<ul>
<li>现在回到<code>objc4.818.2</code>源代码中搜索<code>objc_msgSendSuper</code></li>
</ul>
<p><code>objc</code>源代码的<code>message.h</code>:</p>
<pre><code class="copyable">objc_msgSendSuper(struct objc_super * _Nonnull super, SEL _Nonnull op, ...)
    OBJC_AVAILABLE(10.0, 2.0, 9.0, 1.0, 2.0);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li><code>objc_msgSendSuper</code>的第一个参数是<code>struct objc_super * _Nonnull super</code>类型，继续在源码中查找<code>objc_super</code> 类型</li>
</ul>
</blockquote>
<h4 data-id="heading-10"><code>objc_super</code>结构体</h4>
<pre><code class="copyable">struct objc_super &#123;
    /// Specifies an instance of a class.
    __unsafe_unretained _Nonnull id receiver;

    /// Specifies the particular superclass of the instance to message. 
#if !defined(__cplusplus)  &&  !__OBJC2__
    /* For compatibility with old objc-runtime.h header */
    __unsafe_unretained _Nonnull Class class;
#else
    __unsafe_unretained _Nonnull Class super_class;
#endif
    /* super_class is the first class to search */
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li><code>objc_super</code>结构体类型里面有<code>两个</code>参数:<code>id receiver</code>和<code>Class super_class</code></li>
</ul>
</blockquote>
<h4 data-id="heading-11">验证<code>objc_msgSendSuper</code>方法</h4>
<ul>
<li>在源代码工程中声明一个<code>objc_super</code>结构体变量，赋值后验证方法。</li>
</ul>
<p>代码:</p>
<pre><code class="copyable">int main(int argc, char * argv[]) &#123;
    @autoreleasepool &#123;
        LGTeacher *teach = [LGTeacher alloc];
        [teach sayHello];
//        struct objc_super &#123;
//            /// Specifies an instance of a class.
//            __unsafe_unretained _Nonnull id receiver;
//            __unsafe_unretained _Nonnull Class super_class;
//        #endif
//            /* super_class is the first class to search */
//        &#125;;
        
        struct objc_super kc_objc_super;
        kc_objc_super.receiver = teach;
        kc_objc_super.super_class = LGPerson.class;

       objc_msgSendSuper(&kc_objc_super,@selector(sayHello));
    &#125;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>llvm</code>打印:</p>
<pre><code class="copyable">2021-07-06 01:29:15.208080+0800 001-运行时感受[9801:834295] 666 -[LGPerson sayHello]
2021-07-06 01:29:15.208545+0800 001-运行时感受[9801:834295] 666 -[LGPerson sayHello]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li><code>[teach sayHello]</code>和直接通过<code>objc_msgSendSuper</code>给<code>父类发消息</code>的是一样的。<code>子类的对象</code>可以<code>调用父类的方法</code>。</li>
<li>验证了:方法调用，首先在本类中找，如果没有就到父类中找.</li>
</ul>
</blockquote>
<h2 data-id="heading-12"><code>objc_msgSend</code>汇编原理</h2>
<p>首先找到<code>objc_msgSend</code>所在的<code>libobic.A.dylib</code>汇编库，按住<code>control</code>+单点调试进入<code>objc_msgSend</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c280ff77ac794c928b705e20b6e2ab60~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-07 at 1.01.15 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d654b1ef80143cb8139d82c777da34c~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-07 at 12.59.55 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ul>
<li>汇编显示<code>objc_msgSend</code>在<code>libobjc.A.dylib</code>系统库，在<code>objc4</code>源码中全局搜索<code>objc_msgSend</code>，找到真机的汇编<code>objc-msg-arm64.s</code></li>
</ul>
</blockquote>
<h3 data-id="heading-13">objc_msgSend汇编入口</h3>
<p>通过查找<code>msg_Send</code>的入口<code>ENTERY</code>发现了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/562658693a524539ba27cbc95aed5457~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-07 at 1.49.53 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>p0</code>的定义搜索头文件<code>arm64-asm.h</code>发现了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68dcb2f9446f4af09e0a2395a96e6cf0~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-07 at 1.48.29 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ul>
<li>下面的汇编会用到<code>p0-p17</code>，大家可能对汇编中<code>x0</code>，<code>x1</code>比较熟悉知道是<code>寄存器</code>。<code>p0-p1</code>7就是对<code>x0-x17</code>重新定义。</li>
</ul>
</blockquote>
<h4 data-id="heading-14">分析<code>ENTRY _objc_msgSend</code></h4>
<p>汇编源代码:</p>
<pre><code class="copyable">ENTRY _objc_msgSend //_objc_msgSend 入口，此时有两个输入参数:(isa)id receiver 还有一个是SEL _cmd
UNWIND _objc_msgSend, NoFrame

cmpp0, #0// receiver 和 0 比较 nil check and tagged pointer check
#if SUPPORT_TAGGED_POINTERS     //__LP64__ 64位系统 支持Taggedpointer类型
b.leLNilOrTagged// <= 0时,支持Taggedpointer类型 走LNilOrTagged流程 (MSB tagged pointer looks negative)
#else
b.eqLReturnZero         // == 0时,直接返回nil 就是给空指针发送消息
#endif                          // 对象有值或者isa有值
ldrp13, [x0]// p13 = isa 把x0寄存器里面的地址读取到p13寄存器,对象地址等于isa地址
GetClassFromIsa_p16 p13, 1, x0// p16 = class // p13,1,x0作为参数传到GetClassFromIsa_p16方法里
LGetIsaDone:    //这是一个标记符号,拿到isa操作完以后继续后面的操作
// calls imp or objc_msgSend_uncached   //这个函数传递3个参数 NORMAL _objc_msgSend _objc_msgSend_uncached
CacheLookup NORMAL, _objc_msgSend, __objc_msgSend_uncached  //下一步调用CacheLookup

#if SUPPORT_TAGGED_POINTERS
LNilOrTagged:
    //== 0 直接返回nil
b.eqLReturnZero// nil check
GetTaggedClass
bLGetIsaDone
// SUPPORT_TAGGED_POINTERS
#endif

LReturnZero:
// x0 is already zero
movx1, #0
movid0, #0
movid1, #0
movid2, #0
movid3, #0
ret
    //结束进入_objc_msgSend
END_ENTRY _objc_msgSend
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li>判断<code>receiver</code>是否等于<code>nil</code>， 在判断是否支持<code>Taggedpointer</code>小对象类型</li>
<li>支持<code>Taggedpointer</code>小对象类型，小对象为空 ，返回<code>nil</code>，不为<code>nil</code>处理<code>isa</code>获取<code>class</code>跳转<code>CacheLookup</code>流程</li>
<li>不支持<code>Taggedpointer</code>小对象类型且<code>receiver = nil</code>，跳转<code>LReturnZero</code>流程返回<code>nil</code></li>
<li>不支持<code>Taggedpointer</code>小对象类型且<code>receiver != nil</code>，通过<code>GetClassFromIsa_p16</code>把获取到<code>class</code>存放在<code>p16</code>的寄存器中，然后走<code>CacheLookup</code>流程</li>
</ul>
</blockquote>
<h4 data-id="heading-15"><code>GetClassFromIsa_p16</code>获取<code>Class</code></h4>
<p>汇编源代码:</p>
<pre><code class="copyable">.macro GetClassFromIsa_p16 src, needs_auth, auth_address /* note: auth_address is not required if !needs_auth */

#if SUPPORT_INDEXED_ISA
// Indexed isa
movp16, \src// optimistically set dst = src
tbzp16, #ISA_INDEX_IS_NPI_BIT, 1f// done if not non-pointer isa
// isa in p16 is indexed
adrpx10, _objc_indexed_classes@PAGE
addx10, x10, _objc_indexed_classes@PAGEOFF
ubfxp16, p16, #ISA_INDEX_SHIFT, #ISA_INDEX_BITS  // extract index
ldrp16, [x10, p16, UXTP #PTRSHIFT]// load class from array
1:

#elif __LP64__
.if \needs_auth == 0 // _cache_getImp takes an authed class already
movp16, \src
.else
// 64-bit packed isa
ExtractISA p16, \src, \auth_address
.endif
#else
// 32-bit raw isa
movp16, \src

#endif

.endmacro

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li><code>GetClassFromIsa_p16</code>核心功能获取<code>class</code>存放在<code>p16</code>寄存器</li>
</ul>
</blockquote>
<h4 data-id="heading-16"><code>ExtractISA</code></h4>
<p>在汇编<code>arm-asm.h</code>里:</p>
<pre><code class="copyable">// A12 以上 iPhone X 以上的
#if __has_feature(ptrauth_calls)
   ...
#else
   ...
.macro ExtractISA
and    $0, $1, #ISA_MASK  // and 表示 & 操作， $0 = $1(isa) & ISA_MASK  = class
.endmacro
// not JOP
#endif
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ul>
<li><code>ExtractISA</code> 主要功能 <code>isa & ISA_MASK = class</code> 存放到<code>p16</code>寄存器</li>
</ul>
</blockquote>
<h3 data-id="heading-17">缓存查询流程图</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/824c6346053d4c4290c8cb52a5b2340c~tplv-k3u1fbpfcp-watermark.image" alt="objc_msgSend流程分析.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结</p>
<blockquote>
<ul>
<li>由于上一节<code>cache_t</code>引入的<code>objc_msgSend</code>的分析，既然会有这么多内容，说明苹果底层是用了大量方式方法才保证了<code>objc运行时</code>与<code>发送消息</code>的稳定性。</li>
<li>了解其中的实现方式有利于学习苹果架构原理.</li>
</ul>
</blockquote></div>  
</div>
            