
---
title: 'coost v3.0.0 (微型 boost 库)发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3197'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 11:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3197'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fidealvin%2Fcoost" target="_blank"><span style="color:#3498db">coost-A tiny boost library in C++11​</span></a></strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost" target="_blank">coost</a><span> </span>是一个<strong>兼具性能与易用性</strong>的跨平台 C++ 基础库，原名为 co，后改为 cocoyaxi，前者过短，后者过长，取中庸之道，又改为 coost。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">为什么叫 coost 呢？以前有朋友称之为小型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.boost.org%2F" target="_blank">boost</a><span> </span>库，比 boost 小一点，那就叫 coost 好了。它有多小呢？在<span> </span><strong>linux 与 mac 上编译出来的静态库仅 1M 左右大小</strong>。虽然小，却提供了足够强大的功能：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>命令行参数与配置文件解析库(flag)</li> 
 <li>高性能日志库(log)</li> 
 <li>单元测试框架(unitest)</li> 
 <li><strong>go-style 协程</strong></li> 
 <li>基于协程的网络编程框架</li> 
 <li>高效 JSON 库</li> 
 <li><strong>基于 JSON 的 RPC 框架</strong></li> 
 <li>面向玄学编程</li> 
 <li>原子操作(atomic)</li> 
 <li>随机数生成器(random)</li> 
 <li>高效字符流(fastream)</li> 
 <li>高效字符串(fastring)</li> 
 <li>字符串操作(str)</li> 
 <li>时间库(time)</li> 
 <li>线程库(thread)</li> 
 <li>定时任务调度器</li> 
 <li><strong>高性能内存分配器</strong></li> 
 <li>LruMap</li> 
 <li>hash 库</li> 
 <li>path 库</li> 
 <li>文件系统操作(fs)</li> 
 <li>系统操作(os)</li> 
</ul> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次发布的版本，直接从 v2.0.3 跳到了 v3.0.0，跨度非常之大，它在<strong>性能</strong>、<strong>易用性</strong>、<strong>稳定性</strong>等方面均有全面的提升。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">性能优化</h3> 
<h3 style="margin-left:0; margin-right:0; text-align:start">内存分配器</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中实现了一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Fmem.h" target="_blank">新的内存分配器(co/malloc)</a>，它不是通用的内存分配器，在<span> </span><code>free</code><span> </span>与<span> </span><code>realloc</code><span> </span>时，需要额外带上原内存块的 size 信息，这在使用时可能有一点点不便，但可以简化设计，提升内存分配器的性能。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">通用的内存分配器，像 ptmalloc, jemalloc, tcmalloc 以及 mimalloc 等，小内存释放后大概率会被它们缓存住，而并没有归还给操作系统，这可能<strong>造成释放大量小内存后内存占用量却始终不降的疑似内存泄漏的现象</strong>。co/malloc 对此做了优化，在兼顾性能的同时，会尽可能多的将释放的内存归还给操作系统，有利于降低程序的内存占用量，在实测中也取得了良好的效果。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">co/malloc 还提供了<span> </span><strong>co::stl_allocator</strong>，可以替换 STL 容器中默认的分配器 std::allocator。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Fstl.h" target="_blank">co/stl.h</a><span> </span>中提供了一些常用的替换 allocator 后的容器，与 std 版本相比有着性能上的优势。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">co/malloc 已经成为 coost 内部使用的默认内存分配器，像 fastring、fastream、Json 等均基于 co/malloc 实现。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Ftest%2Fmem.cc" target="_blank">co/test</a><span> </span>中提供了简单的测试代码，可以执行如下命令编译及运行：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text">xmake b mem
xmake r mem -t 4 -s</code></pre> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><code>-t</code><span> </span>指定线程数量，<code>-s</code><span> </span>表示与系统的内存分配器进行对比。下面是在不同系统中的测试结果(4线程)：</p> 
 <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; color:#121212; font-family:-apple-system,"> 
  <tbody> 
   <tr> 
    <th style="height:24px">os/cpu</th> 
    <th style="height:24px">co::alloc</th> 
    <th style="height:24px">co::free</th> 
    <th style="height:24px">::malloc</th> 
    <th style="height:24px">::free</th> 
    <th style="height:24px">speedup</th> 
   </tr> 
   <tr> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">win/AMD 3.2G</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">7.32</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">6.83</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">86.05</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">105.06</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">11.7/15.3</td> 
   </tr> 
   <tr> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">mac/i7 2.4G</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">9.91</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">9.86</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">55.64</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">60.20</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">5.6/6.1</td> 
   </tr> 
   <tr> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">linux/i7 2.2G</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">10.80</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">7.51</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1070.5</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">21.17</td> 
    <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">99.1/2.8</td> 
   </tr> 
  </tbody> 
 </table> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">上表中，时间单位为纳秒(ns)，linux 是在 Windows WSL 中运行的 ubuntu 系统，speedup 是 co/malloc 相对于系统内存分配器的性能提升倍数。可以看到<span> </span><strong>co::alloc 在 Linux 上比 ::malloc 提升了近 99 倍</strong>，这其中的一个重要原因是 ptmalloc 在多线程环境中锁竞争开销较大，而 co/malloc 在设计上尽可能避免了锁的使用，小块内存的分配、释放不需要锁，甚至在跨线程释放时连自旋锁也不用。</p> 
 <h3 style="margin-left:0; margin-right:0; text-align:start">原子操作</h3> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中，原子操作支持 memory order，以满足一些高性能应用场景的需求。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Fatomic.h" target="_blank">co/atomic.h</a><span> </span>中定义了 6 种 memory order，与 C++11 标准中保持一致：</p> 
 <div style="margin-left:0; margin-right:0; text-align:start"> 
  <pre style="margin-left:0; margin-right:0"><code class="language-cpp"><span>mo_relaxed</span>    <span>mo_consume</span>    <span>mo_acquire</span> 
<span>mo_release</span>    <span>mo_acq_rel</span>    <span>mo_seq_cst</span>
</code></pre> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>代码示例</li> 
  </ul> 
  <div style="margin-left:0; margin-right:0; text-align:start"> 
   <pre style="margin-left:0; margin-right:0"><code class="language-cpp"><span style="color:#175199">int</span> <span>i</span> <span>=</span> <span style="color:#056de8">0</span><span>;</span>
<span>uint64</span> <span>u</span> <span>=</span> <span style="color:#056de8">0</span><span>;</span>
<span>atomic_inc</span><span>(</span><span>&</span><span>i</span><span>,</span> <span>mo_relaxed</span><span>);</span>
<span>atomic_load</span><span>(</span><span>&</span><span>i</span><span>,</span> <span>mo_relaxed</span><span>);</span>
<span>atomic_add</span><span>(</span><span>&</span><span>u</span><span>,</span> <span style="color:#056de8">3</span><span>);</span> <em>// mo_seq_cst
</em><span>atomic_add</span><span>(</span><span>&</span><span>u</span><span>,</span> <span style="color:#056de8">7</span><span>,</span> <span>mo_acquire</span><span>);</span>
</code></pre> 
   <h3 style="margin-left:0; margin-right:0; text-align:start">易用性提升</h3> 
   <h3 style="margin-left:0; margin-right:0; text-align:start">简化初始化过程</h3> 
   <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v2.0.3 中，main 函数可能得像下面这样写：</p> 
   <div style="margin-left:0; margin-right:0; text-align:start"> 
    <pre style="margin-left:0; margin-right:0"><code class="language-cpp"><span style="color:#999999">#include</span> <span>"co/flag.h"</span><span style="color:#999999">
</span><span style="color:#999999">#include</span> <span>"co/log.h"</span><span style="color:#999999">
</span><span style="color:#999999">#include</span> <span>"co/co.h"</span><span style="color:#999999">
</span>
<span style="color:#175199">int</span> <span style="color:#f1403c">main</span><span>(</span><span style="color:#175199">int</span> <span>argc</span><span>,</span> <span style="color:#175199">char</span><span>**</span> <span>argv</span><span>)</span> <span>&#123;</span>
    <span>flag</span><span>::</span><span>init</span><span>(</span><span>argc</span><span>,</span> <span>argv</span><span>);</span>
    <span>log</span><span>::</span><span>init</span><span>();</span>
    <span>co</span><span>::</span><span>init</span><span>();</span>
    <em>// do something here...
</em>    <span>co</span><span>::</span><span>exit</span><span>();</span>
    <span>return</span> <span style="color:#056de8">0</span><span>;</span>
<span>&#125;</span>
</code></pre> 
    <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">为了提升用户的使用体验，v3.0 中移除了<span> </span><code>log::init()</code>、<code>co::init()</code>、<code>co::exit()</code><span> </span>等 API，现在 main 函数可以写成下面这样：</p> 
    <div style="margin-left:0; margin-right:0; text-align:start"> 
     <pre style="margin-left:0; margin-right:0"><code class="language-cpp"><span style="color:#999999">#include</span> <span>"co/flag.h"</span><span style="color:#999999">
</span>
<span style="color:#175199">int</span> <span style="color:#f1403c">main</span><span>(</span><span style="color:#175199">int</span> <span>argc</span><span>,</span> <span style="color:#175199">char</span><span>**</span> <span>argv</span><span>)</span> <span>&#123;</span>
    <span>flag</span><span>::</span><span>init</span><span>(</span><span>argc</span><span>,</span> <span>argv</span><span>);</span>
    <em>// do something here...
</em>    <span>return</span> <span style="color:#056de8">0</span><span>;</span>
<span>&#125;</span>
</code></pre> 
     <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中，整个 coost 库唯一需要调用的初始化接口就是<span> </span><code>flag::init()</code>，该接口用于解析命令行参数及配置文件。</p> 
     <h3 style="margin-left:0; margin-right:0; text-align:start">flag</h3> 
     <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Fflag.h" target="_blank">co/flag</a><span> </span>是一个简单易用的命令行参数与配置文件解析库，coost 中的日志、协程、RPC框架等组件会用它定义配置项。</p> 
     <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中，对一些细节处进行了改进，如<span> </span><strong>--help</strong><span> </span>只显示用户自己定义的 flag，而不会显示 coost 内部定义的 flag。</p> 
     <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 还新增了 flag 别名功能，在定义 flag 时，可以指定任意数量的别名：</p> 
     <div style="margin-left:0; margin-right:0; text-align:start"> 
      <pre style="margin-left:0; margin-right:0"><code class="language-cpp"><span>DEF_bool</span><span>(</span><span>debug</span><span>,</span> <span style="color:#056de8">false</span><span>,</span> <span style="color:#f1403c">""</span><span>);</span>         <em>// no alias
</em><span>DEF_bool</span><span>(</span><span>debug</span><span>,</span> <span style="color:#056de8">false</span><span>,</span> <span style="color:#f1403c">""</span><span>,</span> <span>d</span><span>);</span>      <em>// d is an alias of debug
</em><span>DEF_bool</span><span>(</span><span>debug</span><span>,</span> <span style="color:#056de8">false</span><span>,</span> <span style="color:#f1403c">""</span><span>,</span> <span>d</span><span>,</span> <span>dbg</span><span>);</span> <em>// 2 aliases
</em></code></pre> 
      <h3 style="margin-left:0; margin-right:0; text-align:start">日志</h3> 
      <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v2.0.3 中，co/log 提供类似 google glog 的日志功能，将日志分成 debug、info、warning、error、fatal等级别。v3.0 中，<strong>新增 TLOG</strong>，即按 topic 分类的日志，不同 topic 的日志输出到不同的文件。</p> 
      <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中，co/log 不需要用户手动初始化，包含<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Flog.h" target="_blank">co/log.h</a><span> </span>即可使用，不需要特别的设置。</p> 
      <div style="margin-left:0; margin-right:0; text-align:start"> 
       <pre style="margin-left:0; margin-right:0; text-align:start"><code class="language-cpp"><span style="color:#999999">#include</span> <span>"co/log.h"</span><span style="color:#999999">
</span>
<span style="color:#175199">int</span> <span style="color:#f1403c">main</span><span>(</span><span style="color:#175199">int</span> <span>argc</span><span>,</span> <span style="color:#175199">char</span><span>**</span> <span>argv</span><span>)</span> <span>&#123;</span>
    <span>flag</span><span>::</span><span>init</span><span>(</span><span>argc</span><span>,</span> <span>argv</span><span>);</span>

    <span>DLOG</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span> <em>// debug
</em>    <span>LOG</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span>  <em>// info
</em>    <span>WLOG</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span> <em>// warning
</em>    <span>ELOG</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span> <em>// error
</em>    <span>FLOG</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span> <em>// fatal
</em>    <span>TLOG</span><span>(</span><span style="color:#f1403c">"rpc"</span><span>)</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span>
    <span>TLOG</span><span>(</span><span style="color:#f1403c">"xxx"</span><span>)</span> <span><<</span> <span style="color:#f1403c">"hello "</span> <span><<</span> <span style="color:#056de8">23</span><span>;</span>

    <span>return</span> <span style="color:#056de8">0</span><span>;</span>
<span>&#125;</span></code></pre> 
       <h3 style="margin-left:0; margin-right:0; text-align:start">JSON</h3> 
       <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v2.0.3 中，JSON 对象构建在连续内存上，可以减少内存分配、提升性能，但易用性会降低。v3.0 中有了 co/malloc，JSON 采用了更加灵活的实现方式，在保持高性能的同时，易用性方面也有了质的提升。</p> 
       <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Ftree%2Fbenchmark%2Fbenchmark" target="_blank">co/json 与 rapidjson 的性能比较</a></strong></p> 
       <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; color:#121212; font-family:-apple-system,"> 
        <tbody> 
         <tr> 
          <th style="height:24px">os</th> 
          <th style="height:24px">co/json stringify</th> 
          <th style="height:24px">co/json parse</th> 
          <th style="height:24px">rapidjson stringify</th> 
          <th style="height:24px">rapidjson parse</th> 
          <th style="height:24px">speedup</th> 
         </tr> 
         <tr> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">win</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">569</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">924</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">2089</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">2495</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">3.6/2.7</td> 
         </tr> 
         <tr> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">mac</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">783</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1097</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1289</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1658</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1.6/1.5</td> 
         </tr> 
         <tr> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">linux</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">468</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">764</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1359</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">1070</td> 
          <td style="border-color:#d3d3d3; border-style:solid; border-width:1px; height:24px">2.9/1.4</td> 
         </tr> 
        </tbody> 
       </table> 
       <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">上表是将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fraw.githubusercontent.com%2Fsimdjson%2Fsimdjson%2Fmaster%2Fjsonexamples%2Ftwitter.json" target="_blank">twitter.json</a><span> </span>最小化后的测试结果，耗时单位为微秒(us)，speedup 是 co/json 相对于 rapidjson 的性能提升倍数。</p> 
       <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中实现了<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Fjson.h" target="_blank">Json</a></strong><span> </span>类，它采用<strong>流畅(fluent)接口设计</strong>，用起来更加方便。</p> 
       <div style="margin-left:0; margin-right:0; text-align:start"> 
        <pre style="margin-left:0; margin-right:0; text-align:start"><code class="language-cpp"><em>// &#123;"a":23,"b":false,"s":"123","v":[1,2,3],"o":&#123;"xx":0&#125;&#125;
</em><span>Json</span> <span>x</span> <span>=</span> <span>&#123;</span>
    <span>&#123;</span> <span style="color:#f1403c">"a"</span><span>,</span> <span style="color:#056de8">23</span> <span>&#125;,</span>
    <span>&#123;</span> <span style="color:#f1403c">"b"</span><span>,</span> <span style="color:#056de8">false</span> <span>&#125;,</span>
    <span>&#123;</span> <span style="color:#f1403c">"s"</span><span>,</span> <span style="color:#f1403c">"123"</span> <span>&#125;,</span>
    <span>&#123;</span> <span style="color:#f1403c">"v"</span><span>,</span> <span>&#123;</span><span style="color:#056de8">1</span><span>,</span><span style="color:#056de8">2</span><span>,</span><span style="color:#056de8">3</span><span>&#125;</span> <span>&#125;,</span>
    <span>&#123;</span> <span style="color:#f1403c">"o"</span><span>,</span> <span>&#123;</span>
        <span>&#123;</span><span style="color:#f1403c">"xx"</span><span>,</span> <span style="color:#056de8">0</span><span>&#125;</span>
    <span>&#125;&#125;,</span>
<span>&#125;;</span>

<em>// equal to x
</em><span>Json</span> <span>y</span> <span>=</span> <span>Json</span><span>()</span>
    <span>.</span><span>add_member</span><span>(</span><span style="color:#f1403c">"a"</span><span>,</span> <span style="color:#056de8">23</span><span>)</span>
    <span>.</span><span>add_member</span><span>(</span><span style="color:#f1403c">"b"</span><span>,</span> <span style="color:#056de8">false</span><span>)</span>
    <span>.</span><span>add_member</span><span>(</span><span style="color:#f1403c">"s"</span><span>,</span> <span style="color:#f1403c">"123"</span><span>)</span>
    <span>.</span><span>add_member</span><span>(</span><span style="color:#f1403c">"v"</span><span>,</span> <span>Json</span><span>().</span><span>push_back</span><span>(</span><span style="color:#056de8">1</span><span>).</span><span>push_back</span><span>(</span><span style="color:#056de8">2</span><span>).</span><span>push_back</span><span>(</span><span style="color:#056de8">3</span><span>))</span>
    <span>.</span><span>add_member</span><span>(</span><span style="color:#f1403c">"o"</span><span>,</span> <span>Json</span><span>().</span><span>add_member</span><span>(</span><span style="color:#f1403c">"xx"</span><span>,</span> <span style="color:#056de8">0</span><span>));</span>

<span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"a"</span><span>).</span><span>as_int</span><span>();</span>       <em>// 23
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"s"</span><span>).</span><span>as_string</span><span>();</span>    <em>// "123"
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"s"</span><span>).</span><span>as_int</span><span>();</span>       <em>// 123, string -> int
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"v"</span><span>,</span> <span style="color:#056de8">0</span><span>).</span><span>as_int</span><span>();</span>    <em>// 1
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"v"</span><span>,</span> <span style="color:#056de8">2</span><span>).</span><span>as_int</span><span>();</span>    <em>// 3
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"o"</span><span>,</span> <span style="color:#f1403c">"xx"</span><span>).</span><span>as_int</span><span>();</span> <em>// 0
</em>
<span>x</span><span>[</span><span style="color:#f1403c">"a"</span><span>]</span> <span>==</span> <span style="color:#056de8">23</span><span>;</span>          <em>// true
</em><span>x</span><span>[</span><span style="color:#f1403c">"s"</span><span>]</span> <span>==</span> <span style="color:#f1403c">"123"</span><span>;</span>       <em>// true
</em><span>x</span><span>.</span><span>get</span><span>(</span><span style="color:#f1403c">"o"</span><span>,</span> <span style="color:#f1403c">"xx"</span><span>)</span> <span>!=</span> <span style="color:#056de8">0</span><span>;</span> <em>// false</em></code></pre> 
        <h3 style="margin-left:0; margin-right:0; text-align:start">RPC</h3> 
        <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中，<strong>RPC 框架新增对 HTTP 协议的支持，将 RPC 服务与 HTTP 服务融为一体</strong>。</p> 
        <div style="margin-left:0; margin-right:0; text-align:start"> 
         <pre style="margin-left:0; margin-right:0; text-align:start"><code class="language-cpp"><span style="color:#999999">#include</span> <span>"co/all.h"</span><span style="color:#999999">
</span>
<span style="color:#175199">int</span> <span style="color:#f1403c">main</span><span>(</span><span style="color:#175199">int</span> <span>argc</span><span>,</span> <span style="color:#175199">char</span><span>**</span> <span>argv</span><span>)</span> <span>&#123;</span>
    <span>flag</span><span>::</span><span>init</span><span>(</span><span>argc</span><span>,</span> <span>argv</span><span>);</span>

    <span>rpc</span><span>::</span><span>Server</span><span>()</span>
        <span>.</span><span>add_service</span><span>(</span><span>new</span> <span>xx</span><span>::</span><span>HelloWorldImpl</span><span>)</span>
        <span>.</span><span>start</span><span>(</span><span style="color:#f1403c">"127.0.0.1"</span><span>,</span> <span style="color:#056de8">7788</span><span>,</span> <span style="color:#f1403c">"/xx"</span><span>);</span>

    <span>for</span> <span>(;;)</span> <span>sleep</span><span>::</span><span>sec</span><span>(</span><span style="color:#056de8">80000</span><span>);</span>
    <span>return</span> <span style="color:#056de8">0</span><span>;</span>
<span>&#125;</span></code></pre> 
         <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><code>rpc::Server</code><span> </span>可以添加多个 service，调用<span> </span><code>start()</code><span> </span>方法即可启动 RPC 服务，该方法的第 3 个参数指定 HTTP 服务的 URL。用户可以通过<span> </span><code>rpc::Client</code><span> </span>调用其服务，也可以通过 HTTP 的方式调用其服务，如：</p> 
         <div style="margin-left:0; margin-right:0; text-align:start"> 
          <pre style="margin-left:0; margin-right:0"><code class="language-text">curl http://127.0.0.1:7788/xx --request POST --data '&#123;"api":"ping"&#125;'
curl http://127.0.0.1:7788/xx --request POST --data '&#123;"api":"HelloWorld.hello"&#125;'</code></pre> 
          <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">RPC 请求或 HTTP 请求的 body 部分是 JSON 字符串，需要用<span> </span><strong>api</strong><span> </span>字段指明调用的方法，该字段的值一般为<span> </span><strong>service.method</strong><span> </span>形式。<strong>ping</strong><span> </span>则是 coost RPC 框架内置的特殊 service，可用于发送心跳或测试。</p> 
          <h3 style="margin-left:0; margin-right:0; text-align:start">稳定性提升</h3> 
          <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">coost 提供了一套简单易用的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Fblob%2Fmaster%2Finclude%2Fco%2Funitest.h" target="_blank">单元测试框架</a>，并且在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Ftree%2Fmaster%2Funitest" target="_blank">unitest</a><span> </span>目录下提供了大量的单元测试代码，几乎覆盖了 coost 内部的所有组件，为 coost 的稳定性提供了重要的保障。</p> 
          <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">v3.0 中又新增了不少单元测试代码，进一步提高了单元测试覆盖率。另外，针对一些不便编写单元测试的功能，coost 在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fcoost%2Ftree%2Fmaster%2Ftest" target="_blank">test</a><span> </span>目录下单独提供了大量的测试代码。</p> 
         </div> 
        </div> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            