
---
title: 'Android Binder 原理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723615057ed94ee88872dc1ed79bdc0f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 07:10:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723615057ed94ee88872dc1ed79bdc0f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. Binder是什么</h1>
<p>在Android中Binder是跨进程通信方式。不过从不同角度来开，binder也可以有如下理解：</p>
<p>1，从进程间通信的角度看，Binder 是一种进程间通信的机制；
2，从 Server 进程的角度看，Binder 指的是 Server 中的 Binder 实体对象；
3，从 Client 进程的角度看，Binder 指的是对 Binder 代理对象，是 Binder 实体对象的一个远程代理
4，从传输过程的角度看，Binder 是一个可以跨进程传输的对象；传输过程中，Binder 驱动会对这个跨越进程的对象，自动完成代理对象和本地对象之间的转换。</p>
<h1 data-id="heading-1">2. Binder优势</h1>
<p>Linux提供了管道、消息队列、共享内存和 Socket 等 IPC 机制。</p>
<ol>
<li>
<p>管道/消息队列：信息复制两次，额外的CPU消耗；不合适频繁或信息量大的通信；</p>
</li>
<li>
<p>共享内存：无须复制，共享缓冲区直接附加到进程虚拟地址空间，速度快；但进程间的同步问题操作系统无法实现，必须各进程利用同步工具解决；</p>
</li>
<li>
<p>Socket：作为更通用的接口，传输效率低（涉及io读写），主要用于不通机器或跨网络的通信；</p>
</li>
<li>
<p>信号量：常作为一种锁机制，防止某进程正在访问共享资源时，其他进程也访问该资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。</p>
</li>
<li>
<p>信号: 不适用于信息交换，更适用于进程中断控制，比如非法内存访问，杀死某个进程等；</p>
</li>
</ol>
<h2 data-id="heading-2">2.1 性能：</h2>
<p>Binder数据拷贝只需要一次，而管道、消息队列、Socket都需要2次，共享不需要内存拷贝；从性能角度看，Binder性能仅次于共享内存。</p>
<h2 data-id="heading-3">2.2 稳定性：</h2>
<p>Binder是基于C/S架构的，Client端有什么需求，直接发送给Server端去完成，架构清晰，Server端与Client端相对独立，稳定性较好；</p>
<p>而共享内存实现方式复杂，没有客户与服务端之别，需要充分考虑到访问临界资源的并发同步问题，否则可能会出现死锁等问题；从这稳定性角度看，Binder架构优越于共享内存。</p>
<h2 data-id="heading-4">2.3 性能：</h2>
<p>传统Linux IPC的接收方无法获得对方进程可靠的UID/PID，从而无法鉴别对方身份；（比如socket  只能由用户在数据包中填入 UID/PID））。</p>
<p>Android系统中对外只暴露Client端，Client端将任务发送给Server端，Server端会根据权限控制策略，判断UID/PID是否满足访问权限，目前权限控制很多时候是通过弹出权限询问对话框，让用户选择是否运行。</p>
<p>注意：Binder是为Android这类系统而生（主要从安全行考虑），并非Linux现有的IPC机制不好，只是根据不通的场景会选择不不同的IPC机制，例如：</p>
<p>1，Android OS中的Zygote进程的IPC采用的是Socket（套接字）机制；</p>
<p>参考：<a href="https://blog.csdn.net/qq_39037047/article/details/88066589" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/qq_39037047…</a></p>
<p>2，Android中的Kill Process采用的signal（信号）机制；</p>
<p>3，而Binder更多则用在system_server进程与上层App层的IPC交互（主要从安全行考虑）。</p>
<h1 data-id="heading-5">3. Binder 通信原理</h1>
<h2 data-id="heading-6">3.1 进程空间划分</h2>
<p>进程间，用户空间的数据不可共享，所以用户空间 = 不可共享空间</p>
<p>进程间，内核空间的数据可共享，所以内核空间 = 可共享空间</p>
<p>所有进程共用1个内核空间</p>
<p>进程内 用户空间 & 内核空间 进行交互 需通过 系统调用，主要通过函数：</p>
<p>1，copy_from_user（）：将用户空间的数据拷贝到内核空间</p>
<p>2，copy_to_user（）：将内核空间的数据拷贝到用户空间</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723615057ed94ee88872dc1ed79bdc0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">3.2 Binder驱动</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b4e21856b99479fa8861f5100c4a295~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">3.3 内存映射</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e42ea42774b487cb8e0dbeaa0f5f7a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先在内核虚拟地址空间，申请一块与用户虚拟内存相同大小的内存；然后再申请1个page大小的物理内存，再将同一块物理内存分别映射到内核虚拟地址空间和用户虚拟内存空间，从而实现了用户空间的Buffer和内核空间的Buffer同步操作的功能。</p>
<h2 data-id="heading-9">3.4 Binder通信原理</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa14d0d4792841d48b31aefb4955f226~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1，Binder驱动在内核空间创建一个数据接收缓存区；</p>
<p>2，实现地址映射关系，将内核缓存区和接收进程地址空间映射到Binde创建一个数据接收缓存区；</p>
<p>3，发送方进程通过系统调用 copy_from_user() 将数据 copy 到内核缓存区，由于内核缓存区和接收进程的地址空间存在内存映射，因此也就相当于把数据发送到了接收进程的用户空间，这样便完成了一次进程间的通信。</p>
<p><strong>问题：为啥不能直接将内核缓存区映射到接收进程地址空间，而需要再开辟一个数据接收缓存区？？？</strong></p>
<p>我的理解是：binder开辟的数据接受缓存区就是就是开辟一块物理内存，然后将内核缓存区和接收进程地址空间映射。</p>
<h1 data-id="heading-10">4. Binder通信模型</h1>
<h2 data-id="heading-11">4.1 通信模型</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43c8720a3cb74b3cb9e602346bc8e40c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2413865c6bdd424b95f41ae1283864b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1，一个进程使用 BINDER_SET_CONTEXT_MGR 命令通过 Binder 驱动将自己注册成为 ServiceManager；</p>
<p>2，Server 通过驱动向 ServiceManager 中注册 Binder（Server 中的 Binder 实体），即注册（可对外提供的）服务。驱动为这个 Binder 创建位于内核中的实体节点以及 ServiceManager 对实体的引用，将名字以及新建的引用打包传给 ServiceManager，ServiceManger 将其填入查找表。</p>
<p>3，Client 通过名字，在 Binder 驱动的帮助下从 ServiceManager 中获取到对 Binder 实体的引用，通过这个引用就能实现和 Server 进程的通信。</p>
<p>注意：</p>
<p>1，ServiceManager进程是使用BINDER_SET_CONTEXT_MGR将自己注册成ServiceManager，并会创建一个Binder 实体</p>
<p>2，这个 Binder 实体的引用在所有 Client 中都固定为 0 ，无需通过其它手段获得。也就是说，一个 Server 想要向 ServiceManager 注册自己的 Binder 就必须通过这个 0 号引用和 ServiceManager 的 Binder 通信。</p>
<h2 data-id="heading-12">4.2 系统服务和自定义服务</h2>
<p>1，系统服务会往ServiceManager注册，ServiceManager运行在单独的进程里，客户端进程需要先向ServiceManager里请求IBinder，再使用IBinder获取关联接口进而使用系统服务。</p>
<p>2，自定义服务所在进程开启后，暴露出IBinder。客户端通过绑定服务端进程里的Service，将IBinder跨进程传递至客户端，客户端再使用IBinder获取关联接口进而使用自定义服务。此过程没有借助于ServiceManager。</p>
<p>参考：<a href="https://www.jianshu.com/p/b39ffcbcb7b7" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/b39ffcbcb…</a></p>
<h1 data-id="heading-13">5. Android Binder 通信代码理解</h1>
<h2 data-id="heading-14">5.1 Binder相关类</h2>
<p>1，IBinder : IBinder 是一个接口，代表了一种跨进程通信的能力。只要实现了这个借口，这个对象就能跨进程传输。</p>
<p>2，IInterface :  IInterface 代表 Server 进程对象具备什么样的能力（能提供哪些方法，其实对应的就是 AIDL 文件中定义的接口）</p>
<p>3，Binder : Java 层的 Binder 类，代表 Binder 本地对象。</p>
<p>4，BinderProxy :表clientd端，远程 Binder 对象的本地代理；</p>
<p>这两个类都继承自 IBinder, 因而都具有跨进程传输的能力；实际上，在跨越进程的时候，Binder 驱动会自动完成这两个对象的转换。</p>
<p>5，Stub : AIDL 的时候，编译工具会给我们生成一个名为 Stub 的静态内部类；这个类继承了 Binder, 说明它是一个 Binder 本地对象，它实现了 IInterface 接口，表明它具有 Server 提供给 Client 的能力；Stub 是一个抽象类，具体的 IInterface 的相关实现需要开发者自己实现。</p>
<h2 data-id="heading-15">5.2 aidl使用流程图:</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b2faba19cf449c89dab8c4aa9d4ed91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-16">6. 参考</h1>
<ol>
<li><a href="https://juejin.cn/post/6844903589635162126" target="_blank">juejin.cn/post/684490…</a></li>
<li><a href="https://www.jianshu.com/p/4ee3fd07da14" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/4ee3fd07d…</a></li>
<li><a href="https://www.jianshu.com/p/4ff66bfb59fb" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/4ff66bfb5…</a></li>
<li><a href="https://www.jianshu.com/p/b39ffcbcb7b7" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/b39ffcbcb…</a></li>
<li><a href="https://blog.csdn.net/fdsafwagdagadg6576/article/details/109862316" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/fdsafwagdag…</a></li>
<li><a href="https://www.zhihu.com/question/39440766" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/39…</a></li>
<li><a href="http://gityuan.com/2015/10/31/binder-prepare/" target="_blank" rel="nofollow noopener noreferrer">gityuan.com/2015/10/31/…</a></li>
<li><a href="https://www.jianshu.com/p/adaa1a39a274" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/adaa1a39a…</a></li>
<li><a href="https://paul.pub/android-binder-driver/#id-%E5%86%85%E5%AD%98%E6%98%A0%E5%B0%84mmap" target="_blank" rel="nofollow noopener noreferrer">paul.pub/android-bin…</a></li>
<li><a href="https://juejin.cn/post/6844903438883651592" target="_blank">juejin.cn/post/684490…</a></li>
</ol></div>  
</div>
            