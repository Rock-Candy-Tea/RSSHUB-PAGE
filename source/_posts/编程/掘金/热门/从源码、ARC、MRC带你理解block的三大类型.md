
---
title: '从源码、ARC、MRC带你理解block的三大类型'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c15b391aeebe42859161f5195c76b821~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 20 Mar 2021 06:47:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c15b391aeebe42859161f5195c76b821~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先,在了解block三大类型之前,我们需要了解一个知识:</p>
<p>(温馨提醒:如果我的之前博客你没有看,有些概念你不清楚的话,你可能很难理解,如果前面你都看了,这篇博客你看就像切菜一样简单!)</p>
<h3 data-id="heading-0">程序的内存分配</h3>
<p>一个由C/C++编译的程序占用的内存分为以下几个部分</p>
<p><strong>栈（stack）</strong>:由编译器自动分配释放 ，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈。</p>
<p><strong>堆（heap）</strong>: 一般由程序员分配释放， 若程序员不释放，程序结束时可能由OS回收 。注意它与数据结构中的堆是两回事，分配方式类似于链表。</p>
<p><strong>全局区（静态区static）</strong>:全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域， 未初始化的全局变量和未初始化的静态变量在相邻的另一块区域，程序结束后由系统释放。</p>
<p><strong>文字常量区</strong>：常量字符串放在这里， 程序结束后由系统释放</p>
<p><strong>程序代码区</strong>：存放函数体的二进制代码。</p>
<p>相信大家对上面的这些内存分配的知识点都已经非常清楚,那我们就看一下</p>
<h3 data-id="heading-1">block的类型</h3>
<h4 data-id="heading-2">block是有3种类型,通过调用class的方法或者isa指针查看具体的类型,最终都是继承NSBlock类型</h4>
<p>接下来我们就看看,block就是一个oc对象,那我们就可以按照oc的,直接调用class就知道它的类型了</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c15b391aeebe42859161f5195c76b821~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里可以看出我前面说的,block就是oc对象,而这个NSGlobalBlock是继承NSBlock的,其他的种类都是继承NSBlock,等说完了,大家可以用这个方法试试其它2种block的的父类.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52ebe3acc3ef437aa4fd12a2ec3e5480~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上面就是block的总共的三种类型:NSGlobalBlock、NSStackBlock、NSMallcBlock,</p>
<p>,这是运行时输出的结果,其实编译的结果可能有点不一样,那我们就把这份文件转成c++文件,这个我之前的博客都提了很多次,这次我就不细说了(xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc main.m -o main.cpp)</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09f1ef733fc94e9dbeccc32ab599a621~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其实你会发现,编译以后生成的都是NSConcreteStackBlock类型,首先我们肯定以运行时为准,因为编译过程还有个运行,运行就会用runtime动态修改你的东西;还有其实用clang转成c++的代码,有时候并不一定就是最终的代码,其实差别是不大,其实在llvm大概6.0以前都是一样的,现在会生成一个中间文件,还有就是程序运行中也是比较准确,如果有同学查看源码感觉不一样,不要很惊讶,这个很正常,可以参考,差别不大.</p>
<p>我们继续看</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4510d620fa874964bcd67eda821e5ade~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>而GlobalBlock是在数据区域,MallocBlock是在堆区,StackBlock是在栈区,我这里不说堆、栈、数据区域的区别了,大家这个知识点如果不懂可以去查阅一下它们的区别,不然后面的很难理解</p>
<h3 data-id="heading-3">什么样的类型的是GlobalBlock?什么样的类型是MallocBlock?什么样的类型是StackBlock?</h3>
<p>先看我的总结,我们再细细看</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a76d1dd33745eebe5ad8aee7b50325~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>auto变量大家清楚吧?auto变量就是它所在的区域执行完毕,自动销毁的变量.如果不知道请看我上一篇博客,介绍的非常清晰.接下来我们就一个一个看每种类型的block</p>
<h4 data-id="heading-4">GlobalBlock类型</h4>
<p>请看下面的代码</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d206da289e3a45e49e61965184b9aba4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>访问static的局部变量,全局变量a,都不是auto变量,所以上面3种情况都是GlobalBlock,因为GlobalBlock我们实际中用的非常少,所以这个也没有过多的需要阐述的</p>
<h3 data-id="heading-5">StackBlock类型(重点)</h3>
<p>按照我们表格上面说的访问了auto变量的block就是StackBlock,那我看一下下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/422e777fb6864dd39f51676ee44a1359~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>ARC下运行的结果</p>
<p>应该有同学注意,结果和我们上面的结论不一样,其实是因为这环境是ARC,ARC下其实帮你做了很多事(这个为什么会这样,这个内容还是有点多,后面的博客,我会细说,你先不管这个为什么是这样),所以我们改成MRC才能看到它的本质(直接把Objective-C Automatic Reference Counting 设置为NO即可),我们再看下面</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ae4c49675ed4499afe8b12c7bca8baf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>MRC下运行的结果</p>
<p>这就是StackBlock类型,下面我们再深入看一下这个StackBlock一个特殊情况,如下图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1fa853274dc485cbf46a78c5fae8d07~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>MRC下运行的结果</p>
<p>注意到没有,这个age的值变得很奇怪.这是因为:test()函数的作用域执行结束以后,它的作用域中的栈上面的变量就会销毁,比如里面的block就是StackBlock,所有test()执行完毕以后,block已经被释放了,导致访问内部就会出现混乱的情况.整个block内存被释放了里面的所有都会出现混乱</p>
<h3 data-id="heading-6">那上面的怎么解决这种问题呢???</h3>
<p>答案很明显,我们把block栈内存变成堆内存就行了哇!怎么变成堆block,是不是直接栈调用copy就能是堆block了,那我们再试试:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d86334a1fc6d41c2bf218d43fecb7a3b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>是不是就很容易解决了!可能有同学还有疑问,如果把GlobalBlock也来调用copy会是怎么样呢?这个大家可以自己验证,答案还是:GlobalBlock,如果把MallocBlock也来调用copy会是怎么样呢?这个大家可以自己验证,答案还是:引用计数加1</p>
<p>还有如果我们block访问一个对象,一个对象也是auto变量,所以也是一样的,这些我就不验证了,如有疑问可以评论区讨论.</p>
<h3 data-id="heading-7">MallocBlock类型</h3>
<p>这个上面已经说的很清楚了</p>
<p>相信还有同学有疑问,刚刚我们是MRC下测试的,至于ARC为什么会是另一个结果,我后面的博客会说到!</p>
<h3 data-id="heading-8">接下来博客我会介绍堆MallocBlock的一些具体情况和使用,来继续探讨block</h3>
<h1 data-id="heading-9">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            