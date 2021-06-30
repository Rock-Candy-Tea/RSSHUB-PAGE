
---
title: 'IOS 底层原理之 alloc 探究'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea751dda063c4763b5d78e65d36a9be5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 00:22:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea751dda063c4763b5d78e65d36a9be5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>作为一名iOS程序员，我们每天基本上都在<code>alloc</code>，但是<code>alloc</code>底层做了什么，我们并不知道。今天就探索下<code>alloc</code>底层流程。在探究之前，我们先做个简单的小测试（不要急，一步一步来）。下面分别输出对象的内容，对象的地址，以及对象指针的地址代码和打印如下：</p>
<pre><code class="copyable">    LWPerson * obj = [LWPerson alloc];
    LWPerson * obj1 = [obj init];
    LWPerson * obj2 = [obj init];
    
    LWPerson * newObj = [LWPerson alloc];
 
    NSLog(@"%@---%p--%p",obj,obj,&obj);
    NSLog(@"%@---%p--%p",obj1,obj1,&obj1);
    NSLog(@"%@---%p--%p",obj2,obj2,&obj2);
    NSLog(@"%@---%p--%p",newObj,newObj,&newObj);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    <LWPerson: 0x281404710>---0x281404710--0x16b5cdbe8
    <LWPerson: 0x281404710>---0x281404710--0x16b5cdbe0
    <LWPerson: 0x281404710>---0x281404710--0x16b5cdbd8
    <LWPerson: 0x281404740>---0x281404740--0x16b5cdbd0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>探究分析得出结论</p>
<ul>
<li><code>obj</code>、<code>obj1</code>、<code>obj2</code> 打印的内容，对象的地址是一样的，但是指针的地址是不一样的。</li>
<li><code>newObj</code> 和 <code>obj</code>、<code>obj1</code>、<code>obj2</code> 打印的内容，对象的地址，指针的地址是不一样的。</li>
</ul>
<p>问题：到底是为什么呢？原因如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea751dda063c4763b5d78e65d36a9be5~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>总结：</p>
<ul>
<li><code>alloc</code>具有开辟一块内存功能，而<code>init</code>没有开辟内存的功能。</li>
<li><code>栈区</code>开辟的内存是<code>高</code>地址到<code>低</code>地址，<code>堆区</code>则是<code>低</code>地址到<code>高</code>地址。</li>
</ul>
</blockquote>
<p>下面我们要探究的内容是在初始化对象时，alloc到底做了什么？</p>
<h1 data-id="heading-1">准备工作</h1>
<ol>
<li>下载源码 <a href="https://opensource.apple.com/tarballs/objc4/" target="_blank" rel="nofollow noopener noreferrer">objc4-818.2</a></li>
<li>编译源码（后续补上）</li>
</ol>
<h1 data-id="heading-2">三种探索底层的方法</h1>
<p>问题：我们想探索<code>alloc</code>的流程，但是发现 xcode 并没有提供<code>alloc</code>的具体实现，那么到底该从哪里入手呢，探索的思维很重要，勇敢的跨出第一步吧，那么下面提供三种探索底层的方法。</p>
<h2 data-id="heading-3">1. 符号断点</h2>
<p>在需要调试的位置打上断点，当断点断住的时候按住<code>control</code>键，然后<code>step into</code> 进入下一步，然后在汇编里面找到方法，然后给这个方法添加符号断点。具体流程如下图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2051013e7f064f7f86c49d4c5ad3c0b9~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2. 汇编（yysd-永远的神）</h2>
<p>当断点断住的时候，<code>Xcode</code> -> <code>Debug</code> -> <code>Debug Workflow</code> -> <code>Always Show Disassembly</code> 进入汇编找到跳转的方法，此时有两种方式，一种找到方法直接添加断点调试。另一种就是断住跳转的地方，按住<code>control</code>键，然后<code>step into</code> 进入下一步，这种<code>stp into</code> 可以一直走，只不过中间过程比较繁琐，如果嫌弃麻烦在你想放弃的时候，此时打一个符号断点。具体流程如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6d5cd25d1ff4da2ba5ef48b6f048f66~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">3. 符号断点，断住位置</h2>
<p>在探究哪个的方法就直接给方法添加符号断点，比如我们探究<code>alloc</code>方法就直接给<code>alloc</code>添加符号断点，没有其他乱七八糟，就是暴力（注意：这个断点在你需要断住的地方，然后再激活，不然可能项目运行的时候很多地方都会调用，你会爆炸的）。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61f977dbb7154c04a81b9d52c37b9731~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">编译源码</h1>
<p>上面说的三种方法，比较繁琐，特别是流程比较深，嵌套比较复杂，人会受不了的。那么现在有没有一种比较丝滑，自然的方法呢？既然这么问了，那是必须有的嘛。 我们已经知道 <code>objc_alloc</code> 是属于<code>libobjc</code>库的，那么我们就把苹果提供给我们的 <code>objc</code> 源码编译成工程跑起来，这种是我们比较舒服的。上面的准备工作已经准备好了，下面我们就一起探索吧。</p>
<h1 data-id="heading-7">alloc源码探索</h1>
<p>根据源码工程，点击进入<code>alloc</code>， 流程图如下
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d609160ace5c42ea9524db5ea64f2f5e~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
探索流程如下断点进入 <code>alloc</code></p>
<pre><code class="copyable">+ (id)alloc &#123;
    return _objc_rootAlloc(self);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>_objc_rootAlloc</code></p>
<pre><code class="copyable">id _objc_rootAlloc(Class cls)
&#123;
    return callAlloc(cls, false/*checkNil*/, true/*allocWithZone*/);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>callAlloc</code></p>
<pre><code class="copyable">static ALWAYS_INLINE id
callAlloc(Class cls, bool checkNil, bool allocWithZone=false)
&#123;
#if __OBJC2__ //判断是不是 objc2.0版本
    //slowpath(x):x很可能为假，为真的概率很小 
    //fastpath(x):x很可能为真 
    //其实将fastpath和slowpath去掉是完全不影响任何功能,写上是告诉编译器对代码进行优化
    if (slowpath(checkNil && !cls)) return nil;
    //判断该类是否实现自自定义的 +allocWithZone，没有则进入if条件句
    if (fastpath(!cls->ISA()->hasCustomAWZ())) &#123;
        return _objc_rootAllocWithZone(cls, nil);
    &#125;
#endif

    // No shortcuts available.
    if (allocWithZone) &#123;
        return ((id(*)(id, SEL, struct _NSZone *))objc_msgSend)(cls, @selector(allocWithZone:), nil);
    &#125;
    return ((id(*)(id, SEL))objc_msgSend)(cls, @selector(alloc));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>_objc_rootAllocWithZone</code></p>
<pre><code class="copyable">id
_objc_rootAllocWithZone(Class cls, malloc_zone_t *zone __unused)
&#123;
    // allocWithZone under __OBJC2__ ignores the zone parameter
    return _class_createInstanceFromZone(cls, 0, nil,
                                         OBJECT_CONSTRUCT_CALL_BADALLOC);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时走入真正的核心代码，断点进入 <code>_class_createInstanceFromZone</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c015247c426f478795c79e82a06d1ce4~tplv-k3u1fbpfcp-watermark.image" alt="static ALWAYS INLINE id.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从流程图和源代码可以看出 <code>_class_createInstanceFromZone</code> 方法中有核心三个方法需要实现</p>
<ul>
<li><code>cls->instanceSize</code> ： 计算内存大小</li>
<li><code>(id)calloc(1, size)</code> ： 开辟内存，返回地址指针</li>
<li><code>obj->initInstanceIsa</code> ：初始化指针，和类关联起来</li>
</ul>
<p>下面就对这三个方法重点分析</p>
<h3 data-id="heading-8"><code>instanceSize</code>：计算内存大小</h3>
<p>断点进入 <code>instanceSize</code></p>
<pre><code class="copyable">inline size_t instanceSize(size_t extraBytes) const &#123;
        //快速计算内存大小
        if (fastpath(cache.hasFastInstanceSize(extraBytes))) &#123;
            return cache.fastInstanceSize(extraBytes);
        &#125;
        //计算类中所有变量需要的内存大小   extraBytes额外字节数一般是0
        size_t size = alignedInstanceSize() + extraBytes;
        // CF requires all objects be at least 16 bytes.
        //最小返回16字节
        if (size < 16) size = 16;  
        return size;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>cache.fastInstanceSize</code></p>
<pre><code class="copyable">size_t fastInstanceSize(size_t extra) const
    &#123;
        ASSERT(hasFastInstanceSize(extra));

        if (__builtin_constant_p(extra) && extra == 0) &#123;
            return _flags & FAST_CACHE_ALLOC_MASK16;
        &#125; else &#123;
            size_t size = _flags & FAST_CACHE_ALLOC_MASK;
            // remove the FAST_CACHE_ALLOC_DELTA16 that was added
            // by setFastInstanceSize
            return align16(size + extra - FAST_CACHE_ALLOC_DELTA16);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>align16</code> (16字节对齐)</p>
<pre><code class="copyable">static inline size_t align16(size_t x) &#123;
    return (x + size_t(15)) & ~size_t(15);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们探究下 <code>align16</code> 方法的具体实现 已 <code>align16(10)</code>为例</p>
<blockquote>
<p>x = 10             (x + size_t(15)) & ~size_t(15)   <code>~</code>(取反)<br>
10 + 15 = 25       <code>0001 1001</code><br>
15                 <code>0000 1111 </code><br>
~15                <code>1111 0000</code><br>
25 & ~15           <code>0001 1001</code> & <code>1111 0000</code><br>
结果：<code>0001 0000</code>     <code>16 </code></p>
</blockquote>
<p>总结：<code>align16</code> 算法实际上就是取16的整数倍。我认为是向下取整，理由我是站在纯算法的角度，<code>(x + 15)</code>是<code>16</code>的<code>几倍</code>，超过的部分抹去。例如 <code>(20 + 15) = 35 = 16 *  2 + 3</code>，结果是<code>32</code>。这种算法和 <code>>> 4 << 4</code> 是一样的，得出的结果就是<code>16</code>的倍数，不足<code>16</code>的全部抹去。</p>
<p>为什么需要<code>16</code>字节对齐</p>
<ul>
<li><code>cpu</code> 读取数据是以固定字节块来读取的，这是一个用空间换取时间的做法，如果频繁的读取字节未对齐的数据，降低了<code>cpu</code>的性能和读取速度。</li>
<li>更安全 由于在一个对象中<code>isa</code>指针是占<code>8</code>个字节，如果不进行节对齐 ，对象之间就会紧挨着，容易造成访问混乱。<code>16</code>字节对齐，会预留部分空间，访问更安全</li>
</ul>
<h3 data-id="heading-9"><code>calloc</code>：开辟内存，返回地址指针</h3>
<p>首先由 <code>instanceSize</code> 方法 计算出需要的内存大小，然后向系统申请 <code>size</code> 大小的内存，返回给<code>objc</code>，因此<code>objc</code>是指向内存地址的指针，下面我们通过断点打印的方法来验证下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa68c6b943c34ba8b74c114a00406de5~tplv-k3u1fbpfcp-watermark.image" alt="id obj.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，<code>obj</code>还没有进行赋值，此时有地址值，说明系统给他分配了一块脏地址</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cb08f28bcd848a3aba58130f629a312~tplv-k3u1fbpfcp-watermark.image" alt="if (slowpath(!obj)) &#123;.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行<code>calloc</code>后打印的是一个<code>16进制</code>的指针地址，说明已经开辟了内存，但是和平常见到的地址指针<code>(<LWPerson: 0x100726d00>)</code>不一样，为什么呢？</p>
<ul>
<li><code>obj</code>没有和<code>cls</code>进行关联绑定</li>
<li>同时验证了<code>calloc</code>只是开辟了内存</li>
</ul>
<h3 data-id="heading-10"><code>initInstanceIsa</code>：初始化指针 ，和类关联起来</h3>
<p>断点进入 <code>initInstanceIsa</code></p>
<pre><code class="copyable">inline void 
objc_object::initInstanceIsa(Class cls, bool hasCxxDtor)
&#123;
    ASSERT(!cls->instancesRequireRawIsa());
    ASSERT(hasCxxDtor == cls->hasCxxDtor());

    initIsa(cls, true, hasCxxDtor);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>具体的 <code>isa</code> 结构和源码探究，会在后面单独发文</p>
</blockquote>
<p>在<code>isa</code>指针初始化以后，打印<code>objc</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18712a3b99246ccb6c8b3b77076c2c7~tplv-k3u1fbpfcp-watermark.image" alt="return _objc_cal1BadAllocHandler();.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中打印结果：指针已经与类进行了关联，<code>alloc</code>探索也完成了。</p>
<h1 data-id="heading-11"><code>init</code>探究</h1>
<pre><code class="copyable">- (id)init &#123;
    return _objc_rootInit(self);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点进入 <code>_objc_rootInit</code></p>
<pre><code class="copyable">id
_objc_rootInit(id obj)
&#123;
    // In practice, it will be hard to rely on this function.
    // Many classes do not properly chain -init calls.
    return obj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>init</code>方法返回的是对象本身</li>
<li><code>init</code>可以提供给开发者更多的自由去自定义 ，通过<code>id</code>实现强转，返回我们需要的类型</li>
</ul>
<h1 data-id="heading-12"><code>new</code>探究</h1>
<pre><code class="copyable">+ (id)new &#123;
    return [callAlloc(self, false/*checkNil*/) init];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码显示 走了<code>callAlloc</code>的方法流程，然后走了<code>init</code>方法 ，所以 <code>new</code>看做是<code>alloc</code> + <code>init</code></p>
<h1 data-id="heading-13">总结</h1>
<p><code>alloc</code> 的核心作用就是开辟内存，通过<code>isa</code>指针与类进行关联，<code>init</code>方法，提供开发者更多的自由，<code>new</code> 是对<code>(alloc+init)</code>进行了封装，无法在初始化的时候添加其它的需求。</p></div>  
</div>
            