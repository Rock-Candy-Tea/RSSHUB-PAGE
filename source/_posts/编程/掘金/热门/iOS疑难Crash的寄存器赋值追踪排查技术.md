
---
title: 'iOS疑难Crash的寄存器赋值追踪排查技术'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e65648aa41384c3d94ea34549b53f39f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 02:34:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e65648aa41384c3d94ea34549b53f39f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们会借助一些崩溃日志收集库来定位和排查线上的崩溃信息，但是有些崩溃堆栈所提供的信息有限又不是必现崩溃，很难直观排查出问题的所在。这里我给大家分享一个采用<strong>寄存器赋值追踪的技术</strong>来排查和分析崩溃日志的技巧。话不多说先看案例：</p>
<pre><code class="copyable">//符号化后的崩溃堆栈
Date/Time:       2021-03-25 04:35:38.211 +0800
OS Version:      iOS 10.3.2 (14F89)
Report Version:  104

Monitor Type:    Unix Signal
Exception Type:  EXC_CRASH (SIGABRT)
Exception Codes: 0x00000000 at 0x00000001808f1014
Crashed Thread:  27


Pthread id: 1313098
Thread 27 Crashed:
0   libsystem_kernel.dylib          __pthread_kill + 8
1   libsystem_pthread.dylib         pthread_kill + 112
2   libsystem_c.dylib               abort + 140
3   libsystem_malloc.dylib          szone_error + 420
4   libsystem_malloc.dylib          free_list_checksum_botch.295 + 36
5   libsystem_malloc.dylib          tiny_free_list_remove_ptr + 288
6   libsystem_malloc.dylib          tiny_free_no_lock + 684
7   libsystem_malloc.dylib          free_tiny + 472
8   CoreFoundation                  _CFRelease + 1228
//只有这句信息可以参考
9   testApp                        __99-[XXX fn:queue:]_block_invoke + 384
10  libdispatch.dylib               _dispatch_call_block_and_release + 24
11  libdispatch.dylib               _dispatch_client_callout + 16
12  libdispatch.dylib               _dispatch_queue_serial_drain + 928
13  libdispatch.dylib               _dispatch_queue_invoke + 884
14  libdispatch.dylib               _dispatch_root_queue_drain + 540
15  libdispatch.dylib               _dispatch_worker_thread3 + 124
16  libsystem_pthread.dylib         _pthread_wqthread + 1096
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//这是原始崩溃栈
Pthread id: 1313098
 Thread 27 Crashed:
0   libsystem_kernel.dylib          0x00000001808f1014 __pthread_kill + 8
1   libsystem_pthread.dylib         0x00000001809bb264 pthread_kill + 112
2   libsystem_c.dylib               0x00000001808659c4 abort + 140
3   libsystem_malloc.dylib          0x0000000180931828 szone_error + 420
4   libsystem_malloc.dylib          0x000000018093b74c 0x180924000 + 96076
5   libsystem_malloc.dylib          0x0000000180928994 0x180924000 + 18836
6   libsystem_malloc.dylib          0x000000018093ba00 0x180924000 + 96768
7   libsystem_malloc.dylib          0x000000018093c0c8 0x180924000 + 98504
8   CoreFoundation                  0x00000001818a701c 0x1817ca000 + 905244
9   testApp                         0x0000000103b9e5b8 __99-[XXX fn:queue:]_block_invoke + 384
10  libdispatch.dylib               0x00000001807ae9e0 0x1807ad000 + 6624
11  libdispatch.dylib               0x00000001807ae9a0 0x1807ad000 + 6560
12  libdispatch.dylib               0x00000001807bcad4 0x1807ad000 + 64212
13  libdispatch.dylib               0x00000001807b22cc 0x1807ad000 + 21196
14  libdispatch.dylib               0x00000001807bea50 0x1807ad000 + 72272
15  libdispatch.dylib               0x00000001807be7d0 0x1807ad000 + 71632
16  libsystem_pthread.dylib         0x00000001809b7100 _pthread_wqthread + 1096


Binary Images:
       0x1000b8000 -        0x108263fff +testApp arm64  <cb8cc0075ed4352b802c6c586b8a93d5> /var/containers/Bundle/Application/0A1F4541-8749-4F9D-B60A-813FFEE69CA6/testApp.app/testApp

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的崩溃信息大概可以看出这是一个GCD队列线程调用时发生了崩溃。其中崩溃的第9层显示是在一个[XXX fn:queue:] 方法内定义的block内部代码发生了崩溃，除此之外没有其它信息。崩溃方法的源代码定义如下：</p>
<pre><code class="copyable">//这是一个简化代码
@interface TestObj:NSObject

-(NSString*)testString;

-(NSInteger)length;

@end

//代码片段
-(void)fn:(TestObj*)testObj queue:(dispatch_queue_t)queue &#123;
    dispatch_async(queue, ^&#123;
        @autoreleasepool &#123;
              if ([testObj length] != 0) &#123;
                  NSString *suffix = [testObj testString];
                  const static int len = 4;
                  if (suffix.length > len) &#123;
                      suffix = [suffix substringToIndex:len];
                  &#125;
              &#125;
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源代码来看确实是在方法-[XXX fn:queue:]内调用了一个dispatch_async，然后block也是定义在方法内。不过依然没办法定位到是哪行代码发生了崩溃,  同时也不是必现的线上崩溃。</p>
<p>所以要想查明原因需要到汇编代码级别定位崩溃原因！！ 步骤如下：</p>
<ol>
<li>
<p>先下载可执行文件到本地或者从CI发布部门获取可执行的app包并解压。</p>
</li>
<li>
<p>用系统自带的otool工具，进行代码的反汇编处理。下面的otool命令格式可以用来显示具体的函数或者方法的反汇编代码：</p>
</li>
</ol>
<pre><code class="copyable"> otool "可执行文件路径"   -p "函数或者方法名" -V -t 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>otool命令中 -p 后面跟的是方法名或者函数名或者符号名。 这里需要注意的时因为系统编译时可能会在函数名或者符号名前多增加一个下划线_ 因此在指定符号名时需要多增加一个_。 -V 是表明打印函数对应的汇编代码。 -t 是表明打印代码段中的代码。</p>
<p>本例的问题使用otool如下：</p>
<pre><code class="copyable">  otool   "/Users/apple/Downloads/Payload/testApp.app/testApp" -p "___99-[XXX fn:queue:]_block_invoke" -V -t 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>汇编出来的局部代码如下：</p>
<pre><code class="hljs language-c copyable" lang="c">/Users/apple/Downloads/Payload/testApp.app/testApp:
(__TEXT,__text) section
___99-[XXX fn:<span class="hljs-built_in">queue</span>:]_block_invoke:
......... 省略部分代码
<span class="hljs-number">0000000103</span>ae6554<+<span class="hljs-number">284</span>>mov x20, x0
<span class="hljs-number">0000000103</span>ae6558<+<span class="hljs-number">288</span>>ldr x0, [x20, #x20]
<span class="hljs-number">0000000103</span>ae655c<+<span class="hljs-number">292</span>>adrpx8, <span class="hljs-number">26695</span> ; <span class="hljs-number">0x10a32d000</span>
<span class="hljs-number">0000000103</span>ae6560<+<span class="hljs-number">296</span>>ldrx1, [x8, #<span class="hljs-number">0x940</span>] ; Objc selector ref: testString
<span class="hljs-number">0000000103</span>ae6564<+<span class="hljs-number">300</span>>bl<span class="hljs-number">0x107fac9e8</span> ; Objc message: -[x0 testString]
<span class="hljs-number">0000000103</span>ae6568<+<span class="hljs-number">304</span>>movx29, x29
<span class="hljs-number">0000000103</span>ae656c<+<span class="hljs-number">308</span>>bl<span class="hljs-number">0x107faca48</span> ; symbol stub <span class="hljs-keyword">for</span>: _objc_retainAutoreleasedReturnValue
<span class="hljs-number">0000000103</span>ae6570<+<span class="hljs-number">312</span>>movx25, x0
<span class="hljs-number">0000000103</span>ae6574<+<span class="hljs-number">316</span>>movx0, x26
<span class="hljs-number">0000000103</span>ae6578<+<span class="hljs-number">320</span>>bl<span class="hljs-number">0x107faca18</span> ; symbol stub <span class="hljs-keyword">for</span>: _objc_release
<span class="hljs-number">0000000103</span>ae657c<+<span class="hljs-number">324</span>>movx0, x25
<span class="hljs-number">0000000103</span>ae6580<+<span class="hljs-number">328</span>>movx1, x22
<span class="hljs-number">0000000103</span>ae6584<+<span class="hljs-number">332</span>>bl<span class="hljs-number">0x107fac9e8</span> ; Objc message: -[x0 testString]  <span class="hljs-comment">//这里是otool的bug真实应该是 length方法。</span>
<span class="hljs-number">0000000103</span>ae6588<+<span class="hljs-number">336</span>>cmpx0, #<span class="hljs-number">0x5</span>
<span class="hljs-number">0000000103</span>ae658c<+<span class="hljs-number">340</span>>b.lo<span class="hljs-number">0x103ae65bc</span>
<span class="hljs-number">0000000103</span>ae6590<+<span class="hljs-number">344</span>>adrpx8, <span class="hljs-number">26674</span> ; <span class="hljs-number">0x10a318000</span>
<span class="hljs-number">0000000103</span>ae6594<+<span class="hljs-number">348</span>>ldrx1, [x8, #<span class="hljs-number">0xb30</span>] ; Objc selector ref: substringToIndex:
<span class="hljs-number">0000000103</span>ae6598<+<span class="hljs-number">352</span>>movx0, x25
<span class="hljs-number">0000000103</span>ae659c<+<span class="hljs-number">356</span>>movw2, #<span class="hljs-number">0x4</span>
<span class="hljs-number">0000000103</span>ae65a0<+<span class="hljs-number">360</span>>bl<span class="hljs-number">0x107fac9e8</span> ; Objc message: -[x0 substringToIndex:]
<span class="hljs-number">0000000103</span>ae65a4<+<span class="hljs-number">364</span>>movx29, x29
<span class="hljs-number">0000000103</span>ae65a8<+<span class="hljs-number">368</span>>bl<span class="hljs-number">0x107faca48</span> ; symbol stub <span class="hljs-keyword">for</span>: _objc_retainAutoreleasedReturnValue
<span class="hljs-number">0000000103</span>ae65ac<+<span class="hljs-number">372</span>>movx22, x0
<span class="hljs-number">0000000103</span>ae65b0<+<span class="hljs-number">376</span>>movx0, x25
<span class="hljs-number">0000000103</span>ae65b4<+<span class="hljs-number">380</span>>bl<span class="hljs-number">0x107faca18</span> ; symbol stub <span class="hljs-keyword">for</span>: _objc_release
<span class="hljs-number">0000000103</span>ae65b8<+<span class="hljs-number">384</span>>movx25, x22
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述的崩溃信息可以看出崩溃的地址是0x0000000103b9e5b8。根据这个地址可以得出崩溃是在我们反汇编代码的倒数第二行。<code>0x0000000103ae65b4<+380></code></p>
<blockquote>
<p>上述的两个地址都不同，结论是如何得出的？</p>
</blockquote>
<ol>
<li>线上的程序运行时程序时会在一个随机的基地址上加载，从崩溃的原始堆栈中最下面部分可以看到程序映像的基地址就是 0x1000b8000。因此：</li>
</ol>
<pre><code class="copyable">0x0000000103b9e5b8 - 0x1000b8000 = 0x0000000103ae65b8
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>又因为一般程序崩溃的地址都有3个特征：</li>
</ol>
<p>a. 崩溃堆栈层级中的非顶层地址都是函数调用指令的下一条地址也就是LR的值，所以真实的崩溃指令处是第1步算出的结果再减去4也就是实际崩溃的地址是：0x0000000103ae65b4</p>
<p>b.  如果崩溃信息出现在最顶层时，一般的崩溃指令都是带有内存访问的指令。假如崩溃是在第上面的第二条指令，也就是在<code>ldr x0, [x20, #x20]</code> 处时很大概率是访问的内存地址无效产生的崩溃。</p>
<p>c . 如果崩溃信息出现在最顶层即无内存访问也无函数调用的指令时，这种崩溃一般是触发了brk断点指令，或者产生了其他一些无法可判断的原因了。前者比较好定位，后者就很难了。</p>
<p>从上面汇编代码倒数第二行<+384>处可以看出是一个对象调用了_objc_release进行释放时导致了崩溃。而_objc_release内部可能会调用_CFRelease方法，这也就是在上面崩溃信息堆栈中__99-[XXX fn:queue:]_block_invoke + 384的上面是_CFRelease函数了。</p>
<p>既然是因为对象调用_objc_release导致的内存释放异常。那么就需要继续追踪是哪个对象调用了_objc_release。</p>
<p>根据arm系统的函数调用ABI规则，以及从倒数第三行<+376>的汇编代码中可以看出是执行了一个 x0 = x25的操作，也就是x0对象是从x25赋值而来的。这时候我们就可以利用寄存器赋值追踪的技巧，继续往上查看x25又是在哪里被赋值。 往上的代码可以看出在<+312>处的指令执行了 x25 = x0的赋值操作，而x0的结果是上一条指令调用_objc_retainAutoreleasedReturnValue函数返回的结果。而_objc_retainAutoreleasedReturnValue的入参又是上一条指令<+300>处的[x0 testString] 方法返回的结果。到这里为止我就可以从源代码中推断出是[testObj testString] 返回的结果对象在释放时导致了崩溃了。</p>
<p>那接下来你就可以仔细查查源代码[testObj testString]的方法哪里有问题了。并最终定位出异常原因。</p>
<p>下面就是用寄存器追踪技术展示的追踪推导图：
<img alt="寄存器追踪图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e65648aa41384c3d94ea34549b53f39f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>小贴士：在arm64位系统中，函数的第一个参数用x0寄存器保存，OC方法调用的对象也是用x0寄存器保存，函数和方法的返回结果也是用x0寄存器保存。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            