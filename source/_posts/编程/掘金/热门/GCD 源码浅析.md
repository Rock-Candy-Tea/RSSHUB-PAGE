
---
title: 'GCD 源码浅析'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1122c57ec9e4f52a136bd1a71526119~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 18:51:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1122c57ec9e4f52a136bd1a71526119~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在iOS开发、面试时，是否对同步、异步、串行队列和并行队列的名词迷惑不解？当这些名词组合起来，同步串行队列，异步串行队列，同步并行队列以及异步并行队列，是否对这些情况在运行时的表现含糊不清，本文试着从源码的角度，来理清它们之间的差异，在开发面试中，更好的掌握gcd接口的用法。</p>
<h2 data-id="heading-0">1.数据结构</h2>
<h3 data-id="heading-1">dispatch_queue_t</h3>
<p><code>dispatch_queue_t</code>是指向<code>dispatch_queue_s</code>的指针。通过代码对<code>dispatch_queue_t</code>的声明，在OC的语言环境中我们可以得到如下的展开。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_DECL(dispatch_queue);

<span class="hljs-comment">// 最终展开如下</span>
@protocol OS_dispatch_queue <OS_dispatch_object>
@end
<span class="hljs-keyword">typedef</span> NSObject<OS_dispatch_queue> * __attribute__((objc_independent_class)) <span class="hljs-keyword">dispatch_queue_t</span>

<span class="hljs-comment">// OS_dispatch_object是由以下的宏定义</span>
OS_OBJECT_DECL_CLASS(dispatch_object);
<span class="hljs-comment">// 最终展开如下</span>
@protocol OS_dispatch_object <NSObject>
@end
<span class="hljs-keyword">typedef</span> NSObject<OS_dispatch_object> * __attribute__((objc_independent_class)) <span class="hljs-keyword">dispatch_object_t</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>OS_dispatch_queue</code>的作用是什么呢？这只是OC中的一个虚拟类，我们可以创建一个Demo工程，创建一个队列，在Demo工程中通过断点查看创建队列所返回的<code>dispatch_queue_t</code>指针，可以看到对应的OC类是<code>OS_dispatch_queue</code>，并且没有任何的成员变量。我们在分配该类的时候，是通过calloc，按照<code>dispatch_queue_s</code>的结构分配的。所以我们可以对分配的对象按照<code>dispatch_queue_s</code>结构赋值，改变。也就是<code>dispatch_queue_s</code>和<code>OS_dispatch_queue</code>是同一种对象的两种标识。有点类似toll-free bridge。当然和toll-free bridge的桥接类并不完全相同，两个类的方法和函数并不能互操作。这个类的isa指向的是<code>dispatch_queue_vtable_s</code>结构。描述这个队列进行一些操作需要调用的函数地址。</p>
<h3 data-id="heading-2">GCD中常见的结构和继承关系</h3>
<p>在<code>queue_internal</code>头文件中有注释说明了，下面两图分别是API使用者常使用的结构体和gcd源码内部使用的结构体的继承关系的图示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1122c57ec9e4f52a136bd1a71526119~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="dispatch-queue-create.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce601ffabe2148e2bc10cbeee314d184~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="dispatch-queue-create.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图1可以看到，我们常用的<code>dispatch_queue_serial_t</code>，<code>dispatch_queue_global_t</code>，<code>dispatch_queue_concurrent_t</code>都是继承于<code>dispatch_queue_t</code>，而主队列<code>dispatch_queue_main_t</code>是继承<code>dispatch_queue_serial_t</code>。因此我们熟知的主队列是串行队列这个结论从这里可以得到印证。</p>
<p>这里说明一下以<code>_t</code>，<code>_class_t</code>，<code>_s</code>结尾类型之间的关系，<code>_t</code>是一个指针类型，指向的结构对应<code>_s</code>的一种，<code>_class_t</code>是一个union类型，表示其指向的结构体可能是多个<code>_s</code>的其中一种，主要用于多种结构体之间的转换。</p>
<p>或许会有疑问C语言怎么来建立这种继承的关系呢？通过源码我们可以看到，GCD通过struct声明了这些结构，只是在声明各个结构体的时候通过一层层的宏定义，强制两个有继承关系的结构体声明一套相同的成员变量，这也增加了读代码的难度，获得一个结构的声明，就要颇费一番功夫。</p>
<p>还有一点就是如何在基类和子类之间转换呢？gcd中采用的是union这个结构，定义指针可能指向的类型，这里只是一个粗糙的面对对象的实现，在指针转换的时候还是需要注意的。这种结构体类型之间的转换是不安全的，也没有编译器帮助我们发现问题。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">union</span> &#123;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> _<span class="hljs-title">os_object_s</span> *_<span class="hljs-title">os_obj</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_object_s</span> *_<span class="hljs-title">do</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_s</span> *_<span class="hljs-title">dq</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_attr_s</span> *_<span class="hljs-title">dqa</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_group_s</span> *_<span class="hljs-title">dg</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_source_s</span> *_<span class="hljs-title">ds</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_mach_s</span> *_<span class="hljs-title">dm</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_mach_msg_s</span> *_<span class="hljs-title">dmsg</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_semaphore_s</span> *_<span class="hljs-title">dsema</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_data_s</span> *_<span class="hljs-title">ddata</span>;</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_io_s</span> *_<span class="hljs-title">dchannel</span>;</span>
&#125; <span class="hljs-keyword">dispatch_object_t</span> DISPATCH_TRANSPARENT_UNION;
 <span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_s</span> *<span class="hljs-title">dispatch_queue_t</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这里声明了<code>dispatch_object_t</code>为一个联合体，成员是里面这些类型指针的一种。其实这也就和上面面对对象中的基类的概念相似，union中每个结构体指针都是其中一种"子类"的类型。
所以面对对象的编程和编程语言没有必然的关系，用C语言也可以写成优秀的面对对象的代码。
下面我们看下<code>dispatch_queue_s</code>的声明</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_s</span> &#123;</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_object_s</span> _<span class="hljs-title">as_do</span>[0];</span>
  <span class="hljs-class"><span class="hljs-keyword">struct</span> _<span class="hljs-title">os_object_s</span> _<span class="hljs-title">as_os_obj</span>[0];</span>
  <span class="hljs-keyword">const</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_vtable_s</span> *<span class="hljs-title">do_vtable</span>;</span>
  <span class="hljs-keyword">int</span> <span class="hljs-keyword">volatile</span> do_ref_cnt;
   <span class="hljs-keyword">int</span> <span class="hljs-keyword">volatile</span> do_xref_cnt;
   <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_s</span> *<span class="hljs-title">volatile</span> <span class="hljs-title">do_next</span>;</span>
   <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_s</span> *<span class="hljs-title">do_targetq</span>;</span>
   <span class="hljs-keyword">void</span> *do_ctxt;
   <span class="hljs-keyword">void</span> *do_finalizer;
   DISPATCH_UNION_LE(<span class="hljs-keyword">uint64_t</span> <span class="hljs-keyword">volatile</span> dq_state, dispatch_lock dq_state_lock, <span class="hljs-keyword">uint32_t</span> dq_state_bits );
   <span class="hljs-keyword">void</span> *__dq_opaque1;
   <span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">long</span> dq_serialnum;
   <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *dq_label;
   DISPATCH_UNION_LE(<span class="hljs-keyword">uint32_t</span> <span class="hljs-keyword">volatile</span> dq_atomic_flags, <span class="hljs-keyword">const</span> <span class="hljs-keyword">uint16_t</span> dq_width, <span class="hljs-keyword">const</span> <span class="hljs-keyword">uint16_t</span> __dq_opaque2 );
   <span class="hljs-keyword">dispatch_priority_t</span> dq_priority;
   <span class="hljs-class"><span class="hljs-keyword">union</span> &#123;</span> 
 <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_specific_head_s</span> *<span class="hljs-title">dq_specific_head</span>;</span>
   <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_source_refs_s</span> *<span class="hljs-title">ds_refs</span>;</span>
   <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_timer_source_refs_s</span> *<span class="hljs-title">ds_timer_refs</span>;</span>
   <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_mach_recv_refs_s</span> *<span class="hljs-title">dm_recv_refs</span>;</span>
   &#125;;
   <span class="hljs-keyword">int</span> <span class="hljs-keyword">volatile</span> dq_sref_cnt;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有几个成员变量这里做下说明：</p>
<ul>
<li><code>_as_do</code>和<code>_as_os_obj</code>这种数组的用法，不符合C语言标准，是编译器扩展的用法，声明的变量不会分配空间，其作用是在不同的类型中间转换。</li>
<li><code>do_vtable</code>这个是定义了如何操作这个队列的一些方法，比如怎么压入队列，怎么唤醒队列。主要用来解决队列的操作和队列结构之间的耦合，如果是OC类它的isa指向的也是vtable。</li>
<li><code>do_ref_cnt</code>这个是记录引用计数的，和ARC的规则类似。</li>
<li><code>dq_label</code>存放队列的名字。</li>
</ul>
<h2 data-id="heading-3">2.串行队列和并行队列</h2>
<p>我们最常用gcd的方法之一，就是创建一个队列，一般情况下使用如下代码</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-comment">// 串行队列</span>
<span class="hljs-keyword">dispatch_queue_t</span> sq = dispatch_queue_create(<span class="hljs-string">"test"</span>, DISPATCH_QUEUE_SERIAL);

<span class="hljs-comment">// 并行队列</span>
<span class="hljs-keyword">dispatch_queue_t</span> cq = dispatch_queue_create(<span class="hljs-string">"testcq"</span>, DISPATCH_QUEUE_CONCURRENT);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有两点需要关注：</p>
<p>其一，需要关注两个attr的类型。</p>
<p>第一个<code>DISPATCH_QUEUE_SERIAL</code> 是一个宏，展开为<code>NULL</code>，是默认属性。第二个即<code>DISPATCH_QUEUE_CONCURRENT</code> 展开为</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_GLOBAL_OBJECT(<span class="hljs-keyword">dispatch_queue_attr_t</span>,_dispatch_queue_attr_concurrent)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里插入说明一下<code>dispatch_queue_attr_t</code>。<code>dispatch_queue_attr_t</code>是<code>dispatch_queue_attr_s</code>的指针类型，
<code>DISPATCH_QUEUE_CONCURRENT</code>对应的实例为<code>_dispatch_queue_attr_concurrent</code>，是一个全局初始化的变量。这个变量是放在了<code>_dispatch_queue_attrs[]</code>的数组中，所有的<code>dispatch_queue_attr_t</code>指针都会放置在这个数组中，每个指针在数组中的位置，会对应<code>dispatch_queue_attr_info_t</code>指向的结构体的信息，例如是不是并发，qos优先级等。同样一个<code>dispatch_queue_attr_s</code>实例的并发，优先级属性的不同，会对应在数组的不同位置。
以下是从<code>dispatch_queue_attr_info_t</code>到<code>dispatch_queue_attr_t</code>的转换，可以看到，数组的index是通过<code>dispatch_queue_attr_info_t</code>的属性计算出来的，而从<code>dispatch_queue_attr_t</code>到<code>dispatch_queue_attr_info_t</code>的转换就是这个计算过程的逆过程，这里不再赘述。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">static</span> <span class="hljs-keyword">dispatch_queue_attr_t</span>
_dispatch_queue_attr_from_info(<span class="hljs-keyword">dispatch_queue_attr_info_t</span> dqai)
&#123;
<span class="hljs-keyword">size_t</span> idx = <span class="hljs-number">0</span>;

idx *= DISPATCH_QUEUE_ATTR_OVERCOMMIT_COUNT;
idx += dqai.dqai_overcommit;

idx *= DISPATCH_QUEUE_ATTR_AUTORELEASE_FREQUENCY_COUNT;
idx += dqai.dqai_autorelease_frequency;

idx *= DISPATCH_QUEUE_ATTR_QOS_COUNT;
idx += dqai.dqai_qos;

idx *= DISPATCH_QUEUE_ATTR_PRIO_COUNT;
idx += (<span class="hljs-keyword">size_t</span>)(-dqai.dqai_relpri);

idx *= DISPATCH_QUEUE_ATTR_CONCURRENCY_COUNT;
idx += !dqai.dqai_concurrent;

idx *= DISPATCH_QUEUE_ATTR_INACTIVE_COUNT;
idx += dqai.dqai_inactive;

<span class="hljs-keyword">return</span> (<span class="hljs-keyword">dispatch_queue_attr_t</span>)&_dispatch_queue_attrs[idx];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其二，<code>dispatch_queue_create</code>方法</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-function"><span class="hljs-keyword">dispatch_queue_t</span>
<span class="hljs-title">dispatch_queue_create</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *label, <span class="hljs-keyword">dispatch_queue_attr_t</span> attr)</span>
</span>&#123;
<span class="hljs-keyword">return</span> _dispatch_lane_create_with_target(label, attr,
DISPATCH_TARGET_QUEUE_DEFAULT, <span class="hljs-literal">true</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数返回<code>dispatch_queue_t</code>，指向分配的队列结构。<code>_dispatch_queue_create</code>最终是通过<code>_dispatch_lane_create_with_target</code>函数来创建的。接下来我们看下<code>_dispatch_lane_create_with_target</code>的具体实现。</p>
<h3 data-id="heading-4">_dispatch_lane_create_with_target</h3>
<pre><code class="hljs language-C copyable" lang="C">_dispatch_lane_create_with_target(label, attr, DISPATCH_TARGET_QUEUE_DEFAULT, <span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先入参分别为，创建队列的名称，<code>attr</code>是上面<code>DISPATCH_QUEUE_SERIAL</code>或者<code>DISPATCH_QUEUE_CONCURRENT</code>指向的属性结构。<code>DISPATCH_TARGET_QUEUE_DEFAULT</code>宏展开即为<code>NULL</code>，最后一个参数<code>legacy</code>为<code>true</code>。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">static</span> <span class="hljs-keyword">dispatch_queue_t</span>
_dispatch_lane_create_with_target(<span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *label, <span class="hljs-keyword">dispatch_queue_attr_t</span> dqa,
<span class="hljs-keyword">dispatch_queue_t</span> tq, <span class="hljs-keyword">bool</span> legacy)
&#123;
        <span class="hljs-comment">//【1】</span>
<span class="hljs-keyword">dispatch_queue_attr_info_t</span> dqai = _dispatch_queue_attr_to_info(dqa);
qos = ...
overcommit = ...

        <span class="hljs-comment">//【2】</span>
<span class="hljs-keyword">if</span> (!tq) &#123;
tq = _dispatch_get_root_queue(
qos == DISPATCH_QOS_UNSPECIFIED ? DISPATCH_QOS_DEFAULT : qos,
overcommit == _dispatch_queue_attr_overcommit_enabled)->_as_dq;
<span class="hljs-keyword">if</span> (unlikely(!tq)) &#123;
DISPATCH_CLIENT_CRASH(qos, <span class="hljs-string">"Invalid queue attribute"</span>);
&#125;
&#125;
        <span class="hljs-comment">//【3】</span>
legacy = ...
<span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> *vtable = ...
dqf = ...
label = ...
        
        <span class="hljs-comment">//【4】</span>
<span class="hljs-keyword">dispatch_lane_t</span> dq = _dispatch_object_alloc(vtable, <span class="hljs-keyword">sizeof</span>(struct dispatch_lane_s));
        <span class="hljs-comment">//【5】</span>
_dispatch_queue_init(dq, dqf, dqai.dqai_concurrent ?
DISPATCH_QUEUE_WIDTH_MAX : <span class="hljs-number">1</span>, DISPATCH_QUEUE_ROLE_INNER |
(dqai.dqai_inactive ? DISPATCH_QUEUE_INACTIVE : <span class="hljs-number">0</span>));
        <span class="hljs-comment">//【6】</span>
dq->dq_label = label;
dq->dq_priority = ...
        <span class="hljs-comment">//【7】</span>
_dispatch_retain(tq);
dq->do_targetq = tq;
        <span class="hljs-comment">//【8】</span>
<span class="hljs-keyword">return</span> dq._dq;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了突出创建过程的主要步骤，截取的代码略去了一些参数的处理过程。下文通过指定代码行号分别来说明其大致的功能。</p>
<p>【1】根据<code>dispatch_queue_attr_t</code>，初始化<code>qos</code>，<code>overcommit</code>，</p>
<p>【2】设置<code>tq</code>变量。其中值得关注的是<code>tq</code>（目标队列，可以理解为我们创建的队列所依赖的全局队列）的获取，<code>tq</code>通过<code>_dispatch_get_root_queue</code>方法获得。通过<code>_dispatch_get_root_queue</code>的定义可以看到，gcd会创建一个全局的队列池，总共有16个，跳过了index为0的，1为<code>main_q</code>，2为<code>mgr_q</code>，3为<code>mgr_root_q</code>，4-15 为<code>global queues</code>，17为<code>workloop_fallback_q</code>。这里就是根据<code>qos</code>和<code>overcommit</code>参数映射到线程池的index。从而获取这个队列。从这里也可以看出新创建的队列的目标队列都是全局的线程池。所以可以通过判断一个队列有没有<code>do_targetq</code>判断是不是系统的全局队列。</p>
<p>【3】根据条件，设置<code>legacy</code>，<code>vtable</code>，<code>dqf</code>，<code>label</code>。</p>
<p>【4】<code>_dispatch_object_alloc</code>方法在内存堆中分配队列结构块，这里会指定队列的<code>isa</code>，指向对应的<code>vtable</code>，这里需要说明的是<code>isa</code>和<code>do_vtable</code>是同一个指针的两个名字，类似union结构。</p>
<p>【5】<code>_dispatch_queue_init</code>初始化结构中成员变量的值。</p>
<p>【6】设置队列的<code>label</code>和优先级。</p>
<p>【7】 把新创建的<code>dq</code>的目标队列设置为上面的<code>tq</code>。并且增加<code>tq</code>的引用计数。</p>
<p>【8】 最后返回队列指针，这就是整个创建队列的整个过程。</p>
<p>这里总结一下整个创建的流程，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/705049522774459d82bc1d944f4223c2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="未命名.001.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建队列就是在内存中分配队列的对象，并初始化成员变量，保存队列的性质。我们可以看到这里并没有和系统底层的线程建立关系，只有当我们通过<code>dispatch_async</code>或者<code>dispatch_sync</code>派发任务的时候，系统底层才会按需要创建线程执行任务。下文将探索异步派发和同步派发通过怎样的调用和底层的线程建立关系。</p>
<h2 data-id="heading-5">3.异步派发（dispatch_async)</h2>
<pre><code class="hljs language-C copyable" lang="C">dispatch_async(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步派发的接口如上，其中有两个参数，<code>dq</code>就是添加任务的目标队列，<code>work</code>就是我们要执行的任务，是一个block类型。</p>
<p>这里<code>dq</code>就会有两种类型，就是前文所说的串行队列和并行队列。根据队列的不同，他们所执行的代码路径也是不同的。下面就是我们常常用来把一个任务提交到队列的代码片段。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-comment">// 串行队列的异步派发</span>
<span class="hljs-keyword">dispatch_queue_t</span> sq = dispatch_queue_create(<span class="hljs-string">"test"</span>, DISPATCH_QUEUE_SERIAL);
dispatch_async(sq, ^&#123;
NSLog(@<span class="hljs-string">"hello"</span>);
&#125;);

<span class="hljs-comment">// 并行队列的异步派发</span>
<span class="hljs-keyword">dispatch_queue_t</span> cq = dispatch_queue_create(<span class="hljs-string">"test"</span>, DISPATCH_QUEUE_CONCURRENT);
dispatch_async(cq, ^&#123;
NSLog(@<span class="hljs-string">"hello"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下文先介绍两种队列派发的相同部分，然后再分别说明其中的不同之处。<code>dispatch_async</code>的具体实现如下。</p>
<pre><code class="hljs language-C copyable" lang="C">dispatch_async(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)
&#123;
        <span class="hljs-comment">//【9】</span>
<span class="hljs-keyword">dispatch_continuation_t</span> dc = _dispatch_continuation_alloc();
<span class="hljs-comment">//【10】</span>
        <span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_CONSUME;
<span class="hljs-keyword">dispatch_qos_t</span> qos;
        <span class="hljs-comment">//【11】</span>
qos = _dispatch_continuation_init(dc, dq, work, <span class="hljs-number">0</span>, dc_flags);
        <span class="hljs-comment">//【12】</span>
_dispatch_continuation_async(dq, dc, qos, dc->dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【9】<code>_dispatch_continuation_alloc</code>从名字可以看出是分配continuation结构的函数，具体实现中有thread关联的缓存机制。维护了一个供复用的continuation链表，可以避免频繁的分配内存，提升性能。</p>
<p>【10】<code>dispatch_continuation_t</code>这个是用来描述gcd任务，其中<code>dc_flags</code>描述了任务的类型，比如是<code>barrier</code>，<code>block</code>，<code>group</code>等等。具体参见<code>DC_FLAG_SYNC_WAITER</code>及其他宏的定义。此处使用的<code>DC_FLAG_CONSUME</code>表示continuation资源在执行的时候已经释放了，这个标志一般在async里设置。</p>
<p>【11】<code>_dispatch_continuation_init</code>初始化continuation，这里我们看下具体实现</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">dispatch_qos_t</span>
_dispatch_continuation_init_f(<span class="hljs-keyword">dispatch_continuation_t</span> dc,
<span class="hljs-keyword">dispatch_queue_class_t</span> dqu, <span class="hljs-keyword">void</span> *ctxt, <span class="hljs-keyword">dispatch_function_t</span> f,
<span class="hljs-keyword">dispatch_block_flags_t</span> flags, <span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
<span class="hljs-keyword">pthread_priority_t</span> pp = <span class="hljs-number">0</span>;
dc->dc_flags = dc_flags | DC_FLAG_ALLOCATED;
dc->dc_func = f;
dc->dc_ctxt = ctxt;
pp = ...
_dispatch_continuation_voucher_set(dc, flags);
<span class="hljs-keyword">return</span> _dispatch_continuation_priority_set(dc, dqu, pp, flags);
&#125;

DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">dispatch_qos_t</span>
_dispatch_continuation_init(<span class="hljs-keyword">dispatch_continuation_t</span> dc,
<span class="hljs-keyword">dispatch_queue_class_t</span> dqu, <span class="hljs-keyword">dispatch_block_t</span> work,
<span class="hljs-keyword">dispatch_block_flags_t</span> flags, <span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
<span class="hljs-keyword">void</span> *ctxt = _dispatch_Block_copy(work);

dc_flags |= DC_FLAG_BLOCK | DC_FLAG_ALLOCATED;

...

<span class="hljs-keyword">dispatch_function_t</span> func = _dispatch_Block_invoke(work);
<span class="hljs-keyword">if</span> (dc_flags & DC_FLAG_CONSUME) &#123;
func = _dispatch_call_block_and_release;
&#125;
<span class="hljs-keyword">return</span> _dispatch_continuation_init_f(dc, dqu, ctxt, func, flags, dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到主要是设置continuation的<code>flags</code>，<code>ctxt</code>，<code>func</code>，<code>priority</code>的字段。其中我们要执行的任务block存放在了<code>func</code>和<code>ctxt</code>字段。</p>
<p>【12】最后交给了<code>_dispatch_continuation_async</code>函数处理，下面是该函数的去除一些debug，性能检测代码的实现。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_continuation_async(<span class="hljs-keyword">dispatch_queue_class_t</span> dqu,
<span class="hljs-keyword">dispatch_continuation_t</span> dc, <span class="hljs-keyword">dispatch_qos_t</span> qos, <span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
<span class="hljs-comment">//... 一些调试，性能探针的处理</span>
<span class="hljs-keyword">return</span> dx_push(dqu._dq, dc, qos);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>dx_push是一个宏，这里最终展开为</p>
<pre><code class="hljs language-C copyable" lang="C">dx_push(dqu._dq, dc, qos)
→ dx_vtable(dqu._dq)->dq_push(dqu._dq, dc, qos)
→ &(dqu._dq)->do_vtable->_os_obj_vtable->dq_push(dqu._dq, dc, qos)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里对gcd中涉及的所有类型队列(串行队列，并行队列，管理队列等)进行了抽象，通过给不同队列赋值相应的dq_push（如何加入队列执行），dq_wakeup（怎么唤醒队列）等函数指针，从而操作某个队列时不必关心具体实现细节，达到调用和实现的分离解耦。和在面对对象编程中通过多态实现解耦的思想是相同的。</p>
<p>在创建队列的时候，<code>_dispatch_queue_init</code>会初始化对应的<code>do_vtable</code>。串行和并行队列的do_vtable指针指向的结构体如下。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_VTABLE_SUBCLASS_INSTANCE(queue_serial, lane,
.do_type        = DISPATCH_QUEUE_SERIAL_TYPE,
.do_dispose     = _dispatch_lane_dispose,
.do_debug       = _dispatch_queue_debug,
.do_invoke      = _dispatch_lane_invoke,

.dq_activate    = _dispatch_lane_activate,
.dq_wakeup      = _dispatch_lane_wakeup,
.dq_push        = _dispatch_lane_push,
);

DISPATCH_VTABLE_SUBCLASS_INSTANCE(queue_concurrent, lane,
.do_type        = DISPATCH_QUEUE_CONCURRENT_TYPE,
.do_dispose     = _dispatch_lane_dispose,
.do_debug       = _dispatch_queue_debug,
.do_invoke      = _dispatch_lane_invoke,

.dq_activate    = _dispatch_lane_activate,
.dq_wakeup      = _dispatch_lane_wakeup,
.dq_push        = _dispatch_lane_concurrent_push,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>程序执行到此处，会根据传入<code>disptach_async</code>的队列，执行不同的代码。下文分别描述传入的为串行队列和并行队列时，<code>disptach_async</code>的执行过程。</p>
<h3 data-id="heading-6">在串行队列上异步派发</h3>
<p><code>_dispatch_lane_push</code>方法是把<code>continuation</code>插入队列的<code>dq_items_tail</code>，<code>dq_items_head</code>指向的双向链表中。最后<code>_dispatch_lane_push</code>会调用<code>dq_wakeup</code>的方法，唤醒队列。我们看到串行队列<code>dq_wakeup</code>指向<code>_dispatch_lane_wakeup</code>。这里简化的代码如下。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">void</span>
_dispatch_queue_wakeup(<span class="hljs-keyword">dispatch_queue_class_t</span> dqu, <span class="hljs-keyword">dispatch_qos_t</span> qos,
<span class="hljs-keyword">dispatch_wakeup_flags_t</span> flags, <span class="hljs-keyword">dispatch_queue_wakeup_target_t</span> target)
&#123;
<span class="hljs-keyword">dispatch_queue_t</span> dq = dqu._dq;

<span class="hljs-keyword">if</span> (target) &#123;
<span class="hljs-keyword">uint64_t</span> old_state, new_state, enqueue;
enqueue = ...;
                qos = _dispatch_queue_wakeup_qos(dq, qos);
                old_state = ...;
                new_state = ...;

<span class="hljs-keyword">if</span> (likely((old_state ^ new_state) & enqueue)) &#123;
<span class="hljs-keyword">dispatch_queue_t</span> tq = ...
                        
<span class="hljs-keyword">return</span> _dispatch_queue_push_queue(tq, dq, new_state);
&#125;
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过检查state字段的状态，判断要不要把当前的队列添加到它的目标队列中。因为state可能会由多个线程访问，所以这里对字段的访问都要通过原子操作来进行，一般情况下最终<code>_dispatch_queue_wakeup</code>会走到<code>_dispatch_queue_push_queue</code>方法。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_queue_push_queue(<span class="hljs-keyword">dispatch_queue_t</span> tq, <span class="hljs-keyword">dispatch_queue_class_t</span> dq,
<span class="hljs-keyword">uint64_t</span> dq_state)
&#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> DISPATCH_USE_KEVENT_WORKLOOP</span>
<span class="hljs-keyword">if</span> (likely(_dq_state_is_base_wlh(dq_state))) &#123;
<span class="hljs-keyword">return</span> _dispatch_event_loop_poke((<span class="hljs-keyword">dispatch_wlh_t</span>)dq._dq, dq_state,
DISPATCH_EVENT_LOOP_CONSUME_2);
&#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span> <span class="hljs-comment">// DISPATCH_USE_KEVENT_WORKLOOP</span></span>
<span class="hljs-keyword">return</span> dx_push(tq, dq, _dq_state_max_qos(dq_state));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到，对于队列的调度执行有两种方式，目前Apple平台大部分都使用的<code>KEVENT_WORKLOOP</code>这种方式。默认兜底的方式，是把当前创建的队列加入到系统的global队列中，形成一个数组的结构，gcd通过管理系统global队列进而管理新创建的队列任务。下文我们主要讨论<code>KEVENT_WORKLOOP</code>这种方式。</p>
<p>可以看到使用<code>KEVENT_WORKLOOP</code>方式，不需要目标队列这个参数。之后执行<code>_dispatch_event_loop_poke</code>，一如它的名字，像发扑克牌一样，系统通过一定的策略分发时间片给各自的队列，进而执行队列中的任务。这个方法里面做了兼容多种事件分发机制的操作，例如linux中使用的是<code>poll</code>，<code>select</code>系统调用实现的队列管理，还有其他一些分发的机制。而如今通用的KEVENT_WORKLOOP方式，最终会由<code>_dispatch_kevent_workloop_poke</code>来执行。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_kevent_workloop_poke(<span class="hljs-keyword">dispatch_wlh_t</span> wlh, <span class="hljs-keyword">uint64_t</span> dq_state,
<span class="hljs-keyword">uint32_t</span> flags)
&#123;
<span class="hljs-keyword">uint32_t</span> kev_flags = KEVENT_FLAG_IMMEDIATE | KEVENT_FLAG_ERROR_EVENTS;
dispatch_kevent_s ke;
<span class="hljs-keyword">int</span> action;
action = _dispatch_event_loop_get_action_for_state(dq_state);

<span class="hljs-keyword">override</span>:
        <span class="hljs-comment">//【!】</span>
_dispatch_kq_fill_workloop_event(&ke, action, wlh, dq_state);
        
        <span class="hljs-comment">//【!】</span>
<span class="hljs-keyword">if</span> (_dispatch_kq_poll(wlh, &ke, <span class="hljs-number">1</span>, &ke, <span class="hljs-number">1</span>, <span class="hljs-literal">NULL</span>, <span class="hljs-literal">NULL</span>, kev_flags)) &#123;
<span class="hljs-comment">// ... error handler</span>
&#125;

<span class="hljs-keyword">if</span> (!(flags & DISPATCH_EVENT_LOOP_OVERRIDE)) &#123;
<span class="hljs-comment">// Consume the reference that kept the workloop valid</span>
<span class="hljs-comment">// for the duration of the syscall.</span>
<span class="hljs-keyword">return</span> _dispatch_release_tailcall((<span class="hljs-keyword">dispatch_queue_t</span>)wlh);
&#125;
<span class="hljs-keyword">if</span> (flags & DISPATCH_EVENT_LOOP_CONSUME_2) &#123;
<span class="hljs-keyword">return</span> _dispatch_release_2_tailcall((<span class="hljs-keyword">dispatch_queue_t</span>)wlh);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法中有两个重要的方法。<code>_dispatch_kq_fill_workloop_event(&ke, action, wlh, dq_state)</code>和<code>_dispatch_kq_poll(wlh, &ke, 1, &ke, 1, NULL, NULL, kev_flags)</code></p>
<p>其中<code>_dispatch_kq_fill_workloop_event</code>是根据队列的属性分配一个<code>dispatch_kevent_s</code>的结构，包装了请求内核的操作，其中<code>NOTE_WL_THREAD_REQUEST</code>表明想要请求内核分配一个线程。</p>
<p><code>_dispatch_kq_poll</code>的实现如下，这里去掉了一些异常处理和无效分支的代码。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span>
_dispatch_kq_poll(<span class="hljs-keyword">dispatch_wlh_t</span> wlh, <span class="hljs-keyword">dispatch_kevent_t</span> ke, <span class="hljs-keyword">int</span> n,
<span class="hljs-keyword">dispatch_kevent_t</span> ke_out, <span class="hljs-keyword">int</span> n_out, <span class="hljs-keyword">void</span> *buf, <span class="hljs-keyword">size_t</span> *avail,
<span class="hljs-keyword">uint32_t</span> flags)
&#123;
<span class="hljs-keyword">bool</span> kq_initialized = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">int</span> r = <span class="hljs-number">0</span>;
        <span class="hljs-comment">//【12】</span>
dispatch_once_f(&_dispatch_kq_poll_pred, &kq_initialized, _dispatch_kq_init);
  
retry:
&#123;
flags |= KEVENT_FLAG_WORKLOOP;
<span class="hljs-keyword">if</span> (!(flags & KEVENT_FLAG_ERROR_EVENTS)) &#123;
flags |= KEVENT_FLAG_DYNAMIC_KQ_MUST_EXIST;
&#125;
r = kevent_id((<span class="hljs-keyword">uintptr_t</span>)wlh, ke, n, ke_out, n_out, buf, avail, flags);
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span> <span class="hljs-comment">// DISPATCH_USE_KEVENT_WORKLOOP</span></span>
&#125;
<span class="hljs-keyword">if</span> (unlikely(r == <span class="hljs-number">-1</span>)) &#123;
<span class="hljs-comment">//error handler</span>
&#125;
<span class="hljs-keyword">return</span> r;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里通过上个函数创建的<code>dispatch_kevent_s</code>结构，发起系统调用<code>kevent_id</code>。等待请求事件调度。这里<code>kqueue</code>和<code>kevent</code>系统调用主要任务是请求系统分配线程，并且当请求完成的时候，通知到用户态。<code>kqueue</code>是一种可扩展的事件通知接口，类似linux中的<code>epoll</code>。</p>
<p>【12】这里会调用一次<code>_dispatch_kq_init</code>方法，该方法处理一些初始化<code>kqueue</code>，<code>rootqueue</code>和<code>managerqueue</code>相关操作。可以通过代码看到该方法会调用到<code>_dispatch_root_queues_init_once</code>方法。 而这个方法又调用了<code>_pthread_workqueue_init_with_kevent</code>。<code>_pthread_workqueue_init_with_kevent</code>方法是在pthread库中实现的。在这个库里会处理和内核的交互，最终会保证我们请求的<code>kqueue</code>和<code>kevent</code>系统调用完成时候，会回调到<code>_dispatch_workloop_worker_thread</code>这个方法入口，具体这个过程中间的实现，这里不再详述，有兴趣的可看下pthread和内核的源码。</p>
<p><code>_dispatch_workloop_worker_thread</code>将通过队列的<code>do_vtable</code>调用队列的<code>invoke</code>函数，串行队列就是<code>_dispatch_lane_invoke</code>函数，最终从队列的任务链表中取出要执行的任务，并处理任务执行完毕队列的状态。调用堆栈如下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97e1bba86ecc44f8be753b0e014fc262~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>_dispatch_lane_invoke</code>中会调用<code>_dispatch_lane_serial_drain</code>方法，其主要功能就是，将串行队列中加入的任务根据先进先出的顺序从链表中遍历执行。</p>
<h3 data-id="heading-7">在并行队列上异步派发</h3>
<p>下面是<code>_dispatch_lane_concurrent_push</code>的实现。并行队列最终调用了<code>_dispatch_continuation_redirect_push</code>方法添加任务.</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">void</span>
_dispatch_lane_concurrent_push(<span class="hljs-keyword">dispatch_lane_t</span> dq, <span class="hljs-keyword">dispatch_object_t</span> dou,
<span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
<span class="hljs-comment">// <rdar://problem/24738102&24743140> reserving non barrier width</span>
<span class="hljs-comment">// doesn't fail if only the ENQUEUED bit is set (unlike its barrier</span>
<span class="hljs-comment">// width equivalent), so we have to check that this thread hasn't</span>
<span class="hljs-comment">// enqueued anything ahead of this call or we can break ordering</span>
<span class="hljs-keyword">if</span> (dq->dq_items_tail == <span class="hljs-literal">NULL</span> &&
!_dispatch_object_is_waiter(dou) &&
!_dispatch_object_is_barrier(dou) &&
_dispatch_queue_try_acquire_async(dq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_continuation_redirect_push(dq, dou, qos);
&#125;

_dispatch_lane_push(dq, dou, qos);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_continuation_redirect_push</code>实现如下。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_continuation_redirect_push(<span class="hljs-keyword">dispatch_lane_t</span> dl,
<span class="hljs-keyword">dispatch_object_t</span> dou, <span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
        dou._dc = ...
<span class="hljs-keyword">dispatch_queue_t</span> dq = dl->do_targetq;
<span class="hljs-keyword">if</span> (!qos) qos = _dispatch_priority_qos(dq->dq_priority);
dx_push(dq, dou, qos);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里重新包装了<code>continuation</code>，替换了<code>continuation</code>的<code>invoke</code>指向的函数实现，并且把重新包装好的<code>continuation</code>加入到系统的全局队列中，加入全局队列调用，所以并行队列的任务链表一直是空的。</p>
<p><code>_dispatch_root_queue_push</code>方法，</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_NOINLINE
<span class="hljs-keyword">void</span>
_dispatch_root_queue_push(<span class="hljs-keyword">dispatch_queue_global_t</span> rq, <span class="hljs-keyword">dispatch_object_t</span> dou,
<span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> HAVE_PTHREAD_WORKQUEUE_QOS</span>
<span class="hljs-keyword">if</span> (_dispatch_root_queue_push_needs_override(rq, qos)) &#123;
<span class="hljs-keyword">return</span> _dispatch_root_queue_push_override(rq, dou, qos);
&#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">else</span></span>
(<span class="hljs-keyword">void</span>)qos;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
_dispatch_root_queue_push_inline(rq, dou, dou, <span class="hljs-number">1</span>);
&#125;

DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_root_queue_push_inline(<span class="hljs-keyword">dispatch_queue_global_t</span> dq,
<span class="hljs-keyword">dispatch_object_t</span> _head, <span class="hljs-keyword">dispatch_object_t</span> _tail, <span class="hljs-keyword">int</span> n)
&#123;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_object_s</span> *<span class="hljs-title">hd</span> =</span> _head._do, *tl = _tail._do;
<span class="hljs-keyword">if</span> (unlikely(os_mpsc_push_list(os_mpsc(dq, dq_items), hd, tl, do_next))) &#123;
<span class="hljs-keyword">return</span> _dispatch_root_queue_poke(dq, n, <span class="hljs-number">0</span>);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法把重新包装的<code>continuation</code>加入到root队列中，然后调用<code>_dispatch_root_queue_poke</code>，启动根队列的任务调度。之后会调用<code>_dispatch_root_queue_poke_slow</code>方法，对并行队列任务进行调度处理。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_root_queue_poke_slow(<span class="hljs-keyword">dispatch_queue_global_t</span> dq, <span class="hljs-keyword">int</span> n, <span class="hljs-keyword">int</span> <span class="hljs-built_in">floor</span>)
&#123;
<span class="hljs-keyword">int</span> remaining = n;
<span class="hljs-keyword">int</span> r = ENOSYS;

_dispatch_root_queues_init();

<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> !DISPATCH_USE_INTERNAL_WORKQUEUE</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> DISPATCH_USE_PTHREAD_ROOT_QUEUES</span>
<span class="hljs-keyword">if</span> (dx_type(dq) == DISPATCH_QUEUE_GLOBAL_ROOT_TYPE)
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
&#123;
r = _pthread_workqueue_addthreads(remaining,
_dispatch_priority_to_pp_prefer_fallback(dq->dq_priority));
(<span class="hljs-keyword">void</span>)dispatch_assume_zero(r);
<span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span> <span class="hljs-comment">// !DISPATCH_USE_INTERNAL_WORKQUEUE</span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数会调用<code>_pthread_workqueue_addthreads</code>（这个方法在pthread库中）。<code>_pthread_workqueue_addthreads</code>这个方法会通过系统调用向workqueue请求分配线程，系统调用完成时，会回调<code>root_queue_init</code>初始化的时候，注册的<code>_dispatch_worker_thread2</code>方法，堆栈如下图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2524f082a00341de8d9da1207517dda1~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后<code>_dispatch_root_queue_drain</code>把前面加入的continuation取出并执行，最终调用到我们传入的block中的代码。</p>
<h3 data-id="heading-8">小结</h3>
<p>下图总结了以上异步派发针对两种队列执行过程。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/117a15c9b1dc46aca0499c0c23c741fc~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="dispatch-queue-create.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上可知，异步派发的实现涉及了pthread库和内核提供的系统调用，如下图。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b8e05434534521bd76107a21f64172~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="未命名.001.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上可以看到，串行和并行队列都会发起系统调用，请求线程。</p>
<p>对于串行队列是通过kqueue系统调用发起的，而并行队列只是通过添加线程。造成这个差异的原因是因为，如果我们向一个串行队列加入多个任务，这个任务是需要在一个线程中执行的，这样才能保证同一时间只能有一个任务在执行，而发起kevent_id系统调用的时候有会传入一个<code>dispatch_kevent_s</code>结构体来标识队列对应的线程，每次添加任务，可以保证加入的是一个线程中。</p>
<p>而对于并行队列，因为同一时间可以执行多个队列中的任务，所以添加任务的时候直接可以添加一个新线程，当然不可能每添加一个任务就开辟一个新线程，当分配的线程执行完一个并行队列任务之后，将可以用来执行之后新加入的任务，类似一个线程池的概念，在代码里我们可以看到没有针对并行队列的并发量做限制，所以这也是为什么我们在使用并发队列的时候，没有直接指定并发数量的API。</p>
<h2 data-id="heading-9">4.同步派发（dispatch_sync）</h2>
<p>接下来看下同步派发的实现，同样派发的队列可以是串行，也可以是并行的。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-keyword">dispatch_queue_t</span> sq = dispatch_queue_create(<span class="hljs-string">"test"</span>, DISPATCH_QUEUE_SERIAL);
dispatch_sync(sq, ^&#123;
NSLog(@<span class="hljs-string">"hello"</span>);
&#125;);

<span class="hljs-keyword">dispatch_queue_t</span> cq = dispatch_queue_create(<span class="hljs-string">"test"</span>, DISPATCH_QUEUE_CONCURRENT);
dispatch_async(cq, ^&#123;
NSLog(@<span class="hljs-string">"hello"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dispatch_sync</code>的实现如下。</p>
<pre><code class="hljs language-C copyable" lang="C"><span class="hljs-function">DISPATCH_NOINLINE
<span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_sync</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)</span>
</span>&#123;
<span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_BLOCK;
<span class="hljs-keyword">if</span> (unlikely(_dispatch_block_has_private_data(work))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_block_with_privdata(dq, work, dc_flags);
&#125;
_dispatch_sync_f(dq, work, _dispatch_Block_invoke(work), dc_flags);
&#125;

DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_sync_f(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">void</span> *ctxt, <span class="hljs-keyword">dispatch_function_t</span> func,
<span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
_dispatch_sync_f_inline(dq, ctxt, func, dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>_dispatch_sync_f_inline</code>的实现如下</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_sync_f_inline(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">void</span> *ctxt,
<span class="hljs-keyword">dispatch_function_t</span> func, <span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
<span class="hljs-keyword">if</span> (likely(dq->dq_width == <span class="hljs-number">1</span>)) &#123;
<span class="hljs-keyword">return</span> _dispatch_barrier_sync_f(dq, ctxt, func, dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dx_metatype(dq) != _DISPATCH_LANE_TYPE)) &#123;
DISPATCH_CLIENT_CRASH(<span class="hljs-number">0</span>, <span class="hljs-string">"Queue type doesn't support dispatch_sync"</span>);
&#125;

<span class="hljs-keyword">dispatch_lane_t</span> dl = upcast(dq)._dl;
<span class="hljs-comment">// Global concurrent queues and queues bound to non-dispatch threads</span>
<span class="hljs-comment">// always fall into the slow case, see DISPATCH_ROOT_QUEUE_STATE_INIT_VALUE</span>
<span class="hljs-keyword">if</span> (unlikely(!_dispatch_queue_try_reserve_sync_width(dl))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_f_slow(dl, ctxt, func, <span class="hljs-number">0</span>, dl, dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dq->do_targetq->do_targetq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_recurse(dl, ctxt, func, dc_flags);
&#125;
_dispatch_introspection_sync_begin(dl);
_dispatch_sync_invoke_and_complete(dl, ctxt, func DISPATCH_TRACE_ARG(
_dispatch_trace_item_sync_push_pop(dq, ctxt, func, dc_flags)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面串行队列创建过程中，<code>_dispatch_queue_init</code>的调用，可以看到<code>dq->dq_width == 1</code>。所以对串行队列执行同步操作，最终是调用<code>_dispatch_barrier_sync_f</code>的方法。
从这里可以得出，如果我们加入的是并行队列，会直接调用<code>_dispatch_sync_invoke_and_complete</code>函数处理。下面分成在串行队列和并行队列两部分来说明。</p>
<h3 data-id="heading-10">在串行队列上同步派发</h3>
<p>在串行队列上接下来会调用</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_barrier_sync_f_inline(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">void</span> *ctxt,
<span class="hljs-keyword">dispatch_function_t</span> func, <span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
dispatch_tid tid = _dispatch_tid_self();

<span class="hljs-keyword">dispatch_lane_t</span> dl = upcast(dq)._dl;
        
<span class="hljs-keyword">if</span> (unlikely(!_dispatch_queue_try_acquire_barrier_sync(dl, tid))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_f_slow(dl, ctxt, func, DC_FLAG_BARRIER, dl,
DC_FLAG_BARRIER | dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dl->do_targetq->do_targetq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_recurse(dl, ctxt, func,
DC_FLAG_BARRIER | dc_flags);
&#125;
_dispatch_lane_barrier_sync_invoke_and_complete(dl, ctxt, func
DISPATCH_TRACE_ARG(_dispatch_trace_item_sync_push_pop(
dq, ctxt, func, dc_flags | DC_FLAG_BARRIER)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>队列没有多重依赖，所以不需要递归的调用。<code>_dispatch_introspection_sync_begin</code>只是帮助调试，性能统计的函数，这里不用特别关注。顺便提及，我们知道如果我们在一个串行队列的任务重再次提交同一个串行队列一个同步任务，会造成死锁，这里第二次调用<code>dispatch_sync</code>执行到这里会获取不到<code>barrier_sync</code>，走到<code>_dispatch_sync_f_slow</code>。其中的<code>__DISPATCH_WAIT_FOR_QUEUE__</code>函数会检查到要执行任务的队列和被锁的队列是同一个队列，然后触发crash。
回到正题，之后会走到<code>_dispatch_lane_barrier_sync_invoke_and_complete</code>。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_lane_barrier_sync_invoke_and_complete(<span class="hljs-keyword">dispatch_lane_t</span> dq,
<span class="hljs-keyword">void</span> *ctxt, <span class="hljs-keyword">dispatch_function_t</span> func DISPATCH_TRACE_ARG(<span class="hljs-keyword">void</span> *dc))
&#123;
_dispatch_sync_function_invoke_inline(dq, ctxt, func);
_dispatch_trace_item_complete(dc);
<span class="hljs-keyword">if</span> (unlikely(dq->dq_items_tail || dq->dq_width > <span class="hljs-number">1</span>)) &#123;
<span class="hljs-keyword">return</span> _dispatch_lane_barrier_complete(dq, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-keyword">uint64_t</span> fail_unlock_mask = ...;
<span class="hljs-keyword">uint64_t</span> old_state, new_state;

<span class="hljs-comment">// similar to _dispatch_queue_drain_try_unlock</span>
os_atomic_rmw_loop2o(dq, dq_state, old_state, new_state, release, &#123;
new_state  = old_state - DISPATCH_QUEUE_SERIAL_DRAIN_OWNED;
new_state &= ~DISPATCH_QUEUE_DRAIN_UNLOCK_MASK;
new_state &= ~DISPATCH_QUEUE_MAX_QOS_MASK;
<span class="hljs-keyword">if</span> (unlikely(old_state & fail_unlock_mask)) &#123;
os_atomic_rmw_loop_give_up(&#123;
<span class="hljs-keyword">return</span> _dispatch_lane_barrier_complete(dq, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
&#125;);
&#125;
&#125;);
<span class="hljs-keyword">if</span> (_dq_state_is_base_wlh(old_state)) &#123;
_dispatch_event_loop_assert_not_owned((<span class="hljs-keyword">dispatch_wlh_t</span>)dq);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_sync_function_invoke_inline</code>这个方法会保存当前线程的信息，然后在当前线程执行提交的block任务，恢复线程信息。最后处理任务执行完成之后的清理工作。</p>
<h3 data-id="heading-11">在并行队列上同步派发</h3>
<p>有前文可知，在<code>_dispatch_sync_f_inline</code>函数指，串行队列会执行到<code>_dispatch_sync_invoke_and_complete</code>。</p>
<pre><code class="hljs language-C copyable" lang="C">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_sync_invoke_and_complete(<span class="hljs-keyword">dispatch_lane_t</span> dq, <span class="hljs-keyword">void</span> *ctxt,
<span class="hljs-keyword">dispatch_function_t</span> func DISPATCH_TRACE_ARG(<span class="hljs-keyword">void</span> *dc))
&#123;
_dispatch_sync_function_invoke_inline(dq, ctxt, func);
_dispatch_trace_item_complete(dc);
_dispatch_lane_non_barrier_complete(dq, <span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_sync_function_invoke_inline</code>就是在当前线程，首先保存线程的上下文，然后执行提交的任务，回复之前执行的上下文。
<code>_dispatch_lane_non_barrier_complete</code>处理执行完任务的清理工作，是否释放队列等等的操作。</p>
<h3 data-id="heading-12">小结</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f80b9d6a9c54ec483802c392c5af2ab~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="dispatch-queue-create.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上可以看出同步派发相比异步派发来说，其实现简单了许多。同步派发就是在当前的线程直接执行提交的任务。对于串行，因为不能同时执行多个，需要判断当前队列是不是有正在执行的任务，所以处理起来稍复杂些。而并行队列，不用关心当前是不是有任务正在执行，则直接在当前线程执行即可。当然任务执行完毕，都需要设置处理队列的状态。</p>
<h2 data-id="heading-13">5.总结</h2>
<p>本文简单介绍了串行和并行队列创建的实现，以及提交同步和异步任务的执行过程。其中的实现细节十分丰富，这里没能做到面面俱到，并且很多细节我也还需要探究。整套gcd的实现不仅仅是libdispatch中的代码，它还紧密的依赖pthread和xnu内核的实现。</p>
<p>回到开始提出的问题。并行和串行，同步和异步是两组独立的概念，并行和串行是描述我们在同一个队列中提交多个任务，任务可以的执行方式。并行就是提交的任务可以在多个线程上同时执行，串行就是队列中的任务只能在特定的线程上一个一个的执行。</p>
<p>同步和异步描述的是当前的执行任务和添加到队列中的任务之间的关系。同步派发就是当前的任务暂停，直到添加到队列中的任务执行完成，当前的任务才继续执行。通过dispatch_sync的实现也可以看出，我们提交的任务一般情况下就是在当前的线程执行，然后返回到调用处，继续执行之后的代码。相对应的异步派发，就是只是把任务提交到队列中，然后继续执行当前的任务，至于什么时候执行提交到队列中的任务，由底层的线程调度来控制。并且一般情况下不会在当前线程中执行队列的任务（如果在当前的串行队列中执行，可能会导致死锁）。通过其实现我们可以看到，串行队列上的异步派发，在执行完kevent_id系统调用之后，就会返回到dispatch_async调用处，继续执行之后的代码了，而提交的任务，在一个新的线程中执行，何时执行队列中的任务，取决于kqueue在内核中的实现。</p>
<blockquote>
<p>hi, 我是快手电商的长天</p>
<p>快手电商无线技术团队正在招贤纳士🎉🎉🎉! 我们是公司的核心业务线, 这里云集了各路高手, 也充满了机会与挑战. 伴随着业务的高速发展, 团队也在快速扩张. 欢迎各位高手加入我们, 一起创造世界级的电商产品~</p>
<p>热招岗位: Android/iOS 高级开发, Android/iOS 专家, Java 架构师, 产品经理(电商背景), 测试开发... 大量 HC 等你来呦~</p>
<p>内部推荐请发简历至 >>>我们的邮箱: <a href="https://link.juejin.cn/?target=mailto%3Ahr.ec%40kuaishou.com" target="_blank" title="mailto:hr.ec@kuaishou.com" ref="nofollow noopener noreferrer">hr.ec@kuaishou.com</a> <<<, <strong>备注我的花名哦~</strong> 😘</p>
</blockquote></div>  
</div>
            