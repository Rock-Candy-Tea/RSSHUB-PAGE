
---
title: '中高级iOS必备知识点之 RunLoop(一)'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69fcee5870e54d9abec998624b80d43d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 22:53:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69fcee5870e54d9abec998624b80d43d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>RunLoop学习起来是很抽象,也不好理解,所以一定多看几次,多学学才能学好!这也是中高级iOS必须掌握的知识点,面试中经常遇到.</p>
<h3 data-id="heading-0">什么是 RunLoop？</h3>
<p>Run 表示运行，Loop 表示循环。结合在一起就是运行循环的意思。RunLoop就是在程序运行过程中循环做一些事情.</p>
<h3 data-id="heading-1">RunLoop的应用范畴有哪些?</h3>
<p>定时器(Timer)、PerformSelector</p>
<p>GCD Async Main Queue</p>
<p>事件响应、手势识别、界面刷新</p>
<p>网络请求</p>
<p>AutoreieasePool</p>
<p>上面这些底层都是RunLoop在支撑,说白了,如果没有RunLoop支撑,上面的这些都无法实现.</p>
<p>如果没有RunLoop会发生什么呢?像我们的命令行项目,创建出来默认就是没有RunLoop,请看下图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69fcee5870e54d9abec998624b80d43d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>因为没有RunLoop,程序执行到第13行的时候,就会自动退出.</p>
<p>而我们iOS项目的main函数里面都有UIApplicationMain(argc, argv,<strong>nil</strong>, appDelegateClassName);这个代码,这里就是创建了一个主线程的RunLoop,所以我们程序不会退出,一直在运行中.我们可以大致写一下main函数里面的伪代码如下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f87813b1c8394fde9dc300cb44abb353~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>retVal这个等于0,当没有事件处理的时候,RunLoop就会sleep就是类似睡觉,一旦有事件需要处理,比如点击、刷新事件等process_message就会去处理这个事件,处理完了继续休息,retVal=0,程序就会一直执行,不会退出,这就是RunLoop作用.</p>
<h3 data-id="heading-2">RunLoop的基本作用</h3>
<p>1.保持程序的持续运行</p>
<p>2.处理App中的各种事件(比如触摸事件、定时器事件等)</p>
<p>3.节省了CPU资源,提高程序性能:该做事时做事,该休息时休息</p>
<p>...</p>
<h3 data-id="heading-3">获取RunLoop对象</h3>
<p>iOS中有2套API来访问和使用RunLoop :</p>
<p>Foundation : NSRunLoop (OC语言里面的)</p>
<p>Core Foundation : CFRunLoopRef (C语言里面的)</p>
<p>NSRunLoop和CFRunLoopRef都代表着RunLoop对象</p>
<p>NSRunLoop是基于CFRunLoopRef的一层OC包装</p>
<p>CFRunLoopRef是开源的.(<a href="https://opensource.apple.com/tarballs/CF/" target="_blank" rel="nofollow noopener noreferrer">CFRunLoopRef参考链接</a>)</p>
<p>其实我们很多都是由OC包装出来的,请看下面:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db42b9fc424f4892ae23b4370bbe12e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>获取当前的RunLoop</p>
<p>获取当前RunLoop和主线程RunLoop</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39cbd4a0078548f48ddd01bf99085531~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>获取RunLoop</p>
<p>这里注意,地址不一样,因为NSRunLoop是对CFRunLoopDef做了一层包装,你可以用OC的NSLog("%@",[NSRunLoop MainRunLoop])获取对比一下,它的地址就是C语言获取的地址.主线程只有一个RunLoop.</p>
<h3 data-id="heading-4">RunLoop与线程</h3>
<p>每条线程都有唯一的一个与之对应的RunLoop对象(一一对应)</p>
<p>RunLoop保存在一个全局的Dictionary里,线程作为key,RunLoop作为value</p>
<p>线程刚创建的时候并没有RunLoop对象,RunLoop会在第一次获取它时创建</p>
<p>RunLoop会在线程结束时销毁</p>
<p>主线程的RunLoop已经自动创建,子线程默认没有开启RunLoop.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b49aebb132564ec7afcddc8d74ed5274~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>源码窥探看一下:CFRunLoopGetCurrent</p>
<p>由于源码不能像objc直接打开,我们把它拉到项目中查看.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08dc6aeae7de45c683a7cbcfbc356abd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dd544d8f47840e4aa7c449935d96e9f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>从字典也能看出来是一对一的关系.而且确实是第一次获取的时候是空的,然后再去创建这个RunLoop.</p>
<p>那我们就继续来了解RunLoop内部的数据结构,到底是怎么工作的.</p>
<h3 data-id="heading-5">RunLoop相关的类</h3>
<p>Core Foundation中关于RunLoop的5个类</p>
<p>1.CFRunLoopRef</p>
<p>2.CFRunLoopModeRef</p>
<p>3.CFRunLoopSourceRef</p>
<p>4.CFRunLoopTimerRef</p>
<p>5.CFRunLoopObserverRef</p>
<p>再看下CFRunLoopRef的底层源码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82b250bb4dc8489f85069c7bdfa07fa1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>就是上面这个结构体,我们用到的可能就是红色这些.pthread是线程,每个runloop都会保存这个东西.最后面那个_modes,这个是个集合来着,CFMutableSetRef我们能想到我们自己用的set也是一个集合来着,比如NSMutableSet也是一个集合,所以这个_modes里面是存着一堆的mode.</p>
<p>这个mode就是CFRunLoopModeRef类型,所以里面存储一堆的CFRunLoopModeRef类型的mode.</p>
<p>而_currentMode也是CFRunLoopModeRef这个类型,所以我们很容易得出一个结论:</p>
<p><strong>一个RunLoop对象里面有一堆的mode,也就是存在_modes里面,里面只有一个是_currentMode.</strong></p>
<p>我们再窥探一下源码,看下mode里面存储的是什么?</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9cde900e040464981b8ab40408c6133~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>所以我们来个总结的图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe14395775c04d6abb303c1ca4e0bae8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>RunLoop有很多种模式,对应的_currentMode只有一种.</p>
<h3 data-id="heading-6">CFRunLoopModeRef</h3>
<p>1.CFRunLoopModeRef它是代表RunLoop的运行模式</p>
<p>2.一个RunLoop包含若干个Mode,每个Mode又包含若干个Source0/Source1/Timer/Observer</p>
<p>3.RunLoop启动时只能选择其中一个Mode,作为currentMode</p>
<p>4.如果需要切换Mode,只能退出当前RunLoop,再重新选择一个Mode进入</p>
<p>5.不同组的Source0/Source1/Timer/Observer能分割开来,互不影响</p>
<p>6.如果Mode里面没有任何Source0/Source1/Timer/Observer,RunLoop会立马退出</p>
<p>如果只能在一种模式下运行,对性能什么的都有很大好处,比如我在滑动模式下,不考虑不滑动的模式,所以就不会卡顿,顺畅很多.还有注意的就是,它切换mode是在循环里面切换的,所以不会导致程序退出.</p>
<p>常见的mode有2种,其他情况很少见,所以掌握这两个一般都是没问题了</p>
<p>1.KCFRunLoopDefaultMode (NSDefaultRunLoopMode):App的默认Mode,通常是主线程是在这个Mode下运行</p>
<p>2.UITrackingRunLoopMode : 界面跟踪Mode,用于ScrollView追踪触摸滑动,保证界面滑动时不受其他Mode影响</p>
<h3 data-id="heading-7">RunLoop到底做哪些事?</h3>
<p>RunLoop在不停执行的时候到底具体做了哪些事?其实是RunLoop在不停循环的时候,就是处理每个mode下的Source0、Source1、Timer、Observer这里面的事件,那我们就来看看这里面具体对应的到底是什么事件.</p>
<p><strong>Source0</strong></p>
<p>触摸事件、performSelector:onThread:</p>
<p>比如我们的touchbegin这个我们看下下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13bc09ca421418e8471466c73058021~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p><strong>Source1</strong></p>
<p>基于Port的线程间的通信,系统事件的捕捉.</p>
<p>(两个线程之间相互传递消息的处理,系统事件捕捉,其实也包括触摸事件,只是把事件捕捉到以后传递给Source0).</p>
<p><strong>Timer</strong></p>
<p>NSTimer定时器,performSelector:withObject:afterDelay(这个方法的底层实现也就是NSTimer来实现的)</p>
<p><strong>Observers</strong></p>
<p>用于监听RunLoop的状态,UI的刷新(BeforeWaiting),Autorelease pool(BeforeWaiting)</p>
<p>(在RunLoop休眠之前都会去执行UI的刷新啊、Autorelease pool的释放等)</p>
<p>以上这些东西,完全就是我们平时开发中经常写的代码,比如设置背景色,设置frame等等.</p>
<p>由于RunLoop知识点比较多,如果写太多不利于大家的阅读和消化,所以其他内容放在后面介绍!</p>
<h2 data-id="heading-8">接下来我会继续介绍Runloop其他知识点.</h2>
<h1 data-id="heading-9">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            