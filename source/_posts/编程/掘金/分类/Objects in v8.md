
---
title: 'Objects in v8'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efea0005cb444fbb20017aaa58cac40~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 18:51:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efea0005cb444fbb20017aaa58cac40~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>图片来源：<a href="https://siliconangle.com/2016/10/10/upcoming-chrome-update-will-speed-web-pages-with-better-memory-usage/" target="_blank" rel="nofollow noopener noreferrer">siliconangle.com</a></p>
</blockquote>
<blockquote>
<p>本文作者：<a href="https://github.com/hsiaosiyuan0" target="_blank" rel="nofollow noopener noreferrer">hsy</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>文本将和大家一起简单了解一下 v8 内部是如何处理对象的，以及 v8 为了高速化对象属性的访问所做的一些优化的细节。除了结合现有的资料外，本文还链接了一些实现所对应的源码位置，以节约大家后续需要结合源码进行深入时所花的时间</p>
<p>本文的目的是了解 v8 的内部实现细节，大家可以根据自己的情况来决定是否需要先阅读下面的资料：</p>
<ul>
<li><a href="https://www.jayconrod.com/posts/52/a-tour-of-v8--object-representation" target="_blank" rel="nofollow noopener noreferrer">A tour of V8: object representation</a></li>
<li><a href="https://v8.dev/blog/fast-properties" target="_blank" rel="nofollow noopener noreferrer">Fast properties in V8</a></li>
</ul>
<h2 data-id="heading-1">TaggedImpl</h2>
<p>在 v8 内部实现中，所有对象都是从 <a href="https://github.com/nodejs/node/blob/2883c855e0105b51e5c8020d21458af109ffe3d4/deps/v8/src/objects/tagged-impl.h#L24" target="_blank" rel="nofollow noopener noreferrer">TaggedImpl</a> 派生的</p>
<p>下图是 v8 中涉及 Object 实现的部分类的继承关系图示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efea0005cb444fbb20017aaa58cac40~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>TaggedImpl 所抽象的逻辑是「打标签」，所以我们需要进一步了解「标签」的含义</p>
<p>v8 的 GC 是「准确式 GC，Precise GC」，与之相对的是「保守式 GC，Conservative GC」</p>
<p>GC 的任务就是帮助我们自动管理堆上的内存。当一个对象被 GC 识别为垃圾对象之后，GC 就需要对其占用的内存进行回收，随之而来的问题是 GC 如何判断指针和非指针，因为我们知道对象的属性可能是值属性、或者引用堆上的其他内容（指针）：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> <span class="hljs-built_in">Object</span> = Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>>;
<span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">field1</span>: <span class="hljs-number">1</span> &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码我们通过 <code>Record</code> 来模拟对象的数据结构，其实就是简单的键值对。不过我们把值都定义成了 number 类型，这是因为对于值类型，我们直接存放它们的值就可以了，而对于引用类型，我们则存放它们的内存地址，而内存地址也是值，所以就都用 number 表示了</p>
<p>保守式 GC 的优势是与应用之间的耦合性很低，为了达到这样的设计目的，就要让 GC 尽可能少的依赖应用提供的信息，结果就是 GC 无法准确判断某个值表示的是指针还是非指针。比如上面的例子，保守式 GC 无法准确知道 <code>field1</code> 的值 <code>1</code> 是表示数值，还是指针</p>
<p>当然保守式 GC 并不是完全不能识别指针，它可以根据应用具体的使用内存时的行为特点（所以也并不是完全解耦），对指针和非指针进行猜测。简单来说就是硬编码一些猜测的逻辑，比如我们知道应用中的一些确定行为，那么我们就不用和应用交互，直接把这部分逻辑硬编码到 GC 实现中就可以了。比如我们知道身份证的编码格式，如果要验证一串数字是不是身份证，我们可以根据编码格式来验证，也可以调用公安的 API（如果有的话），前者就是保守式 GC 的工作方式，可以验证出一部分，但是对于那些符合格式、但却不存在的号码，则也会被识别为身份证</p>
<p>我们知道如果一个内存地址被意外释放，那么一定会导致应用后续进入错误的状态、甚至崩溃。保守式 GC 为了应对这个问题，当它在标记活动对象时，会把看起来像是指针的地址都标记为活动的，这样就不会发生内存被意外释放的问题了，「保守式」之名也因此而得。不过随之而来的是，某些可能已经是垃圾的对象存活了下来，因此保守式 GC 存在压迫堆的风险</p>
<p>v8 的 GC 是准确式 GC，准确式 GC 就需要和应用进行紧密配合了，TaggedImpl 就是为了配合 GC 识别指针和非指针而定义的。TaggedImpl 使用的是称为 <a href="https://en.wikipedia.org/wiki/Tagged_pointer" target="_blank" rel="nofollow noopener noreferrer">pointer tagging</a> 的技术（该技术在 <a href="https://v8.dev/blog/pointer-compression" target="_blank" rel="nofollow noopener noreferrer">Pointer Compression in V8</a> 有提及）</p>
<p>pointer tagging 技术简单来说，就是利用地址都是按字长对齐（字长的整数倍）的特性。这个特性是这样来的：</p>
<ol>
<li>首先 CPU 的字长由于硬件设计上的考量，都是偶数</li>
<li>然后早期 CPU 由于内部设计的原因，对偶数地址的寻址的效率要高于对基数地址寻址的效率（不过由于硬件设计上的升级，目前来看也并非绝对了）</li>
<li>所以大家（编译器，运行时的内存分配）都会确保地址是按字长对齐的</li>
</ol>
<p>这样延续到现在，基本就当成一个默认规则了。基于这个规则，因为偶数的最低二进制位是 <code>0</code>，所以 v8 中：</p>
<ul>
<li>对于数值统一左移一位，这样数值的最低二进制位为 <code>0</code></li>
<li>对于指针则将最低二进制位置为 <code>1</code></li>
</ul>
<p>比如，对于 GC 而言，<code>0b110</code> 表示的是数值 <code>0b11</code>（使用时需右移一位），对于 <code>0b111</code> 表示的是指针 <code>0b110</code>（寻址时需减 1）。</p>
<p>通过打标签的操作，GC 就可以认为，如果某个地址最低二进制位是 <code>0</code> 则该位置就是 <a href="https://github.com/nodejs/node/blob/2883c855e0105b51e5c8020d21458af109ffe3d4/deps/v8/src/objects/smi.h#L23" target="_blank" rel="nofollow noopener noreferrer">Smi - small integer</a>，否则就是 <a href="https://github.com/nodejs/node/blob/fb180ac1107c7f8e7dea9c973844dae93b2eda04/deps/v8/src/objects/heap-object.h#L24" target="_blank" rel="nofollow noopener noreferrer">HeapObject</a></p>
<p>可以参考 <a href="https://item.jd.com/12010270.html" target="_blank" rel="nofollow noopener noreferrer">垃圾回收的算法与实现</a> 一书来更加系统的了解 GC 实现的细节</p>
<h2 data-id="heading-2">Object</h2>
<p><a href="https://github.com/nodejs/node/blob/9cd523d148dcefa6dd86cb7ef6448520aad5c574/deps/v8/src/objects/objects.h#L275" target="_blank" rel="nofollow noopener noreferrer">Object</a> 在 v8 内部用于表示所有受 GC 管理的对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c96151c340ac4fd79ec5f007049fe6ab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图演示了 v8 运行时的内存布局，其中：</p>
<ul>
<li>stack 表示 native 代码（cpp 或 asm）使用的 stack</li>
<li>heap 表示受 GC 管理的堆</li>
<li>native 代码通过 <code>ptr_</code> 来引用堆上的对象，如果是 smi 则无需访问 GC 的堆</li>
<li>如果要操作堆上对象的字段，则需进一步通过在对象所属的类的定义中、硬编码的偏移量来完成</li>
</ul>
<p>各个类中的字段的偏移量都定义在 <a href="https://github.com/hsiaosiyuan0/v8/blob/learn/out/x64.debug/gen/torque-generated/field-offsets.h" target="_blank" rel="nofollow noopener noreferrer">field-offsets-tq.h</a> 中。之所以要手动硬编码，是因为这些类的实例内存需要通过 GC 来分配，而是不是直接使用 native 的堆，所以就不能利用 cpp 编译器自动生成的偏移量了</p>
<p>我们通过一个图例来解释一下编码方式（64bit 系统）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0c2f53310864826a10dc30d36bc720c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>图中通过不同的颜色表示对象自身定义的区域和继承的区域</li>
<li>Object 中没有字段，所以 <code>Object::kHeaderSize</code> 是 <code>0</code></li>
<li>HeapObject 是 Object 类的子类，因此它的字段偏移起始值是 <code>Object::kHeaderSize</code>（<a href="https://github.com/nodejs/node/blob/fb180ac1107c7f8e7dea9c973844dae93b2eda04/deps/v8/src/objects/heap-object.h#L202" target="_blank" rel="nofollow noopener noreferrer">参考代码</a>），HeapObject 只有一个字段偏移 <code>kMapOffset</code> 值等于 <code>Object::kHeaderSize</code> 即 <code>0</code>，因为该字段大小是 <code>kTaggedSize</code>（在 64bit 系统上该值为 8），所以 <code>HeapObject:kHeaderSize</code> 是 8bytes</li>
<li>JSReceiver 是 HeapObject 类的子类，因此它的字段偏移起始值是 <code>HeapObject:kHeaderSize</code>（<a href="https://github.com/nodejs/node/blob/fb180ac1107c7f8e7dea9c973844dae93b2eda04/deps/v8/src/objects/js-objects.h#L277" target="_blank" rel="nofollow noopener noreferrer">参考代码</a>），JSReceiver 也只有一个字段偏移 <code>kPropertiesOrHashOffset</code>，其值为 <code>HeapObject:kHeaderSize</code> 即 8bytes，因为该字段大小是 <code>kTaggedSize</code>，所以 <code>JSReceiver::kHeaderSize</code> 为 16bytes（加上了继承的 8bytes）</li>
<li>JSObject 是 JSReceiver 的子类，因此它的字段偏移起始值是 <code>JSReceiver::kHeaderSize</code>（<a href="https://github.com/hsiaosiyuan0/v8/blob/21eeca5d0f3e7073efd7f481c54bc303fd98712f/out/x64.debug/gen/torque-generated/src/objects/js-objects-tq.inc#L40" target="_blank" rel="nofollow noopener noreferrer">参考代码</a>）, JSObject 也只有一个字段偏移 <code>kElementsOffset</code>，值为 <code>JSReceiver::kHeaderSize</code> 即 16bytes，最后 <code>JSObject::kHeaderSize</code> 就是 24bytes</li>
</ul>
<p>根据上面的分析结果，最终通过手动编码实现的继承后，JSObject 中一共有三个偏移量：</p>
<ul>
<li>kMapOffset</li>
<li>kPropertiesOrHashOffset</li>
<li>kElementsOffset</li>
</ul>
<p>这三个偏移量也就表示 JSObject 有三个内置的属性：</p>
<ul>
<li>map</li>
<li>propertiesOrHash</li>
<li>elements</li>
</ul>
<h3 data-id="heading-3">map</h3>
<p>map 一般也称为 HiddenClass，它描述了对象的元信息，比如对象的大小（instance_size）等等。map 也是继承自 <code>HeapObject</code>，因此它本身也是受 GC 管理的对象，JSObject 中的 map 字段是指向堆上的 map 对象的指针</p>
<p>我们可以结合 map 源码中注释的 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/map.h#L106" target="_blank" rel="nofollow noopener noreferrer">Map layout</a> 和下图来理解 map 的内存的拓扑形式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f4e27bc51094707be17cca1515ef64f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">propertiesOrHash，elements</h3>
<p>在 JS 中，数组和字典在使用上没有显著的差别，但是从引擎实现的角度，在其内部为数组和字典选择不同的数据结构可以优化它们的访问速度，所以分别使用 <code>propertiesOrHash</code> 和 <code>elements</code> 两个属性就是这个目的</p>
<p>对于命名属性（named properties）会关联到 <code>propertiesOrHash</code>，对于索引属性（indexed properties）则关联到 <code>elements</code>。之所以使用「关联」一词，是因为 <code>propertiesOrHash</code> 和 <code>elements</code> 只是指针，引擎会根据运行时的优化策略，将它们连接到堆上的不同的数据结构</p>
<p>我们可以通过下面的图来演示 JSObject 在堆上的可能的拓扑形式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e98432dd4ac4998b75cbdf4d90541b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要说明的是，v8 的分代式 GC 会对堆按对象的活跃度和用途进行划分，所以 map 对象实际会放到专门的堆空间中（所以实际会比上图显得更有组织），不过并不影响上图的示意</p>
<h2 data-id="heading-5">inobject、fast</h2>
<p>上面我们介绍到 named properties 会关联到对象的 <code>propertiesOrHash</code> 指针指向的数据结构，而用于存储属性的数据结构，v8 并不是直接选择了常见的 <a href="https://www.geeksforgeeks.org/hashing-data-structure/" target="_blank" rel="nofollow noopener noreferrer">hash map</a>，而是内置了 3 种关联属性的形式：</p>
<ul>
<li>inobject</li>
<li>fast</li>
<li>slow</li>
</ul>
<p>我们先来了解 inobject 和 fast 的形式，下面是它们的整体图示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/106409d8a2874b0c97fd4f0001cabe48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>inobject 就和它的名字一样，表示属性值对应的指针直接保存在对象开头的连续地址内，它是 3 种形式中访问速度最快的（按照 <a href="https://v8.dev/blog/fast-properties" target="_blank" rel="nofollow noopener noreferrer">fast-properties</a> 中的描述）</p>
<p>注意观察上图中的 <code>inobject_ptr_x</code>，它们只是指向属性值的指针，因此为了按照名称找到对应的属性，需要借助一个名为 <code>DescriptorArray</code> 的结构，这个结构中记录了：</p>
<ul>
<li>key，字段名称</li>
<li>PropertyDetails，表示字段的元信息，比如 <code>IsReadOnly</code>、<code>IsEnumerable</code> 等</li>
<li>value，只有常量时才会存入其中，如果是 <code>1</code> 表示该位置未被使用（可以结合上文的标签进行理解）</li>
</ul>
<p>为了访问 inobject 或者 fast 属性（相关实现在 <a href="https://github.com/hsiaosiyuan0/v8/blob/997d88e64fd48cc8772c1c5d4b60d89b9310fcfe/src/objects/lookup.cc#L1160" target="_blank" rel="nofollow noopener noreferrer">LookupIterator::LookupInRegularHolder</a>）：</p>
<ol>
<li>
<p>v8 需要先根据属性名，在 <code>DescriptorArray</code> 中搜索到属性值在 inobject array（inobject 因为是连续的内存地址，所以可以看成是数组）或者 property array （图中最左边）中的索引</p>
</li>
<li>
<p>然后结合数组首地址与指针偏移、拿到属性值的指针，再通过属性值的指针，访问具体的属性值（相关实现在 <a href="https://github.com/hsiaosiyuan0/v8/blob/627b6b2f06e2046d193ae9c809d0561fcaf8559b/src/objects/js-objects-inl.h#L348" target="_blank" rel="nofollow noopener noreferrer">JSObject::FastPropertyAtPut</a>）</p>
</li>
</ol>
<p>inobject 相比 fast 要更快，这是因为 fast 属性多了一次间接寻址：</p>
<ol>
<li>
<p>inobject 属性知道了其属性值的索引之后，直接根据对象的首地址进行偏移即可（inobject array 之前的 <code>map_ptr</code>，<code>propertiesOrHash_ptr</code>，<code>elements_ptr</code> 是固定的大小）</p>
</li>
<li>
<p>而如果是 fast，则需要先在对象的首地址偏移 <code>kPropertiesOrHashOffset</code> 拿到 PropertyArray 的首地址，然后在基于该首地址再进行索引的偏移</p>
</li>
</ol>
<p>因为 inobject 是访问速度最快的形式，所以在 v8 中将其设定为了默认形式，不过需要注意的是 fast 和 inobject 是互补的，只是默认情况下，添加的属性优先按 inobject 形式进行处理，而当遇到下面的情形时，属性会被添加到 fast 的 PropertyArray 中：</p>
<ul>
<li>当整体 inobject 属性的数量超过一定上限时</li>
<li>当动态添加的属性超过 inobject 的预留数量时</li>
<li>当 slack tracking 完成后</li>
</ul>
<p>v8 在创建对象的时候，会动态地选择一个 inobject 数量，记为 <code>expected_nof_properties</code>（后面会介绍），然后以该数量结合对象的内部字段（比如 <code>map_ptr</code> 等）数来创建对象</p>
<p>初始的 inobject 数量总是会比当前实际所需的尺寸大一些，目的是作为后续可能动态添加的属性的缓冲区，如果后续没有动态添加属性的动作，那么势必会造成空间的浪费，这个问题就可以通过后面介绍的 slack tracking 来解决</p>
<p>比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  b = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> A();
a.c = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在为 <code>a</code> 分配空间时，虽然 <code>A</code> 只有 1 个属性 <code>b</code>，但是 v8 选择的 <code>expected_nof_properties</code> 值会比实际所需的 1 大。因为 JS 语言的动态性，多分配的空间可以让后续动态添加的属性也能享受 inobject 的效率，比如例子中的 <code>a.c = 2</code>，<code>c</code> 也是 inobject property，尽管它是后续动态添加的</p>
<h2 data-id="heading-6">slow</h2>
<p>slow 相比 fast 和 inobject 更慢，是因为 slow 型的属性访问无法使用 inline cache 技术进行优化，跟多关于 inline cache 的细节可以参考：</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inline_caching" target="_blank" rel="nofollow noopener noreferrer">Inline caching</a></li>
<li><a href="https://mrale.ph/blog/2012/06/03/explaining-js-vms-in-js-inline-caches.html" target="_blank" rel="nofollow noopener noreferrer">Explaining JavaScript VMs in JavaScript - Inline Caches</a></li>
</ul>
<p>slow 是和 inobject、fast 互斥的，当进入 slow 模式后，对象内的属性结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d21c540486484aa09a6ec82fe7e9e828~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>slow 模式不再需要上文提到的 <code>DescriptorArray</code> 了，字段的信息统一都存放在一个字典中</p>
<h3 data-id="heading-7">inobject 上限</h3>
<p>上文提到 inobject properties 的数量是有上限的，其计算过程大致是：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// 为了方便计算，这里把涉及到的常量定义从源码各个文件中摘出后放到了一起</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> V8_HOST_ARCH_64_BIT</span>
<span class="hljs-keyword">constexpr</span> <span class="hljs-keyword">int</span> kSystemPointerSizeLog2 = <span class="hljs-number">3</span>;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-keyword">constexpr</span> <span class="hljs-keyword">int</span> kTaggedSizeLog2 = kSystemPointerSizeLog2;
<span class="hljs-keyword">constexpr</span> <span class="hljs-keyword">int</span> kSystemPointerSize = <span class="hljs-built_in"><span class="hljs-keyword">sizeof</span></span>(<span class="hljs-keyword">void</span>*);

<span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> <span class="hljs-keyword">int</span> kJSObjectHeaderSize = <span class="hljs-number">3</span> * kApiTaggedSize;
<span class="hljs-built_in">STATIC_ASSERT</span>(kHeaderSize == Internals::kJSObjectHeaderSize);

<span class="hljs-keyword">constexpr</span> <span class="hljs-keyword">int</span> kTaggedSize = kSystemPointerSize;
<span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> <span class="hljs-keyword">int</span> kMaxInstanceSize = <span class="hljs-number">255</span> * kTaggedSize;
<span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> <span class="hljs-keyword">int</span> kMaxInObjectProperties = (kMaxInstanceSize - kHeaderSize) >> kTaggedSizeLog2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面的定义，在 64bit 系统上、未开启指针压缩的情况下，最大数量是 <code>252 = (255 * 8 - 3 * 8) / 8</code></p>
<h2 data-id="heading-8">allow-natives-syntax</h2>
<p>为了后面可以通过代码演示，这里需要穿插介绍一下 <code>--allow-natives-syntax</code> 选项，该选项是 v8 的一个选项，开启该选项后，我们可以使用一些私有的 API，这些 API 可以方便了解引擎运行时的内部细节，最初是用于 v8 源码中编写测试案例的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// test.js</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;
%DebugPrint(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过命令 <code>node --allow-natives-syntax test.js</code> 即可运行上面的代码，其中 <code>%DebugPrint</code> 就是 natives-syntax，而 <code>DebugPrint</code> 则是私有 API 中的一个</p>
<p>更多的 API 可以在 <a href="https://github.com/hsiaosiyuan0/v8/blob/025af802d15461ece744c129883f95ae3cd04734/src/runtime/runtime.h#L474" target="_blank" rel="nofollow noopener noreferrer">runtime.h</a> 中找到，它们具体的用法则可以通过搜索 v8 源码中的测试案例来了解。另外，DebugPrint 对应的实现在 <a href="https://github.com/hsiaosiyuan0/v8/blob/627b6b2f06e2046d193ae9c809d0561fcaf8559b/src/diagnostics/objects-printer.cc#L104" target="_blank" rel="nofollow noopener noreferrer">objects-printer.cc</a> 中</p>
<p>上面的代码运行后显示的内容类似：</p>
<pre><code class="hljs language-bash copyable" lang="bash">DebugPrint: Smi: 0x1 (1) <span class="hljs-comment"># Smi 我们已经在上文介绍过了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">构造函数创建</h2>
<p>上文提到 v8 创建对象的时候，会动态选择一个预期值，该值作为 inobject 属性的初始数量，记为 <code>expected_nof_properties</code>，接下来我们看下该值是如何选择的</p>
<p>在 JS 中有两种主要的创建对象的方式：</p>
<ul>
<li>从构造函数创建</li>
<li>对象字面量</li>
</ul>
<p>我们先看从构造函数创建的情况</p>
<p>将字段作为 inobject properties 的技术并不是 v8 首创的，在静态语言的编译中，是常见的属性处理方案。v8 只是将其引入到 JS 引擎的设计中，并针对 JS 引擎做了一些调整</p>
<p>从构造函数创建的对象，因为在编译阶段就能<strong>大致</strong>获得属性的数量，所以在分配对象的时候，inobject 属性数就可以借助编译阶段收集的信息：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.p1 = <span class="hljs-number">1</span>;
  <span class="hljs-built_in">this</span>.p2 = <span class="hljs-number">2</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor2</span>(<span class="hljs-params">condition</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.p1 = <span class="hljs-number">1</span>;
  <span class="hljs-built_in">this</span>.p2 = <span class="hljs-number">2</span>;
  <span class="hljs-keyword">if</span> (condition) &#123;
    <span class="hljs-built_in">this</span>.p3 = <span class="hljs-number">3</span>;
    <span class="hljs-built_in">this</span>.p4 = <span class="hljs-number">4</span>;
  &#125;
&#125;

<span class="hljs-keyword">const</span> o1 = <span class="hljs-keyword">new</span> Ctor1();
<span class="hljs-keyword">const</span> o2 = <span class="hljs-keyword">new</span> Ctor2();

%DebugPrint(o1);
%DebugPrint(o2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>「大致」的含义就是，对于上面的 <code>Ctor2</code> 会认为它有 4 个属性，而不会考虑 <code>condition</code> 的情况</p>
<p>我们可以通过运行上面的代码来测试：</p>
<pre><code class="copyable">DebugPrint: 0x954bdc78c61: [JS_OBJECT_TYPE]
 - map: 0x0954a8d7a921 <Map(HOLEY_ELEMENTS)> [FastProperties]
 - prototype: 0x0954bdc78b91 <Object map = 0x954a8d7a891>
 - elements: 0x095411500b29 <FixedArray[0]> [HOLEY_ELEMENTS]
 - properties: 0x095411500b29 <FixedArray[0]> &#123;
    #p1: 1 (const data field 0)
    #p2: 2 (const data field 1)
 &#125;
0x954a8d7a921: [Map]
 - type: JS_OBJECT_TYPE
 - instance size: 104
 - inobject properties: 10
 - elements kind: HOLEY_ELEMENTS
 - unused property fields: 8
 - enum length: invalid
 - stable_map
 - back pointer: 0x0954a8d7a8d9 <Map(HOLEY_ELEMENTS)>
 - prototype_validity cell: 0x0954ff2b9459 <Cell value= 0>
 - instance descriptors (own) #2: 0x0954bdc78d41 <DescriptorArray[2]>
 - prototype: 0x0954bdc78b91 <Object map = 0x954a8d7a891>
 - constructor: 0x0954bdc78481 <JSFunction Ctor1 (sfi = 0x954ff2b6c49)>
 - dependent code: 0x095411500289 <Other heap object (WEAK_FIXED_ARRAY_TYPE)>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码会输出两段 <code>DebugPrint</code>，上面为其中的第一段：</p>
<ul>
<li>紧接着 <code>DebugPrint:</code> 打印的是我们传入的对象 <code>o1</code></li>
<li>随后的 <code>0x954a8d7a921: [Map]</code> 是该对象的 map 信息</li>
<li>我们已经介绍过 map 是对象的元信息，因此诸如 <code>inobject properties</code> 都记录在其中</li>
<li>上面的 <code>inobject properties</code> 是 <code>10 = 2 + 8</code>，其中 2 是编译阶段收集到的属性数，8 是额外预分配的属性数</li>
<li>因为对象 header 中总是有指向 <code>map</code>、<code>propertiesOrHash</code>、<code>elements</code> 的三个指针，所以整个对象的大小（instance size）就是 <code>headerSize + inobject_properties_size</code> 即 <code>104 = (3 + (2 + 8)) * 8</code></li>
</ul>
<p>大家可以根据上面的过程验证下 <code>%DebugPrint(o2)</code> 的输出</p>
<h3 data-id="heading-10">空构造函数</h3>
<p>为了避免大家在试验的过程中产生疑惑，下面再解释一下空构造函数时分配的对象大小：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">const</span> o = <span class="hljs-keyword">new</span> Ctor();
%DebugPrint(o);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的打印结果显示 <code>inobject properties</code> 数量也是 10，按照前文的计算过程，因为编译阶段发现该构造函数并没有属性，数量应该是 <code>8 = 0 + 8</code> 才对</p>
<p>之所以显示 10 是因为，如果编译阶段发现没有属性，那么默认也会给定一个数值 2 作为属性的数量，这么做是基于「大部分构造函数都会有属性，当前没有可能是后续动态添加」的假定</p>
<p>关于上面的计算过程，可以通过 <a href="https://github.com/hsiaosiyuan0/v8/blob/3f9ff062b053155df7897f199e80a8bafe7c34df/src/objects/shared-function-info.cc#L565" target="_blank" rel="nofollow noopener noreferrer">shared-function-info.cc</a> 进一步探究</p>
<h3 data-id="heading-11">Class</h3>
<p>上文我们都是直接将函数对象当做构造函数来使用的，而 ES6 中早已支持了 Class，接下来我们来看下使用 Class 来实例化对象的情况</p>
<p>其实 Class 只是一个语法糖，JS 语言标准对 Class 的运行时语义定义在 <a href="https://tc39.es/ecma262/#sec-runtime-semantics-classdefinitionevaluation" target="_blank" rel="nofollow noopener noreferrer">ClassDefinitionEvaluation</a> 一节中。简单来说就是同样会创建一个函数对象（并设置该函数的名称为 Class 名），这样随后我们的 <code>new Class</code> 其实和我们 <code>new FunctionObject</code> 的语义一致</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class1</span> </span>&#123;&#125;

%DebugPrint(Ctor);
%DebugPrint(Class1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以运行上面的代码，会发现 <code>Ctor</code> 和 <code>Class1</code> 都是 <code>JS_FUNCTION_TYPE</code></p>
<p>我们之前已经介绍过，初始的 inobject properties 数量会借助编译时收集的信息，所以下面的几个形式是等价的，且 inobject properties 数量都是 11（3 + 8）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.p1 = <span class="hljs-number">1</span>;
  <span class="hljs-built_in">this</span>.p2 = <span class="hljs-number">2</span>;
  <span class="hljs-built_in">this</span>.p3 = <span class="hljs-number">3</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class1</span> </span>&#123;
  p1 = <span class="hljs-number">1</span>;
  p2 = <span class="hljs-number">2</span>;
  p3 = <span class="hljs-number">3</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class2</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.p1 = <span class="hljs-number">1</span>;
    <span class="hljs-built_in">this</span>.p2 = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">this</span>.p3 = <span class="hljs-number">3</span>;
  &#125;
&#125;
<span class="hljs-keyword">const</span> o1 = <span class="hljs-keyword">new</span> Ctor();
<span class="hljs-keyword">const</span> o2 = <span class="hljs-keyword">new</span> Class1();
<span class="hljs-keyword">const</span> o3 = <span class="hljs-keyword">new</span> Class2();
%DebugPrint(o1);
%DebugPrint(o2);
%DebugPrint(o3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编译阶段的收集的属性数称为「预估属性数」，因为其只需提供预估的精度，所以逻辑很简单，在解解析函数或者 Class 定义的时候，发了一个设置属性的语句就让「预估属性数」累加 1。下面的形式是等价的，都会将「预估属性数」识别为 0 而造成 inobject properties 初始值被设定为 10（上文有讲道过，当 estimated 为 0 时，总是会分配固定的个数 2，再加上预分配 8，会让初始 inobject 数定成 10）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ctor</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// babel runtime patch</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_defineProperty</span>(<span class="hljs-params">obj, key, value</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> obj) &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-attr">value</span>: value,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    obj[key] = value;
  &#125;
  <span class="hljs-keyword">return</span> obj;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p1"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p2"</span>, <span class="hljs-number">2</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p3"</span>, <span class="hljs-number">3</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> o1 = <span class="hljs-keyword">new</span> Ctor();
<span class="hljs-keyword">const</span> o2 = <span class="hljs-keyword">new</span> Class1();
%DebugPrint(o1);
%DebugPrint(o2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Class1</code> 构造函数中的 <code>_defineProperty</code> 对于目前的预估逻辑来说太复杂了，预估逻辑设计的简单并不是因为从技术上不能分析上面的例子，而是因为 JS 语言的动态性，与为了保持启动速度（也是动态语言的优势）让这里不太适合使用过重的静态分析技术</p>
<p><code>_defineProperty</code> 的形式其实是 babel 目前编译的结果，结合后面会介绍的 slack tracking 来说，即使这里预估数不符合我们的预期，但也不会有太大的影响，因为我们的单个类的属性个数超过 10 的情况在整个应用中来看也不会是大多数，不过如果我们考虑继承的情况：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class1</span> </span>&#123;
  p11 = <span class="hljs-number">1</span>;
  p12 = <span class="hljs-number">1</span>;
  p13 = <span class="hljs-number">1</span>;
  p14 = <span class="hljs-number">1</span>;
  p15 = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Class1</span> </span>&#123;
  p21 = <span class="hljs-number">1</span>;
  p22 = <span class="hljs-number">1</span>;
  p23 = <span class="hljs-number">1</span>;
  p24 = <span class="hljs-number">1</span>;
  p25 = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class3</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Class2</span> </span>&#123;
  p31 = <span class="hljs-number">1</span>;
  p32 = <span class="hljs-number">1</span>;
  p33 = <span class="hljs-number">1</span>;
  p34 = <span class="hljs-number">1</span>;
  p35 = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-keyword">const</span> o1 = <span class="hljs-keyword">new</span> Class3();
%DebugPrint(o1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为继承形式的存在，很可能经过多次继承，我们的属性数会超过 10。我们打印上面的代码，会发现 inobject properties 是 23（15 + 8），如果经过 babel 编译，则代码会变成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_defineProperty</span>(<span class="hljs-params">obj, key, value</span>) </span>&#123; <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> obj) &#123; <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123; <span class="hljs-attr">value</span>: value, <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span> &#125;); &#125; <span class="hljs-keyword">else</span> &#123; obj[key] = value; &#125; <span class="hljs-keyword">return</span> obj; &#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p11"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p12"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p13"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p14"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p15"</span>, <span class="hljs-number">1</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Class1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(...args);

    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p21"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p22"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p23"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p24"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p25"</span>, <span class="hljs-number">1</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class3</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Class2</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(...args);

    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p31"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p32"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p33"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p34"</span>, <span class="hljs-number">1</span>);
    _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"p35"</span>, <span class="hljs-number">1</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> o1 = <span class="hljs-keyword">new</span> Class3();
%DebugPrint(o1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 inobject properties 数量只有 14 个，原因是 Class3 的 inobject 属性数预估值、还需要加上其祖先类的 inobject 属性数的预估值，其两个祖先类的预估值都是 2（因为编译期没有收集到数量而默认分配的固定数量 2），因此 Class3 的 inobject 属性预估值就是 <code>6 = 2 + 2 + 2</code>，加上额外分配的 8 个，最后是 14 个</p>
<p>而我们实际的属性数量是 15 个，这就导致第 15 个属性 <code>p35</code> 被分配成了 fast 型，回顾没有经过 babel 编译的代码，所有属性都会是 inobject 型的</p>
<p>最初发现 babel 和 tsc 的编译结果不同，后者未使用 <code>_defineProperty</code> 的形式，以为是 babel 编译实现有瑕疵。后面发现 babel 的结果其实是标准中规定的行为，见 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#public_instance_fields" target="_blank" rel="nofollow noopener noreferrer">Public instance fields</a> - 实例字段是使用 <code>Object.defineProperty</code> 添加的。对于 tsc 来说，开启 <a href="https://www.typescriptlang.org/tsconfig#useDefineForClassFields" target="_blank" rel="nofollow noopener noreferrer">useDefineForClassFields</a> 后可以达到相同的编译结果（在目前的 deno-v1.9 中这个选项被默认开启了）</p>
<p>本来是想说大家可以选择 tsc 的，但现在看来在一些对性能有极致要求的场景下，避免引入编译环节或许是最好的方法</p>
<h2 data-id="heading-12">从对象字面量创建</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123; <span class="hljs-attr">p1</span>: <span class="hljs-number">1</span> &#125;;
%DebugPrint(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行上面的代码，会发现 <code>inobject properties</code> 数量是 1，这里没有 8 个的预留空间，是因为从对象字面量创建经过的是 <a href="https://github.com/hsiaosiyuan0/v8/blob/51140a440949dbbeea7a4e6c2185ccdeb8b6276e/src/runtime/runtime-literals.cc#L374" target="_blank" rel="nofollow noopener noreferrer">CreateObjectLiteral</a> 方法，其内部没有预留空间的策略，而是 <a href="https://github.com/nodejs/node/blob/9cd523d148dcefa6dd86cb7ef6448520aad5c574/deps/v8/src/objects/map.cc#L2003" target="_blank" rel="nofollow noopener noreferrer">直接使用</a> 编译收集的信息，这与从构造函数创建经过的 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/js-objects.cc#L2122" target="_blank" rel="nofollow noopener noreferrer">JSObject::New</a> 方法内部的策略不同</p>
<p>从对象字面量创建会使用字面量中的属性数作为 <code>inobject properties</code> 的数量，因此后续添加的属性会是 fast 型</p>
<h3 data-id="heading-13">空对象字面量</h3>
<p>和空构造函数的情况类似，空对象字面量的大小也需要另外讨论：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123;&#125;;
%DebugPrint(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行上面的代码，会发现 <code>inobject properties</code> 数量是 4，这是因为：</p>
<ul>
<li><a href="https://github.com/hsiaosiyuan0/v8/blob/51140a440949dbbeea7a4e6c2185ccdeb8b6276e/src/runtime/runtime-literals.cc#L374" target="_blank" rel="nofollow noopener noreferrer">CreateObjectLiteral</a> 内会调用 <a href="https://github.com/hsiaosiyuan0/v8/blob/3d2f61fb720ef0cb884c7b16735174353827012c/src/heap/factory.cc#L3099" target="_blank" rel="nofollow noopener noreferrer">Factory::ObjectLiteralMapFromCache</a></li>
<li>Factory::ObjectLiteralMapFromCache 的逻辑是，当空字面量时，使用 <code>object_function().initial_map()</code> 来做成创建对象的模板</li>
<li><code>object_function()</code> 自身的创建在 <a href="https://github.com/hsiaosiyuan0/v8/blob/51140a440949dbbeea7a4e6c2185ccdeb8b6276e/src/init/bootstrapper.cc#L832" target="_blank" rel="nofollow noopener noreferrer">Genesis::CreateObjectFunction</a> 中，其中的 <code>kInitialGlobalObjectUnusedPropertiesCount</code> 是 4</li>
</ul>
<p>所以 4 是一个硬编码的值，当创建空对象的时候，就使用该值作为初始的 inobject properties 的数量</p>
<p>另外 CreateObjectLiteral 源码中也 <a href="https://github.com/hsiaosiyuan0/v8/blob/51140a440949dbbeea7a4e6c2185ccdeb8b6276e/src/runtime/runtime-literals.cc#L391" target="_blank" rel="nofollow noopener noreferrer">提及</a>，如果使用 <code>Object.create(null)</code> 创建的对象，则直接是 slow 模式</p>
<h2 data-id="heading-14">inobject、fast、slow 之切换</h2>
<p>inobject、fast、slow 三种模式的存在，是基于分而治之的理念。对有静态性的场景（比如构造函数创建），则适用 inobject、fast，对动态性的部分，则适用 slow。下面我们来简单看一下三者之间的切换条件</p>
<ol>
<li>在 inobject 配额足够的情况下，属性优先被当成 inobject 型的</li>
<li>当 inobject 配个不足的情况下，属性被当成是 fast 型的</li>
<li>当 fast 型的配额也不足的情况下，对象整个切换成 slow 模式</li>
<li>中间某一步骤中，执行了 <code>delete</code> 操作删除属性（除了删除最后一个顺位的属性以外，删除其余顺位的属性都会）让对象整个切换成 slow 模式</li>
<li>如果某个对象被设置为另一个函数对象的 <code>property</code> 属性，则该对象也会切换成 slow 模式，见 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/js-objects.cc#L4421" target="_blank" rel="nofollow noopener noreferrer">JSObject::OptimizeAsPrototype</a></li>
<li>一旦对象切换成 slow 模式，从开发者的角度，就基本可以认为该对象不会再切换成 fast 模式了（虽然引擎内部的一些特殊情况下会使用 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/js-objects.cc#L3415" target="_blank" rel="nofollow noopener noreferrer">JSObject::MigrateSlowToFast</a> 切换回 fast）</li>
</ol>
<p>上面的切换规则看起来好像很繁琐（并且也可能并不是全部情况），但其实背后的思路很简单，inobject 和 fast 都是「偏静态」的优化手段，而 slow 则是完全动态的形式，当对象频繁地动态添加属性、或者执行了 <code>delete</code> 操作，则预测它很可能未来还会频繁的变动，那么使用纯动态的形式可能会更好，所以切换成 slow 模式</p>
<p>关于 fast 型的配额我们可以稍微了解一下，fast 型是存放在 PropertyArray 中的，这个数组以每次 <a href="https://github.com/hsiaosiyuan0/v8/blob/627b6b2f06e2046d193ae9c809d0561fcaf8559b/src/objects/js-objects.h#L781" target="_blank" rel="nofollow noopener noreferrer">kFieldsAdded</a>（当前版本是 3）的步长扩充其长度，目前有一个 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/map.h#L944" target="_blank" rel="nofollow noopener noreferrer">kFastPropertiesSoftLimit</a>（当前是 12）作为其 limit，而 <a href="https://github.com/hsiaosiyuan0/v8/blob/627b6b2f06e2046d193ae9c809d0561fcaf8559b/src/objects/map-inl.h#L166" target="_blank" rel="nofollow noopener noreferrer">Map::TooManyFastProperties</a> 中使用的是 <code>></code>，所以 fast 型目前的配额最大是 15</p>
<p>大家可以使用下面的代码测试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;&#125;;
<span class="hljs-keyword">const</span> cnt = <span class="hljs-number">19</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cnt; i++) &#123;
  obj[<span class="hljs-string">"p"</span> + i] = <span class="hljs-number">1</span>;
&#125;
%DebugPrint(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分别设置 <code>cnt</code> 为 <code>4</code>，<code>19</code> 和 <code>20</code>，会得到类似下面的输出：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 4</span>
DebugPrint: 0x3de5e3537989: [JS_OBJECT_TYPE]
 <span class="hljs-comment">#...</span>
 - properties: 0x3de5de480b29 <FixedArray[0]> &#123;

<span class="hljs-comment">#19</span>
DebugPrint: 0x3f0726bbde89: [JS_OBJECT_TYPE]
 <span class="hljs-comment">#...</span>
 - properties: 0x3f0726bbeb31 <PropertyArray[15]> &#123;

<span class="hljs-comment"># 20</span>
DebugPrint: 0x1a98617377e1: [JS_OBJECT_TYPE]
 <span class="hljs-comment">#...</span>
 - properties: 0x1a9861738781 <NameDictionary[101]>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>上面的输出中，当使用了 4 个属性时，它们都是 inobject 型的 <code>FixedArray[0]</code></li>
<li>当使用了 19 个属性时，已经有 15 个属性是 fast 型 <code>PropertyArray[15]</code></li>
<li>当使用了 20 个属性时，因为超过了上限，对象整体切换成了 slow 型 <code>NameDictionary[101]</code></li>
</ul>
<p>至于为什么 inobject 显示的是 <code>FixedArray</code>，只是因为当没有使用到 fast 型的时候 <code>propertiesOrHash_ptr</code> 默认指向了一个 <code>empty_fixed_array</code>，有兴趣的同学可以通过阅读 <a href="https://github.com/hsiaosiyuan0/v8/blob/627b6b2f06e2046d193ae9c809d0561fcaf8559b/src/objects/js-objects-inl.h#L656" target="_blank" rel="nofollow noopener noreferrer">property_array</a> 来确认</p>
<h2 data-id="heading-15">slack tracking</h2>
<p>前文我们提到，v8 中的初始 inobject 属性的数量，总是会多分配一些，目的是让后续可能通过动态添加的属性也可以成为 inobject 属性，以享受到其带来的快速访问效率。但是多分配的空间如果没有被使用一定会造成浪费，在 v8 中是通过称为 slack tracking 的技术来提高空间利用率的</p>
<p>这个技术简单来说是这样实现的：</p>
<ul>
<li>构造函数对象的 map 中有一个 <code>initial_map()</code> 属性，该属性就是那些由该构造函数对象创建的模板，即它们的 map</li>
<li>slack tracking 会修改 <code>initial_map()</code> 属性中的 <code>instance_size</code> 属性值，该值是 GC 分配内存空间时使用的</li>
<li>当第一次使用某个构造函数 C 创建对象时，它的 <code>initial_map()</code> 是未设置的，因此初次会设置该值，简单来说就是创建一个新的 map 对象，并设置该对象的 <code>construction_counter</code> 属性，见 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/map.cc#L2601" target="_blank" rel="nofollow noopener noreferrer">Map::StartInobjectSlackTracking</a></li>
<li>construction_counter 其实是一个递减的计数器，初始值是 <a href="https://github.com/hsiaosiyuan0/v8/blob/089218a87a7a69d9694c7c3020387063eb232c72/src/objects/map.h#L288" target="_blank" rel="nofollow noopener noreferrer">kSlackTrackingCounterStart</a> 即 7</li>
<li>随后每次（包括当次）使用该构造函数创建对象，都会对 construction_counter <a href="https://github.com/hsiaosiyuan0/v8/blob/3d2f61fb720ef0cb884c7b16735174353827012c/src/heap/factory.cc#L2200" target="_blank" rel="nofollow noopener noreferrer">递减</a>，当计数为 0 时，就会汇总当前的属性数（包括动态添加的），然后得到最终的 instance_size</li>
<li>slack tracking 完成后，后续动态添加的属性都是 fast 型的</li>
</ul>
<p>construction_counter 计数的形式类似下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63869bba89ee42a18b7f71bb2b539508~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>slack tracking 是根据构造函数调用的次数来的，所以使用对象字面量创建的对象无法利用其提高空间利用率，这也侧面说明了上文提到的空字面量的创建，默认预分配的是 4 个而不像构造函数创建那样预留 8 个（因为无法利用 slack tracking 后续提高空间利用率，所以只能在开始的时候就节流）</p>
<p>可以通过 <a href="https://v8.dev/blog/slack-tracking" target="_blank" rel="nofollow noopener noreferrer">Slack tracking in V8</a> 进一步了解其实现的细节</p>
<h2 data-id="heading-16">小结</h2>
<p>我们可以将上文的重点部分小结如下：</p>
<ul>
<li>对象的属性有三种模式：inobject，fast，slow</li>
<li>三种模式的属性访问效率由左往右递减</li>
<li>属性默认使用 inobject 型，超过预留配额后，继续添加的属性属于 fast 型</li>
<li>当继续超过 fast 型的配额后，对象整个切换到 slow 型</li>
<li>初始 inobject 的配额会因为使用的是「构造函数创建」还是「对象字面量」创建而不同，前者根据编译器收集的信息（大致属性数 + 8，且上限为 252），后者是固定的 4</li>
<li>使用 <code>Object.create(null)</code> 创建的对象直接是 slow 型</li>
<li>对于任意对象 A，在其声明周期内，使用 <code>delete</code> 删除了除最后顺位以外的其余顺位的属性，或者将 A 设置为另一个构造函数的 <code>prototype</code> 属性，都会将对象 A 整个切换为 slow 型</li>
<li>目前来看，切换到 slow 型后将不能再回到 fast 型</li>
</ul>
<p>在实际使用时，我们不必考虑上面的细节，只要确保在有条件的情况下：</p>
<ul>
<li>尽可能使用构造函数的方式创建对象，换句话说是尽可能的减少属性的动态创建。实际上，像这样尽可能让 JS 代码体现出更多的静态性，是迎合引擎内部优化方式以获得更优性能的核心原则，同样的操作包括尽可能的保持变量的类型始终唯一、以避免 JIT 失效等</li>
<li>如果需要大量的动态添加属性，或者需要删除属性，直接使用 Map 对象会更好（虽然引擎内部也会自动切换，但是直接用 Map 更符合这样的场景，也省去了内部切换的消耗）</li>
</ul>
<p>本文简单结合源码介绍了一下 v8 中是如何处理对象的，希望可以有幸作为大家深入了解 v8 内存管理的初始读物</p>
<h2 data-id="heading-17">参考资料</h2>
<ul>
<li><a href="https://item.jd.com/12010270.html" target="_blank" rel="nofollow noopener noreferrer">垃圾回收的算法与实现</a></li>
<li><a href="https://www.jayconrod.com/posts/52/a-tour-of-v8--object-representation" target="_blank" rel="nofollow noopener noreferrer">A tour of V8: object representation</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/55903492" target="_blank" rel="nofollow noopener noreferrer">V8 引擎 JSObject 结构解析和内存优化思路</a></li>
<li><a href="https://v8.dev/blog/fast-properties" target="_blank" rel="nofollow noopener noreferrer">Fast properties in V8</a></li>
<li><a href="https://v8.dev/blog/pointer-compression" target="_blank" rel="nofollow noopener noreferrer">Pointer Compression in V8</a></li>
<li><a href="https://v8.dev/blog/slack-tracking" target="_blank" rel="nofollow noopener noreferrer">Slack tracking in V8</a></li>
</ul>
<blockquote>
<p>本文发布自 <a href="https://github.com/x-orpheus" target="_blank" rel="nofollow noopener noreferrer">网易云音乐大前端团队</a>，文章未经授权禁止任何形式的转载。我们常年招收前端、iOS、Android，如果你准备换工作，又恰好喜欢云音乐，那就加入我们 grp.music-fe (at) corp.netease.com！</p>
</blockquote></div>  
</div>
            