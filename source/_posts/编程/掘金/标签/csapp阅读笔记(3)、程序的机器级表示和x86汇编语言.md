
---
title: 'csapp阅读笔记(3)、程序的机器级表示和x86汇编语言'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a425029134dd47b0af0f97d83566c170~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:10:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a425029134dd47b0af0f97d83566c170~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>计算机执行的是机器代码。机器代码翻译成可读形式就是汇编，也是逆向工程。
在我们使用gcc的时候实际上是生成了汇编的，只是过程被省略了，在学习的时候我们指定优化等级为 <code>-Og</code></p>
<p>一些在c语言中被省略的细节在汇编语言中是可见的。</p>
<ul>
<li><code>程序计数器</code>: 在x86-64中用 <code>%rip</code>表示，给出将要执行的下一条指令在内存中的位置</li>
<li><code>整数寄存器</code>包含16个命名的位置，分别存储64位的值。这些寄存器可以存放地址的值或者整数。有的寄存器用来保存一个临时的状态</li>
<li><code>条件码寄存器</code>保存着最近执行的算术或者逻辑指令的状态信息。用来实现控制流的变化</li>
<li><code>一组向量寄存器</code>可以存放一个或多个整型或浮点数值</li>
</ul>
<p>让我们来看书上的关于汇编的一个例子
编写一个mstore.c文件。含有以下内容</p>
<pre><code class="hljs language-c copyable" lang="c"> <span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">mult2</span><span class="hljs-params">(<span class="hljs-keyword">long</span>, <span class="hljs-keyword">long</span>)</span></span>;
 <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">multstore</span><span class="hljs-params">(<span class="hljs-keyword">long</span> x, <span class="hljs-keyword">long</span> y, <span class="hljs-keyword">long</span> *des)</span> </span>&#123;
     <span class="hljs-keyword">long</span> t = mult2(x, y);
     *des = t;                                                                                
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a425029134dd47b0af0f97d83566c170~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-variable">$gcc</span> -Og -S mstore.c       <span class="hljs-comment">#生成汇编文件</span>
<span class="hljs-variable">$gcc</span> -Og -c mstore.c       <span class="hljs-comment">#会生成二进制文件(.o)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/621d85850c0040deaf247c34fe9427c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
生成一个.o文件和.s文件
查看.s文件中multstore的定义</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cefda8d9a8f4473cb3b5740f30a53166~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
里面每一行表示一条机器指令(除了一些伪指令)
.o文件里面含有的都是二进制数据
要查看机器代码的内容，我们需要使用反汇编器。在linux里面可以使用objdump命令</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ objdump -d mstore.o
mstore.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <multstore>:
   0:   f3 0f 1e fa             endbr64
   4:   53                      push   %rbx
   5:   48 89 d3                mov    %rdx,%rbx
   8:   e8 00 00 00 00          callq  d <multstore+0xd>
   d:   48 89 03                mov    %rax,(%rbx)
  10:   5b                      pop    %rbx
  11:   c3                      retq
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38ec382b03554125ac4f4f09b2901cfb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
生成可执行文件还有一步很重要的就是链接。
假设我们有一个main.c文件，含有以下代码</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><stdio.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">multstore</span><span class="hljs-params">(<span class="hljs-keyword">long</span>, <span class="hljs-keyword">long</span>, <span class="hljs-keyword">long</span> *)</span></span>;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">long</span> d;
    multstore(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, &d);
    <span class="hljs-built_in">printf</span>(<span class="hljs-string">"2 * 3 ---> %ld\n"</span>, d);
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">mult2</span><span class="hljs-params">(<span class="hljs-keyword">long</span> a, <span class="hljs-keyword">long</span> b)</span> </span>&#123;
    <span class="hljs-keyword">long</span> s = a * b;
    <span class="hljs-keyword">return</span> s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用以下方式生成可执行文件prog</p>
<pre><code class="hljs language-bash copyable" lang="bash">gcc -Og -o prog main.c mstore.c
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8269ae5643464ad0a8b44b04b985c402~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后反汇编器生成反汇编代码</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ objdump -d prog > prog.s
<span class="hljs-comment">## 里面有这样一段，可以看到几乎和mstore.c反汇编出来是一样的</span>
00000000000011d5 <multstore>:
    11d5:       f3 0f 1e fa             endbr64
    11d9:       53                      push   %rbx
    11da:       48 89 d3                mov    %rdx,%rbx
    11dd:       e8 e7 ff ff ff          callq  11c9 <mult2>
    11e2:       48 89 03                mov    %rax,(%rbx)
    11e5:       5b                      pop    %rbx
    11e6:       c3                      retq
    11e7:       66 0f 1f 84 00 00 00    nopw   0x0(%rax,%rax,1)
    11ee:       00 00
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03eedb5b3e88423890c9e3519cf48991~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
所有以<code>.</code>开头的行都是指导链接器和汇编器的伪指令。我们通常忽略这些字段。</p>
<h4 data-id="heading-0">数据格式</h4>
<p>Intel用术语<code>字</code>表示16位数据类型。因此，称32位数为双字，称64位数为四字。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cff465df21c4d1abc89dc5f886f3e5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
多数gcc生成的汇编代码都有一个字符的后缀表明操作数的大小。例如数据传输有四个变种:movb(传送字节)、movw(传送字)、movl(传送双字)、movq(传送四字)。l表示双字。汇编代码也使用后缀<code>l</code>表示四字节整数和八字节双精度浮点数，因为使用的指令不同，所以不会产生歧义。</p>
<h4 data-id="heading-1">16个通用寄存器</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0a551f46aad4c9790fce7b76b37510f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">操作数指示符</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd94d9911454354a95f5652fb7878e9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">数据传送指令</h4>
<p>注意，第一个是源操作数，第二个是目的操作数</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83bd4cbfe6854518ba5e4c43d6c10824~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将较小的源值复制到较大的目的时有两种扩展方式，零扩展和符号扩展</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20c2cd4ae5b342c5a90f345dbbd73ea5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f562786c9c74481ba7a7878bff7b233b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
零扩展是把多出来的位都用0填充，符号扩展则是用符号位填充
<code>cltq</code>指令没有操作数，总是以寄存器%eax作为源，%rax作为符号扩展的目的</p>
<h5 data-id="heading-4">数据传输示例</h5>
<p>写这样一段代码</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">exchange</span><span class="hljs-params">(<span class="hljs-keyword">long</span> *xp, <span class="hljs-keyword">long</span> y)</span> </span>&#123;
    <span class="hljs-keyword">long</span> x = *xp;
    *xp = y;
    <span class="hljs-keyword">return</span> x;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到下面的汇编代码</p>
<pre><code class="hljs language-bash copyable" lang="bash">0000000000000000 <exchange>:
   0:   f3 0f 1e fa             endbr64
   4:   48 8b 07                mov    (%rdi),%rax
   7:   48 89 37                mov    %rsi,(%rdi)
   a:   c3                      retq
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6f110ddfeba4a80a2bbac84946656c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">压入和弹出栈数据</h4>
<p>pushq %rbq 等同于</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/076b27cef7c84ce3971765440c6a6cff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
pop %rax 等价于</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a92a96d7814c33aa8d130a30221ab5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">算术和逻辑操作</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f279cadd45a440c4a71e8722b684f8c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">加载有效地址</h4>
<p>加载有效地址指令leaq实际上是movq指令的变形。它的指令形式是从内存读数据到寄存器，实际上并没有引用内存。
让我们看书中的例子</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">scale</span><span class="hljs-params">(<span class="hljs-keyword">long</span> x, <span class="hljs-keyword">long</span> y, <span class="hljs-keyword">long</span> z)</span> 
</span>&#123;
    <span class="hljs-keyword">long</span> t = x + <span class="hljs-number">4</span> * y + <span class="hljs-number">12</span> * z;
    <span class="hljs-keyword">return</span> t;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>反汇编后是</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc5ffc607dbc419aba5d038bb8f21182~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7aed0572dc64d399cd8d79586eda0e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
leaq指令能执行加法和有限的乘法</p>
<h4 data-id="heading-8">一元和二元操作</h4>
<p>第二组的操作是一元操作。第三组是二元操作，第二个操作数既是源又是目的，当第二个操作数为内存地址时处理器必须从内存读出值。</p>
<h4 data-id="heading-9">移位操作</h4>
<p>最后一组是移位操作，先给出移位量，然后第二项给出的是要移位的数。可以进行算术和逻辑右移。移位量可以是一个立即数，或者放在单字节寄存器%cl中。当%cl中的值为0xFF时，指令salb会移位7位，salw会移15位，sall会移31位，salq会移63位。
左移指令有两种: SAL和SHL。两者的效果是一样的，都是在右边填上0。右移指令则不同，SAR执行算术移位(填上符号位)，SHL执行逻辑移位(填上0)。移位操作的目的操作数可以是一个寄存器或是一个内存位置。</p>
<h4 data-id="heading-10">特殊的算术操作</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11888b6cdc5748de9c66b0c89976d820~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
imulq是补码乘法，mulq是无符号乘法。这两个操作计算128位乘积，两条指令要求一个参数必须在%rax中，而另外一个作为指令的源操作数给出。然后乘积存放在%rdx(高64位)和%rax(低64位)中，虽然imulq这个名字可以用于两个不同的乘法操作，但是汇编器能够通过计算操作数的数目，分辨出想用哪种指令。来看书中的例子</p>
<pre><code class="copyable">#include <inttypes.h>
typedef unsigned __int128 uint128_t;
void store_uprod(uint128_t *dest, uint64_t x, uint64_t y) &#123;
    *dest=x* (uint128_t) y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a98426542d69410eb83a8affb759f155~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1ae36c9c43b4dc88d1453e332a98074~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们再来看看如何实现除法</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">remdiv</span><span class="hljs-params">(<span class="hljs-keyword">long</span> x, <span class="hljs-keyword">long</span> y, <span class="hljs-keyword">long</span> *qp, <span class="hljs-keyword">long</span> *rp)</span> </span>&#123;
    <span class="hljs-keyword">long</span> q = x / y;
    <span class="hljs-keyword">long</span> r = x % y;
    *qp = q;
    *rp = r;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b483a78fda6c46b0ab4de6ffd41c66cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfae252fbe2443aa88dc313eb01e38e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">控制</h3>
<p>机器代码提供两种基本的低级机制来实现有条件的行为:测试数据值，然后根据测试的结果来改变控制流或者数据流</p>
<h4 data-id="heading-12">条件码</h4>
<p>除了整数寄存器以外。cpu还维护这一组单个位的条件码寄存器。它们描述了最近的算术或逻辑操作的属性。最常用的条件码是</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd884116ec949bfaeeee16fd4195ffc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果计算t = a + b。那么下面的c表达式来设置条件码</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24d59b35eae84a00bb9fc00bd41e0027~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">访问条件码</h4>
<p>条件码通常不会直接读取，常用的使用方法有三种: 1)根据条件码的某种组合将一个字设置为0或者1。2)可以条件跳转到程序的某个其他的部分。3)可以有条件的传送数据。对于第一种，我们称为SET指令</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e21e4db38ce42a399ddd49148071fd5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们来看书上的一个例子</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de97def320de4ecb8062e995bda123ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">跳转指令</h4>
<p>jmp是无条件跳转，其他的是根据比较结果跳转
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe6bc9e288bf40a59ac52deb17578c6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">用条件控制来实现条件分支</h4>
<p>让我们来看一个例子</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">long</span> lt_cnt = <span class="hljs-number">0</span>;
<span class="hljs-keyword">long</span> ge_cnt = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">absdiff_se</span><span class="hljs-params">(<span class="hljs-keyword">long</span> x, <span class="hljs-keyword">long</span> y)</span>
</span>&#123;
    <span class="hljs-keyword">long</span> result;
    <span class="hljs-keyword">if</span>(x < y)
    &#123;
        lt_cnt++;
        result = y - x;
    &#125;
    <span class="hljs-keyword">else</span>
    &#123;
        ge_cnt++;
        result = x - y;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1c59c2a17742bcac6eff22045b96af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51e713e498a543f79f8958be1c2bce54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">用条件传送来实现条件分支</h4>
<p>传统的方法是通过使用控制的条件转移。当条件满足时，程序沿着一条执行路径执行，当条件不足时，就走另外一条路径。但是可能会非常低效。我们可以使用条件传送指令来实现，更加符合现代处理器的性能特性</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b6b696e7f9249419d296eb749e5c091~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8df086f1dacc43b89eeefebe48f420f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            