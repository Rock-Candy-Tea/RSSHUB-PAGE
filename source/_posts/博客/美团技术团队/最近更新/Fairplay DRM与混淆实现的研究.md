
---
title: 'Fairplay DRM与混淆实现的研究'
categories: 
 - 博客
 - 美团技术团队
 - 最近更新
headimg: 'https://p0.meituan.net/travelcube/40bf943ad308e7460bbd0a7c3985c5da58252.png'
author: 美团技术团队
comments: false
date: Thu, 25 Nov 2021 00:00:00 GMT
thumbnail: 'https://p0.meituan.net/travelcube/40bf943ad308e7460bbd0a7c3985c5da58252.png'
---

<div>   
<h2 id="什么是drm">什么是DRM？</h2><p>DRM全称Digital Rights Management，即数字版权保护。苹果为了保护App Store分发的音乐/视频/书籍/App免于盗版，开发了Fairplay DRM技术，并申请了很多相关的专利，比较有代表性的如：
- <a href="https://patents.google.com/patent/US8934624B2">US8934624B2: Decoupling rights in a digital content unit from download</a>
- <a href="https://patents.google.com/patent/US8165286B2">US8165286B2: Combination white box/black box cryptographic processes and apparatus</a>
- <a href="https://patents.google.com/patent/ES2373131T3">ES2373131T3: Safe distribution of content using descifrado keys</a></p><p>长久以来，关于App DRM的研究很少，而DRM的关键是授权和加密。破解Fairplay DRM加密的方式俗称“砸壳”，这是进行iOS App安全研究的必要前提。自从2013年苹果引入App DRM机制以后，诞生了如Cluth、Bagbak、Flexdecrypt这样的经典“砸壳工具”，而此类“砸壳工具”通常需要越狱设备的支持，因此具有一定的局限性。</p><p>2020年发布的M1 Mac将Fairplay DRM机制引入了MacOS，由于Mac设备的权限没有iOS严格，因此我们得以在MacOS上探索更多Fairplay DRM的原理，最终目标是使解密流程不受Apple平台的限制。下面，我们先来聊聊Apple中是如何实现的？</p><h2 id="apple上drm的实现-fairplay-drm">Apple上DRM的实现：Fairplay DRM</h2><h3 id="lc-encryption-info中的标记">LC_ENCRYPTION_INFO中的标记</h3><p>加密的MachO含有LC_ENCRYPTION_INFO字段，其中cryptoff标识了加密部分在文件中的起始偏移，cryptsize标识了加密部分的尺寸，cryptid则表明了加密的方法。Fairplay DRM保护下的App，其加密尺寸为4096的倍数，加密方式标识为1。</p><p><img src="https://p0.meituan.net/travelcube/40bf943ad308e7460bbd0a7c3985c5da58252.png" alt="图1" referrerpolicy="no-referrer"></p><p>而负责解密Mach-O的组件主要包括：<strong>内核态的FairplayIOKit和用户态的fairplayd</strong>。</p><h3 id="fairplay的open">Fairplay的Open</h3><p>MacOS的XNU Kernel中有text_crypter_create_hook这个导出符号，IOTextEncryptionFamily驱动则注册了这个Hook，并作为桥梁，将调用转发给了FairplayIOKit内核驱动。</p><p><img src="https://p0.meituan.net/travelcube/2a8546426be32b4b35e533a7d5a51a4b69848.png" alt="图2" referrerpolicy="no-referrer"></p><p>最终负责处理的函数是：</p><pre><code>com_apple_driver_FairPlayIOKit::xhU6d1(
  char const* executable_path,
  long long cpu_type,
  long long cpu_subtype,
  rp6S0jzg** out_handle
)
</code></pre><p>此后，内核中的FairplayIOKit开始初始化，通过host_get_special_port中的unfreed port发送MIG调用到用户态的fairplayd，fairplayd开始处理SC_Info目录下的sinf和supp文件，并将处理的数据返回给内核中的FairplayIOKit。</p><p>注：用户态的fairplayd具体工作流程不在本文讨论范围内。</p><p>其中MIG调用的结构如下：</p><pre><code>struct FPRequest&#123;
    mach_msg_header_t header;
    mach_msg_body_t body;
    mach_msg_ool_descriptor_t ool;
    NDR_record_t ndr;
    uint32_t size;
    uint64_t cpu_type;
    uint64_t cpu_subtype;
&#125;;

struct FPResponse&#123;
    mach_msg_header_t header;
    mach_msg_body_t body;
    mach_msg_ool_descriptor_t ool1; //supf文件映射
    mach_msg_ool_descriptor_t ool2; //unk，正比与加密内容的尺寸
    uint64_t unk1;
    uint8_t unk2[136];
    uint8_t unk3[84];
    uint32_t size1;
    uint32_t size2;
    uint64_t unk5;
&#125;;
</code></pre><p>完成所有调用后，返回的结构rp6S0jzg*实际是一个uint32_t类型的handle，接下来则可以用这个handle来完成解密操作。</p><h3 id="fairplay的decrypt-page">Fairplay的Decrypt Page</h3><p>前面提到的Fairplay Open操作最终返回了一个pager_crypt_info的结构体，其中page_decrypt的Hook由IOTextEncryptionFamily驱动接管，并最终转发给FairplayIOKit。</p><p><img src="https://p1.meituan.net/travelcube/75b5ff12fdbdda830bb8e6c994c7eb2d205715.png" alt="图3" referrerpolicy="no-referrer"></p><p>最后，FairplayIOKit中负责解密的函数定义如下：</p><pre><code>com_apple_driver_FairPlayIOKit::bvqhJ(
  rp6S0jzg *hanlde,
  unsigned long long offset,
  unsigned char const* src,
  unsigned char * dst
)
</code></pre><p>至此，Fairplay的解密逻辑完成调用。值得注意的是，在Fairplay DRM中，page的概念为4096bytes。</p><p>那么，用户态fairplayd处理的sinf和supp文件又是什么样子的呢？</p><h2 id="sinf和supf文件">SINF和SUPF文件</h2><h3 id="结构">结构</h3><p>用户态的fairplayd会读取随IPA携带的两个重要文件：SINF和SUPF，存储在App的SC_Info目录下。</p><p><img src="https://p0.meituan.net/travelcube/3782dd957025f56bfdb5625ebc5f2dbd148036.png" alt="图4" referrerpolicy="no-referrer"></p><p>其中SUPF文件和IPA一起分发，每个用户的IPA和SUPF文件都是一致的，其中SUPF文件中保存了加密Mach-O的密钥，但是密钥本身被另外的机制加密。而SINF文件则作为每个用户的DRM许可，记录了购买用户的标识符和姓名，以及解密SUPF需要的信息，<strong>因此在Sandbox策略下，App无法读取自身的SINF文件，以防止其被作为唯一ID追踪用户</strong>。</p><h3 id="sinf">SINF</h3><p>SINF文件是一个LTV+KV结构的文件，它的字段如下所示：</p><pre><code>sinf.frma: game
sinf.schm: itun
sinf.schi.user: 0xdeadbeef
sinf.schi.key : 0x00000005
sinf.schi.iviv: 0x12345678901234567890123456789012
sinf.schi.righ.veID: 0x000007d3
sinf.schi.righ.plat: 0x00000000
sinf.schi.righ.aver: 0x01010100
sinf.schi.righ.tran: 0xdc64f80c
sinf.schi.righ.sing: 0x00000000
sinf.schi.righ.song: 0x59a73c58
sinf.schi.righ.tool: P550
sinf.schi.righ.medi: 0x00000080
sinf.schi.righ.mode: 0x00002000
sinf.schi.righ.hi32: 0x00000004
sinf.schi.name: User Name
sinf.schi.priv: (432 Bytes Private Key)
sinf.sign: (128 Bytes Private)
</code></pre><h3 id="supf">SUPF</h3><p>SUPF文件主要分为三个部分，我们将其命名为Key Segments、Fairplay Certificate、RSA Signature，其中Key Segments可以含有多个子Segment，用来保存多个架构的解密信息。</p><pre><code>KeyPair Segments:
Segment 0x0: arm64, Keys: 0x36c/4k, sha1sum = e369546960d805dd1188d42e3350430c7e3a0025

Fairplay Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            33:33:af:08:07:08:af:00:01:af:00:00:10
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: C=US, O=Apple Inc., OU=Apple Certification Authority, CN=Apple FairPlay Certification Authority
        Validity
            Not Before: Jul  8 00:48:29 2008 GMT
            Not After : Jul  7 00:48:29 2013 GMT
        Subject: C=US, O=Apple Inc., OU=Apple FairPlay, CN=AP.3333AF080708AF0001AF000010
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (1024 bit)
                Modulus:
                    00:b0:01:16:4b:62:b2:37:8d:60:12:4f:02:15:15:
                    a0:32:1b:e8:ed:44:ed:e9:17:5b:ec:9e:5d:11:24:
                    5a:66:2f:dc:a3:25:aa:52:70:e1:09:22:09:4b:65:
                    0f:67:f5:82:dc:af:78:9b:4c:45:f3:b4:f4:77:aa:
                    fc:a3:b2:84:c3:8b:09:c6:2e:55:f5:14:85:07:ac:
                    ae:0d:ff:ff:ca:41:3b:44:cb:52:b6:28:60:55:23:
                    35:8d:26:71:c6:12:a5:e0:72:58:09:3c:4a:9e:b6:
                    63:df:2a:91:94:27:eb:65:0a:b2:36:45:11:c1:91:
                    43:58:12:d9:e5:18:a1:ad:db
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment, Data Encipherment, Key Agreement
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier: 
                7B:07:34:81:A5:75:D0:F6:11:BB:D2:36:3F:79:93:4B:A1:70:EB:CF
            X509v3 Authority Key Identifier: 
                keyid:FA:0D:D4:11:91:1B:E6:B2:4E:1E:06:49:94:11:DD:63:62:07:59:64

    Signature Algorithm: sha1WithRSAEncryption
         06:11:4e:87:ed:b1:08:70:c2:0d:e4:d2:94:bb:7f:ee:50:18:
         c0:2a:21:34:0e:99:1f:bf:60:a2:58:d0:0c:28:3d:03:5b:ab:
         4e:72:69:ba:41:52:45:b2:29:27:4a:c8:ba:7f:b5:9b:63:78:
         b1:68:41:40:59:3f:05:8a:57:74:c5:63:30:cc:f3:20:41:c0:
         3c:65:d4:0d:22:47:f3:97:76:e6:d6:3c:eb:e7:20:78:10:59:
         fd:96:09:82:c3:41:f0:5f:d0:3e:91:44:6d:77:3f:a5:d9:da:
         f0:f7:53:ad:94:61:28:1c:4c:40:3b:17:2b:dd:e3:00:df:77:
         71:22

RSA Signature: 6aeb00124d62f75f5761f7c26ec866a061f0776be7e84bfad4b6a1941dbddfdb3bd1afdcc5ef305877fa5bee41caa37b1a9d4ce763cf7d2cb89efa60660a49dd5ddff0f46eee7cd916d382f727d912e82b6e0a62e8110c195e298481aa8c8162faac066ef017c6c2c508700d7adb57e0c988af437621e698946da1b09adf89e9
</code></pre><p>下面，我们来聊聊Fairplay DRM的混淆原理和实现。</p><h2 id="混淆原理和一些实现">混淆原理和一些实现</h2><h3 id="llvm-pass">LLVM Pass</h3><p>LLVM是一个优良的编译器框架，其中，我们可以将其大略的分为前端、中端、后端：</p><p><img src="https://p1.meituan.net/travelcube/3a5668fe18250b2f539f1afece7a0a33112414.png" alt="图5" referrerpolicy="no-referrer"></p><p>配图节选自CMU的CS 15-745课程：<a href="https://www.cs.cmu.edu/~15745/">https://www.cs.cmu.edu/~15745</a>。</p><p>前端负责将高级语言转化为LLVM IR；中端处理LLVM IR，完成一系列的分析、优化任务，我们称之为Pass，再次输出LLVM IR；后端则负责将LLVM IR转化为机器码。其中，中端的玩法特别丰富，基本的优化任务：如死代码消除、常量折叠都在这一部分完成；Address Sanitizer、PC Sanitizer等编译器插桩也是在这里进行的；其他的混淆框架如讨论的较多的ollvm以及Hikari，甚至包括苹果的混淆机制，也都是基于此完成。</p><p>这一混淆方式可以基本的分为控制流混淆和数据流混淆，除此之外的一些混淆方式，比如VMP等，不在本文讨论范围内。</p><h3 id="makeopaque">makeOpaque</h3><p>在编译器中，<strong>为了防止一些具体的表达式被优化，我们会将表达式进行等价变化，我们暂时将这样的操作定义为makeOpaque</strong>（如Safari的JavascriptCore，其JIT组件B3就提供这样的机制），C++伪代码如下：</p><pre><code>Expression* makeOpaque(Expression *in);
</code></pre><h3 id="不透明谓词-opaque-predicate">不透明谓词（Opaque Predicate）</h3><p>谓词（Predicate）在计算机中，指的是执行后为True或False的表达式。数论里面的一些结论可以作为我们生成<strong>不透明谓词</strong>的基础，这些不透明谓词的结果恒为True或恒为False。比如下列表达式中，y执行的结果就恒为True：</p><pre><code>uint32_t x = 0;
bool y = ((x * x % 4) == 0 || (x * x % 4) == 1);
</code></pre><p>不透明谓词应用到混淆中的一个例子就是bogus CFG。
如源语句如下：</p><pre><code>foo1();
foo2();
</code></pre><p>经过变换，我们添加了一个虚假的分支（即bogus CFG）
：</p><pre><code>foo1();
if ( false )
  junk_code();
else
  foo2();
</code></pre><p>但是如果没有经过特别处理，编译器、反编译器的死代码消除就会将虚假分支去除掉，因此我们需要makeOpaque的引入，假设我们引入了前面示例中的表达式：</p><pre><code>foo1();
uint32_t x = rand();
bool y = ((x * x % 4) == 0 || (x * x % 4) == 1);
if ( !y )
  junk_code();
else
  foo2();
</code></pre><p>那么如果编译器、反编译器没有相应的识别机制的话，这一部分的死代码就保留了下来，<strong>通过在死代码里面插入大量干扰指令，可以为逆向的人员带来极大的困扰</strong>。经测试在-O2优化下，Clang 11已经可以识别这个规则，但是GCC 5.4无法识别。</p><h3 id="可逆变换">可逆变换</h3><p>这里我们介绍一下目前混淆技术中常用的等价变换方式。</p><h4 id="异或">异或</h4><p>异或规则是最常见的变换，这里不再赘述。</p><pre><code>x ^ c ^ c = x;
</code></pre><h4 id="仿射变换-affine-transformation">仿射变换（Affine transformation）</h4><p>我们先来看一下仿射函数。</p><p><img src="https://p1.meituan.net/travelcube/addbaf2cc1f7f52a83a6e0e07954571f99955.png" alt referrerpolicy="no-referrer"></p><p>下面我们来看一下实际应用。</p><p>由于计算机中的运算属于隐式的模运算，因此会具有一些有意思的性质。如对于一个uint32上的运算，模运算逆元定义如下：</p><pre><code>//对于
uint32_t a, r_a;

//如果满足
(a * r_a) % UINT32_MAX == 1;

//那么 a 和 r_a 互为模反元素
</code></pre><p>对于互为模反元素的a和r_a（可通过扩展欧几里得算法求得），有这样的特性：</p><pre><code>uint32_t x = rand();
uint32_t y1 = a * x + c;
//那么满足
x == ra * y1 +  (- ra * c)
</code></pre><p>最后举个例子来说明：</p><pre><code>//对于互为模反元素的4872655123 * 3980501275，取
uint32_t x = 0xdeadbeef;
uint32_t c = 0xbeefbeef;
//则 -ra * c = 0x57f38dcb，且
((x * 4872655123) + 0xbeefbeef) * 3980501275 + 0x57f38dcb == x
/*
可在lldb中验证如下
(lldb) p/x uint32_t x=0xdeadbeef; (uint32_t)(((x * 4872655123) + 0xbeefbeef) * 3980501275 + 0x57f38dcb)
(uint32_t) $8 = 0xdeadbeef
*/
</code></pre><h3 id="mba表达式-mixed-boolean-arithmetic-expression">MBA表达式（Mixed Boolean-Arithmetic Expression）</h3><p>MBA表达式是把算术运算（+，-，*，/）和位运算（&，|，~）混合在一起用以隐藏原本表达式的混淆方法。它基于不同的数学原理存在多种形式，这里主要介绍多项式MBA，这是目前混淆技术中最常遇到的形式。</p><p><img src="https://p0.meituan.net/travelcube/357afeaa7363fabdbb10c1c01e19c911118871.png" alt referrerpolicy="no-referrer"></p><p>类似的，在Fairplay混淆中用到的MBA表达式为：</p><pre><code>//OperationSet(+, -, *, &, |, ~)
x - c = (x ^ ~c) + ((2 * x) & ~(2 * c + 1)) + 1;
</code></pre><p>而使用MBA进行混淆操作主要依靠以下两个步骤：</p><p><img src="https://p0.meituan.net/travelcube/6465803deb2c3f89f0a494d5ee95ef7853577.png" alt referrerpolicy="no-referrer"></p><h3 id="不透明常量-opaque-constant">不透明常量（Opaque Constant）</h3><p>不透明常量是基于MBA混淆的方法，用于隐藏数据流中的常量。它使用了置换多项式，是一种在有限域上的可逆多项式。</p><p><img src="https://p0.meituan.net/travelcube/5a6ecdeac4ffb7a307598483f16b718b108160.png" alt referrerpolicy="no-referrer"></p><h3 id="控制流平坦化">控制流平坦化</h3><p>这一部分是逆向工程中讨论的最热门的话题，即将正常的控制流转换等价替换为一个状态机，从而干扰静态的控制流分析，业界也有较多的解决方案。同时因为Fairplay DRM中没有明显用到这种类型的混淆，不再多讨论。</p><h3 id="非直接跳转-indirect-branch">非直接跳转（Indirect Branch）</h3><p>将一些基本块的起始地址保存在全局变量中，通过不透明常量的生成，使得反汇编工具和肉眼无法直接获取到基本块跳转的目标，模型如下：</p><pre><code>//记录基本块地址到全局查找表LUT
LUT[i] = PC;

//执行跳转
jmp/call LUT[makeOpaque(i)]
</code></pre><p>具体的实例：</p><p><img src="https://p0.meituan.net/travelcube/6987e85f9c79baa05f6d1eef81a0d3a9212267.png" alt="图6" referrerpolicy="no-referrer"></p><p>这样，逆向人员就无法直接获取跳转的目标函数、基本块了。同理，通过将判断语句的条件映射到跳转表，也可以实现对条件跳转的混淆。</p><p>所以，在逆向被混淆的Fairplay代码时，<strong>IDA Pro大多数时刻，只能识别出来函数的第一个基本块，无法分析出函数的边界</strong>。</p><h3 id="跨函数混淆-调用约定混淆">跨函数混淆 + 调用约定混淆</h3><p>正常情况下，编程语言如C语言的参数传递遵循特定的调用约定，但是部分混淆工具会对一些内部函数的调用约定进行修改，以Fairplay DRM为例：</p><p><img src="https://p1.meituan.net/travelcube/f22cf18955eef562fd347957e1dec71c341493.png" alt="图7" referrerpolicy="no-referrer"></p><p>我们可以看到常规的以寄存器和栈传递参数的方式被替换成了以堆传递参数的方式了，在构造好了结构体的情况下，这个参数传递的特征可以被清晰的看出来。同时，这里面对一些传递的参数进行了异或混淆，在子函数里面再恢复出来，使得我们难以直接得到原始数据，而静态分析的工具比如IDA Pro也不支持跨函数的数据流分析。</p><p>更严重的是，一些影响子函数运行的重要依赖数据，被提升到了父函数内，导致<strong>在没有恢复调用关系前，我们根本无法推测子函数的运行流程。</strong></p><p>那么，Fairplay DRM的破解之道就是要找到它的弱点。</p><h2 id="fairplay混淆的弱点">Fairplay混淆的弱点</h2><p>通过前边的工作，我们已经能Fairplay正常的完成打开和解密工作了，通过一系列的静态分析和追踪调试，我们发现了这一套混淆系统的一些对抗方案。</p><p>这些问题的本质原因是：<strong>混淆系统在IR层面设计，对机器相关的部分操作没有混淆，因此在生成的机器码里面，我们可以推断得到混淆前的一些特征信息</strong>。</p><h3 id="函数边界识别">函数边界识别</h3><p>前面提到，由于Fairplay用到了非直接跳转的混淆技术，IDA Pro无法直接分析函数的边界。通过跟踪，我们发现在arm64e设备下，该内核驱动中，同一个函数的所有基本块在运行到跳转指令时，均使用了同一个PAC Context，或者称之为PAC Modifier。</p><p><img src="https://p0.meituan.net/travelcube/60aacd1c6b71703bb3de9e804bf8968c310067.png" alt="图8" referrerpolicy="no-referrer"></p><p>借由这个特性，我们可以将函数的边界和基本块分组，尽管目前为止这些基本块之间并不是连通的。</p><h3 id="非直接跳转">非直接跳转</h3><p>对于<strong>无条件跳转</strong>，我们通过设置断点跟踪执行流，就可以解决了。</p><p><img src="https://p1.meituan.net/travelcube/03aaa128da1145c61d909a63f75a59be251717.png" alt="图9" referrerpolicy="no-referrer"></p><p>再通过KeyPatch这样的工具，我们可以将一些简单的函数恢复到比较易于理解的地步。</p><p><img src="https://p0.meituan.net/travelcube/f12c3d95a8b80b2042066f32729ee4d9292912.png" alt="图10" referrerpolicy="no-referrer"></p><p>但是这里的难点在于恢复混淆里面的<strong>非直接跳转指令</strong>，如下图所示：</p><p><img src="https://p0.meituan.net/travelcube/b2d4290ae8cddce439172ceeb4f82b97364584.png" alt="图11" referrerpolicy="no-referrer"></p><p>对于这个跳转指令，我们可以生成如下的表达式：</p><pre><code>//cmp x0, #0
w10 = qword[x12 + (EQ * 0xB + w19) << 3]
//0xB代表两个基本块的在LUT中的下标差
</code></pre><p>通过CSET指令的形式，我们已经可以推断跳转指令应该是J.NE或者J.EQ了，通过我们的调试器插件，我们可以得到其中一个分支的跳转地址和原本的跳转指令，再通过表达式的信息，我们可以很快推断出另外一个分支的地址。</p><p><img src="https://p0.meituan.net/travelcube/8336dfe0ebb7eda6ddb92d77cc5acce3426027.png" alt="图12" referrerpolicy="no-referrer"></p><p>再通过Keypatch，我们可以得到混淆前的分支语句结构：</p><p><img src="https://p0.meituan.net/travelcube/87e1d5bf3e1d212ca8c51696963b73f3251405.png" alt="图13" referrerpolicy="no-referrer"></p><p>至此，我们已经可以完整地恢复Fairplay的大多数控制流了。</p><h3 id="数据流混淆">数据流混淆</h3><p>这一部分在前面已经提及到了一些，目前我们已经找到了MBA表达式的模式，但还没能找到Fairplay中生成不透明常量的完整规则。其中MBA表达式的重写规则目前看起来仅有一个，即：</p><pre><code>x - c = (x ^ ~c) + ((2 * x) & ~(2 * c + 1)) + 1;
</code></pre><p>一些基于模式匹配的工具，比如D810已经可以比较好的处理这样的情况了。</p><h2 id="结束语">结束语</h2><p>目前，我们已经可以获取到解密每一段Mach-O的AES密钥了，通过大量的调试和反混淆，我们已经得出了这些密钥生成的初步结论。我们希望最终的目的是不依赖Apple设备的前提下，完成Fairplay DRM加解密的研究。</p><p><img src="https://p0.meituan.net/travelcube/40771c6b4c5ce84d9e3c7c1038790a6a525871.png" alt="图14" referrerpolicy="no-referrer"></p><p>最后，附上<a href="https://github.com/pwn0rz/fairplay_research">源码</a>，欢迎大家进行参考和研究。</p><h2 id="参考文献">参考文献</h2><ul><li>Eyrolles, N. (2017). Obfuscation with Mixed Boolean-Arithmetic Expressions: reconstruction, analysis and simplification tools (Doctoral dissertation, Université Paris-Saclay)</li><li><a href="https://github.com/obfuscator-llvm/obfuscator">https://github.com/obfuscator-llvm/obfuscator</a></li><li><a href="https://github.com/HikariObfuscator/Hikari">https://github.com/HikariObfuscator/Hikari</a></li><li><a href="https://github.com/keystone-engine/keypatch">https://github.com/keystone-engine/keypatch</a></li><li><a href="https://eshard.com/posts/d810_blog_post_1">https://eshard.com/posts/d810_blog_post_1</a></li></ul><h2 id="作者简介">作者简介</h2><p>吴聊、落落、朱米，均来自美团信息安全部。</p>  
</div>
            