
---
title: 'eBPF Up & Running_ Overview'
categories: 
    - 博客
    - 阿里云系统组技术博客 - 首页
author: 阿里云系统组技术博客 - 首页
comments: false
date: Thu, 09 Jul 2020 07:00:00 GMT
thumbnail: 'https://kernel.taobao.org//2020/07/eBPF-Up-and-Running-Overview/1.png'
---

<div>   
<p>eBPF 技术是近几年 Linux 社区一颗闪亮的明星，如果你还没有开始接触并编写过 eBPF 程序，那么不要错过，接下来的一系列文章非常适合你。</p> <p>eBPF Up & Running 系列文章目前主要包括下面三篇：</p> <ul> <li>Overview 总览，你的第一个 eBPF 程序将会在这里诞生；</li> <li>Tracing 跟踪，eBPF 如何在 tracing 场景大展身手；</li> <li>Network 网络，如何使用 eBPF 增强内核网络；</li> </ul> <p>接下来会随着 eBPF 的发展和大家的反响情况，不断丰富扩展更多的文章。废话不多说，让我们开始接下来的干货时间。</p> <h1 id="简介">简介</h1> <p>在写第一行代码之前，首先让我们了解一下 eBPF 技术前世今生。</p> <p>回到 1992 年，eBPF 的前身 BPF (Berkeley Packet Filter)，现在被成为 cBPF (classic BPF) ，主要用于 tcpdump 和 seccomp，场景无外乎是一种灵活的 DSL + 虚拟机帮助用户筛选数据。用户的过滤条件会被编译为 cBPF 程序，程序由预先定义的指令组成，这些指令在内核中解释运行，并通过 JIT 加速执行速度，每当数据经过时，会触发程序执行并判断是否满足筛选条件。</p> <p>时间很快来到了 2011 年，eBPF 在这一年诞生了。经过社区的不断迭代和完善，eBPF 在各个方面得到增强：</p> <ol> <li>定义了全新的指令架构，复用了 cBPF 的 opcode 格式和命令，并引入了大量的寄存器；</li> <li>LLVM 后端支持 BPF target，可以将 C 程序编译为 eBPF 字节码并在内核中运行；</li> <li>引入了 bpf.h 等头文件的支持和丰富的 helpers 函数，简化了 eBPF 程序的编写；</li> </ol> <p>eBPF 是如何在内核中的执行的？<a href="https://kernel.taobao.org/2020/06/eBPF-Internal-Instructions-and-Runtime/">eBPF Internal: Instructions and Runtime </a> 文章中有更详细的介绍，下图展示了 eBPF 程序的大体执行流程。 <img src="https://kernel.taobao.org//2020/07/eBPF-Up-and-Running-Overview/1.png" alt="image.png" referrerpolicy="no-referrer"></p> <p>其实 eBPF 本身其实远没有想象中的复杂，我们可以把内核想象成一个庞大而复杂的电路，如果电路出现了异常，我们可以通过使用万用表测量电路，如果当前电路不能满足需求，但又不能推倒重新设计，我们需要串入其他元件。eBPF 之于电路，既是万用表，也是各种功能元件。再回到内核中的 eBPF，内核预先在各个关键路径埋设了 eBPF 程序入口，用户可以编写不同类型的 eBPF 程序，将 eBPF 程序 attach 在内核中不同路径中执行。</p> <h1 id="示例流量协议统计">示例：流量协议统计</h1> <h2 id="搭建脚手架">搭建脚手架</h2> <p>在编写第一个程序之前，我们需要准备一个顺手的开发环境。内核源码仓库 <code class="highlighter-rouge">samples/bpf</code> 目录下包含了数十个典型的 eBPF 示例程序，除了可供学习和参考之外，我们可以将程序代码放在这个目录，无需自己额外花时间编写和调试 Makefile。</p> <h2 id="代码编写">代码编写</h2> <p>eBPF 程序本质上是一种字节码，我们只需将编写的代码编译成 eBPF 字节码，即可在内核的 eBPF 虚拟机中运行。理论上我们可以使用各种现有的语言编写 eBPF 程序，只要确保这门语言具有对应的 LLVM 前端，帮助我们将其翻译为 LLVM IR 中间代码，并通过 LLVM 最终编译为 eBPF 字节码。通常情况下，推荐使用 C 进行编写，当前内核提供了完备的 C library。因此我们需要确保 clang 已经正确配置好，如果已经按照上面步骤正确配置了脚手架，我们无需再配置 clang 和 LLVM。</p> <p>对于大部分场景下 eBPF 编程模型，eBPF 程序不是单独出现，而是由用户态控制平面 control plane 和内核态数据平面 data plane 两部分组成，经典的数据面和控制面分离。</p> <p>接下来我们将以 <code class="highlighter-rouge">samples/bpf/&#123;xdp1_kern.c,xdp1_user.c&#125;</code> 程序为例，这个示例不只是简单的打印，它可以统计网卡的数据报文的协议分布数量。</p> <p>首先是内核态的 eBPF 代码：xdp1_kern.c，主要功能是从数据报文中解析并判断协议类型，统计数据报文中不同协议的数量分布情况。</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/* 其他省略，完整源码请参考 samples/bpf/xdp1_kern.c */</span>

<span class="cm">/* 定义数据结构存放统计信息 */</span>
<span class="k">struct</span> <span class="n">bpf_map_def</span> <span class="n">SEC</span><span class="p">(</span><span class="s">"maps"</span><span class="p">)</span> <span class="n">rxcnt</span> <span class="o">=</span> <span class="p">&#123;</span>
        <span class="p">.</span><span class="n">type</span> <span class="o">=</span> <span class="n">BPF_MAP_TYPE_PERCPU_ARRAY</span><span class="p">,</span>
        <span class="p">.</span><span class="n">key_size</span> <span class="o">=</span> <span class="k">sizeof</span><span class="p">(</span><span class="n">u32</span><span class="p">),</span>
        <span class="p">.</span><span class="n">value_size</span> <span class="o">=</span> <span class="k">sizeof</span><span class="p">(</span><span class="kt">long</span><span class="p">),</span>
        <span class="p">.</span><span class="n">max_entries</span> <span class="o">=</span> <span class="mi">256</span><span class="p">,</span>
<span class="p">&#125;;</span>

<span class="n">SEC</span><span class="p">(</span><span class="s">"xdp1"</span><span class="p">)</span>
<span class="cm">/* eBPF XDP 类型程序的特定函数签名，ctx 包含数据包的上下文信息 */</span>
<span class="kt">int</span> <span class="n">xdp_prog1</span><span class="p">(</span><span class="k">struct</span> <span class="n">xdp_md</span> <span class="o">*</span><span class="n">ctx</span><span class="p">)</span>
<span class="p">&#123;</span>
        <span class="cm">/* 报文结束位置 */</span>
        <span class="kt">void</span> <span class="o">*</span><span class="n">data_end</span> <span class="o">=</span> <span class="p">(</span><span class="kt">void</span> <span class="o">*</span><span class="p">)(</span><span class="kt">long</span><span class="p">)</span><span class="n">ctx</span><span class="o">-></span><span class="n">data_end</span><span class="p">;</span>
        <span class="cm">/* 报文开始位置 */</span>
        <span class="kt">void</span> <span class="o">*</span><span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kt">void</span> <span class="o">*</span><span class="p">)(</span><span class="kt">long</span><span class="p">)</span><span class="n">ctx</span><span class="o">-></span><span class="n">data</span><span class="p">;</span>
        <span class="k">struct</span> <span class="n">ethhdr</span> <span class="o">*</span><span class="n">eth</span> <span class="o">=</span> <span class="n">data</span><span class="p">;</span>
        <span class="kt">long</span> <span class="o">*</span><span class="n">value</span><span class="p">;</span>
        <span class="n">u16</span> <span class="n">h_proto</span><span class="p">;</span>
        <span class="n">u64</span> <span class="n">nh_off</span><span class="p">;</span>
        <span class="n">u32</span> <span class="n">ipproto</span><span class="p">;</span>

        <span class="n">nh_off</span> <span class="o">=</span> <span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">eth</span><span class="p">);</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">data</span> <span class="o">+</span> <span class="n">nh_off</span> <span class="o">></span> <span class="n">data_end</span><span class="p">)</span>
        <span class="cm">/* 对于非法报文直接返回 XDP_DROP 并丢弃 */</span>
                <span class="k">return</span> <span class="n">XDP_DROP</span><span class="p">;</span>

        <span class="n">h_proto</span> <span class="o">=</span> <span class="n">eth</span><span class="o">-></span><span class="n">h_proto</span><span class="p">;</span>

        <span class="cm">/* 接下来会根据数据报文依次解析协议类型 */</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_8021Q</span><span class="p">)</span> <span class="o">||</span> <span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_8021AD</span><span class="p">))</span> <span class="p">&#123;</span>
                <span class="k">struct</span> <span class="n">vlan_hdr</span> <span class="o">*</span><span class="n">vhdr</span><span class="p">;</span>

                <span class="n">vhdr</span> <span class="o">=</span> <span class="n">data</span> <span class="o">+</span> <span class="n">nh_off</span><span class="p">;</span>
                <span class="n">nh_off</span> <span class="o">+=</span> <span class="k">sizeof</span><span class="p">(</span><span class="k">struct</span> <span class="n">vlan_hdr</span><span class="p">);</span>
        <span class="cm">/* 判断数据包是否合法，否则直接丢弃 */</span>
                <span class="k">if</span> <span class="p">(</span><span class="n">data</span> <span class="o">+</span> <span class="n">nh_off</span> <span class="o">></span> <span class="n">data_end</span><span class="p">)</span>
                        <span class="k">return</span> <span class="n">XDP_DROP</span><span class="p">;</span>
                <span class="n">h_proto</span> <span class="o">=</span> <span class="n">vhdr</span><span class="o">-></span><span class="n">h_vlan_encapsulated_proto</span><span class="p">;</span>
        <span class="p">&#125;</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_8021Q</span><span class="p">)</span> <span class="o">||</span> <span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_8021AD</span><span class="p">))</span> <span class="p">&#123;</span>
                <span class="k">struct</span> <span class="n">vlan_hdr</span> <span class="o">*</span><span class="n">vhdr</span><span class="p">;</span>

                <span class="n">vhdr</span> <span class="o">=</span> <span class="n">data</span> <span class="o">+</span> <span class="n">nh_off</span><span class="p">;</span>
                <span class="n">nh_off</span> <span class="o">+=</span> <span class="k">sizeof</span><span class="p">(</span><span class="k">struct</span> <span class="n">vlan_hdr</span><span class="p">);</span>
        <span class="cm">/* 判断数据包是否合法，否则直接丢弃 */</span>
                <span class="k">if</span> <span class="p">(</span><span class="n">data</span> <span class="o">+</span> <span class="n">nh_off</span> <span class="o">></span> <span class="n">data_end</span><span class="p">)</span>
                        <span class="k">return</span> <span class="n">XDP_DROP</span><span class="p">;</span>
                <span class="n">h_proto</span> <span class="o">=</span> <span class="n">vhdr</span><span class="o">-></span><span class="n">h_vlan_encapsulated_proto</span><span class="p">;</span>
        <span class="p">&#125;</span>

        <span class="k">if</span> <span class="p">(</span><span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_IP</span><span class="p">))</span>
        <span class="cm">/* 从 payload 中解析 Ipv4 protocol */</span>
                <span class="n">ipproto</span> <span class="o">=</span> <span class="n">parse_ipv4</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">nh_off</span><span class="p">,</span> <span class="n">data_end</span><span class="p">);</span>
        <span class="k">else</span> <span class="k">if</span> <span class="p">(</span><span class="n">h_proto</span> <span class="o">==</span> <span class="n">htons</span><span class="p">(</span><span class="n">ETH_P_IPV6</span><span class="p">))</span>
        <span class="cm">/* 从 payload 中解析 Ipv6 protocol */</span>
                <span class="n">ipproto</span> <span class="o">=</span> <span class="n">parse_ipv6</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">nh_off</span><span class="p">,</span> <span class="n">data_end</span><span class="p">);</span>
        <span class="k">else</span>
                <span class="n">ipproto</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
  
        <span class="cm">/* 统计不同协议的访问次数 */</span>
        <span class="n">value</span> <span class="o">=</span> <span class="n">bpf_map_lookup_elem</span><span class="p">(</span><span class="o">&</span><span class="n">rxcnt</span><span class="p">,</span> <span class="o">&</span><span class="n">ipproto</span><span class="p">);</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">value</span><span class="p">)</span>
                <span class="o">*</span><span class="n">value</span> <span class="o">+=</span> <span class="mi">1</span><span class="p">;</span>

        <span class="cm">/* 返回 XDP_PASS 传递报文至下层处理逻辑 */</span>
        <span class="k">return</span> <span class="n">XDP_PASS</span><span class="p">;</span>
<span class="p">&#125;</span>
</code></pre></div></div> <p>接下来是用户态代码：xdp1_user.c，主要功能是载入 eBPF 程序到内核中，并从内核共享的 map 中获得统计信息并展示。</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/* 其他省略，完整源码请参考 samples/bpf/xdp1_kern.c */</span>

<span class="k">static</span> <span class="kt">int</span> <span class="n">ifindex</span><span class="p">;</span>
<span class="k">static</span> <span class="n">__u32</span> <span class="n">xdp_flags</span><span class="p">;</span>

<span class="k">static</span> <span class="kt">void</span> <span class="nf">int_exit</span><span class="p">(</span><span class="kt">int</span> <span class="n">sig</span><span class="p">)</span>
<span class="p">&#123;</span>
        <span class="cm">/* 将 XDP 与网卡解绑 */</span>
        <span class="n">bpf_set_link_xdp_fd</span><span class="p">(</span><span class="n">ifindex</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">xdp_flags</span><span class="p">);</span>
        <span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="k">static</span> <span class="kt">void</span> <span class="nf">poll_stats</span><span class="p">(</span><span class="kt">int</span> <span class="n">map_fd</span><span class="p">,</span> <span class="kt">int</span> <span class="n">interval</span><span class="p">)</span>
<span class="p">&#123;</span>
        <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">nr_cpus</span> <span class="o">=</span> <span class="n">bpf_num_possible_cpus</span><span class="p">();</span>
        <span class="k">const</span> <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">nr_keys</span> <span class="o">=</span> <span class="mi">256</span><span class="p">;</span>
        <span class="n">__u64</span> <span class="n">values</span><span class="p">[</span><span class="n">nr_cpus</span><span class="p">],</span> <span class="n">prev</span><span class="p">[</span><span class="n">nr_keys</span><span class="p">][</span><span class="n">nr_cpus</span><span class="p">];</span>
        <span class="n">__u32</span> <span class="n">key</span><span class="p">;</span>
        <span class="kt">int</span> <span class="n">i</span><span class="p">;</span>

        <span class="n">memset</span><span class="p">(</span><span class="n">prev</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="k">sizeof</span><span class="p">(</span><span class="n">prev</span><span class="p">));</span>

        <span class="k">while</span> <span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="p">&#123;</span>
                <span class="n">sleep</span><span class="p">(</span><span class="n">interval</span><span class="p">);</span>

                <span class="k">for</span> <span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">key</span> <span class="o"><</span> <span class="n">nr_keys</span><span class="p">;</span> <span class="n">key</span><span class="o">++</span><span class="p">)</span> <span class="p">&#123;</span>
                        <span class="n">__u64</span> <span class="n">sum</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
                        <span class="cm">/* 从 map 中获取统计信息 */</span>
                        <span class="n">assert</span><span class="p">(</span><span class="n">bpf_map_lookup_elem</span><span class="p">(</span><span class="n">map_fd</span><span class="p">,</span> <span class="o">&</span><span class="n">key</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">);</span>
                        <span class="k">for</span> <span class="p">(</span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o"><</span> <span class="n">nr_cpus</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
                                <span class="n">sum</span> <span class="o">+=</span> <span class="p">(</span><span class="n">values</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">-</span> <span class="n">prev</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="n">i</span><span class="p">]);</span>
                        <span class="k">if</span> <span class="p">(</span><span class="n">sum</span><span class="p">)</span>
                                <span class="n">printf</span><span class="p">(</span><span class="s">"proto %u: %10llu pkt/s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
                                       <span class="n">key</span><span class="p">,</span> <span class="n">sum</span> <span class="o">/</span> <span class="n">interval</span><span class="p">);</span>
                        <span class="n">memcpy</span><span class="p">(</span><span class="n">prev</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="n">values</span><span class="p">,</span> <span class="k">sizeof</span><span class="p">(</span><span class="n">values</span><span class="p">));</span>
                <span class="p">&#125;</span>
        <span class="p">&#125;</span>
<span class="p">&#125;</span>

<span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">int</span> <span class="n">argc</span><span class="p">,</span> <span class="kt">char</span> <span class="o">**</span><span class="n">argv</span><span class="p">)</span>
<span class="p">&#123;</span>
        <span class="k">struct</span> <span class="n">rlimit</span> <span class="n">r</span> <span class="o">=</span> <span class="p">&#123;</span><span class="n">RLIM_INFINITY</span><span class="p">,</span> <span class="n">RLIM_INFINITY</span><span class="p">&#125;;</span>
        <span class="k">struct</span> <span class="n">bpf_prog_load_attr</span> <span class="n">prog_load_attr</span> <span class="o">=</span> <span class="p">&#123;</span>
       <span class="cm">/* 指定程序类型，这里为 XDP */</span>
                <span class="p">.</span><span class="n">prog_type</span>      <span class="o">=</span> <span class="n">BPF_PROG_TYPE_XDP</span><span class="p">,</span>
        <span class="p">&#125;;</span>
        <span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">optstr</span> <span class="o">=</span> <span class="s">"SN"</span><span class="p">;</span>
        <span class="kt">int</span> <span class="n">prog_fd</span><span class="p">,</span> <span class="n">map_fd</span><span class="p">,</span> <span class="n">opt</span><span class="p">;</span>
        <span class="k">struct</span> <span class="n">bpf_object</span> <span class="o">*</span><span class="n">obj</span><span class="p">;</span>
        <span class="k">struct</span> <span class="n">bpf_map</span> <span class="o">*</span><span class="n">map</span><span class="p">;</span>
        <span class="kt">char</span> <span class="n">filename</span><span class="p">[</span><span class="mi">256</span><span class="p">];</span>

        <span class="k">while</span> <span class="p">((</span><span class="n">opt</span> <span class="o">=</span> <span class="n">getopt</span><span class="p">(</span><span class="n">argc</span><span class="p">,</span> <span class="n">argv</span><span class="p">,</span> <span class="n">optstr</span><span class="p">))</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="p">&#123;</span>
                <span class="k">switch</span> <span class="p">(</span><span class="n">opt</span><span class="p">)</span> <span class="p">&#123;</span>
                <span class="k">case</span> <span class="sc">'S'</span><span class="p">:</span>
    <span class="cm">/* XDP 两种工作模式，第三篇文章会详细展开 */</span>
                        <span class="n">xdp_flags</span> <span class="o">|=</span> <span class="n">XDP_FLAGS_SKB_MODE</span><span class="p">;</span>
                        <span class="k">break</span><span class="p">;</span>
                <span class="k">case</span> <span class="sc">'N'</span><span class="p">:</span>
                        <span class="cm">/* XDP 两种工作模式，第三篇文章会详细展开 */</span>
                        <span class="n">xdp_flags</span> <span class="o">|=</span> <span class="n">XDP_FLAGS_DRV_MODE</span><span class="p">;</span>
                        <span class="k">break</span><span class="p">;</span>
                <span class="nl">default:</span>
                        <span class="n">usage</span><span class="p">(</span><span class="n">basename</span><span class="p">(</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]));</span>
                        <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
                <span class="p">&#125;</span>
        <span class="p">&#125;</span>

        <span class="cm">/* 省略不重要代码 */</span>
  
        <span class="n">snprintf</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="k">sizeof</span><span class="p">(</span><span class="n">filename</span><span class="p">),</span> <span class="s">"%s_kern.o"</span><span class="p">,</span> <span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]);</span>
        <span class="n">prog_load_attr</span><span class="p">.</span><span class="n">file</span> <span class="o">=</span> <span class="n">filename</span><span class="p">;</span>

        <span class="cm">/* 载入 eBPF 字节码至内核 */</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">bpf_prog_load_xattr</span><span class="p">(</span><span class="o">&</span><span class="n">prog_load_attr</span><span class="p">,</span> <span class="o">&</span><span class="n">obj</span><span class="p">,</span> <span class="o">&</span><span class="n">prog_fd</span><span class="p">))</span>
                <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>

        <span class="n">map</span> <span class="o">=</span> <span class="n">bpf_map__next</span><span class="p">(</span><span class="nb">NULL</span><span class="p">,</span> <span class="n">obj</span><span class="p">);</span>
        <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">map</span><span class="p">)</span> <span class="p">&#123;</span>
                <span class="n">printf</span><span class="p">(</span><span class="s">"finding a map in obj file failed</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
                <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
        <span class="p">&#125;</span>
        <span class="cm">/* 获得 eBPF 中定义的数据结构，用以获取统计信息 */</span>
        <span class="n">map_fd</span> <span class="o">=</span> <span class="n">bpf_map__fd</span><span class="p">(</span><span class="n">map</span><span class="p">);</span>

        <span class="cm">/* 省略不重要代码 */</span>

        <span class="cm">/* 设置 XDP 与网卡的绑定，eBPF 字节码将会在指定网卡收包路径执行  */</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">bpf_set_link_xdp_fd</span><span class="p">(</span><span class="n">ifindex</span><span class="p">,</span> <span class="n">prog_fd</span><span class="p">,</span> <span class="n">xdp_flags</span><span class="p">)</span> <span class="o"><</span> <span class="mi">0</span><span class="p">)</span> <span class="p">&#123;</span>
                <span class="n">printf</span><span class="p">(</span><span class="s">"link set xdp fd failed</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
                <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
        <span class="p">&#125;</span>

        <span class="cm">/* 定时从 map fd 中轮询统计数据 */</span>
        <span class="n">poll_stats</span><span class="p">(</span><span class="n">map_fd</span><span class="p">,</span> <span class="mi">2</span><span class="p">);</span>

        <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">&#125;</span>
</code></pre></div></div> <h2 id="编译运行">编译运行</h2> <p>在 Linux 源码仓库根目录执行 <code class="highlighter-rouge">make samples/bpf/</code>，编译完成后会在 <code class="highlighter-rouge">samples/bpf</code> 目录下会得到用户态可执行文件 <code class="highlighter-rouge">xdp1</code> 和 eBPF 字节码文件 <code class="highlighter-rouge">xdp1_kern.o</code>，直接在当前目录直接执行即可。如果是自己编写的代码，可以将文件放入 <code class="highlighter-rouge">samples/bpf</code> 目录下，并在 Makefile 中加入这对应文件的编译配置。</p> <p>如果遇到了任何环境或者编译的问题，可以参考内核文档 <code class="highlighter-rouge">samples/bpf/README.rst</code>。</p> <h1 id="基础概念">基础概念</h1> <p>通过上面的示例程序之后，想必大家已经对如何编写一个 eBPF 程序有了初步的印象。以刚才编写的程序为例，我们可以发现 eBPF 程序包含三个基础的概念：程序类型、数据结构和 helpers。</p> <h2 id="程序类型">程序类型</h2> <p>eBPF 的程序类型 (program type)，决定了 eBPF 程序如何载入内核，以及在内核哪些路径执行 eBPF 程序。例如需要 kprobe 跟踪函数执行，则需要在载入时指定 eBPF 程序的类型为 <code class="highlighter-rouge">BPF_PROG_TYPE_KPROBE</code> 。对于 XDP 则需要指定为 <code class="highlighter-rouge">BPF_PROG_TYPE_XDP</code>；</p> <p>以 XDP 类型 eBPF 程序为例，用户通过 netlink 调用 <code class="highlighter-rouge">dev_change_xdp_fd</code> 为指定 dev 设置 eBPF 程序，例如 veth 网卡 XDP 的支持在 4.14 内核引入，通过 <code class="highlighter-rouge">veth_xdp_set</code> 为网卡绑定 eBPF 字节码，当 NAPI poll 执行时于每个 XDP frame 依次调用 <code class="highlighter-rouge">veth_xdp_rcv_one</code>，并执行对应的 eBPF 程序，根据 eBPF 程序的返回结果决定丢弃、通过或者重定向报文。</p> <p>全量的程序类型定义在 <code class="highlighter-rouge">include/uapi/linux/bpf.h</code>，如需了解详细的程序类型请参考：<a href="https://github.com/iovisor/bcc/blob/master/docs/kernel-versions.md#program-types">BCC 文档</a>。</p> <h2 id="数据结构">数据结构</h2> <p>对于任何程序而言，都离不开各种各样的数据结构。eBPF 提供了各种常用的数据结构，从而实现内核内部数据的组织，以及用户态和内核态的通信；</p> <p>当前 eBPF 定义了26中基础的数据结构，涵盖了 hash、stack、array 和 ringbuf。以 hash 为例，可以指定 key、leaf 的数据类型以及大小，同时提供了相应的 helpers 操作函数 <code class="highlighter-rouge">BPF_FUNC_map_lookup_elem()</code> 和 <code class="highlighter-rouge">BPF_FUNC_map_push_elem() </code> 等。</p> <p>全量的数据结构定义在 <code class="highlighter-rouge">include/uapi/linux/bpf.h</code>，如需了解详细的数据结构列表请参考：<a href="https://github.com/iovisor/bcc/blob/master/docs/kernel-versions.md#tables-aka-maps">BCC 文档</a>。</p> <h2 id="helpers">Helpers</h2> <p>如同其他语言生态会提供丰富的 library，eBPF 也包含了各种常用的 helpers 函数，例如打印输出 <code class="highlighter-rouge">BPF_FUNC_trace_printk</code> 等；</p> <p>eBPF 定义的 helpers 函数不仅为了简化复杂的 eBPF 操作，同时也会将部分危险的操作封装成安全的 helpers 函数，对于内核数据结构的访问和操作需要借助 helper 完成，确保了 eBPF 程序的安全性。</p> <p>全量的 helpers 定义在 <code class="highlighter-rouge">include/uapi/linux/bpf.h</code>，详细的 helps 列表请参考：<a href="https://github.com/iovisor/bcc/blob/master/docs/kernel-versions.md#helpers">BCC 文档</a></p> <h1 id="快速上手的应用">快速上手的应用</h1> <p>学习并掌握一门技术的最好方式是付诸于实践。现在你的脑海中可能已经迸发出各种各样的想法，迫不及待编写 eBPF 程序验证和实践。为了更方便的去验证和实践，除了上面提到的基于 <code class="highlighter-rouge">samples/bpf</code> 示例程序之外，我们还可以基于下面一些社区已有的可供我们快速上手的应用。</p> <h2 id="bcc">BCC</h2> <p>BCC 是一个包含丰富的内核跟踪分析的 eBPF 工具集，用户也可以基于 BCC 创建自己的 eBPF 工具。当前 BCC 工具提供了 Python / Lua 和 Go 语言的 binding，用户可以使用这三种语言编写自己的 eBPF 工具。BCC 提供一个非常友好的 <a href="https://github.com/iovisor/bcc/blob/master/docs/tutorial_bcc_python_developer.md">tutorial</a> 可供大家快速上手。其中 <a href="https://github.com/iovisor/gobpf">iovisor/gobpf</a> 库，可以通过 Go 生态将 eBPF 与云原生、k8s 或各种运维工具相结合。</p> <h2 id="bpftrace">bpftrace</h2> <p>如果使用过 systemtap 动态跟踪分析内核，那么 bpftrace 是一个很好的替代方案。bpftrace 提供了一种类 awk 和 C 的语言，使用 bpftrace 语言编写各种跟踪和分析脚本，并编译成 eBPF 字节码与内核交互，从而实现动态跟踪 Linux 内核。使用文档可以参考：<a href="https://kernel.taobao.org/2020/01/Kernel-analysis-with-bpftrace/">使用 bpftrace 分析内核</a>，和 <a href="https://github.com/iovisor/bpftrace/blob/master/docs/tutorial_one_liners.md">The bpftrace One-Liner Tutorial</a>；</p> <h2 id="ubpf--generic-ebpf">ubpf / generic-ebpf</h2> <p>假如对于 eBPF 字节码和虚拟机非常感兴趣，<a href="https://github.com/iovisor/ubpf">ubpf</a> 提供了一个用户态实现的虚拟机，包含了解释运行和 JIT 特性。不仅帮助我们更好的理解 eBPF 虚拟机的实现，而且可以将 ubpf 嵌入到应用中，以执行编写好的 eBPF 程序，从而实现 Lua 或 WASM 的功能。<a href="https://github.com/generic-ebpf/generic-ebpf">generic-ebpf</a> 则更进一步，提供了更完善的运行时机制和库函数，并将 eBPF 作为一种通用的字节码嵌入到交换机等硬件中并运用在生产环境。</p> <h1 id="总结">总结</h1> <p>eBPF 为内核提供了更多的可能性，社区仍在不断拓宽 eBPF 的场景，通过这篇文章我们了解了如何编写 eBPF 程序，接下来几篇文章将会为大家带来 eBPF 在跟踪和网络方面的特性和应用。</p>   
</div>
            