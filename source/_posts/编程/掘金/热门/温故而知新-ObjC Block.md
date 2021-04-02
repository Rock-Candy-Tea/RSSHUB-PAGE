
---
title: '温故而知新-ObjC Block'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141d8b9133734be79d596ef8caee7711~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 18 Mar 2021 07:24:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141d8b9133734be79d596ef8caee7711~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Block</h1>
<h2 data-id="heading-1">简介</h2>
<p>本文主要是回答以下几个问题：</p>
<ol>
<li>Block 是什么？</li>
<li>Block 不同的类型出现场景是什么？又分别存储在哪？</li>
<li>截获的变量是如何存储的？</li>
<li>如何解决循环引用问题？</li>
</ol>
<p>简洁版的回答：</p>
<ol>
<li>Block 又称为匿名函数，本质是一个 ObjC 对象，其结构体里会有一个指针指向具体的函数实现。</li>
<li>它有 3 种类型，分别存储在静态数据区、栈区、堆区。</li>
<li>截获的变量会直接拷贝到 Block 结构体里，或捕捞其指针。</li>
<li>一般可使用 weak 和 __block 修饰符来解决循环引用问题。</li>
</ol>
<p>接下来针对每个答案进行详细阐述。</p>
<h2 data-id="heading-2">Block 是什么？</h2>
<p>一句话描述：能捕捞局部变量的匿名函数。</p>
<p>但内部实现是怎样的呢？</p>
<p>先写一个简单的 Block</p>
<pre><code class="hljs language-ObjC copyable" lang="ObjC"><span class="hljs-meta">#import <span class="hljs-meta-string"><Foundation/Foundation.h></span></span>

<span class="hljs-keyword">int</span> main() &#123;
    <span class="hljs-keyword">void</span> (^blk)(<span class="hljs-keyword">void</span>) = ^&#123; printf(<span class="hljs-string">"BLOCK\n"</span>); &#125;;
    blk();
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再使用 clang 转换成 c++</p>
<pre><code class="hljs language-sh copyable" lang="sh">clang -rewrite-objc xx.m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到结果的关键代码如下：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_impl_0</span> &#123;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">block_impl</span> <span class="hljs-title">impl</span>;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_desc_0</span>* <span class="hljs-title">Desc</span>;</span>
  __main_block_impl_0(<span class="hljs-keyword">void</span> *fp, struct __main_block_desc_0 *desc, <span class="hljs-keyword">int</span> flags=<span class="hljs-number">0</span>) &#123;
    impl.isa = &_NSConcreteStackBlock;
    impl.Flags = flags;
    impl.FuncPtr = fp;
    Desc = desc;
  &#125;
&#125;;

<span class="hljs-comment">// 源码中的 ^&#123;printf("BLOCK\n",);&#125; 转换成以下代码</span>
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> __main_block_func_0(struct __main_block_impl_0 *__cself) &#123;
  <span class="hljs-built_in">printf</span>(<span class="hljs-string">"BLOCK\n"</span>);
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_desc_0</span> &#123;</span>
  <span class="hljs-keyword">size_t</span> reserved;
  <span class="hljs-keyword">size_t</span> Block_size;
&#125; __main_block_desc_0_DATA = &#123;<span class="hljs-number">0</span>, <span class="hljs-keyword">sizeof</span>(struct __main_block_impl_0)&#125;;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">void</span> (*blk)(<span class="hljs-keyword">void</span>) = ((<span class="hljs-keyword">void</span> (*)())&__main_block_impl_0((<span class="hljs-keyword">void</span> *)__main_block_func_0, &__main_block_desc_0_DATA));
    ((<span class="hljs-keyword">void</span> (*)(__block_impl *))((__block_impl *)blk)->FuncPtr)((__block_impl *)blk);
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再除去构造函数，Block 就变成：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// Block</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_impl_0</span> &#123;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">block_impl</span> <span class="hljs-title">impl</span>;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_desc_0</span>* <span class="hljs-title">Desc</span>;</span>
&#125;;

<span class="hljs-comment">// __block_impl 的声明</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">block_impl</span> &#123;</span>
  <span class="hljs-keyword">void</span> *isa;
  <span class="hljs-keyword">int</span> Flags; <span class="hljs-comment">// 按 bit 保留表示一些 block 附加信息</span>
  <span class="hljs-keyword">int</span> Reserved; <span class="hljs-comment">// 保留变量</span>
  <span class="hljs-keyword">void</span> *FuncPtr;
&#125;;

<span class="hljs-comment">// __main_block_desc_0 的声明</span>
<span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_desc_0</span> &#123;</span>
  <span class="hljs-keyword">size_t</span> reserved;
  <span class="hljs-keyword">size_t</span> Block_size;
&#125; __main_block_desc_0_DATA = &#123;<span class="hljs-number">0</span>, <span class="hljs-keyword">sizeof</span>(struct __main_block_impl_0)&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比一下 ObjC 对象的声明，不难发现 Block 本质也是一种 ObjC 对象。</p>
<p>因为它也有那标志性的 isa 指针。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// Objective-C 对象的声明</span>
<span class="hljs-comment">// id 为 objc_object 结构体的指针类型</span>
<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">objc_object</span> &#123;</span>
  Class isa;
&#125; *id;
<span class="hljs-comment">// Class 为 objc_class 结构体的指针类型</span>
<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">objc_class</span> *<span class="hljs-title">Class</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">objc_class</span> &#123;</span>
  Class *isa;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Block 的 3 种类型</h2>
<p>Block 的 isa 指向是这 3 个类之一，其实从名字上也可以看出各自存储的区域。</p>
<ul>
<li><code>__NSStackBlock__</code> 存储在栈上</li>
<li><code>__NSGlobalBlock__</code> 存储在静态数据区</li>
<li><code>__NSMallocBlock__</code> 堆上</li>
</ul>
<p>各种类型出现的场景如下：</p>
<pre><code class="hljs language-Objective-C copyable" lang="Objective-C">int e = 3;
void (^block)() = ^&#123;
    printf("%c\n", e);
&#125;;

NSLog(@"%@", [block class]); // __NSMallocBlock__
NSLog(@"%@", [^&#123; printf("%c\n", e); &#125; class]); // __NSStackBlock__
NSLog(@"%@", [^&#123; int a = 4; printf("%c\n", a); &#125; class]); // __NSGlobalBlock__
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单理解，未截获变量是 <code>__NSGlobalBlock__</code> 。</p>
<p>若截获了变量，则是 <code>__NSStackBlock__</code>，但它却很容易被复制到堆上。</p>
<p>比如以下情况：</p>
<ul>
<li>当对 Block 对象调用 copy 时。</li>
<li>当 Block 作为返回值返回时。(前提是 ARC 环境)</li>
<li>当 Block 赋值给 strong 对象时。</li>
<li>在方法名中含有 usingBlock 的 Cocoa 框架方法或 GCD 的 API 中传递 Block 时。</li>
</ul>


<p>有时也需要手动添加 copy 方法，来将 block 添加到堆上。</p>
<p>根据不同的 Block，copy 会有不同效果：</p>

























<table><thead><tr><th>Block 类</th><th>副本源的配置存储域</th><th>复制效果</th></tr></thead><tbody><tr><td>_NSConcreteStackBlock</td><td>栈</td><td>从栈复制到堆</td></tr><tr><td>_NSConcreteGlobalBlock</td><td>程序的数据区域</td><td>Nothing</td></tr><tr><td>_NSConcreteMallocBlock</td><td>堆</td><td>引用计数增加</td></tr></tbody></table>
<h2 data-id="heading-4">截获的变量是如何存储的？</h2>
<p>截获的变量会被添加到 <code>__main_block_impl_0</code> 结构体中。</p>
<p>大概就是这样子：</p>





























<table><thead><tr><th>__block_impl</th></tr></thead><tbody><tr><td>isa *</td></tr><tr><td>Flags</td></tr><tr><td>Reserved</td></tr><tr><td>FuncPtr</td></tr><tr><td>截获的变量 1</td></tr><tr><td>截获的变量 2</td></tr><tr><td>...</td></tr></tbody></table>
<p>转换后的代码：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">int</span> count = <span class="hljs-number">3</span>;

    <span class="hljs-keyword">void</span> (*blk)(<span class="hljs-keyword">void</span>) = ((<span class="hljs-keyword">void</span> (*)())&__main_block_impl_0((<span class="hljs-keyword">void</span> *)__main_block_func_0, &__main_block_desc_0_DATA, count));
    ((<span class="hljs-keyword">void</span> (*)(__block_impl *))((__block_impl *)blk)->FuncPtr)((__block_impl *)blk);
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_impl_0</span> &#123;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">block_impl</span> <span class="hljs-title">impl</span>;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> __<span class="hljs-title">main_block_desc_0</span>* <span class="hljs-title">Desc</span>;</span>

  <span class="hljs-keyword">int</span> count; <span class="hljs-comment">// 使用的自动变量被作为成员变量追加到结构体中</span>

  __main_block_impl_0(<span class="hljs-keyword">void</span> *fp, struct __main_block_desc_0 *desc, <span class="hljs-keyword">int</span> _count, <span class="hljs-keyword">int</span> flags=<span class="hljs-number">0</span>) : count(_count) &#123;
    impl.isa = &_NSConcreteStackBlock;
    impl.Flags = flags;
    impl.FuncPtr = fp;
    Desc = desc;
  &#125;
&#125;;

<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> __main_block_func_0(struct __main_block_impl_0 *__cself) &#123;
  <span class="hljs-keyword">int</span> count = __cself->count; <span class="hljs-comment">// bound by copy</span>
  <span class="hljs-built_in">printf</span>(<span class="hljs-string">"BLOCK%d\n"</span>, count);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">__block 说明符</h3>
<p>添加__block 之后，数据若改变了，执行 block 也会打印出最新的数据：</p>
<p>没有添加 __block</p>
<pre><code class="hljs language-Objective-C copyable" lang="Objective-C">int n = 3;
void (^block2)() = ^&#123;
    NSLog(@"%d", n);
&#125;;
n = 4;
block2(); // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加了__block，会捕获变量的指针。</p>
<p>所以数值改变了，block 执行时，也能看到改变后的数据。</p>
<pre><code class="hljs language-Objective-C copyable" lang="Objective-C">__block int n = 3;
void (^block2)() = ^&#123;
    NSLog(@"%d", n);
&#125;;
n = 4;
block2(); // 4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的可以看看，转换后的代码。</p>
<p>增加的 <code>__Block_byref_count_0</code> 结构体里就捕获了变量的指针（__forwarding）。</p>
<pre><code class="hljs language-Objective-C copyable" lang="Objective-C">int main() &#123;
    __attribute__((__blocks__(byref))) __Block_byref_count_0 count = &#123;(void*)0,(__Block_byref_count_0 *)&count, 0, sizeof(__Block_byref_count_0), 3&#125;;
    void (*blk)(void) = ((void (*)())&__main_block_impl_0((void *)__main_block_func_0, &__main_block_desc_0_DATA, (__Block_byref_count_0 *)&count, 570425344));
    ((void (*)(__block_impl *))((__block_impl *)blk)->FuncPtr)((__block_impl *)blk);
    return 0;
&#125;

// 不在 __main_block_impl_0 中声明的原因是，这样可以在多个 block 中使用
struct __Block_byref_count_0 &#123;
  void *__isa;
  __Block_byref_count_0 *__forwarding;
  int __flags;
  int __size;
  int count;
&#125;;

struct __main_block_impl_0 &#123;
  struct __block_impl impl;
  struct __main_block_desc_0* Desc;

  __Block_byref_count_0 *count; // by ref

  ...
&#125;

static void __main_block_func_0(struct __main_block_impl_0 *__cself) &#123;
  __Block_byref_count_0 *count = __cself->count; // bound by ref
    (count->__forwarding->count) = 2;
    printf("BLOCK%d\n", (count->__forwarding->count));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>

<h3 data-id="heading-6">__forwarding</h3>
<p><code>__forwarding</code> 是添加 __block 后的关键实现。</p>
<p>（为方便叙述，以下将 <code>__forwarding</code> 变量用 f 代替）</p>
<p>当 __block 变量在栈上时，f 指向自己本身的指针。</p>
<p>当 __block 变量复制到堆上时，f 会被复制到堆上，假设为 fm。</p>
<p>此时栈上的 f 会变成指向堆上的 __block 变量，而 fm 也指向堆上本身的指针。即 f 和 fm 指向同个指针。</p>
<p>所以使用 <code>__forwarding</code> 变量，可以在以下几种情况下，访问到同个变量：</p>
<ul>
<li>Block 中使用</li>
<li>Block 外使用</li>
<li>变量在栈上或堆上</li>
</ul>
<h2 data-id="heading-7">如何解决 Block 循环引用问题</h2>
<p>使用 Block 容易引起循环引用，主要通过修饰符 __weak 和 __block 避免。</p>
<p>__weak 比较常见，不再赘述。</p>
<p>使用 __block 的主要优点：</p>
<p>可自由控制将变量转为 nil 的时机</p>
<p>使用 __block 的主要缺点：</p>
<p>必须执行 Block，并在 Block 中，将变量置为 nil，才能避免循环引用。</p>
<h2 data-id="heading-8">疑问</h2>
<p>以下是笔者在整理这篇文章时，仍有疑惑的地方，若有读者知道，麻烦告知一声。</p>
<h3 data-id="heading-9">为什么以下代码，打印出来的类型不同？</h3>
<pre><code class="hljs language-Objective-C copyable" lang="Objective-C">int e = 3;
NSLog(@"%@", ^&#123; printf("%c\n", e); &#125;); // <__NSMallocBlock__: 0x10046b050>
NSLog(@"%@", [^&#123; printf("%c\n", e); &#125; class]); // __NSStackBlock__
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下分析汇编代码的思路来源于 <a href="https://juejin.cn/user/1626932938803534/activities" target="_blank">哈就是我26593</a></p>
<p>可以看到前一行代码，会调用 <code>objc_retainBlock()</code>，而后者并没有看到相关操作。</p>
<p><img alt="20210329-2209.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141d8b9133734be79d596ef8caee7711~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="20210329-2211.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4661acdcf7774d9f89e3ac712bbe225a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根据 <a href="https://clang.llvm.org/docs/AutomaticReferenceCounting.html#arc-runtime-objc-retainblock" target="_blank" rel="nofollow noopener noreferrer">objc_retainBlock — Clang 12 documentation</a> 的解释，该函数会 copy 栈上的 block 到堆上。</p>
<p>至于为什么要调用它，评论区已有几位大佬给出见解，但笔者仍未找到佐证的资料😂。</p>
<h3 data-id="heading-10">那为什么要将栈上的 block 复制到堆上呢？</h3>
<p>个人理解是，它被堆上的对象「所需要了」，也就是说，需要控制其被销毁的时机了，所以复制到堆上是为了便于管理。</p>
<h2 data-id="heading-11">感谢</h2>
<p><a href="https://www.zybuluo.com/MicroCai/note/49713" target="_blank" rel="nofollow noopener noreferrer">Block 小测验</a></p>
<p><a href="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502" target="_blank" rel="nofollow noopener noreferrer">苹果官方文档</a></p>
<p><a href="https://blog.devtang.com/2013/07/28/a-look-inside-blocks/" target="_blank" rel="nofollow noopener noreferrer">谈 Objective-C block 的实现 · 唐巧的博客</a></p>
<p><a href="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502" target="_blank" rel="nofollow noopener noreferrer">Block Programming Topics</a></p>
<p><a href="http://clang.llvm.org/docs/Block-ABI-Apple.html" target="_blank" rel="nofollow noopener noreferrer">Block Implementation Specification — Clang 12 documentation</a></p>
<p><a href="https://www.jianshu.com/p/03ad4b2ecedf" target="_blank" rel="nofollow noopener noreferrer">ARC 下 NSStackBlock 去哪了 - 简书</a></p>
<p><a href="https://www.jianshu.com/p/5db1579c5454" target="_blank" rel="nofollow noopener noreferrer">Block 里面的 weak-strong 理解 - 简书</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            