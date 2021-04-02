
---
title: '一种Swift Hook新思路——从Swift的虚函数表说起'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe0635188964e0eb1e7418b2a09a5aa~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 14 Mar 2021 22:29:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe0635188964e0eb1e7418b2a09a5aa~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：业界对Swift的Hook大多都需要依靠OC的消息转发特性来实现，本文从修改Swift的虚函数表的角度，介绍了一种新的Hook思路。并以此为主线，重点介绍Swift的详细结构以及应用。</p>
</blockquote>
<h2 data-id="heading-0">引言</h2>
<p>由于历史包袱的原因，目前主流的大型APP基本都是以Objective-C为主要开发语言。但是敏锐的同学应该能发现，从Swift的ABI稳定以后，各个大厂开始陆续加大对Swift的投入。虽然在短期内Swift还难以取代Objective-C，但是其与Objective-C并驾齐驱的趋势是越来越明显，从招聘的角度就即可管中窥豹。在过去一年的招聘过程中我们总结发现，有相当数量的候选人只掌握Swift开发，对Objective-C开发并不熟悉，而且这部分候选人大多数比较年轻。另外，以RealityKit等新框架为例，其只支持Swift不支持Objective-C。上述种种现象意味着随着时间的推移，如果项目不能很好的支持Swift开发，那么招聘成本以及应用创新等一系列问题将会凸显出来。因此，58同城在2020年Q4的时候在集团内发起了跨部门协同项目，从各个层面打造Objective-C与Swift的混编生态环境——项目代号 <strong>”混天“</strong>。一旦混编生态构建完善，那么很多问题将迎刃而解。</p>
<h2 data-id="heading-1">原理简述</h2>
<blockquote>
<p>文章篇幅较长，且内容较为枯燥，为了方便读者阅读，先抛出结论及原理。如果您对相关代码感兴趣，可以在Github上搜索SwiftVTHook下载Demo</p>
</blockquote>
<p>本文的技术方案仅针对通过虚函数表调用的函数进行Hook，不涉及直接地址调用和objc_msgSend的调用的情况。另外需要注意的是，<code>Swift Compiler</code>设置为<code>Optimize for speed</code>（Release默认）则TypeContext的VTable的函数地址会清空。设置为<code>Optimize for size</code>则Swfit可能会转变为直接地址调用。以上两种配置都会造成方案失效。<strong>因此本文重点在介绍技术细节而非方案推广。</strong></p>
<p><img alt="方案简图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe0635188964e0eb1e7418b2a09a5aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如果Swift通过虚函数表跳表的方式来实现方法调用，那么可以借助修改虚函数表来实现方法替换。即将特定虚函数表的函数地址修改为要替换的函数地址。但是由于虚函数表不包含地址与符号的映射，我们不能像Objective-C那样根据函数的名字获取到对应的函数地址，因此修改Swift的虚函数是依靠函数索引来实现的。简单理解就是将虚函数表理解为数组，假设有一个FuncTable[]，我们修改函数地址只能通过索引值来实现，就像<code>FuncTable[index] = replaceIMP</code> 。但是这也涉及到一个问题，在版本迭代过程中我们不能保证代码是一层不变的，因此这个版本的第index个函数可能是函数A，下个版本可能第index个函数就变成了函数B。显然这对函数的替换会产生重大影响。</p>
<p>为此，我们通过Swift的OverrideTable来解决索引变更的问题。在Swift的OverrideTable中，每个节点都记录了当前这个函数重写了哪个类的哪个函数，以及重写后函数的函数指针。因此只要我们能获取到OverrideTable也就意味着能获取被重写的函数指针<code>IMP0</code>以及重写后的函数指针<code>IMP1</code>。只要在FuncTable[]中找到IMP0并替换成IMP1即可完成方法替换。</p>
<blockquote>
<p>接下来将详细介绍Swift的<strong>函数调用</strong>、<strong>TypeContext</strong>、<strong>Metadata</strong>、<strong>VTable</strong>、<strong>OverrideTable</strong>等细节，以及他们彼此之间有何种关联。为了方便阅读和理解，本文所有代码及运行结果，都是基于arm64架构</p>
</blockquote>
<h2 data-id="heading-2">Swift的函数调用</h2>
<p>首先我们需要了解Swift的函数如何调用的。与Objective-C不同，Swift的函数调用存在三种方式，分别是：基于Objective-C的消息机制、基于虚函数表的访问、以及直接地址调用。</p>
<ul>
<li><strong>Objective-C的消息机制</strong></li>
</ul>
<p>首先我们需要了解在什么情况下Swift的函数调用是借助Objective-C的消息机制。如果方法通过@objc dynamic修饰，那么在编译后将通过objc_msgSend的来调用函数。
假设有如下代码</p>
<pre><code class="copyable">class MyTestClass :NSObject &#123;
    @objc dynamic func helloWorld() &#123;
        print("call helloWorld() in MyTestClass")
    &#125;
&#125;

let myTest = MyTestClass.init()
myTest.helloWorld()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后其对应的汇编为</p>
<pre><code class="copyable">    0x1042b8824 <+120>: bl     0x1042b9578               ; type metadata accessor for SwiftDemo.MyTestClass at <compiler-generated>
    0x1042b8828 <+124>: mov    x20, x0
    0x1042b882c <+128>: bl     0x1042b8998               ; SwiftDemo.MyTestClass.__allocating_init() -> SwiftDemo.MyTestClass at ViewController.swift:22
    0x1042b8830 <+132>: stur   x0, [x29, #-0x30]
    0x1042b8834 <+136>: adrp   x8, 13
    0x1042b8838 <+140>: ldr    x9, [x8, #0x320]
    0x1042b883c <+144>: stur   x0, [x29, #-0x58]
    0x1042b8840 <+148>: mov    x1, x9
    0x1042b8844 <+152>: str    x8, [sp, #0x60]
->  0x1042b8848 <+156>: bl     0x1042bce88               ; symbol stub for: objc_msgSend
    0x1042b884c <+160>: mov    w11, #0x1
    0x1042b8850 <+164>: mov    x0, x11
    0x1042b8854 <+168>: ldur   x1, [x29, #-0x48]
    0x1042b8858 <+172>: bl     0x1042bcd5c               ; symbol stub for:
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的汇编代码中我们很容易看出调用了地址为0x1042bce88的objc_msgSend函数。</p>
<ul>
<li><strong>虚函数表的访问</strong></li>
</ul>
<p>虚函数表的访问也是动态调用的一种形式，只不过是通过访问虚函数表的方式进行调用。
假设还是上述代码，我们将@objc dynamic去掉之后，并且不再继承自NSObject。</p>
<pre><code class="copyable">class MyTestClass &#123;
    func helloWorld() &#123;
        print("call helloWorld() in MyTestClass")
    &#125;
&#125;

let myTest = MyTestClass.init()
myTest.helloWorld()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>汇编代码变成了下面这样👇</p>
<pre><code class="copyable">    0x1026207ec <+120>: bl     0x102621548               ; type metadata accessor for SwiftDemo.MyTestClass at <compiler-generated>
    0x1026207f0 <+124>: mov    x20, x0
    0x1026207f4 <+128>: bl     0x102620984               ; SwiftDemo.MyTestClass.__allocating_init() -> SwiftDemo.MyTestClass at ViewController.swift:22
    0x1026207f8 <+132>: stur   x0, [x29, #-0x30]
    0x1026207fc <+136>: ldr    x8, [x0]
    0x102620800 <+140>: adrp   x9, 8
    0x102620804 <+144>: ldr    x9, [x9, #0x40]
    0x102620808 <+148>: ldr    x10, [x9]
    0x10262080c <+152>: and    x8, x8, x10
    0x102620810 <+156>: ldr    x8, [x8, #0x50]
    0x102620814 <+160>: mov    x20, x0
    0x102620818 <+164>: stur   x0, [x29, #-0x58]
    0x10262081c <+168>: str    x9, [sp, #0x60]
->  0x102620820 <+172>: blr    x8
    0x102620824 <+176>: mov    w11, #0x1
    0x102620828 <+180>: mov    x0, x11
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面汇编代码可以看出，经过编译后最终是通过blr 指令调用了x8寄存器中存储的函数。至于x8寄存器中的数据从哪里来的，留到后面的章节阐述。</p>
<ul>
<li><strong>直接地址调用</strong></li>
</ul>
<p>假设还是上述代码，我们再将<code>Build Setting</code>中<code>Swift Compiler - Code Generaation</code> -> <code>Optimization Level</code>修改为<code>Optimize for Size[-Osize]</code>，汇编代码变成了下面这样👇</p>
<pre><code class="copyable">    0x1048c2114 <+40>:  bl     0x1048c24b8               ; type metadata accessor for SwiftDemo.MyTestClass at <compiler-generated>
    0x1048c2118 <+44>:  add    x1, sp, #0x10             ; =0x10 
    0x1048c211c <+48>:  bl     0x1048c5174               ; symbol stub for: swift_initStackObject
->  0x1048c2120 <+52>:  bl     0x1048c2388               ; SwiftDemo.MyTestClass.helloWorld() -> () at ViewController.swift:23
    0x1048c2124 <+56>:  adr    x0, #0xc70c               ; demangling cache variable for type metadata for Swift._ContiguousArrayStorage<Any>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是大家就会发现bl 指令后跟着的是一个常量地址，并且是<code>SwiftDemo.MyTestClass.helloWorld()</code>的函数地址。</p>
<h2 data-id="heading-3">思考</h2>
<p>既然基于虚函数表的派发形式也是一种动态调用，那么是不是以为着只要我们修改了虚函数表中的函数地址，就实现了函数的替换？</p>
<h2 data-id="heading-4">基于TypeContext的方法交换</h2>
<p>在上篇文章<a href="https://mp.weixin.qq.com/s?__biz=MzI1NDc5MzIxMw==&mid=2247491058&idx=1&sn=3b1d7e68ff51df58046d1e0d0aee1039&chksm=ea3e9960dd491076573553ff0c74d1c41db04c1fd9be9a9d3d080cbe7e27955ac0ec151f5285&scene=27#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">《从Mach-O角度谈谈Swift和OC的存储差异》</a>我们可以了解到在Mach-O文件中，可以通过<code>__swift5_types </code>查找到每个Class的ClassContextDescriptor，并且可以通过ClassContextDescriptor找到当前类对应的虚函数表，并动态调用表中的函数。</p>
<blockquote>
<p>（在Swift中，Class/Struct/Enum统称为Type，为了方便起见，我们在文中提到的TypeContext和ClassContextDescriptor都指的是ClassContextDescriptor）。</p>
</blockquote>
<p>首先我们来回顾下Swift的类的结构描述，结构体ClassContextDescriptor是Swift类在Section64(__TEXT,__const)中的存储结构。</p>
<pre><code class="copyable">struct ClassContextDescriptor&#123;
    uint32_t Flag;
    uint32_t Parent;
    int32_t  Name;
    int32_t  AccessFunction;
    int32_t  FieldDescriptor;
    int32_t  SuperclassType;
    uint32_t MetadataNegativeSizeInWords;
    uint32_t MetadataPositiveSizeInWords;
    uint32_t NumImmediateMembers;
    uint32_t NumFields;
    uint32_t FieldOffsetVectorOffset;
    <泛型签名> //字节数与泛型的参数和约束数量有关
    <MaybeAddResilientSuperclass>//有则添加4字节
    <MaybeAddMetadataInitialization>//有则添加4*3字节
    VTableList[]//先用4字节存储offset/pointerSize，再用4字节描述数量，随后N个4+4字节描述函数类型及函数地址。
    OverrideTableList[]//先用4字节描述数量，随后N个4+4+4字节描述当前被重写的类、被重写的函数描述、当前重写函数地址。
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述结构可以看出，ClassContextDescriptor的长度是不固定的，不同的类ClassContextDescriptor的长度可能不同。那么如何才能知道当前这个类是不是泛型？以及是否有ResilientSuperclass、MetadataInitialization特征？其实在前一篇文章《从Mach-O角度谈谈Swift和OC的存储差异》中已经做了说明，我们可以通过Flag的标记位来获取相关信息。
例如，如果Flag的generic标记位为1，则说明是泛型。</p>
<pre><code class="copyable">|  TypeFlag(16bit)  |  version(8bit) | generic(1bit) | unique(1bit) | unknow (1bi) | Kind(5bit) |
//判断泛型
(Flag & 0x80) == 0x80
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么泛型签名到底能占多少字节呢？Swift的GenMeta.cpp文件中对泛型的存储做了解释，整理总结如下：</p>
<pre><code class="copyable">假设有泛型有paramsCount个参数，有requeireCount个约束

/**
     16B  =  4B + 4B + 2B + 2B + 2B + 2B
     addMetadataInstantiationCache -> 4B
     addMetadataInstantiationPattern -> 4B
     GenericParamCount -> 2B
     GenericRequirementCount -> 2B
     GenericKeyArgumentCount -> 2B
     GenericExtraArgumentCount -> 2B
 */
 short pandding = (unsigned)-paramsCount & 3;
 泛型签名字节数 = (16 + paramsCount + pandding + 3 * 4 * (requeireCount) + 4);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此只要明确了Flag各个标记位的含义以及泛型的存储长度规律，那么就能计算出虚函数表VTable的位置以及各个函数的字节位置。
了解了泛型的布局以及VTable的位置，是不是就意味着能实现函数指针的修改了呢？答案当然是否定的，因为VTable存储在__TEXT段，__TEXT是只读段，我们没办法直接进行修改。不过最终我们通过remap的方式修改代码段，将VTable中的函数地址进行了修改，然而发现在运行时函数并没有被替换为我们修改的函数。那到底是怎么一回事呢？</p>
<h2 data-id="heading-5">基于Metadata的方法交换</h2>
<p>上述实验的失败当然是我们的不严谨导致的。在项目一开始我们先研究的是类型存储描述TypeContext，主要是类的存储描述ClassContextDescriptor。在找到VTable后我们想当然的认为运行时Swift是通过访问ClassContextDescriptor中的VTable进行函数调用的。但是事实并不是这样。</p>
<h3 data-id="heading-6">VTable函数调用</h3>
<p>接下来我们将回答下 <strong>Swift的函数调用</strong> 章节中提的问题，x8寄存器的函数地址是从哪里来的。还是前文中的Demo，我们在helloWorld()函数调用前打断点</p>
<pre><code class="copyable">let myTest = MyTestClass.init()
    ->  myTest.helloWorld()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点停留在0x100230ab0处👇</p>
<pre><code class="copyable">    0x100230aac <+132>: stur   x0, [x29, #-0x30]
->  0x100230ab0 <+136>: ldr    x8, [x0]
    0x100230ab4 <+140>: ldr    x8, [x8, #0x50]
    0x100230ab8 <+144>: mov    x20, x0
    0x100230abc <+148>: str    x0, [sp, #0x58]
    0x100230ac0 <+152>: blr    x8
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时x0寄存器中存储的是myTest的地址<code>x0 = 0x0000000280d08ef0 </code>，<code>ldr    x8, [x0]</code>则是将0x280d08ef0处存储的数据放入x8（注意，这里是只将*myTest存入x8，而不是将0x280d08ef0存入x8）。单步执行后，通过<code>re read</code>查看各个寄存器的数据后会发现x8存储的是type metadata的地址，而不是TypeContext的地址。</p>
<pre><code class="copyable">        x0 = 0x0000000280d08ef0
        x1 = 0x0000000280d00234
        x2 = 0x0000000000000000
        x3 = 0x00000000000008fd
        x4 = 0x0000000000000010
        x5 = 0x000000016fbd188f
        x6 = 0x00000002801645d0
        x7 = 0x0000000000000000
        x8 = 0x000000010023e708  type metadata for SwiftDemo.MyTestClass
        x9 = 0x0000000000000003
       x10 = 0x0000000280d08ef0
       x11 = 0x0000000079c00000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过上步单步执行后，当前程序要做的是<code>ldr    x8, [x8, #0x50]</code>，即将type metadata + 0x50处的数据存储到x8。这一步就是跳表，也就是说经过这一步后，x8寄存器中存储的就是helloWorld()的地址。</p>
<pre><code class="copyable">    0x100230aac <+132>: stur   x0, [x29, #-0x30]
    0x100230ab0 <+136>: ldr    x8, [x0]
->  0x100230ab4 <+140>: ldr    x8, [x8, #0x50]
    0x100230ab8 <+144>: mov    x20, x0
    0x100230abc <+148>: str    x0, [sp, #0x58]
    0x100230ac0 <+152>: blr    x8
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那是否真的是这样呢？<code>ldr    x8, [x8, #0x50]</code>执行后，我们再次查看x8，看看寄存器中是否为函数地址👇</p>
<pre><code class="copyable">        x0 = 0x0000000280d08ef0
        x1 = 0x0000000280d00234
        x2 = 0x0000000000000000
        x3 = 0x00000000000008fd
        x4 = 0x0000000000000010
        x5 = 0x000000016fbd188f
        x6 = 0x00000002801645d0
        x7 = 0x0000000000000000
        x8 = 0x0000000100231090  SwiftDemo`SwiftDemo.MyTestClass.helloWorld() -> () at ViewController.swift:23
        x9 = 0x0000000000000003
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果表明x8存储的确实是helloWorld()的函数地址。上述实验表明经过跳转0x50位置后，程序找到了helloWorld()函数地址。类的Metadata位于__DATA段，是可读写的。其结构如下：</p>
<pre><code class="copyable">struct SwiftClass &#123;
    NSInteger kind;
    id superclass;
    NSInteger reserveword1;
    NSInteger reserveword2;
    NSUInteger rodataPointer;
    UInt32 classFlags;
    UInt32 instanceAddressPoint;
    UInt32 instanceSize;
    UInt16 instanceAlignmentMask;
    UInt16 runtimeReservedField;
    UInt32 classObjectSize;
    UInt32 classObjectAddressPoint;
    NSInteger nominalTypeDescriptor;
    NSInteger ivarDestroyer;
    //func[0]
    //func[1]
    //func[2]
    //func[3]
    //func[4]
    //func[5]
    //func[6]
....
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码在经过0x50字节的偏移后正好位于func[0]的位置。因此要想动态修改函数需要修改Metadata中的数据。经过试验后发现修改后函数确实是在运行后发生了改变。但是这并没有结束，因为虚函数表与消息发送有所不同，虚函数表中并没有任何函数名和函数地址的映射，我们只能通过偏移来修改函数地址。比如，我想修改第1个函数，那么我要找到Meatadata，并修改0x50处的8字节数据。同理，想要修改第2个函数，那么我要修改0x58处的8字节数据。这就带来一个问题，一旦函数数量或者顺序发生了变更，那么都需要重新进行修正偏移索引。举例说明下，假设当前1.0版本的代码为</p>
<pre><code class="copyable">class MyTestClass &#123;
    func helloWorld() &#123;
        print("call helloWorld() in MyTestClass")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们对0x50处的函数指针进行了修改。当2.0版本变更为如下代码时，此时我们的偏移应该修改为0x58，否则我们的函数替换就发生了错误。</p>
<pre><code class="copyable">class MyTestClass &#123;
    func sayhi() &#123;
        print("call sayhi() in MyTestClass")
    &#125;

    func helloWorld() &#123;
        print("call helloWorld() in MyTestClass")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了解决虚函数变更的问题，我们需要了解下TypeContext与Metadata的关系。</p>
<h3 data-id="heading-7">TypeContext与Metadata的关系</h3>
<p>Metadata结构中的nominalTypeDescriptor指向了TypeContext，也就是说当我们获取到Metadata地址后，偏移0x40字节就能获取到当前这个类对应的TypeContext地址。那么如何通过TypeContext找到Metadata呢？我们还是看刚才的那个Demo，此时我们将断点打到init()函数上，我们想了解下MyTestClass的Metadata到底是哪里来的。</p>
<pre><code class="copyable">    -> let myTest = MyTestClass.init()
myTest.helloWorld()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时展开为汇编我们会发现，程序准备调用一个函数。</p>
<pre><code class="copyable">->  0x1040f0aa0 <+120>: bl     0x1040f16a8               ; type metadata accessor for SwiftDemo.MyTestClass at <compiler-generated>
    0x1040f0aa4 <+124>: mov    x20, x0
    0x1040f0aa8 <+128>: bl     0x1040f0c18               ; SwiftDemo.MyTestClass.__allocating_init() -> SwiftDemo.MyTestClass at ViewController.swift:22
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行<code>bl     0x1040f16a8</code>指令之前，x0寄存器为0。</p>
<pre><code class="copyable">x0 = 0x0000000000000000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时通过si 单步调试就会发现跳转到了函数0x1040f16a8处，其函数指令较少，如下所示👇</p>
<pre><code class="copyable">SwiftDemo`type metadata accessor for MyTestClass:
->  0x1040f16a8 <+0>:  stp    x29, x30, [sp, #-0x10]!
    0x1040f16ac <+4>:  adrp   x8, 13
    0x1040f16b0 <+8>:  add    x8, x8, #0x6f8            ; =0x6f8 
    0x1040f16b4 <+12>: add    x8, x8, #0x10             ; =0x10 
    0x1040f16b8 <+16>: mov    x0, x8
    0x1040f16bc <+20>: bl     0x1040f4e68               ; symbol stub for: objc_opt_self
    0x1040f16c0 <+24>: mov    x8, #0x0
    0x1040f16c4 <+28>: mov    x1, x8
    0x1040f16c8 <+32>: ldp    x29, x30, [sp], #0x10
    0x1040f16cc <+36>: ret  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行0x1040f16a8 函数执行完后，x0寄存器就存储了MyTestClass的Metadata地址。</p>
<pre><code class="copyable">x0 = 0x00000001047e6708  type metadata for SwiftDemo.MyTestClass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这个被标记为 type metadata accessor for SwiftDemo.MyTestClass at 的函数到底是什么？在上文介绍的struct ClassContextDescriptor貌似有个成员是AccessFunction，那这个ClassContextDescriptor中的AccessFunction是不是Metadata的访问函数呢？这个其实很容易验证。我们再次运行Demo，此时metadata accessor 为 0x1047d96a8，继续执行后Metadata地址为0x1047e6708。</p>
<pre><code class="copyable">        x0 = 0x00000001047e6708  type metadata for SwiftDemo.MyTestClass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看0x1047e6708，继续偏移0x40字节后可以得到Metadata结构中的nominalTypeDescriptor地址0x1047e6708 + 0x40 = 0x1047e6748。
查看0x1047e6748存储的数据为0x1047df4a0。</p>
<pre><code class="copyable">(lldb) x 0x1047e6748
0x1047e6748: a0 f4 7d 04 01 00 00 00 00 00 00 00 00 00 00 00  ..&#125;.............
0x1047e6758: 90 90 7d 04 01 00 00 00 18 8c 7d 04 01 00 00 00  ..&#125;.......&#125;.....
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ClassContextDescriptor中的AccessFunction在第12字节处，因此对0x1047df4a0 + 12 可知AccessFunction的位置为0x1047df4ac。继续查看0x1047df4ac存储的数据为</p>
<pre><code class="copyable">(lldb) x 0x1047df4ac
0x1047df4ac: fc a1 ff ff 70 04 00 00 00 00 00 00 02 00 00 00  ....p...........
0x1047df4bc: 0c 00 00 00 02 00 00 00 00 00 00 00 0a 00 00 00  ................
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于在ClassContextDescriptor中，AccessFunction为相对地址，因此我们做一次地址计算0x1047df4ac + 0xffffa1fc - 0x10000000 = 0x1047d96a8，与metadata accessor 0x1047d96a8相同，这就说明TypeContext是通过AccessFunction来获取对应的Metadata的地址的。当然，实际上也会有例外，有时编译器会直接使用缓存的cache Metadata的地址，而不再通过AccessFunction来获取类的Metadata。</p>
<h2 data-id="heading-8">基于TypeContext和Metadata的方法交换</h2>
<p>在了解了TypeContext和Metadata的关系后，我们就能做一些设想了。在Metadata中虽然存储了函数的地址，但是我们并不知道函数的类型。这里的函数类型指的是函数是普通函数、初始化函数、getter、setter等。在TypeContext的VTable中，method存储一共是8字节，第一个4字节存储的函数的Flag，第二个4字节存储的函数的相对地址。</p>
<pre><code class="copyable">struct SwiftMethod &#123;
    uint32_t Flag;
    uint32_t Offset;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过Flag我们很容易知道是否是动态，是否是实例方法，以及函数类型Kind。</p>
<pre><code class="copyable"> |  ExtraDiscriminator(16bit)  |... | Dynamic(1bit) | instanceMethod(1bit) | Kind(4bit) |
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Kind枚举如下👇</p>
<pre><code class="copyable">typedef NS_ENUM(NSInteger, SwiftMethodKind) &#123;
    SwiftMethodKindMethod             = 0,     // method
    SwiftMethodKindInit               = 1,     //init
    SwiftMethodKindGetter             = 2,     // get
    SwiftMethodKindSetter             = 3,     // set
    SwiftMethodKindModify             = 4,     // modify
    SwiftMethodKindRead               = 5,     // read
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从Swift的源码中可以很明显的看到，类重写的函数是单独存储的，也就是有单独的OverrideTable。并且OverrideTable是存储在VTable之后。与VTable中的method结构不同，OverrideTable中的函数需要3个4字节描述：</p>
<pre><code class="copyable">struct SwiftOverrideMethod &#123;
    uint32_t OverrideClass;//记录是重写哪个类的函数，指向TypeContext
    uint32_t OverrideMethod;//记录重写哪个函数，指向SwiftMethod
    uint32_t Method;//函数相对地址
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说SwiftOverrideMethod中能够包含两个函数的绑定关系，这种关系与函数的编译顺序和数量无关。如果Method记录用于Hook的函数地址，OverrideMethod作为被Hook的函数，那是不是就意味着无论如何改变虚函数表的顺序及数量，只要Swift还是通过跳表的方式进行函数调用，那么我们就无需关注函数变化了。为了验证可行性，我们写Demo测试一下：</p>
<pre><code class="copyable">class MyTestClass &#123;
    func helloWorld() &#123;
        print("call helloWorld() in MyTestClass")
    &#125;
&#125;//作为被Hook类及函数

<--------------------------------------------------->

class HookTestClass: MyTestClass  &#123;
    override func helloWorld() &#123;
        print("\n********** call helloWorld() in HookTestClass **********")
        super.helloWorld()
        print("********** call helloWorld() in HookTestClass end **********\n")
    &#125;
&#125;//通过继承和重写的方式进行Hook

<--------------------------------------------------->
  
let myTest = MyTestClass.init()
 myTest.helloWorld()

 //do hook
 print("\n------ replace MyTestClass.helloWorld() with  HookTestClass.helloWorld() -------\n")

 WBOCTest.replace(HookTestClass.self);

 //hook 生效
 myTest.helloWorld()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后，可以看出helloWorld()已经被替换成功👇</p>
<pre><code class="copyable">2021-03-09 17:25:36.321318+0800 SwiftDemo[59714:5168073] _mh_execute_header = 4368482304
call helloWorld() in MyTestClass

------ replace MyTestClass.helloWorld() with HookTestClass.helloWorld() -------


********** call helloWorld() in HookTestClass **********
call helloWorld() in MyTestClass
********** call helloWorld() in HookTestClass end **********
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p>本文通过介绍Swift的虚函数表Hook思路，介绍了Swift Mach-O的存储结构以及运行时的一些调试技巧。Swift的Hook方案一直是从Objective-C转向Swift开发的同学比较感兴趣的事情。我们想通过本文向大家介绍关于Swift更深层的一些内容，至于方案本身也许并不是最重要的，重要的是我们希望是否能够从中Swift的二进制中找到更多的应用场景。比如，Swift的调用并不会存储到classref中，那如何通过静态扫描知道哪些Swift 的类或Struct被调用了？其实解决方案也是隐含在本文中。</p>
<h2 data-id="heading-10">作者简介：</h2>
<p><strong>邓竹立：用户价值增长中心-平台技术部-iOS技术部 资深开发工程师，WBBlades开源工具作者
蒋演：用户价值增长中心-平台技术部-iOS技术部 架构师 58APP-iOS版本需求负责人</strong></p>
<h2 data-id="heading-11">参考文献：</h2>
<p><a href="https://github.com/apple/swift/blob/d68d406dae39ea1677d586714b3991b8f2037dab/lib/IRGen/GenMeta.cpp" target="_blank" rel="nofollow noopener noreferrer">github.com/apple/swift…</a>
<a href="https://www.jianshu.com/p/158574ab8809" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/158574ab8…</a>
<a href="https://www.jianshu.com/p/ef0ff6ee6bc6" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/ef0ff6ee6…</a>
<a href="https://mp.weixin.qq.com/s/egrQxxJSympB-L6BdVDQVA" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/egrQxxJSy…</a>
<a href="https://github.com/alibaba/HandyJSON" target="_blank" rel="nofollow noopener noreferrer">github.com/alibaba/Han…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            