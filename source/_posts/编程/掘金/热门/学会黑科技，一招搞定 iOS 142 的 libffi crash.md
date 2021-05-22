
---
title: '学会黑科技，一招搞定 iOS 14.2 的 libffi crash'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3513b580ec3d47548d2d351a6ed399e2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 18:04:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3513b580ec3d47548d2d351a6ed399e2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3513b580ec3d47548d2d351a6ed399e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者：字节移动技术 —— 谢俊逸</p>
<p>苹果升级 14.2，全球 iOS 遭了秧。libffi 在 iOS14.2 上发生了 crash，我司的许多 App 深受困扰，有许多基础库都是用了 libffi。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7330b1a34b2f4e1ebd0535eb43d9a232~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过定位，发现是 vmremap 导致的 code sign error。我们通过使用静态 trampoline 的方式让 libffi 不需要使用 vmremap，解决了这个问题。这里就介绍一下相关的实现原理。</p>
<h2 data-id="heading-0">libffi 是什么</h2>
<blockquote>
<p>高层语言的编译器生成遵循某些约定的代码。这些公约部分是单独汇编工作所必需的。“调用约定”本质上是编译器对函数入口处将在哪里找到函数参数的假设的一组假设。“调用约定”还指定函数的返回值在哪里找到。</p>
</blockquote>
<blockquote>
<p>一些程序在编译时可能不知道要传递给函数的参数。例如，在运行时，解释器可能会被告知用于调用给定函数的参数的数量和类型。Libffi 可用于此类程序，以提供从解释器程序到编译代码的桥梁。</p>
</blockquote>
<blockquote>
<p>libffi 库为各种调用约定提供了一个便携式、高级的编程接口。这允许程序员在运行时调用调用接口描述指定的任何函数。</p>
</blockquote>
<p><strong>ffi 的使用</strong></p>
<p>简单的找了一个使用 ffi 的库看一下他的调用接口</p>
<pre><code class="hljs language-c copyable" lang="c">ffi_type *returnType = st_ffiTypeWithType(self.signature.returnType);
NSAssert(returnType, @<span class="hljs-string">"can't find a ffi_type of %@"</span>, self.signature.returnType);

NSUInteger argumentCount = self->_argsCount;
_args = <span class="hljs-built_in">malloc</span>(<span class="hljs-keyword">sizeof</span>(ffi_type *) * argumentCount) ;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < argumentCount; i++) &#123;
  ffi_type* current_ffi_type = st_ffiTypeWithType(self.signature.argumentTypes[i]);
  NSAssert(current_ffi_type, @<span class="hljs-string">"can't find a ffi_type of %@"</span>, self.signature.argumentTypes[i]);
  _args[i] = current_ffi_type;
&#125;

<span class="hljs-comment">// 创建 ffi 跳板用到的 closure</span>
_closure = ffi_closure_alloc(<span class="hljs-keyword">sizeof</span>(ffi_closure), (<span class="hljs-keyword">void</span> **)&xxx_func_ptr);

<span class="hljs-comment">// 创建 cif，调用函数用到的参数和返回值的类型信息， 之后在调用时会结合call convention 处理参数和返回值</span>
<span class="hljs-keyword">if</span>(ffi_prep_cif(&_cif, FFI_DEFAULT_ABI, (<span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">int</span>)argumentCount, returnType, _args) == FFI_OK) &#123;

        <span class="hljs-comment">// closure 写入 跳板数据页</span>
  <span class="hljs-keyword">if</span> (ffi_prep_closure_loc(_closure, &_cif, _st_ffi_function, (__bridge <span class="hljs-keyword">void</span> *)(self), xxx_func_ptr) != FFI_OK) &#123;
    NSAssert(NO, @<span class="hljs-string">"genarate IMP failed"</span>);
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  NSAssert(NO, @<span class="hljs-string">""</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完这段代码，大概能理解 ffi 的操作。</p>
<ol>
<li>提供给外界一个指针(指向 trampoline entry)</li>
<li>创建一个 closure, 将调用相关的参数返回值信息放到 closure 里</li>
<li>将 closure 写入到 trampoline 对应的 trampoline data entry 处</li>
</ol>
<p>之后我们调用 trampoline entry func ptr 时，</p>
<ol>
<li>会找到 写入到 trampoline 对应的 trampoline data entry 处的 closure 数据</li>
<li>根据 closure 提供的调用参数和返回值信息，结合调用约定，操作寄存器和栈，写入参数 进行函数调用，获取返回值。</li>
</ol>
<p><strong>那 ffi 是怎么找到 trampoline 对应的 trampoline data entry 处的 closure 数据 呢？</strong></p>
<p>我们从 ffi 分配 trampoline 开始说起：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">static</span> ffi_trampoline_table *
<span class="hljs-title">ffi_remap_trampoline_table_alloc</span> <span class="hljs-params">(<span class="hljs-keyword">void</span>)</span>
</span>&#123;
.....
  <span class="hljs-comment">/* Allocate two pages -- a config page and a placeholder page */</span>
  config_page = <span class="hljs-number">0x0</span>;
  kt = vm_allocate (mach_task_self (), &config_page, PAGE_MAX_SIZE * <span class="hljs-number">2</span>,
                    VM_FLAGS_ANYWHERE);
  <span class="hljs-keyword">if</span> (kt != KERN_SUCCESS)
      <span class="hljs-keyword">return</span> <span class="hljs-literal">NULL</span>;

  <span class="hljs-comment">/* Allocate two pages -- a config page and a placeholder page */</span>
  <span class="hljs-comment">//bdffc_closure_trampoline_table_page</span>

  <span class="hljs-comment">/* Remap the trampoline table on top of the placeholder page */</span>
  trampoline_page = config_page + PAGE_MAX_SIZE;
  trampoline_page_template = (<span class="hljs-keyword">vm_address_t</span>)&ffi_closure_remap_trampoline_table_page;
<span class="hljs-meta">#<span class="hljs-meta-keyword">ifdef</span> __arm__</span>
  <span class="hljs-comment">/* bdffc_closure_trampoline_table_page can be thumb-biased on some ARM archs */</span>
  trampoline_page_template &= ~<span class="hljs-number">1UL</span>;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
  kt = vm_remap (mach_task_self (), &trampoline_page, PAGE_MAX_SIZE, <span class="hljs-number">0x0</span>,
                 VM_FLAGS_OVERWRITE, mach_task_self (), trampoline_page_template,
                 FALSE, &cur_prot, &max_prot, VM_INHERIT_SHARE);
  <span class="hljs-keyword">if</span> (kt != KERN_SUCCESS)
  &#123;
      vm_deallocate (mach_task_self (), config_page, PAGE_MAX_SIZE * <span class="hljs-number">2</span>);
      <span class="hljs-keyword">return</span> <span class="hljs-literal">NULL</span>;
  &#125;


  <span class="hljs-comment">/* We have valid trampoline and config pages */</span>
  table = <span class="hljs-built_in">calloc</span> (<span class="hljs-number">1</span>, <span class="hljs-keyword">sizeof</span> (ffi_trampoline_table));
  table->free_count = FFI_REMAP_TRAMPOLINE_COUNT/<span class="hljs-number">2</span>;
  table->config_page = config_page;
  table->trampoline_page = trampoline_page;

......
  <span class="hljs-keyword">return</span> table;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先 ffi 在创建 trampoline 时，会分配两个连续的 page</p>
<p>trampoline page 会 remap 到我们事先在代码中汇编写的 ffi_closure_remap_trampoline_table_page。</p>
<p>其结构如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415980222021439cb83206e47e524eef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们 <code>ffi_prep_closure_loc(_closure, &_cif, _st_ffi_function, (__bridge void *)(self), entry1))</code> 写入 closure 数据时， 会写入到 entry1 对应的 closuer1。</p>
<pre><code class="hljs language-c copyable" lang="c">
<span class="hljs-function">ffi_status
<span class="hljs-title">ffi_prep_closure_loc</span> <span class="hljs-params">(ffi_closure *closure,
                      ffi_cif* cif,
                      <span class="hljs-keyword">void</span> (*fun)(ffi_cif*,<span class="hljs-keyword">void</span>*,<span class="hljs-keyword">void</span>**,<span class="hljs-keyword">void</span>*),
                      <span class="hljs-keyword">void</span> *user_data,
                      <span class="hljs-keyword">void</span> *codeloc)</span>
</span>&#123;
......
  <span class="hljs-keyword">if</span> (cif->flags & AARCH64_FLAG_ARG_V)
      start = ffi_closure_SYSV_V; <span class="hljs-comment">// ffi 对 closure的处理函数</span>
  <span class="hljs-keyword">else</span>
      start = ffi_closure_SYSV;

  <span class="hljs-keyword">void</span> **config = (<span class="hljs-keyword">void</span>**)((<span class="hljs-keyword">uint8_t</span> *)codeloc - PAGE_MAX_SIZE);
  config[<span class="hljs-number">0</span>] = closure;
  config[<span class="hljs-number">1</span>] = start;
......
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是怎么对应到的呢? closure1 和 entry1 距离其所属 Page 的 offset 是一致的，通过 offset，成功建立 trampoline entry 和 trampoline closure 的对应关系。</p>
<p>现在我们知道这个关系，我们通过代码看一下到底在程序运行的时候 是怎么找到 closure 的。</p>
<p>这四条指令是我们 trampoline entry 的代码实现，就是 ffi 返回的 xxx_func_ptr</p>
<pre><code class="hljs language-arm copyable" lang="arm"><span class="hljs-keyword">adr</span> x16, -PAGE_MAX_SIZE
<span class="hljs-symbol">ldp</span> x17, x16, [x16]
<span class="hljs-keyword">br</span> x16
<span class="hljs-keyword">nop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 .rept 我们创建 PAGE_MAX_SIZE / FFI_TRAMPOLINE_SIZE 个跳板，刚好一个页的大小</p>
<pre><code class="hljs language-arm copyable" lang="arm"><span class="hljs-comment"># 动态remap的 page</span>
<span class="hljs-symbol">.align</span> PAGE_MAX_SHIFT
<span class="hljs-symbol">CNAME</span>(ffi_closure_remap_trampoline_table_page):
<span class="hljs-symbol">.rept</span> PAGE_MAX_SIZE / FFI_TRAMPOLINE_SIZE
  <span class="hljs-comment"># 这是我们的 trampoline entry, 就是ffi生成的函数指针</span>
  <span class="hljs-keyword">adr</span> x16, -PAGE_MAX_SIZE                         <span class="hljs-comment">// 将pc地址减去PAGE_MAX_SIZE, 找到 trampoine data entry</span>
  ldp x17, x16, [x16]                             <span class="hljs-comment">// 加载我们写入的 closure, start 到 x17, x16</span>
  <span class="hljs-keyword">br</span> x16                                          <span class="hljs-comment">// 跳转到 start 函数</span>
  <span class="hljs-keyword">nop</span>        <span class="hljs-comment">/* each entry in the trampoline config page is 2*sizeof(void*) so the trampoline itself cannot be smaller that 16 bytes */</span>
<span class="hljs-symbol">.endr</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 pc 地址减去 PAGE_MAX_SIZE 就找到对应的 trampoline data entry 了。</p>
<h2 data-id="heading-1">静态跳板的实现</h2>
<p>由于代码段和数据段在不同的内存区域。</p>
<p>我们此时不能通过 像 vmremap 一样分配两个连续的 PAGE，在寻找 trampoline data entry 只是简单的-PAGE_MAX_SIZE 找到对应关系，需要稍微麻烦点的处理。</p>
<p>主要是通过 adrp 找到<code>_ffi_static_trampoline_data_page1</code> 和 <code>_ffi_static_trampoline_page1</code>的起始地址，用 pc-<code>_ffi_static_trampoline_page1</code>的起始地址计算 offset，找到 trampoline data entry。</p>
<pre><code class="hljs language-arm copyable" lang="arm"><span class="hljs-comment"># 静态分配的page</span>
<span class="hljs-comment">#ifdef __MACH__</span>
<span class="hljs-comment">#include <mach/machine/vm_param.h></span>

<span class="hljs-symbol">.align</span> <span class="hljs-number">14</span>
<span class="hljs-symbol">.data</span>
<span class="hljs-symbol">.global</span> _ffi_static_trampoline_data_page1
<span class="hljs-symbol">_ffi_static_trampoline_data_page1:</span>
    <span class="hljs-meta">.space</span> PAGE_MAX_SIZE*<span class="hljs-number">5</span>
<span class="hljs-symbol">.align</span> PAGE_MAX_SHIFT
<span class="hljs-symbol">.text</span>
<span class="hljs-symbol">CNAME</span>(_ffi_static_trampoline_page1):

<span class="hljs-symbol">_ffi_local_forwarding_bridge:</span>
<span class="hljs-keyword">adrp</span> x17, ffi_closure_static_trampoline_table_page_start<span class="hljs-comment">@PAGE;// text page</span>
<span class="hljs-keyword">sub</span>  x16, x16, x17<span class="hljs-comment">;// offset</span>
<span class="hljs-keyword">adrp</span> x17, _ffi_static_trampoline_data_page1<span class="hljs-comment">@PAGE;// data page</span>
<span class="hljs-keyword">add</span> x16, x16, x17<span class="hljs-comment">;// data address</span>
<span class="hljs-symbol">ldp</span> x17, x16, [x16]<span class="hljs-comment">;// x17 closure x16 start</span>
<span class="hljs-keyword">br</span> x16
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>
<span class="hljs-symbol">.align</span> PAGE_MAX_SHIFT
<span class="hljs-symbol">CNAME</span>(ffi_closure_static_trampoline_table_page):

<span class="hljs-comment">#这个label 用来adrp@PAGE 计算 trampoline 到 trampoline page的offset</span>
<span class="hljs-comment">#留了5个用来调试。</span>
<span class="hljs-comment"># 我们static trampoline 两条指令就够了，这里使用4个，和remap的保持一致</span>
<span class="hljs-symbol">ffi_closure_static_trampoline_table_page_start:</span>
<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>

<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>

<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>

<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>

<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>

<span class="hljs-comment">// 5 * 4</span>
<span class="hljs-symbol">.rept</span> (PAGE_MAX_SIZE*<span class="hljs-number">5</span>-<span class="hljs-number">5</span>*<span class="hljs-number">4</span>) / FFI_TRAMPOLINE_SIZE
<span class="hljs-keyword">adr</span> x16, <span class="hljs-number">#0</span>
<span class="hljs-keyword">b</span> _ffi_local_forwarding_bridge
<span class="hljs-keyword">nop</span>
<span class="hljs-keyword">nop</span>
<span class="hljs-symbol">.endr</span>

<span class="hljs-symbol">.globl</span> CNAME(ffi_closure_static_trampoline_table_page)
<span class="hljs-symbol">FFI_HIDDEN</span>(CNAME(ffi_closure_static_trampoline_table_page))
<span class="hljs-comment">#ifdef __ELF__</span>
        .type        CNAME(ffi_closure_static_trampoline_table_page), <span class="hljs-symbol">#function</span>
        .size        CNAME(ffi_closure_static_trampoline_table_page), . - CNAME(ffi_closure_static_trampoline_table_page)
<span class="hljs-comment">#endif</span>
<span class="hljs-comment">#endif</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">关于字节移动平台团队</h2>
<p>字节跳动移动平台团队(Client Infrastructure)是大前端基础技术行业领军者，负责整个字节跳动的大前端基础设施建设，提升公司全产品线的性能、稳定性和工程效率，支持的产品包括但不限于抖音、今日头条、西瓜视频、火山小视频等，在移动端、Web、Desktop 等各终端都有深入研究。</p>
<p>就是现在！<strong>客户端／前端／服务端／测试开发</strong> 面向社会+校园招聘，base 北上广深杭成！<strong>一起来用技术改变世界</strong>，感兴趣可以联系邮箱 <strong><a href="mailto:chenxuwei.cxw@bytedance.com">chenxuwei.cxw@bytedance.com</a></strong> ，<strong>邮件主题：简历-姓名-求职意向-电话</strong>。</p></div>  
</div>
            