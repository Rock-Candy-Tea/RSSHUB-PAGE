
---
title: 'OC底层原理（六）：cache_t的分析'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853cb5a003164fae94fb111b37a5afb2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 01:01:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853cb5a003164fae94fb111b37a5afb2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><code>cache_t</code>的本质</h2>
<p>在类的方法调用过程中，已知过程是通过<code>SEL</code>(方法编号)在内存中查找<code>IMP</code>(方法指针)，为了使方法响应更加快速，效率更高，不需要每一次都去内存中把方法都遍历一遍，<code>cache_t</code>结构体出现了。<code>cache_t</code>将调用过的方法的<code>SEL</code>和<code>IMP</code>以及<code>receiver</code>以<code>bucket_t</code>结构体方式存储在当前类结构中，以便后续方法的查找。</p>
<p>结构图:</p>
<pre><code class="hljs language-mermaid" lang="mermaid">classDiagram
LGPerson --|> cache_t
bucket_t <|-- cache_t
class LGPerson&#123;
isa
superclass
cache
bits
&#125;
class cache_t&#123;
_buckets
_mask
_flags
_occupied
&#125;
class bucket_t&#123;
_sel
_imp
&#125;
</code></pre>
<p>图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853cb5a003164fae94fb111b37a5afb2~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 12.46.33 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">cache_t结构体</h2>
<p>由结构图可优先探究下<code>cache</code>的类型<code>cache_t</code>，源码<code>objc4-818.2</code>中查看<code>cache_t</code>结构体</p>
<p><code>cache_t</code>源代码:</p>
<pre><code class="copyable">struct cache_t &#123;
private:
    explicit_atomic<uintptr_t> _bucketsAndMaybeMask; // 8bytes
    union &#123;
        struct &#123;
            explicit_atomic<mask_t>    _maybeMask; // 4bytes
#if __LP64__
            uint16_t                   _flags; // 2bytes
#endif
            uint16_t                   _occupied;// 2bytes
        &#125;;
        explicit_atomic<preopt_cache_t *> _originalPreoptCache; // 8bytes
    &#125;;
   
    /*
     #if defined(__arm64__) && __LP64__
     #if TARGET_OS_OSX || TARGET_OS_SIMULATOR
     // __arm64__的模拟器
     #define CACHE_MASK_STORAGE CACHE_MASK_STORAGE_HIGH_16_BIG_ADDRS
     #else
     //__arm64__的真机
     #define CACHE_MASK_STORAGE CACHE_MASK_STORAGE_HIGH_16
     #endif
     #elif defined(__arm64__) && !__LP64__
     //32位 真机
     #define CACHE_MASK_STORAGE CACHE_MASK_STORAGE_LOW_4
     #else
     //macOS 模拟器
     #define CACHE_MASK_STORAGE CACHE_MASK_STORAGE_OUTLINED
     #endif
     ******  中间是不同的架构之间的判断 主要是用来不同类型 mask 和 buckets 的掩码
    */
    
    public:
    void incrementOccupied();
    void setBucketsAndMask(struct bucket_t *newBuckets, mask_t newMask);
    void reallocate(mask_t oldCapacity, mask_t newCapacity, bool freeOld);
    unsigned capacity() const;
    struct bucket_t *buckets() const;
    Class cls() const;
    void insert(SEL sel, IMP imp, id receiver);
    
    // 下面是基本上都是其他的方法的方法
 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ol>
<li><code>_bucketsAndMaybeMask</code>变量<code>uintptr_t</code>占用<code>8字节(bytes)</code>和<code>isa_t</code>中的<code>bits</code>类似，也是一个<code>指针类型</code>里面存放地址</li>
<li>联合体里有一个<code>结构体</code>和一个<code>结构体指针_originalPreoptCache</code></li>
<li>结构体中有三个成员变量 <code>_maybeMask</code>、<code>_flags</code>、<code>_occupied</code>。<code>__LP64__</code>指的是<code>Unix</code>和<code>Unix</code>类系统（<code>Linux</code>和<code>macOS</code>）</li>
<li><code>_originalPreoptCache</code>和<code>结构体</code>是互斥的，<code>_originalPreoptCache</code>初始时候的缓存，现在探究类中的缓存，这个变量基本不会用到</li>
<li><code>cache_t</code>提供了公用的方法去获取值，以及根据不同的架构系统去获取<code>mask</code>和<code>buckets</code>的掩码</li>
</ol>
</blockquote>
<p>在<code>cache_t</code>看到了<code>buckets()</code>，这个类似于<code>class_data_bits_t</code>里面的提供的<code>methods()</code>，都是通过方法获取值。</p>
<p><code>buckets()</code>图:
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feafa418f5d24ae2b5d276ff00ef02b0~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-03 at 3.35.01 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><code>bucket_t</code>结构体</h2>
<p>通过进入<code>bucket_t</code>结构体中查找流程</p>
<p>源代码:</p>
<pre><code class="copyable">struct bucket_t &#123;
private:
    // IMP-first is better for arm64e ptrauth and no worse for arm64.
    // SEL-first is better for armv7* and i386 and x86_64.
#if __arm64__ //真机
    explicit_atomic<uintptr_t> _imp;
    explicit_atomic<SEL> _sel;
#else
    explicit_atomic<SEL> _sel;
    explicit_atomic<uintptr_t> _imp;
#endif
  ....
  //下面是方法省略
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ol>
<li><code>bucket_t</code>区分真机和其它，但是变量没变都是<code>_sel</code>和<code>_imp</code>只不过顺序不一样</li>
<li><code>bucket_t</code>里面存的是<code>_sel</code>和<code>_imp</code>，<code>cache</code>里面缓存的应该是方法</li>
</ol>
</blockquote>
<h3 data-id="heading-3">cache_t 整体结构图</h3>
<p>结构图:</p>
<pre><code class="hljs language-mermaid" lang="mermaid">classDiagram
objc_class --|> cache_t真机
objc_class --|> cache_t模拟器和macos
cache_t模拟器和macos --|> bucket_t非真机
cache_t真机 --|> bucket_t真机
cache_t真机 --|> _maskAndBuckets说明
cache_t真机 --|> cache_t中的mask和buckets
class objc_class&#123;
Class ISA
Class superclass
cache_t cache
class_data_bits_t bits
&#125;
class cache_t模拟器和macos&#123;
struct bucket_t *_buckets
mask_t mask
uint16_t flags
uint16_t _occupied
&#125;
class cache_t真机&#123;
uintptr_t _bucketsAndMaybeMask
mask_t _maybeMask
uint16_t _flags
uint16_t _occupied

capactity()
bucket_t *buckets()
mask_t occupied()
void incrementOccupied()
void setBucketsAndMask()
void reallocate()
void insert()
&#125;

class bucket_t非真机&#123;
explicit_atomic<SEL>_sel
explicit_atomic<uintptr_t>_imp
&#125;
class bucket_t真机&#123;
explicit_atomic<uintptr_t>_sel
explicit_atomic<SEL>_imp
&#125;
class _maskAndBuckets说明&#123;
为了节省内存,读取方便mask和buckets存在一起
&#125;
class cache_t中的mask和buckets&#123;
maskShift = 48
maskZeroBits = 4
maxMask = ((uintptr_t)1 << 
(64 - maskShift)) - 1

static constexpr uintptr_t bucketsMask = ((uintptr_t)1<<
(maskShift - maskZeroBits)) - 1
&#125;
</code></pre>
<p>图:
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf5c02a6c540498a900699af1fff2ac1~tplv-k3u1fbpfcp-watermark.image" alt="Cooci 关于Cache_t原理分析图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">代码断点调试</h2>
<p>创建LGPerson类，自定义一些实例方法，在main函数中创建LGPerson的实例化对象，然后进行lldb调试</p>
<p>代码:</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>

@interface LGPerson : NSObject
@property (nonatomic, copy) NSString *name;
@property (nonatomic) int age;
@property (nonatomic, strong) NSString *hobby;
- (void)saySomething;
+ (void)sayHappy;
@end

@implementation LGPerson

- (instancetype)init&#123;
    if (self = [super init]) &#123;
        self.name = @"Cooci";
    &#125;
    return self;
&#125;
- (void)saySomething&#123;
    NSLog(@"%s",__func__);
&#125;
+ (void)sayHappy&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
@end

int main(int argc, const char * argv[]) &#123;
    @autoreleasepool &#123;

        LGPerson *p  = [LGPerson alloc];
        Class pClass = [LGPerson class];
        NSLog(@"%@",pClass);
    &#125;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>llvm调试:</p>
<pre><code class="copyable">(lldb) p/x pClass
(Class) $0 = 0x00000001000084f0 LGPerson
(lldb) p/x 0x00000001000084f0 + 0x10
(long) $1 = 0x0000000100008500
(lldb) p/x (cache_t *)$1
(cache_t *) $2 = 0x0000000100008500
(lldb) p *$2
(cache_t) $3 = &#123;
  _bucketsAndMaybeMask = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 4298515312
    &#125;
  &#125;
   = &#123;
     = &#123;
      _maybeMask = &#123;
        std::__1::atomic<unsigned int> = &#123;
          Value = 0
        &#125;
      &#125;
      _flags = 32808
      _occupied = 0
    &#125;
    _originalPreoptCache = &#123;
      std::__1::atomic<preopt_cache_t *> = &#123;
        Value = 0x0000802800000000
      &#125;
    &#125;
  &#125;
&#125;
(lldb) p/x $3.buckets()
(bucket_t *) $4 = 0x0000000100362370
(lldb) p *$4
(bucket_t) $5 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = (null) &#123;
      Value = (null)
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 0
    &#125;
  &#125;
&#125;
(lldb) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cdeceab043b4ffa971ea762476b0c84~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 2.25.19 AM.png" loading="lazy" referrerpolicy="no-referrer">
结论:</p>
<blockquote>
<ol>
<li><code>cache</code>的变量的地址，需要<code>首地址偏移16字节</code>即<code>0x10</code>， <code>cache</code>的地址<code>首地址</code>+<code>0x10</code></li>
<li><code>cache_t</code>中的方法<code>buckets()</code>指向的是一块内存的首地址，也是第一个<code>bucket</code>的地址</li>
<li><code>p/x $3.buckets()[indx]</code>的方式打印内存中其余的<code>bucket</code>发现<code>_sel</code>和<code>imp</code></li>
<li><code>LGPerson</code>对象没有调用<code>对象方法</code>，<code>buckets</code>中<code>没有缓存</code>方法的数据</li>
</ol>
</blockquote>
<p>在<code>lldb</code>中调用对象方法，<code>[p sayHello]</code>继续<code>lldb</code>调试</p>
<p>llvm:</p>
<pre><code class="copyable">(lldb) p [p saySomething] //调用了saySomething方法
2021-07-04 02:37:14.269170+0800 KCObjcBuild[26446:4843266] -[LGPerson saySomething]
(lldb) p *$2
(cache_t) $6 = &#123;
  _bucketsAndMaybeMask = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 4316269184
    &#125;
  &#125;
   = &#123;
     = &#123;
      _maybeMask = &#123;
        std::__1::atomic<unsigned int> = &#123;
          Value = 7 //有值
        &#125;
      &#125;
      _flags = 32808
      _occupied = 1 //有值
    &#125;
    _originalPreoptCache = &#123;
      std::__1::atomic<preopt_cache_t *> = &#123;
        Value = 0x0001802800000007
      &#125;
    &#125;
  &#125;
&#125;
(lldb) p/x $6.buckets()
(bucket_t *) $7 = 0x0000000101450a80
(lldb) p *$7
(bucket_t) $8 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = (null) &#123;
      Value = (null)
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 0
    &#125;
  &#125;
&#125;
(lldb) p *($7+1)
(bucket_t) $9 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = (null) &#123;
      Value = (null)
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 0
    &#125;
  &#125;
&#125;
(lldb) p *($7+2)
(bucket_t) $10 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = (null) &#123;
      Value = (null)
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 0
    &#125;
  &#125;
&#125;
(lldb) p *($7+3)
(bucket_t) $11 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = "" &#123;
      Value = ""
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 48416 //直到Value是正常地址值
    &#125;
  &#125;
&#125;
(lldb) p $11.sel()//通过sel()方法获取SEL
(SEL) $12 = "saySomething"
(lldb) p $11.imp(nil,pClass)//通过imp(nil,类)方法获取imp
(IMP) $13 = 0x00000001000039d0 (KCObjcBuild`-[LGPerson saySomething])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结:</p>
<blockquote>
<ol>
<li>调用<code>saySomething</code>后，<code>_mayMask</code>和<code>occupied</code>被赋值，这两个变量应该和缓存是有关系</li>
<li><code>bucket_t</code>结构提供了<code>sel()</code>和<code>imp(nil,pClass)</code>方法</li>
<li><code>saySomething</code>方法的<code>sel</code>和<code>imp</code>，存在<code>bucket</code>中，存在<code>cache</code>中</li>
</ol>
</blockquote>
<h2 data-id="heading-5">脱离源码环境分析<code>cache</code></h2>
<p>通过上一个例子的lldb调试，基本弄清楚<code>cache_t</code>的结构。我们可以按照<code>cache_t</code>的代码结构模仿写一套，这样就不需要在源码环境下的通过<code>lldb</code>。如果需要调用方法，直接添加代码，重新运行就好，这是我们最熟悉的方式了。</p>
<p>代码:</p>
<p>LGPerson:</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
@interface LGPerson : NSObject
@property (nonatomic, copy) NSString *lgName;
@property (nonatomic, strong) NSString *nickName;

- (void)say1;
- (void)say2;
- (void)say3;
- (void)say4;
- (void)say5;
- (void)say6;
- (void)say7;

+ (void)sayHappy;

@end

@implementation LGPerson
- (void)say1&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say2&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say3&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say4&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say5&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say6&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
- (void)say7&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;

+ (void)sayHappy&#123;
    NSLog(@"LGPerson say : %s",__func__);
&#125;
@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>main:</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "LGPerson.h"
#import <objc/runtime.h>

typedef uint32_t mask_t;  // x86_64 & arm64 asm are less efficient with 16-bits

struct kc_bucket_t &#123;
    SEL _sel;
    IMP _imp;
&#125;;
struct kc_cache_t &#123;
    struct kc_bucket_t *_bukets; // 8
    mask_t    _maybeMask; // 4
    uint16_t  _flags;  // 2
    uint16_t  _occupied; // 2
&#125;;

struct kc_class_data_bits_t &#123;
    uintptr_t bits;
&#125;;

// cache class
struct kc_objc_class &#123;
    Class isa;//不可获取
    Class superclass;
    struct kc_cache_t cache;             // formerly cache pointer and vtable
    struct kc_class_data_bits_t bits;
&#125;;

int main(int argc, const char * argv[]) &#123;
    @autoreleasepool &#123;
        LGPerson *p  = [LGPerson alloc];
        Class pClass = p.class;  // objc_clas
        [p say1];
        [p say2];
        //[p say3];
        //[p say4];
        //[p say1];
        //[p say2];
        //[p say3];

        //[pClass sayHappy];
        struct kc_objc_class *kc_class = (__bridge struct kc_objc_class *)(pClass);
        NSLog(@"%hu - %u",kc_class->cache._occupied,kc_class->cache._maybeMask);
        // 0 - 8136976 count
        // 1 - 3
        // 1: 源码无法调试
        // 2: LLDB
        // 3: 小规模取样
        
        // 底层原理
        // a: 1-3 -> 1 - 7
        // b: (null) - 0x0 方法去哪???
        // c: 2 - 7 + say4 - 0xb850 + 没有类方法
        // d: NSObject 父类
        
        for (mask_t i = 0; i<kc_class->cache._maybeMask; i++) &#123;
            struct kc_bucket_t bucket = kc_class->cache._bukets[i];
            NSLog(@"%@ - %pf",NSStringFromSelector(bucket._sel),bucket._imp);
        &#125;
        NSLog(@"Hello, World!");
    &#125;
    return 0;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>llvm:</p>
<pre><code class="copyable">2021-07-04 13:27:58.629469+0800 003-cache_t脱离源码环境分析[27782:4884791] LGPerson say : -[LGPerson say1]
2021-07-04 13:28:08.029414+0800 003-cache_t脱离源码环境分析[27782:4884791] LGPerson say : -[LGPerson say2]
2021-07-04 13:28:08.029963+0800 003-cache_t脱离源码环境分析[27782:4884791] 2 - 3
2021-07-04 13:28:08.030417+0800 003-cache_t脱离源码环境分析[27782:4884791] say1 - 0xb858f
2021-07-04 13:28:08.030502+0800 003-cache_t脱离源码环境分析[27782:4884791] say2 - 0xb808f
2021-07-04 13:28:08.030545+0800 003-cache_t脱离源码环境分析[27782:4884791] (null) - 0x0f
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p>由于<code>objc_class</code>的<code>Class ISA</code>是继承<code>objc_object</code>，自定义的结构体<code>kc_objc_class</code>要手动添加<code>Class ISA</code>，不然代码转换会转换错误</p>
</blockquote>
<p>在<code>main</code>function里取消<code>say3</code>、<code>say4</code>的注释;</p>
<p>再看看llvm打印:</p>
<pre><code class="copyable">2021-07-04 13:47:14.016817+0800 003-cache_t脱离源码环境分析[28227:4896303] LGPerson say : -[LGPerson say1]
2021-07-04 13:47:19.322219+0800 003-cache_t脱离源码环境分析[28227:4896303] LGPerson say : -[LGPerson say2]
2021-07-04 13:47:19.322786+0800 003-cache_t脱离源码环境分析[28227:4896303] LGPerson say : -[LGPerson say3]
2021-07-04 13:47:19.322873+0800 003-cache_t脱离源码环境分析[28227:4896303] LGPerson say : -[LGPerson say4]
2021-07-04 13:47:19.322941+0800 003-cache_t脱离源码环境分析[28227:4896303] 2 - 7
2021-07-04 13:47:19.323424+0800 003-cache_t脱离源码环境分析[28227:4896303] say4 - 0xb9b8f
2021-07-04 13:47:19.323499+0800 003-cache_t脱离源码环境分析[28227:4896303] (null) - 0x0f
2021-07-04 13:47:19.323593+0800 003-cache_t脱离源码环境分析[28227:4896303] say3 - 0xb9e8f
2021-07-04 13:47:19.323660+0800 003-cache_t脱离源码环境分析[28227:4896303] (null) - 0x0f
2021-07-04 13:47:19.323725+0800 003-cache_t脱离源码环境分析[28227:4896303] (null) - 0x0f
2021-07-04 13:47:19.323784+0800 003-cache_t脱离源码环境分析[28227:4896303] (null) - 0x0f
2021-07-04 13:47:19.323845+0800 003-cache_t脱离源码环境分析[28227:4896303] (null) - 0x0f
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<ol>
<li><code>_occupied</code>和<code>_maybeMask</code>是作用？</li>
<li><code>say1</code>和<code>say2</code>方法怎么消失了？</li>
<li><code>cache</code>存储的位置怎么是乱序的呢？比如<code>say4</code>在最前面，第二与第四怎么是空的?</li>
<li>通过这个例子我们想要知道<code>_occupied</code>和<code>_maybeMask</code>是什么？只有去看源码，看看在什么地方赋值的。弄清楚缓存方法是怎么插入到<code>buket</code>中的。</li>
</ol>
</blockquote>
<h2 data-id="heading-6"><code>cache_t</code>源码探究</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c3865c31bd042049fdb8760e622f3e9~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 2.12.38 PM.png" loading="lazy" referrerpolicy="no-referrer">
首先找到<code>cache_t</code>的方法缓存的入口<code>insert(SEL sel, IMP imp, id receiver)</code>，里面有参数<code>sel</code>和<code>imp</code>；而且还有方法名<code>insert</code>，看看它的具体实现，由于<code>insert</code>内的代码过多我们分步骤说明</p>
<p><code>obj-cache.mm</code>中源代码:</p>
<pre><code class="copyable">void cache_t::insert(SEL sel, IMP imp, id receiver)
&#123;
    runtimeLock.assertLocked();

    // Never cache before +initialize is done
    if (slowpath(!cls()->isInitialized())) &#123;
        return;
    &#125;

    if (isConstantOptimizedCache()) &#123;
        _objc_fatal("cache_t::insert() called with a preoptimized cache for %s",
                    cls()->nameForLogging());
    &#125;

#if DEBUG_TASK_THREADS
    return _collecting_in_critical();
#else
#if CONFIG_USE_CACHE_LOCK
    mutex_locker_t lock(cacheUpdateLock);
#endif

    ASSERT(sel != 0 && cls()->isInitialized());
    // Use the cache as-is if until we exceed our expected fill ratio.
    mask_t newOccupied = occupied() + 1; // 1+1 occupied()获取当前的occupied，第一次进入occupied = 0, newOccupied = 1
    unsigned oldCapacity = capacity(), capacity = oldCapacity;//容量的个数 第一次进入oldCapacity = 0, capacity = 0
    if (slowpath(isConstantEmptyCache())) &#123; //缓存是否为空 occupied() == 0, 情况发生的概率小，只有第一次进入时会为0
        // Cache is read-only. Replace it.
        if (!capacity) capacity = INIT_CACHE_SIZE;//4 ,当capacity = 0, 1 << 2 -> 0100 = 4, capacity = 4 首次扩容是4
        reallocate(oldCapacity, capacity, /* freeOld */false);// oldCapacity = 0, capacity = 4, freeOld = false
    &#125;
    else if (fastpath(newOccupied + CACHE_END_MARKER <= cache_fill_ratio(capacity))) &#123; // newOccupied + 1 <= capacity * 3 / 4
        // Cache is less than 3/4 or 7/8 full. Use it as-is.
        //第一次会扩容 capacity = 4, 此时 newOccupied = 1, 1 + 1 <= (4 * 3 / 4 = 3)
        //第二次会扩容 capacity = 4, 此时 newOccupied = 2, 2 + 1 <= 3 不满足条件，走其他流程
        //第三次会扩容 capacity = 4, 此时 newOccupied = 3, 3 + 1 <= 3
        //如果缓存个数小于容量capacity * 3 / 4就什么都不用做，接着往后走
    &#125;
#if CACHE_ALLOW_FULL_UTILIZATION //如果允许存满就是不留空位直接走下面流程
    else if (capacity <= FULL_UTILIZATION_CACHE_SIZE && newOccupied + CACHE_END_MARKER <= capacity) &#123;
        // Allow 100% cache utilization for small buckets. Use it as-is.
        // (FULL_UTILIZATION_CACHE_SIZE = 1 << 3 = 8) && (newOccupied + 1 <= capacity)
        // 比如newOccupied = 7, capacity = 8, 7+1 <= 8满足条件，走后面的存储流程存满
    &#125;
#endif
    else &#123;// 4*2 = 8 容量超过了 3/4 的限制
        capacity = capacity ? capacity * 2 : INIT_CACHE_SIZE;//capacity有值进行2倍扩容,否则 capacity = 4
        if (capacity > MAX_CACHE_SIZE) &#123;//判断 capacity > 2^(16-1) = 2^15 前面我探索了mask和buckets存在一起,其中mask的最大值就是2^15,联系起来了
            capacity = MAX_CACHE_SIZE; // 超过 capacity = 2^15
        &#125;
        reallocate(oldCapacity, capacity, true); //如果超过容量的3/4就会重新开辟新内存 freeOld = true 是oldCapacity内存会被回收
    &#125;

    bucket_t *b = buckets(); //拿到第一个bucket的地址就是buckets()指向这块内存的首地址
    mask_t m = capacity - 1; // 4-1=3 : mask = capacity - 1
    mask_t begin = cache_hash(sel, m);//求哈希hash的下标index: 根据 sel 和 mask
    mask_t i = begin;//开始位置

    // Scan for the first unused slot and insert there.
    // There is guaranteed to be an empty slot.
    do &#123;
        if (fastpath(b[i].sel() == 0)) &#123;//如果当前的bucket是空时
            incrementOccupied();// _occupied ++ : 就是缓存一个bucket,_occupied就会加1, 意思就是占位, bucket的个数等于_occupied
            b[i].set<Atomic, Encoded>(b, sel, imp, cls());// 把sel和imp写入bucket,开始缓存方法
            return;
        &#125;
        if (b[i].sel() == sel) &#123;//如果缓存的buckets中已经有了方法就跳过
            // The entry was added to the cache by some other thread
            // before we grabbed the cacheUpdateLock.
            return;
        &#125;
    &#125; while (fastpath((i = cache_next(i, m)) != begin));//如果存在hash冲突,hash冲突就是方法不一样但是下标一样,再次hash和begin比较不同就缓存

    bad_cache(receiver, (SEL)sel);//坏的缓存
#endif // !DEBUG_TASK_THREADS
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">分析<code>insert</code></h3>
<h4 data-id="heading-8">计算当前所占容量大小</h4>
<p><code>insert</code>计算容量图:
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00763ebeb87c4a7ba6caa50a14617ef6~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 2.27.08 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li><code>occupied()</code>获取当前所占的容量，其实就是告诉你缓存中有几个<code>bucket</code>了</li>
<li><code>newOccupied = occupied() + 1</code>，表示你是第几个进来缓存的</li>
<li><code>oldCapacity</code> 目的是为了重新扩容的时候释放旧的内存</li>
</ol>
</blockquote>
<h4 data-id="heading-9">开辟容量</h4>
<p>第一次进入扩容图:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7715de490f224b6d965dfb787611b1c3~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 2.36.33 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li>只有第一次缓存方法的时，才会去开辟容量默认开辟容量是 <code>capacity = INIT_CACHE_SIZE</code> 即<code>capacity = 4</code> 就是<code>4个bucket的内存大小</code></li>
<li><code>reallocate(oldCapacity, capacity, /* freeOld */false)</code>开辟内存，<code>freeOld</code>变量控制是否释放旧的内存</li>
</ol>
</blockquote>
<h5 data-id="heading-10">reallocate方法探究</h5>
<p>代码:</p>
<pre><code class="copyable">ALWAYS_INLINE
void cache_t::reallocate(mask_t oldCapacity, mask_t newCapacity, bool freeOld)
&#123;
    bucket_t *oldBuckets = buckets();//获取oldBuckets的首地址
    bucket_t *newBuckets = allocateBuckets(newCapacity);//获取新开辟的newBuckets的首地址

    // Cache's old contents are not propagated. 
    // This is thought to save cache memory at the cost of extra cache fills.
    // fixme re-measure this

    ASSERT(newCapacity > 0);
    ASSERT((uintptr_t)(mask_t)(newCapacity-1) == newCapacity-1);
    //设置Buckets和Mash的值, Buckets存的是newBuckets的首地址, Mask存的是newCapacity - 1
    //此时的 _occupied = 0因为是新开辟的
    setBucketsAndMask(newBuckets, newCapacity - 1);
    //如果freeold是true的话，释放回收旧的内存
    if (freeOld) &#123;
        collect_free(oldBuckets, oldCapacity);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>reallocate</code> 方法主要做三件事:<br>
1.<code> allocateBuckets</code>开辟内存<br>
2. <code>setBucketsAndMask</code>设置<code>mask</code>和<code>buckets</code>的值<br>
3. <code>collect_free</code>是否释放旧的内存，由<code>freeOld</code>控制</p>
</blockquote>
<h5 data-id="heading-11"><code>allocateBuckets</code>方法探究</h5>
<p><code>allocateBuckets</code>源代码:</p>
<pre><code class="copyable">size_t cache_t::bytesForCapacity(uint32_t cap)
&#123;
    return sizeof(bucket_t) * cap;//1. bucket_t大小 * cap
&#125;

#if CACHE_END_MARKER // macOS 模拟器

bucket_t *cache_t::endMarker(struct bucket_t *b, uint32_t cap)
&#123;
    return (bucket_t *)((uintptr_t)b + bytesForCapacity(cap)) - 1;//2. (首地址+开辟的内存) - 1: 获取最后一个位置的地址
&#125;

bucket_t *cache_t::allocateBuckets(mask_t newCapacity)
&#123;
    // Allocate one extra bucket to mark the end of the list.
    // This can't overflow mask_t because newCapacity is a power of 2.
    bucket_t *newBuckets = (bucket_t *)calloc(bytesForCapacity(newCapacity), 1);//1.开辟 newCapacity * bucket_t 大小内存

    bucket_t *end = endMarker(newBuckets, newCapacity);//2.获取最后一个位置的bucket的地址

#if __arm__
    // End marker's sel is 1 and imp points BEFORE the first bucket.
    // This saves an instruction in objc_msgSend.
    end->set<NotAtomic, Raw>(newBuckets, (SEL)(uintptr_t)1, (IMP)(newBuckets - 1), nil);
#else
    // End marker's sel is 1 and imp points to the first bucket.
    // 把最后一个位置的bucket的赋值 sel = 1 ,imp = 第一个bucket的地址,最后一个位置默认被占用
    end->set<NotAtomic, Raw>(newBuckets, (SEL)(uintptr_t)1, (IMP)newBuckets, nil);
#endif
    
    if (PrintCaches) recordNewCache(newCapacity);//记录新的缓存

    return newBuckets;
&#125;

#else
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>allocateBuckets</code>方法主要做两件事:</p>
<ol>
<li><code>calloc(bytesForCapacity(newCapacity), 1)</code>开辟<code>newCapacity * bucket_t</code> 大小的内存</li>
<li><code>end->set</code>将开辟内存的最后一个位置存入<code>sel = 1</code>，<code>imp = 第一个buket位置的地址</code></li>
</ol>
</blockquote>
<h5 data-id="heading-12"><code>setBucketsAndMask</code>方法探究</h5>
<p>源代码:</p>
<pre><code class="copyable">#if CACHE_MASK_STORAGE == CACHE_MASK_STORAGE_OUTLINED

void cache_t::setBucketsAndMask(struct bucket_t *newBuckets, mask_t newMask)
&#123;
    // objc_msgSend uses mask and buckets with no locks.
    // It is safe for objc_msgSend to see new buckets but old mask.
    // (It will get a cache miss but not overrun the buckets' bounds).
    // It is unsafe for objc_msgSend to see old buckets and new mask.
    // Therefore we write new buckets, wait a lot, then write new mask.
    // objc_msgSend reads mask first, then buckets.

#ifdef __arm__ //允许使用SUPPORT_MOD = 1 MOD运算符
    // ensure other threads see buckets contents before buckets pointer
    mega_barrier();//防止多线程同时访问

    _bucketsAndMaybeMask.store((uintptr_t)newBuckets, memory_order_relaxed);

    // ensure other threads see new buckets before new mask
    mega_barrier();

    _maybeMask.store(newMask, memory_order_relaxed);
    _occupied = 0;
#elif __x86_64__ || i386 //macOS 和 模拟器
    // ensure other threads see buckets contents before buckets pointer
    //向_bucketsAndMaybeMask 写入数据
    _bucketsAndMaybeMask.store((uintptr_t)newBuckets, memory_order_release);//(uintptr_t)newBuckets是buckets()指向这块内存的首地址(也就是第一个buckets的内存)

    // ensure other threads see new buckets before new mask
    //向_maybeMask 写入数据
    _maybeMask.store(newMask, memory_order_release);
    _occupied = 0;
#else
#error Don't know how to do setBucketsAndMask on this architecture.
#endif
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>setBucketsAndMask</code>主要根据不同的架构系统向<code>_bucketsAndMaybeMask</code> 和 <code>_maybeMask</code>写入数据</p>
</blockquote>
<h5 data-id="heading-13"><code>collect_free</code>方法探究</h5>
<p><code>collect_free</code>源代码:</p>
<pre><code class="copyable">void cache_t::collect_free(bucket_t *data, mask_t capacity)
&#123;
#if CONFIG_USE_CACHE_LOCK
    cacheUpdateLock.assertLocked();
#else
    runtimeLock.assertLocked();
#endif

    if (PrintCaches) recordDeadCache(capacity);

    _garbage_make_room ();//创建垃圾回收站
    garbage_byte_size += cache_t::bytesForCapacity(capacity);//获取开辟内存的大小
    garbage_refs[garbage_count++] = data;//将buckets的地址往后移
    cache_t::collectNolock(false);//清空数据，回收内存
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>collect_free</code>主要是清空数据，回收内存</p>
</blockquote>
<h4 data-id="heading-14">容量小于3/4</h4>
<p>图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5adc3b98bf75486b94a642549a8a81f5~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 3.32.11 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li>当需要缓存的方法所占的容量<code>总容量3/4</code>是就会直接走缓存流程</li>
<li>苹果的设计思想，探究了很多底层就会发现，苹果做什么事情都会留有余地。一方面可能为了日后的优化或者扩展，另一方面可能是为了安全，内存对齐也是这样</li>
</ol>
</blockquote>
<h4 data-id="heading-15">容量存满</h4>
<p>图:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/578ce8461d844e54848c329a976f355a~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 3.36.47 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li>苹果提供变量，很人性化，如果你需要把缓存的容量存满，默认是不存满的</li>
<li>个人建议不要存满，就按照默认的来，如果存满有可能出现其它的问题，很难去排查</li>
</ol>
</blockquote>
<h4 data-id="heading-16">容量超过3/4</h4>
<p>图:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df1439cb4b54da29058fad3774965af~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 3.43.54 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li>容量超过<code>3/4</code>，系统此时会进行<code>两倍扩容</code>，扩容的最大容量不会超过<code>mask</code>的<code>最大值2^15</code></li>
<li>扩容的时候会进行一步重要的操作，开辟新的内存，释放回收旧的内存，此时的<code>freeOld = true</code></li>
</ol>
</blockquote>
<h4 data-id="heading-17">缓存方法</h4>
<p>图解:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e038f79c18c44beaa0d94605200db9e~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 3.53.02 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论:</p>
<blockquote>
<ol>
<li>首先拿到<code>bucket()</code>指向开辟这块内存<code>首地址</code>，也就是第一个<code>bucket</code>的地址，<code>bucket()</code>既不是数组也不是链表，只是一块<code>连续的内存</code></li>
<li><code>hash函数</code>根据缓存<code>sel</code>和<code>mask</code>，计算出<code>hash下标</code>。为什么需要<code>mask</code>呢？<code>mask</code>的实际作用是告诉系统你只能存前<code>capacity - 1</code>中的位置，比如<code>capacity = 4</code>时，缓存的方法只能存前面<code>3个空位</code></li>
<li>开始缓存，当前的位置没有数据，就缓存该方法。如果该位置有方法且和你的方法一样的，说明该方法缓存过了，直接<code>return</code>。如果存在<code>hash冲突</code>，下标一样，<code>sel</code>不一样，此时会进行再次<code>hash</code>，冲突解决继续缓存</li>
</ol>
</blockquote>
<h5 data-id="heading-18">incrementOccupied</h5>
<p>源代码:</p>
<pre><code class="copyable">void cache_t::incrementOccupied() 
&#123;
    _occupied++;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>_occupied</code>自动<code>加1</code>，<code>_occupied</code>表示内存中已经存储缓存方法的的个数</p>
</blockquote>
<h5 data-id="heading-19"><code>cache_hash</code> 和 <code>cache_next</code></h5>
<p><code>cache_hash</code>源代码:</p>
<pre><code class="copyable">static inline mask_t cache_hash(SEL sel, mask_t mask) 
&#123;
    uintptr_t value = (uintptr_t)sel;
#if CONFIG_USE_PREOPT_CACHES //真机
    value ^= value >> 7;
#endif
    return (mask_t)(value & mask); //和mask进行一次与运算
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>cache_next</code>源代码:</p>
<pre><code class="copyable">#if CACHE_END_MARKER //__arm__  ||  __x86_64__  ||  __i386__
static inline mask_t cache_next(mask_t i, mask_t mask) &#123;
    return (i+1) & mask;
&#125;
#elif __arm64__ //真机
static inline mask_t cache_next(mask_t i, mask_t mask) &#123;
    return i ? i-1 : mask;
&#125;
#else
#error unexpected configuration
#endif

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>cache_has</code>主要是生成<code>hash下标</code>，<code>cache_next</code>主要是解决<code>hash冲突</code></p>
</blockquote>
<h5 data-id="heading-20">缓存写入方法<code>set</code></h5>
<p>源代码:</p>
<pre><code class="copyable">//macOS或者模拟器
template<Atomicity atomicity, IMPEncoding impEncoding>
void bucket_t::set(bucket_t *base, SEL newSel, IMP newImp, Class cls)
&#123;
    ASSERT(_sel.load(memory_order_relaxed) == 0 ||
           _sel.load(memory_order_relaxed) == newSel);

    // objc_msgSend uses sel and imp with no locks.
    // It is safe for objc_msgSend to see new imp but NULL sel
    // (It will get a cache miss but not dispatch to the wrong place.)
    // It is unsafe for objc_msgSend to see old imp and new sel.
    // Therefore we write new imp, wait a lot, then write new sel.
    // 原有的imp进行编码 (和class进行异或运算)转化为 uintptr类型
    uintptr_t newIMP = (impEncoding == Encoded
                        ? encodeImp(base, newImp, newSel, cls)
                        : (uintptr_t)newImp);

    if (atomicity == Atomic) &#123;//修饰符号 atomic
        _imp.store(newIMP, memory_order_relaxed);
        
        if (_sel.load(memory_order_relaxed) != newSel) &#123;
#ifdef __arm__
            mega_barrier();
            _sel.store(newSel, memory_order_relaxed);
#elif __x86_64__ || __i386__
            _sel.store(newSel, memory_order_release);
#else
#error Don't know how to do bucket_t::set on this architecture.
#endif
        &#125;
    &#125; else &#123;
        _imp.store(newIMP, memory_order_relaxed);//写入_imp
        _sel.store(newSel, memory_order_relaxed);//写入_sel
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>set</code>把<code>sel</code>和<code>imp</code>写入<code>bucket</code>，开始缓存方法</p>
</blockquote>
<h3 data-id="heading-21"><code>insert</code>调用流程</h3>
<p><code>xcode</code>关闭汇编调试，探究调用一个实例方法是怎么调用了<code>cache</code>里面的<code>insert</code>方法？在<code>insert</code>方法中打个断点，然后运行源码</p>
<p>图:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad1b669332e64930b5fe9d2f161b290b~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 4.20.05 PM.png" loading="lazy" referrerpolicy="no-referrer">
结论:</p>
<blockquote>
<p>堆栈信息显示调用<code>insert方法</code>流程：<code>_objc_msgSend_uncached</code> --> <code>lookUpImpOrForward</code> --> <code>log_and_fill_cache</code> --> <code>cache_t::insert</code></p>
</blockquote>
<p>堆栈信息只显示到<code>_objc_msgSend_uncached</code>，但是我们是调用了 <code>[p say1]</code> 也就是实例方法最后调用了<code>cache_t::insert</code>。现在我们知道了部分流程<code>_objc_msgSend_uncached</code> 到 <code>cache_t::insert</code>过程。<code>[p say1]</code> 到 <code>_objc_msgSend_uncached </code>这个过程并不清楚。只能打开<code>Xcode</code>的汇编调试功能看汇编流程</p>
<p>汇编图:
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/174c5c54eca2415dbe9a0ce92c759aa4~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-04 at 4.28.21 PM.png" loading="lazy" referrerpolicy="no-referrer">
结论:</p>
<blockquote>
<ol>
<li><code>[p say1]</code>底层实现的是<code>objc_msgSend</code>方法，这个方法是<code>消息发送方法</code>将在下一节进行讲解</li>
<li>调用<code>insert</code>方法流程：<code>[p say1]</code>底层实现 <code>objc_msgSend</code> --> <code>_objc_msgSend_uncached</code> --> <code>lookUpImpOrForward</code> --> <code>log_and_fill_cache</code> --> <code>cache_t::insert</code></li>
</ol>
</blockquote>
<h4 data-id="heading-22"><code>insert</code>调用流程图</h4>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR
A[方法] -.-> B(objc_msgSend) -.-> C(_objc_msgSend_uncached) -.-> D(lookUpImpOrForward) -.-> E(log_and_fill_cache) -.-> cache_t::insert
</code></pre>
<h2 data-id="heading-23">补充:</h2>
<h3 data-id="heading-24">小知识:</h3>
<blockquote>
<ol>
<li>_sel _imp可查找上一节</li>
<li>哈希值方便增删,后面补充</li>
<li>数组是根据下标进行查找</li>
<li>链表有利于数组链接</li>
<li><code>哈希</code>函数:<code>>> % 下标</code> -> <code>数据</code></li>
<li><code>8%5 = 1</code> VS <code>8%6 = 1</code></li>
<li>容量的<code>3/4</code> -> 负载因子 <code>0.75</code> 空间利用率 + <code>哈希冲突 </code>-> <code>底层链表</code> + <code>红黑树</code> 频率过多</li>
</ol>
</blockquote>
<h3 data-id="heading-25"><code>buckt</code>结构<code>llvm</code>调试</h3>
<blockquote>
<p>重点:<code>_bucketsAndMaybeMask</code>存储的是<code>bucket首地址</code></p>
</blockquote>
<p>llvm调试:</p>
<pre><code class="copyable">2021-07-03 21:25:55.822979+0800 KCObjcBuild[21684:4692396] LGPerson say : -[LGPerson say1]
KCObjcBuild was compiled with optimization - stepping may behave oddly; variables may not be available.
(lldb) p/x LGPerson.class
(Class) $0 = 0x0000000100008510 LGPerson
(lldb) p (cache_t *)0x0000000100008520
(cache_t *) $1 = 0x0000000100008520
(lldb) p *$1
(cache_t) $2 = &#123;
  _bucketsAndMaybeMask = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 4301421904
    &#125;
  &#125;
   = &#123;
     = &#123;
      _maybeMask = &#123;
        std::__1::atomic<unsigned int> = &#123;
          Value = 3
        &#125;
      &#125;
      _flags = 32808
      _occupied = 1
    &#125;
    _originalPreoptCache = &#123;
      std::__1::atomic<preopt_cache_t *> = &#123;
        Value = 0x0001802800000003
      &#125;
    &#125;
  &#125;
&#125;
(lldb) p $2.buckets()
(bucket_t *) $3 = 0x0000000100627d50
(lldb) p *$3
(bucket_t) $4 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = (null) &#123;
      Value = (null)
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 0
    &#125;
  &#125;
&#125;
(lldb) p $3[1]
(bucket_t) $5 = &#123;
  _sel = &#123;
    std::__1::atomic<objc_selector *> = "" &#123;
      Value = ""
    &#125;
  &#125;
  _imp = &#123;
    std::__1::atomic<unsigned long> = &#123;
      Value = 48912
    &#125;
  &#125;
&#125;
(lldb) p $5.sel()
(SEL) $6 = "say1"
(lldb) p $3+1
(bucket_t *) $7 = 0x0000000100627d60
(lldb) p $7->sel()
(SEL) $8 = "say1"
(lldb) p $2._bucketsAndMaybeMask
(explicit_atomic<unsigned long>) $9 = &#123;
  std::__1::atomic<unsigned long> = &#123;
    Value = 4301421904
  &#125;
&#125;
(lldb) p/x 4301421904
(long) $10 = 0x0000000100627d50
(lldb) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<pre><code class="copyable">buckets = _bucketsAndMaybeMask $3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26"><code>bucketMask</code>注意点</h3>
<blockquote>
<ol>
<li>注意点 <code>bucketMask</code>要注意平台<code>x86-64</code>、<code>ArmV64</code>等大小端地址</li>
<li><code>大端</code>地址<code>从左到右</code></li>
<li><code>小端</code>地址<code>从右到左</code></li>
</ol>
</blockquote>
<p>举例子:</p>
<pre><code class="copyable">lldb) x p
0x100661c70: 11 85 00 00 01 80 1d 01 00 00 00 00 00 00 00 00  ................
0x100661c80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
(lldb) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<pre><code class="copyable">取前8位作为地址
大端:0x1185000001801d01
小端:0x011d800100008511
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            