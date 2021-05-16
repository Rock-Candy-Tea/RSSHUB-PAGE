
---
title: 'Open MPI 源码学习笔记——架构介绍'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea15ad9d6b754529839246ccd79d44a3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 06:29:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea15ad9d6b754529839246ccd79d44a3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Abstract</h2>
<p>Open MPI 架构介绍阅读笔记</p>
<p>参考：</p>
<p><a href="http://www.aosabook.org/en/openmpi.html" target="_blank" rel="nofollow noopener noreferrer">The Architecture of Open Source Applications (Volume 2): Open MPI (aosabook.org)</a></p>
<p><a href="https://www.open-mpi.org/video/internals/Cisco_JeffSquyres-1up.pdf" target="_blank" rel="nofollow noopener noreferrer">www.open-mpi.org/video/inter…</a></p>
<blockquote>
<p>注意：这两篇介绍都是基于Open MPI 的 1.x 版本。在更高的版本中，已经有部分代码架构发生了变化，在结合源码阅读时一定要切换到 1.x 版本，否则容易产生困惑。</p>
</blockquote>
<p><a href="https://github.com/open-mpi/ompi" target="_blank" rel="nofollow noopener noreferrer">open-mpi/ompi: Open MPI main development repository (github.com)</a></p>
<h2 data-id="heading-1">Background</h2>
<h3 data-id="heading-2">The Message Passing Interface (MPI)</h3>
<p>MPI是一套通信标准，由<a href="http://www.mpi-forum.org/" target="_blank" rel="nofollow noopener noreferrer">MPI Forum</a>创建并维护（MPI Forum是一个开放组织，由工业、学术界的高性能计算领域的专家组成）.</p>
<p>MPI是这样一种API：</p>
<ul>
<li>可移植</li>
<li>高性能的IPC通信</li>
</ul>
<p>MPI一般作为一个消息传递的中间件，上层应用程序可以通过调用MPI接口来执行消息传递。</p>
<p>MPI定义了一系列与平台无关的、高度抽象的API接口，用于进程之间的消息传递。举一个最简单的例子，进程X是发送进程，只需提供消息内容（例如一个双精度数组）以及另一个接收进程的标识（例如进程Y），同时接收进程Y只需提供发送进程的标识（例如进程X），消息就可以从X传递给Y。</p>
<p>注意这个例子中，没有建立连接、没有字节流的转换、没有网络地址的交换，MPI将这些细节都抽象封装了起来，不仅仅是隐藏了复杂性，而且使应用程序能够兼容不同的平台、硬件以及网络类型。</p>
<p>MPI提供的通信模式：</p>
<ul>
<li>point to pint</li>
<li>collective</li>
<li>broadcast</li>
</ul>
<h3 data-id="heading-3">Uses of MPI</h3>
<p>Open-MPI 使 MPI 接口的一个开源实现。支持的网络类型包括但不限于: various protocols over Ethernet (e.g., TCP, iWARP, UDP, raw Ethernet frames, etc.), shared memory, and InfiniBand.</p>
<p>MPI 实现一般关注以下几个指标：</p>
<ul>
<li>短消息传递的超低latency：将1-byte数据从linux用户线程传递给另一台服务器的用户线程，通过InfiniBand，只需要消耗1微妙（0.000001 second）</li>
<li>短消息传递的超高网络注入率(Extremely high message network injection rate)：一些MPI实现（搭配特定硬件）能够实现高达28 million / second 向网络注入消息。</li>
<li>Quick ramp-up (as a function of message size) to the maximum bandwidth supported by the underlying transport.</li>
<li>Low resource utilization：不能影响应用程序的性能</li>
</ul>
<h3 data-id="heading-4">Open MPI的诞生</h3>
<p>Open MPI 联合了四种MPI的不同实现：</p>
<ul>
<li>LAM/MPI,</li>
<li>LA/MPI (Los Alamos MPI)</li>
<li>FT-MPI (Fault-Tolerant MPI)</li>
<li>PACX-MPI</li>
</ul>
<h2 data-id="heading-5">Architecture</h2>
<p>Open MPI使用C语言编写</p>
<p>Open MPI 是一个非常庞大、复杂的代码库</p>
<ul>
<li>2003的MPI 标准——MPI-2.0，定义了超过300个API接口</li>
<li>之前的4个项目，每个项目都非常庞大。例如，LAM/MPI由超过1900个源码文件，代码量超过30W行。</li>
<li>希望Open MPI尽可能的支持更多的特性、环境以及网络类型。</li>
</ul>
<p>因此Open MPI花了大量时间设计架构，主要专注于三件事情：</p>
<ul>
<li>将相近的功能划分在不同的抽象层</li>
<li>使用运行时可加载的插件以及运行时参数，来选择相同接口的不同实现</li>
<li>不允许抽象影响性能</li>
</ul>
<h3 data-id="heading-6">Abstraction Layer Architecture</h3>
<p>Open MPi 可以分为三个主要的抽象层，自顶向下依次为：</p>
<ul>
<li>
<p><em>OMPI (Open MPI)</em> (pronounced: oom-pee):</p>
<ul>
<li>由 MPI standard 所定义</li>
<li>暴露给上层应用的 API，由外部应用调用</li>
</ul>
</li>
<li>
<p><em>ORTE (Open MPI Run-Time Environment)</em> (pronounced "or-tay"):</p>
<ul>
<li>MPI 的 run-time system
<ul>
<li>launch, monitor, kill individual processes</li>
<li>Group individual processes into “jobs”</li>
</ul>
</li>
<li>重定向stdin、stdout、stderr</li>
<li>ORTE 进程管理方式：在简单的环境中，通过<code>rsh</code>或<code>ssh</code> 来launch 进程。而复杂环境(HPC专用)会有shceduler、resource manager等管理组件，面向多个用户进行公平的调度以及资源分配，ORTE支持多种管理环境，例如，orque/PBS Pro, SLURM, Oracle Grid Engine, and LSF.</li>
</ul>
<blockquote>
<p>注意 ORTE 在 5.x 版本中被移除，进程管理模块被替换成了[prrte](<a href="https://github.com/openpmix/prrte" target="_blank" rel="nofollow noopener noreferrer">openpmix/prrte: PMIx Reference RunTime Environment (PRRTE) (github.com)</a>)</p>
</blockquote>
</li>
<li>
<p><em>OPAL (Open, Portable Access Layer)</em> (pronounced: o-pull): OPAL 是xOmpi的最底层</p>
<ul>
<li>只作用于单个进程</li>
<li>负责不同环境的可移植性</li>
<li>包含了一些通用功能（例如链表、字符串操作、debug控制等等）</li>
</ul>
</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea15ad9d6b754529839246ccd79d44a3~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<p>以上各个抽象层都是以 library 的形式存在，他们之间的依赖关系只能从上到下，也就是下层的不能依赖上层的。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf9fff07cb0846f491b4c07c31910d61~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210515092155899" loading="lazy" referrerpolicy="no-referrer">
<p>在代码目录中是以project的形式存在，也就是</p>
<pre><code class="hljs language-tex copyable" lang="tex">ompi/
├── ompi
├── opal
└── orte
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的时，考虑到性能因素，Open MPI 有中“旁路”机制（bypass），ORTE以及OMPI层，可以绕过OPAL，直接与操作系统（甚至是硬件）进行交互。例如OMPI会直接与网卡进行交互，从而达到最大的网络性能。</p>
<h3 data-id="heading-7">Plugin Architecture</h3>
<p>为了在 Open MPI 中使用类似但是不同效果的功能，Open MPI 设计一套被称为**Modular Component Architecture (MCA)**的架构.</p>
<p>在MCA架构中，为每一个抽象层（也就是OMPI、ORTE、OPAL）定义了多个framework，这里的framework类似于其他语言语境中的接口（interface），framework对于一个功能进行了抽象，而plugin就是对于一个framework的不同实现。每个 Plugin 都是以动态链接库（DSO，dynamic shared object）的形式存在。因此run time 能够动态的加载不同的plugin。</p>
<p>例如下图中 btl 是一个功能传输bytes的framework，它属于OMPI层，btl framework之下又包含针对不同网络类型的实现，例如 tcp、openib (InfiniBand)、sm (shared memory)、sm-cuda (shared memory for CUDA)</p>
<blockquote>
<p>在Open MPI 2.x 以上版本，btl 模块已经被移到了 OPAL 之下</p>
</blockquote>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cddc2d92b0fa44eeb642d16b0a1a3c32~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210515121838974" loading="lazy" referrerpolicy="no-referrer">
<p>为什么使用Plugin架构：</p>
<ul>
<li>更好的软件工程
<ul>
<li>实行严格的抽象划分</li>
</ul>
</li>
<li>使代码块变得比较小且彼此之间独立
<ul>
<li>对于学习以及新加入的开发者比较友好</li>
<li>更容易维护和扩展</li>
</ul>
</li>
<li>将用户应用于后端库分离
<ul>
<li>在编译时MPI 应用，不需要考虑使用的哪个特定的库，例如 libibverbs.so / libportals.so / libpbs.a</li>
</ul>
</li>
</ul>
<h4 data-id="heading-8">MCA 设计</h4>
<p>MCA：</p>
<ul>
<li>Top-level architecture for component services</li>
<li>Find, load, unload components</li>
</ul>
<p>Frameworks ：</p>
<ul>
<li>包含一系列功能</li>
<li>定义接口</li>
<li>本质: plugin 类型分组</li>
<li>例如：MPI point-to-point, high-resolution timers</li>
</ul>
<p>Components（Plugins）：</p>
<ul>
<li>Code that exports a specific interface</li>
<li>Loaded / unloaded at run-time (usually)</li>
</ul>
<p>Modules：</p>
<ul>
<li>与资源绑定</li>
<li>例如：“btl_tcp” 组件被加载时, 发现两个网卡(eth0, eth1), btl_tcp组件会创建两个 TCP module</li>
</ul>
<h4 data-id="heading-9">MCA 代码结构</h4>
<p>Frameworks：</p>
<ul>
<li>拥有唯一的名字（string name）</li>
</ul>
<p>Components：</p>
<ul>
<li>Belong to exactly one framework</li>
<li>Have unique string names</li>
<li>Namespace is per framework</li>
</ul>
<blockquote>
<p>所有的名字都是可用的C变量名</p>
</blockquote>
<p>目录结构：</p>
<ul>
<li>
<p>层级结构：<project>/mca/<framework>/<component></p>
<ul>
<li>Project = opal, orte, ompi</li>
<li>Framework = framework name, or “base”</li>
<li>Component = component name, or "base"</li>
</ul>
</li>
<li>
<p>Directory names must match</p>
<ul>
<li>Framework name</li>
<li>Component name</li>
</ul>
</li>
<li>
<p>例子：</p>
<ul>
<li>ompi/mca/btl/tcp, ompi/mca/btl/sm</li>
</ul>
</li>
</ul>
<pre><code class="copyable">./ompi/mca
├── allocator
│   ├── Makefile.am
│   ├── allocator.h
│   ├── base
│   ├── basic
│   └── bucket
├── bcol
│   ├── Makefile.am
│   ├── base
│   ├── basesmuma
│   ├── bcol.h
│   └── ptpcoll
├── bml
│   ├── Makefile.am
│   ├── base
│   ├── bml.h
│   └── r2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">MCA 代码实现</h4>
<ul>
<li>使用函数指针实现抽象</li>
<li>一般被编译为动态库（DSO，so文件）</li>
<li>也可以以静态库打包进libmpi</li>
<li>使用GNU工具libltdl，能够进行跨平台的加载DSO</li>
</ul>
<h5 data-id="heading-11">Components struct</h5>
<p>该结构的定义为于 <code>ompi/mca/btl/btl.h</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_base_component_2_0_0_t</span> &#123;</span>
    <span class="hljs-comment">/* Component struct version number */</span>
    <span class="hljs-keyword">int</span> mca_major_version, mca_minor_version, mca_release_version;

    <span class="hljs-comment">/* The string name of the framework that this component belongs to,
       and the framework's API version that this component adheres to */</span>
    <span class="hljs-keyword">char</span> mca_type_name[MCA_BASE_MAX_TYPE_NAME_LEN + <span class="hljs-number">1</span>];
    <span class="hljs-keyword">int</span> mca_type_major_version, mca_type_minor_version,  
        mca_type_release_version;

    <span class="hljs-comment">/* This component's name and version number */</span>
    <span class="hljs-keyword">char</span> mca_component_name[MCA_BASE_MAX_COMPONENT_NAME_LEN + <span class="hljs-number">1</span>];
    <span class="hljs-keyword">int</span> mca_component_major_version, mca_component_minor_version,
        mca_component_release_version;

    <span class="hljs-comment">/* Function pointers */</span>  
    <span class="hljs-keyword">mca_base_open_component_1_0_0_fn_t</span> mca_open_component;
    <span class="hljs-keyword">mca_base_close_component_1_0_0_fn_t</span> mca_close_component;
    <span class="hljs-keyword">mca_base_query_component_2_0_0_fn_t</span> mca_query_component;
    <span class="hljs-keyword">mca_base_register_component_params_2_0_0_fn_t</span> 
        mca_register_component_params;
&#125;;

<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_base_component_2_0_0_t</span> <span class="hljs-title">mca_base_component_t</span>;</span>

<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_base_component_2_0_0_t</span> <span class="hljs-title">mca_base_component_2_0_0_t</span>;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>几个关键的函数指针：</p>
<ul>
<li>open</li>
<li>close</li>
<li>query</li>
<li>register</li>
</ul>
<h5 data-id="heading-12">Framework Interface</h5>
<p>以btl为例，位于 <code>ompi/mca/btl/btl.h</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_base_component_2_0_0_t</span> &#123;</span>
  <span class="hljs-keyword">mca_base_component_t</span> btl_version;
  <span class="hljs-keyword">mca_base_component_data_t</span> btl_data;
  <span class="hljs-keyword">mca_btl_base_component_init_fn_t</span> btl_init;
  <span class="hljs-keyword">mca_btl_base_component_progress_fn_t</span> btl_progress;
&#125;;
<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_base_component_2_0_0_t</span> <span class="hljs-title">mca_btl_base_component_2_0_0_t</span>;</span>
<span class="hljs-keyword">typedef</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_base_component_2_0_0_t</span> <span class="hljs-title">mca_btl_base_component_t</span>;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">Plugin</h5>
<p>以btl_tcp为例：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_tcp_component_t</span> &#123;</span>
    <span class="hljs-comment">/* btl framework-specific component struct */</span> 
    <span class="hljs-keyword">mca_btl_base_component_2_0_0_t</span> super;

    <span class="hljs-comment">/* Some of the TCP BTL component's specific data members */</span>
    <span class="hljs-comment">/* Number of TCP interfaces on this server */</span>
    <span class="hljs-keyword">uint32_t</span> tcp_addr_count;
    
    <span class="hljs-comment">/* IPv4 listening socket descriptor */</span>
    <span class="hljs-keyword">int</span> tcp_listen_sd;

    <span class="hljs-comment">/* ...and many more not shown here */</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">Module</h5>
<p>与Plugin类似，有基类也有实现类。</p>
<p>btl base module：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_base_module_t</span> &#123;</span>
<span class="hljs-comment">// ......</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tcp module：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">mca_btl_tcp_module_t</span> &#123;</span>
    <span class="hljs-keyword">mca_btl_base_module_t</span>  super;
    <span class="hljs-comment">// ......</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个Plugin可能创建多个Module，与该Plugin关联的资源相关。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8188dd1c6522455e8204a598885294c2~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-15">Component / Module Lifecycle</h4>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5075175c360a435796ede26c3733300c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210515163520778" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-16">Run-Time Parameters</h3>
<p>也被称为MCA Parameters，提供 MCA 组件参数，以及base参数。</p>
<h4 data-id="heading-17">设计背景</h4>
<ul>
<li>尽量避免使用constants，用run-time参数代替
<ul>
<li>避免重新编译</li>
</ul>
</li>
<li>在run-time期间改变程序的行为
<ul>
<li>在特定环境中，找到实现最佳性能的参数</li>
</ul>
</li>
</ul>
<h4 data-id="heading-18">如何使用</h4>
<h5 data-id="heading-19">内建参数</h5>
<ul>
<li>每个framework的名字都是mca 参数</li>
<li>能够指定使用哪一个plugin</li>
<li>可以指定include或exclude 行为，例如 btl=tcp,self,sm, 或 btl = ^openib</li>
</ul>
<h5 data-id="heading-20">如何更改参数</h5>
<ul>
<li>应用程序中，使用MPI API接口，覆盖默认参数</li>
<li>使用命令行工具
<ul>
<li>例如：<code>mpirun -mca <name> <value></code></li>
</ul>
</li>
<li>使用环境变量
<ul>
<li><code>setenv OMPI_MCA_<name> <value></code></li>
</ul>
</li>
<li>在文件中更改
<ul>
<li><code>$HOME/.openmpi/mca-params.conf</code></li>
<li><code>$prefix/etc/openmpi-mca-params.conf</code></li>
</ul>
</li>
</ul>
<p>mca 参数特性：</p>
<ul>
<li>一般由字符串以及数字组成</li>
<li>有的参数是只读的，有的是读写的</li>
<li>有的参数是private 的，有的是public的</li>
</ul>
<p>mca参数名称规则：</p>
<p><code><framework>_<component>_<param_name></code></p>
<p>几个mca 参数例子：</p>
<ul>
<li><strong>btl_udverbs_version</strong>：Read-only, string version of the Verbs library that udverbs BTL was compiled against</li>
<li><strong>btl_tcp_if_include</strong>: Read-write, string list of IP interfaces to use</li>
<li><strong>btl</strong>: Read-write, list of BTL components to use</li>
<li><strong>orte_base_singleton</strong>: Private, whether this process is a singleton</li>
</ul>
<p>另外，可以通过 ompi_info 命令行工具查看哪些参数可以使用。</p>
<h5 data-id="heading-21">如何实现</h5>
<p>mca_base负责解析MCA 参数。</p></div>  
</div>
            