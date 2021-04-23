
---
title: '源码解读RunLoop,理解以后面试必加分'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d7611e834924d09bd213697407ed05a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 20:59:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d7611e834924d09bd213697407ed05a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>继上一篇博客</p>
<p><a href="https://juejin.cn/post/6948676084879589389" target="_blank">中高级iOS必备知识点之RunLoop(一)</a></p>
<h2 data-id="heading-0">RunLoop的状态</h2>
<p>首先我们去RunLoop的源码去查看它有几种状态,如下图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d7611e834924d09bd213697407ed05a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它一共有上面的这几种个状态</p>
<p>/* Run Loop Observer Activities */</p>
<p><strong>typedef</strong> CF_OPTIONS(CFOptionFlags, CFRunLoopActivity) &#123;</p>
<p>kCFRunLoopEntry = (1UL << 0), //即将进入loop</p>
<p>kCFRunLoopBeforeTimers = (1UL << 1), //即将处理timer</p>
<p>kCFRunLoopBeforeSources = (1UL << 2), //即将处理source</p>
<p>kCFRunLoopBeforeWaiting = (1UL << 5), //即将进入休眠</p>
<p>kCFRunLoopAfterWaiting = (1UL << 6), //刚从休眠中唤醒</p>
<p>kCFRunLoopExit = (1UL << 7), //即将退出loop</p>
<p>kCFRunLoopAllActivities = 0x0FFFFFFFU //所有模式</p>
<p>&#125;;</p>
<p>现在我们来试一试,怎么去监听RunLoop的状态,是这样,RunLoop的监听模式没有OC的代码,我们可以用C语言代码来实现,如下:<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4c326a7229b487f92345e360304f162~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从执行的结果来看,确实是这么多,点击事件是在source0执行,所以看log日志也是很清楚,</p>
<p>接下来我们看一下定时器唤醒RunLoop.我们知道kCFRunLoopBeforeWaiting是休眠睡觉,而kCFRunLoopAfterWaiting是唤醒休眠,我们看一下定时器是不是唤醒休眠,请看下面的代码:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9628742043fa46889406675859abf53c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从输出结果来看,确实是唤醒休眠.执行block</p>
<h3 data-id="heading-1">证明模式切换会退出RunLoop,再重新进入RunLoop</h3>
<p>由上面的监听,我们是很容易可以证明这个结果吧?我们看一下代码,这次用上面说的另一种创建observe的方法,请看下图:随便创建一个可以滚动的view,比如我创建的Scrollerview.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f17a68004ad48d7a8fdeaa89bf8be22~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当在滚动的时候,我们明显可以看到2种模式在切换,而且RunLoop也是需要退出重新进入才会切换到新的模式.</p>
<h2 data-id="heading-2">深入理解RunLoop的执行流程</h2>
<p>网上的答案很多,这次我们从源码解析,一步一步的查看RunLoop的执行流程到底是怎么样的:因为源码比较抽象,是纯c语言的,不像我们之前的有c++源码比较好懂一点,那我们怎么找runloop开始的函数呢?很容易,我们知道点击也是通过runloop来处理的,那我们直接看点击事件的函数调用栈就知道入口了,请看下图:<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b7f76b48cbe471ab25a2d5bf4b43163~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的代码可以很清楚的看出来是调用了CFRunLoopRunSpecific这个函数.那我们就去源码搜索这段代码很容易就搜索到.请看下面:<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7154c03e4fe44578a5a6a50445cf9153~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一看上面的源码,我们发现执行了非常多,你看绿色里面有锁,有多线程等等,所以我们没有必要研究得很透彻,浪费时间也没有意义,我们只要把大致流程捋顺了就行了,所以我们只要看关键代码,我只展示我们要看的关键代码如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f7a00183462462f83645688a2844ca7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们就去看__CFRunLoopRun源码里面到底执行了哪些操作,接下来的源码是我精简了的,大家可以参照源码看一下,因为里面东西非常多,我们没有必要全部了解,只要知道它的执行流程即可.请看下图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c04c30c928694f0cb270360d8bef67ec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果条件不成立,就会设置返回值,到时候直接退出RunLoop,上面的流程相信我备注的已经非常清楚,对照一下源码看一下,你会印象更加深刻.下面我们用文字总结一下流程如下:<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00b054c4796e4667a84b58e2f59ef0a4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再放一个文字版的:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b910a19bd34c72976032f542020350~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个和源码基本一模一样的流程,可以参照一下,源码还是比较抽象的</p>
<p>接下来再看一个知识点.</p>
<h3 data-id="heading-3">__CFRunLoopDoBlocks、__CFRunLoopDoObservers、__CFRunLoopDoTimers里面执行了什么</h3>
<p>其中RunLoop做了这么几件大事中比如blocks,timers,observers,我们看下里面具体是执行了什么,继续看源码,请看下图,比如我们就看__CFRunLoopDoSources0:<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0444dccd070d4ba093e2fadde6bf4503~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实最终处理的就是这个:</p>
<p>__CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__</p>
<p>我们再看下之前的一个截图<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a302994150d24e6fa7a23f027c843041~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它上面两个处理的函数是一摸一样,也进一步的证明了,触摸事件是source0在处理.</p>
<p>定时器也是一样的道理,大家可以自己尝试一下.</p>
<h3 data-id="heading-4">理解线程休眠具体是什么意思?</h3>
<p>RunLoop的线程休眠是真的休眠,它是不会占用任何cpu的资源,完全休息.它和white(1)这种还是有本质的区别,white(1)它是一直在执行,转成汇编会有几条指令,一直在执行,一直占用cpu资源,比如我们想做优化,那RunLoop的这种休眠模式是不是更节约cpu资源,说白了更省电些.就是如下源码的位置:<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec84ca540114486bb474e9a1fc3adf26~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是执行到当前代码,就不会往下走了,不会接着执行下面的代码,就会堵在这里,一旦别人唤醒它了,它才会接着往下执行.我们可能奇怪它是怎么做到的这种休眠?</p>
<p>我们看一下里面具体是怎么实现的,其实里面是执行了非常内核的函数叫做:mach_msg,我们可以看下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33ee94dd49434dee963536fc58e96cae~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实IPA可以分为内核层面的IPA:它是非常非常底层的,是操作系统层面的,它可以让线程休眠,也是真的休眠,不占用任何cpu资源,一般是不开放给我们程序员使用的,因为是比较内核的,给程序员使用危险也比较大,而应用层面的IPA,都是网络请求什么,页面什么.</p>
<p>所以mach_msg,我们面试的时候可以答出这个函数.</p>
<h3 data-id="heading-5">RunLoop休眠实现的原理</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b55651c0d043486dbb9280388662091a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是用户态和内核态的切换,用户态发消息,内核态休眠,再被唤醒,用户态处理消息.</p>
<p>所以如果面试官问:RunLoop里面线程阻塞是怎么样的?我们千万不能答,里面是个死循环.就是上面刚刚说的那些.</p>
<h3 data-id="heading-6">RunLoop与NSTimer的故事</h3>
<p>相信我们在开发中遇到的次数是非常的多,这里稍微提一下.</p>
<p>比如我们常见的mode模式是有2种</p>
<p>1.KCFRunLoopDefaultMode (NSDefaultRunLoopMode):App的默认Mode,通常是主线程是在这个Mode下运行</p>
<p>2.UITrackingRunLoopMode : 界面跟踪Mode,用于ScrollView追踪触摸滑动,保证界面滑动时不受其他Mode影响</p>
<p>我们在把Timer添加到runloop的时候,直接传入通用模式即可NSRunLoopCommonModes即可.</p>
<p>主要说一下它是怎么个原因.</p>
<p>我们看一下上个博客说的RunLoop的结构:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0c0d86e7f84586916653a389dde9b6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以理解为传入NSRunLoopCommonModes,就是把这2种模式,放入_commonModes里面,也就是timer可以_commonModes数组中的模式下进行工作.注意NSRunLoopCommonModes这个不是一种模式哈.</p>
<p>而_commonModeItems里面存放的都是可以在_commonModes模式下工作的,比如刚刚的timer.</p>
<p></p>
<h2 data-id="heading-7">接下来我会继续介绍'线程保活'知识点.</h2>
<h1 data-id="heading-8">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1></div>  
</div>
            