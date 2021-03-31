
---
title: '彻底搞懂Category的load相关的底层'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93d0fc91128f4aa48fa7508abb431cfc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 15 Mar 2021 21:45:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93d0fc91128f4aa48fa7508abb431cfc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天我们就围绕一个面试题来从源码的角度分析答案！</p>
<h4 data-id="heading-0">一、Category中有load方法吗？load方法是什么时候调用的？load方法能继承吗？如果分类又存在继承是如何加载load顺序的呢？</h4>
<p>首先我们先看下下面的代码，我们先看代码运行结果，再从源码上分析！</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93d0fc91128f4aa48fa7508abb431cfc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>GDPerson.m文件里面+(<strong>void</strong>)load&#123; NSLog(@"GDPerson+load"); &#125; GDPerson+Test1.m文件里面+(<strong>void</strong>)load&#123; NSLog(@"GDPerson+Test1+load");&#125;GDPerson+Test2.m文件里面+(<strong>void</strong>)load&#123; NSLog(@"GDPerson+Test2+load");&#125;</p>
<p>1.GDPerson+Test1和GDPerson+Test2是GDPerson分类;</p>
<p>2.GDStudent+Test1和GDStudent+Test2是GDStudent分类;</p>
<p>3.GDStudent继承于GDPerson</p>
<p>从上面的结果我们可以看出，分类是在加载分类的时候调用load方法，没有任何操作，是主动调用。</p>
<h2 data-id="heading-1">二、GDPerson和GDPerson+Test1和GDStudent+Test2调用顺序和编译顺序有关吗？</h2>
<p>请看下面的截图：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b2209c041d24604bc3e8a48b874a368~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们无论怎么调整编译顺序，GDPerson的load方法总是先输出，剩下2个分类是按照分类的顺序加载load方法。</p>
<p>然后我们在GDPerson和它的分类里面都加一个+（void）test方法，按照上面的顺序，我们知道肯定优先执行GDStudent+Test2的test，我想具体原因就不说了，我之前的博客都有好好介绍这些问题</p>
<h4 data-id="heading-2">思考</h4>
<p>从之前我们知识体，我们知道类方法都是存在元类对象中的，我们也知道+（void）test肯定也是存在元类对象中的，那么GDPerson类和分类的三个+（void）test肯定是在元类对象，那么+（load）是什么样的呢？这里我们可以看一下元类对象里面到底存了哪些方法，还记得我之前的一篇博客吗？有一个方法可以获取对象中的方法(<a href="https://www.jianshu.com/p/05a0a4095ba7" target="_blank" rel="nofollow noopener noreferrer">探索KVO的本质(二)</a>）,可以这里面查看。</p>
<p>我再贴一遍方法：</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cba551ecefe7466d90e1f5b56c747099~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6467da923af4ba38142377308148b95~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从这里可以看出，load方法是合并在元类对象里面的，这也跟我们之前的博客说的知道点是吻合的</p>
<h3 data-id="heading-3">窥探源码来论证我们上面说的结论</h3>
<p>源码地址，我之前几个博客都有说，这里就不说了，直接打开objc4最新源码查看：</p>
<p>我先把查看源码顺序贴上，再和大家一起看一下。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecef21597aab486caa471aff90450b5c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>objc-os.mm就是程序的入口，_objc_init初始化；load_image，image是代表镜像，load_image正好是我们要的load的方法，接下来我就一步一步的带着看一下</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27ed4330c6eb4f7b84a798e9f91f73c1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02068a9b052a43f282cd31d245b73cb4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里很清楚的解决了我们的疑问，类的load方法先调用，分类的load方法后调用。继续看call_class_loads具体是怎么调用的</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0891ab56fc4f4dbb65f11bb539bc78~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里我们清楚了，这个不像我们之前说的，是通过直接找的内存地址直接调用，而不是我们之前的先通过isa找到类对象，再通过类对象的isa找到元类...等等，所以是运行时就会直接调用load方法。</p>
<p>接下来分类的方法也是同样的道理，大家可以自己看一下，这里就不说了。相信大家心中都有答案。</p>
<p>接下来我们看一个更复杂的情况</p>
<h2 data-id="heading-4">如果出现继承会是怎么样的呢？</h2>
<p>下面我把GDStudent是继承GDPerson,然后GDStudent+test1和GDStudent+test2是GDStudent分类</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb44c81167b4b63af4ba90e260f20c5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>无论怎么修改编译顺序，父类的load方法都是优先调用，再调用本类，再根据编译顺序，调用其他分类，这个大家可以自己去验证验证，接下来我们用源码分析看看到底是不是这样。</p>
<h2 data-id="heading-5">出现继承的源码分析调用顺序</h2>
<p>先看类再看分类，我们还是先看call_class_loads方法的实现</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63634e73be2648839df1a6596beb9b96~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以接下来我们就去研究classes的顺序，在调用之前有个prepare_load_methods方法，那很有可能就是在这里面准备了classes的顺序，我们进去看一下有个schedule_class_load，schedule是规划的意思，就是规划我们的类加载，那就接着看（过程比较多，也比较简单，我标记的比较清楚，很容易尝试），请看下面的图</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/429295c027844e6b9dfa4e8feefa1b77~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的图可以看出数组的顺序是父类在前面，而且是schedule_class_load是递归调用会调用所有父类，所以是优先加载。也是优先调用，把我们在看一下add_class_to_loadable_list(cls)的具体实现吧</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/057cdea56c664db0ba787837b5513d55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>说了这么多，我们终于可以总结了😄</p>
<h2 data-id="heading-6">总结：</h2>
<p>+load方法会在runtime加载类、分类时调用</p>
<p>每个类、分类只会在程序运行过程中调用一次</p>
<p>调用顺序：</p>
<p>1.首先会调用类的load方法；</p>
<p>2.调用子类的load方法之前会优先调用父类的load方法；</p>
<p>3.按照编译的顺序（先编译，先调用）</p>
<p>4.再调用分类的load方法，按照先编译，先调用</p>
<p>接下来我们解答面试题</p>
<p>load方法的继承比较简单，我就不说了，它也是消息机制发送，通过isa，所以它会优先调用分类的load，这个大家自己尝试！</p>
<h2 data-id="heading-7">一、Category中有load方法吗？load方法是什么时候调用的？load方法能继承吗？</h2>
<p>有load方法（这个问法就很奇怪）</p>
<p>load方法是在runtime加载类、分类的时候调用</p>
<p>load方法可以继承，但是一般情况下不会主动调用load方法，都是让系统自动调用</p>
<h3 data-id="heading-8">接下来博客我会介绍iOS类别(Category关于initialize的底层知识)的其他底层知识.</h3>
<h1 data-id="heading-9">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1>
<p>===</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            