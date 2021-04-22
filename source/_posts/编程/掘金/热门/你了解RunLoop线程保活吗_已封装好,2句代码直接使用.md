
---
title: '你了解RunLoop线程保活吗_已封装好,2句代码直接使用'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92fe6931a67d471a85b4899ac86f842d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 06:58:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92fe6931a67d471a85b4899ac86f842d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>如果你没有了解RunLoop的一些基础,建议你看看这2篇博客,对线程保活本质理解有很大帮助</p>
<p><a href="https://juejin.cn/post/6948676084879589389" target="_blank">中高级iOS必备知识点之 RunLoop(一)</a></p>
<p><a href="https://juejin.cn/post/6950502345637625864" target="_blank">源码解读RunLoop,理解以后面试必加分</a></p>
<h3 data-id="heading-0">(温馨提示:这里是一步一步探究,步骤过程比较多,如嫌弃啰嗦,可直接拿后面封装的代码直,2句即可完美使用.)</h3>
<p>我们面试中经常遇到很多面试官,问我们关于RunLoop的知识点,可能我们大多数人了解RunLoop,但在项目中,我们真正用到RunLoop还是比较少的,RunLoop其实应用场景还是比较多,比如我们的定时器、线程保活、性能优化、监控应用卡顿.这个博客主要介绍的是'线程保活'</p>
<p>现在的网络请求基本都是用的AFNetworking这个框架,相信大家对它很了解,而它里面就是用RunLoop来控制子线程的生命周期.它会让子线程一直存在内存中不释放,这种好处就是对于我们经常去子线程做事情的话,我们就不必一直去创建-销毁-创建-销毁,这样能很大的提高性能,好处也是多多.</p>
<p>接下来我们来看看怎么能做到控制一个线程的生命周期(也就是线程保活),想让它活多久就多久,想让它什么时候销毁就什么时候销毁.</p>
<p>还是老样子,由简单到复杂,我们创建一个线程,这个用NSThread为例子(也可以用PThread,Operation,GCD都可以)</p>
<p>为了能看到线程是什么时候销毁的,我们可以定一个MyThread,继承NSThread,</p>
<p><strong>@interface</strong> MyThread : NSThread</p>
<p>并在.m文件,主要监测线程啥时候销毁.</p>
<p>-(<strong>void</strong>)dealloc&#123;</p>
<p>NSLog(@"%s",<strong>__func__</strong>);</p>
<p>&#125;</p>
<p>这样我们就能很清楚的看到MyThread啥时候销毁:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92fe6931a67d471a85b4899ac86f842d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>很清楚,上面的代码执行完NSThread就挂了.所以我们在开发中如果有需要经常在子线程干事情,是不是就是希望这个线程能一直不销毁,这样就避免了一直创建-销毁-创建-销毁.</p>
<p>那我们怎么处理?直接在子线程加一个runloop,因为我们知道在获取runloop的时候,就会创建runloop</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e559803dd1846e5b311b4b417331b8f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>还是没能成功,如果你有细看我之前的2篇博客,你会注意到有一点:</p>
<p>如果Mode里面没有任何Source0/Source1/Timer/Observer,RunLoop会立马退出</p>
<p>所以我们只要在runloop里面加上任何一个就能保证线程不退出,那我们立刻试试:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a62d0487a6d845c68f2c84535e2be058~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>因为是子线程,我们只用NSDefaultRunLoopMode就行了,不用考虑另一个模式</p>
<p>我们再想想,run方法只是达到了线程保活的功能,真正要执行的应该还是在这个线程上去执行另外的操作.所以我完整的写一个线程保活的例子,如下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/303728cb97db404fac7c59d612df1153~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>上面就是一个简单的线程保活的例子,其实这个是存在一些弊端的,那我们继续探究一下.</p>
<h2 data-id="heading-1">'线程保活'存在的问题再探究</h2>
<p>为了代码简洁易懂,我换一个block创建,跟上面的效果是一模一样,便于理解,我先是创建2个控制器的跳转,因为我想看看,控制器销毁的时候,线程会不会也跟着销毁.请看下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47332cc70683464b98e4f46203a8b908~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>看控制台很明显,此时并没有达到我们想要的结果,虽然线程确实一直存在,能一直帮我做事情(控制台可以一直输出test),但是我们发现控制器销毁了,而控制器上的线程却没有跟着销毁!我们看不到控制台有输出.那是怎么回事呢?难道出现循环引用?很明显不是!</p>
<p>难道是<strong>self</strong>.Mythread没有清空?你把<strong>self</strong>.MyThread = <strong>nil</strong>;写在VC的dealloc里面,你会发现,线程依然不会销毁!</p>
<p>原因是线程一直没有执行完,它一直卡在[[NSRunLoop currentRunLoop] run]这段代码,所以NSLog(@"---- end ----")也一直没有执行,线程都没有结束,所以它不会销毁.所以如果你想要一个全局的线程,任何页面都可以调用,永远不用销毁的话,那这个线程就能达到这个效果.现在我们想要的效果肯定是在当前页面存在,这个VC销毁的时候,线程也会销毁,我们想控制这个线程的生命周期,想让它销毁它就销毁.那我们继续看看怎么处理.</p>
<p>我们知道线程执行结束,线程就会销毁,只要执行NSLog(@"---- end ----"),就能让线程销毁,所以我们明显的思路就是在VC的dealloc里面停止<strong>self</strong>.MyThread线程的RunLoop.请看下面的代码.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a56fc6bbb1a540f4951b63a72ae83a4b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>线程依旧没有销毁.</p>
<p>有可能有的人会认为,这很有可能是执行dealloc说明VC快销毁了,你在快销毁的VC中执行stop方法,是不是来不及呢?那这样,我用按钮执行stop事件.请看下图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/953e8894a0054fd1b9cc95f39696a68a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>此时发现,线程依旧没有销毁(log中没有输出线程的dealloc).</p>
<h2 data-id="heading-2">[[NSRunLoop currentRunLoop] run]无限循环;</h2>
<p>其实是这个[[NSRunLoop currentRunLoop] run];这个原因导致的,我们先看官方的解释,对于这个方法.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5946993eff154749ac2c519ff3e2dda4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>看这个上面红色的翻译大致意思是:这个方法是无限循环的执行runMode:beforeDate,它是很有效的处理一个无限循环的.大概类似</p>
<p>white(1)</p>
<p>&#123;runMode:beforeDate&#125;</p>
<p>所以我们大概知道,这个方法是无限循环也就是关不了,可以理解为死循环.而我们执行的CFRunLoopStop(CFRunLoopGetCurrent()),其实只是停止它无限循环中的一次runMode:beforeDate,因为它会不断创建,所以无法全部停止,所以我们很自然想到用runMode:beforeDate这个方法来尝试解决.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/363ed855f6444439ae80e172989a9e89~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>看控制台的输出,我们确实是完成了想用它就用它,不用它就让它销毁的操作,也完成了控制器销毁时候,线程也会销毁.(Stop是一个BOOL值,[NSDate distantFuture]是一个很大的值.)</p>
<p>但是上面的还是不够完美,我们看看同样的代码,假如我们其他操作会不会出现什么问题,比如我们很可能不会点击停止,直接点返回,此时我们也想销毁线程,所以我们想着在VC的dealloc里面调用stop方法试试,请看下面:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20e6ee8bd2714ac181709fe59a171e17~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>看上面的操作,此时应该控制器销毁,而线程依旧还是没有销毁</p>
<h2 data-id="heading-3">为什么点击调用stop就可以使线程销毁,而在dealloc里面调用stop就不能使线程销毁?</h2>
<p>我们当前这个写法先看一个注意点:waitUntilDone这个传值如果传NO有时候可能导致崩溃,原因如下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3adafecaf8b74b47b99eda6cc615b48a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>有可能出现的情况</p>
<p>所以上面的参数我改成YES.</p>
<p>而线程不销毁的原因是这样:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86368c1e0de94a939fa0beaf62c0a3f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>再执行到这边的时候,while()里面的条件还是一直是YES,导致还是会一直重复执行里面代码,所以runloop还是会一直运行.所以我们把条件改一下即可: <strong>while</strong>(!weakSelf.Stop&& weakSelf) 把条件改成这个即可(如果这里用**__strong**处理可能产生循环引用).</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58266cc6ba1f4525a2973ee0195bed67~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>看运行结果,这种操作完美解决!</p>
<p>我们再验证一下之前点击停止的那种模式有没有影响!你会发现又崩了!如下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0621d46886b4147b6a39a5bb24297b7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>原因很简单:点击停止已经调用了stop,RunLoop已经结束了,它已经不能做事情了,只是没有销毁.你返回的时候dealloc又调用了stop,又让它去工作,肯定会出问题的.所以我们只要加一个判断即可:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/360fa783748f4ecda2f51a4d7f1d056c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这下真的完美解决了,如论怎么操作,线程和控制器都会销毁!我们看一下成果:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d16e420eeccd4c26a82ae896cb4f224f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>结果完美展示</p>
<p>这里我们发现很多步骤才出来结果,而且是感觉还有点麻烦,那我们直接封装即可:</p>
<h2 data-id="heading-4">线程的封装:</h2>
<p>封装用起来就非常容易了.先看执行调用代码,再看封装</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4992ea1ec5c4183a79a60468d158e95~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>封装以后就剩这3句,初始化,调用做事,停止,代码很少,很好用,请看效果:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8280e5ded54c178a6b9255e55169e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>完美解决了这个问题.请看下面封装代码:(就是把我们之前写的,封装起来了):</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01384e8207ab4199a1f1bc884c0aa052~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>到这里,我们基本把要说的都说了,该封装的已经封装了,有需要可以直接拿去调用!</p>
<p>因为理论上控制器销毁了,线程也会跟着销毁,所以控制的dealloc里面应该是不用调用stop,按照这个思路我们直接在GDThread的dealloc里面调用stop方法即可,那封装的线程将变得更简单,只有2步操作即可.,<strong>初始化,调用做事!</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87001b8405204089b9b30bade29fd450~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p><strong>2句代码完成保活!</strong></p>
<h2 data-id="heading-5">拓展--C语言的封装</h2>
<p>有上面的封装其实已经可以,用C语言的封装作为了解一下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40827af0f88b41069ce6da8f3a477fbd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>只要换了红色圈圈的内容即可,其他的都和原来一样,这里也是可以直接使用.</p>
<h3 data-id="heading-6">接下来我会继续努力编写其他博客,您的支持就是我最大的动力!</h3>
<h1 data-id="heading-7">如果觉得我写得对您有所帮助，请点赞关注我，我会持续更新😄</h1>
<h1 data-id="heading-8">感谢支持🙏🙏🙏!</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            