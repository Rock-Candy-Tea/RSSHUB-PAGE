
---
title: 'iOS符号解析重构之路'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d659396b1016478587b1268ce550ff58~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 02:35:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d659396b1016478587b1268ce550ff58~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d659396b1016478587b1268ce550ff58~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>作者：字节跳动终端技术 —— 丰亚东</p>
</blockquote>
<h1 data-id="heading-0">背景</h1>
<h2 data-id="heading-1">什么是符号解析</h2>
<p>所谓的符号解析就是就是将崩溃日志中的地址映射成为可读的符号和源文件中的行号，方便开发者定位和修复问题。如下图，第一份完全不可读的崩溃日志经过完整的符号解析变成了第三份完全可读的日志。对于字节的稳定性监控平台而言，需要支持iOS端的崩溃/卡死 /卡顿/自定义异常等各种日志类型的反解，因此符号解析也是监控平台必备的一项底层基础能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a56ff14fe194dd0a6149b4e91d4a433~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">系统原生符号解析工具</h2>
<h3 data-id="heading-3"><strong>symbolicatecrash</strong></h3>
<p>Xcode 提供的 <code>symbolicatecrash</code>。该命令位于： <code>/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash</code>，是一个perl 脚本，里面整合了逐步解析的操作（也可以将命令拷贝出来，直接进行调用）。</p>
<p>用法：<code>symbolicatecrash log.crash -d xxx.app.dSYM</code>。</p>
<p>优点：能非常方便的符号化整份crash日志。</p>
<p>缺点：</p>
<ol>
<li>耗时比较久。</li>
<li>粒度比较粗，无法符号化特定的某一行。</li>
</ol>
<h3 data-id="heading-4">atos</h3>
<p>用法：<code>atos -o xxx.app.dSYM/Contents/Resources/DWARF/xxx -arch arm64/armv7 -l loadAddress runtimeAddress</code></p>
<p>优点：速度快，可以符号化特定的某一行，方便上层做缓存。</p>
<h2 data-id="heading-5">原生工具的问题</h2>
<p>但是上面的这两个工具都有两个最大的缺陷就是：</p>
<ol>
<li>都仅仅是单机的工具，无法作为在线服务提供。</li>
<li>必须依赖macOS系统，因为字节服务端基建全部基于Linux，导致无法复用集团各种平台和框架，这就带来了非常高的机器成本，部署成本和运维成本。</li>
</ol>
<h1 data-id="heading-6">历史方案探索</h1>
<p>为了解决这两大痛点，搭建一套Linux上可以提供iOS在线符号解析的服务，历史上我们依次做了如下探索：</p>
<h2 data-id="heading-7">方案1:llvm-atosl</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059df51c782b4d1fa2f70fdf0e5f8932~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这其实就是基于llvm自带的符号解析工具做了一些定制化的改造。</p>
<p>单行日志在线解析流程图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6079eca28a944deb8b4e3b5b54c1e482~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这套方案起初没有太大的问题，但是随着时间的推移，晚高峰期间经常出现因为解析超时导致解析失败进而只能看到地址偏移而看不到符号的问题，因此还需要找到瓶颈再进一步优化。</p>
<h2 data-id="heading-8">方案2:llvm-atosl-cgo</h2>
<p>其实就是将llvm-atosl工具通过<code>cgo</code>而不是命令行形式调用。</p>
<p>方案1上线之后我们观察到在晚高峰期间单行解析pct99非常夸张，因为超时导致的解析失败越来越多，甚至有一次晚高峰期间整个服务直接夯住，登录到线上机器看到大量<code>too many open files</code>报错，当时怀疑到是fd占用超过上限，又联想到每次执行llvm-atosl脚本会占用至少3个fd（stdin，stdout和stderr），因此我们尝试将llvm-atosl从命令行工具的形式封装为一个c的library，再通过<code>cgo</code>在golang侧调用：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-comment">/*
#cgo CFLAGS: -I./tools
#cgo LDFLAGS: -lstdc++ -lncurses -lm -L$&#123;SRCDIR&#125;/tools/ -lllvm-atosl
#include "llvm-atosl-api.h"
#include <stdlib.h>
*/</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"C"</span>

<span class="hljs-keyword">import</span> (
  <span class="hljs-string">"fmt"</span>
  <span class="hljs-string">"strconv"</span>
  <span class="hljs-string">"strings"</span>
  <span class="hljs-string">"unsafe"</span>
)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
    result = symbolicate(<span class="hljs-string">"~/dsym/7.8.0(78007)eb7dd4d73df0329692003523fc2c9586/Aweme.app.dSYM/Contents/Resources/DWARF/Aweme"</span>,<span class="hljs-string">"arm64"</span>,<span class="hljs-string">"0x100008000"</span>,<span class="hljs-string">"0x0000000102cff4b8"</span>);
    fmt.Println(result)
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">symbolicate</span><span class="hljs-params">(go_path <span class="hljs-keyword">string</span>, go_arch <span class="hljs-keyword">string</span>, go_loadAddress <span class="hljs-keyword">string</span>, go_address <span class="hljs-keyword">string</span>)</span> <span class="hljs-title">string</span></span> &#123;
    c_path := C.CString(go_path)
    c_arch := C.CString(go_arch)

    loadAddress := hex2int(go_loadAddress)
    c_loadAddress := C.ulong(loadAddress)

    address := hex2int(go_address)
    c_address := C.ulong(address)

    c_result := C.getSymbolicatedName(c_path, c_arch, c_loadAddress, c_address)

    result := C.GoString(c_result)

    C.free(unsafe.Pointer(c_path))
    C.free(unsafe.Pointer(c_arch))
    C.free(unsafe.Pointer(c_result))

    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">hex2int</span><span class="hljs-params">(hexStr <span class="hljs-keyword">string</span>)</span> <span class="hljs-title">uint64</span></span> &#123;
     <span class="hljs-comment">// remove 0x suffix if found in the input string</span>
     cleaned := strings.Replace(hexStr, <span class="hljs-string">"0x"</span>, <span class="hljs-string">""</span>, <span class="hljs-number">-1</span>)

     <span class="hljs-comment">// base 16 for hexadecimal</span>
     result, _ := strconv.ParseUint(cleaned, <span class="hljs-number">16</span>, <span class="hljs-number">64</span>)
     <span class="hljs-keyword">return</span> <span class="hljs-keyword">uint64</span>(result)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本以为从跨进程调用切换到进程内调用，可以同时减少fd的占用和进程间通信的开销，但是上线之后解析的效率不仅没有提升，反而下降了。</p>
<p>参考一篇博客《如何把Go调用C的性能提升10倍？》（链接见参考资料[1]）中的结论，<code>cgo</code>性能不佳的两大原因：</p>
<ol>
<li>线程的栈在Go运行时是比较少的，受到P(Processor，可以理解为goroutine的管理调度者)以及M(Machine，可以理解为物理线程)数量的限制，一般可以简单的理解成受到<code>GOMAXPROCS</code>限制，go 1.5 版本之后的<code>GOMAXPROCS</code>默认是机器CPU核数，因此一旦<code>cgo</code>并发调用的方法数量超过<code>GOMAXPROCS</code>，就会发生调用阻塞。</li>
<li>由于需要同时保留C/C++的运行时，<code>cgo</code>需要在两个运行时和两个ABI（抽象二进制接口）之间做翻译和协调。这就带来了很大的开销。</li>
</ol>
<p>这说明关于fd占用过多以及跨进程调用的性能瓶颈的猜想其实是不成立的，<strong>因此这个方案也被证实是不可行的</strong>。</p>
<h2 data-id="heading-9">方案3:golang-atos</h2>
<p>基于golang原生的系统库<code>debug/dwarf</code>，可以实现对DWARF文件的解析，将地址解析为符号，可以替换llvm-atosl的实现，并且可以天然利用golang协程的特性实现高并发。实现方案可以参考下面这段源码：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> dwarfexample
<span class="hljs-keyword">import</span> (
    <span class="hljs-string">"debug/macho"</span>
    <span class="hljs-string">"debug/dwarf"</span>
    <span class="hljs-string">"log"</span>
    <span class="hljs-string">"github.com/go-errors/errors"</span>)
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">ParseFile</span><span class="hljs-params">(path <span class="hljs-keyword">string</span>, address <span class="hljs-keyword">int64</span>)</span> <span class="hljs-params">(err error)</span></span> &#123;
    <span class="hljs-keyword">var</span> f *macho.FatFile
    <span class="hljs-keyword">if</span> f, err = macho.OpenFat(path); err != <span class="hljs-literal">nil</span> &#123;
        <span class="hljs-keyword">return</span> errors.New(<span class="hljs-string">"open file error: "</span> + err.Error())
    &#125;

    <span class="hljs-keyword">var</span> d *dwarf.Data
    <span class="hljs-keyword">if</span> d, err = f.Arches[<span class="hljs-number">1</span>].DWARF(); err != <span class="hljs-literal">nil</span> &#123;
        <span class="hljs-keyword">return</span>
    &#125;

    r := d.Reader()

    <span class="hljs-keyword">var</span> entry *dwarf.Entry
    <span class="hljs-keyword">if</span> entry, err = r.SeekPC(address); err != <span class="hljs-literal">nil</span> &#123;
        log.Print(<span class="hljs-string">"Not Found ..."</span>)
        <span class="hljs-keyword">return</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        log.Print(<span class="hljs-string">"Found ..."</span>)
    &#125;

    log.Printf(<span class="hljs-string">"tag: %+v, lowpc: %+v"</span>, entry.Tag, entry.Val(dwarf.AttrLowpc))

    <span class="hljs-keyword">var</span> lineReader *dwarf.LineReader
    <span class="hljs-keyword">if</span> lineReader, err = d.LineReader(entry); err != <span class="hljs-literal">nil</span> &#123;
        <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">var</span> line dwarf.LineEntry

    <span class="hljs-keyword">if</span> err = lineReader.SeekPC(<span class="hljs-number">0x1005AC550</span>, &line); err != <span class="hljs-literal">nil</span> &#123;
        <span class="hljs-keyword">return</span>
    &#125;

    log.Printf(<span class="hljs-string">"line %+v:%+v"</span>, line.File.Name, line.Line)

    <span class="hljs-keyword">return</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在单元测试的时候发现golang-atos单行解析的效率比llvm-atosl的解析效率慢10倍，原因是对DWARF文件的解析golang版本的实现就是要比llvm的C++版本更耗时。<strong>因此这个方案也不可行</strong>。</p>
<h1 data-id="heading-10">终极解决方案</h1>
<h2 data-id="heading-11">方案整体设计</h2>
<p>后来通过监控发现，每次解析效率降低，大量报错的时候，存储符号表文件的分布式文件系统CephFS的读流量都特别高：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79258598e0864d30b87b6112946bd640~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d1de2d3f84b4a8e8e5671bd6abf2ef2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这才意识到符号解析的真正瓶颈在<strong>网络IO</strong>，因为抖音和头条等一些超级App的符号表文件大小经常超过1GB，而且每天内测包上传的数量非常多，虽然符号表在物理机本地有缓存，但是总有一些长尾的符号表是无法命中缓存的，在晚高峰期间需要从分布式文件系统向后端容器实例同步，同时也因为符号解析是随机的分发到集群中的某台物理机，因此会放大这个问题：网络IO流量越高，符号解析就越慢，符号解析越慢，就越容易堆积，反过来可能造成网络IO流量更高，这样一个恶性循环最终可能导致整个服务完全夯住。</p>
<p>我们最终采用了符号表上传时全量解析符号表文件中地址与符号的映射关系，线上直接查在线缓存的终极解决方案：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/798aeaedeffd4534929eb8f88b9a1a84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>核心改动点：</p>
<ol>
<li>将符号和地址的映射从崩溃时查找对应的符号表文件调用命令行工作解析改成了符号表文件上传时全量预解析所有地址与符号的映射关系，然后将映射关系结构化存储，崩溃时查找缓存即可。</li>
<li>为了解决部分C++与Rust符号demangle失效以及各种语言demangle工具不一致的问题。将原本llvm自带的demangle工具替换成了一个Rust实现，支持全语言的demangle工具symbolic-demangle（链接见参考资料[2]），极大的降低了运维成本。</li>
<li>优先采用新方案做符号解析，新方案没命中放量或者新方案解析失败用老方案做兜底。</li>
</ol>
<h2 data-id="heading-12">方案实现细节</h2>
<h3 data-id="heading-13">符号表文件格式</h3>
<h4 data-id="heading-14">DWARF</h4>
<h5 data-id="heading-15">文件结构</h5>
<p>DWARF 是一种调试信息格式，通常用于源码级别调试，也可用于从运行时地址还原源码对应的符号以及行号的工具(如: atos)。</p>
<p>Xcode打包如果在Build Options -> Debug Infomation format 设置了<code>DWARF with dSYM</code>之后，Xcode会生成一个 dSYM 文件，其中显式包含DWARF从而帮助我们根据地址，找到方法符号及文件名和行号等信息，方便开发者在版本正式发布之后排查问题。</p>
<p>我们以AwemeDylib.framework.dSYM中的DWARF文件为例，用macOS下的file指令观察下它的文件类型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fda419c4f4454eb2b522f10792c5835c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图可以看出来，DWARF其实也是Mach-O文件的一种类型，因此它也可以用MachOView工具打开分析。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de1adc939a9e476bbdbed0f9e86ae9cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图中看到它的Mach-O文件的类型是<code>MH_DSYM</code>。既然是Mach-O文件，使用size命令可以查看AwemeDylib这个DWARF文件中包含的Segment和Section，以arm64架构为例：</p>
<pre><code class="copyable">~/Downloads/dwarf/AwemeDylib.framework.dSYM/Contents/Resources/DWARF > size -x -m -l AwemeDylib
AwemeDylib (for architecture arm64):
Segment __TEXT: 0x18a4000 (vmaddr 0x0 fileoff 0)
        Section __text: 0x130fd54 (addr 0x5640 offset 0)
        Section __stubs: 0x89d0 (addr 0x1315394 offset 0)
        Section __stub_helper: 0x41c4 (addr 0x131dd64 offset 0)
        Section __const: 0x1a4358 (addr 0x1321f40 offset 0)
        Section __objc_methname: 0x47c15 (addr 0x14c6298 offset 0)
        Section __objc_classname: 0x45cd (addr 0x150dead offset 0)
        Section __objc_methtype: 0x3a0e6 (addr 0x151247a offset 0)
        Section __cstring: 0x1bf8e4 (addr 0x154c560 offset 0)
        Section __gcc_except_tab: 0x1004b8 (addr 0x170be44 offset 0)
        Section __ustring: 0x1d46 (addr 0x180c2fc offset 0)
        Section __unwind_info: 0x67c40 (addr 0x180e044 offset 0)
        Section __eh_frame: 0x2e368 (addr 0x1875c88 offset 0)
        total 0x189e992
Segment __DATA: 0x5f8000 (vmaddr 0x18a4000 fileoff 0)
        Section __got: 0x4238 (addr 0x18a4000 offset 0)
        Section __la_symbol_ptr: 0x5be0 (addr 0x18a8238 offset 0)
        Section __mod_init_func: 0x1850 (addr 0x18ade18 offset 0)
        Section __const: 0x146cb0 (addr 0x18af670 offset 0)
        Section __cfstring: 0x1b2c0 (addr 0x19f6320 offset 0)
        Section __objc_classlist: 0x1680 (addr 0x1a115e0 offset 0)
        Section __objc_nlclslist: 0x28 (addr 0x1a12c60 offset 0)
        Section __objc_catlist: 0x208 (addr 0x1a12c88 offset 0)
        Section __objc_protolist: 0x2f0 (addr 0x1a12e90 offset 0)
        Section __objc_imageinfo: 0x8 (addr 0x1a13180 offset 0)
        Section __objc_const: 0xb2dc8 (addr 0x1a13188 offset 0)
        Section __objc_selrefs: 0xf000 (addr 0x1ac5f50 offset 0)
        Section __objc_protorefs: 0x48 (addr 0x1ad4f50 offset 0)
        Section __objc_classrefs: 0x16a8 (addr 0x1ad4f98 offset 0)
        Section __objc_superrefs: 0x1098 (addr 0x1ad6640 offset 0)
        Section __objc_ivar: 0x42c4 (addr 0x1ad76d8 offset 0)
        Section __objc_data: 0xe100 (addr 0x1adb9a0 offset 0)
        Section __data: 0xc0d20 (addr 0x1ae9aa0 offset 0)
        Section HMDModule: 0x50 (addr 0x1baa7c0 offset 0)
        Section __bss: 0x1e9038 (addr 0x1baa820 offset 0)
        Section __common: 0x1058e0 (addr 0x1d93860 offset 0)
        total 0x5f511c
Segment __LINKEDIT: 0x609000 (vmaddr 0x1e9c000 fileoff 4096)
Segment __DWARF: 0x2a51000 (vmaddr 0x24a5000 fileoff 6332416)
        Section __debug_line: 0x3e96b7 (addr 0x24a5000 offset 6332416)
        Section __debug_pubnames: 0x16ca3a (addr 0x288e6b7 offset 10434231)
        Section __debug_pubtypes: 0x2e111a (addr 0x29fb0f1 offset 11927793)
        Section __debug_aranges: 0xf010 (addr 0x2cdc20b offset 14946827)
        Section __debug_info: 0x12792a4 (addr 0x2ceb21b offset 15008283)
        Section __debug_ranges: 0x567b0 (addr 0x3f644bf offset 34378943)
        Section __debug_loc: 0x674483 (addr 0x3fbac6f offset 34733167)
        Section __debug_abbrev: 0x2637 (addr 0x462f0f2 offset 41500914)
        Section __debug_str: 0x5d0e9e (addr 0x4631729 offset 41510697)
        Section __apple_names: 0x1a6984 (addr 0x4c025c7 offset 47609287)
        Section __apple_namespac: 0x1b90 (addr 0x4da8f4b offset 49340235)
        Section __apple_types: 0x137666 (addr 0x4daaadb offset 49347291)
        Section __apple_objc: 0x13680 (addr 0x4ee2141 offset 50622785)
        total 0x2a507c1
total 0x4ef6000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到有一个名为 <code>__DWARF</code> 的 Segment, 下面包含 <code>__debug_line</code>, <code>__debug_aranges</code>, <code>__debug_info </code>等很多类Section。我们可以使用<code>dwarfdump</code>来探索DWARF段中的内容，例如输入命令<code>dwarfdump AwemeDylib --debug-info</code> 可展示<code>__debug_info</code>Section下已经格式化之后的内容。关于<code>dwarfdump</code>指令的完整用法可以参考llvm工具链的官方文档（链接见参考资料[3]）。</p>
<p>参考《DWARF文件格式官方文档》（链接见参考资料[4]），这些section之间的关系如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2319ae1ff9964077b205a42a0a64fff8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-16">debug_info</h5>
<p><code>debug_info</code>section是DWARF文件中最核心的信息。DWARF 用<code>The Debugging Information Entry</code> (DIE) 来以统一的形式描述这些信息，每个DIE包含:</p>
<ul>
<li>一个 TAG 属性表达描述什么类型的元素, 如: <code>DW_TAG_subprogram</code>(函数)、<code>DW_TAG_formal_parameter</code>(形式参数)、<code>DW_TAG_variable</code>(变量)、<code>DW_TAG_base_type</code>(基础类型)。</li>
<li>N 个属性(attribute)， 用于具体描述一个DIE。</li>
</ul>
<p>下面是一段示例：</p>
<pre><code class="copyable">0x0049622c:   DW_TAG_subprogram
                DW_AT_low_pc        (0x000000000030057c)
                DW_AT_high_pc        (0x0000000000300690)
                DW_AT_frame_base        (DW_OP_reg29 W29)
                DW_AT_object_pointer        (0x0049629e)
                DW_AT_name        ("+[SSZipArchive _dateWithMSDOSFormat:]")
                DW_AT_decl_file        ("/var/folders/03/2g9r4cnj3kqb5605581m1nf40000gn/T/cocoapods-uclardjg/Pods/SSZipArchive/SSZipArchive/SSZipArchive.m")
                DW_AT_decl_line        (965)
                DW_AT_prototyped        (0x01)
                DW_AT_type        (0x00498104 "NSDate*")
                DW_AT_APPLE_optimized        (0x01)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就其中的一部分关键数据解读如下：</p>
<ul>
<li><code>DW_AT_low_pc</code>, <code>DW_AT_high_pc</code> 分别代表函数的起始/结束PC地址。</li>
<li><code>DW_AT_name</code> 描述函数的名字为+[SSZipArchive _dateWithMSDOSFormat:]。</li>
<li><code>DW_AT_decl_file</code> 说这个函数在.../SSZipArchive.m文件中声明。</li>
<li><code>DW_AT_decl_file</code>指的是这个函数在.../SSZipArchive.m文件第965行声明。</li>
<li><code>DW_AT_type</code>描述的是函数的返回值类型，对于这个函数来说，为NSDate*。</li>
</ul>
<p>值得注意的是:</p>
<ol>
<li>DWARF 只有有限种类的属性, 全部属性的列表可以参考llvm api文档（链接见参考资料[5]）中DW_TAG开头的部分。</li>
<li><code>DW_AT_low_pc</code> 和 <code>DW_AT_high_pc</code> 描述的机器码地址不等价于程序在运行时的地址，我们可以称之为file_address。操作系统基于安全因素的考虑，会应用一种地址空间布局随机化的技术ASLR，加载可执行文件到内存时，会做一个随机偏移(下文中用load_address代指)，我们获取到偏移后还需要加上<code>__TEXT</code>Segment的vmaddr才可以还原出运行时地址。vmaddr可以通过上面的size指令或者<code>otool -l</code>指令拿到。注意vmaddr一般跟架构有着直接的关系，对于armv7架构而言通常是0x4000，对于arm64架构而言通常是0x100000000，但是也不绝对，例如这里的AwemeDylib动态库符号表arm64架构的vmaddr就是0。我们将函数在App运行时的地址称之为runtime_address。</li>
</ol>
<p>上述几种地址他们之间的计算公式为：</p>
<blockquote>
<p>file_address = runtime_address - load_address + vm_address</p>
</blockquote>
<h5 data-id="heading-17">CompileUnit</h5>
<p>CompileUnit翻译过来就是编译单元。一个编译单元通常对应着一个TAG是<code>DW_TAG_compile_unit</code>的DIE。编译单元代表的是一个可执行源文件编译后的<code>__TEXT</code>和<code>__DATA</code>等产物，一般可以简单的理解为我们代码中的一个参与编译的文件，例如.m，.mm，.cpp，.c等不同编程语言对应的源文件。一个编译单元包含在这个编译单元中声明的所有DIE（包括方法，参数，变量等）。举一个典型的例子：</p>
<pre><code class="copyable">0x00495ea3: DW_TAG_compile_unit
              DW_AT_producer        ("Apple LLVM version 10.0.0 (clang-1000.11.45.5)")
              DW_AT_language        (DW_LANG_ObjC)
              DW_AT_name        ("/var/folders/03/2g9r4cnj3kqb5605581m1nf40000gn/T/cocoapods-uclardjg/Pods/SSZipArchive/SSZipArchive/SSZipArchive.m")
              DW_AT_stmt_list        (0x001e8f31)
              DW_AT_comp_dir        ("/private/var/folders/03/2g9r4cnj3kqb5605581m1nf40000gn/T/cocoapods-uclardjg/Pods")
              DW_AT_APPLE_optimized        (0x01)
              DW_AT_APPLE_major_runtime_vers        (0x02)
              DW_AT_low_pc        (0x00000000002fc8e8)
              DW_AT_high_pc        (0x0000000000300828)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就其中的一部分关键数据解读如下：</p>
<ul>
<li><code>DW_AT_language</code>，描述的是当前编译单元使用的是哪种编程语言。</li>
<li><code>DW_AT_stmt_list</code> 指的是当前编译单元对应的行号信息在<code>debug_line</code> section中的偏移，在下一小结中我们再详细介绍。</li>
<li><code>DW_AT_low_pc</code>，<code>DW_AT_high_pc</code> 这里分别代表编译单元包含的所有<code>DW_TAG_subprogram</code>TAG的DIE的整体的起始/结束的PC地址。</li>
</ul>
<h5 data-id="heading-18">debug_line</h5>
<p>通过输入指令<code>dwarfdump AwemeDylib --debug-line</code>可以查看到<code>debug_line</code>section结构化之后的数据。</p>
<p>然后我们搜索上一小结中的<code>DW_AT_stmt_list</code>，也就是<code>0x001e8f31</code>：</p>
<pre><code class="copyable">debug_line[0x001e8f31]
...
include_directories[  1] = "/var/folders/03/2g9r4cnj3kqb5605581m1nf40000gn/T/cocoapods-uclardjg/Pods/SSZipArchive/SSZipArchive"
...
file_names[  1]:
           name: "SSZipArchive.m"
      dir_index: 1
       mod_time: 0x00000000
         length: 0x00000000
...
Address                                     Line  Column File   ISA   Discriminator     Flags
------------------------ ------   ------    --- -----  -------------  --------
0x00000000002fc8e8        46           0       1         0                         0    is_stmt
0x00000000002fc908        48          32       1         0                         0    is_stmt prologue_end
0x00000000002fc920         0          32       1         0                         0 
0x00000000002fc928        48          19       1         0                         0 
0x00000000002fc934        49           9       1         0                         0    is_stmt
0x00000000002fc938        53          15       1         0                         0    is_stmt
0x00000000002fc940        54           9       1         0                         0    is_stmt
...
0x0000000000300828  1058               1       1         0                         0    is_stmt end_sequence
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>include_directories</code>和<code>file_names</code>组合起来就是参与编译文件的绝对路径。</p>
<p>然后下面的列表就是file_address对应的文件名和行号。</p>
<ul>
<li>
<p>Address：这里指的是FileAddress。</p>
</li>
<li>
<p>Line: 指的是FileAddress在源文件中对应的行号。</p>
</li>
<li>
<p>Column：FileAddress在源文件中对应的列号。</p>
</li>
<li>
<p>File:源文件index，与上面file_names中的下标是一致的。</p>
</li>
<li>
<p>ISA:无符号整数，指的是当前指令适用于哪些指令集架构，这里一般都是0。</p>
</li>
<li>
<p>Discriminator：无符号整数，标志当前的指令在多编译单元中的归属，在单编译单元的体系中一般是0。</p>
</li>
<li>
<p>Flags：一些标记位，这里解释其中最重要的两个：</p>
<ul>
<li>end_sequence：是目标文件机器指令结束地址+1，所以可以认为在当前编译单元中，只有end_sequence对应地址之前的地址才是有效的指令。</li>
<li>is_stmt：表示当前指令是否为推荐的断点位置，一般而言is_stmt为false的代码可能对应的是编译器优化后的指令，这部分的指令一般行号都是0，对我们分析问题是有干扰的，下文中会讲如何校正。</li>
</ul>
</li>
</ul>
<h5 data-id="heading-19">符号解析原理</h5>
<p>比如这行调用栈：</p>
<blockquote>
<p>5 AwemeDylib 0x000000010035d580 0x10005d000 + 3147136</p>
</blockquote>
<p>对应的binaryImage是：</p>
<blockquote>
<p>0x10005d000 - 0x1000dffff AwemeDylib arm64 </p>
</blockquote>
<p>通过文件结构这一小节我们可以通过公式计算出崩溃地址对应的file_address：</p>
<blockquote>
<p>file_address = 0x000000010035d580 - 0x10005d000 + 0x0 = 0x300580</p>
</blockquote>
<p>然后我们用<code>dwarfdump --lookup</code>指令可以查找出对应的方法名和行号：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d974d4249eb6452e9656a1d4cf7aae5b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们用流程图描述一下<code>dwarfdump</code>从地址到符号映射的原理（atos等其他工具同理）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb5e5c218cfa47f787e29601a88fc78c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到最终<code>dwarfdump</code>解析的结果与我们手动人肉解析的结果也是完全一致的，下图中0x30057c~0x300593这个地址范围解析出来的文件名和行号都是完全一致的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8372ddf967a347e89ab47dfd2e112d64~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于DWARF文件的符号解析我们预期解析结果的格式是：</p>
<blockquote>
<p>func_name (in binary_name) (file_name:line_number)</p>
</blockquote>
<p>以FileAddress 0x300580为例，我们手动人肉解析的结果是：</p>
<blockquote>
<p>+[SSZipArchive _dateWithMSDOSFormat:] (in AwemeDylib) (SSZipArchive.m:965)</p>
</blockquote>
<p>然后我们用atos工具执行命令手动解析的结果是：</p>
<blockquote>
<p>dwarf atos -o AwemeDylib.framework.dSYM/Contents/Resources/DWARF/AwemeDylib -arch arm64 -l 0x10005d000 0x000000010035d580</p>
</blockquote>
<p>+[SSZipArchive _dateWithMSDOSFormat:] (in AwemeDylib) (SSZipArchive.m:965)</p>
<p>可见atos与我们手动人肉解析的结果也是完全一致的。</p>
<h4 data-id="heading-20">Symbol Table</h4>
<p>上一个大的章节，我们介绍了通过DWARF文件来实现符号解析的原理。但是这种方案并不能覆盖100%的场景。原因是：</p>
<ol>
<li>如果被静态链接的Framework在打包的时候将编译参数<code>GCC_GENERATE_DEBUGGING_SYMBOLS</code>改成NO，那么最终App打包时候生成的dSYM文件将没有这部分代码生成机器指令对应的文件名和行号信息。</li>
<li>对于系统库而言，并没有提供dSYM文件，我们有的仅仅是.dylib或者.framework等格式的MachO文件，例如<code>libobjc.A.dylib</code>，<code>Foundation.framework</code>等。</li>
</ol>
<p>对于没有DWARF文件的符号，我们就需要用另外一种手段：<code>Symbol Table String</code>来进行符号解析。</p>
<h5 data-id="heading-21">文件结构</h5>
<p>MachO文件中Symbol Table部分在MachoView工具中的格式如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7e8ad5235b04e98b9ab0bade4a22dc4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关键信息解读：</p>
<ul>
<li>String Table Index：就是String表中的偏移量。通过这个偏移量可以访问到符号对应的具体字符串，例如上图中圈中的第一个symbol info的偏移量是0x0048C12B，再加上String Table的起始地址0x02BBC360 ，等于0x304848B。查询之后果然是_ff_stream_add_bitstream_filter。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbec97eea32e4138a454b75a3851340a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>value：当前方法对应的起始的FileAddress。</li>
</ul>
<h5 data-id="heading-22">符号解析原理</h5>
<ol>
<li>对Symbol Table列表的value排序。</li>
<li>将value排好序，查找到刚刚好小于value的index，则崩溃的信息就存在于index-1下标的数据区中，再用index-1下标数据区中的String Table Index就可以在String Table索引到对应的方法名。然后FileAddress - 目标数据区的value就是崩溃地址距离方法起始地址的偏移字节数。</li>
</ol>
<p>基于Symbol Table的符号解析我们预期解析结果的格式是：</p>
<blockquote>
<p>func_name (in binary_name) + func_offset</p>
</blockquote>
<p>以FileAddress 0x56C1DE为例，我们手动人肉解析的结果是：</p>
<blockquote>
<p>_ff_stream_add_bitstream_filter (in AwemeDylib) + 2</p>
</blockquote>
<p>然后我们用atos工具执行命令手动解析的结果是：</p>
<blockquote>
<p>dwarf atos -o AwemeDylib.framework.dSYM/Contents/Resources/DWARF/AwemeDylib -arch arm64 -l 0x0 0x56C1DE</p>
</blockquote>
<p>ff_stream_add_bitstream_filter (in AwemeDylib) + 2</p>
<p>可见atos与我们手动人肉解析的结果也可以认为是完全一致的，唯一一点差异在于atos移除了编译器默认给c函数加的_前缀。</p>
<h3 data-id="heading-23">线上预解析方案实现</h3>
<h4 data-id="heading-24">Golang原生实现</h4>
<p>Golang使用原生系统库<code>debug/dwarf</code>解析DWARF文件 ，可以非常方便的打印出address对应的文件名及行号，而Golang天然的就支持跨平台。</p>
<p>但是Golang的原生实现其实并不能满足我们的需求，主要原因有以下几点：</p>
<ol>
<li><code>debug/dwarf</code>并没有提供直接解析方法名的api，这就导致解析结果不完整。</li>
<li>对于内联函数的文件名和行号等更加复杂的场景也没有兼容。</li>
<li>这里的实现其实还是基于已知FileAddress的前提，并没有提供全量预解析的方案。</li>
<li>仅支持Dwarf文件的解析，不支持Symbol Table的解析。</li>
</ol>
<p>因此我们还是得自己分别实现DWARF文件和Symbol Table的解析。</p>
<h4 data-id="heading-25">全量预解析实现</h4>
<p>依据上面的原理，我们首先很自然而然可以想到的一个思路就是：我们只要把<code>__TEXT</code>Segment中的<code>__text</code>Section可能出现的地址范围逐一解析出来，然后存到后端的分布式缓存比如Hbase或者redis不就好了吗？</p>
<p>答案是可以，但是没有必要。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35dbaf9590094c7a8e5d4ce493f3f4f1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面这张图我们可以看出来，代码段的size是0x130FD54，转成10进制的话是将近2000w的数量级！这还只是单个符号表文件的单个架构，然而字节稳定性监控平台线上存量的符号表已经有几十万数量级，这种量级的存储太消耗机器资源，显然是不太现实的。基于符号解析的原理我们不难发现，一段连续的地址他们的解析结果可能是完全相同的。例如上面我们也提到过，这里AwemeDylib dSYM文件arm64架构下的0x30057c到0x300593这个地址范围解析出来的结果都是<code>+[SSZipArchive _dateWithMSDOSFormat:] (in AwemeDylib) (SSZipArchive.m:965)</code>。这样就起码有了20倍的压缩率，而且这个策略无论对DWARF文件还是Symbol Table而言都是适用的。</p>
<p>那么下一个问题又来了，我们已知AwemeDylib dSYM文件arm64架构下0x30057c～0x300593地址范围对应的符号解析结果是[SSZipArchive _dateWithMSDOSFormat:] (in AwemeDylib) (SSZipArchive.m:965)。写入Hbase中的value很简单，我们可以把一段地址范围的最低地址，最高地址，对应符号解析的方法名，文件名，行号等信息封装成一个struct，定义为value，我们称之为unit&#123;&#125;。那么key又是什么呢？</p>
<p>这里其实有一个比较棘手的问题就是：在预解析数据存储的时候我们是存储的一段地址范围，但是在线上解析的时候我们的输入只有一个地址，那么怎么从这一个地址反推出Hbase存储的key呢？我们给出的解决方案是：</p>
<blockquote>
<p>hbase_key = [table_name]+image_name+uuid+chunk_index</p>
</blockquote>
<p>各个部分分别解释如下：</p>
<ul>
<li>table_name：用于区分dwarf和symbol_table两种类型。</li>
<li>image_name：binary的名字，例如Aweme，libobjc.A.dylib等。</li>
<li>uuid：一个符号表文件的唯一标示，注意一般dSYM为多架构的胖二进制文件，而不同架构的MachO文件uuid也不同。</li>
<li>chunk_index：指的是以连续长度为一个常数N（这里以10000为例）的地址空间为单位切分，计算当前地址能落到哪个下标中，也可以认为是当前地址除以常数N然后向下取整。对于单个地址而言是非常明确的，但是对于一段地址范围的话就比较复杂了，如果一段地址范围的下限和上限除以常数N向下取整相同的话，他们就落在相同的下标中，但是如果不同的话，为了保证读取的时候落到这一段地址范围中的每个地址都能够被正确的解析，因此地址范围首尾横跨的所有chunk_index，都需要写入该地址范围。</li>
</ul>
<p>基于此策略，我们Hbase中的value，也就不能是单个地址范围和对应的解析结果了，而应该是落到这个区间内所有的地址范围的数组，记为[]unit&#123;&#125;。示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba7410e3ff1147d19608b2da52eb0b71~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以清晰的看到，因为29001~41000这个地址范围横跨了3个chunk_index，因为他们同时被写入了Hbase的三条缓存中，虽然有一点冗余，但还是最大程度的兼顾了性能和吞吐。在线上查询调用栈地址对应解析结果的时候我们只要用偏移地址除以常数N再向下取整计算出这个偏移地址落到哪个chunk_index中，然后再用二分法找到第一个刚好大于这个地址的unit_index，再往前挪一个就能查到我们需要的解析结果了。</p>
<p>注意：线上优先查询dwarf表中的Hbase缓存，将方法名，文件名和行号拼接成我们需要的格式；如果没有话再查询symbol_table表中的Hbase缓存，并且计算出距离函数起始地址的偏移。为了防止一些冷数据在符号表上传之后一直没用到长期占用存储资源，我们对上图中每个chunk设置了45天的过期时间，如果线上有被查询到的话，就更新该chunk的过期时间为当前时间之后的45天。</p>
<h4 data-id="heading-26">DWARF文件解析</h4>
<h5 data-id="heading-27">全量CompileUnit解析</h5>
<p>从基于DWARF文件的符号解析原理那一小节中我们知道，无论是文件名行号还是函数名的解析都需要依赖CompileUnit，通过DWARF官方文档我们了解到所有CompileUnit在<code>debug_info</code> section中的偏移地址都保存在<code>debug_arranges</code> section中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b608314cc5c40ac9874d1644ec7d66f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面文档也同时给出了<code>debug_arranges</code>binary中的结构，基于文档中的结构，我们需要把所有的<code>debug_info_offset</code>都手动解析出来，因为篇幅的原因这里就不贴代码实现了，需要特别留意一点的就是binary手动解析的时候一定要留意大小端。</p>
<h5 data-id="heading-28">地址全量解析流程</h5>
<p>下图是地址全量解析的流程，需要特别注意的3点是：</p>
<ol>
<li>内联函数函数名还是以函数的声明为准，但是文件名和行号要以被内联的位置为准，这与atos的解析结果是一致的。否则连续的两层调用栈信息就可能出现跳跃，影响分析问题的效率。</li>
<li>从《DWARF文件格式官方文档》中我们可以了解到，<code>debug_line</code>中Flags那一列如果有<code>is_stmt</code>的话，表示当前指令是编译器推荐的断点位置，否则对应的指令就是编译器自动生成的编译器推荐的断点位置。因为断点只可以打在同一行，那么我们可以判断出从有<code>is_stmt</code>flag的那行指令到下一次有<code>is_stmt</code>flag的这若干行指令对应的源码文件名和行号都是完全相同的，那么针对没有<code>is_stmt</code>flag的那行指令，我们只需要找到挨得最近，且地址比它小，且有<code>is_stmt</code>flag的那行信息，就可以准确的获取到对应地址解析后的文件名和行号。所以总结一下结论就是：debug_line连续几行的行号信息是否可以合并的标志就是<code>is_stmt</code>，只有连续两行<code>is_stmt</code>为true之间的的debug line info才可以被合并。</li>
<li>这里写入到Hbase中的地址范围指的是偏移地址，计算公式是：offset = file_address - __TEXT.vmaddr。这样在解析的时候就不需要关心对应DWARF文件的<code>__TEXT</code>Segment的起始地址。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9e1b8fc45984644adef6c4684ef2adc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-29">Symbol Table解析</h4>
<p>Symbol Table的解析相对来说比较简单，我们只需要把Symbol Table中的信息按value排序，然后将每一部分起止地址以及对应的函数名按照上述章节中的策略写入Hbase即可。</p>
<h4 data-id="heading-30">踩坑记</h4>
<p>在这个方案实现的过程中也踩到了各种各样的坑，这里记录下几个典型的例子，方便大家参考：</p>
<ol>
<li>写入耗时远远大于预期。</li>
</ol>
<p>问题原因：在写入Hbase之前调用了demangle工具，每一次都有额外几十ms的性能开销，在量级夸张的情况下这个问题会被放大。</p>
<p>解决方案：将demangle的时机从Hbase写入之前改到了从Hbase查询之后，毕竟崩溃的方法比起全量的方法而言还是少得多得多。</p>
<ol start="2">
<li>CompileUnit获取失败。</li>
</ol>
<p>问题原因：</p>
<p>绝大部分情况下，从.debug_arranges section中取出的compile unit offset需要手动加一个0xB的偏移才刚好是我们预期的CompileUnit的偏移。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aa499d29d864f9bb56ee05b63832426~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在这个case就出现的意外：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7622d78e96f144fd8f29120e5dac2ba9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们看到它的偏移并不是0xB，而且从<code>debug_arranges</code> section中取出的compile unit offset就直接是正确的了，原因暂时未知。</p>
<p>解决方案：做一个兼容，如果加上0xB的offset取compile unit出错的话，那就减去0xB再重试一次。</p>
<ol start="3">
<li><code>debug_line</code>中连续两行出现了一模一样的地址，导致解析结果有歧义。</li>
</ol>
<p>问题原因：虽然连续两行地址相同，但是文件名和行号却不一致，这就导致了结果有歧义。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47ce868614b64d05829710dd7222a2bd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案：参考atos的解析结果，以前面的那一行为准。</p>
<ol start="4">
<li><code>debug_line</code>已经读到<code>end_sequence</code>那行也就是最后那行，但是当前CompileUnit还有一部分TAG为<code>DW_TAG_subprogram</code>的DIE没有被<code>debug_line</code>中的任何地址索引到。那么这一部分地址范围就被漏掉了。</li>
</ol>
<p>问题原因：怀疑与编译器优化有关，这部分DIE的方法名一般都是以<code>_OUTLINED_FUNCTION_</code>开头。</p>
<p>解决方案：如果已经解析完<code>end_sequence</code>那行，当前CompileUnit还有TAG为<code>DW_TAG_subprogram</code>的DIE没被索引到，那么这部分DIE地址范围对应的文件名和行号就是<code>end_sequence</code>这行的的文件名和行号。</p>
<ol start="5">
<li>Symbol Table中出现非法数据</li>
</ol>
<p>问题原因：Symbol Table中这条数据的FileAddress居然比__TEXT.vmaddr还要小，这就导致offset变成负数了，又因为一开始对地址偏移我们定义的是uint_64类型，导致offset被强转成了一个特别大的整数，不符合预期。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e54140d910408cbbdea6141805bb97~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案：过滤掉地址偏移为负数的数据段。</p>
<h1 data-id="heading-31">上线效果</h1>
<p>本解决方案在全量上线之前AB测试了大概2周左右，修复了所有已知与老方案有diff的badcase。各项性能指标在全量上线之后的表现如下：</p>
<h2 data-id="heading-32">单行解析耗时</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6deec5762ad4b0ab49089dca334ca5e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>7.7 10:46 最近6h 平均耗时优化了<strong>70</strong>倍，pct99 <strong>300</strong>多倍</p>
<h2 data-id="heading-33">crash接口整体耗时</h2>
<p>从7.7到7.10 crash解析接口整体平均耗时下降了<strong>50%+。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de53e67da8c54cbdb4165da5c02cca4e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从7.7到7.0 crash解析接口整体pct99耗时下降了<strong>70%+。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59a03446d70543bda05d6e440a686fa8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-34">符号表文件访问量级</h2>
<p>从7.7->7.10日符号表文件访问的量级降低了<strong>50%+。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a19c6c22074eb6b92938997522d015~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-35">解析报错</h2>
<p>从放量开始后的7.7号开始，解析报错就已经完全消失了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ddb222dc0444b61898cd56a2927b8de~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-36">物理机性能</h2>
<p>选取线上一台比较有代表性的物理机监控，可以看到机器负载，内存占用，CPU占用，网络IO同比都有非常明显的优化。</p>
<p>下面截取部分核心指标优化前和优化后的指标看板作对比：</p>
<p>优化前时间范围: 7.3 12:00 - 7.5 12:00</p>
<p>优化后时间范围: 7.10 12:00 - 7.12 12:00</p>
<h3 data-id="heading-37">15min负载</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16e232f890f484e90c30c960f9534cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235a1425df0944febbd1b62d2bffcb86~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>15min负载平均：5.76 => 0.84，可以理解为集群整体的解析效率提升至原来的<strong>6.85倍</strong>。</p>
<h3 data-id="heading-38">IOWait CPU占用</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90b0d39f556e4306bab2557772aa0389~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/117ce4d74dc1403092072345340c1d2a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>IOWait CPU占用平均：4.21 => 0.16，优化<strong>96%。</strong></p>
<h3 data-id="heading-39">内存占用</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95f5bf47c7ec4e63bc02b3ad83fc1890~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baaccf603bc849d3bb0d9db912832784~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>内存占用平均：74.4GiB => 31.7GiB，优化<strong>57%。</strong></p>
<h3 data-id="heading-40">网络Input流量</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/998188b40c684819b590ff24148001a7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7673104164624fa9b36c695c876e9726~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>网络Input流量：13.2MB/s=>4.34MB/s，优化 <strong>67%。</strong></p>
<h1 data-id="heading-41">参考资料</h1>
<p>[1] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmy.oschina.net%2Flinker%2Fblog%2F1529928" target="_blank" rel="nofollow noopener noreferrer" title="https://my.oschina.net/linker/blog/1529928" ref="nofollow noopener noreferrer">my.oschina.net/linker/blog…</a></p>
<p>[2] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.rs%2Fcrate%2Fsymbolic-demangle%2F8.3.0" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.rs/crate/symbolic-demangle/8.3.0" ref="nofollow noopener noreferrer">docs.rs/crate/symbo…</a></p>
<p>[3] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fllvm.org%2Fdocs%2FCommandGuide%2Fllvm-dwarfdump.html" target="_blank" rel="nofollow noopener noreferrer" title="https://llvm.org/docs/CommandGuide/llvm-dwarfdump.html" ref="nofollow noopener noreferrer">llvm.org/docs/Comman…</a></p>
<p>[4] <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.dwarfstd.org%2Fdoc%2FDWARF4.pdf" target="_blank" rel="nofollow noopener noreferrer" title="http://www.dwarfstd.org/doc/DWARF4.pdf" ref="nofollow noopener noreferrer">www.dwarfstd.org/doc/DWARF4.…</a></p>
<p>[5] <a href="https://link.juejin.cn/?target=http%3A%2F%2Fformalverification.cs.utah.edu%2Fllvm_doxy%2F2.9%2Fnamespacellvm_1_1dwarf.html%23a85bda042c02722848a3411b67924eb47" target="_blank" rel="nofollow noopener noreferrer" title="http://formalverification.cs.utah.edu/llvm_doxy/2.9/namespacellvm_1_1dwarf.html#a85bda042c02722848a3411b67924eb47" ref="nofollow noopener noreferrer">formalverification.cs.utah.edu/llvm_doxy/2…</a></p>
<h1 data-id="heading-42">关于字节终端技术团队</h1>
<p>字节跳动终端技术团队(Client Infrastructure)是大前端基础技术的全球化研发团队（分别在北京、上海、杭州、深圳、广州、新加坡和美国山景城设有研发团队），负责整个字节跳动的大前端基础设施建设，提升公司全产品线的性能、稳定性和工程效率；支持的产品包括但不限于抖音、今日头条、西瓜视频、飞书、瓜瓜龙等，在移动端、Web、Desktop等各终端都有深入研究。</p>
<p>就是现在！<strong>客户端／前端／服务端／端智能算法／测试开发</strong> 面向全球范围招聘！<strong>一起来用技术改变世界</strong>，感兴趣请联系 <strong><a href="https://link.juejin.cn/?target=mailto%3Achenxuwei.cxw%40bytedance.com" target="_blank" title="mailto:chenxuwei.cxw@bytedance.com" ref="nofollow noopener noreferrer">chenxuwei.cxw@bytedance.com</a></strong>，邮件主题 <strong>简历-姓名-求职意向-期望城市-电话</strong>。</p></div>  
</div>
            