
---
title: 'Tagged Pointer对象安全气垫为何会失效'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f3ebb46a2b41c9834fb2b4c6eb9af4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 22:56:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f3ebb46a2b41c9834fb2b4c6eb9af4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>安全气垫的功能和原理的介绍可以参考这篇：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fneyoufan.github.io%2F2017%2F01%2F13%2Fios%2FBayMax_HTSafetyGuard%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://neyoufan.github.io/2017/01/13/ios/BayMax_HTSafetyGuard/" ref="nofollow noopener noreferrer">《大白健康系统--iOS APP运行时Crash自动修复系统》</a>，其中OC方法查找不到<code>Unrecognized Selector</code>是线上最容易出现的一类错误。自安全气垫上线之后这一类错误可以被安全气垫兜住，不会触发用户崩溃，同时也支持将报错的异常调用栈上报到公司稳定性监控后台，方便在新版本修复。但是某一天一位同学反馈了一个<code>Unrecognized Selector</code>类型的崩溃并没有被兜住造成了比较大面积的Crash。报错信息如下：</p>
<pre><code class="copyable">NSException -[__NSCFNumber lengthOfBytesUsingEncoding:]: unrecognized selector sent to instance 0xbc58921bca740bf4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检查该产品安全气垫的开关，线上版本一直是开启的状态。因此这个问题确定没有被兜住逃逸为Crash，不符合预期，需要查明原因并解决。</p>
<h1 data-id="heading-1">排查过程</h1>
<p>通过崩溃调用栈可以看到找不到方法的对象是一个NSNumber对象。在APM SDK Example中模拟构建一个NSNumber对象并且调用一个其不存在的方法，果然安全气垫没有生效进而触发了崩溃！打断点调试发现了问题：</p>
<pre><code class="copyable">- (id)hook_forwardingTargetForSelector:(SEL)aSelector &#123;
  id forwardObject = [self hook_forwardingTargetForSelector: aSelector];
  if (forwardObject) &#123;
    return forwardObject;
  &#125;
   
  if ([self methodSignatureForSelector:aSelector]) &#123;
    return forwardObject;
  &#125;
   
  // Check address of 'self' and 'aSelector' are valid
  if (!check_valid_address(self, aSelector)) &#123;
    return nil;
  &#125;
   
  //notify protect happened
  //...
  
  return USELForwarder.class;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打断点调试发现原来这段代码<code>check_valid_address</code>方法校验没有通过，那么这个判断条件的意义是什么呢？</p>
<p>经了解，老版本出现过某个对象变成僵尸对象之后，再执行安全气垫防护的流程会挂在中间某个步骤，因为该对象已经释放，所以内存的结构会是一个极其不确定的状态。因此从APM SDK某个版本开始，新增了判断对象本身和selector地址是否合法的判断，如果地址非法的话则直接返回，不作防护。再看<code>check_valid_address</code>这个方法的具体实现：</p>
<pre><code class="copyable">static bool check_valid_address(id _Nonnull objc, SEL _Nonnull aSelector) &#123;
  vm_offset_t data;
  mach_msg_type_number_t dataSize;
  kern_return_t kt = vm_read(current_task(), (vm_address_t)objc, sizeof(uintptr_t), &data, &dataSize);
   
  if (kt != KERN_SUCCESS) &#123;
    return false;
  &#125;
   
  bool valid = true;
  kt = vm_read(current_task(), (vm_address_t)sel_getName(aSelector), sizeof(uintptr_t), &data, &dataSize);
  if (kt != KERN_SUCCESS) &#123;
    valid = false;
  &#125;
   
  return valid;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到其实实现比较简单，通过<code>vm_read</code>判断对象地址的可读性。单步调试后发现测试case居然进入到了第6行条件的内部，直接返回了。打印出objc的地址居然是一个超大的地址<code>0xffb3bbad03eeba55</code>！查看<code>vm_read</code> api解释，返回值为1的含义是：<code>Specified address is not currently valid.</code>通过苹果的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopensource.apple.com%2Fsource%2Fxnu%2Fxnu-6153.81.5%2Fosfmk%2Fmach%2Farm%2Fvm_param.h" target="_blank" rel="nofollow noopener noreferrer" title="https://opensource.apple.com/source/xnu/xnu-6153.81.5/osfmk/mach/arm/vm_param.h" ref="nofollow noopener noreferrer">XNU内核源码</a>可以看到苹果arm64架构设备的虚拟内存地址的上限是0xfc0000000。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f3ebb46a2b41c9834fb2b4c6eb9af4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很显然，这里NSNumber的地址是一个非法的地址。那么为什么NSNumer对象的地址会如此大呢？突然想到arm64设备发布之后，苹果引入了<code>Tagged Pointer</code>技术，用于优化<code>NSNumber</code>、<code>NSDate</code>、<code>NSString</code>等小对象的存储。这里的现象会不会跟<code>Tagged Pointer</code>有关系呢？</p>
<h1 data-id="heading-2">原理探究</h1>
<h2 data-id="heading-3">Tagged Pointer技术背景</h2>
<p>在arm64设备上苹果引入了<code>Tagged Pointer</code>技术，NSNumber等对象的值直接存储在了指针中，不必在堆上为其分配内存，节省了很多内存开销。在性能上，有着 3 倍空间效率的提升以及 106 倍创建和销毁速度的提升。</p>
<h2 data-id="heading-4">Tagged Pointer内存结构</h2>
<p>与macOS不同，iOS系统采用 <code>MSB</code>（<code>Most Significant Bit</code>，即最高有效位）为<code>Tagged Pointer</code>标志位。</p>
<p>从iOS14系统版本开始苹果对<code>Tagged Pointer</code>的内存结构有调整。以上文中的NSNumber对象为例，参考系统源码，一些技术博客，结合自己实验的结果，NSNumber类型<code>Tagged Pointer</code>的内存结构分析如下，其中扩展标志位因为比较少见，这里分析时暂时忽略。</p>
<h3 data-id="heading-5">iOS14系统以下</h3>
<p>无扩展标志位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/151c3ae8a7e04b57857044f91d187430~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有扩展标志位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32207f6792274285a7d8728d2af7be36~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">iOS14系统以上</h3>
<p>无扩展标志位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/909154c6bbc04fbc92ef83ada8dd0fc3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有扩展标志位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/768d560b07c64c2ba94b1c3f2758fd1d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">各bit含义解释</h3>
<ul>
<li>_OBJC_TAG_MASK：占1bit，是<code>Tagged Pointer</code>标志位，1意味着该地址是<code>Tagged Pointer</code>，0则不是。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2020%2F10163%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/videos/play/wwdc2020/10163/" ref="nofollow noopener noreferrer">WWDC 2020的一个session</a>中解释了，arm64架构采用<code>MSB</code>也就是最高位作为<code>Tagged Pointer</code>标志位的原因就是为了优化性能，<code>objc_msgsend</code>在正常的对象方法查找之前会首先排除nil和<code>Tagged Pointer</code>，相比于分开检查<code>nil</code>和<code>Tagged Pointer</code>，这样就可以给<code>objc_msgsend</code>中的常见情况节省了一个分支条件。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65ff09472436422eb662e19e304d9df2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Tag_Index：占3bit，是类标志位，可以在<code>Runtime</code>源码中查看<code>NSNumber</code>、<code>NSDate</code>、<code>NSString</code>等类的标志位。</li>
<li>Extended_Tag_Index：占8bit，只有当Tag_Index=7的时候才存在，表示这是一个用于扩展的标志位，会额外占用8位来存储扩展的Tag Index。类标识的基本类型和扩展类型我们可以在<code>Runtime</code>源码中的<code>objc_tag_index_t</code>查到：</li>
</ul>
<pre><code class="copyable">// objc_tag_index_t
&#123;
    // 60-bit payloads
    OBJC_TAG_NSAtom            = 0, 
    OBJC_TAG_1                 = 1, 
    OBJC_TAG_NSString          = 2, 
    OBJC_TAG_NSNumber          = 3, 
    OBJC_TAG_NSIndexPath       = 4, 
    OBJC_TAG_NSManagedObjectID = 5, 
    OBJC_TAG_NSDate            = 6,
    // 保留位
    OBJC_TAG_RESERVED_7        = 7,
    // 52-bit payloads
    OBJC_TAG_Photos_1          = 8,
    OBJC_TAG_Photos_2          = 9,
    OBJC_TAG_Photos_3          = 10,
    OBJC_TAG_Photos_4          = 11,
    OBJC_TAG_XPC_1             = 12,
    OBJC_TAG_XPC_2             = 13,
    OBJC_TAG_XPC_3             = 14,
    OBJC_TAG_XPC_4             = 15,
    OBJC_TAG_NSColor           = 16,
    OBJC_TAG_UIColor           = 17,
    OBJC_TAG_CGColor           = 18,
    OBJC_TAG_NSIndexSet        = 19,
    // 前60位负载内容
    OBJC_TAG_First60BitPayload = 0, 
    // 后60位负载内容
    OBJC_TAG_Last60BitPayload  = 6, 
    // 前52位负载内容
    OBJC_TAG_First52BitPayload = 8, 
    // 后52位负载内容
    OBJC_TAG_Last52BitPayload  = 263, 
    // 保留位
    OBJC_TAG_RESERVED_264      = 264
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，当类标识为 0-6 时，负载数据容量为60 bits；当类标识为 7 时(对应二进制为 0b111)，负载数据容量为 52bits。这里要注意的是NSNumber还会额外占用4bit用来存储数据类型。如果 tag index 是 0b111(7)， <code>Tagged Pointer</code> 对象将使用扩展来标记类型。类标识的扩展类型为上面 <code>OBJC_TAG_Photos_1</code> ～<code>OBJC_TAG_NSIndexSet</code>。</p>
<ul>
<li>Payload：对NSNumber而言，最多占56bit，最少占48bit（取决于Tag Index是否为extended tag index），存储具体的数值。</li>
<li>Type_Index: 占4bit，代表NSNumber具体的数据类型，具体的对应关系：</li>
</ul>

































<table><thead><tr><th>Type_Index</th><th>对应数据类型</th></tr></thead><tbody><tr><td>0</td><td>char</td></tr><tr><td>1</td><td>usigned char, short</td></tr><tr><td>2</td><td>unsigned short,int</td></tr><tr><td>3</td><td>unsigned int,NSInteger,NSUInteger,long,unsigned long,long long,unsigned long long</td></tr><tr><td>4</td><td>float</td></tr><tr><td>5</td><td>double</td></tr></tbody></table>
<p>这与CoreFoundation库中CFNumber.h中的一处枚举也是可以对应上的，唯一的区别是Type_Index从0开始而CFNumberType从1开始：</p>
<pre><code class="copyable">typedef CF_ENUM(CFIndex, CFNumberType) &#123;
  /* Fixed-width types */
  kCFNumberSInt8Type = 1,
  kCFNumberSInt16Type = 2,
  kCFNumberSInt32Type = 3,
  kCFNumberSInt64Type = 4,
  kCFNumberFloat32Type = 5,
  kCFNumberFloat64Type = 6,        /* 64-bit IEEE 754 */
  /* Basic C types */
  kCFNumberCharType = 7,
  kCFNumberShortType = 8,
  kCFNumberIntType = 9,
  kCFNumberLongType = 10,
  kCFNumberLongLongType = 11,
  kCFNumberFloatType = 12,
  kCFNumberDoubleType = 13,
  /* Other */
  kCFNumberCFIndexType = 14,
  kCFNumberNSIntegerType API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0)) = 15,
  kCFNumberCGFloatType API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0)) = 16,
  kCFNumberMaxType = 16
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>苹果在iOS14系统之后对于修改<code>Tagged Pointer</code>内存结构的解释是：</p>
<ol>
<li>ARM有个特性是dyld会忽略指针的前8bit(这是由于ARM的<code>Top Byte Ignore</code>特性)，因此Tag_Index作为更重要的信息不适合再放到高8bit。</li>
<li>这样布局数之后，图中的payload就跟普通指针的payload是一模一样了，也就是<code>Tagged Pointer</code>的payload(有效负载位)有包含一个正常的指针的能力；这使得<code>Tagged Pointer</code>具备了引用二进制文件中的常量数据的能力，例如字符串或其他数据结构，可以减少dirty memory的使用。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2e3094b138144c0b72a40e13dc4a056~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">混淆与反混淆</h3>
<p>通过上面内存结构的分析，<code>Tagged Pointer</code>指针上存储的数据我们完全可以自己计算出来的，这个时候数据暴露出来是有比较大风险的，苹果为了防止非法的伪造<code>Tagged Pointer</code>等数据安全问题，自iOS12之后设计了数据混淆机制，这也解释了为什么文章一开头那个NSNumber对象地址那么大。</p>
<p>查阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKanthine%2FSourceCode%2Fblob%2Fmaster%2Fobjc4-818.2%2Fruntime%2Fobjc-runtime-new.mm" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Kanthine/SourceCode/blob/master/objc4-818.2/runtime/objc-runtime-new.mm" ref="nofollow noopener noreferrer">objc runtime源码</a>，混淆策略如下：</p>
<pre><code class="copyable">/** 随机初始化 TaggedPointer 混淆器变量 objc_debug_taggedpointer_obfuscator
 * @discussion 混淆器变量 objc_debug_taggedpointer_obfuscator 用于数据保护；在首次使用时充满随机性；
 *       在设置或检索 TaggedPointer 上的净负荷值时，混淆器与标记指针进行异或，因此该指针被加密；
 *       此时，别人无法通过指针获取 TaggedPointer 上存储的值，有效的进行了数据保护；
 * @note 如果程序的环境变量 OBJC_DISABLE_TAG_OBFUSCATION 设置为 YES ，则禁止使用 TaggedPointer 混淆器
 */
static void initializeTaggedPointerObfuscator(void) &#123;
    ///编译处理 if (!DisableTaggedPointerObfuscation && dyld_program_sdk_at_least(dyld_fall_2018_os_versions)) &#123;
    if (!DisableTaggedPointerObfuscation && (dyld_get_program_sdk_version() >= dyld_fall_2018_os_versions)) &#123;
        /// 将随机数据放入变量中，然后移走所有非净负荷位
        arc4random_buf(&objc_debug_taggedpointer_obfuscator, sizeof(objc_debug_taggedpointer_obfuscator));
        objc_debug_taggedpointer_obfuscator &= ~_OBJC_TAG_MASK;

#if OBJC_SPLIT_TAGGED_POINTERS
        // The obfuscator doesn't apply to any of the extended tag mask or the no-obfuscation bit.
        objc_debug_taggedpointer_obfuscator &= ~(_OBJC_TAG_EXT_MASK | _OBJC_TAG_NO_OBFUSCATION_MASK);

        // 打断class tag index的固定顺序.
        int max = 7;
        for (int i = max - 1; i >= 0; i--) &#123;
            int target = arc4random_uniform(i + 1);
            swap(objc_debug_tag60_permutations[i],
                 objc_debug_tag60_permutations[target]);
        &#125;
#endif
    &#125; else &#123;
        /// 对于链接到旧sdk的应用程序，如果它们依赖于tagged pointer表示，将混淆器设置为0，
        objc_debug_taggedpointer_obfuscator = 0;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>混淆原理：使用一个随机数<code>objc_debug_taggedpointer_obfuscator</code>对真正的内存地址异或操作。根据异或运算的特性，a^b^b=a，因此只需要将混淆后的地址再与<code>objc_debug_taggedpointer_obfuscator</code>异或一次就能够完成反混淆。</p>
<p>阅读源码后可知<code>objc_debug_taggedpointer_obfuscator</code>是一个全局变量，因此只需要在当前文件<code>extern</code>声明一下就可以轻松的实现一个反混淆方法：</p>
<pre><code class="copyable">extern uintptr_t objc_debug_taggedpointer_obfuscator;
uintptr_t _objc_decodeTaggedPointer_(id ptr)&#123; // 这是苹果源码中的解码函数
  return (uintptr_t)ptr ^ objc_debug_taggedpointer_obfuscator;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">验证</h3>
<p>测试环境：iPhone XS Max，iOS14.6。</p>
<p>测试代码：</p>
<pre><code class="copyable">extern int64_t objc_debug_taggedpointer_obfuscator;
intptr_t _objc_decodeTaggedPointer(id ptr)&#123; // 这是苹果源码中的解码函数
 return (uintptr_t)ptr ^ objc_debug_taggedpointer_obfuscator;
&#125;

- (void)printTaggedNumber:(NSNumber *)number description:(NSString *)desc &#123;
  intptr_t maybeTagged = (intptr_t)number;
  if (maybeTagged >= 0LL) &#123;
    NSLog(@"-- %@ - not tagged", desc);
    return;
  &#125;
   
  intptr_t decoded = _objc_decodeTaggedPointer(number);
  NSLog(@"-- %@ - 0x%016lx", desc, decoded);
&#125;

- (void)viewDidLoad &#123;
  [super viewDidLoad];
  // Do any additional setup after loading the view.
#define PRINT_NUMBER(x) \
[self printTaggedNumber:x description:@#x];

  PRINT_NUMBER([NSNumber numberWithChar:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedChar:1]);
  PRINT_NUMBER([NSNumber numberWithShort:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedShort:1]);
  PRINT_NUMBER([NSNumber numberWithInt:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedInt:1]);
  PRINT_NUMBER([NSNumber numberWithInteger:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedInteger:1]);
  PRINT_NUMBER([NSNumber numberWithLong:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedLong:1]);
  PRINT_NUMBER([NSNumber numberWithLongLong:1]);
  PRINT_NUMBER([NSNumber numberWithUnsignedLongLong:1]);
  PRINT_NUMBER([NSNumber numberWithFloat:1]);
  PRINT_NUMBER([NSNumber numberWithDouble:1]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试结果：</p>
<pre><code class="copyable">2021-06-15 22:19:13.688015+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithChar:1] - 0x8000000000000084
2021-06-15 22:19:13.688039+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedChar:1] - 0x800000000000008c
2021-06-15 22:19:13.688057+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithShort:1] - 0x800000000000008c
2021-06-15 22:19:13.688084+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedShort:1] - 0x8000000000000094
2021-06-15 22:19:13.688105+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithInt:1] - 0x8000000000000094
2021-06-15 22:19:13.688119+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedInt:1] - 0x800000000000009c
2021-06-15 22:19:13.688133+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithInteger:1] - 0x800000000000009c
2021-06-15 22:19:13.688352+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedInteger:1] - 0x800000000000009c
2021-06-15 22:19:13.688497+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithLong:1] - 0x800000000000009c
2021-06-15 22:19:13.688673+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedLong:1] - 0x800000000000009c
2021-06-15 22:19:13.688838+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithLongLong:1] - 0x800000000000009c
2021-06-15 22:19:13.688966+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithUnsignedLongLong:1] - 0x800000000000009c
2021-06-15 22:19:13.689178+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithFloat:1] - 0x80000000000000a4
2021-06-15 22:19:13.689333+0800 NSNumberTest[2804:508458] -- [NSNumber numberWithDouble:1] - 0x80000000000000ac
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将不同类型的<code>Tagged Pointer</code>地址转成二进制整理如下：</p>
<pre><code class="copyable">//char
1000000000000000000000000000000000000000000000000000000010000100
//usigned char, short
1000000000000000000000000000000000000000000000000000000010001100
//unsigned short,int
1000000000000000000000000000000000000000000000000000000010010100
//unsigned int,NSInteger,NSUInteger,long,unsigned long,long long,unsigned long long
1000000000000000000000000000000000000000000000000000000010011100
//float
1000000000000000000000000000000000000000000000000000000010100100
//double
1000000000000000000000000000000000000000000000000000000010101100
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以char类型为例，执行返混淆之后打印出原始的<code>Tagged Pointer</code>地址为0x8000000000000083，参照iOS14系统以上章节的内存结构分析对照如下：</p>
<ul>
<li>高4位0x8转成二进制也就是1000，也就是最高位是1，代表<code>Tagged Pointer</code>标志位，意味着该指针就是<code>Tagged Pointer</code>。</li>
<li>低3位0x4换成十进制也是4，代表Tag_Index，注意这里没有和NSNumber对应上的主要原因是iOS14系统以上苹果对于Tag_Index的映射关系也做了混淆，并不是静态的，每次启动都可能会发生互换。</li>
<li>低4-7位换成十进制是0，代表Type_Index，刚好和char类型的索引是能对上的。</li>
<li>从低8位开始剩下的数字就代表payload，十六进制表示是0x1，也就是1，刚好和代码中的数字完全对上。</li>
</ul>
<h3 data-id="heading-10">Tagged Pointer可表示的数字范围</h3>
<p>从上面章节的分析中可以得出结论，在不考虑extended tag的前提下，payload最多占56bit，最高位预留用来表示数字的正负。那么55bit理论上能表示的最大数字范围就是-2^55~2^55-1这么大。转成十进制就是-36028797018963968～36028797018963967。然后我们以表示范围最大的long long类型为例再用上面的测试环境再次验证一下：</p>
<p>首先验证上限部分：</p>
<pre><code class="copyable">PRINT_NUMBER([NSNumber numberWithLongLong:36028797018963967]);
PRINT_NUMBER([NSNumber numberWithLongLong:36028797018963968]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">2021-06-17 13:06:36.663636+0800 NSNumberTest[8324:1617444] -- [NSNumber numberWithLongLong:36028797018963967] - 0xbfffffffffffff98
2021-06-17 13:06:36.663664+0800 NSNumberTest[8324:1617444] -- [NSNumber numberWithLongLong:36028797018963968] - not tagged
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见结果符合我们的猜想。</p>
<p>再来验证下限部分：</p>
<pre><code class="copyable">PRINT_NUMBER([NSNumber numberWithLongLong:-36028797018963968]);
PRINT_NUMBER([NSNumber numberWithLongLong:-36028797018963969]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">2021-06-17 13:09:41.657371+0800 NSNumberTest[8330:1618554] -- [NSNumber numberWithLongLong:-36028797018963968] - not tagged
2021-06-17 13:09:41.657410+0800 NSNumberTest[8330:1618554] -- [NSNumber numberWithLongLong:-36028797018963969] - not tagged
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见-2^55居然已经不能用<code>Tagged Pointer</code>来表示！然后我们再+1缩小范围：</p>
<pre><code class="copyable">PRINT_NUMBER([NSNumber numberWithLongLong:-36028797018963967]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">2021-06-17 13:12:06.286077+0800 NSNumberTest[8333:1619493] -- [NSNumber numberWithLongLong:-36028797018963967] - 0xc000000000000099
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见不知为何NSNumber将<code>Tagged Pointer</code>理论上能表示的数字最大范围的下限修正为-2^55+1。</p>
<p>结论：<code>Tagged Pointer</code>可表示的数字范围是-2^55+1 ~ 2^55-1，对于超出这个范围的数字，NSNumber会自动转换为普通的内存分配在堆上的OC对象。</p>
<h2 data-id="heading-11">如何判断指针是否为Tagged Pointer</h2>
<p>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKanthine%2FSourceCode%2Fblob%2F51fd88340a1d76047dcb8bb02e47f14482d00706%2Fobjc4-750%2Fruntime%2Fobjc-internal.h" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Kanthine/SourceCode/blob/51fd88340a1d76047dcb8bb02e47f14482d00706/objc4-750/runtime/objc-internal.h" ref="nofollow noopener noreferrer">objc runtime源码</a>中找到了 <code>_objc_isTaggedPointer()</code>的实现：</p>
<pre><code class="copyable">static inline bool _objc_isTaggedPointer(const void * _Nullable ptr)&#123;
    //将一个指针地址和 _OBJC_TAG_MASK 常量做 & 运算：判断该指针的最高位或者最低位为 1，那么这个指针就是 Tagged Pointer。
    return ((uintptr_t)ptr & _OBJC_TAG_MASK) == _OBJC_TAG_MASK;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_OBJC_TAG_MASK</code> 的定义：</p>
<pre><code class="copyable">#if OBJC_MSB_TAGGED_POINTERS //MSB 高位优先
#   define _OBJC_TAG_MASK (1UL<<63) //Tagged Pointer 指针
#else //LSB 低位优先
#   define _OBJC_TAG_MASK 1UL //Tagged Pointer 指针
#endif
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此 <code>ptr & _OBJC_TAG_MASK</code> 按位与运算之后如果判断标志位为1则该指针是<code>Tagged Pointer</code> 。</p>
<h1 data-id="heading-12">问题修复</h1>
<p>搞清楚原理之后，问题也就比较容易修复了。只需要在调用<code>vm_read</code>方法判断指针地址是否可读之前，首先判断是否为<code>Tagged Pointer</code>，如果是的话则忽略，直接返回true。</p>
<pre><code class="copyable">tatic inline bool protect_objc_isTaggedPointer(const void *ptr) &#123;
  bool result = ((intptr_t)ptr & _OBJC_TAG_MASK) == _OBJC_TAG_MASK;
  return result;
&#125;

static bool check_valid_address(id _Nonnull objc, SEL _Nonnull aSelector) &#123;
  vm_offset_t data;
  mach_msg_type_number_t dataSize;
  
  vm_address_t address = (vm_address_t)objc;
   
  //reference to https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/
  //vm_read for TaggedPointer may return KERN_INVALID_ADDRESS
#if defined(__LP64__)
  if (protect_objc_isTaggedPointer((void *)address)) &#123;
    return true;
  &#125;
#endif

  kern_return_t kt = vm_read(current_task(), address, sizeof(uintptr_t), &data, &dataSize);
   
  if (kt != KERN_SUCCESS) &#123;
    return false;
  &#125;
   
  bool valid = true;
  kt = vm_read(current_task(), (vm_address_t)sel_getName(aSelector), sizeof(uintptr_t), &data, &dataSize);
  if (kt != KERN_SUCCESS) &#123;
    valid = false;
  &#125;
   
  return valid;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终改动上线之后确认问题修复生效。</p>
<h1 data-id="heading-13">启发</h1>
<p>对于OC的对象，除了分配在堆中的普通OC对象之后，要时刻留意有一些特殊的<code>Tagged Pointer</code>，特别是<code>NSString</code>，<code>NSNumber</code>，<code>NSDate</code>等对象，避免掉进坑里。下面附两个另外比较典型的关于</p>
<p><code>Tagged Pointer</code>的坑：</p>
<ol>
<li><a href="https://juejin.cn/post/6844904146114445320" target="_blank" title="https://juejin.cn/post/6844904146114445320">《一次标签指针（Tagged Pointer）导致的事故》</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falanzj.github.io%2F2017%2F12%2F26%2F%25E4%25BB%258E%25E4%25B8%2580%25E9%2581%2593%25E7%25BD%2591%25E6%2598%2593%25E9%259D%25A2%25E8%25AF%2595%25E9%25A2%2598%25E6%25B5%2585%25E8%25B0%2588-Tagged-Pointer%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://alanzj.github.io/2017/12/26/%E4%BB%8E%E4%B8%80%E9%81%93%E7%BD%91%E6%98%93%E9%9D%A2%E8%AF%95%E9%A2%98%E6%B5%85%E8%B0%88-Tagged-Pointer/" ref="nofollow noopener noreferrer">《从一道网易面试题浅谈 Tagged Pointer》</a></li>
</ol>
<h1 data-id="heading-14">参考&致谢</h1>
<p><a href="https://juejin.cn/post/6844904132940136462" target="_blank" title="https://juejin.cn/post/6844904132940136462">《iOS - 老生常谈内存管理（五）：Tagged Pointer》by 师大小海腾</a></p>
<p><a href="https://juejin.cn/post/6949092664469880839" target="_blank" title="https://juejin.cn/post/6949092664469880839">《Tagged Pointer》by 清风低语</a></p>
<p>感谢微信好友@鹅喵大魔王对NSNumer Type_Index内存结构的逆向探索和测试代码的提供。</p></div>  
</div>
            