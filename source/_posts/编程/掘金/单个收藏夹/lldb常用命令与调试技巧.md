
---
title: 'lldb常用命令与调试技巧'
categories: 
 - 编程
 - 掘金
 - 单个收藏夹
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ab69fd24824e9b9c92aae14995521b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Sep 2020 09:44:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ab69fd24824e9b9c92aae14995521b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、基本介绍</h1>
<p><code>LLDB</code>是个开源的内置于<code>XCode</code>的调试工具，它能帮助我们在开发中更快的定位和调试<code>bug</code>，无论正向和逆向开发中都有很大的作用。<strong>lldb</strong>对于命令的简称，是<strong>头部匹配方式，只要不混淆(不提示歧义)，你可以随意简称某个命令</strong>。</p>
<h3 data-id="heading-1">xcode调试区</h3>
<p>下面是xcode debug区域的按钮讲解
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ab69fd24824e9b9c92aae14995521b~tplv-k3u1fbpfcp-zoom-1.image" alt="Xcode调试区按钮讲解" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">二、调试技巧</h1>
<h3 data-id="heading-3">单步调试</h3>
<p>单步调试通常分为两大类，一类为<code>源码级别（source level）</code>，一类为<code>指令级别（instrution level）</code>。一行源代码一般需要多行汇编才可以实现，所以当我们越狱开发调试汇编指令单步调试需要用到（instrution level）指令级别。而<strong>每一大类又分为step-in和step-over，step-in会进入函数调用，而step-over会跳过函数调用</strong>。</p>
<h5 data-id="heading-4">1)源码级别(source level)</h5>
<ul>
<li>step-in</li>
</ul>
<pre><code class="copyable">(lldb) thread step-in
(lldb) step
(lldb) s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上三条命令是等同的，<strong>在有函数调用的位置，<code>会</code>进入函数内部。</strong></p>
<ul>
<li>step-over</li>
</ul>
<pre><code class="copyable">(lldb) thread step-over
(lldb) next
(lldb) n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上三条命令是等同的，<strong>在有函数调用的位置，<code>不会</code>进入函数内部。</strong></p>
<blockquote>
<p>总结</p>
<blockquote>
<p>s和n都是跳转到断点的下一行代码位置，区别为，如果下一行代码有函数调用，s会进入函数内部，n则会跳过函数执行。如果没有函数调用则两组命令没有任何区别。</p>
</blockquote>
</blockquote>
<h5 data-id="heading-5">2)指令级别(instruction level)</h5>
<p>指令级别的调试，我们需要在xcode的选项卡中设置<code>Debug->Debug Workflow->Always Show Disassembly</code>，这时候才能看到效果。<strong>指令级别的lldb对应的正好是我们点击按钮的同时按下了ctrl键。</strong></p>
<ul>
<li>step-in</li>
</ul>
<pre><code class="copyable">(lldb) thread step-inst
(lldb) si
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两条命令是等同的，在<strong>汇编界面，跳转下一步，在有<code>bl</code>指令的地方，<code>si``会</code>单步进入到<code>bl</code>指令所跳转的子函数内部</strong></p>
<ul>
<li>step-over</li>
</ul>
<pre><code class="copyable">(lldb) thread step-inst-over
(lldb) ni
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两条命令是等同的，在<strong>汇编界面，跳转下一步，在有<code>bl</code>指令的地方，<code>ni``不会</code>单步进入到<code>bl</code>指令所跳转的子函数内部</strong></p>
<ul>
<li>step-out
<ul>
<li>setp out 从一个函数跳出。</li>
<li>如果没有执行s或者si，却执行了finish，其实会跳转到汇编指令bl的下一条位置（step out默认是从一个函数跳出，对系统函数调用一定是通过bl执行了函数调用，下一个位置必定为bl的下一个位置）</li>
<li>要从嵌套的step out中退出，执行c命令即可跳转到下一个断点。</li>
</ul>
</li>
</ul>
<pre><code class="copyable">(lldb) thread step-out
(lldb) finish
(lldb) f
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>c</code>是<code>continue</code>的简写 表示继续运行</li>
<li>s(si)、n(ni)和Xcode调试工具的对应关系如文开始的图</li>
</ul>
<h1 data-id="heading-6">三、lldb常用命令</h1>
<h3 data-id="heading-7">1.计算表达式命令(expression、po、p)</h3>
<ul>
<li><code>expression</code>可简写为<code>expr</code>
<ul>
<li>计算以及生成一个表达式</li>
</ul>
</li>
</ul>
<pre><code class="copyable">(lldb) expr (int)printf ("Print nine: %d.\n", 4 + 5) 
Print nine: 9.
(int) $0 = 15
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建一个变量并分配值</li>
</ul>
<pre><code class="copyable">(lldb) expr int $val = 10
(lldb) expr $val
(int) $val = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>exp</code>打印值、修改值</li>
</ul>
<pre><code class="copyable">(lldb) expr width
(CGFloat) $0 = 10
(lldb) expr width = 2
(CGFloat) $1 = 2
(lldb) po width
2

(lldb) p width
(CGFloat) $3 = 2
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong><code>p</code>、<code>po</code>与<code>expr</code>的关系</strong></li>
</ul>
<pre><code class="copyable">(lldb) expr -- person
(Person *) $0 = 0x000000010053b7f0
(lldb) p person
(Person *) $1 = 0x000000010053b7f0
(lldb) expr -o -- person
<Person: 0x10053b7f0>

(lldb) po person
<Person: 0x10053b7f0>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>总结</p>
<blockquote>
<p><code>p</code>是<code>expr --</code>的简写，它的工作是把接收到参数在当前环境中进行编译，然后打印出来
<code>po</code>是<code>expr -o --</code>的简写，它所做的操作和p相同。如果接收到的参数是一个指针，那么它会调用对象的<code>description</code>方法并打印；如果接收到的参数是一个<code>core foundation</code>对象，那么它会调用<code>CFShow</code>方法并打印。如果这两个方法都调用失败，那么<code>po</code>打印出和<code>p</code>相同的内容。</p>
</blockquote>
</blockquote>
<ul>
<li>使用p做进制转换</li>
</ul>
<pre><code class="copyable">//默认打印为10进制
(lldb) p 10
(int) $0 = 10
//转16进制
(lldb) p/x 10
(int) $1 = 0x0000000a
//转8进制
(lldb) p/o 10
(int) $2 = 012
//转二进制
(lldb) p/t 10
(int) $3 = 0b00000000000000000000000000001010
//字符转10进制数字
(lldb) p/d 'A'
(char) $4 = 65
//10进制数字转字符
(lldb) p/c 66
(int) $5 = B\0\0\0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. 内存读取</h3>
<pre><code class="copyable">(lldb) x person
0x10053a6b0: 5d 22 00 00 01 80 1d 00 00 00 00 00 00 00 00 00  ]"..............
0x10053a6c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
(lldb) x/4gx person
0x10053a6b0: 0x001d80010000225d 0x0000000000000000
0x10053a6c0: 0x0000000000000000 0x0000000000000000
(lldb) x/3wx person
0x10053a6b0: 0x0000225d 0x001d8001 0x00000000
(lldb) x &width
0x7ffeefbff4f0: 00 00 00 00 00 00 00 00 b0 a6 53 00 01 00 00 00  ..........S.....
0x7ffeefbff500: 30 f5 bf ef fe 7f 00 00 01 00 00 00 00 00 00 00  0...............
(lldb) x/4gx &width
0x7ffeefbff4f0: 0x0000000000000000 0x000000010053a6b0
0x7ffeefbff500: 0x00007ffeefbff530 0x0000000000000001
(lldb) x/4go
0x7ffeefbff510: 03777735757772440
0x7ffeefbff518: 03777755321776311
0x7ffeefbff520: 00
0x7ffeefbff528: 01
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>x</code>是读取内存的命令，<code>x/4gx</code>中第一个<code>x</code>是读取内存命令，后面的<code>g</code>是每次读取<code>8字节</code>，<code>x</code>的意思是<code>16进制显示结果</code>，<code>4</code>表示<code>连续打印4段</code>。</p>
<ul>
<li>对于<code>g</code>，常用的大小格式为<code>b</code>对应<code>byte 1字节</code>，<code>h</code>对应<code>half word 2字节</code>，<code>w</code>对应<code>word 4字节</code>，<code>g</code>对应<code>giant word 8字节</code></li>
<li>对于<code>x</code>，我们还可以用<code>o</code>对应<code>8机制</code>，<code>b</code>对应<code>2进制</code>,<code>x</code>对应<code>16进制</code>,<code>f</code>对应<code>浮点</code>，<code>d</code>对应<code>10进制</code></li>
</ul>
<h3 data-id="heading-9">3.<code>call</code>方法调用</h3>
<pre><code class="copyable">(lldb) call width
(CGFloat) $0 = 0
(lldb) call testFunction()
123456
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4.变量检查（frame）</h3>
<pre><code class="copyable">(lldb) fr v b
(Int??) b = nil
(lldb) fr v -r b
(Int??) b = nil
(lldb) fr v -R b
(Swift.Optional<Swift.Optional<Swift.Int>>) b = some &#123;
  some = none &#123;
    some = &#123;
      _value = 0
    &#125;
  &#125;
&#125;
(lldb) fr v -a b
(Int??) b = nil
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们常用<code>fr v -R</code>来查看类型的结构</p>
<h3 data-id="heading-11">5.检查线程状态</h3>
<h5 data-id="heading-12">1) 堆栈打印(<code>bt</code>命令)</h5>
<p><code>bt</code>是<code>thread backtrace</code>的简写，如果嫌堆栈打印太长，可以加一个限制，如<code>bt 10</code>，只打印10行</p>
<pre><code class="copyable">(lldb) thread backtrace 1
* thread #1, queue = 'com.apple.main-thread', stop reason = step over
  * frame #0: 0x0000000100000e02 TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:30:5
    frame #1: 0x00007fff6b47fcc9 libdyld.dylib`start + 1
(lldb) thread backtrace -c 1
* thread #1, queue = 'com.apple.main-thread', stop reason = step over
    frame #0: 0x0000000100000e02 TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:30:5
(lldb) bt 10
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x0000000100000df1 TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:28:13
    frame #1: 0x00007fff6b47fcc9 libdyld.dylib`start + 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的案例一共只有3行，没达到触发10行限制的条件。</p>
<h5 data-id="heading-13">2)<code>thread list</code> 列出当前线程列表</h5>
<pre><code class="copyable">(lldb) thread list
Process 4500 stopped
* thread #1: tid = 0x33d9a, 0x0000000100000e02 TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:30:5, queue = 'com.apple.main-thread', stop reason = step over
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">3）<code>thread select</code> 选取某个线程作为后续命令的默认线程</h5>
<pre><code class="copyable">(lldb) thread select 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">4）<code>frame select</code> 根据下标选择堆栈列表中某帧</h5>
<pre><code class="copyable">(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x0000000100000deb TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:37:5
    frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
(lldb) frame select 1
frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
libdyld.dylib`start:
->  0x7fff6ce68cc9 <+1>: movl   %eax, %edi
    0x7fff6ce68ccb <+3>: callq  0x7fff6ce7c82e            ; symbol stub for: exit
    0x7fff6ce68cd0 <+8>: hlt    
    0x7fff6ce68cd1 <+9>: nop    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时会跳转到汇编页面，即使没有设置<code>Always Show Disassembly</code></p>
<h5 data-id="heading-16">5）<code>frame info</code> 显示当前帧信息</h5>
<pre><code class="copyable">(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x0000000100000deb TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:37:5
    frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
(lldb) frame info
frame #0: 0x0000000100000deb TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:37:5
(lldb) frame select 1
frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
libdyld.dylib`start:
->  0x7fff6ce68cc9 <+1>: movl   %eax, %edi
    0x7fff6ce68ccb <+3>: callq  0x7fff6ce7c82e            ; symbol stub for: exit
    0x7fff6ce68cd0 <+8>: hlt    
    0x7fff6ce68cd1 <+9>: nop    
(lldb) frame info
frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">6）<code>up</code>  移动当前帧(序号加1) <code>down</code>移动当前帧(序号减1)</h5>
<pre><code class="copyable">(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x0000000100000ddf TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:36:5
    frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
(lldb) up
frame #1: 0x00007fff6ce68cc9 libdyld.dylib`start + 1
libdyld.dylib`start:
->  0x7fff6ce68cc9 <+1>: movl   %eax, %edi
    0x7fff6ce68ccb <+3>: callq  0x7fff6ce7c82e            ; symbol stub for: exit
    0x7fff6ce68cd0 <+8>: hlt    
    0x7fff6ce68cd1 <+9>: nop    
(lldb) up
error: Already at the top of the stack.
(lldb) down
frame #0: 0x0000000100000ddf TestWeak`main(argc=1, argv=0x00007ffeefbff530) at main.m:36:5
   33      person.age = 5;
   34      
   35      CGFloat width = 10;
-> 36      testFunction();
        ^
   37      NSLog(@"hello");
   38      return 0;
   39  &#125;
(lldb) down
error: Already at the bottom of the stack.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，如果已经是栈顶或者栈底，会提示已在最顶或者最底部。</p>
<h5 data-id="heading-18">7）<code>register read</code> 读取寄存器 <code>register write</code>写入寄存器</h5>
<pre><code class="copyable">(lldb) register write rax 123
(lldb) register read rax
     rax = 0x000000000000007b
(lldb) register write rax 1
(lldb) register read rax
     rax = 0x0000000000000001
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">8)<code>thread return</code> 跳出当前方法的执行</h5>
<p>Debug的时候，也许会因为各种原因，我们不想让代码执行某个方法，或者要直接返回一个想要的值。这时候就该thread return上场了。
有返回值的方法里，如：numberOfSectionsInTableView:，直接thread return 20，就可以直接跳过方法执行，返回20.</p>
<pre><code class="copyable">//跳出方法
(lldb) thread return
//让带有返回int值的方法直接跳出，并返回值20
(lldb) thread return 20
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">6.镜像(image)操作</h3>
<h5 data-id="heading-21">1) <code>image list</code>镜像列表</h5>
<pre><code class="copyable">(lldb) image list
[  0] 9D17C7F5-7D6B-387D-81E5-1C7ED33709BE 0x0000000100000000 /Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak 
[  1] F9D4DEDC-8296-3E3F-B517-9C8B89A4C094 0x0000000100009000 /usr/lib/dyld 
[  2] 7C69F845-F651-3193-8262-5938010EC67D 0x00007fff35437000 /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation 
[  3] 6DF81160-5E7F-3E31-AA1E-C875E3B98AF6 0x00007fff6bcad000 /usr/lib/libobjc.A.dylib 
[  4] C0C9872A-E730-37EA-954A-3CE087C15535 0x00007fff69e4d000 /usr/lib/libSystem.B.dylib 
[  5] C0D70026-EDBE-3CBD-B317-367CF4F1C92F 0x00007fff32d7a000 /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation 
[  6] B6124448-7690-34AE-8939-ED84AAC630CE 0x00007fff6a04f000 /usr/lib/libauto.dylib 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只截取了部分，因为所有的镜像有几百个，包括了各种动态库</p>
<h5 data-id="heading-22">2) <code>image lookup -a</code> 查看崩溃位置</h5>
<pre><code class="copyable">2020-09-16 00:41:45.605355+0800 TestWeak[2106:87796] *** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[__NSArrayI objectAtIndexedSubscript:]: index 4 beyond bounds [0 .. 2]'
*** First throw call stack:
(
0   CoreFoundation                      0x00007fff32e79b57 __exceptionPreprocess + 250
1   libobjc.A.dylib                     0x00007fff6bcc05bf objc_exception_throw + 48
2   CoreFoundation                      0x00007fff32f2859e -[__NSCFString characterAtIndex:].cold.1 + 0
3   CoreFoundation                      0x00007fff32deab70 +[NSNull null] + 0
4   TestWeak                            0x0000000100001b8f -[Person getInt] + 287
5   TestWeak                            0x0000000100001d73 main + 99
6   libdyld.dylib                       0x00007fff6ce68cc9 start + 1
7   ???                                 0x0000000000000001 0x0 + 1
)
libc++abi.dylib: terminating with uncaught exception of type NSException
(lldb) image lookup --address 0x0000000100001b8f
      Address: TestWeak[0x0000000100001b8f] (TestWeak.__TEXT.__text + 335)
      Summary: TestWeak`-[Person getInt] + 287 at main.m:31:13
(lldb) image lookup -a 0x0000000100001b8f
      Address: TestWeak[0x0000000100001b8f] (TestWeak.__TEXT.__text + 335)
      Summary: TestWeak`-[Person getInt] + 287 at main.m:31:13
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们先得到开始一部分数组越界的崩溃信息，我们找到<code>stack</code>中<code>4</code>的位置，可以看到是调用了<code>[person getInt]</code>,这时候我们使用<code>image lookup -a 地址</code>就可以找到崩溃位置。
<code>image lookup -a</code>是<code>image lookup --address</code>的简写</p>
<h5 data-id="heading-23">3) <code>image lookup -v -a</code>查找完整的源代码行信息</h5>
<p>同样使用上方数组越界案例</p>
<pre><code class="copyable">(lldb) image lookup -v -a 0x0000000100001b8f
      Address: TestWeak[0x0000000100001b8f] (TestWeak.__TEXT.__text + 335)
      Summary: TestWeak`-[Person getInt] + 287 at main.m:31:13
       Module: file = "/Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak", arch = "x86_64"
  CompileUnit: id = &#123;0x00000000&#125;, file = "/Users/liu_david/Desktop/TestWeak/TestWeak/main.m", language = "objective-c"
     Function: id = &#123;0x100000162&#125;, name = "-[Person getInt]", range = [0x0000000100001a70-0x0000000100001bef)
     FuncType: id = &#123;0x100000162&#125;, byte-size = 0, decl = main.m:29, compiler_type = "int (void)"
       Blocks: id = &#123;0x100000162&#125;, range = [0x100001a70-0x100001bef)
    LineEntry: [0x0000000100001b76-0x0000000100001b97): /Users/liu_david/Desktop/TestWeak/TestWeak/main.m:31:13
       Symbol: id = &#123;0x0000001c&#125;, range = [0x0000000100001a70-0x0000000100001bf0), name="-[Person getInt]"
     Variable: id = &#123;0x10000017f&#125;, name = "self", type = "Person *const", location = DW_OP_fbreg(-40), decl = 
     Variable: id = &#123;0x10000018b&#125;, name = "_cmd", type = "SEL", location = DW_OP_fbreg(-48), decl = 
     Variable: id = &#123;0x100000197&#125;, name = "array", type = "NSArray *", location = DW_OP_fbreg(-56), decl = main.m:30
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从信息可以看到，我们有三个变量入栈，分别是<code>self</code>、<code>_cmd</code>、<code>array</code>
<code>image lookup -v -a</code>是<code>image lookup -v --address</code>的简写</p>
<h5 data-id="heading-24">4) <code>image lookup -name</code>查找方法来源</h5>
<pre><code class="copyable">(lldb) image lookup getInt
error: invalid combination of options for the given command
(lldb) image lookup -name getInt
1 match found in /Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak:
        Address: TestWeak[0x0000000100001a70] (TestWeak.__TEXT.__text + 48)
        Summary: TestWeak`-[Person getInt] at main.m:29
1 match found in /usr/lib/libicucore.A.dylib:
        Address: libicucore.A.dylib[0x000000000003b046] (libicucore.A.dylib.__TEXT.__text + 239078)
        Summary: libicucore.A.dylib`icu::ResourceBundle::getInt(UErrorCode&) const
1 match found in /System/Library/Frameworks/Security.framework/Versions/A/Security:
        Address: Security[0x000000000012260e] (Security.__TEXT.__text + 1184206)
        Summary: Security`Security::Context::getInt(unsigned int, int) const
1 match found in /System/Library/Frameworks/SceneKit.framework/Versions/A/SceneKit:
        Address: SceneKit[0x000000000024f396] (SceneKit.__TEXT.__text + 2414070)
        Summary: SceneKit`getInt(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&, int&, bool, bool)
1 match found in /usr/lib/libTelephonyUtilDynamic.dylib:
        Address: libTelephonyUtilDynamic.dylib[0x0000000000012e10] (libTelephonyUtilDynamic.dylib.__TEXT.__text + 69904)
        Summary: libTelephonyUtilDynamic.dylib`ctu::cf::map_adapter::getInt(__CFString const*, int) const
1 match found in /System/Library/PrivateFrameworks/CorePrediction.framework/Versions/A/CorePrediction:
        Address: CorePrediction[0x00000000000475c4] (CorePrediction.__TEXT.__text + 286980)
        Summary: CorePrediction`-[CPMLEvalutionResult getInt]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，所有match到的方法位置信息都给我们了。只不过只有我们自定义的方法给了我们是在<code>main.m:29</code></p>
<h5 data-id="heading-25">5) <code>image lookup -type</code>查看成员</h5>
<pre><code class="copyable">(lldb) image lookup -type Person
Best match found in /Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak:
id = &#123;0x10000002b&#125;, name = "Person", byte-size = 24, decl = main.m:12, compiler_type = "@interface Person : NSObject&#123;
    BOOL _isMan;
    short _age;
    NSString * _name;
&#125;
@property(nonatomic, copy, readwrite, getter = name, setter = setName:) NSString *name;
@property(nonatomic, assign, readwrite, getter = age, setter = setAge:) short age;
@property(nonatomic, assign, readwrite, getter = isMan, setter = setIsMan:) BOOL isMan;
@end"

(lldb) image lookup -type NSObject
Best match found in /Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak:
id = &#123;0x7fffffff000002e8&#125;, name = "NSObject", byte-size = 8, decl = NSObject.h:53, compiler_type = "@interface NSObject&#123;
    Class isa;
&#125;
@end"

(lldb) im loo -t Person
Best match found in /Users/liu_david/Library/Developer/Xcode/DerivedData/TestWeak-egnzdbndwsiikvcheqmcxvkqnwbw/Build/Products/Debug/TestWeak:
id = &#123;0x10000002b&#125;, name = "Person", byte-size = 24, decl = main.m:12, compiler_type = "@interface Person : NSObject&#123;
    BOOL _isMan;
    short _age;
    NSString * _name;
&#125;
@property(nonatomic, copy, readwrite, getter = name, setter = setName:) NSString *name;
@property(nonatomic, assign, readwrite, getter = age, setter = setAge:) short age;
@property(nonatomic, assign, readwrite, getter = isMan, setter = setIsMan:) BOOL isMan;
@end"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>image lookup -type</code>可以用<code>im loo -t</code>简写</p>
<h3 data-id="heading-26">7.断点(breakpoint)操作</h3>
<h5 data-id="heading-27">1) <code>b</code>在某个函数设置一个断点</h5>
<pre><code class="copyable">(lldb) b getInt
Breakpoint 2: 6 locations.
(lldb) c
Process 2274 resuming
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如代码所示，我们使用<code>b</code>在<code>getInt</code>方法中设置了一个断点，执行<code>c</code>指令继续运行后，代码会断在<code>getInt</code>方法中第一行
<code>b</code>是以下的简写</p>
<ul>
<li><code>br s -n</code></li>
<li><code>breakpoint set --name</code></li>
</ul>
<h5 data-id="heading-28">2) <code>b+文件:行</code> 在某个文件的某行设置一个断点</h5>
<pre><code class="copyable">(lldb) b main.m:45
Breakpoint 2: where = TestWeak`main + 102 at main.m:45:5, address = 0x0000000100001d76
(lldb) c
Process 2297 resuming
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法是以下命令的简写:</p>
<ul>
<li><code>br s -f main.m -l 45</code></li>
<li><code>breakpoint set --file main.m --line 45</code></li>
</ul>
<h5 data-id="heading-29">3) <code>b -[类名 方法名]</code>、<code>b +[类名 方法名]</code>设置类中方法的断点</h5>
<ul>
<li><code>b -[类名 方法名]</code>是设置实例方法的断点</li>
<li><code>b +[类名 方法名]</code>是设置类方法的断点</li>
</ul>
<pre><code class="copyable">(lldb) b -[Person getInt]
Breakpoint 2: where = TestWeak`-[Person getInt] + 30 at main.m:30:24, address = 0x0000000100001a6e
(lldb) b +[Person aaa]
Breakpoint 3: where = TestWeak`+[Person aaa] + 23 at main.m:27:5, address = 0x0000000100001a37
(lldb) c
Process 2344 resuming
(lldb) c
Process 2344 resuming
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法是以下命令的简写:</p>
<ul>
<li><code>breakpoint set -- name -[类名 方法名]</code></li>
</ul>
<h5 data-id="heading-30">4) <code>breakpoint list</code> 查看断点列表</h5>
<pre><code class="copyable">(lldb) breakpoint list
Current breakpoints:
1: file = '/Users/liu_david/Desktop/TestWeak/TestWeak/main.m', line = 39, exact_match = 0, locations = 1, resolved = 1, hit count = 1

  1.1: where = TestWeak`main + 41 at main.m:39:5, address = 0x0000000100001d19, resolved, hit count = 1 

2: file = '/Users/liu_david/Desktop/TestWeak/TestWeak/main.m', line = 30, exact_match = 0, locations = 1, resolved = 1, hit count = 0

  2.1: where = TestWeak`-[Person getInt] + 30 at main.m:30:24, address = 0x0000000100001a6e, resolved, hit count = 0 

3: file = '/Users/liu_david/Desktop/TestWeak/TestWeak/main.m', line = 27, exact_match = 0, locations = 1, resolved = 1, hit count = 0

  3.1: where = TestWeak`+[Person aaa] + 23 at main.m:27:5, address = 0x0000000100001a37, resolved, hit count = 0 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-31">5) <code>br en 序号</code>、<code>br dis 序号</code> 启用/禁用断点</h5>
<pre><code class="copyable">(lldb) br dis 2
1 breakpoints disabled.
(lldb) br en 2
1 breakpoints enabled.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用<code>br dis 2</code>后，2号断点就会变灰不可用，<code>br en 2</code>后，2号断点又会恢复亮色可使用状态</p>
<ul>
<li><code>br en 序号</code>是<code>breakpoint enable 序号</code>的简写</li>
<li><code>br dis 序号</code>是<code>breakpoint disable 序号</code>的简写</li>
</ul>
<h5 data-id="heading-32">6) <code>br del 序号</code> 根据序号移除一个断点</h5>
<pre><code class="copyable">(lldb) br del 2
1 breakpoints deleted; 0 breakpoint locations disabled.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在删除2号断点后，它将立刻在界面上移除。</p>
<p><code>br del 序号</code>是<code>breakpoint delete 序号</code>的简写</p>
<p>Xcode中的断点调试技巧可参考:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F43964f1bb80f" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/43964f1bb80f" ref="nofollow noopener noreferrer">iOS Xcode Breakpoint(断点)调试</a></p>
<p><strong>参考链接：</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flldb.llvm.org%2Fuse%2Fmap.html%23breakpoint-commands" target="_blank" rel="nofollow noopener noreferrer" title="https://lldb.llvm.org/use/map.html#breakpoint-commands" ref="nofollow noopener noreferrer">GDB to LLDB command map</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F7fb43e0b956a" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/7fb43e0b956a" ref="nofollow noopener noreferrer">iOS之LLDB常用命令</a></li>
</ul></div>  
</div>
            